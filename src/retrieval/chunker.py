"""Text chunking utilities for document preprocessing.

Splits documents into overlapping chunks for better retrieval granularity.
Overlapping ensures that information at chunk boundaries is not lost.
"""

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ChunkerConfig:
    """Configuration for text chunking."""

    chunk_size: int = 512
    chunk_overlap: int = 64
    min_chunk_size: int = 50


class TextChunker:
    """Splits text into overlapping chunks.

    Example:
        >>> chunker = TextChunker()
        >>> chunks = chunker.chunk("A long document text...")
    """

    def __init__(self, config: ChunkerConfig | None = None):
        self.config = config or ChunkerConfig()

    def chunk(self, text: str, metadata: dict | None = None) -> list[dict]:
        """Split text into overlapping chunks with metadata.

        Args:
            text: The text to split.
            metadata: Optional metadata to attach to each chunk.

        Returns:
            List of chunk dicts with 'text', 'chunk_id', and metadata.
        """
        if not text.strip():
            return []

        words = text.split()
        chunks = []
        start = 0

        while start < len(words):
            end = start + self.config.chunk_size
            chunk_words = words[start:end]

            if len(chunk_words) < self.config.min_chunk_size and chunks:
                # Merge small trailing chunk with the previous one
                break

            chunk_text = " ".join(chunk_words)
            chunk_doc = {
                "text": chunk_text,
                "chunk_id": len(chunks),
                "start_word": start,
                "end_word": min(end, len(words)),
                **(metadata or {}),
            }
            chunks.append(chunk_doc)
            start = end - self.config.chunk_overlap

        logger.info("Created %d chunks from %d words", len(chunks), len(words))
        return chunks
