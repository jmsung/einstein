---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
synthesized_into: ../concepts/k-climbing-and-dof-augmentation.md
cites:
  - ../concepts/k-climbing-and-dof-augmentation.md
---

> **See also**: [`concepts/k-climbing-and-dof-augmentation.md`](../concepts/k-climbing-and-dof-augmentation.md) — the abstract concept distilled from the lessons below. This finding is the **provenance**: per-problem empirical episodes. Read the concept first; come here for the receipts.

# k-Climbing & Dimension Augmentation — empirical lessons

## #24 (k-climbing version): k-climbing beats local optimization at fixed k

Problem 18 (Uncertainty Principle): all k=13 optimization methods (CMA-ES, NM, hillclimb, gradient descent, basin hopping) converge to the same basin at S ~ 0.31835. The fast evaluator has 90%+ false positive rate for improvements (far sign changes). But increasing to k=14 with a single extra root in the far cluster + gap-space Nelder-Mead immediately gave S=0.31817 — a 1.8e-4 improvement that no amount of k=13 optimization could achieve.

When stuck at a local minimum, try adding degrees of freedom before exhausting search at the current dimensionality. The fundamental insight is that the k=13 basin is a genuine local optimum in the k=13 search space — no rearrangement of 13 roots can escape it. But k=14 opens a new dimension that creates descent directions invisible at k=13. The improvement is immediate and large (1.8e-4 vs 0 from k=13 optimization), confirming that the barrier was dimensionality, not optimization quality.

## #66: k-climbing has rapidly diminishing returns

Problem 9 Uncertainty Principle (2026-04-08, refines lesson #24): k=13 -> k=14 dropped the score by 1.8e-4 (above the 1e-4 minImprovement gate, the breakthrough that took us to #1). k=14 -> k=15 dropped the score by only 4.57e-6 (40x below the gate, despite 22 deep-parallel CMA-ES starts, ~70 minutes of CPU, 12+ insertion positions tried). The k-climb step size is NOT roughly constant — it shrinks fast as the polynomial approaches the continuous limit.

### Gate-feasibility ratio

Compute the gate-feasibility ratio `(observed_step_size / minImprovement)` for the FIRST successful climb, then for the SECOND:

- After k=14: ratio was 1.8 (1.8e-4 / 1e-4) — comfortably above gate.
- After k=15: ratio collapsed to 0.046 — 40x below gate.

**Decision rule**: if `ratio_2 < 0.1`, abandon the simple k-climb path. Even if k=15 -> k=16 -> k=17 each gave another 5e-6, you'd need ~22 successful climbs to amortize across the gate — none guaranteed.

### When to pivot

When the second climb's `(step_size / minImprovement)` ratio is < 0.1, pivot to either:

**(a)** A structurally different parameterization (e.g., 4-cluster instead of 3-cluster split for P9).

**(b)** A different basin entirely (different starting cluster topology).

**(c)** Declare the problem locked at the current k and move on.

Continuing to climb at <0.1 ratio is wasted compute — the basin is too narrow to amortize across the gate even with many successful steps.
