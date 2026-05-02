---
wiki: einstein-wiki
status: pilot
contract_version: 0.1

layers:
  raw: ../raw/
  source: ../source/
  notes: ../../mb/notes/        # private; agent never writes
  wiki: ./

raw_subfolders: [papers, arxiv, repos, blog, oeis]

raw_format:
  papers: pdf
  arxiv: pdf
  repos: md
  blog: md
  oeis: md

filename_conventions:
  papers: "<year>-<firstAuthor>-<slug>"
  arxiv: "<year>-<firstAuthor>-<slug>"
  repos: "<org>-<repo>"
  blog: "<YYYY-MM-DD>-<domain>-<slug>"
  oeis: "<oeis-id>-<slug>"

ingest:
  human_gated: true
  auto_distill: true
  touches_wiki: false
  agent_writes_raw: never_without_approval
  agent_writes_source: auto_distill_with_approval
  agent_writes_notes: never
  agent_writes_wiki: with_attribution_either_author

authorship:
  policy: bidirectional   # either human or agent may author wiki pages
  required_frontmatter: [type, author, drafted]
  author_values: [agent, human, hybrid]
  promotion: human_gated  # finding → concept upgrade requires human approval

search:
  default: wiki_first
  corpus: [wiki/, source/]
  qmd_collections:
    wiki: einstein-wiki
    source: einstein-wiki-source
  web: opt_in_explicit
  cross_wiki_allowlist: []

routing:
  default: heuristic
  triggers:
    web: [search web, online, look online, search the internet, google]
    wiki_query_force: [search the wiki, wiki query]
    capture: [learn, save this, add to wiki, file this, wiki-learn]
  empty_wiki_fallback: ask_user
  ambiguous_default: wiki_query

wiki_navigation:
  front_door: home.md
  catalog: index.md
  ops_log: log.md
  categories: [concepts, techniques, personas, findings, problems, questions]

precedence:
  L0: ../.claude/CLAUDE.md
  L1: wiki/
  L2: source/
  L3: raw/
  rule: "lower L wins for what's true; higher L wins for what we decided to do about it"
---

# einstein-wiki — math wisdom contract

A self-improving math knowledge base. The agent and the human co-author it; the wiki + agent code is the public artifact. Math wisdom is the goal — not arena rank.

The YAML frontmatter above is the **machine-readable contract** — wiki skills parse it instead of hardcoding paths. The prose below is the human-facing rationale.

## Scope

- **In bounds**: math concepts (LP duality, Cohn–Elkies, equioscillation, modular forms, …), concrete techniques (parallel tempering, mpmath polish, Remez, SDP flag algebra, …), embodied mathematician personas (Gauss, Tao, Polya, …), cross-problem findings, per-arena-problem index pages, open math questions.
- **Out of bounds**: per-problem live experiment state (in `mb/tracking/`), code (in `src/`), result files (in `results/`).

## Layers

```
../raw/        # GITIGNORED. Local cache of native-format originals (PDFs, html, md).
  papers/  arxiv/  repos/  blog/  oeis/
../source/     # in-git. 1:1 LLM-distilled .md per raw artifact.
  papers/  arxiv/  repos/  blog/  oeis/
./             # synthesized, hand- or agent-curated pages
  home.md      # narrative front door
  index.md     # catalog
  log.md       # append-only ops record
  concepts/    # WHAT-IS — durable mental models
  techniques/  # HOW-TO — concrete methods
  personas/    # embodied mathematician perspectives + _synthesis.md (the 12 stances)
  findings/    # specific Q→A with cites
  problems/    # one index per arena problem + _inventory.md (compass)
  questions/   # open math questions awaiting research
```

`raw/` and `source/` are organized by **provenance** (where it came from). Topic-routing happens here in `wiki/`. `raw/` is gitignored — it's a local working cache; `source/` is the canonical in-git record (frontmatter holds source URL, hash, optional Drive backup).

## Authorship symmetry

Either party — human or agent — can author wiki pages. The honesty layer is **mandatory frontmatter attribution**:

