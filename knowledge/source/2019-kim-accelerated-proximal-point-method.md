---
type: source
kind: paper
title: Accelerated Proximal Point Method and Forward Method for Monotone Inclusions
authors: Donghwan Kim
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.05149
source_local: ../raw/2019-kim-accelerated-proximal-point-method.pdf
topic: general-knowledge
cites:
---

# Accelerated Proximal Point Method and Forward Method for Monotone Inclusions

**Authors:** Donghwan Kim  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.05149

## One-line
Designs an accelerated proximal point method for maximally monotone operators with a fast $O(1/i^2)$ fixed-point residual rate, proved via computer-assisted performance estimation (PEP).

## Key claim
The proposed accelerated proximal point iterate satisfies $\|x_i - y_{i-1}\|^2 \le R^2/i^2$ (Theorem corresponding to Lemma 4.1 + (27)), improving on the proximal point method's $O(1/i)$ bound $\|x_i - x_{i-1}\|^2 \le (1 - 1/i)^{i-1} R^2/i$ from Gu–Yang 2020 — an $i$-fold asymptotic speedup w.r.t. the fixed-point residual.

## Method
Cast the worst-case analysis as a Performance Estimation Problem (PEP) over a finite-dimensional Gram matrix, take its SDP Lagrangian dual $(\mathcal{D})$, and minimize over the step-coefficient schedule $\{h_{i+1,k+1}\}$ via alternating SDP solves (CVX). A closed-form feasible point is then identified analytically (Lemma 4.1: $h_{i,k} = -2(k+1)/(i(i+1))$ for $k<i$, $h_{i,i} = 2i/(i+1)$) and shown to admit an efficient two-term momentum form $y_{i+1} = x_{i+1} + \tfrac{i}{i+2}(x_{i+1}-x_i) - \tfrac{i}{i+2}(x_i - y_{i-1})$ — note the negative second-momentum term, distinguishing it from Güler/FISTA inertia.

## Result
The accelerated scheme attains $O(1/i^2)$ fixed-point residual for any maximally monotone $M$, and under additional $\mu$-strong monotonicity a restarted variant recovers a linear rate. The acceleration is transported to: proximal method of multipliers, preconditioned proximal point (yielding an accelerated PDHG), Douglas–Rachford splitting ($\|\nu_i - \eta_{i-1}\|^2 \le R^2/i^2$, Cor. 6.2), ADMM ($\|Ax_{i+1}+Bz_i - c\|^2 \le R^2/(\rho^2 i^2)$ nonergodic, Cor. 6.3 — $e\times$ tighter than the $O(1/i)$ Davis–Yin bound), and forward methods for $\beta$-cocoercive operators via the Yosida-approximation equivalence $J_{\lambda M} = I - \lambda M_\lambda$.

## Why it matters here
General background; no direct arena tie. Could indirectly inform any future arena problem solved by a saddle-point/primal-dual LP-like formulation (e.g., Cohn–Elkies LP duals, SDP flag-algebra polish) where ADMM/PDHG is the inner solver — the accelerated nonergodic rate is the relevant lever, and heuristic restart every $\sim 10$–$20$ iterations is empirically strong even without strong monotonicity.

## Open questions / connections
- Is the analytic step schedule in Lemma 4.1 actually the PEP minimizer of $(\mathcal{H}_D)$, or only a feasible point? — Kim does not prove uniqueness/optimality.
- Extension to iteration-dependent $\lambda_i$ (cf. Attouch–Chbani–Riahi 2019) and to exact (not just upper-bound) worst-case rates for DR/ADMM — left open.
- Equivalence (per Ryu–Yin 2020) to Lieder's optimized Halpern/Krasnosel'skii–Mann iteration when $T = 2J_{\lambda M} - I$ suggests one canonical "accelerated nonexpansive iteration"; relation to high-resolution ODE acceleration framework (Shi et al., Su–Boyd–Candès) unmapped here.

## Key terms
proximal point method, maximally monotone operator, performance estimation problem (PEP), fixed-point residual, Nesterov acceleration, Güler accelerated proximal, ADMM, Douglas–Rachford splitting, primal-dual hybrid gradient (PDHG), cocoercive operator, Yosida approximation, restart heuristic, SDP dual, Halpern iteration
