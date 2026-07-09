---
type: finding
author: agent
drafted: 2026-05-25
question_origin: js/feat/research-synthesis G7
status: answered
related_findings:
  - research-synthesis-design
  - qmd-metal-embed-fix
cites:
  - ../../../scripts/research_synthesis_shadow.py
  - ../../../src/einstein/research_synthesis/shadow.py
  - ../../../docs/ops/com.einstein.research-synthesis-shadow.plist
  - ../../../../mb/logs/research-synthesis-shadow.md
  - ../../../../mb/logs/shadow-runs/2026-05-25-rs-shadow-cited-sources.jsonl
---

# Research-synthesis first unattended run

**Three runs across three days; six integration bugs found + fixed. Take 9
(2026-05-27) is the first where the synthesis pipeline genuinely fired with
clean content. Verdict: `a_wins=TRUE` (Δfindings=+0.167, citations A=3 vs
B=1) — but DIRECTIONAL, NOT statistically proven: n=3 problems, synthesis
fired exactly once (the rest timed out or were skipped), zero score movement.
Synthesis-when-it-fires makes the agent cite + find more; the efficacy claim
needs a larger sample and a faster pipeline.**

## TL;DR by run

| Run | Date | Wiring | a_wins | What was actually measured |
|---|---|---|---|---|
| G7 first-run | 2026-05-25 | rule_edit only; citation gate read-after-cleanup bug | no (gate broke) | Agent ignored rule; both arms cited from prompt-embedded References |
| G10 take 2 | 2026-05-26 | G8 hook + G9 gate landed, but G8 timed out silently (120s inner cap) | yes | arm A cited more — but from reading the modified RULE, not synthesis output (zero synthesis files generated) |
| G10 take 9 | 2026-05-27 | all 6 bugs fixed + 2 quality improvements (retrieval floor, skip-terminal) | **yes** | **Synthesis genuinely fired** (7.5KB clean file, all hits ≥41%); arm A Δfindings=+0.167, citations 3 vs 1 |

The arc of the verdict over the three runs:
- **G7**: "rule_edit is inert" — wrong, but synthesis wasn't firing
- **take 2**: "a_wins but for the wrong reason" — rule-text influenced the agent; synthesis still didn't fire
- **take 9**: "a_wins for the right reason, weakly" — synthesis fired with clean content; arm A directionally beat control

## Take 9 details (2026-05-27) — the validated run

- **Commit**: `cbc2b0a` (retrieval floor + skip-terminal on top of all G8/G9 fixes)
- **n_cycles**: 3 per arm (deliberately small — validation, not statistics)
- **Verdict**: `a_wins=TRUE`, Δfindings/cycle=+0.167, score_changed_delta=0
- **Citation gate**: A=3, B=1 (per-arm, from sidecar)
- **Debug log**: INVOKE 4, SUCCESS 1, SKIP 2 (conquered), timeout 3
- **Synthesis content**: P1 file 7.5KB, all retrieved hits ≥41% (retrieval floor
  working — vs take 8 which had 30-33% text-to-SQL/TPU-hardware noise)

### What take 9 proves
- The full loop runs end-to-end: orchestrator → synthesis subprocess → qmd
  gather (floored) → claude → file written → file read → prompt injection →
  inner agent cites. Every link passes real data.
- The two improvements work: skip gate (`SKIP P2 conquered`), retrieval floor
  (min hit 41%).
- arm A (synthesis-on) shows a directional edge over arm B (control).

### What take 9 does NOT prove (honesty layer)
- **Efficacy**: n=3, synthesis fired ONCE (SUCCESS=1; 3 timeouts, 2 skips).
  Δfindings=+0.167 = arm A produced 1 finding vs B's 0 — one finding flips it.
  Noise-level, not significance.
- **Problem-solving**: score_changed=0 both arms — these are frozen/conquered
  problems with no headroom. The win is on findings+citations, not scores.
- **The pipeline is slow**: synthesis exceeds the 600s subprocess cap roughly
  half the time (P1 once, P3 twice in take 9). It self-heals (cycle runs
  without the section; no data lost) but wastes ~10 min per timeout. The next
  optimization is parallelizing the qmd queries in `gather()` and/or caching
  synthesis per-problem so it isn't re-run on every visit.

