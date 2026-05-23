---
type: source
kind: paper
title: On the equivariant log-concavity for the cohomology of the flag varieties
authors: Tao Gui
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2205.05408v2
source_local: ../raw/2022-gui-equivariant-log-concavity-cohomology-flag.pdf
topic: general-knowledge
cites: 
---

# On the equivariant log-concavity for the cohomology of the flag varieties

**Authors:** Tao Gui  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2205.05408v2

## One-line
Studies $S_n$-equivariant log-concavity of the graded coinvariant ring $H^*(F_n,\mathbb{C}) \cong \mathbb{C}[t_1,\ldots,t_n]/(\sigma_1,\ldots,\sigma_n)$ and conjectures it holds in all degrees.

## Key claim
Conjecture: for all $n \geq 1$ and $1 \leq m \leq \binom{n}{2}-1$, $H^{2(m-1)} \otimes H^{2(m+1)}$ embeds as a subrepresentation of $H^{2m} \otimes H^{2m}$; proven in degrees $\leq 3$ and co-degrees $\leq 3$ for all $n$ (Theorem 6).

## Method
Representation stability via FI-modules (Church–Ellenberg–Farb): $\{H^{2i}\}_n$ forms a uniformly representation stable sequence that stabilizes once $n \geq 2i$ (for $i \leq 4$). Reduces the infinite family of inequalities to finite checks at $n \leq 4m$, verified computationally with Maple up to $n \leq 12$. Lusztig–Stanley's combinatorial description gives graded multiplicities $b_{\lambda,i}$ as counts of standard Young tableaux of shape $\lambda$ with major index $i$ (the "fake degrees").

## Result
Equivariant log-concavity equivalent to Schur positivity of $S_{n,i} * S_{n,i} - S_{n,i-1} * S_{n,i+1}$ under the internal product (Conjecture 4), or to Kronecker-coefficient inequalities $\sum_{\lambda,\mu} b_{\lambda,i-1}b_{\mu,i+1}g_{\lambda\mu\nu} \leq \sum_{\lambda,\mu} b_{\lambda,i}b_{\mu,i}g_{\lambda\mu\nu}$ for all $\nu \vdash n$ (Conjecture 5). Stronger unimodal Conjecture 7: the multiplicity sequence $d_{\nu,i}$ is symmetric and unimodal in $i$. Property fails for dihedral $I_2(m)$ ($m \neq 2,3$), including Weyl types $B_2$, $G_2$; also fails for general Springer representations (smallest counterexample in $S_7$).

## Why it matters here
General background; no direct arena tie. Log-concavity machinery (Newton's inequalities, ultra-log-concavity, Lorentzian polynomials) underlies several extremal-combinatorics problems; equivariant lifts via FI-module/representation-stability formalism could inform symmetric-group-invariant configurations.

## Open questions / connections
- Whether equivariant log-concavity holds for simply-laced (ADE) Coxeter coinvariant rings beyond type A.
- Whether Atiyah's $S_n$-equivariant map $\mathrm{Conf}_n(\mathbb{R}^3) \to U_n/T$ induces a formal relation between log-concavity conjectures on both sides (Matherne–Miyata–Proudfoot–Ramos for configuration spaces).
- Combinatorial interpretation of Kronecker coefficients — every $g_{\lambda\mu\nu}$ appears in the conjectural inequality since $H^*(F_n)$ is the regular representation.

## Key terms
equivariant log-concavity, coinvariant ring, flag variety, symmetric group $S_n$, representation stability, FI-modules, Kronecker coefficients, Schur positivity, major index, fake degrees, Lusztig–Stanley, Springer representations, unimodality, hard Lefschetz
