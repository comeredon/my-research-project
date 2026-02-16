"""Streamlit demo application for the AI Research project.

Run with: streamlit run src/demo/app.py

This demo showcases:
1. Document embedding and indexing
2. Semantic retrieval with FAISS
3. REFRAG decoding concepts (visualization)
"""

import logging
import sys
import time

import numpy as np
import streamlit as st

# Add project root to path
sys.path.insert(0, ".")

from src.demo.sample_data import SAMPLE_DOCUMENTS
from src.retrieval.chunker import TextChunker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Research Demo: Embedding Retrieval & REFRAG",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 AI Research Demo")
st.markdown(
    """
    **Embedding-based Retrieval** & **REFRAG (Rethinking RAG-based Decoding)**

    This demo illustrates the core concepts from two research papers on
    retrieval-augmented generation. Built for presentation in a **GitHub Codespace**
    and developed using **GitHub Copilot**.
    """
)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")
    chunk_size = st.slider("Chunk size (words)", 50, 500, 200, step=50)
    chunk_overlap = st.slider("Chunk overlap (words)", 0, 100, 30, step=10)
    top_k = st.slider("Top-K results", 1, 10, 3)
    lambda_weight = st.slider("REFRAG λ (interpolation weight)", 0.0, 1.0, 0.3, step=0.05)

    st.divider()
    st.markdown(
        """
        ### 📚 Demo Sections
        1. **Document Chunking** - See how texts are split
        2. **Embedding & Retrieval** - Semantic search
        3. **REFRAG Visualization** - Token-level blending
        """
    )

# ── Tab Layout ───────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(
    ["📄 Document Chunking", "🔍 Embedding & Retrieval", "🧬 REFRAG Visualization"]
)

# ── Tab 1: Document Chunking ─────────────────────────────────────────────────
with tab1:
    st.header("Document Chunking")
    st.markdown(
        "Documents are split into overlapping chunks for better retrieval. "
        "Adjust chunk size and overlap in the sidebar."
    )

    chunker = TextChunker()
    chunker.config.chunk_size = chunk_size
    chunker.config.chunk_overlap = chunk_overlap

    selected_doc = st.selectbox(
        "Select a document",
        range(len(SAMPLE_DOCUMENTS)),
        format_func=lambda i: SAMPLE_DOCUMENTS[i]["title"],
    )

    doc = SAMPLE_DOCUMENTS[selected_doc]
    st.text_area("Original Document", doc["text"], height=150, disabled=True)

    chunks = chunker.chunk(doc["text"], metadata={"title": doc["title"]})
    st.metric("Number of Chunks", len(chunks))

    for i, chunk in enumerate(chunks):
        with st.expander(f"Chunk {i + 1} (words {chunk['start_word']}-{chunk['end_word']})"):
            st.write(chunk["text"])

# ── Tab 2: Embedding & Retrieval ─────────────────────────────────────────────
with tab2:
    st.header("Embedding & Retrieval")
    st.markdown(
        "Type a query to find the most relevant document chunks using "
        "dense vector similarity search."
    )

    # Use a lightweight simulation for the demo to avoid heavy model downloads
    # In production, replace with: from src.retrieval.pipeline import RetrievalPipeline

    @st.cache_data
    def build_simple_index():
        """Build a simple TF-based index for demo purposes."""
        all_texts = [doc["text"] for doc in SAMPLE_DOCUMENTS]
        all_titles = [doc["title"] for doc in SAMPLE_DOCUMENTS]
        # Simple word overlap scoring (replace with real embeddings in production)
        return all_texts, all_titles

    texts, titles = build_simple_index()

    query = st.text_input(
        "Enter your query",
        placeholder="e.g., How does REFRAG differ from standard RAG?",
    )

    if query:
        with st.spinner("Searching..."):
            time.sleep(0.5)  # Simulate search latency

            # Simple word-overlap scoring for demo (no GPU needed)
            query_words = set(query.lower().split())
            scores = []
            for text in texts:
                doc_words = set(text.lower().split())
                overlap = len(query_words & doc_words)
                scores.append(overlap / max(len(query_words), 1))

            # Rank and display
            ranked = sorted(
                enumerate(scores), key=lambda x: x[1], reverse=True
            )[:top_k]

            st.subheader(f"Top {top_k} Results")
            for rank, (idx, score) in enumerate(ranked, 1):
                with st.container():
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.markdown(f"**#{rank}: {titles[idx]}**")
                        st.write(texts[idx][:300] + "..." if len(texts[idx]) > 300 else texts[idx])
                    with col2:
                        st.metric("Score", f"{score:.2f}")
                    st.divider()

        st.info(
            "💡 **Demo Note**: This uses simple word overlap for portability. "
            "The full pipeline uses sentence-transformers + FAISS for dense retrieval. "
            "See `src/retrieval/pipeline.py` for the production implementation."
        )

# ── Tab 3: REFRAG Visualization ──────────────────────────────────────────────
with tab3:
    st.header("REFRAG: Token-Level Distribution Blending")
    st.markdown(
        """
        The key innovation of REFRAG is modifying token probabilities during
        decoding rather than prepending documents to the prompt.

        **Formula**: `P_final(token) = (1 - λ) × P_LLM(token) + λ × P_retrieval(token)`
        """
    )

    st.subheader("Interactive Distribution Blending")

    # Simulated token distributions
    tokens = ["the", "a", "retrieval", "augmented", "generation", "model", "data", "system"]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**P_LLM** (Language Model Distribution)")
        llm_probs = np.array([0.25, 0.15, 0.05, 0.03, 0.08, 0.20, 0.14, 0.10])
        llm_probs = llm_probs / llm_probs.sum()

    with col2:
        st.markdown("**P_retrieval** (Retrieval Distribution)")
        ret_probs = np.array([0.05, 0.02, 0.30, 0.25, 0.20, 0.08, 0.05, 0.05])
        ret_probs = ret_probs / ret_probs.sum()

    # Blend
    lam = lambda_weight
    blended = (1 - lam) * llm_probs + lam * ret_probs
    blended = blended / blended.sum()

    # Display as bar chart
    import pandas as pd

    df = pd.DataFrame(
        {
            "Token": tokens * 3,
            "Probability": list(llm_probs) + list(ret_probs) + list(blended),
            "Distribution": (
                ["P_LLM"] * len(tokens)
                + ["P_retrieval"] * len(tokens)
                + [f"P_final (λ={lam:.2f})"] * len(tokens)
            ),
        }
    )

    st.bar_chart(
        df.pivot(index="Token", columns="Distribution", values="Probability"),
        height=400,
    )

    # Show token selection
    selected_token = tokens[np.argmax(blended)]
    st.success(
        f"**Selected token**: '{selected_token}' "
        f"(probability: {blended.max():.3f})"
    )

    st.markdown(
        """
        ### How It Works
        1. The LLM predicts next-token probabilities as usual
        2. Retrieved passages are tokenized and weighted by relevance score
        3. The two distributions are blended using λ
        4. Higher λ → more influence from retrieved knowledge
        5. When retrieval confidence is low, λ decreases automatically (dynamic mode)
        """
    )

# ── Footer ───────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    """
    ---
    Built with ❤️ using **GitHub Copilot** in a **GitHub Codespace** |
    [Source Code](https://github.com/comeredon/my-research-project)
    """
)
