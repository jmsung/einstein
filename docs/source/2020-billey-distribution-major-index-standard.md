---
type: source
kind: paper
title: On the distribution of the major index on standard Young tableaux
authors: Sara C. Billey, M. Konvalinka, Joshua P. Swanson
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.10341
source_local: ../raw/2020-billey-distribution-major-index-standard.pdf
topic: general-knowledge
cites:
---

# On the distribution of the major index on standard Young tableaux

**Authors:** Sara C. Billey, M. Konvalinka, Joshua P. Swanson  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.10341

## One-line
Extended abstract classifying zeros, asymptotic limit laws, and unimodality structure of the major-index distribution on standard Young tableaux of straight and certain skew shapes.

## Key claim
For $\lambda \vdash n$, the fake-degree coefficient $b_{\lambda,k} > 0$ for all $b(\lambda) \le k \le \binom{n}{2} - b(\lambda')$ except two endpoint-adjacent values when $\lambda$ is a rectangle; and the normalized $\mathrm{maj}$ statistic on $\mathrm{SYT}(\lambda^{(N)})$ converges to the standard normal iff $\mathrm{aft}(\lambda^{(N)}) \to \infty$, otherwise to an Irwin–Hall $IH_M^*$ or a discrete limit.

## Method
Three-pronged: (i) explicit shape-preserving rotation/block maps $\varphi: \mathrm{SYT}(\lambda)\setminus E(\lambda) \to \mathrm{SYT}(\lambda)$ with $\mathrm{maj}(\varphi(T)) = \mathrm{maj}(T)+1$ to fill the support; (ii) method of moments via a clean cumulant formula $\kappa_d^\lambda = \frac{B_d}{d}\bigl(\sum_{j=1}^n j^d - \sum_{c\in\lambda} h_c^d\bigr)$ derived from Stanley's hook-product formula $\mathrm{SYT}(\lambda)_{\mathrm{maj}}(q) = q^{b(\lambda)}[n]_q!/\prod_c [h_c]_q$; (iii) Fréchet–Shohat / cumulant estimates bounding $|\sum j^d - \sum h_c^d| = \Theta(\mathrm{aft}(\lambda)\cdot n^d)$.

## Result
Theorem 2.1 settles internal zeros for straight shapes (and extends via Shephard–Todd $G(m,d,n)$ coinvariants in equation (3)). Theorem 3.3 / 3.8 give the trichotomy of limit laws governed by $\mathrm{aft}(\lambda) := |\lambda| - \max(\lambda_1, \lambda'_1)$: normal if $\mathrm{aft}\to\infty$, $IH_M^*$ if $\mathrm{aft}\to M<\infty$ with $|\lambda|\to\infty$, discrete eventually-constant otherwise. Normalized cumulants scale as $|\kappa_d^{\lambda*}| = \Theta(\mathrm{aft}(\lambda)^{1-d/2})$.

## Why it matters here
General background; no direct arena tie. The cumulant-via-hook-lengths technique and the $\mathrm{aft}$ statistic as the "effective dimension" controlling Gaussian vs. Irwin–Hall limits offer a transferable template for any arena problem whose distribution is parameterized by a shape/multiset where one parameter dominates (sphere packing rank profiles, autocorrelation descent statistics).

## Open questions / connections
- Conjecture 4.1: $\mathrm{SYT}(\lambda)_{\mathrm{maj}}(q)$ unimodal whenever $\lambda$ has $\ge 4$ corners.
- Conjecture 4.2: local limit theorem with $O(1/(\sigma_\lambda \mathrm{aft}(\lambda)))$ error bound.
- Conjecture 4.3: fake-degree polynomials are parity-unimodal for all $\lambda$ (extends Stucky's $q$-Catalan result via $\mathfrak{sl}_2$ on rational Cherednik algebras).
- Extends Canfield–Janson–Zeilberger (words), Chen–Wang–Wang ($q$-Catalan), Klyachko (modular major index); relates to Church–Farb representation stability.

## Key terms
major index, standard Young tableaux, fake degree, hook length formula, aft statistic, asymptotic normality, Irwin–Hall distribution, method of moments, cumulants, Bernoulli numbers, Shephard–Todd groups, coinvariant algebra, unimodality, parity-unimodality, q-Catalan, Stanley hook formula, MacMahon
