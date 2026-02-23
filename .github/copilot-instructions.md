# Microsoft Quantum Research Explorer — Copilot Instructions

## Project Context

This repository implements a **RAG-style semantic retrieval pipeline** over a corpus of Microsoft Quantum research papers. The goal is to let users explore and query quantum computing research using dense vector search. The local demo uses word-overlap search; production search is backed by **Azure AI Search**.

---

## Indexed Research Papers

The following four Microsoft Quantum papers are indexed in this project:

| Paper | Topic |
|---|---|
| *QDK/Chemistry: A Modular Toolkit for Quantum Chemistry Applications* | Quantum Chemistry — end-to-end pipeline from molecular structure → SCF → active space → QPE |
| *Interferometric Single-Shot Parity Measurement in InAs-Al Hybrid Devices* | Majorana / Topological Qubits — single-shot readout of fermion parity via quantum capacitance in InAs-Al heterostructures |
| *Roadmap to Fault-Tolerant Quantum Computation Using Topological Qubit Arrays* | Fault-Tolerant QC — tetron qubits, Floquet codes, lattice surgery, and scalable error correction |
| *Optimizing the Pairwise Measurement-Based Surface Code* | Quantum Error Correction — PyMatching v2 / sparse blossom MWPM over spacetime detector graphs |

---
## Key Research Domain Concepts

| Term | Definition |
|---|---|
| **Tetron qubit** | A Majorana-based logical qubit formed from two topological superconducting wires. Errors are suppressed exponentially by topological protection rather than active correction alone. |
| **Majorana zero modes (MZMs)** | Non-Abelian anyons localised at the ends of topological superconducting wires. Their non-local encoding of quantum information makes them intrinsically protected from local perturbations. |
| **Parity measurement** | Interferometric single-shot readout of the shared fermion parity of two MZMs, implemented via quantum capacitance shifts in InAs-Al gate-defined nanowire devices. |
| **QPE (Quantum Phase Estimation)** | Algorithm for extracting eigenvalues of a unitary; used as a fault-tolerant quantum CASCI solver in QDK/Chemistry. |
| **Floquet / Hastings-Haah codes** | Measurement-only error correcting codes tailored to the tetron architecture; period-3 measurement sequences realise a surface code without needing two-qubit gates. |
| **Surface code decoding** | Minimum-weight perfect matching (MWPM) on spacetime detector graphs; implemented with PyMatching v2 / sparse blossom. |
| **Active space** | The subset of molecular orbitals that capture essential electron correlation, selected to fit available qubit count. |
| **SCF (Self-Consistent Field)** | Hartree-Fock calculation that produces molecular orbitals as a classical starting point for quantum algorithms. |

---


## Architecture Overview

```
src/
├── embeddings/
│   ├── encoder.py        # DocumentEncoder — sentence-transformers, lazy model load
│   └── vector_store.py   # FAISSVectorStore — cosine similarity search
├── retrieval/
│   ├── chunker.py        # TextChunker — fixed-size chunks with overlap
│   └── pipeline.py       # RetrievalPipeline — orchestrates chunk → encode → index → search
├── refrag/
│   └── decoder.py        # Token-level distribution blending (legacy RAG decoder)
└── demo/
    ├── app.py            # Streamlit interactive demo (port 8501)
    └── sample_data.py    # Paper excerpts as SAMPLE_DOCUMENTS list of dicts
scripts/
└── run_retrieval_demo.py  # CLI demo
tests/
├── test_chunker.py
└── test_vector_store.py
```

---

## Python Module Conventions

When adding a new Python module to this repository, follow these patterns:

1. **Location**: Place the module in the appropriate `src/<subsystem>/` folder (e.g. `src/retrieval/`, `src/embeddings/`). Create a new subsystem folder only if the concern is genuinely new.
2. **Module docstring**: Start every file with a module-level docstring that states purpose, key class/function names, and any relevant paper reference.
3. **Configuration dataclass**: Expose tuneable parameters through a `@dataclass` named `<Module>Config` with typed fields and sensible defaults. Accept `config: <Module>Config | None = None` in `__init__` and default to `<Module>Config()`.
4. **Lazy loading**: Defer expensive imports (models, FAISS, etc.) to first use via a `@property`.
5. **Logging**: Use `logger = logging.getLogger(__name__)` — no `print()` statements.
6. **Type hints**: Use built-in generics (`list[dict]`, `X | None`) — Python 3.10+ union syntax.
7. **Docstrings + example**: Public classes and functions get a one-line summary, `Args:`/`Returns:` blocks, and a short `Example:` with `>>>` notation.
8. **`__init__.py`**: Export the primary public class from the subsystem's `__init__.py`.
9. **Tests**: Add a corresponding `tests/test_<module>.py` file.

### Example skeleton

```python
"""Short description of what this module does.

Key classes: MyProcessor
"""

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class MyProcessorConfig:
    param_a: int = 10
    param_b: float = 0.5


class MyProcessor:
    """One-line summary.

    Example:
        >>> proc = MyProcessor()
        >>> proc.run("input")
    """

    def __init__(self, config: MyProcessorConfig | None = None):
        self.config = config or MyProcessorConfig()
```
