---
type: source
kind: paper
title: "The conformal bootstrap: Theory, numerical techniques, and applications"
authors: D. Poland, S. Rychkov, A. Vichi
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1805.04405
source_local: ../raw/2018-poland-conformal-bootstrap-theory-numerical.pdf
topic: general-knowledge
cites:
---

# The conformal bootstrap: Theory, numerical techniques, and applications

**Authors:** D. Poland, S. Rychkov, A. Vichi  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1805.04405

## One-line
A comprehensive review of the modern conformal bootstrap — how conformal symmetry plus crossing symmetry of 4-point functions, encoded as a convex optimization problem, carves out the space of allowed CFTs and yields rigorous, world-record numerical bounds on critical exponents.

## Key claim
By recasting the crossing equation for a CFT 4-point function as a semidefinite program over the space of OPE coefficients and operator dimensions, one obtains *rigorous* exclusion regions in CFT-data space; iterating with mixed correlators produces small "islands" containing the actual critical theories, giving e.g. the world's most precise 3d Ising exponents $\Delta_\sigma = 0.5181489(10)$, $\Delta_\epsilon = 1.412625(10)$ (Kos–Poland–Simmons-Duffin–Vichi 2016).

## Method
Conformal blocks (eigenfunctions of the quadratic Casimir) decompose the 4-point function into a sum over exchanged primaries; the crossing equation becomes an infinite-dimensional linear functional problem. Unitarity bounds make OPE-coefficient-squared $\lambda_{ijk}^2 \geq 0$, so finding a linear functional $\alpha$ that is non-negative on all allowed blocks but negative on a candidate spectrum *excludes* that spectrum. Practical implementation: rational/polynomial approximation of conformal blocks → SDP solved by SDPB (arbitrary-precision semidefinite programming with a custom interior-point method), with linear-programming and simplex variants as predecessors.

## Result
Yields the dimension bound machinery (Rattazzi–Rychkov–Tonni–Vichi 2008) — for any unitary CFT with a scalar $\phi$ of dimension $\Delta_\phi$, the leading scalar in $\phi \times \phi$ obeys a rigorous upper bound $\Delta_\epsilon \leq f(\Delta_\phi)$. The 3d Ising critical point sits at a "kink" in this bound; mixed-correlator bootstrap (Kos et al.) sharpens kink to "island" giving the precision exponents above. Analogous islands exist for $O(N)$ models (with kinks across continuous $N$), Gross-Neveu-Yukawa fermionic CFTs, QED$_3$ monopole bootstrap, deconfined-criticality candidates, and 4d $\mathcal{N}=1$ SCFTs. Central-charge lower bounds and stress-tensor / current OPE constraints are also obtained.

## Why it matters here
General background — the bootstrap toolkit (SDP over a polynomial-matrix cone, rational approximation of special functions, "carving out" allowed regions via linear functionals) is the exact methodological cousin of Cohn–Elkies LP bounds for sphere packing and the SDP flag-algebra method used in extremal combinatorics. Useful framing for any Arena problem cast as "find a functional certifying a bound." No direct numerical bound applies to Einstein Arena problems.

## Open questions / connections
- Can the same SDP-over-positive-functionals scaffolding (SDPB) be repurposed for sphere-packing / kissing-number LP duals, or for autocorrelation extremal problems? (Same convex-cone structure.)
- The "kink → island" phenomenon: when does adding a second crossing equation collapse a 1-d allowed curve to a 0-d point? Possible analogue: adding redundant constraints to LP-bound problems in discrete geometry.
- Analytical bootstrap (lightcone expansion, large-spin perturbation theory) — a route to closed-form bounds where SDP only gives numerics; analogue to Remez exchange's analytic limit.
- Convergence rate of the OPE / conformal-block expansion (Pappadopulo–Rychkov–Espin–Rattazzi 2012) — bounds on truncation error, structurally similar to LP-bound truncation analyses.

## Key terms
conformal bootstrap, conformal field theory, crossing symmetry, conformal blocks, OPE coefficients, semidefinite programming, SDPB, linear programming bounds, unitarity bounds, critical exponents, 3d Ising model, O(N) model, Gross-Neveu-Yukawa, mixed correlators, kink, island, Cohn-Elkies, Rattazzi, Rychkov, Simmons-Duffin, Poland, Vichi, convex optimization, extremal functional, Casimir equation, rational approximation
