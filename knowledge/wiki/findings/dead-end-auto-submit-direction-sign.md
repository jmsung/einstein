---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-2
status: answered
related_concepts: [auto-submit-gate-chain, triple-verify]
cites:
  - src/einstein/auto_submit.py
  - scripts/autonomous_loop.py
  - mb/logs/auto-submit.md
  - mb/logs/leaderboard-audit-2026-06.md
---

# Dead end: auto-submit gate trusted a default direction and submitted a worse P2 score as a "record"

## What we tried
The 2026-05-24 submission-policy change armed the autonomous loop to auto-submit
new arena records IFF the 6-gate chain (`auto_submit.try_submit`) passes. Gate 5
(strict improvement over arena #1) takes a `minimize: bool` flag to know which
direction "improvement" is. The flag defaults to `False` (maximise).

On 2026-06-04 the loop submitted P2 (`first-autocorrelation`) score
`1.5028628585992` as a "new arena record … beats #1=1.5028609073611 by 1.95e-06",
twice (06:00 + 07:28 UTC, HTTP 201, arena ids 2319/2320; `mb/logs/auto-submit.md`).

## Why it failed
P2 is a **minimise** problem (`src/einstein/first_autocorrelation/__init__.py`:
"Minimize C(f) = max(f★f)/(∫f)²"). The submitted score `1.5028628585992` is
**higher** than arena #1 `1.5028609073611` — i.e. *worse* by 1.95e-6, and worse
than our own audited best `1.5028610916080` (`mb/logs/leaderboard-audit-2026-06.md`).

Root cause: `_call_auto_submit` in `scripts/autonomous_loop.py` called
`try_submit(...)` **without passing `minimize=`**, so gate 5 used the maximise
default for *every* problem. For a minimise problem the gate computed
`delta = score − arena_top1 = +1.95e-6` and read that positive delta as
"improvement", firing the submission. The gate code was correct; it was never
told the direction. The `Problem` dataclass carried no direction field and no
canonical per-problem direction map existed anywhere in the codebase.

Triple-verify (gate 2) did **not** catch this: triple-verify confirms the score
is a *correct evaluation of the payload* (3-way agreement on the number), not
that the number *beats* arena #1 in the right direction. Direction is gate 5's
job, and gate 5 was blind.

The submitted score was also just the wrong seed: the manifest note already flags
that the best in-repo P2 seed is the n=30000 basin (`1.50286286`), while the
arena-#1-beating n=90000 solution (`1.502861628`) "was never backed up cleanly".
So the loop submitted a known-suboptimal seed *in the wrong direction*.

No leaderboard damage: a worse score cannot displace #1. The harm was (1) two
false "record" rows in the audit log, (2) polluted daily-cap/throttle counters,
(3) a latent bug that would fire on *every* minimise problem — and four of the
five Phase-7 headroom targets (P2, P4, P10, P12) are minimise.

## What this rules out
- **Trusting the auto-submit chain without a per-problem direction source.** A
  default direction is never safe: half the live problems minimise, half
  maximise. The gate's `minimize` argument is meaningless unless the caller
  supplies it from an authoritative table.
- **Treating triple-verify as sufficient for submission safety.** It validates
  the *value*, not the *comparison*. "3-way agreement" + "passes gate chain" can
  still be a wrong-direction submission. Direction is an independent failure mode.

## What fixed it
- Added `PROBLEM_MINIMIZE: dict[int, bool]` to `src/einstein/auto_submit.py` —
  the canonical per-problem direction, each entry sourced from that problem's
  evaluator docstring (arena-verifier convention).
- `_call_auto_submit` now looks the direction up and passes `minimize=` into the
  gate. **Fail closed:** a problem that passes triple-verify but is absent from
  the map is *skipped* (`auto-submit-skipped@direction-unknown`), never guessed.
- Regression tests: P2→`minimize=True`, P14→`minimize=False`, unknown→fail-closed
  (`tests/scripts/test_autonomous_loop.py`); map-content guard
  (`tests/test_auto_submit.py::test_problem_minimize_map_directions`).

## What might still work / open follow-ups
- Defense-in-depth: make the gate itself reject an unset/`None` direction so a
  future caller can't re-introduce the default-maximise blind spot. Deferred —
  current tests rely on the `minimize=False` default; would need a wider change.
- Seed-backfill gap for P2 (n=90000 `1.502861628`) remains open — the loop still
  can't reach our own best, let alone beat arena #1.
- The two false "record" rows are annotated via a corrigendum in
  `mb/logs/auto-submit.md` (append-only; past rows are never edited).
