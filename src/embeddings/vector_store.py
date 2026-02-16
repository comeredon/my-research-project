"""FAISS-based vector store for efficient similarity search.

Provides approximate nearest neighbor search over document embeddings
using Facebook AI Similarity Search (FAISS).
"""

import logging
from dataclasses import dataclass
from pathlib import Path

import faiss
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class VectorStoreConfig:
    """Configuration for the FAISS vector store."""

    index_type: str = "flat"  # 'flat' for exact, 'ivf' for approximate
    nlist: int = 100  # Number of clusters for IVF index
    nprobe: int = 10  # Number of clusters to search


class FAISSVectorStore:
    """Vector store backed by FAISS for similarity search.

    Supports both exact (Flat) and approximate (IVF) nearest neighbor search.

    Example:
        >>> store = FAISSVectorStore(dimension=384)
        >>> store.add(embeddings, documents)
        >>> results = store.search(query_vector, k=5)
    """

    def __init__(self, dimension: int, config: VectorStoreConfig | None = None):
        self.dimension = dimension
        self.config = config or VectorStoreConfig()
        self.documents: list[dict] = []
        self.index = self._create_index()

    def _create_index(self) -> faiss.Index:
        """Create the FAISS index based on configuration."""
        if self.config.index_type == "ivf":
            quantizer = faiss.IndexFlatIP(self.dimension)
            index = faiss.IndexIVFFlat(
                quantizer, self.dimension, self.config.nlist, faiss.METRIC_INNER_PRODUCT
            )
            return index
        # Default: exact inner product search
        return faiss.IndexFlatIP(self.dimension)

    def add(self, embeddings: np.ndarray, documents: list[dict]) -> None:
        """Add document embeddings to the index.

        Args:
            embeddings: Array of shape (n, dimension).
            documents: List of document metadata dicts.
        """
        if len(embeddings) != len(documents):
            raise ValueError("Embeddings and documents must have the same length")

        # Train IVF index if needed
        if self.config.index_type == "ivf" and not self.index.is_trained:
            logger.info("Training IVF index with %d vectors", len(embeddings))
            self.index.train(embeddings)

        self.index.add(embeddings)
        self.documents.extend(documents)
        logger.info("Added %d documents (total: %d)", len(documents), len(self.documents))

    def search(self, query_vector: np.ndarray, k: int = 5) -> list[dict]:
        """Search for the k most similar documents.

        Args:
            query_vector: Query embedding of shape (dimension,).
            k: Number of results to return.

        Returns:
            List of dicts with 'document', 'score', and 'rank' keys.
        """
        if self.index.ntotal == 0:
            return []

        query = query_vector.reshape(1, -1)
        scores, indices = self.index.search(query, min(k, self.index.ntotal))

        results = []
        for rank, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx == -1:
                continue
            results.append(
                {
                    "document": self.documents[idx],
                    "score": float(score),
                    "rank": rank + 1,
                }
            )
        return results

    def save(self, path: str) -> None:
        """Save the index to disk."""
        faiss.write_index(self.index, path)
        logger.info("Index saved to %s", path)

    def load(self, path: str) -> None:
        """Load the index from disk."""
        self.index = faiss.read_index(path)
        logger.info("Index loaded from %s (%d vectors)", path, self.index.ntotal)
