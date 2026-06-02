---
type: question
author: agent
drafted: 2026-06-01
asked_by: autonomous_loop cycle 54
status: open
related_problems: [14-circle-packing-square]
related_findings:
  - docs/wiki/findings/p14-slack-budget-middle-prediction-confirmed.md
  - docs/wiki/findings/p14-mpmath-slack-budget-analysis.md
---

# Does AlphaEvolve's published n=26 config pass `evaluate_strict(tol=0)`?

## The question (1 sentence)

When `ae_original_notebook.ipynb` coordinates are rounded to float64 and
passed through `einstein.circle_packing_square.evaluator.evaluate_strict`,
does the construction satisfy strict (tol=0) disjointness, or does it
depend on the arena verifier's per-problem tolerance band to rank #1?

## Why this matters

Cycle 53 placed our triple-verified score at 2.6359830849175907, ≈9.3e-15
below AE's `2.6359830849176`. The remaining gap is float64-representable
but not reachable by coordinate-descent ulp-polish on the current contact
graph (per
[p14-slack-budget-middle-prediction-confirmed](../findings/p14-slack-budget-middle-prediction-confirmed.md)).
Two outcomes remain:

- **(2a) AE strict-feasible** → rank #1 is a different contact graph / near-
  rigid deformation our polisher can't reach by coordinate moves. Topology
  enumeration becomes the next door.
- **(2b) AE not strict-feasible** → AE itself exploits a sub-tolerance
  overlap band, and rank #1 is closed by the *verifier*, not the optimizer.
  Closes the rank-#1 question with a dead-end.

The cost is one 5-minute script. The information is enormous.

## What "answer" looks like

A short finding `docs/wiki/findings/p14-ae-strict-feasibility-{verdict}.md`
with:

- AE coordinates extracted from `ae_original_notebook.ipynb` (the JSON
  payload of the notebook's final cell, already mirrored in
  `mb/problems/14-circle-packing-square/solutions/ae_original_notebook.ipynb`)
- `evaluate(tol=1e-9)` Σr
- `evaluate_strict(tol=0)` outcome (pass with Σr, or raise with worst
  overlap)
- `evaluate_verbose` worst pair overlap, worst wall slack
- Verdict: strict-feasible → (2a) live, or NOT strict-feasible → (2b)
  closes rank-#1 door

If (2b), file a dead-end finding closing the rank-#1 question.
If (2a), the next cycle should be topology enumeration (one-edge-flip
sweeps, dual-gated polish on each variant).

## How to run (5 minutes)

Outside the autonomous-loop write scope (needs `uv run python <script>`);
human or wiring cycle:

```python
import json
# extract circles from the notebook's solution cell
sol = {"circles": [...]}  # from ae_original_notebook.ipynb
from einstein.circle_packing_square.evaluator import (
    evaluate, evaluate_strict, evaluate_verbose,
)
print(evaluate(sol, tol=1e-9))
try:
    print('STRICT:', evaluate_strict(sol))
except Exception as e:
    print('STRICT FAILED:', type(e).__name__, e)
print(evaluate_verbose(sol))
```

If the notebook cell already serializes float64 coordinates (the on-disk
`solution-AE-tied-rank2.json` at Σr=2.6359830849176067 may already be
exactly this artifact — verify the source before trusting), the test is
just running the snippet against that JSON.

## See also

- [p14-slack-budget-middle-prediction-confirmed](../findings/p14-slack-budget-middle-prediction-confirmed.md)
- [p14-mpmath-slack-budget-analysis](../findings/p14-mpmath-slack-budget-analysis.md)
- [arena-tolerance-drift](../concepts/arena-tolerance-drift.md)
