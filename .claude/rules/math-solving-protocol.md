# Math-solving protocol — Polya / Hadamard / Tao loop

Every hard math problem in this repo follows this loop. It's drawn from how the great mathematicians actually work (see `wiki/personas/_synthesis.md` for the 12 stances).

```
1. UNDERSTAND        Restate problem in own words. Write unknowns / data / conditions
                     explicitly in mb/tracking/<problem>/strategy.md. Most "stuck" is
                     "haven't really read it." (Polya)

2. WIKI-FIRST        Query wiki/concepts, /techniques, /findings, /problems for prior
                     work, related concepts, similar problems. Cite. (See wiki-first-lookup.)

3. COUNCIL DISPATCH  Pick 3–5 personas from wiki/personas/ based on problem category.
                     EACH writes a QUESTION (not a solution) to wiki/questions/.
                     (See council-dispatch.)

4. GAP DETECT        For each question:
                       answered in wiki?  → cite & continue
                       partial?           → flag for refinement
                       absent?            → escalate to (5)

5. RESEARCH          /wiki-research; user-gated /wiki-ingest into raw/+source/.
                     For each ingested artifact, distill into source/.

6. DISTILL           /wiki-learn turns the answer into wiki/findings/<slug>.md
                     with author: agent|human|hybrid attribution and cites.

7. SPECIALIZE        Try n=2,3,4 by hand BEFORE the optimizer. (Polya / Tao)
                     Compute small examples, look for patterns. (Gauss / Euler)

8. EXECUTE           Implement in src/. Tracking goes to mb/tracking/<problem>/
                     experiment-log.md. Compute routed via compute-router rule.

9. LOOK BACK         After any result, ask: does this generalize? where else?
                     what was the key idea? Update or create wiki/concepts/<x>.md.
                     (This is the only step that compounds. Polya's most-skipped.)

10. FAILURE LOG      Every dead-end → wiki/findings/dead-end-<slug>.md with the WHY.
                     (See failure-is-a-finding.)
```

**Why:** Without this protocol, sessions degenerate into "hammer the optimizer harder." The protocol forces *thinking* before computing — which is where wisdom comes from. The 12 stances are dead text without a procedure that invokes them; this is the procedure.

**How to apply:**

- Open every problem branch with steps 1–4 in writing. Don't run code until step 7.
- The `/goal` skill produces the plan; this protocol fills it.
- Each step has a deliverable (a wiki entry, a tracking entry, a code commit).
- If the loop is stuck between any two steps for >2 hours, that's the signal to do step 5 (research) — gap-detect was insufficient.
- Step 9 is mandatory. Without look-back, no compounding.
- Step 10 is mandatory. Failures without articulated why are wasted compute.

**Trigger:** any branch named `feat/<problem-N>-*`, `research/<problem-N>-*`, or `polish/<problem-N>-*`. Plus any time the agent dispatches the council.

See also: [self-improvement-loop](self-improvement-loop.md), [council-dispatch](council-dispatch.md), [ask-the-question-first](ask-the-question-first.md), [triple-verify](triple-verify.md), [wiki/personas/_synthesis.md](../../wiki/personas/_synthesis.md).
