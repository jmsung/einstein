"""research_synthesis — pre-cycle literature synthesis for the autonomous loop.

Anchored in `knowledge/wiki/findings/research-synthesis-design.md` (G0). The package
turns the four cross-source patterns (raw artifact > summary, change-manifests,
citation provenance, pre-cycle synthesis) into runnable substrate:

- `schema.py`     — typed `LiteratureSynthesis` output (JSON + markdown serializers)
- `query.py`      — qmd subprocess wrapper + multi-query gather/dedupe
- `synthesizer.py`— claude_headless orchestration; takes hits, returns synthesis

The CLI is `cb/scripts/research_synthesis.py`. Tests use injectable runners so no
real `qmd` or `claude -p` invocation happens in CI.
"""

from __future__ import annotations

from einstein.research_synthesis.query import gather, query_qmd
from einstein.research_synthesis.schema import (
    JSON_SCHEMA,
    CrossSourcePattern,
    Hit,
    LiteratureSynthesis,
    ProposedApproach,
)
from einstein.research_synthesis.synthesizer import synthesize

__all__ = [
    "JSON_SCHEMA",
    "CrossSourcePattern",
    "Hit",
    "LiteratureSynthesis",
    "ProposedApproach",
    "gather",
    "query_qmd",
    "synthesize",
]
