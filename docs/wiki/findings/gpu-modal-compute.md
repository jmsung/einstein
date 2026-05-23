---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
  - ../source/repos/jmsung-einstein.md
  - ../source/repos/jmsung-einstein-codebase.md
---

# GPU & Modal Cloud Compute

## #26: GPU Python loop overhead dominates small-tensor workloads {#lesson-26}

For problems where each iteration processes tiny tensors (e.g., 64x594x11), GPU utilization is only 25-35% due to kernel launch overhead. Stronger GPUs don't help — the bottleneck is the Python-to-CUDA dispatch latency, not the compute kernel itself.

**Solutions**:
- **(a)** Batch K operations per Python step — amortize the launch overhead across multiple logical iterations
- **(b)** Custom CUDA/Triton kernel — fuse the entire inner loop into a single kernel launch
- **(c)** `torch.compile` — let the compiler discover fusion opportunities automatically

Problem 6: A100 at 35% utilization, H100 would be no better. The lesson generalizes to any optimization loop where per-iteration tensor sizes are small (< 1024 elements per dimension) and the iteration count is high (> 100K).

## #63: Modal BnB economics — formal exhaustive proofs at single-digit USD {#lesson-63}

Problem 19 Difference Bases (2026-04-09): the full w=3 exhaustive BnB sweep over C(90,3) = 117,480 atom triples ran on Modal in 88 wall-minutes (1175 chunks x 100 triples, 100 concurrent containers), consumed 1.22 trillion compute nodes across ~85 CPU-core-hours, and cost ~$4. The w=4 random sample of 2504 quadruples consumed another 3.45 trillion nodes and ~$4 before being aborted at 25% for repo-split.

**Data point**: for combinatorial problems where a handwritten numba BnB achieves ~10M nodes/sec, Modal's per-core pricing makes 10^12 to 10^13 node sweeps routine at single-digit USD. This puts **formal negative lemmas** (per-configuration tree-exhausted proofs) within easy reach for any problem whose search space can be sharded into independent chunks.

**Rule**: when a combinatorial problem has a natural "pick w items to vary, fix the rest" decomposition AND the full enumeration C(n, w) is in 10^4 to 10^6, a Modal BnB sweep is the right tool — it gives a publishable negative result in minutes if the problem is locked, and hits with certainty if it isn't. Budget 1-2 hours for the Modal wrapper + `@nb.njit(nogil=True)` to avoid the heartbeat-GIL pitfall. Scale the per-chunk compute to ~60-120s to stay safe.

## #83: Exhaustive GPU parallel search confirms basin optimality {#lesson-83}

Problem 13 Edges vs Triangles (2026-04-10): 50 parallel Modal A100 GPU jobs (20 L-BFGS restarts at various noise scales, 10 PyTorch L-BFGS, 5 multi-resolution cascades, 10 simulated annealing, 5 differential evolution) plus a 500-point x 10,000-candidate reinsertion sweep ALL found zero improvement over -0.71170918806610.

This, combined with the theoretical analysis (Razborov proves Turan optimal per row, slope-3 analysis proves lower y always better, remaining headroom of 1.22e-4 is entirely from N=500 discretization), confirms the basin is the global optimum for the 500-point Turan parameterization.

**Rule**: when session saturation (lesson #70) has been declared and you want to confirm rather than pivot, a single large parallel GPU sweep across all optimizer families (gradient, evolutionary, annealing, reinsertion) is more conclusive than N sequential scripts. If all families return zero improvement from the same warm-start, the basin is locked. This is the definitive "basin lock" evidence for closing a problem.

## Modal + numba GIL pitfall {#modal-numba-gil}

When running long-compute numba `@njit` functions inside Modal containers, **you MUST use `nogil=True` on the @njit decorators**. Otherwise the container's heartbeat thread cannot acquire the GIL during compute, Modal marks the worker as dead, and your sweep devolves into a loop of heartbeat failures and worker preemptions.

**Symptoms**: 0 chunks complete for minutes, log full of "Modal Client -> Modal Worker Heartbeat attempt failed / Runner interrupted due to worker preemption" errors.

**Fix**: `@nb.njit(cache=True, nogil=True)` on every @njit decorator. Also add a `time.sleep(0)` between compute batches in the Python worker loop as belt-and-suspenders to give the heartbeat thread a scheduling window.

**Secondary tip**: size your batches so each compute call <= ~120s, not 5+ minutes, because Modal's heartbeat timeout is a few minutes and even nogil may not be perfectly smooth across all Python/numba version combinations. Smaller chunks are safer.

**Context**: CP-SAT ILPs at scale stall in presolve (P19 atom ILP at 7M aux bools). Handwritten numba BnB is the portable fallback — get this plumbing right the first time.
