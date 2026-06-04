"""P2 triple-verify: real seed agrees 3-way; infeasible input fails."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/first_autocorrelation/seeds/best.json.gz"
PINNED_DELTA = 1e-10  # observed 3-way agreement on the seed (np.convolve / FFT / power-spectrum)


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(2))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_negative_values_fail():
    r = core.verify({"values": [-1.0, 2.0, 3.0]}, core.get_verifier(2))
    assert not r.passed  # arena evaluator rejects negative values → honest-zero
