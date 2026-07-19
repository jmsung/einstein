---
type: source
kind: paper
title: Optimal error bounds for non-expansive fixed-point iterations in normed spaces
authors: Juan Pablo Contreras, R. Cominetti
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.10969
source_local: ../raw/2021-contreras-optimal-error-bounds-non-expansive.pdf
topic: general-knowledge
cites:
---

# Optimal error bounds for non-expansive fixed-point iterations in normed spaces

**Authors:** Juan Pablo Contreras, R. Cominetti  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.10969

## One-line
Derives optimal worst-case convergence rates for general Mann-type fixed-point iterations of non-expansive maps in normed spaces via a nested optimal-transport framework.

## Key claim
The optimal rate for general Mann iterations of non-expansive maps is $\Theta(1/n)$; the Halpern iteration with stepsizes $\beta_{n+1} = \tfrac{1}{2}(1+\beta_n^2)$, $\beta_0=0$ attains the tight worst-case residual bound $\|x_n - Tx_n\| \le R_n \le \tfrac{4}{n+4}$, and for affine non-expansive maps the optimal Halpern bound is exactly $\tfrac{1}{n+1}$ (with $\beta_n = n/(n+1)$).

## Method
Worst-case fixed-point residuals $\|x_n - Tx_n\|$ are bounded via a nested family of optimal transport problems $(P_{m,n})$ over the averaging distributions $\pi_n$, yielding a universal bound $R_n(\pi)$ proven tight (Theorem 2.1) by constructing an extremal non-expansive map on the unit cube of $\ell^\infty(I)$ using hyperconvex extension (Aronszajn–Panitchpakdi). The optimal $\pi_n$ are computed by solving either a fixed-horizon nonconvex QP, a sequential one-step QP, or a monotone-restricted variant; for Halpern's special structure $\pi_n = (1-\beta_n)\delta_0 + \beta_n\delta_n$ the recursion admits a closed form via $z_n = R_n/4$ satisfying $z_n = z_{n-1}(1-z_{n-1})$.

## Result
Halpern's iteration with the recursive optimal stepsizes attains $\lim_{n\to\infty}(n+4)R_n = 4$, tight in general normed spaces. For affine non-expansive maps in any normed space, $\beta_n = n/(n+1)$ gives the tight bound $\|x_n - Tx_n\| \le 2\|x_0 - x^*\|/(n+1)$, matching Lieder's [26] Hilbert-space bound and proving Kim's [20] inertial method is equivalent to classical Halpern. Conversely, the Krasnoselskii–Mann iteration with any stepsize sequence cannot beat $\Omega(1/\sqrt{n})$ — proven via the right-shift on $\ell^1(\mathbb{N})$ and bell-shaped Poisson-binomial estimates.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein problems are fixed-point iteration problems. Potentially relevant as meta-methodology for the agent: the optimal-transport-as-worst-case-bound technique and the gap between sequential and fixed-horizon optimization are transferable patterns when designing optimizer iteration schedules.

## Open questions / connections
- Whether Krasnoselskii–Mann achieves $o(1/\sqrt{n})$ in Hilbert space remains open (Baillon & Bruck observation).
- Whether inertial/extended Krasnoselskii–Mann variants can break the $1/\sqrt{n}$ barrier — numerics in the paper suggest no, but no proof.
- Connection to Performance Estimation Problems (Drori–Teboulle) restricted to Hilbert spaces; this paper extends the $1/n$ accelerated rate to general normed spaces for Halpern.

## Key terms
Halpern iteration, Krasnoselskii-Mann iteration, Mann iteration, non-expansive maps, fixed-point residual, optimal transport bounds, convergence rate, Performance Estimation Problems, asymptotic regularity, hyperconvex space, Poisson-binomial, Lieder, Kim, Sabach-Shtern, co-coercive operator
