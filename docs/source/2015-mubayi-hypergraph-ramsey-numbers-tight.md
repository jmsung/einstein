---
type: source
kind: paper
title: "Hypergraph Ramsey numbers: tight cycles versus cliques"
authors: D. Mubayi, V. Rödl
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1503.03855
source_local: ../raw/2015-mubayi-hypergraph-ramsey-numbers-tight.pdf
topic: general-knowledge
cites:
---

# Hypergraph Ramsey numbers: tight cycles versus cliques

**Authors:** D. Mubayi, V. Rödl  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1503.03855

## One-line
Establishes exponential bounds on the 3-uniform hypergraph Ramsey number $r(C_s^3, K_t^3)$ for tight cycles $C_s^3$ with $s \not\equiv 0 \pmod 3$ versus cliques $K_t^3$.

## Key claim
For fixed $s \geq 5$ with $s \not\equiv 0 \pmod 3$, there exist positive constants $a, b$ such that $2^{at} < r(C_s^3, K_t^3) < 2^{bt^2 \log t}$.

## Method
Lower bound uses a probabilistic construction: form random 3-graph $H$ on $[n]$ from $G(n,1/2)$ where $ijk$ is an edge iff $ij, ik \in G$ and $jk \notin G$; a Steiner-triple-system counting argument bounds the independence number by $O(\log n)$. Upper bound for $s \geq 7$ uses a new Ramsey-supersaturation principle: if $F(v)$ clones a vertex of $F$, then $r(F(v), K_t^3) < r(F, K_t^3)^f$; combined with the known $r(K_4^3, K_t^3) = 2^{O(t^2 \log t)}$ from Conlon–Fox–Sudakov and the observation $C_s^3 \subset K_4^{3(s)}$. For $s = 5$, proves new bound $r(K_5^{3-}, K_t^3) = 2^{O(t^2 \log t)}$ via vertex on-line ordered Ramsey game with a builder strategy avoiding ordered $K_4^-$.

## Result
Tight cycle Ramsey number is exponential (not polynomial) when $s \not\equiv 0 \pmod 3$, in contrast to the polynomial regime when $3 \mid s$. Auxiliary bound: $r(K_s^{3-}, K_t^3) = 2^{O(t^{s-3} \log t)}$, one tower-level below $r(K_s^3, K_t^3) = 2^{O(t^{s-2} \log t)}$. Generalization to $k$-graphs gives $2^{c_k t^{k-2}} < r(C_s^k, K_t^k) < t_{k-1}(t^{d_s})$.

## Why it matters here
General background; no direct arena tie. Relevant to extremal-graph/hypergraph reasoning archetypes (Erdős, Szemerédi, Conlon personas) and the supersaturation–blowup technique, which is a transferable tool when bounding hypergraph quantities by reducing to smaller substructures.

## Open questions / connections
- Problem 5.1: Is $\log r(K_s^{3-1}, K_t^3) = o(\log r(K_s^{3-}, K_t^3))$? — i.e., does removing one edge always drop a tower level?
- Problem 5.2: Does $r(C_s^3, K_t^3) < 2^{t^{1+\epsilon_s}}$ with $\epsilon_s \to 0$ as $s \to \infty$ (sparser cycles → smaller Ramsey)?
- Extends Conlon–Fox–Sudakov [5] hypergraph Ramsey machinery; leaves open whether $r(K_5^4, K_t^4)$ grows as a tower of height 3.

## Key terms
hypergraph Ramsey number, tight cycle, $C_s^3$, $K_t^3$, supersaturation, vertex blowup, cloning operation, on-line ordered Ramsey, builder-painter game, $K_5^{3-}$, Conlon-Fox-Sudakov, Steiner triple system, Mubayi, Rödl, probabilistic construction, extremal hypergraph theory
