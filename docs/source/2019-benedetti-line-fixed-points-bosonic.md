---
type: source
kind: paper
title: Line of fixed points in a bosonic tensor model
authors: D. Benedetti, R. Gurau, Sabine Harribey
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.03578
source_local: ../raw/2019-benedetti-line-fixed-points-bosonic.pdf
topic: general-knowledge
cites:
---

# Line of fixed points in a bosonic tensor model

**Authors:** D. Benedetti, R. Gurau, Sabine Harribey  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.03578

## One-line
Rigorous Wilsonian RG analysis of the $O(N)^3$ Klebanov–Tarnopolsky bosonic tensor model in $d<4$ with a modified covariance $(-\Delta)^{d/4}$, proving the existence of an IR-attractive line of conformal fixed points at purely imaginary tetrahedral coupling.

## Key claim
At large $N$ but **non-perturbatively** in the couplings, the beta functions for the pillow and double-trace couplings truncate to quadratic order; the model has four lines of fixed points parameterized by the tetrahedral coupling $\lambda$, and for purely imaginary $\lambda$ one of these is a real, IR-attractive CFT with real spectrum of bilinear operators (for $|g|<g_*$).

## Method
Wilsonian RG with a UV cutoff $\Lambda$ and IR cutoff $k$, using a free covariance $C(p)=1/p^{2\zeta}$ with $\zeta=d/4$ tuned to the IR conformal scaling — interactions are exactly marginal in any $d<4$, removing the $\epsilon$-expansion crutch. The 2PI effective action plus the melonic large-$N$ limit (only melon-tadpole graphs survive) yields closed Schwinger–Dyson equations; BPHZ-style forest subtractions ($R_S, R_U$ operators on ladder/cap generating functions) renormalize the four-point amplitudes. Bilinear spectrum extracted from the Bethe–Salpeter eigenvalue equation $f(h)=1$ with kernel $K=3\lambda^2 G(x_{13})G(x_{24})G(x_{34})^2$.

## Result
Beta functions are exactly quadratic: $\beta_{g_1}=\beta_0^g - 2\beta_1^g g_1 + \beta_2^g g_1^2$ (and similarly for $g_2$ with $g\to\sqrt{3}g$); fixed points $g_{1\pm}=\pm\sqrt{-g^2}+O(g^2)$ with critical exponent $\pm\sqrt{-g^2}\cdot 4\Gamma(d/4)^2/\Gamma(d/2)+O(g^3)$. Tetrahedral coupling has zero beta function ($\beta_g=0$); bare-to-renormalized relation $\lambda=gZ^2$ with $Z=1/(1-g^2/g_c^2)$ is invertible for $|g|<g_c$ (real) or $|g|<g_c/\sqrt{3}$ (imaginary). Bilinear spectrum: $h_{0\pm}=d/2\pm 2\sqrt{3}\,\Gamma(d/4)^2/\Gamma(d/2)\cdot g+O(g^3)$, $h_n=d/2+2n+\alpha_n g^2+O(g^3)$; real for imaginary $g$ with $|g|<g_*$, complex above $g_*$ (signaling spontaneous conformal symmetry breaking via AdS Breitenlohner–Freedman violation $m^2<-d^2/4$). In $d=3$, $g_*\approx 0.186$ with the transition merging $h_{0+}$ and $h_1$.

## Why it matters here
General background; no direct arena tie. Of methodological interest: demonstrates that an unconventional choice (imaginary coupling) renders an otherwise-unstable theory real and well-defined — an analog of the "consider imaginary parameter" move that occasionally unblocks extremal problems (e.g. Cohn–Elkies via imaginary contour, LP duality with complex multipliers). Also a clean example of **non-perturbative truncation of a beta function** to finite polynomial order via large-$N$, which is the kind of rigidity occasionally exploitable in autocorrelation/functional-inequality fixed-point problems.

## Open questions / connections
- Does the mass bilinear acquire a nonzero VEV at $g^2>0$, producing spontaneous breaking of conformal invariance (analog of $\phi^6$ in $d=3$, Bardeen–Moshe–Bander 1984)? Postponed in this paper.
- Extension to the analog of the Kim–Klebanov–Tarnopolsky–Zhao [arXiv:1902.02287] coupled SYK/tensor symmetry-breaking conjecture in $d>1$.
- AdS/CFT interpretation: complex dimensions at $g^2<-g_*^2$ may correspond to bulk fields with $\mathrm{Im}(m^2)\neq 0$, but the model is only RG-defined for $|g|\leq g_0\leq g_*$, so this regime may be unphysical.
- Rigorous RG derivation of the bilinear spectrum (this paper uses CFT/BSE methods less rigorous than the rest).

## Key terms
melonic large-N limit, O(N)^3 tensor model, Klebanov–Tarnopolsky, Carrozza–Tanasa, Wilsonian renormalization group, 2PI effective action, Bethe–Salpeter equation, Schwinger–Dyson equation, tetrahedral coupling, pillow coupling, double-trace coupling, fixed point, imaginary coupling, Breitenlohner–Freedman bound, SYK model, conformal dimension, bilinear operators, BPHZ subtraction, forest formula, anomalous dimension, AdS/CFT
