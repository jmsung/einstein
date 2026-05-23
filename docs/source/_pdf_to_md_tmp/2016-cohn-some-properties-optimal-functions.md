# arXiv:1603.04759v1[math.MG]15Mar2016

## SOME PROPERTIES OF OPTIMAL FUNCTIONS FOR SPHERE PACKING IN DIMENSIONS 8 AND 24

HENRY COHN AND STEPHEN D. MILLER

Abstract. We study some sequences of functions of one real variable and conjecture that they converge uniformly to functions with certain positivity and growth properties. Our conjectures imply a conjecture of Cohn and Elkies, which in turn implies the complete solution to the sphere packing problem in dimensions 8 and 24. We give numerical evidence for these conjectures as well as some arithmetic properties of the hypothetical limiting functions. The conjectures are of greatest interest in dimension 24, in light of Viazovska’s recent solution to the Cohn-Elkies conjecture (and consequently the sphere packing problem) in dimension 8.

1. Introduction

One of the fundamental problems in geometry is to determine the densest sphere packing in Euclidean space. In other words, how large a fraction of Rn can be covered by equal-sized, non-overlapping balls? The answer is known so far only for n ≤ 3 (see [FT] and [H]), and very recently for n = 8 as well [V]. A remarkable feature of this problem is that each dimension has its own idiosyncrasies. Even setting aside the issue of proofs, the best packings known do not seem to follow any simple pattern.

Perhaps the most striking packings are those formed by centering spheres at the points of the E8 root lattice and the Leech lattice. Both have been known for some years now to be the densest lattice packings in their dimensions. The E8 case was proved by Blichfeldt in his 1935 paper [B], and the Leech lattice case was proved by Cohn and Kumar in [CK3] (see also [CK1]). The latter work was based on an analytic approach introduced in [CE] by Cohn and Elkies, who in fact studied the general sphere packing problem (including non-lattice packings, which may improve on the density of lattice packings in some dimensions). Cohn and Elkies proved that E8 and the Leech lattice are optimal among all sphere packings if there exist functions from R to R satisfying certain sign and regularity conditions; they furthermore conjectured that such functions do indeed exist. In this paper we introduce explicit sequences of functions which we conjecture converge to functions satisfying the Cohn-Elkies conditions. (We of course note that the n = 8 case of the Cohn-Elkies conjecture was solved in [V].)

Our functions depend on a parameter n, the dimension of the sphere packing problem. One advantage of our approach is that our conjectures appear to hold for a broader range of values of n, not only for n = 8 and n = 24. Although they have no sphere packing implications except in those two cases, existence might be easier

Date: March 15, 2016. Miller was partially supported by NSF grant DMS-1201362 and an Alfred P. Sloan Foundation

Fellowship.

1

to prove because they no longer depend on delicate facts about these particular dimensions.

A second advantage is that our approach does not rely on numerical optimization. By contrast, the Leech lattice optimality proof makes use of a carefully optimized polynomial of degree 803 with 3000-digit coeﬃcients. The computer-assisted proof in [CK3] reads this polynomial from a ﬁle and veriﬁes that it has the desired properties to complete the proof, but there is no conceptual description of the polynomial or simple method to construct it from scratch. (It was found by combining numerous ad hoc techniques to locate a starting point from which Newton’s method would converge.) Using our approach, one could replace this complicated polynomial with a polynomial that has a much simpler description. That would not remove the need for computer veriﬁcation of its properties, but it is a step towards simplifying the proof.

Our lack of need for optimization also enables us to carry out much larger computations than in previous papers. For example, we arrive at density bounds that are sharp to over ﬁfty decimal places in R8 and R24, compared with the fourteen and twenty-nine decimal places from [CK3]. Strictly speaking our new bounds are not theorems, because we have not bothered to verify them using exact arithmetic, but our ﬂoating point calculations leave no reasonable doubt. We are conﬁdent that the approach from Appendix A in [CK3] could be used to provide a proof (should a rigorous bound be needed for some purpose).

The results of these large calculations display intricate and surprising structure. Most interestingly, in Section 5 we ﬁnd that the second Taylor coeﬃcients appear to be rational. If the pattern governing the higher coeﬃcients could be identiﬁed, it would yield a direct construction by power series of functions satisfying the Cohn-Elkies conjecture.

In the next section we review background from [CE]. Our functions are introduced in Section 3. In Section 4, we provide experimental evidence that our sequences of functions are converging rapidly (despite the failure of a related, naive construction), and we study this numerical data in detail. In Section 5 we examine the Taylor coeﬃcients and values of the Mellin transform of the optimal functions, both of which exhibit some unexplained rationality properties. In Section 6 we study the closely related problem of potential energy minimization. Finally we conclude in Section 7 by describing some related but simpler sequences of functions, which serve as a testing ground for our main conjectures.

2. Background Deﬁne the Fourier transform of a function f : Rn → R by

f(x)e−2πi x,t dx.

- (2.1) f(t) = Rn


We call a continuous function f admissible if both |f(x)| and | f(x)| are bounded by a constant times (1 + |x|)−n−δ for some δ > 0. This bound ensures, for example, that the integral deﬁning f converges. It also guarantees that both sides of the Poisson summation formula

1 |Λ| t∈Λ

f(x) =

### f(t)

∗

x∈Λ

converge absolutely and are equal. Here Λ denotes a lattice in Rn, Λ∗ = {t ∈ Rn : t,x ∈ Z for all x ∈ Λ} its dual, and |Λ| = vol(Rn/Λ) its covolume.

Our primary connection between sphere packing and Fourier analysis is the following theorem of Cohn and Elkies (Theorem 3.1 in [CE]; see also [C1]): Theorem 2.1. Suppose there exists an admissible function f : Rn → R and a constant r such that

- (1) f(0) = f(0) = 0,
- (2) f(x) ≤ 0 for |x| ≥ r, and
- (3) f(t) ≥ 0 for all t.


Then every sphere packing in Rn has density at most

πn/2 (n/2)!

n

r 2

.

As usual (n/2)! is to be interpreted as Γ(n/2 + 1) when n is odd. The density of a sphere packing refers to the fraction of space covered by the packing.

We will brieﬂy explain how to prove Theorem 2.1 using Poisson summation, because the conditions for a sharp bound will be important later in the paper. Proof. First, we give the proof for lattice packings, after which we will sketch the general proof.

Suppose Λ ⊂ Rn is a lattice. We can assume without loss of generality that the minimal nonzero vector length in Λ is r, because sphere packing density is invariant under scaling. That amounts to using balls of radius r/2 in the sphere packing.

By Poisson summation,

1 |Λ| t∈Λ

f(x) =

f(t).

∗

x∈Λ

Applying the inequalities on f and f yields

1 |Λ| t∈Λ

f(0) |Λ|

f(0) ≥

f(t) ≥

.

f(x) =

∗

x∈Λ

Thus,

|Λ| ≥ 1.

In other words, there is at most one lattice point per unit volume in Rn. It follows that the density is at most the volume of a sphere of radius r/2, i.e.,

πn/2 (n/2)!

r 2

n

(because the density equals the volume of a sphere times the number of spheres per unit volume in space).

