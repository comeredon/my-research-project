# ⚛️ Microsoft Quantum Research Explorer

> A semantic-retrieval demo over **Microsoft Quantum** research papers — built to
> demonstrate GitHub Copilot, Copilot Agents, Azure AI Search, and Codespaces.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/comeredon/my-research-project)

---

## 📖 Overview

This project implements a RAG-style retrieval pipeline that lets you explore a
corpus of **Microsoft Quantum** research papers using dense vector search.  The
back-end search index is powered by **Azure AI Search**, and the local demo runs
word-overlap search so it works anywhere without GPU or cloud credentials.

### Indexed Research Papers

| Paper | Topic | Organisation |
|---|---|---|
| *QDK/Chemistry: A Modular Toolkit for Quantum Chemistry Applications* | Quantum Chemistry | Microsoft Quantum |
| *Interferometric Single-Shot Parity Measurement in InAs-Al Hybrid Devices* | Majorana / Topological Qubits | Microsoft Azure Quantum |
| *Roadmap to Fault-Tolerant Quantum Computation Using Topological Qubit Arrays* | Fault-Tolerant QC / Tetrons | Microsoft Quantum |
| *Optimizing the Pairwise Measurement-Based Surface Code* | Quantum Error Correction | Microsoft Quantum |

### Key Research Topics

| Topic | Description |
|---|---|
| **Tetron Qubits** | Majorana-based qubits formed from two topological wires; errors suppressed exponentially by topological protection |
| **QDK/Chemistry** | End-to-end pipeline from molecular structure → SCF → active space → QPE on fault-tolerant hardware |
| **Parity Measurement** | Interferometric single-shot readout of Majorana fermion parity via quantum capacitance shifts in InAs-Al devices |
| **Floquet Codes** | Hastings-Haah codes tailored to measurement-based tetron architecture; basis for lattice surgery |
| **Surface Code Decoding** | PyMatching v2 / sparse blossom minimum-weight perfect matching over spacetime detector graphs |

---

## 🚀 Quick Start (Codespace)

1. **Click the badge above** to open in a Codespace (or create one manually)
2. Wait for the container to build and dependencies to install
3. Run the interactive demo:
   ```bash
   streamlit run src/demo/app.py
   ```
4. Or run the CLI retrieval demo:
   ```bash
   python scripts/run_retrieval_demo.py
   ```

---

## 📁 Project Structure

```
my-research-project/
├── .devcontainer/          # Codespace configuration
│   └── devcontainer.json
├── .github/
│   └── copilot-instructions.md  # Copilot context for this project
├── src/
│   ├── embeddings/         # Document encoding & vector store
│   │   ├── encoder.py      # Sentence-transformer encoder
│   │   └── vector_store.py # FAISS-backed similarity search
│   ├── retrieval/          # Retrieval pipeline
│   │   ├── chunker.py      # Text chunking with overlap
│   │   └── pipeline.py     # End-to-end retrieval orchestration
│   ├── refrag/             # RAG decoding module (legacy)
│   │   └── decoder.py      # Token-level distribution blending
│   └── demo/               # Streamlit demo app
│       ├── app.py          # Interactive web demo
│       └── sample_data.py  # Quantum research paper excerpts
├── scripts/
│   └── run_retrieval_demo.py  # CLI demo script
├── tests/
│   ├── test_chunker.py
│   └── test_vector_store.py
├── requirements.txt
└── README.md
```

---

## 🎯 Demo Guide: Showcasing GitHub Copilot + Azure AI Search

This project is designed as a **live demo** for presenting GitHub Copilot capabilities
with a real Azure AI Search back-end over Microsoft Quantum research papers.

### Demo 1: GitHub Copilot Code Completion

**Goal**: Show how Copilot accelerates writing research retrieval code.

1. Open `src/embeddings/encoder.py`
2. Start typing a new method:
   ```python
   def encode_batch_with_progress(self, texts, desc="Encoding"):
   ```
3. Watch Copilot suggest the full implementation using the existing context

### Demo 2: GitHub Copilot Chat — Research Paper Q&A

**Goal**: Show Copilot Chat for understanding quantum computing concepts in code.

1. Select the `RetrievalPipeline.query()` method in `src/retrieval/pipeline.py`
2. Ask Copilot Chat: *"How would I extend this to connect to Azure AI Search instead of FAISS?"*
3. Ask: *"What query would I write to find information about Majorana zero modes?"*
4. Ask: *"Write a unit test for this method using the quantum research sample data"*

### Demo 3: GitHub Copilot Agents

**Goal**: Show `@workspace` agent for project-wide understanding.

1. In Copilot Chat, type: `@workspace How does the retrieval pipeline process a query about tetron qubits?`
2. Show how it understands cross-file dependencies
3. Ask: `@workspace What changes would I need to add Azure AI Search as a retrieval backend?`

### Demo 4: Copilot Custom Instructions

**Goal**: Show how `.github/copilot-instructions.md` guides Copilot for this domain.

1. Open `.github/copilot-instructions.md` and explain its purpose
2. Show that Copilot suggestions follow conventions (type hints, dataclasses, logging)

### Demo 5: GitHub Codespaces

**Goal**: Show the full cloud development experience.

1. Show `.devcontainer/devcontainer.json` configuration
2. Highlight: pre-installed extensions, automatic dependency install, port forwarding for Streamlit (8501)
3. Run the Streamlit demo and show it works immediately

### Demo 6: Copilot for Testing

1. Open `tests/test_chunker.py`
2. Ask Copilot to generate edge case tests for quantum paper excerpts
3. Run: `pytest tests/ -v`

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 📚 References

- **QDK/Chemistry**: Microsoft Quantum (2025). *QDK/Chemistry: A Modular Toolkit for Quantum Chemistry Applications.*
- **Interferometric Parity**: Microsoft Azure Quantum (2023). *Interferometric Single-Shot Parity Measurement in InAs-Al Hybrid Devices.*
- **Topological Roadmap**: Microsoft Quantum (2025). *Roadmap to Fault-Tolerant Quantum Computation Using Topological Qubit Arrays.*
- **Surface Code Optimization**: Microsoft Quantum (2024). *Optimizing the Pairwise Measurement-Based Surface Code.*
- **Sentence-Transformers**: Reimers, N. & Gurevych, I. (2019). *Sentence-BERT*. [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- **FAISS**: Johnson, J., Douze, M., & Jégou, H. (2019). *Billion-scale similarity search with GPUs*. [arXiv:1702.08734](https://arxiv.org/abs/1702.08734)

---

## 📝 License

MIT License — See [LICENSE](LICENSE) for details.