### Honest bottom line
The branch's central mechanism is **working and clean**, and the directional
signal is positive. But "literature-driven planning improves outcomes" is
**not yet demonstrated** — that needs (a) a faster pipeline so synthesis
fires on most cycles, (b) a larger sample, and ideally (c) problems with
actual score headroom (the frozen subset can't show score movement).

## G10 take-2 details (2026-05-26, historical — synthesis did NOT fire)

The most consequential update over the G7 verdict: **rule edits DO influence
agent behavior** at the prompt-reading layer. The G7 framing ("rule_edit is
inert") was too strong. The accurate framing: a markdown rule can shift
agent attention (the agent in arm A populated `cited_sources` more
diligently), but a rule that instructs the agent to RUN a subprocess
doesn't reliably do that. The right way to make a subprocess fire is to
have the orchestrator inspect the rule and call the subprocess itself
— that's what G8 wires up, but its first execution hit a hidden timeout.

## G10 second-run details

- **Started**: 2026-05-26 04:58 UTC, on commit `ae99b5f` (G9 citation-gate fix on top of G8 orchestrator hook)
- **Finished**: 2026-05-26 ~12:50 UTC (~7.5h wall-clock; both arms hit the 14400s subprocess cap, returned partial rows per the G9 patch)
- **Cycles**: 20 per arm (40 total)
- **Per-arm citation rate**: A = 6/20 = 30%, B = 4/20 = 20%
- **Δfindings/cycle**: +0.056 (A produced 1 finding, B produced 0 over 20 cycles each)
- **`a_wins`**: TRUE — but see "what actually happened" below
- **Distinct sources cited**: A=8, B=5. The 3 sources arm A cited that arm B didn't:
  `2015-tao-sieve-theory-notes.md`, `2025-jaech-autoconvolution.md`,
  `2025-novikov-alphaevolve.md`
- **Critical finding**: zero `literature-synthesis-*.md` files were generated
  anywhere in `mb/problems/` during either arm's run

## What actually happened in G10

The orchestrator IS wired correctly (G8 commit `74eeb8d`) and DOES inspect
the rule file and DOES call `scripts/research_synthesis.py` per cycle when
the marker is present. Manual diagnostic post-run confirmed
`scripts/research_synthesis.py --dry-run --problem-id 14` takes well over
120 seconds end-to-end (3–5 qmd queries × 2 collections at 10-30s each,
plus the claude `-p` synthesizer call). The orchestrator's 120s timeout
killed every synthesis subprocess, so `_run_pre_cycle_synthesis` returned
None on every call (graceful no-op per design), and the prompt never got
the `## Pre-cycle synthesis` section.

Bumped `PRE_CYCLE_SYNTHESIS_TIMEOUT_SECONDS` from 120s to 600s after the
fact. Re-running would actually exercise the synthesis-then-prompt path —
deferred to a follow-on; not within this branch's remaining scope.

## Why A still beat B without G8 firing

Even though synthesis didn't actually run, arm A's modified
`cycle-discipline.md` contains text mentioning:

- `cited_sources` field on the cycle-log row
- the `mb/logs/cited-sources.jsonl` sidecar
- the promotion-candidate detector
- pre-cycle synthesis as a step

The inner agent reads the full rules tree when claude-code initializes its
context. Even though the agent didn't run the script, **seeing the rule
made it cite more aggressively** — particularly noticeable on the
autocorrelation family (P3, P4) where arm A cited the
`jaech-autoconvolution` paper and arm B didn't.

This is a *new* finding that revises G7's verdict:

- **G7 said**: "rule_edit is inert; it doesn't change inner-agent behavior"
- **G10 shows**: rule_edit DOES nudge behavior at the prompt-reading layer,
  just not in the way G7's experiment was set up to detect

The accurate two-part claim:

1. Rule edits CAN shift agent attention and behavior on the in-prompt
   information surface (citations, output schema field population).
2. Rule edits CANNOT reliably make the agent invoke an external script —
   for that you need the orchestrator to inspect the rule and call the
   script itself (which is what G8 wires up, with a too-tight timeout that
   needs the fix above).

## G9 verification (the citation gate fix actually worked)

The G9 fix landed in `ae99b5f`: per-cycle citation records now carry
`arm: "A"` or `arm: "B"` via `EINSTEIN_SHADOW_ARM` env var, and the
shadow CLI reads from the surviving sidecar JSONL (`mb/logs/cited-sources.jsonl`)
rather than the deleted arm cycle-logs. Result: cited_A=6, cited_B=4
showed up correctly in the gate decision, vs G7 where both were always 0.

## Run summary (G7 first-run, historical)

- **Started**: 2026-05-25 17:29 UTC, on commit `89ec2a7` of `js/feat/research-synthesis`
- **Finished**: 2026-05-25 23:22 UTC (6h 49m)
- **Proposal id**: `rs-shadow-enable-synthesis`
- **n_cycles**: 10 (= 10 problem visits per arm, ~2.2 cycles/problem)
- **Total cycles**: 33 (21 arm A + 12 arm B)
- **Arm A** (synthesis-on rule_edit applied): cycles 53–73
- **Arm B** (control): cycles 53–~64

## Verdict from `mb/logs/research-synthesis-shadow.md`

| metric | A (synthesis-on) | B (control) | Δ/cycle |
|---|---|---|---|
| score_changed cycles | 0 | 0 | 0.000 |
| findings_added (per-row column) | 0 | 1 | −0.050 |
| concepts_added | 0 | 0 | 0.000 |

`synthesis_promotion_decision`: **a_wins = false**.

Reasons:

1. `findings_delta = -0.050` (A < B per cycle) — fails gate 1
2. `cycles_with_citations_a = 0` — fails gate 3 — **but this is a bug**, see below

## What the citation sidecar actually says

The arm cycle-logs got deleted by the `cleanup=True` finally block in
`run_shadow`, but the citation sidecar at `mb/logs/cited-sources.jsonl`
survived (shared across arms by design). It's the honest record of what
each cycle declared.

- **33 cycle records this run**
- **13 cycles declared non-empty `cited_sources` (39% citation rate)**
- **17 distinct source paths cited** across both arms

Top-cited sources:

| Source | Citation count |
|---|---|
| `2025-jaech-autoconvolution.md` | 7 |
| `2022-white-erdos-overlap.md` | 3 |
| `2016-haugland-min-overlap.md` | 3 |
| `2026-rechnitzer-autoconvolution-digits.md` | 2 |
| 13 other sources | 1 each |

Rough per-arm citation rates:

- Arm A (first 16 cycles after start): **7 cited / 16 = 44%**
- Arm B (last 17 cycles): **6 cited / 17 = 35%**

**The arms cited at indistinguishable rates.** The 9-point gap is within noise
for n=16-17 cycles and unsurprising: the agent in both arms cited the same
sources (white-erdos, jaech, haugland), drawn from the problem-index
`## References` sections embedded in the prompt.

The G6 gate's "cycles_with_citations_a >= 1" requirement *did* fail in the
final decision, but only because of a code bug — the actual citation count
in arm A was 7, not 0.

## Cross-source patterns the agent surfaced

**Zero `literature-synthesis-*.md` files were generated in either arm.** The
agent never invoked `cb/scripts/research_synthesis.py` in any of the 33
cycles, even in arm A whose `.claude/rules/cycle-discipline.md` had the
explicit instruction "step 0a: run `cb/scripts/research_synthesis.py`
before step 0".

Concretely:

- arm A's `cycle-discipline.md` had the diff applied (verified mid-run);
  line 3 read `## Pre-cycle (research-synthesis branch; A/B-promoted)`
  followed by the step-0a instruction
- the inner agent's prompt embeds the full `.claude/rules/` tree as context
- the agent read the rule (we can see it cited cycle-discipline patterns in
  notes) but did not execute the synthesis script

This is the most important finding of the experiment: **a markdown
instruction in `.claude/rules/` is not sufficient to change inner-agent
tool-use behavior in a measurable way.**

## What this rules out

The `rule_edit` proposal type, when used to introduce a *new mandatory tool
invocation*, is too weak. The agent treats `.claude/rules/` as advisory
context, not as a directive. Without a structural enforcement mechanism, the
rule is decorative.

## What might still work

Three candidate fixes for a follow-on branch:

1. **Wire synthesis into `scripts/autonomous_loop.py` directly.** Before
   spawning `claude -p`, the orchestrator runs `research_synthesis.py
   --problem-id N` and embeds the output in the prompt as a `## Pre-cycle
   synthesis` section. The agent doesn't *decide* to run synthesis — it
   already gets the synthesis as input.
2. **Use a `manifest_tweak` or `code_edit` proposal type** instead of
   `rule_edit`. A meta-loop proposal whose diff modifies `autonomous_loop.py`
   to add the pre-cycle synthesis call would actually change behavior.
3. **Embed the synthesis script call in `docs/tools/cycle_runner.sh`** (the
   post-cycle housekeeping wrapper) — but reversed for pre-cycle. This
   sidesteps the proposal channel entirely.

Option 1 is the most direct and matches the original G2 design intent.

## Bug discovered in `scripts/research_synthesis_shadow.py`

`run_cli()` computes the citation-grounded gate by reading the arm
cycle-log markdown files **after** `run_shadow` has finished. But
`run_shadow(cleanup=True)` deletes both arms in its `finally:` block
before returning. The arm files are gone by the time we check.

Symptom: `cycles_with_citations_a = 0` in the final decision even though
the sidecar JSONL clearly shows arm A had ≥7 cited cycles.

Fix (deferred to a follow-on branch): either

- Pass `cleanup=False` so the arms survive long enough to be measured, then
  manually `git worktree remove` after the decision, OR
- Compute `cycles_with_citations` from the sidecar JSONL (shared, survives
  cleanup) filtered by timestamp range — more robust since it doesn't
  depend on the arm cycle-log surviving.

## Honest interpretation

The shadow experiment **worked as a regression-foresight tool** (per AHE's
89%-unforeseen-regressions framing in
[`research-synthesis-design`](research-synthesis-design.md)): we proposed
a change, ran A vs B for 33 cycles, and got back a measurable answer that
said "don't ship this." The fact that the answer was "this proposal type
can't influence the inner agent's tool use" is itself useful data.

The G6 gate caught a regression that self-attribution would have missed:
without the shadow A/B, the meta-loop's `rule_edit` channel would have
silently shipped a proposal that has no effect. The 89%-unforeseen
asymmetry would have struck again.

## Portable primitives surfaced (revised post-run)

The G7 plan called for distinguishing portable from einstein-specific bits.
After the run, the assessment:

| Primitive | Portability | Notes |
|---|---|---|
| `research_synthesis.schema.LiteratureSynthesis` | high | typed JSON schema, problem-agnostic |
| `research_synthesis.query` (qmd wrapper + gather) | high | depends on qmd CLI shape only |
| `research_synthesis.synthesizer` | high | claude_headless orchestration + prompt template |
| `promotion_candidates.py` | high | JSONL → markdown candidates; no project-specific deps |
| `research_synthesis.shadow.{cycles_with_citations, synthesis_promotion_decision}` | medium | depends on cycle-log row format with trailing cites_src column |
| `meta_loop.shadow.run_shadow` + `default_cycle_runner` | high | already portable; this branch surfaced the timeout + cleanup bugs |
| `make_synthesis_proposal` and the rule_edit diff | **low** | proven inert in this experiment; needs replacement with manifest_tweak or code_edit |

Math-specific bits (qmd collection names, `mb/problems/<id>-<slug>/` layout,
council persona triggers, arena verifier coupling) stay in this repo.

## Follow-on branches

This finding seeds three follow-on candidates, in priority order:

1. **`js/feat/synthesis-orchestrator-wire`** — implement Option 1 above:
   patch `autonomous_loop.py` to run `research_synthesis.py` pre-cycle and
   embed the output in the prompt. Re-run the shadow A/B and see if
   citation behavior changes.
2. **`js/fix/shadow-citation-gate`** — patch
   `scripts/research_synthesis_shadow.py` to read citation counts from
   the surviving sidecar JSONL instead of the deleted arm cycle-logs.
   Add the missing regression test.
3. **`js/refactor/research-synthesis-portable`** — extract the high-portability
   primitives into a sub-package (`research_synthesis_core/` +
   `research_synthesis_adapters/einstein.py`).

## See also

- [`research-synthesis-design`](research-synthesis-design.md) — G0 finding
  that named the cross-source patterns this experiment was meant to test
- [`qmd-metal-embed-fix`](qmd-metal-embed-fix.md) — G1 finding; `QMD_FORCE_CPU=1`
  was active throughout this run
- [`../questions/2026-05-25-regression-foresight-self-evolving-harness.md`](../questions/2026-05-25-regression-foresight-self-evolving-harness.md)
  — the AHE 89%-unforeseen-regressions question this experiment partially answered
- `mb/logs/research-synthesis-shadow.md` — raw shadow-log row
- `mb/logs/shadow-runs/2026-05-25-rs-shadow-cited-sources.jsonl` — per-cycle
  citation records preserved from this run
