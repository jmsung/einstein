---
type: finding
author: hybrid
drafted: 2026-05-02
question_origin: cross-problem
status: answered
related_concepts: [parameterization-selection.md, provable-floor-and-frozen-problems.md, asymmetric-kronecker.md]
related_techniques: []
related_personas: [atiyah.md, polya.md, _synthesis.md]
cites:
  - ../personas/_synthesis.md
  - ../personas/atiyah.md
  - ../questions/2026-05-02-bootstrap-cycle-friction-log.md
  - dead-end-p19-different-k-local-search.md
---

# When prior work is exhausted: cross-pollinate fields, don't add compute

## TL;DR

When a problem has saturated known approaches (all classical algebraic constructions failed, all local search exhausted, established LP/SDP bounds are loose), the path forward is **cross-pollination of seemingly unrelated fields**, not bigger machines running known recipes. "Try harder with more compute" produces rank yield, not wisdom yield. New connections between adjacent fields produce both.

## The principle

For any problem in a wisdom-mining context, every "what to try next" decision admits a binary filter:

| Move | Signal | Yield |
|---|---|---|
| Known recipe + bigger machine | "We just need more GPUs / longer SA / wider basin search" | Rank only. Wisdom static. |
| Cross-pollination from an unrelated field | "Wait, this looks like X from Y, has anyone tried...?" | Wisdom + (sometimes) rank. |

The diagnostic: **can you articulate WHY the connection might exist?** A good cross-pollination has a structural reason — a shared underlying object, a known equivalence between formulations, an analogy at the level of definitions. A bad one is "let's just try more random stuff."

This generalizes Atiyah's "marrying of fields" stance — when one field is stuck, import a tool from another (see [`personas/atiyah.md`](../personas/atiyah.md)). Atiyah did this between algebra and geometry; the same instinct works between additive combinatorics and coding theory, between optimization and measure theory, between complexity theory and Fourier analysis.

## When to apply

The signal that you're past the "more compute" mode and into "cross-pollinate" mode is a combination of:

1. **Local search exhausted** — 1-/2-/3-swap, SA, basin-hopping, CMA-ES from SOTA all fail.
2. **Known constructive families exhausted** — for the problem's domain (Singer / Bose / Paley / GMW for difference sets; Wichmann for sparse rulers; etc.), all standard constructions tested.
3. **Established bounds are loose but won't tighten** — LP / SDP duals proved many years ago, no recent progress on the constants.
4. **The community has converged on a single recipe** — multiple agents byte-identical at SOTA, all using minor variations of the same idea.

When all four hold, the marginal value of more compute is approximately zero. The marginal value of a new connection is bounded only by how unexpected the connection is.

## How to find new connections

Effective queries (try these explicitly during research):

- "What does this problem look like in field X?" — for each unrelated field (coding theory, measure theory, complexity, Fourier analysis, dynamical systems, statistical mechanics, formal languages, ...).
- "Is there an *equivalence*, not just an analogy?" — analogies are weak; equivalences let you import full theorems.
- "Has anyone *inverted* an existence proof into a construction?" — obstruction proofs (Bernshteyn–Tait, Cohn–Elkies dual, etc.) often have a constructive shadow that nobody's explored.
- "What if I relax one constraint?" — the standard Sidon constraint (B₂[1]) generalizes to B₂[g] for g≥2; what does the problem look like in the relaxed regime?
- "What if the problem is *secretly* a different problem?" — Tao's reformulation of P7 PNT as an LP is the canonical example; all sieve-theory problems may be LPs.

Ineffective queries (these are "more compute" in disguise):

- "What's the latest RL/LLM approach to combinatorics?" (it's still local search with a learned heuristic).
- "Should we use a bigger model?" (model size is compute, not connection).
- "What would AlphaEvolve do here?" (AE is itself a known recipe at this point).

## Evidence — P19 Difference Bases (2026-05-02)

This finding emerged from the first post-refactor cycle on P19. After Step-1 reading of prior work, the candidate list naturally split:

**More-compute candidates (DROPPED)** — all promising for *rank* but not *wisdom*:
- TTT-Discover port — RL on a fixed target with bigger compute
- PatternBoost — transformer + local search alternation
- Hybrid AlphaEvolve — generative search with structured seed

**Cross-pollination candidates (KEPT)** — each is a new connection:
- Saarela–Vanhatalo (2024 arXiv:2408.16335) — combinatorics on words ↔ sparse rulers
- Buratti et al. (2025 arXiv:2510.20446) — perfect difference families subsume Singer/Bose/Paley/GMW under one framework
- Optimal transport relaxation — measure theory ↔ rulers, Wasserstein distance to uniform
- Bernshteyn–Tait inversion — turn the 2019 lower-bound *obstruction* proof into a construction
- Asymmetric Kronecker — break the 4-fold symmetry, multi-block decomposition

The filter applied here is *not* "which is most likely to land #1" — it's "which produces a wiki entry whether it lands or fails." That's the wisdom-yield criterion.

## Triggering moment

User stated the principle directly during P19 cycle 1 (2026-05-02): *"sometimes completely new dots, seemly unrelated, could make a new connection. i want to make general knowledge on math from this arena rather than just try already known approach and try harder with more computation."*

The principle was implicit in the project's reframing (math wisdom > rank, biological-evolution-like compounding) but had not been written down as a *filter*. This finding makes the filter explicit.

## Limits

This is a filter, not a theorem. Specifically:

- Cross-pollination has a **success-rate floor near zero on any single attempt** — most cross-field connections turn out to be analogies-not-equivalences or fail when transferred. The wisdom-yield comes from the *attempt* (it produces a finding either way), not from the success rate.
- "More compute" is sometimes the right call — when the recipe is known to work and the question is really just resolution. The filter shouldn't block compute-driven *verification* (e.g., w=4 BnB exhaustive lemma).
- The filter itself can become a cargo cult — "I'm cross-pollinating!" with no structural reason. Watch for "I can articulate WHY this connection might exist" honesty check.

## See also

- [`personas/atiyah.md`](../personas/atiyah.md) — cross-field marriage as a stance
- [`personas/_synthesis.md`](../personas/_synthesis.md) — stance #8 (cross-pollinate fields), where this finding plugs in
- [`findings/dead-end-p19-different-k-local-search.md`](dead-end-p19-different-k-local-search.md) — the immediate predecessor; demonstrates the local-search saturation that triggers the filter

*Last updated: 2026-05-02*
