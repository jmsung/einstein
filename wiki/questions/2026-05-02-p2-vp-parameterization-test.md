---
type: question
author: agent
drafted: 2026-05-02
asked_by: research/p2-peak-locking
status: open
related_problems: [P2, P3, P4]
related_concepts: [parameterization-selection.md]
related_findings: [p2-peak-locking-hessian-mechanism.md, equioscillation-escape.md]
cites:
  - ../findings/p2-peak-locking-hessian-mechanism.md
---

# Does $f = v^p$ for $p > 2$ peak-lock like $\exp(v)$, not unlock like $v^2$?

## Setup

The Hessian-mechanism finding [p2-peak-locking-hessian-mechanism](../findings/p2-peak-locking-hessian-mechanism.md) attributes the peak-locking / escape distinction to $\varphi''(v_i)$ at dead cells $f_i = 0$:

| $\varphi$ | $\varphi'(0)$ | $\varphi''(0)$ | Dead-cell Hessian on $S$ |
|---|---|---|---|
| $\exp(v)$ | $0$ (asymptotic) | $0$ | rank-deficient — peak-locks |
| $v^2$ | $0$ | $2$ | full rank — escapes |
| $v^3$ | $0$ | $0$ | rank-deficient (predicted — peak-locks?) |
| $v^4$ | $0$ | $0$ | rank-deficient (predicted — peak-locks?) |

If the sufficient-condition hypothesis is right, $v^p$ for $p \in \{3, 4, 5, \ldots\}$ should peak-lock similarly to $\exp(v)$, not unlock like $v^2$. Only $p = 2$ is special — it's the smallest power for which $f$ is non-negative *and* $\varphi''(0) \neq 0$.

(Note: $f = v$ with $v \ge 0$ is the natural box-constrained reformulation; that's $p = 1$, with $\varphi'(0) = 1$ and $\varphi''(0) = 0$. It's a different beast — first-order non-vanishing, no Hessian-side mechanism, but L-BFGS-B's hard bounds re-introduce a peak-locking equivalent.)

## The question

Run the same small-$n$ verification (n=80, smooth-max β=200, sparse seed) under each of $\varphi \in \{v^2, v^3, v^4, v^6\}$. Count near-zero Hessian eigenvalues at the v-critical point and check the basin value.

Expected:

- $v^2$: 0 near-zero eigs, escape basin (already verified — see finding)
- $v^3, v^4, v^6$: ~ (#dead cells) near-zero eigs, peak-lock basin near `exp(v)`

If observed, this isolates the mechanism to *exactly* $\varphi''(0) \neq 0$, ruling out the alternative hypothesis that "any reparameterization other than `exp` works" or "any polynomial other than linear works."

## What "answered" looks like

A small extension to `scripts/first_autocorrelation/peak_locking_hessian.py` running the four parameterizations side-by-side, plus a one-line update to the finding's table. Either:

- The prediction holds: stronger evidence that $\varphi''(0) \neq 0$ is the actual mechanism — promote a sharpened version of the sufficient condition.
- The prediction fails (e.g., $v^3$ also escapes): the Hessian-rank story is incomplete; investigate why $v^3$ behaves differently despite $\varphi''(0) = 0$.

## Why this matters

Without this test, the existing Hessian-mechanism finding has a single binary data point (`exp` peak-locks, `v²` escapes). The $v^p$ sweep turns it into a parameterized falsifiable prediction — the mark of a real mechanism vs. a coincidence.

## Cost

Same script, four runs, ~30 seconds local CPU. Trivial. The reason it's filed as a question rather than executed in the same cycle: scope discipline. The current branch's deliverable is the *mechanism*; this is the falsification test, naturally a follow-up.

## Status

**Open.** Easy to answer — should be the first thing the next cycle on this branch (or a follow-up) does.
