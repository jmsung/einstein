---
type: source
kind: paper
title: Parallelizing Linear Transformers with the Delta Rule over Sequence Length
authors: Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, Yoon Kim
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.06484
source_local: ../raw/2024-yang-parallelizing-linear-transformers-delta.pdf
topic: general-knowledge
cites:
---

# Parallelizing Linear Transformers with the Delta Rule over Sequence Length

**Authors:** Songlin Yang, Bailin Wang, Yu Zhang, Yikang Shen, Yoon Kim  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.06484

## One-line
A hardware-efficient training algorithm for DeltaNet (linear transformer with delta-rule updates) that parallelizes the forward/backward pass over sequence length using the WY representation for products of Householder matrices.

## Key claim
DeltaNet can be reparameterized so its recurrence $S_t = S_{t-1}(I - \beta_t k_t k_t^T) + \beta_t v_t k_t^T$ becomes a product of generalized Householder transformations; this admits a chunkwise parallel form with $O(LCd + Ld^2)$ complexity and matmul-rich operations, enabling 1.3B-parameter / 100B-token training that outperforms Mamba and GLA on perplexity, zero-shot tasks, and recall-intensive benchmarks (MQAR, MAD, RegBench).

## Method
Observe that $S_t = \sum_{i=1}^t u_i k_i^T$ with "pseudo-values" $u_t = \beta_t(v_t - \sum_{i<t} u_i (k_i^T k_t))$, and that the transition $I - \beta_t k_t k_t^T$ is a (generalized) Householder reflector. Apply the WY representation [Bischof–Van Loan] to compactly store products of Householders in $O(d)$ rather than $O(d^2)$ per step, then use the UT-transform $T_{[t]} = (I + \mathrm{tril}(\mathrm{diag}(\beta)KK^T, -1))^{-1}\mathrm{diag}(\beta)$ to recast the recurrence on each chunk as a triangular solve plus matmuls suitable for tensor cores. Implement in Triton with hidden-state recomputation on the backward pass.

## Result
Chunkwise DeltaNet achieves up to ~30× speedup over the sequential recurrent kernel at long sequence / large head dimension. At 1.3B params / 100B tokens it beats Mamba and GLA on perplexity and zero-shot downstream tasks; on MQAR and MAD it matches or exceeds transformers in associative recall, scoring 100% on In-Context Recall, Noisy Recall, and Selective Copy. Hybrids interleaving DeltaNet with sliding-window or two global-attention layers beat strong Transformer++ baselines.

## Why it matters here
General background; no direct arena tie. This is a sequence-modeling architecture paper — it informs efficient agent inference / long-context retrieval infrastructure but does not bear on the math-optimization problems (sphere packing, autocorrelation, kissing numbers) the Einstein Arena agent solves. The Householder/WY trick is mathematically pretty but the orthogonal-matrix parameterization context (normalizing flows, RNN stability) is the relevant reuse, not arena optimization.

## Open questions / connections
- The fully parallel form requires a matrix inverse that scales cubically in $L$ — is there a subcubic exact parallel form?
- Does the delta-rule's online-regression-by-SGD framing extend to richer per-step losses (e.g. quadratic with momentum), à la TTT / Gated DeltaNet [125]?
- WY representation as a primitive: where else in agent infra (orthogonal RNNs, normalizing flows, fast-weight programmers) does it cut memory I/O similarly?

## Key terms
DeltaNet, linear attention, delta rule, Widrow-Hoff, Householder transformation, WY representation, UT transform, chunkwise parallel form, fast weight programmer, associative recall, Mamba, GLA, linear transformer, sequence-length parallelism
