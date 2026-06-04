"""P3 triple-verify: 100k board-consistent seed agrees 3-way; negatives fail."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/autocorrelation/seeds/best.json.gz"
PINNED_DELTA = 1e-10  # fast / fftconvolve / mpmath agree to ~2e-14


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(3))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_negative_function_fails():
    r = core.verify({"values": [-1.0, 1.0, 1.0]}, core.get_verifier(3))
    assert not r.passed  # non-negativity is part of the contract → honest-zero
