---
type: source
kind: paper
title: On the Lower Tail Variational Problem for Random Graphs
authors: Yufei Zhao
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1502.00867
source_local: ../raw/2015-zhao-lower-tail-variational-problem.pdf
topic: general-knowledge
cites:
---

# On the Lower Tail Variational Problem for Random Graphs

**Authors:** Yufei Zhao  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1502.00867

## One-line
Partially characterizes the "replica symmetric" phase of the graphon variational problem governing lower-tail large deviations $P(X_H \le (1-\delta)\mathbb{E}X_H)$ for subgraph counts in $G(n,p)$.

## Key claim
For $LT_p(K_3, q) := \min\{\mathbb{E}[I_p(W)] : t(K_3,W) \le q^3\}$, the constant graphon $W \equiv q$ is the unique minimizer when $\overline{q}(p) < q < p$ and is *not* a minimizer when $q < \underline{q}(p)$, with sparse-limit slopes $\lim_{p\to 0} \overline{q}(p)/p = 0.466\ldots$ (root of $h(r) + \tfrac{1}{2}rh'(r)=0$) and $\lim_{p\to 0} \underline{q}(p)/p = 0.209\ldots$.

## Method
Uses graphon calculus on the Chatterjee–Varadhan / Chatterjee–Dembo variational reduction. The replica-symmetric (constant-is-optimal) regime is established via a Goodman-type inequality $t(K_3,W)+t(K_3,U) \ge 2q^3$ when $U+W \ge 2q$, combined with a Hölder-extension bound $t(K_3,W) \le \mathbb{E}[W^2]^{3/2}$ and a tangent-line convex-minorant argument on $I_p$. Symmetry breaking is shown by restricting to bipartite graphons $\mathrm{BIP}_{a,b}$ and exhibiting two-block configurations with strictly lower entropy. General $H$ uses Lagrange multipliers on $t'(H,W)$ plus a lower bound $W \ge r^m \cdot r^{-m}$ a.e.

## Result
**Triangle case (Theorem 2.1, 2.6):** Replica symmetry holds for $r > 0.466\ldots$; symmetry breaking for $r < 0.209\ldots$ in the sparse limit $LT(K_3,r) := \min\{\mathbb{E}[h(W)] : t(K_3,W) \le r^3\}$, where $h(x)=x\log x - x + 1$. **General $H$ (Theorem 2.2, 2.7):** for every $H$ there is $r_H < 1$ with replica symmetry above; for non-bipartite $H$ there is $r_H > 0$ with symmetry breaking below (explicitly $LT(H,r) < h(r)$ for $r < 0.186$ via $\mathrm{BIP}_{0,1}$). **Corollary 2.8:** translates to $\lim n^{-2}p^{-1} \log P(t(H,G(n,p)) \le (rp)^{e(H)}) = -h(r)$ in the replica-symmetric regime, valid for $p \ge n^{-\alpha_H}$.

## Why it matters here
General background; no direct arena tie. Relevant if extremal-graph or Turán-type problems on the arena require large-deviation rates for subgraph counts, or if the entropy-vs-density tangent-line trick (convex minorant of $I_p \circ \sqrt{\cdot}$) is borrowed for other "is the symmetric solution optimal?" variational problems in our wiki (extremal_graph, combinatorics categories).

## Open questions / connections
- Conjecture 2.3/2.5: for bipartite $H$, $W \equiv q$ (resp. $W \equiv r$) is *always* the unique minimizer — open even when Sidorenko's conjecture fails.
- Conjecture 2.4: for non-bipartite $H$ there is a sharp threshold $r_H^*$; conjectured $r_{K_3}^* = 0.209\ldots$ — gap between $0.209$ and $0.466$ unresolved.
- Solve the variational problem in the symmetry-breaking phase at *any* non-trivial point (no exact solutions known).
- Extends Lubetzky–Zhao [28] (upper tail, $d$-regular $H$) to the lower tail; complements Janson–Warnke [17] (sparse Poisson approach, only $\delta \to 0$ and $\delta \to 1$ extremes resolved).

## Key terms
lower tail large deviations, Erdős–Rényi random graph, graphon variational problem, replica symmetry, symmetry breaking, Sidorenko conjecture, Goodman inequality, Kruskal–Katona, Chatterjee–Varadhan, Chatterjee–Dembo, relative entropy $I_p$, triangle density $t(K_3,W)$, bipartite graphon $\mathrm{BIP}_{a,b}$, Lagrange multiplier, sparse limit $p \to 0$
