"""Sidon-set structured warmstart builder.

A Sidon set ``S`` has all pairwise differences distinct, giving the
indicator ``1_S`` a flat off-peak autocorrelation — a natural candidate
starting point for autocorrelation-minimization problems.

Supported Sidon families:
1. Mian-Chowla (greedy Sidon sequence)
2. Bose-Chowla (algebraic Sidon set of size ``q`` for prime ``q``)
3. Singer (tabulated (307, 18, 1) difference set)

Each warmstart is combined with a thick block and normalized to sum = 1.

Usage:
    uv run python scripts/first_autocorrelation/singer_warmstart.py \\
        --n 30000 --family mian_chowla --out warmstart.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from einstein.first_autocorrelation.evaluator import verify_and_compute


def mian_chowla(size: int) -> list[int]:
    """Greedy Sidon sequence (Mian-Chowla): smallest positive integers such
    that all pairwise sums are distinct.

    Returns the first ``size`` elements.
    """
    seq: list[int] = [0]
    sums: set[int] = {0}
    candidate = 1
    while len(seq) < size:
        # Try adding candidate
        new_sums = {candidate + x for x in seq}
        new_sums.add(2 * candidate)
        if new_sums.isdisjoint(sums):
            seq.append(candidate)
            sums |= new_sums
        candidate += 1
    return seq


def bose_chowla(q: int) -> list[int]:
    """Simple quadratic-residue variant ``{i·q + (i² mod q) : i = 0..q-1}``.

    This yields a Sidon set in ``Z/q²`` of size ``q``. Not the full
    Bose-Chowla GF(q²) primitive-root construction — this variant is chosen
    for implementation simplicity and is used here over the raw integers
    (not modular arithmetic) as spike positions.
    """
    return [i * q + (i * i) % q for i in range(q)]


def singer_17() -> list[int]:
    """Tabulated (307, 18, 1) Singer difference set.

    Source: LaJolla Repository of Combinatorial Designs
    (https://ljcr.dmgordon.org/diffsets/ds_307_18_1.html).
    """
    return [
        0, 1, 3, 13, 32, 36, 43, 52, 57,
        88, 126, 144, 154, 198, 212, 257, 278, 290,
    ]


def build_warmstart(
    n: int,
    sidon_set: list[int],
    block_width: int,
    block_mass: float,
    spike_mass: float,
) -> tuple[np.ndarray, list[int]]:
    """Build a structured f at length n with a thick block + Sidon-spaced spikes.

    - Block: positions [0, block_width), uniform value (total mass block_mass)
    - Spikes: at scaled Sidon positions (total mass spike_mass = 1 - block_mass)
    """
    f = np.zeros(n, dtype=np.float64)

    # Thick block
    f[:block_width] = block_mass / block_width

    # Spikes scaled to fit in n
    max_sidon = max(sidon_set)
    # Scale so the largest Sidon element lands near position n - 100 (avoid edge)
    scale = (n - block_width - 200) / (max_sidon if max_sidon > 0 else 1)
    spike_positions = [block_width + 100 + int(round(s * scale)) for s in sidon_set]
    spike_val = spike_mass / len(sidon_set)
    for p in spike_positions:
        if 0 <= p < n:
            f[p] += spike_val

    return f, spike_positions


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n", type=int, default=30000)
    p.add_argument("--family", choices=["mian_chowla", "bose_chowla", "singer_17"],
                   default="singer_17")
    p.add_argument("--size", type=int, default=14,
                   help="Number of Sidon elements (mian_chowla/bose_chowla only)")
    p.add_argument("--block-width", type=int, default=102,
                   help="Thick-block width in grid cells")
    p.add_argument("--block-mass", type=float, default=0.5,
                   help="Fraction of total mass in the block (rest in spikes)")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    if args.family == "mian_chowla":
        sidon = mian_chowla(args.size)
    elif args.family == "bose_chowla":
        # Use q = smallest prime ≥ size
        q = args.size
        while not all(q % d != 0 for d in range(2, int(q**0.5) + 1)):
            q += 1
        sidon = bose_chowla(q)
    elif args.family == "singer_17":
        sidon = singer_17()
    else:
        raise ValueError(args.family)

    print(f"Family: {args.family}")
    print(f"Sidon set ({len(sidon)} elements): {sidon}")

    f, positions = build_warmstart(
        args.n, sidon, args.block_width, args.block_mass, 1.0 - args.block_mass,
    )
    print(f"Spike positions in grid: {positions[:20]}{'...' if len(positions) > 20 else ''}")
    print(f"n = {args.n}, sum(f) = {f.sum():.6f}, max(f) = {f.max():.6e}")
    print(f"Nonzero cells = {(f > 0).sum()}")

    C = float(verify_and_compute(f.tolist()))
    print(f"Raw warmstart C = {C:.10f}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump({
            "values": f.tolist(),
            "score": C,
            "n": args.n,
            "family": args.family,
            "sidon_set": sidon,
            "block_width": args.block_width,
            "block_mass": args.block_mass,
        }, fh)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
