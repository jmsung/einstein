---
type: source
kind: paper
title: Permutations fixing a k-set
authors: Sean Eberhard, Kevin Ford, B. Green
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.04465
source_local: ../raw/2015-eberhard-permutations-fixing-k-set.pdf
topic: general-knowledge
cites:
---

# Permutations fixing a k-set

**Authors:** Sean Eberhard, Kevin Ford, B. Green  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.04465

## One-line
Sharp asymptotic order for the probability that a random permutation in $S_n$ has an invariant set of exactly size $k$.

## Key claim
$i(n,k) \asymp k^{-\delta}(1+\log k)^{-3/2}$ uniformly for $1 \le k \le n/2$, where $\delta = 1 - \frac{1+\log\log 2}{\log 2} \approx 0.08607$. As a corollary, the proportion of $\pi \in S_n$ in a transitive subgroup not containing $A_n$ is $\gg n^{-\delta}(\log n)^{-3/2}$ for even $n > 2$.

## Method
Transports Ford's number-theoretic technique (on integers having a divisor in $[y, 2y]$) to the permutation setting via the cycle/prime analogy: cycle lengths $a_i$ correspond to $\log\log p_i$ of prime factors. A permutation sieve (Proposition 2.1) gives two-sided estimates for cycle-type probabilities at finite $n$, enabling a local-to-global reduction $i(n,k) \asymp k^{-1} \mathbb{E}|\mathscr{L}(X_k)|$, where $\mathscr{L}$ is the subset-sum set of independent Poisson$(1/i)$ variables. Bounds on $\mathbb{E}|\mathscr{L}(X_k)|$ use a dyadic decomposition + Cauchy-Schwarz (lower) and a "cycle lemma" averaging trick that reduces a multinomial sum to a closed form, plus Ford's $U_r$ integral estimates (upper).

## Result
Establishes the sharp order $k^{-\delta}(1+\log k)^{-3/2}$ for $i(n,k)$ for all valid $k$, matching the integer-divisor analog. The exponent $\delta$ arises from a phase transition at $Y = \log k / \log 2 + O(1)$ cycles of length $\le k$, where $|\mathscr{L}(X_k)|$ switches between $2^Y$ and $\asymp k$ behavior; the $(\log k)^{-1/2}$ factor comes from the probability of this transition, and an additional $(\log k)^{-1}$ from order-statistics structure.

## Why it matters here
General background; no direct arena tie. Provides a clean template for "local-to-global" probabilistic reductions and dyadic decomposition arguments that could inform combinatorial / extremal counting problems on the wiki, and exemplifies the Erdős-style "find a phase transition, get the exponent" heuristic.

## Open questions / connections
- Is $i(\infty, k) \sim C k^{-\delta}(\log k)^{-3/2}$ for some explicit constant $C$? (Authors expect yes.)
- Is $i(\infty, k)$ monotonically decreasing in $k$? (Verified up to $k=30$ by Britnell-Wildon.)
- Matching upper bound $O(n^{-\delta}(\log n)^{-3/2})$ for Cameron's transitive-subgroup proportion (even $n$); for odd $n$, conjecturally $O(n^{-\delta'})$ with $\delta' > \delta$.
- Extends Ford's integer-divisor results [For08a, For08b] and refines Łuczak-Pyber's $k^{-1/100}$ bound; complements Pemantle-Peres-Rivin's fixed-$k$ result.

## Key terms
random permutations, cycle structure, invariant sets, Poisson cycle distribution, Ford constant delta, divisors of integers, Besicovitch problem, permutation sieve, cycle-prime analogy, Cameron's conjecture, transitive subgroups, symmetric group generation, dyadic decomposition, Bell numbers
