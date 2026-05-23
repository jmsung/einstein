---
type: source
kind: paper
title: Stability of large cuts in random graphs
authors: Ilay Hoshen, Wojciech Samotij, Maksim Zhukovskii
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2402.14620v1
source_local: ../raw/2024-hoshen-stability-large-cuts-random.pdf
topic: general-knowledge
cites: 
---

# Stability of large cuts in random graphs

**Authors:** Ilay Hoshen, Wojciech Samotij, Maksim Zhukovskii  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2402.14620v1

## One-line
Proves that in $G_{n,p}$ with $1/n \ll p = 1 - \Omega(1)$, all near-maximum $r$-cuts agree on the partition of all but $o(n)$ vertices, and applies this rigidity to settle two conjectures of DeMarco–Kahn on max-cuts and $H$-free subgraphs.

## Key claim
**Theorem 1.1 (core/rigidity):** whp $G_{n,p}$ admits a $(d,r,\alpha)$-core — disjoint sets $S_1,\dots,S_r$ of size $(1/r-\alpha)n$ each contained in different parts of every $r$-cut with deficit $\le d$ — for any $d \ll \sqrt{np}$, and no $\alpha n$ set is monochromatic across all cuts of deficit $\le C\sqrt{np}$ (matching threshold up to constants).

## Method
Tracks the dynamics of $(d,r)$-equivalent vertex pairs under edge addition: a key lemma (2.3) shows that if $e \notin \mathrm{eq}^r_{d+1}(G)$ then $e \notin \mathrm{eq}^r_d(G \cup e)$, yielding a recursion bounding the growth of non-equivalent pairs in $G(n,m)$. Combined with Chernoff-type concentration on cut sizes (Lemma 2.10: every small-deficit cut is balanced) this gives Theorem 2.1 — a non-asymptotic upper bound on $\Pr(G(n,m)\text{ not }(d,r,\varepsilon)\text{-rigid})$. Applications use a resampling trick: perturbing $\Theta(\log n)$ edges leaves the core nearly invariant (Corollary 2.7), so Janson's inequality + Harris's inequality can be applied to fixed cores.

## Result
**Application 1 (Theorem 1.2):** For $p \ge C(\log n/n)^{1/k}$ and $p \gg (\log n)^2/n$, whp every max $r$-cut of $G_{n,p}$ splits the common neighborhood of any $k$-set into parts of size $(1/r \pm \varepsilon)np^k$ — nearly resolving DeMarco–Kahn Conjecture 13.2. **Application 2 (Theorem 1.5):** For nonbipartite, edge-critical, strictly 2-balanced $H$ and $p \le (\theta_H - \varepsilon) \cdot n^{-1/m_2(H)}(\log n)^{1/(e_H-1)}$, whp $G_{n,p}$ is **not** $H$-Simonovits, where $\theta_H$ is the explicit constant from $(\chi(H)-1)^{2-v_H} \pi_H \theta_H^{e_H-1} = 2 - 1/m_2(H)$. This matches the upper bound of Hoshen–Samotij [14], pinning the sharp threshold and refuting DeMarco–Kahn's earlier guess.

## Why it matters here
General background; no direct arena tie. The rigidity/core machinery is a useful template for "near-optimal solutions cluster on a unique skeleton" arguments, which echoes the basin-rigidity intuition in sphere-packing / kissing problems where most local optima share a fixed combinatorial structure.

## Open questions / connections
- Can the $o(n)$ "uncertain" vertex set be sharpened to $\Theta(\sqrt{n/p})$? Authors conjecture yes; cannot even show uniqueness of max 2-cut whp.
- Extend Theorem 1.5 to edge-critical $H$ that are not strictly 2-balanced (no sharp threshold known).
- Weaken the $p \gg (\log n)^2/n$ hypothesis in Theorem 1.2 to $p \gg \log n/n$ — needs better control of cuts with deficit $\Theta(\log n)$.

## Key terms
binomial random graph, maximum cut, max-r-cut, rigidity, core, deficit, Simonovits theorem, edge-critical graph, 2-balanced, chromatic number, Turán-type, $H$-free subgraphs, Janson's inequality, Harris's inequality, DeMarco–Kahn, Kohayakawa–Łuczak–Rödl, sharp threshold
