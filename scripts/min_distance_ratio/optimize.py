"""Optimize Problem 5: Min Distance Ratio (2D, n=16).

Usage:
    uv run python scripts/min_distance_ratio/optimize.py \
        --input results/problem-5-min-distance-ratio/warm_start.json \
        --output results/problem-5-min-distance-ratio/solution-best.json
"""

import argparse
import json
from pathlib import Path

import numpy as np

from einstein.min_distance_ratio.evaluator import evaluate
from einstein.min_distance_ratio.optimizer import polish_full


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True,
                        help="JSON with {'vectors': [[x,y]*16]}")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--lottery-rounds", type=int, default=10)
    parser.add_argument("--n-rotations", type=int, default=20000)
    parser.add_argument("--n-ulp", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    V0 = np.array(json.load(open(args.input))["vectors"], dtype=np.float64)
    s0 = evaluate({"vectors": V0.tolist()})
    print(f"Initial score: {s0:.17f}")

    V, s = polish_full(
        V0,
        slsqp_rounds=3,
        lottery_rounds=args.lottery_rounds,
        n_rotations=args.n_rotations,
        n_ulp=args.n_ulp,
        seed=args.seed,
        verbose=True,
    )

    print(f"Final score:   {s:.17f}")
    print(f"Improvement:   {s0 - s:+.3e}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({"vectors": V.tolist()}, f, indent=2)
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
