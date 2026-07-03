---
type: finding
author: agent
drafted: 2026-05-23
question_origin: feat/autonomous-loop Phase 2 (the workstation calibration)
status: answered
related_concepts: [float64-ceiling.md]
related_techniques: [compute-router.md, mpmath-ulp-polish.md, basin-hopping-multistart.md, cma-es-with-warmstart.md, parallel-tempering-sa.md]
related_findings: [gpu-modal-compute.md]
cites:
  - ../../agent/calibrations/apple-the workstation-high-memory.json
  - ../../tools/calibrate.sh
  - ../../../scripts/local_benchmark.py
  - ../../../scripts/compute_router.py
  - ../../../.claude/rules/compute-router.md
---

# the workstation utilization strategy — what multi-core + MPS + high-memory actually buys

> **Update 2026-05-24**: Modal cloud GPU is no longer in active use. Per the calibration below, the workstation covers everything we've actually needed in practice — including workloads the original routing recommended Modal for. The "→ Modal" recommendations in section D/E below are kept as forward-looking conditions for re-enabling cloud, NOT as current practice. Default is now: try local first; escalate only on a measured precision/throughput failure.

## TL;DR

Apple silicon MacBook Pro Max (multi-core, unified memory, MPS GPU) is **two distinct machines** for our purposes — a 418-GFLOPS f64 CPU **and** a  f32 GPU — sharing one address space. **The router now defaults to local for everything**; Modal re-enable requires a documented measurement. Three counter-intuitive findings make the difference:

1. **MPS is competitive with Modal A100 for f32 workloads.** measured vs ~10–12 TFLOPS A100 effective. Zero $/hr, no startup overhead, no PCIe transfer. Any float32 batched workload (basin-hopping pop, CMA-ES f32, large multistart pop with parallel evals) should route here unless you specifically need f64.
2. **Apple Accelerate already saturates multi-core at the BLAS level — naive `mp.Pool` workers fight each other.** Measured 1.4× speedup across 18 workers running BLAS-heavy numpy. Genuine multiprocess linearity (≈ 16× on multi-core) requires *single-thread BLAS workers* (env vars set in the parent before numpy import) OR Python-bound per-worker payloads.
3. **unified memory raises the local-vs-Modal LP threshold past what Modal A100 single-node offers.** Standard A100 instances have 40–80 GB HBM; some multi-A100 configs reach 160 GB pooled. For LP/SDP/IPM in the 80–120 GB band, the workstation wins on cost AND latency.

## Calibration data (anchor)

From `docs/agent/calibrations/apple-the workstation-high-memory.json` (run 2026-05-23 against numpy 2.4.3 + torch on macOS 26.4.1):

| Metric | Measured | Conservative default | Implication |
|---|---|---|---|
| CPU single-thread f64 matmul 2048³ | 0.042 s (411 GFLOPS) | — | Each core is fast; BLAS already uses all 18 |
| CPU multi-thread f64 matmul 4096³ | 0.329 s (418 GFLOPS) | 5.0 s | **15× the router's pessimistic default** |
| MP speedup, 18 BLAS-heavy workers | 1.4× | — | **Thread contention** — naive Pool is a trap |
| MPS f32 matmul 4096³ | 0.009 s | 0.5 s | **55× the router's default**; A100-competitive |
| mpmath dps=50, 1000 ops | 0.011 s (11 µs/op) | — | High-precision is fast per op; scales with cores |
| RAM headroom | 96 GB confirmed | — | ample unified memory — Modal A100 typically has less HBM |

## Workload routing — measured

### A. Sequential / mpmath / per-iteration CPU optimizers → **local-cpu**

L-BFGS, Nelder-Mead, SLSQP, mpmath ulp polish, single-thread numerical work. The GPU sits idle; the CPU is fast enough that Modal startup overhead alone exceeds total local wall-clock. Default per the router's existing Rule 1.

**No router change needed.** Caveat: if you find yourself running 5+ sequential optimizers serially, parallelize via Rule B below.

### B. Multistart (1000+ trials, short each) → **local-cpu, but pin BLAS threads**

This is where the workstation **looks** like it should excel (multi-core!) and underdelivers if you write the naive code. Measured pitfall: a many-worker `mp.Pool` of `np.random.randn(2048, 2048) @ ...` workers gets 1.4× speedup, not the worker count.

Two ways to get real parallelism:

```python
# Option 1 — single-thread BLAS workers (recommended for numpy-heavy workers)
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"   # set BEFORE first numpy import in parent
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
with mp.get_context("spawn").Pool(processes=18) as pool:
    results = pool.map(worker, range(n_trials))
```

