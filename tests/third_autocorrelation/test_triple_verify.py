"""P4 triple-verify: real seed agrees 3-way; zero-integral input fails."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/third_autocorrelation/seeds/best.json.gz"
PINNED_DELTA = 1e-10


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(4))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_zero_integral_fails():
    r = core.verify({"values": [0.0, 0.0, 0.0, 0.0]}, core.get_verifier(4))
    assert not r.passed  # Σf == 0 raises → honest-zero
