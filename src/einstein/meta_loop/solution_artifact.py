"""Per-cycle solution-artifact persistence — Goal 3 of js/feat/evolve-and-measure.

The cycle-log records *that* a cycle ran and its start→end score, but not the
actual solution/params the cycle produced — so a plateau is uninspectable: you
can't open cycle 312 and see what it tried. This module persists one JSON
artifact per cycle (`cycle-<id>.json`) capturing the score, outcome, technique,
the solution `payload` (the per-problem param shape `auto_submit` consumes), and
the notes. The dashboard links each cycle row to its artifact (see
`dashboard.read_log`'s `artifact:` scheme) so the contents are inspectable
manually.

Pure + filesystem-only (no loop imports): the loop calls `persist_cycle` with a
result dict; the dashboard reads with `load_artifact` / `list_artifact_ids`.
"""

from __future__ import annotations

import json
from pathlib import Path

ARTIFACT_PREFIX = "cycle-"


def artifact_path(artifacts_dir: Path, cycle_id: int) -> Path:
    return artifacts_dir / f"{ARTIFACT_PREFIX}{cycle_id}.json"


def build_record(
    *,
    cycle_id: int,
    problem: str,
    ts: str,
    start_score,
    end_score,
    outcome: str | None,
    technique: str | None,
    payload,
    notes: str | None,
) -> dict:
    """Assemble the per-cycle artifact record (ordered for human reading)."""
    return {
        "cycle_id": cycle_id,
        "problem": problem,
        "ts": ts,
        "outcome": outcome,
        "start_score": start_score,
        "end_score": end_score,
        "technique": technique,
        "payload": payload,
        "notes": notes,
    }


def write_artifact(artifacts_dir: Path, cycle_id: int, record: dict) -> Path:
    """Write `record` as pretty JSON to `cycle-<id>.json`; returns the path.

    `default=str` keeps non-JSON payload values (numpy scalars, Paths) from
    blowing up persistence — the artifact is for human inspection, not round-trip.
    """
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    path = artifact_path(artifacts_dir, cycle_id)
    path.write_text(json.dumps(record, indent=2, default=str) + "\n")
    return path


def persist_cycle(
    artifacts_dir: Path, *, cycle_id: int, problem: str, result: dict, ts: str
) -> Path:
    """Build + write the artifact for one cycle from its `inner_attempt` result.

    `result` is the dict `inner_attempt` returns; `chosen_techniques[0]` is the
    cycle's primary technique, `payload` the solution params (None for
    strategy-only cycles — still worth persisting the score/technique/outcome).
    """
    techs = result.get("chosen_techniques") or []
    record = build_record(
        cycle_id=cycle_id,
        problem=problem,
        ts=ts,
        start_score=result.get("start_score"),
        end_score=result.get("end_score"),
        outcome=result.get("outcome"),
        technique=techs[0] if techs else None,
        payload=result.get("payload"),
        notes=result.get("notes"),
    )
    return write_artifact(artifacts_dir, cycle_id, record)


def load_artifact(artifacts_dir: Path, cycle_id: int) -> dict | None:
    """Read one cycle's artifact, or None if missing/corrupt."""
    try:
        return json.loads(artifact_path(artifacts_dir, cycle_id).read_text())
    except (OSError, ValueError):
        return None


def list_artifact_ids(artifacts_dir: Path) -> set[int]:
    """Cycle ids that have a persisted artifact in `artifacts_dir`."""
    ids: set[int] = set()
    try:
        for p in artifacts_dir.glob(f"{ARTIFACT_PREFIX}*.json"):
            stem = p.stem[len(ARTIFACT_PREFIX) :]
            if stem.isdigit():
                ids.add(int(stem))
    except OSError:
        pass
    return ids
