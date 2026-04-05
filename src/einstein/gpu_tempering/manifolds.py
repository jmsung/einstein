"""Manifold constraints for GPU parallel tempering.

Each manifold must implement:
- project(vecs) → projected vecs: retract to manifold
- perturb(vecs, indices, scale, rng) → perturbed vecs: add noise and project
"""

import torch


class SphereManifold:
    """Unit sphere S^{dim-1} in R^dim. Each vector has unit norm."""

    def __init__(self, dim: int):
        self.dim = dim

    def project(self, vecs: torch.Tensor) -> torch.Tensor:
        """Project vectors to unit sphere (normalize)."""
        return vecs / vecs.norm(dim=-1, keepdim=True).clamp(min=1e-30)

    def perturb_batch(
        self,
        vecs_batch: torch.Tensor,
        indices: torch.Tensor,
        scale: float,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Perturb one vector per replica in-place, return old vectors.
        vecs_batch: (R, N, D), indices: (R,)
        Returns: old_vecs (R, D)
        """
        R = vecs_batch.shape[0]
        device = vecs_batch.device
        batch_idx = torch.arange(R, device=device)

        old_vecs = vecs_batch[batch_idx, indices].clone()

        noise = torch.randn(R, self.dim, device=device, dtype=vecs_batch.dtype) * scale
        vecs_batch[batch_idx, indices] += noise
        norms = vecs_batch[batch_idx, indices].norm(dim=1, keepdim=True).clamp(min=1e-30)
        vecs_batch[batch_idx, indices] /= norms

        return old_vecs


class FlatManifold:
    """Flat R^dim — no constraint. Vectors can have any norm."""

    def __init__(self, dim: int):
        self.dim = dim

    def project(self, vecs: torch.Tensor) -> torch.Tensor:
        return vecs  # no projection needed

    def perturb_batch(
        self,
        vecs_batch: torch.Tensor,
        indices: torch.Tensor,
        scale: float,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        R = vecs_batch.shape[0]
        device = vecs_batch.device
        batch_idx = torch.arange(R, device=device)

        old_vecs = vecs_batch[batch_idx, indices].clone()

        noise = torch.randn(R, self.dim, device=device, dtype=vecs_batch.dtype) * scale
        vecs_batch[batch_idx, indices] += noise

        return old_vecs
