"""Tests for the reusable GPU parallel tempering module."""

import numpy as np
import pytest
import torch

from einstein.gpu_tempering import (
    CoulombLoss,
    FlatManifold,
    HingeOverlapLoss,
    ParallelTemperingSA,
    SphereManifold,
)
from einstein.gpu_tempering.core import TemperingConfig


class TestHingeOverlapLoss:
    def test_orthogonal_zero(self):
        """11 orthogonal unit vectors have no overlap."""
        vecs = torch.eye(11, dtype=torch.float64)
        loss = HingeOverlapLoss()
        assert loss.full_loss(vecs).item() == pytest.approx(0.0, abs=1e-10)

    def test_identical_positive(self):
        """Identical vectors have positive penalty."""
        vecs = torch.randn(10, 5, dtype=torch.float64)
        vecs = vecs / vecs.norm(dim=1, keepdim=True)
        # Make two vectors identical
        vecs[1] = vecs[0]
        loss = HingeOverlapLoss()
        assert loss.full_loss(vecs).item() > 0

    def test_incremental_matches_full(self):
        """Incremental delta matches full loss recomputation."""
        rng = np.random.default_rng(42)
        vecs = torch.randn(20, 5, dtype=torch.float64)
        vecs = vecs / vecs.norm(dim=1, keepdim=True)

        loss = HingeOverlapLoss()
        old_loss = loss.full_loss(vecs).item()

        idx = 7
        old_vec = vecs[idx].clone()
        vecs[idx] += torch.randn(5, dtype=torch.float64) * 0.01
        vecs[idx] /= vecs[idx].norm()

        delta = loss.incremental_delta(vecs, idx, old_vec).item()
        new_loss = loss.full_loss(vecs).item()

        assert delta == pytest.approx(new_loss - old_loss, abs=1e-10)

    def test_batch_incremental_matches(self):
        """Batch incremental matches single incremental."""
        vecs = torch.randn(20, 5, dtype=torch.float64)
        vecs = vecs / vecs.norm(dim=1, keepdim=True)

        loss = HingeOverlapLoss()
        R = 4
        batch = vecs.unsqueeze(0).expand(R, -1, -1).clone()
        indices = torch.tensor([3, 7, 12, 1])
        old_vecs = batch[torch.arange(R), indices].clone()

        # Perturb
        batch[torch.arange(R), indices] += torch.randn(R, 5, dtype=torch.float64) * 0.01
        batch[torch.arange(R), indices] /= batch[torch.arange(R), indices].norm(dim=1, keepdim=True)

        deltas = loss.batch_incremental_delta(batch, indices, old_vecs)

        # Compare with single incremental for each
        for r in range(R):
            single = loss.incremental_delta(batch[r], indices[r].item(), old_vecs[r])
            assert deltas[r].item() == pytest.approx(single.item(), abs=1e-8)

    def test_contributions_nonnegative(self):
        vecs = torch.randn(50, 11, dtype=torch.float64)
        vecs = vecs / vecs.norm(dim=1, keepdim=True)
        c = HingeOverlapLoss().contributions(vecs)
        assert (c >= 0).all()


class TestCoulombLoss:
    def test_two_points_energy(self):
        """Two antipodal points on S^2 have distance 2, energy 0.5."""
        vecs = torch.tensor([[0, 0, 1.0], [0, 0, -1.0]], dtype=torch.float64)
        e = CoulombLoss().full_loss(vecs).item()
        assert e == pytest.approx(0.5, abs=1e-10)

    def test_incremental_matches_full(self):
        vecs = torch.randn(20, 3, dtype=torch.float64)
        vecs = vecs / vecs.norm(dim=1, keepdim=True)

        loss = CoulombLoss()
        old_e = loss.full_loss(vecs).item()

        idx = 5
        old_vec = vecs[idx].clone()
        vecs[idx] = torch.randn(3, dtype=torch.float64)
        vecs[idx] /= vecs[idx].norm()

        delta = loss.incremental_delta(vecs, idx, old_vec).item()
        new_e = loss.full_loss(vecs).item()

        assert delta == pytest.approx(new_e - old_e, abs=1e-8)


