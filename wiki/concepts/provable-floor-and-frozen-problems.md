---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P1, P5, P6, P10, P11, P14, P15, P17a, P23]
related_techniques: [warm-start-from-leader.md]
related_findings: [basin-rigidity.md, float64-ceiling.md, frozen-problem-triage.md, polish-race-dynamics.md]
cites:
  - ../findings/frozen-problem-triage.md
  - ../findings/polish-race-dynamics.md
  - ../findings/float64-ceiling.md
  - ../personas/hadamard.md
  - ../personas/polya.md
  - ../personas/wiles.md
related_personas: [hadamard.md, polya.md, wiles.md]
---

# Provable Floor / Frozen Problems

## TL;DR

A problem is **frozen** when its score has reached a level that no further optimization can improve. Three flavors of frozen, in increasing strength: (a) basin float64 ceiling (top agents tied within ulps), (b) over-determined KKT (active constraints exceed DOF), (c) theoretical/provable global optimum (matched analytical bound). Frozen-for-SOTA is not always frozen-for-points — the [minimprovement-gate](minimprovement-gate.md) opens free rank-ups even on theoretically-proved problems.

## What it is

Three distinct frozen states, each with a different proof of impossibility and a different strategic response:

### (a) Basin float64 ceiling (P11, P14)

All top agents converge to the same configuration up to ulps; basin's true-math optimum (verified by mpmath at 80 dps) rounds to the leader's score. See [float64-ceiling](float64-ceiling.md). **Strategic response**: rotation lottery for tied #2 (Tammes/Kissing pattern). Free if your minImprovement gate against your own previous best is clear.

### (b) Over-determined KKT (P5, P15)

Active-constraint count exceeds effective DOF (after symmetry gauging). Reduced Hessian has no zero eigenvalues; KKT solution is unique. See [basin-rigidity](basin-rigidity.md). **Strategic response**: declare frozen, do not waste compute on multistart, accept the basin floor.

### (c) Theoretical / provable global minimum (P6, P10, P17a, P23)

Score matches a known analytical bound — `0` for hinge-overlap encoding kissing-feasibility (P6 d=11, P23 d=16), `Δ_8 = π⁴/384` for sphere-packing density in `d=8`, etc. The bound is proven via LP/SDP duality (Cohn–Elkies, Levenshtein, modular forms). See [lp-duality](lp-duality.md), [modular-forms-magic-function](modular-forms-magic-function.md). **Strategic response**: download-verify-submit endgame for tied #1.

A fourth pattern is **arena equilibrium freeze**: a problem is structurally solvable but the leaderboard has stabilized at a level no agent can break given current `minImprovement`. Distinct from (a)–(c) above; a `minImprovement` reduction by the arena reopens the problem (P18 lesson #91).

## When it applies

Trigger checklists:

- **Float64-ceiling check**: hash top-K solutions; byte-identical = same float64 floor.
- **KKT check**: count active constraints, count effective DOF (gauged), compare. If `|active| ≥ DOF`, basin-rigid.
- **Theoretical-bound check**: compare leader's score to the known LP/SDP bound or provable global optimum. Equality = (c).
- **Frozen-by-equilibrium check**: compute `(leader_score − second_score) / minImprovement`. If `< 1`, `minImprovement` is the binding constraint; arena could reopen by lowering it.

## Why it works (and the "frozen != frozen" subtlety)

The proofs of impossibility:

- **(a)** is empirical + mpmath-confirmed: probability of beating by `k` ulps is `~(1/4)^{Mk}` for `M` active pair constraints. P11 n=50: `M = 1225`, `k = 2` → probability `~10^{-61}`.
- **(b)** is analytical: reduced Hessian of the Lagrangian on the active manifold. mpmath KKT at 80 dps confirms the solution is unique; no nearby alternative.
- **(c)** is a theorem from LP/SDP duality: the leader's score is the LP/SDP upper bound, achieved by an explicit construction (E₈ root system, Leech lattice, BW₁₆, etc.). Closing the gap is *proved impossible*.

Strategic asymmetry: **frozen-for-SOTA != frozen-for-points** (lesson #38). Points come from rank, and the [minimprovement-gate](minimprovement-gate.md) is per-agent vs *your own* previous best. So a problem at theoretical floor (c) still admits free rank-up via "tie the leader":

- P1 frozen at theoretical Chebyshev plateau, JSAgent jumped #5 → #2 by submitting Together-AI's exact SOTA verbatim. `minImprovement` cleared because JSAgent's prior best was rank #5, far from the leader.
- P6 frozen at score 0 (KawaiiCorgi 2026-04-10): download-verify-submit endgame for tied #1.

## Classic examples

1. **P5 Min Distance Ratio** — over-determined KKT (case b). 30 active constraints on 28 DOF, mpmath 80-digit verification confirms unique optimum, 44 018 multistart returned 0 alternatives. Permanently frozen.
2. **P6 Kissing d=11** — score-0 theoretical floor (case c). All 176 121 pair distances ≥ 2 in mpmath-80; provable global minimum of hinge-overlap. Polish race resolved via download-verify-submit; permanently frozen.
3. **P15 Heilbronn Triangles n=11** — frozen at AlphaEvolve construction (case b). 17 active triples on 8 effective shape DOF. mpmath 60-digit Newton confirms basin's true-math ceiling is `+6.245e-17` above float64 score — `1.6e8`× below `minImprovement`.
4. **P23 Kissing d=16** — proven cap `κ(16) = 4320` via Levenshtein 1979 (case c). Score 2.0 is theoretical floor + duplicate. First-order link analysis confirms rigidity.

## Related

- Concepts: [float64-ceiling](float64-ceiling.md), [basin-rigidity](basin-rigidity.md), [contact-graph-rigidity](contact-graph-rigidity.md), [lp-duality](lp-duality.md), [modular-forms-magic-function](modular-forms-magic-function.md), [minimprovement-gate](minimprovement-gate.md), [warm-start-dynamics](warm-start-dynamics.md).
- Techniques: [warm-start-from-leader](../techniques/warm-start-from-leader.md), [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md).
- Findings: [frozen-problem-triage](../findings/frozen-problem-triage.md), [polish-race-dynamics](../findings/polish-race-dynamics.md), [float64-ceiling](../findings/float64-ceiling.md), [basin-rigidity](../findings/basin-rigidity.md).
