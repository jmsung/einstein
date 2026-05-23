---
type: source
kind: paper
title: Comparison of two convergence criteria for the variable-assignment Lopsided Lovasz Local Lemma
authors: David G. Harris
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1610.01926v9
source_local: ../raw/2016-harris-comparison-two-convergence-criteria.pdf
ingested_for_concept: probabilistic-method.md
cites: 
---

# Comparison of two convergence criteria for the variable-assignment Lopsided Lovasz Local Lemma

**Authors:** David G. Harris  ·  **Year:** 2016  ·  **Source:** http://arxiv.org/abs/1610.01926v9

## One-line
Constructs k-SAT instances where Harris's Moser-Tardos convergence criterion succeeds even though Shearer's criterion (the strongest possible LLL-style bound) is violated, proving the variable-decomposition criterion is strictly stronger.

## Key claim
For bounded-literal-occurrence k-SAT, the Harris criterion proves $f'(k) \geq F_{MT}(k) = (2^k-1)(1-1/k)^{k-1}/k$, while no LLL variant (including Shearer) can exceed $\tilde{F}_{Shearer}(k) = 2^k/(ek) + \Theta(2^k/k^3)$; the gap $F_{MT} - \tilde{F}_{Shearer}$ grows exponentially in $k$ (e.g. at $k=20$: 19784 vs 19311 vs 19287 for LLL).

## Method
Construct a recursive $k$-SAT formula $\Phi$ via auxiliary graph family $H_j$ built from copies of $K_{L-1,L-1}$ glued at vertices via $k-1$ recursive children. Compute Shearer's stable-set polynomial $Q(G,S,p)$ on $H_j$ using a mutual recurrence $r_j, s_j$ (Propositions 4.1-4.3), reduce to a fixed-point equation $g(a) = a$ on $[2^{-2/(2L-2)}, 1]$, and derive an upper-bound function $\tilde{F}_{Shearer}(k)$ on what any LLL variant can prove. Compare against $F_{MT}$ obtained by Harris's orderability criterion (Theorem 1.6) with uniform weights $\mu(B) = \alpha$.

## Result
Proves $\tilde{F}_{Shearer}(k) = 2^k/(ek) + \Theta(2^k/k^3)$ as a hard ceiling on any LLL-style argument, while $F_{MT}(k) \geq 2^k/(ek) + \Omega(2^k/k^2)$ — a provable exponential separation. The variable-assignment structure (decomposition of bad-events into variables) provides genuinely more information than the probabilities-plus-dependency-graph data Shearer uses. Establishes that Harris's criterion is not merely a computational approximation to Shearer but is fundamentally stronger.

## Why it matters here
General background; no direct arena tie — the LLL/LLLL machinery here is for existence proofs in CSP-style discrete problems, not directly relevant to the Einstein Arena's continuous-optimization problems (sphere packing, autocorrelation, kissing numbers). May tangentially inform extremal-combinatorics or hypergraph-coloring problems if those appear.

## Open questions / connections
- Can the variable-decomposition criterion (Harris 2015) be tightened further to characterize *exactly* which variable-assignment LLL instances are satisfiable, analogous to Shearer's characterization for abstract probability spaces?
- Extends Kolipaka-Szegedy (2011) observation that Shearer is not tight for variable-assignment LLL; connects to He-Li-Liu-Wang-Xia (2017) "beyond Shearer's bound" work.
- Exact value of $f(k)$ and $f'(k)$ for small $k$ remains open — narrow gap to NP-completeness threshold has practical SAT-solver implications.

## Key terms
Lovász Local Lemma, Lopsided LLL, Moser-Tardos algorithm, Shearer's criterion, stable set polynomial, cluster-expansion criterion, k-SAT, bounded variable occurrence, lopsidependency graph, orderability, variable-assignment LLL, dependency graph
