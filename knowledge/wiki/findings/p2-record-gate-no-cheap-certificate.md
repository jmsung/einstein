---
type: finding
author: agent
drafted: 2026-06-07
question_origin: problem-2
status: answered
related_problems: [2]
related_concepts: [autocorrelation-inequality, lp-duality]
related_findings:
  - p2-lower-bound-research-state.md
  - dead-end-p2-lasserre-l2-weaker-than-cs.md
  - dead-end-p2-compact-support-basin-floor.md
cites:
  - ../findings/p2-lower-bound-research-state.md
  - ../findings/dead-end-p2-lasserre-l2-weaker-than-cs.md
  - ../findings/dead-end-p2-compact-support-basin-floor.md
  - ../../source/2010-matolcsi-autoconvolution.md
  - ../../source/2017-cloninger-autoconvolution-sidon.md
---

# P2 record-gate: no cheap dual certificate can adjudicate the arena floor

## Question (Goal 0 of `js/feat/p2-record-breakthrough`)

Is a Cohn-style LP/SDP dual lower-bound certificate for P2 cheap, and would it
prove `1.5028609073611` (arena #1, OrganonAgent) is the infimum? If provable,
freeze the branch instead of burning nights on a proven floor.

## Answer: the certificate route cannot reach the arena value — by a wide margin

The dual/certificate landscape for the *continuous* constant $C_1 =
\inf\{\|f\star f\|_\infty : f\ge 0,\ \mathrm{supp}\,f\subseteq[-\tfrac14,\tfrac14],\ \int f=1\}$
is fully mapped (see [p2-lower-bound-research-state](p2-lower-bound-research-state.md)):

| Certificate route | Best lower bound | Ceiling reason |
|---|---:|---|
| Fourier-kernel / Cohn–Elkies LP duality | **1.2748** | **Theoretical ceiling ≈1.276** (Matolcsi–Vinuesa 2010 §4) |
| Lasserre / SOS level-2 | ~1.0 (asymptote) | Structurally looser than C-S at every tested $n$; $\sim n^4$ wall-clock, intractable at arena $n{=}90000$ ([dead-end-p2-lasserre-l2-weaker-than-cs](dead-end-p2-lasserre-l2-weaker-than-cs.md)) |
| Cloninger–Steinerberger LP-BnB | **1.28** | Compute-bound; $\sim10^6$ CPU-h to push to ~1.30, exponential in $n$ |

Every provable lower bound caps at **≤1.28**. The arena value **1.5028609073611**
sits ~0.22 above that ceiling. So **no cheap certificate proves the arena floor** —
the certificate route is not too expensive, it is *structurally too weak* to say
anything about whether 1.5028609073611 can be beaten. (The conjectured continuous
infimum is $C_1\approx 3/2$, consistent with the construction side, but that is a
conjecture, not a certificate.)

## The gate therefore turns on empirical evidence, not a proof

Goal 0's literal "stop because proven" exit is unavailable. But the floor is
nonetheless near-certain on empirical grounds
([dead-end-p2-compact-support-basin-floor](dead-end-p2-compact-support-basin-floor.md)):

- **Two independent agents tied to 1e-13.** OrganonAgent #1 (1.5028609073611) and
  CHRONOS #2 (…612) are *bit-identical in structure* — same 74489/90000 nonzero
  cells, same compact support, same max. Two independent searches landing on the
  same compact-support configuration is strong global-minimum evidence.
- **Polishing the leader's own solution gains 2.57e-10** — 25× *below*
  `minImprovement` (1e-8). The compact-support basin is at its floor.

## What this rules out

- A provable-floor freeze (the certificate can't prove it).
- Any expectation that a dual certificate could *guide* the search toward a
  sub-1.5028609073611 basin — it caps 0.22 too low to discriminate.

## What might still work (the only remaining lever → Goal 1, if run)

The one genuinely untried construction: a **compact-support-targeting search** —
we only ever *landed* full-support basins; we never *searched* for an even-better
compact-support basin. Zero the outer ~17% (or a support-shrinking schedule) +
v² L-BFGS on the smooth-max surrogate, multistart, **not** warm-started from our
full-support basin. EV is low (the 2-agent tie argues the leaders already found
the compact-support floor), but it is the only unexplored door and is the explicit
content of Goal 1.

## Verdict for the branch

Goal 0 resolves to: **certificate route dead for adjudicating the record; floor
rests on empirical 2-agent-tie evidence; Goal 1 is the lone low-EV lever.** This is
a go/no-go decision on multi-day compute, surfaced to the human.
