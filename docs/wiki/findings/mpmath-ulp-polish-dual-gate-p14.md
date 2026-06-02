---
type: finding
author: agent
drafted: 2026-06-01
question_origin: problem-14
status: answered
related_concepts: [float64-ceiling, arena-tolerance-drift, triple-verify]
related_problems: [14, 5, 11, 17, 18, 22, 23]
cites:
  - scripts/circle_packing_square/mpmath_ulp_polish.py
  - src/einstein/circle_packing_square/evaluator.py
  - docs/wiki/techniques/mpmath-ulp-polish.md
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
  - mb/problems/14-circle-packing-square/experiment-log.md
---

# mpmath ULP-polish needs a DUAL gate (arena-float64 AND mpmath-exact), not exact alone

## The question

When ULP-step coordinate descent proposes a radius-growth move on a packing problem,
what is the correct feasibility gate — the mpmath-exact constraint (`gap ≥ 0` at high
dps), the arena's float64 strict check (`tol=0`), or both?

## What we found

**Both, conjoined.** Gating on mpmath-exact *alone* admits moves the arena rejects, and
gating on float64 *alone* re-opens the tolerance-exploit door. The first kernel on P14
used exact-only and accepted a move whose exact pair gap was ≥ 0 but whose **float64**
distance computation (`np.sqrt((Δx)²+(Δy)²)`, the arena's own arithmetic) showed an
overlap of 5.55e-17. `evaluate_strict(tol=0)` raised on the result — axiom A1 working
as designed. The two evaluators disagree at the 1e-17 scale because float64 `sqrt` and
the subtraction round differently than 100-digit mpmath.

The correct gate:

| Move passes… | float64 strict (arena) | mpmath-exact (≥0) | Verdict |
|---|---|---|---|
| both | ✓ | ✓ | **accept** — real, honest gain |
| float64 only | ✓ | ✗ | reject — exact overlap = the 2026-04-09 tolerance exploit |
| exact only | ✗ | ✓ | reject — arena verifier scores it as overlapping |
| neither | ✗ | ✗ | reject |

## Why it matters (the payoff)

With the dual gate, P14's submitted rank-2 seed (2.6359830849175245) polished to
**2.6359830849175907** — a triple-verified **+6.617e-14** with worst exact pair gap
+1.44e-19 (genuinely disjoint). The gain is SLSQP line-search residual: `slsqp_polish`
at ftol=1e-16 halts sub-ulp short of the basin's true float64 ceiling; discrete ±1/±2
ulp descent that checks the *exact arena constraint per move* reclaims it. Below arena
`minImprovement=1e-7` so not submittable, but it confirms the basin had reclaimable
slack and the body is correct.

## What this rules out / what it enables

- **Rules out**: any ULP / high-precision polisher that trusts a single evaluator. On
  every float64-ceiling packing problem the accept test must run the arena's *own*
  float64 arithmetic as the binding gate, with mpmath as the honesty cross-check — not
  the reverse.
- **Enables**: the body generalizes to the float64-ceiling family — the
  dual-gate accept logic is invariant; only the evaluator import and score
  direction change. **Phase 2a outcome (2026-06-01):** the engine was extracted
  to `src/einstein/ulp_polish.py` and wired to P11 + P5 (both confirmed at the
  float64 ceiling, 0 submittable). The "verbatim to all of P5/P11/P17/P18/P22/P23"
  optimism was **too broad** — the technique has a soundness boundary. It applies
  only to **small-n (n ≲ 50), continuous-objective, strict-feasible-seed**
  problems. Out of scope by construction (not tuning):
  [P18 tolerance-band seed](dead-end-ulp-polish-tolerance-band-seed-p18.md),
  [P17 penalty-shaped score](dead-end-ulp-polish-no-seed-penalty-score-p17.md),
  [P22/P23 O(n²) mpmath at n=841/4321](dead-end-ulp-polish-scale-limit-kissing-p22-p23.md).

## See also

- [dead-end-newton-max-strict-tol-lockout-p14](dead-end-newton-max-strict-tol-lockout-p14.md) — the strict-tol-unsafe optimizer this one replaces.
- [mpmath-ulp-polish technique](../techniques/mpmath-ulp-polish.md) — the procedure; this finding adds the dual-gate refinement for arena-float64-scored problems.
- `src/einstein/ulp_polish.py` — the Phase-2a generic engine extracted from this finding's body.
