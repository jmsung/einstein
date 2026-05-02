# questions/

Open math questions awaiting research. The seed-bed of the self-improvement loop.

## How questions get here

1. **Council dispatch** — when a problem starts, each persona writes 1 question (not a solution). All land here.
2. **Gap detect** — wiki-first lookup returns nothing → write the question, file it here.
3. **Manual** — human or agent notices something they want answered.

Filename pattern: `<YYYY-MM-DD>-<slug>.md`.

## Page structure

```yaml
---
type: question
author: agent | human | hybrid
drafted: YYYY-MM-DD
status: open | answered | abandoned | superseded
asked_by: [persona-name OR "human" OR "agent"]
related_problems: [P6, P22]
related_concepts: [sphere-packing.md, ...]   # if any exist yet
answered_at: YYYY-MM-DD                       # populated when answered
answer_finding: findings/<slug>.md            # populated when answered
---
```

Body:
1. **Question** — plainly stated
2. **Why it matters** — what would the answer unblock?
3. **What's been tried** — quick rundown if anything
4. **Hypotheses** — informed guesses with cites
5. **Next step** — concrete action (search literature, derive, code experiment, …)

## Lifecycle

```
new question → status: open
              ↓
      research / derive / experiment
              ↓
   answered → status: answered
              answer_finding: findings/<slug>.md
              the finding becomes the canonical reference; the question stays as provenance
              ↓
              if cited 3+ times → finding promotes to concept (human-gated)
```

Closed questions are NEVER deleted. The trail of "what we asked and what we learned" is the self-improvement evidence.
