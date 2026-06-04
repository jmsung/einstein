---
type: question
author: agent
asked_by: razborov
drafted: 2026-06-04
status: open
related_problems: [12]
---

# P12 headroom (Razborov lens): pin the grid-sampling drift with a certificate, not a denser grid

Razborov's instinct: stop guessing arena's sampling — turn "is our score == arena's score" into a checkable bound. The drift (1.2809320520721 local vs 1.2809320527987977 arena, ~7.3e-10) is currently treated as opaque sampling noise; that opacity is exactly what blocks the submission gate.

1. Is arena's N actually 1,000,000 uniform k-th roots starting at k=0, or does the +7.3e-10 (always *above* our value, per the drift table) prove arena uses a strictly finer/offset grid — i.e. can we recover arena's exact (N, phase, k-range) by minimizing |arena_score − grid_max(N,φ)| over a small probe set, turning a mystery into three integers?
2. For a fixed ±1 polynomial of degree 69, what is the provable Bernstein/Markov upper bound on |max_{|z|=1}|p(z)| − max over the 1M-grid| (a function of degree and grid spacing), and is that bound already below minImprovement (1e-7) so that *any* genuine basin improvement of ≥1e-7 survives the drift regardless of which grid arena uses?
3. Can the continuous sup be certified to <1e-9 by FFT zero-padding to 2^k ≥ 8·N plus one Newton step per local peak (a finite, machine-checkable witness set of ~70 peaks), making the grid quantity obsolete as the authoritative score and the drift a non-issue by construction?
