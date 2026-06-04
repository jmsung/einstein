"""P10 triple-verify: Wales global-min seed agrees 3-way + is a KKT critical point."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/thomson/seeds/best.json"
PINNED_DELTA = 1e-9  # observed 3-way agreement (fast / direct / mpmath) ~8e-11


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(10))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA


def test_seed_is_kkt_critical_point():
    """Riemannian-gradient stationarity: the projection of the Coulomb gradient
    onto each point's tangent plane vanishes at a genuine critical point. This
    is the branch's third structural cross-check (a real minimum, not just a
    number that happens to triple-agree)."""
    pts = np.asarray(load_seed(SEED)["vectors"], dtype=np.float64)
    pts = pts / np.linalg.norm(pts, axis=1, keepdims=True)
    diff = pts[:, None, :] - pts[None, :, :]
    d2 = np.sum(diff**2, axis=-1, keepdims=True)
    np.fill_diagonal(d2[:, :, 0], np.inf)
    grad = -np.sum(diff / d2**1.5, axis=1)  # ∇E
    radial = np.sum(grad * pts, axis=1, keepdims=True) * pts
    tangential = grad - radial  # project off the sphere normal
    assert np.max(np.linalg.norm(tangential, axis=1)) < 1e-3


def test_wrong_point_count_fails():
    r = core.verify({"vectors": [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]}, core.get_verifier(10))
    assert not r.passed  # evaluator requires exactly 282 points → honest-zero
