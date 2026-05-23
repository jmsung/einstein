---
type: source
kind: paper
title: Numerical integration in arbitrary-precision ball arithmetic
authors: Fredrik Johansson
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1802.07942v1
source_local: ../raw/2018-johansson-numerical-integration-arbitrary-precision-bal.pdf
topic: general-knowledge
cites: 
---

# Numerical integration in arbitrary-precision ball arithmetic

**Authors:** Fredrik Johansson  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1802.07942v1

## One-line
Presents Arb's implementation of rigorous arbitrary-precision numerical integration via the Petras algorithm (adaptive bisection + adaptive Gaussian quadrature) in ball arithmetic, with certified error bounds.

## Key claim
For piecewise complex-analytic integrands, the method achieves $O(p)$ integrand evaluations at precision $p$ with rigorous enclosures, often outperforming heuristic high-precision integrators (Pari/GP `intnum`, mpmath `quad`); e.g. Rump's $\int_0^8 \sin(x+e^x)\,dx$ is computed to ~100 digits in 0.02 s.

## Method
Petras algorithm: maintain a queue of subintervals; on each, attempt a direct ball enclosure, else find an ellipse $E$ with foci $(\alpha,\beta)$ and degree $n\le n_{\max}$ such that $f$ is analytic on $E$ and the Gauss-Legendre error bound $|I-\sum w_k f(x_k)|\le M\rho^{-2n}C_\rho$ (with $\rho=X+Y$) meets the tolerance; else bisect. Analyticity is enforced by a user-supplied flag-bit on $f$ that returns NaN off the analytic region; quadrature nodes are computed on demand at high precision via the Johansson–Mezzarobba algorithm and cached on a sparse $n\approx 2^{k/2}$ schedule.

## Result
Complexity is $O(p)$ evaluations for analytic $f$ and $O(p^2)$ for piecewise-analytic $f$ with mid-interval singularities; degree alone would give $2^{O(p)}$ and bisection alone would fail. Benchmarks at $p\in\{32,64,333,3333\}$ on integrals with poles, branch cuts, oscillation, kinks, and complex paths (Lambert $W$, $\Gamma$ on $[1,1+1000i]$, Riemann $N(T)$ via argument principle up to $T=10^9$) show 10–1000× speedups over Pari/GP and mpmath while delivering certified balls of radius $\sim 2^{-p}$.

## Why it matters here
Direct toolchain for the **triple-verify** axiom: Arb integration provides check #2/check #3 (independent, certified) for any arena problem whose evaluator involves an integral or Cauchy contour — autocorrelation inequalities (P5, P14, P17), Cohn–Elkies LP duals (sphere packing, kissing), modular-form integrals, and verifier cross-checks at 50–80 dps mpmath-equivalent precision. Complements [[gpu-modal-compute]] by anchoring the CPU-local high-precision tier of the compute router.

## Open questions / connections
- Can improper integrals with user-supplied tail bounds $|f(x)|<Cx^\alpha\exp(-\beta x^\gamma)$ be wrapped to avoid manual truncation in autocorrelation/Fourier-tail bounds?
- Companion paper Johansson–Mezzarobba 2018 (arXiv:1802.03948) on Gauss-Legendre node generation — likely worth a separate ingest for the node-precomputation cost model.
- Oscillatory + slow-decay integrals ($\int_0^1 \sin(1/x)\,dx$ class) remain $2^{O(p)}$; relevant if any arena problem reduces to such an integral, would need specialized Levin/Filon methods.

## Key terms
ball arithmetic, interval arithmetic, Arb library, Petras algorithm, Gaussian quadrature, adaptive bisection, rigorous error bounds, arbitrary precision, Gauss-Legendre nodes, Cauchy integral formula, argument principle, Riemann zeta zero counting, branch cut handling, Johansson, mpmath
