---
type: source
kind: paper
title: Two families of circulant nut graphs
authors: Ivan Damnjanovi'c
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2210.08334
source_local: ../raw/2022-damnjanovic-two-families-circulant-nut.pdf
topic: general-knowledge
cites:
---

# Two families of circulant nut graphs

**Authors:** Ivan Damnjanovi'c  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2210.08334

## One-line
Constructs two explicit families of $4t$-regular circulant nut graphs and proves they are nut graphs by showing their associated lacunary polynomials have no non-trivial $n$-th roots of unity, fully resolving the $4t$-regular circulant nut graph order–degree existence problem for odd $t$.

## Key claim
For every odd $t \in \mathbb{N}$ and every even $n \geq 4t+4$, a $4t$-regular circulant nut graph of order $n$ exists (Theorem 6); additionally, for every $t \in \mathbb{N}$ and every $n \equiv_4 2$ with $n \geq 4t+6$, such a graph exists (Theorem 12). Concrete generator sets $S'_{t,n}$ and $S''_{t,n}$ are given explicitly.

## Method
Reduces "nut graph" to a spectral condition via Damnjanović–Stevanović's lemma: $\mathrm{Circ}(n,S)$ is a nut graph iff $n$ even, $|S|$ has equal odd/even split, and $P(\omega^j) \ne 0$ for all $j = 1,\ldots,n/2-1$ (where $\omega = e^{2\pi i/n}$). Then proves the polynomial $P(x)$ shares no root with any cyclotomic $\Phi_b(x)$ (except $\Phi_1,\Phi_2$) by combining the Filaseta–Schinzel theorem on lacunary divisibility (bounded nonzero terms force only small prime factors of $b$) with explicit case analysis modulo $b \in \{3,5,6,10,15,30\}$ via large tabulated residue tables.

## Result
Two families: $D'_{t,n} = \mathrm{Circ}(n, \{1,\ldots,t-1\} \cup \{n/4, n/4+1\} \cup \{n/2-(t-1),\ldots,n/2-1\})$ for odd $t$, $4 \mid n$, $n \geq 4t+4$; and $D''_{t,n}$ with $\{(n+2)/4, (n+6)/4\}$ for $n \equiv_4 2$, $n \geq 4t+6$. Both are proved to be $4t$-regular nut graphs. The odd-$t$ case is fully resolved; for even $t$, only the $n \equiv_4 2$ subcase is covered, leaving $4 \mid n$ open (Conjecture 19: such graphs exist for all even $t \geq 4$ and $4 \mid n \geq 4t+8$).

## Why it matters here
General background; no direct arena tie. Circulant nut graphs and the cyclotomic/lacunary-polynomial machinery do not match any of the 23 Einstein Arena problems (sphere packing, autocorrelation, kissing, sieve, extremal graph, etc.); the techniques are spectral graph theory + algebraic number theory rather than continuous optimization or LP/SDP bounds.

## Open questions / connections
- Conjecture 19: existence of $4t$-regular circulant nut graphs of order $n$ for even $t \geq 4$ and $4 \mid n \geq 4t+8$ — left open.
- The $t=2$ case has a documented irregularity (no 8-regular circulant nut graph of order 16); generalizations of this anomaly across small even $t$ remain unclassified.
- Extends Damnjanović–Stevanović (2022, Linear Algebra Appl.) and Bašić et al. (2021); resolves the original Bašić et al. Conjecture 2 for odd $t$.

## Key terms
circulant graph, nut graph, graph spectrum, cyclotomic polynomial, lacunary polynomial, Filaseta–Schinzel theorem, nullity one, generator set, primitive root of unity, Euler totient, algebraic graph theory, Damnjanović–Stevanović
