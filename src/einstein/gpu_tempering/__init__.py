"""GPU-accelerated parallel tempering SA — reusable across problems.

Provides a fused CUDA implementation of parallel tempering simulated annealing
for optimization on sphere manifolds. Eliminates Python loop overhead that
limits PyTorch-based implementations to ~35% GPU utilization.

Supports:
- Configurable loss functions (hinge overlap, Coulomb, custom)
- Configurable manifolds (sphere S^d, flat R^d)
- Batch parallel tempering with replica exchange
- Contribution-weighted sampling

Usage:
    from einstein.gpu_tempering import ParallelTemperingSA, HingeOverlapLoss, SphereManifold

    sa = ParallelTemperingSA(
        loss_fn=HingeOverlapLoss(),
        manifold=SphereManifold(dim=11),
        n_vectors=594,
        n_replicas=64,
        temps=(1e-12, 1e-4),
        scale=1e-6,
    )
    result = sa.run(initial_vectors, n_steps=1_000_000)
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
