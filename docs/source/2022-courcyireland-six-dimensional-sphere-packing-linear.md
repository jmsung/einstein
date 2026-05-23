---
type: source
kind: paper
title: Six-dimensional sphere packing and linear programming
authors: M. D. Courcy-Ireland, M. Dostert, M. Viazovska
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2211.09044
source_local: ../raw/2022-courcyireland-six-dimensional-sphere-packing-linear.pdf
topic: general-knowledge
cites:
---

# Six-dimensional sphere packing and linear programming

**Authors:** M. D. Courcy-Ireland, M. Dostert, M. Viazovska  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2211.09044

## One-line
Proves the Cohn–Elkies LP bound for sphere packing is *not* sharp in dimension 6 by constructing a dual measure of impossibly high "fake-packing" density.

## Key claim
The LP center-density bound in $\mathbb{R}^6$ is at least $0.0795223$ (density $\geq 0.410948$), strictly above the Cohn–de Laat–Salmon SDP upper bound $0.410304$ — so no actual packing can saturate the LP bound. Adds D=6 to the list of provably non-sharp dimensions (joining 3, 4, 5, 12, 16).

## Method
Use LP weak duality (Theorem 1.5): exhibit a measure $\mu = \delta_0 + \nu$ with $\nu \geq 0$ supported on $\{|x| \geq r\}$ and $\hat\mu \geq c\delta_0$, giving LP bound $\geq c(r/2)^D$. Following Cohn–Triantafillou, take $\mu = \sum a_n \delta_{\sqrt n}$ where $a_n$ are Fourier coefficients of a modular form $g$; extend their construction to **odd weight** $k=3$ with **non-trivial quadratic characters** $\chi_3, \chi_4$, working in the 44-dimensional space $M_3(\Gamma_0(48),\chi_3) \oplus M_3(\Gamma_0(48),\chi_4)$. Solve a finite LP over coefficients in $\mathbb{Q}(\sqrt 3)$; verify positivity of $a_n, b_n$ for all $n$ by splitting Eisenstein (grows as $\varepsilon n^2$) vs cuspidal (bounded by $Cn\sigma_0(n)$ via Deligne).

## Result
Exact lower bound is a quadratic irrational $\alpha + \beta\sqrt 3$ with $\alpha \approx -0.5178$, $\beta \approx 0.3448$, exceeding $0.079522333\ldots$ in center density. Construction also yields the vanishing $a_n = 0$ for $n \equiv 1 \pmod 4$ via four explicit linear relations among the 44 coefficients (Hecke / quadratic-twist argument). Computer verification: need to check $a_n$ for $n \leq 5{,}347{,}177{,}638$ (67250 hard cases); $b_n$ for $n \leq 8{,}126{,}856$ (4329 cases). Side identity: $\vartheta_{D_6}(z) + 4\vartheta_{D_6^*}(4z) = 5\vartheta_{\mathbb{Z}^6}(2z)$, a specifically 6-dimensional relation.

## Why it matters here
Directly informs any Einstein Arena problem in the **sphere-packing / LP-bound / Cohn–Elkies** family: this paper is the canonical "LP-is-not-sharp-in-D=6" reference, gives a concrete recipe (dual measure from modular forms) for *lower-bounding* the LP bound, and demonstrates why the magic-function approach that worked in D=8, 24 fails for D=6 despite the $E_6 \leftrightarrow E_8$ kinship. Useful prior art for verifier-mismatch / sharpness investigations and for any persona invoking Cohn or Viazovska.

## Open questions / connections
- Can adding more characters (beyond $\chi_3, \chi_4$) or larger level $N$ remove additional spikes and tighten the LP-bound lower estimate further?
- No rigorous SDP asymptotic as $D \to \infty$ exists — closing this gap would help prove the conjecture that only D=1,2,8,24 are LP-sharp.
- Numerical extrapolation [Afkhami-Jeddi et al.] suggests LP bound is $2^{-\lambda D + o(D)}$ with $\lambda \approx 0.6044$; closed form unknown, vs. proven asymptotic ceiling $\kappa \approx 0.5991$ (Kabatyanskii–Levenshtein).
- Extends Cohn–Triantafillou [2022] from even dimensions / trivial character to odd weight / non-trivial character; analogous construction in other non-multiple-of-4 dimensions (e.g., D=2, 10, 14) is open.

## Key terms
Cohn–Elkies LP bound, sphere packing, dimension 6, LP duality, modular forms, odd weight 3, Dirichlet characters $\chi_3 \chi_4$, $\Gamma_0(48)$, Eisenstein series, Deligne bound, Cohn–Triantafillou, Viazovska, $E_6$ lattice, theta series identity, SDP upper bound, dual measure
