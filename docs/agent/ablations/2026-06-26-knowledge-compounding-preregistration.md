---
type: ablation-protocol
author: hybrid
drafted: 2026-06-26
status: proposed            # pre-registered; not yet run
hypothesis: "An agent that logs what it learns each cycle and reuses it on later problems (Warm) closes more of the start→optimum gap, and does so increasingly over a problem sequence, than an identical agent whose memory is wiped between problems (Cold). Both start from a blank slate and from scratch on every answer."
harness: src/einstein/meta_loop/ablation.py   # reuse run-matrix + metrics; extend for cross-problem memory
relates:
  - 2026-06-12-three-arm-knowledge-ablation.md   # different question (curated KB vs web); this one is blank-slate accumulation
  - 2026-05-03-surgical-removal-protocol.md       # page-level attribution; complementary, run after
  - 2026-05-03-cold-vs-warm-p9-uncertainty.md     # audit-style precursors (not controlled paired runs)
paper_hook: "main.tex §6 (Evaluation), §10 (Limitations) — currently say the cold-vs-warm memory ablation is future work and evidence is observational. This is that experiment."
---

# Pre-registration — Does the accumulation loop compound? (blank-slate Cold vs Warm)

> **Pre-registration discipline.** Everything in §§3–9 is fixed *before* the first
> run. Sections marked **FROZEN** may not change after data collection begins; if
> they must, that voids the pre-registration and starts a new one (new file, new
> date). Results go in a *separate* results file, not by editing this one.

---

## 1. The claim under test

The paper's central, currently-**unproven** claim (`main.tex` §6, §10; abstract):

> *Accumulated, reused, human-readable knowledge causally makes the agent better
> across cycles — it compounds — beyond the raw model.*

Today the support is **observational**: cycle logs show findings get reused
(hit-rate 26%, cite-reuse 84%) but no controlled run shows reuse *causes* better
results. A reviewer's fair objection: the agent might do just as well without the
loop. This experiment is the causal test.

**What this experiment does NOT test** (deliberately out of scope — keep it simple):
- whether the *pre-built* 23-problem wiki helps (that's contaminated by answer
  storage; see §7);
