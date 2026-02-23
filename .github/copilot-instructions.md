# GitHub Copilot Instructions for This Project

This is an AI research demo project focused on **semantic retrieval over Microsoft Quantum research papers**,
using **Azure AI Search** as the back-end search index.

## Project Context
- We implement retrieval-augmented generation (RAG) pipelines applied to a corpus of **Microsoft Quantum** research papers
- The search index (Azure AI Search) contains four papers:
  1. *QDK/Chemistry: A Modular Toolkit for Quantum Chemistry Applications* — end-to-end pipeline from molecular geometry through quantum phase estimation (QPE) on fault-tolerant hardware
  2. *Interferometric Single-Shot Parity Measurement in InAs-Al Hybrid Devices* — single-shot readout of Majorana zero mode fermion parity via quantum capacitance
  3. *Roadmap to Fault-Tolerant Quantum Computation Using Topological Qubit Arrays* — Majorana-based tetron qubit devices, Hastings-Haah Floquet codes, lattice surgery
  4. *Optimizing the Pairwise Measurement-Based Surface Code* — decoding graph construction, PyMatching v2, vacancy mitigation
- The embedding retrieval module uses sentence-transformers for dense vector search
- FAISS is used for local approximate nearest neighbor search; Azure AI Search handles hybrid BM25 + vector search in production
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
  embeddings/    → Document embedding and vector store (sentence-transformers + FAISS)
  retrieval/     → Retrieval pipeline (dense + hybrid)
  refrag/        → Legacy RAG decoding integration (token-level distribution blending)
  demo/          → Streamlit demo application (Microsoft Quantum Research Explorer)
```

## Key Research Domain Concepts
- **Tetron Qubits**: Majorana-based qubits formed from parallel topological nanowires; errors suppressed exponentially via topological gap and wire length ratios
- **Quantum Phase Estimation (QPE)**: Algorithm for extracting molecular ground-state energies on fault-tolerant quantum hardware; treated as a quantum CASCI solver in QDK/Chemistry
- **Active Space Selection**: Reducing the full molecular Hamiltonian to an orbital subspace tractable on near-term quantum hardware (CASCI, MCSCF, valence space methods)
- **Fermion Parity Measurement**: Interferometric readout of shared parity of two Majorana zero modes via quantum capacitance shift in InAs-Al heterostructures
- **Hastings-Haah Floquet Codes**: Quantum error-correction codes using only one- and two-body measurements, naturally suited to the tetron measurement-based architecture
- **Lattice Surgery**: Logical qubit operations by stitching/splitting code patches; used for two-logical-qubit gates in the tetron roadmap
- **Dense Retrieval**: Encode queries and documents into dense vectors, retrieve via cosine similarity
