---
type: source
kind: paper
title: Isoperimetric Inequalities for Ramanujan Complexes and Topological Expanders
authors: T. Kaufman, D. Kazhdan, A. Lubotzky
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1409.1397
source_local: ../raw/2014-kaufman-isoperimetric-inequalities-ramanujan-complexes.pdf
topic: general-knowledge
cites:
---

# Isoperimetric Inequalities for Ramanujan Complexes and Topological Expanders

**Authors:** T. Kaufman, D. Kazhdan, A. Lubotzky  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1409.1397

## One-line
First explicit construction of bounded-degree 2-dimensional topological expanders, answering Gromov's question affirmatively, via new $\mathbb{F}_2$ isoperimetric inequalities for Ramanujan complexes.

## Key claim
The 2-skeletons $Y_a$ of 3-dimensional non-partite Ramanujan complexes $X_a$ arising from $\mathrm{PGL}_4(\mathbb{F}_q((t)))$ (for $q$ a sufficiently large prime power) form an infinite family of bounded-degree 2-dimensional **topological expanders**. Conditional on Serre's congruence subgroup conjecture for the Cartwright–Steger lattice, infinitely many are also bounded-degree **coboundary expanders**.

## Method
Combines (i) a criterion of Kaufman–Wagner (Theorem 1.7): cocycle expansion + large $\mathbb{F}_2$-systole $\Rightarrow$ topological overlapping (extending Gromov's coboundary-expander criterion to non-vanishing cohomology); (ii) new isoperimetric inequalities on $X_a$ proved via a *locally minimal cochain* analysis using thick/thin vertex+edge dichotomies in vertex links, combined with the Ramanujan spectral bound on $X(1)$ and the Alon–Milman / mixing-lemma machinery on the spherical building $S(4,q)$ links. Then the result on $X_a$ is transferred to its 2-skeleton $Y_a$.

## Result
**Theorem 1.8:** for non-partite Ramanujan quotients of $\tilde A_3(F)$ and any locally-minimal $\alpha \in C^i(X,\mathbb{F}_2)$ with $\|\alpha\|\le \eta_i$ ($i=0,1,2$): $\|\delta_i\alpha\| \ge \epsilon_i \|\alpha\|$, with $\epsilon_i,\eta_i$ independent of $q$ (for $\epsilon_i$ at least). **Theorem 1.9 / Cor. 1.10:** in $\dim 2$, every nontrivial 1-cocycle satisfies $\|\alpha\| \ge \frac{1}{4(1+\epsilon_0)}$ — the first *linear* lower bound on an $\mathbb{F}_2$ cohomological systole. **Cor. 7.15:** every non-trivial 2-cocycle has $|\alpha|\ge q^3|X(0)|$, again linear.

## Why it matters here
General background; no direct arena tie. Closest relevance is the **Ramanujan spectral / mixing-lemma toolkit** (Alon–Milman bound, bipartite bi-regular mixing) usable in autocorrelation / extremal-graph problems, and as a reference point for *systolic linear lower bounds* (which the paper notes feed CSS quantum-code distance estimates).

## Open questions / connections
- Are 2-dimensional Ramanujan complexes themselves topological expanders (not just their 3-dim ambient $X_a$'s 2-skeleton)?
- Can the constant $\mu_2$ (cofilling at level 2) be made independent of $q$?
- Unconditional removal of the Serre/CSP assumption for Cartwright–Steger lattices to get bounded-degree coboundary expanders outright.
- Extends Meshulam–Wallach and Linial–Meshulam coboundary expansion of $\Delta_n^{(d)}$ to bounded-degree regime; complements Fox–Gromov–Lafforgue–Naor–Pach geometric-expander result.

## Key terms
Ramanujan complex, topological expander, coboundary expander, cocycle expansion, $\mathbb{F}_2$ systole, Bruhat–Tits building, PGL_4, spherical building, Cartwright–Steger lattice, congruence subgroup property, Alon–Milman inequality, Gromov overlap theorem, locally minimal cochain, isoperimetric inequality, CSS quantum codes
