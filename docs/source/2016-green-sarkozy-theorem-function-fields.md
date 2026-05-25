---
type: source
kind: paper
title: Sarkozy's theorem in function fields
authors: B. Green
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1605.07263
source_local: ../raw/2016-green-sarkozy-theorem-function-fields.pdf
topic: general-knowledge
cites:
---

# Sarkozy's theorem in function fields

**Authors:** B. Green  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1605.07263

## One-line
Proves a function-field analogue of Sárközy's theorem with polynomial (not logarithmic) density bounds, using the Croot–Lev–Pach polynomial method.

## Key claim
For $k \geq 2$, $q$ a prime power, if $A \subset P_{q,n}$ (polynomials over $\mathbb{F}_q$ of degree $< n$) has $|A| > 2q^{(1-c(k,q))n}$ with $c(k,q) = (2k^2 D_q(k)^2 \log q)^{-1}$ where $D_q(k)$ is the digit sum of $k$ in base $q$, then $A$ contains distinct $p, p'$ with $p - p' = b(T)^k$ for some $b \in \mathbb{F}_q[T]$.

## Method
Croot–Lev–Pach polynomial method: represent $|\Phi^{-1}(x)|$ (counting preimages of a polynomial map $\Phi: \mathbb{F}_q^m \to \mathbb{F}_q^n$) as a low-degree polynomial $P$ supported on $\mathrm{im}(\Phi)$ with $P(0) \neq 0$. If $A - A$ avoids $\mathrm{im}(\Phi) \setminus \{0\}$, the matrix $M_{a,a'} = P(a-a')$ has rank $|A|$, bounded above by twice the number of low-degree monomials. Hoeffding's inequality converts this count to the exponential bound $|A| \leq 2q^n e^{-m^2/2nd^2}$.

## Result
Theorem 1.3 (master result): $|A| \leq 2q^n e^{-m^2/2nd^2}$ when $A - A$ meets $\mathrm{im}(\Phi)$ only at $0$, where $\Phi: \mathbb{F}_q^m \to \mathbb{F}_q^n$ has total degree $d$ and $|\Phi^{-1}(0)|$ is coprime to $q$. Theorems 1.1 and 1.2 specialize to $k$-th powers and to general degree-$k$ polynomials $F$ (with root count coprime to $q$). These polynomial-in-$N$ savings ($N^{1-c_F}$ analogue) are dramatically stronger than the $(\log N)^{-c_F}$ bound known over $\mathbb{Z}$.

## Why it matters here
General background; no direct arena tie — but the **Croot–Lev–Pach polynomial method** is the engine behind the cap-set $O((2.756)^n)$ breakthrough (Ellenberg–Gijswijt, cited as [3]) and could inform extremal combinatorics problems involving forbidden difference patterns in $\mathbb{F}_q^n$.

## Open questions / connections
- Can the polynomial method yield analogous polynomial savings for the **integer** Sárközy problem? Currently only $(\log N)^{-c}$-type bounds known (Balog–Pelikán–Pintz–Szemerédi [1]).
- Construction-side gap: Link [5] / Ruzsa [6] give $|A| = N^{3/4}$ square-difference-free sets in $P_{5,2n}$ — large gap vs. the $1 - c(k,q)$ upper bound.
- Extends Croot–Lev–Pach [2] (3-APs in $\mathbb{Z}_4^n$) and Ellenberg–Gijswijt [3] (cap sets in $\mathbb{F}_q^n$) beyond linear forbidden patterns to polynomial image sets.

## Key terms
Sárközy theorem, function fields, Croot–Lev–Pach polynomial method, cap set problem, Ellenberg–Gijswijt, polynomial method, $\mathbb{F}_q$, difference sets, $k$-th powers, slice rank, Hoeffding inequality, extremal combinatorics
