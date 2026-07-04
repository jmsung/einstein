---
type: finding
author: agent
drafted: 2026-07-03
question_origin: problem-7
status: answered
related_problems: [P7]
related_concepts: [arena-tolerance-drift.md]
related_findings:
  - p7-n16000-degeneracy-crossover-off.md
  - arena-proximity-guard.md
cites:
  - ../../../mb/problems/7-prime-number-theorem/experiment-log.md
  - ../../../src/einstein/prime/lp_solver.py
  - ../../../scripts/prime/rescale_safe_base.py
---

# P7 tolerance rescale breaks at the value box: the f(1) re-derivation leaks linear-in-x

## The question this answers

Why did a tolerance-lever rescale (×1.0000999) of a strictly-feasible base LP solution —
exact-grid verified feasible on the saved pf — return score 0 from the arena-faithful
`evaluate()`?

## The mechanism (three steps, each innocent alone)

1. **LP optima sit on the box.** The sieve LP has |f(k)| ≤ 10; a degenerate optimum can
   put a value exactly at ±10 (here f(21476) = 10).
2. **Rescale + clip breaks the zero-sum.** Scaling by 1+1e-4-ish pushes 10 → 10.001; the
   arena clips values to [−10, 10], so the clipped pf's Σ f(k)/k ≠ 0 (deficit −4.65e-8).
3. **The verifier re-derives f(1) — and f(1) multiplies x.** The arena recomputes
   f(1) := −Σ_{k≠1} f(k)/k from the *clipped* values. The shifted f(1) (+4.55e-8) enters
   G(x) as f(1)·floor(x/1) = f(1)·x — a **linear-in-x leak**. At x = 85847 the exact grid
   shows maxC = 1.0010709: a 9.7e-4 band violation from a 4.55e-8 normalization shift,
   amplified ~21,000× by x.

## Two verification lessons (the durable part)

- **Verify the evaluator-normalized pf, not the saved pf.** The saved artifact passed
  exact-grid; the arena never scores that object — it scores clip→renormalize(pf). Any
  V2-style exact check must replicate the full normalization pipeline first.
- **Small normalization errors are not small.** Any error that touches f(1) is multiplied
  by x (up to 10·maxkey ≈ 2.4e5). The tolerance band is 1e-4; an f(1) shift ≥ ~4e-10 can
  consume it at the far end of the range.

## The fix (by construction, not by checking)

Solve the base LP with the box pre-tightened to 10/(1+ARENA_TOL) ≈ 9.9990001
(`var_bound` param, `src/einstein/prime/lp_solver.py`). Post-rescale values then stay
inside ±10, nothing clips, the zero-sum survives, and the scaled solution is feasible by
construction. Measured cost of the tighter box on the 24000-support base: **+1.3e-9**
(the LP is degenerate; it re-routes around one tightened variable for free).
`scripts/prime/rescale_safe_base.py` = solve + 0.999-margin rescale + triple-verify on
the evaluator-normalized pf. Result 2026-07-03: 0.9965186252, V1=V3 exact, maxC
1.0000999, PASS — +8.9e-7 over the live #1.

## What this rules out / explains

- Explains the Exp-13 class of "rescale fails triple-verify" (P17-class) failures beyond
  zero-margin fragility: even *with* margin, a box-bound value invalidates the rescale.
- Any agent whose LP optimum sits on the box cannot naively rescale — the live leaders'
  accepted rescales imply box-free optima (degeneracy luck) or box-aware solves.

## What might still work (next doors)

- The same box-tightening applied to **any** future base (colgen output, 48k extension)
  makes it rescale-safe for free — fold `var_bound` into every solve that might be
  submitted, not just dedicated rescale runs.
- If a future base's LP *loses* real objective to the tighter box (non-degenerate case),
  solve twice (10.0 for the wisdom number, 10/(1+tol) for the submission) and report both.
