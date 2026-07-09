---
type: source
kind: paper
title: Smallest graphs with given automorphism group
authors: Danai Deligeorgaki
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.10384
source_local: ../raw/2021-deligeorgaki-smallest-graphs-given-automorphism.pdf
topic: general-knowledge
cites:
---

# Smallest graphs with given automorphism group

**Authors:** Danai Deligeorgaki  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.10384

## One-line
Sharpens Babai's bound on the minimum number of vertices $\alpha(G)$ needed for a graph whose automorphism group is isomorphic to a given finite group $G$, identifying all exceptions.

## Key claim
For every finite group $G$ of order $n$, $\alpha(G) \le n$ except for four explicit infinite families (cyclic of order $p^k$, cyclic of order $2p$, generalised quaternion $Q_{2^r}$, and $Q_{2^r} \times C_2$) plus 17 small exceptional groups of order $\le 25$ — an improvement over Babai's prior bound $\alpha(G) \le 2|G|$.

## Method
Reduction to the GRR-Theorem (Godsil/Hetzel): if $G$ admits a graphical regular representation — a Cayley graph $\text{Cay}(G,S)$ with $\text{Aut} = G$ — then $\alpha(G) \le |G|$ automatically. The paper then case-analyses each GRR-exception: abelian groups use Arlinghaus's algorithm; for non-abelian exceptions, explicit graph constructions on $\le |G|$ vertices are built, and orbit/stabilizer arguments (Cauchy's theorem, faithfulness of action, swap-automorphism contradictions) establish matching lower bounds. GAP is used to verify automorphism groups of constructed examples.

## Result
Theorem 1 characterises $\alpha(G)$ vs $|G|$. Corollary: $\alpha(G) = 2|G|$ iff $G \in \{Q_{2^r}\ (r\ge 3),\ C_p\ (p\ge 7\ \text{prime}),\ C_3 \times C_3\}$. Computes previously-unknown values: $\alpha(\text{Dic}_3)=17$, $\alpha(\text{Dic}_5)=23$, $\alpha(\text{Dic}_6)=\alpha(Q_8\times C_3)=25$, $\alpha(A_4)=16$, $\alpha(G_{16})=\alpha(G'_{16})=18$, $\alpha(Q_{2^{r+1}} \times C_2) = 2^{r+2}+2$.

## Why it matters here
General background; no direct arena tie. The 23 Einstein Arena problems are continuous-geometry / packing / autocorrelation / extremal-graph optimisation; finite-group graph realisation is adjacent to extremal graph theory but does not bear on any current arena problem's evaluator or bound.

## Open questions / connections
- Extends a long chain (Frucht 1939 → Sabidussi → Babai → Arlinghaus → Graves–Lauderdale → Liebeck) of $\alpha(G)$ determinations for specific group families.
- $\alpha(G)$ for non-abelian groups outside the catalogued families remains computed only via construction-plus-lower-bound; no closed form.
- The GRR-Theorem exceptions list is the structural bottleneck — any future tightening of Babai's bound must address the same exceptional families.

## Key terms
automorphism group, Cayley graph, graphical regular representation, GRR, Babai bound, generalised quaternion group, dicyclic group, dihedral group, alternating group $A_4$, Frucht theorem, orbit-stabilizer, extremal graph theory, finite group realisation
