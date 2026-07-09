---
type: source
kind: paper
title: On the number of integers in a generalized multiplication table
authors: Dimitris Koukoulopoulos
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1102.3236
source_local: ../raw/2011-koukoulopoulos-number-integers-generalized-multiplicati.pdf
topic: general-knowledge
cites:
---

# On the number of integers in a generalized multiplication table

**Authors:** Dimitris Koukoulopoulos  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1102.3236

## One-line
Determines the order of magnitude of the number of distinct products $n_1 \cdots n_{k+1}$ with $n_i \le N_i$ in a generalized $(k+1)$-dimensional multiplication table, generalizing the Erdős multiplication table problem.

## Key claim
For $2 \le k \le 5$ and arbitrary side lengths $N_1, \dots, N_{k+1}$, the count $A_{k+1}(N_1, \dots, N_{k+1})$ has known order of magnitude $\asymp x \cdot \beta \sqrt{\log\log y_k} \prod_{i=1}^k (\log y_i / \log y_{i-1})^{-Q((k-i+2)\alpha)}$, where $\alpha, \beta$ are explicit parameters of the side lengths and $Q(u) = u\log u - u + 1$. The upper bound holds for all $k \ge 2$; the matching lower bound requires condition (1.1) on $\alpha$, which is shown essentially optimal — the smallest $k$ where (1.1) can fail is $k=6$.

## Method
Reduction from a "local" counting problem $H^{(k+1)}(x, \mathbf{y}, 2\mathbf{y})$ (integers $\le x$ with divisors in prescribed dyadic intervals) to a "global" sum over square-free vectors $\mathbf{a}$ weighted by $L^{(k+1)}(\mathbf{a})$ — a Lebesgue measure quantifying clumping of the logarithmic-divisor set $D_{k+1}(\mathbf{a})$ (Theorem 1.7). Core analytic tools: Poisson approximation of $\omega(a_i)$, linear constraints on multidimensional Poisson distributions near a hyperplane (Section 4), Stirling + Lagrange multipliers to locate the optimum $r_i \sim (k-i+2)^\alpha \ell_i$, and a "method of low moments" interpolating between $L^1$ and $L^2$ estimates with order-statistic arguments.

## Result
The order of $A_{k+1}(N_1, \dots, N_{k+1})$ is established unconditionally for $k \in \{2,3,4,5\}$ (Theorem 1.3) and conditionally — under $\log y_k \le (\log y_1)^{1+\delta}$ — for $k \ge 6$ (Theorem 1.4). The constant $\alpha = \alpha(k; \mathbf{y})$ satisfies $0.5288 \le \alpha < 1$, with $\alpha = 1/\log 2 \cdot \log(1/\log 2)$ in the equal-sides case recovering the Ford/Koukoulopoulos exponent $Q(k/\log(k+1))$. The optimality range (1.2) is non-empty exactly when $k \ge 6$, explaining why the method's natural ceiling is $k = 5$.

## Why it matters here
General background; no direct arena tie. Multiplicative-structure / divisor-distribution machinery (Poisson model of $\omega$, hyperplane-proximity estimates, $Q$-function exponents) is adjacent to sieve theory and could inform autocorrelation or extremal counting problems, but no current Einstein Arena problem is a direct application.

## Open questions / connections
- Extends Ford's $k=1$ result [Fo08a, Fo08b] and the author's equal-sides $k\ge 2$ result [K10a] to arbitrary side lengths.
- Open: tight order of $A_{k+1}$ for $k \ge 6$ when $\alpha$ violates condition (1.1) — heuristics in Section 2 predict a strictly smaller order but no proof.
- The Poisson-hyperplane-proximity estimates of Section 4 may have independent use in problems where divisor counts are constrained to lie near a linear subspace.

## Key terms
Erdős multiplication table, generalized divisor problem, Ford theorem, Koukoulopoulos, Poisson approximation, omega function, Q-function exponent, local-to-global reduction, anatomy of integers, Smirnov statistics, order statistics, divisor distribution, sieve methods, low-moment method
