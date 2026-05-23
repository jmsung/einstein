---
type: source
kind: paper
title: Fourier Uniqueness and Non-Uniqueness Pairs
authors: A. Kulikov, F. Nazarov, M. Sodin
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2306.14013
source_local: ../raw/2023-kulikov-fourier-uniqueness-non-uniqueness-pairs.pdf
topic: general-knowledge
cites:
---

# Fourier Uniqueness and Non-Uniqueness Pairs

**Authors:** A. Kulikov, F. Nazarov, M. Sodin  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2306.14013

## One-line
Gives near-tight density conditions on discrete pairs $(\Lambda, M) \subset \mathbb{R}^2$ that force a Schwartz function vanishing on $\Lambda$ with Fourier transform vanishing on $M$ to be identically zero, generalizing the Radchenko–Viazovska interpolation phenomenon via real-variable (Poincaré–Wirtinger) rather than modular-forms methods.

## Key claim
For conjugate exponents $1<p,q<\infty$, $1/p+1/q=1$: if $\limsup_{|j|\to\infty} |\lambda_j|^{p-1}(\lambda_{j+1}-\lambda_j) < 1/2$ and the analogous $q$-bound holds for $M$ (**supercritical**), then $(\Lambda,M)$ is a uniqueness pair for $\mathcal{S}$; if both $\liminf$s exceed $1/2$ (**subcritical**), it is a non-uniqueness pair. The threshold $a^{1/p} b^{1/q} \lessgtr 1/2$ is sharp up to the boundary.

## Method
Uniqueness proved via a quantitative Poincaré–Wirtinger / trace inequality (Lemmas 1–3) bounding $\int |f|^2$ by gap-sums of $|f(\lambda_j)|^2$ and $\int \xi^2|\hat f|^2$, iterated against the Fourier-Plancherel duality to force $f\equiv 0$; works in a Hilbert space $H \supset \mathcal{S}$ defined by $f, \hat f \in H^1$. Non-uniqueness constructed via Levin's entire-function theory: build $\Phi$ with prescribed zeros of density matching the gap density using a $p$-trigonometrically convex indicator $k_p \in K_p$ (Brelot–Hadamard / Weierstrass products), then bound $\hat F_\lambda$ by Phragmén–Lindelöf + saddle-point in Young's-inequality form. Yields quantitative frame bound → interpolation formula → crystalline measures.

## Result
Theorem 1 (sharp density dichotomy) plus Theorem 2 (frame-equivalence): $\|f\|_{H_{s,p,q}}^2 \asymp \sum_\Lambda (1+|\lambda|)^{(2s-1)p+1}|f(\lambda)|^2 + \sum_M (1+|\mu|)^{(2s-1)q+1}|\hat f(\mu)|^2$. Corollary 2 produces an explicit interpolation formula $f = \sum f(\lambda)a_\lambda + \sum \hat f(\mu) b_\mu$ converging in $H_{s,p,q}$. Corollary 3: every supercritical pair supports an infinite-dimensional space of crystalline measures (tempered distributions with discrete support and discrete Fourier transform). Recovers Radchenko–Viazovska ($p=q=2$, $\Lambda=M=\{\pm\sqrt{n}\}$) and improves Ramos–Sousa's $\alpha < 1 - \sqrt{2}/2$ to the full range $\alpha < 1/2$.

## Why it matters here
Direct ammunition for the **autocorrelation / uncertainty / Fourier-extremal** problem family on Einstein Arena (P5, P6, P11, P14, P17 use Fourier-side constraints; equioscillation / Beurling–Selberg / Cohn–Elkies sit nearby). Provides a real-analytic, non-modular construction route for "magic functions" and explicit interpolation kernels — useful when the arithmetic Viazovska route is too rigid for a given problem geometry.

## Open questions / connections
- Boundary case $a^{1/p}b^{1/q} = 1/2$ — uniqueness or not? (Radchenko–Viazovska sits exactly here at $p=q=2$, $a=1$.)
- Schwartz-topology convergence of the interpolation formula (authors note their $a_\lambda, b_\mu$ depend on $s$ and they don't know $\mathcal{S}$-convergent versions).
- Extends/sharpens Ramos–Sousa (analytic) and recovers Radchenko–Viazovska (modular); multi-dimensional analogs by Adve, Ramos–Stoller, Viazovska remain less precise.
- Crystalline-measure construction connects to Kurasov–Sarnak, Lev–Reti, Meyer, Olevskii–Ulanovskii one-dimensional quasicrystal program.

## Key terms
Fourier uniqueness pair, Fourier interpolation, Radchenko-Viazovska, Poincaré-Wirtinger inequality, Schwartz space, Sobolev space $H^1$, supercritical density, conjugate exponents, crystalline measure, quasicrystal, Beurling-Malliavin, Phragmén-Lindelöf, $p$-trigonometric indicator, Levin entire function theory, Gelfand-Shilov space, frame bound, Cohn-Elkies magic function, Ramos-Sousa
