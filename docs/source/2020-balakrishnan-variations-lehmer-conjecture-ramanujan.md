---
type: source
kind: paper
title: Variations of Lehmer's Conjecture for Ramanujan's tau-function
authors: Jennifer S. Balakrishnan, William Craig, K. Ono
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.10345
source_local: ../raw/2020-balakrishnan-variations-lehmer-conjecture-ramanujan.pdf
topic: general-knowledge
cites:
---

# Variations of Lehmer's Conjecture for Ramanujan's tau-function

**Authors:** Jennifer S. Balakrishnan, William Craig, K. Ono  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.10345

## One-line
Proves that Ramanujan's $\tau(n)$ never takes the values $\pm 1, \pm 3, \pm 5, \pm 7, \pm 691$ for $n > 1$, a structured variant of Lehmer's nonvanishing conjecture.

## Key claim
**Theorem 1.1:** For all $n > 1$, $\tau(n) \notin \{\pm 1, \pm 3, \pm 5, \pm 7, \pm 691\}$. The set is exactly the small odd primes plus $691$ — the primes appearing in Ramanujan's classical congruences (mod 3, 5, 7, 691).

## Method
Three-tool stack: (1) **Bilu–Hanrot–Voutier** primitive-prime-divisor theory for Lucas sequences $u_n(\alpha_p,\beta_p) = (\alpha_p^n - \beta_p^n)/(\alpha_p - \beta_p)$ with $\alpha_p,\beta_p$ roots of $X^2 - \tau(p)X + p^{11}$; this reduces $|\tau(n)| = \ell$ to $n = p^d$ with $d+1$ an odd prime dividing $\ell(\ell^2-1)$. (2) **Ramanujan's mod-$\ell$ congruences** (1.2) pin down the admissible $d$ via the index $m_\ell(p) = \min\{n : \ell \mid \tau(p^n)\}$. (3) Resulting Diophantine constraints become integer points on hyperelliptic curves $H_{d,\ell}^\pm: Y^2 = 5X^{2d}\pm 4\ell$ and $C_{d,\ell}^\pm: Y^2 = X^{2d-1}\pm\ell$, or Thue equations $F_{2m}(p^{11},\tau(p)^2) = \pm\ell$ — solved by **Chabauty–Coleman** (rank-0 Jacobians, $p=3$ Coleman integrals in SageMath) and the **Bilu–Hanrot Thue solver** in PARI/GP.

## Result
For $\ell \in \{3,5,7\}$ the value of $d$ is forced (2, 4, 6 respectively) by $m_\ell(p)$, and the relevant curves $C_6^\pm{}_{,3}$, $H_{11}^\pm{}_{,5}$, $F_6(X,Y)=\pm 7$ have no solutions of the required form (Lemmas 2.2, 2.5(1)). For $\ell = 691$, four cases $d \in \{2,4,22,690\}$ must be killed: $C_6^\pm{}_{,691}$ and $H_{11}^\pm{}_{,691}$ have no integer points (Chabauty–Coleman + a degree-11 / degree-22 Thue equation), and $F_{22}(X,Y)=\pm 691$, $F_{690}(X,Y)=\pm 691$ have no nontrivial solutions — the degree-345 case reduced via $F_{p-1}(X,Y) = F_p(X, Y-2X)$ to known continued-fraction / convergent arguments from BHV.

## Why it matters here
General background; no direct arena tie. The arena problems are extremal/optimization-flavored (sphere packing, autocorrelation, kissing), while this is pure analytic+arithmetic number theory on modular forms. It is methodologically interesting only as an example of Chabauty–Coleman + Thue-equation Diophantine pipelines, which do not currently appear in any Einstein Arena problem.

## Open questions / connections
- Lehmer's original conjecture ($\tau(n) \neq 0$) remains open; this work is a structured *variant*, not a step toward Lehmer itself.
- Extends Murty–Murty–Saradha (1987), which used linear forms in logarithms to handle odd $\alpha$ for large $n$ with intractable bounds; the BHV+Chabauty pipeline replaces the ineffective approach with explicit curve computations.
- Companion paper [2] (Balakrishnan–Craig–Ono–Tsai) generalizes to all newforms with trivial mod-2 residual Galois representation, extending the excluded set to $\{\pm 1, \pm 3, \pm 5, \pm 7, \pm 13, \pm 17, -19, \pm 23, \pm 37, \pm 691\}$ and more under GRH.
- Calegari–Sardari (arXiv:2003.07570) attack a different angle: only finitely many non-CM newforms of fixed tame level have vanishing $p$-th coefficient.

## Key terms
Lehmer conjecture, Ramanujan tau-function, Lucas sequences, primitive prime divisors, Bilu-Hanrot-Voutier, Chabauty-Coleman method, hyperelliptic curves, Thue equations, Ramanujan congruences, modular forms, Hecke multiplicativity, Mordell-Weil rank, Coleman integrals, PARI Magma SageMath