- whether curated KB beats web search (that's `2026-06-12-three-arm`, phase 2);
- which *individual page* carries the uplift (that's `surgical-removal`, later).

This tests one thing: **the read→solve→write-back→reuse loop itself**, from a
blank slate, isolated from every other advantage.

---

## 2. Design in one paragraph

Two identical agents solve the **same ordered sequence of fresh, structurally
related optimization problems**, each from scratch (no leaderboard/warm-start
seed). The **only** difference: the **Warm** agent writes a short lesson after
each problem and may read its own accumulated lessons before later problems; the
**Cold** agent's memory is wiped between problems, so every problem is solved
independently. Both start with an **empty** knowledge base — the only knowledge
that ever exists is what the Warm agent generates *during the run*. The claim
predicts (H1) Warm closes more of the start→optimum gap on average, and (H2) the
Warm-minus-Cold advantage **grows with position in the sequence** as lessons
accumulate. Outcome is the **local triple-verified score**; nothing is submitted
to the arena.

This is exactly the original framing: *agent1 = no accumulation; agent2 = log
lessons and start from them.* The blank-slate start is what makes it clean — with
no pre-built wiki on disk, there is nothing to firewall and no stored answer to
leak.

---

## 3. Independent variable — the two arms  **[FROZEN]**

Everything is identical between arms except the memory loop.

| | **Cold (control)** | **Warm (treatment)** |
|---|---|---|
| Start-of-run KB | empty | empty |
| Read lessons before a problem | ✗ | ✓ (its own, from earlier problems in this run) |
| Write a lesson after a problem | ✗ (discarded) | ✓ (persisted to the run KB) |
| Memory between problems | **wiped** (fresh session, empty KB each time) | **carried** (KB grows across the sequence) |
| Base model, temperature, tools | identical | identical |
| Generic solver code (`src/`) | identical | identical |
| Compute / cycle budget per problem | identical | identical |
| Answer access (leaderboard, optimum) | none | none |
| Solution warm-start seed | none (cold init) | none (cold init) |

**Operational definition of "a lesson":** after each problem, the Warm agent
writes ≤1 page (a `finding`/`dead-end` in the run KB) capturing: what operator/
parameterization worked, what dead-ends to skip, and any transferable structural
observation. This is the unit that may compound. The Cold agent is prompted to do
the same reflection (to equalize "thinking time") but the output is **discarded
and never re-read** — so reflection effort is held constant; only *persistence +
reuse* differs.

---

## 4. What is shared vs withheld  **[FROZEN]**

The cut between *infrastructure* (shared) and *treatment* (withheld from Cold).

| Shared by BOTH arms (infrastructure) | Withheld from Cold (the treatment channel) |
|---|---|
| `src/einstein/optimizer.py` + **generic** solvers (L-BFGS, Nelder–Mead, CMA-ES, basin-hopping) | the read→write-back loop (the only real difference) |
| `src/einstein/{problem}/` evaluator + **triple-verify** harness | the run KB (Warm's accumulated lessons) |
| `scripts/` runners, compute routing | council/personas, if used (see §11 — off by default for v1) |
| the problem statement + constraints | — |

**Generic-solvers-only rule [FROZEN]:** neither arm gets a *problem-specific
plugin* that bakes in past wisdom (no k-climbing plugin, no Dinkelbach wiring,
etc.). Such a plugin would be accumulated knowledge smuggled through code and
shared equally — which mutes the signal. The agent must *choose and configure*
generic solvers; remembering how is exactly what Warm gets to do. (Fresh problems
with no existing plugin satisfy this automatically — see §6.)

---

## 5. The no-warm-start rule  **[FROZEN]**

Two senses of "warm" — keep them separate:
- **Warm-*start* (solution-level)** — seeding the optimizer from a known/leaderboard
  configuration. **OFF in both arms.** Every problem begins from random/scratch
  init. Otherwise we measure "started near the optimum," not memory.
- **Warm-*memory* (knowledge-level)** — reading accumulated lessons. This **is**
  the treatment (Warm only).

So the only thing that ever differs is access to accumulated *technique/reasoning*,
never access to the *answer*. Both arms climb from nothing. Absolute scores will
be lower than our SOTA runs — fine; we measure the *gap and its trend between
arms*, not records.

---

## 6. Problem set  **[FROZEN before first run]**

Requirements (all must hold):

1. **Held-out:** not present in the existing wiki/source as a solved instance.
   (Blank-slate start enforces this anyway, but pick problems the *model* is also
   least likely to have memorized — prefer less-famous instances.)
2. **Known or computable optimum / strong reference**, so the dependent variable
   is *gap-to-optimum* (clean), not raw score. Sources: Packomania (circle/sphere
   packing at arbitrary n), Hardin–Sloane / Sloane's tables (Tammes), Wales–Doye
   (Thomson energies), published Heilbronn values. Record the reference + URL per
   problem in the run config.
3. **Structurally related, so a lesson can transfer.** A sequence of *new-n
   instances within a family* (e.g., Tammes at several held-out n, or circle
   packing at several held-out n) is the primary set — same machinery applies, so
   what Warm learns on problem k can help problem k+1. (Unrelated problems → no
   transfer → null by construction; that is a *design failure*, not a result.)
4. **Genuine headroom from a cold init** — a generic solver from scratch should
   *not* trivially hit the optimum on attempt 1, or there is no room to show
   learning.

**Size [FROZEN]:** sequence length **L = 6** problems; **S = 3** seeds per arm.
→ 6 × 2 arms × 3 seeds = **36 full agent runs**. (Justification: L≥5 needed to see
a trend; S=3 is the floor for mean±stdev given stochastic solvers — see §8.)

**Ordering [FROZEN]:** one fixed canonical order (e.g., increasing n), used
identically for every seed and both arms. The Cold arm sees the same order but
cannot benefit from it. (A later robustness check may shuffle order; not in v1.)

**Optional generalization probe (record but secondary):** make problem 6 a
*different family* that shares one transferable idea with 1–5, to test whether
Warm's advantage is mere within-family tuning or genuine technique transfer.

---

## 7. Isolation — clean-room, not permission-gating  **[FROZEN]**

Air-gap by construction, not by policing. Build two checkouts:

```
einstein-warm/    # full harness; run KB starts EMPTY (see below)
einstein-cold/    # identical, but no persistence between problems
```

Both are built from the **same commit** by `scripts/build_ablation_repos.sh`
(§10). The knowledge layer is *removed from disk* so there is nothing to monitor
and nothing to leak:

- `rm -rf knowledge/wiki/ knowledge/source/ docs/agent/`  (the pre-built knowledge + answers)
- strip `.claude/rules/` to the **generic** subset only — remove
  `wiki-first-lookup.md`, `council-dispatch.md`, `self-improvement-loop.md`,
  `wall-hit-escalation.md`, `cycle-discipline.md`, `wiki-attribution.md`,
  `ask-the-question-first.md` (these *are* the knowledge harness); keep
  `triple-verify.md`, `compute-router.md`, `axioms.md` (A1/A4 only), `agent-stance.md`.
- delete `mb/` and any `results/`, `solution-best*`, `*.json` solution dumps.
- keep `src/`, `scripts/`, `tests/`, and the per-problem statement files.

The **Warm run KB** is a fresh empty directory (e.g., `run-kb/`) created at run
start and written into only by the Warm agent during the run. The Cold agent has
no such directory (or one that is emptied between problems by the driver).

Why clean-room beats a permission system: a gated agent inside the live repo can
`grep` the wiki, and you must trust + audit that it didn't. A checkout that
*physically lacks* the data cannot leak it. Simpler **and** more rigorous.

---

## 8. Dependent variables & sample size  **[FROZEN]**

All measured **locally**, triple-verified (A1). **No arena submission** — the
board is a moving, confounded ruler; the local verified score is the clean DV.

**Primary metric (pre-registered):**
- **gap-closed fraction** per problem =
  `(score_final − score_coldinit) / (score_optimum − score_coldinit)`,
  clamped to [0, 1], where `score_coldinit` is the median first-evaluation score
  across seeds for that problem (a fixed per-problem baseline). 1.0 = reached the
  reference optimum; 0 = no progress.

**Secondary metrics (reuse `src/einstein/meta_loop/ablation.py` where the API
matches — verify signatures in a fresh session before relying on them):**
- `climb_rate` — verified improvement per cycle;
- `cycles_to_fraction_of_floor` — cycles to close X% of the gap (None if never;
  never silently 0);
- `dead_ends_avoided` — known dead-ends *not* re-run (Warm should avoid lessons it
  already wrote; Cold cannot). This is the metric most directly about reuse.
- wall-clock / compute per problem (efficiency, even when final score ties).

**Seeds & stats [FROZEN]:** S = 3 seeds per (problem, arm). Report mean ± stdev
(or median ± IQR) per cell; never a single-run point estimate. The solvers and
model sampling are stochastic — one run proves nothing.

---

## 9. Hypotheses & decision rules  **[FROZEN]**

State both the level effect and the compounding (slope) effect, each falsifiable.

- **H1 (level — knowledge helps):** mean gap-closed(Warm) > mean gap-closed(Cold)
  across the 6 problems. *Decision:* supported if the Warm mean exceeds Cold by
  more than the pooled per-cell stdev (a clear separation, not overlap). Null =
  no controlled evidence the loop helps at all.
- **H2 (slope — it compounds):** the per-problem advantage
  Δ_k = gap-closed(Warm, problem k) − gap-closed(Cold, problem k) **increases with
  k** (sequence position). *Decision:* supported if Δ_k trends upward (positive
  slope of Δ_k vs k; later-third mean Δ > first-third mean Δ by more than pooled
  stdev). H2 is the *headline* — it is what "compounds" means.
- **H1 holds but H2 fails:** knowledge helps but does not accumulate within the
  run — a level shift, not compounding. Honest, publishable, weaker claim.
- **Both fail (Warm ≈ Cold):** the loop earns nothing in this regime. **Report it.**
  A clean negative result is a real contribution and directly informs the paper's
  limitation section. Pre-commit to publishing it (no quiet re-runs to "fix" it).

**Sanity / manipulation checks (must pass or the run is void):**
- Warm's run KB actually grows (≥1 lesson per problem) and is read on later
  problems (transcript shows reads). If Warm never reuses, the manipulation
  failed.
- Cold's between-problem KB is provably empty at each problem start (driver
  asserts).
- Firewall/transcript audit (§10) shows neither arm read an answer source.

---

## 10. Artifacts to build  ← **dev checklist for a fresh session**

Build these, in order. Each is small; reuse existing code where noted.

1. **`scripts/build_ablation_repos.sh`** — from a given commit, produce
   `einstein-warm/` and `einstein-cold/` per §7 (clone/worktree → `rm` the
   knowledge layer → strip `.claude/rules/` → create empty `run-kb/`). Idempotent;
   prints a manifest of what was removed so the air-gap is auditable.
2. **`config/ablation_problems.yaml`** — the 6 problems: id, statement file,
   constraints, reference optimum + source URL, canonical order index, cold-init
   recipe. **Freeze this before run 1.**
3. **Per-arm session launcher** — wraps a *fresh* Claude Code session per problem
   with: the arm's tool set (Cold: web/search/MCP retrieval **disabled**; both:
   `src/` + triple-verify enabled), the problem statement, and (Warm only) read
   access to `run-kb/`. Autonomous self-execution from inside one session would
   defeat the control — spawn a clean session per (problem, arm, seed), same as
   the surgical-removal + 3-arm protocols require.
4. **Run driver** — builds the (problem × arm × seed) matrix (reuse
   `ablation.build_run_matrix` / `RunSpec` if present), runs each cell, and for
   Warm threads `run-kb/` across problems in order; for Cold wipes it each problem.
   Asserts the §9 sanity checks per cell.
5. **Logging** — per run, append one JSON record (schema §below). Per cycle within
   a run, append the trajectory point. Store under
   `results/ablation-2026-06-26/` (gitignored).
6. **`scripts/analyze_ablation.py`** — compute primary + secondary metrics,
   aggregate over seeds, emit: the gap-closed table (problem × arm), the Δ_k
   trend, and the H1/H2 decisions per §9. Reuse `summarize_arm` / `rank_arms` if
   the API matches.
7. **Transcript auditor** — grep each Cold session's tool calls to confirm no
   forbidden retrieval (no web, no arena host, no cross-arm KB path). Reuse
   `ablation.ANSWER_KEY_PROBES` / `firewall_verified` as the block-list. Emit a
   pass/fail receipt per run.
8. **`tests/`** — assert: build script removes exactly the §7 paths; Cold KB
   empty at each problem start; Warm KB monotonically grows; metric math on a
   tiny synthetic fixture; auditor catches a planted violation.

**Run record schema (one JSON object per (problem, arm, seed)):**
```json
{
  "problem_id": "...", "arm": "cold|warm", "seed": 0,
  "sequence_index": 0,
  "score_coldinit": 0.0, "score_final": 0.0, "score_optimum_ref": 0.0,
  "gap_closed": 0.0,
  "cycles": 0, "wall_clock_s": 0.0,
  "trajectory": [{"cycle": 0, "best_verified": 0.0}],
  "lessons_written": 0, "lessons_read": 0, "dead_ends_avoided": 0,
  "kb_state_hash_before": "...", "kb_state_hash_after": "...",
  "audit": {"firewall_pass": true, "forbidden_hits": []},
  "harness_commit": "...", "model": "...", "temperature": 0.0
}
```

---

## 11. Knobs held at default for v1 (record, don't vary)  **[FROZEN]**

Keep v1 minimal; each of these is a *future* axis, not part of this experiment:
- **Council/personas: OFF for both arms in v1.** Personas are part of the
  knowledge harness; including them adds a second varying thing. Test their
  contribution later (the README "persona ablation"), after H1/H2 are settled.
- **Web search: OFF for both arms in v1** (so the comparison is purely
  loop-on vs loop-off; web is the *3-arm* phase-2 question).
- **Cross-family transfer:** only the single optional probe at problem 6 (§6).

---

## 12. Threats to validity & mitigations

| Threat | Mitigation |
|---|---|
| Model memorized famous optima (helps both arms) | prefer less-famous held-out instances; it biases *both* equally, so it inflates the floor, not the Warm−Cold gap; note it |
| Warm wins only via more context tokens | cap retrieved-lesson tokens to a fixed budget; both arms get equal max context |
| "Reflection time" confound | Cold also reflects each problem; output discarded — effort equalized, only persistence/reuse differs |
| Problem-specific plugin leaks wisdom | generic-solvers-only rule (§4); fresh problems have no plugin |
| Stochastic noise mistaken for effect | S=3 seeds, mean±stdev, separation-beyond-stdev decision rule |
| Order effects | one frozen canonical order in v1; shuffle-order robustness check deferred |
| Null gets quietly re-run until positive | pre-commit (§9) to publishing the negative; runs are logged 1:1, no cherry-pick (cycle-discipline rule) |
| Lessons transfer trivially (same answer reused) | no-warm-start (§5) + held-out instances: a *lesson* is technique, not a stored configuration |

---

## 13. Relationship to prior ablations

- **`2026-06-12-three-arm-knowledge-ablation`** — asks *curated KB vs web vs
  model-only* on existing problems behind a firewall. Different question (answer
  access controlled, not removed). **Phase 2**: add a web arm here only after
  H1/H2 settle.
- **`2026-05-03-surgical-removal-protocol`** — *which page* carries uplift.
  Complementary, finer-grained; run after this establishes the loop helps at all.
- **`2026-05-0x cold-vs-warm-pNN`** — audit-style (analyze what the wiki had), not
  controlled paired runs. This supersedes them as the *causal* version.

---

## 14. Implications (what the result changes)

- **H1 + H2 supported** → replace the paper's "observational" hedge (§6, §10) with
  a controlled causal result; the compounding claim becomes earned, not asserted.
- **H1 only** → soften the claim to "knowledge helps but in-run compounding
  unproven"; keep the loop, drop "compounds" language.
- **Null** → the strongest honesty signal the project can produce; rewrite the
  thesis around verification (which is solid) and report that the memory loop did
  not pay off in this regime. Pre-committed.

---

*Pre-registered 2026-06-26. Results → a separate `results-…md` file; do not edit
this document after the first run (per the pre-registration discipline at top).*
