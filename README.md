# 🔬 AI Research Demo: Embedding Retrieval & REFRAG

> A hands-on demo project showcasing **Embedding-based Retrieval** and **REFRAG (Rethinking RAG-based Decoding)** — built to demonstrate GitHub Copilot, Copilot Agents, Skills, and Codespaces.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/comeredon/my-research-project)

---

## 📖 Overview

This project implements the core concepts from two research papers:

1. **Embedding-based Retrieval** — Encoding documents into dense vector representations for semantic search using sentence-transformers and FAISS.
2. **REFRAG** ([Lin et al., 2025](https://arxiv.org/abs/2509.01092)) — A novel approach to RAG that modifies token-level probability distributions during LLM decoding, rather than prepending retrieved documents to the prompt.

### Key Concepts

| Concept | Standard RAG | REFRAG |
|---|---|---|
| Retrieved docs | Prepended to prompt | Used during decoding |
| Integration level | Prompt-level | Token-level |
| Context window | Consumed by docs | Preserved for generation |
| Control | All-or-nothing | Fine-grained (λ weight) |

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
│   ├── refrag/             # REFRAG decoding
│   │   └── decoder.py      # Token-level distribution blending
│   └── demo/               # Streamlit demo app
│       ├── app.py          # Interactive web demo
│       └── sample_data.py  # Sample documents
├── scripts/
│   └── run_retrieval_demo.py  # CLI demo script
├── tests/
│   ├── test_chunker.py
│   └── test_vector_store.py
├── requirements.txt
└── README.md
```

---

## 🎯 Demo Guide: Showcasing GitHub Copilot Features

This project is designed as a **live demo** for presenting GitHub Copilot capabilities. Below is a structured walkthrough.

### Demo 1: GitHub Copilot Code Completion

**Goal**: Show how Copilot accelerates writing research code.

1. Open `src/embeddings/encoder.py`
2. Start typing a new method:
   ```python
   def encode_batch_with_progress(self, texts, desc="Encoding"):
   ```
3. Watch Copilot suggest the full implementation
4. Show how it understands the context (uses `self.model`, `self.config.batch_size`, etc.)

### Demo 2: GitHub Copilot Chat

**Goal**: Show Copilot Chat for code understanding and generation.

1. Select the `RefragDecoder.generate()` method in `src/refrag/decoder.py`
2. Ask Copilot Chat: *"Explain how this REFRAG decoding works step by step"*
3. Ask: *"Add error handling for when the retrieval pipeline returns no results"*
4. Ask: *"Write a unit test for this method"*

### Demo 3: GitHub Copilot Agents (Workspace Agent)

**Goal**: Show `@workspace` agent for project-wide understanding.

1. In Copilot Chat, type: `@workspace How does the retrieval pipeline connect to the REFRAG decoder?`
2. Show how it understands cross-file dependencies
3. Ask: `@workspace What changes would I need to support GPU acceleration?`
4. Ask: `@workspace Generate a diagram of the data flow in this project`

### Demo 4: GitHub Copilot Custom Skills / Instructions

**Goal**: Show how `.github/copilot-instructions.md` guides Copilot.

1. Open `.github/copilot-instructions.md` and explain its purpose
2. Show that Copilot suggestions follow the project conventions (type hints, dataclasses, logging)
3. Create a new file and show Copilot following the documented architecture

### Demo 5: GitHub Codespaces

**Goal**: Show the full cloud development experience.

1. Show `.devcontainer/devcontainer.json` configuration
2. Highlight: pre-installed extensions (Copilot, Python, Jupyter)
3. Highlight: automatic dependency installation (`postCreateCommand`)
4. Highlight: port forwarding for Streamlit (port 8501)
5. Run the Streamlit demo and show it works immediately

### Demo 6: Copilot for Testing

**Goal**: Show Copilot generating tests.

1. Open `tests/test_chunker.py`
2. Ask Copilot to generate additional edge case tests
3. Run tests: `pytest tests/ -v`
4. Show Copilot fixing any failing tests

### Demo 7: Copilot Workflow (Code Review & PR)

**Goal**: Show Copilot in the PR workflow.

1. Create a branch: `git checkout -b feature/hybrid-retrieval`
2. Use Copilot to implement a hybrid retrieval method (BM25 + dense)
3. Commit and push
4. Create a PR — show Copilot PR description generation
5. Show Copilot code review suggestions

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🔧 Development

### Adding New Retrieval Methods

1. Create a new file in `src/retrieval/`
2. Implement the retrieval interface (see `pipeline.py` for the pattern)
3. Add tests in `tests/`
4. Use Copilot to help with implementation!

### Extending the REFRAG Decoder

The decoder in `src/refrag/decoder.py` can be extended with:
- Different interpolation strategies (learned λ, attention-based weighting)
- Caching of retrieval results across decoding steps
- Beam search with REFRAG blending

---

## 📚 References

- **REFRAG**: Lin, X., Ghosh, A., Low, B.K.H., Shrivastava, A., & Mohan, V. (2025). *REFRAG: Rethinking RAG based Decoding*. [arXiv:2509.01092](https://arxiv.org/abs/2509.01092)
- **Sentence-Transformers**: Reimers, N. & Gurevych, I. (2019). *Sentence-BERT*. [arXiv:1908.10084](https://arxiv.org/abs/1908.10084)
- **FAISS**: Johnson, J., Douze, M., & Jégou, H. (2019). *Billion-scale similarity search with GPUs*. [arXiv:1702.08734](https://arxiv.org/abs/1702.08734)

---

## 📝 License

MIT License — See [LICENSE](LICENSE) for details.
