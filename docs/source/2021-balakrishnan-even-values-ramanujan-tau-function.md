---
type: source
kind: paper
title: Even Values of Ramanujan’s Tau-Function
authors: Jennifer S. Balakrishnan, K. Ono, Wei-Lun Tsai
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.00111
source_local: ../raw/2021-balakrishnan-even-values-ramanujan-tau-function.pdf
topic: general-knowledge
cites:
---

# Even Values of Ramanujan's Tau-Function

**Authors:** Jennifer S. Balakrishnan, K. Ono, Wei-Lun Tsai  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.00111

## One-line
First explicit families of *even* integers proven never to occur as values of Ramanujan's $\tau(n)$, extending the Lehmer-style "is $\alpha$ a tau-value?" program from odd to even $\alpha$.

## Key claim
For every $n$, $\tau(n) \notin \{\pm 2\ell : 3 \le \ell < 100 \text{ prime}\} \cup \{\pm 2\ell^2 : 3 \le \ell < 100\} \cup \{\pm 2\ell^3 : 3 \le \ell < 100,\ \ell \ne 59\} \cup \{\pm 2 \cdot 691\}$, plus infinitely many higher powers $\pm 2\ell^j$ parameterized by arithmetic-progression sets $S^\pm$ on $j \pmod{t}$ with $t \mid 44$.

## Method
Combines three ingredients: (i) the prime-divisor lower bound $\Omega(\tau(n)) \ge \sum_{p\mid n}(\sigma_0(\mathrm{ord}_p(n)+1)-1) \ge \omega(n)$ from Balakrishnan-Craig-Ono-Tsai, which forces $n$ to have at most two prime factors when $\tau(n)=\pm 2\ell$; (ii) the Bilu-Hanrot-Voutier classification of defective Lucas numbers applied to the sequences $\{\tau(p^m)\}$, ruling out $\pm 2\ell^i$ as defective; (iii) Ramanujan's classical mod-$2,3,5,7,23$ congruences on $\tau(p)$ to eliminate the remaining $m=1$ case, together with the Bennett-Gherga-Patel-Siksek result $|\tau(n)| \ne \ell^b$ for $3 \le \ell < 100$.

## Result
For example $\tau(n) \notin \{2 \cdot 97^j : j \not\equiv 0 \pmod{44}\} \cup \{-2 \cdot 97^j : j \ge 1\}$, and for the 18 primes $\ell \in \{7,11,13,19,23,29,31,37,41,43,47,53,61,67,71,73,79,97\}$, $\tau(n) \ne -2\ell^j$ for all $j \ge 1$. Method generalizes mutatis mutandis to integer-coefficient newforms with residually reducible mod-2 Galois representation.

## Why it matters here
General background; no direct arena tie. Tangentially informs modular-forms / $L$-function machinery (relevant to autocorrelation and Cohn-Elkies-style problems through the role of newform coefficients), but the arena's 23 problems don't directly require tau-value avoidance.

## Open questions / connections
- Extends the line of work from Murty-Murty-Shorey 1987 (odd $\alpha$) through Bennett-Gherga-Patel-Siksek 2021 ($|\tau(n)| = \ell^b$ impossible).
- Lehmer's conjecture $\tau(n) \ne 0$ remains the parent open problem.
- Whether the prime $\ell = 59$ exclusion for $\pm 2\ell^3$ can be removed via curve-point analysis is left implicit.
- Generalization to higher-weight newforms with arbitrary mod-2 behavior is sketched but not carried out.

## Key terms
Ramanujan tau function, Lehmer conjecture, newforms, modular forms, Lucas sequences, primitive prime divisors, Bilu-Hanrot-Voutier, residually reducible Galois representation, Hecke eigenform, hyperelliptic curves, Thue equations, Deligne bound
