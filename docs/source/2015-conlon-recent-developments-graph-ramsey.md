---
type: source
kind: paper
title: Recent developments in graph Ramsey theory
authors: D. Conlon, J. Fox, B. Sudakov
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1501.02474
source_local: ../raw/2015-conlon-recent-developments-graph-ramsey.pdf
topic: general-knowledge
cites:
---

# Recent developments in graph Ramsey theory

**Authors:** D. Conlon, J. Fox, B. Sudakov  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1501.02474

## One-line
A broad survey of progress on graph and hypergraph Ramsey numbers $r(H)$, $r(s,t)$, $r_k(t)$ and their variants (induced, size, ordered, Folkman), summarizing best known bounds and central open problems.

## Key claim
The classical diagonal bound $r(t) \le \binom{2t-2}{t-1} = O(4^t/\sqrt{t})$ has only been improved by sub-exponential factors (Conlon: $r(t) \le t^{-c\log t/\log\log t} 4^t$); the lower bound $r(t) \ge (1+o(1))\frac{\sqrt{2}t}{e}\sqrt{2}^t$ (Spencer) has stood since 1975. For the off-diagonal triangle case, $r(3,t) = (1/4 + o(1)) t^2/\log t$ (Shearer upper; Bohman–Keevash / Fiz Pontiveros–Griffiths–Morris lower via triangle-free process).

## Method
Erdős–Szekeres recursion + Goodman/Thomason triangle-counting (upper bounds); probabilistic method, Lovász local lemma, and the $H$-free stochastic process (lower bounds); Erdős–Rado stepping-up lemma for hypergraph uniformity escalation; quasirandomness and dependent random choice for sparse-graph Ramsey; Frankl–Wilson intersection construction and Barak–Rao–Shaltiel–Wigderson 2-source dispersers for explicit Ramsey graphs.

## Result
Best known: $r(t) = 2^{\Theta(t)}$ with multiplicative gap; $r_3(t)$ between $2^{c't^2}$ and $2^{2^{ct}}$ (a full exponential gap, with $500 Erdős conjecture that lower bound is correct); $r_3(t;4) \ge 2^{2^{c't}}$ via stepping-up; $r(s,t) \le c_s t^{s-1}/(\log t)^{s-2}$ (Ajtai–Komlós–Szemerédi); Chvátal–Rödl–Szemerédi–Trotter: bounded-degree graphs have $r(H) = O_\Delta(n)$. Explicit Ramsey graphs achieve $2^{2^{(\log\log t)^{1+\epsilon}}}$ vertices (Barak et al.), beating Frankl–Wilson's $t^{c\log t/\log\log t}$.

## Why it matters here
General background on extremal/Ramsey methodology (probabilistic method, LLL, pseudorandomness, dependent random choice, stepping-up) — these techniques recur in extremal-graph and combinatorics problems on the Arena (e.g., autocorrelation, Sidon sets, kissing-number combinatorial relaxations). No single Arena problem is the Ramsey number itself, but the upper/lower-bound *technique inventory* is directly transferable.

## Open questions / connections
- Improve Spencer's lower bound $r(t) \ge (1+\epsilon)\sqrt{2}^t/e \cdot \sqrt{2}t$ by *any* constant factor (Problem 2.3).
- Resolve Erdős's conjecture $r_3(t) \ge 2^{2^{c't}}$ (the $500 problem); would automatically close gaps for all $r_k(t)$ via stepping-up.
- Close the polynomial gap in $r(s,t)$ for $s \ge 4$ between Bohman–Keevash $H$-free-process lower bound and Ajtai–Komlós–Szemerédi upper bound.
- Explicit constructions matching the probabilistic $r(t) > (1+\epsilon)^t$ bound (Erdős $100 problem).

## Key terms
Ramsey number, Erdős–Szekeres, diagonal Ramsey, off-diagonal Ramsey, hypergraph Ramsey, stepping-up lemma, triangle-free process, Lovász local lemma, probabilistic method, dependent random choice, Frankl–Wilson construction, quasirandomness, Bohman–Keevash, Spencer lower bound, Ajtai–Komlós–Szemerédi, Folkman numbers, induced Ramsey, size Ramsey, Erdős–Hajnal conjecture
