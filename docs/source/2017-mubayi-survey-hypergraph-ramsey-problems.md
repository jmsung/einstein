---
type: source
kind: paper
title: A survey of hypergraph Ramsey problems
authors: Dhruv Mubayi, Andrew Suk
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1707.04229v3
source_local: ../raw/2017-mubayi-survey-hypergraph-ramsey-problems.pdf
topic: general-knowledge
cites: 
---

# A survey of hypergraph Ramsey problems

**Authors:** Dhruv Mubayi, Andrew Suk  ·  **Year:** 2017  ·  **Source:** http://arxiv.org/abs/1707.04229v3

## One-line
A survey of quantitative hypergraph Ramsey theory — bounds, conjectures, and open problems for $r_k(s,n)$ and its many generalizations when $k \geq 3$.

## Key claim
For $k$-graphs ($k \geq 3$), there is a one-exponential gap between known lower and upper bounds for $r_k(n,n)$: $\mathrm{twr}_{k-1}(c_1 n^2) \leq r_k(n,n) \leq \mathrm{twr}_k(c_2 n)$. The Erdős–Hajnal–Rado conjecture asserts the upper bound is tight (Erdős's \$500 conjecture: $r_3(n,n) > 2^{2^{cn}}$); via stepping-up, the $k=3$ case implies all $k \geq 4$.

## Method
Survey synthesis — collects results obtained via the Erdős–Hajnal stepping-up lemma, Erdős–Rado partition arguments, probabilistic deletion / supersaturation, the triangle-free process and independent-neighborhood process, Steiner-system constructions, and partial-order / ideal-counting bijections (Moshkovitz–Shapira, Milans–Stolee–West). No new central technique; organizes a decade-plus of $k$-graph Ramsey advances.

## Result
Catalogues sharp/near-sharp bounds across regimes: $r_3(s,n)$ between $2^{csn\log(n/s+1)}$ and $2^{(c'n/s)^{s-2}\log(n/s)}$; $r_4(5,n) > 2^{n^{c\log n}}$, $r_4(6,n) > 2^{2^{cn^{1/5}}}$; Erdős–Rogers $g(k,N)=O(\log^{(k-13)}N)$ for $k\geq 14$; tight-cycle $r_3(TC_s,n)$ between $2^{c_1 n}$ and $2^{c_2 n^2 \log n}$ when $s \not\equiv 0\pmod 3$; bipartite $r_3(S_n,S_n) = 2^{\Theta(n^2)}$; ordered tight-path identities $r_3(P_s;q)=P_{q-1}(s)+1$ (Moshkovitz–Shapira).

## Why it matters here
General background; no direct arena tie. Closest connection is to Problem 18 (extremal graph / Ramsey-style) — the stepping-up + tower-height machinery and probabilistic-construction lower-bound techniques are reusable templates for any extremal-counting problem the agent encounters.

## Open questions / connections
- Conjecture 3.1 (Erdős, \$500): is $r_3(n,n) > 2^{2^{cn}}$? Equivalent (Cor. 10.5) to $r_4(P_5,n) \geq 2^{2^{cn}}$.
- Conjecture 4.2: $r_4(5,n) > 2^{2^{n^c}}$ — would propagate via stepping-up to all $r_k(k+1,n)$.
- Conjecture 5.3 (Erdős–Hajnal): $r_k(k+1,t;n) \geq \mathrm{twr}_{t-1}(cn)$ — open for $k=4$ ($t=4,5$) and $k=5$ ($t=4,5$); resolved for $k\geq 6$, $4\leq t\leq k-2$ (Mubayi–Suk).
- Erdős–Rogers Conjecture 6.2: $g(k,N) = \Theta(\log^{(k-2)} N)$.
- Conlon–Fox–Lee–Sudakov: is $f_k(N,p,\binom{p-i}{k-i}) = (\log^{(i-1)}N)^{o(1)}$?

## Key terms
hypergraph Ramsey number, $r_k(s,n)$, Erdős–Hajnal–Rado, stepping-up lemma, tower function, diagonal Ramsey, off-diagonal Ramsey, Erdős–Rogers function, Erdős–Gyárfás $(p,q)$-coloring, tight cycle, loose cycle, ordered tight-path, Mubayi–Suk, Conlon–Fox–Sudakov, Moshkovitz–Shapira, independent-neighborhood process
