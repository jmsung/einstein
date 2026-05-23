# source/

In-git, LLM-distilled `.md` summaries of artifacts in `../raw/`. 1:1 with raw — same subpath, same stem, always `.md`.

Subfolders by **provenance** (where it came from), not topic:

- `papers/` — academic papers (PDF in raw/, distilled summary here)
- `arxiv/` — arXiv preprints
- `repos/` — README distillation, never the cloned repo
- `blog/` — blog posts (Tao, Cohn, Ellenberg, Bloom, …)
- `oeis/` — OEIS sequence pages

Each `source/<type>/<stem>.md` has frontmatter:

```yaml
---
type: source
provenance: papers | arxiv | repos | blog | oeis
source_url: https://...
retrieved: YYYY-MM-DD
distilled_from_hash: <sha256-prefix-of-raw>
drive_backup: optional Drive link
distilled_by: agent | human
---
```

`raw/` is gitignored — these distillations are the canonical in-git record. If raw is missing, the frontmatter has enough to re-fetch.

Populated in Goal 6 (references pass) — currently empty stubs.
