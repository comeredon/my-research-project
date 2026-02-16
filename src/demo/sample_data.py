"""Sample documents for the demo.

Contains example documents about AI and RAG so the demo can run
without requiring external data sources.
"""

SAMPLE_DOCUMENTS = [
    {
        "title": "Introduction to RAG",
        "source": "demo",
        "text": (
            "Retrieval-Augmented Generation (RAG) is a technique that combines "
            "the strengths of retrieval-based and generation-based approaches "
            "in natural language processing. Instead of relying solely on the "
            "parametric knowledge stored in a language model's weights, RAG "
            "systems retrieve relevant documents from an external knowledge base "
            "and use them to ground the generation process. This leads to more "
            "factual, up-to-date, and verifiable outputs. RAG was popularized "
            "by Lewis et al. (2020) and has since become a standard approach "
            "for knowledge-intensive NLP tasks."
        ),
    },
    {
        "title": "Dense Retrieval Methods",
        "source": "demo",
        "text": (
            "Dense retrieval methods encode both queries and documents into "
            "continuous vector representations using neural networks, typically "
            "transformer-based encoders. The similarity between a query and a "
            "document is computed as the dot product or cosine similarity "
            "between their respective embeddings. Popular models include DPR "
            "(Dense Passage Retrieval), Contriever, and sentence-transformers. "
            "These methods significantly outperform traditional sparse retrieval "
            "methods like BM25 on many benchmarks, especially when fine-tuned "
            "on domain-specific data."
        ),
    },
    {
        "title": "REFRAG Approach",
        "source": "demo",
        "text": (
            "REFRAG (Rethinking RAG-based Decoding) proposes a fundamentally "
            "different approach to integrating retrieved information during "
            "text generation. Instead of prepending retrieved passages to the "
            "input prompt, REFRAG modifies the token-level probability "
            "distribution during autoregressive decoding. At each generation "
            "step, the model computes both an LLM distribution and a retrieval- "
            "based distribution, then blends them using a dynamic interpolation "
            "weight (lambda). This approach avoids the context window limitations "
            "of standard RAG and allows for more fine-grained control over how "
            "retrieved knowledge influences generation."
        ),
    },
    {
        "title": "Vector Databases and FAISS",
        "source": "demo",
        "text": (
            "Vector databases are specialized systems for storing and querying "
            "high-dimensional vectors. FAISS (Facebook AI Similarity Search) "
            "is one of the most popular libraries for efficient similarity "
            "search. It supports multiple index types including flat (exact), "
            "IVF (inverted file), and HNSW (hierarchical navigable small world) "
            "indices. FAISS can handle billions of vectors and provides both "
            "CPU and GPU implementations. For research prototypes, the flat "
            "index provides exact results, while IVF and HNSW trade a small "
            "amount of accuracy for significantly faster search."
        ),
    },
    {
        "title": "Embedding Models Comparison",
        "source": "demo",
        "text": (
            "Modern embedding models vary in size, performance, and speed. "
            "Small models like all-MiniLM-L6-v2 (22M params, 384 dims) offer "
            "fast inference suitable for demos and prototyping. Medium models "
            "like BGE-base (110M params, 768 dims) provide better accuracy. "
            "Large models like E5-large or GTE-large (335M params, 1024 dims) "
            "achieve state-of-the-art results on retrieval benchmarks like "
            "MTEB. The choice depends on the trade-off between latency, "
            "accuracy, and available compute resources."
        ),
    },
    {
        "title": "Chunking Strategies for RAG",
        "source": "demo",
        "text": (
            "Document chunking is a critical preprocessing step in RAG pipelines. "
            "Common strategies include fixed-size chunking (split by word or "
            "character count), sentence-based chunking, and semantic chunking "
            "(split at topic boundaries). Overlapping chunks help preserve "
            "context at boundaries. The optimal chunk size depends on the "
            "embedding model's context window and the retrieval granularity "
            "needed. Typical sizes range from 128 to 1024 tokens, with 256-512 "
            "being most common for general use cases."
        ),
    },
]
