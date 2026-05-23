---
type: source
kind: paper
title: "The Tensor Harish-Chandra–Itzykson–Zuber Integral II: Detecting Entanglement in Large Quantum Systems"
authors: B. Collins, R. Gurau, L. Lionni
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2201.12778
source_local: ../raw/2022-collins-tensor-harish-chandra-itzykson-zuber.pdf
topic: general-knowledge
cites:
---

# The Tensor Harish-Chandra–Itzykson–Zuber Integral II: Detecting Entanglement in Large Quantum Systems

**Authors:** B. Collins, R. Gurau, L. Lionni  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2201.12778

## One-line
Large-$N$ asymptotic analysis of the tensor HCIZ integral $\int dU\, e^{t\,\mathrm{Tr}(AUBU^*)}$ over local unitaries $U=U^{(1)}\otimes\cdots\otimes U^{(D)}$, classifying its cumulant regimes as a function of how trace-invariants of the external tensors scale with $N$.

## Key claim
For a two-parameter scaling ansatz $\mathrm{Tr}_\tau(B)\sim N^{\beta\sum_c \#(\tau_c)+\epsilon\sum_{c_1<c_2}\#(\tau_{c_1}\tau_{c_2}^{-1})}\mathrm{tr}_\tau(b)$, the cumulants $C_n$ admit a $1/N$ expansion whose leading-order combinatorics partitions the $(\beta,\epsilon)$-plane into eight distinct regimes (Theorems 6, 7); in the "entangled" regime $V$ ($0\le\beta<\min\{1/D,\epsilon\}$), $\lim_N N^{-\beta D}C_n(N^{D-\frac{D(D-1)\epsilon}{2}}\mathrm{Tr}(AUBU^*))=(n-1)!\,\mathrm{tr}(a^n)\mathrm{tr}(b^n)$.

## Method
Combinatorial analysis of cumulant expansions from the companion paper [3], representing pairs $(\sigma,\tau)\in S_n^D\times S_n^D$ as colored bipartite graphs and tracking the scaling exponent $s(\sigma,\tau)=\sum_c|\Pi(\sigma_c\tau_c^{-1})|-2|\Pi(\sigma,\tau)|+2$. Leading-order graphs are characterized via non-negative invariants (genus $g(\sigma_c,\tau_c)$, melonic degree $\omega$, $(D+1)$-melonicity, $\Delta$, $l_\tau$); when $(\sigma,\tau)$ is transitive, $f[\sigma,\tau]$ reduces to a product of $D$ Möbius functions on non-crossing partitions.

## Result
The $(\beta,\epsilon)$ phase diagram contains: microscopic ($\beta=\epsilon=0$, all connected $\sigma$), mesoscopic separable (connected $(D+1)$-melonic $\sigma=\tau$), macroscopic separable ($\beta=1-\epsilon(D-1)>1/D$, $\tau\preceq\sigma$), macroscopic boundary ($\beta=\epsilon=1/D$, proliferating), entangled ($0\le\beta<\min\{1/D,\epsilon\}$ where all $\sigma_c,\tau_c$ collapse to a single $n$-cycle), and hyper-macroscopic regimes where $\tau_c=\mathrm{id}$. Cumulants — unlike moments, which are universal — discriminate among scalings; the line $\epsilon=\beta<1/D$ is the entanglement-detection threshold. Conjecture: $\beta+\epsilon(D-1)=1$ saturates degrees of freedom; $\beta=0,\epsilon=1/(D-1)$ corresponds to maximally entangled (asymptotically pure) states.

## Why it matters here
General background; no direct arena tie — this is multipartite-quantum-entanglement / random-matrix asymptotics, not optimization on the 23 Einstein Arena problems (sphere packing, autocorrelation, etc.). The graph-genus / non-crossing-partition / Möbius-function combinatorial machinery has tangential overlap with free-probability tools that occasionally appear in extremal-combinatorics or SDP-flag-algebra contexts.

## Open questions / connections
- Conjecture (Sec. 3.1.3, Sec. 3.5): states with $\beta+\epsilon(D-1)=1$ saturate the degrees-of-freedom bound; $\beta=0,\epsilon=1/(D-1)$ characterizes maximally entangled states — proved only in confirmatory examples.
- Conjecture in Sec. 5: any connected $(\sigma,\tau)$ with $\Pi(\sigma)=1$, $\tau\preceq\sigma$, $l_\tau(\sigma,\tau)=\omega(\tau)=0$ must have $\omega(\sigma)=0$ (melonic) — would make the symmetric S-I regime strictly richer than A-microscopic I.
- Extends companion paper [3] (Weingarten calculus, monotone Hurwitz numbers); connects to randomized-measurement entanglement criteria [10–14] and PPT-criterion limitations.

## Key terms
Harish-Chandra-Itzykson-Zuber integral, tensor HCIZ, multipartite entanglement, local unitary invariance, density matrix, cumulant expansion, large-N asymptotics, Weingarten calculus, monotone Hurwitz numbers, melonic graphs, non-crossing partitions, Möbius function, randomized local measurements, separable vs entangled states
