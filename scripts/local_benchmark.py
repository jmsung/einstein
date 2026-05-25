#!/usr/bin/env python3
"""local_benchmark.py — calibrate this a local workstation for the compute router.

Measures:
- CPU per-core throughput (numpy matmul, sequential)
- CPU multiprocess scaling (np.linalg per-worker)
- MPS (Apple Silicon GPU via PyTorch) batched float32 throughput
- RAM headroom (allocate large array, measure peak)
- mpmath sequential throughput (high-precision computation)

Output: prints calibration constants + writes to docs/agent/local-calibration.json
for compute_router.py to consume.

Run periodically (every few weeks) — calibration drifts with macOS updates,
torch versions, and machine state.
"""

from __future__ import annotations

import json
import multiprocessing as mp
import os
import platform
import sys
import time
from pathlib import Path

import numpy as np


def time_block(label: str, fn, *args, **kwargs):
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    dt = time.perf_counter() - t0
    print(f"  {label}: {dt:.3f}s")
    return dt, out


def cpu_single_core_matmul():
    """Single-thread numpy matmul throughput."""
    os.environ["OMP_NUM_THREADS"] = "1"
    n = 2048
    a = np.random.randn(n, n).astype(np.float64)
    b = np.random.randn(n, n).astype(np.float64)
    dt, _ = time_block("cpu single-thread matmul 2048^3", lambda: a @ b)
    return {"matmul_2048_seconds": dt, "gflops_estimate": (2 * n**3) / dt / 1e9}


def cpu_multicore_matmul():
    """Multi-thread (default OMP) matmul throughput."""
    if "OMP_NUM_THREADS" in os.environ:
        del os.environ["OMP_NUM_THREADS"]
    n = 4096
    a = np.random.randn(n, n).astype(np.float64)
    b = np.random.randn(n, n).astype(np.float64)
    dt, _ = time_block(f"cpu multi-thread matmul {n}^3", lambda: a @ b)
    return {"matmul_4096_seconds": dt, "gflops_estimate": (2 * n**3) / dt / 1e9}


_MP_WORKER_N = 2048      # bigger matrix — make the math dominate pickle overhead
_MP_WORKER_ITERS = 50    # 50 iters: serial workload ~5-10s, parallel should be ≤1s on multi-cores


_BLAS_THREAD_ENV = {
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "VECLIB_MAXIMUM_THREADS": "1",
}


def _mp_worker(_seed: int) -> float:
    """Module-level worker — picklable for macOS spawn-mode mp.Pool.

    BLAS thread caps must be set in the *parent* environment before this
    process is spawned; setting them here is too late (numpy already
    inherits whatever it sees at first import).
    """
    n = _MP_WORKER_N
    a = np.random.randn(n, n)
    b = np.random.randn(n, n)
    for _ in range(_MP_WORKER_ITERS):
        a = a @ b
    return float(a.sum())


def cpu_mp_scaling():
    """Measure speedup of N parallel processes vs single.

    Each worker is constrained to 1 BLAS thread so we measure process-level
    scaling, not thread oversubscription. Without this, 18 workers ×
    Accelerate-using-all-cores would produce ≈1× speedup (thread contention).
    """
    cores = mp.cpu_count()
    print(f"  cores reported: {cores}")
    # Set BLAS thread caps in parent env BEFORE spawning. macOS spawn-mode
    # inherits env at process start; setting these in-worker is too late.
    saved_env = {k: os.environ.get(k) for k in _BLAS_THREAD_ENV}
    os.environ.update(_BLAS_THREAD_ENV)
    try:
        ctx = mp.get_context("spawn")
        t0 = time.perf_counter()
        with ctx.Pool(processes=cores) as pool:
            list(pool.map(_mp_worker, range(cores)))
        dt_parallel = time.perf_counter() - t0
        t0 = time.perf_counter()
        [_mp_worker(0) for _ in range(cores)]
        dt_serial = time.perf_counter() - t0
    finally:
        for k, v in saved_env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    speedup = dt_serial / dt_parallel if dt_parallel > 0 else 0
    print(f"  mp scaling: {dt_serial:.2f}s serial vs {dt_parallel:.2f}s parallel ({speedup:.1f}x)")
    return {
        "cores": cores,
        "mp_speedup": speedup,
        "serial_seconds": dt_serial,
        "parallel_seconds": dt_parallel,
    }


