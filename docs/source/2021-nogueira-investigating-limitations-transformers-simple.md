---
type: source
kind: paper
title: Investigating the Limitations of Transformers with Simple Arithmetic Tasks
authors: Rodrigo Nogueira, Zhiying Jiang, Jimmy J. Li
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.13019
source_local: ../raw/2021-nogueira-investigating-limitations-transformers-simple.pdf
topic: general-knowledge
cites:
---

# Investigating the Limitations of Transformers with Simple Arithmetic Tasks

**Authors:** Rodrigo Nogueira, Zhiying Jiang, Jimmy J. Li  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.13019

## One-line
Shows that the surface tokenization of numbers — not model size or data — determines whether a pretrained transformer (T5) can learn addition/subtraction, and that even the best representation fails to extrapolate to digit lengths unseen in training.

## Key claim
With a "10E-BASED" orthography (e.g., $832 \to$ "8 10e2 3 10e1 2 10e0") that interleaves explicit positional power-of-10 tokens between digits, T5-220M reaches near-100% accuracy on addition/subtraction of up to 60-digit numbers from only 1,000 training examples, whereas the default subword (DECIMAL) representation fails entirely beyond 5 digits. No model size (up to T5-3B) or data scale reliably extrapolates to lengths beyond the training distribution.

## Method
Sequence-to-sequence fine-tuning of T5 (60M–3B params) on programmatically generated addition/subtraction questions ("What is [n1] plus [n2]?"), sweeping six number orthographies: DECIMAL, CHARACTER, FIXED-CHARACTER, UNDERSCORE, WORDS, 10-BASED, 10E-BASED. Training uses "balanced sampling" (uniform over digit-counts $d \in [2,D]$); test uses both balanced and random ("random" $\Rightarrow$ ~90% have $D$ digits). Ablations: from-scratch vs pretrained, alternative position embeddings (sinusoidal vs position-wise masked), inverse vs regular digit-output order, varying bases (2, 3, 10, 19), and varying training-set size $10^3$–$10^7$.

## Result
On 30-digit addition with 1,000 examples: 10E-BASED $\approx$ 10-BASED $\approx 100\%$; WORDS 40–60% (stable 5–15 digits, collapses at 20+); FIXED-CHARACTER peaks then falls to ~20% at 15 digits; CHARACTER/UNDERSCORE drop to 0 by 15 digits; DECIMAL $\approx 0$ from 5 digits up. Interpolation to 60 digits with 10E-BASED succeeds for all sizes; extrapolation (train $\le 50$, test 60) succeeds only at T5-3B (~97–99%); smaller models score 0–86%. Pretraining cuts data requirement ~10×. With $10^7$ training examples, all representations except DECIMAL reach $\ge 99.9\%$. Model can correctly emit position tokens beyond training range but mid-sequence "skips" position tokens (e.g., jumps "10e38" $\to$ "10e27") — so the failure is not EOS-bias but length-prediction bias.

## Why it matters here
General background; no direct arena tie. Loosely informs how to feed numeric tokens (digit positions, magnitudes, exponents) to LLM agents that reason about numerical optimization or write evaluator/optimizer code — the "explicit positional scaffolding beats raw subwords" lesson could apply to representing high-precision floats or large coefficient vectors when an agent must read/produce them in text. Not relevant to optimizer mathematics itself.

## Open questions / connections
- Can the 10E-BASED "trick" be generalized to arbitrary numeric reasoning (multiplication, modular arithmetic, mpmath-style high-precision)?
- Why does the model truncate mid-sequence during length extrapolation despite correct EOS placement? Unresolved by Newman et al. (2020) EOS-bias hypothesis.
- Extends Wallace et al. 2019 (numeracy probing), Saxton et al. 2018 (mathematics dataset), Trask et al. 2018 (NALU); contrasts with neuro-symbolic approaches (Andor et al. 2019, Ran et al. 2019).
- Open: position-encoding redesigns (DeBERTa, TUPE, Ke et al. 2020) evaluated on NLP — would they fix arithmetic extrapolation?

## Key terms
transformer arithmetic, subword tokenization, positional encoding, T5, surface representation, digit position tokens, 10E-BASED orthography, length extrapolation, interpolation vs extrapolation, EOS bias, pretraining transfer, numeracy probing
