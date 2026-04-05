"""GPU-accelerated parallel tempering SA — reusable across problems.

Eliminates Python loop overhead that limits PyTorch implementations to
~35% GPU utilization. Three execution levels (benchmark to choose):

  Level 1: Vanilla PyTorch    — ParallelTemperingSA.run()
  Level 2: Fused R×K step     — run_fused_tempering()    [131K p/s on A100]
  Level 3: Triton kernel      — run_triton_tempering()   [auto-fallback to L2]

Quick start:
    # 1. Benchmark to pick the right approach:
    python -m einstein.gpu_tempering.benchmark --solution <path>

    # 2. Use the recommended runner:
    from einstein.gpu_tempering import run_fused_tempering
    result = run_fused_tempering(
        vectors,              # (N, D) numpy array
        n_replicas=64,        # parallel SA replicas
        n_steps=200_000,      # outer steps (each does R×K perturbations)
        k_per_step=5,         # perturbations per replica per step
        scale=1e-6,           # perturbation magnitude
        loss_type="hinge",    # "hinge" (kissing) or "coulomb" (Thomson)
    )

Supported loss functions:
    - HingeOverlapLoss: kissing number / sphere packing
    - CoulombLoss: Thomson problem
    - Custom: register via fused_step.DELTA_FNS["name"] = your_fn

Supported manifolds:
    - SphereManifold(dim): unit sphere S^{dim-1}
    - FlatManifold(dim): unconstrained R^dim
"""

from einstein.gpu_tempering.core import ParallelTemperingSA
from einstein.gpu_tempering.losses import HingeOverlapLoss, CoulombLoss
from einstein.gpu_tempering.manifolds import SphereManifold, FlatManifold
from einstein.gpu_tempering.fused_step import fused_sa_step, run_fused_tempering
from einstein.gpu_tempering.triton_kernel import triton_sa_step, run_triton_tempering

__all__ = [
    "ParallelTemperingSA",
    "HingeOverlapLoss",
    "CoulombLoss",
    "SphereManifold",
    "FlatManifold",
    "fused_sa_step",
    "run_fused_tempering",
    "triton_sa_step",
    "run_triton_tempering",
]
