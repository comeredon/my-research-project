# GitHub Copilot Instructions for This Project

This is an AI research demo project focused on **Embedding-based Retrieval** and **REFRAG (Rethinking RAG-based Decoding)**.

## Project Context
- We implement retrieval-augmented generation (RAG) pipelines
- The embedding retrieval module uses sentence-transformers for dense vector search
- The REFRAG module modifies the LLM decoding process by integrating retrieval signals at the token level
- We use FAISS for approximate nearest neighbor search
- The demo is designed to run in GitHub Codespaces

## Coding Conventions
- Use Python 3.11+ with type hints
- Follow PEP 8 style guidelines
- Use dataclasses for configuration objects
- Keep modules small and focused
- Document public functions with docstrings
- Use `logging` module instead of print statements

## Architecture
```
src/
  embeddings/    → Document embedding and vector store
  retrieval/     → Retrieval pipeline (dense + hybrid)
  refrag/        → REFRAG decoding integration
  demo/          → Streamlit demo application
```

## Key Research Concepts
- **Dense Retrieval**: Encode queries and documents into dense vectors, retrieve via cosine similarity
- **REFRAG Decoding**: Instead of prepending retrieved documents to the prompt, REFRAG modifies token-level probabilities during decoding by interpolating the LLM distribution with a retrieval-based distribution
- **Chunking Strategies**: Documents are split into overlapping chunks for better retrieval granularity
