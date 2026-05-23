---
type: source
kind: paper
title: Strong Bounds for 3-Progressions
authors: Zander Kelley, Raghu Meka
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.05537
source_local: ../raw/2023-kelley-strong-bounds-3-progressions.pdf
topic: general-knowledge
cites:
---

# Strong Bounds for 3-Progressions

**Authors:** Zander Kelley, Raghu Meka  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.05537

## One-line
A near-Behrend-strength upper bound on the density of 3-AP-free subsets of $[N]$, achieved via new analytic "spreadness $\Rightarrow$ regularity" machinery in both $\mathbb{F}_q^n$ and $\mathbb{Z}$.

## Key claim
Any $A \subseteq [N]$ with $|A|/N \geq 2^{-\Omega(\log(N)^\beta)}$ for some absolute $\beta > 0$ contains a non-trivial 3-AP. Quantitatively, if $|A| \geq 2^{-d} N$ then the count of triples $(x,y,z) \in A^3$ with $x+y=2z$ is at least $2^{-O(d^{12})} N^2$ — a huge leap from the prior $N/\log(N)^{1+c}$ (Bloom–Sisask) frontier toward Behrend's lower bound $\delta \approx 2^{-\sqrt{\log N}}$.

## Method
Three-step density-increment via an analytic structure-vs-pseudorandomness dichotomy: (1) greedy density increment gives **spreadness** ($\|A\|_{\perp,r} \leq \gamma$ on affine subspaces); (2) a **sifting lemma** — a refinement of Schoen's Pre-BSG using degree-$k$ compressions $D^{\wedge k} \propto D^k$ on iterated intersections $A \cap (A+s_1) \cap \cdots \cap (A+s_{k-1})$ — combined with Sanders' invariance lemma (Croot–Sisask + Chang's inequality) upgrades spreadness to **regularity** ($\|A\|_{*,k} \leq \gamma$); (3) a **decoupling inequality** plus an odd-moments / positive-correlation argument gives strong two-sided bounds $\|A*B - 1\|_k \leq 2\varepsilon$ from self-regularity. The $\mathbb{F}_q^n$ case is developed first as a model, then transferred to $\mathbb{Z}$ with Bohr-set / GAP substitutes.

## Result
Theorem 1.1: 3-AP-free $A \subseteq [N] \Rightarrow \delta \leq 2^{-\Omega(\log(N)^\beta)}$. Theorem 1.3 ($\mathbb{F}_q^n$): triple count $\geq q^{-O(d^9)}|\mathbb{F}_q^n|^2$. Lemma 1.5 (structural): every dense $A \subseteq \mathbb{F}_q^n$ contains $A' \subseteq A$ of the same relative density with $|A' + A'| \geq (1-\tau)|\mathrm{Span}^*(A')|$ and $\mathrm{Codim}(\mathrm{Span}^*(A')) \leq O(d^5 \log(1/\tau)^4)$ — answers Hatami–Hosseini–Lovett's question on Approximate Bogolyubov for $2A$ and Schoen–Sisask's on Exact Bogolyubov for $3A$.

## Why it matters here
General background; no direct arena tie. Closest relevance is to combinatorics/additive-structure problems and to the analytic technique catalog (Croot–Sisask, Chang's inequality, BSG, sifting) — potentially useful framing if an arena problem reduces to bounding solution counts of linear equations in dense subsets of $\mathbb{F}_q^n$ or $\mathbb{Z}$.

## Open questions / connections
- Can the exponent $\beta$ be pushed to $1/2$, matching Behrend's lower bound?
- Does sifting + decoupling extend to longer progressions (4-APs, $k$-APs) where Gowers norms currently dominate?
- The Extended Pre-BSG Lemma (Lemma B.8) is conjectured to have independent applications — where, beyond 3-APs?
- Algebraic methods (Croot–Lev–Pach, Ellenberg–Gijswijt, slice-rank) give better $\mathbb{F}_q^n$ bounds ($q^{-O(d)}$) but don't transfer to $\mathbb{Z}$; this paper's analytic route is the bridge.

## Key terms
3-term arithmetic progression, Roth's theorem, Behrend construction, Bogolyubov–Ruzsa lemma, sifting lemma, Pre-BSG lemma, Balog–Szemerédi–Gowers, Croot–Sisask lemma, Chang's inequality, Sanders invariance lemma, spreadness, regularity, self-regularity, decoupling inequality, degree-$k$ compression, density increment, additive combinatorics, cap-set problem, Kelley–Meka
