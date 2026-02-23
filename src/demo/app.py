"""Streamlit demo application for the Microsoft Quantum Research Explorer.

Run with: streamlit run src/demo/app.py

This demo showcases semantic retrieval over a corpus of Microsoft Quantum
research papers indexed in Azure AI Search, covering:
  - QDK/Chemistry: quantum chemistry workflows on quantum hardware
  - Interferometric single-shot parity measurement (Majorana/InAs-Al devices)
  - Roadmap to fault-tolerant quantum computation using topological qubit arrays
  - Optimizing the pairwise measurement-based surface code
"""

import logging
import sys
import time

import streamlit as st

# Add project root to path
sys.path.insert(0, ".")

from src.demo.sample_data import MCP_DEMO_RESULTS, PAPER_METADATA, SAMPLE_DOCUMENTS
from src.retrieval.chunker import TextChunker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Microsoft Quantum Research Explorer",
    page_icon="⚛️",
    layout="wide",
)

st.title("⚛️ Microsoft Quantum Research Explorer")
st.markdown(
    """
    Semantic retrieval over **Microsoft Quantum** research papers using
    dense vector search — powered by **Azure AI Search**.
    Use the **🤖 Agentic AI Guide** tab to learn how to build custom
    instructions, skills, and agents that accelerate research workflows like this one.
    """
)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")
    chunk_size = st.slider("Chunk size (words)", 50, 500, 200, step=50)
    chunk_overlap = st.slider("Chunk overlap (words)", 0, 100, 30, step=10)
    top_k = st.slider("Top-K results", 1, 10, 3)

    st.divider()
    st.markdown(
        """
        ### 📚 Demo Sections
        1. **Document Chunking** — See how papers are split into retrieval chunks
        2. **Semantic Search** — Query the quantum research corpus
        3. **Research Papers** — Browse the indexed paper collection
        4. **Agentic AI Guide** — Build custom instructions, skills & agents
        5. **Agent + MCP Data** — Live agent reasoning loop over Azure AI Search
        """
    )

    st.divider()
    st.caption("Data source: Azure AI Search index over Microsoft Quantum PDFs")

# ── Tab Layout ───────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📄 Document Chunking", "🔍 Semantic Search", "📖 Research Papers", "🤖 Agentic AI Guide", "🔌 Agent + MCP Data"]
)

# ── Tab 1: Document Chunking ─────────────────────────────────────────────────
with tab1:
    st.header("Document Chunking")
    st.markdown(
        "Research papers are split into overlapping chunks before embedding. "
        "This preserves local context while keeping each chunk small enough "
        "for the embedding model. Adjust chunk size and overlap in the sidebar."
    )

    chunker = TextChunker()
    chunker.config.chunk_size = chunk_size
    chunker.config.chunk_overlap = chunk_overlap

    selected_doc = st.selectbox(
        "Select a document excerpt",
        range(len(SAMPLE_DOCUMENTS)),
        format_func=lambda i: SAMPLE_DOCUMENTS[i]["title"],
    )

    doc = SAMPLE_DOCUMENTS[selected_doc]

    col_meta1, col_meta2 = st.columns(2)
    with col_meta1:
        st.caption(f"**Source paper:** {doc['source']}")
    with col_meta2:
        paper_info = PAPER_METADATA.get(doc["source"], {})
        st.caption(f"**Topic:** {paper_info.get('topic', 'N/A')}")

    st.text_area("Document Excerpt", doc["text"], height=150, disabled=True)

    chunks = chunker.chunk(doc["text"], metadata={"title": doc["title"]})
    st.metric("Number of Chunks", len(chunks))

    for i, chunk in enumerate(chunks):
        with st.expander(f"Chunk {i + 1} (words {chunk['start_word']}-{chunk['end_word']})"):
            st.write(chunk["text"])

