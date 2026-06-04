"""P14 triple-verify: real seed agrees 3-way; overlapping circles fail."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/circle_packing_square/seeds/p14_canonical.json"
PINNED_DELTA = 1e-9  # Σr is trivially identical across routes (numpy / fsum / mpmath)


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(14))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_overlapping_circles_fail():
    seed = load_seed(SEED)
    # Move circle 1 onto circle 0 → gross overlap → feasibility raises → honest-zero
    seed["circles"][1][0] = seed["circles"][0][0]
    seed["circles"][1][1] = seed["circles"][0][1]
    r = core.verify(seed, core.get_verifier(14))
    assert not r.passed
