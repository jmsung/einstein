---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P11, P10]
related_techniques: [warm-start-from-leader.md, mpmath-ulp-polish.md]
related_findings: [float64-ceiling.md, frozen-problem-triage.md, p22-d12-construction-survey.md]
cites:
  - ../findings/float64-ceiling.md
  - ../personas/conway.md
  - ../concepts/sphere-packing.md
  - ../concepts/kissing-number.md
  - ../personas/archimedes.md
related_personas: [archimedes.md, conway.md]
---

# Hardin-Sloane spherical codes — canonical reference table

## TL;DR

The **Hardin-Sloane database** is the standard catalog of best-known spherical codes — `n` points on the unit sphere `S^{d−1}` maximizing minimum pairwise distance (or related extremal property). It's the *first place to look* before optimizing any sphere-on-sphere problem. For most arena problems on `S²` (n ≤ ~60), the Hardin-Sloane table is already at the basin's float64 ceiling; the agent's job is to *confirm* the basin and polish at high precision, not re-discover.

## What it is

Hardin and Sloane assembled, over decades of computation, a table of putative-optimal point configurations on the sphere indexed by `(d, n, λ)`:

- **d** — ambient dimension (most entries on `S² ⊂ ℝ³`)
- **n** — number of points
- **λ** — minimum chord (or angular) distance achieved

The data is offered as a reference for researchers and as a competitive benchmark. Each entry includes the actual coordinate list (so you can warm-start, rotate, or polish).

URL: typically accessed via Sloane's NeilSloane.com archive of spherical codes, mirrored at AT&T research labs historically.

## When it applies

- **Tammes-type problems** — `n` points on `S²` maximizing `min_{i≠j} ‖p_i − p_j‖`. P11 Tammes (n=50) is a direct hit.
- **Thomson-related problems** — `n` points on `S²` minimizing Coulomb energy. Hardin-Sloane is one of several references (Wales-Doye Cambridge database is the other; both confirm the same basin for "magic" `n`).
- **Spherical code construction generally** — any problem where the answer is "place n points on a sphere with some extremal property."

Signal that you should query Hardin-Sloane *first*:

- The problem statement involves "place `n` points on a sphere"
- All prior leaderboard agents converge to scores within 1-2 ulps of each other
- The contact graph (set of point pairs at minimum distance) has a specific symmetry — usually a known polyhedron's vertex configuration

## Why it works

Hardin-Sloane configurations are the result of decades of computer search using methods that long predated arena-style optimizers: simulated annealing, basin hopping, hand-tuned gradient descent at high precision, and explicit symmetry-group enumeration. For most `n`, the Hardin-Sloane configuration is *the* configuration; only at the float64 ceiling do top agents differ.

Empirically, in this project:

- P11 Tammes (n=50) — JSAgent rank #2 at 0.513472084680564, exactly at the Hardin-Sloane published value mod ulps. SOTA float64 ceiling proven via mpmath at 80 dps.
- Multi-agent consensus on Tammes-type problems converges to the same contact graph, with rank determined by polish-precision artifacts.

The Hardin-Sloane configuration is not a *construction* in the algebraic sense — it's a numerical record. Beating it requires either (a) finding a different basin (very rare for tabulated `n`), or (b) higher precision in the same basin (the standard arena play).

## Classic examples

| n | configuration | source |
|---|---|---|
| 4 | tetrahedron | trivial; Sloane confirms |
| 6 | octahedron | trivial; Sloane confirms |
| 8 | square antiprism (NOT cube — Tammes ≠ packing) | Hardin-Sloane note: the cube is *not* optimal for Tammes |
| 12 | icosahedron | Tammes 1930, Schütte-van der Waerden 1951 |
| 24 | snub cube vertices (best known; conjectured optimal) | Hardin-Sloane |
| 50 | non-symmetric polyhedron (50 vertices, 102 edges, 12 deg-5 + 36 deg-4) | Hardin-Sloane (P11 SOTA) |

The n=8 case is folklore: the *packing* optimum is the cube, but the *minimum-pairwise-distance* (Tammes) optimum is the square antiprism — twisting one face by 45° gains slightly more separation.

## Related to / distinguished from

- **Cohn-Elkies LP bound** ([`concepts/lp-duality.md`](lp-duality.md)) — LP *upper bound* on packing density; Hardin-Sloane provides *lower bounds* via explicit constructions. The two are complementary; together they bracket the optimum.
- **Conway-Sloane SPLAG** ([`personas/conway.md`](../personas/conway.md)) — the comprehensive sphere-packing reference. Hardin-Sloane is specifically the spherical-codes subset; SPLAG covers lattices, sphere packings in general, and related codes.
- **Packomania** (Specht) — analogous database for *bounded-region packings* (disks in square, rectangle, hexagon). Not for spherical problems.
- **Wales-Doye Cambridge database** — Coulomb-energy spherical configurations. Used alongside Hardin-Sloane for Thomson-type problems.
- **Friedman's packing records** ([`source/blog/friedman-packing-records.md`](../../source/blog/friedman-packing-records.md)) — yet another database, focused on min/max distance ratios in 2D.

## How the agent should use it

When the council dispatch returns a problem with category `spherical_configuration` or `spherical_code`:

1. **Conway persona** ([`personas/conway.md`](../personas/conway.md)) explicitly asks: *"Has Hardin-Sloane already tabulated this spherical code?"* Reach for the table FIRST.
2. If `(d, n)` is in the table, download the configuration → use as warm-start for `slsqp-active-pair-polish` ([`techniques/slsqp-active-pair-polish.md`](../techniques/slsqp-active-pair-polish.md)).
3. Triple-verify ([`triple-verify`](../../.claude/rules/triple-verify.md)) with mpmath at 80 dps to confirm the basin's true ceiling.
4. The score gap between the Hardin-Sloane published value and your float64-polished result is the basin's float64 representation — beating it requires either a new basin (rare) or a deeper polish (common).

## Limits

- **Coverage thins for large d, n** — most of Sloane's table is `d ∈ {2, 3}`. Higher dimensions have sparser coverage.
- **Some entries are old** — early-2000s computer search at then-current precision. A modern mpmath polish on the same configuration sometimes shifts the published value by ulps.
- **Not a proof of optimality** — entries are *putative* (best known). For proven optimality, see ([`concepts/provable-floor-and-frozen-problems.md`](provable-floor-and-frozen-problems.md)) and Cohn-Elkies-style LP duals.

## See also

- [`concepts/sphere-packing.md`](sphere-packing.md) — broader concept
- [`concepts/kissing-number.md`](kissing-number.md) — related extremal problem
- [`concepts/float64-ceiling.md`](float64-ceiling.md) — what the polish converges to
- [`personas/conway.md`](../personas/conway.md) — the persona that reaches for it
- [`techniques/warm-start-from-leader.md`](../techniques/warm-start-from-leader.md) — generic warm-start protocol; Hardin-Sloane is the spherical-codes-specific instance
