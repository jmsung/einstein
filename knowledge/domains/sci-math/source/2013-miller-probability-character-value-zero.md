---
type: source
kind: paper
title: The probability that a character value is zero for the symmetric group
authors: A. Miller
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1306.1219
source_local: ../raw/2013-miller-probability-character-value-zero.pdf
topic: general-knowledge
cites:
---

# The probability that a character value is zero for the symmetric group

**Authors:** A. Miller  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1306.1219

## One-line
Proves that a uniformly random irreducible character $\chi$ of $S_n$ evaluated at a uniformly random element $g$ vanishes with probability tending to $1$ as $n \to \infty$.

## Key claim
$P_n = \Pr[\chi(g) = 0] \to 1$ as $n \to \infty$ for $S_n$ (and by restriction, for $A_n$), where $\chi$ is drawn uniformly from $\mathrm{Irr}(S_n)$ and $g$ uniformly from $S_n$.

## Method
Centralizer-orthogonality lemma: for any set $\Omega_n$ of partitions, $P_n \geq Q_n - |\Omega_n|/p_n$ where $Q_n = \Pr[\lambda(g) \in \Omega_n]$, using $\sum_\chi |\chi(g)|^2 = z_\lambda$ so at least $p_n - z_\lambda$ characters vanish at $g$. Choose $\Omega_n$ = partitions with largest part $\lambda_1 \geq C\sqrt{n}(\log n + f(n))$; combine Erdős–Lehner (counting partitions by largest part) with Goncharov (cycle-count CLT: number of cycles $\approx \log n$) to force $Q_n \to 1$ while $|\Omega_n|/p_n \to 0$.

## Result
Theorem: $P_n \to 1$ for $S_n$. Corollary: $P_n \to 1$ for $A_n$, via the standard restriction correspondence (non-self-conjugate $\lambda$ contribute two extensions, self-conjugate ones split). A general proposition holds for any finite group: $P(G) \geq Q(G,\Omega) - R(G,\Omega)$, maximized when $\Omega$ is the set of larger-than-average conjugacy classes ($|\mathrm{Cl}(G)| \geq |C_G(g)|$).

## Why it matters here
General background; no direct arena tie. Sparsity of character tables is a structural fact about $S_n$ representation theory; could weakly inform combinatorial counting via characters but does not bear on current arena problems (sphere packing, autocorrelation, kissing, sieve).

## Open questions / connections
- Question 1: Does $P(G) \to 1$ for random finite simple groups of bounded size? Conjecturally yes.
- Question 2: If $\chi$ and class $K$ are both drawn uniformly (weighting classes equally rather than by size), does $\Pr[\chi(g_K) = 0]$ converge — to $1/e$ or $1/3$?
- Question 3: Does the ratio of positive to negative entries in the character table of $S_n$ tend to $1$?

## Key terms
symmetric group, character table, irreducible characters, character zeros, random partitions, Erdős–Lehner, Goncharov, cycle distribution, centralizer orthogonality, conjugacy classes, alternating group, partition asymptotics
