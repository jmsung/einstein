---
type: source
kind: paper
title: Combinatorial optimization and reasoning with graph neural networks
authors: Quentin Cappart, Didier Chételat, Elias Boutros Khalil, Andrea Lodi, Christopher Morris, Petar Velickovic
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.09544
source_local: ../raw/2021-cappart-combinatorial-optimization-reasoning-graph.pdf
topic: general-knowledge
cites:
---

# Combinatorial optimization and reasoning with graph neural networks

**Authors:** Quentin Cappart, Didier Chételat, Elias Boutros Khalil, Andrea Lodi, Christopher Morris, Petar Velickovic  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.09544

## One-line
A structured survey of how graph neural networks (GNNs) are being used to solve, accelerate, or replace components of classical combinatorial optimization (CO) pipelines.

## Key claim
GNNs are a natural inductive-bias match for CO because they are permutation-invariant, sparsity-aware, and handle node/edge features — making them suitable both as primal heuristics (predicting solutions) and as learned components inside exact solvers (branching, cutting, variable selection), but they still face a hard trade-off triangle between scalability, expressivity, and out-of-distribution generalization.

## Method
Conceptual review, not a new algorithm. Partitions the literature into (i) primal-side uses — GNNs that emit feasible solutions directly via supervised, unsupervised (Erdős-style differentiable proxy loss), or reinforcement learning regimes; (ii) dual-side uses — GNNs embedded in branch-and-bound, branch-and-cut, SAT, and CSP solvers to learn branching, cut selection, or variable ordering on the variable-constraint bipartite graph; (iii) algorithmic reasoning — training GNNs to imitate classical algorithms (BFS, Bellman-Ford, pointer-based data structures) and then transferring that prior to raw-input CO.

## Result
No theorem; the synthesis is the artifact. Establishes a taxonomy (primal vs dual vs raw-input end-to-end), catalogs four core challenges (permutation/sparsity, expressivity vs scale, side-information handling, data efficiency / OOD transfer), and documents concrete wins — e.g., Gasse et al. (2019) GCN branching, Mirhoseini et al. (2021) chip placement on TPUs, Selsam et al. NeuroSAT, Khalil MIP-GNN — alongside known limits tied to the Weisfeiler–Leman expressivity ceiling (Morris et al., Xu et al.).

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are currently framed as GNN-learnable, and the wiki's CO content centers on LP/SDP duality, Cohn–Elkies, and Remez exchange rather than learned heuristics — but the survey is useful if the agent ever considers learning a branching/cut-selection heuristic for the LP-bound problems (P1 sphere packing, P15/P16 autocorrelation) or a primal heuristic for discrete packing problems.

## Open questions / connections
- Can a GNN trained on the variable-constraint bipartite graph of the Cohn–Elkies LP accelerate dual-bound tightening across sphere-packing dimensions?
- The expressivity ceiling at 1-WL (Morris, Xu) — does it preclude GNNs from recognizing the symmetry structure (e.g. E8, Leech) that the arena's sphere-packing problems exploit?
- Data-efficiency / OOD transfer remains open — relevant if anyone tries cross-problem transfer (P1 → P15 → P16) via a shared GNN backbone.
- Mirhoseini chip-placement and Gasse branching as templates for "GNN inside an exact solver," contrasted with end-to-end pointer-network TSP solvers (Kool, Joshi) which are primal-only.

## Key terms
graph neural network, combinatorial optimization, branch-and-bound, branch-and-cut, mixed-integer programming, LP relaxation, SAT solver, constraint satisfaction, Weisfeiler-Leman, message passing, permutation invariance, Erdős unsupervised loss, neural algorithmic reasoning, variable-constraint bipartite graph, TSP, learning to branch
