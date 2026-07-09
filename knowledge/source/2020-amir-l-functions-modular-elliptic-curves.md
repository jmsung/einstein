---
type: source
kind: paper
title: On L-functions of modular elliptic curves and certain K3 surfaces
authors: Malik Amir, Letong Hong
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.09803
source_local: ../raw/2020-amir-l-functions-modular-elliptic-curves.pdf
topic: general-knowledge
cites:
---

# On L-functions of modular elliptic curves and certain K3 surfaces

**Authors:** Malik Amir, Letong Hong  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.09803

## One-line
Extends Lehmer-style "which odd integers can appear as Fourier coefficients?" analysis from weight $k \geq 4$ newforms down to weights 2 and 3, applying the results to L-functions of modular elliptic curves and a one-parameter family of singular K3 surfaces.

## Key claim
For the seven weight-3 $\eta$-product newforms $f_\lambda(z) = \sum a_\lambda(n) q^n$ attached to the singular K3 surfaces $X_\lambda$ ($\lambda \in \{1, 8, 1/8, -4, -1/4, -64, -1/64\}$), if $|a_\lambda(n)| < 100$ is odd with $n > 1$ and $\gcd(n, 2N_\lambda) = 1$, then $a_\lambda(n)$ is confined to an explicit short list (e.g. $\{-5, 9, \pm 11, 25, \pm 41, \ldots, 99\}$); assuming GRH the list shrinks further to $\{-5, 9, \pm 11, 25, -45, 49, 55, -69, 75, \pm 81, \pm 93, 99\}$. Parallel "inadmissible-value" theorems hold for weight-2 newforms attached to elliptic curves with rational 2-, 3-, or 5-torsion.

## Method
Builds on Bilu–Hanrot–Voutier's theorem that Lucas numbers $u_n(\alpha,\beta) = (\alpha^n-\beta^n)/(\alpha-\beta)$ with $n > 30$ always have a primitive prime divisor: by Hecke recurrence the local sequence $a(p^{n-1})$ at a good prime $p$ is a Lucas sequence with $F_p(x) = x^2 - a(p)x + \chi(p) p^{k-1}$, so $|a(n)| = \ell$ reduces to finite case analysis of defective Lucas terms plus integer solutions of Thue equations $F_{2m}(X,Y) = \pm \ell$. For weights $<4$ the new wrinkle is that low-degree Thue equations ($m=1,2$) have infinitely many solutions; the authors close them using rational-torsion congruences ($\ell \mid \#E_{\mathrm{tor}}(\mathbb{Q})$ forces $a_E(p) \equiv p+1 \pmod \ell$) and the curve constraints $C_2^\pm: y^2 = \pm x^2 + \ell$, $C_4^\mp: y^4 \mp 3x^2 y^2 + x^4 = \ell$.

## Result
Three explicit "inadmissible odd values" theorems: (1.1) for $E/\mathbb{Q}$ with rational 6-torsion or rational 10-torsion, listing the forbidden coefficients $|a_E(n)| < 101$; (1.2) for each of the four singular K3 $\eta$-product weight-3 newforms (and their quadratic twists, seven $\lambda$'s total), with $\gcd(n, 2N_\lambda)=1$; (1.3) a universal statement for the full family $\{L(X_\lambda, s)\}_{\lambda \in \mathbb{Q}\setminus\{0,-1\}}$ that does not depend on modularity of $X_\lambda$ — only on the Galois conjugates $\pi_{\lambda,p}, \bar\pi_{\lambda,p}$ from the auxiliary elliptic curve $E_\lambda: y^2 = (x-1)(x^2 - \frac{1}{\lambda+1})$, exploiting $a_\lambda(p) = \gamma(b_\lambda(p)^2 - 2p)$. Tables 3–8 enumerate all integer solutions to the relevant Thue equations for $7 \le \ell \le 97$.

## Why it matters here
General background; no direct arena tie — this is analytic/algebraic number theory (modular forms, Lucas sequences, Thue equations on K3 L-functions), well outside the Einstein Arena problem families (sphere packing, autocorrelation, kissing, extremal graphs). The only loose connection is methodological: it's a clean example of Diophantine + recurrence + finite-case-enumeration reasoning, which is structurally analogous to LP/SDP bound + extremal-configuration enumeration in arena problems.

## Open questions / connections
- Extends Balakrishnan–Craig–Ono–Tsai (2020, weights $k\geq 4$) to weights 2–3; lower weights (weight 1, half-integral) remain open.
- Lehmer's original conjecture ($\tau(n) \neq 0$) still unresolved; this paper sidesteps it by ruling out specific odd values rather than zero.
- Several "omitted" values (e.g. $a_1(9) = -5$, $a_\lambda(7^2) = 49$) are realized — open question whether the remaining listed values are truly attained or further inadmissible.

## Key terms
Lucas sequences, Lehmer conjecture, Ramanujan tau function, modular forms, newforms, weight 2 newforms, weight 3 newforms, eta-products, K3 surfaces, singular K3, Picard number, modular elliptic curves, symmetric square L-function, Thue equations, Bilu-Hanrot-Voutier, primitive prime divisors, Mazur torsion theorem, complex multiplication, Inose-Shioda, GRH