class TestSphereManifold:
    def test_project_normalizes(self):
        vecs = torch.randn(10, 5, dtype=torch.float64) * 3
        m = SphereManifold(dim=5)
        proj = m.project(vecs)
        norms = proj.norm(dim=1)
        assert torch.allclose(norms, torch.ones(10, dtype=torch.float64), atol=1e-10)

    def test_perturb_stays_on_sphere(self):
        vecs = torch.randn(3, 10, 5, dtype=torch.float64)
        vecs = vecs / vecs.norm(dim=2, keepdim=True)
        m = SphereManifold(dim=5)
        indices = torch.tensor([2, 5, 8])
        m.perturb_batch(vecs, indices, scale=0.01)
        norms = vecs[torch.arange(3), indices].norm(dim=1)
        assert torch.allclose(norms, torch.ones(3, dtype=torch.float64), atol=1e-10)


class TestParallelTemperingSA:
    def test_small_run(self):
        """Smoke test: run a tiny SA and verify it returns a valid result."""
        rng = np.random.default_rng(42)
        vecs = rng.standard_normal((20, 5))
        vecs /= np.linalg.norm(vecs, axis=1, keepdims=True)

        cfg = TemperingConfig(
            n_replicas=4,
            n_steps=100,
            k_per_step=5,
            scale=1e-3,
            report_every=50,
            recompute_every=50,
            timeout_sec=30,
            use_compile=False,
        )
        sa = ParallelTemperingSA(
            loss_fn=HingeOverlapLoss(),
            manifold=SphereManifold(dim=5),
            n_vectors=20,
            config=cfg,
        )
        result = sa.run(vecs, device="cpu")

        assert result.best_score <= result.initial_score
        assert result.best_vectors.shape == (20, 5)
        assert result.elapsed_seconds > 0
        assert result.total_perturbations == 100 * 4 * 5


class TestFusedStep:
    def test_fused_step_runs(self):
        """Smoke test: fused step runs without error."""
        from einstein.gpu_tempering.fused_step import fused_sa_step

        R, N, D, K = 4, 20, 5, 3
        replicas = torch.randn(R, N, D, dtype=torch.float64)
        replicas = replicas / replicas.norm(dim=2, keepdim=True)
        losses = torch.tensor([HingeOverlapLoss().full_loss(replicas[r]).item() for r in range(R)],
                              dtype=torch.float64)
        temps = torch.tensor([1e-12, 1e-8, 1e-4, 1e-2], dtype=torch.float64)
        probs = torch.ones(N, dtype=torch.float64) / N

        new_losses, n_acc = fused_sa_step(replicas, losses, temps, probs, 1e-3, K, "hinge")

        assert new_losses.shape == (R,)
        assert 0 <= n_acc <= R * K

    def test_fused_step_coulomb(self):
        """Fused step works with Coulomb loss."""
        from einstein.gpu_tempering.fused_step import fused_sa_step

        R, N, D, K = 4, 20, 3, 5
        replicas = torch.randn(R, N, D, dtype=torch.float64)
        replicas = replicas / replicas.norm(dim=2, keepdim=True)
        losses = torch.tensor([CoulombLoss().full_loss(replicas[r]).item() for r in range(R)],
                              dtype=torch.float64)
        temps = torch.tensor([1e-12, 1e-8, 1e-4, 1e-2], dtype=torch.float64)
        probs = torch.ones(N, dtype=torch.float64) / N

        new_losses, n_acc = fused_sa_step(replicas, losses, temps, probs, 1e-3, K, "coulomb")
        assert new_losses.shape == (R,)

    def test_fused_custom_loss(self):
        """Can register and use a custom loss type."""
        from einstein.gpu_tempering.fused_step import DELTA_FNS, fused_sa_step

        # Register a dummy loss that always returns 0 delta
        def dummy_delta(old_dots, new_dots, flat_indices, RK, device):
            return torch.zeros(RK, device=device, dtype=old_dots.dtype)

        DELTA_FNS["dummy"] = dummy_delta

        R, N, D, K = 2, 10, 3, 2
        replicas = torch.randn(R, N, D, dtype=torch.float64)
        replicas = replicas / replicas.norm(dim=2, keepdim=True)
        losses = torch.zeros(R, dtype=torch.float64)
        temps = torch.tensor([1e-12, 1e-4], dtype=torch.float64)
        probs = torch.ones(N, dtype=torch.float64) / N

        new_losses, n_acc = fused_sa_step(replicas, losses, temps, probs, 1e-3, K, "dummy")
        # All deltas are 0, so all should be accepted
        assert n_acc == R * K

        del DELTA_FNS["dummy"]


def test_init():
    pass