def mps_throughput():
    """Apple Silicon GPU (MPS) float32 batched matmul."""
    try:
        import torch
    except ImportError:
        print("  torch not available; skipping MPS")
        return {"mps_available": False}
    if not torch.backends.mps.is_available():
        print("  MPS not available")
        return {"mps_available": False}
    n = 4096
    dev = torch.device("mps")
    a = torch.randn(n, n, dtype=torch.float32, device=dev)
    b = torch.randn(n, n, dtype=torch.float32, device=dev)
    # warm-up
    _ = a @ b
    torch.mps.synchronize()
    t0 = time.perf_counter()
    for _ in range(5):
        c = a @ b
    torch.mps.synchronize()
    dt = (time.perf_counter() - t0) / 5
    print(f"  MPS float32 matmul {n}^3: {dt:.3f}s/iter")
    return {
        "mps_available": True,
        "matmul_4096_f32_seconds": dt,
        "gflops_estimate": (2 * n**3) / dt / 1e9,
    }


def mpmath_seq_throughput():
    """Sequential mpmath (CPU-bound, high precision)."""
    try:
        import mpmath
    except ImportError:
        print("  mpmath not available; skipping")
        return {"mpmath_available": False}
    mpmath.mp.dps = 50
    n_iter = 1000
    t0 = time.perf_counter()
    s = mpmath.mpf(0)
    x = mpmath.mpf("1.234567890123456789")
    for i in range(n_iter):
        s = s + mpmath.sin(x * i) * mpmath.exp(-mpmath.mpf(i) / 100)
    dt = time.perf_counter() - t0
    print(f"  mpmath dps=50 {n_iter} ops: {dt:.3f}s")
    return {"mpmath_available": True, "dps50_1k_iters_seconds": dt}


def ram_headroom():
    """How much float64 we can allocate (one big contiguous array)."""
    # On high-memory unified-memory a local workstation, test up through 96GB — leave headroom
    # for the kernel + other processes. macOS will OOM-kill above ~100GB.
    sizes_gb = [1, 4, 16, 32, 64, 96]
    headroom = {}
    for gb in sizes_gb:
        try:
            n = int((gb * 1e9 / 8) ** 0.5)
            a = np.zeros((n, n), dtype=np.float64)
            del a
            headroom[f"{gb}GB"] = "ok"
        except MemoryError:
            headroom[f"{gb}GB"] = "fail"
            break
    print(f"  RAM headroom: {headroom}")
    return headroom


def _fingerprint_device() -> dict:
    """Capture the fields that compute_router uses to build the device key."""
    # Lazy import to avoid pulling scripts/ onto sys.path eagerly
    sys.path.insert(0, str(Path(__file__).parent))
    import compute_router as cr
    key = cr.device_key()
    return {
        "key": key,
        "brand": cr._sysctl("machdep.cpu.brand_string") or platform.processor() or "unknown",
        "cores": int(cr._sysctl("hw.ncpu") or "0"),
        "memory_bytes": int(cr._sysctl("hw.memsize") or "0"),
        "platform": platform.platform(),
        "hostname": platform.node(),
    }


def main():
    print("local_benchmark.py — device calibration")
    device = _fingerprint_device()
    print(f"  device:   {device['key']}  ({device['brand']}, {device['cores']} cores, "
          f"{device['memory_bytes'] // 1024**3} GB)")
    print(f"  python:   {sys.version.split()[0]}")
    print(f"  numpy:    {np.__version__}")
    print(f"  platform: {platform.platform()}")
    print()
    out: dict = {
        "version": 1,
        "timestamp": time.strftime("%Y-%m-%d"),
        "device": device,
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "numpy": np.__version__,
    }
    print("[1/5] CPU single-core matmul")
    out["cpu_single_core"] = cpu_single_core_matmul()
    print("[2/5] CPU multi-core matmul")
    out["cpu_multi_core"] = cpu_multicore_matmul()
    print("[3/5] CPU multiprocess scaling")
    out["cpu_mp_scaling"] = cpu_mp_scaling()
    print("[4/5] MPS GPU throughput")
    out["mps"] = mps_throughput()
    print("[5/5] mpmath sequential throughput")
    out["mpmath"] = mpmath_seq_throughput()
    print("[bonus] RAM headroom")
    out["ram"] = ram_headroom()
    print()

    cal_dir = Path(__file__).parent.parent / "docs" / "agent" / "calibrations"
    cal_dir.mkdir(parents=True, exist_ok=True)
    out_path = cal_dir / f"{device['key']}.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"calibration written to {out_path}")


if __name__ == "__main__":
    main()
