---
type: source
kind: paper
title: Lower tails via relative entropy
authors: Gady Kozma, Wojciech Samotij
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.04850v1
source_local: ../raw/2021-kozma-lower-tails-relative-entropy.pdf
topic: general-knowledge
cites: 
---

# Lower tails via relative entropy

**Authors:** Gady Kozma, Wojciech Samotij  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2104.04850v1

## One-line
Proves that the naive mean-field (product-measure) approximation correctly captures the leading-order logarithmic lower-tail probability for subgraph counts in $G(n,p)$ and $k$-AP counts in random subsets of $[n]$, throughout the entire density range where mean-field is viable.

## Key claim
For any nonempty graph $H$, $p_0<1$, $\varepsilon>0$, there exists $L$ such that for $Ln^{-1/m_2(H)} \le p \le p_0$ and $X = N_H(G(n,p))$:
$$(1-\varepsilon)\Phi^H_{n,p}(\eta+\varepsilon) \le -\log\mathbb{P}(X \le \eta\mathbb{E}[X]) \le (1+\varepsilon)\Phi^H_{n,p}((1-\varepsilon)\eta)$$
where $\Phi^H_{n,p}(\eta)$ is the minimum relative-entropy cost over product measures supported on the lower-tail event. The lower bound on $p$ is optimal up to constants. Analogous results for $s$-uniform hypergraphs (with $m_s(H)$) and for $k$-AP counts (with threshold $n^{-1/(k-1)}$).

## Method
Entropy-based: condition the random graph on the tail event, then iteratively condition on randomly-chosen "chunks" of edges, tracking the drop in Kullback–Leibler divergence. The key technical device (Lemma 16) is a strengthened Pinsker-type inequality — inspired by Janson's inequality — that converts small conditional KL divergence into approximate conditional independence of remaining variables, sharper than total-variation Pinsker for rare events. Harris/FKG ensures conditioned edge marginals stay $\le p$, making the method lower-tail-specific.

## Result
Main technical theorem (Theorem 5): for an $r$-uniform weighted hypergraph $\mathcal{H}$ with degree bounds $\Delta_s(\mathcal{H}) \le K(\lambda p)^{s-1} \cdot e(\mathcal{H})/v(\mathcal{H})$ for all $s \in [r]$, the random induced edge-count $X = e(\mathcal{H}[R])$ satisfies $-\log\mathbb{P}(X \le \eta\mathbb{E}[X]) \le (1-\varepsilon)\Phi^{\mathcal{H}}_p(\eta+\varepsilon) - C$. Matching lower bound (Theorem 7) via standard tilting argument. Explicit dependence: $\lambda \gtrsim 10^{-5}K^{-2}r^{-4}\varepsilon^9(1-p_0)$. Reformulated equivalently as a statement about $r$-homogeneous multilinear polynomials with nonneg coefficients (Theorem 6).

## Why it matters here
General background; no direct arena tie. The relative-entropy / mean-field framework is the canonical tool for nonlinear large deviations on Bernoulli product spaces — relevant scaffolding for any arena problem where one analyzes rare events in random discrete structures (e.g. counting configurations in random sets, Sidon/B_h problems, additive-combinatorics-flavored optimizations). The "weak probabilistic hypergraph container lemma" reformulation links to container-method machinery used across extremal combinatorics.

## Open questions / connections
- Method explicitly **fails for upper tails** (Harris inequality only one-directional); upper-tail problem remains harder, resolved separately for cliques [Harel-Mousset-Samotij] and regular graphs [Basak-Basu].
- Computing $\Phi^H_{n,p}(\eta)$ itself — the variational problem — remains open for most $H$; even triangles have only partial results [Lubetzky-Zhao, Zhao].
- Strengthens KŁR conjecture / container-theorem corollaries [Balogh-Morris-Samotij, Saxton-Thomason] from the $\eta=0$ (forbidden-substructure) case to all $\eta \in [0,1]$.

## Key terms
relative entropy, Kullback-Leibler divergence, nonlinear large deviations, lower tail, subgraph counts, $G(n,p)$, mean-field approximation, hypergraph container method, arithmetic progressions, Janson inequality, Pinsker inequality, 2-density $m_2(H)$, KŁR conjecture, Harris/FKG inequality
