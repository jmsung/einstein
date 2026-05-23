---
type: source
kind: paper
title: General formulas for a class of Euler sums
authors: David H Bailey, Ross McPhedran, Bruno Salvy
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2604.02384v1
source_local: ../raw/2026-bailey-general-formulas-class-euler.pdf
topic: general-knowledge
cites: 
---

# General formulas for a class of Euler sums

**Authors:** David H Bailey, Ross McPhedran, Bruno Salvy  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2604.02384v1

## One-line
A residue-based algorithm and explicit catalog for closed-form evaluation of Euler sums $\sum_{k\geq 1} R(k)H_k$ in terms of digamma and polygamma values at rational points.

## Key claim
For any rational $R(s)=P(s)/Q(s)$ with $\deg Q - \deg P \geq 2$ and no positive-integer poles, $\sum_{k=1}^\infty R(k)H_k = \tfrac{1}{2}\sum_{\alpha} \operatorname{Res}_{s=\alpha}\!\big[R'(s)(\psi(-s)+\gamma) - R(s)(\psi(-s)+\gamma)^2\big]$ (Proposition 1), giving fully symbolic closed forms via partial-fraction decomposition.

## Method
Residue calculus applied to the contour-integral representation of Euler sums (extending Flajolet–Salvy 1998), combined with the Laurent expansion $\psi(-s)+\gamma = 1/s + \sum_{k\geq 2}\zeta(k)s^{k-1}$ near $s=0$ and the Taylor expansion of $\psi(-s)+\gamma$ near nonintegers. Square-free factorization of $Q$ lets the algorithm sum symbolically over conjugate roots without explicit pole computation. Verification uses Euler–Maclaurin tail summation to ~280-digit precision plus PSLQ integer-relation detection.

## Result
Theorem 2 gives the master closed form $\sum_{k\geq 1} H_k/(k+t)^p = T(t,p)$ where $T(t,p) = \tfrac{(-1)^{p-1}}{2(p-1)!}\big[\psi^{(p)}(t) - 2\gamma\psi^{(p-1)}(t) - \sum_{k=0}^{p-1}\binom{p-1}{k}\psi^{(k)}(t)\psi^{(p-1-k)}(t)\big]$; Theorem 3 extends this via partial fractions to arbitrary $R$. Corollary 2 handles $\sum k^q H_k/(mk+n)^p$. A catalog (Appendix B) gives ~100 explicit formulas for $m\in\{2,3,4\}$, $p\leq 8$. The fast digamma/polygamma evaluation route is ~30,000× faster than direct summation at 280-digit precision.

## Why it matters here
General background; no direct arena tie. Could marginally inform high-precision constant evaluation for autocorrelation / sieve-theory problems (P14, P17) where mpmath-class polygamma values arise, but Euler sums are not the bottleneck in any of the 23 arena problems.

## Open questions / connections
- Extending the residue method to $\sum H_k^2/(mk+n)^p$, alternating sums $\sum (-1)^k H_k/(mk+n)^p$, and $\sum H_{2k}/(mk+n)^p$ (Section 6).
- Accelerating series whose summand has a logarithmic numerator (paper's suggested application).
- Builds on Flajolet–Salvy's contour-integral framework [12] and Bailey–McPhedran's earlier catalog of mixed-denominator sums (arXiv:2311.06294).

## Key terms
Euler sums, harmonic numbers, digamma function, polygamma function, Hurwitz zeta, residue calculus, partial fraction decomposition, Flajolet-Salvy contour integral, PSLQ integer relation, Euler-Maclaurin summation, high-precision arithmetic, closed-form evaluation
