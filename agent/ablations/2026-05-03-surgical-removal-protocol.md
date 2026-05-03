---
type: ablation-protocol
author: agent
drafted: 2026-05-03
status: protocol  # not yet executed; this is the experimental design
prior_ablations:
  - 2026-05-02-cold-vs-warm-p10-thomson.md
  - 2026-05-03-cold-vs-warm-p11-tammes.md
  - 2026-05-03-cold-vs-warm-p22-kissing-d12.md
  - 2026-05-03-cold-vs-warm-p9-uncertainty.md
---

# Surgical-removal ablation protocol — methodology + 4 pre-registered experiments

## Why this protocol

The 4-audit cold-vs-warm series (PRs #79, #83, #86, #87) measured **aggregate** wiki uplift on each problem. It does not isolate which *individual page* is load-bearing. A warm agent has access to ~170 wiki pages; the audit infers which 3–5 pages "carry" the uplift from page-citation patterns + qualitative reasoning, but doesn't *prove* it.

The surgical-removal protocol is the rigorous version: take a warm agent, *remove one specific page*, re-run the same problem, compare. This isolates page-level contribution.

## Methodology

### Setup

For each (problem, page) candidate pair:

1. **Branch a temporary worktree** at the wiki commit immediately after the wiki bootstrap (PR #55) — the canonical "warm" baseline.
2. **`git rm`** the target page from this worktree only. Do not edit citing pages — leave the dangling cite. The agent will encounter it as a 404.
3. **Refresh `qmd`** in the worktree so the removed page is not discoverable.
4. **Spawn a fresh Claude Code session** in the worktree with no memory of this ablation (no shared CLAUDE.md hint about the removal).
5. **Give the agent the same problem-statement-only briefing** the cold-vs-warm audits used. The agent then runs its normal `/where → /goal → /act` flow. Wiki access is full; just one page is missing.
6. **Measure**: final score, total wall-time, list of pages cited during the cycle, list of attempts (especially attempts that would have been ruled out by the removed page), and whether the agent re-derives the removed page's content.

### What "load-bearing" means operationally

A page is **load-bearing for problem P** if its removal causes one of:

1. **Score regression**: warm-minus-page agent gets a worse score on P than the warm baseline.
2. **Direction loss**: warm-minus-page agent pursues a strategy ruled out by the removed page (chases impossible target, runs known dead-end, etc.).
3. **Validity loss**: warm-minus-page agent celebrates a result that the removed page would have flagged as invalid.
4. **Compute regression**: warm-minus-page agent uses substantially more compute (≥2× threshold) reaching the same outcome.

A page is **redundant** if its removal causes *none* of the above — the agent re-derives the content from sibling pages or training data without measurable cost.

### Statistical caveats

- Single-trial: each (problem, page) experiment is one run. Variance comes from random seeds in optimizers, model sampling temperature, etc. To call a result "load-bearing" with confidence, repeat 3× with different random seeds and look for consistent outcomes.
- Confounds: the agent might re-derive the page's content via web search or training data. Document whenever this happens — it's evidence that the page is *correctly summarizing public knowledge* rather than *carrying private wisdom*.
- The agent's behavior is non-deterministic. Treat predictions below as point-estimates with ±1 ablation worth of variance.

## Four pre-registered experiments

Below are four (problem, page) candidates — one per uplift mechanism from the 4-audit series. Each experiment removes the page the audit identified as load-bearing and predicts what the agent will do.

### Experiment 1 — Compute (P10 / `findings/frozen-problem-triage.md`)

- **Problem**: P10 Thomson n=282.
- **Page removed**: [`findings/frozen-problem-triage.md`](../../wiki/findings/frozen-problem-triage.md). The 3-check entry-gate rule + the "magic-number Thomson" inventory hook.
- **Hypothesis**: warm-minus-page agent attempts at least one optimizer run on P10 before realizing it's a magic-number frozen problem.
- **Prediction**:
  - **Score**: same (the SOTA basin is rigid; both agents reach it).
  - **Compute**: 2–10× more (warm-minus-page burns 30 min – 4 hours on SLSQP/SA before checking the inventory page or the basin-rigidity finding and concluding "frozen").
  - **Pages cited**: warm-minus-page will cite `concepts/basin-rigidity.md` and `findings/basin-rigidity.md` more heavily — re-derives the frozen conclusion from the rigidity machinery rather than the inventory hook.
  - **Re-derivation**: yes (the magic-number theory is documented in Wales–Doye + Hardin–Sloane references; warm-minus-page should reach the same conclusion via slower paths).
- **Verdict if confirmed**: `frozen-problem-triage.md` is **redundant for P10** — its content is shortcut-only, derivable from the rigidity concept page. (This would actually be a *useful* signal: the page is a *speed-up*, not a unique-content carrier.)
- **Verdict if falsified** (warm-minus-page never reaches the frozen conclusion in budget): the page is genuinely load-bearing as a *trigger* — without the inventory hook, the agent doesn't think to apply the rigidity machinery.

### Experiment 2 — Score (P11 / `findings/float64-ceiling.md` lessons #34/#43/#44)

- **Problem**: P11 Tammes n=50.
- **Page removed**: [`findings/float64-ceiling.md`](../../wiki/findings/float64-ceiling.md). The 9-row table + lessons including #34/#43/#44 (the wide-tolerance recipe).
- **Hypothesis**: warm-minus-page agent applies SLSQP polish at default tolerance (`1e-7`), stalls 1–10 ulps below the float64 ceiling.
- **Prediction**:
  - **Score**: 1–10 ulps worse than baseline. With probability 70%, the agent stalls at `0.51347208468055xx` instead of `0.51347208468056470`.
  - **Compute**: similar to baseline; the cost is in score, not time.
  - **Pages cited**: the agent may cite `concepts/contact-graph-rigidity.md` (the Maxwell counting test) and `findings/tammes-50-basin-uniqueness-evidence.md`, but *without* the wide-tolerance lesson, the SLSQP call uses defaults.
  - **Re-derivation**: unlikely. The wide-tolerance recipe is calibrated empirical wisdom (1e-3 vs 1e-7); SciPy docs don't recommend it. A cold-style web search would not surface it.
- **Verdict if confirmed**: `findings/float64-ceiling.md` is **load-bearing for P11 score** — its removal causes a measurable score regression.
- **Verdict if falsified**: the wide-tolerance recipe is documented elsewhere I missed (e.g., in `techniques/slsqp-active-pair-polish.md`), and the removal doesn't matter.

### Experiment 3 — Direction (P22 / `findings/structural-cap-at-score-2-meta.md`)

- **Problem**: P22 d=12 kissing n=841.
- **Page removed**: [`findings/structural-cap-at-score-2-meta.md`](../../wiki/findings/structural-cap-at-score-2-meta.md). The score-2 floor finding cross-cutting P22/P23.
- **Hypothesis**: warm-minus-page agent attempts to reach score < 2.0 on P22 because it doesn't know score 2.0 is the floor.
- **Prediction**:
  - **Score**: variable. Without the structural-cap finding, the agent may either:
    - (a) re-derive the floor from `concepts/coxeter-todd-k12.md` + `findings/p22-d12-construction-survey.md` + `concepts/cohn-elkies-bound.md` (~50% likelihood given those pages also document κ(12) = 840 conjectured tight). Reaches rank #3 same as warm baseline.
    - (b) attempt rank #1 first, burn 5–20 GPU-hours, eventually settle for rank #3 after running into the constructive impossibility. Reaches rank #3 with 5–20× more compute.
    - (c) miss the floor entirely, submit a sub-2 score thinking it's correct (verifier should reject — but if verifier is permissive, this is the "celebrate invalid" failure mode). Probability ~10% with a well-instructed agent.
  - **Pages cited**: warm-minus-page will lean heavily on `findings/p22-d12-construction-survey.md` (which has the 8-way cap argument distributed throughout but not pulled out into a meta-finding). Re-derives the cap from the survey contents.
  - **Re-derivation**: probable but inefficient. The survey has all the ingredients (K₁₂ + P₁₂ₐ + Leech + SDP cluster bound) but doesn't have the snappy "score 2.0 is the floor" framing.
- **Verdict if confirmed (case b)**: the meta-finding is **load-bearing for direction-discipline** — without it, the agent runs longer to reach the same conclusion.
- **Verdict if confirmed (case c)**: catastrophic — the meta-finding is what prevents invalid submissions.
- **Verdict if confirmed (case a)**: meta-finding is a *consolidation* of dispersed evidence, not the unique source. Page is a *redundant accelerator* — useful but not load-bearing alone.

### Experiment 4 — Validity (P9 / `concepts/bourgain-clozel-kahane.md`)

- **Problem**: P9 sign-uncertainty.
- **Page removed**: [`concepts/bourgain-clozel-kahane.md`](../../wiki/concepts/bourgain-clozel-kahane.md). The BCK 2010 floor `S ≥ 0.2025` + the operational rule "below 0.2025 ⇒ verifier artifact."
- **Hypothesis**: warm-minus-page agent celebrates a sub-0.2025 score before the verification check would have caught it.
- **Prediction**:
  - **Score**: depends on which evaluator the agent implements. If correct evaluator (with constraint enforcement) → ~0.318 (matches warm baseline). If buggy evaluator (no constraint enforcement) → sub-0.2025 invalid score.
  - **Pages cited**: agent may cite `findings/verification-patterns.md` *but without the BCK floor concept*, the verification rule's force is reduced — "check against literature bounds" depends on knowing what the bounds are.
  - **Re-derivation**: possible via `source/papers/2017-goncalves-hermite-uncertainty.md` (which does mention the BCK 2010 framing). Warm-minus-page might find this and re-derive the 0.2025 number.
  - **Probability of celebrating invalid score**: 20% (down from 30% in the cold-vs-warm audit, because the verification-patterns finding still exists; the floor itself is the missing piece).
- **Verdict if confirmed**: BCK concept page is **load-bearing for validity** — its removal breaks the closed-form sanity check, but the verification rule still survives via the source paper.
- **Verdict if falsified**: the source paper alone is sufficient — concept page is a redundant distillation.

## What this protocol does and doesn't measure

**Measures**:

- Page-level load-bearing across the four uplift mechanisms.
- Whether agents re-derive removed content from siblings (=> page is a consolidation/accelerator, not a unique-content carrier).
- Whether removal triggers known failure modes (compute waste, direction error, score regression, validity failure).

**Does not measure**:

- Multi-page cumulative effect: removing two pages might compound into a worse outcome than the sum of single-page removals. Future protocol extension.
- Long-tail effects: a page that's load-bearing for an *adjacent* problem (e.g., removing the BCK page might also affect P22 via the d=12 modular-form connection). To measure this, run the same removal across multiple problems.
- Wiki-vs-no-wiki dynamics: this is the cold-vs-warm direction, already covered.

## Cost estimate

Each experiment requires a fresh Claude Code session from a checkpoint. Wall-time per experiment: 1–6 hours depending on the problem's compute envelope. Total for 4 experiments × 3 random seeds = 12 trials, ~3 days of cumulative compute (mostly idle waiting for model token output, not GPU).

Cost is dominated by **agent attention budget**, not compute. The user must run each session manually unless we set up a sandbox.

## Recommended sequencing

If running only one experiment, do **Experiment 3 (P22 / structural-cap-meta)** first. Highest expected information gain:

- Most divergent prediction across cases (a/b/c).
- Direct test of the strongest claim from the cold-vs-warm series ("direction-affecting uplift").
- Failure mode (case c) is catastrophic — has the highest stakes.

If running all four, sequence: 3 → 4 → 2 → 1 (descending stakes). Compute Experiment 1 last because both prediction outcomes (page is redundant, page is a trigger) are merely *interesting*, not load-bearing critical.

## Pre-registration

This document **pre-registers** the experimental predictions above. After the experiments run:

- Each experiment's actual outcome should be appended to the corresponding section as `## Result (YYYY-MM-DD)`.
- The verdict should match one of the pre-registered options or note a third unanticipated outcome.
- If the actual outcome falsifies the prediction, the affected wiki page should be re-evaluated (is the framing wrong? is the page genuinely redundant?).

The pre-registration is the honesty mechanism — without it, post-hoc reasoning would always conclude "the page is load-bearing" because the agent cites at least one related page.

*Last updated: 2026-05-03*
