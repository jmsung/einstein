---
type: source
kind: paper
title: Replica symmetry in upper tails of mean-field hypergraphs
authors: Somabha Mukherjee, B. Bhattacharya
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1812.09841
source_local: ../raw/2018-mukherjee-replica-symmetry-upper-tails.pdf
topic: general-knowledge
cites:
---

# Replica symmetry in upper tails of mean-field hypergraphs

**Authors:** Somabha Mukherjee, B. Bhattacharya  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1812.09841

## One-line
Identifies the universal region of replica symmetry for the mean-field upper-tail variational problem counting edges in a $p$-percolated regular $s$-uniform hypergraph, and extends the analysis to subgraph counts in vertex-percolated dense graphs via graphon limits.

## Key claim
For any sequence of regular $s$-uniform hypergraphs $\{H_n\}$, the upper-tail rate $\varphi_{H_n}(r,p) = I_p(r)$ (replica symmetric, uniquely minimized by the constant $r$) iff $(r^s, I_p(r))$ lies on the convex minorant of $x \mapsto I_p(x^{1/s})$; this region $C_s$ depends only on $s$ and is tight across the class of regular $s$-uniform hypergraphs.

## Method
Variational analysis of the mean-field entropic optimization $\inf \frac{1}{|V|} \sum I_p(x_v)$ subject to $t(H,x) \ge r^s |E(H)|$. The replica-symmetric direction uses a degree-counting lemma ($t(H,x) \le \frac{d}{s} \sum x_v^s$ for $d$-regular $H$) plus Jensen's inequality against the convex minorant of $I_p(x^{1/s})$. Symmetry breaking is shown by constructing disjoint unions of complete $s$-uniform hypergraphs with two-level vertex weights. For dense-graph subgraph counts, the variational problem is shown to converge (via cut-metric / graphon limits) to a functional optimization over $h:[0,1]\to[0,1]$.

## Result
Theorem 1.1 gives the tight universal replica-symmetry region $C_s$ for regular $s$-uniform hypergraphs and the corresponding tail asymptotic $\frac{1}{|V(H_n)|}\log P(T_p(H_n) \ge r^s \mathbb{E}[T_p(H_n)]) \to -I_p(r)$. Theorem 1.2 gives the graphon-limit variational form $\psi_2(H,W,r,p) = \inf_h \int_0^1 I_p(h) \, dx$ subject to $t(H,W,h) \ge r^{|V(H)|} t(H,W)$, yielding the exact Bahadur slope of the subgraph-sampling estimator. Appendix A proves a simpler mean-field condition: $|E(H_n)| \gg |V(H_n)|^{s-1}$ and $\Delta_1(H_n) = O(|E(H_n)|/|V(H_n)|)$.

## Why it matters here
General background; no direct arena tie — the 23 Einstein Arena problems are deterministic extremal/optimization tasks, not random-graph large-deviation problems. Closest indirect relevance is methodological: the convex-minorant criterion for when a sum-separable entropic functional is minimized by the constant function is a clean template for symmetry-vs-symmetry-breaking analyses (cf. equioscillation / basin rigidity findings).

## Open questions / connections
- Tight regular construction realizing $R(H) = C_s$ for arbitrary $(p,r)$ off the concave region remains open (Example 1 only covers the concave part).
- Extends Lubetzky–Zhao [23] from $F$-counting (2-uniform) to general $s$-uniform regular hypergraphs; sharpens $R(H_n(F)) \supseteq C_{|E(F)|}$ vs prior $C_{\Delta(F)}$.
- Sparse-$p$ regime (e.g., Cook–Dembo, Augeri for cycle counts in $G(n,p)$) requires different machinery — variational structure changes.

## Key terms
mean-field variational problem, replica symmetry, symmetry breaking, upper tail large deviations, regular hypergraph, convex minorant, relative entropy, graphon, cut-metric, Bahadur slope, Erdős–Rényi subgraph counts, nonlinear large deviations
