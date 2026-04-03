#!/usr/bin/env python3
"""Packet-coordinate ascent for Problem 3 (Second Autocorrelation Inequality).

Starts from the best known solution, finds contiguous
support blocks, and tries scalar multipliers on each block to improve C.

CPU-only implementation using FFT-based scoring with closed-form formula.

Usage:
    uv run python scripts/packet_coordinate_ascent.py
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"


# ------------------------------------------------------------------
# Fast scoring via closed-form (avoids linspace/diff overhead)
# ------------------------------------------------------------------
def score(f: np.ndarray) -> float:
    """Compute C using closed-form: (2*sum(c^2) + sum(c[:-1]*c[1:])) / (3*sum(c)*max(c))."""
    conv = fftconvolve(f, f, mode="full")
    c_sum = np.sum(conv)
    c_max = np.max(conv)
    if c_sum == 0 or c_max == 0:
        return 0.0
    num = 2.0 * np.dot(conv, conv) + np.dot(conv[:-1], conv[1:])
    return float(num / (3.0 * c_sum * c_max))


# ------------------------------------------------------------------
# Block identification
# ------------------------------------------------------------------
def find_blocks(f: np.ndarray, threshold: float = 1e-10) -> list[tuple[int, int]]:
    """Find contiguous blocks of nonzero values. Returns [(start, end), ...]."""
    mask = f > threshold
    d = np.diff(mask.astype(np.int8))
    starts = np.where(d == 1)[0] + 1
    ends = np.where(d == -1)[0] + 1
    # Handle edge cases
    if mask[0]:
        starts = np.concatenate(([0], starts))
    if mask[-1]:
        ends = np.concatenate((ends, [len(f)]))
    return list(zip(starts.tolist(), ends.tolist()))


# ------------------------------------------------------------------
# Packet-coordinate ascent
# ------------------------------------------------------------------
def packet_ascent_cycle(
    f: np.ndarray,
    blocks: list[tuple[int, int]],
    alphas: np.ndarray,
    verbose: bool = True,
) -> tuple[np.ndarray, float, int]:
    """One cycle of packet-coordinate ascent over all blocks.

    For each block, tries each alpha. If any alpha improves C, refines with
    golden section. Accepts the best and moves to the next block.
    """
    C_current = score(f)
    f_current = f.copy()
    n_improved = 0
    total_gain = 0.0
    t0 = time.time()

    for i, (s, e) in enumerate(blocks):
        original_block = f_current[s:e].copy()
        if original_block.sum() < 1e-15:
            continue

        best_alpha = 1.0
        best_C = C_current

        # Coarse search over alphas
        for alpha in alphas:
            if alpha == 1.0:
                continue
            f_current[s:e] = original_block * alpha
            C_trial = score(f_current)
            if C_trial > best_C:
                best_C = C_trial
                best_alpha = alpha

        # If we found improvement, refine with golden section
        if best_alpha != 1.0:
            lo = max(0.0, best_alpha - 0.05)
            hi = best_alpha + 0.05
            for _ in range(15):
                if hi - lo < 1e-9:
                    break
                m1 = lo + 0.382 * (hi - lo)
                m2 = lo + 0.618 * (hi - lo)
                f_current[s:e] = original_block * m1
                C1 = score(f_current)
                f_current[s:e] = original_block * m2
                C2 = score(f_current)
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

        # Apply best or restore
        if best_C > C_current + 1e-15:
            f_current[s:e] = original_block * best_alpha
            gain = best_C - C_current
            total_gain += gain
            n_improved += 1
            if verbose and gain > 1e-10:
                print(
                    f"    block {i:4d} [{s:6d}:{e:6d}] w={e-s:3d}: "
                    f"alpha={best_alpha:.6f}, dC={gain:+.2e}"
                )
            C_current = best_C
        else:
            f_current[s:e] = original_block

        # Progress every 500 blocks
        if (i + 1) % 500 == 0 and verbose:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            eta = (len(blocks) - i - 1) / rate
            print(
                f"    ... {i+1}/{len(blocks)} blocks, C={C_current:.13f}, "
                f"{rate:.0f} blocks/s, ETA {eta:.0f}s"
            )

    return f_current, C_current, n_improved


# ------------------------------------------------------------------
# Support modifications (extend/contract)
# ------------------------------------------------------------------
def try_support_modifications(
    f: np.ndarray,
    blocks: list[tuple[int, int]],
    verbose: bool = True,
) -> tuple[np.ndarray, float, int]:
    """Try extending and contracting block boundaries."""
    f_best = f.copy()
    C_best = score(f)
    n_improved = 0

    for i, (s, e) in enumerate(blocks):
        # Extend left
        if s > 0 and f[s - 1] < 1e-10:
            f_trial = f_best.copy()
            f_trial[s - 1] = f_best[s] * 0.5
            C_trial = score(f_trial)
            if C_trial > C_best:
                if verbose:
                    print(f"    extend_left block {i} [{s}:{e}]: dC={C_trial-C_best:+.2e}")
                C_best = C_trial
                f_best = f_trial
                n_improved += 1

        # Extend right
        if e < len(f) and f[e] < 1e-10:
            f_trial = f_best.copy()
            f_trial[e] = f_best[e - 1] * 0.5
            C_trial = score(f_trial)
            if C_trial > C_best:
                if verbose:
                    print(f"    extend_right block {i} [{s}:{e}]: dC={C_trial-C_best:+.2e}")
                C_best = C_trial
                f_best = f_trial
                n_improved += 1

        # Contract left
        if e - s > 1:
            f_trial = f_best.copy()
            f_trial[s] = 0.0
            C_trial = score(f_trial)
            if C_trial > C_best:
                if verbose:
                    print(f"    contract_left block {i} [{s}:{e}]: dC={C_trial-C_best:+.2e}")
                C_best = C_trial
                f_best = f_trial
                n_improved += 1

        # Contract right
        if e - s > 1:
            f_trial = f_best.copy()
            f_trial[e - 1] = 0.0
            C_trial = score(f_trial)
            if C_trial > C_best:
                if verbose:
                    print(f"    contract_right block {i} [{s}:{e}]: dC={C_trial-C_best:+.2e}")
                C_best = C_trial
                f_best = f_trial
                n_improved += 1

    return f_best, C_best, n_improved


# ------------------------------------------------------------------
# Pairwise block rescaling
# ------------------------------------------------------------------
def try_pairwise_rescale(
    f: np.ndarray,
    blocks: list[tuple[int, int]],
    n_pairs: int = 500,
    verbose: bool = True,
) -> tuple[np.ndarray, float, int]:
    """Try rescaling pairs of blocks simultaneously."""
    f_best = f.copy()
    C_best = score(f)
    n_improved = 0
    rng = np.random.default_rng(42)
    n_blocks = len(blocks)
    if n_blocks < 2:
        return f_best, C_best, 0

    scale_pairs = [
        (0.9, 1.1), (1.1, 0.9), (0.95, 1.05), (1.05, 0.95),
        (0.8, 1.2), (1.2, 0.8), (0.5, 1.5), (1.5, 0.5),
    ]

    for trial in range(n_pairs):
        i, j = rng.choice(n_blocks, 2, replace=False)
        s1, e1 = blocks[i]
        s2, e2 = blocks[j]

        for a1, a2 in scale_pairs:
            f_trial = f_best.copy()
            f_trial[s1:e1] *= a1
            f_trial[s2:e2] *= a2
            C_trial = score(f_trial)
            if C_trial > C_best:
                n_improved += 1
                if verbose:
                    print(
                        f"    pair ({i},{j}) a=({a1:.2f},{a2:.2f}): "
                        f"dC={C_trial - C_best:+.2e}"
                    )
                C_best = C_trial
                f_best = f_trial

    return f_best, C_best, n_improved


# ------------------------------------------------------------------
# Verify score matches arena verifier
# ------------------------------------------------------------------
def verify_score(f: np.ndarray) -> float:
    """Verify using the full Simpson's rule formula (arena-compatible)."""
    sys.path.insert(0, str(ROOT / "src"))
    from einstein.autocorrelation.fast import fast_evaluate
    return fast_evaluate(f)


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
def main():
    print("=" * 70)
    print("Packet-Coordinate Ascent for Second Autocorrelation Inequality")
    print("=" * 70)

    # Load public best solution
    npy_path = RESULTS / "public_best_100k.npy"
    if not npy_path.exists():
        print(f"ERROR: {npy_path} not found.")
        return

    f = np.maximum(np.load(npy_path).astype(np.float64), 0.0)
    n = len(f)
    C_initial = score(f)
    C_verified = verify_score(f)
    print(f"Loaded: n={n}")
    print(f"  Score (closed-form): {C_initial:.13f}")
    print(f"  Score (arena verif): {C_verified:.13f}")

    # Analyze structure
    blocks = find_blocks(f, threshold=1e-10)
    print(f"Blocks: {len(blocks)}")
    widths = np.array([e - s for s, e in blocks])
    print(
        f"  Widths: min={widths.min()}, median={np.median(widths):.0f}, "
        f"max={widths.max()}, mean={widths.mean():.1f}"
    )

    C_best = C_initial
    f_best = f.copy()

    # ------------------------------------------------------------------
    # Phase 1: Packet ascent with standard multipliers
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("Phase 1: Packet-coordinate ascent (standard multipliers)")
    print(f"{'='*60}")

    standard_alphas = np.array([0.5, 0.9, 0.95, 0.99, 1.01, 1.05, 1.1, 1.5, 2.0])

    for cycle in range(3):
        blocks = find_blocks(f_best, threshold=1e-10)
        print(f"\n  Cycle {cycle} ({len(blocks)} blocks)...")
        t0 = time.time()

        f_new, C_new, n_impr = packet_ascent_cycle(
            f_best, blocks, standard_alphas, verbose=True
        )
        dt = time.time() - t0
        print(
            f"  Cycle {cycle}: C={C_new:.13f} "
            f"(dC={C_new - C_best:+.2e}), {n_impr} improved [{dt:.0f}s]"
        )

        if C_new > C_best:
            C_best = C_new
            f_best = f_new

        if n_impr == 0:
            print("  Converged.")
            break

    # ------------------------------------------------------------------
    # Phase 2: Extended multiplier search
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("Phase 2: Extended multiplier search")
    print(f"{'='*60}")

    extended_alphas = np.array([
        0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
        0.9, 0.95, 0.99, 0.995, 0.999,
        1.001, 1.005, 1.01, 1.05, 1.1,
        1.2, 1.3, 1.5, 1.7, 2.0, 3.0, 5.0,
    ])

    blocks = find_blocks(f_best, threshold=1e-10)
    f_new, C_new, n_impr = packet_ascent_cycle(
        f_best, blocks, extended_alphas, verbose=True
    )
    print(f"  Extended: C={C_new:.13f} (dC={C_new - C_best:+.2e}), {n_impr} improved")
    if C_new > C_best:
        C_best = C_new
        f_best = f_new

    # ------------------------------------------------------------------
    # Phase 3: Pairwise rescaling
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("Phase 3: Pairwise block rescaling (500 random pairs)")
    print(f"{'='*60}")

    blocks = find_blocks(f_best, threshold=1e-10)
    t0 = time.time()
    f_new, C_new, n_impr = try_pairwise_rescale(f_best, blocks, n_pairs=500, verbose=True)
    dt = time.time() - t0
    print(f"  Pairwise: C={C_new:.13f} (dC={C_new - C_best:+.2e}), {n_impr} improved [{dt:.0f}s]")
    if C_new > C_best:
        C_best = C_new
        f_best = f_new

    # ------------------------------------------------------------------
    # Phase 4: Support modifications
    # ------------------------------------------------------------------
    print(f"\n{'='*60}")
    print("Phase 4: Support modifications (extend/contract)")
    print(f"{'='*60}")

    for round_i in range(2):
        blocks = find_blocks(f_best, threshold=1e-10)
        t0 = time.time()
        f_new, C_new, n_impr = try_support_modifications(f_best, blocks, verbose=True)
        dt = time.time() - t0
        print(f"  Round {round_i}: C={C_new:.13f} (dC={C_new - C_best:+.2e}), {n_impr} improved [{dt:.0f}s]")
        if C_new > C_best:
            C_best = C_new
            f_best = f_new
        if n_impr == 0:
            break

    # ------------------------------------------------------------------
    # Verify and save
    # ------------------------------------------------------------------
    C_final_verified = verify_score(f_best)
    improvement = C_best - C_initial

    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"  Initial C (closed-form): {C_initial:.13f}")
    print(f"  Final C (closed-form):   {C_best:.13f}")
    print(f"  Final C (arena verify):  {C_final_verified:.13f}")
    print(f"  Improvement:             {improvement:+.2e}")
    print(f"{'='*70}")

    # Save
    out_tag = f"c2_n{n}_{C_best:.8f}_packet_ascent"
    out_json = RESULTS / f"{out_tag}.json"
    out_npy = RESULTS / f"{out_tag}.npy"

    data = {
        "problem": "second_autocorrelation_inequality",
        "n_points": n,
        "score": C_best,
        "score_verified": C_final_verified,
        "values": f_best.tolist(),
        "tag": out_tag,
        "method": "packet_coordinate_ascent",
        "initial_score": C_initial,
        "improvement": improvement,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    with open(out_json, "w") as fout:
        json.dump(data, fout)
    np.save(out_npy, f_best)
    print(f"Saved: {out_json}")
    print(f"Saved: {out_npy}")


if __name__ == "__main__":
    main()
