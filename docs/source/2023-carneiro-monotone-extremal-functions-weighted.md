---
type: source
kind: paper
title: Monotone extremal functions and the weighted Hilbert's inequality
authors: Emanuel Carneiro, Friedrich Littmann
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2302.14658v2
source_local: ../raw/2023-carneiro-monotone-extremal-functions-weighted.pdf
topic: general-knowledge
cites:
---

# arXiv:2302.14658v2[math.CA]3Jul2023

## MONOTONE EXTREMAL FUNCTIONS AND THE WEIGHTED HILBERT’S INEQUALITY

EMANUEL CARNEIRO AND FRIEDRICH LITTMANN

Abstract. In this note we find optimal one-sided majorants of exponential type for the signum function subject to certain monotonicity conditions. As an application, we use these special functions to obtain a simple Fourier analysis proof of the (non-sharp) weighted Hilbert-MontgomeryVaughan inequality.

1. Introduction An entire function F : C → C is said to be of exponential type if τ(F) := limsup

|z|−1 log |F(z)| < ∞.

|z|→∞

In this case, the number τ(F) is called the exponential type of F. An entire function F : C → C is said to be real entire if it its restriction to R is real-valued. In this note we solve the following extremal problem with a monotonicity constraint.

Theorem 1. Let F : C → C be a real entire function such that:

- (i) F has exponential type at most 2π;
- (ii) F(x) ≥ sgn(x) for all x ∈ R;
- (iii) F is non-decreasing on (−∞,0) and non-increasing on (0,∞).


Then ∞

F(x) − sgn(x) dx ≥ 2. (1.1)

−∞

Moreover, there exists a unique real entire function M : C → C verifying properties (i), (ii) and (iii) for which the equality in (1.1) holds. This function is given by

z

sin2 πs π2s(s + 1)2

M(z) = −2

ds − 1. (1.2)

−∞

Remark: The integral in (1.2) is understood to be along the path (−∞,0] ∪ [0,z], where the latter is the line segment connecting 0 to z.

Without the monotonicity constraint (iii) in Theorem 1, this problem was solved by Beurling in the late 1930’s, and the value of the minimal integral on the right-hand side of (1.1) is actually equal

Date: July 4, 2023. 2010 Mathematics Subject Classification. 41A29, 41A30, 41A44, 15A63. Key words and phrases. Extremal functions, exponential type, monotonicity, weighted Hilbert’s inequality.

1

1.0

0.5

-3 -2 -1 1

- -1.0

- -0.5


1.0

0.5

-3 -2 -1 1

- -1.0

- -0.5


Figure 1. The monotone extremal majorant M(x) on the left, and the classical Beurling majorant B(x) on the right.

to 1; see Vaaler’s classical survey [9] on the subject. The unique extremal function in this case is

2 ∞

−1

1 (z − n)2 −

sinπz π

1 (z − m)2

2 z

+

. (1.3)

B(z) =

m=−∞

n=0

See Figure 1 for the plots of these functions on R. As an application of Theorem 1 we revisit the following result of Montgomery and Vaughan [4].

Corollary 2 (Weighted Hilbert-Montgomery-Vaughan inequality). Let N ∈ N. Let λ1,...,λN be a set of distinct real numbers and define δn := min{|λn − λm| : m ̸= n}. If a1,...,aN ∈ C then

holds with C = 2π.

N

N

|an|2 δn

aman (λm − λn) ≤ C

m,n=1 m̸=n

n=1

(1.4)

Inequality (1.4) has a long history. In the case λm = m, inequality (1.4) with constant C = 2π was first proved by Hilbert. This was later improved by Schur [8], who obtained the sharp constant C = π on the right-hand side. The equally-spaced case of (1.4) (i.e. when the {δn}Nn=1 on the right-hand side are replaced by a uniform δ) with the sharp constant C = π was established by Montgomery and Vaughan in [4] with a spectral analysis approach, and by Vaaler [9] with a Fourier analysis approach based on Beurling’s extremal functions. The general weighted case was first proposed by Montgomery and Vaughan [4], who proved inequality (1.4) with constant C = 23π. This was later improved by Preissmann [7] who obtained

C = 1 + 23 65 π = (1.3154...)π , currently the best known bound in the literature. Selberg privately reported to Montgomery a proof of (1.4) with constant C = 3.2, but the ideas of such a proof were never made public. It is conjectured that (1.4) should hold with constant C = π, and this has been an open problem since 1974.

Our contribution in this application is to provide, for the first time, a Fourier analysis proof of the weighted Hilbert-Montgomery-Vaughan inequality. Such a proof turns out to be simple, with the caveat of giving a slightly worse constant C = 2π. The previous proofs of Montgomery and Vaughan [4] and of Preissmann [7] live within the realm of linear algebra, relying on an intricate series of estimates to directly bound the largest eigenvalue of the associated hermitian matrix.

