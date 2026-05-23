---
type: source
kind: paper
title: STOLARSKY'S INVARIANCE PRINCIPLE FOR FINITE METRIC SPACES
authors: A. Barg
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.12995
source_local: ../raw/2020-barg-stolarsky-invariance-principle-finite.pdf
topic: general-knowledge
cites:
---

# STOLARSKY'S INVARIANCE PRINCIPLE FOR FINITE METRIC SPACES

**Authors:** A. Barg  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.12995

## One-line
Establishes a Stolarsky-type invariance principle for finite metric spaces — quadratic discrepancy of a subset equals the gap between the global and subset averages of an explicit distance-kernel $\lambda(x,y)$ — and works out the Hamming-space case in full, including LP bounds and discrepancy-minimizing code families.

## Key claim
For $Z \subset X$ finite metric, $D_{L_2}(Z)^2 = \langle \lambda \rangle_X - \langle \lambda \rangle_Z$ with $\lambda(x,y) = \tfrac{1}{2}\sum_u |d(x,u)-d(y,u)|$. In the Hamming space $\{0,1\}^n$ with $d(x,y)=w$: $\lambda(w) = 2^{n-w} w \binom{w-1}{\lfloor w/2\rfloor - 1}$, the average is $\Lambda_n = \tfrac{n}{2^{n+1}}\binom{2n}{n}$, and for extremal discrepancy $c\sqrt{n}\,\sqrt{2^n/N} \le D_{L_2}(n,N) \le C\sqrt{n}\,\sqrt{2^n/N}$. **All binary perfect codes (repetition, Hamming, Golay$_{23}$) are discrepancy-minimizers.**

## Method
Geometric / combinatorial expansion of the squared-discrepancy sum into ball-intersection volumes, reduced to the radial kernel $\lambda$ via the identity $|B(x,t)\cap B(y,t)| = |X|(n+1)-\sum_z d(z,u)-\tfrac{1}{2}\sum_z|d(z,x)-d(z,y)|$. Krawtchouk-polynomial Fourier expansion of $\lambda$ on $\{0,1\}^n$ gives explicit coefficients $\lambda_k = -2^{-n}\sum_t K_t^{(n-1)}(k-1)^2$, with $\lambda$ negative-definite (constant term excluded). Delsarte-style linear programming on the dual distance distribution $A_k^\perp$ — using $\lambda_k \ge 0$ for $k\ge 1$ ($\mu$ positive-definite) — yields universal lower bounds; matching constructions confirm optimality.

## Result
- Closed form Hamming-code discrepancy: $D_{L_2}(H_m)^2 = \tfrac{n}{2^n}\binom{n-1}{(n-1)/2} \approx n/(4\pi)$ for $n=2^m-1$.
- Random-code expectation: $E[D_{L_2}(Z)^2] = \tfrac{n}{N 2^{n+1}}\binom{2n}{n}(1-\alpha_n/n) \sim \tfrac{n}{\pi}\cdot 2^{n-1}/N$.
- LP bounds (Cor. 5.3): e.g. $D_{L_2}(n,N)^2 \ge \Lambda_n - (2^n/N - 1)|\lambda_{(n+1)/2}|$ for $n$ odd — tight for Hamming, Golay, shortened-Hamming, certain BCH and quadratic-residue codes.
- Extension scaling: $D_{L_2}(Z_{ex})^2 = 2 D_{L_2}(Z)^2 + \tfrac{1}{2^{n+1}}\binom{2n}{n}$.
- Weighted ($D_{L_2}^G$), Krawtchouk-expansion, and metric-association-scheme generalizations all proved.

## Why it matters here
Direct ammunition for Hamming-space / coding-theoretic Einstein Arena problems: gives an LP-bound machinery on a *non-completely-monotonic* potential, where the universal Cohn-Kumar / Boyvalenkov-Dragnev bounds don't apply — relevant any time the agent considers binary codes, autocorrelation-style energy functionals, or Sidon-like distance-distribution objectives. Also a clean example of "perfect codes = energy minimizers" and of LP-feasibility-via-Krawtchouk-coefficient-sign-control, a template reusable across discrete extremal problems.

## Open questions / connections
- Extensions to nonbinary Hamming and Johnson schemes left open (Johnson likely reveals new combinatorial structure).
- $L_p$ discrepancies in Hamming space (started in Barg-Skriganov 2021 follow-up) — bounds for $p\ne 2$.
- Classification of discrepancy-minimizing codes beyond perfect codes; relation to sum-of-distances minimizers (Ahlswede-Katona, Fu-Wei-Yeung).
- Discrepancy w.r.t. hemispheres / other geometric shapes (not metric balls); $t$-designs / orthogonal arrays in Hamming space do *not* automatically have small discrepancy — unlike the spherical case.

## Key terms
Stolarsky invariance principle, quadratic discrepancy, Hamming space, Krawtchouk polynomials, Delsarte linear programming, distance distribution, dual distance distribution, MacWilliams identity, perfect codes, Hamming code, Golay code, energy minimization, association scheme, central binomial coefficient, radial kernel, Barg, Skriganov
