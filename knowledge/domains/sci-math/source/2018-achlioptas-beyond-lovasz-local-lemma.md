---
type: source
kind: paper
title: "Beyond the Lovasz Local Lemma: Point to Set Correlations and Their Algorithmic Applications"
authors: Dimitris Achlioptas, Fotis Iliopoulos, Alistair Sinclair
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1805.02026v4
source_local: ../raw/2018-achlioptas-beyond-lovasz-local-lemma.pdf
topic: general-knowledge
cites:
---

# Beyond the Lovasz Local Lemma: Point to Set Correlations and Their Algorithmic Applications

**Authors:** Dimitris Achlioptas, Fotis Iliopoulos, Alistair Sinclair  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1805.02026v4

## One-line
A new algorithmic Lovász Local Lemma (LLL) condition based on point-to-set correlations between bad events, unifying resampling and backtracking local-search algorithms and yielding a new vertex coloring bound for graphs with bounded triangles per neighborhood.

## Key claim
For any graph $G$ with max degree $\Delta$ where each vertex's neighborhood spans at most $T$ edges, $\chi(G) \leq (1+\epsilon)\, \Delta / \ln(\sqrt{T+1})$ for $\Delta \geq \Delta_\epsilon$ and $T \leq \Delta^{2-\epsilon}$ (constant $(2+\epsilon)$ otherwise); also a unified algorithmic LLL: convergence holds whenever $\frac{1}{\psi_i} \sum_{S \subseteq [m]} \gamma_{iS} \prod_{j \in S} \psi_j < 1$.

## Method
Spectral-radius framing of local search: the transition submatrix $A$ on flawed states is decomposed flaw-by-flaw, and a change of basis by measure $\mu$ converts each block's induced operator norm into a "charge" $\gamma_{iS}$ — an ergodic-flow ratio counting transitions into $\tau$ that introduce at least the flaws in $S$. Introducing *primary flaws* (flaws never fixed collaterally) sharpens charges via set-equality on primary indices, making backtracking steps fit the LLL framework. The coloring algorithm is *hybrid*: resampling explores the state space while backtracking escapes triangle-induced bad regions where Molloy's pure-resampling argument collapses.

## Result
The main algorithmic LLL condition (Theorem 2.4) captures the strongest prior condition [Achlioptas-Iliopoulos-Kolmogorov] as a special case by replacing dependency-graph neighborhoods with point-to-set charges that vanish on subsets never co-introduced. The coloring theorem (Theorem 2.5/1.1) extends Molloy's triangle-free $(1+o(1))\Delta/\ln\Delta$ bound to arbitrary graphs, within a factor 4 of $\chi(G)$ universally, and matches the algorithmic barrier for $G(n, d/n)$ random graphs in the regime $T \leq \Delta^{2-\epsilon}$. Recovers Esperet-Parreau's $4\Delta$ acyclic edge-coloring bound black-box; makes Bernshteyn's acyclic-index bound constructive; converts variable-setting LLL into constructive single-clause-backtracking DPLL.

## Why it matters here
General background; no direct arena tie — the wiki has no current problem on chromatic number or LLL-based local search, and Einstein Arena problems lean on continuous-geometric optimization rather than discrete CSP convergence. Latent relevance: the spectral-radius-of-transition-matrix framing could inform convergence analysis of resampling-style optimizers (e.g., basin-hopping, parallel tempering) if rephrased as bounding $\rho(A)$ for the "stay-in-bad-basin" sub-stochastic operator.

## Open questions / connections
- Can hybrid resample/backtrack be adapted to continuous optimization where "primary flaws" become persistent geometric obstructions (e.g., contact-graph constraint violations in P11/P18)?
- Davies et al. (follow-up) generalize to local $k$-cycle density — what's the right "cycle-density" analog for geometric packings?
- The algorithmic barrier for $G(n,d/n)$ chromatic number — does an analogous information-computation gap exist for our random-init packing problems?
- Spectral-radius bound vs traditional convergence proofs — would a $\rho(A)$ view sharpen the diagnosis of stuck basins in CMA-ES / basin-hopping?

## Key terms
Lovász Local Lemma, Moser-Tardos, resampling algorithms, backtracking algorithms, entropy compression, point-to-set correlations, primary flaws, spectral radius, transition matrix, Molloy triangle-free coloring, chromatic number, list chromatic number, acyclic edge coloring, hybrid local search, charge, dependency graph
