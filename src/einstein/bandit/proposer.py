"""proposer.py — register the Thompson bandit as a meta-loop proposer (Goal 6).

The meta-loop swap surface is one callable type:
    Callable[[ProposerInput], list[dict]]
`thompson_proposer` is the first NON-LLM proposer to use it. It reads the same
`ProposerInput` the LLM proposer gets, computes the bandit's current best arm
per category from the skill-library's Beta-Bernoulli posteriors, and emits a
`manifest_tweak` proposal tagged `proposer_id="thompson-bandit-v0"` —
distinguishable from LLM proposals in the audit log from row one (no backfill;
the swap-surface chore reserved this id).

The emitted diff is a **reviewable recommendation** appended to
`src/einstein/optimizer_manifest.yaml` (the bandit's best arm per category,
with posterior means), not an auto-apply patch — wiring technique → optimizer
key is a human follow-up. The point of Goal 6 is to prove the swap surface
end-to-end with a real non-LLM proposer, with provenance from row one. See
`docs/wiki/findings/meta-loop-swap-surface.md`.
"""

from __future__ import annotations

import sys
from pathlib import Path

from einstein.bandit.thompson import arm_from_row

THOMPSON_PROPOSER_ID = "thompson-bandit-v0"
MANIFEST_TARGET = "src/einstein/optimizer_manifest.yaml"

_REPO = Path(__file__).resolve().parents[3]


def _strategy_picker():
    tools = _REPO / "docs" / "tools"
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    import strategy_picker  # type: ignore[import-not-found]

    return strategy_picker


def _best_arm_per_category(library_path: Path) -> dict[str, tuple[str, float, int]]:
    """{category_key: (technique, posterior_mean, tried)} — best arm per category.

    Multi-category rows like `kissing / Coulomb` are bucketed under the FIRST
    segment (`kissing`) — same convention as strategy_picker's segment match.
    """
    sp = _strategy_picker()
    rows = sp.load_skill_library(library_path)
    best: dict[str, tuple[str, float, int]] = {}
    for r in rows:
        cat = r.category.split("/")[0].strip()
        arm = arm_from_row(r)
        cur = best.get(cat)
        if cur is None or arm.mean > cur[1]:
            best[cat] = (r.technique, arm.mean, r.tried)
    return best


def _render_recommendation_diff(best: dict[str, tuple[str, float, int]]) -> str:
    """A unified-diff body that appends a `# thompson-bandit-v0 recommends:`
    block to optimizer_manifest.yaml. Reviewable, not auto-applied."""
    body_lines = ["# thompson-bandit-v0 recommendations (Beta posterior means):"]
    for cat in sorted(best):
        tech, mean, tried = best[cat]
        body_lines.append(f"#   {cat}: {tech} (mean={mean:.2f}, tried={tried})")
    return (
        "--- a/src/einstein/optimizer_manifest.yaml\n"
        "+++ b/src/einstein/optimizer_manifest.yaml\n"
        "@@ append bandit recommendations @@\n"
        + "\n".join("+" + line for line in body_lines)
        + "\n"
    )


def _recent_cycle_ids(cycle_log_path: Path, *, n: int = 5) -> list[int]:
    """Last `n` cycle ids from the cycle-log. Empty on any parse hiccup."""
    try:
        from einstein.meta_loop import diagnose  # local import — keeps proposer light

        rows = diagnose.parse_cycle_log(cycle_log_path)
        return [r.cycle_id for r in rows[-n:]]
    except Exception:  # noqa: BLE001 — proposer must never raise
        return []


def thompson_proposer(inp) -> list[dict]:
    """Emit one `manifest_tweak` proposal from the bandit's current posteriors.

    Callable-typed for the meta-loop swap surface — same shape as the LLM
    proposer (`Callable[[ProposerInput], list[dict]]`). Returns `[]` honestly
    when the skill-library is empty (nothing learned → nothing to recommend),
    mirroring `stagnation_heuristic` in the swap-surface finding's worked
    example.
    """
    best = _best_arm_per_category(inp.skill_library_path)
    if not best:
        return []
    diff = _render_recommendation_diff(best)
    return [
        {
            "type": "manifest_tweak",
            "target_path": MANIFEST_TARGET,
            "proposed_diff": diff,
            "evidence_cycles": _recent_cycle_ids(inp.cycle_log_path),
            "expected_metric_delta": {},
            "predicted_regressions": [
                "bandit explore step may pick a worse arm than the manifest default",
                "diff is advisory — recommendations need a technique→optimizer-key map to auto-apply",
            ],
            "confidence": "low",
            "requires_shadow": True,
            "rationale": (
                "thompson-bandit-v0: Beta-Bernoulli posterior over skill-library "
                "(Beta(top3+1, tried-top3+1)) ranks techniques per category. "
                "Recommends the current best arm per category as the manifest default. "
                "Exploration is the bandit's own (posterior-variance-proportional); "
                "recency is implicit in the warm-started counts. The diff is a "
                "reviewable recommendation, not an auto-apply patch."
            ),
            "proposer_id": THOMPSON_PROPOSER_ID,
        }
    ]


__all__ = ["THOMPSON_PROPOSER_ID", "MANIFEST_TARGET", "thompson_proposer"]
