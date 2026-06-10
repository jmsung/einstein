---
type: question
author: agent
asked_by: ramanujan
drafted: 2026-06-04
status: open
related_problems: [12]
---

# P12 headroom (Ramanujan lens): does the SOTA vector hide a modular/character structure the metaheuristic can't see?

Ramanujan's instinct: stare at the SOTA ±1 vector itself, not the score. The strategy notes its first 18 coefficients are exactly [-1,-1,1]×6 and conjecture it is "likely PSL-related." A metaheuristic that flips bits to minimize a grid max is structurally blind to number-theoretic seeds — it cannot *recognize* a character sequence, only stumble onto one. The right algebraic object is recognized, not searched.

1. Does the byte-identical SOTA vector (sha256 `992570de7873`) match any character/q-series sequence — a twisted Legendre/Fekete with a non-trivial shift, a Gauss-sum sign pattern mod 71, or a Φ_35-aware sequence (since the evaluator flags Φ_35's 24 primitive roots as the spectral bottleneck) — i.e. is the period-3 prefix a fragment of a modular pattern rather than "a consequence of optimality"?
2. The peak lives on the Φ_35 cyclotomic component (35 = 5·7, coprime to the degree+1 = 70 = 2·5·7); does choosing coefficients via a multiplicative character that makes |p| *equioscillate* across the coprime-modulus roots (CRT tensor over 2×5×7) give a construction whose worst peak is provably lower than any incoherent ±1 vector — the flat-polynomial analogue of Rudin-Shapiro's √2 bound but tuned to 71's arithmetic?
3. Is there a degree-69 polynomial from a known flat family (Turyn with the *optimal* shift solved exactly, not t=22 by guess; or a Sidelnikov/Legendre-Sidelnikov two-prime sequence at the right prime pair) whose continuous sup beats 1.2809 — and if every classical family overshoots, does that *itself* certify the SOTA is non-algebraic (genuinely transcendental optimum), redirecting all future effort to the grid-drift reconciliation rather than construction search?

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"headroom Ramanujan lens does the SOTA") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
