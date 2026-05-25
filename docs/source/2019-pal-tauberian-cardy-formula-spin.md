---
type: source
kind: paper
title: Tauberian-Cardy formula with spin
authors: Sridip Pal, Zheng Sun
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1910.07727
source_local: ../raw/2019-pal-tauberian-cardy-formula-spin.pdf
topic: general-knowledge
cites:
---

# Tauberian-Cardy formula with spin

**Authors:** Sridip Pal, Zheng Sun  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1910.07727

## One-line
Proves a 2D Tauberian theorem extending the Cardy formula to the $(h,\bar h)$ plane, yielding rigorous spin-sensitive asymptotic density of states for 2D CFTs with controlled error terms.

## Key claim
For 2D CFTs at finite central charge $c$, the integrated density of states satisfies $F(h,\bar h) = \frac{1}{4\pi^2}\sqrt{\frac{36}{c^2 h\bar h}} \exp\!\left(2\pi\sqrt{c h/6}+2\pi\sqrt{c\bar h/6}\right)\bigl(1+O(\tau^{-1/4})\bigr)$ where $\tau = 2\min(h,\bar h)$ is the twist; the error is controlled by twist, not spin. An "areal gap" inequality $A g \le \pi(c-1)r^2/24$ with $r = 4\sqrt{3}/\pi \approx 2.21$ is proved for compact unitary 2D CFTs without conserved currents, where $g$ is the twist gap and $A$ the minimal areal spectral gap.

## Method
Two-dimensional Tauberian analysis applied to the modular-invariant torus partition function, splitting into light/heavy sectors à la Hartman-Keller-Stoica. Uses bandlimited "magic" test functions $\Phi_\pm$ (Beurling–Selberg type, following Mukhametzhanov–Zhiboedov) to bound contour integrals via saddle-point evaluation at $\beta=\pi\sqrt{c/(6h)}$, $\bar\beta = \pi\sqrt{c/(6\bar h)}$. The areal-gap bound comes from circumscribing squares with circles on the $(h,\bar h)$ lattice.

## Result
- Spin-sensitive Cardy with error $O(\tau^{-1/4})$ when $h/\bar h = O(1)$; extends to $h = \bar h^\upsilon$ with $1/2 < \upsilon < 2$ under a twist gap, error $O(\tau^{\Upsilon/4 - 1/2})$.
- For $\Upsilon \ge 2$: error degrades to $O(\tau^{-3/4})$ on the exponential (no polynomial prefactor trusted).
- Asymptotic twist gap $\le 8\sqrt{3}/\pi \approx 4.42$ along the diagonal; $\le 2\sqrt{2}$ with conjectural improvement to optimal value 2 (saturated by Monster $\otimes$ anti-Monster).
- Windowed microcanonical entropy with universal $\sinh$-correction at large bin size.
- For holographic ($c\to\infty$, $h = c\epsilon + 1/24$): Cardy regime valid for $\epsilon, \bar\epsilon > 1/6$ (slightly weaker than HKS's $1/24$); twist gap $g$ improves this.
- Finite-twist large-spin: upper bound only; reproduces lightcone-bootstrap $(h - (c-1)/24)^{3/2}$ square-root edge.

## Why it matters here
General background; no direct arena tie. The Tauberian-with-error-bar machinery (bandlimited test functions, saddle-point error control on lattice counting) is methodologically transferable to LP/SDP-bound arguments for sphere packing, kissing numbers, and autocorrelation problems — the Cohn–Elkies and modular-bootstrap programs share infrastructure (magic functions, dual-pair extremization).

## Open questions / connections
- Can $r$ in the areal-gap bound be reduced to $1$ (optimal) via better magic functions or sharper heavy-sector estimates? Would tighten the proposed $(c-1)/16$ twist-gap bound of Benjamin–Ooguri–Shao–Wang.
- Lower bound on finite-twist large-spin density of states matching lightcone bootstrap [Kusuki; Maxfield; Benjamin et al.] — current attempts give negative coefficients.
- Extending to spin-sensitive asymptotic OPE coefficients and reaching the HKS sparseness threshold $\epsilon_*\bar\epsilon_* > 1/(24)^2$ rigorously.

## Key terms
Tauberian theorem, Cardy formula, 2D CFT, modular bootstrap, twist gap, conformal weights, lightcone bootstrap, areal spectral gap, magic functions, Beurling-Selberg, Hartman-Keller-Stoica, holographic CFT, Mukhametzhanov-Zhiboedov, microcanonical entropy, conserved currents
