#!/usr/bin/env python3
"""Packet-coordinate ascent on the 1.6M public best solution.

Targets small blocks first (most likely to benefit from rescaling).
One cycle, then saves.

Usage:
    uv run python scripts/packet_ascent_1600k.py
"""

import os
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

os.environ["PYTHONUNBUFFERED"] = "1"

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"


def score(f: np.ndarray) -> float:
    conv = fftconvolve(f, f, mode="full")
    c_sum = np.sum(conv)
    c_max = np.max(conv)
    if c_sum == 0 or c_max == 0:
        return 0.0
    num = 2.0 * np.dot(conv, conv) + np.dot(conv[:-1], conv[1:])
    return float(num / (3.0 * c_sum * c_max))


def find_blocks(f, threshold=1e-10):
    mask = f > threshold
    d = np.diff(mask.astype(np.int8))
    starts = np.where(d == 1)[0] + 1
    ends = np.where(d == -1)[0] + 1
    if mask[0]:
        starts = np.concatenate(([0], starts))
    if mask[-1]:
        ends = np.concatenate((ends, [len(f)]))
    return list(zip(starts.tolist(), ends.tolist()))


def main():
    print("=" * 70)
    print("Packet-Coordinate Ascent on 1.6M Solution")
    print("=" * 70)

    f = np.maximum(
        np.load(RESULTS / "public_best_1600k.npy").astype(np.float64), 0.0
    )
    n = len(f)
    C_initial = score(f)
    print(f"Loaded: n={n}, C={C_initial:.13f}")

    blocks = find_blocks(f, threshold=1e-10)
    widths = np.array([e - s for s, e in blocks])
    print(f"Blocks: {len(blocks)}")
    print(f"  Widths: min={widths.min()}, median={np.median(widths):.0f}, max={widths.max()}")

    # Sort blocks by width (small first -- most likely to benefit)
    block_order = sorted(range(len(blocks)), key=lambda i: blocks[i][1] - blocks[i][0])

    # Only process blocks with width <= 50 (most adjustable)
    small_blocks = [(i, blocks[i]) for i in block_order if blocks[i][1] - blocks[i][0] <= 50]
    print(f"Small blocks (width <= 50): {len(small_blocks)}")

    alphas = np.array([0.5, 0.9, 0.95, 0.99, 1.01, 1.05, 1.1, 1.5, 2.0])

    C_best = C_initial
    f_best = f.copy()
    n_improved = 0
    t0 = time.time()

    for idx, (bi, (s, e)) in enumerate(small_blocks):
        original = f_best[s:e].copy()
        if original.sum() < 1e-15:
            continue

        best_alpha = 1.0
        best_C = C_best

        for alpha in alphas:
            if alpha == 1.0:
                continue
            f_best[s:e] = original * alpha
            C_trial = score(f_best)
            if C_trial > best_C:
                best_C = C_trial
                best_alpha = alpha

        # Golden section refinement if improved
        if best_alpha != 1.0:
            lo = max(0.0, best_alpha - 0.05)
            hi = best_alpha + 0.05
            for _ in range(15):
                if hi - lo < 1e-9:
                    break
                m1 = lo + 0.382 * (hi - lo)
                m2 = lo + 0.618 * (hi - lo)
                f_best[s:e] = original * m1
                C1 = score(f_best)
                f_best[s:e] = original * m2
                C2 = score(f_best)
                if C1 > C2:
                    hi = m2
                    if C1 > best_C:
                        best_C = C1
                        best_alpha = m1
                else:
                    lo = m1
                    if C2 > best_C:
                        best_C = C2
                        best_alpha = m2

        if best_C > C_best + 1e-15:
            f_best[s:e] = original * best_alpha
            gain = best_C - C_best
            n_improved += 1
            if gain > 1e-12:
                print(
                    f"  block {bi:5d} [{s:8d}:{e:8d}] w={e-s:3d}: "
                    f"alpha={best_alpha:.6f}, dC={gain:+.2e}"
                )
            C_best = best_C
        else:
            f_best[s:e] = original

        if (idx + 1) % 200 == 0:
            elapsed = time.time() - t0
            rate = (idx + 1) / elapsed
            eta = (len(small_blocks) - idx - 1) / rate
            print(
                f"  ... {idx+1}/{len(small_blocks)}, C={C_best:.13f}, "
                f"{n_improved} improved, {rate:.1f} blocks/s, ETA {eta:.0f}s"
            )

    elapsed = time.time() - t0
    improvement = C_best - C_initial

    print(f"\n{'='*70}")
    print("RESULTS (1.6M)")
    print(f"  Initial C: {C_initial:.13f}")
    print(f"  Final C:   {C_best:.13f}")
    print(f"  Improvement: {improvement:+.2e}")
    print(f"  Time: {elapsed:.0f}s, {n_improved} blocks improved")
    print(f"{'='*70}")

    # Save
    np.save(RESULTS / f"c2_n{n}_{C_best:.8f}_packet_ascent.npy", f_best)
    print(f"Saved to results/")


if __name__ == "__main__":
    main()
