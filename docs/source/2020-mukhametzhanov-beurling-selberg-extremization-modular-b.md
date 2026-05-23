---
type: source
kind: paper
title: Beurling-Selberg extremization and modular bootstrap at high energies
authors: Baur Mukhametzhanov, Sridip Pal
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.14316
source_local: ../raw/2020-mukhametzhanov-beurling-selberg-extremization-modular-b.pdf
topic: general-knowledge
cites:
---

# Beurling-Selberg extremization and modular bootstrap at high energies

**Authors:** Baur Mukhametzhanov, Sridip Pal  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.14316

## One-line
Solves the optimization of upper/lower bounds on the number of operators in a window $[\Delta-\delta,\Delta+\delta]$ at asymptotically large $\Delta$ in 2d unitary modular-invariant CFTs by recognizing it as the classical Beurling-Selberg extremal problem.

## Key claim
At asymptotically large $\Delta$, the windowed operator count obeys $2\pi\hat\phi_-(0)\rho_0(\Delta) \le \int_{\Delta-\delta}^{\Delta+\delta}\rho(\Delta')d\Delta' \le 2\pi\hat\phi_+(0)\rho_0(\Delta)$, with the simple form $(2\delta-1)\rho_0(\Delta) \le N_\delta(\Delta) \le (2\delta+1)\rho_0(\Delta)$ optimal whenever $2\delta\in\mathbb{Z}$, where $\rho_0(\Delta) = (c/48\Delta^3)^{1/4}\exp(2\pi\sqrt{c\Delta/3})$.

## Method
Modular invariance + light/heavy splitting reduces the bound to choosing bandlimited majorants/minorants $\phi_\pm(x)$ of the indicator $\theta_{[-\delta,\delta]}(x)$ with Fourier support $|t|<2\pi$ (the shortest possible recurrence time); minimizing $\|\phi_\pm - \theta\|_{L^1}$ is the Beurling-Selberg problem. For $2\delta\in\mathbb{Z}$ Selberg's explicit extremal functions built from $\sin^2(\pi x)/\pi^2$ with double poles at integers/half-integers attain the Poisson-summation bound; for $2\delta\notin\mathbb{Z}$ Littmann's generalized Poisson summation with transcendental nodes $x_n$ (roots of $x\sin(\pi x) - \gamma\cos(\pi x) = 0$ etc.) gives strictly sharper bounds.

## Result
For $2\delta\in\mathbb{Z}_{\ge 0}$ the $(2\delta\pm 1)\rho_0(\Delta)$ bounds are saturated by integer-spaced-spectrum partition functions at $c=4k$, e.g. $j(\tau)^{1/3}$, $j(\tau)-744$, and $j^{a/3}P_k(j)$ for $a\in\{0,1,2\}, k\in\mathbb{Z}_{\ge 0}$. The maximum degeneracy of an individual operator at dimension $\Delta$ is $\rho_0(\Delta)$ (Cardy density) up to subleading corrections, saturated at $c=4k$. Analogous bounds with $\Lambda=\pi$ and $\rho_0^J(\Delta) = \frac{2}{1+\delta_{J,0}}\sqrt{c/12\Delta^3}\exp(2\pi\sqrt{c\Delta/3})$ hold for fixed-spin operators (gap-2 spectra saturate), and shifting $c\to c-1$ gives the Virasoro-primary version for $c>1$.

## Why it matters here
General background; no direct arena tie. The Beurling-Selberg majorant/minorant technique (bandlimited functions extremizing a characteristic-function approximation in $L^1$ with prescribed Fourier support) is a sibling of the Cohn-Elkies LP method and overlaps with magic-function constructions used in sphere packing and uncertainty extremals — potentially relevant background for problems where the agent must extremize over a class of test functions with Paley-Wiener-type support constraints.

## Open questions / connections
- Can the bounds be saturated for $c \ne 4k$ or for $2\delta\notin\mathbb{Z}$? (Authors explicitly do not know.)
- Connection to conformal-bootstrap extremal functionals (Mazac, Paulos, Hartman-Mazac-Rastelli sphere-packing/quantum-gravity work) — both produce functions non-negative outside an interval and vanishing on the physical spectrum.
- Step-two program: adding "no conserved currents except stress tensor" to lift coarse-grained limitations and probe RMT statistics — left open.

## Key terms
Beurling-Selberg extremal problem, bandlimited majorant/minorant, Paley-Wiener theorem, Poisson summation, modular bootstrap, Cardy formula, Selberg extremal function, Littmann quadrature, $j$-invariant integer-spaced spectrum, Virasoro primaries, spectral form factor, exponential type entire function
