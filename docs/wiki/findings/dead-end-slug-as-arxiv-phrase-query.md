---
type: finding
author: agent
drafted: 2026-05-23
question_origin: feat/autonomous-loop Phase 1 (seed_ingest dogfood)
status: answered
related_concepts: []
related_techniques: []
related_findings: []
cites:
  - ../../tools/seed_ingest.py
  - ../../tools/gap_search.py
  - ../../agent/concept-coverage.json
---

# Dead end: feeding wiki concept slugs as exact-phrase arxiv queries

## TL;DR

The first end-to-end dogfood of `seed_ingest.py propose` against the real wiki yielded ~0 useful arxiv hits across 36 actionable (under-sourced + missing-page) concepts. Root cause: wiki concept slugs are agent-internal jargon (`bounded-lbfgs-per-region-sigmoid.md`, `slsqp-active-pair-polish.md`, `mpmath-ulp-polish.md`), not literature vocabulary. Passed verbatim as quoted phrase queries to arxiv, they hit 0 papers. The 1/36 hit (`packing-techniques.md`) returned irrelevant matches because "packing techniques" is too generic. The tools work mechanically — the empirical seeding strategy needs a slug → search-vocabulary translation step before this pipeline produces useful priors.

## What we tried

- Built `concept_inventory.py` to classify 77 referents into `well-covered` / `under-sourced` / `missing-page` / `orphan-or-singleton`. 36 rows were actionable.
- Built `seed_ingest.py propose` to call `gap_search.build_query` + `search_arxiv` per actionable concept, then write a candidates JSON for human approval.
- Ran propose against the real wiki (twice — first without rate-limit, hit HTTP 429; second with 3.5s sleep but during the IP cooldown window). Inspected the first run's partial results: 1/36 concept blocks had candidates; the 1 hit was off-topic.

## Why it failed

Two overlapping reasons, listed in order of importance:

1. **Vocabulary mismatch.** Wiki concept slugs encode method names from our internal frame: `slsqp-active-pair-polish`, `bounded-lbfgs-per-region-sigmoid`, `mpmath-ulp-polish`, `larger-n-cascade`, `warm-start-from-leader`. None of these phrases appear verbatim in arxiv abstracts because they're our compound-noun shorthand for several literature concepts. Even substantive math slugs (`basin-rigidity`, `parameterization-selection`, `equioscillation-escape`) are project-coined terms — a literature search for `"basin rigidity"` returns 0; the literature talks about `"local minima"`, `"plateau structure"`, `"first-order rigidity"`, etc. The slug-as-phrase strategy assumes our naming aligns with the literature; it doesn't.

2. **Exact-phrase + math-category filter is over-constrained.** `gap_search.build_query` wraps the keyword in `all:"..."` quotes and ANDs with a 7-category math filter. Two layers of restriction over an already-bad query produces nothing. Even relaxing to AND-of-individual-words would miss most of these (`mpmath` and `ulp` are unlikely to co-occur in any math paper).

A secondary operational issue surfaced: arxiv's anti-abuse layer applied an IP-level cooldown after the first un-throttled run, so the rate-limit-fixed second run also returned 429s for ~10–20 minutes. The 3.5s inter-request sleep is the correct steady-state policy but doesn't help during a cooldown burn-off.

## What this rules out

- **1:1 slug-as-exact-phrase arxiv search** for bulk seeding wiki priors. The shape "iterate over our slugs, query each verbatim" cannot produce useful seed papers at any meaningful yield.
- Any autonomous-loop component that uses our internal slugs unmediated as external-search keys.

## What might still work

Listed in increasing ambition:

- **Multi-keyword AND with stop-words stripped + de-jargoned heads.** E.g., for `mpmath-ulp-polish.md`, drop `mpmath` (tool name, not a concept), search `"high precision polish"` OR `"final-digit accuracy"`. Hand-curated for the 36 rows; ~2 hours. Tests the rest of the pipeline (download + pdf_to_md + source/ frontmatter) with real arxiv hits.
- **Slug → vocabulary mapping file.** A YAML at `docs/tools/concept-search-terms.yaml` that maps each in-wiki slug to one or more search queries. Human-curated, auditable, version-controlled. Once populated, propose reads it instead of round-tripping through gap_search's slug heuristic.
- **LLM-assisted vocabulary translation.** At propose time, an LLM call: "given concept page `<wiki/concepts/basin-rigidity.md>` (full body), return 3 search-vocabulary phrases that a math literature search would actually hit." This is the autonomous version, but adds an LLM dep + cost.
- **Diversify beyond arxiv.** Google Scholar (no API), semanticscholar.org (has API, less math-jargon-aligned than arxiv), zbMATH (math-specific abstract index). Each adds engineering cost.

## Side-effect lessons (worth incorporating regardless of strategy)

- **arxiv API 429 backoff.** `gap_search.search_arxiv` should retry with exponential backoff on 429 instead of silently returning `[]`. Small change; would catch transient throttling without losing data.
- **Cooldown awareness.** When a propose run is interrupted by 429s, the candidates JSON ends up with 0-hit rows for the throttled concepts. Re-running propose should detect 0-hit rows that were previously throttled and re-search them, not skip on "I already saw this concept."

## Status of dependent work

- The three Phase-1 tools (`concept_inventory.py`, `pdf_to_md.py`, `seed_ingest.py`) are mechanically validated by 35 passing tests.
- The vocabulary mapping pivot (sub-task 1.4b) added `docs/tools/concept-search-terms.yaml` with 33 hand-curated slug → arxiv-phrase entries. Re-running propose yielded **9/36 concepts with hits** (vs 1/15 pre-pivot), totalling ~19 raw candidates (~10–12 clearly relevant after eyeballing + dedup).
- Phase 1 deliverable "30–50 new source/ papers" remains **partially met**: ~10–12 good candidates is the honest size of the gap, not 30–50. 18/36 mapped concepts still return 0 (vocab needs iteration); 9/36 are intentionally project-coined and unmappable.
- Phase 2 (a local workstation calibration) does not depend on this; can proceed.
- Phase 3 (outer orchestrator) is the natural home for the autonomous version of the vocabulary translation.

## Updated rule of thumb

- Wiki concepts that map to **named methods** (CMA-ES, Lovász local lemma, basin hopping, first-order rigidity, Chebyshev equioscillation, Remez exchange) **search well**. Yield ≥ 1 hit each, often relevant.
- Wiki concepts that are **arena/optimizer-specific framings** (`arena-tolerance-drift`, `minimprovement-gate`, `multistart-with-rotation-lottery`, `gpu-decision-framework`) **do not exist in the literature**. Mark intentionally-unmapped; don't waste an arxiv slot.
- Wiki concepts that are **project compound nouns** (`mpmath-ulp-polish`, `bounded-lbfgs-per-region-sigmoid`, `larger-n-cascade`) **need de-jargoning to component literature terms** before they search well — and even then often return 0 because the literature talks about the *general* method, not our specific application stack.
