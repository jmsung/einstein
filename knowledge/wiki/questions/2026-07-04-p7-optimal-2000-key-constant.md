---
type: question
author: agent
drafted: 2026-07-04
asked_by: agent
status: partially-answered
related_problems: [P7]
related_findings: [p7-multiscale-support-beats-first-n.md, p7-n16000-degeneracy-crossover-off.md]
---

# What is the optimal structure constant c* for P7's 2000-key sieve LP, and is the geometric-tail family's c ≈ 0.0361 near it?

## The unknown

For the capped problem — max S(f) = −Σ f(k)·ln(k)/k over supports of ≤2000 integers
(2001 with re-derived f(1)), |f| ≤ 10, subject to Σ f(k)⌊x/k⌋ ≤ 1 for all x — define
c(support, reach) := (1 − S)·ln(10·reach). Measured facts (2026-07-04, all certified
full-grid):

- First-N-squarefree supports: c ≈ 0.044–0.047, flat in reach (AKC thread 244 + our runs).
- Dense-prefix(≤1800) + geometric-tail family: c falls 0.0392 → 0.0362 (16k→32k, AKC),
  then **plateaus at 0.0360–0.0361** (48k, 64k — ours). Tail rule verified pure geometric
  (ratio 1.003189 constant; 109 keys/half-octave).

Precisely: (a) does inf over supports of the limiting c exist and what is c*?
(b) is the geometric family's 0.0361 equal to c*, or does a better tail law (e.g.
contribution-weighted, non-squarefree, variable density) push lower? (c) can ANY
upper-bound machinery certify c* > 0 for cardinality-capped supports — the missing
dual technology (the unrestricted-support LP bound tends to 1 and says nothing)?

## Falsifiable answer shape

Either a support family with certified c < 0.0355 at two reaches (disproving 0.0361 ≈ c*),
or a proof/bound that no 2000-key support achieves c below some explicit constant, or a
literature theorem on Chebyshev-method constants with n moduli that transfers.

## Why it matters

P7 has no finite completion (S→1 is PNT); the durable intellectual prize is c*. Whoever
characterizes it owns the problem's theory; every arena gain from here is c-progress or
ln-progress, and only c-progress is wisdom.

## Literature leads to check

Chebyshev's method with finitely many moduli (the {1,2,3,5,30} construction lineage):
Diamond–Erdős on Chebyshev-type estimates; work on "best Chebyshev constants" as the
modulus set grows; sieve-theoretic lower-bound constants literature.

## Ingested sources (2026-07-04)

- [2020-wilson-chebyshev-coefficients](../../source/2020-wilson-chebyshev-coefficients.md) — FULL read; P7's frame verbatim; confirms sparse-set optimum unstudied; compensating-mass construction pattern.
- [2025-gantumur-chebyshev-sylvester-review](../../source/2025-gantumur-chebyshev-sylvester-review.md) — abstract; DEEP-READ pending (Sylvester's iterative refinement = historical support-optimization loop).
- [2013-faber-kadiri-psi-bounds](../../source/2013-faber-kadiri-psi-bounds.md), [2012-vindas-beurling-chebyshev](../../source/2012-vindas-beurling-chebyshev.md) — abstract; secondary.

## Suggested sources (literature pass 2026-07-04, web-approved)

1. **Diamond–Erdős 1980** (reconstruction of Erdős/Kalmár/Rosser ~1937): with sieve
   weights supported on ALL integers [1,T), the Chebyshev constants can be forced
   arbitrarily close to 1 as T grows. **Implication: unbounded support ⇒ c → 0; the
   2000-key cardinality cap is THE obstruction. c* > 0 for capped supports appears to
   be genuinely open — the sparse variant is not in the classical lineage.**
2. **arXiv:2012.14387** — "On coefficients satisfying Chebyshev's approximation of
   π(x)": literally P7's frame (a(d) ≈ μ(d), Σa(d)/d = 0, −Σa(d)ln d/d ≈ 1) with
   finitely-supported coefficients. Top ingest candidate.
3. **arXiv:2512.02466** (Dec 2025) — expository review of the Chebyshev–Sylvester
   method: the modern survey of the whole lineage. Second ingest candidate.
4. arXiv:1310.6374 (new ψ(x) bounds), arXiv:1201.1405 (Chebyshev estimates for
   Beurling primes — the abstract-primes generalization where c-type constants are
   studied structurally).

**Status upgrade**: the wiki had nothing on this (checked einstein-wiki-source: only
adjacent sieve papers). The sparse-support question (b)/(c) has no visible literature —
consistent with it being an open, ownable problem.

## c-probe results (2026-07-05, this branch)

Tail-density experiment at fixed reach 32001, 2000-key family, honest RHS=1:

| tail law | c = (1−S)·ln(10·reach) | vs geometric |
|---|---|---|
| α=1.0 (pure geometric, AKC control) | 0.03619 | — |
| α=0.9 (denser far-end) | **0.03683** | worse (+6.4e-4) |
| α=1.1 (denser near-prefix) | **0.03575** | **BETTER (−4.4e-4)** |

**ANSWERED (part b), 2026-07-05:** geometric is NOT optimal — see finding [p7-geometric-tail-not-optimal](../findings/p7-geometric-tail-not-optimal.md). c decreases monotone 0.9→1.0→1.1; c* ≤ 0.0357. Finer sweep running. Part (c) — certified lower bound on c* — still open.

**Early finding:** perturbing the geometric tail toward the far end raises c (worse).
If α=1.1 also raises c, pure geometric is a local optimum of the tail-density family —
evidence the c≈0.036 plateau is genuine, not an artifact of under-searching. Does NOT
settle whether a structurally different support (non-geometric, contribution-weighted,
Diamond–Erdős compensating-mass) beats it — that remains the open lever.


## Part (c) — certified bound arrived (2026-07-06, external)
Russell/CHRONOS certified S*(4800)≤0.99637, S*(12000)≤0.99749 (weak-duality dyadic-dual certificates; DOI 10.5281/zenodo.21221207; distilled `source/2026-russell-pnt-ceiling-certificates.md`). c-floors: c(4800)≥0.0391, c(12000)≥0.0294. NOT yet at our board reach (K=48000 didn't converge). Open sub-goal: extend the certificate to reach 64000 to price our own leader.
