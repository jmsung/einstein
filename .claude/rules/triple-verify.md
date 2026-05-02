# Triple-verify every score

Every score MUST be verified three ways before trusting:

1. **Fast local evaluator** — for the optimization loop. Approximations OK.
2. **Exact / independent reimplementation** — catches numerical bugs, off-by-one, sign errors. Different code path.
3. **Cross-check** — vs a known analytical result, theoretical bound, or different method. Different *kind* of evidence.

If any two disagree, **the score is fake** — debug before proceeding.

**Why:** Local evaluator drift from the arena verifier has caused real damage in this project — P9 (verifier bug, problem hidden), P14 (arena tolerance band exploitable), P17 (strict-tol trap, would-be 500-pt penalty). Single-evaluator results are not trustworthy. Multiple-evaluator agreement is the only safe ground for "this number is real."

This is also the closed loop. Submission to the arena is the *fourth* check, but it's the second-rate signal — slow, binary, doesn't iterate. The triple-verify locally IS the closed loop.

**How to apply:**

- After any optimizer reports a new best score, run check #2 (exact reimplementation) BEFORE updating the tracking log.
- Run check #3 (analytical / different method) before any submission decision. If no analytical bound exists for the problem, use a structurally different optimizer or a higher-precision computation (mpmath at 60 dps).
- For float-precision-critical problems (P5, P6, P11, P14, P17), check #2 = mpmath at sufficient dps (typically 50–80).
- Document the three numbers and the agreement (or disagreement) in `mb/tracking/<problem>/experiment-log.md`.

**Disagreement protocol:**
- Two-way mismatch → bug. Stop. Find it.
- Three-way agreement → score is real. Proceed.
- Three-way disagreement → evaluator definitions diverge. Refer to arena verifier as the ground truth, not just the most-recent code.

**Triggering pattern:** any time the agent is tempted to say "we improved to X" — that statement requires three numbers, not one.

See also: [agent-stance](agent-stance.md) (objective > subjective), [failure-is-a-finding](failure-is-a-finding.md) (verifier-mismatch findings), [axioms](axioms.md) (A1).
