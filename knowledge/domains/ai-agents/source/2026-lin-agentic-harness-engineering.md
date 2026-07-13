<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
authors: [Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Zhiheng Xi, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui, Yu-Gang Jiang]
year: 2026
doi: null
source_url: https://arxiv.org/abs/2604.25850
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

## TL;DR
AHE is a closed self-evolution loop in which a meta-agent edits a coding agent's *harness* (system prompt, tools, middleware, long-term memory) — not the base model — driven by three "observability" pillars that make every edit a falsifiable, file-level contract verified against the next round's task outcomes. Ten iterations lift pass@1 on Terminal-Bench 2 from 69.7% to 77.0%, beating human-designed (Codex 71.9%) and prompt-only self-evolving baselines, and the frozen harness transfers to new benchmarks and model families.

## Key findings
- **Three observability pillars.** (1) *Component observability* — the NexAU substrate exposes 7 orthogonal, file-level editable component types (system prompt, tool description, tool impl, middleware, skill, sub-agent config, long-term memory) at fixed mount points; each failure pattern maps to one component class, each edit is one git commit (free rollback). (2) *Experience observability* — an "Agent Debugger" distills ~10M raw trajectory tokens down to ~10K via a layered, drill-down evidence corpus (per-task root-cause reports + a benchmark-level overview). (3) *Decision observability* — a change manifest pairs every edit with a self-declared prediction (predicted fixes + at-risk regressions), intersected next round with observed task-level deltas to keep or roll back.
- **Headline result.** 10 AHE iterations on Terminal-Bench 2 (89 tasks; 4 easy / 55 medium / 30 hard) raise pass@1 **69.7% → 77.0%**, finishing in ~32 hours. Beats human-designed harnesses OpenCode (47.2%), Terminus-2 (62.9%), Codex (71.9%) and self-evolving baselines ACE (68.9%) and Training-Free GRPO (72.3%). Only Hard tier marginally trails Codex (53.3% vs 56.7%).
- **Cross-benchmark transfer (frozen, no re-evolution).** On SWE-bench-verified (500 tasks) AHE gets the highest aggregate success (75.6% vs seed 75.2%) while using **12% fewer tokens than the seed** (461k vs 526k), 32% fewer than ACE, 21% fewer than TF-GRPO. Prompt-only baselines (ACE, TF-GRPO) actually regress below the seed while spending 11–29% more tokens — their distilled text rides every model call without reshaping policy.
- **Cross-model transfer.** Frozen harness yields +2.3 to +10.1 pp across five alternate bases; cross-family gains dominate: deepseek-v4-flash +10.1 pp (51.7→61.8%), qwen-3.6-plus +6.3 pp, gemini-3.1-flash-lite +5.1 pp. Bases further from saturation lean more on the coordination patterns AHE fixes in tools/middleware/memory.
- **Ablations localize the gain.** Single-component swaps into the seed: memory-only 75.3%, tool-only 73.0%, middleware-only 71.9% — but **system-prompt-only regresses to 67.4%** (−2.3 pp). The three positive gains sum to +11.1 pp vs full AHE's +7.3 pp, so components interact **non-additively** (overlapping closure-style verification spends turns on redundant re-checks), capping aggregate gain. Factual harness structure transfers; prose-level strategy does not.

## Methods (brief)
All three role agents (Code Agent, Agent Debugger, Evolve Agent) share one base model, GPT-5.4 at high reasoning, isolating gains to harness edits rather than analyzer/editor capability. The seed is deliberately minimal (bash-only, no middleware/skills/memory) so every added component must earn its place. Outer loop (Algorithm 1): rollout (k≥2 per task) → clean → attribute prior manifest & roll back rejected edits → distill → edit → git-commit, run unattended for N iterations. Runs use Harbor dispatch, fresh E2B sandboxes per rollout, 3600 s per-task timeout; pass@1 counts infrastructure aborts as failures.

## Limitations
Evolution driven only on Terminal-Bench 2, transfer probed only on SWE-bench-verified — broader languages, repo-scale deployment, and human-in-the-loop untested. The step-budget/timeout was fitted to GPT-5.4 high, so cross-model numbers conflate harness portability with operating-point coupling (within-family gain is non-monotone across reasoning tiers). Critically, the loop's **self-attribution is reliable for fixes but blind to regressions**: fix precision/recall ≈ 33.7%/51.4% (~5× random) but regression precision/recall ≈ 11.8%/11.1% (~2× random) — across 9 rounds only 5 of 43 predicted regressions landed while 40 unforeseen ones occurred. High-variance setting; a research prototype, not a mature autonomous self-improver.

## Citations of interest
- Terminal-Bench [21] — the 89-task command-line benchmark AHE evolves on.
- SWE-bench [14] — repo-scale issue-resolution benchmark used for transfer.
- ACE / Agentic Context Engineering [49] — prompt-playbook self-evolution baseline.
- Training-Free GRPO [4] — trajectory-feedback tool-sequence reinforcement baseline.
- NexAU [23, 37] — the decoupled, file-level harness framework AHE instantiates.
- Sutton, "The Bitter Lesson" [34] — motivates the minimal-human-prior design stance.
