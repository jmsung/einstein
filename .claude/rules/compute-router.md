# Compute routing — pick the right home for each workload

**2026-05-24**: Modal cloud GPU is currently **NOT IN USE**. All workloads run on the local workstation (CPU + MPS). Modal scripts remain available; re-enable only if a workload genuinely needs sustained float64-CUDA throughput that MPS f32 + unified memory can't cover. The "cloud" column is kept in the decision matrix below as forward-looking reference.

## Environments

**Local: a local workstation — primary** ✅
- Many CPU cores + Apple Silicon GPU via MPS (float32 native)
- ample unified memory — fits LP / multistart / large-batch workloads this machine didn't previously cover
- Zero marginal cost; good for unbounded experimentation
- Single-precision-tier on GPU (MPS = float32 only)

**Cloud: Modal A100/H100 — currently unused (kept available)**
- float64 CUDA — would be required for final polish if a problem genuinely needs it
- $/hr cost — was the original reason for the cost gate
- Re-enable trigger: a measured run on MPS f32 + high-memory RAM shows the workload is precision-bound (not memory-bound) AND the expected speedup is > 3× over local

## Decision matrix (Modal column reflects historical recommendation; treat as forward-looking)

| Workload | Local CPU | Local MPS | Modal A100/H100 | Notes |
|---|---|---|---|---|
| mpmath ulp polish (any dps) | ✅ best | ❌ | ❌ | Pure CPU; scales with cores |
| L-BFGS / Nelder-Mead / SLSQP (single run) | ✅ best | ❌ | ❌ | Sequential; GPU sits idle |
| LP / IPM (HiGHS) | ✅ best | ❌ | only if high-memory RAM exhausted (rare) | the workstation usually fits |
| Basin-hopping (small populations) | ✅ best | △ | ❌ | Python overhead dominates |
| Basin-hopping (float32 large pop) | △ | ✅ best | △ | MPS shines for batched float32 |
| CMA-ES large population | △ | ✅ float32 (default) | only if f64 strictly required | Default to MPS f32 |
| Multistart 1000+ trials, quick each | ✅ best | △ | overkill | Multiprocess across cores |
| SA parallel tempering (float64) | △ | ✅ try f32 first | only if f32 verified insufficient | Default to MPS f32 + verify precision |
| Large LP / SDP (RAM-bound) | △ | ❌ | only if matrices > 96GB | ample unified memory usually covers it |
| GPU benchmark / calibration | ✅ | ✅ | (skip — not in use) | Local-only by default now |

**Why:** Modal was justified when local CPU/GPU was undersized; the workstation's MPS + ample unified memory eliminates most of the original reasons. Cost without speedup is waste; speedup at wrong precision is wrong score. Default local; revisit Modal only when a measurement says otherwise.

**How to apply:**

1. **Before launching any compute job**, fill in:
   - **Workload class** (sequential / parallel / batched / RAM-bound)
   - **Precision required** (float32 OK / float64 needed / mpmath needed)
   - **Expected wall-clock** (minutes / hours / GPU-hours)
   - **RAM footprint** (fits in high-memory / needs more)

2. **Match against the matrix.** If clear, go.

3. **If unclear**, run `scripts/compute_router.py <spec>` (see Goal 13) for a recommendation, OR run `python -m einstein.gpu_tempering.benchmark` (existing) for the GPU-specific call.

4. **If recommendation is `STAY ON CPU`** for a workload you assumed needed GPU, trust it. The GPU sits idle on sequential workloads.

5. **Modal re-enable gate (currently in standby):** if a benchmark shows local workstation can't cover the workload (e.g. MPS f32 result fails the triple-verify precision floor and exact f64 reimpl is too slow), then and only then justify Modal with `hours × $/hr × ≥3× speedup-over-local`. Document the measurement that motivates the switch in `mb/<problem>/experiment-log.md`.

**Common pitfalls:**
- Running Python `for` loop on GPU → idle GPU, slow wall-clock
- Running 1000-trial multistart anywhere but a multicore local — multiprocess + Apple Accelerate single-thread workers is the right shape (see [the workstation-utilization-strategy](../../knowledge/wiki/findings/the workstation-utilization-strategy.md))
- Defaulting to Modal when MPS f32 hasn't been verified for precision — start local, escalate only on measurement
- Skipping the local benchmark on a fresh machine — calibration drifts

**Triggering pattern:** any time the agent is about to write `import torch` + `cuda` OR `modal.function`, the router check runs first. **Local-only by default as of 2026-05-24**; cloud re-enable requires a documented benchmark + cost/speedup case.

See also: [knowledge/wiki/techniques/compute-router.md](../../knowledge/wiki/techniques/compute-router.md) (built in Goal 13), [findings/gpu-modal-compute.md](../../knowledge/wiki/findings/gpu-modal-compute.md), [axioms](axioms.md) (A4 GPU/compute pre-audit).
