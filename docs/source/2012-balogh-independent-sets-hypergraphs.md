---
type: source
kind: paper
title: Independent sets in hypergraphs
authors: J. Balogh, Robert Morris, Wojciech Samotij
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.6530
source_local: ../raw/2012-balogh-independent-sets-hypergraphs.pdf
topic: general-knowledge
cites:
---

# Independent sets in hypergraphs

**Authors:** J. Balogh, Robert Morris, Wojciech Samotij  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.6530

## One-line
Proves a structural "container" theorem: every independent set in a uniform hypergraph with sufficiently balanced edge distribution is almost contained in one of a small number of sparse "almost-independent" sets, yielding sparse-random analogues of Szemerédi, Erdős–Stone, Erdős–Simonovits, and the KŁR conjecture.

## Key claim
Main theorem (Theorem 2.2): for a $k$-uniform hypergraph $H$ whose co-degrees satisfy $\Delta_\ell(H) \leq c \cdot p^{\ell-1} e(H)/v(H)$, the independent sets $\mathcal{I}(H)$ admit a partition into few classes, each contained in one "fingerprint" set $S \subseteq V(H)$ of size $O(pv(H))$ with $|S| \leq C p v(H)$ such that the complement contains $\leq \varepsilon e(H)$ edges. Concrete consequence: for every $\beta>0$, $k\in\mathbb{N}$ there is $C$ s.t. $m \geq C n^{1-1/(k-1)}$ implies at most $\binom{\beta n}{m}$ $m$-subsets of $[n]$ are $k$-AP-free.

## Method
A clustering / "container" argument refining Kleitman–Winston's graph technique to uniform hypergraphs: iteratively peel high-degree vertices to assign each independent set $I$ a small "fingerprint" $g(I) \subseteq I$ inside a low-edge-density container $f(g(I))$. The balanced-co-degree hypothesis ensures the peeling collapses $\mathcal{I}(H)$ to few containers. No Szemerédi regularity lemma — that is the methodological point.

## Result
Establishes (i) sparse-random Szemerédi (Corollary 1.2) at threshold $n^{-1/(k-1)}$, (ii) Turán for $G(n,p)$ at threshold $n^{-1/m_2(H)}$ (Theorem 1.3), (iii) Erdős–Simonovits stability in sparse random graphs (Theorem 1.5), (iv) counting versions: $f_{n,m}(H) \leq \binom{\text{ex}(n,H)+\delta n^2}{m}$ (Theorem 1.6), (v) the KŁR conjecture (Theorem 1.9): at most $\beta^m \binom{n^2}{m}^{e(H)}$ exceptional regular blow-ups lack canonical copies of $H$. Bounds are tight up to the constant $C$.

## Why it matters here
General background; no direct arena tie. The container method is a structural counting / packing tool — relevant conceptually as a way of bounding the number of "almost-extremal configurations" in combinatorial problems (e.g., Sidon-set / sum-free / arithmetic-progression-free counts), which touches autocorrelation and additive-combinatorics flavored arena problems but is not an optimizer technique.

## Open questions / connections
- Parallel work of Saxton–Thomason ("hypergraph containers", 2012) gives an independent proof with somewhat different quantitative constants — comparison of the two formulations.
- The KŁR sparse counting lemma of Conlon–Gowers–Samotij–Schacht (2014) strengthens Theorem 1.9 in some aspects; how do their dependencies compare on specific small $H$?
- Concrete numerical optimization: tightening the container constant $C(H,\beta)$ for explicit $H$ (cycles, cliques) — open.

## Key terms
hypergraph containers, independent sets, KŁR conjecture, sparse random graphs, Szemerédi theorem, Erdős–Stone, Erdős–Simonovits stability, Turán density, 2-density $m_2(H)$, transference theorem, arithmetic progressions, Kleitman–Winston, sparse regularity lemma, Ramsey threshold
