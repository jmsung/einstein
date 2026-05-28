"""Typed output schema for pre-cycle literature synthesis.

The `LiteratureSynthesis` shape is the contract between the synthesizer's
`claude -p` JSON output and the markdown file written under `mb/problems/`.
`JSON_SCHEMA` is exported as a string for use with `claude -p --json-schema`.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class Hit:
    """One qmd search hit (lex, vec, or hybrid)."""

    path: str
    score: float
    snippet: str
    collection: str


@dataclass
class CrossSourcePattern:
    """A claimed pattern attested by 2+ sources."""

    name: str
    description: str
    supporting_sources: list[str] = field(default_factory=list)


@dataclass
class ProposedApproach:
    """One concrete approach the inner agent could try, grounded in citations."""

    description: str
    cited_sources: list[str] = field(default_factory=list)
    rationale: str = ""


@dataclass
class LiteratureSynthesis:
    """Pre-cycle synthesis output. Written to mb/problems/<id>-<slug>/."""

    problem_id: int
    problem_slug: str
    drafted_at: str  # YYYY-MM-DD
    queries: list[str] = field(default_factory=list)
    top_sources: list[Hit] = field(default_factory=list)
    top_wiki: list[Hit] = field(default_factory=list)
    cross_source_patterns: list[CrossSourcePattern] = field(default_factory=list)
    proposed_approaches: list[ProposedApproach] = field(default_factory=list)
    gaps_identified: list[str] = field(default_factory=list)

    # ---------- serialization ----------

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int | None = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    @classmethod
    def from_json(cls, s: str) -> "LiteratureSynthesis":
        try:
            data = json.loads(s)
        except json.JSONDecodeError as e:
            raise ValueError(f"invalid JSON for LiteratureSynthesis: {e}") from e
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LiteratureSynthesis":
        required = ("problem_id", "problem_slug", "drafted_at")
        for key in required:
            if key not in data:
                raise ValueError(f"missing required field: {key}")
        return cls(
            problem_id=int(data["problem_id"]),
            problem_slug=str(data["problem_slug"]),
            drafted_at=str(data["drafted_at"]),
            queries=list(data.get("queries", [])),
            top_sources=[Hit(**h) for h in data.get("top_sources", [])],
            top_wiki=[Hit(**h) for h in data.get("top_wiki", [])],
            cross_source_patterns=[
                CrossSourcePattern(**p) for p in data.get("cross_source_patterns", [])
            ],
            proposed_approaches=[
                ProposedApproach(**a) for a in data.get("proposed_approaches", [])
            ],
            gaps_identified=list(data.get("gaps_identified", [])),
        )

    # ---------- markdown ----------

    def to_markdown(self) -> str:
        """Render as the mb/problems/<id>-<slug>/literature-synthesis-<date>.md file."""
        lines: list[str] = []
        lines.append("---")
        lines.append("type: literature-synthesis")
        lines.append("author: agent")
        lines.append(f"problem_id: {self.problem_id}")
        lines.append(f"problem_slug: {self.problem_slug}")
        lines.append(f"drafted: {self.drafted_at}")
        lines.append("---")
        lines.append("")
        lines.append(f"# Literature synthesis: P{self.problem_id} — {self.problem_slug}")
        lines.append("")
        lines.append("## Queries")
        if self.queries:
            for q in self.queries:
                lines.append(f"- `{q}`")
        else:
            lines.append("_None._")
        lines.append("")
        lines.append("## Top sources")
        lines.extend(_format_hits(self.top_sources))
        lines.append("")
        lines.append("## Top wiki pages")
        lines.extend(_format_hits(self.top_wiki))
        lines.append("")
        lines.append("## Cross-source patterns")
        if self.cross_source_patterns:
            for p in self.cross_source_patterns:
                lines.append(f"### {p.name}")
                lines.append("")
                lines.append(p.description)
                if p.supporting_sources:
                    lines.append("")
                    lines.append("Supporting sources:")
                    for src in p.supporting_sources:
                        lines.append(f"- [`{src}`]({_rel(src)})")
                lines.append("")
        else:
            lines.append("_None identified._")
            lines.append("")
        lines.append("## Proposed approaches")
        if self.proposed_approaches:
            for i, a in enumerate(self.proposed_approaches, 1):
                lines.append(f"### {i}. {a.description}")
                if a.rationale:
                    lines.append("")
                    lines.append(f"**Rationale:** {a.rationale}")
                if a.cited_sources:
                    lines.append("")
                    lines.append("Cites:")
                    for src in a.cited_sources:
                        lines.append(f"- [`{src}`]({_rel(src)})")
                lines.append("")
        else:
            lines.append("_None proposed._")
            lines.append("")
        lines.append("## Gaps identified")
        if self.gaps_identified:
            for g in self.gaps_identified:
                lines.append(f"- {g}")
        else:
            lines.append("_None._")
        lines.append("")
        return "\n".join(lines)


def _format_hits(hits: list[Hit]) -> list[str]:
    if not hits:
        return ["_None._"]
    out: list[str] = []
    for h in hits:
        pct = int(round(h.score * 100))
        out.append(f"- **{pct}%** [`{h.path}`]({_rel(h.path)}) — {h.snippet}")
    return out


def _rel(path: str) -> str:
    """Make a docs/source/foo path into a relative link from mb/problems/<id>-<slug>/."""
    # mb/problems/<id>-<slug>/X.md → cb/<path> means ../../../cb/<path>
    return f"../../../cb/{path}"


# JSON Schema used by `claude -p --json-schema`. Shape mirrors LiteratureSynthesis.
JSON_SCHEMA: str = json.dumps(
    {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["problem_id", "problem_slug", "drafted_at"],
        "properties": {
            "problem_id": {"type": "integer"},
            "problem_slug": {"type": "string"},
            "drafted_at": {"type": "string"},
            "queries": {"type": "array", "items": {"type": "string"}},
            "top_sources": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["path", "score", "snippet", "collection"],
                    "properties": {
                        "path": {"type": "string"},
                        "score": {"type": "number"},
                        "snippet": {"type": "string"},
                        "collection": {"type": "string"},
                    },
                },
            },
            "top_wiki": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["path", "score", "snippet", "collection"],
                    "properties": {
                        "path": {"type": "string"},
                        "score": {"type": "number"},
                        "snippet": {"type": "string"},
                        "collection": {"type": "string"},
                    },
                },
            },
            "cross_source_patterns": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["name", "description"],
                    "properties": {
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "supporting_sources": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                },
            },
            "proposed_approaches": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["description"],
                    "properties": {
                        "description": {"type": "string"},
                        "cited_sources": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "rationale": {"type": "string"},
                    },
                },
            },
            "gaps_identified": {"type": "array", "items": {"type": "string"}},
        },
    }
)
