"""meta_loop.proposals — typed proposal schema + ProposalStore.

The proposal is the *change-manifest* of the meta-loop (AHE pattern, Lin et al.
2026): every edit ships with evidence, predicted regressions, expected
metric delta, and a confidence call.

Schema choice: the branch file (`mb/active/js-feat-meta-loop.md`) named
pydantic; the repo doesn't depend on pydantic yet and `auto_submit.py` uses
plain dataclasses with explicit `_validate()` calls — so we match that
style to keep the diff minimal. Same typed-validation semantics; one fewer
heavyweight dep.

Storage: `mb/proposals/{pending,applied,rejected,reverted}/<id>.md`.
Each proposal is one markdown file with YAML frontmatter (the schema) plus
a unified-diff body. Human-readable + git-tracked = audit trail.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import re
from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path

import yaml

# ---------------- enums ----------------


class ProposalType(str, Enum):
    """Proposal types — every typed change the meta-loop can emit.

    - `RULE_EDIT` / `MANIFEST_TWEAK` / `QUEUE_REORDER` / `NEW_QUESTION` —
      the original L1 set (see `meta-loop-design-from-literature.md`).
    - `META_SELF_EDIT` landed on `js/feat/recursive-meta` per the design
      finding `recursive-meta-design.md`: edits scoped to
      `scripts/meta_loop.py` only, never auto-merged, gate chain tightened.
      The proposer that emits this type tags
      `proposer_id=recursive-meta-v0`.
    - `CODE_EDIT` landed on `js/feat/tool-autosynthesis` per
      `tool-autosynthesis-design.md`: drafts a NEW optimizer script at
      `scripts/proposed/<tool>.py` when a tool gap recurs across ≥3
      cycles / ≥2 problems. Drafts NEVER overwrite `scripts/<tool>.py`;
      promotion (mv + manifest wire) happens in `apply_proposal_to_worktree`
      under a shadow A/B run. The proposer tags
      `proposer_id=tool-autosynthesis-v0`.
    """

    RULE_EDIT = "rule_edit"
    MANIFEST_TWEAK = "manifest_tweak"
    QUEUE_REORDER = "queue_reorder"
    NEW_QUESTION = "new_question"
    META_SELF_EDIT = "meta_self_edit"
    CODE_EDIT = "code_edit"


class Confidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


VALID_PROPOSAL_TYPES = {t.value for t in ProposalType}
VALID_CONFIDENCES = {c.value for c in Confidence}


# ---------------- target-path policy ----------------


# Each proposal type restricts where the diff can land. Keeps a "queue_reorder"
# proposal from sneaking a rule edit through. Patterns are repo-relative.
_TARGET_PATTERNS: dict[str, list[re.Pattern[str]]] = {
    ProposalType.RULE_EDIT.value: [
        re.compile(r"^\.claude/rules/[a-z0-9_\-]+\.md$"),
    ],
    ProposalType.MANIFEST_TWEAK.value: [
        re.compile(r"^src/einstein/optimizer_manifest\.yaml$"),
        re.compile(r"^src/einstein/[a-z0-9_]+/manifest\.yaml$"),
    ],
    ProposalType.QUEUE_REORDER.value: [
        # The autonomous-loop queue currently lives in the script; if it
        # graduates to a YAML file later (likely), accept either.
        re.compile(r"^scripts/autonomous_loop\.py$"),
        re.compile(r"^src/einstein/autonomous_loop_queue\.yaml$"),
    ],
    ProposalType.NEW_QUESTION.value: [
        re.compile(r"^knowledge/wiki/questions/\d{4}-\d{2}-\d{2}-[a-z0-9_\-]+\.md$"),
    ],
    # Scope-of-one for the recursive case (see recursive-meta-design.md):
    # the meta-loop may propose edits to its own CLI driver, and ONLY to that
    # file. Touching auto_submit / triple_verify / arena_submit / tests via this
    # type fails at schema validation, before any gate or shadow runs.
    ProposalType.META_SELF_EDIT.value: [
        re.compile(r"^scripts/meta_loop\.py$"),
    ],
    # Tool autosynthesis (see tool-autosynthesis-design.md): drafts land
    # in `scripts/proposed/<tool>.py`, never directly in `scripts/`.
    # Promotion to `scripts/` happens at the apply-to-worktree step under a
    # shadow A/B and a human-approval gate.
    ProposalType.CODE_EDIT.value: [
        re.compile(r"^scripts/proposed/[a-z0-9_\-]+\.py$"),
    ],
}


def _target_path_ok(proposal_type: str, target_path: str) -> bool:
    pats = _TARGET_PATTERNS.get(proposal_type, [])
    return any(p.match(target_path) for p in pats)


# ---------------- schema ----------------


@dataclass
class Proposal:
    """One typed proposal — the meta-loop's change-manifest unit.

    Mirrors AHE's change-manifest fields: evidence (cycles), predicted fixes
    (expected_metric_delta), predicted regressions, plus the auditable diff.
    `requires_shadow` defaults to True only for proposal types that can
    plausibly regress the inner loop's outcomes.
    """

    id: str
    type: str  # one of VALID_PROPOSAL_TYPES
    target_path: str  # repo-relative
    proposed_diff: str  # unified diff OR full file for new files (new_question)
    evidence_cycles: list[int] = field(default_factory=list)
    expected_metric_delta: dict[str, float] = field(default_factory=dict)
    predicted_regressions: list[str] = field(default_factory=list)
    confidence: str = Confidence.LOW.value
    requires_shadow: bool = False
    rationale: str = ""
    created_at: dt.datetime = field(default_factory=lambda: dt.datetime.now(dt.timezone.utc))
    author: str = "agent"  # mirror wiki-attribution rule
    proposer_id: str = (
        ""  # provenance: which proposer emitted this (free-text, see swap-surface finding)
    )

    def __post_init__(self) -> None:
        self._validate()

    # ----- validation -----

    def _validate(self) -> None:
        """Raise ProposalValidationError on any schema violation."""
        if not self.id or not re.match(r"^[a-z0-9][a-z0-9_\-]{2,63}$", self.id):
            raise ProposalValidationError(
                f"id={self.id!r} must be 3-64 chars, [a-z0-9_-], starts with alnum"
            )
        if self.type not in VALID_PROPOSAL_TYPES:
            raise ProposalValidationError(
                f"type={self.type!r} not in {sorted(VALID_PROPOSAL_TYPES)}"
            )
        if self.confidence not in VALID_CONFIDENCES:
            raise ProposalValidationError(
                f"confidence={self.confidence!r} not in {sorted(VALID_CONFIDENCES)}"
            )
        if not self.target_path:
            raise ProposalValidationError("target_path is required")
        if not _target_path_ok(self.type, self.target_path):
            raise ProposalValidationError(
                f"target_path={self.target_path!r} not allowed for type={self.type!r}; "
                f"see _TARGET_PATTERNS in proposals.py"
            )
        if not self.proposed_diff.strip():
            raise ProposalValidationError("proposed_diff is required")
        for cid in self.evidence_cycles:
            if not isinstance(cid, int) or cid < 0:
                raise ProposalValidationError(f"evidence_cycles must be list[int>=0]; got {cid!r}")
        for k, v in self.expected_metric_delta.items():
            if not isinstance(v, (int, float)):
                raise ProposalValidationError(
                    f"expected_metric_delta[{k!r}] must be numeric; got {v!r}"
                )

    # ----- serialization -----

    def to_markdown(self) -> str:
        """Serialize as YAML frontmatter + diff body."""
        front = {
            "id": self.id,
            "type": self.type,
            "target_path": self.target_path,
            "evidence_cycles": list(self.evidence_cycles),
            "expected_metric_delta": dict(self.expected_metric_delta),
            "predicted_regressions": list(self.predicted_regressions),
            "confidence": self.confidence,
            "requires_shadow": self.requires_shadow,
            "rationale": self.rationale,
            "author": self.author,
            "proposer_id": self.proposer_id,
            "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        yaml_text = yaml.safe_dump(front, sort_keys=False, default_flow_style=False)
        return f"---\n{yaml_text}---\n\n{self.proposed_diff}\n"

    @classmethod
    def from_markdown(cls, text: str) -> Proposal:
        """Parse a markdown file emitted by to_markdown(). Raises on malformed input."""
        m = re.match(r"^---\n(.*?)\n---\n+(.*)$", text, re.DOTALL)
        if not m:
            raise ProposalValidationError("missing YAML frontmatter delimiters (--- … ---)")
        try:
            front = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            raise ProposalValidationError(f"YAML parse error: {e}") from e
        if not isinstance(front, dict):
            raise ProposalValidationError("frontmatter must be a mapping")
        body = m.group(2).rstrip() + "\n"
        created_at_raw = front.get("created_at")
        try:
            created_at = (
                dt.datetime.strptime(created_at_raw, "%Y-%m-%dT%H:%M:%SZ").replace(
                    tzinfo=dt.timezone.utc
                )
                if created_at_raw
                else dt.datetime.now(dt.timezone.utc)
            )
        except ValueError as e:
            raise ProposalValidationError(f"created_at parse error: {e}") from e
        return cls(
            id=front["id"],
            type=front["type"],
            target_path=front["target_path"],
            proposed_diff=body,
            evidence_cycles=list(front.get("evidence_cycles", [])),
            expected_metric_delta=dict(front.get("expected_metric_delta", {})),
            predicted_regressions=list(front.get("predicted_regressions", [])),
            confidence=front.get("confidence", Confidence.LOW.value),
            requires_shadow=bool(front.get("requires_shadow", False)),
            rationale=front.get("rationale", ""),
            author=front.get("author", "agent"),
            proposer_id=front.get("proposer_id", ""),
            created_at=created_at,
        )

    def to_dict(self) -> dict:
        d = asdict(self)
        d["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%SZ")
        return d


class ProposalValidationError(ValueError):
    """Raised by Proposal._validate() or from_markdown() on schema violations."""


# ---------------- id helper ----------------


def make_proposal_id(
    *, proposal_type: str, target_path: str, now: dt.datetime | None = None
) -> str:
    """Deterministic short id from timestamp + content hash. Stable across rewrites."""
    now = now or dt.datetime.now(dt.timezone.utc)
    h = hashlib.sha1(f"{proposal_type}|{target_path}|{now.isoformat()}".encode()).hexdigest()
    return f"{now.strftime('%Y%m%dt%H%M%S')}-{h[:8]}"


# ---------------- store ----------------


class ProposalStore:
    """File-backed store at `mb/proposals/{pending,applied,rejected,reverted}/`."""

    SUBDIRS = ("pending", "applied", "rejected", "reverted")

    def __init__(self, root: Path) -> None:
        self.root = root
        for sub in self.SUBDIRS:
            (root / sub).mkdir(parents=True, exist_ok=True)

    def _path(self, sub: str, proposal_id: str) -> Path:
        if sub not in self.SUBDIRS:
            raise ValueError(f"unknown subdir: {sub!r}")
        return self.root / sub / f"{proposal_id}.md"

    def write_pending(self, proposal: Proposal) -> Path:
        """Write a fresh proposal to pending/. Refuses overwriting an existing id."""
        path = self._path("pending", proposal.id)
        if path.exists():
            raise FileExistsError(f"proposal id collision: {path}")
        path.write_text(proposal.to_markdown())
        return path

    def list_pending(self) -> list[Proposal]:
        return self._list("pending")

    def list_applied(self) -> list[Proposal]:
        return self._list("applied")

    def list_rejected(self) -> list[Proposal]:
        return self._list("rejected")

    def list_reverted(self) -> list[Proposal]:
        return self._list("reverted")

    def _list(self, sub: str) -> list[Proposal]:
        dir_ = self.root / sub
        if not dir_.is_dir():
            return []
        out: list[Proposal] = []
        for p in sorted(dir_.iterdir()):
            if not p.is_file() or p.suffix != ".md":
                continue
            try:
                out.append(Proposal.from_markdown(p.read_text()))
            except ProposalValidationError:
                # Skip malformed — the human can clean those up.
                continue
        return out

    def move(self, proposal_id: str, *, from_: str, to: str) -> Path:
        """Move a proposal between subdirs (e.g., pending→applied on accept).

        Idempotent in the trivial sense: if from_==to, returns the existing path.
        """
        src = self._path(from_, proposal_id)
        dst = self._path(to, proposal_id)
        if from_ == to:
            return src
        if not src.exists():
            raise FileNotFoundError(f"no proposal at {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)
        return dst


__all__ = [
    "Confidence",
    "Proposal",
    "ProposalStore",
    "ProposalType",
    "ProposalValidationError",
    "VALID_CONFIDENCES",
    "VALID_PROPOSAL_TYPES",
    "make_proposal_id",
]
