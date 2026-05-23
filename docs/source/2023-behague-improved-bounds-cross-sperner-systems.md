---
type: source
kind: paper
title: Improved Bounds for Cross-Sperner Systems
authors: Natalie C. Behague, Akina Kuperus, Natasha Morrison, Ashna Wright
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.02516
source_local: ../raw/2023-behague-improved-bounds-cross-sperner-systems.pdf
topic: general-knowledge
cites:
---

# Improved Bounds for Cross-Sperner Systems

**Authors:** Natalie C. Behague, Akina Kuperus, Natasha Morrison, Ashna Wright  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.02516

## One-line
New upper and lower bounds on the sum $\sigma(n,k)$ and product $\pi(n,k)$ of sizes of $k$-tuples of set families on $[n]$ in which no two families contain a comparable pair, disproving a 2011 conjecture of Gerbner et al.

## Key claim
For all $k \geq 2$ and $n$ large, $\pi(n,k) \geq (2^n/(ek))^k$, exponentially exceeding the prior conjectured upper bound $2^{k(n-\ell^\ast)}$ (with $\binom{\ell^\ast}{\lfloor \ell^\ast/2\rfloor} \geq k$); also $\pi(n,k) \leq (2^n/k^2)^k \cdot k^k / (\lfloor k/2\rfloor^{k/2} \lceil k/2\rceil^{k/2})$, and $2^n - 2\sqrt{3/2}\sqrt{2^n k} + 2(k-1) \leq \sigma(n,k) \leq 2^n - 2\sqrt{2^n(k-1)} + 2(k-1)$ for $n \geq 2k$.

## Method
Reduces $k$-tuple bounds to pair bounds via a partition lemma: if $(F_1,\ldots,F_k)$ is cross-Sperner then so is $(\cup_{i\leq j} F_i, \cup_{i>j} F_i)$, then applies AM–GM. The key tool is the **comparability number** $c(n,m) = \min\{|\{X: X \text{ comparable to some } A \in F\}| : |F|=m\}$, lower-bounded by $2^{n/2+1}\sqrt{m} - m$ via the Harris–Kleitman (FKG) inequality applied to the upset/downset $U_F, D_F$ of a convex extremal family. Lower bound for $\pi$ uses a product construction: partition $[n]$ into $k$ blocks $A_i$, take $X_i \subseteq P(A_i)$ as colex initial segments of measure $\approx 1/k$.

## Result
Disproof of Gerbner–Lemons–Palmer–Patkós–Szécsi (2011) conjecture $\pi(n,k) \leq 2^{k(n-\ell^\ast)}$ by exponential factor $(k \cdot g(k))^k$ with $g(k)\to\infty$. Upper bound on $\pi$ improves prior by factor $2^k$. For $\sigma$, sum bounds are within a constant factor $\sqrt{3/2}$ of each other; when $k=2^a$ and $n - \log_2 k$ even, lower bound tightens to $2^n - 2\sqrt{2^n k}(1-1/(2k))^{1/2} + 2(k-1)$, matching the upper bound asymptotically. Recovers Gerbner et al.'s pair sum bound $2^n - 2^{\lfloor n/2\rfloor} - 2^{\lceil n/2 \rceil} + 2$ for all $n \geq 2$ (was only large $n$).

## Why it matters here
General background; no direct arena tie — this is extremal poset combinatorics (Sperner-type, antichain), not directly any of the 23 problem categories. Potentially informs sieve-theory / discrete-geometry problems via the AM–GM-then-partition reduction trick and FKG-style correlation inequalities; the convex-family lemma may be reusable when minimizing comparable-pair counts under cardinality constraints.

## Open questions / connections
- Conjecture 5.1: $\pi(n,k) = (1+o(1)) \cdot 2^{kn}(k-1)^{k-1}/k^k$ for fixed $k$, large $n$ — close the factor-$(2/e)^k$ gap.
- Small cases ($f(4,3)=9$, $f(5,3)\geq 81$, $f(6,3)\geq 810$, $f(5,4)\geq 108$) — exact values unknown.
- Concurrent work of Gowty–Horsley–Mammoliti (arXiv:2212.13112) gives a different proof of the comparability bound and further analysis of $c(n,m)$-minimizers; extends Kleitman 1966 and Seymour 1973.
- Extension: cross-Sperner under additional intersection constraints (Erdős–Ko–Rado-style), unstudied.

## Key terms
cross-Sperner, antichain, Sperner's theorem, comparability number, Harris-Kleitman inequality, FKG inequality, upset, downset, AM-GM, colex initial segment, extremal set theory, Kleitman, Seymour, Gerbner
