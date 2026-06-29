---
type: ablation-protocol
author: hybrid
drafted: 2026-06-26
status: draft            # NOT yet frozen — sketch for review; freeze before run 1
builds_on: 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2 — the single-family causal test
hypothesis: "The compounding effect demonstrated on Heilbronn (v2) is a GENERAL property of the accumulation loop, not an artifact of one family: the same Warm-vs-Cold within-family design yields mean Δ > 0 AND a positive banked-count slope in ≥2 additional, mechanistically distinct problem families that independently exhibit cold headroom."
family: MULTI (Heilbronn + ≥2 more, selected by the §3 headroom screen)
model: claude-haiku-4-5
harness: src/einstein/meta_loop/compounding_ablation.py + ablation_runner.py   # unchanged — family-agnostic since a3f45dc
relates:
  - 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2: the design this replicates
paper_hook: "main.tex §6, §10 — external validity: the loop compounds across families, not just Heilbronn."
---

# Pre-registration v3 (DRAFT) — Does compounding GENERALIZE across families?

> **What this adds over v2.** v2 is the *internal-validity* test: a clean causal
> demonstration that the loop compounds **on Heilbronn**. v3 is the *external-validity*
> test: the same effect in ≥2 more families ⇒ "compounding is a property of the loop,"
> the claim a reviewer actually doubts. v3 **reuses v2's frozen design verbatim** per
> family; the only new object is the cross-family meta-analysis (§5). This is a fresh
> pre-registration — it does not touch v2.

---

## 0. REVISED FRAMING — generalize the EFFICIENCY win (post Stage C, 2026-06-27)

Stage C (S=18) found the Heilbronn *capability* effect null (Δ gap_closed CI includes 0) but a
clean **efficiency** effect (cold timeout 26.9% vs warm 4.6%; wall 370 s vs 242 s) — see evidence
ledger §2.7. So the thing worth generalizing is **efficiency, not capability**.

**v3's generalization claim pivots accordingly:**
- **Primary per-family DV:** the efficiency measures (timeout rate, mean wall-clock, and — once v4's
  timestamped trajectory lands — `time_to_target`), with gap_closed as a secondary non-inferiority
  check (warm must not score *worse*).
- **G1-eff (level generalizes):** warm is more efficient than cold (lower timeout rate / faster) in
  **every** run family.
- **G2-eff (it generalizes as a property):** the efficiency advantage holds in the cross-family
  mixed model (family random effect), not just one family.
