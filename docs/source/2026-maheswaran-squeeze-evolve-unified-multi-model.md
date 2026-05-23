---
type: source
kind: paper
title: Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution
authors: Monishwaran Maheswaran, Leon Lakhani, Zhongzhu Zhou, Shijia Yang, Junxiong Wang, Coleman Hooper, Yuezhou Hu, Rishabh Tiwari, Jue Wang, Harman Singh, Qingyang Wu, Yuqing Jian, Ce Zhang, Kurt Keutzer, Tri Dao, Xiaoxia Wu, Ben Athiwaratkun, James Zou, Chenfeng Xu
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2604.07725
source_local: ../raw/2026-maheswaran-squeeze-evolve-unified-multi-model.pdf
topic: general-knowledge
cites: 
---

# Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution

**Authors:** Monishwaran Maheswaran, Leon Lakhani, Zhongzhu Zhou, Shijia Yang, Junxiong Wang, Coleman Hooper, Yuezhou Hu, Rishabh Tiwari, Jue Wang, Harman Singh, Qingyang Wu, Yuqing Jian, Ce Zhang, Kurt Keutzer, Tri Dao, Xiaoxia Wu, Ben Athiwaratkun, James Zou, Chenfeng Xu  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.07725

## One-line
A test-time evolutionary inference framework that orchestrates multiple LLMs of differing cost/capability — using token-level confidence as a routing signal — to do verifier-free self-evolution while preserving diversity and slashing API cost.

## Key claim
Verifier-free evolution is jointly bottlenecked by *diversity collapse* and *cost*; assigning the expensive model only to high-marginal-utility stages (initialization + low-confidence recombination groups) and routing the rest to a cheap model yields up to ~3× lower API cost and ~10× higher fixed-budget throughput, while matching or exceeding single-model baselines and, on circle packing, becoming the first verifier-free evolutionary method to match/exceed verifier-based AlphaEvolve.

## Method
Casts test-time scaling (majority voting, self-refinement, RSA, AlphaEvolve) as a single evolutionary operator $\Phi_f = \text{recomb}_f \circ \text{select}_f$ iterated for $T$ loops over a population of $N$ candidates with $K$-subsets. The strongest model $M_2$ generates the initial population $P^{(0)}$; thereafter, each $K$-subset is scored by group confidence $\mathrm{GC}(g) = \frac{1}{|g|}\sum_{\tau\in g}\frac{1}{|\tau|}\sum_i \tfrac{-1}{K_\ell}\sum_{j=1}^{K_\ell}\log p_\theta(v_j^{(i)}\mid t_{<i},Q)$ (top-$K_\ell$ logprobs, DeepConf-style) or, when logprobs are unavailable, by answer-diversity $D(g)$. A per-problem $p$-th-percentile threshold routes each group to $M_2$ (low confidence/high diversity), the cheap $M_1$ (high confidence), or a non-LLM lite aggregator (consensus). A custom vLLM prefill engine returns only the scalar confidence on-GPU (∼100 B instead of ∼13 MB token-logprob tensors), giving 4–10× lower scoring latency; Model-1/Model-2 GPU pools are latency-matched for fixed-budget throughput.

## Result
Across AIME'25, HMMT'25, GPQA-Diamond, LiveCodeBench-V6, MMMU-Pro, BabyVision, ARC-AGI-V2, and Erich Friedman 26-circle packing: cost reduced 1.3–3.3× while matching/exceeding single-model RSA. ARC-AGI-V2: **97.5%** at **\$7.74/task** (vs GPT-5.4-Pro xhigh 92.2% at \$17.60), a new SOTA cost–capability frontier without code execution. MMMU-Pro: 79.1% (Claude Opus 4.6 73.9%); BabyVision: 41.6% (Kimi-2.5-Thinking 36.5%); on vision tasks a *text-only* cheap $M_1$ that never sees images suffices because visual understanding is only needed at initialization. Circle packing $n=26$: matches/exceeds verifier-based AlphaEvolve via a hybrid LP+SA+SLSQP program (decompose centers $\in\mathbb{R}^{52}$ as combinatorial hard part, radii as LP). Routing overhead 2.4–4.3% end-to-end; fixed-budget throughput up to 10.7× higher. Ancestor model dominates: Qwen3-4B strong-init→weak-agg = 88% vs weak-init→strong-agg = 65% (Δ +23 pp on AIME'25). Group confidence separates correct/incorrect subsets by Δ ≥ +3.0 nats.

## Why it matters here
Directly relevant to the einstein agent's circle-packing problem family (P11, P18, etc.) — the paper's evolved program is essentially the *same* LP-decomposition + SA + SLSQP recipe the wiki already uses, so it both validates the technique and offers a verifier-free orchestration layer that could replace single-model `Agent` calls in the autonomous-loop branch. More broadly, the diversity-collapse finding and confidence-as-fitness routing inform any council-dispatch / multi-step recombination pipeline (`council-dispatch.md`, `self-improvement-loop.md`) where the agent currently uses one model uniformly.

## Open questions / connections
- Does cross-model confidence remain a reliable fitness proxy on math-discovery tasks where verifiers *do* exist (cf. triple-verify rule) — i.e., how often does GC disagree with the exact evaluator?
- The accumulate-update rule with fitness-weighted sampling ($\zeta=0.5$) on circle packing — can this replace standard basin-hopping restart schedules on einstein problems P5/P11/P14/P17?
- Extends FunSearch / AlphaEvolve [Romera-Paredes 2024, Novikov 2025] and RSA [Recursive Self-Aggregation, 2025]; leaves open whether the routing scheme survives when $M_1$ and $M_2$ have disjoint failure modes (e.g., open-weight vs proprietary chains-of-thought).
- Spearman correlation between confidence and circle-packing score across loops hovers near 0 (Fig. 18) — when does GC stop being a valid fitness signal for hard discovery problems?

## Key terms
verifier-free evolution, multi-model orchestration, test-time scaling, recursive self-aggregation, AlphaEvolve, FunSearch, group confidence, DeepConf, token logprobs, diversity collapse, pass@K, confidence-based routing, circle packing, LP decomposition, SLSQP, simulated annealing, ARC-AGI, MMMU-Pro, vLLM prefill engine, ancestor function
