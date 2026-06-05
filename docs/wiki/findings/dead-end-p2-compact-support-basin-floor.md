---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-2
status: answered
related_concepts: [autocorrelation-inequality, equioscillation, parameterization-induced-rank-deficiency, triple-verify]
related_problems: [2]
cites:
  - ../problems/2-first-autocorrelation.md
  - ../findings/autocorrelation-family-displaced-2026-06.md
  - ../findings/p2-peak-locking-hessian-mechanism.md
  - scripts/first_autocorrelation/exact_polish.py
  - src/einstein/first_autocorrelation/evaluator.py
---

# Dead end: P2 polish can't reclaim rank #1 — the leaders' basin is compactly supported and at its floor

## What we tried
P2 (`min C = max(f★f)/(∫f)²`) was the branch's tightest gap (+1.84e-7) and the
best polish-shaped reclaim candidate. Plan: re-run the v² parameterization +
larger-n cascade to beat arena #1 (OrganonAgent 1.5028609073611). First did the
council's cheapest-decisive checks: (1) verify our recoverable seeds, (2)
download the leaders' live solutions and compare basin structure, (3) polish the
leader's own solution to probe the basin floor.

## Why it failed (the obstruction)
**Our basin and the leaders' basin are structurally different points, and the
leaders' basin is already at its floor.**

Downloaded the live P2 leaderboard (`check_submission.check_leaderboard(2)`) and
re-scored each solution with the canonical evaluator:

| solution | n | nonzero cells | support frac | score |
|---|---|---|---|---|
| OrganonAgent #1 | 90000 | 74489 | **0.828 (compact)** | 1.5028609073611 |
| CHRONOS #2 | 90000 | 74489 | **0.828 (compact)** | 1.5028609073612 |
| JSAgent #3 (ours) | 90000 | 89963 | **1.000 (full)** | 1.5028610916080 |

Two observations:

1. **OrganonAgent and CHRONOS are bit-identical in structure** (same 74489
   nonzero cells, same max 0.00382) and tied to 1e-13. Two independent agents at
   the same compactly-supported configuration → this is a genuine basin floor,
   not a one-agent artifact.
2. **Their basin has ~17% of cells exactly zero (compact support); ours has full
   support.** Polishing our full-support basin cannot cross into their
   compact-support basin — they are different optimisation geometries, not the
   same basin at different polish depths. This is why our −1.84e-7 gap never
   closed by "polish harder": it was never a polish gap.

3. **Polishing the leaders' OWN solution confirms the floor.** Ran
   `exact_polish.py` (KKT-consistent exact-max gradient, 2000 iters) warm-started
   from OrganonAgent's #1. It converged (line-search stall at iter 183) to
   **1.5028609071045573** — a Δ of only **2.57e-10** below arena #1, triple-verified
   (fast/exact/cross 3-way agreement to 16 digits). That is **25× below
   minImprovement (1e-8)** — the compact-support basin is essentially at its
   minimum; not even starting from the leader's exact point yields a submittable
   record.

## What this rules out
- **Reclaiming P2 rank #1 by polishing our basin.** The reachable improvement is
  ~1e-10, two orders below the submission threshold. Full-support → compact-
  support is a basin change, not a polish.
- **The "v² escape ⇒ rank #1" narrative.** Our wiki credited v²-parameterization
  escape for the rank-1 win, but our actual surviving seed is *full support*
  (89963/90000 nonzero). The escape the leaders used is the **dead-cell /
  compact-support** mechanism (`p2-peak-locking-hessian-mechanism`,
  `parameterization-induced-rank-deficiency`) — and we are in the basin that did
  *not* take it. The mechanism is correct; we simply never reached the
  compact-support basin with a surviving seed.

## What might still work
- **Target compact support directly.** Re-optimise with a support-shrinking
  schedule or a compact-support initialisation (e.g. zero the outer ~17% of
  cells and re-run the v² L-BFGS), aiming for an *even lower* compact-support
  basin. Low EV: two independent agents tied to 1e-13 strongly implies this is
  the continuous infimum at n=90000, so a ≥1e-8 improvement is unlikely. A
  Cohn-style dual lower-bound certificate (Q
  `2026-06-04-p2-headroom-cohn-dual-certificate-floor`) would decide whether
  1.5028609074 is provably the floor.
- **Honest-zero is the outcome.** We hold our best-ever P2 artifact (the polished
  1.5028609071 in `mb/.../solutions/solution-organon-polished-…`), but it is not
  submittable (Δ < minImprovement) and would be a tied-basin squeeze requiring
  human approval regardless. P2 is closed as floor-confirmed for this branch.
