---
type: source
kind: paper
title: Saturating Sperner Families
authors: Dániel Gerbner, Balázs Keszegh, N. Lemons, C. Palmer, Dömötör Pálvölgyi, Balázs Patkós
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1105.4453
source_local: ../raw/2011-gerbner-saturating-sperner-families.pdf
topic: general-knowledge
cites:
---

# Saturating Sperner Families

**Authors:** Dániel Gerbner, Balázs Keszegh, N. Lemons, C. Palmer, Dömötör Pálvölgyi, Balázs Patkós  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1105.4453

## One-line
Initiates the study of saturation for Sperner-type properties, asking for the minimum size of a family $\mathcal{F}\subseteq 2^{[n]}$ that is $k$-Sperner but cannot be extended.

## Key claim
For $k\ge 1$, $\mathrm{sat}(n,k)\le 2^{k-1}$ via a product construction independent of $n$; conjecturally tight for $n\ge n_0(k)$. They prove $2^{k/2-1}\le \mathrm{wsat}(n,k)\le \mathrm{sat}(n,k)$, $\mathrm{wsat}(n,k)=O(\log k\cdot 2^k/k)$, and a stability theorem for flat antichains in $\binom{[n]}{2}\cup\binom{[n]}{3}$: minimum size is $(3/8-o(1))n^2$ with the extremal family essentially unique (a complete bipartite "non-edge" set $K_{A\cup B,C}$ plus a matching $M$ between $A,B$).

## Method
Combinatorial constructions (product / level-wise general construction using covering codes $\mathcal{F}_l\subseteq\binom{[k]}{l}$ with prescribed shadow/shade), interval-covering lower bounds (each non-member sits in an interval $I_{F_i,F_{i+1}}$ of size $\le 2^{n-k+2}$). The stability proof uses Ruzsa–Szemerédi triangle removal plus the Erdős–Simonovits stability of triangle-free graphs; generalization to $(l,l+1)$-flat antichains uses the hypergraph removal lemma and the Turán density $t_l$ of $K_{l+1}^l$.

## Result
$\mathrm{sat}(k,k)\le \tfrac{15}{16}\cdot 2^{k-1}$ (via explicit $n=k=6$ construction giving 30, plus the doubling lemma $\mathrm{sat}(n,k)\le 2\,\mathrm{sat}(n-1,k-1)$). Lower bound $\mathrm{wsat}(k+c,k)\ge 2^{k+c}/(k+c)^{c+1}$. Flat antichain bound: $(1-\tfrac{l-1}{l}t_l-o(1))\binom{n}{l}\le \mathrm{sat}(n,l,l+1)\le (1-\tfrac12(1-1/l)^{l-1}+o(1))\binom{n}{l}$; for $l=2$ this is tight at $3n^2/8$ with full stability characterization.

## Why it matters here
General background; no direct arena tie — informs the extremal-set-theory / antichain side of the wiki (Sperner, LYM, shadow/shade machinery) and demonstrates a stability-via-removal-lemma argument template that could be reused for any arena problem cast as "saturation of a forbidden chain/configuration."

## Open questions / connections
- Conjecture: $\mathrm{sat}(n,k)=2^{k-1}$ for $n\ge n_0(k)$ — is the product construction tight?
- Is $\mathrm{wsat}(k,k)=\Theta(2^k/k)$? Equivalent to a covering-code existence question for $\mathcal{F}_l\subseteq\binom{[n]}{l}$ with $|\mathcal{F}_l|=O(\binom{n}{l}/k)$.
- Close the gap between upper and lower bounds for $\mathrm{sat}(n,l,l+1)$ with $l\ge 3$; find a lower bound that does not invoke the unknown Turán density $t_l$ (even $t_3$ is open, conjectured $5/9$, best upper bound $(3+\sqrt{17})/12$).

## Key terms
Sperner family, k-Sperner, saturation, weak saturation, antichain, flat antichain, shadow, shade, Ruzsa–Szemerédi, triangle removal lemma, Erdős–Simonovits stability, Turán density, hypergraph removal, covering codes, extremal set theory