For the general case, one can assume without loss of generality that the sphere packing is periodic, i.e., a union of translates of a lattice packing. Suppose it is the disjoint union of Λ + v1,...,Λ + vn. Then applying the identity

2

N

N

1 |Λ| t∈Λ

e2πi v

j,t

f(x + vj − vk) =

### ,

f(t)

∗

j,k=1 x∈Λ

j=1

which follows from Poisson summation and some manipulation, completes the proof

- as above.


One can weaken the hypothesis of admissibility in this theorem, at the cost of complicating the proof (see Proposition 9.3 in [CK2], which is set in the more general context of potential energy minimization, or the proof in [CZ2], which does not even use Poisson summation). However, the applications in this paper will use only admissible functions.

Unfortunately, Theorem 2.1 does not address the issue of how to ﬁnd functions f that lead to good sphere packing bounds (i.e., that minimize r). Doing so amounts to grappling with an inﬁnite-dimensional optimization problem, which has a simple solution when n = 1 but is unsolved and appears diﬃcult for n > 1. Cohn and Elkies performed a computer search to locate explicit functions that improve on the previously known density upper bounds for 4 ≤ n ≤ 36. (For 4 ≤ n ≤ 7 and n = 9, a reﬁnement of this approach from [LOV] yields slightly better bounds.) These functions are probably nearly optimal in terms of minimizing the values r achieved by functions satisfying the hypotheses of Theorem 2.1. However, in most cases these bounds are still far above the densities of the best packings known.

The most remarkable application of Theorem 2.1 occurs when the dimension n is 8 or 24. In those dimensions, Cohn and Elkies found functions that come tantalizingly close to solving the sphere packing problem completely. Using more sophisticated search techniques, Cohn and Kumar [CK3] later achieved a bound within a factor of 1 + 1.65 × 10−30 of the conjectured optimum for n = 24 and a factor of 1 + 10−14 for n = 8. Typically it is harder to get more accurate bounds for larger values of n; the reason the bound for n = 24 is so much better is that Cohn and Kumar required that level of accuracy for their application and thus devoted much more computer time to optimizing this case.

One may ask whether the functions produced by these computer searches asymptotically produce a sharp sphere packing bound in these dimensions. That appears to be true, and Cohn and Elkies conjectured an even stronger statement, namely that the sphere packing problem in dimensions 2, 8, and 24 can be solved exactly by the use of a single function f in Theorem 2.1:

Conjecture 2.2 (Conjecture 7.3 in [CE]; now a theorem when n = 8 [V]). When n ∈ {2,8,24}, there exists a function f satisfying the hypotheses of Theorem 2.1 with

 

(4/3)1/4 if n = 2, √2 if n = 8, and 2 if n = 24.

r =



The sphere packing problem is of course trivial for R1, where f(x) =

2

1 1 − x2

sinπx πx

gives an optimal function for use in Theorem 2.1. At ﬁrst glance it may seem quite unlikely that Theorem 2.1 leads to a sharp sphere packing bound in any other dimension n > 1. For example, positivity arguments such as its proof (which involve dropping a number of terms to get an inequality) nearly always lose information; in analytic number theory it is essentially a given that they will not produce sharp results.

Despite this, there is ample numerical evidence that Conjecture 2.2 is true in the special dimensions n = 2, 8 (where it was proved in [V]), and 24. Similarly sharp solutions have been found for related problems in R2, R8, and R24 such as the kissing problem (see [Lev, OS]), and there are many analogies with error-correcting codes (see, for example, [CZ1]).

The main purpose of this paper is to introduce explicit sequences which we conjecture converge to functions satisfying Conjecture 2.2. We will focus on n = 8 and 24, not only because these cases are more interesting, but also because they appear to be more similar to each other than either is to the n = 2 case.

3. Explicit functions

The conditions on f in Theorem 2.1 are radially symmetric, so any function satisfying them can be rotationally symmetrized. Thus, without loss of generality we will assume that f is a radial function, and we will sometimes write f(r) for the common value f(x) with |x| = r. A convenient family of functions to consider are products of polynomials with Gaussians. If we write

2

- (3.1) f(x) = p(|x|2)e−π|x|


### with p a polynomial, then a calculation shows f(t) = (T p)(|t|2)e−π|t|

2

for some polynomial T p depending on p. In other words, T is the linear map given by

2

2

e−2πi x,t dx, which one can check maps polynomials to polynomials.

- (3.2) (T p)(|t|2) = eπ|t|


p(|x|2)e−π|x|

Rn

The functions f used in [CE] are of the form (3.1). They are created by requiring that

f(0) = f(0) = 1

and also that f and f must have forced single and double roots at certain locations. Together these can be interpreted as a set of linear conditions satisﬁed by the coeﬃcients of the polynomial p, which can be solved when the degree of p is appropriately large compared to the number of forced roots. Cohn and Elkies used a computer search to choose locations for these forced roots in order to optimize the sphere packing bound obtained from Theorem 2.1.

This procedure works well in practice, but it is diﬃcult to analyze. It is not at all obvious that these successively optimized functions f (coming from polynomials of higher and higher degree) even converge to a locally optimal choice of f, let alone the global optimum. The numerical evidence is compelling, but a proof is completely lacking.

In this paper, we examine a simpler variant of this approach. Instead of carefully optimizing the forced root locations, we specify them a priori. Specifying the roots is worse in practice, but not much worse: for example, using 200 roots we will come within a factor of 1 + 1.23 × 10−27 of the Leech lattice’s density, compared with 1+1.65×10−30 in [CK3] using 200 carefully optimized roots. Because our functions are explicit and do not involve a computer search, they can be computed more quickly and may be easier to analyze.

Table 1. Vector lengths in optimal lattices normalized with |Λ| = 1.

dimension lattice vector lengths

- 1 Z {k : k ≥ 0}
- 2 hexagonal {(4/3)1/4√k2 + k  + 2 : (k, ) ∈ Z2}


√

