<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Learning to Discover at Test Time
authors: [Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun]
year: 2026
doi: null
source_url: https://test-time-training.github.io/discover/
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Learning to Discover at Test Time

## TL;DR
TTT-Discover performs reinforcement learning *at test time* on a single scientific problem — continuing to train an open LLM (gpt-oss-120b) on its own search attempts rather than prompting a frozen model — and sets new state-of-the-art across mathematics, GPU kernels, algorithm contests, and single-cell denoising for ~$500/problem.

## Key findings
- **Core idea:** Where AlphaEvolve-style methods search by prompting a *frozen* LLM with an evolutionary buffer, TTT-Discover keeps *training* the LLM via RL on attempts at the single test problem. The test problem provides the most valuable training data precisely because it is out-of-distribution.
- **Two design departures from standard RL**, motivated by discovery's goal of one great solution (not high average reward):
  - **Entropic objective** Jβ(θ) = E[log E[e^(βR)]], which as β→∞ approaches the *max* reward rather than the mean. β is set *adaptively per initial state* by constraining the KL of the induced tilted distribution to γ = ln 2 (a constant β was found brittle).
  - **PUCT reuse subroutine** for selecting which buffered solution to warm-start from. Unlike AlphaZero, Q(s) tracks the **maximum** child reward (optimistic), the prior P(s) is rank-based, and visitation counts back-propagate to all ancestors to discourage over-exploitation.
- **Results (open model gpt-oss-120b, 50 steps × 512 rollouts, LoRA rank 32):**
  - **Erdős minimum overlap:** improved upper bound to **0.380876** (vs AlphaEvolve 0.380924; human 0.380927) — a 600-piece *asymmetric* step function; the improvement is ~16× larger than AlphaEvolve's gain over prior SOTA.
  - **First autocorrelation inequality:** C1 ≤ **1.50286** (30,000-piece function) vs ThetaEvolve 1.50314 / AlphaEvolve V2 1.50317, found *from scratch*. Second inequality: 0.959, *not* a discovery (AlphaEvolve V2's 0.961 stands).
  - **GPU kernel (TriMul, AlphaFold primitive):** SOTA on all GPU types — H100 **1161 µs** (vs best human 1371), A100 **2198 µs** (~50% faster than top human, despite never training on A100). Strategy: fuse LayerNorm/gating elementwise ops, store activations FP16, delegate the O(N³) matmul to cuBLAS/rocBLAS.
  - **AtCoder Heuristic Contests:** would have placed **1st** in both ahc039 (geometry, 567,062) and ahc058 (scheduling), beating ALE-Agent and ShinkaEvolve which used frontier-model ensembles (Gemini 2.5 Pro, Claude, gpt-5).
  - **Single-cell denoising (OpenProblems):** score **0.71 PBMC / 0.73 Tabula** vs MAGIC baseline 0.64/0.64; adds gene-adaptive transform ensembling, low-rank SVD refinement, log-space polishing to MAGIC.
- **Beats concurrent test-time RL (ThetaEvolve) at equal model + compute**, attributed to the entropic objective + PUCT vs brittle evolutionary heuristics. Even a weaker Qwen3-8B variant outperforms ThetaEvolve on both autocorrelation inequalities.

## Methods (brief)
RL in an MDP induced by each problem: state = candidate solution (step function, kernel, C++/Python code), action = thinking tokens + code, reward = continuous quality (1/bound, 1/runtime, contest score, 1/MSE), zero on validity failure. Single gradient step per 512-rollout batch on gpt-oss-120b via Tinker (Thinking Machines API), importance-sampling-corrected, KL-penalized. Ablations (Table 8) confirm both adaptive-entropic training and PUCT reuse are each load-bearing; naive RL or no-reuse barely improve.

## Limitations
Restricted to problems with **continuous, verifiable rewards**; sparse/binary or non-verifiable domains are explicitly future work. Benchmark gains may not transfer to biological validity — the authors and reviewer (Prof. Eric Sun, MIT) caution that denoising-metric improvements need not yield better downstream biological insight. Some kernels relied on FP16, raising numerical-stability concerns flagged by GPUMode reviewers; AMD MLA-Decode kernels did not beat top humans with statistical significance.

## Citations of interest
- AlphaEvolve (Novikov et al. 2025) — frozen-LLM evolutionary search baseline TTT-Discover surpasses.
- ThetaEvolve (Wang et al. 2025) — closest concurrent test-time-learning method; direct head-to-head comparison.
- Sun et al. 2020/2023 — foundational test-time-training framework the method builds on.
- Jiang et al. 2025 — concurrent risk-sensitive/entropic RL objective for pass@k.
- Van Dijk et al. 2018 (MAGIC) — the single-cell denoising baseline that TTT-Discover refines.
- Sutton, "The Bitter Lesson" 2019 — framing argument that learning supersedes search at scale.
