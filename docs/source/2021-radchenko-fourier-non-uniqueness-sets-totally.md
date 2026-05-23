---
type: source
kind: paper
title: Fourier non-uniqueness sets from totally real number fields
authors: Danylo Radchenko, Martin Stoller
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.11828v3
source_local: ../raw/2021-radchenko-fourier-non-uniqueness-sets-totally.pdf
topic: general-knowledge
cites: 
---

# Fourier non-uniqueness sets from totally real number fields

**Authors:** Danylo Radchenko, Martin Stoller  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2108.11828v3

## One-line
Constructs explicit infinite-dimensional families of Schwartz Fourier eigenfunctions that vanish on $\sqrt{\Lambda}$-type discrete sets built from the codifferent of a totally real number field, exhibiting Fourier *non*-uniqueness sets in $\mathbb{R}^n$ ($n\geq 2$).

## Key claim
For any totally real $K/\mathbb{Q}$ of degree $n \geq 2$, the set $\sqrt{\mathcal{O}_K^\vee}$ (square-root lifts of the codifferent) sits inside $\bigcup_{m\geq 0}\sqrt{m}\,S^{n-1}$ with $\sim c_K m^{n-1}/(n-1)!$ points on the $m$-th sphere ($c_K = 2^n\sqrt{|\mathrm{disc}(K)|}$), yet the space of Schwartz functions with $\hat f = \varepsilon f$ ($\varepsilon = \pm 1$) vanishing on this set is *infinite-dimensional* — sharply contrasting Stoller's earlier uniqueness theorem on $\bigcup\sqrt{m}\,S^{n-1}$.

## Method
Slash-action on $\mathbb{C}[\Gamma_\vartheta]$ for a theta-subgroup of the Hilbert modular group $\mathrm{PSL}_2(\mathcal{O}_K)$, using Hecke theta functions of fractional ideals as automorphic factors (1-cocycle $j_\vartheta$). Non-trivial Fourier eigenfunctions are produced as finite $\mathbb{C}$-linear combinations of Gaussians $e^{\pi i\sum z_j x_j^2}$ slashed by elements of the right ideal $I=\sum_{\beta\in\mathcal{O}_K}(1-T_{2\beta})\mathbb{C}[\Gamma_\vartheta]$ intersected with $(1\pm S)\mathbb{C}[\Gamma_\vartheta]$; concrete 16-Gaussian witnesses are exhibited using units in congruence classes $1+4\mathcal{O}_K$ and $1+3\mathcal{O}_K$ (Dirichlet). A separate §4 obstruction uses Margulis' normal subgroup theorem on irreducible lattices in $\mathrm{PSL}_2(\mathbb{R})^n$; §5 builds Poincaré-type series for Hecke groups $H(\lambda)$ of infinite covolume ($\lambda > 2$).

## Result
- **Theorem 1:** Infinite-dimensional space of $\hat f = \varepsilon f$ Schwartz functions vanishing on $\sqrt{\mathcal{O}_K^\vee}$.
- **Theorem 2:** Same for the ellipsoid-supported set $E(c,\mathfrak{a})$ when $c\mathfrak{a}^2 = \mathfrak{d}^{-1}$.
- **Density asymptotic:** $|\sqrt{\mathfrak{d}^{-1}} \cap \sqrt{m}S^{n-1}| = \frac{2^n\sqrt{|\mathrm{disc}(K)|}}{(n-1)!}m^{n-1}+O(m^{n-2})$.
- **Theorem 3 (radial uniqueness):** For $d\geq 5$ and $\alpha\beta \geq 1$, $\bigl(\bigcup\sqrt{m/\alpha}\,S^{d-1},\bigcup\sqrt{m/\beta}\,S^{d-1}\bigr)$ is a Fourier uniqueness *pair* for $\mathcal{S}_{\mathrm{rad}}(\mathbb{R}^d)$ with explicit interpolation; if $\alpha\beta>1$, finitely many spheres may be removed.

## Why it matters here
Directly informs P5/P6/P11/P14/P17-class problems where the "magic function" / Fourier-interpolation toolkit (Cohn–Elkies, Radchenko–Viazovska, Viazovska $E_8$) is the dominant lens: it maps the *boundary* of where uniqueness fails — non-uniqueness emerges precisely when the lattice has number-theoretic rigidity (Hilbert modular group) but the relevant slash-ideal intersection is non-empty. Useful as a sanity-check: not every "nice" discrete subset of $\bigcup\sqrt{m}S^{n-1}$ is a uniqueness set, so any conjectured interpolation node design must avoid these constructions.

## Open questions / connections
- Characterize *all* discrete Fourier uniqueness sets inside $\bigcup\sqrt{m}S^{n-1}$ — paper notes this is "subtle" (gap between Ramos–Stoller uniform-density positives and these number-theoretic negatives).
- Extends Radchenko–Viazovska (2019) [12], Stoller (2021) [17], Ramos–Stoller [13], Cohn–Kumar–Miller–Radchenko–Viazovska [5]; uses Hecke 1936 [6] infinite-covolume modular forms for $\lambda>2$.
- Open: can $n_0$ in Corollary 5.1 be sharpened to $\lceil (d+4)/8\rceil$ for $\lambda>2$ as it is for $\lambda=2$ (cf. [4])? Conditions (D) discreteness and (F) free-product remain conjecturally necessary for interpolation when $n\geq 2$.

## Key terms
Fourier interpolation, Fourier uniqueness pair, non-uniqueness set, totally real number field, codifferent, different ideal, Hilbert modular group, theta function, Hecke group, Poincaré series, Schwartz eigenfunction, Gaussian slash action, Margulis normal subgroup theorem, $\mathrm{PSL}_2(\mathcal{O}_K)$, Radchenko–Viazovska, Cohn–Elkies, sphere packing, modular forms infinite covolume
