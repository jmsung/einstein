---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P6, P9, P13, P22]
compute_profile: [local-cpu, local-mps, modal-gpu]
cost_estimate: "30s benchmark; deciding factor for GPU-hours"
hit_rate: "TBD"
---

# GPU Decision Framework

## TL;DR

Before any Modal GPU run, run `python -m einstein.gpu_tempering.benchmark --solution <path>` and follow its recommendation. The framework: GPU helps only when the inner loop is genuinely parallel AND tensors are large enough that kernel-launch overhead doesn't dominate. Sequential mpmath / NM / L-BFGS-B / single-replica greedy on GPU is wasted money and slower than CPU.

## When to apply

Before running anything on Modal — and before writing any new GPU script. Re-run the benchmark whenever algorithm, N, D, or hardware changes.

## Procedure

1. **Profile locally** — time each pipeline stage; identify the bottleneck.
2. **Categorize the bottleneck**:

   | Pattern | GPU-friendly? |
   |---|---|
   | Batch eval N candidates × M grid points | YES |
   | Sequential optimizer (NM, L-BFGS-B, mpmath) | NO |
   | CMA-ES / DE population eval | PARTIALLY (pop must be large) |
   | Matrix solve (N×N) | Only if N > ~100 |

3. **Run the benchmark**:
   ```bash
   python -m einstein.gpu_tempering.benchmark --solution <solution.json> --duration 30
   ```
   Outputs one of `STAY ON CPU` / `USE GPU VANILLA` / `USE GPU COMPILED` / `CONSIDER TRITON`.

4. **Cost gate**: estimate `hours × $/hr`. Only proceed if expected speedup > 3× over local.

5. **Verify on Modal**: target GPU utilization > 50%. Below 50%, Python overhead dominates — stronger GPU will not help; only kernel fusion (torch.compile / Triton) will.

## The three GPU levels

| Level | Approach | Effort | Typical Speedup | When |
|---|---|---|---|---|
| 1 | Vanilla PyTorch | 1 hr | 5–20× over CPU | First GPU attempt |
| 2 | torch.compile | 1 line | 1.5–5× over L1 | Always try — free |
| 3 | Triton kernel | 1–3 days | 3–10× over L2 | Only if util < 50% AND reused |

Use the existing module `src/einstein/gpu_tempering/` (tested on P6, 16-test coverage):

```python
from einstein.gpu_tempering import run_fused_tempering
result = run_fused_tempering(
    vectors,                    # (N, D) numpy array
    n_replicas=64,
    n_steps=200_000,
    k_per_step=5,               # K=5 safe for Jacobi; K=50 breaks at high overlap
    scale=1e-6,
    loss_type="hinge",          # or "coulomb" for Thomson
)
```

## Pitfalls

- **Sequential Python on GPU**: GPU sits idle while Python dispatches one tiny op at a time. Costs $/hr, slower than CPU. Most common GPU mistake in this repo.
- **Stronger-GPU doesn't help when util < 50%**: bottleneck is Python overhead, not FLOPs. H100 = no faster than A100 in this regime.
- **K-step batching limit**: P6 fused-tempering K=50 breaks the Jacobi approximation (K=5 safe). Test correctness at every K before scaling.
- **mpmath on GPU**: arbitrary precision is CPU-only. Putting an mpmath polish loop on Modal wastes 100% of the GPU.
- **Small populations**: CMA-ES with pop=11 won't saturate even a single GPU core. Need pop ≥ 256 for serious GPU use.

## Compute profile

This page IS the routing layer. Decision tree:

```
Run benchmark →
  GPU < 3× CPU?         → Stay on CPU
  GPU > 3× CPU? Check util:
    util > 70%?         → Use compiled. Compute-bound. Done.
    util 50–70%?        → Use compiled. Triton optional.
    util < 50%?         → Python overhead dominates.
      One-off problem?  → Use compiled, accept inefficiency.
      Will reuse?       → Build Triton.
```

Measured P6 (A100, N=594, D=11, R=64):
- CPU baseline: 31K p/s
- GPU vanilla (L1): 28K p/s (kernel-launch bound)
- GPU fused K=5 (L2): 131K p/s ← **recommended default**
- GPU fused K=50 (L2): 1.2M p/s (Jacobi breaks at high K)
- Triton (L3): built; auto-falls back to L2 if Triton not installed

## References

- `mb/wiki/cross-problem-lessons-gpu.md` (source — full decision matrix + per-problem audits).
- `wiki/findings/gpu-modal-compute.md` (lesson #26 Python overhead, lesson #63 Modal BnB economics, GIL pitfall).
- `wiki/techniques/compute-router.md` (broader local-vs-cloud routing including non-GPU workloads).
- `src/einstein/gpu_tempering/` (production module: `core.py`, `fused_step.py`, `triton_kernel.py`, `benchmark.py`).
