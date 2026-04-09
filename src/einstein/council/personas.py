"""Persona dataclass, markdown loader, and dispatch function.

All persona content (names, prompt seeds, triggers, literature) is parsed
at runtime from a private config file. This module contains no persona
text — only the data shape and the parser.

Path resolution order:

1. Explicit ``path=`` argument to ``load_personas`` / ``dispatch``
2. ``EINSTEIN_COUNCIL_PATH`` environment variable
3. Sibling of the knowledge layer's resolved path (if available)

If none of these point at an existing file, ``load_personas`` returns an
empty list and ``dispatch`` returns ``[]``. CI environments without the
private config simply get an empty council.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from einstein.knowledge import KNOWLEDGE_PATH

_COUNCIL_FILENAME = "mathematician-council.md"


def _resolve_default_path() -> Path | None:
    """Resolve the default council file location without hard-coding it.

    Prefers the env var; otherwise sits next to whatever the knowledge
    layer already resolved (the council file lives in the same private
    docs directory as ``knowledge.yaml``).
    """
    env_path = os.environ.get("EINSTEIN_COUNCIL_PATH")
    if env_path:
        candidate = Path(env_path)
        return candidate if candidate.exists() else None
    if KNOWLEDGE_PATH is not None:
        candidate = KNOWLEDGE_PATH.parent / _COUNCIL_FILENAME
        if candidate.exists():
            return candidate
    return None


COUNCIL_PATH: Path | None = _resolve_default_path()


@dataclass(frozen=True)
class Persona:
    """A mathematician persona used to seed a research subagent.

    Attributes:
        name: Mathematician's name (e.g. "Gauss", "Viazovska").
        perspective: Short tag line for the perspective they bring.
        tier: "core" (always dispatched) or "bench" (conditional).
        expertise: One-line summary of real-world expertise.
        prompt_seed: Seed prompt text injected into the subagent.
        literature: Recommended literature focus.
        example_insight: Worked example of the persona's insight.
        trigger_categories: Problem categories that trigger a bench
            persona. Always empty for core personas.
    """

    name: str
    perspective: str
    tier: str
    expertise: str
    prompt_seed: str
    literature: str
    example_insight: str
    trigger_categories: frozenset[str] = field(default_factory=frozenset)


# ---------------------------------------------------------------------------
# Markdown parser
# ---------------------------------------------------------------------------

# Core headers look like `### 1. Gauss — Number theory, algebraic constructions`
# Bench headers look like `### Viazovska — Sphere packing optimality proofs`
# We accept both em-dash (—) and hyphen (-) as the separator.
_PERSONA_HEADER = re.compile(
    r"^###\s+(?:\d+\.\s+)?(?P<name>[^—\-\n]+?)\s*[—\-]\s*(?P<perspective>.+?)\s*$",
    re.MULTILINE,
)
_FIELD_LINE = re.compile(r"^-\s+\*\*(?P<key>[^*]+?)\*\*:\s*(?P<value>.+?)\s*$")
_CATEGORY_TOKEN = re.compile(r'"([^"]+)"')

_FIELD_KEY_MAP = {
    "real expertise": "expertise",
    "expertise": "expertise",
    "prompt seed": "prompt_seed",
    "literature focus": "literature",
    "literature": "literature",
    "example insight": "example_insight",
    "trigger rule": "trigger_rule",
}


def _parse_trigger_categories(raw: str) -> frozenset[str]:
    """Pull quoted category strings out of a trigger-rule expression.

    The config writes triggers like:
        ``problem.category in {"sphere_packing", "kissing_number"}``
        ``problem.category == "graph_theory"``
    We just collect every quoted token — order-independent and tolerant
    of either form.
    """
    return frozenset(_CATEGORY_TOKEN.findall(raw))


def _parse_section(text: str, tier: str) -> list[Persona]:
    """Parse one tier section of the council markdown into Persona objects."""
    personas: list[Persona] = []
    matches = list(_PERSONA_HEADER.finditer(text))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]

        fields: dict[str, str] = {}
        for line in body.splitlines():
            fm = _FIELD_LINE.match(line)
            if not fm:
                continue
            key = _FIELD_KEY_MAP.get(fm.group("key").strip().lower())
            if key:
                fields[key] = fm.group("value").strip().strip('"')

        triggers = (
            _parse_trigger_categories(fields.get("trigger_rule", ""))
            if tier == "bench"
            else frozenset()
        )

        personas.append(
            Persona(
                name=m.group("name").strip(),
                perspective=m.group("perspective").strip(),
                tier=tier,
                expertise=fields.get("expertise", ""),
                prompt_seed=fields.get("prompt_seed", ""),
                literature=fields.get("literature", ""),
                example_insight=fields.get("example_insight", ""),
                trigger_categories=triggers,
            )
        )
    return personas


def load_personas(path: Path | None = None) -> list[Persona]:
    """Parse the council markdown into Persona objects.

    The file is split on the ``## Specialist Bench`` header — everything
    before is core, everything after is bench. Returns an empty list if
    the file is missing (e.g. CI environments without the private config).
    """
    target = path if path is not None else COUNCIL_PATH
    if target is None or not Path(target).exists():
        return []

    raw = Path(target).read_text()

    # Split on the specialist bench header. Anything before is core; after
    # is bench. If the bench header is absent, treat the whole file as core.
    bench_split = re.split(
        r"^##\s+Specialist Bench.*$", raw, maxsplit=1, flags=re.MULTILINE
    )
    core_text = bench_split[0]
    bench_text = bench_split[1] if len(bench_split) == 2 else ""

    # Trim core_text to start at the "## Core Council" header if present,
    # so we don't pick up persona-like headers from the preamble.
    core_match = re.search(r"^##\s+Core Council.*$", core_text, flags=re.MULTILINE)
    if core_match:
        core_text = core_text[core_match.end():]

    return _parse_section(core_text, "core") + _parse_section(bench_text, "bench")


def dispatch(
    problem_category: str,
    *,
    path: Path | None = None,
) -> list[Persona]:
    """Return personas to deploy for a given problem category.

    Always returns every core persona, in declaration order, followed by
    every bench persona whose ``trigger_categories`` contains
    ``problem_category``.

    Args:
        problem_category: Category string from the problem metadata
            (e.g. "kissing_number", "graph_theory", "autocorrelation").
        path: Optional override for the council config location.
            Defaults to the resolved ``COUNCIL_PATH``.

    Returns:
        Ordered list of Persona objects: core first, then triggered
        bench specialists. Empty list if the council file is missing.
    """
    personas = load_personas(path)
    if not personas:
        return []
    core = [p for p in personas if p.tier == "core"]
    bench = [
        p
        for p in personas
        if p.tier == "bench" and problem_category in p.trigger_categories
    ]
    return core + bench
