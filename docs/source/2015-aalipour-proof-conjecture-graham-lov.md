---
type: source
kind: paper
title: Proof of a conjecture of Graham and Lov\'asz concerning unimodality of coefficients of the distance characteristic polynomial of a tree
authors: G. Aalipour, A. Abiad, Zhanar Berikkyzy, L. Hogben, Franklin Kenter, J. Lin, Michael Tait
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.02341
source_local: ../raw/2015-aalipour-proof-conjecture-graham-lov.pdf
topic: general-knowledge
cites:
---

# Proof of a conjecture of Graham and Lov\'asz concerning unimodality of coefficients of the distance characteristic polynomial of a tree

**Authors:** G. Aalipour, A. Abiad, Zhanar Berikkyzy, L. Hogben, Franklin Kenter, J. Lin, Michael Tait  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.02341

## One-line
Proves the 1978 Graham–Lovász conjecture that the normalized coefficients of the distance characteristic polynomial of a tree form a unimodal (in fact log-concave) sequence, and bounds where the peak sits.

## Key claim
For every tree $T$ of order $n$, the sequence $d_0(T),\ldots,d_{n-2}(T)$ with $d_k(T) = |\delta_k(T)|/2^{n-k-2}$ is log-concave and unimodal; its peak index lies in $[\lceil (n-2)/(1+d)\rceil,\ \lfloor 2n/3\rfloor]$ where $d = \mathrm{diam}(T)$.

## Method
Uses Newton's inequalities for real-rooted polynomials: since $D(T)$ is a real symmetric matrix, $p_{D(T)}(x)$ is real-rooted, which gives $a_j^2\binom{n}{j}^{-2} \ge a_{j-1}a_{j+1}\binom{n}{j-1}^{-1}\binom{n}{j+1}^{-1}$, hence log-concavity. Combined with Graham–Lovász's sign fact $(-1)^{n-1}\delta_k(T) > 0$, log-concavity plus positivity gives unimodality. Peak-location bounds come from explicit ratio estimates $d_1/d_0$ (via Edelberg–Garey–Graham's count of $P_3$ subtrees) and $d_{n-3}/d_{n-2} < \tfrac{1}{3}nd$ (via traces $\mathrm{tr}(D^2),\mathrm{tr}(D^3)$ and the row-sum bound $\lambda_{\max}\le nd$).

## Result
Upper bound: peak $\le \tfrac{2-\rho}{3-\rho}n$ where $\rho = N_{P_3}(T)/\binom{n-1}{2}$ is the fraction of length-2 paths relative to a star; $\rho=0$ gives the universal $2n/3$ bound, $\rho=1$ (star) recovers $n/2$. Lower bound: peak $\ge (n-2)/(1+d)$. Counterexample (Heawood graph) shows the tree hypothesis is essential — for non-trees, coefficients can mix signs and unimodality fails.

## Why it matters here
General background; no direct arena tie — distance-matrix spectral combinatorics is adjacent to the agent's discrete-geometry / extremal-graph problems but doesn't directly inform any of the 23 Einstein problems. Possible peripheral use: the **real-rooted ⇒ log-concave ⇒ unimodal** chain (Newton's inequalities) is a generic tool that could show up in autocorrelation-coefficient or LP-bound dual-sequence analyses.

## Open questions / connections
- Tighten Collins–Shor: is the true peak always in $[n/2,\ \lceil n - \sqrt{n/5}\rceil]$? (verified by Sage for $n\le 20$; this paper proves only $[n/(1+d),\ 2n/3]$).
- Extends Collins (1989) which handled only stars and paths; extends Graham–Lovász (1978) and Edelberg–Garey–Graham (1976) on distance matrices of trees.
- For graphs $G$ that are not trees, characterize when $\{|\delta_k(G)|\}$ retains unimodality — Heawood shows it can fail.

## Key terms
distance matrix, distance characteristic polynomial, unimodal sequence, log-concave sequence, Newton's inequalities, real-rooted polynomial, Graham-Lovász conjecture, Collins-Shor conjecture, tree, Heawood graph, peak location, $P_3$ subtree count
