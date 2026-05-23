arXiv:1312.6884v2[math.CA]31Dec2014

QUASICRYSTALS AND POISSON’S SUMMATION FORMULA

NIR LEV AND ALEXANDER OLEVSKII

Abstract. We characterize the measures on R which have both their support and spectrum uniformly discrete. A similar result is obtained in Rn for positive measures.

1. Introduction

The subject of this paper is the analysis of measures in Rn with discrete support and spectrum. This subject is often discussed in the framework of so-called Fourier quasicrystals, see J. C. Lagarias’ survey [13] and the references therein. The name “quasicrystals” was inspired by an experimental discovery in the middle of 80’s of nonperiodic atomic structures with diﬀraction patterns consisting of spots.

Sometimes a Fourier quasicrystal is deﬁned as a countable set Λ which supports an (inﬁnite) pure point measure µ, such that its Fourier transform µ is also a pure point measure, see [7]. This deﬁnition is too wide, though, and includes examples where the support and spectrum are both everywhere dense sets. Usually the support Λ is assumed to be a uniformly discrete set (see e.g. [3], [4]).

The subject goes back to the classical Poisson summation formula: if f is a function on R (satisfying some mild smoothness and decay conditions) and f is its Fourier transform, then

f(n).

f(n) =

In other words, the measure

n∈Z

n∈Z

δn satisﬁes the equality

µ =

n∈Z

µ = µ.

There is also a multi-dimensional version of Poisson’s formula. Let L be a (full-rank) lattice in Rn, and L∗ be the dual lattice. Then

1 det(L) s∈L

δλ =

δs.

![image 1](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile1.png>)

λ∈L

∗

By simple procedures – shifts, multiplication on exponentials, and taking linear combinations – one may get diﬀerent forms of this result. In particular (for n = 1) it includes the Cauchy-Ramanujan formulas and more general ones due to V. Lin (see [9, pp. 283–289]).

However, there are Poisson-type formulas which cannot be obtained this way. In the one-dimensional case, the problem of which other discrete summation formulas may exist was studied by J.-P. Kahane and S. Mandelbrojt [10].

![image 2](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile2.png>)

Both authors are partially supported by their respective Israel Science Foundation grants.

1

An interesting example can be found in [8, p. 265], which involves weighted sums of

f and f at the nodes {±(n + 91)1/2} (n = 0, 1, 2, . . .). This summation formula is also deduced from Poisson’s one, but in a more tricky way. Notice that in contrast to the

![image 3](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile3.png>)

classical case, the nodes in this example do not lie in a uniformly discrete set.

The cut-and-project method, applied to lattices in a generic position, leads to an important class of quasicrystals – the “model sets”. Y. Meyer [18, 19] discovered fundamental connections of these non-periodic sets to harmonic analysis.

On the other hand, if µ is the sum of equal atoms along a discrete set Λ and µ is a positive pure point measure, then Λ is just a lattice. A simple proof of this fact was given by A. C´rdoba [5]. A more general situation, when the atoms take ﬁnitely many diﬀerent values, was considered in [17, p. 25], [6], [11]. These results are based on the Helson-Cohen characterization of idempotent measures in locally compact abelian groups.

There is a conjecture (see e.g. [13, p. 79]) that if the support and spectrum of a measure are both uniformly discrete sets, then the measure has a periodic structure, and the corresponding summation formula can be obtained from Poisson’s one by the procedures mentioned above.

The main goal of this paper is to prove this conjecture. In the one-dimensional case this is done in full generality, while in several dimensions – for positive (or positivedeﬁnite) measures. Our results were outlined in [15].

2. Results A set Λ ⊂ Rn is called uniformly discrete (u.d.) if d(Λ) := inf

|λ − λ′| > 0. (1) We consider a (complex) measure µ on Rn supported on a u.d. set Λ:

λ,λ′∈Λ,λ =λ′

µ(λ)δλ, µ(λ) = 0, d(Λ) > 0. (2)

µ =

λ∈Λ

Assume that µ is a temperate distribution, and that its Fourier transform µ(x) :=

µ(λ)e−2πi λ,x

λ∈Λ

(in the sense of distributions) is also a measure, supported by a u.d. set S: µ =

µ(s)δs, µ(s) = 0, d(S) > 0. (3)

s∈S

The set S is the spectrum of the measure µ.

- Theorem 1. Let µ be a measure on R satisfying (2) and (3). Then the support Λ is contained in a ﬁnite union of translates of a certain lattice. The same is true for S (with the dual lattice).
- Theorem 2. Let µ be a positive measure on Rn, n > 1, satisfying (2) and (3). Then the conclusion of Theorem 1 holds.


The following proposition completes the results, describing the explicit form of µ.

- Theorem 3. Let µ be a measure in Rn, n 1, satisfying (2) and (3), and such that Λ is contained in a ﬁnite union of translates of a lattice L. Then µ is of the form


N

µ =

Pj

δλ (4)

j=1

λ∈L+θj

where θj is a vector in Rn, and Pj(x) is a trigonometric polynomial (1 j N).

By a trigonometric polynomial P(x) on Rn we mean a ﬁnite linear combination of exponentials exp 2πi ω, x .

The conclusion of Theorem 3 shows that µ can be obtained from the measure λ∈L δλ in Poisson’s summation formula by a ﬁnite number of shifts, multiplication on exponentials, and taking linear combinations.

Conversely, one can easily see that every measure µ of the form (4) satisﬁes both (2) and (3), since µ is of the same form (with the dual lattice).

3. Preliminaries

- 3.1. Notation. By  ·, ·  and | · | we denote the Euclidean scalar product and norm in Rn. The open ball of radius r centered at the origin is denoted Br := {x ∈ Rn : |x| < r}.

