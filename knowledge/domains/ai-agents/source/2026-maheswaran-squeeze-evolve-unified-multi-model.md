<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution"
authors: [Monishwaran Maheswaran, Leon Lakhani, Zhongzhu Zhou, Shijia Yang, Junxiong Wang, Coleman Hooper, Yuezhou Hu, Rishabh Tiwari, Jue Wang, Harman Singh, Qingyang Wu, Yuqing Jian, Ce Zhang, Kurt Keutzer, Tri Dao, Xiaoxia Wu, Ben Athiwaratkun, James Zou, Chenfeng Xu]
year: 2026
doi: 10.48550/arXiv.2604.07725
source_url: https://doi.org/10.48550/arXiv.2604.07725
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution

## TL;DR
SqueezeEvolve casts test-time scaling methods (majority voting, self-refinement, RSA, AlphaEvolve) as one evolutionary framework, then uses model-intrinsic confidence as a zero-cost fitness signal to route each recombination group to either a cheap or an expensive LLM — preserving the answer diversity that verifier-free evolution otherwise collapses, while cutting API cost ~1.3–3.3× and raising fixed-budget throughput up to ~10×.

## Key findings
- **Two coupled bottlenecks in verifier-free evolution:** (1) without an external verifier the loop amplifies only modes the model already recognizes, collapsing semantic diversity and dragging down the pass@K ceiling (Fig. 2); (2) running one high-cost model uniformly is economically impractical (RSA can emit 500–700× more tokens than single-shot inference; proprietary output tokens cost ~4–25× more than hosted open-weight models as of March 2026).
- **Diversity is the central lever.** pass@K is highly correlated with generation diversity; introducing models with different priors/failure modes via multi-model routing keeps both diversity and pass@K "higher and flatter" across RSA loops.
- **Initialization dominates final accuracy.** Strong-init→weak-agg beats weak-init→strong-agg: +4 pts on HMMT'25 (GPT-OSS-120B/20B) and +23 pts on AIME'25 (Qwen3-4B Thinking/Instruct, 88% vs 65%) (Table 2). Hence the population is always seeded by the expensive Model 2.
- **Weak models aggregate well when the candidate set is strong.** Aggregation accuracy scales with #correct seeds in a group: 0% with no correct seed → 100% with all four correct (Fig. 3a). This justifies routing high-confidence/low-diversity groups to the cheap model.
- **Confidence ≈ fitness.** Group confidence (GC), computed from top-Kℓ token log-probs already produced at inference (Eq. 3–4, same per-token statistic as DeepConf), separates correct-containing from all-incorrect subsets (ΔGC ≥ +3.0). Self-confidence is free; cross-model confidence needs one prefill-only forward pass. Where logprobs are unavailable (e.g. Gemini API), answer-diversity D (count of unique answers) substitutes.
- **Routing mechanism:** each group is assigned to one of L+1 tiers — L=2 LLMs ordered by cost plus a lightweight non-LLM "lite" tier (majority vote). Consensus groups → lite; remaining groups split at a per-problem p-th-percentile threshold (Eq. 6–7), so "easy" groups go to Model 1 and hard groups to Model 2. The routing percentile **p** is the single deployment knob.
- **Results across 8 benchmarks:** 1.3–3.3× cost reduction while matching or exceeding single-model accuracy; in several pairs it *beats* Model 2 alone (e.g. +1.5 pts AIME25, +2.3 pts HMMT25). On multimodal tasks a **text-only** cheap Model 1 (Qwen3.5-35B) that never sees images after loop 0 matched/exceeded the vision model on MMMU-Pro (79.1% vs 78.6%) at 2.7× savings — confirming visual grounding is needed mainly at initialization.
- **ARC-AGI-V2:** 97.5% at $7.74/task without code execution — a new cost-capability SoTA, beating code-execution solvers Confluence Lab (97.9%, $11.77) and Imbue (95.1%, $8.71) on cost.
- **Scientific discovery (circle packing n=26):** score 2.635896, matching/exceeding AlphaEvolve (2.635862) and OpenEvolve — the first **verifier-free** evolutionary method to reach verifier-based performance, using only weak confidence↔objective correlation as a verification surrogate.
- **Systems:** a custom vLLM prefill engine returns only the confidence scalar (~100 bytes vs ~13 MB), giving 4–10× lower scoring latency; end-to-end routing overhead is just 2.4–4.3%; latency-matched GPU pools yield up to ~10× fixed-budget throughput (Qwen3-30B/235B pair).

## Methods (brief)
Test-time inference framework unifying select/recomb operators and a fitness signal f (Eq. 1–2). Evaluated with population N=16, group size K=4, T=10 loops (T=5 vision; T=50 circle packing), 4 seeds, over open-source, mixed open/closed, and multimodal model pairs. Cost reported in actual API dollars per problem; throughput as requests/sec under a fixed GPU budget.

## Limitations
Confidence and answer-diversity are noisy, model-intrinsic proxies — no correctness guarantee; the authors flag the verifier-free/verifier-based gap as narrowest (and confidence weakest) precisely on discovery tasks. Hyperparameters (N, K, T, routing percentile p) are fixed per task, not adapted. Math/coding benchmarks are small (AIME/HMMT = 30 problems each); circle packing is a single instance. No convergence theory for when confidence reliably separates correct from incorrect populations.

## Citations of interest
- Venkatraman et al. 2026 [50] — RSA (Recursive Self-Aggregation); the verifier-free multi-step baseline SqueezeEvolve generalizes.
- Novikov et al. 2025 [34] — AlphaEvolve; the verifier-based evolutionary search SqueezeEvolve matches without code execution.
- Fu et al. 2025 [13] — DeepConf; source of the per-token confidence statistic, here repurposed for routing rather than filtering.
- Singh et al. 2026 [43] — v1; documents RSA diversity collapse and proposes self-verification as an orthogonal remedy.
- Wang et al. 2024 [51] — Mixture-of-Agents; multi-LLM aggregation with fixed (non-adaptive) model assignment.
- Maheswaran et al. 2025 [32] — Arbitrage; fine-grained step-level routing between draft/target models.
- Chollet et al. 2025 [10] — ARC-AGI-2 benchmark used for the SoTA cost-capability result.