```yaml
---
type: concept | technique | finding | persona | question | problem
author: agent | human | hybrid
drafted: YYYY-MM-DD
confirmed_by: human       # optional, after human review of an agent-drafted page
cites: [paths to findings/concepts/source]
---
```

Quality bar applies regardless of author: grounded in `source/` or established literature, citations to specific files, claims that can be checked. **Promotion** (e.g., finding cited 3+ times → concept) is human-gated.

This is a deliberate departure from the jongmin-wiki "wiki pages NEVER created automatically" rule. For einstein, agent CAN create pages — that *is* the self-improvement signal. Attribution makes the experiment honest.

## Ingest

- **Human-gated.** `/wiki-ingest` shows a preview of the source/ distillation; one approval covers raw + source.
- **`raw/` is gitignored.** Native originals live as PDFs/html/md in local cache. `source/` is the canonical in-git record.
- **Auto-distill.** Every ingest writes both raw/ + source/.
- **Wiki/ is never touched on ingest.** Synthesis pages are authored separately (manual, `/wiki-learn`, or `/wiki-query --file-back`).

## Categories

| Category | Cardinality | Examples | Authored from |
|---|---|---|---|
| `concepts/` | many:1 from sources | LP duality, equioscillation, Cohn-Elkies, modular forms, basin rigidity, parameterization selection | Distillation across multiple problems / sources |
| `techniques/` | many:1 from concepts | Parallel tempering, mpmath ulp polish, Remez exchange, SDP flag algebra, compute router | Concept + implementation knowledge |
| `personas/` | bounded ~21 | Gauss, Riemann, Tao, Conway, Polya, Hilbert, …, plus `_synthesis.md` (12 stances) | Hand-curated per mathematician |
| `findings/` | seed for concepts | Q→A pages with cites | Single-problem or council outputs |
| `problems/` | 23 + `_inventory.md` | One short index per arena problem | Per-problem rollup |
| `questions/` | open seed-bed | "Why does X work?" with status: open/answered/abandoned | Council dispatch + gap detect |

## Search

Two qmd collections cover this wiki:

- `einstein-wiki` — indexes `wiki/` (synthesis layer; primary)
- `einstein-wiki-source` — indexes `source/` (distilled summaries; cited evidence)

`/wiki-query` queries both and merges. Web search is opt-in only — say "search the web" to enable.

## Default question routing

Questions in this repo route automatically (no need to type `/wiki-query`):

- **Math / arena / einstein-related** → implicit `/wiki-query`, cited answer
- **General programming / common ML** → answer from training

Trigger words override:
- `"search web"` / `"online"` → web flow with ingest approval
- `"search the wiki"` → force `/wiki-query`
- `"learn"` / `"save this"` / `"add to wiki"` → capture the answer

## Wiki page creation triggers

| Trigger | What happens |
|---|---|
| Manual edit | Author writes a page directly |
| `/wiki-learn` | Distills *conversation* insights into wiki pages (with attribution) |
| `/wiki-query --file-back` | Saves a synthesized answer as a wiki page |
| Council dispatch | Each persona writes a question to `wiki/questions/` |
| Question answered | Distill answer + cites into `wiki/findings/` |
| Approach failed | Write the *why* into `wiki/findings/dead-end-<slug>.md` |
| Worktree-done distillation | Reusable concept/technique → `wiki/concepts|techniques/` |
| Finding cited 3+ times | Promote to a concept (human-gated) |

## Precedence

See `precedence` in the frontmatter. Default for this wiki:

- **L0 `.claude/CLAUDE.md` + rules/ + axioms** wins on scope, gates, behavior.
- **L1 `wiki/`** wins on interpretation, synthesis, decisions.
- **L2 `source/`** wins on "what does the artifact say."
- **L3 `raw/`** is ground truth about the artifact itself.

## What this wiki is NOT

- Not per-problem live experiment state — that's `mb/tracking/<problem>/`.
- Not code — that's `src/`.
- Not result files — that's `results/`.
- Not external posts — there are none. The wiki *is* the publication channel.
