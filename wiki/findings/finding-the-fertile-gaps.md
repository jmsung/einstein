---
type: finding
author: hybrid
drafted: 2026-05-02
question_origin: cross-problem
status: answered
related_concepts: []
related_techniques: []
related_findings: [cross-pollination-not-compute.md]
related_personas: [atiyah.md, _synthesis.md]
cites:
  - cross-pollination-not-compute.md
---

# Finding fertile gaps: how the wiki should detect its own missing connections

## TL;DR

Five distinct types of "knowledge gap" surface different breakthrough opportunities. Detect them mechanically: parse the wiki as a graph, layer it with semantic similarity from qmd, compare the two graphs. **The cross-pollination-not-compute filter says *which* candidates to keep; the gap detector says *which* candidates to even consider.** Together they form the discipline that produces FLT-style cross-domain breakthroughs.

## The five gap types (FLT-illustrated)

Wiles needed: modular forms (analytic), Galois representations (algebraic), elliptic curves (geometric), Frey curve (specific construction), Ribet's theorem (bridge). The proof was 7 years of closing connections that *should have been there but weren't*. The gap-detector classifies these:

| Type | Description | FLT example | Detection mechanism |
|---|---|---|---|
| **1. Missing concept** | Noun phrase mentioned ≥3 times across pages, no own page | "Galois representation" referenced in many places, no dedicated page | Parse pages, extract concept-like noun phrases, count, check against existing slugs |
| **2. Missing connection** | Two concepts both exist but no page bridges them | Modular forms + Galois reps both exist; Serre's connection wasn't documented | Co-citation matrix: high qmd similarity, zero explicit edge |
| **3. Missing equivalence** | Problem in domain X is secretly the same problem in domain Y | "Counterexample to FLT ⟺ elliptic curve with non-modular Galois rep" — Frey's insight | LLM-driven structural pattern-matching across problem statements |
| **4. Missing chain** | Path A → B → C → … → Z too long or absent in the explicit graph | Frey curve → Ribet → modularity; without all three the proof can't span the gap | Graph shortest-path on the citation network |
| **5. Missing umbrella** | Property held by multiple pages with no abstracting meta-page | "All semistable elliptic curves over Q are modular" abstracts a property of many curves | Cluster pages by qmd similarity, find clusters whose centroid has no concept page |

Wiles' breakthrough was simultaneously closing types 2, 3, and 4. The wiki should be designed to *surface* these gaps actively, not wait for them to be noticed.

## Why this is detectable

The wiki *contains* the citation graph implicitly — every `cites:` field, `[[wikilink]]`, and `related_*` is an edge. **Materializing** the graph (extracting it into a NetworkX-style structure) makes algorithms possible: in-degree, out-degree, shortest paths, components, co-citation matrices.

That alone catches Types 1, 4, and 5 (partial).

For Type 2 — the *most valuable* gap type, the FLT one — the explicit graph isn't enough. Two pages can be on the same topic but never link to each other (because nobody noticed). Adding a **semantic-similarity layer** from qmd embeddings creates a second graph: pages with similarity ≥ 0.7 get a "latent edge."

The Type-2 detection is then: **pairs with high latent-edge weight but zero explicit edge.** That's "wiki thinks they're related; nobody wrote it down."

Type 3 (structural analogy) requires LLM judgment — too creative for a graph algorithm. Stays a research-subagent task.

## How the discipline composes with cross-pollination-not-compute

The two findings are complementary:

| Finding | Question it answers |
|---|---|
| `cross-pollination-not-compute.md` | Of the candidates I'm considering, which should I actually pursue? (filter for *retention*) |
| `finding-the-fertile-gaps.md` | What candidates should I even consider? (filter for *generation*) |

In sequence: gap-detector generates 10 candidate gaps → cross-pollination filter keeps 1-3 of them → those become questions in `wiki/questions/` → next cycle picks one up.

Without gap-detector: candidates are ad-hoc, mostly recycled from the council's seed prompts. The agent reaches for what's nearby in context, not what's structurally missing.

Without cross-pollination filter: gap-detector outputs 50 candidates, the agent burns compute on 50 different threads, no convergence.

Both halves are needed.

## Implementation: tools/wiki_graph.py

Built 2026-05-02. Concrete capabilities:

- Parse all `wiki/*.md` for explicit citations (frontmatter `cites:`, `related_*`, body markdown links, `[[wikilinks]]`)
- Build a NetworkX-style DiGraph from explicit edges
- Compute Type 1 (concept mentions ≥3, no page) — heuristic noun-phrase extraction
- Compute Type 2 (semantic similarity ≥ 0.7, no explicit edge) — qmd vsearch per page
- Compute Type 4 (long shortest-path between Type-2 pairs) — BFS on undirected citation graph
- Compute Type 5 (cluster of related pages with no concept centroid in top-N qmd neighbors)
- Output markdown report → `agent/wiki-gaps-<date>.md`
- Optionally file top-N Type-2 candidates as `wiki/questions/<date>-gap-<slug>.md`

Run cadence (per `cycle-discipline.md`):

- **End of every cycle**: `uv run python tools/wiki_graph.py --file-questions`
- The top-3 candidates auto-file as questions; the next cycle's council dispatch can include them.

## Cycle structure with both findings active

```
[start cycle] →
  qmd query (REFUSE without — wiki-first rule) →
  council dispatch generates persona questions →
  GAP DETECTOR adds structural-gap questions →
  cross-pollination filter keeps the most-fertile candidates →
  research / ingest / distill on the kept candidates →
  [end cycle: refresh qmd index + run gap detector + log row]
```

## Limits

- **Type 1 noun-phrase extraction is heuristic** — false positives (e.g., "circle packing" extracted from "the circle packing problem"). Manual filtering still required. The threshold (≥3 pages) catches the worst noise.
- **Type 2 similarity is qmd-dependent** — the embedding model dominates "similar" judgments. Switching the model can change Type-2 outputs significantly. Document the model in the report.
- **Type 5 is the weakest** — cluster detection without ground-truth labels is hard. The current heuristic ("findings/techniques whose top-3 qmd neighbors don't include any concept page") is a first pass.
- **Type 3 (structural analogy) is NOT in the tool** — needs LLM judgment. Recommend monthly research-subagent run with a structured prompt.

## Triggering moment

Filed during js/feat/wiki-graph branch (2026-05-02), companion to `cross-pollination-not-compute.md`. The user's framing: *"how can I find knowledge gap and fill the empty gap for generalized knowledge and breakthrough via inter-connection? for example FLT requires lots of seemingly unrelated concepts connected to each other."*

That framing made explicit what the wiki *should* be designed to do — not just store knowledge, but actively detect where its own structure is failing to connect.

## See also

- [`findings/cross-pollination-not-compute.md`](cross-pollination-not-compute.md) — the filter that decides which gap candidates to actually pursue
- [`personas/atiyah.md`](../personas/atiyah.md) — cross-field marriage as a stance
- `tools/wiki_graph.py` — the implementation
- `agent/wiki-gaps-<date>.md` — the recurring output (one per gap-detector run)

*Last updated: 2026-05-02*