A set Λ ⊂ Rn is uniformly discrete (u.d.) if it satisﬁes (1). The set Λ is relatively dense if there is R > 0 such that every ball of radius R intersects Λ.

By a “distribution” we shall mean a temperate distribution on Rn (see [25]). By a “measure” we mean a complex, locally ﬁnite measure (usually inﬁnite) which is also a temperate distribution. As usual δλ is the Dirac measure at the point λ.

If α is a temperate distribution, and ϕ is a Schwartz function on Rn, then α, ϕ will denote the action of α on ϕ.

The Fourier transform in Rn will be normalized as follows: ϕ(t) =

Rn

ϕ(x) e−2πi t,x dx. If α is a temperate distribution then its Fourier transform α is deﬁned by α, ϕ = α, ϕ .

We denote by supp(α) the support of the distribution α, and by spec(α) the support of its Fourier transform α.

By a (full-rank) lattice L ⊂ Rn we mean the image of Zn under some invertible linear transformation T. The determinant det(L) is equal to | det(T)|. The dual lattice L∗ is the set of all vectors λ∗ such that λ, λ∗ ∈ Z, λ ∈ L.

If A is a set in Rn then #A is the number of elements in A, mes(A) or |A| denote the Lebesgue measure of A, diam(A) is the diameter of A, and 1A is the indicator function of A. By A + B and A − B we denote the set of sums and set of diﬀerences of two sets A, B in Rn.

- 3.2. Measures. We will need a few simple facts about measures in Rn.


- Lemma 1. Let µ be a measure in Rn supported by a u.d. set Λ. Then µ is a temperate distribution if and only if


|µ(λ)| C(1 + |λ|N), λ ∈ Λ, for some positive constants C and N.

This can be proved using standard arguments.

- Lemma 2. Let µ be a measure in Rn satisfying (2) and (3). Then

sup

λ∈Λ

|µ(λ)| < ∞. (5)

Proof. Fix a Schwartz function ϕ such that ϕ(0) = 1 and supp( ϕ) ⊂ Bδ, where δ := d(Λ) > 0. Then

|µ(λ)| = ϕ(x − λ) dµ(x) = ϕ(t) e2πi λ,t d µ(t)

s∈S

|ϕ(s)| | µ(s)|. (6)

By Lemma 1 there are constants C, N such that | µ(s)| C(1+|s|N). Thus the sum on the right-hand side of (6) converges, and this establishes (5).

- Lemma 3. Let µ be a non-zero, positive measure in Rn. Then 0 ∈ spec(µ).


Proof. If not, there is δ > 0 such that the support of the distribution µ is disjoint from Bδ. Choose a Schwartz function ϕ such that supp(ϕ) ⊂ Bδ and ϕ > 0. Then

ϕ dµ = µ, ϕ = 0. Hence ϕµ is a non-zero positive measure with zero total mass, a contradiction.

- 3.3. Densities. We will use the classical concepts of lower and upper uniform density of a set Λ. The ﬁrst one plays a central role in Beurling’s sampling theory for entire functions of exponential type. The second one was used by Kahane and Beurling in the interpolation problem. Here are their deﬁnitions:

D−(Λ) := liminf

R→∞

inf

x∈Rn

#(Λ ∩ (x + BR)) |BR|

![image 4](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile4.png>)

,

D+(Λ) := limsup

R→∞

sup

x∈Rn

#(Λ ∩ (x + BR)) |BR|

![image 5](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile5.png>)

.

We also need the following version of density: D#(Λ) := liminf

R→∞

#(Λ ∩ BR) |BR|

![image 6](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile6.png>)

.

Clearly we have D−(Λ) D#(Λ) D+(Λ). Notice that if Λ is a u.d. set then the densities above are ﬁnite, and that their values

are invariant under translation of Λ. The last claim is obvious for D− and D+, and is easy to check for D#.

- 3.4. Sampling and interpolation. Let Ω be a compact set in Rn, whose boundary has Lebesgue measure zero. We denote by B(Ω) the Bernstein space consisting of all bounded, continuous functions f on Rn such that the distribution f is supported by Ω.


Let Λ be a u.d. set in Rn. One says that

- (i) Λ is a sampling set for B(Ω) if there is a constant C = C(Λ, Ω) such that

sup

x∈Rn

|f(x)| C sup

λ∈Λ

|f(λ)|, f ∈ B(Ω);

- (ii) Λ is an interpolation set for B(Ω) if for any bounded sequence of complex numbers {cλ}λ∈Λ, there exists some f ∈ B(Ω) satisfying f(λ) = cλ (λ ∈ Λ).


Landau proved in [14] that the classical density conditions for sampling and interpolation remain to be necessary in the more general situation:

- (i) If Λ is a sampling set for B(Ω), then D−(Λ) mes(Ω);
- (ii) If Λ is an interpolation set for B(Ω), then D+(Λ) mes(Ω).


Actually, Landau considered L2 versions of the sampling and interpolation problems (a simple proof can be found in [22]). The above results for the Bernstein space can be deduced e.g. as in [24, Theorem 2.1].

4. Spectral gaps

- 4.1. A measure (or a distribution) µ is said to have a spectral gap of size a > 0 if the Fourier transform µ vanishes on a ball of radius a.


In dimension one, there is a simple condition which is necessary for a u.d. set Λ to support a measure with a spectral gap.

Proposition 4. Let Λ ⊂ R be a u.d. set, d(Λ) δ > 0. Assume that Λ supports a non-zero measure µ, such that µ vanishes on the open interval (0, a) for some a > 0. Then

D#(Λ) c(a, δ), where c(a, δ) > 0 depends on a and δ only.

