---
type: source
kind: paper
title: Variants of Lehmer's speculation for newforms
authors: Jennifer S. Balakrishnan, William Craig, K. Ono, Wei-Lun Tsai
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.10354
source_local: ../raw/2020-balakrishnan-variants-lehmer-speculation-newforms.pdf
topic: general-knowledge
cites:
---

# Variants of Lehmer's speculation for newforms

**Authors:** Jennifer S. Balakrishnan, William Craig, K. Ono, Wei-Lun Tsai  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.10354

## One-line
Gives an algorithm to decide whether a fixed odd integer (e.g. $\pm\ell^m$) can occur as a Fourier coefficient $a_f(n)$ of a newform with integer coefficients and trivial mod-2 Galois representation, and rules out many small odd primes as values of Ramanujan's $\tau(n)$.

## Key claim
For every $n>1$, $\tau(n) \notin \{\pm 1, \pm 3, \pm 5, \pm 7, \pm 13, \pm 17, -19, \pm 23, \pm 37, \pm 691\}$ (unconditional), with a much larger excluded set $\{\pm\ell: 41\le\ell\le 97\}$ minus a handful under GRH. More generally, for an odd prime $\ell$ with $\ell\nmid \tau(\ell)$, if $\tau(n)=\pm\ell^m$ then $n=p^{d-1}$ with $p$ odd prime and $d\mid \ell(\ell^2-1)$ odd prime — only finitely many such $n$. In the weight aspect, $\pm\ell^m$ is not a coefficient of any qualifying newform with weight $2k > M_\pm(\ell,m) = O_\ell(m)$, with explicit constants like $M_+(3,m) \le 2m+10^{23}\sqrt{m}$.

## Method
Reduces newform coefficients $a_f(p^{d-1})$ to **Lucas sequences** via Hecke recursion, then applies Bilu–Hanrot–Voutier's theorem that every Lucas number $u_n$ with $n>30$ has a primitive prime divisor. The classification of defective Lucas numbers (combined with Catalan's conjecture for divisibility constraints) forces $|a_f(n)|=\ell^m$ to live on finitely many algebraic curves: elliptic curves $Y^2 = X^{2k-1} \pm \ell^m$, hyperelliptic curves, and Thue equations $F_{d-1}(X,Y)=\pm\ell$ derived from the generating function $1/(1-\sqrt{Y}T+XT^2)$. Integer points are then enumerated via PARI/GP Thue solvers, Chabauty–Coleman, and the Bilu–Hanrot–Voutier bound $|X|\le e^8$ for primes $31\le p\le 787$.

## Result
Theorem 1.2 lists explicit small odd primes that cannot be $|\tau(n)|$; Theorem 1.3 extends this to all newforms in $S_{2k}(\Gamma_0(2N))\cap\mathbb{Z}[[q]]$ with trivial mod-2 representation, with case splits by weight $2k\in\{4,6,8,10\}$ and by congruences like $\gcd(3\cdot 5\cdot 7, 2k-1)=1$. Theorem 1.5: $\Omega(\tau(n)) \ge \sum_{p\mid n}(\sigma_0(\mathrm{ord}_p(n)+1)-1) \ge \omega(n)$ when $n$ has only ordinary prime factors — sharp, achieved by Lehmer's $\tau(2^{512})$ being prime.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems (sphere packing, autocorrelation, kissing numbers, extremal graphs) don't use newform-coefficient arithmetic or Lucas-sequence primitive-divisor theorems. The only loose connection is methodological — reducing a Diophantine question to integer points on finitely many curves, a pattern that occasionally surfaces in combinatorial extremal problems but isn't operative for the current 23 problems.

## Open questions / connections
- Generalize the algorithm beyond prime powers to arbitrary odd $\alpha$ (claimed feasible via Hecke multiplicativity; Bennett–Gherga–Patel–Siksek already settled $|\tau(n)|=\ell^m$ for all $3\le\ell<100$).
- Extend to odd-level newforms and real Nebentypus; weight-2 case is explicitly out of scope (positive-genus requirement fails).
- Unconditional versions of the GRH-conditional Thue-equation enumerations for $41\le\ell\le 97$.

## Key terms
Ramanujan tau function, Lehmer's conjecture, newforms, Hecke eigenforms, Lucas sequences, primitive prime divisors, Bilu-Hanrot-Voutier, Thue equations, Chabauty-Coleman, Galois representations, Siegel's theorem, integer points on curves, modular forms, Diophantine equations, Atkin-Lehner
