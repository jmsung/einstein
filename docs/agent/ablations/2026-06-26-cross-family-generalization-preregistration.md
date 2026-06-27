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
- DV = `gap_closed`, harness triple-verified; **S = 12** (two Latin squares), matching
  the v2 Stage-C freeze.
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
   smoke beyond a 1-session wiring check): S=12 × 6 problems × 2 arms = 144 sessions
   ≈ **$66/family**. Two families ≈ $132; three ≈ $198. Sequential, resumable, one
   seed-batch at a time (v2 §9 execution rules carry over unchanged).
3. **Meta-analysis** once all families' records are in.

Run families **sequentially**, each fully resumable; a family is analyzable the moment
its 144 cells complete, independent of the others.

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
