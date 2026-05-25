---
type: source
kind: paper
title: An $L^p$ theory of sparse graph convergence I: limits, sparse random graph models, and power law distributions
authors: Christian Borgs, Jennifer T. Chayes, Henry Cohn, Yufei Zhao
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1401.2906v4
source_local: ../raw/2014-borgs-theory-sparse-graph-convergence.pdf
topic: general-knowledge
cites: 
---

# An $L^p$ theory of sparse graph convergence I: limits, sparse random graph models, and power law distributions

**Authors:** Christian Borgs, Jennifer T. Chayes, Henry Cohn, Yufei Zhao  ·  **Year:** 2014  ·  **Source:** http://arxiv.org/abs/1401.2906v4

## One-line
Extends graphon limit theory from dense / $L^\infty$ graphs to sparse graphs with unbounded average degree and power-law degree distributions by replacing boundedness with $L^p$ upper regularity for $p>1$.

## Key claim
Every $C$-upper $L^p$ regular sequence of weighted graphs ($p>1$) has a subsequence whose normalized graphons $G_n/\|G_n\|_1$ converge in the cut metric to an $L^p$ graphon $W$ with $\|W\|_p \le C$; equivalently, the ball $B_{L^p}(C) = \{W : \|W\|_p \le C\}$ is compact under $\delta_\square$.

## Method
Replaces the Bollobás–Riordan "no dense spots" ($L^\infty$) hypothesis with the weaker partition-based condition that averaged-edge-density step-functions $W_{\mathcal P}$ have bounded $L^p$ norm. The proof combines (i) a new $L^p$ weak (Frieze–Kannan) regularity lemma derived by truncating $W$ at level $K$ and applying $L^2$ weak regularity to the truncation, with (ii) a martingale-convergence compactness argument in the $L^p$ ball. An $L^1$ analogue (Appendix C) uses uniform integrability ($K$-bounded tails) in place of the $L^p$ bound.

## Result
Three main theorems: (1) **Compactness** — $B_{L^p}(C)$ is compact under $\delta_\square$ for $p>1$ (Thm 2.13); (2) **Convergence characterization** — $L^p$ upper regular $\Leftrightarrow$ has cut-metric limit that is an $L^p$ graphon (Thm 2.8, Prop 2.10); (3) **Sparse $W$-random model** — for any $L^1$ graphon $W$ and edge-scale $\rho_n$ with $\rho_n \to 0$, $n\rho_n \to \infty$, the sparse random graph $G(n,W,\rho_n)$ satisfies $\rho_n^{-1}G(n,W,\rho_n) \to W$ in cut metric a.s. (Thm 2.14). Also: $L^p$ upper regularity forces unbounded average degree (App A); a counting lemma $|t(F,U)-t(F,W)| \le O(\varepsilon^{(p-\Delta)/(p-\Delta+m-1)})$ holds when $p > \Delta(F)$, and fails for $p \le \Delta$ (§8).

## Why it matters here
General background; no direct arena tie. Provides the right functional-analytic framework if any arena problem ever reduces to extremal questions on sparse / power-law graph ensembles (Sidon-like density questions, extremal subgraph counts with unbounded degree); the $L^p$-vs-degree counting-lemma threshold $p > \Delta$ is a clean reusable principle for sparse extremal arguments.

## Open questions / connections
- Counting lemmas for sparse pseudorandom graphs (Conlon–Fox–Zhao) extended to $L^p$ upper regular hosts — left explicitly open.
- Right convergence / quotient convergence for $L^p$ graphons — addressed in the companion paper (arXiv:1408.0744).
- Stronger ($L^p$ partition-norm) regularity lemma analogues beyond the weak / Frieze–Kannan form.
- Connection to statistical graphon estimation (Wolfe–Olhede) for networks with dense spots.

## Key terms
graphon, $L^p$ graphon, cut metric, cut norm, Frieze–Kannan weak regularity, Szemerédi regularity lemma, sparse graph convergence, Bollobás–Riordan, $L^p$ upper regularity, uniform integrability, $W$-random graph, power-law degree distribution, counting lemma, generalized Hölder inequality, martingale convergence
