"""Path-1 test: extend Jaech's Adam + upsampling cascade past n=50k → n=400k.

Hypothesis: the existing `adam_peak_flatten.py` caps the upsampling cascade at
50k and tops out at C ~ 0.908 (per `mb/tracking/problem-3-autocorrelation/strategy.md`).
That ceiling may be a *cascade-length* artifact, not a true from-scratch limit:
Jaech & Joseph 2025 use upsampling all the way to their target n. If the
extended cascade unlocks a basin > 0.91 from random init at n=400k, we have
genuine new ground (and motivation for a GPU campaign at n ≥ 1.6M). If the
cascade tops out at 0.91 anyway, the from-scratch ceiling is structural.

Usage: budget ~30-45 min on local M5 Max (MPS or CPU).
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "src")
sys.path.insert(0, "scripts/autocorrelation")

import numpy as np
import torch

from einstein.autocorrelation.fast import fast_evaluate
from adam_peak_flatten import adam_optimize, upscale_linear, compute_C_batch


REPO_ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = REPO_ROOT / "results" / "problem-3-autocorrelation"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def trim_zeros(f: np.ndarray, tol: float = 1e-8) -> np.ndarray:
    """Trim leading/trailing near-zero values."""
    nz = np.nonzero(f > tol)[0]
    if len(nz) == 0:
        return f
    return f[nz[0]:nz[-1] + 1]


def refine_upscaled(f_up: np.ndarray, n_iters: int, lr: float, device: str,
                    time_limit: float) -> tuple[np.ndarray, float]:
    """Refine an upscaled solution with single-trajectory Adam at lr."""
    h = torch.tensor(f_up, dtype=torch.float32, device=device).unsqueeze(0)
    h.requires_grad_(True)
    opt = torch.optim.Adam([h], lr=lr)

    best_score = fast_evaluate(f_up)
    best_f = f_up.copy()
    t0 = time.time()

    for t in range(n_iters):
        if time.time() - t0 > time_limit:
            break
        opt.zero_grad()
        C = compute_C_batch(h, device)
        (-C).backward()
        opt.step()
        with torch.no_grad():
            h.clamp_(min=0)

        if (t + 1) % 500 == 0:
            with torch.no_grad():
                cur = h[0].detach().cpu().numpy()
            cur_score = fast_evaluate(np.maximum(cur, 0))
            if cur_score > best_score:
                best_score = cur_score
                best_f = np.maximum(cur, 0).copy()
            print(f"      refine iter {t+1}: C={cur_score:.8f} best={best_score:.8f}")

    return best_f, best_score


def main():
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print("=" * 70)
    print(f"Jaech extended cascade test — device={device}")
    print(f"  Cascade: 768 → 3072 → 12288 → 49152 → 196608 → 400000")
    print(f"  Time budget per stage: ~5 min, total ~30 min")
    print("=" * 70)

    t_global = time.time()

    # Stage 1: small-n exploration
    n_start = 768
    print(f"\n--- Stage 1: n={n_start} (Adam exploration + exploitation) ---")
    f, score = adam_optimize(
        n_start, batch_size=128, n_explore=4000, n_exploit=4000,
        lr_explore=3e-2, lr_exploit=5e-3, device=device,
        seed=42, time_limit=300,
    )
    f = trim_zeros(f)
    score = fast_evaluate(np.maximum(f, 0))
    print(f"  Stage 1 done: n={len(f)} C={score:.10f}  ({int(time.time()-t_global)}s)")
    track = [(len(f), score)]

    # Stages 2-6: upsampling cascade past 50k
    targets = [3072, 12288, 49152, 196608, 400000]
    for new_n in targets:
        if time.time() - t_global > 35 * 60:  # hard 35-min cap
            print(f"\nGlobal time cap hit, stopping cascade at n={len(f)}")
            break
        print(f"\n--- Stage: upsample {len(f)} → {new_n} ---")
        f_up = upscale_linear(f, new_n)
        score_up = fast_evaluate(np.maximum(f_up, 0))
        print(f"  After linear interp: C={score_up:.10f}")

        # Refine at the new resolution. Use shorter run at higher n.
        if new_n <= 16000:
            iters, lr, tlim = 4000, 1e-2, 240
        elif new_n <= 64000:
            iters, lr, tlim = 3000, 5e-3, 240
        elif new_n <= 200000:
            iters, lr, tlim = 2000, 3e-3, 360
        else:  # n=400k
            iters, lr, tlim = 1500, 2e-3, 360

        f, score = refine_upscaled(f_up, iters, lr, device, tlim)
        score = fast_evaluate(np.maximum(f, 0))
        f = trim_zeros(f)
        score = fast_evaluate(np.maximum(f, 0))
        print(f"  Stage done: n={len(f)} C={score:.10f}  ({int(time.time()-t_global)}s)")
        track.append((len(f), score))

    # Save the final result
    out = {
        "n_points": len(f),
        "score": score,
        "values": np.maximum(f, 0).tolist(),
        "tag": "jaech_cascade_extended",
        "track": track,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    out_path = RESULTS_DIR / f"jaech_cascade_n{len(f)}_C{score:.8f}.json"
    with open(out_path, "w") as fh:
        json.dump(out, fh)
    print()
    print("=" * 70)
    print(f"FINAL: n={len(f)} C={score:.10f} ({int(time.time()-t_global)}s total)")
    print(f"Track: " + " → ".join(f"({n},{s:.6f})" for n, s in track))
    print()
    print(f"Comparison to strategy.md ceilings:")
    print(f"  From-scratch ceiling (Adam only): 0.908")
    print(f"  Warmstart SOTA 400k (Dinkelbach): 0.96264")
    print(f"  Submission gate (#1 + minImp):    0.9627433")
    print()
    if score > 0.91:
        print(f">>> BREAKTHROUGH: extended cascade EXCEEDED from-scratch ceiling.")
        print(f">>> Worth scaling to n=1.6M+ on GPU.")
    else:
        print(f"--- Cascade tops at {score:.6f}, within from-scratch family. ---")
        print(f"--- Confirms 0.908 from-scratch ceiling is structural. ---")
    print(f"Saved: {out_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