- Family **headroom screen** (§3) still applies, but read "headroom" as *cold must sometimes fail to
  finish in budget* (so there's an efficiency gap to close), not only *cold scores mid-range*.

Keep the §4–§7 machinery; swap the estimand from gap-Δ to the efficiency DV. Freeze before run 1.

---

## 0b. TWO DESIGNS — Transfer (PRIMARY) + Replication (supporting)  (set 2026-06-28)

"Cross-problem wisdom" has two distinct meanings; v3 runs both, transfer as the headline.

### Design B — TRANSFER (primary): does wisdom cross problem TYPES?
The real README claim ("the wiki compounds across all 23 problems"). Two phases:
1. **Train:** a Warm agent solves family **A**'s sequence, accumulating lessons → a **frozen** `KB_A`.
2. **Test on a DIFFERENT family B:**
   - **Warm-transfer arm:** starts with `KB_A` (frozen — A's lessons), reads them, solves B.
   - **Cold arm:** no KB, solves B fresh.
   - ONE variable: presence of A's frozen lessons. Paired cold-init on B; equal solve budget;
     equal-max-context (cap A's lessons to the same char budget, Cold's empty); air-gap; isolated
     cwd (the now-fixed runner); harness-side triple-verify.
- **Transfer-distance gradient (the strong design):** run **near** transfer (Heilbronn→Tammes —
  both geometric spreading/packing) AND **far** transfer (Heilbronn→autocorrelation — unrelated).
  The *gradient* is the finding: generic meta-strategy (multi-phase opt, basin-hopping, derivative-
  free-first) should transfer *near*; problem-specific lessons should not transfer *far*. A clean
  monotone "near helps, far doesn't" is more informative than a single yes/no.
- **DV:** efficiency (timeout rate, wall, time-to-target) on B + gap_closed (non-inferiority).
  **H-transfer:** mean Δ(warm-transfer − cold) on B > 0; bootstrap CI excludes 0.
- **Honest prior:** likely NULL for far transfer, maybe positive for near — and that map is the result.
- **Harness work:** the current `compounding_ablation` threads a run-KB *within one arm's sequence*.
  Transfer needs: (i) build+persist `KB_A` from family A, (ii) load it as the *fixed*
  `accumulated_lessons` for family B's warm-transfer arm (a new "frozen-KB inject" path), (iii) a
  family-B evaluator + cold_init registered. Reuses everything else.

### Design A — REPLICATION (supporting): does the within-family effect generalize?
The original v3 (§1–§7 below): re-run the within-family Cold/Warm design on ≥2 more families,
efficiency DV, cross-family mixed model (G1/G2). Cheaper; shows the #4 effect isn't Heilbronn-only.

### Shared readiness (both designs)
- **Family headroom screen (§3):** keep only families where COLD has headroom (cold sometimes
  fails to finish in budget). Known: Heilbronn ✅, Tammes ✅ (evaluator exists, non-smooth → cold
  stalls), Thomson ❌ (smooth, screened out). autocorrelation / kissing / min-dist-ratio → probe.
- **Wiring:** register chosen families into `ablation_packing/families.py` (`.score`,
  `.triple_verify`, `cold_init`); Tammes is the cheapest add (evaluator already in `src/einstein/tammes/`).
- **Cost:** LLM-in-loop, expensive — gate the actual run on #4's clean verdict + an explicit go.
  Stage it: headroom probe (~$3) → small exploratory per family/pair (~$40) → freeze S → confirmatory.

---

## 0c. MODEL STRENGTH AS A FACTOR — the wisdom×capability gradient  (set 2026-06-28)

Run the transfer test (and replication) at **TWO model tiers — Haiku and Opus** — because the
deepest hypothesis is that *the value of accumulated wisdom decreases as raw capability rises*
(a weak agent needs the notes; a strong one already knows the method). This is the question that
matters for whether the wiki investment keeps paying off as models improve, and it answers the
external-validity worry ("Haiku isn't the agent we ship — Opus is").

- **Factor:** `model ∈ {haiku, opus}`. **Primary interaction H-model:** the transfer/within-family
  Δ is **larger for Haiku than Opus** (wisdom helps the weaker agent more). Test the model×arm
  interaction, not just each model alone.
- **Model-MATCHED difficulty (required).** Opus *saturates* the easy families (solves cold →
  zero headroom → wrong-reason null), so you cannot run both models on the same instances. Each
  model runs problems where **it** has cold headroom (cold sometimes fails in budget): Haiku on
  the current band (Heilbronn n=11–16 / Tammes), Opus on **harder** instances/families found by a
  **per-model headroom probe**. Each model is tested in its own flailing regime — "does wisdom
  help this model where it struggles."
- **THE RIGOR CATCH + fix.** Matched-difficulty confounds *model* with *difficulty* — a Haiku>Opus
  gap could be "weaker model" OR "easier problems." Mitigation: also run an **OVERLAP band** — a
  difficulty hard enough that Opus still has headroom yet not impossible for Haiku — and compare
  the two models **within that band**. The overlap gives the clean, difficulty-controlled model
  effect; the matched-difficulty arms give the broader picture. Report both; lead with the overlap
  for the causal model claim.
- **Cost:** Opus ≈ 2–3× Haiku/call → the Opus tier dominates the budget. Stage Haiku first (cheaper,
  has #4 continuity); add Opus only if Haiku shows the within-tier effect worth chasing, OR run the
  overlap band on both as the minimal model-comparison if budget is tight.
- **Don't:** run Opus on the *current easy* families (saturates), or swap the whole program to Opus
  (loses the #4 Haiku comparison, headroom, and budget).

---

## 1. Why a separate v3 (the threat it kills)

v2, however clean, tests **one family**. The strongest attack on the paper's
"the loop compounds" claim is selection: *"you screened families and kept Heilbronn,
the one where cold flails and warm helps."* The honest answer is replication — show
the effect in families chosen by a **pre-committed screen**, report every family run
(including nulls). One family is an anecdote; three concordant families is a property.

---

## 2. The claim under test

> *The Warm-over-Cold compounding effect (mean Δ > 0 and a positive banked-count slope)
> reproduces in mechanistically distinct families — so it reflects the accumulation
> loop, not the specific landscape of Heilbronn.*

Each family is its own complete v2 experiment (same arms, same counterbalanced order,
same DV, same H1/H2). v3 adds nothing to a single family's design — it pools across them.

---

## 3. Family selection — a PRE-COMMITTED headroom screen  **[FREEZE before run 1]**

The same screen that (correctly) rejected circle-packing in v2 §1. A family is
**eligible** iff, on a cheap probe (1 Cold session × 2 instances, the hardest two n
in the family's range):

- cold `gap_closed ∈ [0.2, 0.8]` on **both** probed instances — genuine headroom, not
  saturated (circle-packing failure mode) and not floored (unsolvable → no signal), AND
- the family has **L ≥ 6 consecutive instances** that share machinery (so a lesson can
  transfer and the Latin square has ≥6 positions), AND
- a **generic** harness-side evaluator + triple-verify exists or is ≤1 day to build
  (no baked problem-specific method — v2 §4 generic-solvers rule).

**Candidate pool** (screen in this order; take the first 2 that pass, 3 if budget allows):

| candidate | family kind | why distinct from Heilbronn | a-priori headroom guess |
|---|---|---|---|
| **min-distance-ratio** | spread/dispersion in the square | different objective (ratio, not min-area) but related geometry | likely mid |
| **Thomson** | min-energy points on the sphere | smooth potential, many local minima — *opposite* smoothness profile to Heilbronn's non-smooth min | mid (deceptive basins) |
| **low-autocorrelation binary seq** | discrete/combinatorial | discrete search space — most distinct landscape class | unknown — probe decides |
| **Tammes** | spherical packing (max-min angle) | sphere vs square; min-over-pairs like Heilbronn but different geometry | mid |

The probe results (table of cold gap_closed per candidate) get recorded here, then the
chosen families are **frozen**. Probing is exploratory; it informs selection, not any
H verdict.

**Pre-committed reporting rule:** every family that passes the screen and is run is
reported, effect or null. No dropping a family after seeing its Δ.

---

## 4. Per-family design — IDENTICAL to v2  **[FROZEN by reference]**

For each selected family, run v2 exactly:
- Arms (§v2.3), counterbalanced cyclic order (§v2.5), paired cold-init + equal context
  budget + reflection-equalized + air-gap (§v2.6), manipulation checks (run void on fail).
- DV = `gap_closed`, harness triple-verified; **S = 18** (three Latin squares), matching
  the v2 Stage-C freeze (raised from 12 by v2's measured within-problem SD ≈ 28 pts).
- **`--replicates 2`** (k-replicate variance reduction, branch `js/feat/ablation-kreplicate`):
  each cell is solved twice with independent cold-inits (shared across arms per replicate)
  and `gap_closed` is the mean of the two. **Note — this is NOT a power bargain:** SE of
  the per-family mean Δ scales as 1/√(S·k) at cost ∝ S·k, so k=2 is compute-equivalent to
  doubling S for the *level* test. It is specified here for what seeds *don't* give:
  (a) tighter per-cell `gap_closed` (σ/√2), which the per-problem **dose-response / H2
  shape** and the **heavy-tail diagnosis** need; (b) precision decoupled from the
  Latin-square block size. If the level effect is all that's wanted, k=1 at S=24 is an
  equally valid substitute — record the choice before the run.
- L = 6 consecutive instances spanning the family's headroom band (set per family from
  the probe; frozen before that family's run).

Only the family-specific objective + reference optima differ; the runner is already
family-agnostic (commit a3f45dc), so no harness change — just a config + evaluator per
family (mirror `ablation_packing` / the Heilbronn evaluator).

---

## 5. The NEW analysis — cross-family meta-test  **[FROZEN]**

Per family f, compute the v2 estimands: mean Δ_f and the banked-count slope β_f (Δ on
banked, problem fixed effect, bootstrap CIs).

- **G1 (level generalizes):** mean Δ_f > 0 in **every** run family (Heilbronn from v2
  included). *Decision:* supported if each family's 95% bootstrap CI of mean Δ excludes 0
  on the positive side; a single null family downgrades to "holds in k of n families,"
  reported honestly.
- **G2 (compounding generalizes):** β_f > 0 in every run family. *Decision:* per-family
  bootstrap CI of β excludes 0, positive.
- **Pooled estimate:** a mixed model `Δ ~ banked + (1 | family) + (1 | family:problem)`
  — family as a random effect — gives the across-family mean Δ and mean slope with
  family-level uncertainty folded in. Pre-committed as the headline generalization
  number. (Fixed-effect family dummies as a sensitivity check.)
- **Null handling:** if the effect appears in Heilbronn but vanishes elsewhere, that is
  the finding — "compounding is landscape-dependent" — and it ships. Pre-committed; no
  quiet family-swapping.

---

## 6. Staging & cost  **[FROZEN staging]**

1. **Screen (~$2–4):** the §3 probes across the candidate pool. Record → freeze the 2–3
   families.
2. **Per family, Stage C only** (the v2 pipeline is already validated, so no per-family
   smoke beyond a 1-session wiring check): S=18 × 6 problems × 2 arms × **k=2 replicates**
   = 432 sessions ≈ **$198/family** (≈ $0.46/session). Two families ≈ $396; three ≈ $594.
   Sequential, resumable, one seed-batch at a time (v2 §9 execution rules carry over).
   *Cost lever:* dropping to k=1 halves this to ≈ $99/family and still answers the level
   test (G1) at S=18 — k=2's spend buys the per-cell precision for the dose-response /
   heavy-tail reads, not the headline mean Δ.
3. **Meta-analysis** once all families' records are in.

Run families **sequentially**, each fully resumable; a family is analyzable the moment
its 432 cells complete, independent of the others.

**Dependency:** `--replicates` requires branch `js/feat/ablation-kreplicate` merged into
the runner first; until then v3 falls back to k=1 (S=18) with no design change.

---

## 7. Threats specific to v3

| threat | mitigation |
|---|---|
| Family cherry-picking | pre-committed headroom screen (§3) + report-every-family rule |
| "Distinct" families secretly similar (all geometric min-over-pairs) | pool deliberately spans objective *kinds* — ratio, smooth-energy, discrete-combinatorial — not just more geometry |
| Per-family evaluator bakes in wisdom | generic objective only, harness-side triple-verify (v2 §4/§6) — same bar |
| Multiple-comparisons (k families → inflated chance of one positive) | claim requires **every** run family positive (G1/G2 are conjunctions), not "≥1"; pooled mixed model is the headline, not per-family cherry-picks |
| Cross-family heterogeneity mistaken for null | random-effect family term models it explicitly; report the family-level SD |

---

## 8. Implications

- **G1 + G2 across families** → "the accumulation loop compounds" graduates from a
  Heilbronn result to a general property — the paper's external-validity backbone.
- **Heilbronn-only** → claim narrows to "compounds in non-smooth min-over-terms
  landscapes"; still a real, scoped result.
- **Mixed** → a map of *where* the loop pays off — arguably the most useful outcome.

*DRAFT pre-registration 2026-06-26. Freeze §3 (family screen) and the L-per-family
choices before the first confirmatory family run. Results → a separate `results-…md`.*
