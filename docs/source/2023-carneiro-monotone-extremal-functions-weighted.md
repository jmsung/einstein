---
type: source
kind: paper
title: Monotone extremal functions and the weighted Hilbert's inequality
authors: Emanuel Carneiro, Friedrich Littmann
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2302.14658v2
source_local: ../raw/2023-carneiro-monotone-extremal-functions-weighted.pdf
topic: general-knowledge
cites: 
---

# Monotone extremal functions and the weighted Hilbert's inequality

**Authors:** Emanuel Carneiro, Friedrich Littmann  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2302.14658v2

## One-line
Solves the Beurling-type extremal majorant problem for $\operatorname{sgn}(x)$ under an added monotonicity constraint, and uses it to give the first Fourier-analytic proof of the weighted Hilbert–Montgomery–Vaughan inequality.

## Key claim
Among real entire functions $F$ of exponential type $\leq 2\pi$ with $F \geq \operatorname{sgn}$ on $\mathbb{R}$ and $F$ monotone on each half-line (non-decreasing on $(-\infty,0)$, non-increasing on $(0,\infty)$), one has $\int_{-\infty}^{\infty}(F-\operatorname{sgn})\,dx \geq 2$, with unique extremizer $M(z) = -2\int_{-\infty}^{z}\frac{\sin^2\pi s}{\pi^2 s(s+1)^2}\,ds - 1$ (twice the Beurling-unconstrained value of $1$).

## Method
Reduce to the Heaviside case $x_+^0$; for any admissible majorant $G$ with derivative $g$, the function $H(u) = -u\,g(u)$ is real entire, non-negative on $\mathbb{R}$, of type $\leq 2\pi$, integrable, with a double zero at $0$. Apply Krein's decomposition $H(z) = z^2 h(z)\overline{h(\bar z)}$ with $h$ of type $\leq \pi$, then Poisson summation gives $\int(G-x_+^0)\,dx = \sum_{n\in\mathbb{Z}} |nh(n)|^2 \geq -\sum n|h(n)|^2 = 1$. Equality forces $h$ supported at $n=-1,0$, fixing $z\,h(z)$ via Shannon–Whittaker interpolation. The Hilbert–Montgomery–Vaughan corollary follows by stacking shifted copies $\psi_{\delta_j}-\psi_{\delta_{j-1}}\geq 0$ (monotonicity!) inside $\big\|\sum a_m e^{-2\pi i\lambda_m x}\big\|^2$.

## Result
A clean Fourier proof of $\big|\sum_{m\neq n} a_m\overline{a_n}/(\lambda_m-\lambda_n)\big| \leq C\sum |a_n|^2/\delta_n$ with $C = 2\pi$, where $\delta_n = \min_{m\neq n}|\lambda_m-\lambda_n|$. Worse than Preissmann's $C=(1.3154\ldots)\pi$ and Selberg's private $C=3.2$, but the first proof outside linear-algebra/eigenvalue territory. Conjectured sharp constant is $C=\pi$ (open since 1974).

## Why it matters here
Direct relevance to autocorrelation/uncertainty problems (P14, P17 family) where one-sided band-limited majorants of indicator/sign functions drive sharp Fourier-analytic bounds — extends the Beurling/Selberg/Vaaler toolkit with a monotonicity-constrained variant. The technique (Krein decomposition + Poisson summation + interpolation pinning extremizers) is a transferable recipe for extremal-function problems beyond the classical Beurling case.

## Open questions / connections
- Can the Beurling majorant $B$ (instead of $M$) be used to push the constant in (1.4) down to the conjectured $C=\pi$? Authors flag the missing step: verify non-negativity of the analog of (2.1) with $\psi = B - \operatorname{sgn}$.
- Extension to higher-dimensional/multivariate weighted Hilbert inequalities and to other monotonicity-constrained extremal problems (one-sided majorants of $\mathbf{1}_{[a,b]}$, $e^{-\lambda|x|}$, etc.).
- Bridge between linear-algebra approaches (Montgomery–Vaughan, Preissmann, Selberg, Schur) and Fourier-analysis approaches (Vaaler, this paper) — can a hybrid recover the sharp $\pi$?

## Key terms
Beurling extremal function, Selberg majorant, weighted Hilbert inequality, Montgomery-Vaughan, exponential type, Paley-Wiener, Krein decomposition, Poisson summation, Shannon-Whittaker interpolation, monotone majorant, signum function majorant, Vaaler, autocorrelation inequalities, band-limited function, large sieve
