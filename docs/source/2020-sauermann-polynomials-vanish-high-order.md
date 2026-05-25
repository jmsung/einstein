---
type: source
kind: paper
title: Polynomials that vanish to high order on most of the hypercube
authors: Lisa Sauermann, Yuval Wigderson
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.00077
source_local: ../raw/2020-sauermann-polynomials-vanish-high-order.pdf
topic: general-knowledge
cites:
---

# Polynomials that vanish to high order on most of the hypercube

**Authors:** Lisa Sauermann, Yuval Wigderson  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.00077

## One-line
Determines the minimum degree of a real polynomial that vanishes to order $\geq k$ at every nonzero hypercube point $\{0,1\}^n \setminus \{0\}$ while not vanishing at the origin, generalizing Alon–Füredi to higher multiplicities.

## Key claim
For $k \geq 2$ and $n \geq 2k-3$, any $P \in \mathbb{R}[x_1,\ldots,x_n]$ with $P(0)\neq 0$ and zeros of multiplicity $\geq k$ on $\{0,1\}^n\setminus\{0\}$ satisfies $\deg P \geq n + 2k - 3$, and this bound is tight (Theorem 1.3). If $P$ has a zero of multiplicity exactly $k-1$ at the origin, the answer jumps to $n + 2k - 2$ (Theorem 1.5).

## Method
Reduce to a "$k$-reduced" canonical form (no monomial divisible by $k$ squared variables) via iterative monomial subtraction, then show a derivative-evaluation linear map $\psi_k : U_k \to \mathbb{R}^N$ is an isomorphism by dimension counting. To prove a homogeneous-top-part map $\phi_k$ is injective, expand a specific explicit polynomial in the power-sum-symmetric basis and show that a key coefficient — which turns out to equal a Catalan number $C_{\ell-1}$ up to sign — is nonzero. The Catalan identity $\sum_{i=0}^{s}(-1)^i C_i \binom{i+1}{s-i}=0$ drives the algebraic verification.

## Result
Resolves Problem 1.2 for all $k \geq 2$ with the sharp bound $n + 2k - 3$, improving Clifton–Huang's $n + k + 1$ bound for $k \geq 5$. Corollary 1.6: any hyperplane arrangement $k$-covering $\{0,1\}^n\setminus\{0\}$ but missing the origin needs $\geq n + 2k - 3$ hyperplanes (vs. the Clifton–Huang upper bound of $n + \binom{k}{2}$, still open for $k \geq 4$). Over fields of characteristic $p$, the bound fails precisely when $C_{k-2} \equiv 0 \pmod{p}$ (e.g., char 2 with $k=4$, char 3 with $k=7$, char $p>3$ with $k=(p+5)/2$).

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — the Combinatorial Nullstellensatz / Alon–Füredi family of degree-lower-bound techniques is a recurring tool for discrete-geometry and extremal-combinatorics problems, and the Catalan-number appearance in a multiplicity-Nullstellensatz argument is a transferable surprise pattern for "what symmetric-function identities show up when counting derivative conditions."

## Open questions / connections
- Gap between $n + 2k - 3$ (this paper) and $n + \binom{k}{2}$ (Clifton–Huang upper bound) for the hyperplane-cover problem with $k \geq 4$ remains open; the linear-factor structure of the polynomial $f$ would need to be exploited beyond what the Nullstellensatz captures.
- For $\ell$-at-origin variants with $0 \leq \ell \leq k-4$, whether the hyperplane (product-of-linears) answer differs from the general-polynomial answer $n+2k-3$ is open.
- Fixed $n$, large $k$ regime (Clifton–Huang showed $(H_n + o(1))k$) for Problem 1.2 is unexplored.

## Key terms
Combinatorial Nullstellensatz, Alon-Füredi, higher multiplicity vanishing, hypercube covering, hyperplane cover, Catalan numbers, power-sum symmetric polynomials, punctured Nullstellensatz, Ball-Serra, Clifton-Huang, Komjáth hyperplane problem, multiplicity Schwartz-Zippel
