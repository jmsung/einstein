---
type: source
kind: paper
title: Improved Convergence Rates for Lasserre-Type Hierarchies of Upper Bounds for Box-Constrained Polynomial Optimization
authors: E. Klerk, Roxana Hess, M. Laurent
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.03329
source_local: ../raw/2016-klerk-improved-convergence-rates-lasserre-type.pdf
topic: general-knowledge
cites:
---

# Improved Convergence Rates for Lasserre-Type Hierarchies of Upper Bounds for Box-Constrained Polynomial Optimization

**Authors:** E. Klerk, Roxana Hess, M. Laurent  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.03329

## One-line
Sharpens the convergence rate of Lasserre's measure-based upper-bound hierarchy for minimizing a polynomial over the box $[-1,1]^n$ from $O(1/\sqrt{r})$ to $O(1/r^2)$ by switching to Chebyshev measure plus Schmüdgen-type SOS densities.

## Key claim
For $f_{\min} = \min_{x\in[-1,1]^n} f(x)$ and the hierarchy $f^{(r)} = \inf_h \int f h\, d\mu$ where $d\mu(x) = \prod_i (\pi\sqrt{1-x_i^2})^{-1} dx$ and $h$ has a Schmüdgen-type representation $h = \sum_{I\subseteq[n]} \sigma_I(x) \prod_{i\in I}(1-x_i^2)$ of degree $\le r$, one has $f^{(r)} - f_{\min} = O(1/r^2)$ (Theorem 1.5/3.6, with explicit constant $C_f n^3/(r+1)^2$).

## Method
Reformulate via Lasserre's measure-based view: optimize over polynomial densities approximating the Dirac delta at a minimizer. Construct the density using the **Jackson kernel** (kernel polynomial method) expanded in Chebyshev polynomials of the first kind $T_k$; tensor univariate kernels for the multivariate case. The Fekete/Markov-Lukács theorem certifies that any nonnegative univariate polynomial on $[-1,1]$ admits a degree-tight Schmüdgen decomposition $\sigma_0 + (1-x^2)\sigma_1$, which makes the Jackson-kernel density feasible. The bound $f^{(r)}$ reduces to a generalized eigenvalue problem $A^I x = \lambda B^I x$ over subsets $I\subseteq[n]$ (Theorem 4.2), avoiding full SDP.

## Result
- $f^{(r)} - f_{\min} \le C_f n^3 / (r+1)^2$ with $C_f = (\sum_\alpha |f_\alpha|) C_d \pi^2 / 2$, where $f = \sum f_\alpha T_\alpha$ in the Chebyshev basis (Theorem 3.6).
- Improves prior rates $O(1/\sqrt{r})$ (SOS density + Lebesgue, de Klerk–Laurent–Sun 2014) and $O(1/r)$ (beta-distribution density on $[0,1]^n$, de Klerk–Lasserre–Laurent–Sun 2015).
- Jackson coefficients satisfy $|1-g_k^r| \le C_d \pi^2/(2(r+2)^2)$ (Lemma 2.2) — this is the $1/r^2$ source.
- Numerical tables (Booth, Matyas, Motzkin, Three-Hump, Styblinski-Tang, Rosenbrock) confirm $O(1/r^2)$ empirically; surprisingly $f^{(r)} \ge f_K^{(r)}$ in most examples, suggesting the SOS+Lebesgue bound may also be tighter than $O(1/\sqrt{r})$ in practice.

## Why it matters here
Direct lever for any Einstein Arena problem framable as polynomial minimization on a box (autocorrelation inequalities, low-degree functional inequalities, parameter-space scans for packing/kissing surrogate polynomials): swap Lebesgue for the Chebyshev arcsine measure and use Schmüdgen densities to get quartic-better convergence at the same degree, computable as a generalized eigenvalue rather than full SDP. Connects to the wiki's LP/SOS-bound machinery and the compute-router (eigenvalue problem, not SDP) lane.

## Open questions / connections
- Can the $O(1/\sqrt{r})$ analysis for SOS+Lebesgue densities on $[-1,1]^n$ be tightened to $O(1/r^2)$? (Numerics suggest yes.)
- Extension of the Jackson-kernel construction beyond the box — to the simplex, sphere, or general convex bodies with their natural orthogonal-polynomial measures?
- Trade-off: $2^n$ eigenvalue problems (one per $I\subseteq[n]$) of order $\binom{n+\lfloor r/2\rfloor-|I|}{n}$ — scaling to moderate $n$ for arena-relevant problem sizes?
- Connection to Putinar vs Schmüdgen representations: does the degree-tight univariate Fekete certificate generalize multivariately under the box's archimedean module?

## Key terms
Lasserre hierarchy, Schmüdgen positivstellensatz, Jackson kernel, Chebyshev polynomials, kernel polynomial method, sum-of-squares, polynomial optimization, generalized eigenvalue problem, Fekete-Markov-Lukács, box-constrained optimization, arcsine measure, measure-based upper bounds
