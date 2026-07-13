<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning"
authors: [Peng Xia, Kaide Zeng, Jiaqi Liu, Can Qin, Fang Wu, Yiyang Zhou, Caiming Xiong, Huaxiu Yao]
year: 2025
doi: 10.48550/arxiv.2511.16043
source_url: https://doi.org/10.48550/arxiv.2511.16043
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Agent0: Unleashing Self-Evolving Agents from Zero Data via Tool-Integrated Reasoning

## TL;DR
Agent0 co-evolves two agents from the same base LLM — a curriculum agent that proposes ever-harder tasks and an executor agent that solves them — with no human data and a shared code-interpreter tool, lifting Qwen3-8B-Base by 18% on math and 24% on general reasoning.

## Key findings
- **Two-agent symbiotic competition from one base model.** A *curriculum agent* (πθ) generates frontier tasks; an *executor agent* (πϕ) learns to solve them. Both initialize from the same base LLM (Qwen3-4B-Base, Qwen3-8B-Base) and co-evolve over iterations via GRPO — no external/human-curated data.
- **Curriculum reward = uncertainty + tool-use − repetition.** The uncertainty reward `R_unc = 1 − 2|p̂ − 0.5|` peaks when executor self-consistency p̂ = 0.5 (maximally confusing tasks); a tool-use reward `R_tool = γ·min(N_tool, C)` (γ=0.6, cap C=4) explicitly incentivizes tasks requiring the code interpreter; a BLEU-based repetition penalty enforces batch diversity. Composite reward is gated by a format check.
- **Executor trained on a difficulty-filtered band.** Tasks are kept only where self-consistency falls in p̂ ∈ [0.3, 0.8] (threshold δ=0.25), i.e. neither too easy nor too hard. Pseudo-labels come from the executor's own majority vote over k=10 samples.
- **ADPO (Ambiguity-Dynamic Policy Optimization).** A GRPO variant that (1) scales advantage by self-consistency to down-weight noisy pseudo-labels on ambiguous tasks, and (2) dynamically relaxes the upper PPO clipping bound `ε_high(x)` as a decreasing function of p̂(x), letting low-probability correct-reasoning tokens grow on hard tasks while keeping tight bounds on confident ones.
- **Results.** On Qwen3-8B-Base: math AVG 49.2 → 58.2, general AVG 34.5 → 42.1. Beats data-free R-Zero by 6.4%, tool-using Absolute Zero by 10.6%, and even API-dependent Socratic-Zero by 3.7% (Tables 1–2).
- **Co-evolution is real, not static.** Across 3 iterations the math AVG climbs 55.1 → 56.5 → 58.2. A fixed Iter-1 executor's pass rate on later curricula drops 64.0% → 58.5% → 51.0% while average tool calls rise 1.65 → 2.10 → 2.60 (Table 5) — direct evidence the curriculum agent escalates difficulty and tool reliance.
- **Ablations (Table 3).** Removing curriculum training −9.3%, tool reward −7.2%, repetition penalty large drop on general tasks, ADPO −1.9%, multi-turn rollout notable on math. Increasing curriculum interaction turns 1→4 adds +3.4% overall (Table 9).

## Methods (brief)
Built on VeRL with a VeRL-Tool sandboxed Python interpreter using a "stop-and-go" multi-turn rollout (generation halts on a ```python``` block, executes, appends ```output```, resumes). Both agents trained with GRPO; executor with the ADPO modification. k=10 executor samples per task for uncertainty/pseudo-labels; GPT-4o used only as an evaluation answer-checker. Evaluated pass@1 (mean@32 for AMC/AIME) across 10 math + general benchmarks.

## Limitations
Tasks are restricted to verifiable, single-answer math/reasoning problems where majority voting yields usable pseudo-labels; pseudo-labels on high-ambiguity tasks remain noisy (the motivation for ADPO). Evaluated on only two Qwen3 base sizes, 3 iterations, ≤4 turns, and a code-interpreter as the sole tool — generalization to open-ended or non-verifiable domains is untested.

## Citations of interest
- **GRPO / DeepSeekMath** (Shao et al., 2024) — the critic-free relative-advantage RL backbone Agent0 builds on.
- **R-Zero** (Huang et al., 2025) — closest data-free self-evolving baseline; no tools, the ceiling Agent0 claims to break.
- **Absolute Zero** (Zhao et al., 2025) — self-play with a code executor used only for verification; main tool-aware comparison.
- **Socratic-Zero** (Wang et al., 2025d) — data-free co-evolution leaning on external proprietary models (OpenAI APIs).
- **DAPO** (Yu et al., 2025b) — analysis of clipping asymmetry motivating ADPO's dynamic trust region.
- **SimpleTIR / ASPO** (Xue et al., 2025; Lin & Xu, 2025) — stability techniques for multi-turn tool-integrated RL.
