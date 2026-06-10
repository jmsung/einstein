---
type: question
author: agent
drafted: 2026-06-04
status: open
related_problems: [2, 3, 4, 10, 12]
cites:
  - ../findings/autocorrelation-family-displaced-2026-06.md
  - ../findings/dead-end-p3-resolution-inflation.md
  - ../../../../mb/logs/leaderboard-audit-2026-06.md
---

# Phase 7 headroom council — synthesis + goal re-prioritisation (2026-06-04)

Synthesis of the per-target council dispatch (17 question files,
`2026-06-04-p{2,3,4,10,12}-headroom-*`). Each panel was seeded with the
displacement findings and told to build *past* known facts. The recon surfaced
four discoveries that re-order the branch's effort.

## Discoveries that change the plan

1. **P2 seed is NOT lost.** `mb/problems/2-first-autocorrelation/solutions-v3/solution-best.json`
   holds the 90000-cell basin (stored score 1.5028616283497658). The real gap is
   **verifiability** — a naive recompute gives 8.3e-6 because the score only holds
   under the canonical arena grid-normalisation. Same *class* of hazard as P12's
   grid drift. Also: all 90000 cells are nonzero, so the wiki's "v² dead-cell
   escape" mechanism may not explain the actual winning basin (a load-bearing
   claim to re-check).
2. **P3 may be fundamentally capped.** A 30-min lookup of Rechnitzer (2026)'s
   rigorous continuum upper bound could close P3 as capped *before* any compute —
   cheapest decisive check in the branch.
3. **P10: we submitted the wrong basin.** We hold the Wales seed (37147.2944) but
   our live submission is a worse basin (37147.53, ~#5). Wales only *ties* arena
   #1 (AlphaEvolve), so this is a human-approval "tied-SOTA" case, **not**
   auto-submittable (strict-improve gate rejects a tie). Pure rank upside, zero
   compute — flag for the human.
4. **P12 is tied-at-SOTA, not losing a race.** MTS rediscovered the byte-identical
   arena SOTA (sha256 992570de…); the only blocker is the ~7.3e-10 grid drift
   (always positive — arena samples the continuous peak more finely than our 1M
   grid). Goal 2 (drift reconciliation) is the actual unlock, not a new construction.

## Top-3 questions per problem (ranked by expected impact)

**P2 (Goal 1)** — polish-shaped, 1.84e-7 gap:
1. Is OrganonAgent's 1.5028609074 a structurally distinct basin or our basin
   polished? (compare active-peak count/positions; needs arena-API download of
   their values) — decides polish vs new-basin, gating everything.
2. Does the v3 seed re-evaluate to 1.5028616283497658 under all three verify
   paths today, under the canonical normalisation? (reproducibility + the
   dead-cell claim)
3. Is n=90000 an L-BFGS-converges-too-fast artifact, curable by 3× longer low-β
   exploration at n≥120000? (cheapest shot at new headroom)

**P3 (Goal 3)** — large gap, new-basin:
1. (Cohn) Is Rechnitzer 2026's rigorous continuum upper bound below the gate
   threshold 0.9627433? — could close P3 as capped, cheapest check.
2. (Tao) Does the quadratic ★ inject above-Nyquist energy that no f-side
   downsample can pre-empt — is ‖down(f)★down(f) − down(f★f)‖ irreducible? —
   decides whether the high-res→100k path is structurally possible at all.
3. (Hilbert) State the minimal cross-resolution agreement predicate for
   `triple_verify/problems/p03` as a gate-2 prerequisite (closes the false-record
   auto-submit risk).

**P4 (Goal 4)** — family-twin of P2:
1. (Tao) What single Fourier-side move produces both the P2 and P4 extremizers,
   differing only by one positivity constraint? (family-twin technique)
2. (Hilbert/Riemann) Optimise in a signed spectral/Chebyshev space exploiting
   negative-lobe cancellation — the sign freedom our toolkit never used.
3. (Cohn) Signed-f LP/SDP dual certificate to decide polish-vs-new-basin for C₃.

**P10 (Goal 5)** — frozen, low EV:
1. (Archimedes) Replace our submission with the Wales basin we already own
   (rank upside, zero compute — human-approval tied-SOTA submission).
2. (Archimedes) Certify the floor: projected Hessian λ_min > 0 on the 561
   rotation-gauged tangent DOF — turns "20 years unbeaten" into a verifiable
   strict-local-min statement (the honest-zero deliverable).
3. (Conway) Is there an unsearched symmetry-broken / alternate-T=28-isomer
   sub-basin? Every prior search warm-started from the symmetric Wales seed.

**P12 (Goal 2)** — tied-SOTA, drift-blocked:
1. (Razborov) Certify the continuous sup to <1e-9 via FFT zero-padding + per-peak
   Newton, replacing the grid quantity — dissolves the submission blocker by
   construction.
2. (Erdős) Second-moment estimate of E[#vectors below 1.2809] over {±1}⁷⁰ —
   decides whether "search exhausted" is evidence-backed or faith-based.
3. (Ramanujan) Decode the byte-identical SOTA vector as a character/q-series
   sequence — if it matches a known family the construction generalises.

## Re-prioritisation (cheapest-decisive first)

The branch's goal order assumed all five targets need heavy compute. The recon
says otherwise. Recommended execution order:

- **Goal 2 (P12)** — drift certification is pure analysis and unblocks a
  tied-SOTA submission. Highest EV-per-hour.
- **Goal 1 (P2)** — verify the v3 seed under canonical normalisation; download
  OrganonAgent's values to decide polish-vs-basin before spending compute.
- **P3 Rechnitzer-bound lookup** (within Goal 3) — a literature check that may
  close P3 with zero compute.
- **Goal 5 (P10)** — the Wales-seed swap + Hessian floor certificate are cheap;
  surface the tied-SOTA submission for human approval.
- **Goals 3/4 (P3/P4) heavy search** — only after the above; gated on the
  cross-resolution agreement predicate existing first.

The unifying thread: **three of five targets (P2, P3, P12) are gated by a
score-comparability / resolution problem, not by search.** Build the
cross-resolution / continuous-sup verification *before* chasing basins.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"Phase 7 headroom council — synthesis") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
