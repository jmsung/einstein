---
type: source
kind: paper
title: Refined Turán numbers and Ramsey numbers for the loose 3-uniform path of length three
authors: J. Polcyn, A. Rucinski
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1510.06057
source_local: ../raw/2015-polcyn-refined-tur-numbers-ramsey.pdf
topic: general-knowledge
cites:
---

# Refined Turán numbers and Ramsey numbers for the loose 3-uniform path of length three

**Authors:** J. Polcyn, A. Rucinski  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1510.06057

## One-line
Computes the third- and fourth-order Turán numbers for the loose 3-uniform path $P$ of length 3 and uses them to extend the multicolor Ramsey identity $R(P;r)=r+6$ to $r\in\{8,9\}$.

## Key claim
For all $n\ge 7$, $\mathrm{ex}^{(3)}(n;P)$ is determined exactly (piecewise formula, e.g. $\binom{n-2}{2}+5$ for $n\ge 15$ with unique extremal $K_4\cup S_{n-4}$), and consequently $R(P;r)=r+6$ holds for $r\le 9$.

## Method
Higher-order Turán analysis: define $\mathrm{ex}^{(s+1)}(n;F)$ as the max edge count among $F$-free 3-graphs not contained in any lower-order extremal graph, then split candidates by whether they contain a matching $M$ or triangle $C$, using conditional Turán numbers $\mathrm{ex}(n;\{P,C\}\mid M)$. The Ramsey extension is a pigeonhole-plus-induction argument: a majority color class must be a star or sub-comet, whose center is peeled off to reduce to a smaller proven case (Lemma 4: $K_n-2e\to(P;n-6)$ for $9\le n\le 13$).

## Result
Piecewise formula for $\mathrm{ex}^{(3)}(n;P)$: $3n-8$ ($7\le n\le 10$), $25$ ($n=11$), $32$ ($n=12$), $20+\binom{n-2}{7}$-type ($n=13,14$), $4+\binom{n-2}{5}$-type for $n\ge 15$; extremal families are $G_1(n),G_2(n)$, the comet $Co(n)$, $K_6\cup S_{n-6}$, or $K_4\cup S_{n-4}$ depending on range. Theorem 10 gives the full fourth-order list, with the "rocket" $Ro(n)$ extremal for $n\ge 16$. Theorem 2: $R(P;r)=r+6$ for all $r\le 9$.

## Why it matters here
General background; no direct arena tie — hypergraph extremal/Ramsey for the specific loose 3-path doesn't map onto the current Einstein Arena problem inventory (sphere packing, autocorrelation, kissing, Sidon-type). The higher-order Turán *technique* (peeling off lower-order extremal structures to expose secondary maxima) is a transferable idea for extremal-combinatorics problems if any appear.

## Open questions / connections
- Higher-order numbers $\mathrm{ex}^{(s)}(n;P)$ for $s\ge 5$ and small $n$ — needed to push $R(P;r)=r+6$ past $r=9$ (authors note 4th-order is "not good enough").
- Extends prior work: Gyárfás–Raeisi ($r=2$), Jackowska ($r=3$), Jackowska–Polcyn–Ruciński ($r=4,\dots,7$); leaves $r\ge 10$ open.
- Connects to Erdős–Ko–Rado ($\mathrm{ex}^{(1)}(n;M)$), Hilton–Milner (2nd-order matching), Han–Kohayakawa (3rd-order matching), Frankl–Füredi (triangle Turán) — same toolkit of layered extremal families.

## Key terms
Turán number, Ramsey number, loose 3-uniform path, 3-graph, hypergraph, higher-order extremal, conditional Turán number, comet, full star, Erdős-Ko-Rado, Hilton-Milner, Frankl-Füredi, extremal combinatorics