2k : k ≥ 0} 24 Leech {

8 E8 {

√

2k : k ≥ 0,k = 1}

In order to describe where and why we force roots of f and f, it is helpful to recall the proof of Theorem 2.1. There we proved the inequality

1 |Λ| t∈Λ

f(0) |Λ|

f(0) ≥

f(t) ≥

f(x) =

∗

x∈Λ

using the conditions that f(x) ≤ 0 for |x| ≥ r and f(t) ≥ 0 for all t. If the lattice Λ is actually the densest sphere packing in Rn, and if this method proves a sharp bound, then both inequalities must actually be equalities. For that to happen, one must ﬁrst have |Λ| = 1. (Recall that in the proof, we scaled Λ so its minimal vector length is r.) For this scaling of Λ, the terms f(x) and f(t) must vanish whenever x ∈ Λ =0 and t ∈ Λ∗ =0. In other words,

- (3.3)

f must vanish at all nonzero vector lengths, and f must vanish at all nonzero dual vector lengths.

In order to preserve the sign constraints (2) and (3) from Theorem 2.1, the order of vanishing at every vector length must be even, with the exception of f(x) at |x| = r, where a sign change should in fact occur.

Note that even if one did not assume that f is radial, it would still vanish on concentric spheres through the lattice points, not simply at the individual lattice points. This is because the above argument applies not only to Λ, but to any rotation of it; consequently, f must vanish at each rotated lattice point.

Table 1 lists the lengths of nonzero vectors in the optimal lattices in dimensions 1, 2, 8, and 24 (scaled so that |Λ| = 1, which is the usual scaling except in R2); these lattices are undoubtedly the densest sphere packings in their respective dimensions, but of course this has not been proved in 8 or 24 dimensions. For each of these lattices, the dual vector lengths are the same as the vector lengths: in each case except dimension 2, Λ∗ = Λ, and in dimension 2, Λ∗ is a rotation of Λ.

One naive approach to constructing optimal functions would be to force roots at exactly these locations. Speciﬁcally, let r1 < r2 < ... be the nonzero vector lengths in the last column of Table 1. (In other words, r1 = √2 if n = 8 and r1 = 2 if n = 24, etc.) For any integer k ≥ 1 we deﬁne the function fk(x) to be of the form

- (3.1), with p(x) = qk(x) a polynomial of degree 4k − 1, subject to the following 4k constraints:


- (3.4)


fk(0) = 1,

- fk(x) vanishes to order 1 at |x| = r1,
- fk(x) vanishes to order 2 at |x| = r2,...,rk, and fk(x) vanishes to order 2 at |x| = r1,...,rk.


Such a function is designed to satisfy the requirements of (3.3) and thereby be used in Theorem 2.1. However condition (1) of the theorem has not been addressed; i.e., we have not forced fk(0) = 1 as well. This condition in fact holds automatically for the limit f of the functions fk, provided it exists; the reason is that f and f vanish

- at all non-zero lattice points, and Poisson summation over the lattice Λ implies


f(0) = f(0) = 1. If one wishes to use the functions fk themselves to prove sphere packing bounds, then one must rescale them to force condition (1) to hold. This rescaling changes the bound to

πn/2 (n/2)!

n fk(0)

r1 2

fk(0) (i.e., it introduces a factor of fk(0)/ fk(0)).

Unfortunately, this sequence of functions fails, at ﬁrst subtly and then dramatically: the functions do not converge as k → ∞, and for suﬃciently large k they do not even prove packing bounds at all (because they develop unwanted sign changes). See Section 4 for a discussion of the numerical evidence.

Instead of using the exact vector lengths in the deﬁnition of fk, we modify them as follows. Let m denote the actual m-th vector length. Given k, we deﬁne modiﬁed root locations r1,...,rk (depending on k) as follows:

 

m if m < 2k/3 , and

- (3.5) rm =


2

2 m + 41 2k mk− − 22k/k/33



if 2k/3 ≤ m ≤ k.

In other words, the ﬁrst two-thirds of the root locations are left unchanged, while the squares of the others are perturbed by a quadratically growing amount culminating in making the ﬁnal one 25% larger. The numbers 2/3 and 1/4 in (3.5) are somewhat arbitrary, but these choices appear to work well in practice. The rescaling (3.5) was motivated by the empirical location of the roots of the optimized functions of particular degrees mentioned earlier, as well as the similar spacing of large roots of orthogonal polynomials (see [D]).

We can now use these modiﬁed root locations to deﬁne functions fk. Unlike the naive deﬁnition using m, the improved deﬁnition using rm appears to work well. In Section 4 we will examine numerical evidence and make conjectures, but before that we must resolve one theoretical issue: it is not obvious that the functions fk even exist, because the linear equations deﬁning them may have no solution. In fact, if the forced root locations r1,r2,... were chosen diﬀerently, then this diﬃculty could occur. For example, for n = 1, k = 2, r1 = 1, and r2 = 1.3403207576... (chosen to satisfy a certain polynomial equation with coeﬃcients in Q[π]), the constraints (3.4) deﬁning f2 have no solution. Fortunately, existence and uniqueness do hold in our cases:

Lemma 3.1. For any algebraic numbers 0 < r1 < ··· < rk, there exists a unique polynomial qk of degree 4k − 1 such that the constraints (3.4) hold for fk(x) = qk(|x|2)e−π|x|

2

.

For the proof of this lemma, we will need to diagonalize the transform T deﬁned in (3.2). Deﬁne pj(x) = Ljn/2−1(2πx), where Lαj is the Laguerre polynomial of degree j and index α = n/2 − 1. Recall that the polynomials Lαj are orthogonal

polynomials with respect to the measure x−αe−x dx on [0,∞), which can be written as

x−αex j!

dj dxj

(xα+je−x). The product pj(|x|2)e−π|x|

Lαj (x) =

2

is a radial eigenfunction of the Fourier transform (2.1) with eigenvalue (−1)j. In other words,

T pj = (−1)jpj.

Writing an arbitrary polynomial as a linear combination of the polynomials pj makes it easy to apply T .

Proof. Write the polynomial qk as a linear combination

4k−1

qk =

cjpj.

j=0

The constraints (3.4) amount to the following linear equations in c0,...,c4k−1:

4k−1

cjpj(0) = 1

j=0

4k−1

cjpj(2πrm2 ) = 0 for 1 ≤ m ≤ k

j=0

4k−1

cjp j(2πrm2 ) = 0 for 2 ≤ m ≤ k

- (3.6)


j=0

4k−1

(−1)jcjpj(2πrm2 ) = 0 for 1 ≤ m ≤ k

j=0

4k−1

(−1)jcjp j(2πrm2 ) = 0 for 1 ≤ m ≤ k.

j=0

To prove the lemma, we need only show that the determinant of the 4k × 4k matrix of coeﬃcients is nonzero. View the coeﬃcients as polynomials in π (recall that

pj(x) = Ln/j 2−1(2πx), where Ln/j 2−1 has coeﬃcients in Q, and that the forced root locations r1,...,rk are algebraic). We will use the transcendence of π to prove that the determinant is nonzero, by identifying its leading coeﬃcient as a polynomial in π and showing that it does not vanish.

Each column of the matrix corresponds to pj for some j, with entries of the form pj(0), pj(2πrm2 ), p j(2πrm2 ), (−1)jpj(2πrm2 ), and (−1)jp j(2πrm2 ) for suitable values of m. If we write pj as a linear combination of monomials, then we can expand the determinant as a corresponding linear combination, with the highest power of π coming from the monomial xj of highest degree. Thus, if we can show that the determinant is nonzero after replacing pj(x) with xj for all j, then it must have been nonzero to start with.

This replacement dramatically simpliﬁes the equations, because we can reinterpret them as describing a more tractable interpolation problem. The new equations ask for the coeﬃcients of a polynomial of degree 4k−1 with the following constraints. Its value at 0 is speciﬁed, its value at 2πr12 is speciﬁed, its values and ﬁrst derivatives at

2πr22,...,2πrk2 are speciﬁed, and its values and ﬁrst derivatives at −2πr12,...,−2πrk2 are speciﬁed. For the negative cases, note that replacing pj(x) with xj transforms (−1)jpj(x) into (−x)j. This interpolation problem is a special case of Hermite interpolation, and the determinant of the coeﬃcient matrix is therefore nonzero. (See Subsection 2.1 of [CK2] for a review of Hermite interpolation.)

It follows that the coeﬃcient matrix of the original equations also has a nonzero determinant, so there exists a unique solution.

4. Numerical evidence

In this section we will examine the numerical evidence for convergence. Our calculations are based on ﬂoating-point arithmetic, with no rigorous bounds on the rounding error, but we believe all reported digits are correct. (We believe that these calculations could be made rigorous if necessary, for example by using interval arithmetic or the techniques from Appendix A in [CK3].) When using k forced root locations, we carried out all computations to 8k + 75 digits of precision using PARI/GP. Experimentation suggests that 8k + 75 digits is far more precision than is actually needed, but it is easier to pick an unnecessarily high bound than to calibrate how little precision we could get away with.

First, consider the naive approach discussed in the previous section, in which one takes the forced root locations r1,...,rk to be the ﬁrst k nonzero vector lengths in the optimal lattice. Though at ﬁrst this approach gives good bounds, it subtly reverses course and eventually fails completely for large n (see Table 2). In the R8 case, the bound improves as k grows until k = 40, at which point it is slightly better than the bound proved in [CE] (and much better than the previous record bound of ≈ 1.012). However, after k = 40 the bound steadily gets worse. By k = 130, the bound would be less than 1, which is impossible and indicates that the function must have developed an unwanted sign change by that point. In the R24 case, the problems are even more dramatic.

This failure demonstrates the diﬃculty of making predictions based on limited numerical data. If one looked at only the data for k ≤ 40 and n = 8, one might reasonably conjecture that the bound was converging to 1 (although a sophisticated analysis would indicate that the convergence was happening uncomfortably slowly

- as k neared 40). This eﬀect is reminiscent of Runge’s phenomenon from interpolation theory (see

[Ep]). Although the problem is not literally overconstrained, forcing too many roots

- at the limiting locations constrains the function so much that it develops undesired oscillations to compensate. Pushing the larger roots towards inﬁnity seemingly relaxes the constraints, dampens the oscillations, and allows convergence.


We have been unable to analyze the asymptotic behavior of the functions fk deﬁned using the roots (3.5), but they lead to excellent bounds (see Table 3) and appear to converge rapidly. In what follows, we refer to fk and fk, as well as their hypothetical limits as k → ∞, as analytic functions of a radial variable.

- Conjecture 4.1. As k → ∞, fk converges to a function f and fk converges to f, on some neighborhood of the real line in C. The convergence is uniform on compact subsets of this neighborhood.


The evidence for uniform convergence is of course not as strong as that for convergence, but it implies that f and f are analytic and thus rapidly decreasing

- Table 2. Supposed upper bounds for packing density using the exact vector lengths as forced root locations, without checking for unwanted sign changes. Bounds are expressed as a multiple of the density of the optimal lattice.

k naive packing bound in R8 naive packing bound in R24

10 1.0001507518... 1.3706005433... 20 1.0000052091... 1.1082380574... 30 1.0000013138... 1.1109658270... 40 1.0000009656... 1.2417952436... 50 1.0000014330... 2.1249579472... 60 1.0000035296... −3.7219923464... 70 1.0000128440... 80 1.0000634933... 90 1.0004126231...

100 1.0031219206... 110 1.0256918168... 120 1.5572034878... 130 0.9163797290...

- Table 3. Upper bounds for packing density using the modiﬁed vector lengths as forced root locations. Bounds are expressed as a multiple of the density of the optimal lattice. Note the contrast with Table 2.


k packing bound in R8 packing bound in R24

25 1 + 2.013636284513588... × 10−10 1 + 1.276838479911905... × 10−6 50 1 + 5.356893094673532... × 10−16 1 + 4.112485306793651... × 10−11 75 1 + 2.843270958834257... × 10−20 1 + 1.034793038360603... × 10−14

100 1 + 6.131875484794015... × 10−24 1 + 6.036832814830833... × 10−18 200 1 + 7.957229644125821... × 10−35 1 + 1.224810072437178... × 10−27 300 1 + 8.043925729944741... × 10−43 1 + 6.139675825632854... × 10−35 400 1 + 1.554622153413999... × 10−49 1 + 3.603565234648839... × 10−41 500 1 + 4.477920519243749... × 10−55 1 + 2.511348284489217... × 10−46 600 1 + 6.319153710652842... × 10−60 1 + 7.276989083620164... × 10−51

(because their Fourier transforms are analytic and hence smooth). It follows that they are admissible.

As evidence for Conjecture 4.1, we oﬀer Figure 1, which demonstrates steady convergence as k increases from 30 to 100, at a selection of sample points with real parts up to 5 and imaginary parts up to 0.2. In fact, convergence seems to hold even for somewhat larger imaginary parts; for example, Table 4 shows the values at i/2. However, convergence does not occur when the imaginary part is 1 or more; for example, for n = 8 we have

f500(i) = 1786219116279967.87...

15

| |
|---|
| |
| |


N

0

30 k 100

Figure 1. Number N of digits to which the values of fk and fk

agree with those of fk−5 and fk−5 at all of the points x/10+(y/10)i, for integers 0 ≤ x ≤ 50 and 0 ≤ y ≤ 2. Data points for n = 8 are gray and those for n = 24 are black.

Table 4. Values of fk(i/2) and fk(i/2).

n k fk(i/2) fk(i/2)

8 100 0.939432541969057457603843... 0.526774741363446491086599... 8 200 0.939432541959478373173290... 0.526774741373025575517211... 8 300 0.939432541959477686529550... 0.526774741373026262160950... 8 400 0.939432541959477685343726... 0.526774741373026263346775... 8 500 0.939432541959477685338723... 0.526774741373026263351777... 8 600 0.939432541959477685338602... 0.526774741373026263351898...

24 100 0.909504018094605062955468... 0.543934528596990605074180... 24 200 0.909504017149389039571803... 0.543934529542206632888889... 24 300 0.909504017149302144551677... 0.543934529542293527909015... 24 400 0.909504017149301977449339... 0.543934529542293695011353... 24 500 0.909504017149301976704937... 0.543934529542293695755754... 24 600 0.909504017149301976686050... 0.543934529542293695774641...

while

f600(i) = 474994401497433517.69....

- Conjecture 4.2. The limiting functions f and f from Conjecture 4.1 have no real roots other than the forced roots.


When n = 24, f2 has another real root, but we have found no other case in which fk or fk has any non-forced real roots. If Conjecture 4.1 holds and there is a neighborhood of the real line into which the complex roots never intrude, then that is enough to imply Conjecture 4.2. However, it is unclear whether this stronger hypothesis is true. As one can see from the data in Table 5, the complex roots are growing steadily closer to the real axis, and they might reach it around k = 1400. Even if they eventually reach the axis, we conjecture that any unwanted sign changes will occur far from the origin and will disappear in the limit as k → ∞. It is plausible that one could remove them entirely by modifying (3.5).

Table 5. The minimal distance between the complex roots of fk or fk and the real axis.

n k minimal imaginary part for fk minimal imaginary part for fk

8 100 0.6217063862230323... 0.6217063862269778... 8 200 0.5288857517088769... 0.5288857517088764... 8 300 0.4616044778908506... 0.4616044778908506... 8 400 0.4160654620013710... 0.4160654620013710... 8 500 0.3678529442190859... 0.3678529442190859... 8 600 0.3248411054701392... 0.3248411054701392...

24 100 0.6236132212733594... 0.6236132212943291... 24 200 0.5282754706164285... 0.5282754706164232... 24 300 0.4605618680853859... 0.4605618680853859... 24 400 0.4148144356278994... 0.4148144356278994... 24 500 0.3664964681747482... 0.3664964681747482... 24 600 0.3234610116479302... 0.3234610116479302...

The complex root locations have several mysterious properties. See Figure 2 for plots with k = 600 and n = 8, and Figure 3 for plots with n = 24 (which are very similar to the n = 8 case). The roots lie on several clear curves, and they are most likely accumulating on the boundary of the domain of holomorphy. Note that their nearest approach to the real axis is quite far from the origin, as we asserted above.

One surprising observation is that fk and fk have nearly the same roots away from the origin. In the third part of these two ﬁgures, we show the roots of one of fk or fk that do not agree to six decimal places with any root of the other. Only the roots relatively near the origin appear in these plots. See also Table 5, in which the fk and fk columns become nearly identical as k grows.

For comparison, Table 6 shows the nearest roots to the origin. In each case, fk has a purely imaginary root that is probably converging as k → ∞ (the numbers show clear convergence when n = 8 and possible convergence when n = 24). The other roots are roughly paired up for fk and fk, but these pairs are not nearly as close to each other as those further from the origin. We see no reason to think any of the non-real roots are converging except for the purely imaginary roots.

It is clear from this data that the roots have considerable structure, which we are unable to explain conceptually. More data could help, but calculations for large k are very time consuming. We have computed fk and fk for k = 700, 800, and 900, but we have not located their roots. If they have no unexpected sign changes, then with k = 900 we get sphere packing bounds within a factor of 1 + 5.33 × 10−72 of the density of E8 or 1 + 3.04 × 10−62 of that of the Leech lattice. We expect that these bounds are true and could be proved given enough computing power, but the evidence is not as conclusive as it is in the cases for which we have located the roots.

It follows from Conjecture 4.2 that f and f have no unexpected sign changes. Thus, Conjectures 4.1 and 4.2 for n = 8 or 24 would solve the sphere packing problem in Rn.

It is interesting to note that the parameter n in these conjectures can be varied, while leaving the forced root locations ﬁxed. Of course there is no connection with

Figure 2. The non-real roots of f600 (above) and f600 (middle) in the right half-plane, for n = 8. The lower graph shows the points in either of the previous two graphs for which no point in the other agrees to within 10−6 in real and imaginary parts.

Table 6. The leftmost roots of fk and fk in the right half-plane. Each of the four parts of the table corresponds to the values of n and k speciﬁed in square brackets.

roots of fk roots of fk [n = 8, k = 500] ±0.6817374606...i

0.01864424055... ± 0.7968630734...i 0.01969453528... ± 0.7922341309...i 0.05589098197... ± 0.7966856319...i 0.05879879542... ± 0.7927998039...i

[n = 8, k = 600] ±0.6817374605...i

0.01690822801... ± 0.7854640419...i 0.01788437319... ± 0.7806599882...i 0.05069999170... ± 0.7853472831...i 0.05339644678... ± 0.7812202661...i

[n = 24, k = 500] ±0.7236064057...i

0.01960883579... ± 0.7855031742...i 0.02223833238... ± 0.7756885639...i 0.05877932631... ± 0.7854671622...i 0.06451464105... ± 0.7782266879...i

[n = 24, k = 600] ±0.7235866774...i 0.01772546664... ± 0.7746247816...i 0.02044183069... ± 0.7644882404...i

- 0.05314786265... ± 0.7746157584...i 0.05868760933... ± 0.7671872439...i


Figure 3. The non-real roots of f600 (above) and f600 (middle) in the right half-plane, for n = 24. The lower graph shows the points in either of the previous two graphs for which no point in the other agrees to within 10−6 in real and imaginary parts.

sphere packing for general n (it does not even have to be an integer). If a limiting f exists, it also does not follow in general that f(0) = f(0), since that requires Poisson summation over an appropriate lattice. However, the analogues of Conjectures 4.1 and 4.2 do seem to hold in all small dimensions (although we have not investigated

- them as carefully as the n = 8 and n = 24 cases). In particular, we conjecture


that if fk is deﬁned with forced roots based on the E8 vector lengths, then these conjectures hold for 0 < n < 10 (for n = 10 there in fact appear to be extraneous real roots). This ﬂexibility is encouraging, because it suggests that a proof need not depend on speciﬁc facts about R8, but rather could hold for much more general reasons. Similarly, for the Leech lattice vector lengths the conjectures seem to hold for 0 < n < 26. More generally, many of the phenomena we study in this paper are not restricted to n = 8 and n = 24. For example, we make the following conjecture:

- Conjecture 4.3. For 0 < n < 10, forcing roots at the E8 vector lengths yields a limiting function f satisfying


n4 − 56n3 + 1184n2 − 11200n + 40320 16(n − 10)(n − 14)(n − 18)

f(0) f(0)

= −

.

For 0 < n < 26, using the Leech lattice vector lengths yields instead

f(0) f(0)

p24(n) 32(n − 26)(n − 34)(n − 38)(n − 42)(n3 − 116n2 + 4480n − 57024)

= −

,

where p24(n) = n8 − 284n7 + 35312n6 − 2510720n5 + 111652352n4 − 3180064256n3

+ 56651266048n2 − 577142292480n + 2574499479552.

This conjecture is evidence that the limiting functions have even more intricate structure than is apparent just from the n = 8 and n = 24 cases.

Note that for reasons of computational eﬃciency, one should never solve the equations (3.6) directly. Instead, it is more convenient to solve two systems, each of half the size. To form them, we write the polynomial qk from the deﬁnition qk(|x|2)e−π|x|

2

of fk(x) as the sum qk0 + qk1, where

qk + (−1)εT qk 2 for ε ∈ {0,1}. Then

qkε =

T qkε = (−1)εqkε. (In other words, we have diagonalized the Fourier transform.)

We can express qk0 as a linear combination of the rescaled Laguerre polynomials pj with j even, and qk1 as a linear combination with j odd. The constraints on fk and fk amount to the following individual constraints on qkε:

- (4.1) qkε vanishes to order 1 at r12 and order 2 at r22,r32,...,rk2.


The only missing constraint is that fk must have a double root at r1 ((4.1) forces only a single root). The issue is that given only the constraints above, qk0 and qk1 are only determined up to scaling, and may be scaled independently; to produce the double root the scalings must be compatible.

The following determinant gives a formula for qkε(x), up to scaling (it follows using the approach of Lemma 3.1 that this determinant is not identically zero):

pε(x) p2+ε(x) p4+ε(x) ··· p4k−2+ε(x) pε(r12) p2+ε(r12) p4+ε(r12) ··· p4k−2+ε(r12) pε(r22) p2+ε(r22) p4+ε(r22) ··· p4k−2+ε(r22) p ε(r22) p 2+ε(r22) p 4+ε(r22) ··· p 4k−2+ε(r22) pε(r32) p2+ε(r32) p4+ε(r32) ··· p4k−2+ε(r32) p ε(r32) p 2+ε(r32) p 4+ε(r32) ··· p 4k−2+ε(r32) .

pε(rk2) p2+ε(rk2) p4+ε(rk2) ··· p4k−2+ε(rk2) p ε(rk2) p 2+ε(rk2) p 4+ε(rk2) ··· p 4k−2+ε(rk2)

It is tempting to take the limit as k → ∞ and hope to write down an inﬁnite determinant for the limiting function. However, we see no way to make sense of this idea.

Computing qk0 and qk1 independently is substantially faster than computing qk (approximately four times faster using a cubic-time algorithm). So far, it has not led to any theoretical advances, but in Section 7 we will see a closely related example in which it is theoretically important to separate the Fourier eigenfunctions.

5. Rationality

Although we are unable to identify the proposed limiting functions f for dimensions 8 and 24, we can say two things about their special values. In fact, the analysis we provide applies to the functions in the statement of Conjecture 2.2, and in particular the function explicitly exhibited in [V] for the n = 8 case. The ﬁrst is a property we can derive, while the second has been observed only numerically and so far lacks an explanation.

The ﬁrst observation is that we can predict the value of f (r1), where r1 is the ﬁrst forced root. Here we view f as a function of a single radial variable, so f is the radial derivative. By condition (3.4), knowing f (r1) means we know the values of both f and f at every vector length in the respective lattices (E8 and Leech) for dimensions 8 and 24.

Lemma 5.1. Let n ∈ {2,8,24}, and let f be a hypothetical optimal function for use in Theorem 2.1, as in Conjecture 2.2. Then

n Nr1

- (5.1) f (r1) = −


f(0), where

 

(4/3)1/4 for n = 2, √2 for n = 8, and 2 for n = 24

r1 = the minimal vector length =



and

 

6 for n = 2, 240 for n = 8, and 196560 for n = 24.

N = the number of minimal vectors =



Note that without loss of generality, we assume that f is radial. Proof. Deﬁne rescaled functions for r > 0 by

fr(x) = f(rx) and fr(t) = r−n f (t/r). Let

d dr r=1

fr(x) = |x|f (x), so that

F(x) =

F(t) = −n f(t) − t f (t). Now apply Poisson summation to F over optimal lattice Λ. Removing terms where F or F is forced to vanish, this identity states

which is (5.1).

|x|f (x) = −n f(0),

x∈Λ, |x|=r1

The second—and perhaps more interesting—feature we have noticed is that the Taylor series for f and f, normalized so that f(0) = f(0) = 1, have rational quadratic coeﬃcients. Table 7 shows numerical evidence for this. It displays the second and fourth Taylor coeﬃcients for f and f in dimensions 8 and 24. (We cannot be certain that all the reported digits are correct for the limiting functions, but they

Table 7. Approximate Taylor series coeﬃcients of f and f about 0.

n function order coeﬃcient conjecture 8 f 2 −2.7000000000000000000000000000... −27/10 8 f 2 −1.5000000000000000000000000000... −3/2

24 f 2 −2.6276556776556776556776556776... −14347/5460 24 f 2 −1.3141025641025641025641025641... −205/156

8 f 4 4.2167501240968298210998965628... ? 8 f 4 −1.2397969070295980026220596589... ?

24 f 4 3.8619903167183007758184168473... ? 24 f 4 −0.7376727789015322303799539712... ?

agree for k = 300 and k = 600.) One can see from the decimal expansions that the quadratic coeﬃcients are rational, but the quartic coeﬃcients remain mysterious.

- Conjecture 5.2. For n = 8, the limiting functions f and f have quadratic Taylor coeﬃcients −27/10 and −3/2, respectively (when normalized so that f(0) = f(0) =


- 1). For n = 24, the corresponding coeﬃcients are −14347/5460 and −205/156.


The same is true when n = 8 for the functions studied in [V]. We do not know whether the higher Taylor coeﬃcients are rational or even given by simple expressions at all. Needless to say, it would be interesting to have explicit formulas for the general coeﬃcients, because this would give a direct construction of f and f by power series and analytic continuation.

To put this conjecture in a slightly broader context, consider the Mellin transform

Mf(s) =

∞

f(x)xs−1 dx.

0

When f is smooth and rapidly decreasing (as Conjecture 4.1 implies), the integral converges to a holomorphic function for s > 0. It is a standard fact that Mf(s) can be meromorphically continued to C, with at most simple poles at s ∈ Z≤0; furthermore, for integers j ≥ 0 its residue at s = −j is the j-th Taylor coeﬃcient of f. To see why, note that if f(x) has the Taylor series expansion j≥0 cjxj about x = 0, then

 f(x) −

 xs−1 dx +

∞

1

cj s + j

f(x)xs−1 dx,

cjxj

+

Mf(s) =

1

0

j=0

j=0

where both integrals converge as long as s > −( + 1). Since our function f is radial, its Taylor coeﬃcients cj vanish if j is odd.

A short calculation (see [LL, Theorem 5.9]) shows that if f is the n-dimensional Fourier transform of f (interpreted as a radial function), then

πn/2−sΓ(s/2) Γ((n − s)/2)

Mf(n − s),

(5.2) M f(s) =

valid as an identity of meromorphic functions on C. In particular, computing the residue of Mf(s) at s = −j shows that the j-th Taylor coeﬃcient of f equals

2πj+n/2 Γ(j/2 + 1)Γ((n + j)/2)

(−1)j/2

M f(n + j), and vice versa with f and f switched.

Thus, in n dimensions Conjecture 5.2 amounts to specifying Mf(n + 2) and

M f(n + 2). The values Mf(n) and M f(n) are easy consequences of f(0) = f(0) = 1. We have identiﬁed one other value, namely the midpoint 4 of the s ↔ n−s symmetry when n = 8:

- Conjecture 5.3. For n = 8, the limiting functions satisfy


1 15 when normalized with f(0) = f(0) = 1.

Mf(4) = M f(4) =

The equality Mf(4) = M f(4) follows from (5.2), but not the value 1/15. It is natural to expect a corresponding conjecture for n = 24, but we have been unable to identify the numerical value

Mf(12) = M f(12) = 0.177860964729650276645646126241... in that case.

6. Energy minimization

One natural generalization of sphere packing is potential energy minimization. Given a radial potential function ϕ: Rn → R and a set P of point particles, the energy Eϕ(P,x) of a particle x ∈ P is deﬁned to be

ϕ(x − y),

y∈P, y =x

and the energy Eϕ(P) is deﬁned as the average of Eϕ(P,x) over all x ∈ P. (Of course some hypotheses are needed for this to make sense, but it is well deﬁned when P is a periodic discrete set and ϕ is rapidly decreasing.) The question of how to choose P so as to minimize energy with a ﬁxed density, arises naturally in physics; see [C2] for a survey.

Cohn and Kumar [CK2] deﬁned a conﬁguration P to be universally optimal if it minimizes energy whenever ϕ(x) is completely monotonic as a function of |x|2 and decreases suﬃciently quickly. For example, ϕ could be a suﬃciently steep inverse power law. As explained in Section 9 of [CK2], it suﬃces to check optimality for the Gaussians ϕ(x) = e−c|x|

2

with c > 0, i.e., the Gaussian core model [S] from mathematical physics. Cohn and Kumar conjectured that the hexagonal lattice, E8, and the Leech lattice are universally optimal. (See [CKS] for information about ground states in other dimensions.)

Proposition 9.3 of [CK2] oﬀers an approach to proving this conjecture by linear programming bounds, which Cohn and Kumar conjectured were sharp in these special dimensions (much like the case of sphere packing). Given an admissible auxiliary

function h: Rn → R satisfying h ≤ ϕ and h ≥ 0 everywhere, this proposition says that every conﬁguration P of density 1 satisﬁes

Eϕ(P) ≥ h(0) − h(0).

We can construct h by imitating the sphere packing construction: let h(x) be a radial polynomial times e−π|x|

2

, with the polynomial chosen with minimal degree so that ϕ − h and h have double roots at the modiﬁed root locations from Section 3. We conjecture that as the number of roots tends to inﬁnity, these functions converge and the limiting functions prove a sharp bound for energy.

The closest analogue of Conjectures 5.2 and 5.3 we have found is the following.

2

in Rn with n = 8 or 24, the limiting auxiliary function h satisﬁes

- Conjecture 6.1. For the potential function ϕ(x) = e−c|x|


2c n

h(0) =

Eψ(Λn),

where Λn is E8 or the Leech lattice when n = 8 or 24, respectively, and ψ(x) = |x|2ϕ(x).

Besides numerical evidence, one reason to believe this conjecture is that it is compatible with duality symmetry. If the auxiliary function h proves an energy bound for an integrable potential function ϕ, then g := ϕ − h does so for ϕ. Speciﬁcally, g ≤ ϕ since h ≥ 0, and g ≥ 0 since h ≤ ϕ. This duality transformation preserves optimality: if h proves that a lattice Λ of covolume 1 minimizes Eϕ,

- then g proves that the dual lattice Λ∗ minimizes E ϕ. To see why, note that ϕ(0)+ h(0)−h(0) = ϕ(0)+ g(0)−g(0), from which it follows by Poisson summation that


h(0) − h(0) = Eϕ(Λ) if and only if

g(0) − g(0) = E ϕ(Λ∗). This duality is compatible with Conjecture 6.1, in the sense that h satisﬁes the conjecture if and only if g does; the compatibility is not obvious, but it follows from a short calculation using Poisson summation.

7. Forcing single roots

In this section we discuss a related problem: constructing functions with forced single roots (instead of the forced double roots used earlier in the paper). Such functions do not have direct applications to sphere packing, but they can be explicitly written down in some cases and thus serve as a testing ground for ideas concerning our main conjectures. Furthermore, their properties are quite a bit more interesting than one would guess from their deﬁnition.

The structure in this problem is best seen by forcing single roots for Fourier eigenfunctions. The use of eigenfunctions was merely a computational convenience in Section 4, but in this section it will play an essential role in our conjectures.

For ε ∈ {0,1}, let

2

gn,kε = rn,kε (|x|2)e−π|x|

,

where rn,kε is a polynomial of degree at most 2k + ε that is not identically zero, vanishes at 2,4,...,2k, and is a linear combination of the polynomials p2n/j+2−ε1 for 0 ≤ j ≤ k. The last condition means that gn,kε = (−1)εgn,kε . The same arguments

as in Lemma 3.1 shows that these functions exist and are unique, up to scaling. We see no canonical way to scale them, so we will not choose a preferred scaling.

The choice of 2,4,...,2k as forced root locations is inspired by the norms of the vectors in the E8 lattice. One could also study the analogous functions for the Leech lattice, but we have focused on the simplest case. Note that we use the exact vector norms, with no need to modify them along the lines of (3.5).

- Conjecture 7.1. As k → ∞ with n and ε ﬁxed, gn,kε converges (when suitably normalized) to a Fourier eigenfunction gnε (not identically zero) that vanishes at


all radii of the form √2j. If we view gn,kε as an entire function of |x|, then the convergence is uniform on all compact subsets of C.

Uniform convergence implies that gnε(x) is an entire function of |x|. These limiting functions are mysterious in general, but when n is a multiple of

- 4 we can conjecture explicit formulas for half of them. The remaining functions appear to be much more subtle, as we will see shortly. Conjecture 7.2. If the scaling is chosen appropriately, then


sinπ|x|2/2 π|x|2/2

√3|x|2/2.

e−π

g40(x) =

If n > 4 is a multiple of 4 and ε  ≡ n/4 (mod 2), then (again up to scaling) gnε(x) = sinπ|x|2/2 e−π

√3|x|2/2

- if n ≡ 0 (mod 3),

gnε(x) = sinπ|x|2/2

  |x|2 −

(n + 2)√3 6π

2

−

n + 2 6π2

 e−π

√3|x|2/2

- if n ≡ 1 (mod 3), and

gnε(x) = sinπ|x|2/2 |x|2 − n/(2π

√

3) e−π

√3|x|2/2

- if n ≡ 2 (mod 3). We have no explanation for the exceptional behavior in four dimensions.


Proposition 7.3. The functions listed in Conjecture 7.2 are all eigenfunctions of the Fourier transform, with the appropriate eigenvalues. Sketch of proof. This can be veriﬁed by straightforward calculation. Because x  → e−π|x|

2

is its own Fourier transform, it follows that when Re(α) > 0, the Fourier transform of x  → e−π|x|

2/α/αn/2. Diﬀerentiating with respect to α allows one to compute the Fourier transform of x  → |x|2ke−π|x|

2α is x  → e−π|x|

2α for k ∈ {1,2,...}. Finally, we write

2(√3/2−i/2) − e−π|x|

2(√3/2+i/2)

e−π|x|

√3|x|2/2 =

sinπ|x|2/2 e−π

.

2i

The result when n ≡ 0 (mod 3) follows easily from the fact that √3/2 + i/2 is a 12-th root of unity, and the results when n  ≡ 0 (mod 3) follow from similar but slightly more elaborate calculations. The trickiest case is when n = 4, because it involves dividing by |x|2. That can be handled by integrating with respect to α instead of diﬀerentiating.

Figure 4. The complex roots of g81,20.

Note that the limiting functions in Conjecture 7.2 are entire and have imaginary roots at √

−2j for each j > 0. It is not clear where these imaginary roots come from. There are also a ﬁnite number of extraneous real roots, which appear to be needed to create Fourier eigenfunctions. If one plots the roots of these functions (as in Figure 4), one sees the expected roots on the real axis, the surprising purely imaginary roots, the ﬁnite set of extraneous roots, and a V-shaped collection of non-real roots spreading out from the imaginary axis. It seems that as k → ∞, that ﬁnal collection tends to inﬁnity and contributes no roots in the limit. It does serve, however, to reduce the exponent in the Gaussian from the original −π to −π√3/2.

Note also that the root of g81m at the origin must occur by Poisson summation over E8m (so it is not extraneous in the same sense, even though it was not deliberately forced).

Whenever the dimension is a multiple of 4, Conjecture 7.2 predicts one of the two eigenfunctions Conjecture 7.1 asserts exists. The other eigenfunction is more mysterious. It does not have imaginary roots at √

−2j. Instead, it almost has roots at −(2j − 1), but not quite. For example, g80 appears to vanish at the square roots of the numbers from Table 8. The precise perturbations away from the odd integers depend on the dimension. We do not know an explanation for this interesting behavior. The most natural possibility is that these functions are given by a dominant term, which has roots at exactly −(2j − 1), plus some lower order terms. However, we have been unable to conjecture a formula of this sort.

More general convergence theorems are likely true. For example, in four dimensions, if we force an extra factor of |x|2−c in the +1 eigenfunction, then the resulting functions seem to converge to

√

√

g40(x) |x|2 − c π2|x|4 + (cπ2 − 2π

3)|x|2 + c(cπ2 − 2π

3) .

(Note that now the extraneous roots need not be real.) It seems plausible that in each case covered by Conjecture 7.2, forcing some additional ﬁnite set of roots simply creates an additional factor corresponding to a ﬁnite set of extraneous roots. That does not seem to be true for the mysterious eigenfunctions not predicted by Conjecture 7.2 (i.e., forcing another root does not seem to multiply them by a polynomial factor, but instead changes the imaginary root perturbations as well).

Table 8. Squares of the imaginary roots of g80.

−0.980217784819734913... −2.999513816437548808... −4.999987267218782800... −6.999999651348489332... −8.999999990471834691...

−10.999999999741389569... −12.999999999993001822... −14.999999999999810493... −16.999999999999994854... −18.999999999999999859... −20.999999999999999996... −22.999999999999999999...

In dimensions that are not multiples of four, we do not know any closed form expressions for the limiting eigenfunctions. It appears that they behave somewhat like the mysterious eigenfunctions in the multiple-of-four case (i.e., those not predicted by Conjecture 7.2). For example, g20 appears to have imaginary roots at some perturbation of the square roots of −2.5, −4.5, −6.5, etc., and g21 at some perturbation of the square roots of −1.5, −3.5, −5.5, etc. We have focused on the multiples of four because they seem simpler (and perhaps more relevant to sphere packing).

Acknowledgements

We are grateful to Percy Deift, Noam Elkies, Doug Hardin, Abhinav Kumar, Greg Moore, Ed Saﬀ, Alex Samorodnitsky, Terence Tao, and Frank Vallentin for helpful conversations.

References

[AAR] G. Andrews, R. Askey, and R. Roy, Special Functions, Cambridge University Press, 1999.

- [B] H. F. Blichfeldt, The minimum values of positive quadratic forms in six, seven and eight variables, Math. Z. 39 (1935), 1–15.
- [C1] H. Cohn, New upper bounds on sphere packings II, Geom. Topol. 6 (2002), 329–353, arXiv:math.MG/0110010.


[C2] H. Cohn, Order and disorder in energy minimization, Proceedings of the International Congress of Mathematicians, Hyderabad, August 19–27, 2010, Volume IV, pages 2416–2443, Hindustan Book Agency, New Delhi, 2010, arXiv:1003.3053.

[CE] H. Cohn and N. Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157

(2003), 689–714, arXiv:math.MG/0110009.

- [CK1] H. Cohn and A. Kumar, The densest lattice in twenty-four dimensions, Electron. Res. Announc. Amer. Math. Soc. 10 (2004), 58–67, arXiv:math.MG/0408174.
- [CK2] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007), 99–148, arXiv:math.MG/0607446.
- [CK3] H. Cohn and A. Kumar, Optimality and uniqueness of the Leech lattice among lattices, Ann. of Math. (2) 170 (2009), 1003–1050, arXiv:math.MG/0403263.


