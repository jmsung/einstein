---
type: source
kind: paper
title: How to hunt wild constants
authors: D. R. Stoutemyer
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.16720
source_local: ../raw/2021-stoutemyer-how-hunt-wild-constants.pdf
topic: general-knowledge
cites:
---

# How to hunt wild constants

**Authors:** D. R. Stoutemyer  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.16720

## One-line
Survey of tools — tables, web apps, CAS functions, and integer-relation algorithms — that take a floating-point number and return concise closed-form candidates it might approximate.

## Key claim
Given a float (e.g. $6.518670730718491$), a portfolio of tools (OEIS, WolframAlpha, ISC, Ordner, MESearch, RIES, Maple `identify`, AskConstants, Plouffe's Inverter, custom PSLQ) can usefully often recover an exact closed form (e.g. $3\arctan 2 + \ln 9 + 1$); no single tool dominates, so trying several is essential.

## Method
The tools split into five categories: (1) curated text tables sorted by fractional part with sign aliasing; (2) precomputed lookup tables (ISC, Plouffe, AskConstants — up to $\sim 8\times 10^{10}$ entries); (3) exhaustive breadth-first bidirectional search (MESearch, RIES) that enumerates expressions by complexity; (4) PSLQ / LLL integer-relation algorithms over a basis $[\tilde x, 1, \pi, \sqrt 2, \ln 2, \dots]$ — including linear, linear-fractional, minimal-polynomial (algebraic-number), power-product, and inverse-function model classes; (5) web search engines on the raw digit string. PSLQ requires roughly $mn$ digits of input precision to recover an $m$-component integer vector with coefficients up to $n$ digits.

## Result
Establishes practical protocols: truncate (don't round) trailing digits; try multiple precisions to distinguish persistent limits from impostors (a result that survives precision increase is likely real); apply Pareto trade-off of Agreement vs Entropy10 complexity ($\text{Margin} = \text{Agreement} - \text{Entropy10}$); exploit fractional-part and significand aliasing. Documents the "curse of extreme magnitude" — tools fail for $|x| \ll 1$ or $\gg 1$ because rational coefficients blow up; Finch's 10,000-constant table has median magnitude $\sim 0.9$, quartiles $\sim 0.4$ and $\sim 1.9$.

## Why it matters here
Directly relevant to the wild-constants problem: arena solves often produce mystery floats (basin energies, optimal radii, equioscillation values) that may have closed forms — this paper is the operating manual for that recognition step. Connects to LP-bound / Cohn-Elkies work where dual optimal values sometimes coincide with named constants, and to mpmath polish results that should be tested against PSLQ before declaring "irrational".

## Open questions / connections
- Can custom PSLQ basis vectors (cofactors $\pi^k, \ln 2, \ln 3, \zeta(m), \text{Li}_m(1/2)$) recover closed forms for arena-problem optimal values that general-purpose tools miss?
- Impostor-detection: at what precision threshold does a candidate that persists across two precision levels become trustworthy enough to attempt a proof?
- Extends Ferguson–Bailey PSLQ [7,8] and Bailey–Broadhurst parallel integer relation work [2]; related to the Ramanujan Machine [16] for auto-conjecturing constants.

## Key terms
PSLQ, LLL, integer relation algorithm, inverse symbolic calculator, OEIS, WolframAlpha, RIES, MESearch, AskConstants, Plouffe inverter, closed-form recognition, algebraic number identification, Cohn-Elkies, wild constants, Entropy10, fractional-part aliasing, minimal polynomial, Bailey, Broadhurst
