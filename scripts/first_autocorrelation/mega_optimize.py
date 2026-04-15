"""Mega optimizer for P2 First Autocorrelation — pull out all stops.

Strategy:
1. Start from SOTA at n=30000
2. L-BFGS cascade with aggressive betas at native resolution
3. Block-repeat to larger n (60000, 90000) and optimize
4. Multi-resolution cycling for basin escaping
5. Noise-perturbed restarts for diversity
6. Final exact polish on the best solution

Usage:
    uv run python scripts/first_autocorrelation/mega_optimize.py \
        --warmstart results/problem-2-first-autocorrelation/sol-01-*.json \
        --out results/problem-2-first-autocorrelation/mega_best.json
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.first_autocorrelation.evaluator import verify_and_compute
from einstein.first_autocorrelation.optimizer import (
    autoconv_fft,
    exact_score_f,
    smooth_max,
    surrogate_v,
    to_v,
    upsample,
)


# ── helpers ──────────────────────────────────────────────────────────────

def block_repeat(f: np.ndarray, n_target: int) -> np.ndarray:
    assert n_target % len(f) == 0
    return np.repeat(f, n_target // len(f))


def block_average_down(f: np.ndarray, n_target: int) -> np.ndarray:
    assert len(f) % n_target == 0
    block = len(f) // n_target
    return f.reshape(n_target, block).mean(axis=1)


def save_best(f: np.ndarray, score: float, path: Path, tag: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        json.dump({"values": f.tolist(), "score": score, "n": len(f), "tag": tag}, fh)


# ── L-BFGS cascade ──────────────────────────────────────────────────────

def lbfgs_cascade(v_np: np.ndarray, betas: list[float], iters: int,
                  lr: float = 1.0, history_size: int = 200) -> tuple[np.ndarray, float]:
    """Run L-BFGS cascade over smooth surrogate, return (f, exact_score)."""
    v = torch.tensor(v_np.copy(), dtype=torch.float64, requires_grad=True)
    best_c = float("inf")
    best_v = v_np.copy()

    for beta in betas:
        opt = torch.optim.LBFGS(
            [v], lr=lr, max_iter=iters, tolerance_grad=1e-15,
            tolerance_change=1e-20, history_size=history_size,
            line_search_fn="strong_wolfe",
        )
        def closure():
            opt.zero_grad()
            loss = surrogate_v(v, beta, fft=True)
            loss.backward()
            return loss
        opt.step(closure)
        f_np = np.exp(v.detach().cpu().numpy()).astype(np.float64)
        c = exact_score_f(f_np)
        if c < best_c:
            best_c = c
            best_v = v.detach().cpu().numpy().copy()

    best_f = np.exp(best_v).astype(np.float64)
    return best_f, best_c


def multi_peak_polish(f: np.ndarray, iters: int = 200, topk: int = 500,
                      lr0: float = 1e-5) -> tuple[np.ndarray, float]:
    """Subgradient polish on top-K peaks simultaneously."""
    f = f.astype(np.float64).copy()
    n = len(f)
    dx = 0.5 / n
    best_c = exact_score_f(f)
    best_f = f.copy()
    lr = lr0
    no_improve = 0

    for it in range(iters):
        s = f.sum()
        m = 2 * n - 1
        m_pad = 1 << (m - 1).bit_length()
        F = np.fft.rfft(f, n=m_pad)
        conv = np.fft.irfft(F * F, n=m_pad)[:m]
        ratios = conv * dx / (s * dx) ** 2

        top_idx = np.argpartition(ratios, -topk)[-topk:]
        top_vals = ratios[top_idx]
        max_val = top_vals.max()

        beta = 1e8
        z = beta * (top_vals - max_val)
        w = np.exp(np.clip(z, -500, 0))
        w /= w.sum()

        mirror_sum = np.zeros(n, dtype=np.float64)
        c_sum = 0.0
        for wi, ti in zip(w, top_idx):
            if wi < 1e-20:
                continue
            lo = max(0, ti - (n - 1))
            hi = min(n - 1, ti)
            i_idx = np.arange(lo, hi + 1)
            j_idx = ti - i_idx
            mirror_sum[i_idx] += wi * f[j_idx]
            c_sum += wi * ratios[ti]
        grad = (2.0 * mirror_sum) / (s * s * dx) - (2.0 * c_sum) / s

        active = (f > 1e-30) | (grad < 0)
        step = np.where(active, -grad, 0.0)
        gnorm = np.linalg.norm(step)
        if gnorm < 1e-30:
            break
        d = step / gnorm

        accepted = False
        for _ in range(60):
            f_try = np.maximum(f + lr * d, 0.0)
            if f_try.sum() <= 0:
                lr *= 0.5
                continue
            c_try = exact_score_f(f_try)
            if c_try < best_c:
                f = f_try
                best_c = c_try
                best_f = f.copy()
                lr = min(lr * 1.3, lr0 * 10)
                accepted = True
                no_improve = 0
                break
            lr *= 0.5
        if not accepted:
            no_improve += 1
            lr = lr0
            if no_improve >= 8:
                break

    return best_f, best_c


# ── Phase 1: Aggressive L-BFGS at native n ──────────────────────────────

def phase1_native_lbfgs(f0: np.ndarray, seeds: int = 8) -> tuple[np.ndarray, float]:
    """L-BFGS from SOTA at native n with multiple noise seeds."""
    n = len(f0)
    best_c = exact_score_f(f0)
    best_f = f0.copy()
    print(f"\n=== Phase 1: Native L-BFGS at n={n} ===")
    print(f"Starting C = {best_c:.18f}")

    betas_aggressive = [1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14]

    for seed in range(seeds):
        rng = np.random.default_rng(seed)
        v0 = to_v(f0, floor=1e-30)
        noise_scale = 1e-3 if seed > 0 else 0.0
        if noise_scale > 0:
            v0 = v0 + rng.normal(scale=noise_scale, size=v0.shape)

        t0 = time.time()
        f_new, c_new = lbfgs_cascade(v0, betas_aggressive, iters=2000,
                                      history_size=200)
        dt = time.time() - t0
        tag = ""
        if c_new < best_c:
            delta = best_c - c_new
            best_c = c_new
            best_f = f_new.copy()
            tag = f"  *** NEW BEST  Δ={delta:.3e}"
        print(f"  seed={seed} noise={noise_scale:.0e} C={c_new:.18f} "
              f"({dt:.1f}s){tag}", flush=True)

    return best_f, best_c


# ── Phase 2: Higher resolution ───────────────────────────────────────────

def phase2_higher_resolution(f0: np.ndarray, n_targets: list[int],
                             seeds: int = 3) -> tuple[np.ndarray, float]:
    """Upsample to higher n and optimize there."""
    best_c = exact_score_f(f0)
    best_f = f0.copy()
    best_n = len(f0)
    n_src = len(f0)
    print(f"\n=== Phase 2: Higher Resolution ===")
    print(f"Starting C = {best_c:.18f} at n={n_src}")

    betas = [1e8, 1e9, 1e10, 1e11, 1e12, 1e13]

    for n_target in n_targets:
        if n_target % n_src == 0:
            f_up = block_repeat(f0, n_target)
        else:
            f_up = upsample(f0, n_target)
        c_up = exact_score_f(f_up)
        print(f"\n  n={n_target}: upsampled C={c_up:.18f}")

        for seed in range(seeds):
            rng = np.random.default_rng(42 + seed)
            v0 = to_v(f_up, floor=1e-30)
            if seed > 0:
                v0 = v0 + rng.normal(scale=1e-3, size=v0.shape)

            t0 = time.time()
            f_new, c_new = lbfgs_cascade(v0, betas, iters=1500, history_size=150)
            dt = time.time() - t0
            tag = ""
            if c_new < best_c:
                delta = best_c - c_new
                best_c = c_new
                best_f = f_new.copy()
                best_n = n_target
                tag = f"  *** NEW BEST  Δ={delta:.3e}"
            print(f"    seed={seed} C={c_new:.18f} ({dt:.1f}s){tag}", flush=True)

    print(f"  Phase 2 best: C={best_c:.18f} at n={best_n}")
    return best_f, best_c


# ── Phase 3: Multi-resolution cycling ────────────────────────────────────

def phase3_cycling(f0: np.ndarray, cycles: int = 3) -> tuple[np.ndarray, float]:
    """Cycle through different n values for basin escaping."""
    best_c = exact_score_f(f0)
    best_f = f0.copy()
    f_current = f0.copy()
    print(f"\n=== Phase 3: Multi-Resolution Cycling ===")
    print(f"Starting C = {best_c:.18f}")

    # Choose n values that are NOT multiples of the current n to force resampling
    ns = [29997, 30007, 30011, 30013, 29989, 29999, 30001, 30000,
          60000, 45000, 50000]
    betas = [1e9, 1e10, 1e11, 1e12, 1e13]

    for cyc in range(cycles):
        for n_target in ns:
            f_resized = upsample(f_current, n_target)
            v0 = to_v(f_resized, floor=1e-30)
            f_new, c_new = lbfgs_cascade(v0, betas, iters=1200, history_size=100)
            tag = ""
            if c_new < best_c:
                delta = best_c - c_new
                best_c = c_new
                best_f = f_new.copy()
                tag = f"  *** NEW BEST  Δ={delta:.3e}"
            f_current = f_new
            print(f"  cycle={cyc} n={n_target:>6} C={c_new:.18f}{tag}", flush=True)

    return best_f, best_c


# ── Phase 4: Final polish ────────────────────────────────────────────────

def phase4_polish(f0: np.ndarray, rounds: int = 5) -> tuple[np.ndarray, float]:
    """Alternating cascade + multi-peak polish."""
    best_c = exact_score_f(f0)
    best_f = f0.copy()
    f = f0.copy()
    print(f"\n=== Phase 4: Final Polish ===")
    print(f"Starting C = {best_c:.18f}")

    for r in range(rounds):
        # Cascade
        v0 = to_v(f, floor=1e-30)
        f, c_cas = lbfgs_cascade(v0, [1e10, 1e11, 1e12, 1e13, 1e14], iters=3000,
                                  history_size=250)
        if c_cas < best_c:
            best_c = c_cas
            best_f = f.copy()
        print(f"  round {r}: cascade C={c_cas:.18f}", flush=True)

        # Multi-peak polish
        f, c_pol = multi_peak_polish(f, iters=300, topk=500, lr0=1e-5)
        if c_pol < best_c:
            best_c = c_pol
            best_f = f.copy()
        print(f"  round {r}: polish  C={c_pol:.18f}", flush=True)

    return best_f, best_c


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--phases", type=str, default="1,2,3,4",
                   help="Comma-separated phase numbers to run")
    args = p.parse_args()

    with open(args.warmstart) as fh:
        data = json.load(fh)
    f0 = np.array(data["values"], dtype=np.float64)
    c0 = exact_score_f(f0)
    print(f"Warmstart: {args.warmstart}")
    print(f"n={len(f0)}, C={c0:.18f}")
    print(f"Target: < 1.502862758705311 (SOTA - 1e-7)")

    phases = [int(x) for x in args.phases.split(",")]
    global_best_c = c0
    global_best_f = f0.copy()
    t_total = time.time()

    if 1 in phases:
        f1, c1 = phase1_native_lbfgs(f0, seeds=8)
        if c1 < global_best_c:
            global_best_c = c1
            global_best_f = f1.copy()

    if 2 in phases:
        n_src = len(global_best_f)
        n_targets = [n_src * 2, n_src * 3, 50000, 45000]
        n_targets = [n for n in n_targets if n != n_src]
        f2, c2 = phase2_higher_resolution(global_best_f, n_targets, seeds=2)
        if c2 < global_best_c:
            global_best_c = c2
            global_best_f = f2.copy()

    if 3 in phases:
        f3, c3 = phase3_cycling(global_best_f, cycles=2)
        if c3 < global_best_c:
            global_best_c = c3
            global_best_f = f3.copy()

    if 4 in phases:
        f4, c4 = phase4_polish(global_best_f, rounds=3)
        if c4 < global_best_c:
            global_best_c = c4
            global_best_f = f4.copy()

    dt = time.time() - t_total
    print(f"\n{'='*60}")
    print(f"FINAL BEST: C = {global_best_c:.18f}  n={len(global_best_f)}")
    print(f"SOTA:       C = 1.502862858705310556")
    print(f"Delta:      {1.502862858705311 - global_best_c:+.3e}")
    print(f"Target:     < 1.502862758705311 (need delta > 1e-7)")
    print(f"Total time: {dt:.1f}s")

    save_best(global_best_f, global_best_c, args.out, tag="mega_optimize")
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
