"""Goal 5 construction battery — try every distinct ansatz to find a NEW basin.

Optimisation from the n=400 anchor caps in our 23%-neg basin (~1.4525). A record
needs a structurally different basin. This screens many genuinely-distinct
piecewise-constant CONSTRUCTIONS at n=6400 (fast); our basin scores 1.4527526
there, so any construction polishing BELOW that is a better basin. Winners are
lifted to n=100000 + triple-verified against the 1.4522043 record threshold.

Families: periodic sign-modulated envelopes (varied period/duty/decay), compact
support, multi-scale fragmentation, chirp-sign, ours↔leader morph, and
sign-perturbed equioscillation. Run in background; prints a sorted ladder.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import arena_c, signed_descent, upsample

SOL = Path(".mb/problems/4-third-autocorrelation/solutions")
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
N_SCREEN = 6400
OURS_AT_6400 = 1.4527526158024  # our basin at n=6400 (progression table)
SCREEN_BETAS = [1e4, 3e4, 1e5, 3e5, 1e6, 1e7]
SCREEN_ITERS = 500
OUT = Path("results/problem-4-third-autocorrelation")


def _env(n, decay):
    x = np.linspace(-1, 1, n)
    return 1.0 / (1.0 + decay * np.abs(x))


def gen(name, n):
    """Yield (label, seed_array) construction candidates."""
    out = []
    x = np.linspace(0, 1, n)
    # 1. periodic square-wave sign on a decaying envelope, varied period & duty
    for period in [4, 6, 8, 12, 16, 24, 32, 48, 64]:
        for duty in [0.30, 0.40, 0.50]:
            for decay in [0.0, 1.0, 3.0]:
                ph = (np.arange(n) % period) / period
                sign = np.where(ph < duty, -1.0, 1.0)  # duty = negative fraction
                out.append((f"periodic_p{period}_d{duty}_dec{decay}", _env(n, decay) * sign + 0.05))
    # 2. multi-scale fragmentation (two periods)
    for p1, p2 in [(8, 64), (4, 32), (16, 128), (6, 48)]:
        s1 = np.where((np.arange(n) % p1) / p1 < 0.4, -1.0, 1.0)
        s2 = np.where((np.arange(n) % p2) / p2 < 0.4, -1.0, 1.0)
        out.append((f"multiscale_{p1}_{p2}", _env(n, 1.0) * (0.6 * s1 + 0.4 * s2) + 0.05))
    # 3. chirp-sign (frequency sweeps across the domain)
    for f0, f1 in [(2, 40), (5, 80), (1, 120)]:
        phase = np.cumsum(np.linspace(f0, f1, n)) * np.pi / n
        out.append((f"chirp_{f0}_{f1}", _env(n, 1.0) * np.sign(np.sin(phase)) + 0.05))
    # 4. compact support: signed oscillation on central fraction, zero outside
    for frac in [0.6, 0.75, 0.9]:
        v = _env(n, 1.0) * np.where((np.arange(n) % 8) / 8 < 0.4, -1.0, 1.0)
        lo, hi = int((1 - frac) / 2 * n), int((1 + frac) / 2 * n)
        m = np.zeros(n)
        m[lo:hi] = v[lo:hi]
        out.append((f"compact_{frac}", m + 0.05))
    # 5. ours↔leader morph at n (downsampled), swept blend
    lead = np.array(
        json.load(open(SOL / "sol-organon-rank1-p4-1.4523043332.json"))["values"], float
    )
    ours = np.array(
        json.load(open(SOL / "solution-feat-third-autocorrelation-1.4525211550469.json"))["values"],
        float,
    )
    ld = lead[: (len(lead) // n) * n].reshape(n, -1).mean(1)
    od = ours[: (len(ours) // n) * n].reshape(n, -1).mean(1)
    for a in [0.25, 0.5, 0.75]:
        out.append((f"morph_a{a}", (1 - a) * od + a * ld))
    # 6. sign-perturbed equioscillation: n=400 SOTA upsampled, flip every k-th block
    sota = np.array(json.load(open(SOL / "rank01_DarwinAgent8427_n400.json"))["values"], float)
    su = upsample(sota, n)
    for k in [13, 17, 23, 31]:
        v = su.copy()
        v[(np.arange(n) % k) == 0] *= -1.0
        out.append((f"equiflip_k{k}", v))
    del x, name
    return out


def screen_one(label, seed):
    if seed.sum() <= 0:
        seed = seed + (abs(seed.sum()) / len(seed) + 0.1)  # ensure ∫f>0
    v, c = signed_descent(seed, SCREEN_BETAS, SCREEN_ITERS, 0.8, 0.0, 0.0)
    return v, c, float((v < 0).mean())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cands = gen("all", N_SCREEN)
    print(
        f"battery: {len(cands)} constructions, screening at n={N_SCREEN} "
        f"(our basin here = {OURS_AT_6400:.10f})",
        flush=True,
    )
    rows = []
    for i, (label, seed) in enumerate(cands):
        t0 = time.time()
        try:
            v, c, neg = screen_one(label, seed)
        except Exception as e:
            print(f"[{i + 1}/{len(cands)}] {label}: ERROR {e}", flush=True)
            continue
        better = bool(c < OURS_AT_6400 - 1e-6)
        rows.append({"label": label, "C6400": c, "neg": neg, "better_basin": better, "v": v})
        flag = "  <-- BETTER BASIN" if better else ""
        print(
            f"[{i + 1}/{len(cands)}] {label:28s} C={c:.10f} neg={neg * 100:4.1f}%{flag} ({time.time() - t0:.0f}s)",
            flush=True,
        )
        ladder = sorted(
            ({k: r[k] for k in ("label", "C6400", "neg", "better_basin")} for r in rows),
            key=lambda r: r["C6400"],
        )
        json.dump(
            {"our_basin_6400": OURS_AT_6400, "ladder": ladder},
            open(OUT / "battery_ladder.json", "w"),
            indent=2,
        )

    rows.sort(key=lambda r: r["C6400"])
    print("\n=== TOP 5 at n=6400 ===")
    for r in rows[:5]:
        print(f"  {r['label']:28s} C={r['C6400']:.10f} neg={r['neg'] * 100:.1f}%")

    # lift the best screened construction to 100k if it beats our basin at 6400
    best = rows[0]
    print(f"\nbest construction: {best['label']} C6400={best['C6400']:.10f}")
    if best["C6400"] < OURS_AT_6400 - 1e-6:
        print("LIFTING best to n=100000...")
        v = best["v"]
        for n in [12800, 25600, 51200, 100000]:
            vup = upsample(v, n)
            vup = vup + np.random.default_rng(0).normal(scale=1e-6 * vup.std(), size=n)
            betas = [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7] + (
                [1e8, 3e8, 1e9, 1e10] if n >= 100000 else []
            )
            v, c = signed_descent(vup, betas, 1500 if n >= 100000 else 800, 0.8, 0.0, 0.0)
            print(f"  n={n}: C={c:.13f} neg={(v < 0).mean() * 100:.1f}%", flush=True)
        print(f"LIFTED: C={arena_c(v):.13f} (leader {LEADER_C}, target {TARGET})")
        json.dump(
            {"values": v.tolist(), "score": arena_c(v), "n": 100000, "label": best["label"]},
            open(OUT / "battery_best_100k.json", "w"),
        )
    else:
        print("No construction beat our basin at n=6400 — the basin wall holds for these families.")


if __name__ == "__main__":
    main()
