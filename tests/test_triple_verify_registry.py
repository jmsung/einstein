"""Registry-coverage gate (Goal 4).

Every problem wired into ``optimizer_manifest.yaml`` MUST have a registered
triple-verify — otherwise the autonomous loop could dispatch + score a problem
that gate 2 can never honestly verify, and Phase 6's manifest expansion would
silently outpace verification. This test fails CI if a manifest problem has no
registration (real scorers OR an honest ``unavailable_reason``).
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein import triple_verify as tv  # noqa: E402

MANIFEST = _REPO / "src" / "einstein" / "optimizer_manifest.yaml"


def _manifest_problem_ids() -> list[int]:
    data = yaml.safe_load(MANIFEST.read_text())
    return sorted(int(k) for k in data)


def test_every_manifest_problem_has_a_triple_verify():
    manifest_ids = set(_manifest_problem_ids())
    registered = set(tv.registered_ids())
    missing = sorted(manifest_ids - registered)
    assert not missing, (
        f"manifest problems with no triple-verify registration: {missing}. "
        f"Register real scorers in src/einstein/triple_verify/problems/, or an "
        f"honest unavailable_reason for stubs. Never let dispatch outpace verify."
    )


def test_registry_is_nonempty_and_ids_are_ints():
    ids = tv.registered_ids()
    assert ids, "triple-verify registry is empty — problems/ side-effect imports failed"
    assert all(isinstance(i, int) for i in ids)
