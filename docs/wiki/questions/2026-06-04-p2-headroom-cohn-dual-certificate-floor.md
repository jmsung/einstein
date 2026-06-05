---
type: question
author: agent
asked_by: cohn
drafted: 2026-06-04
status: open
related_problems: [2]
---

# P2 headroom — Cohn: what does the LP/dual lower bound say about how much headroom is left below OrganonAgent?

1. **What is the best dual lower bound on C achievable at n=90000, and how far is OrganonAgent's 1.5028609074 from it?**
   Why it matters: P2 is a min-of-max-over-nonneg problem with a Kolountzakis-Matolcsi LP dual; the dual gives a *certificate floor* below which no construction can go at fixed n. If OrganonAgent is within (say) 1e-8 of the n=90000 LP dual bound, the problem is essentially solved at this resolution and chasing more wins is wasted compute. If the dual bound is well below OrganonAgent, headroom provably exists. A good answer is the dual bound value plus the gap to the current arena #1, framed as "provably exhausted at n=90000" vs "X of headroom remains."

2. **The cutting-plane LP showed strong first-round descent (s*=1.54) from SOTA but was too slow to converge with FOSS solvers at n≥5000. With a warm-start from our v² 90k seed (not the old exp(v) SOTA) and a commercial-grade or GPU LP, does the LP reach s*=1 (fixed point) or s*>1 (escape direction exists)?**
   Why it matters: the experiment log never resolved whether s* converges to exactly 1 (our basin is a true LP fixed point, no escape) or stays >1 (a descent direction exists we couldn't follow). This is *the* unanswered question from Phase B, and warm-starting from the better v² basin rather than the old exp(v) SOTA may change the answer. A good answer is the converged s* value at n≥30000 with the v² warm-start.

3. **Can a magic-function-style dual certificate be built whose Fourier-positivity structure predicts the optimal support, giving a constructive seed rather than an L-BFGS-discovered one?**
   Why it matters: the rank-#1 v² seed was found by a non-deterministic L-BFGS trajectory ("the exact score depends on L-BFGS trajectory") — this is exactly why reconstruction is fragile. A dual certificate that pins the active constraint set would make the seed reproducible by construction. A good answer either sketches the certificate's sign pattern on the 69-cluster support or rules out a clean dual for this asymmetric extremizer.
