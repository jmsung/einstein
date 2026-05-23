---
type: source
kind: paper
title: Donoho-Logan Large Sieve Principles for Modulation and Polyanalytic Fock Spaces
authors: L. D. Abreu, Michael Speckbacher
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1808.02258
source_local: ../raw/2018-abreu-donoho-logan-large-sieve-principles.pdf
topic: general-knowledge
cites:
---

# Donoho-Logan Large Sieve Principles for Modulation and Polyanalytic Fock Spaces

**Authors:** L. D. Abreu, Michael Speckbacher  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1808.02258

## One-line
Extends Donoho-Logan large sieve / signal-recovery inequalities from band-limited functions to the short-time Fourier transform (STFT) with Hermite windows, giving explicit concentration bounds on arbitrary time-frequency sets $\Delta \subset \mathbb{R}^2$.

## Key claim
For $f \in M^1$ (Feichtinger's algebra) and the $r$th Hermite window $h_r$, $\|V_{h_r} f \cdot \chi_\Delta\|_1 \leq \frac{\rho(\Delta,R)}{C_r(R)} \|V_{h_r} f\|_1$, where $\rho(\Delta,R) = \sup_{z}|\Delta \cap (z+D_{1/R})|$ is the planar maximum Nyquist density and $C_r(R) = \int_0^{\pi R^2} L_r^0(t)^2 e^{-t}\,dt$. The result extends to $1 \leq p < \infty$ and yields explicit deterministic perfect-recovery thresholds via $L^1$-minimization when $\delta(\Delta) < 1/2$.

## Method
Two new technical ingredients replace Beurling's extremal-function machinery (which has no STFT analogue): (1) a Schur-test-style argument on hermitian integral kernels in a general Banach-space setting (Proposition 1), and (2) an extension of Seip's local reproducing formula on discs from the Bargmann-Fock space to polyanalytic Fock spaces $F_{r+1}^2$ associated with Landau levels, using the closed form of complex Hermite polynomials $H_{j,r}(z,\bar z)$ in terms of generalized Laguerre polynomials $L_r^{j-r}$. Cross-window local reproduction (kernel $K_{h_r}$ reproduces $V_{h_j}f$ locally on discs for $j \neq r$) is the surprising lemma.

## Result
Explicit large-sieve constant $\rho(\Delta,R)/C_r(R)$ for any measurable $\Delta$ and any $R>0$, optimized by infimum over $R$. Recovery corollaries: if $A_r(\Delta,R) < C_r(R)/2$ the noisy STFT $G = V_{h_r}f + N$ is uniquely $L^1$-recoverable; if $A_r(\Delta,R) < C_r(R)$ inpainting error is $\leq 2\varepsilon C_r(R)/(C_r(R) - A_r(\Delta,R))$. A Donoho-Stark-type decoupling theorem (Proposition 8) shows the concentration constant on disjoint $\Delta = \bigcup \Delta_k$ tends to $\max_k$ as separation $\to \infty$. Conjecture 1: the disc $D_{\sqrt{A/\pi}}$ uniquely maximizes Gaussian-STFT concentration over $|\Delta|=A$.

## Why it matters here
General background for the agent's autocorrelation / uncertainty-principle problem family — large-sieve / concentration inequalities in time-frequency are the continuous analogue of the trigonometric large sieve that underlies several extremal-Fourier problems on Einstein Arena. The disc-extremality conjecture and the Laguerre/polyanalytic-Fock kernel machinery connect to any problem where Gaussian/Hermite windows optimize concentration; no direct arena tie to a specific numbered problem in current wiki.

## Open questions / connections
- Is the Hermite family the *only* class with disc-local reproducing formulas (Question 1 of §7)? Would extend Seip's double-orthogonality characterization.
- Prove Conjecture 1: discs are the unique extremizers for $L^p$ STFT concentration with Gaussian window — phase-space analogue of Donoho-Stark Conjecture 1.
- Can Carneiro-Littmann extremal functions in de Branges spaces [Carneiro-Littmann 2014] replace Beurling-Selberg to sharpen these constants?
- Concentration estimate is provably non-tight: gives factor 2 on the disc where truth is 1 — gap-tightening is open.
- Discrete Gabor frame version (§6.1) suggests deterministic compressed-sensing guarantees for sparse time-frequency representations.

## Key terms
large sieve, short-time Fourier transform, STFT, modulation space, Feichtinger algebra $M^1$, polyanalytic Fock space, Hermite functions, Laguerre polynomials, Bargmann transform, Donoho-Logan, Donoho-Stark, Beurling-Selberg extremal function, planar Nyquist density, Schur test, Seip local reproducing formula, Gabor frame, signal recovery, $L^1$-minimization, compressed sensing, Landau levels, concentration inequality
