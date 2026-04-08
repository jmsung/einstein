"""Polish CHRONOS #1 to reclaim rank #1 on Problem 6.

Loads solution_best.json (set to CHRONOS id 1150 by recon), runs multi-round
contribution-weighted micro-perturbation at fine scales, and saves whenever
the score strictly improves. minImprovement = 0, so any improvement wins.

Usage:
    uv run python scripts/kissing_number/polish_chronos.py [--budget 600] [--rounds 12]
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import time
from pathlib import Path

import numpy as np

from einstein.kissing_number.evaluator import overlap_loss

RESULTS = Path("results/problem-6-kissing-number")
MB_SOLUTIONS = Path.home() / "projects/workbench/memory-bank/einstein/docs/problem-6-kissing-number/solutions"
N = 594
D = 11
CHRONOS_NEW_1 = 0.156133128358060  # arena #1 we are trying to beat


def fast_score(u: np.ndarray) -> float:
    g = u @ u.T
    n = len(u)
    i, j = np.triu_indices(n, k=1)
    cos = np.clip(g[i, j], -1.0, 1.0)
    d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos))
    return float(np.maximum(0.0, 2.0 - d).sum())


def vec_contribs(u: np.ndarray) -> np.ndarray:
    g = u @ u.T
    n = len(u)
    i, j = np.triu_indices(n, k=1)
    cos = np.clip(g[i, j], -1.0, 1.0)
    d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos))
    p = np.maximum(0.0, 2.0 - d)
    c = np.zeros(n)
    np.add.at(c, i, p)
    np.add.at(c, j, p)
    return c


def incremental_loss(u: np.ndarray, idx: int, total: float, old_v: np.ndarray) -> float:
    others = np.concatenate([u[:idx], u[idx + 1 :]], axis=0)
    oc = np.clip(old_v @ others.T, -1.0, 1.0)
    od = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - oc))
    op = np.maximum(0.0, 2.0 - od)
    nc = np.clip(u[idx] @ others.T, -1.0, 1.0)
    nd = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - nc))
    np_ = np.maximum(0.0, 2.0 - nd)
    return total - float(op.sum()) + float(np_.sum())


def polish_round(
    u: np.ndarray,
    scale: float,
    n_iters: int,
    seed: int,
    time_limit_s: float,
    label: str,
) -> tuple[np.ndarray, float, int]:
    rng = np.random.default_rng(seed)
    cur = fast_score(u)
    best = cur
    best_u = u.copy()
    contribs = vec_contribs(u)
    probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N
    improvements = 0
    t0 = time.time()
    for it in range(n_iters):
        if it > 0 and it % 50_000 == 0:
            contribs = vec_contribs(u)
            probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N
        idx = int(rng.choice(N, p=probs))
        old_v = u[idx].copy()
        u[idx] += rng.standard_normal(D) * scale
        u[idx] /= np.linalg.norm(u[idx])
        new = incremental_loss(u, idx, cur, old_v)
        if new < cur:
            cur = new
            improvements += 1
            if cur < best:
                best = cur
                best_u = u.copy()
        else:
            u[idx] = old_v

        if (it + 1) % 200_000 == 0:
            elapsed = time.time() - t0
            print(
                f"  [{label} {scale:.0e}] {it+1:>8,d} | best={best:.15f} "
                f"impr={improvements} ({improvements/(it+1)*100:.2f}%) {elapsed:.0f}s",
                flush=True,
            )
        if time.time() - t0 > time_limit_s:
            print(
                f"  [{label} {scale:.0e}] time-limit at {it+1:,} iters", flush=True
            )
            break
    return best_u, best, improvements


def save_best(u: np.ndarray, score: float) -> None:
    """Atomically save to solution_best.json + MB backup."""
    p = RESULTS / "solution_best.json"
    out = {"vectors": u.tolist(), "score": score, "source": "polish_chronos.py"}
    tmp = p.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, p)
    # MB backup
    mb_p = MB_SOLUTIONS / f"polish_chronos_{score:.13f}.json"
    with open(mb_p, "w") as f:
        json.dump(out, f)
    print(f"  >>> SAVED {score:.15f}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=int, default=600, help="Total seconds")
    parser.add_argument("--rounds", type=int, default=12)
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()

    print("=" * 70)
    print(f"POLISH CHRONOS #1 — total budget {args.budget}s, {args.rounds} rounds")
    print("=" * 70)

    with open(RESULTS / "solution_best.json") as f:
        data = json.load(f)
    u = np.array(data["vectors"], dtype=np.float64)
    u = u / np.linalg.norm(u, axis=1, keepdims=True)

    start_score = overlap_loss(u)
    print(f"Start score (exact):  {start_score:.15f}")
    print(f"CHRONOS #1 to beat:   {CHRONOS_NEW_1:.15f}")
    print(f"Gap to CHRONOS:       {start_score - CHRONOS_NEW_1:+.3e}")
    best_u = u.copy()
    best = start_score

    # Schedule: alternate fine scales 1e-13 / 1e-14 with occasional 1e-12
    rng = np.random.default_rng(args.seed)
    schedule = []
    # Mix scales: 1e-11 (broader) → 1e-12 → 1e-13 → 1e-14 (finest). 1e-11 helps escape
    # micro-pockets that the finer scales have already exhausted.
    for _ in range(args.rounds):
        for scale in (1e-11, 1e-13, 1e-14, 1e-12, 1e-13, 1e-14):
            schedule.append((scale, int(rng.integers(1_000_000_000))))
    per_round = max(20, args.budget // len(schedule))
    print(f"  schedule: {len(schedule)} rounds, {per_round}s each")

    t_start = time.time()
    for ridx, (scale, sd) in enumerate(schedule, start=1):
        if time.time() - t_start > args.budget:
            print("  total budget reached")
            break
        new_u, new_score, n_imp = polish_round(
            best_u.copy(),
            scale=scale,
            n_iters=10_000_000,
            seed=sd,
            time_limit_s=per_round,
            label=f"R{ridx:02d}",
        )
        # Verify with the slow exact evaluator
        exact = overlap_loss(new_u)
        if exact < best:
            best = exact
            best_u = new_u.copy()
            print(
                f"  Round {ridx}/{len(schedule)} {scale:.0e}: exact={exact:.15f} "
                f"(Δ={start_score - exact:+.3e}, vs CHRONOS={CHRONOS_NEW_1 - exact:+.3e}) "
                f"[{n_imp} improvements]"
            )
            save_best(best_u, best)
        else:
            print(
                f"  Round {ridx}/{len(schedule)} {scale:.0e}: exact={exact:.15f} (no improvement)"
            )

    final = overlap_loss(best_u)
    print()
    print("=" * 70)
    print(f"FINAL: {final:.15f}")
    print(f"Start: {start_score:.15f}")
    print(f"Delta: {start_score - final:+.6e}")
    print(f"CHRONOS #1: {CHRONOS_NEW_1:.15f}")
    print(f"Margin over CHRONOS #1: {CHRONOS_NEW_1 - final:+.6e}")
    if final < CHRONOS_NEW_1:
        print(">>> WINNING — strict improvement, ready for submission")
    else:
        print("    NOT yet beating CHRONOS — keep polishing")
    print("=" * 70)


if __name__ == "__main__":
    main()
