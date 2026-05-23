---
type: source
kind: paper
title: Stanley-Wilf limits are typically exponential
authors: J. Fox
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1310.8378
source_local: ../raw/2013-fox-stanley-wilf-limits-typically-exponential.pdf
topic: general-knowledge
cites:
---

# Stanley-Wilf limits are typically exponential

**Authors:** J. Fox  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1310.8378

## One-line
Disproves the long-standing conjecture that Stanley-Wilf limits $L(\pi)$ grow quadratically in pattern length $k$, showing they are typically exponential in $k$.

## Key claim
For each $k$, there exists a $k$-permutation $\pi$ with $L(\pi) = 2^{\Omega(k^{1/4})}$ (Theorem 1), and almost all $k$-permutations satisfy $L(\pi) = 2^{\Omega((k/\log k)^{1/4})}$ (Theorem 2). Matching upper bound: $L(\pi) = 2^{O(k)}$ and $c(\pi) = 2^{O(k)}$ (Theorem 3), improving Marcus–Tardos's $2^{O(k \log k)}$.

## Method
Introduces **interval minors** of matrices (analogue of graph minors using interval contraction instead of edge contraction) and constructs a dense random matrix from **random dyadic rectangles**: an $N \times N$ matrix where each entry is 1 iff all $(r+1)^2$ dyadic rectangles containing it are selected (each selected i.i.d. with prob $1-q$). A linearity-of-expectation argument bounds copies of $J_\ell$ in an auxiliary matrix $B$, forcing the constructed matrix to avoid $J_\ell$ as interval minor while keeping mass $\geq (1-q)^{(r+1)^2} N^2$. Upper bound uses a refined Marcus–Tardos block decomposition tracking "wide" and "tall" blocks with sharper pigeonhole on $f_{r,k}(t,s)$.

## Result
Lower bound: for $k \geq 3\ell^2 \ln \ell$ almost all $k$-permutations contain $J_\ell$ as interval minor (Lemma 5); combined with the dyadic construction (Theorem 6), this gives Füredi–Hajnal limit $c(\pi) = 2^{\Omega(k^{1/4})}$ (Corollary 8). Upper bound: $m(n, J_k) \leq 3k^2 8^k n$ (Theorem 13), giving $c(\pi) \leq 3k^2 8^k$ and via Cibulka's $L(\pi) = O(c(\pi)^2)$, the bound $L(\pi) = O(k^2 \cdot 2^{16k})$. Algorithmic corollary: permutation-containment runs in $2^{O(k^2)} n$ time, improving Guillemot–Marx's $2^{O(k^2 \log k)} n$.

## Why it matters here
General background; no direct arena tie. Provides methodology relevant to extremal combinatorics on ordered structures — random dyadic rectangle construction is a transferable technique for ordered/extremal problems, and the upper/lower bound interplay via super-additive limits parallels the Cohn–Elkies LP-bound program style used on packing problems.

## Open questions / connections
- Conjecture 1: if $\pi$ avoids some fixed $t$-permutation, is $L(\pi) = k^{O(1)}$? (would explain why layered patterns are easier to avoid).
- Tightening the $2^{\Omega(k^{1/4})}$ lower bound vs $2^{O(k)}$ upper bound gap on $L(\pi)$.
- Develop Robertson–Seymour-style structure theory for interval minors (matrices avoiding fixed $P$).
- Better estimates for $S_n(P)$ and $m(n,P)$ for general (non-permutation) matrices $P$.
- Minor Ramsey number $r(P) \leq k^2$ for $k\times k$ matrices — sharp value unknown.

## Key terms
Stanley-Wilf conjecture, Füredi-Hajnal conjecture, pattern avoidance, permutation matrices, interval minors, random dyadic rectangles, Marcus-Tardos theorem, layered permutations, extremal matrix theory, super-multiplicativity, Cibulka bound, Guillemot-Marx algorithm
