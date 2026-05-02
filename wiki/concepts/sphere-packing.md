---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P5, P6, P10, P11, P14, P17a, P17b, P22, P23]
related_techniques: [slsqp-active-pair-polish.md, parallel-tempering-sa.md, mpmath-ulp-polish.md, basin-hopping-multistart.md]
related_findings: [packing-techniques.md, basin-rigidity.md, float64-ceiling.md, sa-parallel-tempering.md]
cites:
  - ../source/papers/1971-leech-sphere-packing.md
  - ../source/papers/1959-barnes-wall-lattice.md
  - ../source/papers/2024-cohn-li-kissing.md
  - ../source/papers/2024-delaat-kissing-sdp.md
  - ../source/blog/cohn-kissing-numbers.md
  - ../source/blog/friedman-packing-records.md
---

# Sphere Packing

## TL;DR

Sphere packing asks: how densely can equal-radius spheres tile `ℝᵈ` (or fit in a bounded region)? Optimal density `Δ_d` is known exactly only for `d ∈ {1, 2, 3, 8, 24}` (Viazovska 2016; Cohn–Kumar–Miller–Radchenko–Viazovska 2017). Most arena geometric-packing problems (P14, P17a, P17b) are *bounded-region* packings — Packomania-style records — while kissing problems P6, P11, P22, P23 are *local-density* (kissing-number) packings.

## What it is

Two formulations:

- **Lattice / infinite-density packing in `ℝᵈ`**: density `Δ = lim_{R → ∞} (vol(B_R ∩ packing) / vol(B_R))`. Optimal in `d = 1` trivially, `d = 2` hexagonal (Thue 1910), `d = 3` FCC (Hales 1998), `d = 8` E₈ (Viazovska 2016), `d = 24` Leech (Cohn–Kumar–Miller–Radchenko–Viazovska 2017; see `source/papers/1971-leech-sphere-packing.md`).
- **Bounded-region packing**: pack `n` disks/spheres in a fixed container (square, rectangle, hexagon, sphere) maximizing some functional (sum of radii, minimum gap, count for fixed radius). Reference databases: Packomania (Specht), Friedman's packing records (`source/blog/friedman-packing-records.md`), Hardin-Sloane (sphere codes).

The **kissing variant** (`κ(d)`, see [kissing-number](kissing-number.md)) is a local-density question: how many `d`-spheres can simultaneously touch one. Different from infinite-density but sharing tools (LP/SDP bounds, lattice constructions, Cohn–Elkies duality).

## When it applies

Concept umbrella for:

- **Geometric packing problems** (P5 min-distance ratio, P14 circles-in-square, P17a hexagon, P17b circles-in-rectangle) — bounded-region, finite `n`, contact-graph-rigid.
- **Sphere code problems** (P10 Thomson, P11 Tammes) — points on a sphere maximizing minimum pairwise distance / minimizing Coulomb energy.
- **Kissing problems** (P6 d=11, P22 d=12, P23 d=16) — see [kissing-number](kissing-number.md).
- **Magic-function existence** (Viazovska): when an explicit modular-form construction matches the LP upper bound, the bound is tight and density is solved.

## Why it works (the unifying machinery)

Three load-bearing concepts power all sphere-packing work in this codebase:

1. **Cohn–Elkies LP upper bound** (`source/papers/2024-cohn-li-kissing.md`). For density: minimize `f(0) / f̂(0)` over Schwartz `f` with `f(x) ≤ 0` for `‖x‖ ≥ 1` and `f̂(ξ) ≥ 0`. Strong duality says any feasible `f` gives an upper bound. See [lp-duality](lp-duality.md).
2. **Magic functions via modular forms** (Viazovska 2016 for `d = 8`; CKMRV 2017 for `d = 24`). Construct `f` as `(1 − ‖x‖²)`-times a Laplace transform of a quasimodular form; verify positivity by Eisenstein-series computation. The function *exists* because of unique modular structure in `d = 8, 24`. See [modular-forms-magic-function](modular-forms-magic-function.md).
3. **Contact graph + rigidity**. For finite-`n` arena packings: count active touching pairs (contact graph edges) vs DOF. Over-determined ⇒ basin-rigid; multistart wasted; KKT solution unique. See [contact-graph-rigidity](contact-graph-rigidity.md), [basin-rigidity](basin-rigidity.md).

The arena practitioner's trio:

- **Hardin-Sloane / Packomania reference** before optimizing — saves hours.
- **SLSQP active-pair polish** with wide tolerance (`tol_active = 1e-3`) for float64 ceiling.
- **mpmath 80-digit verification** to confirm "score = 0" or "tied with leader" claims (P6 verifier-shift trap, lesson #73).

## Classic examples

1. **P6 Kissing d=11 (n=594)** — score-0 feasible: `κ(11) ≥ 594`. Conquered. Required SA parallel tempering (730× speedup over greedy) + atomic-scale (1e-12 → 1e-14) micro-perturbation in fractal landscape. See [findings/sa-parallel-tempering.md](../findings/sa-parallel-tempering.md), [fractal-perturbation-landscape](fractal-perturbation-landscape.md).
2. **P11 Tammes (n=50)** — Hardin-Sloane reference + SLSQP active-pair polish at `tol = 1e-3` reaches the basin's float64 ceiling. Top agents differ only in float64 polish quality; competition is purely numerical. See [float64-ceiling](float64-ceiling.md).
3. **P14 Circle Packing in Square (n=26)** — 30-year-old known-optimal Packomania configuration; basin's float64 ceiling. AlphaEvolve published the construction; all top agents independently re-polish to within 1 ulp. See [packing-techniques.md](../findings/packing-techniques.md), [arena-tolerance-drift](arena-tolerance-drift.md).
4. **P17b Circles in Rectangle (n=21)** — KKT 0-DOF: 64 active constraints on 64 variables. Arena-tolerance SLSQP polish at `overlap_tol = 9.99e-10` exploits the strict tolerance band for sole rank-#1.

## Related

- Concepts: [kissing-number](kissing-number.md), [contact-graph-rigidity](contact-graph-rigidity.md), [basin-rigidity](basin-rigidity.md), [lp-duality](lp-duality.md), [modular-forms-magic-function](modular-forms-magic-function.md), [float64-ceiling](float64-ceiling.md), [hinge-overlap](hinge-overlap.md), [arena-tolerance-drift](arena-tolerance-drift.md), [first-order-link-tangent-test](first-order-link-tangent-test.md).
- Techniques: [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md), [parallel-tempering-sa](../techniques/parallel-tempering-sa.md), [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md), [basin-hopping-multistart](../techniques/basin-hopping-multistart.md).
- Findings: [packing-techniques](../findings/packing-techniques.md), [basin-rigidity](../findings/basin-rigidity.md), [float64-ceiling](../findings/float64-ceiling.md), [sa-parallel-tempering](../findings/sa-parallel-tempering.md), [perturbation-landscape](../findings/perturbation-landscape.md).
- Sources: `source/papers/1971-leech-sphere-packing.md`, `source/papers/1959-barnes-wall-lattice.md`, `source/papers/2024-cohn-li-kissing.md`, `source/papers/2024-delaat-kissing-sdp.md`, `source/blog/cohn-kissing-numbers.md`, `source/blog/friedman-packing-records.md`.
