# Codex Instructions

This repository uses Claude-facing rule files as the durable project contract.
When working anywhere under `/Users/jongmin/projects/einstein`, Codex should
load the same context before planning or editing.

## Required Startup Reads

Read these first:

- `/Users/jongmin/projects/einstein/CLAUDE.md`
- `/Users/jongmin/projects/einstein/.claude/CLAUDE.md`
- Relevant files under `/Users/jongmin/projects/einstein/.claude/rules/`
- The active branch tracker under `/Users/jongmin/projects/einstein/mb/active/`

For branch work, identify the current git branch and read the matching tracker
when present, for example:

- `feat/autonomous-loop` -> `mb/active/feat-autonomous-loop.md`

## How To Use `mb/`

`mb/` is the private worktree memory layer. Do not bulk-read it. Use targeted
reads/searches:

- current active branch file in `mb/active/`
- relevant completed branch notes in `mb/completed/`
- `mb/log.md` or `mb/progress.md` only when status/history is needed

## Precedence

Treat these files as repository workflow guidance. If they conflict with
system/developer instructions from the Codex harness, follow the higher-priority
Codex instructions and mention the conflict briefly.

