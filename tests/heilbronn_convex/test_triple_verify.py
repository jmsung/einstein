"""P16 triple-verify: real seed agrees 3-way; degenerate (collinear) hull fails."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/heilbronn_convex/seeds/best.json"
PINNED_DELTA = 1e-9  # observed ~3e-18 (vectorized / scalar / mpmath shoelace)


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(16))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_nan_coordinate_fails():
    seed = load_seed(SEED)
    seed["points"][0][0] = float("nan")  # non-finite → fast/exact -inf, cross blows up → disagree
    r = core.verify(seed, core.get_verifier(16))
    assert not r.passed
