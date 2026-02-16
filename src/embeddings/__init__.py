"""Embedding module for document encoding and vector storage."""

from src.embeddings.encoder import DocumentEncoder
from src.embeddings.vector_store import FAISSVectorStore

__all__ = ["DocumentEncoder", "FAISSVectorStore"]
