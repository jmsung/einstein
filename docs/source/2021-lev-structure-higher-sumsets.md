---
type: source
kind: paper
title: The structure of higher sumsets
authors: V. Lev
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2110.03554
source_local: ../raw/2021-lev-structure-higher-sumsets.pdf
topic: general-knowledge
cites:
---

# The structure of higher sumsets

**Authors:** V. Lev  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2110.03554

## One-line
For a normalized finite integer set $A$ with $\min(A)=0$, $\gcd(A)=1$, $|A|=n$, $\max(A)=l$, the $m$-fold sumset $mA$ has an explicit "head + long interval + shifted tail" structure as soon as $m \geq l-n+2$, and the separating interval is provably long.

## Key claim
**Theorem 3:** For all $m \geq M := l-n+2$, $mA = [0, ml] \setminus (E \cup (ml - E'))$ where $E, E'$ are the Frobenius exceptional sets of $A$ and $l-A$. Moreover $E$ and $ml-E'$ are disjoint, separated by an interval of length $\geq (m-M+1)l + \Delta$ with $\Delta = l(k-1)(n-3) + rk(n-3) + r^2 + k + 1 \geq 2$, where $l-1 = k(n-2)+r$, $r \in [0,n-3]$. **Theorem 4:** For $n \geq 6$ and $m \geq \max(l - \tfrac{3}{2}n + \tfrac{9}{2},\, \tfrac{2}{3}(l-n+2))$, the same decomposition holds unless $A$ is essentially a dense subset of $\{0,1\} \cup [m+2, l]$ or its mirror.

## Method
Combines Nathanson's 1972 head/tail structure theorem with Granville–Walker's 2021 tight bound, giving a shorter unified proof. Core technique: reduce $A$ modulo $l$; use the zero-sum-free property of the residue sequence in $\mathbb{Z}/l\mathbb{Z}$; apply Olson's addition theorem (and corollaries), Scherk's theorem, Freiman's $(3n-3)$-theorem, and the Savchev–Chen / Yuan structure theorem for long zero-sum-free sequences in cyclic groups. Stability (Theorem 4) splits into cases $g < l$, $l < g < 2l$, $g > 2l$, using box-principle counting plus subset-sum structure (Lev's earlier theorems on small-subsum-set sequences).

## Result
Sharp lower bound $(m-M+1)l + \Delta$ on the gap between $\max(E)$ and $\min(ml-E')$ is best possible — attained by $A = \{0,d,2d,\ldots,l\} \cup \{l-1\}$ with $d \mid l$, and more generally by $\{0,d,\ldots,sd\} \cup \{sd-1-td,\ldots,sd-1\}$. Theorem 4 fully classifies the "extremal" sets requiring $m$ near $l-n+2$: they are dense subsets ($> 2/3$ density) of $\{0,1\} \cup [m+2,l]$ or its reflection.

## Why it matters here
General background; no direct arena tie. Closest relevance is to additive-combinatorics infrastructure that could surface in Sidon-set / B_h-set problems (autocorrelation, extremal sequences) — sumset growth, zero-sum-free sequences, and Frobenius-style structure are dual to the additive-energy / Sidon side. No current arena problem is framed as a Frobenius / postage-stamp problem.

## Open questions / connections
- Extends Granville–Walker (2021) tight structure theorem by quantifying the interval length and characterizing extremal sets — opens the question of full classification for $m \geq l - n - C$ as $C$ grows.
- Generalization to higher dimensions / sumsets in $\mathbb{Z}^d$ left open.
- The Frobenius number for $|A| \geq 4$ remains without a closed form; structural results like this are the partial substitute.

## Key terms
sumset structure, Frobenius problem, exceptional set, Nathanson theorem, Granville-Walker, zero-sum-free sequence, Olson addition theorem, Freiman 3n-3 theorem, Savchev-Chen, Scherk theorem, Dixmier, additive combinatorics, cyclic group, subset sums, postage stamp problem
