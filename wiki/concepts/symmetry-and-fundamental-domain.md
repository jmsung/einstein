---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P5, P11, P14, P15, P16, P17a]
related_techniques: [multistart-with-rotation-lottery.md, slsqp-active-pair-polish.md]
related_findings: [basin-rigidity.md]
cites:
  - ../findings/basin-rigidity.md
---

# Symmetry and Fundamental Domain

## TL;DR

When a problem is invariant under a group `G` of transformations (rotations, translations, reflections, permutations), the optimization variable lives in `Ω / G` — the fundamental domain. Working modulo `G` removes spurious DOF that no optimizer can productively explore (rotation in 2D contributes 1 DOF; affine gauges in Heilbronn contribute 4). Forgetting the gauge inflates DOF counts and hides basin rigidity. Noether's framing: every symmetry is a conserved quantity, so a symmetry-respecting optimizer never wastes effort on its conjugate direction.

## What it is

For an optimization problem `min_x f(x)` with `x ∈ Ω`, suppose `G` acts on `Ω` and `f(g · x) = f(x)` for all `g ∈ G`. Then:

- The objective is **`G`-invariant**.
- Critical points come in `G`-orbits.
- The effective optimization variable is `[x] ∈ Ω / G` — the **fundamental domain** of the action.
- The effective dimension is `dim(Ω) − dim(G)` (when `G` acts freely; subtract additionally for stabilizer dimensions if the action has fixed points).

Common symmetry groups in arena problems:

| Group | Where it appears | Effective DOF reduction |
|---|---|---|
| Translation `ℝᵈ` | sphere/disk packing | `d` |
| Rotation `SO(d)` | sphere code, Heilbronn (free 2D), Tammes | `d(d−1)/2` |
| Reflection `O(d) / SO(d)` | usually 1 (sign flip) | 1 |
| Scale (affine) | Heilbronn (`d_max / d_min` invariant) | 1 |
| Permutation `S_n` | identical-particle problems (Thomson, Tammes) | `n!` factor (combinatorial, not dimensional) |
| Cyclic `C_k` | hexagon packing (P17a `C_6`), Heilbronn-symmetric | `1` |
| Dihedral `D_k` | Heilbronn convex, Heilbronn triangle (D1) | `2` |

The **fundamental domain** is a representative subset of `Ω` such that every orbit intersects it exactly once (or the boundary is identified). Optimization in the fundamental domain avoids exploring orbit-equivalent points.

## When it applies

- Geometric packing (translation + rotation invariance is universal).
- Sphere codes / Tammes (rotation + reflection invariance).
- Heilbronn-type problems (affine invariance, sometimes additional reflection symmetry).
- Symmetric polynomial / lattice constructions (cyclic and dihedral group actions).

Recognition pattern: "the score depends only on pairwise distances / ratios / angles" — Euclidean group invariance. "The score is invariant under a relabeling" — permutation invariance.

## Why it works

Three operational consequences:

1. **DOF counting** for basin-rigidity diagnostics requires gauging out symmetries. P5 has 32 coords − 4 affine gauges = 28 effective DOF; without the gauging, the (22, 8) configuration looks under-determined (32 vars, 30 constraints) but is actually over-determined (28 effective DOF, 30 constraints — over by 2). See [basin-rigidity](basin-rigidity.md).
2. **Multistart discipline**: random initialization from `Ω` over-counts orbits. Sampling `[x] ∈ Ω/G` (e.g. fix center of mass, principal axis) gives the same coverage at lower cost. The "rotation lottery" technique (random orthogonal rotations of the polished configuration) is precisely the inverse: deliberately exploit the rotation group to find float64-equivalent points where one happens to land at the basin's float64 ceiling.
3. **Symmetric optima**: when `G` has a fixed point and `f` has a unique global minimum, the minimum lies at the fixed point (e.g. P17a hexagon packing's `C_6`-symmetric optimum). Restricting to fixed-point parameterizations reduces DOF and stabilizes optimization.

The Noether-style framing: every symmetry of the objective is a "conservation law" — the optimizer should never move along the orbit. If it does, you are wasting compute and hiding rigidity.

## Classic examples

1. **P5 Min Distance Ratio (n=16)** — affine gauge: 4 DOF (2 translation, 1 rotation, 1 scale). 32 − 4 = 28 effective. With 30 active constraints, over-determined by 2 — fully rigid. Without gauging, the count is wrong. See [findings/basin-rigidity.md](../findings/basin-rigidity.md) lessons #84, #85.
2. **P11 Tammes (n=50)** — `SO(3)` rotation + reflection invariance. Rotation lottery (86/2000 random rotations land at the basin float64 ceiling) exploits the symmetry. Without exploiting it, all polishers find the same float64 score.
3. **P15 Heilbronn Triangles (n=11)** — D1 reflection symmetry (in equilateral triangle); 8 effective shape DOF after symmetry + boundary incidences. 17 active triples on 8 DOF gives over-determination; basin-rigid.
4. **P17a Hexagon Packing (n=12)** — `C_6` rotational symmetry. The unique-basin global optimum is `C_6`-symmetric; restricting to symmetric configurations reduces from 40 free params to 8.

## Related

- Concepts: [basin-rigidity](basin-rigidity.md), [contact-graph-rigidity](contact-graph-rigidity.md), [discretization-as-structure](discretization-as-structure.md), [parameterization-selection](parameterization-selection.md).
- Techniques: [multistart-with-rotation-lottery](../techniques/multistart-with-rotation-lottery.md), [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md).
- Findings: [basin-rigidity](../findings/basin-rigidity.md), [packing-techniques](../findings/packing-techniques.md).
