"""Tests for the FAISS vector store."""

import numpy as np

from src.embeddings.vector_store import FAISSVectorStore


def test_add_and_search():
    dim = 64
    store = FAISSVectorStore(dimension=dim)

    # Create random embeddings
    embeddings = np.random.randn(10, dim).astype(np.float32)
    # Normalize for cosine similarity
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    docs = [{"id": i, "text": f"doc {i}"} for i in range(10)]
    store.add(embeddings, docs)

    # Search with the first embedding (should find itself)
    results = store.search(embeddings[0], k=3)
    assert len(results) == 3
    assert results[0]["document"]["id"] == 0
    assert results[0]["rank"] == 1


def test_empty_store_search():
    store = FAISSVectorStore(dimension=32)
    query = np.random.randn(32).astype(np.float32)
    results = store.search(query, k=5)
    assert results == []


def test_mismatched_lengths():
    store = FAISSVectorStore(dimension=32)
    embeddings = np.random.randn(5, 32).astype(np.float32)
    docs = [{"id": i} for i in range(3)]  # Wrong length
    try:
        store.add(embeddings, docs)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
