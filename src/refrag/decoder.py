"""REFRAG Decoder: Token-level retrieval-augmented decoding.

Instead of prepending retrieved documents to the LLM prompt (standard RAG),
REFRAG modifies the token probability distribution during decoding by
interpolating the LLM's output distribution with a retrieval-based
distribution computed from relevant passages.

Key idea from the paper:
  P_final(token) = (1 - lambda) * P_LLM(token) + lambda * P_retrieval(token)

where lambda is a dynamic interpolation weight based on retrieval confidence.

Reference: "REFRAG: Rethinking RAG based Decoding" (Lin et al., 2025)
https://arxiv.org/abs/2509.01092
"""

import logging
from dataclasses import dataclass

import numpy as np
import torch
import torch.nn.functional as F

logger = logging.getLogger(__name__)


@dataclass
class RefragConfig:
    """Configuration for REFRAG decoding."""

    # Interpolation weight between LLM and retrieval distributions
    lambda_weight: float = 0.3
    # Whether to dynamically adjust lambda based on retrieval confidence
    dynamic_lambda: bool = True
    # Temperature for retrieval distribution
    retrieval_temperature: float = 1.0
    # Maximum number of retrieved passages to consider
    max_passages: int = 5
    # Minimum retrieval score to include a passage
    min_retrieval_score: float = 0.1
    # Maximum tokens to generate
    max_new_tokens: int = 256


class RefragDecoder:
    """Implements REFRAG: retrieval-augmented token-level decoding.

    This modifies the standard autoregressive decoding loop to blend
    the LLM's next-token distribution with a retrieval-based distribution
    at each generation step.

    Example:
        >>> decoder = RefragDecoder(model, tokenizer, retrieval_pipeline)
        >>> output = decoder.generate("What is retrieval augmented generation?")
    """

    def __init__(self, model, tokenizer, retrieval_pipeline, config=None):
        self.model = model
        self.tokenizer = tokenizer
        self.retrieval_pipeline = retrieval_pipeline
        self.config = config or RefragConfig()

    def _compute_retrieval_distribution(
        self, query: str, vocab_size: int
    ) -> torch.Tensor:
        """Compute a token distribution from retrieved passages.

        Retrieves relevant passages, tokenizes them, and builds a
        distribution over the vocabulary based on token frequencies
        weighted by retrieval scores.

        Args:
            query: The current generation context.
            vocab_size: Size of the model's vocabulary.

        Returns:
            Normalized probability distribution over vocabulary.
        """
        results = self.retrieval_pipeline.query(
            query, top_k=self.config.max_passages
        )

        # Filter by minimum score
        results = [
            r for r in results if r["score"] >= self.config.min_retrieval_score
        ]

        if not results:
            # Uniform distribution if no relevant passages found
            return torch.ones(vocab_size) / vocab_size

        # Build weighted token frequency distribution
        token_scores = torch.zeros(vocab_size)

        for result in results:
            passage_text = result["document"]["text"]
            score = result["score"]

            # Tokenize the retrieved passage
            tokens = self.tokenizer.encode(passage_text, add_special_tokens=False)

            # Weight each token by retrieval score
            for token_id in tokens:
                if token_id < vocab_size:
                    token_scores[token_id] += score

        # Apply temperature and normalize
        token_scores = token_scores / self.config.retrieval_temperature
        retrieval_dist = F.softmax(token_scores, dim=0)

        return retrieval_dist

    def _compute_dynamic_lambda(self, retrieval_results: list[dict]) -> float:
        """Compute dynamic interpolation weight based on retrieval confidence.

        Higher retrieval scores → higher lambda → more reliance on retrieval.
        Low scores → lower lambda → fall back to LLM.

        Args:
            retrieval_results: Results from the retrieval pipeline.

        Returns:
            Lambda value between 0 and 1.
        """
        if not retrieval_results:
            return 0.0

        avg_score = np.mean([r["score"] for r in retrieval_results])
        # Sigmoid mapping to [0, 1] centered around 0.5 retrieval score
        dynamic_lambda = 1.0 / (1.0 + np.exp(-5 * (avg_score - 0.5)))
        return float(np.clip(dynamic_lambda, 0.05, 0.95))

    @torch.no_grad()
    def generate(self, prompt: str) -> str:
        """Generate text using REFRAG decoding.

        At each token step:
        1. Compute P_LLM(token | context) from the language model
        2. Compute P_retrieval(token | query) from retrieved passages
        3. Blend: P_final = (1 - λ) * P_LLM + λ * P_retrieval
        4. Sample from P_final

        Args:
            prompt: Input prompt for generation.

        Returns:
            Generated text string.
        """
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        input_ids = input_ids.to(self.model.device)
        vocab_size = self.model.config.vocab_size

        generated_tokens = []

        for step in range(self.config.max_new_tokens):
            # Step 1: Get LLM distribution
            outputs = self.model(input_ids)
            llm_logits = outputs.logits[:, -1, :]  # Last token logits
            llm_dist = F.softmax(llm_logits, dim=-1).squeeze(0)

            # Step 2: Get retrieval distribution
            context = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)
            retrieval_dist = self._compute_retrieval_distribution(context, vocab_size)
            retrieval_dist = retrieval_dist.to(llm_dist.device)

            # Step 3: Compute lambda
            if self.config.dynamic_lambda:
                results = self.retrieval_pipeline.query(context)
                lam = self._compute_dynamic_lambda(results)
            else:
                lam = self.config.lambda_weight

            # Step 4: Blend distributions
            blended_dist = (1 - lam) * llm_dist + lam * retrieval_dist

            # Sample next token
            next_token = torch.multinomial(blended_dist.unsqueeze(0), num_samples=1)
            generated_tokens.append(next_token.item())

            # Check for EOS
            if next_token.item() == self.tokenizer.eos_token_id:
                break

            # Append to input for next step
            input_ids = torch.cat([input_ids, next_token], dim=-1)

        output_text = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        return output_text
