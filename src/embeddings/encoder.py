"""Document encoder using sentence-transformers for dense embeddings.

This module implements the embedding component of a retrieval pipeline.
Documents and queries are encoded into dense vectors that can be compared
via cosine similarity for efficient retrieval.

Reference: Embedding-based retrieval research paper (attached).
"""

import logging
from dataclasses import dataclass, field

import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class EncoderConfig:
    """Configuration for the document encoder."""

    model_name: str = "all-MiniLM-L6-v2"
    max_seq_length: int = 256
    batch_size: int = 32
    normalize_embeddings: bool = True
    device: str = "cpu"


class DocumentEncoder:
    """Encodes documents and queries into dense vector representations.

    Uses sentence-transformers to produce embeddings suitable for
    semantic similarity search.

    Example:
        >>> encoder = DocumentEncoder()
        >>> embeddings = encoder.encode(["Hello world", "AI research"])
        >>> print(embeddings.shape)  # (2, 384)
    """

    def __init__(self, config: EncoderConfig | None = None):
        self.config = config or EncoderConfig()
        self._model = None

    @property
    def model(self):
        """Lazy-load the sentence-transformer model."""
        if self._model is None:
            from sentence_transformers import SentenceTransformer

            logger.info("Loading model: %s", self.config.model_name)
            self._model = SentenceTransformer(
                self.config.model_name, device=self.config.device
            )
            self._model.max_seq_length = self.config.max_seq_length
        return self._model

    @property
    def embedding_dimension(self) -> int:
        """Return the dimensionality of the embeddings."""
        return self.model.get_sentence_embedding_dimension()

    def encode(self, texts: list[str]) -> np.ndarray:
        """Encode a list of texts into dense vectors.

        Args:
            texts: List of text strings to encode.

        Returns:
            numpy array of shape (len(texts), embedding_dim).
        """
        logger.info("Encoding %d texts", len(texts))
        embeddings = self.model.encode(
            texts,
            batch_size=self.config.batch_size,
            normalize_embeddings=self.config.normalize_embeddings,
            show_progress_bar=True,
        )
        return np.array(embeddings, dtype=np.float32)

    def encode_query(self, query: str) -> np.ndarray:
        """Encode a single query string."""
        return self.encode([query])[0]
