---
type: source
kind: paper
title: Transformer Quality in Linear Time
authors: Weizhe Hua, Zihang Dai, Hanxiao Liu, Quoc V. Le
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2202.10447
source_local: ../raw/2022-hua-transformer-quality-linear-time.pdf
topic: general-knowledge
cites:
---

# Transformer Quality in Linear Time

**Authors:** Weizhe Hua, Zihang Dai, Hanxiao Liu, Quoc V. Le  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2202.10447

## One-line
Introduces FLASH, a Transformer variant that matches full-attention quality in linear time over context length on accelerators, via a gated single-head attention layer plus a mixed local-quadratic / global-linear "chunked" attention.

## Key claim
A simplified single-head, softmax-free Gated Attention Unit (GAU) — using $A = \text{relu}^2(QK^\top + b)$ in place of multi-head softmax — matches multi-head Transformers in perplexity, and combining GAU with non-overlapping chunked attention achieves up to $4.9\times$ training speedup on Wiki-40B (512–8192 ctx), $12.1\times$ on PG-19, $4.8\times$ on C4 MLM at $\sim$110M parameters.

## Method
GAU fuses GLU and attention into one block: $O = (U \odot \hat{V})W_o$ with $\hat{V}=AV$, where $U,V$ are GLU branches and $A$ is a cheap relu-squared attention over a shared low-dim projection $Z \in \mathbb{R}^{T\times s}$ (default $s=128$). For long sequences, "mixed chunk attention" splits the input into $G$ chunks of size $C$, applies exact quadratic attention within each chunk ($O(TCd)$) and a linear attention (Katharopoulos-style, $\hat V_g^{\text{lin}} = Q_g^{\text{lin}}\sum_{h\le g}K_h^{\text{lin}\top}V_h$) across chunks, cutting the cumulative-sum sequential dependency from $T$ to $T/C$ for auto-regressive training.

## Result
On C4 MLM at 8192 ctx, FLASH reaches PPLX 3.897 vs Transformer++ 3.933 with $\sim 4\times$ less latency; on Wiki-40B LM at 8192, FLASH 15.109 vs Transformer++ 15.254 at $\sim 4\times$ speedup. Ablations show: (1) softmax can be replaced by squared-ReLU without loss when gating is present; (2) approximation cost (FLASH-Quad → FLASH) is much smaller than (TFM++ → MC-TFM++), confirming GAU is more compatible with weak/approximate attention than MHSA. Constant per-step decoding cost $O(Cd^2)$.

## Why it matters here
General background; no direct arena tie — this is a sequence-modeling architecture paper, orthogonal to the project's optimization-and-knowledge-distillation pipeline. Possibly relevant to compute-routing intuitions (parallel-vs-sequential structure on TPU/GPU, RNN-style cumsum bottlenecks) and to any future agent-internal long-context modeling, but not to the 23 Einstein Arena math problems.

## Open questions / connections
- Scaling laws of GAU vs MHSA at >1B parameters, and downstream-task transfer — explicitly left open by the authors.
- Whether mixed chunk attention generalizes to non-language modalities (vision, audio) where Performer/Longformer/BigBird have been tried.
- Optimal partial-attention substitute for the local-quadratic component (overlapping windows, hashing, axial) appears task-specific and unresolved.
- Connection to Combiner (Ren et al., 2021): chunked design is similar but FLASH stores larger $O(sd)$ per-chunk summary vs Combiner's $O(d)$, trading more memory for quality.

## Key terms
gated attention unit, GAU, FLASH, linear attention, mixed chunk attention, Transformer, squared ReLU, GLU, multi-head self-attention, RoPE, cumulative sum, Performer, Combiner, auto-regressive training
