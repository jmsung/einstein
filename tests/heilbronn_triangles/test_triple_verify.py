"""P15 triple-verify: real seed agrees 3-way; point outside triangle fails."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/heilbronn_triangles/seeds/best.json"
PINNED_DELTA = 1e-9  # observed ~3e-17 (vectorized / scalar / mpmath@50)


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(15))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_point_outside_triangle_fails():
    seed = load_seed(SEED)
    seed["points"][0] = [5.0, 5.0]  # far outside → fast/exact -inf, cross finite → disagree
    r = core.verify(seed, core.get_verifier(15))
    assert not r.passed
