---
type: source
kind: paper
title: Large deviations of subgraph counts for sparse Erdős–Rényi graphs
authors: Nicholas A. Cook, A. Dembo
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1809.11148
source_local: ../raw/2018-cook-large-deviations-subgraph-counts.pdf
topic: general-knowledge
cites:
---

# Large deviations of subgraph counts for sparse Erdős–Rényi graphs

**Authors:** Nicholas A. Cook, A. Dembo  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1809.11148

## One-line
Establishes the sharp exponential rate for the probability that a sparse Erdős–Rényi graph $G(n,p)$ contains $(1+u)$ times the expected number of copies of a fixed subgraph $H$, valid for $p \gg n^{-1/(2\Delta)}$.

## Key claim
For any fixed simple $H$ and $u>0$, $-\log P(\hom(H,G) \geq (1+u)n^{v(H)}p^{e(H)}) = (1+o(1))\,\varphi_{n,p}(H,u)$ whenever $n^{-1}\log n \ll p^{2\Delta_\star(H)} \ll 1$, where $\Delta_\star(H) = \tfrac{1}{2}\max_{\{v_1,v_2\}\in E}(\deg_H(v_1)+\deg_H(v_2))$ and $\varphi_{n,p}$ is the entropic variational problem (1.13). For cycles $C_\ell$ this extends to $p \gg n^{-1/2}$ (essentially optimal), and $\mathrm{UT}_{n,p}(C_\ell,u) = (c_\ell(u)+o(1))n^2 p^2 \log(1/p)$ with $c_\ell(u) = \min(\tfrac12 \theta_\ell(u), \tfrac12 u^{2/\ell})$.

## Method
Quantitative versions of Szemerédi's regularity lemma and the counting lemma tailored to the large-deviations regime: cover the space of adjacency matrices by convex sets indexed by low-rank approximants (spectral truncation $X = X_{\leq k} + X_{>k}$), with $X_{>k}$ controlled in Schatten-$\ell$ norm. Combine with a covering/union-bound transfer from entropic variational problem $\varphi_p$ to tail probability, plus eigenvalue concentration for the "exceptional" set. Lower tails for Sidorenko graphs use a "uniform edge thinning" planted graphon $r J_n$ with $r=q/p$.

## Result
Three concrete improvements over Chatterjee–Dembo [CD16] $\kappa = c/(\Delta|E|)$: (1) general $H$: $\kappa(H) = 1/(2\Delta)$ — within a factor 2 of conjectured $1/\Delta$; (2) cycles: $\kappa(C_\ell) = 1/2$ for $\ell \geq 4$ (optimal), $\kappa(C_3)=1/3$; (3) sharp upper tail for Schatten norms $\|A\|_{S_\alpha}$ ($\alpha>2$) and operator norm $\|A\|_{\mathrm{op}}$, $\|A-p\mathbf{1}\mathbf{1}^T\|_{\mathrm{op}}$; (4) sharp lower tail $P(\hom(H,G)\leq q^{e(H)}n^{v(H)}) \asymp \exp(-\binom{n}{2}I_p(q))$ for any Sidorenko $H$ when $p \gg n^{-1/(2\Delta_\star-1)}$. The upper-tail rate is dominated by **planted "clique" or "hub"** events — broken-symmetry — while lower tails arise from **uniform edge-density depression** (preserved symmetry).

## Why it matters here
General background; no direct arena tie. Useful methodology for any arena problem framed as "rare configurations in sparse random structures" — closest hooks are extremal graph theory (P-class graph density / Turán-type) and the LP / entropy variational machinery shared with Cohn–Elkies-style problems. The clique-vs-hub dichotomy and entropic variational characterization $\varphi_p(h,t) = \inf\{I_p(x): h(x)\geq t\}$ may inform any future "rare event in random combinatorial objects" finding.

## Open questions / connections
- Can $\kappa(H) = 1/\Delta$ (conjectured optimum, Chatterjee Open Problem 4) be reached for general $H$? Subsequent work [HMS], [BB] achieves this for *regular* $H$ via different methods.
- Solution of variational problem $\varphi_p(\|\cdot\|_{S_\alpha}, nq)$ for general $\alpha$; only $\alpha=\infty$ (operator norm) was resolved in [BG].
- Lower-tail analog of broken-symmetry: are there functionals where the lower tail is dominated by a planted *anti-structure* rather than uniform thinning?
- Extends [CD16,Eld18] (nonlinear large deviations); refuted in part by [SW19] (DeMarco–Kahn conjecture counterexample).

## Key terms
large deviations, upper tail problem, Erdős–Rényi G(n,p), homomorphism counts, subgraph counts, Szemerédi regularity lemma, counting lemma, sparse random graphs, Sidorenko conjecture, Schatten norm, entropic variational problem, Kullback–Leibler divergence, clique planting, hub event, broken symmetry, Chatterjee–Varadhan, graphon, maximum degree, cycle counts, independence polynomial, Lubetzky–Zhao, nonlinear large deviations, spectral truncation, operator norm tail
