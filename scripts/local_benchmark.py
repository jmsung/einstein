#!/usr/bin/env python3
"""local_benchmark.py — calibrate this M5 Max for the compute router.

Measures:
- CPU per-core throughput (numpy matmul, sequential)
- CPU multiprocess scaling (np.linalg per-worker)
- MPS (Apple Silicon GPU via PyTorch) batched float32 throughput
- RAM headroom (allocate large array, measure peak)
- mpmath sequential throughput (high-precision computation)

Output: prints calibration constants + writes to agent/local-calibration.json
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


def cpu_mp_scaling():
    """Measure speedup of N parallel processes vs single."""
    n = 1024
    iters_per = 10

    def worker(_):
        a = np.random.randn(n, n)
        b = np.random.randn(n, n)
        for _ in range(iters_per):
            a = a @ b
        return float(a.sum())

    cores = mp.cpu_count()
    print(f"  cores reported: {cores}")
    t0 = time.perf_counter()
    with mp.Pool(processes=cores) as pool:
        list(pool.map(worker, range(cores)))
    dt_parallel = time.perf_counter() - t0
    t0 = time.perf_counter()
    [worker(0) for _ in range(cores)]
    dt_serial = time.perf_counter() - t0
    speedup = dt_serial / dt_parallel if dt_parallel > 0 else 0
    print(f"  mp scaling: {dt_serial:.2f}s serial vs {dt_parallel:.2f}s parallel ({speedup:.1f}x)")
    return {"cores": cores, "mp_speedup": speedup, "serial_seconds": dt_serial, "parallel_seconds": dt_parallel}


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
    return {"mps_available": True, "matmul_4096_f32_seconds": dt, "gflops_estimate": (2 * n**3) / dt / 1e9}


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
    """How much float64 we can allocate."""
    sizes_gb = [1, 4, 16, 32, 64]
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


def main():
    print("local_benchmark.py — M5 Max calibration")
    print(f"  python:   {sys.version.split()[0]}")
    print(f"  numpy:    {np.__version__}")
    print(f"  platform: {platform.platform()}")
    print()
    out: dict = {
        "version": 1,
        "timestamp": time.strftime("%Y-%m-%d"),
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

    out_path = Path(__file__).parent.parent / "agent" / "local-calibration.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"calibration written to {out_path}")


if __name__ == "__main__":
    main()
