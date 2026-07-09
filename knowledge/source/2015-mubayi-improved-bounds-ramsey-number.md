---
type: source
kind: paper
title: Improved Bounds for the Ramsey Number of Tight Cycles Versus Cliques
authors: D. Mubayi
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.09104
source_local: ../raw/2015-mubayi-improved-bounds-ramsey-number.pdf
topic: general-knowledge
cites:
---

# Improved Bounds for the Ramsey Number of Tight Cycles Versus Cliques

**Authors:** D. Mubayi  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1511.09104

## One-line
Proves a near-tight upper bound $r(C_s^3, K_n^3) < 2^{cn\log n}$ for the 3-uniform hypergraph Ramsey number of tight cycles versus cliques, for $s \not\equiv 0 \pmod 3$ with $s \geq 16$ or $s \in \{8,11,14\}$.

## Key claim
For every $s \not\equiv 0 \pmod 3$ with $s \geq 16$ or $s \in \{8,11,14\}$, there exists $c_s > 0$ such that $r(C_s^3, K_n^3) < 2^{c_s n \log n}$. This answers strongly a question of Mubayi–Rödl asking for $r(C_s^3, K_n^3) < 2^{n^{1+\epsilon_s}}$ with $\epsilon_s \to 0$; matches the known $2^{c_1 n}$ lower bound up to a $\log n$ factor in the exponent.

## Method
Three-component proof: (i) supersaturation/blowup machinery — Theorem 2.1 of Mubayi–Rödl extended to *families* of 3-graphs via pigeonhole, so $r(\mathcal{F}(p), K_n^3) < r(\mathcal{F}, K_n^3)^c$; (ii) a strengthened Erdős–Hajnal argument using Spencer's Turán-type bound for 3-graphs ($\alpha(H) \geq (2/3) N/D^{1/2}$) plus induction on $n$ to show $r(\{K_4^3, H_5, H_6\}, K_n^3) < 2^{cn\log n}$, where $H_5, H_6$ are specific small 3-graphs on 5 and 6 vertices; (iii) explicit homomorphisms exhibiting $C_8^3 \subset H_6(2)$, $C_{s+3}^3 \subset C_s^3(2)$, and $C_{2s}^3 \subset C_s^3(2)$ to bootstrap from $C_8^3$ to all admissible $s$.

## Result
$r(C_s^3, K_n^3) < 2^{cn\log n}$ for $s \not\equiv 0 \pmod 3$, $s \geq 16$ or $s \in \{8,11,14\}$. Intermediate: $r(\{K_4^3, H_5, H_6\}, K_n^3) < 2^{cn\log n}$ via induction with threshold $N \geq 4^n (n!)^2$; consequently $r(H_6, K_n^3) < 2^{cn\log n}$ since $H_6 \subset K_4^3(2)$. Cases $s \in \{4,5,7,10,13\}$ remain open.

## Why it matters here
General background for extremal combinatorics / Ramsey-type bounds; no direct Einstein Arena problem tie, but the *blowup-amplification + family supersaturation* trick (proving a result for a family then transferring to a single target via embedding into a blowup) is a transferable methodological pattern relevant to extremal-graph and discrete-geometry problems in the arena where direct attacks fail but the target embeds into a blowup of a tractable structure.

## Open questions / connections
- Small cases $s \in \{4,5,7,10,13\}$ of $r(C_s^3, K_n^3)$ remain open — is the $2^{cn\log n}$ upper bound achievable there?
- Tightening the $\log n$ gap between $2^{c_1 n}$ lower bound and $2^{cn\log n}$ upper bound; for $r(K_4^3 \setminus e, K_n^3)$ the same gap persists (Conlon–Fox–Sudakov 2010).
- Extends Mubayi–Rödl [9] (BLMS) and the Erdős–Hajnal [5] foundational $r(K_4^3 \setminus e, K_n^3)$ bound; relates to the broader open question of determining $\log r(F, K_n^3)$ for any non-3-partite $F$.

## Key terms
hypergraph Ramsey number, tight cycle, 3-uniform hypergraph, blowup, supersaturation, Erdős–Hajnal, Mubayi–Rödl, Spencer Turán bound, independent set, homomorphism embedding, extremal hypergraph theory, $K_4^3 \setminus e$
