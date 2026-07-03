"""MPS smoke test — proves Apple Silicon GPU is healthy on this machine.

When `compute_router.py` routes a workload to `local-mps`, the assumption is
that MPS produces correct numerical results AND is faster than CPU. If a
torch / macOS update silently breaks the MPS backend (wrong results, or
order-of-magnitude regression), routed workloads would produce bad scores
on the arena. This test catches both classes of regression.

Skipped automatically on machines without MPS (Linux CI, Intel Macs).
"""
from __future__ import annotations

import time

import numpy as np
import pytest

torch = pytest.importorskip("torch")

if not torch.backends.mps.is_available():
    pytest.skip("MPS not available on this machine", allow_module_level=True)


@pytest.fixture(scope="module")
def mps_device():
    return torch.device("mps")


def test_mps_matmul_runs(mps_device) -> None:
    """Bare-minimum: a float32 matmul on MPS doesn't crash or return NaN."""
    n = 128
    a = torch.randn(n, n, dtype=torch.float32, device=mps_device)
    b = torch.randn(n, n, dtype=torch.float32, device=mps_device)
    c = a @ b
    torch.mps.synchronize()
    assert c.shape == (n, n)
    assert torch.isfinite(c).all().item(), "MPS produced NaN/Inf — backend broken"


def test_mps_matches_cpu_f32_matmul(mps_device) -> None:
    """MPS f32 result must match CPU f32 within float32 tolerance.

    Catches the failure mode where MPS silently returns the wrong numbers
    after a torch / macOS update. Tolerance is loose (1e-3 relative on a
    128² matmul of N(0,1) entries) — the test is for *gross* drift, not
    bit-exact agreement.
    """
    n = 128
    torch.manual_seed(0)
    a = torch.randn(n, n, dtype=torch.float32)
    b = torch.randn(n, n, dtype=torch.float32)

    cpu_out = (a @ b).cpu().numpy()
    mps_out = (a.to(mps_device) @ b.to(mps_device)).cpu().numpy()

    # Sample-relative comparison — both results are O(sqrt(n)) so direct
    # rtol works; we additionally inspect the worst element to be honest
    # about outliers.
    rel_err = np.abs(cpu_out - mps_out) / (np.abs(cpu_out) + 1e-6)
    assert rel_err.max() < 1e-3, (
        f"MPS f32 matmul diverges from CPU f32: worst rel err = {rel_err.max():.4g} "
        f"at index {np.unravel_index(rel_err.argmax(), rel_err.shape)}. "
        "Torch/macOS MPS backend may be broken — investigate before trusting "
        "compute_router.py local-mps recommendations."
    )


def test_mps_faster_than_cpu_for_large_f32_matmul(mps_device) -> None:
    """MPS should beat CPU on a 2048² float32 matmul, otherwise the router's
    'route batched f32 to local-mps' rule is uneconomical."""
    n = 2048
    a = torch.randn(n, n, dtype=torch.float32)
    b = torch.randn(n, n, dtype=torch.float32)

    # Warm up CPU + MPS
    _ = a @ b
    a_m, b_m = a.to(mps_device), b.to(mps_device)
    _ = a_m @ b_m
    torch.mps.synchronize()

    # CPU time
    t0 = time.perf_counter()
    for _ in range(3):
        _ = a @ b
    dt_cpu = (time.perf_counter() - t0) / 3

    # MPS time
    torch.mps.synchronize()
    t0 = time.perf_counter()
    for _ in range(3):
        _ = a_m @ b_m
    torch.mps.synchronize()
    dt_mps = (time.perf_counter() - t0) / 3

    # MPS should be at least 2× faster for this size; if not, MPS is
    # falling back to CPU silently or the MPS path has regressed.
    speedup = dt_cpu / dt_mps
    assert speedup >= 2.0, (
        f"MPS speedup over CPU for 2048² f32 matmul is only {speedup:.1f}× "
        f"(cpu={dt_cpu*1000:.1f}ms, mps={dt_mps*1000:.1f}ms). "
        "Expected ≥2× — torch may have stopped using MPS. "
        "Check torch.backends.mps.is_available() + torch version."
    )
