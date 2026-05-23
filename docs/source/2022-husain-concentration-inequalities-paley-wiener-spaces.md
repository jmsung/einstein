---
type: source
kind: paper
title: Concentration inequalities for Paley-Wiener spaces
authors: Syed Husain, Friedrich Littmann
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2210.10029v2
source_local: ../raw/2022-husain-concentration-inequalities-paley-wiener-spaces.pdf
topic: general-knowledge
cites: 
---

# Concentration inequalities for Paley-Wiener spaces

**Authors:** Syed Husain, Friedrich Littmann  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2210.10029v2

## One-line
Extends Donoho–Logan-style $L^1$ concentration inequalities for bandlimited (Paley–Wiener) functions to all density regimes in dimension one and to multivariate cube-spectrum windows, giving Nyquist-density thresholds for perfect $L^1$ signal recovery from sparse noise.

## Key claim
For $G \in B^1(\tau)$ (1-D Paley–Wiener), $\|G\chi_N\|_1 \le C_{\tau,\delta}\,\sup_x |N \cap [x,x+\delta]|\,\|G\|_1$ with $C_{\tau,\delta} \le 1380(\tau+\delta^{-1})$ in general, $\le \tfrac{5}{2}(\tau+\delta^{-1})$ for $\tau\delta \ge 2$, and $\lim_{\tau\delta\to\infty} C_{\tau,\delta} = 2$ — removing the $\delta\tau < 1$ restriction of Donoho–Logan (1992). In $d$ dimensions with spectrum cube $[-\lambda,\lambda]^d$ and ball window $B(x,\alpha)$, the constant is $(\sqrt{d}\lambda)^{d/2}/(\alpha^{d/2} J_{d/2}(2\pi\sqrt{d}\lambda\alpha))$ provided $2\pi\sqrt{d}\alpha\lambda < j_{d/2}(1)$.

## Method
Donoho–Logan kernel/minimal-extrapolation scheme: choose $g$ with $\operatorname{supp}(g)\subset W_\delta$ so convolution with $g$ is invertible on $B^1$ and $\|g\|_\infty\|T_g^{-1}\|$ is small; bound $\|G\chi_N\|_1$ by this product times the relative density. In 1-D they use $g_\tau(x) = -2(1-|x|)\{\cos 2\pi(\tau+1)x - \cos 2\pi\tau x\}/(4\pi^2 x^2)\,\chi_{[-1,1]}$, whose Fourier transform $\hat g_\tau$ is positive and has $1/\hat g_\tau$ convex on $[-\tau,\tau]$, yielding a discrete inverse measure $\nu$ via Beurling-style minimal extrapolation. In $d$-D they take $g_\alpha = \chi_{B(0,\alpha)}$ with $\hat g_\alpha \propto J_{d/2}(2\pi\alpha|t|)/|t|^{d/2}$ and use a Laguerre–Pólya/Schoenberg Laplace representation of $x^p/J_p(x)$ to prove the Fourier coefficients of $1/\hat g_\alpha$ have signs $(-1)^{n_1+\cdots+n_d}$, giving the total-variation norm.

## Result
Plugging $C_{\tau,\delta} < \tfrac{1}{2}$ into Logan's phenomenon gives $L^1$ perfect signal recovery whenever the noise support's Nyquist density falls below the explicit threshold. For cube spectrum + ball window of radius $\alpha = \delta\sqrt{d}/2$ with $\lambda\delta = 2\pi^2$, the ball-window density bound scales like $\Gamma(1/3)/(2^{1/3} 3^{1/6}\pi\,d^{1/6})$ for large $d$, while the cube window gives $\tfrac{1}{2}\{4\pi^2\sin(1/4\pi^2)\}^d$ — the cube-window bound is larger in every dimension tested.

## Why it matters here
Direct large-sieve / uncertainty-principle machinery: gives explicit constants for the Donoho–Logan / Logvinenko–Sereda concentration program, which underlies Cohn–Elkies-style LP bounds and Selberg/Beurling extremal-function constructions used across sphere-packing, autocorrelation, and uncertainty problems. The minimal-extrapolation construction (cosine-difference kernel with convex $1/\hat g$, signed Dirac comb inverse) is a transferable technique for $B^1$ duality problems.

## Open questions / connections
- Extends Donoho–Logan 1992 (Theorem 7) to $\delta\tau \ge 1$ and shows the asymptotic constant is exactly $2$ — improving the $1380$ prefactor is open.
- Treats only $M$ = cube in higher dimensions; ball-spectrum $M$ is flagged as obstructed (which Fourier-coefficient sign pattern fails).
- Connects to Kovrijkine's effective Logvinenko–Sereda constants (densities up to 1) but with non-effective constants — bridging the two regimes is open.
- Related to Abreu–Speckbacher large-sieve principles on polyanalytic Fock spaces and Candès–Romberg–Tao sparse-recovery uncertainty principles.

## Key terms
Paley-Wiener space, concentration inequality, Donoho-Logan, Logan phenomenon, minimal extrapolation, Beurling, large sieve, Logvinenko-Sereda, Nyquist density, Bessel function, Laguerre-Polya class, signal recovery, bandlimited, uncertainty principle, Kovrijkine
