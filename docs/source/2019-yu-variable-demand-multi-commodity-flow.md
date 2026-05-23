---
type: source
kind: paper
title: Variable demand and multi-commodity flow in Markovian network equilibrium
authors: Yue Yu, Daniel J. Calderone, Sarah H. Q. Li, L. Ratliff, Behccet Accikmecse
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1901.08731
source_local: ../raw/2019-yu-variable-demand-multi-commodity-flow.pdf
topic: general-knowledge
cites:
---

# Variable demand and multi-commodity flow in Markovian network equilibrium

**Authors:** Yue Yu, Daniel J. Calderone, Sarah H. Q. Li, L. Ratliff, Behccet Accikmecse  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1901.08731

## One-line
Extends Markovian network equilibrium (MDP routing games) to handle variable demand (a quitting option) and multi-commodity flow (heterogeneous ending times), with dynamic-programming-based Frank-Wolfe and subgradient algorithms that outperform Mosek.

## Key claim
Both extended equilibria can be characterized as solutions of convex primal-dual pairs satisfying a Wardrop-type principle, and solved in $O(\sigma T S^2 A/\epsilon)$ arithmetic operations (single-commodity) or $O(\sigma T^2 S^2 A/\epsilon)$ (multi-commodity), where $\sigma$ is transition-kernel sparsity, beating Mosek by 1–2 orders of magnitude at 0.5% relative error.

## Method
Each player solves a $T$-horizon MDP rather than a shortest path; the equilibrium is cast as a convex primal (flow) / dual (potential) pair on a $T$-layered Markovian network. Linearizing the convex objective reduces each Frank-Wolfe iteration to a standard MDP solvable in closed form by backward + forward induction (Algorithms 1–2). Convergence follows from Lipschitz-gradient / strong-convexity bounds on the unlinearized objective.

## Result
Theorems 1–2 establish Wardrop-equilibrium KKT characterizations: at equilibrium, only minimum-expected-cost actions carry flow, and the quitting threshold matches $v_{ts} = \psi_{ts}(z_{ts})$. Theorems 3–4 give explicit $O(1/\epsilon)$ iteration complexity for Frank-Wolfe (primal) and projected subgradient (dual). Numerical experiments on $T=A=10$, $S \in [20,200]$ show Frank-Wolfe ~$100\times$ faster than Mosek; subgradient ~$10\times$ faster.

## Why it matters here
General background; no direct arena tie. The MDP-routing-game / mean-field-on-graph framing and the linearization-via-DP trick could remotely inform any arena problem cast as an equilibrium-on-network (e.g., flow-style LP relaxations), but none of the 23 Einstein Arena problems is a transportation/routing equilibrium.

## Open questions / connections
- Stochastic perceived costs (SUE-style) on top of stochastic transitions — unified model still open.
- Allowing players to revise their ending time and recompute equilibrium periodically (dynamic horizon).
- Connection to discrete mean-field games on graphs (Gomes, Guéant, Tanaka) — convergence rates, congestion effects.

## Key terms
Markovian network equilibrium, Wardrop equilibrium, Markov decision process, multi-commodity flow, variable demand, Frank-Wolfe method, projected subgradient, dynamic programming, mean-field game, routing games, ride-sharing, convex optimization
