---
type: source
kind: paper
title: Existence of Regular Nut Graphs for Degree at Most 11
authors: P. Fowler, J. B. Gauci, J. Goedgebeur, T. Pisanski, Irene Sciriha
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1908.11635
source_local: ../raw/2019-fowler-existence-regular-nut-graphs.pdf
topic: general-knowledge
cites:
---

# Existence of Regular Nut Graphs for Degree at Most 11

**Authors:** P. Fowler, J. B. Gauci, J. Goedgebeur, T. Pisanski, Irene Sciriha  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1908.11635

## One-line
Determines, for every degree $d \le 11$, the exact set of orders $n$ for which a $d$-regular nut graph (singular graph with 1-dimensional kernel whose eigenvector has no zero entries) exists.

## Key claim
$N(d)$ — the set of orders admitting a $d$-regular nut graph — is computed exactly for $d = 5, \ldots, 11$: $N(5)=\{2k:k\ge 5\}$, $N(6)=\{k:k\ge 12\}$, $N(7)=\{2k:k\ge 6\}$, $N(8)=\{12\}\cup\{k:k\ge 14\}$, $N(9)=\{2k:k\ge 8\}$, $N(10)=\{k:k\ge 15\}$, $N(11)=\{2k:k\ge 8\}$. Smallest regular nut graph has order 8 (4-regular).

## Method
Two-pronged: (i) Meringer's `genreg` generator enumerates all $d$-regular graphs of small order, filtered by a nullity-1 / no-zero-entry test, establishing both non-existence at small $n$ and explicit seed graphs at $2d$ consecutive (even-only for odd $d$) orders. (ii) The **Fowler construction** $F(G,v)$ extends any $d$-regular nut graph of order $n$ to one of order $n+2d$ by inserting two layers spanning $K_{d,d}$ minus a perfect matching, with eigenvector entries $q_i=u_i$, $p_i=x_v$, and $v$'s entry replaced by $(1-d)x_v$ — preserving nullity 1 and regularity. Iterating gives all orders $\ge n$ in the appropriate residue class mod $2d$.

## Result
For each $d\in\{5,\ldots,11\}$ a complete characterization of $N(d)$, plus exact counts of all $d$-regular nut graphs at small orders (e.g. 9 cubic nut graphs of order 12; 665,456,900 5-regular nut graphs of order 18; zero 8/9/10/11-regular nut graphs of order 14). Theorem 5 gives necessary conditions for **vertex-transitive** nut graphs: degree $d$ must be even, and if $d\equiv 2\pmod 4$ then $n\equiv 0\pmod 4$ and $n\ge d+6$; if $d\equiv 0\pmod 4$ then $n\ge d+4$. Proof uses that the kernel eigenvector transforms as a 1-d real irrep so entries are $\pm 1$, forcing local-sum-zero (even degree) and global-sum-zero (even $n$).

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are about graph nullity / nut graphs; the constructive lifting trick ($n \mapsto n+2d$ via local extension preserving an eigenvector property) is a transferable pattern for extremal-graph existence proofs but does not bear on sphere packing, autocorrelation, or kissing-number objectives.

## Open questions / connections
- Question 2/3: Is every valence $d>2$ "normal" — i.e. is $A(d)\setminus N(d)$ finite for all $d$?
- Question 5: Realizability of vertex-transitive nut graphs for $(n,d)$ satisfying Theorem 5's necessary conditions (open cells "?" remain in Figure 2 for $n\le 30$).
- Question 6/7: Constrain by girth $g$ (set $N(p,g)$) or by simultaneous $q$-regularity for all $3\le q\le p$ (set $N(p)$).
- Extends Gauci–Pisanski–Sciriha (arXiv:1904.02229) which handled $d\le 4$.

## Key terms
nut graph, singular graph, nullity, kernel eigenvector, regular graph, vertex-transitive graph, Fowler construction, seed graph, cocktail-party graph, Hückel molecular orbital, omni-conductor, Meringer genreg, House of Graphs, Sciriha
