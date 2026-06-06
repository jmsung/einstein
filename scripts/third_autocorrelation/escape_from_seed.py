"""Escape an arbitrary low-resolution seed up to n=100000 — the production tool.

Given a low-res piecewise-constant seed (any n; a JSON file with a "values" list,
or a bare JSON array), block-repeat + tiny-noise + strong smooth-max β-cascade up
through the levels to n=100000, then triple-verify and report against the leader
(1.4523043332) and the record threshold (1.4522043). Keeps the best across a few
noise seeds per level (greedy beam) so the basin's true continuous limit is
reached, not a 1e-4-sloppy approximation.

Usage:
    uv run python scripts/third_autocorrelation/escape_from_seed.py SEED.json \\
        [--out OUT.json] [--seeds 3]
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import scipy.signal

from einstein.third_autocorrelation.evaluator import verify_and_compute
from einstein.third_autocorrelation.optimizer import arena_c, signed_descent, upsample

LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4  # 1.4522043...
LEVELS = [800, 1600, 3200, 6400, 12800, 25600, 51200, 100000]


def load_seed(path: str) -> np.ndarray:
    raw = json.load(open(path))
    vals = raw["values"] if isinstance(raw, dict) else raw
    return np.array(vals, dtype=np.float64)


def betas_for(n: int) -> list[float]:
    if n >= 100000:
        return [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 1e10]
    return [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7]


def block_repeat(v: np.ndarray, n: int) -> np.ndarray:
    if n % len(v) == 0:
        return np.repeat(v, n // len(v))
    return upsample(v, n)


def triple_verify(f: np.ndarray) -> dict:
    n = len(f)
    dx = 0.5 / n
    c1 = verify_and_compute(f.tolist())
    ac2 = scipy.signal.fftconvolve(f, f, mode="full") * dx
    c2 = abs(ac2.max()) / (f.sum() * dx) ** 2
    m = 2 * n - 1
    F = np.fft.rfft(f, n=1 << (m - 1).bit_length())
    c3 = abs((np.fft.irfft(F * F)[:m] * dx).max()) / (f.sum() * dx) ** 2
    return {
        "c_arena": c1,
        "c_scipy": c2,
        "c_rfft": c3,
        "spread": max(c1, c2, c3) - min(c1, c2, c3),
        "passed": (max(c1, c2, c3) - min(c1, c2, c3)) < 1e-9,
    }


def escape(seed: np.ndarray, n_seeds: int, iters_mid: int, iters_top: int, base_seed: int):
    v = seed.copy()
    start_n = len(v)
    for n in LEVELS:
        if n <= start_n:
            continue
        vup = block_repeat(v, n)
        best_v, best_c = None, float("inf")
        sigma = vup.std()
        iters = iters_top if n >= 100000 else iters_mid
        for s in range(n_seeds):
            rng = np.random.default_rng(base_seed + 1000 * int(np.log2(n)) + s)
            init = vup + rng.normal(scale=1e-6 * sigma, size=n)
            cand_v, cand_c = signed_descent(init, betas_for(n), iters, 0.8, 0.0, 0.0)
            if cand_c < best_c:
                best_v, best_c = cand_v, cand_c
        v = best_v
        print(f"  n={n:6d}: C={best_c:.13f}  neg={(v < 0).mean() * 100:.1f}%", flush=True)
    return v, arena_c(v)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("seed")
    p.add_argument("--out", type=Path, default=None)
    p.add_argument("--seeds", type=int, default=3, help="noise seeds per level (greedy beam)")
    p.add_argument("--iters-mid", type=int, default=1500)
    p.add_argument("--iters-top", type=int, default=2000)
    p.add_argument("--base-seed", type=int, default=0)
    args = p.parse_args()

    seed = load_seed(args.seed)
    print(
        f"seed: n={len(seed)}  C={arena_c(seed):.10f}  neg={(seed < 0).mean() * 100:.1f}%",
        flush=True,
    )
    t0 = time.time()
    v, c = escape(seed, args.seeds, args.iters_mid, args.iters_top, args.base_seed)
    tv = triple_verify(v)
    print(f"\nESCAPED n=100000: C={c:.13f}  ({time.time() - t0:.0f}s)")
    print(
        f"  triple-verify: arena={tv['c_arena']:.13f} scipy={tv['c_scipy']:.13f} "
        f"rfft={tv['c_rfft']:.13f} spread={tv['spread']:.2e} passed={tv['passed']}"
    )
    print(f"  leader={LEADER_C:.13f}  target={TARGET:.13f}")
    if c < TARGET and tv["passed"]:
        print("  *** RECORD CANDIDATE — beats target AND triple-verified ***")
    elif c < LEADER_C - 1e-8:
        print("  beats leader but not the 1e-4 arena threshold")
    else:
        print("  does not beat leader")
    out = args.out or Path(f"results/problem-4-third-autocorrelation/escaped_{len(seed)}.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    json.dump({"values": v.tolist(), "score": c, "n": 100000, "triple_verify": tv}, open(out, "w"))
    print(f"  saved: {out}")


if __name__ == "__main__":
    main()
