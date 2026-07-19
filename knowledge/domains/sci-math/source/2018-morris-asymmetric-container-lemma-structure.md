---
type: source
kind: paper
title: An asymmetric container lemma and the structure of graphs with no induced $4$-cycle
authors: R. Morris, Wojciech Samotij, D. Saxton
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1806.03706
source_local: ../raw/2018-morris-asymmetric-container-lemma-structure.pdf
topic: general-knowledge
cites:
---

# An asymmetric container lemma and the structure of graphs with no induced $4$-cycle

**Authors:** R. Morris, Wojciech Samotij, D. Saxton  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1806.03706

## One-line
Introduces an asymmetric refinement of the hypergraph container method that distinguishes edges from non-edges, and uses it to pin down the typical structure of sparse graphs with no induced $C_4$.

## Key claim
For $n^{4/3}(\log n)^4 \le m \ll n^2$, almost every $n$-vertex graph with $m$ edges and no induced $C_4$ is $\varepsilon$-close to a split graph (vertex set partitions into an almost-independent set with $o(m)$ edges and an almost-clique of density $1-o(1)$); below $n^{4/3}$ a typical such graph is $\varepsilon$-quasirandom, exhibiting two phase transitions at $p = n^{-2/3+o(1)}$ and $p = n^{-1/3+o(1)}$ for $G^{\text{ind}}_{n,p}(C_4)$.

## Method
Generalises the Balogh–Morris–Samotij / Saxton–Thomason container method to $(k_0,k_1)$-uniform hypergraphs whose "edges" are pairs $(A_0,A_1)$ of disjoint sets — a function $h\in\{0,1\}^V$ is forbidden if it is $0$ on $A_0$ and $1$ on $A_1$. The asymmetric container lemma (Thm 1.4) builds containers tailored to $|h^{-1}(1)|=m$, trading off degree assumptions $\Delta^{(\ell_0,\ell_1)}$ against a parameter $r\ll m$ so that the two "directions" ($0$-forcing on $\delta v(H)$ vertices vs $1$-forcing on $\delta r$ vertices) are balanced by volume. Combined with a new robust balanced-stability theorem for pregraphs (partial 2-colourings) characterising those with few "good" induced $C_4$s.

## Result
The main structural dichotomy (Theorem 1.2) gives three regimes: (a) $n\ll m \lesssim \delta n^{4/3}$ — a.a.s. $\varepsilon$-quasirandom; (b) $n\ll m \le \delta n^{4/3}(\log n)^{1/3}$ — a.a.s. *not* $1/4$-close to split; (c) $n^{4/3}(\log n)^4 \le m \le \delta n^2$ — a.a.s. $\varepsilon$-close to split. Corollary 1.3: $e(G^{\text{ind}}_{n,p}(C_4))$ is $(1+o(1))p\binom{n}{2}$ for $p\ll n^{-2/3}$, stays at $n^{4/3}(\log n)^{O(1)}$ on the "long flat segment" $n^{-2/3}\lesssim p\lesssim n^{-1/3}(\log n)^4$, then jumps to $\Theta(p^2 n^2/\log(1/p))$. Theorem 1.5 sharpens the symmetric container theorem with an $r$-trade-off.

## Why it matters here
General background; no direct arena tie — the arena problems are continuous-optimisation / packing / autocorrelation, not induced-subgraph enumeration. The asymmetric container idea (separately budgeting "forcing 0" and "forcing 1" sides) is a methodological pointer for any future combinatorial problem where the constraint structure is naturally two-sided (e.g. constraint-satisfaction-style counting), but is not load-bearing for current problems P1–P23.

## Open questions / connections
- Conjecture 6.1: for $n^{4/3}(\log n)^{1/3} \ll m \le n^2-\Omega(n^2)$, a typical induced-$C_4$-free graph is *exactly* a split graph (not just $\varepsilon$-close); $\log n$ exponent should drop from $4$ to $1/3$.
- Extends Promel–Steger (1991) on induced-$C_4$-free graphs and Luczak (2000) on sparse triangle-free graphs; complements Balogh–Morris–Samotij–Warnke on sparse $K_{r+1}$-free graphs.
- The "long flat segment" of $e(G^{\text{ind}}_{n,p}(H))$ on $p\in [n^{-2/3+o(1)},n^{-1/3+o(1)}]$ mirrors random Turán phenomena for even cycles and $K_{s,t}$ — does it appear for every bipartite $H$?
- Theorem 6.2 (Kalvari–Samotij, in prep) generalises (a)/(b) to all non-bipartite $H$ via the same asymmetric lemma; the analogous precise structural statement for general hereditary properties remains open.

## Key terms
hypergraph container method, asymmetric container lemma, induced-$C_4$-free graphs, split graphs, hereditary graph properties, quasirandom graphs, 2-density $m_2(H)$, phase transition, Erdős–Kleitman–Rothschild, Prömel–Steger, Balogh–Morris–Samotij, Saxton–Thomason, random Turán problem, monotone graph property
