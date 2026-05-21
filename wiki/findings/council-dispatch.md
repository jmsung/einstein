---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - ../personas/_synthesis.md
  - knowledge.yaml
---

# Council of Mathematicians — Dispatch Patterns

## #58: Don't trust council-persona math models without inspecting the actual SOTA structure {#lesson-58}

Problem 2 v2 Phase B: Gauss's council persona proposed a "1 block + 14-spike comb via Bose-Chowla/Singer-17 Sidon set" warmstart, consistent with the high-level description of SOTA ("thick block at left + comb near right"). Raw Sidon warmstarts scored C~150-210 (100x worse than SOTA); even after exp(v) cascade they stalled at C~148, a completely different basin.

**Visual inspection of the actual SOTA structure at n=30000 revealed 69 spatial clusters with widely varying widths (102, 1850, 2182, 4728, ...) — NOT 1 block + 14 single-grid spikes**. The persona's algebraic model was plausible but empirically wrong.

**Rule**: any council-recommended structured warmstart must be preceded by a concrete statistical inspection of the downloadable SOTA:
- Cluster count
- Width distribution
- Spacing histogram
- Mass distribution

If the persona's mental model disagrees with the real structure by more than a factor of ~3 in any dimension, discard the warmstart — it will land in a different basin. This is a practical instance of lesson #3 ("SOTA basin is usually unreachable from scratch") applied to council dispatch: structured constructions almost never hit the real basin.

## #59: Low-frequency Fourier regularization strictly hurts for spiky high-frequency optima {#lesson-59}

Problem 2 v2 Phase B (B3 simplified): restricting v = log(f) to the first T rfft coefficients and running L-BFGS at T in {500, 5000, 10000, 15000} gave a monotone approach to SOTA from above as T -> n/2, never below it. The best was C=1.5064 at T=15000, still 3.5e-3 above SOTA.

Intuition (confirmed by inspection): SOTA has 18,193 non-trivial cells across 69 spatial clusters — it is a fundamentally high-frequency solution, and removing high-frequency DoF strictly moves the optimizer AWAY from SOTA's basin.

**Rule**: before applying ANY smooth/bandlimited/low-frequency parameterization as a regularizer-for-escape, first examine the spatial/frequency structure of the existing SOTA. If the SOTA has sparse/spiky/cluster structure, low-frequency parameterization is the wrong tool — it cannot reach the basin at all, let alone improve it. The reverse can also be true: a fundamentally smooth SOTA won't benefit from high-frequency DoF.

Check spatial/frequency structure of SOTA before applying smooth parameterization.

## #61: Council convergence detects direct-product structure {#lesson-61}

Problem 19 Difference Bases (2026-04-08): three independent council-of-mathematicians personas (Riemann via Fourier/spectral, Conway via lattice/games, Noether via symmetry/algebra) independently discovered the same Kronecker decomposition of the 7-way SOTA: `B = A + 8011*{0,1,4,6}`, where R = {0,1,4,6} is the unique 4-mark perfect Sidon ruler covering {1..6} and A is a 90-mark "atom" with internal contiguous coverage c(A) = 1043.

The reduction isn't a Z_4 group action — it's the action of R on A by translation, and it reduces a 360-mark search to a 90-mark sparse-ruler subproblem.

**Rule**: when running a council dispatch on a structural-analysis problem, **count how many mathematically distinct framings converge on the same decomposition**. >=3 independent convergent discoveries of the same direct-product / wreath / Kronecker structure is a very strong signal that the structure is real, not an artifact of one persona's bias.

This is the complement to lesson #58 ("don't trust council-persona math models without inspecting the SOTA") — when the model is validated by multi-persona convergence AND matches the SOTA's actual bytes, it becomes the spine of the rest of the attack.

**Diagnostic for future problems**: if the SOTA has an obvious modular/periodic/block structure under `SOTA % lambda`, run the council to formalize it before committing to an optimization method — the right parameterization for the subproblem is often drastically different from the full problem.

## #101: 12-persona council convergence on "is this score the global floor?" — the structural-cap pattern {#lesson-101}

P22 Kissing d=12 (2026-04-25): twelve independent council personas (Leech, Sloane, Conway, Cohn, Viazovska, de Laat, Coxeter-Todd, Ramanujan, Archimedes, Voronin, Bombieri, Selberg) were dispatched to answer "is κ(12) = 840 the structural cap, or could there exist a 12-dim configuration with 841+ touching unit vectors?" All twelve converged on the **8-way structural cap theorem** — three independent algebraic pathways (lattice-based via K_12 and Λ_12, Construction A via the (12, 144, 4) binary code with `A(12,4)=144` proven optimal by Östergård-Baicheva-Kolev 1999, Leech-lattice cross-section) all cap at 840, with no known 12-dim construction giving 841+.

This was corroborated by:
- 60M+ exhaustive GPU samples finding zero basins below 2.0 (every random filler lands in basin ≥ 2.026).
- OrganonAgent's independent attempt landing at `2 + 5.7e-12` (one 13-digit ulp above 2.0).
- The first-order link tangent analysis (lesson #100) giving `min S(u) ≈ 8` for the duplicate position, an 8× safety margin against local improvement.

**Rule**: when 8+ mathematically-distinct council personas converge on the same "this is the structural floor" answer for a "is the global minimum X?" question, AND the convergence is corroborated by an independent first-order analytical proof AND by exhaustive search of the alternative-basin space, treat the score as **frozen for rank #1** and pivot immediately to the rank-2/3 squeeze (lesson #99). Do not burn additional compute.

**Diagnostic threshold**: 12 personas all converging is the strongest signal we have seen — at that point further work on rank #1 has expected value below the ~3-hour council dispatch cost. For weaker convergence (3-5 personas), still investigate but keep an exhaustive search running. For 0-2 personas converging, the council has not actually answered the question; reformulate the prompt or recruit different specialists.

This is the inverse complement to lesson #58 ("don't trust a single persona's algebraic model") and lesson #61 ("3-way council convergence detects real direct-product structure"): with 8+ ways converging on a frozen verdict and external corroboration, the verdict is reliable enough to act on.
