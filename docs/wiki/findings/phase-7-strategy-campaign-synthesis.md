---
type: finding
author: agent
drafted: 2026-06-04
question_origin: leaderboard-points-campaign
status: answered
related_concepts: [autocorrelation-inequality, basin-rigidity, discretization-as-structure, triple-verify, parameterization-selection]
related_problems: [2, 3, 4, 7, 10, 12, 13]
cites:
  - ./dead-end-auto-submit-direction-sign.md
  - ./dead-end-p2-compact-support-basin-floor.md
  - ./p12-grid-drift-resolution.md
  - ./dead-end-p3-antialias-transplant-fails.md
  - ./dead-end-p4-organon-floor-negative-content-lever.md
  - ./p10-wales-global-min-hessian-certificate.md
  - ./p7-p13-scoping-required-conditions.md
---

# Phase 7 strategy campaign — synthesis (the first real shot at records)

Phase 7 (`js/feat/strategy-attempts-headroom`) ran the optimisers against the
headroom targets for the first time. **Arena records reclaimed: zero.** But the
honest-zero is decisive, not a shrug — each target is now characterised, and the
campaign produced one safety-critical fix plus four reusable artifacts.

## The headline: a safety bug that had already fired
Before any optimiser ran, the auto-submit log showed the loop had submitted a
*worse* P2 score as a "new record" twice that morning — the gate defaulted to
maximise and never received per-problem direction
(`dead-end-auto-submit-direction-sign`). Four of five targets minimise, so the
bug would have recurred on each. Fixed (canonical `PROBLEM_MINIMIZE` map +
fail-closed caller + regression tests) before running the campaign. **This alone
justified the branch** — running it with the bug live would have spammed
wrong-direction submissions.

## Per-target outcome (all honest-zero, all characterised)

| target | direction | result | why no record |
|---|---|---|---|
| **P2** first-autocorr | min | floor-confirmed | leaders' basin is *compact-support*; ours is *full-support* — distinct. Polishing the leader's own solution gains only 2.6e-10 |
| **P3** second-autocorr | max | transplant dead | the quadratic ★ injects above-Nyquist energy; no anti-aliased downsample of our 1.6M solution survives to 100k (best 0.9596 < SOTA 0.9626) |
| **P4** third-autocorr | min | floor-confirmed | family-twin of P2; leader uses more negative content (27.5% vs our 23.6%); its basin polishes to itself |
| **P10** thomson-n282 | min | global-min certified | projected Hessian: 3 rotational zero modes + 561 positive eigs (λ_min gap 3.41); six agents tied |
| **P12** flat-polynomials | min | tied-SOTA, drift resolved | continuous-sup certifier (1.2809320528750) dissolves the ~7e-10 grid drift; search re-finds the SOTA basin |
| **P7** prime-number-thm | max | deferred | real 5.35e-5 gap; needs a constrained-certificate LP, different protocol |
| **P13** edges-triangles | max | deferred | arena proximity guard blocks our 2e-6 edge; needs ≥1e-5 over the whole cluster |

## The unifying wisdom
1. **The gaps were not polish gaps — they were basin / comparability / policy.**
   P12 was sampling noise (drift), P3 a resolution artifact, P2/P4 distinct
   basins, P10 the proven global min, P13 an arena policy. None was "optimise
   harder." This is the campaign's central lesson: *a leaderboard gap is a
   question about what KIND of difference it is, before it is an optimisation
   target.*
2. **The P2/P4 family lever: push f to its feasible boundary.** OrganonAgent holds
   both twins by driving more of f to the constraint edge than the symmetric
   equioscillation basin — P2 to exactly zero (compact support), P4 to negative
   (cancellation). Our basins stop short on both; that shortfall *is* the gap.
3. **Three of five targets were gated by score-comparability, not search** (P2
   normalisation, P3 resolution, P12 grid). The right first move on a discretised-
   functional problem is to pin the comparability, not to launch a search.

## Reusable artifacts produced
- **Continuous-sup certifier** (`flat_poly.continuous_sup_score`) — grid-
  independent score via exact trig-polynomial Newton; dissolves grid drift for
  any `max|p|` problem.
- **Projected-Hessian floor certificate** (P10) — second-order strict-local-min
  test for sphere-constrained energies; replaces perturbation lotteries.
- **Cross-resolution agreement predicate** (stated) — the gate-2 prerequisite for
  any P3/P4 submission (reject scores that rise under re-discretisation).
- **Live basin-structure download+compare** — the cheapest-decisive recon move
  (support fraction / negative fraction vs the leader) that resolved P2/P4/P10 in
  minutes instead of multi-hour searches.

## Next-phase decision
**Do NOT re-enable Phase 4's steady-state launchd loop on these targets.** It is
now *safe* (gate fixed) but would burn compute re-confirming floors — all five
are at parity-or-floor under current technique. New records need new
*construction* methods, not more iterations:

- **Phase 8 candidate A (highest value):** promote the two certificates into the
  triple-verify layer as reusable components, and wire the cross-resolution
  agreement predicate into gate 2 for the autocorrelation family — turning this
  campaign's wisdom into standing infrastructure.
- **Phase 8 candidate B (research):** construction-search for new basins —
  compact-support-targeting for P2, signed-Chebyshev for P4, 100k-native
  Dinkelbach for P3 — explicitly low-EV; pursue only as a learning exercise.
- **Phase 8 candidate C (cheap rank points):** the two human-approval submissions
  this branch surfaced — P10 Wales-seed swap (worse #6 → tied #1) — pending
  human sign-off (tied-SOTA, not auto-submittable).

Recommendation: **A**, then revisit B/C. The campaign's value was wisdom +
safety, exactly as the repo's "math wisdom, not arena rank" goal intends.