The proof given below is similar to the one used in [23, pp. 1044–1045]. It is based on the following

- Lemma 5. Let Λ be a ﬁnite set contained in (−R, R) \ (−δ, δ), where d(Λ) δ > 0, R 1, and let a > 0. There is c(a, δ) > 0 such that if (#Λ)/(2R) < c(a, δ) then one can ﬁnd a Schwartz function ϕ with the following properties:


ϕ(0) = 1, ϕ(λ) = 0 (λ ∈ Λ), spec(ϕ) ⊂ (0, a), sup

|ϕ(x)| 1.

|x| R

Proof. It will be convenient to assume that the number of points in Λ is even (if not, we may just add a point to Λ). Let n := (#Λ)/2 and ε := n/R. Deﬁne the polynomial

z − eiπλ/R 1 − eiπλ/R

P(z) :=

.

![image 7](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile7.png>)

λ∈Λ

Then P(1) = 1. We have

max

|P(z)|

|z|=1

R |λ|

2 2 sin 2 πλR λ∈Λ

.

![image 8](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile8.png>)

![image 9](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile9.png>)

![image 10](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile10.png>)

λ∈Λ

The right-hand side is maximized when Λ is the set {jδ : 1 |j| n}. Hence max

R2n δ2n(n!)2

eR δn

e δε

2n

2εR

|P(z)|

=

.

![image 11](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile11.png>)

![image 12](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile12.png>)

![image 13](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile13.png>)

|z|=1

Given a > 0, we choose a Schwartz function ψ satisfying spec(ψ) ⊂ (0, a/4), ψ(0) = 1, γ := sup

|ψ(x)| < 1. Set

|x| 1

ϕ(x) := P(eiπx/R) · (ψ(x/R))⌊R⌋+1 . (7)

Then ϕ is a Schwartz function, ϕ(0) = 1, ϕ(λ) = 0 for λ ∈ Λ. The spectrum of the ﬁrst factor in (7) is contained in [0, ε], while the spectrum of the second factor is contained in (0, a/2). Hence, if ε < a/2 then spec(ϕ) ⊂ (0, a). Finally, we have

sup

|ϕ(x)| γ

|x| R

e δε

![image 14](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile14.png>)

2ε R

.

If ε is suﬃciently small (depending on a, δ) then the expression in square brackets is smaller than one. The lemma is therefore proved.

Proof of Proposition 4. It will be enough to prove the claim under the assumption that µ is a ﬁnite measure. The general case may be easily reduced to this one by multiplying µ on a Schwartz function ϕ, such that |ϕ| > 0 and spec(ϕ) ⊂ (−a/2, 0). Then ϕµ is a non-zero, ﬁnite measure (by Lemma 1) supported by Λ and has a spectral gap (0, a/2).

Assume that D#(Λ) < c(a, δ), where c(a, δ) is given by Lemma 5. We will show that this implies µ = 0. Observe that, by translating µ and Λ, and since D#(Λ−λ) = D#(Λ) for every λ, it will be enough to consider the case when 0 ∈ Λ and to prove that µ(0) must be zero.

Choose a sequence Rj → ∞ such that (#Λj)/(2Rj) < c(a, δ), where Λj := Λ ∩ (−Rj, Rj) \ {0},

and let ϕj be the function given by Lemma 5 with Λ = Λj and R = Rj. Since µ vanishes on (0, a) we have

![image 15](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile15.png>)

ϕj(t) µ(t) dt = 0. On the other hand,

R

![image 16](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile16.png>)

ϕj(t) µ(t) dt =

R

![image 17](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile17.png>)

![image 18](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile18.png>)

ϕj(x) dµ(x) = µ(0) +

ϕj(λ) µ(λ).

R

|λ| Rj

It follows that

|µ(0)|

|µ(λ)| → 0 (j → ∞),

|λ| Rj

hence µ(0) = 0. Remarks. 1. A similar result can be found in [10, Proposition 7].

2. In [20] a complete characterization is given of u.d. sets in R which may support a ﬁnite measure with a spectral gap of given size, in terms of the lower Beurling-Malliavin density. It follows from this characterization that one may take c(a, δ) = a in Proposition

- 4 (however we do not use this result).


- 4.2. The situation in the multi-dimensional case (n > 1) is diﬀerent, and the existence of a spectral gap is not suﬃcient to make a conclusion about the density of the support. As a simple example consider the set Λ = Z × {0} in R2, which has density zero, but which is the support of the measure


µ =

n∈Z

having a spectral gap around the origin.

(−1)n δ(n,0)

However, if a u.d. set Λ supports a measure which has not just a spectral gap, but an isolated atom in the spectrum, then the support must have positive density. More precisely, we have the following

- Lemma 6. Let Λ be a u.d. set in Rn. Assume that Λ supports a measure µ satisfying

(5), and such that spec(µ) ∩ Ba = {0} for some a > 0. Then

D−(Λ) c(a, n), where c(a, n) > 0 depends on a and n only.

Proof. It is well-known that a distribution supported by the origin is a ﬁnite linear combination of derivatives of δ0. But condition (5) ensures that the distribution µ can only have order zero in a neighborhood of the origin. Hence there is a non-zero complex number w such that µ = w δ0 in Ba. By multiplying µ on 1/w we may suppose that

- w = 1. Fix a Schwartz function ψ, such that supp( ψ) ⊂ Ba/2 and ψ = 1 in Ba/3. For each
- x ∈ Rn deﬁne a measure νx by νx := ψx µ, where ψx(y) := ψ(y − x).


Then we have the following properties:

- (i) νx is supported by Λ;
- (ii) νx(t) = ( ψx ∗ µ)(t) = e−2πi x,t in Ba/3;
- (iii) νx is a ﬁnite measure, and |dνx| C for some constant C not depending on x.


Let f be a function in the Bernstein space B(Ω), where Ω := {x : |x| a/4}. Let ϕ be a Schwartz function such that ϕ(0) = 1 and spec(ϕ) is contained in the open unit ball. Then fδ(x) := f(x)ϕ(δx) is a Schwartz function, and spec(fδ) ⊂ Ba/4+δ. Hence

fδ(x) = fδ(t) e2πi x,t dt = fδ(t) νx(t) dt = fδ dνx . Letting δ → 0 it follows (e.g. by the bounded convergence theorem) that

![image 19](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile19.png>)

![image 20](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile20.png>)

f(x) = f dνx , and hence

![image 21](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile21.png>)

|f(x)| C sup

λ∈Λ

|f(λ)|.

As this holds for any f ∈ B(Ω), we get that Λ is a sampling set for B(Ω). By Landau’s theorem we therefore have D−(Λ) mes(Ω) = c(a, n), and this proves the claim.

- 4.3.


- Lemma 7. Given a > 0 there is R = R(a, n) such that, if a measure ν is supported by a u.d. set Q in Rn, d(Q) > a, and if ν vanishes on a ball of radius R, then ν = 0.


Proof. This follows from Ingham type theorems used in interpolation theory in Rn. Given a > 0 there is R = R(a, n) such that if Q is any u.d. set in Rn, d(Q) > a, then Q is an interpolation set for the Bernstein space B(Ω), where Ω := {x : |x| R/2} (see for example [24]).

Let ν be a measure supported by Q and such that the distribution ν vanishes on

BR (there is no loss of generality in assuming that the ball is centered at the origin). Given λ ∈ Q one can ﬁnd f ∈ B(Ω) such that f(λ) = 1 and f(λ′) = 0 for any λ′ ∈ Q,

λ′ = λ. Let ϕ(x) := f(x)ψ(x), where ψ is a Schwartz function such that ψ(λ) = 1 and spec(ψ) ⊂ BR/2. Then ϕ is a Schwartz function, satisfying

ϕ(λ) = 1, ϕ(λ′) = 0 (λ′ ∈ Q, λ′ = λ), spec(ϕ) ⊂ BR. It follows that

![image 22](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile22.png>)

ν(λ) = ϕdν = ν, ϕ = 0. As this holds for any λ ∈ Q, we obtain ν = 0.

![image 23](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile23.png>)

5. Delone and Meyer sets

- 5.1. We will need the following concepts of Delone and Meyer sets in Rn.


- Deﬁnition 1. Λ is called a Delone set if Λ is both a u.d. and relatively dense set.
- Deﬁnition 2. Λ is called a Meyer set if the following two conditions are satisﬁed:


- (i) Λ is a Delone set;
- (ii) There is a ﬁnite set F such that Λ − Λ ⊂ Λ + F.


Meyer [18, 19] discovered important connections of this class of sets to certain problems in harmonic analysis. In particular, to the characterization of classes of almostperiodic functions with common almost-periods, and to the concepts of Pisot and Salem numbers in algebraic number theory.

- 5.2. Meyer observed that a Delone set Λ is a Meyer set if and only if Λ −Λ−Λ is u.d. (see [19]).


Lagarias [12] proved that if Λ is a Delone set and Λ−Λ is u.d. then Λ is a Meyer set. We need a stronger version of this result:

- Lemma 8. Let Λ ⊂ Rn be a Delone set, such that D+(Λ−Λ) < ∞. Then Λ is a Meyer set.


The proof below follows Lagarias’ argument, and simpliﬁes it, basing also on [21] (see also [2]). Proof of Lemma 8. By translation we may assume that 0 ∈ Λ. We ﬁx R > 0 such that every ball of radius R intersects Λ.

Let h ∈ Λ − Λ. Then h = y − x for some x, y ∈ Λ. Choose a sequence x0, x1, . . ., xs such that x0 = x, xs = 0, |xi − xi+1| < R. Deﬁne yi = xi + h, then y0 = y, ys = h, |yi − yi+1| < R. Choose pi, qi ∈ Λ such that |pi − xi| < R, |qi − yi| < R (0 i s), where p0 = x, q0 = y and ps = 0 (recall that 0 ∈ Λ). It follows that pi − pi+1 and qi − qi+1 belong to the ﬁnite set F1 := (Λ − Λ) ∩ B3R.

Set hi := qi − pi. Then

hi − hi+1 = (qi − qi+1) − (pi − pi+1) ∈ F2 := F1 − F1. Also

|hi − h| = |(qi − yi) − (pi − xi)| < 2R, hence

hi ∈ V (h) := (Λ − Λ) ∩ (h + B2R).

Since D+(Λ−Λ) < ∞, there is a constant M independent of h such that #V (h) M. Thus in the sequence h0, h1, . . ., hs appear at most M distinct values. Write

h0 − hs = (h0 − h1) + (h1 − h2) + · · · + (hs−1 − hs).

If some hi and hj (i < j) admit the same value, then we may remove from the sum above all the terms (hk −hk+1), i k < j. By removing all such “cycles” it follows that h0 − hs belongs to the ﬁnite set F consisting of all vectors which may be expressed as the sum of at most M − 1 elements from F2. Hence

h = h0 = h0 + (qs − hs) = qs + (h0 − hs) ∈ Λ + F. This proves that Λ − Λ ⊂ Λ + F, so Λ is a Meyer set.

- 5.3. Let Γ be a lattice in Rn+m = Rn × Rm (m 0), and let p1 and p2 denote the projections onto Rn and Rm, respectively. We assume that the restriction of p1 to Γ is injective, and that p2(Γ) is dense in Rm. Let Ω be a bounded set in Rm.

Deﬁnition 3. Under the assumptions above, the set

M(Rn × Rm, Γ, Ω) := {p1(γ) : γ ∈ Γ, p2(γ) ∈ Ω}, (8) is called the model set deﬁned by Γ and Ω.

This construction is known as “cut-and-project”. Remark that the case m = 0 is not excluded in the above deﬁnition. In this case one

should understand Rm to be {0}, and the model set obtained is just a lattice in Rn.

The following theorem [18, Sections II.5, II.14] gives a characterization of Meyer sets in terms of model sets (see also [21]). Theorem M (Meyer). Let Λ be a Delone set in Rn. Then the following are equivalent:

- (i) Λ is a Meyer set;
- (ii) There exists a model set M and a ﬁnite set F such that Λ ⊂ M + F.


- 5.4.

Lemma 9. Let M = M(Rn × Rm, Γ, Ω) be a model set in Rn, and suppose that the boundary of Ω is a set of Lebesgue measure zero in Rm. Then

D−(M) = D+(M) =

mes(Ω) det(Γ)

![image 24](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile24.png>)

.

This fact is well-known, see for example [16, Proposition 5.1].

- 5.5. For a set A ⊂ Rn we shall denote by Z[A] the additive group generated by the elements of A.


- Lemma 10. Let M = M(Rn × Rm, Γ, Ω) be a model set, and F be a ﬁnite set in Rn. Then there is another model set M′ = M(Rn × Rm, Γ′, Ω′) and a ﬁnite set F′, such that


M + F ⊂ M′ + F′, p1(Γ′) ∩ Z[F′] = {0}, Γ ⊂ Γ′.

Proof. The elements of F generate a ﬁnite-dimensional vector space over the rationals Q, which we denote by V = Q[F]. Let U := V ∩ Q[p1(Γ)], a linear subspace of V . Let W be any linear subspace of V such that U ⊕ W = V .

Denote by θ1, . . ., θs the elements of F. Then each θj admits a unique representation as θj = uj + wj, where uj ∈ U, wj ∈ W. Since U ⊂ Q[p1(Γ)] we may ﬁnd a non-zero integer q and elements γ1, . . ., γs ∈ Γ such that uj = p1(γj/q), 1 j s. Deﬁne

Γ′ := (1/q)Γ, Ω′ :=

s

(Ω + p2(γj/q)), F′ := {w1, . . ., ws}.

j=1

Then Γ′ is a lattice in Rn × Rm, the restriction of p1 to Γ′ is injective, and p2(Γ′) is dense in Rm. The set Ω′ is a bounded set in Rm, and F′ is a ﬁnite set in Rn.

Let M′ be the model set deﬁned by Γ′ and Ω′. We show that M + F ⊂ M′ + F′. Indeed, an element λ ∈ M +F is of the form λ = p1(γ)+θj, where γ ∈ Γ and p2(γ) ∈ Ω. Set γ′ := γ + γj/q, then γ′ ∈ Γ′ and p2(γ′) ∈ Ω′. Hence

λ = p1(γ′) + wj ∈ M′ + F′.

Finally, observe that the set p1(Γ′)∩ Z[F′] must be equal to {0}, since it is contained in both U and W. It is also clear that Γ ⊂ Γ′, and so the lemma is proved.

Notice that in the special case when m = 0, Lemma 10 reduces to:

Corollary 11. Let L be a lattice, and F be a ﬁnite set in Rn. Then there is another lattice L′ and a ﬁnite set F′, such that L + F ⊂ L′ + F′, L′ ∩ Z[F′] = {0}, L ⊂ L′.

6. Proof of Theorems 1 and 2

- 6.1. We will use the following notation: for h ∈ Λ − Λ, denote Λh := Λ ∩ (Λ − h) = {λ ∈ Λ : λ + h ∈ Λ}.


Clearly Λh is a non-empty subset of Λ.

Let µ be a measure in Rn satisfying (2) and (3). For each h ∈ Λ − Λ we introduce a new measure

![image 25](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile25.png>)

µ(λ) µ(λ + h) δλ. (9)

µh :=

λ∈Λh

Clearly it is a non-zero measure with supp(µh) = Λh and with bounded atoms (by Lemma 2), so it is a temperate distribution.

- Lemma 12. Let a := d(S) > 0. Then we have spec(µh) ∩ Ba ⊂ {0}, that is, the punctured ball Ba \ {0} is free from the spectrum of the measure µh.


Proof. We ﬁx a Schwartz function ϕ on Rn, such that ϕ(0) = 1, and whose spectrum is contained in the open unit ball. Denote ϕδ(x) := ϕ(δx).

Let u ∈ Rn. Consider the measure

![image 26](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile26.png>)

( ϕδ ∗ µ)(t + u) · µ(t). (10) It is a temperate distribution, supported by the set S ∩ (S − u + Bδ). Hence, if

u ∈ Uδ := Rn \ [(S − S) + Bδ], then the measure in (10) vanishes identically.

Now consider the Fourier transform of the measure (10). It is the measure [e2πi u,x ϕδ(−x)µ(−x)] ∗ µ(x) =

![image 27](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile27.png>)

![image 28](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile28.png>)

e−2πi u,λ ϕδ(λ)µ(λ)µ(λ′)δλ′−λ

λ∈Λ λ′∈Λ

![image 29](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile29.png>)

e−2πi u,λ ϕδ(λ)µ(λ)µ(λ + h) δh

=

h∈Λ−Λ λ∈Λh

=

(ϕδ · µh) (u) · δh.

h∈Λ−Λ

It follows that for every h ∈ Λ − Λ we have (ϕδ · µh) (u) = 0, u ∈ Uδ.

The ﬁnite measure ϕδ · µh tends to µh (in the sense of temperate distributions) as δ → 0. This implies that spec(µh) is contained in the closure of the set S − S, which is disjoint from Ba \ {0}. The lemma is therefore proved.

Remark. If µ is a positive measure, then so is µh. Hence in this case Lemmas 3 and 12 imply that the distribution µh has an isolated atom at the origin.

- 6.2.


- Lemma 13. Let Λ be a u.d. set in Rn. Suppose there is c = c(Λ) > 0 such that D#(Λh) > c for every h ∈ Λ − Λ. Then D+(Λ − Λ) < ∞.

Proof. Let x ∈ Rn. Suppose that h1, . . ., hN are distinct vectors belonging to the set (Λ − Λ) ∩ (x + Bδ), where δ := d(Λ)/2 > 0. If λ ∈ Λh

i

∩ Λh

j

(i = j) then hi − hj = (λ + hi) − (λ + hj) ∈ (Λ − Λ) ∩ B2δ = {0},

which is not possible. Hence Λh

1

, . . ., Λh

N

are pairwise disjoint subsets of Λ. Since the density D# is super-additive, it follows that

D#(Λ)

N

j=1

D#(Λh

j

) cN.

This shows that the set Λ − Λ cannot have more than D#(Λ)/c elements in any ball of radius δ, thus D+(Λ − Λ) < ∞.

6.3.

- Lemma 14. Let E be a bounded set in Rm, and let ξ be a vector in E − E such that |ξ|2 > (diamE)2 − δ2


for some δ > 0. Suppose that we are given two representations of ξ as the diﬀerence of two elements from E:

ξ = y1 − x1 = y2 − x2, x1, y1, x2, y2 ∈ E.

Then |x1 − x2| < δ. Proof. By the parallelogram law we have

- 1

![image 30](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile30.png>)

- 2


|ξ|2 + |x1 − x2|2 =

(|y1 − x2|2 + |y2 − x1|2) (diamE)2, so the claim follows.

- 6.4.


- Lemma 15. Let Λ be a Meyer set in Rn. Suppose there is c = c(Λ) > 0 such that D+(Λh) > c (11)


for every h ∈ Λ−Λ. Then Λ is contained in a ﬁnite union of translates of some lattice. Proof. (i) By Theorem M there exists a model set M = M(Rn × Rm, Γ, Ω) and a ﬁnite set F such that Λ ⊂ M + F. By Lemma 10 we may suppose that

p1(Γ) ∩ Z[F] = {0}. (12) Thus each λ ∈ Λ admits a unique representation as

λ = p1(γ(λ)) + θ(λ), γ(λ) ∈ Γ, p2(γ(λ)) ∈ Ω, θ(λ) ∈ F. (13) The uniqueness follows from (12) and the fact that the restriction of p1 to Γ is injective.

(ii) Let h ∈ Λ − Λ, and suppose that λ1, λ2 ∈ Λh. Denote

λ′j := λj + h, j = 1, 2. Then from (13) we have

h = λ′j − λj = p1(γ(λ′j) − γ(λj)) + (θ(λ′j) − θ(λj)), j = 1, 2. The condition (12) implies that the representation of h as the sum of an element from p1(Γ) and an element from F − F is unique. Hence, we must have

p1(γ(λ′1) − γ(λ1)) = p1(γ(λ′2) − γ(λ2)). Since the restriction of p1 to Γ is injective, this implies

γ(λ′1) − γ(λ1) = γ(λ′2) − γ(λ2). We thus obtain the following: to each h ∈ Λ−Λ there corresponds an element H(h) ∈ Γ such that

γ(λ + h) − γ(λ) = H(h), λ ∈ Λh. (14) (iii) Let E := {p2(γ(λ)) : λ ∈ Λ}. Then E is a bounded set in Rm, E ⊂ Ω. Given

δ > 0, we may choose a vector ξ ∈ E −E such that |ξ|2 > (diamE)2 −δ2. Observe that E − E = {p2(H(h)) : h ∈ Λ − Λ},

hence ξ = p2(H(h)) for some h ∈ Λ − Λ. Let us ﬁx such an h. Now suppose that λ1, λ2 ∈ Λh. Then by (14) we have H(h) = γ(λj + h) − γ(λj), j = 1, 2. This yields two representations of ξ as the diﬀerence of two elements from E:

ξ = p2(H(h)) = p2(γ(λj + h)) − p2(γ(λj)), j = 1, 2. By Lemma 14 we must therefore have

|p2(γ(λ2)) − p2(γ(λ1))| < δ. Hence, we conclude the following: denote

E(h) := {p2(γ(λ)) : λ ∈ Λh}. (15) Then, given any δ > 0 one can ﬁnd h ∈ Λ − Λ such that diam(E(h)) < δ.

(iv) Let h ∈ Λ − Λ, and suppose that diam(E(h)) < δ for some δ > 0. We may ﬁnd an open ball Ω′ of radius δ such that E(h) ⊂ Ω′. Consider the model set

M′ = M(Rn × Rm, Γ, Ω′).

Then by (8), (13) and (15) we have Λh ⊂ M′ + F. Since the density D+ is sub-additive and invariant under translations, this implies

D+(Λh) #F · D+(M′). Recall that D+(M′) = (det Γ)−1|Ω′|, according to Lemma 9. Hence

cmδm detΓ

D+(Λh) #F ·

, where cm denotes the volume of the unit ball in Rm.

![image 31](<2013-lev-quasicrystals-poisson-summation-formula_images/imageFile31.png>)

(v) It follows from (iii),(iv) that if m 1, then we may ﬁnd elements h ∈ Λ− Λ with D+(Λh) arbitrarily small, in contradiction to (11). Hence we must have m = 0, that is, M must be a lattice. Thus M + F is a ﬁnite union of translates of a lattice. Since Λ ⊂ M + F, this concludes the proof.

- 6.5. Now we can ﬁnish the proof of Theorems 1 and 2.


Proof of Theorems 1 and 2. For each h ∈ Λ − Λ, let µh be the measure deﬁned by (9). Then µh is a non-zero measure, supp(µh) = Λh, and supλ |µh(λ)| < ∞ (by Lemma 2).

By Lemma 12 we have

spec(µh) ∩ Ba ⊂ {0}, (16) where a = d(S) > 0.

In the one-dimensional case n = 1, observe that condition (16) implies that µh vanishes on the open interval (0, a). So we may use Proposition 4 which gives

D#(Λh) c, h ∈ Λ − Λ, (17) where c > 0 is a constant which depends on d(Λ) and d(S).

In the multi-dimensional case n > 1, we use the extra assumption that µ is a positive measure. It implies that µh is also positive, for every h ∈ Λ − Λ. By Lemma 3 we therefore have 0 ∈ spec(µh), so spec(µh) ∩ Ba = {0}. This allows us to use Lemma 6, which gives that D−(Λh) c, where c > 0 is a constant which now depends on d(S) only. Since D#(Λh) D−(Λh), we obtain (17) again.

With (17) established, we now proceed to apply Lemma 13 which gives

D+(Λ − Λ) < ∞. (18) Also, using Lemma 7 with Q = S and ν = µ gives that Λ is a relatively dense set.

Hence Λ is a Delone set (see also [6, Lemma 1]). This together with (18) gives, by Lemma 8, that Λ is a Meyer set. Finally, we apply Lemma 15. Since from (17) we get D+(Λh) c for every h ∈ Λ−Λ,

the lemma gives that Λ is contained in a ﬁnite union of translates of some lattice, and this completes the proof.

7. Proof of Theorem 3

- 7.1.


- Lemma 16. Let θ ∈ Rn \ Qn. Then the set H(θ) := {m ∈ Zn : θ, m ∈ Z}


is contained in some (n − 1)-dimensional hyperplane.

Proof. Deﬁne V (θ) := {x ∈ Qn : θ, x ∈ Q}. It is a linear subspace of Qn over the rationals. Since θ ∈/ Qn, this subspace cannot contain all the standard basis vectors e1, . . ., en. Hence V (θ) is a proper subspace of Qn, and so it is necessarily contained in some (n − 1)-dimensional hyperplane. But H(θ) ⊂ V (θ), so this proves the claim.

Since the union of a ﬁnite number of hyperplanes cannot cover Zn, it follows that: Corollary 17. Let θ1, . . ., θs ∈ Rn \ Qn. Then there is m ∈ Zn such that

θj, m ∈ / Z, 1 j s.

- 7.2.


Proof of Theorem 3. We suppose that µ is a measure in Rn (n 1) satisfying (2) and (3), and that the support of µ is contained in a ﬁnite union of translates of a lattice L.

Using Corollary 11 we can ﬁnd a larger lattice L′ ⊃ L and a ﬁnite set F′ such that L′ ∩Z[F′] = {0}, and the support of µ is contained in L′ +F′. We will show that µ can be represented in the form (4) with the lattice L′. The desired representation with the original lattice can be obtained by covering L′ with a ﬁnite number of translates of L.

It will be enough, by applying a linear transformation, to consider the case L′ = Zn. Denote by θ1, . . ., θs the elements of F′. For each j = 1, . . ., s deﬁne a measure

µ(k + θj) δk.

µj :=

k∈Zn

It is a temperate distribution (by Lemma 2) supported by Zn, and we have

µ(x) =

s

µj(x − θj). (19)

j=1

The Fourier transform µj is a temperate distribution on Rn which is Zn-periodic. Deﬁne a distribution

j,t µj(t). (20) From (19), (20) and the periodicity of µj it follows that

αj(t) := e−2πi θ

s

µ(t − k) =

j=1

e2πi θ

j,k αj(t) (21)

for each k ∈ Zn. Since Zn ∩ Z[θ1, . . ., θs] = {0}, we have θj − θℓ ∈/ Qn (j = ℓ). Using Corollary 17, we may therefore choose a vector m ∈ Zn such that θj − θℓ, m ∈ / Z (j = ℓ). (22)

Applying (21) with k = pm (p = 0, 1, 2, . . ., s − 1) yields a system of s linear equations, with a Vandermonde determinant that does not vanish due to (22). Hence this linear system may be inverted, and we obtain that

s−1

αj(t) =

cjp µ(t − pm)

p=0

for appropriate coeﬃcients {cjp}.

But now using (20) this implies that the distribution µj is a measure, supported by the closed, discrete set S + {0, m, 2m, . . ., (s − 1)m}. On the other hand, the measure µj is Zn-periodic. Hence it must be of the form

δk,

µj = νj ∗

k∈Zn

where νj is a measure which is a ﬁnite sum of point masses. It follows that µj(x) = Pj(x)

δk

k∈Zn

where Pj is a trigonometric polynomial, Pj(x) = νj(−x). By (19) this completes the proof of Theorem 3.

8. Remarks

1. Theorems 1 and 2 give an aﬃrmative answer to Problem 4.1(a) in [13, p. 79]. The Problem 4.1(b) from that paper, asking whether one can remove the uniformity requirement for discrete sets Λ and S, remains open. For signed (not positive) measures, one may expect a counter-example due to the results in [8].

We also leave open the problem whether Theorem 2 holds for non-positive measures. In [15] we proved this under the additional assumption that S − S is a u.d. set.

2. It is well-known that if one requires from S in Theorems 1 and 2 to be just a countable (non-discrete) set, then the result fails. As an example one may take the model set deﬁned by (8) (with m 1). It is a u.d. set, which supports a positive measure µ whose Fourier transform is a sum of point masses (see [19]), but is not contained in a ﬁnite union of translates of a lattice.

- 3. It is likely that our proofs can be extended to the more general context of locally

compact abelian groups. We do not attempt to work out the details in this paper.

- 4. Sometimes diﬀerent approaches to mathematical models of quasicrystals are con-


sidered. In particular, inspired by the Fibonacci sequence, one may look at the “block complexity” of a u.d. sequence in R, characterized by the number of distinct blocks of given length occurring in the sequence, see [1], [3] and the references therein. It seems to be interesting to investigate the spectral properties of measures supported by sequences with “low complexity”.

References

- [1] J.-P. Allouche, Y. Meyer, Quasicrystals, model sets, and automatic sequences. C. R. Physique 15

(2014), 6–11.

- [2] M. Baake, D. Lenz, R. Moody, Characterization of model sets by dynamical systems. Ergod. Th. and Dynam. Sys. 27 (2007), 341–382.


- [3] E. Bombieri, J. E. Taylor, Quasicrystals, tilings, and algebraic number theory: some preliminary connections. The legacy of Sonya Kovalevskaya, Contemp. Math., vol. 64, Amer. Math. Soc., Providence, RI, 1987, pp. 241–264.
- [4] J. W. Cahn, J. E. Taylor, An introduction to quasicrystals. The legacy of Sonya Kovalevskaya, Contemp. Math., vol. 64, Amer. Math. Soc., Providence, RI, 1987, pp. 265–286.
- [5] A. C´rdoba, La formule sommatoire de Poisson. C. R. Acad. Sci. Paris S´er. I Math. 306 (1988), 373–376.
- [6] A. C´ordoba, Dirac combs. Lett. Math. Phys. 17 (1989), 191–196.
- [7] F. Dyson, Birds and frogs. Notices Amer. Math. Soc. 56 (2009), 212–223.
- [8] A. P. Guinand, Concordance and the harmonic analysis of sequences. Acta Math. 101 (1959), 235–271.
- [9] V. P. Gurarii, Group methods of commutative harmonic analysis. Current problems in mathematics. Fundamental directions. Vol. 25 (Russian) Akad. Nauk SSSR, Vsesoyuz. Inst. Nauchn. i Tekhn. Inform., Moscow, 1988. English translation in Commutative harmonic analysis II, edited by V. P. Havin and N. K. Nikolski. Springer-Verlag, Berlin, 1998.
- [10] J.-P. Kahane, S. Mandelbrojt, Sur l’´equation fonctionnelle de Riemann et la formule sommatoire de Poisson. Ann. Sci. Ecole´ Norm. Sup. 75 (1958), 57–80.
- [11] M. N. Kolountzakis, J. C. Lagarias, Structure of tilings of the line by a function. Duke Math. J. 82 (1996), 653–678.
- [12] J. C. Lagarias, Meyer’s concept of quasicrystal and quasiregular sets. Comm. Math. Phys. 179

(1996), 365–376.

- [13] J. C. Lagarias, Mathematical quasicrystals and the problem of diﬀraction. Directions in mathematical quasicrystals, 61–93, CRM Monogr. Ser., 13, Amer. Math. Soc., Providence, 2000.
- [14] H. J. Landau, Necessary density conditions for sampling and interpolation of certain entire functions. Acta Math. 117 (1967), 37–52.
- [15] N. Lev, A. Olevskii, Measures with uniformly discrete support and spectrum. C. R. Math. Acad. Sci. Paris 351 (2013), 613–617.
- [16] B. Matei, Y. Meyer, Simple quasicrystals are sets of stable sampling. Complex Var. Elliptic Equ. 55 (2010), 947–964.
- [17] Y. Meyer, Nombres de Pisot, nombres de Salem et analyse harmonique. Lecture Notes in Mathematics 117, Springer-Verlag, 1970.
- [18] Y. Meyer, Algebraic numbers and harmonic analysis. North-Holland, Amsterdam, 1972.
- [19] Y. Meyer, Quasicrystals, diophantine approximation and algebraic numbers. Beyond quasicrystals (Les Houches, 1994), 3–16, Springer, Berlin, 1995.
- [20] M. Mitkovski, A. Poltoratski, Po´lya sequences, Toeplitz kernels and gap theorems. Adv. Math. 224 (2010), 1057–1070.
- [21] R. V. Moody, Meyer sets and their duals. The mathematics of long-range aperiodic order (Waterloo, ON, 1995), 403–441, NATO Adv. Sci. Inst. Ser. C Math. Phys. Sci., 489, Kluwer Acad. Publ., Dordrecht, 1997.
- [22] S. Nitzan, A. Olevskii, Revisiting Landau’s density theorems for Paley-Wiener spaces. C. R. Math. Acad. Sci. Paris 350 (2012), 509–512.
- [23] A. Olevskii, A. Ulanovskii, Universal sampling and interpolation of band-limited signals. Geom. Funct. Anal. 18 (2008), 1029–1052.
- [24] A. Olevskii, A. Ulanovskii, On multi-dimensional sampling and interpolation. Anal. Math. Phys. 2 (2012), 149–170.
- [25] W. Rudin, Functional analysis. Second edition. McGraw-Hill, New York, 1991.


Department of Mathematics, Bar-Ilan University, Ramat-Gan 52900, Israel E-mail address: levnir@math.biu.ac.il

School of Mathematical Sciences, Tel-Aviv University, Tel-Aviv 69978, Israel E-mail address: olevskii@post.tau.ac.il

