"""Tests for the text chunker."""

from src.retrieval.chunker import ChunkerConfig, TextChunker


def test_basic_chunking():
    chunker = TextChunker(ChunkerConfig(chunk_size=10, chunk_overlap=2, min_chunk_size=3))
    text = " ".join([f"word{i}" for i in range(25)])
    chunks = chunker.chunk(text)
    assert len(chunks) > 1
    assert all("text" in c for c in chunks)


def test_empty_text():
    chunker = TextChunker()
    assert chunker.chunk("") == []
    assert chunker.chunk("   ") == []


def test_metadata_propagation():
    chunker = TextChunker(ChunkerConfig(chunk_size=10, chunk_overlap=0, min_chunk_size=3))
    chunks = chunker.chunk("hello world this is a test of chunking", metadata={"source": "test"})
    assert all(c["source"] == "test" for c in chunks)


def test_chunk_ids_sequential():
    chunker = TextChunker(ChunkerConfig(chunk_size=5, chunk_overlap=1, min_chunk_size=2))
    text = " ".join([f"w{i}" for i in range(20)])
    chunks = chunker.chunk(text)
    ids = [c["chunk_id"] for c in chunks]
    assert ids == list(range(len(chunks)))
