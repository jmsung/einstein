---
type: source
kind: paper
title: Subspace coverings with multiplicities
authors: Anurag Bishnoi, Simona Boyadzhiyska, Shagnik Das, Tam'as M'esz'aros
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2101.11947
source_local: ../raw/2021-bishnoi-subspace-coverings-multiplicities.pdf
topic: general-knowledge
cites:
---

# Subspace coverings with multiplicities

**Authors:** Anurag Bishnoi, Simona Boyadzhiyska, Shagnik Das, Tam'as M'esz'aros  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2101.11947

## One-line
Determines the minimum number $f(n,k,d)$ of codimension-$d$ affine subspaces over $\mathbb{F}_2^n$ needed to cover every nonzero point at least $k$ times while covering the origin fewer than $k$ times, extending Jamison's $k=1$ theorem to higher multiplicities.

## Key claim
For large multiplicity ($k \geq 2^{n-d-1}$), $f(n,k,d) = 2^d k - \lceil k / 2^{n-d} \rceil$; for large dimension ($n > 2^{2^d k - d - k + 1}$), $f(n,k,d) = n + 2^d k - d - 2$; in between, $n + 2^d k - d - \log_2(2k) \leq f(n,k,d) \leq n + 2^d k - d - 2$.

## Method
Avoids the polynomial method (Jamison/Alon–Füredi style) in favor of direct combinatorial and probabilistic arguments. Key tools: a double-counting lower bound; a recursive reduction from codimension-$d$ to hyperplane case via partitioning into translates; a probabilistic argument (random hyperplane through origin) showing $f(n,k,d)$ is strictly increasing in $n$; and a Hamming-bound argument exploiting an equivalence between $(k,1;0)$-covers and binary linear codes of minimum distance $k$.

## Result
Exhibits a *separation* between the hyperplane-covering problem and the polynomial-degree problem of Sauermann–Wigderson: for $k \geq 4$ and large $n$, $f(n,k,1) = n + 2k - 3$, strictly above the polynomial answer $\leq n + 2k - 4$ over $\mathbb{F}_2$. Provides exact tables of $f(n,k)$ for $3 \leq n \leq 12$, $3 \leq k \leq 10$, and uses the extended binary Golay code (length 24, dim 12, distance 8) to prove $f(12,8) = 24$, breaking the conjectured threshold $n_0(k) = k+1$.

## Why it matters here
General background for extremal combinatorics over $\mathbb{F}_2$ — covering, blocking sets, and the coding theory ↔ covering equivalence. No direct Einstein Arena problem tie, but the coding-theory bridge (covers ↔ minimum-distance codes) and the demonstration that polynomial-method bounds can be loose are methodologically relevant for any discrete-combinatorics arena problem where the polynomial method is tempting.

## Open questions / connections
- Determine $n_0(k)$ exactly: does $n_0(k) = k+1$ hold for all $k \geq 12$ (Question 4.3)?
- Extend to $\mathbb{F}_q$ for $q > 2$ — the code/cover equivalence breaks; new algebraic tools needed (Question 5.1).
- Sauermann–Wigderson polynomial Question 5.2 over $\mathbb{F}_2$ for $k \geq 2^{n-2}$: does $\deg(P) \geq 2k - \lceil k/2^{n-1} \rceil$?
- Connection to the Gilbert–Varshamov and Hamming bounds for binary linear codes.

## Key terms
affine subspace cover, blocking set, Jamison theorem, Alon-Füredi, polynomial method, Punctured Combinatorial Nullstellensatz, Sauermann-Wigderson, Clifton-Huang, extended Golay code, Hamming bound, Gilbert-Varshamov, minimum distance code, $\mathbb{F}_2^n$ hypercube cover, multiplicity covering
