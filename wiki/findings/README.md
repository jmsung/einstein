# findings/

Specific Q→A pages with cites. Each finding answers a particular question that came up while solving a problem; once it's been useful for 3+ problems, it gets promoted to `concepts/` (human-gated).

Findings are the *seed-bed* for concepts. Most of them stay as findings forever — that's fine.

## Page structure

```yaml
---
type: finding
author: agent | human | hybrid
drafted: YYYY-MM-DD
question_origin: [problem-{id} or `cross-problem`]
related_concepts: [...]   # populated as concepts emerge
cites: [source/..., wiki/findings/..., other refs]
status: open | answered | superseded
---
```

Body:
1. **Question** — the actual question, plainly
2. **Answer** — TL;DR, then full reasoning
3. **Evidence** — code, math, citations
4. **Where it applied** — which problem(s) used this finding
5. **Limits** — when the answer doesn't apply

## Failure findings (dead-ends)

Filename pattern: `dead-end-<slug>.md`. These are *just as valuable* as positive findings — every "I tried X and Y obstruction killed it" is data tomorrow's breakthrough sits on. Same structure but body section 2 becomes "Why it failed" and section 5 is "What this rules out."

## Promotion to concept

Once a finding is cited by 3+ other wiki pages OR explicitly invoked across 3+ problems, propose promotion:

1. Author a `concepts/<slug>.md` with the durable mental model
2. The finding stays in place (provenance) but gets `superseded_by: concepts/<slug>.md` in frontmatter
3. Human approval gate

The 24 thematic findings inherited from `wiki/findings/` are migrated in Goal 5.
