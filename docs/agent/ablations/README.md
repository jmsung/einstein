# ablations/

Controlled experiments measuring whether the wiki + agent infrastructure actually causes self-improvement (vs. memorization, vs. compute-time, vs. human-laundered).

## Cadence

Monthly. One file per ablation: `<YYYY-MM>-<slug>.md`.

## Page structure

```yaml
---
type: ablation
author: human
drafted: YYYY-MM-DD
hypothesis: <falsifiable claim>
status: proposed | running | complete | inconclusive
---
```

Body:
1. **Hypothesis** — what we predict, in falsifiable terms
2. **Method** — variables held constant, variables varied, sample size
3. **Setup** — exact commands / branches / wiki snapshots used
4. **Results** — raw measurements, no spin
5. **Conclusion** — was the hypothesis supported, falsified, or inconclusive?
6. **Implications** — what we change in the agent / wiki / rules as a result

## Standing ablations

1. **Cold-wiki vs warm-wiki** (monthly) — solve a held-out problem with empty `wiki/` (clean checkout at `pre-wiki` tag) vs current wiki. Measure delta in time-to-top-3 and concept coverage.
2. **Persona ablation** (quarterly) — for each persona, disable it; rerun a council on a sample problem; measure whether the persona's specific question class is missed.
3. **Skill-library trust** (semi-annual) — does following `skill-library.md` rank for technique selection actually correlate with success? Or is the rank purely correlational?

The honest answer to "is the wiki earning its keep" lives here.
