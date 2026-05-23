---
type: source
kind: paper
title: The structure of large sum-free sets in $\mathbb{F}_p^n$
authors: Leo Versteegen
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2303.00828
source_local: ../raw/2023-versteegen-structure-large-sum-free-sets.pdf
topic: general-knowledge
cites:
---

# The structure of large sum-free sets in $\mathbb{F}_p^n$

**Authors:** Leo Versteegen  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2303.00828

## One-line
Sharpens the structural theorem for large sum-free subsets of $\mathbb{F}_p^n$ ($p \equiv 2 \bmod 3$), proving that any sufficiently large such set is "normal" — contained in $(p+1)/3$ cosets of a codimension-1 subspace.

## Key claim
For $p \equiv 2 \bmod 3$, every sum-free $A \subset \mathbb{F}_p^n$ with $|A| \geq (m_p - 1/2 + 1/p)p^{n-1}$ (where $m_p = (p+1)/3$) is normal (Theorem 1.6). For $p=5$ specifically, the threshold drops to $|A| > 1.2 \cdot 5^{n-1}$ (Theorem 1.4), improving Lev's $1.5 \cdot 5^{n-1}$.

## Method
Induction on $n$ combined with additive-combinatorics machinery: Kneser's theorem (symmetry-group lower bound on $|A+B|$), Vosper's theorem (critical pairs as arithmetic progressions), and a coset-averaging lemma (Lemma 2.3) that finds two codimension-1 subspaces capturing $\geq |A|/p$ of $A$. Reduction proceeds by analyzing the distribution of $A$ across cosets of an $(n-2)$-dimensional subspace via "good/bad/doubly-bad" classification of offsets $t_v$ and case analysis on scattered/semi-scattered/focused rows. Replaces Lev's Fourier-theoretic step with the inductive $(n-2)$-dim argument, which retains strength as $|A|$ shrinks.

## Result
Theorem 1.6: threshold $(m_p - 1/2 + 1/p)p^{n-1}$ vs. prior Green–Ruzsa bound $(m_p - 1/(3p^2+3p))p^{n-1}$ — improvement by a positive proportion of $p^{n-1}$. Example 1.7 shows the bound cannot drop below $(m_p-1)p^{n-1}$. Theorem 1.4: $p=5$ threshold $1.2 \cdot 5^{n-1}$ vs. Lev's $1.5 \cdot 5^{n-1}$; Example 1.5 caps any future improvement at $1.12 \cdot 5^{n-1}$. Example 1.8 shows the picture breaks for $p \equiv 1 \bmod 3$: non-normal maximal sum-free sets exist in $\mathbb{F}_7^2$.

## Why it matters here
General background for the combinatorics/extremal-graph and sieve-theory problem families — sum-free set structure theorems are the canonical example of "inverse Freiman-style" theorems where size threshold forces coset structure. Adds a concrete template for inductive-on-dimension arguments using Kneser+Vosper, and a worked $\mathbb{F}_p^n$ vs $\mathbb{Z}_n$ contrast useful for any arena problem reducible to additive structure in vector spaces over small primes.

## Open questions / connections
- Exact threshold for $p=5$: somewhere in $[1.12, 1.2] \cdot 5^{n-1}$ — does $\lambda(\mathbb{F}_5^n)$ even achieve its supremum?
- Analogous structure theorem for $p \equiv 1 \bmod 3$ blocked by Example 1.8 (non-normal maximal sets in $\mathbb{F}_7^2$).
- Extends Davydov–Tombak / Clark–Pedersen ($p=2$, Thm 1.2), Lev 2005 ($p=3$), Green–Ruzsa 2005 (general $p$), Lev 2023 ($p=5$).
- Suggests analyzing non-normal sum-free sets in $\mathbb{F}_5^k$ for small fixed $k \geq 3$ as a route to tighter bounds.

## Key terms
sum-free set, Kneser's theorem, Vosper's theorem, $\mathbb{F}_p^n$, normal sum-free set, coset structure, symmetry group, critical pairs, Green-Ruzsa, Lev, Davydov-Tombak, additive combinatorics, arithmetic progression, inverse theorem, codimension-1 subspace
