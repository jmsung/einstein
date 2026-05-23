---
type: source
kind: paper
title: Symmetry Breaking in Coupled SYK or Tensor Models
authors: Jaewon Kim, I. Klebanov, G. Tarnopolsky, Wenli Zhao
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.02287
source_local: ../raw/2019-kim-symmetry-breaking-coupled-syk.pdf
topic: general-knowledge
cites:
---

# Symmetry Breaking in Coupled SYK or Tensor Models

**Authors:** Jaewon Kim, I. Klebanov, G. Tarnopolsky, Wenli Zhao  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.02287

## One-line
Two coupled SYK (or $O(N)^3$ tensor) models with tetrahedral quartic interaction parameter $\alpha$ exhibit spontaneous breaking of an anti-unitary $\mathbb{Z}_2$ particle-hole symmetry for $-1 \le \alpha < 0$, signaled by a complex scaling dimension of the form $1/2 + if(\alpha)$ on the fermion number operator $Q = i\psi_1^{abc}\psi_2^{abc}$.

## Key claim
For $-1 \le \alpha < 0$ the conformal phase is unstable: the fermion number operator $Q$ acquires a complex scaling dimension $h = 1/2 \pm if(\alpha)$ (with $f$ determined by $f \tanh(\pi f/2) = -3\alpha(1-\alpha)/(1+3\alpha^2)$, peaking at $f(-1) \approx 1.5251$), and in the true low-temperature phase $Q$ acquires a VEV $\langle i\psi_1^I \psi_2^J\rangle = \delta^{IJ} A$, producing a gapped phase via a second-order transition at finite $(\beta J)_{\rm crit}$ (e.g. $\approx 2.87$ for $\alpha = -1$). A duality $\alpha \to (1-\alpha)/(1+3\alpha)$ restricts the model to $-1 \le \alpha \le 1/3$.

## Method
Large-$N$ melonic Schwinger–Dyson equations for two-point functions $G_{11}, G_{12}$; Bethe–Salpeter analysis of $O(N)^3$-invariant bilinears yields four sectors with eigenvalue equations $g_i(h) = 1$ built from the SYK conformal kernel $g_A(h), g_S(h)$. Numerical solution of the finite-temperature SD equations gives the free energy, condensate, and gap; exact diagonalization for $N_{\rm SYK} \le 16$ (resolved into $\mathbb{Z}_4$ charge sectors) cross-checks the gap, ground-state energy, and condensate $\langle 0_+|Q|0_+\rangle$.

## Result
Complex dimension appears only in the antisymmetric-bilinear sector $O_4^{2n}$ (containing $Q$) when $6\alpha(1-\alpha)/(1+3\alpha^2) < 0$; for $0 \le \alpha \le 1/3$ the dimensions are real with $h_+ + h_- = 1$ (two CFTs related by the $Q^2$ double-trace flow, merging/annihilating at $\alpha = 0$). In the broken phase, $G_{11}$ and $G_{12}$ decay exponentially with a common rate equal to the energy gap $E_1 - E_0$, the low-$T$ entropy vanishes (vs $S_0/N = 2c_0$ with $c_0 \approx 0.2324$ in the conformal window), and ED extrapolations give $E_0/N_{\rm SYK} \approx -0.283$ at $\alpha=-1$ and $-0.179$ at $\alpha=-0.5$, matching the SD curve. The $\alpha = -1$ bipartite point has an exact $E \to -E$ spectrum symmetry and a counted number of $E=0$ states per $\mathbb{Z}_4$ sector given by an explicit binomial alternating sum.

## Why it matters here
General background; no direct arena tie — this is a hep-th paper on coupled SYK/tensor large-$N$ dynamics, not on sphere packing, autocorrelation, or any of the 23 arena problems. The only transferable idea is methodological: a complex scaling dimension $d/2 + if$ in a large-$N$ system is a diagnostic of instability that resolves by an order-parameter VEV — a pattern that could be cited if einstein ever encounters a large-$N$/conformal-bootstrap-style formulation.

## Open questions / connections
- Critical exponents of the second-order transition at $(\beta J)_{\rm crit}(\alpha)$ — explicitly deferred to future work.
- Conjecture proposed: any large-$N$ single-trace operator with complex dimension $d/2 + if$ acquires a VEV in the true low-$T$ phase. Verifying this beyond SYK/tensor settings is open.
- Holographic interpretation: is the gapped $-1 \le \alpha < 0$ phase dual to a traversable wormhole (à la Maldacena–Qi, Gao–Jafferis–Wall), now with spontaneous rather than explicit $\mathbb{Z}_2$ breaking?
- Extension to the $M$-site SYK chain (3.4) generalizing Gu–Qi–Stanford with tied couplings.

## Key terms
SYK model, tensor model, $O(N)^3$ symmetry, melonic diagrams, Schwinger-Dyson equations, complex scaling dimension, Breitenlohner-Freedman bound, particle-hole symmetry, spontaneous symmetry breaking, bipartite tensor model, traversable wormhole, Maldacena-Qi, large-$N$ duality, Bethe-Salpeter kernel, Kitaev, Klebanov-Tarnopolsky
