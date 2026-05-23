---
type: source
kind: paper
title: High powers of Hamiltonian cycles in randomly augmented graphs
authors: Sylwia Antoniuk, A. Dudek, Christian Reiher, A. Ruci'nski, M. Schacht
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2002.05816
source_local: ../raw/2020-antoniuk-high-powers-hamiltonian-cycles.pdf
topic: general-knowledge
cites:
---

# High powers of Hamiltonian cycles in randomly augmented graphs

**Authors:** Sylwia Antoniuk, A. Dudek, Christian Reiher, A. Ruci'nski, M. Schacht  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2002.05816

## One-line
Determines how few random edges must be added to a dense graph $G$ (with $\delta(G) \ge \alpha n$, $\alpha > k/(k+1)$) to force the $(k\ell+r)$-th power of a Hamiltonian cycle with high probability.

## Key claim
For all integers $k \ge 1$, $r \ge 0$, $\ell \ge r(r+1)$, and $m = k\ell + r$, the $(k,m)$-Dirac threshold satisfies $d_{k,m}(n) \le n^{-2/\ell}$ — i.e., adding $O(n^{2-2/\ell})$ random edges to any $G$ with $\delta(G) \ge (k/(k+1) + \varepsilon)n$ a.a.s. yields $C_n^m$.

## Method
Absorption method built on four lemmas (Connecting, Reservoir, Absorbing, Covering), following the framework of Dudek–Reiher–Ruciński–Schacht (2020). Core technical tool: a structural decomposition of $m$-paths into a blow-up of a $k$-path plus $(k+1)$ copies of a "braid graph" $B(\ell, r, t)$ of $\ell$-cliques tied by $r$-bridges; Janson's inequality (a tailored variant, Theorem 2.2) bounds the failure probability for finding these braids in $G(n,p)$. Lower bounds use a blow-up construction $G_\alpha$ on $k+1$ parts plus Pigeonhole + Fact 2.1 (random graphs are $K_\ell$-sparse below threshold).

## Result
Tight thresholds in many regimes (Theorem 1.3): $d_{k,m}(n) = n^{-2/\ell}$ for $(k+1)(\ell-1) \le m \le k\ell + \lfloor(\sqrt{4\ell+1}-1)/2\rfloor$. Corollary 1.4 enumerates: $d_{k,m} = n^{-1}$ for $k+1 \le m \le 2k+1$; $n^{-2/3}$ for $2k+2 \le m \le 3k+1$; $n^{-1/2}$ for $3k+3 \le m \le 4k+1$; $n^{-2/5}$ for $4k+4 \le m \le 5k+1$; $n^{-1/3}$ for $5k+5 \le m \le 6k+2$. Theorem 1.5 extends the $n^{-1/3}$ case to small $k \in \{1,2\}$. First open case: $k=1, m=5$ (threshold depends on $\alpha$ in the exponent, not just the constant).

## Why it matters here
General background; no direct arena tie. Random-graph + absorption techniques and the braid/blow-up decomposition could inform combinatorial-construction problems where one perturbs a structured base by random noise, but none of the 23 Einstein problems are explicitly Hamiltonian-power instances.

## Open questions / connections
- Exact threshold for $C_n^5$ (case $k=1, m=5$) — authors show it depends on $\alpha$ through the exponent, not just a multiplicative constant.
- Extends Pósa–Seymour conjecture (Komlós–Sárközy–Szemerédi) into the randomly-augmented regime.
- $k=0$ case ($\delta(G) = o(n)$): only $d_{0,m} = o(n^{-1/m})$ is known for $m \ge 2$ (Böttcher–Montgomery–Parczyk–Person).

## Key terms
Hamiltonian cycle power, Pósa–Seymour conjecture, Dirac threshold, randomly augmented graph, absorption method, Janson inequality, braid graph, blow-up decomposition, Szemerédi regularity, Komlós–Sárközy–Szemerédi, extremal graph theory, random graphs
