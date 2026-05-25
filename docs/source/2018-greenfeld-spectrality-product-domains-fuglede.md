---
type: source
kind: paper
title: Spectrality of product domains and Fuglede’s conjecture for convex polytopes
authors: Rachel Greenfeld, Nir Lev
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.02164
source_local: ../raw/2018-greenfeld-spectrality-product-domains-fuglede.pdf
topic: general-knowledge
cites:
---

# Spectrality of product domains and Fuglede's conjecture for convex polytopes

**Authors:** Rachel Greenfeld, Nir Lev  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.02164

## One-line
Proves that for a product set $\Omega = A \times B$ with $A$ a convex polygon in $\mathbb{R}^2$, $\Omega$ is spectral iff both $A$ and $B$ are spectral, thereby settling Fuglede's conjecture for decomposable convex polytopes in $\mathbb{R}^4$.

## Key claim
**Theorem 2.3:** If $A \subset \mathbb{R}^2$ is a convex polygon and $B \subset \mathbb{R}^m$ is bounded measurable, then $\Omega = A \times B$ is spectral iff $A$ and $B$ are both spectral. **Corollary 2.4:** Fuglede's conjecture (spectral $\Leftrightarrow$ tiles by translation) holds for decomposable convex polytopes in $\mathbb{R}^4$. **Theorem 2.1:** If $A \times B$ is spectral with $A$ a convex polytope, then $A$ must be centrally symmetric with centrally symmetric facets.

## Method
Introduces a new geometric object called a **"window"** $W$ for $A$ — a relaxation of the classical "orthogonal packing region" where the zero set $Z(\widehat{1_A})$ is replaced by a larger set $H(A)$ built from edge-translation conditions. Combines this with Kolountzakis' **cut-and-project** spectral-transfer theorem (Theorem 4.2), a weak-limit / translation-iteration argument to extract a spectrum $\Lambda$ satisfying $(\Lambda - \Lambda) \subset (H(A) \times \mathbb{R}^m) \cup (\mathbb{R}^2 \times Z(\widehat{1_B}))$ (Lemma 6.4), and a tiling-vs-packing measure inequality (Lemmas 3.1, 3.2) to force $|W| = |A|^{-1}$.

## Result
For any convex, centrally symmetric polygon $A \subset \mathbb{R}^2$: there exists a window $W$ with $|W| \geq |A|^{-1}$; with equality iff $A$ is a parallelogram or centrally symmetric hexagon, strict inequality otherwise (Theorem 7.2). Combined with Theorem 4.2, the strict inequality case is incompatible with spectrality, recovering the Iosevich–Katz–Tao 2003 classification (Corollary 7.4) as a byproduct. **Theorem 2.2:** If $A \subset \mathbb{R}^n$ ($n \geq 2$) is a centrally symmetric convex body with smooth boundary, then $A \times B$ is never spectral.

## Why it matters here
General background on the spectral-set / tiling correspondence — a Fourier-analytic structural result for product domains. No direct Einstein Arena tie; potentially informs P11/P15/P16-style packing/equioscillation problems via the tiling-spectrality dictionary, but the connection is indirect.

## Open questions / connections
- **Problem 8.1:** Extend to $A$ a convex polytope in $\mathbb{R}^n$, $n \geq 3$ — requires defining $H(A)$ correctly and proving an $n$-dim window-measure theorem.
- Conjectured 3D window theorem (Section 8.2) would yield a new proof of Greenfeld–Lev 2017 (Fuglede for convex polytopes in $\mathbb{R}^3$) and resolve Problem 8.1 for $n=3$.
- Extends Kolountzakis 2016 (interval × set; two-intervals × set) and Greenfeld–Lev 2016/2017 (cylindric / 3D polytope cases).

## Key terms
Fuglede conjecture, spectral set, tiling by translation, convex polytope, centrally symmetric, product domain, orthogonal packing region, window, cut-and-project, exponential basis, Iosevich-Katz-Tao, Kolountzakis, Greenfeld-Lev, centrally symmetric hexagon, parallelogram, decomposable polytope
