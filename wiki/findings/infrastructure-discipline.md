---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
---

# Infrastructure & Publication Discipline

## #30: Reusable GPU modules pay compound interest {#lesson-30}

Problem 6: building `src/einstein/gpu_tempering/` (4 acceleration levels, auto-benchmark, 16 tests) took extra time but produces a provider-agnostic SA parallel tempering module reusable across all future sphere-packing and continuous optimization problems. Invest in infrastructure when 2+ future problems will benefit. The upfront cost is amortized across every problem that uses it, and the per-problem integration cost drops to near zero once the module is tested and documented.

## #53: Private-path resolver derivation — leaky strings stay in one module {#lesson-53}

When a new public module needs to read a file under the private MB tree (e.g. `src/einstein/council/` loading the canonical persona playbook), DO NOT duplicate the path-resolution logic. Derive from an already-leaked resolver instead: `from einstein.knowledge import KNOWLEDGE_PATH; path = KNOWLEDGE_PATH.parent / "docs" / ...`.

This keeps every `mb` / `memory-bank` / `workbench` string confined to the one module that already leaks them (`knowledge.py`), so a repo-wide grep for private-path strings has a single, known-clean hit. The council-dispatch branch (2026-04-08) used this pattern to ship `council/personas.py` with zero private strings in code or docstrings even though the module loads a file from the private tree at runtime.

**General rule**: second-and-later consumers of any private path or credential must import the existing resolver, never re-implement the lookup. Public modules must pass `grep -riE 'mb|memory[-_]bank|workbench'` as a hygiene check on any new file before commit.

## #78: Polisher scratch output must never write to knowledge base {#lesson-78}

Problem 6 Kissing Number (2026-04-09): 15 polish loop scripts writing every improvement cycle directly into the workbench MB `solutions/` directory produced 17k+ orphaned snapshots for a single problem. The MB is a *publication layer*, not a scratch pad.

**Root-cause fix**: redirect all polisher output to the local gitignored `results/<problem>/polish-trail/` directory, and require explicit promotion via `scripts/promote_to_mb.py` to move any file into MB. This separation means the MB contains only deliberately curated milestones.

**Rule**: any long-running loop that produces intermediate files must write to a local gitignored directory; the knowledge base is downstream of curation, never upstream of experimentation.

## #79: Atomic rolling single-file output {#lesson-79}

Even with self-filtering (write only on strict improvement), a long polish session can produce many intermediate files. The fix: one rolling file per session (`session-{YYYYMMDD-HHMMSS}-{script}-best.json`) updated via tmp+rename atomicity. Storage cost drops from O(cycles x sessions) to O(sessions).

The tmp+rename pattern (write to `.tmp-{id}.json`, then `os.replace()` to final path) guarantees no partial files on POSIX — kill -9 mid-write leaves zero files, not a corrupt one. This is the standard POSIX atomic-write pattern and should be the default for any long-running script that updates a results file.

## #80: Deliberate promotion gate {#lesson-80}

`scripts/promote_to_mb.py` requires `--tag` and `--score` arguments, computes a keeper-pattern filename, copies (not moves) the file, and appends an audit-trail line to `experiment-log.md`. Every file in MB has a human who said "this matters" and a log entry explaining why.

This replaces the prior ad-hoc `cp` pattern and prevents the class of bug where a polisher accumulates thousands of files in a publication-layer directory. The copy-not-move semantics mean the source file remains in the scratch directory for reference, and the promotion is idempotent (re-running with the same arguments produces the same result).

## #41: Shared submission tooling pays compound interest {#lesson-41}

Building one `check_submission.py` module (verify_api, wait_for_leaderboard, launch_monitor) and reusing it across all problem submit scripts eliminates per-problem bugs. Every new problem now gets pre-flight URL/auth checks, triple-verification, and blocking leaderboard polling for free. Invest in shared submission infrastructure once — it amortizes across every future submission.
