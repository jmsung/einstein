---
type: source
kind: paper
title: Littlewood’s Problem for Sets with Multidimensional Structure
authors: Brandon Hanson
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.01561
source_local: ../raw/2020-hanson-littlewood-problem-sets-multidimensional.pdf
topic: general-knowledge
cites:
---

# Littlewood's Problem for Sets with Multidimensional Structure

**Authors:** Brandon Hanson  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.01561

## One-line
Sharpens the McGehee–Pigno–Smith / Konyagin lower bound on the $L^1$-norm of exponential sums $\sum_{a\in A} e(at)$ when the set $A$ carries genuine multidimensional structure (either as a lattice subset or as a multiscale subset of $\mathbb{Z}$).

## Key claim
For an $(n_1,\dots,n_r)$-strongly $r$-dimensional $A\subseteq \mathbb{Z}^r$, $\int_{[0,1]^r}|\sum_{a\in A} e(a\cdot t)|\,dt \geq C_{\mathrm{MPS}}^{r}\log(n_1)\cdots\log(n_r)$ (Thm 1.3); the same $\prod \log(n_i)$ lower bound holds for $(\delta_1,\dots,\delta_{r-1};n_1,\dots,n_r)$-strongly $r$-dimensional subsets of $\mathbb{Z}$ with explicit constant $C^r_{\mathrm{MPS}}(2^9\pi)^{-r}\prod(2+\log(1+2/\delta_j))^{-1}$ (Thm 1.4). Both bounds are sharp up to the constant.

## Method
Fibre/projection induction in $\mathbb{Z}^r$: view $\sum_{a\in A}e(a\cdot t)$ as a trigonometric polynomial in $t_1$ with fibre-sum coefficients, then apply the McGehee–Pigno–Smith generalized Hardy inequality and iterate. For $\mathbb{Z}$-subsets with multiscale (gap $d_2>(2+\delta)d_1$) structure, amplify gaps using a smoothed Dirichlet–Fejér kernel $K_{M,N}=\frac{1}{M}D_{N+M}F_{M-1}$ (Lem 3.3) restricted to a residue class $I(q;s)$ chosen via a pigeonhole/dyadic argument ($|I|^{1/3}/8\le |I(q;s)|\le q^{1/2}$, Lem 3.6), then apply MPS again after Riemann-sum discretization (Bernstein + Koksma).

## Result
Improves Petridis's Theorem 1.2/1.3: the lower bound scales as $\prod_{i=1}^{r}\log(n_i)$ rather than a single $\log$, matching the trivial upper bound from an $r$-dimensional arithmetic progression (Shao Thm 3.3). Constants are made fully explicit, including the dependence on the multiscale gap parameters $\delta_j$ through $(2+\log(1+2/\delta_j))^{-1}$. Theorem 1.4 extends to $r=2$, a case Petridis's Freiman-isomorphism approach did not cover, under the size condition $n_i\ge \pi 32^2 \cdot 21 C_{\mathrm{MPS}}^3 \prod_{j\ge i}(\log n_j)^3$.

## Why it matters here
General background; no direct arena tie. Closest contact is autocorrelation/exponential-sum problems (P14-family): the MPS-type $L^1$ lower bound is the analytic foundation behind "additive structure shows up in low $L^p$-norms", which is the dual to the autocorrelation/Sidon framing used in arena problems.

## Open questions / connections
- Sharp constant in Littlewood's conjecture (1) — proving $C=1$ asymptotically remains open; this paper only sharpens the $n_i$-dependence, not the absolute constant.
- Inverse Littlewood problem (Green): characterize all $A$ with $\|F\|_1 \le C\log N$ — Thm 1.4 gives a multiscale-structure sufficient condition; necessity remains open.
- Extends Petridis (2013) [P] and complements Shao (2013) [S] on generalized APs; uses MPS (1981) and Konyagin (1981) as black boxes.

## Key terms
Littlewood conjecture, L1 norm exponential sums, McGehee-Pigno-Smith, Konyagin, generalized Hardy inequality, Bernstein inequality, Dirichlet kernel, Fejér kernel, generalized arithmetic progression, Freiman isomorphism, additive combinatorics, multiscale structure, Petridis, Hanson, fibre projection induction
