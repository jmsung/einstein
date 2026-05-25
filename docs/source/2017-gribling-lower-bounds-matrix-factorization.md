---
type: source
kind: paper
title: Lower Bounds on Matrix Factorization Ranks via Noncommutative Polynomial Optimization
authors: S. Gribling, David de Laat, M. Laurent
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.01573
source_local: ../raw/2017-gribling-lower-bounds-matrix-factorization.pdf
topic: general-knowledge
cites:
---

# Lower Bounds on Matrix Factorization Ranks via Noncommutative Polynomial Optimization

**Authors:** S. Gribling, David de Laat, M. Laurent  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.01573

## One-line
Builds SDP hierarchies that lower-bound four matrix factorization ranks (nonnegative, psd, completely positive, completely positive semidefinite) using (tracial) noncommutative polynomial optimization.

## Key claim
For each rank $r \in \{\text{rank}_+, \text{psd-rank}, \text{cp-rank}, \text{cpsd-rank}\}$ there is a monotone SDP hierarchy $\xi_1^r(A) \le \xi_2^r(A) \le \cdots \le r(A)$ with controlled convergence: $\xi_t^+(A) \to \tau^+(A)$ (Fawzi–Parrilo bound) as $t\to\infty$, and a strengthened $\xi_t^{cp}$ converges to $\tau^{cp}(A)-\varepsilon$ via finitely many extra linear constraints; the new $\xi_1^{cpsd}$ dominates the prior analytic cpsd-rank bound of Prakash et al.

## Method
Express a minimum-rank factorization $A=(\langle X_i,X_j\rangle)$ as a trace-evaluation linear functional $L_X(p)=\mathrm{Re}\,\mathrm{Tr}(p(X))$ on (non)commutative polynomials, then minimize $L(1)$ over symmetric tracial positive functionals satisfying $L(x_ix_j)=A_{ij}$ and localizing constraints $\sqrt{A_{ii}}\,x_i - x_i^2 \succeq 0$ (which ensure Archimedean property). Truncation at degree $2t$ yields an SDP relaxation; convergence and tightness arguments use the moment side (Hankel matrix flatness, GNS-type C*-algebra reconstructions, Curto–Fialkow / Burgdorf–Klep / Klep–Povh extension theorems).

## Result
Defines $\xi_t^{cpsd}, \xi_t^{cp}, \xi_t^+, \xi_t^{psd}$ as semidefinite programs of growing size, each a valid lower bound on its rank. Shows $\xi_1^{cpsd}\ge$ the analytic cpsd lower bound from [62], and exhibits a small matrix where a strengthening of $\xi_2^{cpsd}$ strictly exceeds both $\text{rank}(A)$ and that analytic bound. Numerical experiments (Mosek via CVX/Julia) show $\xi_3^+(A)$ improves on Fawzi–Parrilo's $\tau^{+sos}(A)$ on small literature matrices.

## Why it matters here
General background; no direct arena tie. The SDP-on-moments + flatness machinery is the same toolkit that powers Lasserre/Parrilo hierarchies relevant to extremal-combinatorics flag SDPs (P1-style sphere-packing bounds) and quantum-correlation problems, so it informs `concepts/sdp-lasserre-hierarchy` and `findings/sdp-relaxation-uselessness` as a counterpoint (here SDP hierarchies are actually used productively for rank lower bounds).

## Open questions / connections
- Can $\xi_t^{cpsd}(A)$ ever exceed the matrix size $n$? (No small example known; possibly because matrices with large cpsd-rank are hard to construct.)
- Is the cpsd-rank computable at all? (Open; $\mathrm{CS}^n_+$ is non-closed for $n\ge 10$.)
- Extends Fawzi–Parrilo [27,28] from atomic ranks ($\text{rank}_+$, cp-rank) to non-atomic ones (psd-rank, cpsd-rank); related to Connes' embedding conjecture via $f^{tr}_{II_1}=f^{tr}_*$.

## Key terms
nonnegative rank, positive semidefinite rank, completely positive rank, completely positive semidefinite rank, noncommutative polynomial optimization, Lasserre hierarchy, Parrilo SOS, tracial moment problem, flat extension, Curto-Fialkow, Archimedean quadratic module, slack matrix, extension complexity, Fawzi-Parrilo, Putinar Positivstellensatz, C*-algebra tracial state
