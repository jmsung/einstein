"""V-squared optimizer for P2 First Autocorrelation — reclaim rank #1.

f = v^2 parameterization with L-BFGS cascade.
Key insight: v^2 allows exact zeros, vanishing gradient near zero (sparsity),
and fundamentally different Hessian landscape vs f=exp(v).

Usage:
    uv run python scripts/first_autocorrelation/optimize_v2.py
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.first_autocorrelation.evaluator import verify_and_compute

RESULTS = Path("results/problem-2-first-autocorrelation")
RESULTS.mkdir(parents=True, exist_ok=True)

# ── Helpers ──────────────────────────────────────────────────────────────

def exact_score(f: np.ndarray) -> float:
    return float(verify_and_compute(f.astype(np.float64).tolist()))


def autoconv_fft(f: torch.Tensor) -> torch.Tensor:
    n = f.shape[-1]
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = torch.fft.rfft(f, n=m_pad)
    return torch.fft.irfft(F * F, n=m_pad)[:m]


def smooth_max(x: torch.Tensor, beta: float) -> torch.Tensor:
    return (1.0 / beta) * torch.logsumexp(beta * x, dim=-1)


def surrogate_vsq(v: torch.Tensor, beta: float) -> torch.Tensor:
    """Surrogate C(f) with f = v^2 (square parameterization)."""
    f = v * v
    n = f.shape[-1]
    dx = 0.5 / n
    conv = autoconv_fft(f)
    s = f.sum()
    ratios = conv / (s * s * dx)
    return smooth_max(ratios, beta)


def block_repeat(f: np.ndarray, n_target: int) -> np.ndarray:
    assert n_target % len(f) == 0
    return np.repeat(f, n_target // len(f))


def save_solution(f: np.ndarray, score: float, path: Path, tag: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        json.dump({"values": f.tolist(), "score": score, "n": len(f), "tag": tag}, fh)
    print(f"  Saved: {path} (C={score:.18f})")


# ── V^2 L-BFGS optimizer ────────────────────────────────────────────────

def lbfgs_vsq(v_init: np.ndarray, beta: float, max_iter: int = 2000,
              lr: float = 1.0, history_size: int = 200) -> tuple[np.ndarray, float]:
    """Single L-BFGS run with v^2 parameterization."""
    v = torch.tensor(v_init.copy(), dtype=torch.float64, requires_grad=True)
    opt = torch.optim.LBFGS(
        [v], lr=lr, max_iter=max_iter,
        tolerance_grad=1e-15, tolerance_change=1e-20,
        history_size=history_size, line_search_fn="strong_wolfe",
    )

    def closure():
        opt.zero_grad()
        loss = surrogate_vsq(v, beta)
        loss.backward()
        return loss

    opt.step(closure)
    f_np = (v.detach().cpu().numpy() ** 2).astype(np.float64)
    c = exact_score(f_np)
    return f_np, c


def lbfgs_vsq_cascade(v_init: np.ndarray, betas: list[float],
                       max_iter: int = 2000, lr: float = 1.0,
                       history_size: int = 200) -> tuple[np.ndarray, float]:
    """Run L-BFGS cascade with v^2 parameterization."""
    v = v_init.copy()
    best_c = float("inf")
    best_f = None

    for beta in betas:
        v_t = torch.tensor(v.copy(), dtype=torch.float64, requires_grad=True)
        opt = torch.optim.LBFGS(
            [v_t], lr=lr, max_iter=max_iter,
            tolerance_grad=1e-15, tolerance_change=1e-20,
            history_size=history_size, line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate_vsq(v_t, beta)
            loss.backward()
            return loss

        opt.step(closure)
        v = v_t.detach().cpu().numpy()
        f_np = (v ** 2).astype(np.float64)
        c = exact_score(f_np)
        if c < best_c:
            best_c = c
            best_f = f_np.copy()
        print(f"    beta={beta:.0e} C={c:.18f} {'***' if c <= best_c else ''}", flush=True)

    return best_f, best_c


# ── Multi-peak subgradient polish ────────────────────────────────────────

def multi_peak_polish(f: np.ndarray, iters: int = 500, topk: int = 1000,
                      lr0: float = 1e-5) -> tuple[np.ndarray, float]:
    """Subgradient polish on top-K peaks simultaneously."""
    f = f.astype(np.float64).copy()
    n = len(f)
    dx = 0.5 / n
    best_c = exact_score(f)
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
            c_try = exact_score(f_try)
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
            if no_improve >= 10:
                break

    return best_f, best_c


# ── Approach 1: V^2 L-BFGS from OrganonAgent warmstart ──────────────────

def approach_vsq_lbfgs(f_warm: np.ndarray, seeds: int = 8,
                        label: str = "vsq-lbfgs") -> tuple[np.ndarray, float]:
    """V^2 L-BFGS cascade from warmstart with multiple seeds."""
    n = len(f_warm)
    best_c = exact_score(f_warm)
    best_f = f_warm.copy()
    print(f"\n{'='*60}")
    print(f"Approach: {label} at n={n}")
    print(f"Starting C = {best_c:.18f}")
    print(f"{'='*60}")

    # Beta schedules to try
    schedules = [
        # Ultra-aggressive low-beta exploration (v3 winning recipe)
        [1e6] * 1 + [1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14],
        # Start lower
        [5e5, 1e6, 5e6, 1e7, 5e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13],
        # Extended low-beta
        [1e6, 1e6, 1e6, 1e7, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12],
    ]

    for seed in range(seeds):
        rng = np.random.default_rng(seed)
        v0 = np.sqrt(np.maximum(f_warm, 0.0))

        # Add noise for diversity
        noise_scale = 0.0 if seed == 0 else 1e-4 * (1 + seed)
        if noise_scale > 0:
            v0 = v0 + rng.normal(scale=noise_scale, size=v0.shape)

        sched_idx = seed % len(schedules)
        betas = schedules[sched_idx]
        hist = 300 if seed < 3 else 200
        iters = 3000 if seed < 3 else 2000

        t0 = time.time()
        print(f"\n  Seed {seed}: noise={noise_scale:.1e}, schedule={sched_idx}, "
              f"hist={hist}, iters={iters}", flush=True)
        f_new, c_new = lbfgs_vsq_cascade(v0, betas, max_iter=iters,
                                           history_size=hist)
        dt = time.time() - t0
        tag = ""
        if c_new < best_c:
            delta = best_c - c_new
            best_c = c_new
            best_f = f_new.copy()
            tag = f"  *** NEW BEST delta={delta:.3e}"
            save_solution(best_f, best_c,
                         RESULTS / f"{label}-seed{seed}-{best_c:.8f}.json",
                         tag=f"{label}-seed{seed}")
        print(f"  => C={c_new:.18f} ({dt:.1f}s){tag}", flush=True)

    return best_f, best_c


# ── Approach 2: Higher resolution ────────────────────────────────────────

def approach_higher_n(f_warm_30k: np.ndarray, n_targets: list[int],
                      seeds: int = 3) -> tuple[np.ndarray, float]:
    """Try higher n with v^2 parameterization."""
    best_c = float("inf")
    best_f = None
    print(f"\n{'='*60}")
    print(f"Approach: higher-n from n=30k base")
    print(f"{'='*60}")

    for n_target in n_targets:
        if n_target % len(f_warm_30k) == 0:
            f_up = block_repeat(f_warm_30k, n_target)
        else:
            # Nearest-neighbor upsample
            n_src = len(f_warm_30k)
            f_up = np.empty(n_target, dtype=np.float64)
            for i in range(n_target):
                f_up[i] = f_warm_30k[int(i * n_src / n_target)]

        c_up = exact_score(f_up)
        print(f"\n  n={n_target}: upsampled C={c_up:.18f}")

        for seed in range(seeds):
            rng = np.random.default_rng(100 + seed)
            v0 = np.sqrt(np.maximum(f_up, 0.0))
            if seed > 0:
                v0 = v0 + rng.normal(scale=1e-4, size=v0.shape)

            betas = [1e6, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]
            t0 = time.time()
            print(f"    seed={seed}:", flush=True)
            f_new, c_new = lbfgs_vsq_cascade(v0, betas, max_iter=3000,
                                               history_size=300)
            dt = time.time() - t0
            tag = ""
            if c_new < best_c:
                delta = best_c - c_new if best_c < float("inf") else 0
                best_c = c_new
                best_f = f_new.copy()
                tag = f"  *** NEW BEST"
                save_solution(best_f, best_c,
                             RESULTS / f"higher-n{n_target}-seed{seed}-{best_c:.8f}.json",
                             tag=f"higher-n{n_target}-seed{seed}")
            print(f"    => C={c_new:.18f} ({dt:.1f}s){tag}", flush=True)

    return best_f, best_c if best_f is not None else (f_warm_30k, float("inf"))


# ── Approach 3: Direct polish on OrganonAgent solution ───────────────────

def approach_polish(f_warm: np.ndarray) -> tuple[np.ndarray, float]:
    """Multi-peak subgradient polish on the warmstart."""
    c0 = exact_score(f_warm)
    print(f"\n{'='*60}")
    print(f"Approach: direct polish at n={len(f_warm)}")
    print(f"Starting C = {c0:.18f}")
    print(f"{'='*60}")

    best_f, best_c = multi_peak_polish(f_warm, iters=500, topk=1000, lr0=1e-5)
    print(f"  => C={best_c:.18f} (delta={c0 - best_c:.3e})", flush=True)

    if best_c < c0:
        save_solution(best_f, best_c,
                     RESULTS / f"polish-{best_c:.8f}.json",
                     tag="multi-peak-polish")

    return best_f, best_c


# ── Approach 4: Exp(v) L-BFGS (baseline comparison) ─────────────────────

def approach_exp_lbfgs(f_warm: np.ndarray, seeds: int = 4) -> tuple[np.ndarray, float]:
    """Exp(v) parameterization as baseline."""
    n = len(f_warm)
    best_c = exact_score(f_warm)
    best_f = f_warm.copy()
    print(f"\n{'='*60}")
    print(f"Approach: exp(v) L-BFGS at n={n} (baseline)")
    print(f"Starting C = {best_c:.18f}")
    print(f"{'='*60}")

    for seed in range(seeds):
        rng = np.random.default_rng(200 + seed)
        v0 = np.log(np.maximum(f_warm, 1e-30))
        if seed > 0:
            v0 = v0 + rng.normal(scale=1e-3, size=v0.shape)

        betas = [1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14]
        v_t = torch.tensor(v0.copy(), dtype=torch.float64, requires_grad=True)

        t0 = time.time()
        for beta in betas:
            from einstein.first_autocorrelation.optimizer import surrogate_v
            opt = torch.optim.LBFGS(
                [v_t], lr=1.0, max_iter=2000,
                tolerance_grad=1e-15, tolerance_change=1e-20,
                history_size=200, line_search_fn="strong_wolfe",
            )
            def closure():
                opt.zero_grad()
                loss = surrogate_v(v_t, beta, fft=True)
                loss.backward()
                return loss
            opt.step(closure)

        f_np = np.exp(v_t.detach().cpu().numpy()).astype(np.float64)
        c = exact_score(f_np)
        dt = time.time() - t0
        tag = ""
        if c < best_c:
            delta = best_c - c
            best_c = c
            best_f = f_np.copy()
            tag = f"  *** NEW BEST delta={delta:.3e}"
        print(f"  seed={seed} C={c:.18f} ({dt:.1f}s){tag}", flush=True)

    return best_f, best_c


# ── Approach 5: Alternating v^2 and polish ───────────────────────────────

def approach_alternating(f_warm: np.ndarray, rounds: int = 5) -> tuple[np.ndarray, float]:
    """Alternate between v^2 L-BFGS and subgradient polish."""
    best_c = exact_score(f_warm)
    best_f = f_warm.copy()
    f = f_warm.copy()
    print(f"\n{'='*60}")
    print(f"Approach: alternating v^2 + polish (n={len(f)})")
    print(f"Starting C = {best_c:.18f}")
    print(f"{'='*60}")

    for r in range(rounds):
        # V^2 L-BFGS
        v0 = np.sqrt(np.maximum(f, 0.0))
        betas = [1e8, 1e9, 1e10, 1e11, 1e12, 1e13]
        print(f"\n  Round {r}: L-BFGS phase", flush=True)
        f_lb, c_lb = lbfgs_vsq_cascade(v0, betas, max_iter=2000, history_size=200)
        if c_lb < best_c:
            best_c = c_lb
            best_f = f_lb.copy()
            print(f"  Round {r}: L-BFGS => C={c_lb:.18f} *** NEW BEST", flush=True)
        else:
            print(f"  Round {r}: L-BFGS => C={c_lb:.18f}", flush=True)

        # Polish
        print(f"  Round {r}: polish phase", flush=True)
        f_pol, c_pol = multi_peak_polish(f_lb, iters=200, topk=500, lr0=1e-5)
        if c_pol < best_c:
            best_c = c_pol
            best_f = f_pol.copy()
            print(f"  Round {r}: polish => C={c_pol:.18f} *** NEW BEST", flush=True)
        else:
            print(f"  Round {r}: polish => C={c_pol:.18f}", flush=True)

        f = best_f.copy()

    if best_c < exact_score(f_warm):
        save_solution(best_f, best_c,
                     RESULTS / f"alternating-{best_c:.8f}.json",
                     tag="alternating")

    return best_f, best_c


# ── Main ─────────────────────────────────────────────────────────────────

def main():
    t_start = time.time()

    # Load warmstarts
    org_path = RESULTS / "sol-01-OrganonAgent-1798.json"
    with open(org_path) as f:
        org_data = json.load(f)
    f_org = np.array(org_data["values"], dtype=np.float64)
    c_org = exact_score(f_org)
    print(f"OrganonAgent warmstart: n={len(f_org)}, C={c_org:.18f}")

    # Also load n=30k base for higher-n experiments
    sol30k_path = RESULTS / "sol-03-Together_AI-44.json"
    if sol30k_path.exists():
        with open(sol30k_path) as f:
            sol30k_data = json.load(f)
        f_30k = np.array(sol30k_data["values"], dtype=np.float64)
    else:
        # Downsample from 90k
        f_30k = f_org.reshape(30000, 3).mean(axis=1)

    target = c_org - 1e-7
    print(f"Target: < {target:.18f}")
    print(f"Time budget: 3.5h (reserve 30 min for submit/exit)")

    global_best_c = c_org
    global_best_f = f_org.copy()

    def update_global(f, c, label):
        nonlocal global_best_c, global_best_f
        if c < global_best_c:
            delta = global_best_c - c
            global_best_c = c
            global_best_f = f.copy()
            save_solution(f, c, RESULTS / f"global-best-{c:.8f}.json",
                         tag=label)
            print(f"\n  >>>>>> GLOBAL BEST: {c:.18f} (delta={delta:.3e}) <<<<<<")
            return True
        return False

    # ── Run approaches ──────────────────────────────────────────────────

    # 1. V^2 L-BFGS from OrganonAgent (most promising)
    f1, c1 = approach_vsq_lbfgs(f_org, seeds=8, label="vsq-from-org")
    update_global(f1, c1, "vsq-from-org")

    # Check time
    elapsed = time.time() - t_start
    print(f"\n--- Elapsed: {elapsed/60:.1f} min ---")

    # 2. Direct polish on OrganonAgent
    f2, c2 = approach_polish(f_org)
    update_global(f2, c2, "polish-org")

    elapsed = time.time() - t_start
    print(f"\n--- Elapsed: {elapsed/60:.1f} min ---")

    # 3. Higher resolution from 30k
    if elapsed < 7200:  # only if under 2h
        f3, c3 = approach_higher_n(f_30k, [120000, 150000, 180000], seeds=2)
        update_global(f3, c3, "higher-n")

    elapsed = time.time() - t_start
    print(f"\n--- Elapsed: {elapsed/60:.1f} min ---")

    # 4. Alternating v^2 + polish on best so far
    if elapsed < 9000:  # under 2.5h
        f4, c4 = approach_alternating(global_best_f, rounds=5)
        update_global(f4, c4, "alternating")

    elapsed = time.time() - t_start
    print(f"\n--- Elapsed: {elapsed/60:.1f} min ---")

    # 5. Exp(v) baseline comparison (quick)
    if elapsed < 10000:
        f5, c5 = approach_exp_lbfgs(f_org, seeds=3)
        update_global(f5, c5, "exp-v-baseline")

    # ── Summary ──────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"OPTIMIZATION COMPLETE")
    print(f"{'='*60}")
    print(f"OrganonAgent #1: {c_org:.18f}")
    print(f"Our best:        {global_best_c:.18f}")
    print(f"Delta:           {c_org - global_best_c:+.6e}")
    print(f"Target delta:    > 1e-7")
    beat = global_best_c < target
    print(f"BEATS #1:        {'YES' if beat else 'NO'}")
    print(f"Total time:      {elapsed/60:.1f} min")

    # Save final best
    save_solution(global_best_f, global_best_c,
                 RESULTS / "final-best.json",
                 tag="optimize_v2-final")


if __name__ == "__main__":
    main()
