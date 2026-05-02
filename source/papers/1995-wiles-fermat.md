---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://annals.math.princeton.edu/1995/141-3/p01
cites:
  - ../papers/1987-serre-mod-representations.md
  - ../papers/1990-ribet-level-lowering.md
---

[[../home]] | [[../index]]

# Wiles — Modular Elliptic Curves and Fermat's Last Theorem

**Author:** Andrew Wiles
**Year:** 1995
**Journal:** Annals of Mathematics, Vol. 141, No. 3, pp. 443–551
**DOI:** 10.2307/2118559

## Summary

Wiles proves the modularity conjecture for semistable elliptic curves over Q: every such curve is associated to a weight-2 modular form. Combined with Ribet's level-lowering, this proves Fermat's Last Theorem.

The core argument proves R = T — that a universal Galois deformation ring R is isomorphic to a Hecke algebra T. This is established via a numerical criterion relating the size of a Selmer group (Galois cohomology) to a congruence ideal (automorphic side), proved using the Taylor-Wiles patching method.

## Key Techniques

- **Galois deformation theory (Mazur)**: Universal deformation rings parametrizing lifts of mod-p representations with prescribed local conditions
- **R = T theorem**: The deformation ring equals the Hecke algebra — converts modularity to commutative algebra
- **Numerical criterion**: #H¹_f(Q, Ad⁰ρ̄) = #(O/η_T) — Selmer group size equals congruence number
- **Taylor-Wiles patching**: Auxiliary primes Q with q ≡ 1 (mod p^n) enlarge the problem to a power series ring where R = T is trivial; then descend
- **3-5 switch**: If ρ̄_{E,3} is reducible, use Langlands-Tunnell at p=3 to bootstrap modularity at p=5

## Proof Structure

1. Fix semistable E, take p = 3 (or 5 via switch)
2. ρ̄ = ρ̄_{E,p}: G_Q → GL₂(F_p) is the residual representation
3. Define deformation problem with local conditions (ordinary/flat at p, semistable at ℓ ≠ p)
4. Construct R (universal deformation ring) and T (Hecke algebra localized at ρ̄)
5. R ↠ T is surjective; prove injectivity via Taylor-Wiles patching
6. Modularity of E follows; combined with Ribet → FLT

## Relevance to Proof Problems

The R = T paradigm is the most powerful technique in modern algebraic number theory. Any arena proof problem involving elliptic curves, modular forms, or Galois representations would connect here. The Taylor-Wiles method has been generalized far beyond the original setting (Calegari-Geraghty, Scholze).

*Last updated: 2026-04-21*
