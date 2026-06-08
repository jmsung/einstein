---
type: finding
author: agent
drafted: 2026-06-08
question_origin: problem-2
status: answered
related_problems: [2]
related_concepts: [autocorrelation-inequality, parameterization-induced-rank-deficiency]
related_findings:
  - dead-end-p2-compact-support-basin-floor.md
  - p2-peak-locking-hessian-mechanism.md
  - p2-record-gate-no-cheap-certificate.md
cites:
  - ../findings/dead-end-p2-compact-support-basin-floor.md
  - ../findings/p2-peak-locking-hessian-mechanism.md
  - scripts/first_autocorrelation/compact_support_search.py
  - src/einstein/first_autocorrelation/optimizer.py
---

# Dead end: cold-seed v² L-BFGS (full or fixed compact window) can't reach the competitive P2 basin

## What we tried

Goal 1 built the compact-support-targeting search the branch envisioned: contiguous
**window mask** (`f = mask · v²`, support compact by construction) + **cold-seed
multistart** (smooth bumps — cos/parab/gauss/uniform/bimodal — NOT warm-started
from our full-support basin), over a support-width schedule. Code:
[`compact_support_search.py`](../../scripts/first_autocorrelation/compact_support_search.py),
primitives in [`optimizer.py`](../../src/einstein/first_autocorrelation/optimizer.py).

Diagnostic at the real grid n=90000, full β-cascade to 1e13, 3000 L-BFGS iters
(~10 min/task), one cold cos seed per width:

| width | support frac | cold-seed C | vs arena #1 (1.5028609073611) |
|---:|---:|---:|---:|
| 90000 | 1.000 (full) | **1.5252031** | +0.0223 |
| 74493 | 0.8277 (leader width) | **1.8386484** | +0.336 |

(Smaller-budget probe — 600 iters, β≤1e11 — gave 1.5745 / 1.7267 / 1.8752 for
w=90000 / 81000 / 74493: same ordering, worse from under-convergence.)

Triple-verified 3-way at 4.4e-16 agreement, so the scores are real.

## Why it failed (the obstruction)

**Cold smooth-bump seeds land in shallow basins ~1.5% above the competitive
region, and a fixed narrow window is strictly worse than full support.**

1. **Cold seeds don't reach even our own basin.** Our existing 1.5028610916 basin
   was reached by *warm-starting* from block-repeated coarser solutions
   (30k→90k) plus extensive optimization. A single cold bump, even with the full
   β-cascade, stalls at 1.5252 (full support) — a 0.022 gap. The competitive basin
   is not reachable from a cold smooth seed; it requires the coarse-to-fine warm
   structure. Adding more cold seeds of the same quality cannot close a 1.5% gap
   to reach a sub-1e-8 record — this is a wrong-regime failure, not a
   need-more-samples failure.

2. **A fixed compact window is worse, not better.** Forcing a smooth bump onto a
   narrower window (74493 cells) converges to 1.8386 — far above full support.
   Compact support is *not* achieved by pre-masking a contiguous interval and
   optimizing a bump inside it. The leaders' 74489-nonzero configuration is not a
   smooth bump on a sub-interval; it has fine structure.

3. **The mechanism mismatch.** The leaders' compact support almost certainly arose
   from **peak-locking / self-pruning** ([p2-peak-locking-hessian-mechanism],
   [parameterization-induced-rank-deficiency]): during v² optimization of a
   near-converged full-support solution, the Hessian drives a subset of cells to
   exactly zero (v=0 is a gradient fixed point). That is a *different* operation
   from "pre-mask a window, then optimize a cold bump." Our build implemented the
   latter; the basin lives behind the former.

## What this rules out

- **Cold-seed-on-fixed-window as a route to the compact-support basin.** Both
  pieces fail: cold seeds are too shallow, fixed windows are worse than full.
- **"More seeds / more widths overnight will find it."** The best cold case is
  +0.022 above arena #1; the gap is structural, not statistical. A multi-day cold
  run would confirm honest-zero at high cost — the wall-hit anti-pattern.

## What might still work

A **self-pruning support-shrinking schedule**, warm not cold:
1. Reach a near-converged *full-support* solution (warm: block-repeat coarse →
   fine, as our 1.5028610 basin was found).
2. Progressively zero the *smallest* cells (let the optimizer choose which — not a
   pre-imposed contiguous window) and re-optimize with v² L-BFGS, allowing
   peak-locking to set in.
3. Repeat, shrinking support toward ~74489, watching whether C drops below
   1.5028609073611 − 1e-8.

This reconciles the tension between two established dead-ends:
[dead-end-p2-compact-support-basin-floor] (pure polish can't *change* support) and
this finding (cold seeds can't reach competitive scores). The viable path is warm
enough to be competitive **and** actively shrinking support — which contradicts
Goal 1's "not warm-started from our full-support basin" stipulation, so it is a
**revise of the goal**, surfaced to the human.

## Confidence

- High on the numbers (n=90000, triple-verified 4.4e-16).
- High on "cold-seed wrong regime" — two budgets, consistent ordering, 0.022 gap
  to our own basin.
- Medium on the self-pruning prescription — it is the mechanism the findings
  attribute to the leaders, but unproven by us that it crosses below the record.
