"""P19 triple-verify: real seed agrees 3-way; non-covering set fails."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/difference_bases/seeds/best.json"
PINNED_DELTA = 0.0  # exact integer ratio k²/v — bit-identical across the 3 algorithms


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(19))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) <= PINNED_DELTA


def test_noncovering_set_fails():
    # {0, 2}: difference 1 is unrepresentable → v=0 → score inf on all routes;
    # inf never agrees with inf → passed=False (honest: this isn't a real score).
    r = core.verify({"set": [0, 2]}, core.get_verifier(19))
    assert not r.passed
