---
type: source
kind: paper
title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"
authors: Tri Dao, Albert Gu
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2405.21060
source_local: ../raw/2024-dao-transformers-ssms-generalized-models.pdf
topic: general-knowledge
cites:
---

# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

**Authors:** Tri Dao, Albert Gu  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2405.21060

## One-line
Establishes a duality between structured state-space models (SSMs) and a generalized form of linear attention via the algebra of semiseparable matrices, yielding the Mamba-2 architecture that is 2–8× faster than Mamba while matching Transformer language-modeling quality.

## Key claim
Selective SSMs are exactly equivalent to matrix multiplication by N-sequentially-semiseparable (N-SSS) matrices, and the intersection of SSMs with kernel/masked attention (the "Structured State Space Duality", SSD) admits both an $O(T)$ recurrent form and an $O(T^2)$ "attention-like" form $Y=(L \circ QK^\top)V$, where $L_{ij}=a_i \cdots a_{j+1}$ is a data-dependent 1-semiseparable mask. Any autoregressive masked-attention layer with constant-time per-token generation is provably an SSM (Theorem C.3).

## Method
Reframe the SSM recurrence $h_t = A_t h_{t-1} + B_t x_t$, $y_t = C_t^\top h_t$ as a matrix transformation $Y = MX$ with $M_{ji} = C_j^\top A_j \cdots A_{i+1} B_i$, identify $M$ as a semiseparable matrix, then exploit structured block decompositions (chunkwise state-passing, dilated, parallel block, associative scan) to derive a hardware-efficient hybrid algorithm that does diagonal blocks in quadratic-attention form and off-diagonal blocks via the linear SSM recurrence. Generalizes linear attention via "Structured Masked Attention" (SMA): the causal lower-triangular 1-mask is replaced by any structured mask $L$ for which fast multiplication exists.

## Result
SSD is 2–8× faster than Mamba's selective-scan kernel and crosses FlashAttention-2 at sequence length 2K, reaching 6× faster at 16K, while permitting 8× larger recurrent state. Mamba-2 Pareto-dominates Mamba and Transformer++ on Chinchilla scaling laws; Mamba-2 2.7B on 300B Pile tokens beats Pythia-6.9B on standard zero-shot benchmarks (avg 60.2 vs 58.3). Closure theorems: sums of $N$-SS and $P$-SS are $(N+P)$-SS, products $(N+P)$-SS, inverses $(N+1)$-SS — so SSMs are closed under composition and inversion.

## Why it matters here
General background; no direct arena tie — this is ML architecture, not math-optimization. Tangentially useful as a worked example of how recognizing a hidden structured-matrix class (semiseparable) collapses a quadratic computation to linear, an analogy worth keeping for problems where naive $O(n^2)$ pair interactions might admit rank-structured factorizations (e.g. autocorrelation Gram matrices, kernel evaluations in LP-bound problems).

## Open questions / connections
- Which other "structured-mask" families $L$ admit subquadratic multiplication, and do any correspond to mathematically natural recurrences beyond 1-SS?
- Extends Katharopoulos et al. "Transformers are RNNs" linear-attention duality and RetNet/GateLoop generalized-decay masks; suggests a broader taxonomy of efficient causal sequence models parameterized by structured-matrix class.
- Closure under inversion ties to the banded-matrix ↔ semiseparable-matrix correspondence (Vandebril et al., Eidelman–Gohberg); banded inverses are an underused structured-matrix family.

## Key terms
state space model, SSM, Mamba-2, structured state space duality, SSD, semiseparable matrix, sequentially semiseparable, SSS, linear attention, structured masked attention, SMA, selective SSM, associative scan, Woodbury inverse, banded matrix, Dao, Gu, Katharopoulos