# ── Tab 2: Semantic Search ───────────────────────────────────────────────────
with tab2:
    st.header("Semantic Search over Quantum Research")
    st.markdown(
        "Type a question to find the most relevant excerpts from the "
        "Microsoft Quantum research paper corpus."
    )

    @st.cache_data
    def build_simple_index():
        """Return per-document text and titles for word-overlap retrieval."""
        all_texts = [doc["text"] for doc in SAMPLE_DOCUMENTS]
        all_titles = [doc["title"] for doc in SAMPLE_DOCUMENTS]
        all_sources = [doc["source"] for doc in SAMPLE_DOCUMENTS]
        return all_texts, all_titles, all_sources

    texts, titles, sources = build_simple_index()

    # Suggested queries relevant to the quantum research corpus
    st.markdown("**Example queries:**")
    example_queries = [
        "How does QPE extract molecular ground state energies?",
        "What is a tetron and how does it encode a qubit?",
        "How is fermion parity measured in InAs-Al devices?",
        "What error correction codes are used with topological qubits?",
        "How does active space selection work in QDK/Chemistry?",
        "What is lattice surgery in fault-tolerant quantum computing?",
    ]
    cols = st.columns(3)
    for i, eq in enumerate(example_queries):
        if cols[i % 3].button(eq, key=f"eq_{i}", use_container_width=True):
            st.session_state["query_input"] = eq

    query = st.text_input(
        "Enter your query",
        value=st.session_state.get("query_input", ""),
        placeholder="e.g., How do Majorana zero modes provide topological protection?",
        key="query_field",
    )
    # Sync back so button clicks populate the field on next render
    if query:
        st.session_state["query_input"] = query

    if query:
        with st.spinner("Searching..."):
            time.sleep(0.3)

            query_words = set(query.lower().split())
            scores = []
            for text in texts:
                doc_words = set(text.lower().split())
                overlap = len(query_words & doc_words)
                scores.append(overlap / max(len(query_words), 1))

            ranked = sorted(
                enumerate(scores), key=lambda x: x[1], reverse=True
            )[:top_k]

        st.subheader(f"Top {top_k} Results")
        for rank, (idx, score) in enumerate(ranked, 1):
            paper_info = PAPER_METADATA.get(sources[idx], {})
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"**#{rank}: {titles[idx]}**")
                    st.caption(
                        f"Paper: {paper_info.get('title', sources[idx])}  |  "
                        f"Topic: {paper_info.get('topic', 'N/A')}"
                    )
                    st.write(
                        texts[idx][:350] + "…"
                        if len(texts[idx]) > 350
                        else texts[idx]
                    )
                with col2:
                    st.metric("Score", f"{score:.2f}")
                st.divider()

        st.info(
            "💡 **Demo Note**: This uses word-overlap scoring for portability. "
            "The production pipeline connects to **Azure AI Search** for hybrid "
            "BM25 + dense vector retrieval. See `src/retrieval/pipeline.py` for "
            "the full implementation."
        )

# ── Tab 3: Research Papers ───────────────────────────────────────────────────
with tab3:
    st.header("Indexed Research Papers")
    st.markdown(
        "The following Microsoft Quantum papers are indexed in the Azure AI Search "
        "instance that backs this demo. Each paper is chunked and embedded for "
        "semantic retrieval."
    )

    for pdf_key, meta in PAPER_METADATA.items():
        with st.expander(f"📄 {meta['title']}"):
            col_a, col_b = st.columns([1, 2])
            with col_a:
                st.markdown(f"**Organization:** {meta['organization']}")
                st.markdown(f"**Topic:** {meta['topic']}")
                st.markdown(f"**File:** `{pdf_key}`")
            with col_b:
                st.markdown(f"**Abstract / Description:**")
                st.write(meta["description"])

            # Show how many demo document chunks come from this paper
            chunks_from_paper = [
                d for d in SAMPLE_DOCUMENTS if d["source"] == pdf_key
            ]
            st.caption(
                f"{len(chunks_from_paper)} excerpts from this paper are included "
                "in the local demo corpus."
            )

    st.divider()
    st.subheader("Corpus Statistics")
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    stat_col1.metric("Papers indexed", len(PAPER_METADATA))
    stat_col2.metric("Demo document excerpts", len(SAMPLE_DOCUMENTS))
    stat_col3.metric("Research organisation", "Microsoft Quantum")

