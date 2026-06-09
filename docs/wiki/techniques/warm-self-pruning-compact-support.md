---
type: technique
author: agent
drafted: 2026-06-08
related_problems: [2, 3, 4]
related_concepts:
  - parameterization-induced-rank-deficiency
  - autocorrelation-inequality
  - n-agent-tie-not-global-min
compute_profile: [local-cpu]
cost_estimate: "~10 min single warm chain at n=90000; multiprocess over warm-starts"
hit_rate: "1/1 (P2 arena record, 2026-06-08)"
status: validated
cites:
  - ../findings/p2-warm-self-pruning-beats-record.md
  - ../findings/p2-peak-locking-hessian-mechanism.md
  - ../findings/dead-end-p2-cold-seed-fixed-window.md
  - ../../scripts/first_autocorrelation/self_pruning_search.py
  - ../../src/einstein/first_autocorrelation/optimizer.py
---

# Warm data-driven self-pruning for compact-support optima

## TL;DR

When the SOTA for a non-negativity-constrained problem has **exactly-zero cells**
(compact support), reach a better basin by: **warm-start from a near-converged
full-support solution → iteratively zero the smallest-magnitude cells (the optimizer
chooses which, not a pre-imposed window) → re-optimize under the `f = v²`
parameterization, letting peak-locking drive cells to exact zero → repeat, shrinking
support toward the SOTA's support count.** This broke a 2-agent tie on P2 and set a
new arena record (1.5028609 → 1.5028506).

## When to use

All three must hold:

1. **Non-negativity constraint** (`f ≥ 0`) so cells *can* sit at exactly zero.
2. **The empirical SOTA has compact support** — count its zero cells; if > 0, the
   optimum lives in a compact-support basin
   ([parameterization-induced-rank-deficiency](../concepts/parameterization-induced-rank-deficiency.md)).
3. **You can reach a competitive *full*-support basin warm** (block-repeat coarse→
   fine, or a public seed). Cold smooth-bump seeds do NOT work — they stall ~1.5%
   high ([dead-end-p2-cold-seed-fixed-window](../findings/dead-end-p2-cold-seed-fixed-window.md)).

Autocorrelation family (P2/P3/P4) is the canonical fit; the Hessian mechanism is
verified objective-shape-agnostic on P2/P3.

## The recipe

1. **Parameterize `f = v²`** (not `exp(v)`). Only `v²` has `φ''(0)=2`, which keeps
   Hessian curvature on the dead-cell subspace so the optimizer gets a finite KKT
   signal at `v=0` and can decide to keep a cell dead. `exp(v)` hides this behind an
   exponential asymptote and can never reach exact zeros. (The whole mechanism:
   [p2-peak-locking-hessian-mechanism](../findings/p2-peak-locking-hessian-mechanism.md).)
2. **Warm start.** Load a near-converged full-support solution; `v = sqrt(f)`.
3. **Prune data-driven, not geometric.** Zero the `k` smallest-|v| *currently active*
   cells (`prune_smallest`). Crucial: let the optimizer's own magnitudes pick which
   cells die. A pre-imposed contiguous window is strictly *worse*
   (P2: +0.336 vs the record) — the leaders' support is fine-structured, not an
   interval.
4. **Re-optimize** with a full smooth-max β-cascade L-BFGS (`lbfgs_vsq`), warm-started
   from the current `v`. Masked cells are exact-zero gradient fixed points, so support
   only shrinks.
5. **Shrink on a schedule** (geometric, finer near the target) down to the SOTA's
   support count. Track the arena-exact score per level; the signature of a genuine
   better basin is **C monotonically decreasing** as support shrinks (a discretization
   spike would not behave this way).

## Implementation

- Primitives in [`optimizer.py`](../../src/einstein/first_autocorrelation/optimizer.py):
  `vsq_from_f`, `prune_smallest`, `self_pruning_search` (with an `on_level` streaming
  callback), reusing `surrogate_vsq` / `lbfgs_vsq` / `score_vsq_masked`.
- Entry point [`self_pruning_search.py`](../../scripts/first_autocorrelation/self_pruning_search.py):
  multiprocess over warm-starts, 1 BLAS thread/worker (A4), live per-level logging.
- Compute: sequential L-BFGS ⇒ **local CPU**; GPU sits idle. ~10 min per warm chain
  at n=90000.

```
uv run python scripts/first_autocorrelation/self_pruning_search.py \
  --warmstarts <full-support-basin.json> --steps 6 --floor-support <SOTA-support>
```

## Verification discipline

A record that overturns an N-agent-tie prior is an extraordinary claim — verify before
trusting (it could be evaluator drift, the P9/P14/P17 pattern). The checks that
confirmed P2: (1) evaluator = verbatim arena code; (2) **calibrate it on the leader's
own solution** — it must reproduce their published score to the digit; (3) threshold-
robustness — clip near-zero cells and confirm C still beats SOTA (rules out filler-
gaming); (4) no proven bound violated. See
[p2-warm-self-pruning-beats-record](../findings/p2-warm-self-pruning-beats-record.md).

## What this opens

- **Direct transfer to P3 / P4** — same family, same compact-support leaders, mechanism
  already verified on P3. Warm-self-prune from our full-support basins there.
- A general move for any compact-support extremal problem: don't *impose* the support
  geometry, *discover* it by data-driven pruning under a `φ''≠0` parameterization.
