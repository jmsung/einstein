---
type: source
kind: paper
title: Maximizing Profit with Convex Costs in the Random-order Model
authors: Anupam Gupta, R. Mehta, M. Molinaro
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.08172
source_local: ../raw/2018-gupta-maximizing-profit-convex-costs.pdf
topic: general-knowledge
cites:
---

# Maximizing Profit with Convex Costs in the Random-order Model

**Authors:** Anupam Gupta, R. Mehta, M. Molinaro  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.08172

## One-line
Online algorithms in the random-order (secretary) model for picking items to maximize value minus a convex production cost over $d$ shared resources.

## Key claim
$O(d)$-competitive for the unconstrained supermodular-cost case, $O(d^2 \log\log\text{rank})$ for matroid-constrained separable costs, and $O(d^3 \log\log\text{rank})$ for matroid-constrained supermodular costs — improving Barman et al.'s $O(d^5\alpha)$ by a factor of $d^3$.

## Method
Convex (Fenchel) duality: write $g(z) = \max_\lambda(\langle\lambda,z\rangle - g^*(\lambda))$ and reduce the offline problem to a saddle-point in $(x,\lambda)$ where $\lambda^* = \nabla g(Sx^*)$ acts as a per-resource price classifier. Restrict candidate classifiers to a monotone 1-D curve $C \subset \mathbb{R}^d_+$ satisfying $g^*_i(\lambda_i) = g^*_j(\lambda_j)$ (balanced curve), then learn the right point on $C$ from a random sample $L$ of the items. A gradient-truncation trick makes the (possibly negative) profit submodular function non-negative monotone so black-box submodular-secretary algorithms apply.

## Result
For unconstrained supermodular $g$: randomized $O(d)$-competitive (Thm 1.1), matching offline $\Omega(d^{1-\varepsilon})$ hardness of $d$-dim knapsack. For matroid-constrained separable $g$: $O(d^2\alpha)$ where $\alpha = O(\log\log\text{rank})$ is the submodular-matroid-secretary ratio (Thm 1.2). A black-box reduction (Thm 6.1) lifts any $\beta$-approx for separable cost to $d(\beta+2ed)$-approx for supermodular cost via the inequality $g(y) \le \tfrac1d\sum_i g_i(d y_i)$.

## Why it matters here
General background; no direct arena tie. The duality framing (replace a hard convex objective by its linearization at the optimal dual price, then learn the price from a sample) is a clean template for any wiki technique page on online convex optimization or threshold/price-learning algorithms.

## Open questions / connections
- Can the matroid-constrained gap between separable and supermodular costs ($d^2$ vs $d^3$) be closed?
- Extends Blum–Gupta–Mansour–Sharma, Huang–Kim, Azar et al., and Barman–Umboh–Chawla–Malec by removing the separability / low-degree restriction on $g$.
- Bridges to Agrawal–Devanur's online packing LPs with large right-hand sides — when do random-order regret bounds replace explicit threshold construction?

## Key terms
convex duality, Fenchel conjugate, supermodular cost, separable cost, random-order model, secretary problem, matroid secretary, submodular maximization, threshold classifier, online packing, profit maximization, gradient truncation