[CKS] H. Cohn, A. Kumar, and A. Schu¨rmann, Ground states and formal duality relations in the Gaussian core model, Phys. Rev. E (3) 80 (2009), 061116, 7 pp., arXiv:0911.2169.

- [CZ1] H. Cohn and Y. Zhao, Energy-minimizing error-correcting codes, IEEE Trans. Inform. Theory 60 (2014), 7442–7450, arXiv:1212.1913.


- [CZ2] H. Cohn and Y. Zhao, Sphere packing bounds via spherical codes, Duke Math. J. 163


(2014), 1965–2002, arXiv:1212.5966. [CS] J. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, third edition, Springer-Verlag, 1999.

- [D] P. Deift, T. Kriecherbauer, K. T-R McLaughlin, S. Venakides, and X. Zhou, Strong asymptotics of orthogonal polynomials with respect to exponential weights, Comm. Pure Appl. Math. 52 (1999), 1491–1552.


[El] N. Elkies, Lattices, linear codes, and invariants I and II, Notices Amer. Math. Soc. 47

(2000), 1238–1245 and 1382–1391. [Ep] J. F. Epperson, On the Runge example, Amer. Math. Monthly 94 (1987), 329–341. [FT] L. Fejes T´oth, Uber¨ einen geometrischen Satz, Math. Z. 46 (1940), 79–83. [H] T. Hales, A proof of the Kepler conjecture, Ann. of Math. 162 (2005), 1065–1185. [LOV] D. de Laat, F. M. de Oliveira Filho, and F. Vallentin, Upper bounds for packings of spheres

