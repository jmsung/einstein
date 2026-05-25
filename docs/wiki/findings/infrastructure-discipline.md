---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
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

## #93: CI gates must land before agent-co-authored scale, not after {#lesson-93}

Branch `js/chore/ci-precommit` (2026-05-24): added GitHub Actions test workflow + pre-commit (ruff lint+format + 5 hygiene hooks) + `[tool.ruff]` config. The trigger was the audit observation that the repo had shifted to agent-co-authored ~1k LOC per branch with **no** PR-time CI, no linter config, no pre-commit — `feat/autonomous-loop` had already shipped despite this. Without structural gates, agent edits silently regress tests and accumulate lint debt that compounds across branches.

**Concrete pitfalls discovered during the rollout** (each one would have bitten the next agent branch):

1. **Pytest collection conflict from missing `__init__.py` in test subdirs.** `tests/first_autocorrelation/` and `tests/third_autocorrelation/` had duplicate test-file basenames (`test_*.py`) with the parent `tests/` package — pytest silently shrank the suite from 493→487 tests (6 hidden) and emitted a collection error. The fix is one empty `__init__.py` per subdir. **Rule**: any new `tests/<subdir>/` must include `__init__.py` from the first commit. CI now catches this because pytest exits non-zero on collection errors.
2. **Pre-existing F821 (missing-import) bugs in scripts** — `scripts/uncertainty/exact_hillclimb.py`, `scripts/uncertainty/k_climb_optimizer.py`, `scripts/kissing_number/polish_mpmath.py` referenced `TARGET` / `time` without import. These shipped under the no-linter regime and would have been caught by E/F/I on day 1. Per-file-ignored for landing the gate; tracked for follow-up fix.
3. **B (bugbear) + UP (pyupgrade) carry ~275 non-auto-fixable issues** on the existing tree — must be cleaned in a follow-up branch, not bundled with the gate-introduction. **B023 closure bugs are real, not noise**; demoting them to ignored would forfeit the find. Land E/F/I first, B+UP second.
4. **Pre-commit `--all-files` needs two converging runs** when both `end-of-file-fixer` and `ruff-format` are enabled — the first run's EOF fix touches pyproject.toml, which triggers ruff-format on the second run. Document this in onboarding to prevent "I ran pre-commit, why is it dirty?" confusion.

**General rule**: introduce CI + lint + format gates as **early as possible** when agent-co-authoring starts, with the minimum rule set (E/F/I) that catches real bugs without forcing a big-bang cleanup. The cost of landing this branch is a fraction of the cost of debugging silent regressions across the next 10 agent branches. Bundling pyright/mypy or dependabot in the same branch dilutes the signal; ship one quality dimension per chore branch (`js/chore/typecheck`, `js/chore/dependabot` separately).

## #102: `claude -p --allowedTools` is variadic — comma-join values and use `--` before the prompt {#lesson-102}

Branch `feat/autonomous-loop` Goal 7.2 (2026-05-24): the headless wrapper around `claude -p` initially built the argv as `["claude", "-p", "--allowedTools", "Read", "Grep", "Bash(qmd:*)", prompt]`. Symptom: every subprocess invocation reported "tool not allowed: <first words of prompt>" — the prompt itself was being consumed as an additional tool name. Root cause: `--allowedTools` is declared variadic in commander.js (the CLI parser used by `claude -p`), so it greedily eats every following positional until the next flag. Space-separated values + a bare positional prompt = the prompt joins the tool list.

**Fix (two parts, both required):**

1. **Comma-join values into a single argv token**: `--allowedTools Read,Grep,Bash(qmd:*),Task` (one argv, comma-delimited).
2. **Use `--` separator** before the prompt: `claude -p --allowedTools Read,Grep,... -- "<prompt>"`. The `--` ends option parsing so the prompt cannot be mis-parsed as a flag value even if commander adds new variadic flags later.

