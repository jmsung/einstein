---
type: source
kind: paper
title: A non-uniform extension of Baranyai's Theorem
authors: Jinye He, Hao Huang, Jie Ma
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2207.00277v1
source_local: ../raw/2022-he-non-uniform-extension-baranyai-theorem.pdf
topic: general-knowledge
cites: 
---

# A non-uniform extension of Baranyai's Theorem

**Authors:** Jinye He, Hao Huang, Jie Ma  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2207.00277v1

## One-line
Characterizes exactly when the hypergraph $K_n^{\le k}$ of all non-empty subsets of $[n]$ of size up to $k$ admits a 1-factorization, extending Baranyai's classical theorem to the non-uniform setting.

## Key claim
For $k < n/2$, $K_n^{\le k}$ is 1-factorable iff either (i) $n \equiv 0 \pmod{k}$ and $n \ge k(k-2)$, or (ii) $n \equiv -1 \pmod{k}$ and $n \ge k(\lceil k/2 \rceil - 1) - 1$; the $k \ge n/2$ case reduces to $K_n^{\le n-k-1}$. In particular, for fixed $k$ and large $n$, 1-factorability holds iff $n \equiv 0$ or $-1 \pmod{k}$.

## Method
Reduce 1-factorization of $K_n^{\le k}$ (or more generally $\binom{[n]}{L}$ for $L \subseteq [k]$ with $k \in L$) to the existence of a non-negative integer solution of a linear system $A_L^T x = b_L$ indexed by admissible $(n,L)$-types $\lambda$ (partitions of $n$ with $\lambda_j$ parts of size $j$). Sufficiency is proven by a Baranyai-style Max-Flow Min-Cut / Integral Flow argument that inductively grows empty sets to size-$j$ blocks one element at a time. Necessity uses Farkas' Lemma — explicit separating hyperplanes $y$ are constructed (e.g. $y_i = \binom{j}{2}$ entries with $y_k = -1$) to certify infeasibility outside the stated congruence/size range.

## Result
Complete characterization (Theorems 1.2 & 1.3) of all $(n,k)$ with $K_n^{\le k}$ 1-factorable. Sharp thresholds: $n \ge k(k-2)$ for $n \equiv 0$, $n \ge k(\lceil k/2 \rceil - 1) - 1$ for $n \equiv -1$. Counterexample noted: $K_{18}^{\le 6}$ is *not* 1-factorable despite $18 \equiv 0 \pmod 6$. The flow reduction (Theorem 2.2) is stated for arbitrary $L \ni k$, giving a general LP-feasibility-equivalent characterization.

## Why it matters here
General background; no direct arena tie. The Farkas-Lemma-with-explicit-dual-certificate template (construct $y$, verify $A y \ge 0$ and $b^T y < 0$ via careful binomial-ratio bounds) is a transferable technique for proving infeasibility of LP relaxations in extremal-combinatorics-style packing/covering problems, which touches the agent's LP-bound toolkit (Cohn–Elkies, kissing-number LP).

## Open questions / connections
- Conjecture 4.4: classify $L \subseteq [k]$ with $k \in L$ into "needs $n \equiv 0 \pmod k$" vs "needs $n \equiv 0, -1 \pmod k$"; criterion when $k-1 \in L$ is open.
- Extend to multiset hypergraphs: for which $\{m_i\}$ is $\bigcup_{i=1}^n m_i \binom{[n]}{i}$ 1-factorable? (Bahmanian's symmetric-Latin-cube connection.)
- Connection to Chvátal's hereditary-family intersection conjecture via 1-factorability ⇒ $\chi(G_{\mathcal{F}}) = \max_x |\mathcal{F}_x|$, a strengthening of $\alpha(G_{\mathcal{F}}) = \max_x |\mathcal{F}_x|$.

## Key terms
Baranyai's theorem, 1-factorization, perfect matching decomposition, complete uniform hypergraph, non-uniform hypergraph, Farkas' lemma, Max-Flow Min-Cut, Integral Flow Theorem, partition types, LP feasibility, Chvátal conjecture, extremal hypergraph combinatorics