of several radii, Forum Math. Sigma 2 (2014), e23, 42 pp., arXiv:1206.2608. [Leb] N. N. Lebedev, Special Functions and Their Applications, Dover Publications, Inc., New York, 1972.

[Lev] V. I. Levenshtein, On bounds for packings in n-dimensional Euclidean space (Russian), Dokl. Akad. Nauk SSSR 245 (1979), 1299–1303; English translation in Soviet Math. Dokl. 20 (1979), 417–421.

[LL] E. H. Lieb and M. Loss, Analysis, second edition, Graduate Studies in Mathematics 14, Amer. Math. Soc., 2001.

[OS] A. M. Odlyzko and N. J. A. Sloane, New bounds on the number of unit spheres that can touch a unit sphere in n dimensions, Journal of Combinatorial Theory A 26 (1979), 210–214.

[P] PARI/GP, version 2.3.5, Bordeaux, 2010, http://pari.math.u-bordeaux.fr/. [S] F. H. Stillinger, Phase transitions in the Gaussian core system, J. Chem. Phys. 65 (1976),

3968–3974. [V] M. S. Viazovska, The sphere packing problem in dimensions 8, preprint, 2016, arXiv:1603.04246.

Microsoft Research New England, One Memorial Drive, Cambridge, MA 02142 E-mail address: cohn@microsoft.com

Department of Mathematics, Hill Center–Busch Campus, Rutgers, 110 Frelinghuysen Rd., Piscataway, NJ 08854-8019

E-mail address: miller@math.rutgers.edu

