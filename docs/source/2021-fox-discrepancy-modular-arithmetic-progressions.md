---
type: source
kind: paper
title: Discrepancy in modular arithmetic progressions
authors: Jacob Fox, Max Wenqiang Xu, Yunkun Zhou
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.03929v1
source_local: ../raw/2021-fox-discrepancy-modular-arithmetic-progressions.pdf
topic: general-knowledge
cites: 
---

# Discrepancy in modular arithmetic progressions

**Authors:** Jacob Fox, Max Wenqiang Xu, Yunkun Zhou  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2104.03929v1

## One-line
Determines the discrepancy of arithmetic progressions in $\mathbb{Z}_n$ asymptotically (log-scale, all $n$) and up to constants for prime powers, resolving Hebbinghaus–Srivastav.

## Key claim
For all positive integers $n$, $\frac{1}{8d(n)}\min_{r\mid n}(n/r+\sqrt{r})\le \mathrm{disc}(\mathcal{A}_n)\le \min_{r\mid n}(n/r+c\sqrt{r}\cdot 2^{\omega(r)})$, giving $\mathrm{disc}(\mathcal{A}_n)=n^{1/3+x+o(1)}$ where $x\ge 0$ is the largest value such that no divisor of $n$ lies in $(n^{2/3-x},n^{2/3+2x})$. For $n=p^k$, $\mathrm{disc}(\mathcal{A}_n)=\Theta(p^{(k-\lfloor k/3\rfloor)/2})=\Theta(n^{1/3+r_k/(6k)})$ with $r_k=k\bmod 3$.

## Method
Upper bound: partial-coloring via Matoušek–Spencer entropy method (Lemma 2.1) applied to a dyadic decomposition of the set system, plus a key reduction (Lemma 3.2) that lifts a coloring on $\mathbb{Z}_r$ ($r\mid n$) having small discrepancy on *both* $\mathcal{A}_r$ and the congruence-class family $\mathcal{A}^0_r$ to a coloring on $\mathbb{Z}_n$. The joint-low-discrepancy coloring on $\mathbb{Z}_r$ is constructed by translation-pairing on $\mathbb{Z}_{p^k}$ then combined across prime factors. Lower bound: Fourier analysis on $\mathbb{Z}_n$ via the second-moment identity $\sum_{r}|\widehat{\chi}(r)|^2=n^2$ combined with bounds on $G_\chi(n/k)=\sum_a|g_\chi(a,n/k)|^2$ and a divisor-sum tail estimate (Proposition 4.7).

## Result
Closes the $\sqrt{\log p}$ gap from Hebbinghaus–Srivastav: $\mathrm{disc}(\mathcal{A}_p)=\Theta(\sqrt{p})$ for prime $p$. Establishes that the exponent depends on the divisor structure of $n$ (neither Roth's $n^{1/4}$ lower nor random-coloring $\tilde O(\sqrt n)$ upper is sharp in general). Prime-power case: $\mathrm{disc}(\mathcal{A}_{p^k})=\Theta(p^{(k-\lfloor k/3\rfloor)/2})$, e.g. exponent $1/3, 1/2, 1/2$ for $k\equiv 0,1,2\pmod 3$. Bonus: hereditary-discrepancy bound $\mathrm{herdisc}(\mathcal{A}_n)\le c\,\varphi(n)^{1/2}(\log(en/\varphi(n)))^{3/2}$ (Theorem 5.1).

## Why it matters here
General background; no direct arena tie. Closest hooks are to extremal combinatorics / discrete-geometry problems where two-coloring discrepancy bounds inform construction-vs-obstruction balance (e.g. Sidon-set / autocorrelation flavor problems on cyclic groups); the divisor-sensitive exponent illustrates how arithmetic structure of $n$ can change the optimization landscape qualitatively.

## Open questions / connections
- Problem 5.1: close the $O(d(n)^{3/2})$ gap between upper and lower bounds for $\mathrm{disc}(\mathcal{A}_n)$ for general $n$.
- Problem 5.2: estimate $\mathrm{herdisc}(\mathcal{A}_n)$; is the $\varphi(n)^{1/2}$ upper bound tight up to $n^{o(1)}$?
- Extends Roth (1964) $n^{1/4}$ and Matoušek–Spencer (1996) $\Theta(n^{1/4})$ on $[n]$ to the modular setting; lower bound also covers complex unit-circle colorings (Remark 4.8), connecting to Tao's solution of the Erdős discrepancy problem.

## Key terms
discrepancy, arithmetic progressions, $\mathbb{Z}_n$, Roth bound, Matoušek–Spencer entropy method, partial coloring, Fourier analysis on cyclic groups, hereditary discrepancy, Hebbinghaus–Srivastav, divisor function, Euler totient, prime-power exponent
