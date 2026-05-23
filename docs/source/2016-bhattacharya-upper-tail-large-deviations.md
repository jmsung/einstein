---
type: source
kind: paper
title: Upper Tail Large Deviations for Arithmetic Progressions in a Random Set
authors: B. Bhattacharya, S. Ganguly, X. Shao, Yufei Zhao
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1605.02994
source_local: ../raw/2016-bhattacharya-upper-tail-large-deviations.pdf
topic: general-knowledge
cites:
---

# Upper Tail Large Deviations for Arithmetic Progressions in a Random Set

**Authors:** B. Bhattacharya, S. Ganguly, X. Shao, Yufei Zhao  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1605.02994

## One-line
Determines the precise log-asymptotics of the probability that a sparse random subset of $[N]$ or $\mathbb{Z}/N\mathbb{Z}$ contains far more $k$-term arithmetic progressions than expected.

## Key claim
For $k \geq 3$, fixed $\delta > 0$, $\Omega = [N]$, and $p = p_N \geq N^{-1/(6k(k-1))} \log N$ with $p \to 0$:
$$\mathbb{P}(X_k \geq (1+\delta)\mathbb{E}X_k) = p^{(1+o(1))\sqrt{\delta} N p^{k/2}}.$$
This answers a question of Chatterjee–Dembo and gives the first $N^{-c}$-decay regime for $k \geq 4$.

## Method
Apply Eldan's nonlinear large deviation principle (stochastic control / Gaussian-width hypotheses, improving Chatterjee–Dembo) to reduce the upper-tail probability to an entropy variational problem $\phi_{p,\Omega}^{(k)}(\delta) = \inf \sum_a I_p(f(a))$ subject to $T_k(f) \geq (1+\delta) p^k T_k(\Omega)$. Bound the Gaussian width of the gradient set $\{\nabla T_k(y)/N\}$ via Fourier analysis ($k=3,4$) and a Chinese-remainder-style covering by small bounded sets ($k \geq 5$), then solve the variational problem by thresholding into macroscopic (interval-dominated) and microscopic (replica-symmetric) regimes.

## Result
Two regimes, separated by $\delta^{-3} p^{k-2} \log^2(1/p)$:
- **Macroscopic** ($\to 0$): $\phi = (1+o(1))(k-1)\sqrt{\delta} p^{k/2} N \log(1/p)$ for $\Omega = [N]$; minimizer is an interval (Green–Sisask extremal extended to $k$-APs in Thm. 2.4).
- **Microscopic** ($\to \infty$): $\phi = (1/(2\gamma_k) + o(1)) \delta^2 N p$ on $[N]$ and $(1/(2k^2)+o(1))\delta^2 Np$ on $\mathbb{Z}/N\mathbb{Z}$, with $\gamma_3 = 28/3$, $\gamma_4 = 17$, $\gamma_5 = 718/27$, and $\gamma_k/k^2 \to (30-2\pi^2)/9 \approx 1.14$.
Gaussian width bound: $\mathrm{GW}(T_k/N) = O(N^{1-1/(2(k-1))})$, with conjectured optimal $\sqrt{N} (\log N)^{O(1)}$.

## Why it matters here
General background; no direct arena tie. Potentially relevant framing for problems involving counting structures in random/discrete sets (sieve-style, autocorrelation-style) — the macroscopic/microscopic dichotomy (clustered vs uniform density boost) is a transferable heuristic for thinking about how extremal configurations form.

## Open questions / connections
- Extend the LDP to $p$ decaying as fast as $(\log N/N)^{1/(k-1)}$ (Warnke's order-of-magnitude range); Briët–Gopi improved the Gaussian-width exponent to $1/(2\lceil (k-1)/2\rceil)$ post-print.
- Conjecture 4.2: $\mathrm{GW}(T_k/N) = \sqrt{N}(\log N)^{O(1)}$ for $k \geq 4$.
- Closed-form for $\gamma_k$ unknown.
- Full replica-symmetry phase boundary for fixed $p,\delta$ on $\mathbb{Z}/N\mathbb{Z}$ open (Thm. 7.1 likely not tight).

## Key terms
large deviations, arithmetic progressions, $k$-AP, Eldan LDP, Chatterjee–Dembo, Gaussian width, nonlinear large deviation principle, entropy variational problem, replica symmetry, Green–Sisask extremal, additive combinatorics, Freiman rectification
