---
type: source
kind: paper
title: Stable polynomials and crystalline measures
authors: P. Kurasov, P. Sarnak
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.05678
source_local: ../raw/2020-kurasov-stable-polynomials-crystalline-measures.pdf
topic: general-knowledge
cites:
---

# Stable polynomials and crystalline measures

**Authors:** P. Kurasov, P. Sarnak  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.05678

## One-line
Constructs explicit positive Fourier quasicrystals from pairs of multivariate stable polynomials, resolving several open questions about crystalline measures that are not generalized Dirac combs.

## Key claim
For any "stable pair" $(P,Q)$ of $D$-stable multivariate polynomials satisfying a functional equation, and parameters $b_1,\dots,b_n>1$, the measure $\mu_P=\sum_{\gamma:F(i\gamma)=0}\delta_\gamma$ (where $F(s)=P(b_1^{-s},\dots,b_n^{-s})$) is a positive crystalline measure and a Fourier quasicrystal; for the explicit example $P(z_1,z_2)=1-\tfrac{1}{3}z_1-\tfrac{1}{3}z_2^2-z_1z_2^2$ with $\xi_1/\xi_2 \notin \mathbb{Q}$, $\mu$ is a positive idempotent ($a_\lambda=1$), $\dim_{\mathbb{Q}}\Lambda=\infty$, $\dim_{\mathbb{Q}}S=2$, $\Lambda$ is Delone but $S$ is not, and every arithmetic progression meets $\Lambda$ in finitely many points.

## Method
A summation formula is derived by contour-shifting the integral $\frac{1}{2\pi i}\int F'/F \cdot \tilde\Psi\,ds$ and applying the functional equation $F(-s)=\eta^{-1}b^{\ell s}G(s)$ that links the stable pair; logarithmic-derivative expansions on both sides yield a Poisson-type identity whose left side sums over zeros (on $i\mathbb{R}$ by stability) and right side is a discrete Dirichlet-series spectrum. Boundedness of $\arg P$ on $D^n$ and a mean-value bound on $\log|P|$ give $|c_P(k)| \le C$, making $|\hat\mu|$ tempered. The additive structure of $\Lambda$ in the explicit example is analyzed via Liardet's theorem (Lang's conjecture in dimension two) on intersections of algebraic subvarieties with division groups of finitely generated subgroups of $(\mathbb{C}^*)^2$.

## Result
Theorem 1: every stable pair yields a positive Fourier quasicrystal that is almost periodic. Theorem 2 (explicit lasso-graph example): produces a Delone-support, non-Delone-spectrum positive idempotent Fourier quasicrystal that is provably not a generalized Dirac comb, simultaneously answering open questions of Meyer (last question in [25]), Lev–Olevskii (Q11.2 parts 2,3 in [22]), and Lagarias (Problem 4.4 in [15]). Theorem 3 (announced): general structure $\Lambda = L_1 \sqcup \cdots \sqcup L_\nu \sqcup N$ with $L_i$ arithmetic progressions and $N$ infinite-dimensional over $\mathbb{Q}$, with $\dim_{\mathbb{Q}}S=\dim_{\mathbb{Q}}\{\xi_1,\dots,\xi_n\}$ and finitely many $N$-hits per arithmetic progression.

## Why it matters here
General background; no direct arena tie. The summation-formula machinery (stable-polynomial Dirichlet series with zeros on the imaginary axis, Poisson-type identity from a functional equation) is structurally adjacent to autocorrelation/uncertainty-principle problems where one designs functions whose zero set and Fourier support are simultaneously controlled — same toolkit family as Cohn–Elkies / Radchenko–Viazovska magic functions used in sphere packing and kissing-number bounds.

## Open questions / connections
- Extends Lev–Olevskii [20–22] and Meyer [24,25] classification program; complements Radchenko–Viazovska Fourier interpolation [27] which also lives in the "discrete-support + discrete-spectrum" world.
- Companion paper Kurasov–Sarnak [14] (additive structure of metric-graph spectra) carries the higher-dimensional Diophantine arguments needed for Theorem 3.
- Open: can one classify *all* positive crystalline measures, or characterize which stable pairs give a non-Dirac-comb $\mu$? Lemma 5 of [25] constrains $S \cap (0,\infty)$ to be $\mathbb{Q}$-dependent — what is the exact rank?
- Connection to Lee–Yang polynomials [19,28] and to secular polynomials of quantum graphs [1,3,10,12,13] as the two main sources of stable pairs.

## Key terms
stable polynomial, Fourier quasicrystal, crystalline measure, generalized Dirac comb, Poisson summation formula, Lee–Yang theorem, quantum graph secular polynomial, Lang conjecture, Liardet theorem, Delone set, Meyer theorem, Cohn–Elkies, Radchenko–Viazovska, Kronecker density, multiplicative subgroup division group
