---
type: source
kind: paper
title: Fourier Analysis on Finite Groups and the Lovász ϑ-Number of Cayley Graphs
authors: Evan DeCorte, David de Laat, F. Vallentin
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1307.5703
source_local: ../raw/2013-decorte-fourier-analysis-finite-groups.pdf
topic: general-knowledge
cites:
---

# Fourier Analysis on Finite Groups and the Lovász ϑ-Number of Cayley Graphs

**Authors:** Evan DeCorte, David de Laat, F. Vallentin  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1307.5703

## One-line
Reduces the Lovász $\vartheta$-number of a Cayley graph to a small SDP (or LP, when the connection set is conjugation-closed) over irreducible representations of the group, via Fourier analysis on finite groups.

## Key claim
For $G = \mathrm{Cay}(\Gamma, X)$, $\vartheta(G)$ equals the optimum of a block-diagonal SDP with one PSD block $A_\pi \in S^{d_\pi}_{\succeq 0}$ per irreducible representation $\pi \in \hat\Gamma$; if $X$ is closed under conjugation, this collapses to a character-only LP: maximize $a_1$ subject to $a_\pi \ge 0$, $\sum_\pi d_\pi^2 a_\pi = |\Gamma|$, and $\sum_\pi d_\pi a_\pi \chi_\pi(x) = 0$ for $x \in X$.

## Method
Apply Bochner's theorem for finite groups (positive-type $f$ $\iff$ $\hat f(\pi) \succeq 0$ for all $\pi$) to the function-on-$\Gamma$ reformulation of $\vartheta$, replacing the $|\Gamma| \times |\Gamma|$ matrix variable with block matrices indexed by irreps. When $X$ is conjugation-closed, Schur's lemma forces each block to be a scalar multiple of identity, collapsing the SDP to an LP in the character table. The constraints reduce further to one $C_x$ per conjugacy class.

## Result
Two applications: (i) for $k$-intersecting permutations in $S_n$ (Ellis–Friedgut–Pilpel), the LP verifies the EFP conjecture $|A| = (n-k)!$ for $n \ge 2k+1$ on small $(n,k)$ via rigorous rational arithmetic (gap + lrs), and identifies cases where $\vartheta$ is not tight; (ii) a $q$-analog for $k$-intersecting families in $GL(n,\mathbb F_q)$ where $\vartheta(G_{q,n,1}) = \prod_{i=1}^{n-1}(q^n - q^i)$ numerically, conjectured tight for all $(n,q)$, and an EKR-type conjecture for $k>1$.

## Why it matters here
General background on symmetry-reducing SDPs to LPs through representation theory — directly relevant to any Arena problem where the feasible set has a transitive group action (extremal-graph, combinatorial, kissing-number-on-finite-quotients, $q$-analog problems). Adds the conjugation-closed → LP shortcut not present in the existing Lovász-$\vartheta$ wiki content.

## Open questions / connections
- Quantify $n_0(k)$ in Ellis–Friedgut–Pilpel; $\vartheta$ alone is not tight for some small $(n,k)$, suggesting need for stronger hierarchies (Lasserre, SOS).
- Resolve Conjecture 1 ($\vartheta = \alpha$ for $G_{q,n,1}$) and Conjecture 2 (EKR-type bound for $k$-intersecting invertible matrices) — currently only numerical evidence.
- Extends naturally to vertex-transitive graphs via the blow-up construction (Theorem 6): $\alpha(G) = (|V|/|\Gamma|)\,\alpha(\mathrm{Cay}(\Gamma,X))$.

## Key terms
Lovász theta number, Cayley graph, finite Fourier analysis, Bochner's theorem, Schur orthogonality, irreducible representation, character table, semidefinite programming, linear programming relaxation, Erdős-Ko-Rado, k-intersecting permutations, symmetric group, GL(n,Fq), q-analog, vertex-transitive graph
