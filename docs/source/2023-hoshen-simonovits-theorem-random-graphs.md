---
type: source
kind: paper
title: Simonovits's theorem in random graphs
authors: Ilay Hoshen, Wojciech Samotij
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2308.13455
source_local: ../raw/2023-hoshen-simonovits-theorem-random-graphs.pdf
topic: general-knowledge
cites:
---

# Simonovits's theorem in random graphs

**Authors:** Ilay Hoshen, Wojciech Samotij  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2308.13455

## One-line
Determines the sharp threshold above which the largest $H$-free subgraph of the random graph $G_{n,p}$ is exactly $(\chi(H)-1)$-partite, for edge-critical, strictly 2-balanced $H$.

## Key claim
If $H$ is nonbipartite, edge-critical, and strictly 2-balanced, then for $p \geq (\theta_H + \varepsilon) \cdot n^{-1/m_2(H)} (\log n)^{1/(e_H-1)}$, a.a.s. every largest $H$-free subgraph of $G_{n,p}$ is $(\chi(H)-1)$-partite — the explicit constant $\theta_H$ is (conjecturally) optimal, partially resolving a DeMarco–Kahn conjecture.

## Method
Reduction to bounding a matching number $\nu(\mathcal{F}_Q[G \cap \mathrm{ext}(\Pi)])$ in an auxiliary hypergraph of $H$-copies, split into low-degree and high-degree regimes for the "defect" subgraph $Q \subseteq F[V_1]$. The high-degree case uses a Janson-type lower-tail bound combined with the DeMarco–Kahn "rigidity + core" correlation inequality (Harris) to reduce control over largest-cut deficits to a fixed near-cut. A union bound over cuts with small deficit closes the loop, using sharp constants from a blowup-copy density $\pi_H$.

## Result
Theorem 1.5: a.a.s. $G_{n,p}$ is $H$-Simonovits at $p \geq (\theta_H + \varepsilon) n^{-1/m_2(H)} (\log n)^{1/(e_H-1)}$, where $\theta_H$ is defined by $(\chi(H)-1)^{2-v_H} \pi_H \theta_H^{e_H-1} = 2 - 1/m_2(H)$ and $\pi_H = \lim_m N(H, K_{\chi(H)-1}(m)^+)/m^{v_H-2}$. Generalizes DeMarco–Kahn's clique result (Theorem 1.4) to all edge-critical strictly 2-balanced $H$ (cliques and odd cycles included).

## Why it matters here
General background; no direct arena tie. Edge-critical extremal/random structure is tangential to the current 23 problems (sphere packing, autocorrelation, kissing) — closest relevance is to extremal-graph problems if any arise, and as a methodological template for sharp-threshold proofs (Janson lower tail + rigidity/core + cut-deficit union bound).

## Open questions / connections
- Is $\theta_H$ actually optimal? The paper conjectures yes, contradicting DeMarco–Kahn's earlier prediction (every edge extends to some $H$-copy, not necessarily $\Pi$-crossing).
- Removing the strictly-2-balanced hypothesis (Conlon–Gowers/Samotij removed it in the approximate setting).
- Extending the exact threshold to non-edge-critical $H$ (no graph of chromatic number $\geq \chi(H)$ can be $H$-Simonovits there, so the question is different).
- Relationship to the random-$H$-free-graph thresholds of Balogh–Morris–Samotij–Warnke and Engelberg–Samotij–Warnke (same $\theta'_H$-shaped function with $(\log n)^{1/(e_H-1)}$).

## Key terms
Simonovits's theorem, edge-critical graph, strictly 2-balanced, 2-density $m_2(H)$, $H$-free subgraph, random graph $G_{n,p}$, sharp threshold, DeMarco–Kahn rigidity, Janson inequality, chromatic number, extremal graph theory, Turán-type
