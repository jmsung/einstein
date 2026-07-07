"""Triple-verify registration for the kissing family (P6/24/25).

The kissing objective (total sphere-overlap penalty) is shared across every
fixed-n kissing problem — only (n, d) change. One registration parametrized by
the seed's own shape covers d11 n=594 (id 6), d11 n=605 (id 24), and d12 n=842
(id 25). The three checks are three *independent code paths* on the same
objective: overlap_loss_fast (dot-product), overlap_loss (distance-matrix), and
overlap_loss_mpmath (bignum ground truth).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein import triple_verify as tv  # noqa: E402


def _spread_config(n: int, d: int, seed: int = 0) -> dict:
    """A feasible-ish random config: overlap penalty is finite and the three
    scorers must agree on it (agreement is the property under test, not the
    score value)."""
    rng = np.random.default_rng(seed)
    v = rng.standard_normal((n, d))
    return {"vectors": v.tolist()}


def test_kissing_ids_registered() -> None:
    ids = set(tv.registered_ids())
    assert {6, 24, 25} <= ids, f"kissing ids missing from registry: {ids}"


def test_kissing_three_scorers_agree_d11() -> None:
    seed = _spread_config(n=40, d=11, seed=1)
    result = tv.run_payload(6, seed)
    assert result.passed, result.reason
    assert result.fast is not None and result.exact is not None and result.cross is not None
    delta = max(
        abs(result.fast - result.exact),
        abs(result.fast - result.cross),
        abs(result.exact - result.cross),
    )
    assert delta < 1e-9, f"scorers diverge by {delta}"


def test_kissing_verifier_shared_across_dims() -> None:
    """Same objective, different (n, d) — id 25 (d12) must verify a d=12 seed."""
    seed = _spread_config(n=30, d=12, seed=2)
    result = tv.run_payload(25, seed)
    assert result.passed, result.reason


def test_kissing_sign_bug_is_caught() -> None:
    """A tampered 'exact' that negates the score must fail the agreement gate —
    proves the three checks are genuinely independent, not one function thrice."""
    from einstein.kissing_number import evaluator as ev

    seed = _spread_config(n=40, d=11, seed=3)
    verifier = tv.get_verifier(6)
    # Monkey-free: build a bad verifier inline to confirm the agreement rule bites.
    from einstein.triple_verify.core import TripleVerifier, verify

    bad = TripleVerifier(
        problem_id=6,
        fast=verifier.fast,
        exact=lambda s: -ev.overlap_loss(np.asarray(s["vectors"], dtype=float)),
        cross=verifier.cross,
        tolerance=verifier.tolerance,
    )
    result = verify(seed, bad)
    assert not result.passed