# ── Tab 4: Agentic AI Guide ──────────────────────────────────────────────────
with tab4:
    st.header("🤖 Agentic AI for Research Acceleration")
    st.markdown(
        """
        This tab is a **hands-on reference** for building the three layers of
        Copilot customisation that turn a generic AI into a domain-aware research
        assistant. Use this as a live reference during the demo or as a workshop
        prompt card.
        """
    )

    st.info(
        "**How this project uses all three layers:** "
        "`.github/copilot-instructions.md` provides always-on quantum domain context → "
        "Skills encode repeatable research workflows → "
        "A custom Agent combines them with Azure AI Search as a tool."
    )

    st.divider()

    # ── Layer 1: Instructions ────────────────────────────────────────────────
    st.subheader("Layer 1 — Custom Instructions")
    st.markdown(
        """
        **File:** `.github/copilot-instructions.md` (or a `.instructions.md` in any folder)

        Instructions are *always-on context* — loaded into every Copilot chat session
        automatically. They tell the agent what your project is, what terminology matters,
        and how code should be structured.
        """
    )

    with st.expander("📋 What good instructions cover"):
        st.markdown(
            """
            | Section | Purpose |
            |---|---|
            | **Project context** | What problem is being solved, what data exists |
            | **Domain vocabulary** | Key terms with one-line definitions |
            | **Coding conventions** | Language version, style, patterns |
            | **Architecture overview** | Module map — helps the agent navigate files |
            | **Data sources** | Index names, file paths, API endpoints |
            """
        )

    with st.expander("📝 Minimal instructions template"):
        st.code(
            """\
# Copilot Instructions — [Your Project Name]

## Project Context
- This project does [goal] using [data/tools]
- The main data source is [describe it]

## Domain Vocabulary
- **[Term 1]**: [One-line definition]
- **[Term 2]**: [One-line definition]

## Coding Conventions
- Python 3.11+, type hints, PEP 8
- Use dataclasses for configuration
- Use `logging` instead of print statements

## Architecture
- `src/[module]/` — [purpose]
""",
            language="markdown",
        )

    with st.expander("💡 Try it — paste this into Copilot Chat"):
        st.markdown(
            """
            After creating your instructions file, verify it works:

            ```
            @workspace What research papers does this project cover?
            @workspace What is the core domain concept of [your term]?
            @workspace How should I structure a new Python module here?
            ```

            If Copilot answers using your definitions — instructions are working.
            """
        )

    st.divider()

    # ── Layer 2: Skills ──────────────────────────────────────────────────────
    st.subheader("Layer 2 — Custom Skills")
    st.markdown(
        """
        **Location:** `~/.copilot/skills/<skill-name>/SKILL.md` (user-level)
        or `.github/skills/<skill-name>/SKILL.md` (repo-level)

        A skill packages a **repeatable workflow** into a reusable file. When Copilot
        detects you are performing that type of task, it follows the skill's proven steps.
        Think of it as capturing your best expert's approach and making it available on demand.
        """
    )

    with st.expander("📋 Research skills worth building"):
        st.markdown(
            """
            | Skill | trigger phrase | What it does |
            |---|---|---|
            | `literature-review` | "review this paper" | Summarises + proposes corpus additions |
            | `query-formulation` | "help me search for" | Converts a question into search queries |
            | `hypothesis-to-code` | "implement this hypothesis" | Turns a research idea into testable code |
            | `paper-to-sample-data` | "add this paper to the corpus" | Extracts excerpts for `sample_data.py` |
            | `evaluation-design` | "design an evaluation" | Creates a retrieval benchmark |
            """
        )

    with st.expander("📝 Skill template (SKILL.md)"):
        st.code(
            """\
---
name: literature-review
description: >
  Step-by-step workflow for reviewing a new research paper and integrating
  it into the project corpus. Use when the user asks to summarise, compare,
  or add a new paper.
applyTo: "**/*.py, **/*.md"
---

# Literature Review Skill

## When to use this skill
When the user asks to review, summarise, or integrate a new paper.

## Workflow
1. Extract the paper's core claim and experimental method in 2-3 sentences
2. Identify which existing papers it most closely relates to, and why
3. List 3-5 new domain terms introduced — suggest additions to instructions.md
4. Draft a `SAMPLE_DOCUMENTS` entry (title, source, text) for sample_data.py
5. Suggest one retrieval query that would surface this paper from Azure AI Search
""",
            language="markdown",
        )

    with st.expander("💡 Try it — test your skill in Copilot Chat"):
        st.markdown(
            """
            ```
            Follow the literature-review skill for the tetron roadmap paper.

            Follow the query-formulation skill to help me find papers about
            Majorana zero mode lifetime measurements.
            ```

            Watch how Copilot structures its response to match the numbered workflow steps.
            """
        )

    st.divider()

    # ── Layer 3: Agents ──────────────────────────────────────────────────────
    st.subheader("Layer 3 — Custom Agents")
    st.markdown(
        """
        **Location:** `~/.copilot/agents/<agent-name>.agent.md` (user-level)

        A custom agent combines a **persona**, a **tool policy**, and an optional **skill set**
        into a named AI collaborator. Your researchers interact with the agent by name — it
        knows its role, what tools it can call, and what workflows it follows.
        """
    )

    with st.expander("📝 Agent template (.agent.md)"):
        st.code(
            """\
---
name: QuantumPaperAssistant
description: >
  Research assistant specialised in Microsoft Quantum literature retrieval.
  Always cites source papers. Uses Azure AI Search as primary tool.
tools:
  - azure-ai-search
  - file_search
  - semantic_search
skills:
  - literature-review
  - query-formulation
---

# Quantum Paper Assistant

You are a research assistant with deep expertise in topological quantum computing,
quantum chemistry workflows, and quantum error correction.

You have access to an Azure AI Search index containing four Microsoft Quantum papers.
Always cite the source paper and section when answering research questions.

## Primary workflows
1. Answer research questions by querying Azure AI Search first
2. When comparing papers, structure your answer around shared concepts (e.g. QPE usage, error correction approach)
3. When asked to extend the corpus, follow the `literature-review` skill
4. Never speculate about experimental results — only report what is in the indexed papers
""",
            language="markdown",
        )

    with st.expander("💡 Try it — test your agent"):
        st.markdown(
            """
            Switch the Copilot Chat mode selector to your custom agent, then ask:

            ```
            Compare how QPE is used in QDK/Chemistry versus the tetron roadmap paper.

            What hardware requirements does the interferometric parity measurement
            paper place on the InAs-Al device?

            I have a new paper on Floquet code thresholds. Add it to the corpus.
            ```

            The agent will call Azure AI Search, cite sources, and apply the relevant skill.
            """
        )

    st.divider()

    # ── The Three-Layer Stack ────────────────────────────────────────────────
    st.subheader("The Three-Layer Stack")
    st.markdown(
        """
        ```
        ┌─────────────────────────────────────────────────────┐
        │           Custom Agent  (.agent.md)                 │
        │   persona  ·  tool policy  ·  skill set             │
        ├─────────────────────────────────────────────────────┤
        │           Custom Skills  (SKILL.md)                 │
        │   repeatable domain workflows                       │
        ├─────────────────────────────────────────────────────┤
        │     Custom Instructions  (copilot-instructions.md)  │
        │   always-on domain context                          │
        └─────────────────────────────────────────────────────┘
        ```

        **Start here →** Instructions are the highest ROI, lowest effort first step.
        Add a skill every time you catch yourself explaining the same workflow to Copilot twice.
        Define an agent when your team needs a consistent, named AI collaborator.
        """
    )

    guide_col1, guide_col2, guide_col3 = st.columns(3)
    with guide_col1:
        st.success("**Step 1 — Instructions**\nEdit `.github/copilot-instructions.md` with your domain terms and project context. Test immediately.")
    with guide_col2:
        st.info("**Step 2 — Skills**\nCapture one recurring research workflow as a `SKILL.md`. Name it after the trigger phrase (e.g. `literature-review`).")
    with guide_col3:
        st.warning("**Step 3 — Agent**\nCombine instructions + skills + tools into a named `.agent.md`. Give it a role, a tool list, and 3–5 primary workflows.")

