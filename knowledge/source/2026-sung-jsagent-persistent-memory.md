<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
domains: [ai-agents, ai-reasoning, sci-math]
title: "JSAgent: Compounding Mathematical Discovery Through Persistent Agent Memory"
authors: [Jongmin Sung]
year: 2026
doi: 10.5281/zenodo.23852094
source_url: https://zenodo.org/records/23852094
drive_file_id: 1isHtgW7waYezpy-WFXFjiO76FCj0eMrB
text_source: pdf
ingested_by: agent
---

# JSAgent: Compounding Mathematical Discovery Through Persistent Agent Memory

**Sung (independent). Zenodo preprint, published 2026-11-01 (build dated 2026-09-05), CC-BY-4.0.
33 pages. Also submitted to AIAS+ 2026; an arXiv v1 sits on moderation hold.**

## Thesis

LLM agents can already produce mathematical constructions that pass objective verifiers, but the
*reusable reasoning* behind them evaporates when the run ends. JSAgent is a mathematical-optimization
agent built around **persistent, human-readable memory** — a knowledge base of concepts, failed
attempts, techniques and behavioral rules carried across problem-solving cycles. The claim is
deliberately bounded: in domains with cheap objective verifiers, agentic discovery can be made
**auditable** through a verification-and-memory loop, while human judgment stays central to problem
selection, promotion and submission.

The headline the paper defends is **efficiency, not quality**: memory makes the agent reach
comparable solutions with fewer budget-exhausting runs; it does not raise final solution quality at
a fixed budget. The paper reports that distinction as its own result, nulls included.

## Verified results (EinsteinArena, SOTA-when-submitted)

| Problem | Value | Rank | Status |
|---|---|---|---|
| P14 circle-packing (26 in unit square) | 2.6359830849 | #1 | clean |
| P18 circles-in-rectangle (n=21) | 2.3658323852 | #1 | clean |
| P2 first-autocorrelation | 1.5028506 | #1 at submission, later #2 | clean, a verified record |
| P1 Erdős min-overlap | 0.3808703 | #2 | matched arena best, not global |
| P3 second-autocorrelation | 0.962214 | #3 | clean |
| P4 third-autocorrelation | 1.452521 | #3 | clean |
| P7 prime-number-theorem | 0.994847 | #3 | clean |
| P11 Tammes | 0.513472 | #3 | clean |
| P22 kissing-d12 | 2.001403 | #3 | clean |
| P9 uncertainty | ≈0.318 | #1 | **contested** — above the proven 0.3102 upper bound; kept as a verification-scar case |

"Clean" = strictly-feasible, triple-verified construction. The board has since moved as other agents
built on these; the paper treats that as the ecosystem working, and what does not decay is the
verified construction itself. The P9 row is reported as a failure of the arena's verifier, not a win.

## Controlled ablations (pre-registered)

Pre-registration files are committed before the data (`docs/agent/ablations/…`); CIs are 95%
percentile bootstrap over 10,000 resamples, fixed seed, 600-second per-run solve timeout equal
across arms. A CI straddling 0 is reported as "no detected effect", never as proof of no effect.

| Mechanism | Verdict | Effect |
|---|---|---|
| Knowledge base (cold vs. warm) | quality null; **efficiency supported** | quality Δ=+0.036 gap-closed, CI [−0.006, +0.080]; budget exhausted 10/108 warm vs 28/108 cold |
| Problem-specific plugins | supported (family with headroom) | Δ=+0.214, CI [+0.185, +0.242]; ~30× faster |
| Persona council | null (pilot, n=8) | Δ=+0.004, CI [−0.11, +0.13] |
| System-prompt framing | null (pilot, n=8) | Δ=+0.035, CI [−0.10, +0.18] |
| Adaptive scheduling | null | Δ=−0.001, CI [−0.010, +0.009] |

The cold-vs-warm test is the best-powered result: 18 seeds on each of 6 problems = **108 paired
comparisons, 216 runs**. Memory cut budget-exhausting timeouts by a paired Δ=−16.7pp
(CI [−26.9, −6.5]) and saved 89s of wall-clock on average (CI [−142, −34]s). Both efficiency
intervals exclude zero; the quality interval does not.

**Memory raises the floor, not the ceiling.** By quantile within the 108-pair experiment, warm
exceeds cold by +0.113 at the 10th percentile, +0.021 at the 25th, +0.039 at the median, and only
+0.014 at the 90th. A tail-sensitive 60-cell follow-up pointed the same way but was not significant
(+0.075, CI [−0.002, +0.152]) and is uncorrected for multiplicity.

A cross-family transfer test (circle packing at n=60, 80 against tabulated optima) was
**uninterpretable under saturation**: the base model reached ~99% of the true optimum unaided, so
the harness had no headroom to demonstrate.

## Harness mechanisms

- **Wiki-first retrieval** — the agent consults its own knowledge base before searching; a written
  plan stating what to do and why precedes any optimizer run.
- **Triple verification** of every construction before submission.
- **Wall-hit escalation** — a plateau or "wall" event re-triggers the persona council. The council
  reframing that produced the P2 record was exactly such an event, and it is the kind of rare,
  high-value event a mean-over-runs ablation is structurally unable to detect — the paper says so
  about its own null.
- **Obstruction-indexed technique reuse** — techniques filed under the obstruction they overcome.
- **Compute routing** — MacBook Air M4 locally for most work, Modal for heavy runs (kissing d=11).
- Reuse telemetry: wiki hit-rate 26%, cite-reuse 84%. A record-producing direction was recovered
  and refined from an earlier dead-end note.

## Why it matters

The paper is a worked example of the discipline this corpus's gate design asks for: pre-registration
before data, ablations that report their own nulls, a saturation case called uninterpretable rather
than spun, and a contested result (P9) kept in the table as a verifier failure. The claim it ends on
is bounded to verifier-rich domains, and it says plainly where human judgment is still load-bearing.

## Open questions

- Transfer beyond cheap objective verifiers (formal proof, algorithm design, wet-lab biology) is
  untested; the one transfer experiment attempted saturated.
- Three of five ablations are pilot-scale (n=8) and underpowered — their nulls are weak evidence.
- Single author and single agent, so the "compounding" claim rests on one system's trace history.
- The efficiency result is at a fixed 600s timeout; whether the advantage survives a much larger
  budget is not measured.
