---
type: question
author: agent
drafted: 2026-06-28
asked_by: human
status: open
related_problems: [meta]
related_concepts: []
---

# Does an encouraging prompt preamble change the agent's solving performance — and if so, is it effort or efficiency?

**The claim under test.** During the early competition phase, the human reported that
prepending an encouraging preamble to `/auto-branch` runs (e.g. *"you can do it, never
give up, push to the ultimate limit, keep it up, never stop until reaching rank 1"*)
felt helpful. Emotion/encouragement prompting is folklore-effective on weaker models
(GPT-3.5-era EmotionPrompt), but the effect consistently shrinks toward noise on
frontier models and several reproductions find null. The human's memory is an
**uncontrolled** signal (recall bias; early phase also had abundant low-hanging fruit) —
exactly the kind of subjective claim [triple-verify](../../.claude/rules/triple-verify.md)
and [cycle-discipline](../../.claude/rules/cycle-discipline.md) exist to distrust.

**The two mechanisms (the actual question).** If an encouraging preamble *does* lift the
final score, it could be either of two very different things:

1. **Effort** — the preamble just makes the agent run longer (more inference / CoT /
   optimizer iterations). Same score is reachable by spending the same compute on a
   neutral prompt. Uninteresting: equivalent to raising the budget.
2. **Efficiency** — the preamble makes reasoning/optimization *better per unit compute*:
   a higher score at the *same* token / wall-clock budget. The real, interesting claim.

**Falsifiable answer.** Compare the **score-vs-compute frontier** per tone arm, not the
endpoints (endpoints conflate the two mechanisms). Cross tone × budget-regime:
- Encouraging wins only **unconstrained** (and spends more) → *effort*.
- Encouraging wins at **fixed budget** too (curve sits above neutral at equal x) →
  *efficiency*.
- Neither beats control across seeds → **null** (the expected frontier-model outcome;
  a clean null is paper-worthy and fits the v2 "efficiency, not capability" pivot).

**Why this is gap-detect-worthy.** The repo's whole thesis is a *measured*
self-improving agent. "What we say to the agent affects it" is a testable harness
property, and the ablation infrastructure (`compounding_ablation.py` + `ablation_runner.py`:
arms, multi-seed `run_fanout`, distributional `rank_arms`, per-cycle token/wall-clock
telemetry) already supports it almost for free — tone is just one more factor.

**Pre-registration:** `docs/agent/ablations/2026-06-28-prompt-tone-effort-vs-efficiency-preregistration.md`.

## Suggested sources
- Li et al. 2023, "Large Language Models Understand and Can Be Enhanced by Emotional Stimuli" (EmotionPrompt) — the original positive result; note the model generation.
- Reproductions / null findings on frontier models (politeness & emotional-stimulus studies) — for the honest prior.
