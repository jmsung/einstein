---
type: source
kind: paper
title: A restriction estimate using polynomial partitioning
authors: L. Guth
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.1916
source_local: ../raw/2014-guth-restriction-estimate-using-polynomial.pdf
topic: general-knowledge
cites:
---

# A restriction estimate using polynomial partitioning

**Authors:** L. Guth  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.1916

## One-line
Guth imports polynomial partitioning from incidence geometry into harmonic analysis to push the 3D Fourier restriction exponent below the Wolff–Tao $10/3$ barrier.

## Key claim
For any smooth compact $S \subset \mathbb{R}^3$ with strictly positive second fundamental form, $\|E_S f\|_{L^p(\mathbb{R}^3)} \le C(p,S)\|f\|_{L^\infty(S)}$ holds for all $p > 13/4 = 3.25$, improving the previous threshold $56/17 \approx 3.29$ (Bourgain–Guth) and $10/3 \approx 3.33$ (Wolff/Tao), still short of Stein's conjectured $p > 3$.

## Method
Apply Stone–Tukey ham-sandwich polynomial partitioning (degree $D$) to the $L^{3.25}$ integral of the broad part $\mathrm{Br}_{K^{-\epsilon}} Ef$, splitting $B_R$ into $\sim D^3$ cells $O_i'$ plus a tubular wall $W$ around $Z(P)$. Cell contributions close by induction on radius (each $R^{1/2}$-tube enters $\le D+1$ cells); transverse-tube wall contributions close by induction on scales after sub-balling; tangential-tube contributions are bilinearised on $K^{-1}$-separated caps and bounded by Córdoba's $L^4$ square-root cancellation, exploiting that tangential tubes lie in a near-tangent plane. The geometric input is Lemma 4.1: an algebraic tangency lemma (via Bezout, Wongkew volume bound, Sard) showing a tube can be tangent to $Z(P)$ in only $\mathrm{Poly}(D)$ segments.

## Result
Theorem 0.3 (broad estimate, paraboloid): $\|\mathrm{Br}_{K^{-\epsilon}} E_S f\|_{L^{3.25}(B_R)} \le C_\epsilon R^\epsilon \|f\|_{L^2(S)}^{12/13} \|f\|_{L^\infty(S)}^{1/13}$, with exponent $3.25$ shown sharp via the planar example given this right-hand side. Theorem 0.1 follows by Bourgain–Guth's broad-to-linear reduction plus Tao's $\epsilon$-removal. A weighted variant $\|\mathrm{Br}\, Ef\|_{L^3} \lesssim \|f\|_2^{2/3}\|f\|_\infty^{1/3}$ is conjectured plausible.

## Why it matters here
General background; no direct arena tie — the 23 Einstein problems do not include Fourier restriction. Methodologically relevant as the canonical example of polynomial partitioning + induction-on-scales + bilinear/broad reduction extending from incidence geometry to analytic estimates, which informs the wiki's polynomial-method and ham-sandwich entries that may inform sphere-packing / kissing / autocorrelation LP-bound work (e.g., as scaffolding for Cohn–Elkies and related dual problems).

## Open questions / connections
- Can the exponent be pushed below $3.25$ by weighting $\|f\|_\infty$ more heavily (e.g., the conjectured $L^3$ bound with $f^{2/3}_2 f^{1/3}_\infty$)?
- Does polynomial partitioning extend to higher-dimensional restriction (paraboloid in $\mathbb{R}^n$, $n \ge 4$) and to the Kakeya conjecture proper?
- Connects to Dvir's finite-field Kakeya, Guth–Katz Erdős distinct distances, and Wolff's Kakeya hairbrush — all polynomial-method milestones still leaving the Euclidean Kakeya/restriction conjectures open.

## Key terms
Fourier restriction, polynomial partitioning, ham sandwich theorem, paraboloid, wave packet decomposition, broad points, bilinear restriction, induction on scales, Kakeya conjecture, Wongkew volume bound, Bezout's theorem, Córdoba $L^4$, Guth, Wolff, Tao, Bourgain
