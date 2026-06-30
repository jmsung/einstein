---
type: ablation-protocol
author: hybrid
drafted: 2026-06-27
status: frozen              # smoke validated 2026-06-29; directional design frozen below (§9)
builds_on: 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # reuses the v2 harness + air-gap + DV
hypothesis: "Injecting persona-council QUESTIONS before solving improves the agent's gap_closed on a headroom family, at equal solve-budget — i.e. the council's question-framing helps the solve even before counting its token cost."
family: heilbronn_triangle
model: claude-haiku-4-5
harness: scripts/run_council_ablation.py (reuses ablation_runner solve + air-gap + triple-verify)
relates:
  - mechanism-claims-test-matrix.md     # claim #1
  - results-compounding-evidence.md
paper_hook: "main.tex §6 — the council mechanism, controlled."
---

# Pre-registration — Does the persona council help? (claim #1)

## 1. Claim under test
> Persona-council questions, generated before solving and injected into the solve prompt,
> improve `gap_closed` vs solving directly — on a family where the agent genuinely flails.

## 2. Independent variable — the two arms  **[FROZEN]**
Identical except the council. One variable: the injected questions block.

| | **Council-off (control)** | **Council-on (treatment)** |
|---|---|---|
| Pre-solve step | none | dispatch ~4 core personas; each writes 2–3 questions (separate LLM call); concatenate |
| Solve prompt | normal | normal **+ "## Questions from a math council"** block |
| Solve budget (timeout / cap) | B | **B (same)** |
| Cold-init, family, tools, air-gap | identical | identical |
| Wiki / qmd | **off (air-gapped, stripped)** | **off** — council runs WIKI-LESS |

## 3. Frozen design decisions (2026-06-27)
- **Budget match = equal SOLVE-budget** ("does it help at all?"). The council's N persona calls are
  overhead NOT charged against the solve. This is the *favorable-to-council* framing — so a NULL
  here is strong ("doesn't help even for free"); a positive result still owes a follow-up
  compute-matched test (best-of-(N+1) for council-off) before claiming it's *worth its cost*.
- **Wiki-less council** — isolates the *persona-framing* contribution from the KB claim (#4). The
  production council also pulls wiki literature; that confound is deliberately removed here.
- **Small council (~4 core personas)** — cost control; record the exact set. Bench specialists off.

## 4. DV, hypothesis, decision rule  **[FROZEN]**
- **Primary DV:** `gap_closed` (v2 §8), harness triple-verified, paired by cold-init.
  **Δ(P,s) = gap_closed(on) − gap_closed(off)**.
- **H (council helps):** mean Δ > 0; supported iff the 95% bootstrap CI of mean Δ excludes 0.
- **Secondary:** wall-clock / time-to-target (efficiency), question quality (qualitative).
- **Pre-committed:** report the null. No quiet re-runs.

## 5. Controls
Paired cold-init per (problem, seed); air-gap by construction (no web tools, wiki stripped);
harness-side triple-verify (agent self-report ignored); **identical solve budget both arms** so the
only difference is the questions. Manipulation check: council-on prompts must actually contain a
non-empty questions block (else the cell is void).

## 6. Staging  **[FROZEN staging]**
- **Smoke (~$1–2):** 1 council-on + 1 council-off on (n=13, seed=1). Verify personas return
  questions, injection lands, both arms score. (Wiring validation only.)
- **Exploratory (S=4–6):** 6 Heilbronn problems × 2 arms × S. Manipulation checks; per-cell stdev;
  directional Δ. GO/NO-GO: checks pass, cold non-saturated, Δ ≥ 0 directionally.
- **Freeze S** from exploratory variance (expect the same ~30-pt per-cell SD as #4 → S≈18 for power).
- **Confirmatory:** apply §4 rule once.

## 7. Cost
Council-on ≈ (N personas + 1 solve) ≈ 5 LLM calls/cell; council-off = 1. At ~$0.5/call, one
S=6 exploratory pass ≈ 6 problems × (5+1) calls × 6 seeds ≈ $100; confirmatory S=18 ≈ $300.
Sequential, resumable (reuse v2 §9). The cost asymmetry is real — hence equal-solve-budget framing
and a small council.

## 8. Threats
| Threat | Mitigation |
|---|---|
| "Helps" = more compute | equal solve-budget isolates the *questions*; compute-matched follow-up if positive |
| Wiki-less ≠ production council | acknowledged; this tests persona-framing alone (the cleaner isolatable claim) |
| Small council ≠ full council | record the set; scale up only if the small council shows signal |
| Per-cell noise dwarfs effect | power to S≈18, bootstrap CIs (per #4's measured variance) |
| Null quietly re-run | pre-committed null reporting |

## 9. FROZEN directional design (2026-06-29)

Smoke (n=13, seed=1, haiku) validated the wiring 2026-06-29: air-gap `passed=True`,
all 4 core personas (Gauss/Conway/Erdős/Cohn) returned genuine on-topic questions
(cost $0.49, 100s), pairing held (identical cold-init both arms), and both arms scored
(off gap 0.000 — output invalid, floored; on gap 0.383). Persona config:
`config/ablation_council_smoke.md` (4 core personas, faithful condensation of
`docs/wiki/personas/`).

Given the equal-solve-budget cell cost (~22 min: 100s dispatch + 2×600s solves) and the
single-credential serial constraint, the confirmatory is run at a **directional** scale,
not the §6 power target (S≈18 is ~40 h serial — deferred). Frozen choices:

- **Instances:** `heil-n13`, `heil-n14` (Heilbronn, confirmed cold headroom).
- **Seeds:** S=4 (1–4), paired cold-init per (n, seed).
- **Budget:** 600 s solve timeout, equal both arms (the §3 equal-solve-budget framing).
  Billing is the Claude-Code login → $0 token cost; the budget that binds is wall-clock.
- **Model:** haiku. **DV:** `gap_closed` paired delta, mean + 95% bootstrap CI (§4 rule).
- **Driver:** `scripts/run_council_confirmatory.py` (resumable; reuses the smoke's
  validated single-cell logic). 8 cells.
- **Reporting caveat:** 8 cells is **underpowered** — report the directional Δ + CI
  honestly as a pilot, not a powered confirmatory. A wide CI straddling 0 is a NULL-pilot,
  not evidence of no effect. Also flag the smoke's off-arm *invalidity* channel: part of
  any positive Δ may be "council helped produce a VALID result," not pure quality — record
  per-cell `off_verify`/`on_verify` so the analysis can separate the two.

*Frozen 2026-06-29 (was draft 2026-06-27). Results → `results-compounding-evidence.md`.*
