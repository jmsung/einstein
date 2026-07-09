---
type: source
kind: paper
title: Hyperelliptic curves and newform coefficients
authors: S. Dembner, Vanshika Jain
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.08358
source_local: ../raw/2020-dembner-hyperelliptic-curves-newform-coefficients.pdf
topic: general-knowledge
cites:
---

# Hyperelliptic curves and newform coefficients

**Authors:** S. Dembner, Vanshika Jain  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.08358

## One-line
Rules out specific odd primes and prime-powers as values of the Ramanujan tau-function and more general newform Fourier coefficients, by reducing the question to perfect powers in Fibonacci-type recurrences and to Frey-curve / level-lowering arguments.

## Key claim
Unconditionally: $\tau(n) \neq \pm\ell$ for every odd prime $\ell < 100$ and every $n$, and $\tau(n) \neq \pm 5^m$ for all $m \geq 1$. Conditionally (Frey–Mazur): for a newform $f$ of even weight $2k$ with integer coefficients and an ordinary prime $p$, $a_f(p^2)$ is never a perfect $j$-th power for $j \geq 4$ dividing $2k-1$, and $a_f(p^4)$ is never an $\ell$-th power for $\ell \geq 19$ dividing $2k-1$.

## Method
Combines two threads: (1) Reduce $a_f(p^4) = \alpha$ to integer points on hyperelliptic curves $Y^2 = 5X^{2(2k-1)} + 4\alpha$, then to perfect $(2k-1)$-st powers in Fibonacci-type sequences $a u_n + b v_n$ via the arithmetic of $\mathbb{Q}(\sqrt{5})$; rule these out by mod-$m$ periodicity (period $\pi(m)$) plus Baker-style linear-forms-in-logarithms bounds. (2) For general newforms, apply the modular method: attach a Frey curve to a primitive solution of $AX^n + BY^n = CZ^2$, use modularity + Ribet level-lowering, and invoke Frey–Mazur to exclude rational level-lowering targets; Bilu–Hanrot–Voutier bounds make the Thue computations unconditional.

## Result
Theorem 1.1 (unconditional): $\tau(n) \neq \pm\ell$ for all odd primes $\ell < 100$ — resolves the conspicuous $\ell = 19$ case left open by Balakrishnan–Craig–Ono–Tsai. Theorem 1.2: $\tau(n) \neq \pm 5^m$. Theorem 1.3: $\tau(p^4)$ has prime divisors only from $\{p\} \cup \{\ell : \ell \equiv 0,1,4 \pmod 5\}$. Theorem 1.4 (Frey–Mazur-conditional in parts): for newforms of weight $2k$, $a_f(p^2)$ is never an $\ell$-th power for $\ell \geq 4$ dividing $2k-1$ at ordinary $p$; $a_f(p^4) \neq m^\ell$ for $\ell \geq 19$ dividing $2k-1$ at ordinary $p \neq 2,5$. Method extends to any Lebesgue–Nagell $x^2 + D = Cy^{2n}$ with $\mathbb{Q}(\sqrt{C})$ of class number one.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems concern modular-form coefficients or Lehmer-type Diophantine questions — this is pure analytic/algebraic number theory. The only transferable technique is the **periodicity-mod-$m$ sieve on binary recurrences** (Lemma 3.1, Prop. 3.2), which is a generic "rule out perfect powers by congruences" tool that could conceivably surface in a Sidon/$B_h$ or extremal-sequence problem.

## Open questions / connections
- Perfect powers in general Fibonacci-type sequences $a u_n + b v_n$ are largely open beyond the classical Fibonacci/Lucas cases of Bugeaud–Mignotte–Siksek; sequences like $u_n + 2 v_n$ resist the congruence sieve because $u_{-1} + 2 v_{-1} = -1$.
- Removing the Frey–Mazur dependence in Theorem 1.4 parts (2)–(3) requires ruling out level-lowering to specific irrational newforms (e.g. LMFDB 380.2.a.c, 380.2.a.d).
- Extension to composite odd values $\alpha < 100$ runs into Thue equations $F_{p-1}(X,Y) = \pm\alpha$ where $p \mid \alpha$, outside the Bilu–Hanrot–Voutier bound regime.

## Key terms
Ramanujan tau-function, Lehmer's conjecture, newform coefficients, hyperelliptic curve, Lebesgue–Nagell equation, Fibonacci-type recurrence, Lucas sequence, linear forms in logarithms, Thue equation, Frey curve, modularity theorem, Ribet level-lowering, Frey–Mazur conjecture, Galois representation, Bilu–Hanrot–Voutier, real quadratic field $\mathbb{Q}(\sqrt{5})$, primitive divisors