**Rule**: any CLI built on commander.js (Anthropic's `claude`, many Node CLIs) needs comma-join + `--` separator for any flag that takes lists. Test by inspecting the parsed argv inside the subprocess, not by trusting the help text. Add a regression test that asserts a benign prompt containing recognisable words (e.g. `"hello world"`) does not appear in the disallowed-tool error.

## #103: `git status --untracked-files=all` is mandatory for any newly-created-directory audit {#lesson-103}

Branch `feat/autonomous-loop` Goal 7.6 (2026-05-24): the wiki/mb write audit takes a snapshot of `git status --porcelain` before and after each `claude -p` cycle, diffs them, and notes the per-cycle file deltas into `docs/agent/cycle-log.md`. The first implementation used the bare `git status --porcelain` (which defaults to `--untracked-files=normal`). Symptom: cycles that created an entire new directory (e.g. `docs/wiki/questions/2026-05-24-p14-newton-tol/`) showed up in the delta as a single entry `?? docs/wiki/questions/2026-05-24-p14-newton-tol/` — the individual files inside were invisible to the audit, and the cycle-log notes column reported "1 new path" when the cycle had actually written 4 files.

Root cause: `--untracked-files=normal` collapses an untracked directory into one porcelain line for performance. Audits need file-level granularity → `--untracked-files=all` (expands every untracked file).

**Fix**: always use `git status --porcelain --untracked-files=all` for any delta-audit between two points in time. Tradeoff is wall-clock (slightly slower on huge untracked trees) for completeness.

**Rule**: any agent-side audit / hygiene check that needs per-file granularity on a freshly-created tree MUST pass `--untracked-files=all` (or equivalently `-uall`, but spelled out for clarity). Document this in the audit tool's docstring; otherwise the next maintainer "simplifies" it back to default and silently breaks the audit.

## #104: Agent cycles produce wisdom even when execution is blocked — structural diagnosis is the deliverable {#lesson-104}

Branch `feat/autonomous-loop` cycle 51 on P14 (2026-05-24): the inner agent could not execute `scripts/circle_packing_square/newton_max.py` because (a) the warm-start file `results-temp/p14_top.json` did not exist in the worktree, and (b) the manifest's empty `cli_args: []` left the optimizer running with `--pair-gap=-9e-10` defaults, which are strict-tol-unsafe for the P14 arena verifier. The cycle could not produce a score. **But the cycle still produced wisdom**: a finding (`dead-end-newton-max-strict-tol-lockout-p14.md`) diagnosing the structural blocker and proposing a concrete wire-fix — which became PR #101.

The pattern: when the cycle hits an execution blocker, the gap-detect step produces a finding *about the blocker*, not a finding about the math problem. The finding is just as valuable — it removes the blocker for every future cycle on the same problem, *and* often for a class of problems sharing the same manifest pattern.

**Rule**: do not measure inner-cycle success by "score improved." Measure it by "did this cycle produce a wiki page that the next cycle can stand on." Execution-blocked cycles that write structural findings count as full cycles in the cycle-log. The autonomous-loop's `outcome:` field already supports this (`outcome: new-finding-no-improvement`), but the *evaluator of the loop* (the human reading metrics) has to internalize that this outcome is not failure — it's the loop working as designed.

**Corollary**: per-problem manifest entries (`optimizer_manifest.yaml`) should be stress-tested by the autonomous loop itself, not by hand-curation. The first cycle on a newly-added problem will surface manifest holes the maintainer didn't anticipate; treat that as the manifest's QA pass.

## #105: `claude -p` subprocess from inside Claude Code is safe — no recursion fence needed {#lesson-105}

Branch `feat/autonomous-loop` Goal 7.7 (2026-05-24): the autonomous loop's inner agent is implemented as `claude -p` invoked as a subprocess from `docs/tools/cycle_runner.sh`, which itself runs inside a parent Claude Code session (during interactive development) and also under launchd (in production). The concern at design time was recursion / context-pollution / billing entanglement: would the inner `claude -p` somehow see the outer session's context, or get rate-limited under the outer session's budget, or recurse indefinitely?

**Observed behaviour**: no recursion issues. The inner `claude -p` is a fresh process with its own context window, its own auth (same API key, different session token), its own per-cycle budget (tracked in `mb/inner-agent-budget.md`). The outer session sees only the subprocess's stdout / stderr / exit code, exactly like any other shell command. Tool allow-list is enforced inside the inner process — outer Claude's tools are not inherited.

**Mechanism**: `claude -p` is implemented as a single-shot CLI that constructs its own conversation from argv + stdin and exits. It does not look at the parent process's TTY, env, or open file descriptors for state. Each invocation is independent.

**Rule**: agents that need to spawn other agents can use `claude -p` as a subprocess without special recursion-fence engineering. The only cross-process state is what you pass on argv / stdin / file. Budget tracking is the caller's responsibility (record input/output tokens after each call into a ledger file — see `inner_agent_budget.py`). This is the recommended pattern for any "agent-of-agents" workflow in this repo.
