---
type: source
kind: paper
title: The K-moment problem for continuous linear functionals
authors: J. Lasserre
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1102.5763
source_local: ../raw/2011-lasserre-k-moment-problem-continuous-linear.pdf
topic: general-knowledge
cites:
---

# The K-moment problem for continuous linear functionals

**Authors:** J. Lasserre  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1102.5763

## One-line
Solves the $K$-moment problem on non-compact basic closed semialgebraic sets $K \subseteq \mathbb{R}^n$ by switching from the finest locally convex topology to a weighted $\ell_1$-norm $\ell_w$ on $\mathbb{R}[x]$, under which preorderings and quadratic modules become dense in $\mathrm{Psd}(K)$.

## Key claim
With weights $w_\alpha := (2\lceil |\alpha|/2 \rceil)!$, the $\ell_w$-closures of the preordering $P(g)$ and quadratic module $Q(g)$ both equal $\mathrm{Psd}(K)$, and an $\ell_w$-continuous linear functional $L_y$ is a $K$-moment functional iff $L_y(h^2 g_j) \geq 0$ for all $h, j$ and $|y_\alpha| \leq M w_\alpha$ for some $M$.

## Method
Reformulates projection onto truncated cones $P_d(g), Q_d(g)$ as a semidefinite program; uses Hahn–Banach separation in the $\ell_w$-Banach-space setting together with Carleman's condition (which holds automatically because the weights $(2k)!$ enforce determinacy) to recover a representing measure. A preliminary theorem of independent interest: for $\mu$ with sub-factorial-growth moments, $f \geq 0$ on $\mathrm{supp}\,\mu$ iff $\int h^2 f \, d\mu \geq 0$ for all $h \in \mathbb{R}[x]$, iff localizing matrices $M_d(fy) \succeq 0$ for all $d$.

## Result
Explicit canonical $\ell_w$-projection $g_f^{P_w}(x) = f(x) + \lambda_0 + \sum_{i=1}^n \sum_{k=1}^d \lambda_{ik}\, x_i^{2k}/(2k)!$ with $\lambda \geq 0$ from an SDP — the support is independent of $K$ and of $d$, with $\|g_f\|_0 \leq \|f\|_0 + n + 1$. Yields a non-compact Positivstellensatz: $f \geq 0$ on $K$ iff for every $\epsilon > 0$ there exists $d$ with $f + \epsilon(1 + \sum_i \sum_{k=1}^d x_i^{2k}/(2k)!) \in P(g)$. Also gives a clean description of the sequential closure $P(g)^\ddagger = Q(g)^\ddagger$ via the simple perturbation $q = 1 + \sum_i x_i^{2d}$.

## Why it matters here
General background; no direct arena tie. Touches the SDP / sum-of-squares / Lasserre-hierarchy toolkit that underlies LP/SDP bounds for sphere packing (Cohn–Elkies) and autocorrelation problems, but this paper's contribution is the topology/closure question, not a constructive bound — it would inform a project that needed to certify non-negativity over a non-compact semialgebraic set without Putinar's Archimedean assumption.

## Open questions / connections
- Extends Schmüdgen (1991) and Putinar (1993) Positivstellensätze to the non-compact case via a weighted-norm topology, sidestepping Scheiderer's (2009) negative results.
- The canonical sparse perturbation $1 + \sum x_i^{2d}$ refines [Kuhlmann–Marshall–Schwartz 2005] and [Lasserre–Netzer 2006]; can this be pushed further to give tighter quantitative degree bounds for specific $K$?
- Practical: the perturbation requires $\epsilon \to 0$ and $d \to \infty$ jointly — what is the convergence rate of $p^{d}_w$ for structured $K$ (boxes, balls, simplices)?

## Key terms
K-moment problem, Positivstellensatz, preordering, quadratic module, sum of squares, semidefinite programming, Lasserre hierarchy, Carleman condition, weighted $\ell_1$-norm, Hahn–Banach separation, Schmüdgen, Putinar, basic semialgebraic set, localizing matrix, non-compact semialgebraic
