---
type: source
kind: paper
title: Multidimensional Padé approximation of binomial functions: Equalities
authors: Michael A. Bennett, Greg Martin, Kevin O'Bryant
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.00549v2
source_local: ../raw/2021-bennett-multidimensional-pad-approximation-binomial.pdf
topic: general-knowledge
cites: 
---

# Multidimensional Padé approximation of binomial functions: Equalities

**Authors:** Michael A. Bennett, Greg Martin, Kevin O'Bryant  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2108.00549v2

## One-line
A unified compendium of all known closed-form expressions for the multidimensional Padé approximants and remainders of the binomial functions $(1-z)^{\omega_m}$, with complete proofs and a new perfectness criterion.

## Key claim
For distinct $\omega_0,\dots,\omega_M \in \mathbb{C}$ with no two differing by an integer and degree bounds $\rho_0,\dots,\rho_M$, the Padé remainder $G(z) = \sum_{m=0}^M H_m(z)(1-z)^{\omega_m}$ has a zero of order exactly $\sigma-1 = \sum(\rho_m+1)-1$ at $z=0$, and both $G$ and the $H_m$ admit five equivalent explicit representations (iterated integral, $M$-dim integral over $[0,1]^M$, contour integral, Maclaurin series, Meijer $G$-function). A new perfectness criterion is proved: for $\rho \in \mathbb{N}^{M+1}$ and shifts $\vec\epsilon_0,\dots,\vec\epsilon_M$, if the max permutation sum $S$ is achieved uniquely and $T+M=S$, then $\det H = C z^{\sigma(\rho)+T-1}$ with $C \neq 0$ independent of $z$ and of $\omega$.

## Method
Function-theoretic / complex-analytic. Existence and uniqueness via linear algebra on coefficients; equivalent forms derived by (a) induction with differential operators $d_\omega$ that lower $\rho$, (b) residue calculus on the contour integral kernel $\prod_k (\xi-\omega_k)^{-(\rho_k+1)}$, (c) Slater's theorem to convert the Meijer $G$-function to ${}_{M+1}F_M$ hypergeometric form, and (d) Euler's reflection formula to reorganize the closed-form coefficient expressions. Perfectness is proved by permutation-expansion of $\det H$ combined with order-of-vanishing bounds.

## Result
All five remainder forms (Theorem 4) and five approximant forms (Theorem 5) coincide; in particular the Maclaurin coefficient is $g_n = (-1)^n \sum_m \frac{1}{\rho_m!} \sum_r \binom{\rho_m}{r} (-1)^r (\omega_m+r)^n / \prod_{k\neq m}(\omega_k-\omega_m-r)^{\rho_k+1}$, vanishing for $n \leq \sigma-2$ and equal to $1$ at $n=\sigma-1$. Closed form: $\mathrm{Poly}_m = \frac{1}{\rho_m!} \sum_{r=0}^{\rho_m} (z-1)^r \binom{\rho_m}{r} \prod_{k\neq m}(\omega_k-\omega_m-r)^{-(\rho_k+1)}$. Theorem 6 generalizes the Mahler–Chudnovsky–Bennett perfectness lemma ($\vec\epsilon_k = \vec e_k$) and Jager's extension, covering substantially more shift patterns.

## Why it matters here
General background for analytic number theory machinery (Thue–Siegel method, irrationality measures of $(a/b)^{s/n}$); no direct arena tie among the 23 problems, but the explicit closed forms for $(1-z)^\omega$ Padé systems are the workhorse for sharp Diophantine bounds and could inform any future problem involving rational approximation, algebraic-number bounds, or hypergeometric optimization.

## Open questions / connections
- Is there a contour-free iterated integral for $\mathrm{Poly}_m$ analogous to Theorem 4(i) for the remainder?
- Geometric characterization of which shift vectors $\vec\epsilon_k$ yield perfect systems — empirically bounded by some $B(M)$.
- Explicit value of the constant $C$ in the perfectness determinant.
- Sequel papers promised: archimedean and non-archimedean size bounds on $H_m$ and $G$, yielding new irrationality measures for $(a/b)^{s/n}$ (extending Baker's $\sqrt[3]{2}$ work).

## Key terms
Padé approximation, multidimensional Padé, Thue–Siegel method, binomial function, hypergeometric function, Meijer G-function, Slater's theorem, irrationality measure, contour integral representation, perfect system, Mahler, Chudnovsky, Bennett, Jager, Diophantine approximation
