---
type: source
kind: paper
title: Fast Algorithms for Online Stochastic Convex Programming
authors: Shipra Agrawal, Nikhil R. Devanur
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1410.7596
source_local: ../raw/2014-agrawal-fast-algorithms-online-stochastic.pdf
topic: general-knowledge
cites:
---

# Fast Algorithms for Online Stochastic Convex Programming

**Authors:** Shipra Agrawal, Nikhil R. Devanur  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1410.7596

## One-line
A fast primal-dual algorithm for online stochastic convex programming — concave objective $f$ on the average vector $\bar v^\dagger$ subject to a convex feasibility set $S$ — with optimal regret in both the i.i.d. and random-permutation input models.

## Key claim
Algorithm 5.1 achieves $\mathbb{E}[\text{avg-regret}_1(T)] = (Z+L)\cdot O(\sqrt{C/T})$ on the objective and $\mathbb{E}[\text{avg-regret}_2(T)] = O(\sqrt{C/T})$ on the constraint distance $d(\bar v^\dagger, S)$, with $C = d\log d$ (Euclidean) or $C = \log d$ ($L_\infty$); for online stochastic packing, Algorithm 6.1 attains competitive ratio $1 - O(\epsilon)$ whenever $\min\{B, \text{OPT}/T\} \geq \log(d)/\epsilon^2$, using only a single sample LP.

## Method
Fenchel-duality "linearization": rewrite $d(x,S) = \max_{\|\theta\|_*\leq 1}\{\theta\cdot x - h_S(\theta)\}$ and similarly for $-f$ via $f^*$, turning the constrained concave problem into a saddle point. Dual variables $\theta_t, \phi_t$ are produced by black-box online convex optimization / online mirror descent / multiplicative weights with regret $R(T)=O(L\sqrt{dT})$ or $O(L\sqrt{\log(d) T})$, while the primal step solves the now-linear per-step subproblem $\arg\min_{v\in A_t}\theta_t\cdot v$. A doubling-phase scheme estimates the problem-dependent tradeoff parameter $Z$ (the optimal dual on the feasibility constraint) from a growing sample of past observations.

## Result
Regret bounds are optimal (matching the Agrawal–Devanur–Hayes [3] lower bound for online packing) and hold in the strictly stronger random-permutation model, not just i.i.d. The proof formalizes the "sampling without replacement vs. with replacement" intuition by showing the gap between RP and IID contributes only an $O(\|1_d\|\sqrt{s T \log d})$ concentration term. For online packing, the algorithm needs to solve only one LP total (vs. DJSW solving an LP periodically and Kesselheim et al. solving one per step), making it both fast and RP-optimal.

## Why it matters here
General background; no direct arena tie. The Fenchel-conjugate / strong-convexity-smoothness duality (Lemmas 3.1–3.2) and multiplicative-weights regret bounds are reusable scaffolding for any online or dual-driven optimizer the agent might build, but no Einstein Arena problem currently calls for stochastic packing or online ad allocation.

## Open questions / connections
- Whether the extra $\sqrt{\log T}$ factor in high-probability bounds can be removed in the general CP case, as Gupta–Molinaro [26] did for online linear programming.
- Extension to Bandits-with-Knapsacks-style explore/exploit settings (Agrawal–Devanur [4]) where arms persist across rounds — the present problem has independent per-step option sets.
- Connection to Blackwell approachability [1, 9]: both use online learning as a sub-routine on the dual, suggesting a unified primal-dual approachability framework.

## Key terms
online stochastic convex programming, Fenchel duality, primal-dual algorithm, online mirror descent, multiplicative weights update, random permutation model, i.i.d. model, online packing LP, regret bound, strong convexity smoothness duality, Lipschitz constant, competitive ratio, Agrawal, Devanur