Note: Apple Accelerate (numpy's default macOS backend) **does not always honor these env vars** — it has its own thread pool. The robust workaround is to use `threadpoolctl.threadpool_limits(limits=1)` inside the worker, or pin to OpenBLAS explicitly via `OPENBLAS=1 pip install numpy`.

```python
# Option 2 — Python-bound workers (no need to pin BLAS)
def worker(seed):
    rng = np.random.default_rng(seed)
    state = ...
    for _ in range(100_000):
        # Tight Python loop with tiny numpy ops — interpreter overhead dominates,
        # BLAS doesn't contend.
        ...
    return state
```

For our problem stack, Option 2 fits multistart-with-rotation-lottery (small numpy per trial), Option 1 fits multistart-with-LP-solve (HiGHS per trial is BLAS-heavy).

### C. Float32 batched parallel (basin-hopping pop, CMA-ES f32) → **local-mps**

The flagship the workstation win. f32 measured; that's competitive with what an A100 actually delivers in production for f32 GEMM (theoretical 19.5 TFLOPS, real ~10–12 with kernel + memory overhead). On Modal you pay $1.50–3.50/hr for marginal speedup; on the workstation you pay nothing.

**Routing decision unchanged** — Rule 2 already correctly fires. Confirm via:

```bash
uv run python scripts/compute_router.py --workload basin-hop-pop --precision f32 --hours 4 --ram 16
# → local-mps
```

Where this gets interesting: workloads that would *normally* be on Modal because they're "GPU workloads" — like CMA-ES large population — should be down-promoted to MPS when f32 is acceptable. P-problems that don't require f64 precision (i.e., not in {P5, P6, P11, P14, P17, P18}) are MPS-eligible.

### D. Sustained parallel float64 (parallel tempering, SA-tempering, CMA-ES large f64) → **Modal**

MPS does not support f64. CPU f64 parallel at the throughput needed for parallel tempering is uneconomical (the 730× speedup vs greedy on P6 needs Modal A100). Router Rule 3 unchanged.

### E. Large LP / SDP / IPM — **local up to ~100 GB, Modal above**

Underexploited the workstation asset: ample \*\*unified\*\* memory means HiGHS IPM with 100 GB sparse matrices works locally. Modal A100 single instances are commonly 40 / 80 GB HBM; multi-A100 RAM-pooled configs are more expensive than the workstation savings justify.

**Suggested router refinement:** Rule 4's current threshold (`ram_gb > 96 → modal`) is approximately correct, but the rationale should be updated to "unified-memory comfort zone is 96GB; above that, kernel + python overhead + safety margin push us toward swap-thrashing — go Modal." Tests already cover this (`test_route_large_lp_under_local_ram_stays_local` / `_over_local_ram_goes_modal`).

### F. High-precision mpmath multistart (P5 / P11 / P14 / P17 ulp-polish across seeds) → **local-cpu, parallelized**

This is a special case of B. mpmath at dps=50–80 is pure Python + GMP — no BLAS, no GPU. multi-core multiprocess scales **linearly** because there's nothing to contend with. Measured 11 µs/op at dps=50 means a 1000-step polish per seed × 1000 seeds = 11 s serial, ~0.7 s parallel on multi-core.

**The router currently treats `mpmath` as Rule 1 (single-process sequential).** This is correct for any single polish, but for multistart-of-mpmath the rule should suggest multiprocess explicitly. Adding `mpmath-multistart` as a recognized workload could be a Goal 13+ refinement; for now, callers can pass `workload=multistart` with the mpmath caveat.

## What this changes about Phase 3 (autonomous loop) design

1. **Strategy picker should call `compute_router` programmatically** before launching any optimizer — exact-match calibration is now per-device, so the picker's decisions transfer across the Pro/Air/Max fleet.
2. **MPS f32 basin-hopping is a first-class default** for any problem where f32 precision is sufficient. The autonomous loop should prefer it over Modal CMA-ES f64 unless the problem is in the float64-ceiling tier.
3. **multistart workloads should auto-pin BLAS** via the orchestrator's env setup — drop the contention trap before it bites.
4. **The 96–120 GB LP band is uniquely local-friendly** on this hardware — Modal LP at that size would be more expensive and slower than the workstation.

## What we did NOT measure / open questions

- **Sustained MPS thermal throttle.** 4096³ f32 measurement is one-shot. Long-running MPS sessions (10+ min) may throttle as the chip heats. Modal A100s have data-center cooling — for >30-min sustained runs, this could matter. Worth a follow-up dedicated test if Phase 3 starts hammering MPS.
- **MPS f64.** PyTorch's MPS backend has historically not supported f64; recent versions emulate. We didn't test correctness or speed for the f64 emulation path. If it's competitive, it would shift Rule 3's threshold materially.
- **Modal A100 cost-vs-speedup for f32 workloads.** We assumed MPS at dominates, but actual cost-per-result on Modal could still be competitive at certain workload sizes. A direct benchmark would close the loop.
- **high-memory upper RAM headroom.** Calibration confirmed 96 GB allocatable in a single numpy array; we didn't push to 120/128. macOS will OOM-kill above some threshold — knowing it precisely tightens Rule 4.

## See also

- [.claude/rules/compute-router.md](../../../.claude/rules/compute-router.md) — authoritative decision matrix; this finding is the workstation-specific empirical addendum.
- [docs/wiki/techniques/compute-router.md](../techniques/compute-router.md) — public framing of the router.
- [docs/wiki/findings/gpu-modal-compute.md](gpu-modal-compute.md) — the prior finding about "running sequential Python on GPU wastes money"; this one is the dual: "running parallel float32 on CPU wastes time."
- [scripts/local_benchmark.py](../../../scripts/local_benchmark.py) — the measurement instrument.
- [scripts/compute_router.py](../../../scripts/compute_router.py) — where these findings should flow into routing rules.
- [docs/tools/calibrate.sh](../../tools/calibrate.sh) — recalibrate on this Mac or a new one (writes per-device).
