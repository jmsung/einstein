---
type: source
kind: paper
title: An example concerning Fourier analytic criteria for translational tiling
authors: Nir Lev
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.09930
source_local: ../raw/2020-lev-example-concerning-fourier-analytic.pdf
topic: general-knowledge
cites:
---

# An example concerning Fourier analytic criteria for translational tiling

**Authors:** Nir Lev  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.09930

## One-line
Constructs a discrete set $\Lambda \subset \mathbb{R}$ (small perturbation of $\mathbb{Z}$) for which the Fourier zero set $Z(\hat f)$ alone cannot decide whether $f + \Lambda$ tiles $\mathbb{R}$, resolving negatively a long-standing sufficiency question.

## Key claim
**Theorem 1.2:** There exists $\Lambda \subset \mathbb{R}$ of bounded density such that for any real $w$, two real-valued $f, g \in L^1(\mathbb{R})$ exist with $Z(\hat f) = Z(\hat g)$, yet $f + \Lambda$ tiles at level $w$ while $g + \Lambda$ tiles at no level; if $w > 0$, both $f, g$ can be chosen positive. Hence the necessary condition $\operatorname{supp}(\widehat{\delta_\Lambda}) \setminus \{0\} \subset Z(\hat f)$ (Kolountzakis–Lev 2016) is **not sufficient** for non-lattice $\Lambda$.

## Method
Reduces tiling to **Malliavin's non-spectral synthesis** counterexample on $\mathbb{T}$: pick $S \in PM(\mathbb{T})$, $\varphi \in A(\mathbb{T})$ with $\varphi = 0$ on $\operatorname{supp}(S)$ but $\langle S, \varphi \rangle \neq 0$; build $\psi$ with the same zero set as $\varphi$ but smooth (so $S\psi = 0$). Construct $\Lambda$ via **Kargaev's implicit-function method** (Banach fixed-point on Fourier coefficients of $\alpha_n$, where $\lambda_n = n + \alpha_n$) so that $\widehat{\delta_\Lambda} = \delta_0 + r(S + \tilde S)$ on $(-b, b)$. Then $\hat f \cdot \widehat{\delta_\Lambda}$ kills the $S$-term (smooth $\psi$) but not the $S\varphi$-term.

## Result
- Main: counterexample $\Lambda$ exists with $|\lambda_n - n| \le \varepsilon$ for any $\varepsilon > 0$.
- **Corollary 1.3:** positive $f \in L^1(\mathbb{R})$ exists satisfying the Fourier necessary condition but not tiling.
- Extends to $\mathbb{R}^d$ via Cartesian products.
- **Theorem 5.1 (Kolountzakis addendum):** $\Lambda$ with $A \le \lambda_{n+1} - \lambda_n \le B$ exists admitting tilings only at level zero — hence no nonnegative tiler. The bounded-density $\Lambda$ from Theorem 1.2 is neither periodic nor a finite union of periodic sets; $f$ in Corollary 1.3 cannot have fast decay.

## Why it matters here
General background; no direct arena tie. Tangentially relevant to autocorrelation / uncertainty-style problems where Fourier-zero-set reasoning is invoked — this paper is a **cautionary boundary** showing that Fourier-support criteria characterize lattice tilings only, and break for perturbed-lattice translation sets. Worth citing if the agent ever leans on "Fourier zeros determine tiling" intuition near problems P4/P11/P17.

## Open questions / connections
- Extends Kolountzakis–Lev (2016) sufficiency question; closes it negatively.
- Builds on Kargaev (1982) implicit-function construction and Malliavin (1959) non-synthesis; KV92 (Kargaev–Volberg) supplies the smooth-function tail estimate.
- Leaves open: which **stronger** invariants of $f$ (beyond $Z(\hat f)$) characterize tiling by general bounded-density $\Lambda$?
- Connection to Fuglede/spectral-set conjectures via $A(\mathbb{T})$ / $PM(\mathbb{T})$ duality.

## Key terms
translational tiling, Fourier transform zero set, pseudomeasure, spectral synthesis, Malliavin counterexample, Kargaev implicit function method, bounded density discrete set, Poisson summation, Banach fixed-point, Wiener algebra $A(\mathbb{T})$, Kolountzakis–Lev, perturbed lattice
