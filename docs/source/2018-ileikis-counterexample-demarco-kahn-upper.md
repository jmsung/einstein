---
type: source
kind: paper
title: A counterexample to the DeMarco‐Kahn upper tail conjecture
authors: Matas Šileikis, L. Warnke
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1809.09595
source_local: ../raw/2018-ileikis-counterexample-demarco-kahn-upper.pdf
topic: general-knowledge
cites:
---

# A counterexample to the DeMarco‐Kahn upper tail conjecture

**Authors:** Matas Šileikis, L. Warnke  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1809.09595

## One-line
Disproves the 2011 DeMarco–Kahn conjecture on the exponential decay rate of the upper tail $P(X_H \geq (1+\varepsilon)\mathbb{E}X_H)$ for subgraph counts in $G_{n,p}$, by exhibiting an infinite family of explicit counterexamples near the appearance threshold.

## Key claim
For the graph family $\mathcal{H} = \{C_{\ell+r} : \ell \geq 3, r \geq 2\}$ (an $\ell$-cycle with $r$ pendant edges attached to one vertex), there exists $c_H > 0$ such that for $n^{-1/m_H}(\log n)^{c_H} \ll p \ll n^{-1/m_H}$, $-\log P(X_H \geq (1+\varepsilon)\mathbb{E}X_H) = o(\min\{\Phi_H, M_H \log(1/p)\})$, violating the conjectured $\Theta$-bound. A new "locally-disjoint" mechanism gives a strictly better lower bound than both prior (clustered and disjoint) mechanisms.

## Method
Two-round edge exposure of $G_{n,p}$: split $p = p_1 + p_2 - p_1 p_2$, use $E_1$ to find a random copy of the cycle $C_\ell$ (above its own threshold since $m_{C_\ell}=1$), then use $E_2$ to attach $z \asymp \mu_H^{1/r}$ extra neighbors to one cycle vertex, forcing $\binom{z}{r} \geq (1+\varepsilon)\mu_H$ copies of $H$. This sequential embedding replaces the naive $\log(1/p)$ factor by $\log(np)$. Section 3 generalizes via three-round exposure with $G$ primal and $J_1,\dots,J_r$ covering primals "glued" into $K$.

## Result
**Lemma 3:** $P(X_H \geq (1+\varepsilon)\mathbb{E}X_H) \geq \exp(-O(\mu_H^{1/r} \log(np)))$ for $H = C_{\ell+r}$, $1 \ll np \ll n^{1/(1+\ell/r)}$. **Theorem 4 / Lemma 5:** general locally-disjoint lower bound $\exp(-O((\varepsilon\mu_K)^{1/r} \log(np^{m_H})))$ whenever $K = \bigcup J_i$ with $v_K/r < \min_{F \in \mathcal{L}_H} v_F$. **Theorem 10:** for the "snail-like" graphs $H_r$ ($r \geq 7$), even the natural revised conjecture mixing all three mechanisms fails — a hybrid clustered+disjoint construction beats it.

## Why it matters here
General background for random-graph extremal probability; no direct Einstein Arena tie. Tangentially relevant to extremal_graph and combinatorics personas (Erdős, Janson, Rucínski lineage) as an example of how lower-bound constructions can defeat plausible Θ-conjectures — the methodological lesson (multi-round exposure, "covering primals", mechanism mixtures) is a transferable technique-pattern for any problem where a heuristic lower bound looks too clean.

## Open questions / connections
- Conjecture 2: the original DeMarco–Kahn bound is conjectured true for strictly balanced $H$ and for $p \gg n^{-1/m_H + \gamma}$ — still open.
- Formulating a corrected upper-tail conjecture for non-strictly-balanced $H$ (even balanced) is left open; Theorem 10 shows the natural three-way-min guess (27) is wrong.
- Connects to large deviation theory [Chatterjee–Varadhan, Chatterjee–Dembo, Eldan] and Stein's method as alternative routes to the right exponent near the appearance threshold.
- Bollobás–Wierman grading decomposition does NOT identify the optimal primal $G$ minimizing $\zeta_H(G)$ (Example 9, snail graph).

## Key terms
upper tail, subgraph count, DeMarco-Kahn conjecture, binomial random graph, $G_{n,p}$, Janson inequality, strictly balanced graph, primal subgraph, appearance threshold, fractional independence number, Bollobás-Wierman grading, locally-disjoint mechanism, large deviation, Šileikis, Warnke
