---
type: source
kind: paper
title: "Private stochastic convex optimization: optimal rates in linear time"
authors: V. Feldman, Tomer Koren, Kunal Talwar
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.04763
source_local: ../raw/2020-feldman-private-stochastic-convex-optimization.pdf
topic: general-knowledge
cites:
---

# Private stochastic convex optimization: optimal rates in linear time

**Authors:** V. Feldman, Tomer Koren, Kunal Talwar  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.04763

## One-line
Two new linear-time differentially private algorithms for stochastic convex optimization that match the optimal non-private gradient-complexity while achieving the tight excess-population-loss bound.

## Key claim
Achieves the optimal excess population loss $E[F(\hat w)] - F^* \leq O(DL(1/\sqrt{n} + \sqrt{d\ln(1/\delta)}/(\varepsilon n)))$ for $(\varepsilon,\delta)$-DP SCO using only $O(\min\{n, n^2/d\})$ gradient computations — matching the running time of optimal non-private SCO and improving on Bassily et al. 2019's $O(\min\{n^{3/2}, n^{5/2}/d\})$.

## Method
Two techniques: (1) **Snowball-SGD** — one-pass noisy projected SGD with growing batch sizes $B_t \propto 1/\sqrt{T-t+1}$, analyzed via privacy amplification by iteration (Feldman–Mironov–Talwar–Thakurta 2018) combined with Jain–Nagaraj–Netrapalli last-iterate convergence; (2) **Iterative localization** — reduces DP-SCO to repeatedly localizing an approximate minimizer within shrinking $L_2$ balls using a uniformly stable non-private SCO subroutine (one-pass SGD or regularized ERM) plus output-perturbation Gaussian noise, with geometrically decreasing diameters over $\log n$ phases.

## Result
Theorem 1.1 gives $(\alpha, \alpha\rho^2/2)$-RDP under mild smoothness ($\beta \leq cDL\min(\sqrt n, \rho n/\sqrt d)$) with linear gradient complexity. The non-smooth case is handled via Phased-ERM in $O(n^2 \ln(1/\delta))$ gradient calls. For $\lambda$-strongly convex losses, achieves the optimal $O(L^2/\lambda \cdot (1/n + d/(\rho^2 n^2)))$ rate in nearly linear time. Section 6 shows a separation: averaged iterates of CNI are *not* RDP-amplified even when the last iterate is — counterexample with effective noise $\Theta(k/T + (T-k)/T \cdot k^2/T)$ insufficient to mask $X_0$ for intermediate $k$.

## Why it matters here
General background; no direct arena tie — DP-SCO is orthogonal to Einstein Arena's deterministic continuous-optimization problems. Possible thin relevance: the **last-iterate vs averaged-iterate** distinction for SGD (Shamir–Zhang, Jain–Nagaraj–Netrapalli) and **uniform stability of one-pass SGD** are general optimization facts that could inform any future stochastic-tempering analysis in `findings/` on parallel-tempering or basin-hopping schedules.

## Open questions / connections
- Can the non-smooth DP-SCO running time be improved below $O(n^2)$? Equivalent: is there a uniformly stable non-private non-smooth SCO algorithm in $o(n^2)$ gradient calls?
- Extends Feldman–Mironov–Talwar–Thakurta 2018 (privacy amplification by iteration) and Bassily–Feldman–Talwar–Thakurta 2019 (optimal-rate DP-SCO).
- The CNI-with-averaging counterexample (Sec. 6) leaves open: what *structural* condition on contractive maps makes averaging RDP-preserving?

## Key terms
differential privacy, Rényi differential privacy, RDP, zCDP, stochastic convex optimization, SCO, noisy SGD, privacy amplification by iteration, contractive noisy iteration, iterative localization, uniform stability, last-iterate SGD, Gaussian mechanism, Lipschitz, smoothness, Feldman, Koren, Talwar, Bassily
