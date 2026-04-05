"""Loss functions for GPU parallel tempering.

Each loss function must implement:
- full_loss(vecs) → scalar: O(n²) full evaluation
- incremental_delta(vecs, idx, old_vec) → scalar: O(n) delta after modifying vecs[idx]
- contributions(vecs) → (n,) tensor: per-vector contribution for weighted sampling
"""

import torch


class HingeOverlapLoss:
    """Kissing number overlap loss: sum_{i<j} max(0, 2 - dist(c_i, c_j)).

    Used for sphere packing / kissing number problems.
    Centers at c_i = 2 * v_i (unit vectors on S^d).
    """

    def full_loss(self, vecs: torch.Tensor) -> torch.Tensor:
        """O(n²) full loss evaluation."""
        n = vecs.shape[0]
        gram = vecs @ vecs.T
        idx_i, idx_j = torch.triu_indices(n, n, offset=1, device=vecs.device)
        cos_vals = gram[idx_i, idx_j].clamp(-1.0, 1.0)
        dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=0.0))
        return torch.clamp(2.0 - dists, min=0.0).sum()

    def incremental_delta(
        self, vecs: torch.Tensor, idx: int, old_vec: torch.Tensor
    ) -> torch.Tensor:
        """O(n) delta loss after vecs[idx] was modified. Returns new_loss - old_loss."""
        others = torch.cat([vecs[:idx], vecs[idx + 1 :]], dim=0)

        old_cos = (old_vec @ others.T).clamp(-1.0, 1.0)
        old_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - old_cos, min=0.0))
        old_p = torch.clamp(2.0 - old_d, min=0.0).sum()

        new_cos = (vecs[idx] @ others.T).clamp(-1.0, 1.0)
        new_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - new_cos, min=0.0))
        new_p = torch.clamp(2.0 - new_d, min=0.0).sum()

        return new_p - old_p

    def batch_incremental_delta(
        self,
        vecs_batch: torch.Tensor,
        indices: torch.Tensor,
        old_vecs: torch.Tensor,
    ) -> torch.Tensor:
        """Vectorized batch incremental delta across R replicas.
        vecs_batch: (R, N, D), indices: (R,), old_vecs: (R, D)
        Returns: (R,) tensor of deltas
        """
        R = vecs_batch.shape[0]
        device = vecs_batch.device
        batch_idx = torch.arange(R, device=device)

        new_vecs = vecs_batch[batch_idx, indices]

        old_dots = torch.bmm(old_vecs.unsqueeze(1), vecs_batch.transpose(1, 2)).squeeze(1)
        new_dots = torch.bmm(new_vecs.unsqueeze(1), vecs_batch.transpose(1, 2)).squeeze(1)

        old_dots[batch_idx, indices] = -1.0
        new_dots[batch_idx, indices] = -1.0

        old_cos = old_dots.clamp(-1.0, 1.0)
        old_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - old_cos, min=0.0))
        old_p = torch.clamp(2.0 - old_d, min=0.0).sum(dim=1)

        new_cos = new_dots.clamp(-1.0, 1.0)
        new_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - new_cos, min=0.0))
        new_p = torch.clamp(2.0 - new_d, min=0.0).sum(dim=1)

        return new_p - old_p

    def contributions(self, vecs: torch.Tensor) -> torch.Tensor:
        """Per-vector contribution to total loss for weighted sampling."""
        n = vecs.shape[0]
        device = vecs.device
        gram = vecs @ vecs.T
        idx_i, idx_j = torch.triu_indices(n, n, offset=1, device=device)
        cos_vals = gram[idx_i, idx_j].clamp(-1.0, 1.0)
        dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=0.0))
        pens = torch.clamp(2.0 - dists, min=0.0)
        c = torch.zeros(n, device=device, dtype=vecs.dtype)
        c.scatter_add_(0, idx_i, pens)
        c.scatter_add_(0, idx_j, pens)
        return c


class CoulombLoss:
    """Thomson problem Coulomb energy: sum_{i<j} 1/dist(p_i, p_j).

    Used for Thomson problem (points on S^2 or S^d).
    """

    def full_loss(self, vecs: torch.Tensor) -> torch.Tensor:
        n = vecs.shape[0]
        diff = vecs.unsqueeze(0) - vecs.unsqueeze(1)  # (N, N, D)
        dist_sq = (diff * diff).sum(dim=2)  # (N, N)
        idx_i, idx_j = torch.triu_indices(n, n, offset=1, device=vecs.device)
        dists = torch.sqrt(dist_sq[idx_i, idx_j]).clamp(min=1e-12)
        return (1.0 / dists).sum()

    def incremental_delta(
        self, vecs: torch.Tensor, idx: int, old_vec: torch.Tensor
    ) -> torch.Tensor:
        others = torch.cat([vecs[:idx], vecs[idx + 1 :]], dim=0)

        old_dists = torch.norm(old_vec - others, dim=1).clamp(min=1e-12)
        old_e = (1.0 / old_dists).sum()

        new_dists = torch.norm(vecs[idx] - others, dim=1).clamp(min=1e-12)
        new_e = (1.0 / new_dists).sum()

        return new_e - old_e

    def batch_incremental_delta(
        self,
        vecs_batch: torch.Tensor,
        indices: torch.Tensor,
        old_vecs: torch.Tensor,
    ) -> torch.Tensor:
        R, N, D = vecs_batch.shape
        device = vecs_batch.device
        batch_idx = torch.arange(R, device=device)

        new_vecs = vecs_batch[batch_idx, indices]  # (R, D)

        # Old distances: (R, N)
        old_diff = old_vecs.unsqueeze(1) - vecs_batch  # (R, 1, D) - (R, N, D)
        old_dist = old_diff.norm(dim=2).clamp(min=1e-12)
        old_dist[batch_idx, indices] = 1e12  # exclude self
        old_e = (1.0 / old_dist).sum(dim=1)

        new_diff = new_vecs.unsqueeze(1) - vecs_batch
        new_dist = new_diff.norm(dim=2).clamp(min=1e-12)
        new_dist[batch_idx, indices] = 1e12
        new_e = (1.0 / new_dist).sum(dim=1)

        return new_e - old_e

    def contributions(self, vecs: torch.Tensor) -> torch.Tensor:
        n = vecs.shape[0]
        device = vecs.device
        diff = vecs.unsqueeze(0) - vecs.unsqueeze(1)
        dist_sq = (diff * diff).sum(dim=2)
        idx_i, idx_j = torch.triu_indices(n, n, offset=1, device=device)
        dists = torch.sqrt(dist_sq[idx_i, idx_j]).clamp(min=1e-12)
        energies = 1.0 / dists
        c = torch.zeros(n, device=device, dtype=vecs.dtype)
        c.scatter_add_(0, idx_i, energies)
        c.scatter_add_(0, idx_j, energies)
        return c
