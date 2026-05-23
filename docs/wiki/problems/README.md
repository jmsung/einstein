# problems/

One short index page per Einstein Arena problem. NOT the operational playbook — that lives in `mb/tracking/problem-{id}-{slug}/` (private, time-bound).

Each `problems/<id>-<slug>.md` page is the *publishable* summary:
- Problem statement
- Approach summary (sanitized — no specific seeds, multipliers, in-flight params)
- Final result + score
- Concepts and techniques used (links into `concepts/`, `techniques/`)
- Findings produced (links into `findings/`)
- Pointer to the live tracking dir (private)

Plus the project compass:

- **[`_inventory.md`](_inventory.md)** — concept-coverage matrix across all 23 problems. Drives the wiki refactor and the self-improvement cycle.

## Page structure

```yaml
---
type: problem
author: agent | human | hybrid
drafted: YYYY-MM-DD
problem_id: 6
arena_url: https://einsteinarena.com/problems/kissing-number-d11
status: conquered | top-3 | rank-N | frozen | open
score_current: 0.000000
tier: S | A | B | C       # learning-ROI tier from _inventory.md
concepts_invoked: [sphere-packing.md, hinge-loss.md, ...]
techniques_used: [parallel-tempering.md, mpmath-ulp-polish.md, ...]
findings_produced: [perturbation-landscape.md, ...]
private_tracking: ../../../mb/tracking/problem-6-kissing-d11/
---
```

Body:
1. **Statement** — math problem in plain language
2. **Approach** — what worked, what didn't (narrative-level, not param-level)
3. **Result** — final score, rank, date
4. **Wisdom hook** — the one-sentence generalizable insight this problem teaches
5. **References** — links into concepts/techniques/findings/personas, and out to source/papers/

Per-problem index pages are populated in Goal 9 (tracking move), one per problem.
