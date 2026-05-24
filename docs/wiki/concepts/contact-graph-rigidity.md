---
type: concept
author: agent
drafted: 2026-05-02
revised: 2026-05-23
related_problems: [P5, P11, P14, P16, P17a, P17b, P22]
related_techniques: [slsqp-active-pair-polish.md, mpmath-ulp-polish.md]
related_findings: [basin-rigidity.md, packing-techniques.md, float64-ceiling.md]
cites:
  - ../findings/basin-rigidity.md
  - ../findings/packing-techniques.md
  - ../personas/archimedes.md
  - reduced-hessian.md
  - ../../source/2011-cohn-rigidity-spherical-codes.md
related_personas: [archimedes.md]
---

# Contact Graph Rigidity

## TL;DR

For a sphere/disk packing, the **contact graph** has a node per disk and an edge per touching pair. Rigidity asks: is there an infinitesimal motion of the disks (modulo Euclidean group) preserving every contact? Maxwell's count `2|V| − 3 ≤ |E|` (in 2D) is the rigidity threshold. When `|E| ≥ 2|V| − 3`, the packing is generically rigid — locked. This is the geometric subspecies of [basin-rigidity](basin-rigidity.md): the basin is rigid because the contact graph is rigid.

## What it is

For a packing of unit disks `D_1, ..., D_n` in `ℝ²` (or unit balls in `ℝᵈ`), the **contact graph** `Γ = (V, E)` has:

- `V = {1, ..., n}` (one vertex per disk).
- `(i, j) ∈ E` iff `D_i, D_j` are touching (`‖c_i − c_j‖ = 2r` for radius `r`).

A **flex** is a smooth one-parameter family of motions `c_i(t)` preserving every contact: `‖c_i(t) − c_j(t)‖ = 2r` for all `(i,j) ∈ E` and all `t`. **Trivial flexes** are the rigid motions (translation, rotation, reflection of the whole packing).

The packing is **rigid** if every flex is trivial. **Maxwell's count** (1864) gives a generic-position lower bound:

```
|E| ≥ 2|V| − 3   (in 2D)
|E| ≥ d|V| − d(d+1)/2   (in ℝᵈ).
```

The right-hand side is `dim(rigid motions)` subtracted from total DOF. Generic rigidity follows from the count via Laman's theorem (2D, 1970): a 2D bar-joint framework is generically minimally rigid iff `|E| = 2|V| − 3` and every subgraph satisfies `|E'| ≤ 2|V'| − 3`.

For arena problems, **non-trivial structure**: the disks are constrained to a container (square, rectangle, larger sphere). Container contacts contribute additional edges; counting them correctly is essential.

## When it applies

- **Bounded-container packings** (P14 disks in square, P17a hexagons in hexagon, P17b circles in rectangle).
- **Sphere codes / Tammes-type problems** (P11 — points on `S²`, contact = exact min-distance).
- **Min-distance-ratio problems** (P5 — contacts are min-edge and max-edge equalities).
- Any problem where the optimum is characterized by a discrete graph of saturated constraints.

Recognition: "the optimum has many touching pairs / equality constraints, and adding any touching pair freezes the configuration" — this is contact-graph rigidity.

## Why it works

Geometric Maxwell counting:

- Each vertex contributes `d` translation DOF.
- Subtract `d(d+1)/2` for the global Euclidean group.
- Each contact edge is one equality constraint, eating one DOF generically.
- When `|E| − (d|V| − d(d+1)/2) > 0`, the system is over-determined; reduced Hessian (KKT) is non-degenerate.

For 2D arena packings:

- P14 (n=26 disks in square): 52 position DOF; container contributes ≤ 4 boundary contacts; pair contacts saturate at `2·26 − 3 = 49`. Add boundary, near-saturated.
- P5 (n=16 in min-distance-ratio): 32 − 4 affine gauges = 28; 30 active equalities = +2 over-determined.

Distinct from [basin-rigidity](basin-rigidity.md) more broadly:

- **Basin rigidity** is about reduced-Hessian non-degeneracy for any constrained optimum (geometric or non-geometric).
- **Contact-graph rigidity** is the *geometric instance*: the active set is a graph, edges are pair contacts, and Maxwell-style counting gives the rigidity diagnostic.

