---
type: question
author: agent
asked_by: hilbert
drafted: 2026-06-04
status: open
related_problems: [3]
---

# Hilbert — P3 headroom: the right submission-safety axiom and the Rayleigh-quotient frame

The acute danger now that auto-submit is armed: a high-res seed makes triple-verify report
a false record (all three checks at 1.6M agree on 0.9627 and are all wrong about the arena).
I want the cleanest statement of the safety condition and the cleanest frame for the optimum.

1. **What is the minimal cross-resolution agreement axiom that makes a P3 submission safe —
   precisely, which invariant must hold between C2(local n) and C2(100k) for the same f
   before gate 2 may pass?** Why it matters: gate 2 (triple-verify) is currently
   single-resolution and would mis-fire on this family; the fix is one clean predicate, not a
   patch. A good answer is a stated condition of the form "submit only if |C2(n_local) −
   C2(100k_resample)| < ε via the validated anti-alias kernel" with ε derived from the
   Simpson O(h²) term, ready to drop into `triple_verify/problems/p03`.

2. **Written as a Rayleigh quotient ⟨T f★f, f★f⟩ / (normalisers), is C2 an eigenvalue of a
   known operator, and is its extremizer an eigenfunction (smooth, resolution-stable) or a
   boundary/corner optimum on the non-negativity cone (sparse, resolution-fragile)?**
   Why it matters: an interior eigenfunction optimum downsamples cleanly; a cone-boundary
   optimum is exactly the alias-fragile sparse-block case — this single distinction predicts
   whether the headroom is submittable. A good answer classifies the optimum type with the
   operator written explicitly.

3. **Which classical inequality (Young's convolution, Hardy–Hilbert) gives the tightest
   resolution-independent bracket on C2, and does the bracket width shrink fast enough at
   n=100k to certify a sub-1e-4 improvement?** Why it matters: a resolution-independent
   bracket converts the fragile high-res number into a statement that survives to the arena
   grid. A good answer is the inequality, the resulting [lower, upper] bracket on C2(100k),
   and whether 0.9627433 lies inside it.
