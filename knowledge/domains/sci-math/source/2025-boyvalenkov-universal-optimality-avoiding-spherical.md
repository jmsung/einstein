---
type: source
kind: paper
title: Universal optimality of $T$-avoiding spherical codes and designs
authors: P. Boyvalenkov, D. Cherkashin, P. Dragnev
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2501.13906
source_local: ../raw/2025-boyvalenkov-universal-optimality-avoiding-spherical.pdf
topic: general-knowledge
cites:
---

# Universal optimality of $T$-avoiding spherical codes and designs

**Authors:** P. Boyvalenkov, D. Cherkashin, P. Dragnev  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2501.13906

## One-line
Introduces $T$-avoiding spherical codes (codes whose inner-product set avoids a prescribed open set $T \subset [-1,1)$) and proves several distinguished codes — Leech-derived, Barnes–Wall minimal vectors, Golay-complement, SRG embeddings — are universally optimal, maximal, and tight as designs within their $T$-avoiding class.

## Key claim
For carefully chosen $T$, the codes $C_{1/4}$ (47104 pts), $C_0$ (93150 pts), $C_{\sqrt6/6}$ (11178 pts), $C_{\sqrt6/12}$ (48600 pts) on $S^{22}$, the Barnes–Wall kissing code (4320 pts on $S^{15}$), the Golay-complement code $C_G$ (2048 pts on $S^{22}$), the derived codes $C_{2816}, C_{2025}$ on $S^{21}$, and SRG-eigenspace embeddings (under $p+q\le 0$) are simultaneously (i) maximal $T$-avoiding $s$-codes, (ii) tight $T$-avoiding $\tau$-designs, and (iii) universally optimal $T$-avoiding codes (minimize $h$-energy for every absolutely monotone $h$).

## Method
Linear programming on the sphere in the Delsarte–Goethals–Seidel / Kabatianskii–Levenshtein / Cohn–Kumar framework, adapted to the $T$-avoiding setting: instead of requiring $f(t)\le 0$ on $[-1,s]$ (or $f\le h$ on $[-1,1)$), conditions are relaxed to hold only on $[-1,1)\setminus T$, while keeping nonnegative Gegenbauer coefficients $f_i\ge 0$ in the expansion $f = \sum f_i P_i^{(n)}$. Interpolation polynomials are built from $\{$inner products of the target code$\}$ as Hermite nodes; positive-definiteness of partial products is checked via explicit Gegenbauer expansions (computed in an appendix). Extends DGS three-distance bound by dropping the strict inequality in (12).

## Result
- $A(23, 7/15; T) = 47104$ for three choices of $T$ → $C_{1/4}$ maximal.
- $A(23, 1/2; (-1/2,-1/4)\cup(0,1/4)) = 93150$ → $C_0$ maximal.
- $A(23, 2/5; T) = 11178$ → $C_{\sqrt6/6}$ maximal.
- $A(23, 11/23; (-13/23,-7/23)\cup(5/23,6/23)) = 48600$ → $C_{\sqrt6/12}$ maximal.
- Reproves $A(23, 7/23; (-9/23,-1/23)) = 2048$ (Golay complement).
- Energy bounds $E_h \ge $ explicit closed forms at the design distance distributions for each code, valid for any absolutely monotone $h$ with sufficient derivative positivity (typically $h^{(4)}$ to $h^{(12)} > 0$).
- General theorem (Thm 7.6): any 3-distance spherical 3-design $\{\alpha,\beta,\gamma\}$ satisfying $\alpha\beta+\beta\gamma+\gamma\alpha \ge -3/(n+2)$ and $\alpha+\beta+\gamma\le 0$ is $T$-avoiding universally optimal for $T=(\alpha,\beta)$ or $(\beta,\gamma)$.
- SRG theorem (Thm 7.11): every SRG-eigenspace embedding with $p+q\le 0$ is universally optimal among $[-1,p)$-avoiding codes of cardinality $v$; Lemma 4.1 shows at least one of the two embeddings always satisfies this.

## Why it matters here
Directly relevant to **kissing-number / sphere-packing-style arena problems** and any optimization on $S^{n-1}$ with **forbidden inner-product bands**: the $T$-avoiding LP framework gives a recipe for proving optimality (or computing tight bounds) when the configuration must dodge a prescribed range of distances — a regime that arises whenever physical/structural constraints exclude certain pair angles. The Hermite-interpolation + Gegenbauer-positivity construction is a transferable technique for the optimizer's wiki (extends the existing Cohn–Kumar universal-optimality / LP-bound entries to a richer constraint class). Builds on the 48-dim $T$-avoiding kissing result (Boyvalenkov–Cherkashin 2025; Gonçalves–Vedana 2025) and the universal-optimality machinery of Cohn–Kumar (2007) and CKMRV (2017/2022).

## Open questions / connections
- Cohn–de Laat–Leijenhorst conjecture (4.2): can SDP three-point bounds prove maximality for all connected triangle-free SRGs (non-bipartite)? This paper resolves the energy side under $p+q\le 0$ but not the SDP-tight cardinality side.
- Which other $T$-avoiding classes admit universally optimal codes beyond Leech-derived / Barnes–Wall / SRG-embedded / 3-distance? The technique is presented as general but only instantiated for these.
- Can the relaxed three-distance hypothesis (Thm 7.6) — dropping the strict inequality from DGS (12) — be pushed further to recover new boundary-case configurations missed by classical DGS?
- The remark that universal optimality extends to a larger potential class than absolutely monotone (Remark 7.2, not shown in excerpt) suggests room to characterize the maximal potential class.

## Key terms
spherical codes, T-avoiding codes, universal optimality, linear programming bound, Delsarte-Goethals-Seidel, Gegenbauer polynomials, Cohn-Kumar, Leech lattice, Barnes-Wall lattice, Golay code, strongly regular graph, spherical design, kissing number, tight design, Hermite interpolation, absolutely monotone potential
