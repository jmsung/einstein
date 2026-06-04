"""P5 triple-verify: real seed agrees 3-way; degenerate (coincident) points fail."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/min_distance_ratio/seeds/best.json"
PINNED_DELTA = 1e-9  # observed ~7e-15 (numpy / pure-python / mpmath@60)


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(5))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_coincident_points_fail():
    pts = [[0.0, 0.0]] * 16  # all identical → min distance 0 → degenerate
    r = core.verify({"vectors": pts}, core.get_verifier(5))
    assert not r.passed
