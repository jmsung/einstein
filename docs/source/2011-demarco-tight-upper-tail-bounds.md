---
type: source
kind: paper
title: Tight upper tail bounds for cliques
authors: B. DeMarco, J. Kahn
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1111.6687
source_local: ../raw/2011-demarco-tight-upper-tail-bounds.pdf
topic: general-knowledge
cites:
---

# Tight upper tail bounds for cliques

**Authors:** B. DeMarco, J. Kahn  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1111.6687

## One-line
Proves a sharp upper-tail bound for the number of $K_k$-copies in the Erdős–Rényi random graph $G(n,p)$, closing a long-standing $\log(1/p)$ gap in the exponent.

## Key claim
For $k \geq 2$, $p \geq n^{-2/(k-1)}$, $\eta > 0$, with $\xi_k$ the number of $K_k$ in $G(n,p)$:
$$\Pr(\xi_k > (1+\eta)\mathbb{E}\xi_k) < \exp\!\left(-\Omega_{\eta,k}\,\min\{n^2 p^{k-1}\log(1/p),\; n^k p^{\binom{k}{2}}\}\right),$$
tight up to the constant in the exponent (matched by a companion lower bound for $\eta = 1$).

## Method
Induction on $k$ combined with a "reduction to the $k$-partite version" via Harris's inequality and a Janson-type Poisson approximation. The core technical work classifies $K_k$-copies into four types (containing a high-degree vertex, a high-degree pair, a heavy edge, or "typical"), bounds each anomalous class using elementary large-deviation tools (Chernoff, a Bernstein-type bound, and a counting lemma of Alon on $r$-partite graphs with edge caps), and handles the typical copies by a direct concentration argument on the truncated weight $\min(w'(a,b), \zeta)$.

## Result
Theorem 1.1: the displayed bound holds for any $H$ on $k$ vertices with $\delta(H) \geq k-2$ (complement is a matching), in particular all cliques. Theorem 1.2: matching lower bound $\Pr(\xi_{K_k} \geq 2\mathbb{E}\xi_{K_k}) \geq \exp[-O(f(k,n,p))]$ where $f(k,n,p) := \min\{n^2 p^{k-1}\log(1/p),\, n^k p^{\binom{k}{2}}\}$. The two regimes correspond to (i) "planting a clique of size $\sim np^{(k-1)/2}$" and (ii) the small-$p$ regime where one cheaply forces the upcount by tossing extra random edges. Extends Kim–Vu (triangles, 2004) and Chatterjee / DeMarco–Kahn (2010) for $K_3$ to all $K_k$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — sharp upper-tail concentration for subgraph counts in $G(n,p)$ as a template for extremal/large-deviation reasoning in random discrete structures (could marginally inform extremal-graph or sieve-theory framings, but is not a direct technique for any of the 23 arena problems).

## Open questions / connections
- Conjecture 10.1: for general $H$, the truth of $\Pr(\xi_H \geq 2\mathbb{E}\xi_H)$ is the max of "plant a $K \subseteq H$" lower bounds $\exp[-O(\Psi(K,n,p))]$ and the Janson–Oleszkiewicz–Ruciński bound $\exp[-\Theta(M_H(n,p)\log(1/p))]$.
- Extends Kim–Vu polynomial concentration [14,15] and Janson–Oleszkiewicz–Ruciński [11]; leaves the non-clique case $\Delta_H \leq k-2$ open at the constant level.
- Estimating $\Pr(\xi_H \geq \gamma \mathbb{E}\xi_H)$ for $\gamma = \omega(1)$ is only partly settled (eq. 49 for cliques); general $H$ open.

## Key terms
upper tail, large deviations, random graphs, Erdős–Rényi, $G(n,p)$, subgraph counts, clique counts, $K_k$, Janson inequality, Harris inequality, Kim–Vu polynomial concentration, fractional independence number, DeMarco, Kahn, Chatterjee