Weighted inequalities like (1.4) have many applications in number theory, e.g. [3] and [5]. Other works related to the weighted Hilbert-Montgomery-Vaughan inequality include [2] and [10].

2. A Fourier analysis proof of the weighted Hilbert-Montgomery-Vaughan inequality

In this section we assume the validity of Theorem 1 and prove Corollary 2.

2.1. Proof of Corollary 2. Let ψ(x) := M(x)−sgn(x). Throughout this proof we use the notation ψδ(x) := ψ(δx), for δ > 0. By construction, ψ ∈ L1 ∩ L2(R), and we denote its Fourier transform on the real line by

∞

ψ(x)e−2πixt dx. We remark that

ψ(t) :=

−∞

ψδ(t) = δ−1 ψ(δ−1t), and hence, by the Paley-Wiener theorem,

ψδ(t) = −(πit)−1 for |t| ≥ δ.

Reorder the sequence {λn}Nn=1 so that δ1 ≥ δ2 ≥ ... ≥ δN > 0. Then, evidently, |λm−λn| ≥ δmin(m,n). We adopt the convention ψ0 ≡ 0. From the monotonicity condition we note that ψδ

### (x) ≥ ψδ

(x) for all x ∈ R and j = 1,2,...,N. Hence

j−1

j

2

N

N

∞

ame−2πiλ

mx

0 ≤

### (x) − ψδ

ψδ

(x)

dx (2.1)

j−1

j

−∞

j=1

m=j

N

N

### (λm − λn) − ψδ

(λm − λn)

aman ψδ

=

j−1

j

j=1

m,n=j

min(m,n)

N

=

aman

m,n=1

j=1

### (λm − λn) − ψδ

ψδ

j−1

j

N

aman ψδmin(m,n)(λm − λn)

=

m,n=1

N

N

aman πi(λm − λn)

= −

+ ψ(0)

n=1

m,n=1 m̸=n

|an|2 δn

.

(λm − λn)

It then follows that

N

N

|an|2 δn

aman πi(λm − λn) ≤ ψ(0)

.

m,n=1 m̸=n

n=1

The function −M(−x) is a minorant of sgn(x) which is non-increasing on (−∞,0), and non-decreasing on (0,∞). Repeating the above argument with φ(x) := sgn(x) + M(−x) ≥ 0 yields

N

N

|an|2 δn ≤

aman πi(λm − λn)

− ψ(0)

,

n=1

m,n=1 m̸=n

and this concludes the proof of Corollary 2 since ψ(0) = 2.

Remark: One might wonder whether these techniques can be used to prove the sharp weighted Hilbert-Montgomery-Vaughan inequality. If one replaces the function M from Theorem 1 by the original Beurling majorant B described in (1.3), and defines ψ(x) := B(x) − sgn(x) instead, one would need to verify the non-negativity of the corresponding expression appearing in (2.1).

3. Monotone extremal functions: Proof of Theorem 1

To simplify the calculations let us consider the analogous extremal problem replacing sgn(x) by the upper semi-continuous Heaviside function x0+ (i.e. x0+ = 1 for x ≥ 0, and x0+ = 0 for x < 0).

We first find necessary conditions that the optimal function must satisfy, and then construct a function that satisfies these conditions. Let G be an entire majorant of x0+ of exponential type at most 2π that is non-decreasing on (−∞,0) and non-increasing on (0,∞), and such that G − x0+ ∈ L1(R). Then g = G′ is of one sign on each of the half-lines. Since limx→−∞ G(x) = 0, it follows that

x

G(x) =

g(x)dx.

−∞

Also, from the fact that limx→∞ G(x) = 1, it follows that g ∈ L1(R) and

∞

g(x)dx = 1. (3.1)

−∞

Since G − x0+ ∈ L1(R), Fubini’s theorem and (3.1) imply that the following two integrals are finite:

0

0

x

0

g(u)dudx = −

ug(u)du, (3.2) and

G(x)dx =

−∞

−∞

−∞

−∞

∞

∞

∞

∞

G(x) − 1 dx =

−

g(u)du dx = −

ug(u)du. (3.3)

0

0

x

0

Define H : C → C by H(u) = −ug(u). Then H is a real entire function of exponential type at most 2π that is non-negative on R. From (3.2) and (3.3) we find also that H ∈ L1(R). Moreover, since g

is entire, H has a zero at the origin of even order at least 2. It follows by Krein’s decomposition1 [1, p. 154] that there exists h : C → C entire of exponential type at most π such that

H(z) = z2h(z)h(z)

