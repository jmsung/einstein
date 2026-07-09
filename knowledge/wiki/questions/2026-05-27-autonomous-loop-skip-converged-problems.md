---
type: question
author: agent
drafted: 2026-05-27
status: open
asked_by: autonomous-loop
related_problems: [22, 23, 17]
related_concepts: [first-order-link-tangent-test.md]
related_findings: [structural-cap-at-score-2-meta.md, hinge-overlap-rank3-squeeze.md]
cites:
  - ../findings/structural-cap-at-score-2-meta.md
  - ../findings/hinge-overlap-rank3-squeeze.md
  - ../problems/22-kissing-d12.md
  - ../../../src/einstein/optimizer_manifest.yaml
---

# Should the autonomous loop also skip mathematically-converged problems, not just retired ones?

Sibling question to `2026-05-27-autonomous-loop-skip-retired-problems.md` (retired + no-manifest case). This question covers a different shape: **converged + stub-manifest**.

## The shape

P22 (kissing-d12, n=841) on 2026-05-27, cycle_id=0:

- `knowledge/wiki/problems/22-kissing-d12.md` declares `status: rank-3`, tier A; current score 2.0014030891913.
- `findings/structural-cap-at-score-2-meta.md` proves score < 2.0 ⇔ κ(12) ≥ 841, contradicting the empirical 8-way cap κ(12) = 840 (Coxeter–Todd 756, P₁₂ₐ 840, SDP cluster 840, Leech cross-section 756). Rank-1 mathematically infeasible.
- `findings/hinge-overlap-rank3-squeeze.md` recipe is already optimally tuned (δ=1e-4 lands mid-window between silver and bronze; sub-ulp polish is the only headroom).
- `optimizer_manifest.yaml` has only a **stub_no_op** entry (recon.py --dry-run, no result-file emitter). Dispatch returns `result_file missing` — silent no-op.
- Prior cycle 44 (2026-05-27) outcome: `strategy-picked-no-execution`. This cycle (45+) repeats the same shape because nothing structural has changed.

## Why this is distinct from the retired case

Retired + no-manifest (P17): arena URL returns 404, problem is gone, further compute is purely overhead. Filter is unambiguous: skip.

Converged + stub-manifest (P22): arena URL is live, rank-3 is banked, mathematical proof rules out rank-1. A *real* optimizer wrapper could still squeeze ulps for verification (sub-ulp mpmath polish), but no rank or point gain is achievable. The question is whether "wisdom-via-recompute" justifies an inner-agent budget when the wisdom is already crystallized.

## Proposed filter

In `scripts/autonomous_loop.py` problem-picker:

1. If problem status ∈ {`retired`, `converged`, `rank-3` with `tier: A` and structural-floor proof} AND manifest is stub_no_op, **down-weight to 0.1× base rate** (still run rarely as a regression check, not every cycle).
2. Recompute base rate after Goal 7.6's promotion-candidate detector lands — that may reveal categories of converged problems where re-running pays.

## What the right answer would look like

A small picker tweak that down-weights P22, P17, and the post-retirement P23 to ≈ 0.1× until either (a) a real manifest entry replaces the stub, or (b) new mathematical evidence reopens the problem (e.g. κ(12) ≥ 841 proof — vanishingly unlikely). Evidence: count of `strategy-picked-no-execution` rows in `docs/agent/cycle-log.md` since 2026-05-23 vs `improved-local` rows; if the no-execution ratio > 0.5, the filter pays for itself.

## Suggested sources

- `docs/agent/cycle-log.md` — base rate.
- `scripts/autonomous_loop.py` — picker logic (currently in `_pick_problem` or equivalent).
- `findings/structural-cap-at-score-2-meta.md` — proof that score 2.0 is the floor for P22/P23 class.
