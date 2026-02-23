"""Script to run the Microsoft Quantum Research retrieval pipeline demo.

Usage:
    python scripts/run_retrieval_demo.py

This script demonstrates the end-to-end retrieval pipeline over the
Microsoft Quantum research paper corpus:
1. Load document excerpts from the quantum paper corpus
2. Chunk documents
3. Encode chunks into embeddings
4. Index in FAISS
5. Run quantum-research queries and display results

Requires: sentence-transformers, faiss-cpu
"""

import logging
import sys

sys.path.insert(0, ".")

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from src.demo.sample_data import SAMPLE_DOCUMENTS
from src.retrieval.pipeline import RetrievalPipeline

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(name)s | %(message)s")
console = Console()


def main():
    console.print(Panel("[bold blue]Microsoft Quantum Research Explorer: Retrieval Pipeline[/]", expand=False))

    # Step 1: Initialize pipeline
    console.print("\n[bold]Step 1:[/] Initializing retrieval pipeline...")
    pipeline = RetrievalPipeline()

    # Step 2: Index documents
    console.print("\n[bold]Step 2:[/] Indexing sample documents...")
    num_chunks = pipeline.index_documents(SAMPLE_DOCUMENTS)
    console.print(f"  ✓ Indexed {num_chunks} chunks from {len(SAMPLE_DOCUMENTS)} documents")

    # Step 3: Run queries relevant to the Microsoft Quantum research corpus
    queries = [
        "How does quantum phase estimation extract molecular ground state energies?",
        "What is a tetron qubit and how does topological protection work?",
        "How is fermion parity of Majorana zero modes measured interferometrically?",
        "What quantum error correction codes are used in fault-tolerant topological qubit arrays?",
        "How does active space selection reduce the qubit count in QDK/Chemistry?",
    ]

    console.print("\n[bold]Step 3:[/] Running queries...\n")

    for query in queries:
        console.print(f"[bold yellow]Query:[/] {query}")
        results = pipeline.query(query, top_k=3)

        table = Table(title="Results")
        table.add_column("Rank", style="cyan")
        table.add_column("Score", style="green")
        table.add_column("Title", style="white")
        table.add_column("Preview", style="dim")

        for r in results:
            doc = r["document"]
            preview = doc["text"][:80] + "..."
            table.add_row(
                str(r["rank"]),
                f"{r['score']:.4f}",
                doc.get("title", "N/A"),
                preview,
            )

        console.print(table)
        console.print()

    console.print("[bold green]✓ Demo complete![/]")


if __name__ == "__main__":
    main()