for all z ∈ C. From (3.2), (3.3) and Poisson summation (that holds pointwise everywhere since H′ ∈ L1(R) by a classical result of Plancherel and P´lya [6], and hence H has bounded variation on R) we have

∞

∞

G(x) − x0+ dx =

|nh(n)|2.

H(x)dx =

H(n) =

−∞

−∞

n∈Z

n∈Z

Another application of Poisson summation, together with (3.1), yields −

∞

n|h(n)|2 =

g(n) = g(0) =

g(x)dx = 1. (3.4)

−∞

n∈Z

n∈Z

Hence

∞

G(x) − x0+ dx =

|nh(n)|2 ≥

|n||h(n)|2 ≥ −

n|h(n)|2 = 1, (3.5)

−∞

n∈Z

n∈Z

n∈Z

which establishes the desired inequality.

In order to have equality in (3.5) we must have h(n) = 0 if n ̸= −1,0. From (3.4), this implies that |h(−1)| = 1. Since z h(z) ∈ L2(R) and has exponential type at most π, the classical ShannonWhittaker interpolation formula yields

sinπz π(z + 1)

z h(z) = h(−1)

, which implies that

sin2 πz π2z (z + 1)2

sin2 πz π2z (z + 1)2

g(z) = −z h(z)h(z) = −|h(−1)|2

= −

. One can check directly that this g satisfies (3.1) (e.g. via Poisson summation) and that G(x) = −

x

sin2 πu π2u(u + 1)2

du (3.6)

−∞

is indeed a majorant of x+0 with ∞

∞

G(x) − x0+ dx =

|ug(u)|du = 1.

−∞

−∞

Finally, observe that G : R → R defined by (3.6) is the restriction to R of the entire function

z

sin2 πs π2s(s + 1)2

G(z) = G(0) −

ds. (3.7)

0

1If f : C → C is a real entire function of exponential type at most 2π, that is non-negative and integrable on R, then there exists g : C → C entire of exponential type at most π such that f(z) = g(z)g(z) for all z ∈ C.

1.0

0.8

0.6

0.4

0.2

-3 -2 -1 1

Figure 2. The extremal function G(x)

The integration is over the line segment connecting 0 to z, and the value G(0) is a linear combination of known constants with decimal expansion G(0) = 1.0749... . If z = x+iy, it is clear from (3.7) that |G(z)| ≤ C|z|e2π|y| for some C > 0, and therefore G has exponential type at most 2π. This concludes the proof in the case of x0+.

Naturally, in the case of sgn(x) our unique extremal function is then M(z) := 2G(z) − 1.

Acknowledgements

We are thankful to Hugh Montgomery and Jeffrey Vaaler for the enlightening discussions on the history of this problem. We are also thankful to Harald Helfgott and Michael Kelly for helpful discussions during the preparation of this note. Finally, we thank the anonymous referees for the helpful remarks in order to improve the presentation.

References

- [1] N. I. Achieser, Theory of Approximation, New York, 1956.
- [2] X.-J. Li, A note on the weighted Hilbert’s inequality, Proc. Amer. Math. Soc. 133 (2005), 1165–1173.
- [3] H. L. Montgomery, The analytic principle of the large sieve, Bull. Amer. Math. Soc. 84 (1978), 547–567.
- [4] H. L. Montgomery and R. C. Vaughan, Hilbert’s Inequality, J. London Math. Soc. 8 (2) (1974), 73–81.
- [5] H. L. Montgomery and R. C. Vaughan, The large sieve, Mathematika 20 (1973), 119–134.
- [6] M. Plancherel and G. P´olya, Fonctions entie´res et inte´grales de Fourier multiples, (Seconde partie) Comment. Math. Helv. 10, (1938), 110–163.
- [7] E. Preissmann, Sur une ine´galite´ de Montgomery and Vaughan, Enseign. Math. (2) 30 (1984), no. 1-2, 95–113.
- [8] I. Schur, Bemerkungen zur Theorie der beschr¨ankten Bilinearformen mit unendlich vielen Ver¨anderlichen, J. Reine Angew. Math. 140 (1911), 1–28.
- [9] J. D. Vaaler, Some extremal functions in Fourier analysis, Bull. Amer. Math. Soc. 12 (1985), 183–215.
- [10] W. Yangjit, On the Montgomery–Vaughan weighted generalization of Hilbert’s inequality, preprint at https://arxiv.org/abs/2203.14950.


ICTP - The Abdus Salam International Centre for Theoretical Physics, Strada Costiera, 11, I - 34151, Trieste, Italy.

Email address: carneiro@ictp.it

Department of mathematics, North Dakota State University, Fargo, ND 58105-5075. Email address: friedrich.littmann@ndsu.edu