# ── Tab 5: Agent + MCP Data ──────────────────────────────────────────────────
with tab5:
    st.header("🔌 Agent + MCP Data: Why Agents Need Data Sources")
    st.markdown(
        """
        This tab shows the **complete agent reasoning loop** over real data from the
        **Azure AI Search MCP server** that backs this project.  
        Select a research question below to see every step: the tool call sent to the
        MCP server, the raw results returned, the agent's reasoning trace, and the
        final cited answer — compared side-by-side with what a generic agent (no MCP)
        would have said.
        """
    )

    st.info(
        "**What is an MCP server?**  "
        "The Model Context Protocol (MCP) is an open standard that lets agents call "
        "external tools and data sources. Here, the agent calls **Azure AI Search** "
        "as an MCP tool — it formulates a query, sends it, receives structured chunks "
        "from our four quantum papers, and reasons over them before answering."
    )

    st.divider()

    # ── Scenario Selector ───────────────────────────────────────────────────
    scenario_labels = [s["question"] for s in MCP_DEMO_RESULTS]
    selected_idx = st.selectbox(
        "Select a research question:",
        range(len(MCP_DEMO_RESULTS)),
        format_func=lambda i: scenario_labels[i],
    )
    scenario = MCP_DEMO_RESULTS[selected_idx]

    st.subheader(f"❓ {scenario['question']}")
    st.divider()

    # ── Step-by-step reasoning loop ─────────────────────────────────────────
    st.markdown("### Agent Reasoning Loop")

    loop_col1, loop_col2 = st.columns([1, 2])
    with loop_col1:
        st.markdown(
            """
            ```
            User Question
                  │
                  ▼
            Agent plans tool call
                  │
                  ▼
            ┌─────────────┐
            │  MCP Server │  ← Azure AI Search
            │  (tool call)│
            └─────────────┘
                  │
                  ▼
            Raw structured results
            (id, location, score, content)
                  │
                  ▼
            Agent reads + reasons
                  │
                  ▼
            Answer with citations
            ```
            """
        )
    with loop_col2:
        st.markdown("**Step 1 — Agent formulates the MCP tool call:**")
        st.code(
            f'tool: {scenario["mcp_tool"]}\nquery: "{scenario["mcp_query"]}"',
            language="yaml",
        )

        st.markdown("**Step 2 — MCP server returns structured results:**")
        for r in scenario["mcp_raw_results"]:
            with st.expander(
                f"📄 score {r['@search.score']:.4f} · {r['location'].split('/')[-1][:55]}…",
                expanded=False,
            ):
                st.markdown(f"**id:** `{r['id']}`")
                st.markdown(f"**source:** `{r['location']}`")
                st.markdown(f"**@search.score:** {r['@search.score']}")
                st.markdown("**content:**")
                st.write(r["content"])

        st.markdown("**Step 3 — Agent reasoning trace:**")
        for step in scenario["agent_reasoning_steps"]:
            st.markdown(f"- {step}")

    st.divider()

    # ── Side-by-side comparison ──────────────────────────────────────────────
    st.markdown("### Answer Quality: Without MCP vs With MCP")
    cmp_col1, cmp_col2 = st.columns(2)

    with cmp_col1:
        st.markdown("#### ❌ Agent WITHOUT MCP")
        st.markdown(
            "*Relies only on training data. No access to the indexed papers.*"
        )
        st.warning(scenario["answer_without_mcp"])
        st.caption(
            "Generic · No source citations · May miss domain-specific details · "
            "Cannot be updated when new papers are added"
        )

    with cmp_col2:
        st.markdown("#### ✅ Agent WITH Azure AI Search MCP")
        st.markdown(
            "*Queries the live index, retrieves grounded chunks, cites sources.*"
        )
        st.success(scenario["answer_with_mcp"])
        st.caption(
            "Grounded · Source-cited · Reflects the actual indexed papers · "
            "Automatically improves when new papers are added to the index"
        )

    st.divider()

    # ── Why this matters ─────────────────────────────────────────────────────
    st.markdown("### Why Connecting Agents to MCP Data Sources Matters")
    why_col1, why_col2, why_col3 = st.columns(3)
    with why_col1:
        st.info(
            "**Grounding**  \n"
            "Answers are tied to real, versioned documents — not hallucinated from "
            "training data patterns. Every claim can be traced to a chunk ID and paper."
        )
    with why_col2:
        st.info(
            "**Recency**  \n"
            "Add a new paper to the Azure AI Search index — the agent immediately "
            "knows about it. No retraining, no fine-tuning, no prompt engineering."
        )
    with why_col3:
        st.info(
            "**Precision**  \n"
            "The agent retrieves only what is relevant to the query. Specific numbers "
            "(SNR, error rates, device dimensions) come from the source, not from "
            "generalised training knowledge."
        )

    st.divider()
    st.markdown(
        """
        #### The pattern in one sentence
        > **Without MCP**: the agent reasons from frozen training weights.  
        > **With MCP**: the agent reasons from live, curated, domain-specific data — the difference
        > between a generic assistant and a domain expert that knows your research.

        The agent configuration that unlocks this is a single line in `.agent.md`:
        """
    )
    st.code(
        "tools:\n  - azure-ai-search   # gives the agent access to all indexed paper chunks",
        language="yaml",
    )
