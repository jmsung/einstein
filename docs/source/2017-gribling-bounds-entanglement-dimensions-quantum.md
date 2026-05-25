---
type: source
kind: paper
title: Bounds on entanglement dimensions and quantum graph parameters via noncommutative polynomial optimization
authors: S. Gribling, David de Laat, M. Laurent
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.09696
source_local: ../raw/2017-gribling-bounds-entanglement-dimensions-quantum.pdf
topic: general-knowledge
cites:
---

# Bounds on entanglement dimensions and quantum graph parameters via noncommutative polynomial optimization

**Authors:** S. Gribling, David de Laat, M. Laurent  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.09696

## One-line
Constructs SDP hierarchies, via tracial noncommutative polynomial optimization, that lower-bound the minimal Hilbert-space dimension realizing a bipartite quantum correlation and that bound the quantum chromatic / stability numbers of a graph.

## Key claim
The tracial-moment SDP hierarchy $\{\xi^r_q(P)\}$ converges (under a flatness condition) to a new parameter $\xi^*_q(P) = A_{qc}(P)$, the *minimal average entanglement dimension* — the convex-hull analogue of $D_q(P)$ when shared randomness is free — and analogous hierarchies $\{\gamma^r_{\text{col}}\}, \{\gamma^r_{\text{stab}}\}$ converge to $\chi_{qc}(G), \alpha_{qc}(G)$ and unify the projective rank $\xi_f(G)$ and tracial rank $\xi_{\text{tr}}(G)$ within one framework.

## Method
Tracial polynomial optimization: optimize a linear functional $L$ on noncommutative polynomials in degree $\le 2r$ that models a non-normalized trace $L(1) \approx \dim$, subject to positivity, tracial, and ideal constraints encoding POVM / projector / synchronicity relations. Truncating degree gives finite SDPs; Artin–Wedderburn block decomposition handles the commuting-vs-tensor reduction; Curto–Fialkow-style flat extensions give finite convergence certificates.

## Result
Defines $A_q(P) = \inf \sum_i \lambda_i D_q(P_i)$ over convex decompositions and proves $A_q = A_{qc}$, $A_q(P)=1 \iff P \in C_{\text{loc}}$, and $A_q(P_i) \to \infty$ on non-closure instances. Establishes the chain $\vartheta(G) = \xi^1_{\text{col}}(G) \le \xi^r_{\text{col}}(G) \le \xi_{\text{tr}}(G) \le \xi_f(G) \le \chi_q(G)$ and the duality $\xi^r_{\text{stab}}(G)\,\xi^r_{\text{col}}(G) \ge |V|$ with equality for vertex-transitive $G$; recovers Paulsen et al.'s $\xi_{\text{SDP}} \le \xi^2_{\text{col}}$ and $\xi^\infty_{\text{col}}(C_{2n+1}) = (2n+1)/n$.

## Why it matters here
General background; no direct arena tie. The tracial-SDP machinery for bounding minimum factorization rank / dimension is methodologically adjacent to LP/SDP duality techniques used on packing-style arena problems, but the quantum-correlation domain is outside the current 23-problem set.

## Open questions / connections
- Whether $\xi^\infty_q(P) = \xi^*_q(P)$ always — equivalent to Connes' embedding conjecture variant.
- Whether $\chi_q(G) = \chi_{qc}(G)$ and $\alpha_q(G) = \alpha_{qc}(G)$ separations exist (Slofstra-style non-closure for parameters).
- Whether the supremum in $\xi^*_{\text{stab}}(G) = \alpha_p(G)$ is attained (open in [45]); blocks extending Props. 3.10–3.11 to $r=*$.
- Extends Lasserre / Parrilo SOS hierarchies (Lasserre 2001, Parrilo 2000) and the Navascués–Pironio–Acín NPA hierarchy to dimension-restricted / trace-minimizing settings.

## Key terms
tracial noncommutative polynomial optimization, Lasserre hierarchy, NPA hierarchy, semidefinite programming, completely positive semidefinite rank, projective rank, tracial rank, quantum chromatic number, quantum stability number, Connes embedding conjecture, Tsirelson problem, flat extension, Artin–Wedderburn, theta number, Bell inequalities, synchronous correlations
