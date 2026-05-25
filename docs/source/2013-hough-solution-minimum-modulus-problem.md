---
type: source
kind: paper
title: Solution of the minimum modulus problem for covering systems
authors: Bob Hough
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1307.0874
source_local: ../raw/2013-hough-solution-minimum-modulus-problem.pdf
topic: general-knowledge
cites:
---

# Solution of the minimum modulus problem for covering systems

**Authors:** Bob Hough  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1307.0874

## One-line
Resolves Erdős's 1950 minimum modulus problem by proving that every distinct covering system of congruences has at least one modulus $\leq 10^{16}$.

## Key claim
**Theorem 1.** The least modulus of any distinct covering system $\{a_i \bmod m_i : 1 < m_1 < m_2 < \dots < m_k\}$ that covers $\mathbb{Z}$ satisfies $m_1 \leq 10^{16}$. This refutes the conjecture that distinct coverings exist with arbitrarily large minimum modulus and confirms Nielsen's (2009) suggestion that the answer is negative.

## Method
Probabilistic method via a **staged sieve** using the **Lovász Local Lemma (LLL)** in a novel *relative form*. Moduli are filtered by smoothness thresholds $P_0 < P_1 < \dots$ with $Q_i = \prod_{p \leq P_i} p^{v_p}$; the uncovered set $R$ is built as a nested chain $R_0 \supset R_1 \supset \dots$ where each stage sieves by "new factors" $\mathcal{N}_{i+1}$ (squarefree numbers with primes in $(P_i, P_{i+1}]$). LLL is applied twice: once to lower-bound the density of "good" fibres satisfying a dilation condition $\sum_{n: p|n} |A_{n,r} \bmod nQ_i| e^{\lambda \omega(n)} / n \leq 1 - e^{-\lambda}$, and once relatively to show that good fibres are automatically *well-distributed*. Bias statistics $\beta_k(i) = \sum_{m|Q_i} \ell_k(m) \max_b \mu_i(R^* \cap (b \bmod m))/\mu_i(R^*)$ (weighted by $\ell_k(m) = (2k-1)^{\omega(m)}$ for squarefree $m$) are tracked iteratively and controlled by a reweighting measure $\mu_i$. Final numerical verification uses Rosser–Schoenfeld explicit prime estimates and Pari/GP.

## Result
With parameters $M = 10^{16}$, $P_i = e^{11+i}$, $e^\lambda = 2$, $\pi_{\text{good}} = 1/2$, and the 3rd bias statistic $\beta_3(0) < 731.8$, the iterative constraint (C1) holds for all $i \geq 0$, proving the uncovered set has positive density whenever the minimum modulus exceeds $10^{16}$. Builds directly on Filaseta–Ford–Konyagin–Pomerance–Yu (2007), whose argument essentially constitutes the first stage ($i = 0$).

## Why it matters here
General background; no direct arena tie. The **relative Lovász Local Lemma** machinery (good fibres ⟹ well-distributed fibres) and the **iterated-sieve + bias-statistic moment control** template are reusable for any extremal-combinatorics / discrete-geometry problem where dependent bad events must be ruled out across multiple scales — potentially relevant to Sidon-set, sphere-packing density, or autocorrelation-style problems where LLL-flavored arguments may bound the size of "uncovered" configurations.

## Open questions / connections
- Odd-modulus problem (Erdős–Selfridge): does a distinct covering system exist with all moduli odd? Hough notes Theorem 1 implies any covering contains a modulus divisible by one of an initial segment of primes — a quantitative strengthening is promised in future work.
- Can the bound $10^{16}$ be reduced substantially? The argument is not tight; Nielsen's record-holder has minimum modulus 40, leaving an enormous gap.
- Extends Filaseta et al. (2007) reciprocal-sum lower bound by completing the staged-sieve induction beyond the first threshold.

## Key terms
covering systems, minimum modulus problem, Erdős, distinct congruences, Lovász Local Lemma, relative LLL, probabilistic method, sieve method, smooth numbers, bias statistics, Rankin's trick, Filaseta-Ford-Konyagin-Pomerance-Yu, Rosser-Schoenfeld, Chinese Remainder Theorem, Nielsen
