---
type: source
kind: paper
title: On a Solution to the Monge Transport Problem on the Real Line Arising from the Strictly Concave Case
authors: N. Juillet
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1907.00681
source_local: ../raw/2019-juillet-solution-monge-transport-problem.pdf
topic: general-knowledge
cites:
---

# On a Solution to the Monge Transport Problem on the Real Line Arising from the Strictly Concave Case

**Authors:** N. Juillet  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1907.00681

## One-line
Selects a canonical solution to the non-unique $L^1$ Monge transport problem on $\mathbb{R}$ as the limit of strictly concave $L^p$ ($p \to 1^-$) optima, and characterizes it four equivalent ways.

## Key claim
For $\mu, \nu \in \mathcal{P}_1(\mathbb{R})$, four properties of $\pi \in \text{Marg}(\mu,\nu)$ are equivalent: (1) $\pi$ is a limit of $L^{p_n}$ optima with $p_n \to 1^-$; (2) $\pi$ minimizes $\int |y-x|^q\, d\pi$ over $\text{Marg}^*_1(\mu,\nu)$ for any $q<1$ (secondary problem); (3) $\pi$ is supported on a set of arches that are non-crossing, non-connecting, and co-oriented when nested; (4) $\pi$ is the explicitly-constructed "excursion coupling." Hence all three selection mechanisms yield the same unique plan.

## Method
Cyclical-monotonicity / swapping-lemma analysis applied to the strictly concave cost $|y-x|^p$, $p<1$: comparing the four-point configurations $xxyy$, $xyyx$, $xyxy$ shows arches cannot cross or connect; passing to $p \to 1^-$ adds the same-orientation rule for nested arches. The excursion coupling is built from the càdlàg signed cdf $F_\sigma = F_\mu - F_\nu$ using Bertoin–Yor's generalized Banach indicatrix to enumerate level-set crossings $\{x : F_\sigma(x)=h\}$ and pair consecutive ones as transport routes.

## Result
The excursion coupling is shown to exist, be unique, and admit the explicit construction via $F_\sigma$ level-sets (Theorem 1.1). It is the $p \to 1^-$ counterpart of the quantile (monotone) coupling that arises as $p \to 1^+$. Corollary 0.2 gives convergence of *every* sequence of $L^{p_n}$ optima (not just subsequences) and simultaneous minimization across all $q<1$ secondary costs.

## Why it matters here
General background; no direct arena tie — none of the 23 problems are 1D optimal transport. Tangentially useful as a worked example of *selection-by-limit*: when a primal problem (here $L^1$) has a non-unique solution set, perturbing with a strictly concave penalty and taking the limit picks out a canonical element. This pattern could inform regularization choices for degenerate optima in autocorrelation / LP-bound problems where the solution set is a face rather than a vertex.

## Open questions / connections
- Conjecture (Remark 5.7): in Euclidean / geodesic spaces, the $L^{1-}$ limit transport disintegrates along transport rays as excursion couplings — extends Ambrosio–Pratelli's $L^{1+}$ result.
- Conjecture (Remark 5.4): for $\mu, \nu$ with $X \le Y$ constraint, excursion coupling minimizes $\mathbb{E}(Y-X)^p$ for all $p \in (0,1)$ simultaneously — connects to Last–Mörters–Thorisson Brownian-shift problem.
- Conjecture (Remark 5.8): the quotient measure on the tree associated to $F_\sigma^*$ is always the 1-dim Hausdorff (length) measure.

## Key terms
optimal transport, Monge problem, Kantorovich, $L^p$ cost, strictly concave cost, excursion coupling, quantile coupling, monotone rearrangement, cyclical monotonicity, swapping lemma, Bertoin-Yor, Banach indicatrix, Gangbo-McCann, McCann, secondary transport problem, transport rays, càdlàg, bounded variation
