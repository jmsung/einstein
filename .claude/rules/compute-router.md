# Compute routing — pick the right home for each workload

Two first-class compute environments. Route every workload to its best home **before launching**. Sequential mpmath on Modal wastes money; large LP on MPS leaves CPU cores idle; parallel float64 SA on local CPU takes 730× too long.

## Environments

**Local: MacBook Pro M5 Max (128GB unified memory)**
- Many CPU cores + Apple Silicon GPU via MPS (float32 native)
- 128GB unified memory — most LP / multistart workloads fit in RAM
- Zero marginal cost; good for unbounded experimentation
- Single-machine, single-precision-tier (MPS = float32 only)

**Cloud: Modal A100/H100**
- float64 CUDA — required for final polish near SOTA
- $/hr cost — only justified for sustained parallel float64
- Multi-GPU / multi-node capable for LP/SDP that exceeds local RAM

## Decision matrix

| Workload | Local CPU | Local MPS | Modal A100/H100 | Notes |
|---|---|---|---|---|
| mpmath ulp polish (any dps) | ✅ best | ❌ | ❌ | Pure CPU; scales with cores |
| L-BFGS / Nelder-Mead / SLSQP (single run) | ✅ best | ❌ | ❌ | Sequential; GPU sits idle |
| LP / IPM (HiGHS) | ✅ best | ❌ | only if RAM-bound | CPU IPM scales well in 128GB |
| Basin-hopping (small populations) | ✅ best | △ | ❌ | Python overhead dominates |
| Basin-hopping (float32 large pop) | △ | ✅ best | △ | MPS shines for batched float32 |
| CMA-ES large population | △ | ✅ float32 | ✅ float64 | Choose precision per problem |
| Multistart 1000+ trials, quick each | ✅ best | △ | overkill | Multiprocess across cores |
| SA parallel tempering (float64) | ❌ | ❌ | ✅ best | Sustained GPU parallel |
| Large LP / SDP (RAM-bound) | △ | ❌ | ✅ best | When matrices > 64GB |
| GPU benchmark / calibration | ✅ | ✅ | ✅ | Run on each before deciding |

**Why:** Cost without speedup is waste; speedup at wrong precision is wrong score. The current `findings/gpu-modal-compute.md` already documents the pitfall of "running sequential Python on GPU — the GPU sits idle." The dual is also true: parallel float64 on local CPU is a wall-clock disaster.

**How to apply:**

1. **Before launching any compute job**, fill in:
   - **Workload class** (sequential / parallel / batched / RAM-bound)
   - **Precision required** (float32 OK / float64 needed / mpmath needed)
   - **Expected wall-clock** (minutes / hours / GPU-hours)
   - **RAM footprint** (fits in 128GB / needs more)

2. **Match against the matrix.** If clear, go.

3. **If unclear**, run `tools/compute_router.py <spec>` (see Goal 13) for a recommendation, OR run `python -m einstein.gpu_tempering.benchmark` (existing) for the GPU-specific call.

4. **If recommendation is `STAY ON CPU`** for a workload you assumed needed GPU, trust it. The GPU sits idle on sequential workloads.

5. **Cost gate** for Modal: `hours × $/hr`. Only proceed if expected speedup > 3× over local. Document the cost estimate in `mb/tracking/<problem>/experiment-log.md`.

**Common pitfalls:**
- Running Python `for` loop on GPU → idle GPU, slow wall-clock, $$$ wasted
- Running 1000-trial multistart on Modal when local 16-core multiprocess is faster
- Running mpmath at high dps on Modal → CPU-bound, GPU idle
- Skipping the local benchmark on a fresh machine — calibration drifts

**Triggering pattern:** any time the agent is about to write `import torch` + `cuda` OR `modal.function`, the router check runs first. Local-first by default; cloud only when justified.

See also: [wiki/techniques/compute-router.md](../../wiki/techniques/compute-router.md) (built in Goal 13), [findings/gpu-modal-compute.md](../../wiki/findings/gpu-modal-compute.md), [axioms](axioms.md) (A4 GPU/compute pre-audit).
