---
type: source
kind: paper
title: The Frobenius postage stamp problem, and beyond
authors: Andrew Granville, G. Shakan
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.04076
source_local: ../raw/2020-granville-frobenius-postage-stamp-problem.pdf
topic: general-knowledge
cites:
---

# The Frobenius postage stamp problem, and beyond

**Authors:** Andrew Granville, G. Shakan  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.04076

## One-line
Precisely characterizes the $N$-fold sumset $NA$ of a finite integer/lattice set $A$ for sufficiently large $N$, generalizing the classical Frobenius "postage stamp" problem to multi-dimensional sets with explicit bounds.

## Key claim
For $A \subset \mathbb{Z}$ with $0 = \min A$, $b = \max A$, $\gcd(A) = 1$: if $N \geq 2\lceil b/2 \rceil$, then $NA = \{0, \ldots, bN\} \setminus (E(A) \cup (bN - E(b - A)))$, where $E(A)$ is the (finite) exceptional set. Extends to $A \subset \mathbb{Z}^n$ (Theorem 2) where $E(A)$ has $O(N^{n-1})$ points and decomposes as a finite union of translates of cones over $\leq n-1$ linearly independent vectors from $A$ (Theorem 3).

## Method
Combinatorial / additive-combinatorics arguments. The 1D proof uses the Savchev–Chen structure theorem on long minimal zero-sum sequences in $\mathbb{Z}/b\mathbb{Z}$ plus Kneser's theorem on sumset growth. The higher-dimensional proof leans on Carathéodory's theorem (every $v \in NH(A)$ lies in $NH(B)$ for some $(n+1)$-subset $B \subset A$) and Mann's lemma (finite generating set under coordinatewise $\leq$ in $\mathbb{Z}_{\geq 0}^n$), yielding a finite "deficiency" set $A^+$ with $P(A) = A^+ + P(B)$.

## Result
1D bound $N \geq 2\lceil b/2 \rceil$ improves Nathanson 1972 ($N \geq b^2(\#A-1)$) and [WCC11] ($N \geq \sum_{a \neq 0}(a-1)$); conjectured optimum is $N \geq b - 2$ (or $b + 2 - \#A$ when $\#A \geq 4$), tight on $A = \{0, 1, b-1, b\}$. Higher-dim Theorem 2 establishes the equality $NA = (NH(A) \cap \mathbb{Z}^n) \setminus E_N(A)$ for some unspecified threshold $N_A$; combined with Theorem 3 it reproves Khovanskii's polynomial-growth result $|NA| = \mathrm{poly}_n(N)$ via elementary means.

## Why it matters here
General background; no direct arena tie. Closest relevance is to discrete combinatorics / sumset-growth problems and integer-point counting in convex hulls — could inform Sidon-set or extremal-set problems where one needs the structure of $NA$ at large $N$, or sumset-volume estimates in lattice geometry.

## Open questions / connections
- Sharp threshold conjecture: can the 1D bound be pushed to $N \geq b - 2$ (best possible for $A = \{0, 1, b-1, b\}$)?
- Explicit bound for $N_A$ in higher dimensions in terms of the geometry of $H(A)$ — left open.
- Connection to Khovanskii (1992) and Nathanson–Ruzsa (2002) polynomial-growth theorems for sumsets; this paper provides an alternative elementary derivation.

## Key terms
Frobenius number, postage stamp problem, sumsets, $N$-fold sumset, exceptional set, Khovanskii theorem, Savchev–Chen structure theorem, minimal zero-sum sequence, Carathéodory theorem, Mann's lemma, Kneser theorem, additive combinatorics, lattice points, convex hull, integer cone
