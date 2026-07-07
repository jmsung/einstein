"""P22 (kissing-d12, n=841) real triple-verify registration.

P22 was a `stub_no_op_no_solution` unavailable-stub. It shares the kissing
overlap objective and has its own shape-locked (841, 12) evaluator, so it can
register three genuinely independent scorers like the rest of the family.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein import triple_verify as tv  # noqa: E402


def _config(seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    return {"vectors": rng.standard_normal((841, 12)).tolist()}


def test_p22_registered_as_real_not_stub() -> None:
    v = tv.get_verifier(22)
    assert v is not None
    assert v.unavailable_reason is None, "P22 should be a real verifier, not a stub"
    assert v.fast is not None and v.exact is not None and v.cross is not None


def test_p22_three_scorers_agree() -> None:
    result = tv.run_payload(22, _config(1))
    assert result.passed, result.reason
    delta = max(
        abs(result.fast - result.exact),
        abs(result.fast - result.cross),
        abs(result.exact - result.cross),
    )
    assert delta < 1e-9, f"scorers diverge by {delta}"
