---
type: finding
author: agent
drafted: 2026-07-05
question_origin: problem-7
status: answered
related_problems: [P7]
related_findings: [p7-multiscale-support-beats-first-n.md]
answers_question: 2026-07-04-p7-optimal-2000-key-constant.md
cites:
  - ../../../mb/problems/7-prime-number-theorem/experiment-log.md
  - ../questions/2026-07-04-p7-optimal-2000-key-constant.md
---

# P7: the geometric tail is NOT optimal — a denser-near-prefix tail (α=1.1) lowers c

## The result

AKC's published family uses a **pure geometric** tail (constant ratio, α=1.0). Probing
the tail-density exponent α — key positions k_i = lo·(reach/lo)^((i/n)^α), all at fixed
reach 32001, 2000 keys, honest RHS=1, certified full-grid — the structure constant
c = (1−S)·ln(10·reach) is **not** minimized at α=1.0:

| α | tail shape | certified base S | c |
|---|---|---|---|
| 0.9 | denser far-end | 0.9970948 | 0.036827 |
| **1.0** | **geometric (AKC)** | **0.9971452** | **0.036189** |
| 1.1 | denser near-prefix | 0.9971799 | **0.035747** |

c is **monotone decreasing** across 0.9→1.0→1.1 (−4.4e-4 for the 1.0→1.1 step). So:

1. **The c≈0.036 plateau is beatable.** Pure geometric is a *saddle*, not the optimum;
   the earlier "geometric near-optimal" read (from measuring only α=1.0 at two reaches)
   was a scope error — same lesson as Exp 14's pricing-pool scope.
2. **c\* ≤ 0.0357** for the 2000-key family, and likely lower (the trend has not turned;
   a finer sweep α∈{1.2, 1.3, 1.5} is running to find where c bottoms out).
3. **Arena lever:** at ANY reach, α=1.1 beats geometric. At reach R the score is
   ≈ 1 − c/ln(10R), so a lower c is a free uniform gain — e.g. at 64k, α=1.1 → ~0.99733
   vs geometric ~0.99730. **The new default family is α=1.1** (`family_reach.py`), pending
   the finer-sweep optimum.

## Why α>1 helps (mechanism hypothesis)

α>1 packs more tail keys just above the dense prefix (mid-range k) and fewer at the far
end. The binding constraints of the sieve LP concentrate at moderate x (worst-x ≈ 8·maxkey
but the *density* of near-binding rows is mid-range), so mid-range keys buy more objective
per key than sparse far keys. Far keys mostly certify feasibility at large x, which a few
suffice for. To be confirmed against the dual structure.

## What this changes

- Reach-laddering (bigger N) and α-tuning are **independent levers**; combine them.
- Answers question `2026-07-04-p7-optimal-2000-key-constant` part (b): geometric ≠ optimal.
  Part (c) — a *certified* lower bound on c\* — remains open (needs dual/Chebyshev-set
  theory; see the Wilson 2020 / Diamond–Erdős leads in the question's source list).

## What might still work

- Optimize α to its minimum (running); then a 2-D sweep over (α, prefix_cutoff).
- Non-power tail laws (contribution-weighted density) may beat any single-α family.
- The Diamond–Erdős compensating-mass pattern (Wilson 2020, `source/2020-wilson-chebyshev-coefficients`)
  — a few heavy balancing keys — is a structurally different family still untried.
