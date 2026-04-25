"""Massively parallel random filler scan over S^15.

Sample N points uniformly on S^15, compute hinge against BW16 (4320),
report best basin found.
"""

from __future__ import annotations

import argparse
import time

import numpy as np

from einstein.p23_kissing_d16.baseline import bw16_min_vectors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-samples", type=int, default=1_000_000)
    parser.add_argument("--batch", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--top-k", type=int, default=20)
    args = parser.parse_args()

    bw = bw16_min_vectors()  # (4320, 16) unit vectors
    centers = 2.0 * bw  # already unit
    rng = np.random.default_rng(args.seed)

    n = args.n_samples
    batch = args.batch
    top_scores = []
    t0 = time.time()
    for b in range(0, n, batch):
        m = min(batch, n - b)
        # uniform on S^15
        z = rng.standard_normal((m, 16))
        z /= np.linalg.norm(z, axis=1, keepdims=True)
        # hinge: c_filler = 2z, distances to all c_i = 2 bw[i]
        # ||2z - 2bw||^2 = 4 + 4 - 8 <z, bw> = 8(1 - <z, bw>)
        ip = z @ bw.T  # (m, 4320)
        # only IP > 0.5 contributes
        # dist = 2 sqrt(2(1-IP)); penalty = max(0, 2 - dist)
        gt = ip > 0.5
        dist = np.where(gt, 2.0 * np.sqrt(np.maximum(0.0, 2.0 * (1.0 - ip))), 2.0)
        penalty = np.maximum(0.0, 2.0 - dist).sum(axis=1)
        # collect best
        for s in penalty:
            if len(top_scores) < args.top_k or s < top_scores[-1]:
                top_scores.append(float(s))
                top_scores.sort()
                top_scores = top_scores[: args.top_k]
        if (b // batch) % 5 == 0:
            elapsed = time.time() - t0
            rate = (b + m) / max(1e-9, elapsed)
            best = top_scores[0] if top_scores else None
            print(f"[{b+m:>10}/{n}] best={best:.6f}  rate={rate:.0f}/s  elapsed={elapsed:.0f}s", flush=True)

    print("\nTop-K scores:", top_scores)
    print(f"Best random non-duplicate basin score: {top_scores[0]:.6f}")


if __name__ == "__main__":
    main()
