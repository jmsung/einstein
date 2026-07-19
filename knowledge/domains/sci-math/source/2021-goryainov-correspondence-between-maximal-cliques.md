---
type: source
kind: paper
title: On a correspondence between maximal cliques in Paley graphs of square order
authors: S. Goryainov, A. Masley, L. Shalaginov
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.03822
source_local: ../raw/2021-goryainov-correspondence-between-maximal-cliques.pdf
topic: general-knowledge
cites:
---

# On a correspondence between maximal cliques in Paley graphs of square order

**Authors:** S. Goryainov, A. Masley, L. Shalaginov  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.03822

## One-line
Establishes an explicit linear-fractional (Möbius) bijection between two previously known families of maximal-but-not-maximum cliques of size $\frac{q+r(q)}{2}$ in the Paley graph $P(q^2)$.

## Key claim
The two known constructions of size-$\frac{q+r(q)}{2}$ maximal cliques in $P(q^2)$ — the Baker–Ebert–Hemmeter–Woldar $(\mathbb{F}_q,\alpha)$-pencil construction [1] and the Goryainov–Kabanov–Shalaginov–Valyuzhenich subgroup-of-norm-1 construction $Q_0$ [5] — are related by explicit involutive linear-fractional maps $\varphi(\gamma) = \frac{\gamma+1}{\gamma-1}$ and $\psi(\gamma) = \frac{\alpha\gamma+d}{\gamma-\alpha}$ on $\mathbb{F}_{q^2}$, where $r(q) := q \bmod 4$ and $d$ is a fixed non-square in $\mathbb{F}_q^*$.

## Method
View $\mathbb{F}_{q^2}$ as the affine plane $AG(2,q)$ with $\alpha$ a root of $t^2-d$; then $Q = \mathrm{Ker}(N)$ (norm-1 subgroup, an oval of size $q+1$) splits as $Q_0 \cup Q_1$ by squares vs non-squares. The proof computes $\varphi$ on a square $\gamma^2 = (x+y\alpha)^2 \in Q_0$ using $x^2-y^2 d = 1$ to get $\varphi(\gamma^2) = \frac{x}{yd}\alpha \in \alpha\mathbb{F}_q$, then checks the norm $N(1 - \frac{x}{yd}\alpha) = -\frac{1}{y^2 d}$ to determine adjacency via Proposition 2 ($-1$ is a square iff $q\equiv 1 \pmod 4$).

## Result
Theorem 1: $\varphi(Q_0) = \{1, c_1\alpha,\dots,c_{(q-1)/2}\alpha\}$ when $q\equiv 1\pmod 4$ (maximal independent set of size $\frac{q+1}{2}$); $\varphi(Q_0\cup\{0\})$ is the corresponding maximal clique of size $\frac{q+3}{2}$ when $q\equiv 3\pmod 4$. Theorem 2: the conjugate map $\psi$ sends $\alpha Q_0$ to the $(\mathbb{F}_q,\alpha)$-construction's clique. Worked examples are given for $q=29$ (where $r(q)=1$, size 15) and $q=31$ (where $r(q)=3$, size 17).

## Why it matters here
General background; no direct arena tie. Closest relevance is to extremal-combinatorics / strongly-regular-graph problems via the Delsarte clique bound $|C| \le 1 + k/m$, which is the LP-bound mechanism reused in Cohn–Elkies-style sphere-packing dualities.

## Open questions / connections
- Problem 3 (open): are there maximal cliques in $P(q^2)$ of size strictly between $\frac{q+r(q)}{2}$ and $q$? Computer search shows only the two known families for $25 \le q \le 83$, but extras exist for $9 \le q \le 23$.
- Problem 2 (open): characterize eigenfunctions of $P(q^2)$ of minimum support — these are tied to maximal cliques of size $\frac{q+1}{2}$ via the complete-bipartite structure of [Krotov–Mogilnykh–Potapov, Thm 3].
- Hirschfeld–Szőnyi [6, Thm 5.2] implicitly constructs maximal cliques of size $\sim 2qm$ for any $m\ge 0$ — the $m=1$ case is the one studied here; higher $m$ unexplored.

## Key terms
Paley graph, maximal clique, linear fractional transformation, Möbius involution, strongly regular graph, Delsarte clique bound, affine plane $AG(2,q)$, oval, quadratic line, norm map kernel, finite field $\mathbb{F}_{q^2}$, eigenfunction minimum support
