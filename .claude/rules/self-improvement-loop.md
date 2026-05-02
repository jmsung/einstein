# Self-improvement loop — gap → search → ingest → distill → page

The agent gets smarter ONLY by closing this loop. Skipping any step breaks compounding.

```
   ┌──────────────────────────────────────────────────────────────┐
   ▼                                                              │
1. GAP DETECT     A question came up that wiki/ doesn't answer.   │
                  (From council dispatch, from work, from         │
                  protocol step 4.)                                │
                                                                  │
2. FILE QUESTION  wiki/questions/<YYYY-MM-DD>-<slug>.md            │
                  status: open, asked_by, related_problems         │
                  THIS IS THE STEP MOST OFTEN SKIPPED.             │
                                                                  │
3. SEARCH         /wiki-research first (web with explicit         │
                  approval). Read related findings/concepts        │
                  for partial answers.                             │
                                                                  │
4. INGEST         /wiki-ingest the relevant artifact —             │
                  human-gated. Lands in raw/ + source/ atomic.     │
                                                                  │
5. DISTILL        /wiki-learn or /wiki-query --file-back to        │
                  produce wiki/findings/<slug>.md with cites,      │
                  closing the question (status: answered,          │
                  answer_finding: <path>).                         │
                                                                  │
6. PROMOTE?       If the finding is cited 3+ times OR              │
                  generalizes beyond a single problem,             │
                  human-gated promotion to wiki/concepts/.         │
                                                                  │
7. CYCLE          Next question loops back to step 1.              │
                                                                  └──
```

**Why:** Without this loop, knowledge is generated in-context and lost at end-of-session. The wiki is the *only* persistence layer that survives across sessions/contexts/models. Every gap that doesn't get filed is wisdom permanently lost. Every finding that doesn't get cited is wasted distillation work.

**How to apply:**

- **Step 2 is non-optional.** Even if you can't answer the question right now, file it. An open question is a future research seed.
- **Filing is fast** — 30 seconds, 4 frontmatter fields, 2 sentences of body. No excuse.
- **Step 5 is the deliverable** — a question without a finding is half-done work. After answering, ALWAYS author the finding before moving on.
- **Step 6 (promotion)** is human-gated to prevent agent-driven concept inflation. Don't promote your own findings unprompted.
- **Cite hygiene**: every finding cites at least one source/ entry or external paper; every concept cites the findings it grew from.

**Triggering moments:** any time `/wiki-query` returns "the wiki has nothing on this." Any time a council persona surfaces a question with no answer. Any time the optimizer hits a wall and the why is unclear.

**The honesty check:** if a session produces zero new wiki questions/findings/concepts, either (a) you only worked on already-mapped territory (fine, but rare), or (b) you skipped the loop. Cycle log will show which.

See also: [math-solving-protocol](math-solving-protocol.md), [council-dispatch](council-dispatch.md), [failure-is-a-finding](failure-is-a-finding.md), [wiki-attribution](wiki-attribution.md).
