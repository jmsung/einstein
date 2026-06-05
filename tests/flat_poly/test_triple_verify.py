"""P12 triple-verify: SOTA seed certifies the continuous sup 3-way (drift-free).

Reconciled 2026-06-04 (Phase 7, Goal 2): the three checks now target the
continuous supremum, not the 1e6-point grid max. See p12-grid-drift-resolution.md.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _triple_verify_util import load_seed, max_pairwise_delta  # noqa: E402

from einstein.flat_poly.evaluator import (  # noqa: E402
    compute_score,
    continuous_sup_score,
)
from einstein.triple_verify import core  # noqa: E402

SEED = "scripts/flat_poly/seeds/best.json"
PINNED_DELTA = 1e-10  # FFT-Newton / dense-Newton / mpmath-Newton agree to ~2e-16
CONT_SUP = 1.2809320528750  # certified continuous sup of the SOTA basin
ARENA_REPORTED = 1.2809320527988  # arena's grid value for the same coefficients


def test_seed_passes_three_way():
    r = core.verify(load_seed(SEED), core.get_verifier(12))
    assert r.passed, r.reason
    assert max_pairwise_delta(r) < PINNED_DELTA
    # the certified quantity is the continuous sup, not the 1M grid max
    assert abs(r.fast - CONT_SUP) < 1e-9


def test_continuous_sup_is_grid_independent():
    """The certified sup is stable across FFT seeding density (a flat polynomial
    has many near-equal peaks; the certifier refines the top-K, not just one)."""
    coeffs = load_seed(SEED)["coefficients"]
    s20 = continuous_sup_score(coeffs, m_grid=1 << 20)
    s22 = continuous_sup_score(coeffs, m_grid=1 << 22, k_peaks=512)
    assert abs(s20 - s22) < 1e-12


def test_drift_is_below_min_improvement():
    """Both the 1M grid and the arena value sit below the true continuous sup,
    and every gap is < minImprovement (1e-8) — so the historical local↔arena
    drift cannot manufacture a false P12 improvement. See the resolution finding.
    """
    coeffs = load_seed(SEED)["coefficients"]
    grid_1m = compute_score(coeffs)
    cont = continuous_sup_score(coeffs)
    assert grid_1m <= cont + 1e-15  # grid never exceeds the continuum
    assert 0 < cont - grid_1m < 1e-8  # drift real but below minImprovement
    assert abs(cont - ARENA_REPORTED) < 1e-8  # arena is a finer grid, same basin


def test_wrong_coeff_values_fail():
    r = core.verify({"coefficients": [2] * 70}, core.get_verifier(12))
    assert not r.passed  # not in {+1,-1} → honest-zero
