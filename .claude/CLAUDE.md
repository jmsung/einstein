# `.claude/` — repo-specific Claude config for einstein

Layout overview. The substantive rules live in `rules/`; this file stays short.

## Repo character

einstein is a **single-developer math knowledge base + agent codebase**, public, with two layers that grow together:

- `wiki/` — the math wisdom (concepts, techniques, personas, findings, problems, questions). Either human or agent may author, with mandatory frontmatter attribution.
- `src/` — the agent code that solves Einstein Arena problems and writes back to the wiki.

The work loop is **understand → wiki-first → council dispatch → gap detect → research → distill → specialize → execute → look back → failure-log → commit**. Each cycle compounds in the wiki.

Math wisdom is the goal — not arena rank. Submission is verification only. No external posts; the wiki is the publication channel.

## Layout

```
.claude/
├── CLAUDE.md            # this file — repo character + rules index
├── rules/               # behavioral rules, one topic per file
│   ├── agent-stance.md             (always loads)
│   ├── wiki-first-lookup.md        (always loads)
│   ├── math-solving-protocol.md    (always loads)
│   ├── council-dispatch.md         (always loads)
│   ├── self-improvement-loop.md    (always loads)
│   ├── ask-the-question-first.md   (always loads)
│   ├── triple-verify.md            (always loads)
│   ├── failure-is-a-finding.md     (always loads)
│   ├── wiki-attribution.md         (always loads)
│   ├── compute-router.md           (always loads)
│   └── axioms.md                   (always loads — slim, 4 axioms)
├── settings.local.json   # gitignored, machine-specific
└── (skills/, agents/ — only if einstein-specific; otherwise rely on harness)
```

## Rules — loading + conventions

Per Claude Code docs: rules without `paths:` frontmatter load every session; rules with `paths:` only load when files matching those globs are read. One topic per file.

Each rule body: rule itself → **Why** (triggering incident if applicable) → **How to apply**. The "why" is what keeps rules from decaying into cargo-cult.

### Size budget (soft caps)

| File | Lines | When exceeded |
|---|---|---|
| `CLAUDE.md` (this file) | ≤100 | Demote to subdir READMEs |
| `rules/*.md` | 25–80 | Compress / merge / promote / delete |

| Folder | Limit | When exceeded |
|---|---|---|
| `rules/` always-loaded | ≤12 active | Audit; merge or demote |
| `rules/` total | ≤25 | Audit; nest by area |

## Notes

- **No `commands/`** — older mechanism; superseded by skills. Don't add it back.
- **Root `CLAUDE.md` (cb/CLAUDE.md)** is the repo's umbrella contract (code conventions + pointers to wiki and rules). Edit there for code-level rules; here for behavioral rules.
- **`wiki/CLAUDE.md`** is the wiki contract (machine-readable + prose). Edit there for wiki-layer changes.
- **harness/** holds global agents/skills/CLAUDE.md applying to all repos. Check there before adding einstein-specific equivalents.
