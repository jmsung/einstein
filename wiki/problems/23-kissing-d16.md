---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 23
arena_url: https://einsteinarena.com/problems/kissing-d16
status: open
score_current: 2.0
tier: C
concepts_invoked: [kissing-number.md, sphere-packing.md, first-order-link-tangent-test.md]
techniques_used: [first-order-link-tangent-test.md]
findings_produced: []
private_tracking: ../../mb/tracking/problem-23-kissing-d16/
---

# Problem 23 — Kissing Number in Dimension 16 (n=4321)

## Statement
Place 4321 unit vectors in R^16; minimize the hinge-overlap score = sum_{i<j} max(0, 2 - ||c_i - c_j||). Score 0 would prove kappa(16) >= 4321.

## Approach
kappa(16) = 4320 is *proven* (Levenshtein 1979 plus Odlyzko-Sloane 1979 LP bound; achieved by Barnes-Wall BW_16 = Lambda_16). Hence at least one pair must overlap and score 0 is impossible. The SOTA construction uses the BW_16 lattice's 4320 minimal vectors plus one exact duplicate, giving score = 2.0. The link of any BW_16 minimal vector has 280 neighbors at 60 degrees; first-order link analysis applies. Methods explored: filler-only L-BFGS, link-projection SDP/LP relaxation. Submission would tie SOTA at score 2.0 (no points).

## Result
- **Score**: 2.0 (theoretical floor for any (4320 + duplicate) construction)
- **Rank**: not yet submitted
- **Date**: as of 2026-05-02
- **Status**: open; structural confirmation only

## Wisdom hook
Proven kissing numbers (kappa(16) = 4320 via Levenshtein) reduce the problem to structural analysis — focus on confirming the known cap, not beating it.

## Concepts invoked
- [kissing-number.md](../concepts/kissing-number.md)
- [sphere-packing.md](../concepts/sphere-packing.md)
- [first-order-link-tangent-test.md](../concepts/first-order-link-tangent-test.md)

## Techniques used
- [first-order-link-tangent-test.md](../techniques/first-order-link-tangent-test.md)

## Findings
None yet.

## References
- Levenshtein (1979), kissing-number LP bound for d=16.
- Odlyzko-Sloane (1979), independent proof.
- Barnes-Wall lattice BW_16 = Lambda_16.
- Conway and Sloane, "Sphere Packings, Lattices and Groups."

## Private tracking
For owner's reference: `mb/tracking/problem-23-kissing-d16/` contains the link-projection survey and the BW_16 SOTA archive. Not part of the public artifact.
