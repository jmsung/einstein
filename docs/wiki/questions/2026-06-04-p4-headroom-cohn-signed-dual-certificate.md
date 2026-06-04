---
type: question
author: agent
asked_by: cohn
drafted: 2026-06-04
status: open
related_problems: [4]
---

# P4 headroom (Cohn) — is there a signed-f LP/SDP dual that lower-bounds C₃ and tells us if 1.4523 is near-optimal?

1. The signed P4 has a *cleaner* Plancherel identity (`(f★f)^ = f̂²`, no |·|² needed) but loses the `∫f = ‖f‖₁` pairing the f≥0 majorant exploits — can we still write a Cohn–Elkies-style dual where a "magic" test measure g with `ĝ ≥ 0` certifies a lower bound on `max(f★f)/(∫f)²`? — A certified lower bound is the only way to know whether OrganonAgent's 1.4523 is essentially the continuous infimum (polish target) or whether there is still real headroom below it (new-basin target).

2. Does the sign-freedom of f turn the constraint geometry into a *two-sided* LP (test functions constrained at both +max and −max lags), making this a signed analog of the Gonçalves lonely-runner / Selberg-majorant LP — and does that LP's optimum value match 1.4523 or sit strictly below it? — If the LP optimum is strictly below 1.4523, a primal construction reaching it exists and we should chase it; if it equals 1.4523, the problem is frozen and we stop.

3. The literature upper bound is C ≤ 1.45810 (Tao 2025) and we sit at 1.45252 — is there a known *lower* bound in the autoconvolution literature (Matolcsi, Cloninger–Steinerberger, Barnard–Steinerberger) that has been adapted to the signed case, or is the signed lower bound genuinely open? — Knowing whether any rigorous floor exists below 1.4523 distinguishes "polish toward a proven wall" from "search an open gap," and changes the whole compute allocation.
