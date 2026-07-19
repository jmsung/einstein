---
type: source
kind: paper
title: Absolute Minima of Potentials of Certain Regular Spherical Configurations
authors: S. Borodachov
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2210.04295
source_local: ../raw/2022-borodachov-absolute-minima-potentials-certain.pdf
topic: general-knowledge
cites:
---

# Absolute Minima of Potentials of Certain Regular Spherical Configurations

**Authors:** S. Borodachov  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2210.04295

## One-line
Identifies the exact locations on the sphere where the sum-of-pair-potential of icosahedron / dodecahedron / $E_8$ minimal-vector configurations attains its absolute minimum, for a broad class of absolutely monotone potentials.

## Key claim
For a configuration $\omega_N\subset S^d$ whose index set contains $\{1,\dots,2m-3, 2m-1, 2m\}$, and any potential $f$ with non-negative derivatives $f^{(2m-2)},f^{(2m-1)},f^{(2m)}$ on $(-1,1)$: if there exist $-1<t_1<\dots<t_m<1$ with $\sum t_i < t_m/2$ and $\sum t_i^2 - 2(\sum t_i)^2/m < \tfrac{m(2m-1)}{4m+d-3}$ (the ratio of the $t^{2m-2}$ coefficient to the leading coefficient of the Gegenbauer polynomial $P_{2m}^{(d)}$), then $\min_{x\in S^d}\sum_i f(x\cdot x_i)$ is attained exactly at the points $x^*$ that form dot products $\{t_1,\dots,t_m\}$ with $\omega_N$. Concrete corollaries: icosahedron's potential is minimized on the dual dodecahedron and vice versa; the $E_8$ minimal-vector set $\omega_{240}\subset S^7$ has its potential minimized on an explicit 2160-point set $\omega_{2160}$.

## Method
Linear-programming / polynomial (Delsarte) method extended by exploiting non-trivial **even** indexes of antipodal designs beyond their design strength. The lower bound is built from a Hermite interpolant $p(t;a)\le f(t)$ (with $f^{(2m)}\ge 0$) whose remainder $\Pi_m(t)=\prod (t-t_i)^2$ is controlled by showing the Gegenbauer expansion of three auxiliary polynomials $Q_i(t)=(t-t_m)^i\prod_{j<m}(t-t_j)^2$ has positive inner product with $P_{2m-2}^{(d)}$ — a structural condition that the configuration's index set + the dot-product locations $t_i$ together imply.

## Result
- Theorem 3.1 (general): explicit characterization of minimizers via the Gegenbauer-coefficient inequality (4)/(6), with uniqueness when $f^{(2m)}>0$.
- Theorem 3.3: icosahedron $\omega_{12}$ on $S^2$, $m=4$, $\sum t_i^2 = 4/3 < 28/15$ — minimum at dodecahedron vertices.
- Theorem 3.4: dodecahedron $\omega_{20}$, same arithmetic, minimum at icosahedron vertices.
- Theorem 3.5: $E_8$ minimal vectors $\omega_{240}$ on $S^7$, $m=5$, $\sum t_i^2 = 5/4 < 15/8$ — minimum at the 2160-point set $\omega_{2160}$ (1120 vectors with four $\pm 1/2$ coords, 16 standard-basis vectors $\pm e_i$, 1024 vectors with seven $\pm 1/4$ and one $\pm 3/4$ with odd negative count).
- Covers Coulomb, Riesz $-2<s<\infty$, log potential, Gaussian, and any completely monotone $g$ of squared distance.

## Why it matters here
Direct ingredient for any Einstein Arena problem that resembles **polarization** (min-of-sum over the sphere) on highly symmetric configurations — relevant to sphere-packing/kissing-number neighborhoods (Cohn–Elkies / Viazovska family) and any potential-minimization problem on regular polytopes in $S^d$. Gives a verified-correct closed-form minimizer for $E_8$, icosahedron, dodecahedron potentials, useful as an analytical cross-check (triple-verify level 3) for optimizers operating near these configurations.

## Open questions / connections
- Extension to non-stiff, non-sharp configurations beyond those analyzed — e.g., 600-cell, Leech-lattice minimal vectors (the latter is antipodal, $S^{23}$).
- Maximum (polarization) counterpart for these same configurations under matching derivative-sign assumptions.
- Sharpness of the Gegenbauer-coefficient inequality (4): which configurations sit on the boundary and what happens there.
- Connection to universal optimality of Cohn–Kumar (sharp configurations) — Borodachov's framework is strictly broader (covers dodecahedron, which is not sharp).

## Key terms
Gegenbauer polynomials, spherical design, non-trivial index, Delsarte LP method, polarization problem, Riesz potential, Coulomb potential, completely monotone, $E_8$ lattice, icosahedron, dodecahedron, Hermite interpolation, antipodal configuration, sharp configuration
