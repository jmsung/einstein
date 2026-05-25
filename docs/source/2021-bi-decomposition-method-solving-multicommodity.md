---
type: source
kind: paper
title: A decomposition method for solving multicommodity network equilibria
authors: Minh N. Bùi
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.03339
source_local: ../raw/2021-bi-decomposition-method-solving-multicommodity.pdf
topic: general-knowledge
cites:
---

# A decomposition method for solving multicommodity network equilibria

**Authors:** Minh N. Bùi  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.03339

## One-line
A block-iterative primal-dual splitting algorithm for Rockafellar's multicommodity network equilibrium problem that activates each maximally monotone operator separately via its resolvent.

## Key claim
For a network $(N, A, \vartheta)$ with commodity set $C$ and the flow-tension/divergence-potential inclusion system $\Delta_j v^* \in Q_j x_j + R_j x_j$ and $\operatorname{div}_i x \in S_i^{-1} v_i^*$, Proposition 4 gives an iteration whose iterates $((x_{j,n})_{j\in A}, (v_{i,n}^*)_{i\in N})$ converge to a solution of (1.6) under only maximal monotonicity (no Lipschitz/cocoercivity), with full splitting of $(Q_j)$, $(R_j)$, $(S_i)$ and asynchronous block activation under the sweeping condition $\bigcup_{k=n}^{n+T} A_k = A$, $\bigcup_{k=n}^{n+T} N_k = N$.

## Method
Reformulates (1.6) as the multivariate monotone inclusion (2.3) via dual variable $x^* \in X$, then instantiates the Combettes–Eckstein asynchronous block-iterative primal-dual decomposition framework [6, Algorithm 12] with $I = A$, $K = A \cup N$, signed incidence weights $\varepsilon_{i,j} \in \{-1, 0, 1\}$ encoding divergence/tension. Resolvents $J_{\gamma_j Q_j}, J_{\mu_j R_j}, J_{\sigma_i S_i}$ are computed independently per arc/node; convergence follows from [6, Theorem 13]. Worked resolvent formulas are given for separable flows, BPR, logarithmic, TRC, and exponential capacity operators (some involve the Lambert $W$-function).

## Result
Establishes weak convergence of the full iteration (2.2) to a primal-dual solution of (1.6) without strong-monotonicity or smoothness hypotheses, improving over: [5] (must activate all operators each iteration), [7, 11] (no deterministic block selection), [7] (requires inverting a linear operator on $\mathbb{R}^{MN}$ with $M = 2|A|+|N|$, $N = |C|$), and [1] (requires $\operatorname{dom} c_j = \mathbb{R}$ and Lipschitz $c_j$, which excludes BPR/log/TRC link-cost functions). Closed-form resolvents are derived for the four standard traffic-assignment cost models, including $J_{\gamma c}\xi = \omega - \gamma W(\omega \gamma^{-1} \exp(\theta - \xi/\gamma + \omega/\gamma))$ for the logarithmic capacity operator.

## Why it matters here
General background; no direct arena tie. This is convex/monotone-operator splitting for traffic/hydraulic/price equilibria on graphs, not sphere packing, autocorrelation, or extremal combinatorics; the only thin thread is shared machinery (proximal/resolvent calculus, Lambert $W$) with techniques the agent uses for smooth-min/max parameterizations and LP-bound polish.

## Open questions / connections
- Could asynchronous block-iterative resolvent splitting accelerate large per-arc subproblems in flow-based LP relaxations (e.g., LP duality cycles in $\ell_2$/$\ell_\infty$ optimization) where current solvers activate all dual blocks each iteration?
- Resolvents of $Q_j + R_j$ are not expressible from $J_{Q_j}, J_{R_j}$ in general (Remark 5(i)) — generic dead-end pattern for proximal compositions worth recording.
- Extends the Combettes–Eckstein 2018 framework [6] and Rockafellar's 1995 equilibrium model [13]; orthogonal to Douglas–Rachford [9, 10] which needs polyhedral projections without closed form.

## Key terms
maximally monotone operator, resolvent splitting, primal-dual decomposition, multicommodity network flow, network equilibrium, block-iterative algorithm, Combettes-Eckstein, Rockafellar, traffic assignment, Bureau of Public Roads cost, Lambert W function, divergence-potential
