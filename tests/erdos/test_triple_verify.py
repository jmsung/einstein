"""P1 triple-verify: real seed agrees 3-way; out-of-range input fails."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/erdos/seeds/best.json"
PINNED_DELTA = 1e-12  # observed 3-way agreement (FFT / np.correlate / mpmath) ~5e-17


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(1))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_out_of_range_values_fail():
    # values > 1 make fast_evaluate return inf and compute_upper_bound raise →
    # honest-zero (a non-finite or raising scorer can never pass the gate).
    r = core.verify({"values": [2.0, 0.5, 0.5]}, core.get_verifier(1))
    assert not r.passed
