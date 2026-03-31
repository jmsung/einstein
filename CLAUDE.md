# Einstein Arena

## Setup

```bash
uv sync
uv run python -m pytest tests/ -v  # 108 tests
```

## File Organization

- `src/einstein/` — importable library (evaluators, verifiers)
- `scripts/` — optimizer entry points
- `tests/` — pytest tests
- `docs/` — one MD per problem + arena overview

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
