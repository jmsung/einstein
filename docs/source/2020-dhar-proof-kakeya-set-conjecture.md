---
type: source
kind: paper
title: Proof of the Kakeya set conjecture over rings of integers modulo square-free N
authors: Manik Dhar, Zeev Dvir
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2011.11225
source_local: ../raw/2020-dhar-proof-kakeya-set-conjecture.pdf
topic: general-knowledge
cites:
---

# Proof of the Kakeya set conjecture over rings of integers modulo square-free N

**Authors:** Manik Dhar, Zeev Dvir  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2011.11225

## One-line
Proves that any Kakeya set in $(\mathbb{Z}/N\mathbb{Z})^n$ for square-free $N$ has size $\geq C_{n,\epsilon} N^{n-\epsilon}$, settling a case of the Hickman–Wright conjecture.

## Key claim
For $N = p_1 \cdots p_r$ a product of distinct primes, any Kakeya set $S \subseteq (\mathbb{Z}/N\mathbb{Z})^n$ satisfies $|S| \geq N^n / \prod_{i=1}^{r}(2 - 1/p_i)^n \geq N^n / 2^{rn}$, which is $\geq N^{n - O(n/\log\log N)}$.

## Method
Reformulates the polynomial method via the **line-matrix** $M_S$ (rows = direction-indexed indicator vectors of lines in $S$) whose $\mathbb{F}_p$-rank lower-bounds $|S|$. Constructs fixed matrices $A, B$ with $A = M_S \cdot B$ and $A$ of high rank, using point-hyperplane incidence matrices $W_{p,n}$ and the $\mathbb{F}_p$-rank bound $\binom{p+n-2}{n-1}+1$ from coding theory (Goethals–Delsarte, MacWilliams–Mann, Smith). Composite-$N$ case uses Chinese remainder theorem + Kronecker products $W_{p,n} \otimes I_{q^n}$, inducting on number of prime factors; the tighter exponent uses Hasse derivatives and multiplicity Schwartz–Zippel (DKSS).

## Result
Theorem 1.4 gives $|S| \geq N^n / \prod (2-1/p_i)^n$ for square-free $N$. Matching upper bound (Theorem 1.5) from Saraf–Sudan product: $|S| \leq \prod (p_i^n / 2^{n-1} + C p_i^{n-1})$, leaving a gap of at most $2^r = N^{o(1)}$. Reduction (Theorem 1.6): for prime powers, $|S| \geq \text{rank}_{\mathbb{F}_p}(W_{p^k,n})$; currently only $\approx p^{kn/2}$ rank known via matching-vector families (Yuan–Guo–Kan), insufficient for new bounds.

## Why it matters here
General background; no direct arena tie. The line-matrix → rank-of-incidence-matrix reduction is a clean polynomial-method reformulation worth noting for combinatorial/extremal problems where direct polynomial interpolation fails (e.g., when degree budget is exhausted).

## Open questions / connections
- Lower-bound $\text{rank}_{\mathbb{F}_p}(W_{p^k,n})$ by $p^{(1-\epsilon)kn}$ — would close the general $N$ case (currently only $p^{kn/2}$ via MV families, with [DH13b] showing MV families can't exceed $N^{n/2+O(1)}$).
- Extends [Dvi09] polynomial-method proof and [DKSS13] multiplicity extension to composite modulus.
- Connects to $p$-adic Kakeya Minkowski dimension via [HW18]; tight 2D bound $|S| \geq |R|^2/2k$ for $\mathbb{Z}/p^k\mathbb{Z}$ from [DH13a].

## Key terms
Kakeya set, finite field Kakeya conjecture, polynomial method, Hasse derivatives, multiplicity Schwartz-Zippel, point-hyperplane incidence matrix, line-matrix, Kronecker product, Chinese remainder theorem, matching vector family, Dvir, DKSS, square-free modulus
