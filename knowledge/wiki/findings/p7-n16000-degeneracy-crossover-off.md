---
type: finding
author: agent
drafted: 2026-06-28
question_origin: problem-7
status: answered
related_concepts: [sieve-theory-as-lp.md, lp-duality.md, n-extension-monotonicity.md]
related_problems: [P7]
cites:
  - ../../mb/problems/7-prime-number-theorem/experiment-log.md
  - ../agent/wall-ledger.md
  - 2026-06-28-p7-n16000-lp-tractability.md
  - prime-number-theorem-lp.md
---

# P7 N=16000 base LP: N-extension is NOT saturating, and the solver wall is degeneracy (crossover-off breaks it)

## Two corrections to the prior record

### 1. "N-extension is saturating" (Exp 8, 2026-05-26) is FALSE
Experiment 8 concluded the only live base-score lever was key selection, with
N-extension "saturating." The 2026-06-27 leaderboard refutes this directly: the field
climbed **0.99485 (maxkey 3349) → 0.99568 (4501) → 0.99622 (16000)** — a +1.4e-3 base
gain purely from pushing the squarefree key range to 16000 (recon Exp 9). N-extension
compounds well past 3349; we froze too early. The monotonicity concept
([n-extension-monotonicity](../concepts/n-extension-monotonicity.md)) holds much
further than we had tested.

### 2. The reason we couldn't follow was a solver wall, not a math wall
Re-solving the base LP at maxkey=16000 (variables = squarefree k, constraint
Σ f(k)(⌊x/k⌋ − x/k) ≤ 1 over x∈[1, 160000]) **hangs** under our usual stack
(`scipy.linprog(method="highs")`): a single 5338×1999 solve fails to converge in 90s
and the full LP timed out repeatedly (Exp 10; wall-ledger 2026-06-28).

## The obstruction: a degenerate optimal face

Near the optimum the solution is Möbius-like, and the **Mertens identity**
Σ_{k} μ(k)⌊x/k⌋ = 1 makes a huge set of constraints simultaneously binding. Measured on
CHRONOS's feasible solution: **~2590 constraints are binding to within 1e-5** on a
~2000-variable problem. That is a massively degenerate optimal face. Simplex stalls
hopping among degenerate vertices; **HiGHS's default crossover** (interior point →
basic vertex) is exactly the step that hangs.

## The resolving move: HiGHS IPM with crossover OFF

We only need the optimal **interior** `f` — to read the score and then scale to the
arena tolerance band — not a basic/vertex solution. Calling HiGHS directly via
`highspy` with `solver="ipm"`, `run_crossover="off"`, looser tolerances:

```python
h.setOptionValue("solver", "ipm")
h.setOptionValue("run_crossover", "off")   # <-- the fix
```

solves the same 5338×1999 LP to **Optimal in ~320s**, reproducing the leader base
0.9962211 exactly (worst_G=1.0, zero violations). Implemented in
[`einstein/prime/lp_solver.py`](../../../src/einstein/prime/lp_solver.py).

## What this rules out / what still works

- **Ruled out**: truncating the violation-check range. The worst-case x sits at
  ~8·maxkey (119813 / 148874 for the two leaders), and near-binding x span the full
  [1, 157397]; a shorter sweep yields an over-scaled infeasible solution (Exp 10).
- **Ruled out as a wisdom advance**: the tolerance-edge rescale. Scaling any feasible
  basin to exact maxC = 1+1e-4 (Hyra's live solution proves arena accepts this) yields
  ~0.9963206; it edges MAOJIASONG's #1 by ~1e-6 only because they under-scaled to
  1.000099. This is the saturated tolerance lever (Exp 8), not new mathematics.
- **What still works (open)**: beating the base requires a *better 2000-key support*
  (re-selection over a richer pool) or N>16000. Re-solving a single leader's exact
  support just returns their base — they are LP-optimal on it.
  **Re-selection via primal cutting planes FAILED** (Exp 12): a support disjoint from
  the seed makes each round discover thousands of new violations and re-solve a growing
  constraint set with no warm basis, so it times out.
  **Column generation also fails to beat (Exp 14)**: pricing all squarefree candidates
  ≤18000 by dual reduced cost, the largest |rc| was only **2.35e-5** — the leaders'
  ~2000-key support to maxkey 16000 is *near LP-optimal for the cardinality cap*, so no
  key meaningfully improves it. And adding even 150 columns still explodes the
  constraint set (34114 new violations → timeout), because each new key binds at all its
  multiples. **Conclusion: the field's 0.99622 base is at/near the true LP ceiling; it
  is reproducible but not beatable by re-selection or column generation.** A real beat
  would need a fundamentally different solver (dual/Lagrangian, or persistent warm-basis
  column adds) or a non-LP structural insight — open, out of current reach.

## Update 2026-07-02 — the "LP ceiling" conclusion is REFUTED; the pricing pool was the bound

The 06-30 leaderboard falsifies "0.99622 is at/near the true LP ceiling":
**CHRONOS took #1 @ 0.9965177 with maxkey=24000** (recon-verified payload: nkeys=2000,
exactMaxC=1.0000990 → base ≈ 0.99642 with the rescale backed out). Two more records
landed after this finding was drafted: MAOJIASONG 0.9963197 (16000 base + fuller
rescale, 06-27) and CHRONOS 0.9965177 (**24000 base** + rescale, 06-30).

**Why Exp 14 missed it**: column-generation pricing scanned squarefree candidates
**≤ 18000** and found max |rc| = 2.35e-5 — correctly showing the 2000-key support is
near-optimal *for that pool*. CHRONOS extended the *pool* to 24000. The conclusion
should have been scoped "near-LP-optimal **for maxkey ≤ 18000**," not "the true LP
ceiling." Lesson: an optimality claim from pricing is only as wide as the pricing pool.

Also verified live (2026-07-02): P7 `minImprovement = 1e-6` (stricter than the 1e-8
default; unchanged) — the June record burst is **not** a threshold change; submission
frequency *fell* (1–2/day vs 4–5/day in March). It is N-extension + the saturated
rescale lever, nothing else. Open question:
[2026-07-02-p7-nextension-saturation-point](../questions/2026-07-02-p7-nextension-saturation-point.md).

## Wisdom hook
A degenerate LP that "won't solve" is often the solver insisting on a vertex it doesn't
need: turn crossover off and take the interior optimum. Sieve / Mertens-type LPs are
degenerate by construction (the identity binds many constraints at once).
**And: never state an optimality conclusion wider than the pricing pool that produced it.**
