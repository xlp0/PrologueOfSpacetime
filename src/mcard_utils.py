import hashlib
import json
import logging
from typing import Dict, List, Optional
import math
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MCard:
    """
    Represents an MCard (Memory Card) - The Static Truth.
    Encapsulates content with a SHA-3/256 hash identity.
    """
    def __init__(self, content: str, card_type: str = "mcard"):
        self.content = content
        self.card_type = card_type
        self.hash_id = self._calculate_hash(content)

    @staticmethod
    def _calculate_hash(content: str) -> str:
        """Calculates the SHA-3/256 hash of the content."""
        return hashlib.sha3_256(content.encode('utf-8')).hexdigest()

    def to_dict(self) -> Dict[str, str]:
        """Returns a dictionary representation of the MCard."""
        return {
            "type": self.card_type,
            "hash": self.hash_id,
            "content": self.content
        }

    def save(self, directory: str) -> str:
        """Saves the MCard to a JSON file."""
        path = Path(directory) / f"{self.hash_id}.json"
        with open(path, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
        logger.info(f"Saved MCard to {path}")
        return str(path)

class AlignmentCalculator:
    """
    Calculates alignment between Specification, Implementation, and Expectation
    using vector similarity (mock implementation for phase 1).
    """
    @staticmethod
    def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
        """Calculates cosine similarity between two vectors."""
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        magnitude_a = math.sqrt(sum(a * a for a in vec_a))
        magnitude_b = math.sqrt(sum(b * b for b in vec_b))
        
        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0
        return dot_product / (magnitude_a * magnitude_b)

    @staticmethod
    def calculate_alignment(spec: str, impl: str, exp: str) -> float:
        """
        Mock alignment calculation. 
        In a real system, this would use embeddings (e.g., OpenAI, BERT).
        Here we use simple word overlap for demonstration.
        """
        def get_vector(text: str) -> List[float]:
            # Mock vector: simple character counts of key terms
            terms = ["system", "logic", "code", "test", "user"]
            text_lower = text.lower()
            return [float(text_lower.count(term)) for term in terms]

        v_spec = get_vector(spec)
        v_impl = get_vector(impl)
        v_exp = get_vector(exp)
        
        # Calculate pairwise similarities
        sim_spec_impl = AlignmentCalculator.cosine_similarity(v_spec, v_impl)
        sim_impl_exp = AlignmentCalculator.cosine_similarity(v_impl, v_exp)
        sim_spec_exp = AlignmentCalculator.cosine_similarity(v_spec, v_exp)
        
        # Average alignment score
        return (sim_spec_impl + sim_impl_exp + sim_spec_exp) / 3.0

def load_curriculum(file_path: str) -> str:
    """Loads the curriculum file."""
    with open(file_path, 'r') as f:
        return f.read()

def load_10k_docs(directory: str) -> List[str]:
    """Recursively loads all markdown files from the docs directory."""
    docs = []
    path = Path(directory)
    for p in path.rglob("*.md"):
        with open(p, 'r') as f:
            docs.append(f.read())
    logger.info(f"Loaded {len(docs)} documents from {directory}")
    return docs

if __name__ == "__main__":
    # Smoke Test
    m = MCard("The Prologue of Spacetime")
    print(f"MCard Hash: {m.hash_id}")
    
    score = AlignmentCalculator.calculate_alignment(
        "System logic", "System code logic", "User test logic"
    )
    print(f"Alignment Score: {score}")
