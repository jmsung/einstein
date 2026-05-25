---
type: source
kind: paper
title: "Learning Combinatorial Optimization on Graphs: A Survey With Applications to Networking"
authors: N. Vesselinova, Rebecca Steinert, Daniel F. Pérez-Ramírez, Magnus Boman
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.11081
source_local: ../raw/2020-vesselinova-learning-combinatorial-optimization-graphs.pdf
topic: general-knowledge
cites:
---

# Learning Combinatorial Optimization on Graphs: A Survey With Applications to Networking

**Authors:** N. Vesselinova, Rebecca Steinert, Daniel F. Pérez-Ramírez, Magnus Boman  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.11081

## One-line
A survey of machine-learning approaches (graph neural networks, attention, deep reinforcement learning) for NP-hard combinatorial optimization problems formulated on graphs, with applications to telecommunications networking.

## Key claim
ML methods — particularly GNN encoders combined with pointer-network or attention decoders trained via supervised or RL objectives — can learn approximation heuristics for graph CO problems (TSP, VRP, MVC, MaxCut, MIS, SAT, GC) that generalize to unseen instances drawn from the same distribution, often matching or approaching specialized solvers (Concorde, Gurobi, CPLEX) without hand-engineered rules.

## Method
Synthesizes a taxonomy over (i) graph representation: graph embeddings, message-passing GNNs (Scarselli, GG-NN, MPNN, GAT), structure2vec; (ii) decoder/policy architecture: pointer networks (Vinyals), attention/Transformer (Bahdanau, Vaswani multi-head self-attention), seq2seq with LSTM; (iii) training signal: supervised learning on solved instances vs. deep RL (REINFORCE policy gradient, DQN/fitted-Q, A3C, AlphaGo-Zero-style MCTS). Models are categorized by problem class and evaluated against exact / approximation / metaheuristic baselines.

## Result
No new theorem; the survey compiles per-problem performance tables across TSP, VRP, MVC, MaxCut, MIS, MaxClique, MCP, GC, SAT, KP. Notes worst-case bounds for context: VC parametrized $O(1.2738^k + kn)$ (Chen et al.); MIS $O(1.1736^{|V|})$ (Xiao–Nagamochi); decision GC 4-colorability $O(1.7272^{|V|})$ (Fomin); KP exact $O(nW)$ DP. Concludes ML solvers trade theoretical guarantees for amortized inference speed and cross-instance generalization.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are continuous/analytic optimization (sphere packing, autocorrelation, kissing) rather than graph CO over discrete combinatorial structures, and the surveyed ML approaches (GNN+RL pointer decoders for TSP/MVC/SAT) are off-domain for the agent's current problem set. Possible tangential relevance: attention/Transformer machinery as a meta-architecture, and the methodological observation that learned heuristics generalize within a distribution but not across — analogous to per-problem specialization in the agent's council dispatch.

## Open questions / connections
- Can attention-based encoders learn structure for *continuous* extremal problems (e.g., point configurations on a sphere) rather than node-set selection on graphs?
- The survey's "learned heuristic generalizes to same-distribution instances" claim (Mittal et al., Dai et al.) parallels the wiki's basin-rigidity / parameterization-selection question — does learning the *symmetry class* of optima transfer across problem sizes?
- Extends Smith 1999 review of NN-for-CO; predates the 2021+ wave of diffusion-model and equivariant GNN approaches to discrete optimization.

## Key terms
graph neural network, pointer network, attention mechanism, Transformer, self-attention, deep reinforcement learning, REINFORCE policy gradient, TSP, vehicle routing, minimum vertex cover, maximum clique, maximum independent set, MaxCut, graph coloring, SAT, message passing, structure2vec, Concorde, NP-hard, combinatorial optimization
