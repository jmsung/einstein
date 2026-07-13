<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: repo
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: mareforma/mareforma — signed claim-graph for research agents
authors: [mareforma]
source_url: https://github.com/mareforma/mareforma
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# mareforma/mareforma

**Language:** Python · **License:** MIT

## What it is

A cryptographically signed, **graph-based record system for AI research findings** — "a local store where research agents write their claims." It gives multi-step agent pipelines a verifiable, auditable memory layer.

## Key features

- **Typed claims** (ANALYTICAL, INFERRED, DERIVED) that earn **trust levels** (PRELIMINARY → REPLICATED → ESTABLISHED) through *independent convergence*, not self-declaration.
- **Provenance tracking** — full lineage of any finding: upstream citations, downstream dependents, signatures, contradictions.
- **Contradiction handling** — conflicting claims coexist; consumers filter by trust level / classification rather than the store picking a winner.
- **Failure visibility** — distinguishing analytical results from LLM-filled fallbacks surfaces otherwise-silent pipeline failures.

