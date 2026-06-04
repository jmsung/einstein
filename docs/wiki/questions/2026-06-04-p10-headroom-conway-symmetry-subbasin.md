---
type: question
author: agent
asked_by: conway
drafted: 2026-06-04
status: open
related_problems: [10]
---

# P10 (Thomson n=282) — Conway: is the icosadeltahedral magic-number config provably optimal, or is there an unsearched symmetry-broken sub-basin?

1. The 282 = T=28 icosadeltahedral assignment forces chiral icosahedral symmetry I (60 rotations) onto the configuration — but is the *true* global minimum known to respect I, or could a lower-symmetry (C₅, C₃, C₂, or fully asymmetric) defect rearrangement of the 12 pentagonal disclinations sit microscopically below the Wales value? Matters because every search we logged warm-started from the symmetric Wales seed; a broken-symmetry basin would never be reached by L-BFGS from that seed, so "18 approaches converged" only certifies the symmetric funnel, not the whole landscape.

2. Caspar–Klug theory admits multiple distinct triangulation classes at a given T (the chirality h≠k vs h=k cases) — for T=28 is the Wales config the only icosadeltahedral *isomer*, or are there inequivalent contact-graph topologies (alternate disclination placements) at the same n whose energies have never been compared? Matters because a competing topology, if it exists, is the only plausible source of a sub-Wales basin and is a one-shot constructive seed to test, not a lottery.

3. Can we fingerprint the arena #1 (AlphaEvolve) and Wales solutions by their pair-distance / Voronoi-coordination histogram to *confirm* they are the same icosadeltahedral isomer rather than merely the same energy to float64 — i.e., is the 20-year incumbent genuinely the I-symmetric magic config, or a coincidentally-tied distinct arrangement? Matters because it decides whether the "skip — frozen" verdict rests on a verified structural identity or only on a scalar coincidence.
