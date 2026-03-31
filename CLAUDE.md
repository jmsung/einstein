# Einstein Arena — Agent Instructions

## This Repo is PUBLIC

Competitors can read every file and commit. Never put secret methodology in committed files.

### What goes where
- **`docs/*.md`** (committed) — high-level approach only. No exact parameters, seeds, multipliers, block positions, or step-by-step reproduction details.
- **`docs/strategy.md`** (gitignored) — local index pointing to MB docs. Read this first.
- **`scripts/`** (committed) — generic optimizer scaffolding. Not the exact parameters that produced winning scores.
- **`scripts/secret/`** (gitignored) — symlinks to MB winning scripts.
- **`results/`** (gitignored) — solution files, never committed.
- **Workbench MB** (`~/projects/workbench/memory-bank/einstein/`) — ALL secrets go here.

### Before committing any .md or .py file, ask:
> "Would I want my competitor to read this?"
> If no → put it in MB, not the repo.

## Before Starting a New Problem

1. Read `docs/strategy.md` for MB reference paths
2. Read MB `docs/cross-problem-lessons.md` for transferable wisdom
3. Read MB `docs/problem-{id}/docs/strategy.md` if the problem has prior work

## Testing

```bash
uv run python -m pytest tests/ -v
```

All tests must pass before committing. Currently 108 tests.

## File Organization

- `src/einstein/` — importable library (evaluators, verifiers)
- `scripts/` — optimizer entry points (one per approach)
- `tests/` — pytest tests for all library code
- `docs/` — one public MD per problem + arena overview
- `results/` — gitignored, organized per-problem subfolder

## Doc Rules

- One public MD per problem: `docs/problem-{id}-{name}.md`
- Every MD file has `*Last updated: YYYY-MM-DD*` at the bottom
- Update timestamp whenever the file is revised

## Dependencies

```bash
uv sync        # install all deps
uv run ...     # run scripts
modal run ...  # GPU scripts (needs Modal account)
```

## Arena

- API key: `.env` (gitignored)
- Agent name: JSAgent
- 5 submissions per 30 min
- n ≤ 100,000 for array solutions
- Always verify locally before submitting
