---
type: source
kind: paper
title: Existence of extremals for a Fourier restriction inequality on the one-sheeted hyperboloid
authors: Ren'e Quilodr'an
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2207.10587
source_local: ../raw/2022-quilodran-existence-extremals-fourier-restriction.pdf
topic: general-knowledge
cites:
---

# Existence of extremals for a Fourier restriction inequality on the one-sheeted hyperboloid

**Authors:** Ren'e Quilodr'an  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2207.10587

## One-line
Proves that extremizers exist for the endpoint $L^2 \to L^4$ adjoint Fourier restriction inequality on the one-sheeted hyperboloid $\mathbb{H}^3 \subset \mathbb{R}^4$, and that $L^2$-normalized extremizing sequences are precompact modulo symmetries.

## Key claim
For $\mathcal{H}^3 = \{(x,t) \in \mathbb{R}^3 \times \mathbb{R} : t = \sqrt{|x|^2 - 1},\ |x| \geq 1\}$ with Lorentz-invariant measure, the sharp constants satisfy the strict inequalities $\mathbf{H}_4 > (2\pi)^{5/4}$ and $\overline{\mathbf{H}}_4 > (3/2)^{1/4}(2\pi)^{5/4}$ (strictly greater than the corresponding cone constants), and extremizers in $L^2$ exist for both the upper-half and full hyperboloid endpoint inequalities (Theorems 1.2, 1.3).

## Method
Combines (i) the Fanelli–Vega–Visciglia missing-mass criterion (weak limit + a.e. convergence ⇒ strong convergence), (ii) explicit computation of the double convolution $\mu_s * \mu_s$ to prove strict comparison with the cone (ruling out concentration at infinity), (iii) Lions-style concentration-compactness with bilinear/dyadic refinements to kill vanishing and dichotomy, and (iv) "lifting" Tomas–Stein cap refinements from $S^2$ to the hyperboloid. Lorentz boosts $L_t$ rescale large-measure caps into bounded balls.

## Result
Endpoint $p=4$ extremizers exist on both $H^3$ (upper half) and $\mathcal{H}^3$ (full); every normalized extremizing sequence has a subsequence converging in $L^2$ after multiplication by characters $e^{i(x\cdot y + t\sqrt{|y|^2-1})}$ and (for the full hyperboloid) composition with Lorentz transforms. Nonnegative real extremizers exist and are necessarily even: $f(x,t)=f(-x,-t)$. The strict gap vs. the cone constant is the key quantitative input.

## Why it matters here
General background; no direct arena tie. Touches sharp-constant / extremizer existence machinery (concentration-compactness, missing-mass, bilinear refinements) that overlaps in spirit with autocorrelation/uncertainty-style sharp inequalities, but the one-sheeted hyperboloid geometry is not a current arena target.

## Open questions / connections
- Endpoint $p = 10/3$ existence on $\mathbb{H}^3$ and non-endpoint cases in all dimensions $d \geq 2$ remain open (cf. [6,7] for two-sheeted analogue).
- Nonnegativity of all real extremizers, complex↔real relationship, and $C^\infty$ smoothness (proven for $S^2$ in [10,30,31]) not yet established here.
- Decay rate at infinity of extremizers — possible route via Hundertmark–Shao analyticity arguments [19].
- Extends Strichartz [37] and the two-sheeted nonexistence result [33]; contrasts qualitatively with two-sheeted case where extremizers don't exist.

## Key terms
Fourier restriction, adjoint restriction operator, one-sheeted hyperboloid, Strichartz inequality, sharp constants, extremizers, concentration-compactness, Lorentz invariance, Tomas–Stein, bilinear estimates, missing-mass, Klein–Gordon imaginary mass, Quilodrán, Foschi, Carneiro
