"""End-to-end retrieval pipeline combining encoding, indexing, and search.

Orchestrates the document encoder, chunker, and vector store to provide
a simple interface for indexing and querying documents.
"""

import logging
from dataclasses import dataclass

from src.embeddings.encoder import DocumentEncoder, EncoderConfig
from src.embeddings.vector_store import FAISSVectorStore, VectorStoreConfig
from src.retrieval.chunker import ChunkerConfig, TextChunker

logger = logging.getLogger(__name__)


@dataclass
class PipelineConfig:
    """Configuration for the full retrieval pipeline."""

    encoder: EncoderConfig | None = None
    vector_store: VectorStoreConfig | None = None
    chunker: ChunkerConfig | None = None
    top_k: int = 5


class RetrievalPipeline:
    """Full retrieval pipeline: chunk → encode → index → search.

    Example:
        >>> pipeline = RetrievalPipeline()
        >>> pipeline.index_documents([{"text": "...", "title": "doc1"}])
        >>> results = pipeline.query("What is RAG?")
    """

    def __init__(self, config: PipelineConfig | None = None):
        self.config = config or PipelineConfig()
        self.encoder = DocumentEncoder(self.config.encoder)
        self.chunker = TextChunker(self.config.chunker)
        self._store: FAISSVectorStore | None = None

    @property
    def store(self) -> FAISSVectorStore:
        """Lazy-init the vector store after we know the embedding dimension."""
        if self._store is None:
            dim = self.encoder.embedding_dimension
            self._store = FAISSVectorStore(dim, self.config.vector_store)
        return self._store

    def index_documents(self, documents: list[dict]) -> int:
        """Chunk and index a list of documents.

        Args:
            documents: List of dicts with at least a 'text' key.

        Returns:
            Total number of chunks indexed.
        """
        all_chunks = []
        for doc in documents:
            meta = {k: v for k, v in doc.items() if k != "text"}
            chunks = self.chunker.chunk(doc["text"], metadata=meta)
            all_chunks.extend(chunks)

        if not all_chunks:
            return 0

        texts = [c["text"] for c in all_chunks]
        embeddings = self.encoder.encode(texts)
        self.store.add(embeddings, all_chunks)

        logger.info("Indexed %d chunks from %d documents", len(all_chunks), len(documents))
        return len(all_chunks)

    def query(self, question: str, top_k: int | None = None) -> list[dict]:
        """Query the index and return relevant chunks.

        Args:
            question: Natural language query.
            top_k: Number of results (defaults to config value).

        Returns:
            List of result dicts with 'document', 'score', 'rank'.
        """
        k = top_k or self.config.top_k
        query_vec = self.encoder.encode_query(question)
        results = self.store.search(query_vec, k=k)
        return results
