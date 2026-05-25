---
type: source
kind: paper
title: A tauberian theorem for the conformal bootstrap
authors: Jiaxin Qiao, S. Rychkov
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.00008
source_local: ../raw/2017-qiao-tauberian-theorem-conformal-bootstrap.pdf
topic: general-knowledge
cites:
---

# A tauberian theorem for the conformal bootstrap

**Authors:** Jiaxin Qiao, S. Rychkov  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.00008

## One-line
Rigorous tauberian theorem proving that the leading crossed-channel singularity of a 1d CFT 4pt function uniquely fixes the asymptotic spectral density of exchanged primaries.

## Key claim
For a non-negative spectral density $p(\Delta)$ with conformal-block expansion $G(z)=\int d\Delta\, p(\Delta) G_\Delta(z)$ obeying $G(1-x)\sim x^{-2\Delta_\phi}$ as $x\to 0$, the integrated density satisfies $Q(Y)=\int_0^Y d\Delta\, C(\Delta) p(\Delta) \sim (A\gamma)^{-1} Y^\gamma$ with $\gamma=4\Delta_\phi$ and $A=\Gamma(\gamma/2)^2/4$ — no further assumption needed.

## Method
Reduce conformal blocks at large $\Delta$ and small $x$ to a Bessel kernel $K_0(2\sqrt{x\Delta})$; recast the asymptotic relation as an additive convolution $\rho * W_1 \to 1$ in log variables. Prove $(W_1) \Rightarrow (W_2)$ via Fourier analysis: sandwich the discontinuous target weight $W_2$ between smooth $W_2^\pm$ whose Fourier transforms decay faster than $\hat W_1$, then invoke non-negativity of $\rho$. Simplification of Bochner/Wiener tauberian machinery; non-vanishing $\hat W_1$ is essential (a zero allows oscillating counterexamples $\rho=1+\cos(p_0 x)$).

## Result
Establishes (2.8) rigorously with prefactor $A=\Gamma(2\Delta_\phi)^2/4$, ruling out oscillating powerlaw behavior in $Q(Y)$. Includes self-contained re-proof of Hardy–Littlewood tauberian theorem, extension to unequal external dimensions, and application to large-$N$ gauge theories. Appendix F shows the same machinery upgrades the Fitzpatrick–Kaplan–Poland–Simmons-Duffin / Komargodski–Zhiboedov lightcone-bootstrap asymptotics for high-spin bounded-twist operators from heuristic to rigorous (modulo existence of the twist-space spectral density limit).

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: tauberian arguments are the rigorous tool for turning "leading singularity in dual channel" into "asymptotic density of states", a pattern that appears in LP-bound / Cohn–Elkies-style analyses and in any setting where a known transform asymptotic must be inverted to a spectral statement. Complements existing wiki content on LP duality and equioscillation as the spectral-side counterpart.

## Open questions / connections
- Existence of the twist-space spectral-density limit $\rho(\sigma)$ in eq. (F.17) for general CFTs — left open.
- Subleading-term control in tauberian theorems generally requires complex-analytic methods (Korevaar Ch. III); real-analysis approach here cannot extract subleading powerlaws of OPE coefficients/twists conjectured in [9, 10].
- Connection to Caron-Huot's analytic-in-spin inversion formula (1703.00278) as an alternative to tauberian routes.

## Key terms
tauberian theorem, conformal bootstrap, Hardy-Littlewood, Wiener, Bochner, Karamata, spectral density asymptotics, Bessel kernel K_0, conformal blocks, lightcone bootstrap, large spin, twist gap, Fourier convolution, OPE coefficients, generalized free theory, Mean Field Theory, 1d CFT, SL(2,R), Cardy formula, crossing symmetry
