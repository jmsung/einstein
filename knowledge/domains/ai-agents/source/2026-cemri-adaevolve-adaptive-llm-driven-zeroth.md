<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization"
authors: [Mert Cemri, Shubham Agrawal, Akshat Gupta, Shu Liu, Audrey Cheng, Qiuyang Mang, Ashwin Naren, Lutfi Eren Erdogan, Koushik Sen, Matei Zaharia, Alexandros G. Dimakis, Ion Stoica]
year: 2026
doi: 10.48550/arXiv.2602.20133
source_url: https://doi.org/10.48550/arXiv.2602.20133
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# AdaEvolve: Adaptive LLM Driven Zeroth-Order Optimization

## TL;DR
AdaEvolve replaces the static schedules of LLM-guided evolutionary program-search systems (OpenEvolve, AlphaEvolve) with a single "accumulated improvement signal" that drives adaptation at three levels — within-population exploration intensity, bandit-based compute routing across populations, and LLM-generated meta-strategies on stall — beating open-source baselines across 185 optimization/algorithm-discovery problems with one fixed hyperparameter set.

## Key findings
- **Core idea**: treat the trajectory of fitness improvements as a gradient analogue (like Adam/RMSProp moments) in a gradient-free search. Each island k maintains a scalar signal `G_t = ρ·G_{t-1} + (1−ρ)·δ_t²`, where δ_t is the normalized improvement over the island's best. High G = productive ("steep gradient"); decaying G = stagnation.
- **Level 1 — Local Adaptation**: exploration intensity `I_t = I_min + (I_max−I_min)/√(1+G_t+ε)`, with I_min=0.1, I_max=0.7. High productivity → exploit (refine top-quartile parents); stagnation → explore (uniform-random parents + orthogonal-solution prompts). Removes manual restart thresholds.
- **Level 2 — Global Adaptation**: islands are arms of a UCB bandit (C=√2). Crucially, rewards are normalized by the **global** best fitness, not local best, to avoid "poor island bias" (an island at fitness 1 making +0.5 should not outrank one at fitness 100 making +10). Decayed cumulative reward/visit counts (R, V) prevent stale early-breakthrough islands from dominating. Ring migration every M iterations; **dynamic island spawning** when all islands fall below τ_S=0.02.
- **Level 3 — Meta-Guidance**: when all islands drop below τ_M=0.12 ("System 2" trigger), a separate LLM analyzes the evaluator + failed attempts and emits high-level *solution tactics* (e.g. "switch greedy → dynamic programming", "use SLSQP continuous optimization") injected into mutation prompts.
- **Minimal config**: user supplies only model name + iteration budget — no per-task tuning of mutation rates, island counts, or prompts.
- **Results**: matches/exceeds human or AlphaEvolve SOTA on 4/6 math optimization tasks. On **Circle Packing (N=26)** reaches 2.636, beating human SOTA (2.634) and AlphaEvolve (2.635). Wins all 7 ADRS systems benchmarks on both GPT-5 and Gemini-3-Pro backbones. On **Frontier-CS (172 problems)**, mean 61.33 vs OpenEvolve 50.75 / ShinkaEvolve 47.79 / GEPA 43.04, and ~3× over single-call GPT-5 (20.64, median 0). ARC-AGI-2: 49–50% vs OpenEvolve 42–44%.
- **Ablations** (Table 4): removing Meta-Guidance hurts most (circle packing 2.629→2.521; signal processing 0.718→0.548); bandit island-selection matters more for signal processing, local adaptation more for circle packing; dynamic spawning beats fixed 2- or 5-island setups.

## Methods (brief)
LLM-driven evolutionary search over executable programs: K asynchronous islands each running select→LLM-mutate→evaluate→update cycles, coordinated by the three adaptive levels above. Evaluated with GPT-5 and Gemini-3-Pro backbones, identical hyperparameters throughout, 50–100 LLM calls/iterations per run, mean±std over 3 runs, against open-source baselines GEPA, ShinkaEvolve, OpenEvolve (plus AlphaEvolve/human references where available).

## Limitations
Inference-only (no fine-tuning); benchmarks are optimization/algorithm-discovery tasks with cheap-ish executable evaluators, so transfer to expensive wet-lab-style objectives is untested. Thresholds (τ_S=0.02, τ_M=0.12, ρ, I_min/I_max) are fixed but still chosen empirically. ARC-AGI-2 results are flagged as exploratory (evolutionary test-time adaptation violates strict train/test separation). Gains shrink on smooth-reward tasks where static schedules already align well.

## Citations of interest
- Novikov et al. 2025, *AlphaEvolve* — the proprietary population-based program-evolution agent AdaEvolve benchmarks against.
- Sharma 2025, *OpenEvolve* — open-source AlphaEvolve reimplementation; primary baseline whose static schedules AdaEvolve replaces.
- Romera-Paredes et al. 2024, *FunSearch* (Nature) — established LLMs as semantic mutation operators in evolutionary search.
- Lange et al. 2025, *ShinkaEvolve* — sample-efficient island-based evolution baseline.
- Agrawal et al. 2025, *GEPA* — reflective prompt evolution over a Pareto set; related scaffold and baseline.
- Kingma 2014 / Duchi et al. 2011, *Adam / AdaGrad* — adaptive-gradient inspiration for the improvement-signal-as-gradient analogy.
- Cheng et al. 2025, *ADRS / "Barbarians at the gate"* — source of the 7 real-world systems-optimization benchmarks.
