---
type: source
kind: paper
title: Extremal functions in de Branges and Euclidean spaces
authors: E. Carneiro, Friedrich Littmann
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1406.5456
source_local: ../raw/2014-carneiro-extremal-functions-branges-euclidean.pdf
topic: general-knowledge
cites:
---

# Extremal functions in de Branges and Euclidean spaces

**Authors:** E. Carneiro, Friedrich Littmann  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1406.5456

## One-line
Constructs optimal exponential-type majorants/minorants of $e^{-\lambda|x|}$ (and a wide class of radial subordinated functions) on $\mathbb{R}^N$ in the weighted $L^1(|x|^{2\nu+2-N}dx)$ metric via de Branges space interpolation.

## Key claim
For $\lambda>0$, $\nu>-1$, $\delta>0$, there exist real entire functions $L_\nu(\delta,\lambda,\cdot), M_\nu(\delta,\lambda,\cdot)\in\mathcal{E}_\delta^N$ with $L_\nu\le e^{-\lambda|x|}\le M_\nu$ minimizing $\int_{\mathbb{R}^N}(\cdot)|x|^{2\nu+2-N}dx$; the multidimensional optimum reduces to the $N=1, \delta=2$ case via $U_\nu^{N\pm}(\delta,\lambda)=\tfrac12\omega_{N-1} U_\nu^{1\pm}(\delta,\lambda)$ with closed-form sums over zeros of Bessel-type functions $A_\nu,B_\nu$ (related to $J_\nu, J_{\nu+1}$).

## Method
Reformulates the extremal problem inside a homogeneous de Branges Hilbert space $\mathcal{H}(E_\nu)$ where $E_\nu = A_\nu - iB_\nu$ generalizes $\cos z - i\sin z$ via Bessel functions. Uses Laplace-transform representations of reciprocals of Laguerre-Pólya functions (Hirschman-Widder theory) to build interpolating entire functions at zeros of $A^2, B^2$. Extends from $F_\lambda(x)=e^{-\lambda|x|}$ to subordinated radial functions $G_\mu(x)=\int_0^\infty(e^{-\lambda|x|}-e^{-\lambda})d\mu(\lambda)$ by integrating against measures satisfying weighted finiteness conditions.

## Result
Explicit formulas (1.14)-(1.15) for $U_\nu^{1\pm}(2,\lambda)$ as sums $\sum_{A_\nu(\xi)=0} e^{-\lambda|\xi|}/(c_\nu K_\nu(\xi,\xi))$ minus $2\Gamma(2\nu+2)/\lambda^{2\nu+2}$. Asymptotics: $U_\nu^{1\pm}(2,\lambda)\ll_\nu \lambda^{-(2\nu+2)}$ as $\lambda\to\infty$, $\ll_\nu \lambda$ as $\lambda\to 0$. Yields multidimensional Hilbert-type inequalities (Theorem 4), extremal trigonometric polynomials for periodic exponential/log-sine functions via OPUC theory, and polynomial majorants on $S^{N-1}$ for axially-symmetric functions.

## Why it matters here
Directly informs **autocorrelation/uncertainty problems** (P15, P16, P17 in arena) via Beurling-Selberg machinery, and **sphere/discrete-geometry bounds** through Hilbert-type inequalities with radial Poisson-kernel majorants — the de Branges-space lens generalizes the LP-bound / magic-function framework already used in [[cohn-elkies]] and [[viazovska-sphere-packing]] to weighted $|x|^{2\nu+2-N}$ metrics.

## Open questions / connections
- Extends Holt-Vaaler (1996, ref [25]) from characteristic functions of Euclidean balls to general radial subordinated functions; what other arena-relevant radials (Gaussians, truncated powers) admit similar weighted multidim extremals?
- Polynomial-approximation analog on $[-1,1]$ solved by Bojanic-DeVore [5] with different methods — does the de Branges route give sharper constants for finite-interval kissing-number LP bounds?
- Connection [9,37] to pair-correlation of Riemann zeros suggests transfer to **extremal-graph-theory** discrepancy problems via Montgomery's pair-correlation framework.

## Key terms
de Branges spaces, Beurling-Selberg extremal problem, Hermite-Biehler function, Laguerre-Pólya class, Bessel functions $J_\nu$, reproducing kernel Hilbert space, exponential-type entire functions, Hilbert-type inequalities, Poisson kernel, radial majorants, OPUC orthogonal polynomials unit circle, Holt-Vaaler, Plancherel-Pólya, Cohn-Elkies LP bound
