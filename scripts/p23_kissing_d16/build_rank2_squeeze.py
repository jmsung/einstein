"""Build a rank-2 squeeze candidate for P23.

Strategy: BW16 (4320 perfect kissing) + filler placed near v_0 along the
direction u* that minimizes S(u) = sum_i [<u, w_i>]_+ over the link of v_0.

Score ≈ 2 + δ * (sqrt(3) * S(u*) - 2). For S(u*) ≈ 18.4, penalty rate
≈ 29.9 per unit δ. We sweep δ in {1e-5, 1e-4, 1e-3, 1e-2} and pick the
smallest one that float64 + mpmath50 verify identically to ≥ a few ULPs
above 2.0.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.p23_kissing_d16.baseline import bw16_min_vectors
from einstein.p23_kissing_d16.evaluator import overlap_loss_fast, overlap_loss_mpmath
from einstein.p23_kissing_d16.optimal_direction import find_min_s_direction


def build_squeeze(delta: float, u_perp: np.ndarray, v0: np.ndarray) -> np.ndarray:
    """Construct 4321 vectors: 4320 BW16 + filler at cos(δ) v0 + sin(δ) u_perp."""
    bw = bw16_min_vectors()
    filler = np.cos(delta) * v0 + np.sin(delta) * u_perp
    filler /= np.linalg.norm(filler)
    return np.vstack([bw, filler[None, :]])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--deltas", type=float, nargs="+",
                        default=[1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 5e-3, 1e-2])
    parser.add_argument("--n-starts", type=int, default=400)
    parser.add_argument("--out", default="results/p23_kissing_d16/squeeze")
    args = parser.parse_args()

    print("Finding u* that minimizes S(u) over the link of v_0...")
    bw = bw16_min_vectors()
    v0 = bw[0]
    u_perp_15, s_min = find_min_s_direction(bw, v0, n_starts=args.n_starts)
    # embed back into 16-d
    basis = np.eye(16)[1:]  # 15 x 16
    u_perp = u_perp_15 @ basis  # (16,)
    print(f"  S(u*) ≈ {s_min:.6f} (smaller is better; threshold to beat 2.0 is 2/sqrt(3) ≈ 1.155)")
    print(f"  u_perp norm = {np.linalg.norm(u_perp):.10f}")
    print(f"  <u_perp, v0> = {u_perp @ v0:.2e}\n")

    Path(args.out).mkdir(parents=True, exist_ok=True)
    rows = []
    for delta in args.deltas:
        v = build_squeeze(delta, u_perp, v0)
        s_fast = overlap_loss_fast(v)
        t0 = time.time()
        s_mp50 = overlap_loss_mpmath(v, dps=50)
        t_mp = time.time() - t0
        # Save
        out_path = f"{args.out}/squeeze_delta{delta:.0e}.json"
        with open(out_path, "w") as f:
            json.dump({"vectors": v.tolist()}, f)
        rows.append((delta, s_fast, s_mp50, t_mp, out_path))
        print(f"  δ={delta:.0e}  fast={s_fast:.10f}  mp50={s_mp50:.10f}  ({t_mp:.1f}s)  -> {out_path}")

    print("\nSummary:")
    print(f"  {'delta':>10}  {'fast':>14}  {'mpmath50':>14}  {'rank':>8}")
    for delta, s_fast, s_mp50, _, _ in rows:
        rank = "#1" if s_mp50 < 2.0 else ("#2" if s_mp50 < 2.873843 else "#3" if s_mp50 < 4.6862915 else "#4+")
        print(f"  {delta:>10.0e}  {s_fast:>14.10f}  {s_mp50:>14.10f}  {rank:>8}")


if __name__ == "__main__":
    main()
