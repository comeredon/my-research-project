"""REFRAG module: Rethinking RAG-based Decoding.

Implements token-level retrieval-augmented decoding as described in the
REFRAG research paper (Lin et al., 2025).
"""

from src.refrag.decoder import RefragDecoder

__all__ = ["RefragDecoder"]
