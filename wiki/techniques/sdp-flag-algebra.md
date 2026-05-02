---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P13]
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "hours (formulation + solve); CPU is usually adequate"
hit_rate: "TBD"
---

# Razborov SDP Flag Algebra

## TL;DR

Flag algebra (Razborov 2007) translates extremal-graph problems — counting subgraph densities — into a hierarchy of semidefinite programs whose duals provide rigorous upper bounds on the densities. Used on P13 (Edges vs Triangles) to derive the slope-3 envelope and Turán construction that the local-polish pipeline (`bounded-lbfgs-per-region-sigmoid`, `boundary-snap-for-kinks`) operates on.

## When to apply

- Extremal graph theory problem expressed as a polynomial in subgraph densities.
- Goal is a rigorous upper bound on a density ratio (edges-to-triangles, etc.).
- The Turán-type construction (blow-up of a small graph) is a candidate for tightness.
- A flag-algebra solver (FlagMatic, Csdp, or hand-rolled) is available.

## Procedure

1. **Encode the problem in flag densities**: choose flag types `F_1, ..., F_m` (small graphs); the density of a flag in a host graph `G` is the asymptotic frequency of `F_i` as a labelled subgraph.
2. **Build the SDP**: the dual provides a rigorous upper bound on the target density combination.
   - Variables: PSD matrices `Q_i` indexed by flag pairs.
   - Constraints: for every type, the average density over flags must equal the target.
3. **Solve the SDP** (CVXPY + Mosek/SCS, or FlagMatic):
   ```python
   import cvxpy as cp
   Q = cp.Variable((m, m), PSD=True)
   constraints = [...]
   prob = cp.Problem(cp.Minimize(target_combo), constraints)
   prob.solve(solver=cp.MOSEK)
   ```
4. **Identify the extremal construction** from the SDP's complementary slackness: which flags have positive density at the optimum? These are the support of the Turán-type construction.
5. **Pass the construction downstream**: the local-polish pipeline (`bounded-lbfgs-per-region-sigmoid` + `boundary-snap-for-kinks`) optimizes within the construction's parametric family.

## Pitfalls

- **SDP relaxation is not always tight**: bilinear minimax problems (P1 Erdős overlap) defeat SDP — rank-1 structure is load-bearing; lifting destroys it (lesson `sdp-relaxation-uselessness-on-bilinear-minimax`). Run the bound first; if it's far from the conjectured optimum, the relaxation isn't tight.
- **FOSS SDP solvers (SCS, CLARABEL) bog at large flag types**. Mosek / Gurobi handle dense PSD matrices much better. Mosek is paid; budget accordingly.
- **The SDP is upper-bounding the density**: the "construction" extracted is the conjectured tight family, not the local maximum of the polish. The latter (P13: −0.71170918806610) is reached by polishing within the family.
- **Flag-type cardinality blows up**: |flags of size n| grows fast; truncate at the smallest n that still yields a useful bound.
- **Tightness is delicate**: P13's slope-3 was proven tight by Razborov; P1's bilinear minimax has no such certificate.

## Compute profile

Local CPU usually suffices for flag types up to size ~7–8. Larger flags need Modal RAM (Mosek loves 128GB+). FlagMatic is CPU-only.

## References

- knowledge.yaml: see strategy notes on Razborov flag algebra (P13).
- `wiki/findings/optimizer-recipes.md` (#68 boundary L-BFGS, #69 multi-seed BH — the downstream polish).
- `wiki/findings/equioscillation-escape.md` (when SDP is the wrong tool).
- `mb/wiki/problem-13-edges-triangles/literature.md` (Razborov 2007, FlagMatic, Turán construction).
- Razborov, "Flag Algebras", J. Symbolic Logic 72 (2007).
