---
type: source
kind: paper
title: Condition numbers for the Moore-Penrose inverse and the least squares problem involving rank-structured matrices
authors: Sk. Safique Ahmad, Pinki Khatun
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2306.12177v3
source_local: ../raw/2023-ahmad-condition-numbers-moore-penrose-inverse.pdf
topic: general-knowledge
cites:
---

# Condition numbers for the Moore-Penrose inverse and the least squares problem involving rank-structured matrices

**Authors:** Sk. Safique Ahmad, Pinki Khatun  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2306.12177v3

## One-line
Derives structured mixed and componentwise condition numbers for the Moore–Penrose inverse and minimum-norm least-squares solution of rank-deficient Cauchy–Vandermonde and $\{1,1\}$-quasiseparable matrices, parameterized by $O(m+n)$ real parameters.

## Key claim
Under the rank-preserving perturbation set $S(\Psi) = \{\Delta\Psi : \mathrm{rank}(M(\Psi+\Delta\Psi)) = \mathrm{rank}(M(\Psi)) = r,\ \|M^\dagger\|_2\|\Delta M\|_2 < 1\}$, the structured MCN/CCN admit closed-form upper bounds expressible via $\partial M/\partial\psi_k$, $M^\dagger$, $E_M = I - MM^\dagger$, $F_M = I - M^\dagger M$; for Givens-vector (GV) representation the bounds are provably tighter than the QS representation, and "effective" CNs (dropping the two $O(n)$ sum terms) reliably estimate the full bound within a factor of $n-1$.

## Method
Componentwise perturbation analysis applied to a parameterized matrix $M(\Psi)$ whose entries are differentiable in $\Psi \in \mathbb{R}^p$. Uses the Stewart–Sun perturbation expansion of $M^\dagger$ (Lemma 3.5) restricted to acute perturbations (Proposition 2.3), then specializes the general formula to CV matrices and to QS / GV parameterizations of $\{1,1\}$-quasiseparable matrices, bounding term-by-term using $|p_i|, |q_i|, |r_i|, |s_i| \leq 1$ for GV tangent parameters.

## Result
For an $m\times n$ rank-$r$ parameterized matrix, $\kappa^\dagger_M(M(\Psi)) \leq \|X^\dagger_\Psi\|_{\max}/\|M^\dagger\|_{\max}$ where $X^\dagger_\Psi = \sum_k \big(|M^\dagger \partial_k M\, M^\dagger| + |M^\dagger M^{\dagger\top}(\partial_k M)^\top E_M| + |F_M (\partial_k M)^\top M^{\dagger\top}M^\dagger|\big)|\psi_k|$. For $\{1,1\}$-QS matrices $\tilde\kappa^\dagger(M(\Psi_{GV})) \leq \tilde\kappa^\dagger(M(\Psi_{QS}))$ and $\tilde\kappa^\dagger(M(\Psi_{QS})) \leq n\,\tilde\kappa^\dagger(M)$ (unstructured). Numerical experiments report structured bounds 2–8 orders of magnitude below unstructured (e.g. Example 6.2: unstructured $\tilde\kappa^\dagger \approx 5.4\times 10^7$ vs structured $\approx 3.4\times 10^4$).

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems involves CV or quasiseparable matrices, and condition-number analysis for LS problems is outside the current optimizer stack (mpmath polish + L-BFGS / SLSQP / CMA-ES / parallel tempering). Possibly relevant only if a future problem requires sensitivity bounds for a structured linear system inside the inner loop.

## Open questions / connections
- Extension to weighted M-P inverse and weighted LS (explicitly listed as future work).
- Extension to multiple right-hand side LS problems with structured coefficient matrices.
- Generalization to other rank-structured classes (Cauchy, semiseparable, hierarchical-rank) beyond CV and $\{1,1\}$-QS.

## Key terms
Moore-Penrose inverse, condition number, mixed condition number, componentwise condition number, Cauchy-Vandermonde matrices, quasiseparable matrices, Givens-vector representation, rank-deficient least squares, perturbation theory, structured sensitivity, acute perturbation, minimum norm least squares
