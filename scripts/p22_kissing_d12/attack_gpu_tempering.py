"""Parallel tempering SA attack on P22 using the repo's gpu_tempering module.

Start from CHRONOS's 841 (840 + duplicate) → score 2.0.
Run parallel tempering with HingeOverlapLoss on SphereManifold.
K=50 perturbations/step × many replicas, tiny scales.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, "src")
from einstein.gpu_tempering.core import ParallelTemperingSA, TemperingConfig
from einstein.gpu_tempering.losses import HingeOverlapLoss
from einstein.gpu_tempering.manifolds import SphereManifold
from einstein.p22_kissing_d12.evaluator import overlap_loss

RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"

N = 841
D = 12


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-steps", type=int, default=200_000)
    ap.add_argument("--n-replicas", type=int, default=64)
    ap.add_argument("--k-per-step", type=int, default=50)
    ap.add_argument("--scale", type=float, default=1e-6)
    ap.add_argument("--t-min", type=float, default=1e-12)
    ap.add_argument("--t-max", type=float, default=1e-4)
    ap.add_argument("--device", type=str, default="mps")
    ap.add_argument("--tag", type=str, default="sa")
    args = ap.parse_args()

    data = json.loads(CHRONOS_PATH.read_text())
    vecs = np.array(data["vectors"], dtype=np.float64)
    vecs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)
    print(f"Initial: {vecs.shape}", flush=True)
    s0 = overlap_loss(vecs)
    print(f"CHRONOS initial score: {s0!r}", flush=True)

    cfg = TemperingConfig(
        n_replicas=args.n_replicas,
        n_steps=args.n_steps,
        k_per_step=args.k_per_step,
        scale=args.scale,
        t_min=args.t_min,
        t_max=args.t_max,
        swap_interval=100,
        recompute_every=1000,
        report_every=5000,
        timeout_sec=1800,
        use_compile=False,  # MPS may not support compile
    )

    loss_fn = HingeOverlapLoss()
    manifold = SphereManifold(dim=D)
    sa = ParallelTemperingSA(loss_fn, manifold, n_vectors=N, config=cfg)

    t0 = time.time()
    result = sa.run(vecs, device=args.device)
    elapsed = time.time() - t0

    best_vecs = result.best_vectors
    # Re-verify with arena path
    s_final = overlap_loss(best_vecs)
    print(f"\nSA done in {elapsed:.1f}s", flush=True)
    print(f"SA reported best: {result.best_score!r}", flush=True)
    print(f"Arena-path re-score: {s_final!r}", flush=True)
    print(f"Initial vs final: {s0!r} vs {s_final!r}  (Δ = {s_final - s0:+.6e})", flush=True)

    out = RESULTS_DIR / f"sa_{args.tag}_best.json"
    json.dump(
        {
            "initial_score": s0,
            "sa_reported": result.best_score,
            "arena_rescored": s_final,
            "elapsed_sec": elapsed,
            "vectors": best_vecs.tolist(),
            "config": cfg.__dict__,
        },
        open(out, "w"),
    )
    print(f"Saved → {out}", flush=True)


if __name__ == "__main__":
    main()
