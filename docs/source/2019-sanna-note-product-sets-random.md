---
type: source
kind: paper
title: A note on product sets of random sets
authors: C. Sanna
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.05188
source_local: ../raw/2019-sanna-note-product-sets-random.pdf
topic: general-knowledge
cites:
---

# A note on product sets of random sets

**Authors:** C. Sanna  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.05188

## One-line
Generalizes a Cilleruelo–Ramana–Ramaré asymptotic for the size of the product set $A^2$ of a random subset of $\{1,\dots,n\}$ to multi-set, multi-power products $A_1^{k_1}\cdots A_s^{k_s}$.

## Key claim
If $A_i \sim B(n_i,\alpha_i)$ are independent random subsets (each element of $\{1,\dots,n_i\}$ included i.i.d. with probability $\alpha_i$), $k_i$ are fixed positive integers, $\alpha_i n_i \to \infty$, and $\alpha_i = o\!\big((\log n_1)^{k_1-1}\prod_{j=2}^{s}(\log n_j)^{k_j}\big)^{-(k_1+\cdots+k_s-1)/2}$, then $|A_1^{k_1}\cdots A_s^{k_s}| \sim \frac{|A_1|^{k_1}}{k_1!}\cdots\frac{|A_s|^{k_s}}{k_s!}$ with probability $1-o(1)$ (Theorem 1.2).

## Method
Second-moment / Bonferroni-inequality count of expected product-set size, combined with a Rankin-method bound (Lemma 3.1) on $\sum 1/(a_1\cdots a_m) \ll (\log x)^m$. The crux is Lemma 3.3, a matrix-decomposition upper bound on the number of solutions of $a_1\cdots a_n = b_1\cdots b_m$ with bounded factors, used to control collision pairs $\Pr(E_a \wedge E_{a'})$. Closes with Chebyshev on $|A|^k$ and Markov on the slack between $|A^k|$ and $|A|^k/k!$.

## Result
The product set is asymptotically as large as if all $k_i$-tuples produced distinct products — i.e., almost no multiplicative coincidences occur in the random regime. Specifically $\mathbb{E}|A_1^{k_1}\cdots A_s^{k_s}| \sim \prod_i (\alpha_i n_i)^{k_i}/k_i!$ (Lemma 4.3), and concentration around this mean follows. The density threshold $\alpha_i$ may grow nearly as fast as the inverse of a polylogarithmic factor before collisions start to dominate.

## Why it matters here
General background; no direct arena tie — this is multiplicative number theory / random-set combinatorics, not packing, autocorrelation, or extremal geometry. Marginally relevant to Sidon-set / sumset-style problems where one asks "how often does a random structured set behave like a generic one?" but the multiplicative setting is orthogonal to the additive/geometric problems on Einstein Arena.

## Open questions / connections
- Extends Cilleruelo–Ramana–Ramaré (s=1, k=2); natural to ask whether the polylog upper bound on $\alpha_i$ is sharp or an artifact of the second-moment method.
- Ties to Erdős/Ford/Tenenbaum multiplication-table problem $M_n = |\{1,\dots,n\}^2|$ — random-set analogue of the deterministic order-of-magnitude theory.
- Koukoulopoulos's uniform bounds for $|\{1,\dots,n_1\}\cdots\{1,\dots,n_s\}|$ — does the random asymptotic match the deterministic upper bound in the dense regime?

## Key terms
product set, random set, probabilistic model $B(n,\alpha)$, multiplication table problem, Erdős, Ford, Tenenbaum, Cilleruelo–Ramana–Ramaré, Rankin's method, Bonferroni inequality, multiplicative coincidences, second-moment method
