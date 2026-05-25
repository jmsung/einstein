---
type: source
kind: paper
title: Bounded degree cosystolic expanders of every dimension
authors: Shai Evra, T. Kaufman
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1510.00839
source_local: ../raw/2015-evra-bounded-degree-cosystolic-expanders.pdf
topic: general-knowledge
cites:
---

# Bounded degree cosystolic expanders of every dimension

**Authors:** Shai Evra, T. Kaufman  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1510.00839

## One-line
Constructs, for every dimension $d$, infinite families of bounded-degree $d$-dimensional simplicial complexes with the topological overlapping property, resolving Gromov's question affirmatively.

## Key claim
For every $d \in \mathbb{N}$ there exists an infinite family of $d$-dimensional, bounded-degree simplicial complexes with the $c$-topological overlapping property (Theorem 1.3); concretely, $(d-1)$-skeletons of $(d+1)$-dimensional $q$-thick Ramanujan complexes for $q \ge q_0(d)$ are $(\epsilon, \mu)$-cosystolic expanders with $\mu = \mu(d) > 0$, $\epsilon = \epsilon(d,q) > 0$.

## Method
Introduces a local-to-global criterion (Theorem 1.10): if a $Q$-bounded-degree complex $X$ has all proper links being $\beta$-coboundary expanders and all proper links plus $X$ itself being $\alpha$-skeleton expanders, then the $(d-1)$-skeleton is an $(\epsilon, \mu)$-cosystolic expander. Verifies the hypotheses on Ramanujan complexes by showing $q$-thick spherical buildings with strongly transitive action are $\sqrt{\theta_d/q}$-skeleton expanders (Theorem 5.19), via a "symmetric-convex" bipartite-graph eigenvalue bound $\lambda(X) \le \theta \cdot \max(1/\sqrt{k}, 1/\sqrt{k'})$ (Prop. 5.21). Then invokes Gromov's criterion (cosystolic expansion ⇒ topological overlap, via [DKW]).

## Result
For $D \ge 2d+1$, gives infinite bounded-degree families $\{X_n\}$ with embeddings into $\mathbb{R}^D$ (non-adjacent simplices at distance $\ge 1$) whose $1$-neighborhood volume is $\ge C(D) \cdot |X_n|^{1/(D-d)}$ — sharpening the Gromov–Guth generalization of Kolmogorov–Barzdin (Cor. 1.4). The cosystolic expansion is strictly weaker than coboundary expansion (allows nontrivial cocycles, as long as systole $\ge \mu$), which is essential because Ramanujan complexes are known not to be coboundary expanders [KKL].

## Why it matters here
General background; no direct arena tie. Relevant tangentially to extremal-combinatorics / discrete-geometry problems where high-dimensional expansion or overlap arguments could bound configurations, but no concept currently in the einstein wiki invokes cosystolic/coboundary expansion or topological overlap.

## Open questions / connections
- Conjecture [Lub2, 3.2.4]: Ramanujan complexes themselves (not just $(d-1)$-skeletons) are cosystolic expanders.
- Generalizes [KKL] from dimension 2 to all $d$; extends Gromov [Gro] from unbounded-degree examples (complete complexes, spherical buildings, random complexes) to bounded degree.
- Connection to quantum LDPC codes via [GL] (4-dim arithmetic hyperbolic manifolds) and [EOT] (systole upper bounds for high-dim expanders).
- Whether random constructions can yield bounded-degree topological overlappers (currently open).

## Key terms
cosystolic expander, coboundary expander, topological overlapping property, Ramanujan complex, spherical building, Bruhat-Tits building, high-dimensional expander, simplicial complex, Gromov question, link expansion, skeleton expander, F2-cohomology, Cheeger constant, strongly transitive action, Linial-Meshulam-Wallach
