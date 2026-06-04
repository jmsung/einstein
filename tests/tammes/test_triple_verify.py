"""P11 triple-verify: real seed agrees 3-way; NaN coordinate fails."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/tammes/seeds/best.json"
PINNED_DELTA = 1e-9  # observed ~1e-16 (numpy / pure-python / mpmath@50)


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(11))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_nan_coordinate_fails():
    seed = load_seed(SEED)
    seed["vectors"][0][0] = float("nan")
    r = core.verify(seed, core.get_verifier(11))
    assert not r.passed  # NaN never agrees with itself → disagreement
