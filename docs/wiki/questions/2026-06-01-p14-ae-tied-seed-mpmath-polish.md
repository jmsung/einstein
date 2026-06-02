---
type: question
author: agent
drafted: 2026-06-01
status: open
asked_by: autonomous_loop_p14_cycle54
related_problems: [14]
related_concepts: [float64-ceiling, basin-rigidity, arena-tolerance-drift, mpmath-ulp-polish]
cites:
  - mb/problems/14-circle-packing-square/solutions/solution-AE-tied-rank2.json
  - docs/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md
---

# Does mpmath-ulp-polish from the AE-tied seed reveal more sub-ulp slack than from our rank-2 seed?

## Background

Cycle 53 ran `mpmath_ulp_polish` from `seeds/p14_canonical.json` (our submitted rank-2,
`2.6359830849175245`) → `2.6359830849175907` (Δ +6.617e-14, triple-verified, dual-gate
arena-f64 ∧ mpmath-exact). The gain is SLSQP line-search residual reclaimed at ulp
resolution.

We also have an archived alternative seed `solution-AE-tied-rank2.json` at score
`2.6359830849176067` — strict-tol-disjoint and ≈ AE submitted #1's score `2.6359830849176`
plus 6.7e-15. The "proximity guard" custom safety rule (not arena-required) blocked its
submission in 2026-04, but the seed itself sits in a strict-tol-feasible coordinate
configuration ~0.16e-12 ulps higher than our rank-2 seed.

## The question

Running `mpmath_ulp_polish --seed solution-AE-tied-rank2.json --dps 80 --max-iter 100`
(or higher dps / max-iter): does the dual-gated ULP coordinate descent reclaim more
sub-ulp radius slack than it did from our rank-2 seed (cycle 53's +6.617e-14), or
hit float64-representability immediately?

If MORE slack is reclaimed, this is evidence that AE's submitted #1 is itself not at
its basin's float64 ceiling — interesting for understanding how arena #1 was
constructed (e.g. is AE submitting line-search-residual scores, not ulp-polished
ones?). Even tiny additional gains stay sub-`minImprovement=1e-7` so submission is
not in scope — this is pure characterisation of the basin's true f64 ceiling.

## Falsifiable answer

A single command + the resulting Σr triple-verified under axiom A1's dual gate. Two
cases:

- **More slack reclaimed (+ε > +6.617e-14)** → AE seed is sub-ceiling; document the
  margin in `findings/p14-ae-seed-not-at-f64-ceiling.md`.
- **Equal-or-less slack reclaimed (+ε ≤ +6.617e-14)** → AE seed IS at its basin's
  f64 ceiling; document as a positive finding about AE's optimizer discipline.

## Why this matters

Generalises beyond P14: the same question applies on every float64-ceiling problem
in the family (P5/P11/P17/P18/P22/P23) where we have an archived AE-tied seed.
Answers feed into a cross-problem finding about "is arena #1 typically ulp-polished
or line-search-residual?".

## Suggested next step

Add a `--seed-name` parameter to `mpmath_ulp_polish.py` (or just override `--seed`
on the command line — the script already accepts `--seed`), run once, triple-verify,
file the finding. ~30s of compute. Not in scope for the cycle-54 autonomous attempt
because the manifest dispatch path uses the canonical seed only.
