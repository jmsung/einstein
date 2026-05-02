---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P6, P7, P9, P13, P14, P22]
compute_profile: [local-cpu, local-mps, modal-gpu]
cost_estimate: "negligible — 1-time decision per workload"
hit_rate: "TBD"
status: scaffold (full content in Goal 13)
---

# Compute Router

## TL;DR

Route every workload to its right home **before launching**. Local M5 Max (128GB, MPS float32) handles mpmath, sequential CPU optimizers, large multistart, and float32 batched ops at zero marginal cost. Modal A100/H100 (float64 CUDA, $/hr) is only for sustained float64 parallel workloads. Mismatching either way wastes wall-clock or money.

This page documents the decision matrix today. The full automation tool (`tools/compute_router.py`) is **TBD** and will be implemented in Goal 13.

## When to apply

Before any compute job. Specifically: any time the agent is about to write `import torch` + CUDA, `modal.function`, or kick off a long multistart. The router check runs first; local-first by default.

## Decision matrix

| Workload | Local CPU | Local MPS | Modal A100/H100 | Notes |
|---|---|---|---|---|
| mpmath ulp polish (any dps) | best | — | — | Pure CPU; arbitrary precision is CPU-only |
| L-BFGS / NM / SLSQP (single run) | best | — | — | Sequential; GPU idle |
| LP / IPM (HiGHS) | best | — | only if RAM-bound | CPU IPM scales in 128GB |
| Basin-hopping (small populations) | best | partial | — | Python overhead dominates |
| Basin-hopping (float32 large pop) | partial | best | partial | MPS shines for batched float32 |
| CMA-ES large population | partial | best (float32) | best (float64) | Choose precision per problem |
| Multistart 1000+ trials, quick each | best | partial | overkill | Multiprocess across cores |
| SA parallel tempering (float64) | — | — | best | Sustained GPU parallel |
| Large LP / SDP (RAM-bound) | partial | — | best | When matrices > 64GB |
| GPU benchmark / calibration | run | run | run | Calibrate per machine |

## Procedure

1. **Profile locally** — time the bottleneck stage. Sequential or parallel?
2. **Fill the spec**:
   - **Workload class**: sequential / parallel / batched / RAM-bound
   - **Precision**: float32 OK / float64 needed / mpmath needed
   - **Wall-clock estimate**: minutes / hours / GPU-hours
   - **RAM footprint**: fits in 128GB / needs more
3. **Match against the matrix.** If clear, go.
4. **GPU-specific call**: defer to `gpu-decision-framework.md` and run `python -m einstein.gpu_tempering.benchmark`.
5. **Cost gate** for Modal: `hours × $/hr`. Only proceed if speedup > 3× over local. Document estimate in `mb/tracking/<problem>/experiment-log.md`.
6. **TBD (Goal 13)**: `tools/compute_router.py <spec>` will produce the recommendation programmatically.

## Pitfalls

- **Sequential Python on GPU** → idle GPU, slow wall-clock, $$$ wasted (P9 grid-eval audit: 40ms of 210ms total — not worth $4/hr H100).
- **1000-trial multistart on Modal** when local 16-core multiprocess is faster.
- **mpmath at high dps on Modal** — CPU-bound; GPU idle 100% of the time.
- **Skipping local benchmark on a fresh machine** — calibration drifts; assumed throughputs go stale.
- **Treating MPS as float64** — MPS is float32 only; final SOTA polish needs float64 → Modal.

## Compute profile

This page is the routing layer for everything else. It does not run compute; it dispatches.

## References

- `mb/wiki/cross-problem-lessons-gpu.md` (full decision framework, per-problem audits).
- `wiki/findings/gpu-modal-compute.md` (lesson #26 Python overhead; lesson #63 Modal BnB economics; GIL pitfall).
- `wiki/techniques/gpu-decision-framework.md` (GPU-specific decision tree; benchmark tool).
- `.claude/rules/compute-router.md` (the rule that triggers this page).
- `src/einstein/gpu_tempering/benchmark.py` (existing GPU benchmark).
- `tools/compute_router.py` — **TBD** (Goal 13).
