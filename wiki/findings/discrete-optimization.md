---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
---

# Discrete & Combinatorial Optimization

## Generic ILP solvers hit scale walls

CP-SAT's python API (OR-tools) cannot handle atomic "exists a pair with difference d" constraints when the variable universe is large. For P19 atom sparse-ruler (S_max=6967, target_v=1044), both tried encodings — linear pair lower-envelope AND AddElement witness-index — expand to ~7M aux booleans via CP-SAT's internal boolean engine, and presolve stalls without making search progress. Disabling presolve (`cp_model_presolve=False`) doesn't help because boolean encoding happens pre-presolve.

**Signal**: if `[SAT presolve] num removable Booleans: N/M` where N ≈ M, and the solver prints "Stopped after presolve" with `booleans: 0 conflicts: 0`, the formulation is dead. No tuning will rescue it. The ~7M aux boolean count is the CP-SAT boolean engine wall — `num_removable_booleans ≈ num_booleans` in presolve is the smoking gun.

**Alternatives**:
1. **Handwritten numba BnB** — goal-directed DFS, iterative with explicit stack, `@nb.njit(nogil=True)`. ~20M nodes/sec. Works for problems where the branching can be constrained (e.g., goal-directed "add a mark to cover the smallest uncovered d").
2. **Commercial solver** (Gurobi/CPLEX) with lazy constraint callbacks — not in current stack.
3. **Specialized literature algorithms** (e.g., Pegg's 2020 sparse-ruler enumeration) — reimplement.

Do NOT retry CP-SAT at the same scale with a "different formulation" — the wall is the boolean engine itself, not the encoding.

## #62: "When to write your own solver" decision framework

CP-SAT boolean wall leads to numba BnB. Problem 19 Difference Bases (2026-04-09): CP-SAT cannot handle "exists a pair with difference d" constraints at S_max = 6967. A handwritten goal-directed numba BnB at `~10M nodes/sec` (after 4x speedup via incremental `uncov_cache[level]` and `d_star_cache[level]`) solved the same w=3 LNS subproblem in seconds per trial.

**Three conditions that must ALL hold to justify writing your own solver**:

**(a)** The generic ILP/CP-SAT solver hits a scale wall that parameter tuning won't rescue (`num_removable_booleans ≈ num_booleans` in presolve is the smoking gun).

**(b)** The problem has a natural goal-directed branching rule where each branch decision is constrained to a tiny set (e.g., "the new mark must be `existing_a ± d_star`" — branching factor ≤ 2·depth, not ≤ S_max).

**(c)** You can encode the inner loop in numba with `@nb.njit(cache=True, nogil=True)` and expect ≥1M nodes/sec.

**Anti-pattern**: trying a third, fourth, fifth CP-SAT formulation for the same problem — if encoding #1 and encoding #2 both blow up to the same aux-bool count, the wall is CP-SAT's boolean engine, not the formulation. Pivot to custom code. **ROI signal**: for P19, 2 hours of custom BnB development replaced a dead-end CP-SAT attempt and unlocked a formal negative lemma.

## #64: Goal-directed BnB "no-deferral" caveat

Always document the soundness boundary of your pruning. Problem 19 Difference Bases (2026-04-09): the `atom_bnb.py` w=3 LNS sweep uses the goal-directed branching rule "at each node, find the smallest uncovered d* and branch only on `new_mark = existing_a ± d*`". This makes branching factor ≤ 2·depth instead of ≤ S_max, but introduces a soundness caveat: if a solution exists where the smallest uncovered d* at some node is covered ONLY by a pair of TWO new marks (both added later), the BnB never explores it. For w=3 the residual miss is small (only 3 new-new pairs possible).

**Rule**: when writing a custom BnB with problem-specific pruning, explicitly document the invariant your branching enforces and the class of solutions it cannot reach. Without this, a 0-hit sweep is at risk of being wrongly promoted to a "complete negative proof" when it's only a proof-within-the-pruning-model. The claim should read "no w=3 swap produces c(A) ≥ 1044 such that each new mark immediately covers the current smallest uncovered d*", NOT "no w=3 swap produces c(A) ≥ 1044". Scope the negative lemma correctly. A well-scoped negative lemma is publishable; a sloppy one is a footgun.

## Modal + numba: GIL pitfall

When running long-compute numba @njit functions inside Modal containers, you MUST use `nogil=True` on the @njit decorators. Otherwise the container's heartbeat thread cannot acquire the GIL during compute, Modal marks the worker as dead, and your sweep devolves into a loop of "Modal Client -> Modal Worker Heartbeat attempt failed / Runner interrupted due to worker preemption". Symptoms: 0 chunks complete for minutes, log full of heartbeat errors.

**Fix**: `@nb.njit(cache=True, nogil=True)` on every @njit decorator. Also add a `time.sleep(0)` between compute batches in the Python worker loop as belt-and-suspenders to give the heartbeat thread a scheduling window.

**Secondary tip**: size your batches so each compute call is 60-120s, not 5+ minutes, because Modal's heartbeat timeout is a few minutes and even nogil may not be perfectly smooth across all Python/numba version combinations. Smaller chunks are safer.
