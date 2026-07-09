---
type: source
kind: paper
title: Quasirandomness in hypergraphs
authors: Elad Aigner-Horev, D. Conlon, Hiêp Hàn, Y. Person, M. Schacht
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.04750
source_local: ../raw/2017-aignerhorev-quasirandomness-hypergraphs.pdf
topic: general-knowledge
cites:
---

# Quasirandomness in hypergraphs

**Authors:** Elad Aigner-Horev, D. Conlon, Hiêp Hàn, Y. Person, M. Schacht  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.04750

## One-line
Gives short purely combinatorial proofs that Towsner's hierarchy of hypergraph quasirandomness notions (discrepancy, weighted discrepancy, subgraph counting, octahedral deviation) are equivalent for every antichain $Q \subseteq \mathcal{P}([k])$.

## Key claim
For every $k \geq 2$, every set system $Q \subseteq \mathcal{P}([k]) \setminus \{[k]\}$, and every $d \in [0,1]$, the four properties $\mathrm{DISC}_{Q,d}$, $\mathrm{WDISC}_{Q,d}$, $\mathrm{CL}_{Q,d}$, and $\mathrm{DEV}_{Q,d}$ are asymptotically equivalent (Theorem 2.8), and these notions are strictly distinct across different $Q$ (Proposition 2.11).

## Method
Proves the cycle $\mathrm{DISC} \Rightarrow \mathrm{WDISC} \Rightarrow \mathrm{CL} \Rightarrow \mathrm{DEV} \Rightarrow \mathrm{WDISC} \Rightarrow \mathrm{DISC}$ by combinatorial arguments only: a Gowers-style averaging/random-extension trick for $\mathrm{DISC}\Rightarrow\mathrm{WDISC}$; telescoping a product $\prod_f(1_E(\phi(f))-d+d)$ over $Q$-simple $F$ for the counting step; inclusion–exclusion for $\mathrm{CL}\Rightarrow\mathrm{DEV}$; and an iterated Cauchy–Schwarz "doubling" $\mathrm{db}_Q$ that builds the minimiser $M_Q$ for $\mathrm{DEV}\Rightarrow\mathrm{WDISC}$. The separation construction uses random $i$-set systems $B \subseteq \binom{V}{i}$ with $H^{(k)}(B)$ defined by parity, analysed via Chernoff and Chebyshev.

## Result
Establishes a unified, finitary equivalence theorem subsuming Chung–Graham (octahedron, $Q = \binom{[k]}{k-1}$), Kohayakawa–Rödl–Skokan (general $p$), and Conlon–Hàn–Person–Schacht (linear/weak, $Q = \binom{[k]}{1}$), with explicit minimiser hypergraphs $M_Q$ of $2^{|Q|}$ edges and $\sum_{i=1}^k 2^{|Q|-\deg_Q(i)}$ vertices. Proposition 2.11 produces, for any $U \subsetneq Q \subseteq \binom{[k]}{i}$, a sequence satisfying $\mathrm{DISC}_{U,1/2}(\epsilon)$ but failing $\mathrm{DISC}_{Q,1/2}(\delta)$ with $\delta = 2^{-|Q|-3}$.

## Why it matters here
General background for extremal-combinatorics problems on the arena where uniform-distribution-style assumptions on hypergraphs are needed (e.g. Turán-type and Sidon/autocorrelation problems lifted to $k$-uniform structures); supplies the catalogue of equivalent quasirandom characterisations and the canonical minimiser $M_Q$ which generalises $C_4$. No direct tie to a current arena problem beyond background.

## Open questions / connections
- Closing the omitted technical step $\mathrm{MIN}_{Q,d} \Rightarrow \mathrm{CL}_{Q,d}$ combinatorially.
- Extending the separation construction (Prop 2.11) beyond $p=1/2$ and beyond antichains in a single level $\binom{[k]}{i}$.
- Spectral/eigenvalue analogues à la Lenz–Mubayi for the full antichain poset and connections to hypergraph norms (Conlon–Lee, [11, Lemma 5.8]).

## Key terms
quasirandomness, hypergraph, discrepancy, octahedron, $C_4$ counting, Chung–Graham–Wilson, Towsner, $Q$-simple hypergraph, doubling operation, Cauchy–Schwarz, weak regularity lemma, linear hypergraph, Gowers
