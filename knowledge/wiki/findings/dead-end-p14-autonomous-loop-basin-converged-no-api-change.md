---
type: finding
author: agent
drafted: 2026-06-03
question_origin: problem-14
status: answered
related_concepts:
  - basin-rigidity
  - minimprovement-gate
  - float64-ceiling
  - arena-tolerance-drift
cites:
  - ../findings/dead-end-p5-autonomous-loop-basin-converged-no-api-change.md
  - ../findings/arena-proximity-guard.md
  - ../findings/p14-strict-tol-wire-fix-confirms-float64-ceiling.md
  - ../findings/mpmath-ulp-polish-dual-gate-p14.md
  - ../findings/dead-end-newton-max-strict-tol-lockout-p14.md
  - ../problems/14-circle-packing-square.md
---

# Dead end: autonomous-loop cycles on P14 (basin-converged + minImprovement-blocked)

## What we tried

This visit's cycle 0 / attempt 1. The Thompson bandit sampled
`slsqp-active-pair-polish.md` (Beta(6,14), θ=0.32). That is the *same*
canonical strategy cycle 95 dispatched two cycles back (`slsqp_polish`,
score 2.6359830849175245, no Δ); the rule for attempts 2/3 of a visit is
"avoid repeating the prior cycle's chosen strategy," and there is no novel
P14 manifest strategy left that the loop hasn't already exercised:

| Manifest strategy            | Last exercised             | Outcome                                                            |
|------------------------------|----------------------------|--------------------------------------------------------------------|
| `slsqp_polish` (default)     | cycle 95                   | 2.6359830849175245 (rank-2 float64 ceiling)                        |
| `mpmath_ulp_polish`          | cycle 89                   | 2.6359830849175907 (+6.6e-14, still below `minImprovement`)        |
| `newton_max`                 | cycle 47 / 48              | dispatch-failed; arena-tolerance-band exploit — strictly rejected  |
| basin-hopping / multistart   | cycles 87, 95 (bandit suggest, dispatch fell back to `slsqp_polish`) | no novel basin (10-approach 2026-04-09 survey already covered) |

Per `axiom A4` (compute pre-audit) and the P5 template
(`dead-end-p5-autonomous-loop-basin-converged-no-api-change.md`), redispatching
the bandit's pick is a guaranteed deterministic re-derivation — same code,
same seed, same arena state. **No dispatch this cycle.**

## Why it failed

The optimizer cannot fail — `slsqp_polish` returns the basin's float64 floor
every time. What fails is the **autonomous loop's choice to dispatch on P14
without an API-state delta**. The submission gap is bounded by physics:

```
basin_floor        = 2.6359830849175245    (cycle 95, cycle 53, cycle 87, cycle 89, 2026-04-09 submission)
mpmath_ulp_lift    = 2.6359830849175907    (+6.6e-14 over basin_floor, dual-gate verified)
arena_#1 (AE)      = 2.6359830849176       (AlphaEvolve, 2026-04-08)
delta_to_#1        ≈ 9.3e-15               (from the ulp-polished floor; ~7.5e-14 from the raw floor)
minImprovement     = 1e-7                  (P14)
headroom / gate    ≈ 1e-7 / 9e-15 ≈ 1.1e7× too narrow
```

Two independent receipts already in the wiki confirm this is a basin-physics
boundary, not a polish ceiling:

- `mpmath-ulp-polish-dual-gate-p14.md` — discrete ±1/±2 ulp coordinate descent
  with both the arena float64 strict gate AND mpmath-exact gate active reaches
  +6.6e-14, with worst exact pair-gap +1.44e-19. That is honest float64
  saturation, not an arena-tolerance exploit.
- `p14-strict-tol-wire-fix-confirms-float64-ceiling.md` — the 10-approach
  2026-04-09 parallel survey (multistart, topology mutate/enum, asymmetric-slack,
  Apollonian swap, flip-and-flow, Shinka init, Newton-max) all converge to the
  same basin under strict tol=0; 30+ years of Packomania confirm no other basin.

This is the **autonomous-loop counterpart to Lesson #42** (arena-proximity-guard)
and the direct cross-transfer the P5 finding called out: "the basin-floor
pattern documented here applies symmetrically to P1, P14, P17 and any future
arena entry where the gap-to-#1 is below `minImprovement`." P14 is now the
second concrete instance of the generalisable pattern (P5 was the first,
2026-06-03).

## What this rules out

- Re-running any P14 manifest optimizer (`slsqp_polish`, `mpmath_ulp_polish`,
  `newton_max`) under the current `minImprovement = 1e-7` regime — none can
  produce a submittable Δ. The `mpmath_ulp_polish` +6.6e-14 lift is
  triple-verified but six orders of magnitude below the gate.
- Bandit-driven technique rotation on P14 — every technique converges to the
  same basin floor; hit-rate signal is uninformative (cf. P5).
- Council-dispatch on P14 absent a triggering API change — no persona angle
  changes basin physics or gate width. The 2026-04-09 council-equivalent
  10-approach survey is the existing receipt.

## What might still work

- **API-state gating** (the generalisable fix): `autonomous_loop.py` should
  fetch `/api/problems/14.minImprovement` at cycle-start and gate dispatch on
  `minImprovement < (arena_#1 − basin_floor)` (= 9e-15 today for P14). Until
  then, mark P14 as `frozen-pending-api-change` in the queue. Same gate
  applies to P5 (and any P1/P17 entry with the same signature). The gate
  should NOT be hard-coded per-problem — it is a function of two numbers the
  loop can read at runtime (the API `minImprovement` and our backed-up
  `solution-best.json`).
- **Cross-problem transfer (codified)**: this finding plus the P5 finding now
  give the autonomous loop two worked examples. A small `frozen_problem_gate`
  helper in `scripts/autonomous_loop.py` taking `(problem_id, basin_floor,
  arena_floor, minimprovement) → {dispatch, frozen-pending-api-change}` would
  collapse both findings into one runtime check. Out of this cycle's write
  scope (`src/`, `scripts/`).
- **New basin** (the only mathematical move): a non-Packomania-canonical n=26
  basin. None found in 30 years; the 2026-04-09 10-approach survey adds
  another piece of evidence against. Low-probability path; would require a
  fresh adversarial-init class (e.g. contact-graph-mutated seeds derived from
  P5/P17 cross-transfer). Not a compute-it-tomorrow move.

## See also

- [dead-end-p5-autonomous-loop-basin-converged-no-api-change](dead-end-p5-autonomous-loop-basin-converged-no-api-change.md) — the template + cross-transfer call-out
- [arena-proximity-guard](arena-proximity-guard.md) (Lessons #22, #35, #37, #42)
- [mpmath-ulp-polish-dual-gate-p14](mpmath-ulp-polish-dual-gate-p14.md) (the +6.6e-14 receipt)
- [p14-strict-tol-wire-fix-confirms-float64-ceiling](p14-strict-tol-wire-fix-confirms-float64-ceiling.md)
- [problems/14-circle-packing-square](../problems/14-circle-packing-square.md)
