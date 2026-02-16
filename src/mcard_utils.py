import hashlib
import json
import os
from typing import Dict, Any, Optional

class MCard:
    """
    Represents an M-Card (Memory Card) - The Static Truth.
    Encapsulates knowledge as a verifiable, hash-linked data structure.
    """
    def __init__(self, content: str, metadata: Dict[str, Any] = None):
        self.content = content
        self.metadata = metadata or {}
        self.hash = self._calculate_hash()

    def _calculate_hash(self) -> str:
        """Calculates the SHA-256 hash of the content."""
        return hashlib.sha256(self.content.encode('utf-8')).hexdigest()

    def to_json(self) -> str:
        """Returns the JSON representation of the MCard."""
        return json.dumps({
            "content": self.content,
            "metadata": self.metadata,
            "hash": self.hash
        }, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'MCard':
        """Creates an MCard instance from a JSON string."""
        data = json.loads(json_str)
        return cls(data["content"], data.get("metadata"))

    def verify(self) -> bool:
        """Verifies integrity by re-calculating the hash."""
        return self._calculate_hash() == self.hash

class Librarian:
    """
    The Librarian (DeepSeek) Agent Utility.
    Responsible for storing, retrieving, and validating MCards.
    """
    def __init__(self, storage_path: str = "./knowledge_base"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)

    def save_card(self, card: MCard, filename: Optional[str] = None) -> str:
        """Saves an MCard to disk. Returns the file path."""
        if not filename:
            filename = f"{card.hash}.json"
        
        file_path = os.path.join(self.storage_path, filename)
        with open(file_path, 'w') as f:
            f.write(card.to_json())
        return file_path

    def load_card(self, filename: str) -> Optional[MCard]:
        """Loads an MCard from disk."""
        file_path = os.path.join(self.storage_path, filename)
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r') as f:
            return MCard.from_json(f.read())

    def align_vectors(self, spec_card: MCard, impl_card: MCard, wit_card: MCard) -> float:
        """
        Placeholder for Cosine Similarity Calculation.
        In a real scenario, this would import numpy/sklearn to calculate
        the vector alignment between the Specification, Implementation, and Witness.
        Returns a score between 0.0 and 1.0.
        """
        # TODO: Implement actual vector embedding logic here.
        # For now, we return a mock high score if hashes are valid.
        if spec_card.verify() and impl_card.verify() and wit_card.verify():
            return 0.99
        return 0.0
