# source/

In-git, LLM-distilled `.md` summaries of artifacts in `../raw/`. Flat layout: each file at `source/<stem>.md` corresponds 1:1 with a native original at `../raw/<stem>.<ext>` (gitignored).

Provenance lives in **frontmatter**, not folders.

## Frontmatter schema

```yaml
---
type: source
kind: paper | arxiv | repo | blog | oeis | book | talk
title: <full title>
authors: [<author 1>, <author 2>, ...]
year: 2025
source_url: https://...
source_local: ../raw/<stem>.<ext>      # optional — pointer to gitignored original
source_hash: sha256:<prefix>           # optional — verify integrity
ingested_at: YYYY-MM-DD
ingested_by: agent | human
drafted: YYYY-MM-DD                    # alias of ingested_at; kept for back-compat
level: 4                               # precedence layer (4 = raw distillation, L2 conceptually)
status: complete | partial | stub | needs-update
summary: <one-line>                    # optional but recommended — makes qmd queries sharper
tags: [<concept-or-topic>, ...]        # optional — free-form topic tags
cites:                                 # back-cites: which wiki pages reference this
  - <wiki/path>.md
related_problems: [<problem-id-or-slug>, ...]   # optional — which arena problems use this
drive_backup: <gdrive-id>              # optional — cold-storage backup
---
```

`kind` replaces the old `provenance:` folder. `paper-*.md`, `blog-*.md`, etc. **are not** the filename convention — filenames stay flat (e.g., `1971-leech-sphere-packing.md`); `kind` in frontmatter is the queryable index.

## Filename convention

`<year>-<author-or-slug>-<topic>.md` for papers; `<year-or-empty>-<slug>.md` otherwise.

Examples:
- `1971-leech-sphere-packing.md` (paper)
- `2026-togetherai-einstein-arena.md` (blog)
- `jmsung-einstein.md` (repo)

## Lifecycle

```
external artifact → /wiki-ingest
                     ├──→ ../raw/<stem>.<ext>     (gitignored, local cache)
                     └──→ source/<stem>.md        (in git, distilled, frontmatter complete)
```

`../raw/` is gitignored — `source/` is the canonical in-git record. If `../raw/` is missing, the frontmatter has enough (`source_url`, `source_hash`, `drive_backup`) to re-fetch.

## Querying

```bash
qmd query "<question>" -c einstein-wiki-source -n 5
```

The qmd index is keyed by content, not path. Frontmatter `kind`, `year`, `tags` are visible in `qmd ls` output for filtering.
