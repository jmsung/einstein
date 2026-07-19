---
type: source
kind: paper
title: An Erdős–Gallai-Type Theorem for Keyrings
authors: Alexander Sidorenko
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1705.10254
source_local: ../raw/2017-sidorenko-erd-gallai-type-theorem-keyrings.pdf
topic: general-knowledge
cites:
---

# An Erdős–Gallai-Type Theorem for Keyrings

**Authors:** Alexander Sidorenko  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1705.10254

## One-line
Proves that any graph with average degree exceeding $k-1$ must contain a "keyring" (a cycle with $r$ pendant leaves attached at one vertex) of total size $\geq k$, extending the classical Erdős–Gallai cycle theorem.

## Key claim
**Theorem 1.4:** For any positive integer $r \leq (k-1)/2$, every graph $G \in \mathcal{D}_k$ (i.e., $2e(G) > (k-1)v(G)$) contains a keyring $C_r(l)$ with $r$ leaves and $l+r \geq k$ edges. Also **Theorem 1.3:** every $k$-edge tree $T$ with $p$ preleaves, one adjacent to $\geq (k-p-1)/2$ leaves, lies in $\mathcal{T}_k$ (satisfies Erdős–Sós).

## Method
Uses the standard $k$-minimal subgraph reduction (Remark 1.5: any vertex subset $X$ has $d_G(X) > \frac{k-1}{2}|X|$). For Theorem 1.4, starts from a long cycle (guaranteed by Erdős–Gallai Theorem 1.2), averages degrees on the cycle to find a vertex $u_i$ with $t_i + 2r_i \geq k$, then applies a Hamiltonian-graph lemma (Lemma 3.1) that locates a sub-cycle of length $\geq \lambda$ through $u_i$ using neighbor positions on the Hamiltonian cycle. Theorem 1.3 proceeds by induction on $m(T)$ (max leaves per preleaf), via an augmenting-path argument in a bipartite directed graph $F$ on preleaves/leaves/external vertices.

## Result
For $r \leq (k-1)/2$, the average-degree threshold $k-1$ (Erdős–Gallai cycle threshold) already forces a keyring of $\geq k$ edges — no extra degree assumption needed. The leaf-rich-preleaf tree class is enlarged: from "one preleaf with $\geq (k-1)/2$ leaves" (prior, [13]) to "one preleaf with $\geq (k-p-1)/2$ leaves", confirming more cases of the Erdős–Sós conjecture.

## Why it matters here
General background; no direct arena tie. Extremal graph theory result relevant if the agent encounters Erdős–Sós-type or Turán-type subgraph-containment problems where average-degree thresholds force specific tree/cycle-with-tail structures.

## Open questions / connections
- Full Erdős–Sós conjecture remains open for general $k$-edge trees (only large $k$ resolved by Ajtai–Komlós–Simonovits–Szemerédi).
- Can the constraint $r \leq (k-1)/2$ in Theorem 1.4 be relaxed? Conjectured analog for larger $r$?
- Extends Fan–Sun's lasso theorem (cycle + path sharing one vertex) — natural generalization: cycle with arbitrary tree appended at one vertex.

## Key terms
Erdős–Gallai theorem, Erdős–Sós conjecture, keyring graph, lasso, extremal graph theory, average degree threshold, k-minimal graph, spider tree, caterpillar, preleaf, Hamiltonian cycle, subgraph containment, Sidorenko
