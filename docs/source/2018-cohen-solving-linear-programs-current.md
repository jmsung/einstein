---
type: source
kind: paper
title: Solving linear programs in the current matrix multiplication time
authors: Michael B. Cohen, Y. Lee, Zhao Song
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1810.07896
source_local: ../raw/2018-cohen-solving-linear-programs-current.pdf
topic: general-knowledge
cites:
---

# Solving linear programs in the current matrix multiplication time

**Authors:** Michael B. Cohen, Y. Lee, Zhao Song  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1810.07896

## One-line
Solves dense LPs $\min_{Ax=b, x\ge 0} c^\top x$ in $O^*(n^\omega \log(n/\delta))$ time — matching the cost of solving a single linear system — by combining a stochastic central-path method with sub-quadratic projection-matrix maintenance.

## Key claim
Total runtime $O^*((n^\omega + n^{2.5-\alpha/2} + n^{2+1/6})\log(n/\delta))$, where $\omega$ is the matrix-multiplication exponent and $\alpha$ is the dual exponent of rectangular matrix multiplication. For current $\omega \sim 2.37$, $\alpha \sim 0.31$ this collapses to $O^*(n^\omega \log(n/\delta))$; if $\omega=2$ it becomes $O^*(n^{2+1/6}\log(n/\delta))$. This is the first improvement over Vaidya's $O^*(n^{2.5})$ from 1989.

## Method
Two new ingredients on top of the short-step primal–dual interior-point method. (1) **Stochastic central path:** at each of the $O^*(\sqrt n)$ steps move along a $k$-sparse random direction $\widetilde{\delta_\mu}$ that is unbiased ($\mathbb{E}[\widetilde{\delta_\mu}]=\delta_\mu$) with controlled variance (Eq. 6), and bound $x_i s_i$ via a soft-max potential $\sum_i \cosh(\lambda(x_i s_i/t - 1))$ rather than $\ell_2$-closeness. (2) **Lazy projection maintenance:** keep an approximate $P = \sqrt{W}A^\top(AWA^\top)^{-1}A\sqrt{W}$ with $W=\mathrm{diag}(x/s)$; use the Woodbury identity to patch small changes, and trigger a batched rectangular-matrix-multiply rebuild only when $\ge n^\alpha$ coordinates of $w$ drift, scheduled via a "soft threshold" $|y_{\pi(1.5k)}| < (1-1/\log n)|y_{\pi(k)}|$ instead of a hard cutoff.

## Result
Theorem 2.1: for any $0<\delta\le 1$, the algorithm returns $x\ge 0$ with $c^\top x \le \min c^\top x + \delta\cdot \|c\|_\infty R$ and $\|Ax-b\|_1 \le \delta\cdot(R\sum_{i,j}|A_{i,j}|+\|b\|_1)$ in expected time $(n^{\omega+o(1)} + n^{2.5-\alpha/2+o(1)} + n^{2+1/6+o(1)})\log(n/\delta)$. The bound holds for any rectangular MM algorithm satisfying $\omega \le 3-\alpha$ (Lemma A.4); Strassen alone gives $\sim n^{2.807}$. Per-iteration amortized cost is $\sim n^{\omega-1/2}$, with total coordinate updates $O^*(n)$ — nearly optimal.

## Why it matters here
General background; no direct arena tie. Useful as a reference ceiling for any large dense LP/SDP step inside the agent's compute-router decisions (relates to LP/IPM rows of the routing matrix in `.claude/rules/compute-router.md` and the SDP/LP techniques touched in P1's SDP-relaxation dead-end). Sets the modern asymptotic for "how cheap can the inner LP solve get" before RAM-bound regimes force Modal.

## Open questions / connections
- Can the additive $n^{2+1/6}$ term be reduced further? [JSWZ20] already pushes it to $2+1/18$; the $\omega=2$ barrier remains open.
- Can the doubling-trick $\log n$ overhead be removed to get $O(T(n)\log(n/\delta))$ exactly (authors flag this explicitly)?
- Generalizations already in flight: ERM [LSZ19], cutting plane [JLSW20], SDP [JKL+20], deep-net training [BPSW20] — i.e. the stochastic-IPM + lazy-projection template transfers beyond LP.
- Connects to inverse-maintenance / leverage-score sampling [SS11, CW13, NN13, Sar06] and to Laplacian-solver data-structure ideas [KOSZ13].

## Key terms
linear programming, interior point method, central path, stochastic central path, primal-dual, short-step method, projection maintenance, Woodbury identity, matrix multiplication exponent omega, dual exponent alpha, rectangular matrix multiplication, leverage score sampling, soft-max potential, inverse maintenance, Vaidya, Renegar, Karmarkar, Cohen-Lee-Song
