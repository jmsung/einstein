---
type: question
author: agent
drafted: 2026-06-22
status: open
asked_by: agent
related_problems: [6]
cites:
  - ../../source/2026-bianchi-einstein-arena-collective-intelligence.md
  - ../problems/6-kissing-d11.md
---

# Is arena kissing-d11 "achieve valid n=594" or "maximize n"? Our record is 604, not 594.

## The discrepancy

Our `problems/6-kissing-d11.md` treats the problem as **fixed n=594**: score = total hinge overlap,
score 0 proves κ(11) ≥ 594, status "conquered / terminal-min / unbeatable, no improvement possible"
(excluded from the active queue on that basis, 2026-05-28).

The platform paper (Bianchi et al., arXiv 2606.10402, Table 1 + §3) frames kissing-d11 as **scoring =
max**, with prior best 593 (AlphaEvolve) and **EinsteinArena best 604**. It explicitly narrates agents
extending a valid 594 config to 604 via a shared 496-vector backbone and integer-snapping.

## The unknown

Either (a) the live arena problem is "maximize the kissing-number lower bound n," and our page is
**stale** (frozen at the 594-feasibility sub-goal), or (b) the arena hosts a fixed-594 feasibility
problem distinct from the maximize-n problem the paper describes. Our `arena_url` in the P6 frontmatter
is `.../problems/kissing-number-d11` — which formulation does it currently serve?

## Falsifiable answer

Fetch the live problem spec (`scoring`, `solutionSchema`, `verifier`) via the arena API / `skill.md`.
- If `scoring: max` over n → our page is stale; P6 should be **reopened** with target > 594 and the
  integer-snapping + Σ(cᵢᵀcⱼ−2)²-surrogate operator (per the recognition finding) as the next move.
- If it is genuinely a fixed-594 feasibility verifier → keep "terminal," but add a note distinguishing
  it from the maximize-n record of 604 so the wiki doesn't read as "594 is the best known."

## Suggested sources

- Live arena API problem spec for `kissing-number-d11`.
- Bianchi et al. Appendix B (the n=604 construction).
- Finding: [`einstein-arena-paper-jsagent-recognition-2026-06`](../findings/einstein-arena-paper-jsagent-recognition-2026-06.md)
