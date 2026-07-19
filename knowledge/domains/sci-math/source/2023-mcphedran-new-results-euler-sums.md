---
type: source
kind: paper
title: New Results for Euler Sums
authors: Ross C. McPhedran, David H. Bailey
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.06294v4
source_local: ../raw/2023-mcphedran-new-results-euler-sums.pdf
topic: general-knowledge
cites: 
---

# New Results for Euler Sums

**Authors:** Ross C. McPhedran, David H. Bailey  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2311.06294v4

## One-line
Extends the closed-form catalog of classical Euler sums $\sum_k H(k)^m/k^n$ and their mixed-denominator generalizations up to order 12, and introduces harmonic-Stieltjes constants $\gamma_p^H$ as their natural asymptotic counterparts.

## Key claim
For mixed Euler sums $M(m,n_0,n_1,\ldots,n_t) = \sum_{k\ge1} H(k)^m / [k^{n_0}(k+1)^{n_1}\cdots(k+t)^{n_t}]$ of order $r \le 12$, every such sum is a rational linear combination of an explicit finite "atomic" basis consisting of products of $\zeta$-values plus five conjecturally irreducible constants $M(2,6), M(2,8), M(3,8), M(2,10), M(4,8)$ (Theorem 1). PSLQ rules out integer relations with Euclidean norm below $5.88\cdot10^{22}$ (order 8), $1.28\cdot10^{13}$ (order 10), and $2.13\cdot10^{6}$ (order 12).

## Method
High-precision numerical evaluation (enhanced Euler–Maclaurin scheme to 400+ digits) combined with the PSLQ integer-relation algorithm to detect rational linear dependencies among candidate basis constants. Algebraic reduction uses two elementary techniques: "completing the square" to shift $(k+w)$ denominators to $k$, and partial-fraction decomposition (e.g. $\tfrac1{k^2(k+1)^2} = -\tfrac2k + \tfrac2{k+1} + \tfrac1{k^2} + \tfrac1{(k+1)^2}$). The integral approximation $\sum_k (\log k + \gamma)^m/k^2 \approx m!\,[e^\gamma]_m$ (truncated exponential) gives sharp asymptotics for $I_h(m,2)$.

## Result
Closed-form rational-zeta expressions are tabulated for all $I_h(m,n)$ at orders 8–12 (assuming $I_h(2,6), I_h(2,8), I_h(3,8), I_h(2,10), I_h(4,8)$ as basis constants), plus hundreds of mixed-denominator sums $M(m,n_0,\ldots,n_t)$ in the appendix. The harmonic-Stieltjes constants $\gamma_p^H = \lim_n [\sum_{k=1}^n H_k^{p-1}/k - H_n^p/p]$ are all positive and grow rapidly with $p$; explicit finite-sum identity $\sum_{k=1}^n H_k^{p-1}/k = \tfrac1p H_n^p + D_{p,1}H_n^{(p)} + \sum_{q=2}^{p-1} D_{p,q}\sum_k H_k^{q-1}/k^{p-q+1}$ with tabulated rational coefficients $D_{p,q}$ (symmetric / antisymmetric per parity of $p$).

## Why it matters here
General background; no direct arena tie — this is analytic number theory (Euler sums, Stieltjes constants, Keiper–Li / Riemann hypothesis context), not in the sphere-packing / kissing / autocorrelation / extremal-combinatorics families the agent targets. The PSLQ-driven "atomic basis + integer-relation hunt" methodology is the only transferable element: it generalizes the workflow already used in `findings/` for hunting closed forms of optimizer outputs.

## Open questions / connections
- Are $M(2,6), M(2,8), M(3,8), M(2,10), M(4,8)$ genuinely irreducible, or expressible in terms of polylogarithms / multiple zeta values not yet in the basis? (PSLQ lower bounds rule out small-coefficient relations but prove nothing.)
- Does Theorem 1's basis structure extend to all orders, with new "atoms" appearing at each order? (Conjectured but unproven.)
- Asymptotic behavior of harmonic-Stieltjes constants $\gamma_p^H$ as $p \to \infty$ — only preliminary results given.
- Connection to Keiper–Li criterion coefficients $a_n$ and $C_{n,p}$ for the Riemann hypothesis (the original motivation in [1]).

## Key terms
Euler sums, harmonic numbers, Stieltjes constants, Riemann zeta function, multiple zeta values, PSLQ integer-relation algorithm, experimental mathematics, Euler-Maclaurin summation, Keiper-Li criterion, partial fraction decomposition, Bailey Borwein, mixed Euler sums
