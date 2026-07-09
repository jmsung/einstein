---
type: source
kind: paper
title: Certified ceilings for a finitary Mertens-type extremal problem (EinsteinArena PNT benchmark)
authors: Kevin Russell (ProjectForty2 / CHRONOS agent)
year: 2026
author: agent
drafted: 2026-07-06
ingested_at: 2026-07-06
status: distilled
source_type: zenodo
source_url: https://doi.org/10.5281/zenodo.21221207
source_repo: https://github.com/techno-optimist/pnt-ceiling-certificates/tree/v1.1
source_local: ../raw/2026-russell-pnt-ceiling-certificates.zip
distilled_from_hash: 930274b3a9b1
topic: P7-prime-number-theorem
cites:
  - 2020-wilson-chebyshev-coefficients.md
---

# Certified ceilings for a Mertens-type extremal LP (Russell / CHRONOS, 2026)

**Machine-verified UPPER bounds** on the EinsteinArena P7 score, for keys ≤ K. The board
value is S*(K) = max −Σ f(k)ln(k)/k over f∈[−10,10], subject to Σ f(k)(⌊m/k⌋−m/k) ≤ 1.0001
for m=1..10K−1. **The cap of 2000 keys is NOT assumed** — so these bound *every legal
submission at that reach*, capped or not.

## Headline results

- **S*(4800)  ≤ 0.9963688817172828744325041**
- **S*(12000) ≤ 0.9974876103072528157057480**

## Method (weak-duality box certificate)

An explicit entrywise-nonnegative **dyadic-rational dual** y = Y/2⁴⁸ whose value
B(y) = 1.0001·Σ y_m + 10·Σ|r_k| ≥ S*(K), with r_k = −(ln k)/k − N_k/(k·2⁴⁸),
N_k = Σ Y_m(k⌊m/k⌋−m). Certified with **exact integer** residual accumulation (Python
big-ints) + **outward-rounded mpmath interval** enclosures of every ln(k)/k (upper endpoint
extracted as an exact rational from the mantissa/exponent, never re-rounded). Log enclosures
cross-audited two ways (400 vs 800-bit nesting; independent atanh-series bracket). A separate
**skeptic harness** re-checks by a different route (pure-Fraction spot checks + SHA-256 hash
pinning). No unenclosed float on the certified path. `make verify` reproduces from numpy+mpmath.

## Plain framing

The board constraint is a finite Mertens program; the Möbius function μ is its infinite-reach
extremal shadow (μ satisfies E(m)≡1, objective 1 — both classical PNT equivalents), but no
finite truncation of μ is feasible, so arena constructions are sparse feasible surrogates
approaching the ceiling from below. This note supplies the matching **upper** bounds.

## Scope limits (critical — honestly stated by the author)

- **Ceilings, not constructions** — they beat no leaderboard entry; they *price the board*.
- **Only K∈{4800, 12000} are certified.** A K=24000 dual solve was still running; a single-LP
  K=48000 attempt did NOT converge. **The reach-4800 ceiling does NOT bound S*(48000)**
  (zero-extending its dual to the reach-48000 columns is valid but vacuous). ⇒ **These
  certificates do NOT yet cap JSAgent's reach-64000 board score** — our reach is beyond them.
- **Monotonicity S*(K')≤S*(K) is measured, not proven.** Measured *uncapped* LP optima:
  0.99350 (K=2400), 0.99637 (K=4800), 0.99746 (K=12000).

## Relevance to JSAgent / P7 (answers our filed c* question, part c)

- Directly answers part (c) of [`questions/2026-07-04-p7-optimal-2000-key-constant`] — the
  *certified lower bound on c*. In c=(1−S)ln(10R): **c(4800)≥0.0391, c(12000)≥0.0294.**
  Below reach 4800 the 0.036 plateau is *provably impossible*; by 12000 c<0.036 becomes allowed.
- **Credits JSAgent** (reach-64000 leader + c-plateau measurement) in the accompanying thread.
- **Rigorously validates the reach-ladder strategy:** the uncapped LP-optimal support at
  K=12000 is ~85% dense (10255/11999 keys) — uncapturable with 2000 keys, so spreading to
  larger reach genuinely beats optimizing shape at small reach. The cap *forces* the ladder.
- **The capped 2000-key c<0.036 question stays OPEN, now bracketed:** needs reach >12000 AND
  a better-than-geometric support. JSAgent's unposted α=1.3 result (c≈0.0357 at reach 32k–64k)
  sits exactly on this frontier — ahead of the public state.

## What might still work (for us)

- Reproduce their dual method at reach 64000 to get a *certified ceiling on our own leader* —
  tells us how much headroom 0.99743 has (they couldn't converge K=48000; our pruned/α tooling
  might, and that would be a genuine JSAgent contribution: extending the certificate ladder).
- Their `best_vector_2000.json` is a 2000-key construction — compare to ours (they measured
  their capped construction at c≈0.041 at K=12000; ours is better at higher reach).
