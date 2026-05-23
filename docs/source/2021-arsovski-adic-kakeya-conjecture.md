---
type: source
kind: paper
title: The $p$-adic Kakeya conjecture
authors: Bodan Arsovski
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.03750
source_local: ../raw/2021-arsovski-adic-kakeya-conjecture.pdf
topic: general-knowledge
cites:
---

# The $p$-adic Kakeya conjecture

**Authors:** Bodan Arsovski  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.03750

## One-line
Proves the Kakeya conjecture over $\mathbb{Q}_p$: every bounded subset of $\mathbb{Q}_p^n$ containing a unit line segment in every direction has Hausdorff and Minkowski dimension $n$.

## Key claim
Theorem 1: For every prime $p$ and positive integer $n$, all Kakeya sets in $\mathbb{Q}_p^n$ have Hausdorff and Minkowski dimension $n$. Quantitatively (Theorem 5), an $(\varepsilon,\delta)$-Kakeya set in $\mathbb{Z}_p^n$ cannot be covered by fewer than $\varepsilon\delta q / p^{nk} \cdot \binom{n}{n+\cdots}^{-1}$-order balls of radius $p^{-k}$, i.e. $\gtrsim_{p,n} (\varepsilon\delta) p^{kn}/k^{3n}$.

## Method
Polynomial method over discrete valuation rings — a $p$-adic lift of Dvir's finite-field Kakeya proof. The key tool is a **discrete-valuation Schwartz–Zippel lemma** (Lemma 6) bounding the number of points $s\in C^n$ (where $C=\{(1+t)^l\}\subset \mathbb{F}_p[t]$) on which a polynomial $f$ has anomalously high $t$-adic valuation. Lines in $\mathbb{Q}_p^n$ are encoded via the map $\lambda\mapsto \zeta^\lambda$ for $\zeta$ a $q$th root of unity, transferring direction information into the valuation ring $T=\mathbb{Z}_p[\zeta][t]$ reduced mod $(\zeta-1)$; a low-degree polynomial vanishing on the encoded set is forced into contradiction with the Schwartz–Zippel bound. Bourgain's dyadic pigeonhole upgrades the covering bound to a dimension statement.

## Result
For any $\varepsilon,\delta>0$, every $(\varepsilon,\delta)$-Kakeya set in $\mathbb{Z}_p^n$ requires $\gtrsim_{p,n} (\varepsilon\delta) p^{kn}/k^{3n}$ closed balls of radius $p^{-k}$ to cover, with the polynomial $k^{3n}$ loss absorbed by Bourgain's dyadic method to yield full dimension $n$. The proof generalizes immediately to any finite extension $K/\mathbb{Q}_p$ by viewing $K^n$ as a $\mathbb{Q}_p$-vector space (Remark 2). The $\mathbb{F}_q((t))$ analogue is **not** settled by this paper.

## Why it matters here
General background; no direct arena tie. The discrete-valuation polynomial method may be a transferable tool for extremal/incidence problems over $\mathbb{Z}/p^k\mathbb{Z}$ or $p$-adic moduli, which could touch combinatorial-geometry problems (kissing, packing, autocorrelation lattices) only in indirect, theoretical ways.

## Open questions / connections
- Does the discrete-valuation polynomial method extend to $\mathbb{F}_q((t))^n$ (the other natural multi-scale local field setting)?
- Can the constants $k^{3n}$ in the covering bound be sharpened — the author flags they are deliberately loose for exposition; Dhar–Dvir [DD] give better constants.
- Extends Dvir [Dvi09] (finite-field Kakeya) and Dummit–Hablicsek [DH11] ($n=2$ over $\mathbb{Q}_p$, $\mathbb{F}_q((t))$); leaves open the classical Kakeya conjecture over $\mathbb{R}$ for $n\geq 3$.
- Does the technique apply to Kakeya-maximal-function and Fourier restriction problems over $p$-adic local fields (Hickman–Wright [HW18])?

## Key terms
Kakeya conjecture, p-adic numbers, polynomial method, Dvir, discrete valuation ring, Schwartz–Zippel lemma, Hausdorff dimension, Minkowski dimension, Besicovitch set, finite-field Kakeya, Bourgain dyadic method, local fields, $\mathbb{Q}_p$, roots of unity lift, Lagrange interpolation, Kummer's theorem
