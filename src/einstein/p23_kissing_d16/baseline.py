"""Barnes-Wall BW16 baseline construction.

BW16 = Lambda16 (laminated lattice in dim 16) achieves the kissing number
kappa(16) = 4320 = 32 + 2240 + 2048:

- 32  axis vectors  ±e_i, i = 0..15
- 2240 four-coord vectors  (1/2)(±1, ±1, ±1, ±1, 0,...,0) supported on
       any of the 140 weight-4 codewords of the [16,11,4] extended
       Hamming code, with all 2^4 = 16 independent sign choices.
- 2048 sixteen-coord vectors  (1/4)(s_0, ..., s_15) with s_i in {-1,+1}
       and the bit-pattern (1-s)/2 in the full [16,11,4] code (2^11 = 2048
       codewords).

All 4320 vectors are unit-norm; pairwise inner products lie in
{-1, -1/2, -1/4, 0, +1/4, +1/2}, so all pair distances are >= 2 (perfect
kissing).

For the n = 4321 problem we duplicate v[0] to get the floor score 2.0.
"""

from __future__ import annotations

import numpy as np


def extended_hamming_16_11_4() -> np.ndarray:
    """Return all 2048 codewords of the [16, 11, 4] extended Hamming code.

    Parity-check matrix is the [16, 5, 8] Reed-Muller RM(1, 4) generator:
        rows = (all-ones, then 4 binary coordinate-bit indicators).
    A binary vector c in {0,1}^16 is a codeword iff H @ c = 0 (mod 2).
    """
    H_rows = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    ]
    H = np.array(H_rows, dtype=np.int64)
    all_words = np.array(
        [[(k >> b) & 1 for b in range(15, -1, -1)] for k in range(1 << 16)],
        dtype=np.int64,
    )
    syndromes = (all_words @ H.T) % 2
    is_codeword = np.all(syndromes == 0, axis=1)
    return all_words[is_codeword]


def bw16_min_vectors() -> np.ndarray:
    """Return the 4320 minimum vectors of BW16, all unit length."""
    code = extended_hamming_16_11_4()  # (2048, 16) of {0,1}
    weights = code.sum(axis=1)

    # Axis: ±e_i for each i.
    axis = np.concatenate([np.eye(16), -np.eye(16)], axis=0)
    assert axis.shape == (32, 16)

    # Four-coord: support = weight-4 codeword (140 of them); for each support
    # all 2^4 sign patterns yield a valid BW16 vector at norm 1.
    weight4 = code[weights == 4]
    assert weight4.shape == (140, 16)
    four_vecs = []
    for support in weight4:
        positions = np.flatnonzero(support)
        for k in range(16):
            signs = np.array([(1 if (k >> b) & 1 else -1) for b in range(4)])
            v = np.zeros(16)
            v[positions] = 0.5 * signs
            four_vecs.append(v)
    four = np.array(four_vecs)
    assert four.shape == (2240, 16)

    # Sixteen-coord: ±¼ in every position; bit pattern (1-s)/2 in [16,11,4].
    sixteen = (1 - 2 * code) * 0.25  # (2048, 16) of {±0.25}
    assert sixteen.shape == (2048, 16)

    vectors = np.concatenate([axis, four, sixteen], axis=0)
    assert vectors.shape == (4320, 16)

    norms = np.linalg.norm(vectors, axis=1)
    assert np.allclose(norms, 1.0)

    return vectors


def bw16_plus_duplicate(dup_index: int = 0) -> np.ndarray:
    """Return 4321 unit vectors: BW16 (4320) + an exact duplicate.

    Score = 2.0 from the single duplicate pair.
    """
    bw = bw16_min_vectors()
    dup = bw[dup_index]
    return np.concatenate([bw, dup[None, :]], axis=0)


def build_bw16_plus_duplicate(out_path: str | None = None) -> dict:
    """Build the canonical BW16 + 1 duplicate; optionally save to JSON."""
    vectors = bw16_plus_duplicate()
    payload = {"vectors": vectors.tolist()}
    if out_path:
        import json
        from pathlib import Path

        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(payload, f)
    return payload
