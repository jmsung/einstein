"""Goal 5 — P14 end-to-end: real triple-verify → gate 2 passes → SOTA/improvement
gate rejects (rank-2 doesn't beat arena #1) → NO live submission.

This is the closed-loop proof that wiring gate 2 to the real verdict does not
accidentally open the submission path: a rank-2 solution that genuinely passes
triple-verify is still correctly rejected for not improving on arena #1, and
the POST submitter is never called.

Corroboration: the live record-campaign audit log (mb/logs/auto-submit.md) shows
real rows of the same shape — P14 2.6359830849175 rejected at `no-improvement`
vs arena #1 2.6359830952608 — which is only reachable AFTER gate 2 passes.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein import auto_submit, triple_verify  # noqa: E402

SEED = _REPO / "scripts" / "circle_packing_square" / "seeds" / "p14_canonical.json"
# AlphaEvolve arena #1 for P14 (mb/problems/14-circle-packing-square/strategy.md
# and the live leaderboard fetch in mb/logs/auto-submit.md).
ARENA_TOP1 = 2.6359830952608


def test_p14_triple_verify_passes_then_no_improvement_rejects(tmp_path, monkeypatch):
    monkeypatch.delenv("EINSTEIN_AUTO_SUBMIT", raising=False)  # kill switch off

    # Stage 1: real triple-verify on the real rank-2 seed → 3-way agreement.
    tv = triple_verify.run(14, SEED)
    assert tv.passed, tv.reason
    assert tv.fast == tv.exact  # Σr is identical across routes

    payload = json.loads(SEED.read_text())
    score = tv.fast
    assert score < ARENA_TOP1  # rank-2: below arena #1

    # A POST must never happen in this scenario.
    posted: list = []

    def sentinel_submitter(*a, **k):
        posted.append((a, k))
        raise AssertionError("submit_solution must NOT be called — gate 1 should reject")

    # Stage 2: full gate chain with a stubbed leaderboard (no network, no POST).
    res = auto_submit.try_submit(
        14,
        payload,
        score,
        triple_verify=tv.as_dict(),
        leaderboard_fetcher=lambda pid: ARENA_TOP1,
        submitter=sentinel_submitter,
        audit_log=tmp_path / "audit.md",  # isolated — fresh, no throttle/cap history
    )

    assert res.submitted is False
    assert res.rejected_at_gate == "no-improvement"  # gate 2 PASSED, SOTA gate rejected
    assert not posted  # no live submission

    # The audit row records the decision; gate 2 was not the rejection point.
    audit = (tmp_path / "audit.md").read_text()
    assert "no-improvement" in audit
    assert "triple-verify-failed" not in audit
