---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
  - problem-6-kissing-number/strategy.md
  - ../source/repos/jmsung-einstein-codebase.md
---

# Simulated Annealing & Parallel Tempering

## #24 (SA version): SA parallel tempering beats greedy by 730x

For sphere packing problems where greedy micro-perturbation stalls, simulated annealing with parallel tempering (multiple replicas at different temperatures + replica exchange) finds improvements 730x faster. Problem 6: greedy at 1e-12 gave 6.45e-10 in 110M iters; SA at 1e-6 with 8 replicas gave 9.15e-7 in 20M iters. The key: Metropolis acceptance of uphill moves at hot replicas discovers escape routes that greedy never sees. 8 replicas at different temperatures + replica exchange is the recipe. The improvement ratio scales dramatically — P6 scale 1e-6 gave 9.15e-7 in 20M iters vs greedy 6.45e-10 in 110M iters at scale 1e-12.

## #25: Smooth loss approximation is a trap

Replacing hinge loss max(0, 2-d) with softplus(β(2-d))/β seems theoretically sound but fails in practice. The smooth loss has a different optimum that pulls the solution away from the hinge optimum, regardless of β. Low β changes the objective; high β recovers the flat gradient. No β works. Problem 6: tested β=100-5000, all made score worse (0.35-1.5 vs 0.156 SOTA). The softplus(β·hinge)/β formulation changes the objective at low β, recovers the flat gradient at high β — there is no β that simultaneously approximates the loss landscape and maintains useful gradient information.

## #27 (SA decay): SA diminishing returns follow exponential decay

Each round of SA parallel tempering finds ~50-60% less improvement than the previous. This is convergence within the basin, not a plateau across basins. Each round yields approximately half the improvement of the previous round, following an exponential decay curve. To escape: either much larger perturbation scale (risky — may leave the productive region entirely) or fundamentally different starting point (new basin). The convergence is within-basin — it tells you the basin is being exhausted, not that no other basins exist.

## #28: Cage structure diagnostic

Count pinning neighbors before optimizing. Problem 6: 3 pairs dominate 72.5% of total loss, each worst-vector caged by 25-30 neighbors at cos=0.5. This geometric lock makes local escape impossible regardless of method (SA, gradient, eigenvalue, remove-readd). Before investing GPU hours, analyze the constraint structure: if a small number of pairs dominate loss AND those vectors are heavily pinned, the basin is locked.

The diagnostic is: identify which pairs contribute most to loss, then for each worst vector, count how many other vectors are at exactly the critical distance (cos=0.5 for kissing number). If the count is high (25-30 in the P6 case), the vector is caged — every direction of movement simultaneously moves it closer to some neighbor. No local method (SA, gradient descent, eigenvalue perturbation, remove-and-readd) can escape this cage. The constraint structure must be analyzed before committing compute, not after exhausting it.
