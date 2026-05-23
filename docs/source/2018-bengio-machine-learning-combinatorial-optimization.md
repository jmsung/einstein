---
type: source
kind: paper
title: "Machine Learning for Combinatorial Optimization: a Methodological Tour d'Horizon"
authors: Yoshua Bengio, Andrea Lodi, Antoine Prouvost
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1811.06128
source_local: ../raw/2018-bengio-machine-learning-combinatorial-optimization.pdf
topic: general-knowledge
cites:
---

# Machine Learning for Combinatorial Optimization: a Methodological Tour d'Horizon

**Authors:** Yoshua Bengio, Andrea Lodi, Antoine Prouvost  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1811.06128

## One-line
A methodological survey of how machine learning (especially deep RL and graph neural networks) can be embedded inside combinatorial optimization algorithms to replace handcrafted heuristics with learned policies tuned to a distribution of problem instances.

## Key claim
ML and CO should be integrated by treating optimization problems as data points drawn from an unknown distribution, and learning policies via either (a) imitation of an expert oracle or (b) reward-driven experience (RL); the latter can in principle outperform any expert, while exactness can be preserved if the ML component only chooses among already-valid algorithmic decisions (branching, cut selection, node selection, heuristic scheduling).

## Method
Taxonomic survey along two orthogonal axes: (1) *demonstration vs. experience* — supervised imitation of an oracle (e.g., strong branching) vs. reinforcement learning from a reward signal; (2) *ML/CO interplay* — end-to-end ML solvers, ML to configure/parameterize a CO algorithm, or repeated ML↔CO interaction inside branch-and-bound. Architectures discussed: MLPs, RNNs, attention/pointer networks, graph neural networks on bipartite variable–constraint graphs, Sinkhorn layers for permutation outputs.

## Result
No new theorem; the paper consolidates a methodology and identifies failure modes: imitation is bounded by the expert and suffers distribution shift (state distribution at test ≠ expert's); RL faces sparse-reward, exploration, and non-convergence issues; end-to-end ML heuristics give neither feasibility nor optimality guarantees, while ML-inside-B&B preserves exactness when all candidate decisions are valid. Highlights generalization, scaling beyond training sizes (e.g., TSP n=50→500 degrades), data generation, and state representation as the core open challenges.

## Why it matters here
General background; no direct arena tie — the Einstein Arena problems are continuous global optimization / extremal-geometry tasks, not MILP/CO. Relevant only as conceptual scaffolding for the JSAgent's own self-improvement loop (imitation-vs-experience framing, cycle-log as distribution-of-instances thinking, GNNs as a possible representation for graph-structured problems like Sidon sets or contact graphs).

## Open questions / connections
- Can the "policy learned on a distribution of instances" framing be repurposed for *parameter selection* across the 23 arena problems (e.g., learning when to switch optimizer / temperature schedule)?
- Are GNN representations of contact graphs / packing configurations useful priors for problems like P11 (Hardin–Sloane) or kissing-number variants?
- Imitation-then-RL ordering (AlphaGo-style) as a template for council-dispatch → execute → reward refinement.

## Key terms
machine learning, combinatorial optimization, branch and bound, MILP, reinforcement learning, imitation learning, graph neural networks, attention mechanism, pointer networks, traveling salesman problem, cutting planes, strong branching
