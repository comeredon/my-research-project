# 🎤 Presenter's Demo Guide

> Step-by-step walkthrough for presenting this project. Estimated total time: 30-45 minutes.

---

## Pre-Demo Checklist

- [ ] GitHub account with Copilot access
- [ ] Codespace created from this repo (click the badge in README)
- [ ] Codespace fully built (dependencies installed)
- [ ] Verify Copilot extension is active (check status bar)
- [ ] Open a terminal and run `pytest tests/ -v` to confirm tests pass

---

## Part 1: Setting the Stage (5 min)

### What to show:
1. **Open the repo in GitHub** — show the repo structure
2. **Click "Open in Codespaces"** — show instant dev environment
3. **Explain the research context**:
   - "We're building a retrieval-augmented generation system"
   - "Two papers: one on embedding retrieval, one on REFRAG"
   - "REFRAG modifies token probabilities during decoding instead of stuffing the prompt"

### Talking points:
- Codespaces gives every team member the same environment
- No "works on my machine" problems
- Pre-configured with Copilot, Python, Jupyter

---

## Part 2: Code Understanding with Copilot Chat (8 min)

### Steps:
1. Open `src/refrag/decoder.py`
2. Select the `generate()` method (lines ~120-170)
3. Open Copilot Chat (`Ctrl+Shift+I`)
4. Ask: **"Explain how this REFRAG decoding works"**
5. Ask: **"What are the performance implications of calling retrieval at every token step?"**
6. Ask: **"Suggest an optimization to cache retrieval results"**

### What to highlight:
- Copilot understands the research concepts
- It can suggest real optimizations
- It reads the docstrings and comments for context

---

## Part 3: Code Generation with Copilot (10 min)

### Steps:
1. Open `src/retrieval/pipeline.py`
2. Position cursor after the `query()` method
3. Type:
   ```python
   def query_with_reranking(self, question: str, top_k: int = 5, rerank_top_n: int = 20) -> list[dict]:
       """Query with a two-stage retrieve-then-rerank approach."""
   ```
4. Let Copilot complete the implementation
5. Show it generates a sensible reranking pipeline

### Alternative: Build a new module
1. Create `src/retrieval/hybrid.py`
2. Type a module docstring explaining hybrid retrieval (BM25 + dense)
3. Let Copilot scaffold the class

### What to highlight:
- Copilot understands the project structure
- It follows the patterns (dataclasses, type hints, logging)
- The `.github/copilot-instructions.md` guides its style

---

## Part 4: Workspace Agent Deep Dive (8 min)

### Steps:
1. In Copilot Chat, use `@workspace`:
   - **"@workspace Describe the data flow from document ingestion to query results"**
   - **"@workspace What would I need to change to support GPU-based FAISS indices?"**
   - **"@workspace Create a new endpoint that combines retrieval with REFRAG decoding"**

2. Show how it navigates across files:
   - `encoder.py` → `vector_store.py` → `pipeline.py` → `decoder.py`

### What to highlight:
- @workspace understands the entire codebase
- It can reason about cross-file dependencies
- It generates code that fits the existing architecture

---

## Part 5: Interactive Demo (5 min)

### Steps:
1. Run: `streamlit run src/demo/app.py`
2. Show the three tabs:
   - **Chunking**: Change chunk size, see how documents split
   - **Retrieval**: Type queries, see results
   - **REFRAG**: Adjust λ slider, see distribution blending
3. Explain: "This is the research concept made interactive"

### What to highlight:
- Built rapidly with Copilot assistance
- Running in Codespace with port forwarding
- Audience can follow along in their own Codespace

---

## Part 6: Testing & Quality (5 min)

### Steps:
1. Open `tests/test_chunker.py`
2. Ask Copilot: **"Generate edge case tests for the TextChunker"**
3. Accept suggestions and run: `pytest tests/ -v`
4. Show all tests passing

### What to highlight:
- Copilot generates meaningful tests, not just boilerplate
- Tests cover edge cases (empty input, single word, etc.)
- Quick feedback loop in Codespace

---

## Part 7: PR Workflow (5 min)

### Steps:
1. Stage changes: `git add .`
2. Ask Copilot to generate a commit message
3. Create a branch and push
4. Open a PR on GitHub
5. Show Copilot PR description suggestions
6. Show Copilot code review features

### What to highlight:
- Copilot helps at every stage of the workflow
- From writing code → testing → committing → reviewing

---

## Closing (2 min)

### Key takeaways:
1. **Copilot** accelerates research code development
2. **Copilot Chat** helps understand complex research papers and code
3. **@workspace agent** reasons across the entire project
4. **Copilot instructions** customize behavior per-project
5. **Codespaces** provide instant, reproducible environments
6. **The full workflow** — code, test, commit, review — all enhanced by AI

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Copilot not suggesting | Check extension is enabled; ensure file is saved |
| Import errors | Run `pip install -r requirements.txt` |
| Streamlit not loading | Check port 8501 is forwarded; try `streamlit run src/demo/app.py --server.port 8501` |
| Tests failing | Ensure you're in the project root; run `pytest tests/ -v --tb=short` |
| FAISS import error | Run `pip install faiss-cpu` |
