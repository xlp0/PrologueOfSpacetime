# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "chromadb",
#     "google-genai",
#     "pymupdf",
#     "python-docx",
# ]
# ///
import argparse
import os
import sys
from pathlib import Path
import chromadb
from google import genai
import fitz  # PyMuPDF
import docx

# Configuration
DOCUMENTS_DIR = Path(os.path.expanduser("~/.openclaw/documents"))
VECTOR_DB_DIR = Path(os.path.expanduser("~/.openclaw/vector_db"))
MODEL_NAME = "text-embedding-004"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Configure Gemini
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Warning: GEMINI_API_KEY environment variable not set. Gemini API calls will fail unless configured elsewhere.")

client_genai = genai.Client(api_key=api_key)

# Ensure directories exist
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)

# Initialize ChromaDB client
client = chromadb.PersistentClient(path=str(VECTOR_DB_DIR))
collection = client.get_or_create_collection(
    name="document_corpus", 
    metadata={"hnsw:space": "cosine"}
)

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Splits text into overlapping chunks."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def extract_text_from_file(file_path):
    """Extracts raw text from widely used document formats."""
    text = ""
    ext = file_path.suffix.lower()
    
    try:
        if ext in ['.md', '.txt']:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        elif ext == '.pdf':
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text()
        elif ext == '.docx':
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        
    return text

def index_documents():
    """Scans the documents directory and indexes any new files."""
    print(f"Scanning {DOCUMENTS_DIR} for documents...")
    
    files = []
    for ext in ['**/*.md', '**/*.txt', '**/*.pdf', '**/*.docx']:
        files.extend(DOCUMENTS_DIR.glob(ext))
        
    for file_path in files:
        doc_id = str(file_path.relative_to(DOCUMENTS_DIR))
        
        # Check if already indexed
        existing = collection.get(ids=[doc_id + "_0"])
        if existing and existing['ids']:
            continue
            
        print(f"Processing: {doc_id}")
        text = extract_text_from_file(file_path)
        if not text.strip():
            continue
            
        chunks = chunk_text(text)
        if not chunks:
            continue
            
        # Generate Embeddings using Gemini
        try:
            response = client_genai.models.embed_content(
                model=MODEL_NAME,
                contents=chunks,
                config={"task_type": "RETRIEVAL_DOCUMENT"}
            )
            embeddings = response.embeddings
        except Exception as e:
            print(f"Error generating embeddings for {doc_id}: {e}")
            continue
        
        ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
        metadatas = [{"source": doc_id, "chunk_index": i} for i in range(len(chunks))]
        
        # Add to Chroma
        collection.add(
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )
    print("Indexing complete.")

def search_documents(query, top_k=5):
    """Searches the vector database for the most relevant chunks."""
    if collection.count() == 0:
        return "The document database is empty."
        
    try:
        response = client_genai.models.embed_content(
            model=MODEL_NAME,
            contents=query,
            config={"task_type": "RETRIEVAL_QUERY"}
        )
        query_embedding = [response.embeddings[0]]
    except Exception as e:
        return f"Error generating query embedding: {e}"
    
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )
    
    if not results['documents'][0]:
        return "No relevant documents found."
        
    output = []
    for i, doc in enumerate(results['documents'][0]):
        source = results['metadatas'][0][i]['source']
        distance = results['distances'][0][i]  # Cosine distance
        output.append(f"--- Document: {source} (Score: {1-distance:.4f}) ---\n{doc}\n")
        
    return "\n".join(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenClaw Document Indexer & Search (Gemini Powered)")
    parser.add_argument("--index", action="store_true", help="Index new documents in the corpus.")
    parser.add_argument("--query", type=str, help="Search the document corpus with a query.")
    args = parser.parse_args()
    
    if args.index:
        index_documents()
    elif args.query:
        print(search_documents(args.query))
    else:
        parser.print_help()
