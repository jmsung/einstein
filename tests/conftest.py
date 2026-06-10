"""Session-wide seals against real-world side effects from tests.

Incident (2026-06-10): dozens of tests exercised inner_attempt /
run_one_visit / _try_llm_path without injecting an `auto_submitter` seam.
The default (None) lazily imports the REAL `einstein.auto_submit.try_submit`,
which fetches the live arena leaderboard and appends rows to the real
`mb/logs/auto-submit.md` audit ledger — ~40 fake rows per suite run polluting
a weekly-human-reviewed log, plus live network from CI. The same pattern
earlier leaked real `claude -p` calls (see Goal 0 of
js/feat/meta-learning-scheduler).

The autouse fixture below seals the module attribute that
`_call_auto_submit` resolves lazily at call time, so every implicit path is
blocked. `tests/test_auto_submit.py` is exempt — it tests the real unit and
already isolates itself (tmp audit_log + leaderboard_fetcher/submitter
seams).
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest


@pytest.fixture(autouse=True)
def _seal_real_auto_submit(request: pytest.FixtureRequest, monkeypatch: pytest.MonkeyPatch):
    # Exempt the modules whose unit under test IS the real try_submit; both
    # fully isolate themselves (tmp audit_log + leaderboard/submitter seams).
    # Match the last dotted component — tests/ is a package, so __name__ is
    # e.g. "tests.test_auto_submit".
    module_basename = request.node.module.__name__.rsplit(".", 1)[-1]
    if module_basename in ("test_auto_submit", "test_p14_e2e_gate_chain"):
        yield
        return
    try:
        import einstein.auto_submit as _auto_submit
    except ImportError:
        yield
        return

    def _sealed(problem_id, payload, score, **kw):
        return SimpleNamespace(
            submitted=False,
            rejected_at_gate="sealed-by-conftest",
            reason="real try_submit is blocked in tests — inject an auto_submitter seam",
        )

    monkeypatch.setattr(_auto_submit, "try_submit", _sealed)
    yield
