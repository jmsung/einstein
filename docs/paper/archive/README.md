# Paper version archive

Frozen, as-submitted PDFs of the JSAgent methodology paper. Kept so each arXiv
version can be diffed against what actually shipped (the working tree drifts;
`main.tex` uses `\today`, so a fresh build no longer reproduces a past upload).

| File | arXiv version | Submitted | Pages | md5 |
|---|---|---|---|---|
| `arxiv-v1-2026-07-01.pdf` | v1 (on moderation hold) | 2026-07-01 | 29 | `504cdfb041d7629d121e5226870e102f` |

## Notes

- **v1 source is not tagged.** The completed-branch note claimed a `paper-v1`
  git tag, but none exists. The uploaded PDF is dated "July 1, 2026"; the paper
  saw many commits that day (`git log --since=2026-07-01 --until=2026-07-02 --
  docs/paper/main.tex`), so the exact source commit is ambiguous. **This PDF is
  the ground-truth v1 record**, not any rebuild.
- The live working build (`docs/paper/main.pdf`) is already 32 pages — drifted
  past v1 — as v2 material accumulates (P7 → #1, AKC collaboration case study,
  A2 open-participation revision). See `mb/active/docs-paper-ablation-integration.md`.