In arena practice, contact-graph rigidity tells you to:

- Use a **wide active-pair tolerance** (`tol = 1e-3` for P11) to capture all near-contacts that the basin is actually saturating.
- Stop investing compute in multistart once `|E| ≥ d|V| − d(d+1)/2`; the basin is locked.
- mpmath polish at 80 dps to find the basin's true-math floor (P11, P14, P17b).

## Classic examples

1. **P11 Tammes (n=50)** — contact graph has `~95` near-contact edges (within `1e-3`); 50 vectors on `S²` with 3 DOF each minus 3 rotation gauges = 147 DOF; `2 · 50 − 3 = 97` is the 2D-style threshold (sphere is locally 2D). Wide active-pair tolerance is essential; narrow tolerance (1e-7) misses 95+ pairs and stalls below ceiling. See [findings/packing-techniques.md](../findings/packing-techniques.md).
2. **P14 Circle Packing in Square (n=26)** — Packomania-known-optimal contact graph. All top agents converge to the same contact graph; competition reduces to float64 polish quality.
3. **P17b Circles in Rectangle (n=21)** — KKT 0-DOF: 64 active constraints on 64 variables. Exactly contact-graph-rigid (no slack, no over-determination). Arena-tolerance SLSQP exploits the strict tolerance band for the only available improvement.

## Literature: Cohn et al. on spherical-code rigidity

The exact LP formulation of contact-graph rigidity on the sphere is in **Cohn–Jiao–Kumar–Torquato 2011** ([`source/2011-cohn-rigidity-spherical-codes.md`](../../source/2011-cohn-rigidity-spherical-codes.md)). The setup is identical to what JSAgent uses for P11:

```
perturb x_i → x_i + ε y_i  with  ⟨x_i, y_i⟩ = 0  (stay on sphere),
constraints: ⟨x_i, y_j⟩ + ⟨x_j, y_i⟩ ≤ 0  on every contact pair (i,j),
rigid iff every feasible y is an infinitesimal rotation (y_i = Φ x_i, Φ skew-symmetric).
```

Two facts from the paper that directly apply to arena work:

1. **Connelly–Roth–Whiteley** (cited in §2): *infinitesimal* jamming $\Rightarrow$ finite jamming via tensegrity frameworks with bars to origin and struts between neighbors. Practical implication — the LP certificate (cheap) implies the basin-floor certificate (otherwise verified by mpmath polish). The two checks should agree; disagreement means an off-by-one in the contact tolerance.
2. **$K_{12}$ is not jammed.** The Coxeter–Todd kissing configuration in $\mathbb{R}^{12}$ is *not* infinitesimally jammed, despite being a record. The paper exploits this non-jamming to construct *new* kissing-number records in $\mathbb{R}^{25}$–$\mathbb{R}^{31}$ (e.g. $230872$ in $\mathbb{R}^{31}$). **Cautionary tale for P22**: "current record" does not entail "rigid"; an LP test could reveal a non-trivial deformation and a route to improvement. The exact-rational `QSopt_ex` LP is the certificate of record.

The paper also lists configurations that *are* infinitesimally jammed: $D_n$ for $n \ge 4$, $E_6, E_7, E_8$, Barnes–Wall $\Lambda_{16}$, and all best known kissing configs in dimensions 4–12. These match the arena's empirical "frozen" set.

## Related

- Concepts: [basin-rigidity](basin-rigidity.md), [sphere-packing](sphere-packing.md), [kissing-number](kissing-number.md), [symmetry-and-fundamental-domain](symmetry-and-fundamental-domain.md), [float64-ceiling](float64-ceiling.md), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md).
- Techniques: [slsqp-active-pair-polish](../techniques/slsqp-active-pair-polish.md), [mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md).
- Findings: [basin-rigidity](../findings/basin-rigidity.md), [packing-techniques](../findings/packing-techniques.md), [float64-ceiling](../findings/float64-ceiling.md).
- Sources: [Cohn–Jiao–Kumar–Torquato 2011](../../source/2011-cohn-rigidity-spherical-codes.md).
