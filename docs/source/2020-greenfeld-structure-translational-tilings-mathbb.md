---
type: source
kind: paper
title: The structure of translational tilings in $\mathbb{Z}^d$
authors: Rachel Greenfeld, Terence Tao
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2010.03254v3
source_local: ../raw/2020-greenfeld-structure-translational-tilings-mathbb.pdf
topic: general-knowledge
cites:
---

## arXiv:2010.03254v3[math.CA]23Sep2021

DISCRETE ANALYSIS, 2021:16, 28 pp. www.discreteanalysisjournal.com

# The Structure of Translational Tilings in Zd

##### Rachel Greenfeld* Terence Tao†

Received 4 November 2020; Published 24 September 2021

Abstract: We obtain structural results on translational tilings of periodic functions in Zd by ﬁnite tiles. In particular, we show that any level one tiling of a periodic set in Z2 must be weakly periodic (the disjoint union of sets that are individually periodic in one direction), but present a counterexample of a higher level tiling of Z2 that fails to be weakly periodic. We also establish a quantitative version of the two-dimensional periodic tiling conjecture which asserts that any ﬁnite tile in Z2 that admits a tiling, must admit a periodic tiling, by providing a polynomial bound on the period; this also gives an exponential-type bound on the computational complexity of the problem of deciding whether a given ﬁnite subset of Z2 tiles or not. As a byproduct of our structural theory, we also obtain an explicit formula for a universal period for all tilings of a one-dimensional tile.

Key words and phrases: tiling, periodicity, decidability

#### 1 Introduction

###### 1.1 Translational tiling

Let d 1 be an integer, and let F ⊂ Zd be a ﬁnite subset of the standard lattice Zd. A tiling1 of Zd by F is a subset A of Zd with the property that every element of Zd has precisely one representation of the form f +a with f ∈ F and a ∈ A. We refer to F as the tile and A as the tiling set, thus Zd is partitioned (or tiled) by translates F +a of the tile F by elements a of the tiling set. In terms of the convolution operation

f ∗g(x):= ∑

f(y)g(x−y)

y∈Zd

*Partially supported by the Eric and Wendy Schmidt Postdoctoral Award. †Partially supported by NSF grant DMS-1764034 and by a Simons Investigator Award. 1All tilings in this paper are by translation; we do not consider tilings that involve rotation or reﬂection in addition to

translation.

© 2021 Rachel Greenfeld and Terence Tao cb Licensed under a Creative Commons Attribution License (CC-BY) DOI: 10.19086/da.28324

on Zd (which is well-deﬁned if at least one of f,g is compactly supported, and f,g are real-valued; alternatively, one of f,g can take values in the unit circle R/Z if the other is integer-valued), this property can be expressed as

1F ∗1A = 1,

where 1F denotes the indicator function of F, and similarly for A. More generally, for any natural number k and a subset E ⊂ Zd, a tiling of level k of E by the tile F is a set A such that

1F ∗1A = k1E. We omit the qualiﬁer “of level k” if k = 1, and “of E” if E = Zd.

###### 1.2 Periodicity

We call a function f : Zd → R Λ-periodic for some subgroup Λ of Zd if f(x+λ) = f(x) for all x ∈ Zd and λ ∈ Λ; we simply call f periodic if it is Λ-periodic for some Λ which is a lattice (a subgroup on Zd whose index [Zd : Λ] is ﬁnite).

We call a set E ⊂ Zd Λ-periodic (resp. periodic) if 1E is Λ-periodic (resp. periodic). Note from Lagrange’s theorem that if Λ is a lattice of index := [Zd : Λ], then any Λ-periodic set or function will also be Zd-periodic. We call a set E ⊂ Z2 weakly periodic if it can be represented as the disjoint union

- E = E1  ··· Em of ﬁnitely many sets E1,...,Em, with each Ej hj -periodic along a one-dimensional subgroup hj := {nhj : n ∈ Z} for some non-zero hj ∈ Z2.

1.3 Periodicity of tiling

In one dimension it is easy to see from the pigeonhole principle that any tiling A by a ﬁnite tile, of any level k, is periodic (see [N]). However in higher dimensions tiling sets need not be periodic. For instance, if d = 2 and F1 is the square F1 = {0,1}2, then any set A1 of the form

A1 := {(2n,2m+a(n)): n,m ∈ Z} (1)

with a: Z → {0,1} an arbitrary function, is a tiling by F1, but is only periodic if a is periodic. On the other hand, we observe that this tiling is still (0,2) -periodic. As a slightly more complex example of this type, if F2 := {0,2}×{0,1}, then any set A2 of the form

A2 := {(4n,2m+a(n)): n,m ∈ Z}∪{(4n+1+2b(m),2m): n ∈ Z} (2)

for arbitrary functions a,b: Z → {0,1} is a tiling by F2. In general, A2 will not be periodic along any non-trivial group Λ, but will always be weakly periodic, being the disjoint union of a (0,2) -periodic set and a (4,0) -periodic set.

Our investigations were primarily motivated by the periodic tiling conjecture of Lagarias and Wang [LW] (which also implicitly appears previously in [GS, p. 23]): Conjecture 1.1 (Periodic tiling conjecture). Let F ⊂ Zd be a ﬁnite tile. If there is at least one tiling A by

- F, then there exists a tiling A by F which is periodic.


This conjecture was established in d = 1 in [N] as a quick application of the pigeonhole principle. For d = 2, the conjecture was recently established by Bhattacharya [B2] using ergodic theory techniques and a “dilation lemma” proven using elementary number theory (or elementary commutative algebra); see [WV] for some earlier partial results in the d = 2 case. For d > 2 the conjecture is known when the cardinality |F| of F is prime or equal to 4 [S5], but remains open in general. On the other hand, the tiling conjecture for multiple tiles F1,...,Fk in Zd is known to be false [B], [R]. Finally, we remark that by a well known argument attributed to Wang (see [B], [R]), the validity of Conjecture 1.1 at a given dimension d implies that the problem of determining whether a given tile F tiles Zd or not is decidable. We refer the reader to [R], [S5] for further discussion and surveys of tiling problems in lattices.

Remark 1.2. There is also extensive literature on tiling problems on other groups than Zd, both by indicator functions 1F and by more general tiling functions f. For instance, the analogue of Conjecture

- 1.1 in Rd is known for convex polytopes [V], [M, M2] and for topological disks [GN], [K2], and the one-dimensional case is established (for bounded tiles) in [LM], [LW], [KL]. See the recent papers [L], [KL3] for further results and open problems of tiling in R and in Rd. Tiling of more general locally compact groups by functions is studied in [HN], [LM]. There is also substantial literature on tiling ﬁnite abelian groups, which in this context is also known as factorization; see the text [SS] for a detailed presentation of this topic. Finally, we note some connections between discrete tilings and low-complexity subshifts of ﬁnite type, see for instance the recent survey [K]. However, the focus of this paper will be exclusively on tiling problems in lattices Zd.


###### 1.4 Results

We can now state our ﬁrst main theorem, which clariﬁes the nature of level one tilings of periodic sets in two dimensions, in particular revealing a fundamental difference between level one tilings and higher level tilings.

###### Theorem 1.3 (Tilings in Z2).

- (i). (Level one tilings in the plane are weakly periodic) If F ⊂ Z2 is ﬁnite and A is a level one tiling of a periodic set by F, then A is weakly periodic.
- (ii). (Higher level tilings in the plane need not be weakly periodic) There exists an eight-element subset F ⊂ Z2 and a level 4 tiling of Z2 which is not weakly periodic.


Theorem 1.3(ii) is established by an explicit construction which we give in Section 2; the tiling set is a ﬁnite Boolean combination of “Bohr sets”. We now discuss Theorem 1.3(i). In fact, we have a more quantitative version of this result. Here and in the sequel we use the asymptotic notation X = O|F|(Y), X |F| Y, or Y |F| X to denote an estimate of the form |X| C|F|Y where C|F| is a quantity depending only on |F|. Similarly with the subscript |F| replaced by other parameters.

###### Theorem 1.4 (Quantitative weak periodicity of level one tilings in Z2). Let F ⊂ Z2 be a tile with 1 < |F| < ∞ and 0 ∈ F, and let A be a level one tiling of an Z2-periodic set E by F for some natural number . Then there is a lattice Λ ⊂ Z2 of index

[ Z2 : Λ] |F| diam(F)2(|F|−1)2

and pairwise incommensurable vectors h1,...,hm ∈ Z2 for some 1 m |F|−1 with magnitude bounds

h1 ,..., hm diam(F)|F|−1 (3) and a positive integer multiple L of size

L |F| diam(F)|F|(|F|−1) (4)

such that the intersection of A with each coset of Λ is Lhj -periodic for some j = 1,...,m. Furthermore each hj is an integer multiple of a vector in F\{0}. The lattice Λ, integer L, and the vectors h1,...,hm are allowed to depend on E, ,F but do not otherwise depend on the choice of tiling set A.

Note that Theorem 1.4 implies Theorem 1.3(i) after translating the tile F so that 0 ∈ F and dealing with the easy case |F| = 1 separately. Theorem 1.4 also allows us to classify two-dimensional tilings of level one in terms of one-dimensional tilings. This classiﬁcation, in turn, provides a description of the structure of any two-dimensional tiling of level one. Moreover, using Theorem 1.4 we prove the following quantitative generalization of the d = 2 case of Conjecture 1.1, with polynomial type bounds (and also an extension to tilings of other periodic subsets E of Z2 than the full lattice Z2):

- Theorem 1.5 (Quantitative periodic tiling conjecture in two dimensions). Let F ⊂ Z2 be a ﬁnite tile, and let E ⊂ Z2 be an Z2-periodic set for some 1. If there is at least one tiling A of E by F, then there exists a tiling A of E by F by an MZ2-periodic set with


M |F| diam(F)O(|F|4).

This theorem has the following bound on the computational complexity of deciding whether a given ﬁnite set F is a tile, which is of exponential type in the diameter of F if |F| is bounded: Corollary 1.6 (Computational complexity bound for planar tiling). There is an algorithm which, when

given a ﬁnite subset F of Z2 as input, decides whether F can tile Z2 in time O|F|(exp(O|F|(diam(F)O(|F|4)))) (counting each arithmetic operation as costing time O(1)).

Proof. By Theorem 1.5, it sufﬁces to check tilings A that are MZ2-periodic for some M |F| diam(F)O(|F|4).

Each such tiling can be checked in time O|F|(M2), and the number of MZ2-periodic tilings is at most 2M2 for each M, giving the claim.

| |
|---|


Note that the results in [B2] established that the tiling problem in Z2 was decidable, but gave no bound on the computational complexity. The proof of Corollary 1.6 also shows that for ﬁxed |F|, the decision problem is in the complexity class NP with respect to the diameter diam(F); for instance, in the unlikely event that P = NP, the decision problem could now be performed in time polynomial in the diameter. It seems of interest to see if the exponential bound can be improved without the P = NP hypothesis in the regime when |F| is bounded. In one dimension the best complexity bound currently known is exp(Oε(diam(F)1/3+ε)) for any ε > 0, due to Bíró [B3].

We now discuss further the proof of Theorem 1.4. Our starting point is the following quite explicit structural theorem valid in all dimensions and levels, which we believe to be of independent interest:

Theorem 1.7 (Structure of tilings). Let d 1, let F be a ﬁnite subset of Zd, and let A ⊂ Zd be a set such that 1F ∗1A is Zd-periodic for some 1. We normalize 0 ∈ F. Then there exists a decomposition

1A =1F ∗1A− ∑

ϕf (5)

f∈F\{0}

where for each f ∈ F\{0}, ϕf : Zd → [0,1] is a function which is qf -periodic, where q is the least common multiple of and all the primes less than or equal to 2|F|.

We establish this result in Section 3. It is a consequence of (a generalization of) the dilation lemma from [B2], which roughly speaking asserts that if a set (or multi-set) A is a tiling for a tile F, then it is also a tiling for all dilations rF of that tile, as long as r is congruent to 1 with respect to a suitable modulus. This fact is number-theoretic in nature, ultimately boiling down to the Frobenius identity (x+y)p = xp +yp that is valid in any commutative ring of characteristic p. Theorem 1.7 is then established by averaging over all such dilations r.

- Remark 1.8. Theorem 1.7 has the Fourier-analytic consequence that the distributional Fourier transform 1A of A, which is a distribution on the torus (R/Z)d, is supported on the union of the ﬁnite subgroup


- 1 Z/Z d and the codimension one subgroups (qf)⊥ := {ξ ∈ (R/Z)d : qf · ξ = 0} for f ∈ F\{0}.


A qualitatively similar conclusion2 regarding the spectral measure of a measure-preserving system associated to a tiling was obtained in [B2, Lemma 3.2]. Our initial arguments relied heavily on this Fourier analytic structure, but we found eventually that physical-space arguments were simpler and gave superior bounds to those relying on the Fourier transform. Furthermore, the physical-space approach we developed provided us with more structural data, which in particular allowed us to gain better understanding of the rigidity of tiling structures in Z2.

Theorem 1.7 already resembles an assertion of weak periodicity of 1A, except that the terms on the right-hand side of (5) are not indicator functions. Nevertheless, the structural theorem turns out to be particularly powerful in the case of level one tilings, when it imposes a powerful pointwise constraint

### ∑

ϕf 1 (6)

f∈F\{0}

on the functions ϕf. Furthermore, by working modulo 1 to eliminate the 1A and 1F ∗1A terms from (5), we also have the important identity

### ∑

ϕf = 0 mod 1.

f∈F\{0}

In dimension two, one can apply discrete differentiation operators, exploiting the partial periodicity of the ϕf to conclude that the functions ϕf mod 1 are polynomials (after collecting commensurable terms). The classical Weyl equidistribution theory of these polynomials then asserts that these functions are

2We also note a possibly related result of Granville and Rudnick [GR, Corollary 3.1], which in our notation states that if f : Zd → Z is compactly supported and not identically zero (e.g., if f = 1F for some ﬁnite non-empty F ⊂ Zd), then the set {ξ ∈ (Q/Z)d : f(ξ) = 0} of roots of unity in the zero set of f can be placed inside the union of a ﬁnite number of explicitly computable codimension one subgroups; this implies a special case of a conjecture of Lang [L2]. We thank the anonymous referee for this reference.

either periodic or equidistributed in the unit circle. The powerful constraint (6) lets us eliminate the equidistributed case, and some further elementary arguments (involving linear algebra facts such as Cramer’s rule) then allow us to conclude Theorem 1.4.

The proof of Theorem 1.5 also proceeds by exploiting the dilation lemma, though in a simpler fashion (there is no need to work modulo 1 in this case). One could also establish results similar to Theorem

- 1.5 but with weaker bounds (of exponential type in the diameter rather than polynomial) by using the pigeonhole principle instead of the dilation lemma, but we do not present these arguments here.


As a further application of our structural results, we establish in Corollary 3.5 an explicit formula for a universal period for all tilings A of a given one-dimensional tile F ⊂ Z, which (remarkably) is only of polynomial size in the diameter, as opposed to exponential, in the regime where the cardinality |F| of the tile is bounded.

Our results leave open the question of whether the analogue of Conjecture 1.1 for higher level (i.e., whether any tile F that admits a level k tiling, also admits a level k tiling by a periodic set) is true in two dimensions; neither our positive or negative results seem strong enough to resolve this question. In the one dimensional lattice the claim easily follows from the pigeonhole principle (or from Corollary 3.5 below), which forces all tiling sets at any level to be periodic. On the other hand, on the continuous line R an example was given in [KL2] of an L1(R) function of unbounded support that tiled R by a set which was not the ﬁnite union of periodic sets. We also mention the recent result of Liu [L] that if a function f ∈ L1(Rd) tiles by a ﬁnite union of lattices at some level, then it also tiles by a single lattice at a possibly different level. We refer the reader to the recent survey [KL3] for further discussion of tiling results in R and Rd.

We plan to investigate the applications of this theory to higher-dimensional lattice tilings in subsequent work.

###### 1.5 Organization of the paper

In Section 2, we present a constructive proof of Theorem 1.3(ii). This section is self-contained and will not be used in what follows. In Section 3, we develop an approach to study tiling structures in Zd and prove our structure theorem, Theorem 1.7. The proof relies on Lemma 3.1, which we refer to as the “dilation lemma”. As a direct corollary of our structure theorem, we obtain an explicit universal period of one-dimensional tilings, of polynomial size in the diameter of the tile. In Sections 4, 5 and 6, we apply the results of Section 3 to level one tilings of periodic sets in Z2. In more detail:

In Section 4, using polynomial sequences (based on [B2]), we prove Theorem 1.4, which is a quantitative version of Theorem 1.3(i). In Section 5, we prove Theorem 1.5 by combining the former presented results with a “slicing lemma”. In Section 6, by combining Theorem 1.4 and the results in Section 5, we establish a satisfactory description of the structure of any tiling of level one of a periodic set in Z2. In particular, we show that the question whether a tile F ⊂ Z2 admits non one-periodic tiling, is decidable.

###### 1.6 Notation

If F ⊂ Zd is a set and r is a natural number, we use rF := {r f : f ∈ F} to denote the dilation of F by r. In particular we have the lattices rZd = {rn : n ∈ Zd}. We use |F| to denote the cardinality of F; by

abuse of notation we also use |z| to denote the magnitude of a real or complex number z.

We use x  → x mod 1 to denote the projection homomorphism from R to the (additive) unit circle R/Z. A polynomial of degree at most d from Z to R/Z is a map P: Z → R/Z of the form

P(n) = α0 +α1n+···+αdnd for some α0,...,αd ∈ R/Z.

Two vectors h1,h2 ∈ Zd are said to be commensurable if one is a scalar multiple of the other, and incommensurable otherwise. In the two-dimensional case d = 2, we deﬁne the wedge product h1 ∧h2 to be the determinant of the 2×2 matrix with rows h1,h2; thus h1,h2 are commensurable if and only if h1 ∧h2 = 0. If h1,h2 are incommensurable, we observe the Cramer rule

v∧h2 h1 ∧h2

v∧h1 h2 ∧h1

v =

h1 +

h2 (7)

for any v ∈ Z2 (this is easily veriﬁed by ﬁrst testing the cases v = h1,h2, then extending by linearity). In particular, if we let h1,h2 denote the lattice generated by h1,h2, we have the inclusion

|h1 ∧h2|Z2 ⊂ h1,h2 . (8)

This inclusion can also be established from Lagrange’s theorem, since |h1 ∧h2| is the index of h1,h2 . From Hadamard’s inequality one has

|h1 ∧h2| h1 h2

where h denotes the Euclidean length of an element h of Zd.

An element h ∈ Zd is said to be primitive if it cannot be written as h = mh for some h ∈ Zd and some integer m > 1. Note that every non-zero element h of Zd can be uniquely expressed as h = mh where m is a natural number and h ∈ Zd is primitive.

If h ∈ Zd, we use δh = 1{h} to denote the Kronecker delta function at h, and let ∆h denote the discrete differentiation operator

∆h f(x) := (δ0 −δh)∗ f(x) = f(x)− f(x−h) in the direction h applied to a function f : Zd → R (or f : Zd → R/Z) at a location x ∈ Zd. Note that these operators ∆h commute with each other and with convolution by any additional function g:

∆h(f ∗g) = (∆h f)∗g = f ∗∆hg.

#### 2 The counterexample

In this section we prove Theorem 1.3(ii). The constructions here are not used elsewhere in the paper; however, the analysis presented in the rest of the paper was what led us to the counterexample presented here.

We ﬁrst need to locate a sign pattern on Z2 that obeys certain cancellation properties.

- Lemma 2.1. There exists a 4Z2-periodic function χ : Z2 → {−1,1} such that one has the cancellations


- χ ∗1{(0,0),(0,2)} = 0 (9)
- χ ∗1{(0,0),(1,0)} = 0. (10)


Proof. It is a routine matter to check that the function

χ(m1,m2) := (−1) m2/2 +m1 (11) satisﬁes the claimed properties, where  ·  is the integer part function.

| |
|---|


Note that (9) and (10) imply

χ ∗1{(0,0),(2,−2)} = 0 (12) since

1{(0,0),(2,−2)} = 1{(0,0),(0,2)} ∗1{(0,−2)} +1{(0,0),(1,0)} ∗(1{(1,−2)} −1{(0,−2)}). Let α be an arbitrary irrational number (e.g., α = √2). Consider the function3

a(m1,m2) := χ(m1,m2)({αm1}+{αm2}−{α(m1 +m2)}−1/2)+1/2

on Z2, where χ is as in Lemma 2.1 and {x} = x −  x ∈ [0,1) denotes the fractional part of x ∈ R. Observe that {α(m1 +m2)} is either equal to {αm1}+{αm2} or {αm1}+{αm2}−1, hence a(m1,m2) takes values in {0,1}. Hence this is the indicator function of some set A ⊂ Z2:

1A(m1,m2) := χ(m1,m2)({αm1}+{αm2}−{α(m1 +m2)}−1/2)+1/2. Now introduce the eight-element tile

F := {t1(0,2)+t2(1,0)+t3(2,−2) : t1,t2,t3 ∈ {0,1}}. Note that we have the factorization

1F = 1{(0,0),(0,2)} ∗1{(0,0),(1,0)} ∗1{(0,0),(2,−2)}. From (9) we see that the functions

(m1,m2)  → χ(m1,m2), (m1,m2)  → χ(m1,m2){αm1}

are annihilated by convolution with 1{(0,0),(0,2)}. Similarly, from (10) we see that

(m1,m2)  → χ(m1,m2){αm2}

- is annihilated by convolution with 1{(0,0),(1,0)}, and from (12) we see that (m1,m2)  → χ(m1,m2){α(m1 +m2)}


3The function (m1,m2)  → {αm1} + {αm2} − {α(m1 + m2)} was also mentioned in a closely related context in [KS, Example 4], [S4, Example 3.4.6].

- is annihilated by convolution with 1{(0,0),(2,−2)}. Finally, we have 1F ∗1 = 1F ∗1Z2 = |F| = 8. Using the bilinear, commutative, and associative properties of convolution, we conclude that


1F ∗1A = 4.

It remains to show that A is not weakly periodic. Suppose for contradiction that we had a decomposition

1A = 1A1 +···+1Am (13)

where each Ai is hi -periodic for some non-zero hi ∈ Z2. By repeatedly grouping together sets Ai corresponding to commensurate hi and passing to least common multiples, we may assume that the hi are pairwise incommensurable. In particular, at most one of the hi is commensurate with (1,0); by relabeling we may assume that hi is incommensurate with (1,0) for all 2 i m; by adding a dummy index if necessary (and an empty set A1) we may assume that h1 is commensurate with (1,0). We now rearrange (13) as

m

### ∑

χ(m1,m2){αm2}−1A1(m1,m2) =

1Ai(m1,m2)−χ(m1,m2){αm1}

(14)

i=2

+χ(m1,m2){α(m1 +m2)}+ 21χ(m1,m2)− 12.

The two terms on the left-hand side of (14) are (4,0) -periodic and h1 -periodic respectively, thus the left-hand side of (14) is 4h1 -periodic. Meanwhile, each of the terms on the right-hand side of (14) is

h -periodic with respect to some h incommensurate with (1,0) and hence with 4h1. Let e˜ ∈ Z2 be a vector incommensurate with all of these periods h. Then we may ﬁnd an integer multiple e = Ne˜ of e˜ which lies in 4h1,h for all the periods h on the right-hand side of (14), thus one has a decomposition

e = ah(4h1)+bhh

for each such h. Applying the discrete differentiation operator ∆e−ah(4h1) then annihilates any term on the right-hand side of (14) that is h -periodic, and the operator is equivalent to ∆e when applied to the left-hand side of (14). Applying enough of these discrete differentiation operators to annihilate the entire right-hand side of (14), we conclude that

∆ke(χ(m1,m2){αm2}−1A1(m1,m2)) = 0

for some integer k. Thus, when evaluated on any coset of e = {ne : n ∈ Z}, the kth discrete derivative of function

χ(m1,m2){αm2}−1A1(m1,m2) (15) vanishes. A simple induction on k then shows that (15) is a polynomial (of degree at most k−1); it is also bounded, hence it is constant. In other words, (15) is e -periodic. As it is also 4h1 -periodic, it is in fact periodic, and thus attains at most ﬁnitely many values. But this implies that {αm2} attains at most ﬁnitely many values, contradicting the irrationality of α. This concludes the proof of Theorem 1.3(ii).

- Remark 2.2. Since {(0,0),(0,2)} admits a periodic tiling of level 1, F admits a periodic tiling of level


- 4. Hence this example does not provide a counterexample to the higher level version of Conjecture 1.1, which remains open even in two dimensions.


#### 3 A dilation lemma and the structure theorem

In [B2, Proposition 3.1], some elementary commutative algebra was used to establish a dilation lemma that asserted, roughly speaking, that if A was a (multi-set) tiling of Zd of a tile F at some level k, then A was also a tiling of the dilate rF for an arithmetic progression of r’s. A one-dimensional version of this lemma previously appeared in [T2]; see also [HIPRV, Proposition 3.2] (or [IMP, Theorem 3.3]) for a related Fourier-analytic dilation lemma for tilings of Fdp. Variants of this lemma were also established in [S5, Lemma 10] and [KS, Lemma 2]. We re-prove this lemma using elementary number theory, and generalize it from tilings of Zd to tilings of periodic level functions.

- Lemma 3.1 (Dilation lemma). Let F be a ﬁnite subset of Zd for some d 1, and let g: Zd → Z be a bounded function.


- (i). If 1F ∗g = k for some integer k, then for any prime p with p > (supg−infg)|F|, one has 1pF ∗g = k.
- (ii). If 1F ∗g = k for some integer k, and q is the product of all primes less than or equal to (supg− infg)|F|, then one has 1rF ∗g = k whenever r is a natural number coprime to q.
- (iii). If 1F ∗g is Zd-periodic for some 1, and q is the least common multiple of and all primes less than or equal to 2(supg−infg)|F|, then 1rF ∗g = 1F ∗g whenever r is a natural number with r = 1 mod q.


Proof. We begin with (i). The claim is easily veriﬁed when g is constant, so we may assume that g is non-constant, in particular p > |F|. We convolve the equation 1F ∗g = k by p−1 further copies of 1F using the identity 1F ∗1 = |F| to conclude that

(1F)∗p ∗g = |F|p−1k

where (1F)∗p is the convolution of p copies of 1F. As all functions here are integer-valued, this identity also holds modulo p:

(1F)∗p ∗g = |F|p−1k mod p. By Fermat’s little theorem we have |F|p−1 = 1 mod p. Also, from the binomial theorem4 we have (f +g)∗p = f∗p +g∗p mod p for all ﬁnitely supported functions f,g: Zd → Z. Iterating this observation and writing 1F = ∑f∈F δf as the sum of Kronecker delta functions δf, we see that

(1F)∗p = 1pF mod p. We conclude that

1pF ∗g = 1F ∗g mod p or equivalently

(1pF −1F)∗g = 0 mod p.

4Alternatively, one can apply the Frobenius endomorphism f  → f∗p to the group algebra Fp[Zd], where Fp denotes the ﬁnite ﬁeld of order p.

Observe that the left-hand side takes values in the integers of magnitude at most (supg−infg)|F| (to show this, one can ﬁrst shift g by a constant to normalize infg = 0 if desired). By the assumption on p, we thus see that (1pF −1F)∗g = 0, and (i) follows.

To prove (ii), observe from the fundamental theorem of arithmetic that any r = 1 mod q is the product of a ﬁnite number of primes p > (supg−infg)|F| (possibly with repetition). The claim then follows by iterating (i).

Finally, we prove (iii). If 1F ∗g is Zd-periodic, then for any λ ∈ Zd we have 1F ∗∆λg = ∆λ(1F ∗g) = 0.

The discrete derivative ∆λg takes values in the integers of magnitude at most supg−infg. Applying (ii), we conclude that

1rF ∗∆λg = 0

whenever λ ∈ Zd and r = 1 mod q. Equivalently, 1rF ∗g is Zd-periodic for all r = 1 mod q, which implies that

(1rF −1F)∗g

is Zd-periodic. In particular, if BR denotes a Følner sequence on Zd (for instance one can take BR := {−R,...,R}d), then we have

1 |BR|

(1rF −1F)∗g = (1rF −1F)∗

1BR ∗g (16)

for any R > 0. But as r −1 is a multiple of , we have r f − f ∈ Zd for all f ∈ F. From the Følner property we then have

1 |BR|

(δr f −δf)∗

lim

###### = 0

1BR

R→∞

1(Zd)

for all f; from Young’s inequality and the boundedness of g we hence have

lim

R→∞

and hence by the triangle inequality

1 |BR|

(δr f −δf)∗

1BR ∗g

###### = 0

∞(Zd)

lim

R→∞

1 |BR|

1BR ∗g

(1rF −1F)∗

###### = 0.

∞(Zd)

Combining this with (16) one has (1rF −1F)∗g = 0, which gives (iii).

| |
|---|


- Remark 3.2. The above proof shows that if the requirement r = 1 mod q in Lemma 3.1(iii) is relaxed to r merely being coprime to q, then 1rF ∗g is no longer necessarily equal to 1F ∗g, but will still be


Z2-periodic. In [S5, Theorems 10, 13] it is also shown that if 1F ∗1A = 1 then 1−F ∗1A = 1, and also 1rF ∗1A 1 whenever r is an integer coprime to |F|. (In fact one can improve the inequality 1rF ∗1A 1 to 1F ∗1A = 1 by volume packing arguments; see, e.g., [GL2, Lemma 3.2].)

Now we can prove Theorem 1.7.

Proof of Theorem 1.7. Let the notation and hypotheses be as in that theorem. From Lemma 3.1(iii) we have

1rF ∗1A = 1F ∗1A

for all natural numbers r with r = 1 mod q, where q being as in Lemma 3.1(iii). As 0 ∈ F, we can rewrite this identity as

1A =1F ∗1A− ∑

δr f ∗1A.

f∈F\{0}

We can average this to obtain

1A =1F ∗1A− ∑

ϕf,N

f∈F\{0}

for any natural number N 1, where ϕf,N : Zd → [0,1] is the function

ϕf,N :=

N

1 N

### ∑

δ(1+nq)f ∗1A.

n=1

It is clear that ϕf,N takes values in [0,1]. Also from telescoping series we have

|ϕf,N(x+qf)−ϕf,N(x)|

2 N

(17)

for any x ∈ Zd. By the Arzelá-Ascoli theorem, we can ﬁnd a sequence Ni → ∞ such that for every f ∈ F\{0}, ϕf,Ni converges locally uniformly to a limit ϕf, which then also takes values in [0,1], and we now have

1A =1F ∗1A− ∑

ϕf.

f∈F\{0}

Setting N = Ni in (17) and taking limits, we conclude that ϕf(x+qf)−ϕf(x) = 0 for all x ∈ Zd, thus ϕf is qf -periodic, and Theorem 1.7 follows.

| |
|---|


Remark 3.3. The above argument shows that one can interpret ϕf(x) as a limiting density of A along the ray {x+(1+nq)f : n ∈ N}. A similar averaging argument (using ultraﬁlter limits instead of generalized limits) appears in [S4, Section 7.3] in a related context, under different assumptions.

For our application it is convenient to group together “commensurable” terms in Theorem 1.7.

Theorem 3.4 (Structure of tilings, II). Let d, ,k 1, let F be a ﬁnite subset of Zd, let E be an Zdperiodic subset of Zd, and let A be a tiling of E by F of level k. We normalize 0 ∈ F, and assume |F| > 1. Then there exists a decomposition

m

### ∑

ϕj (18)

1A = k1E −

j=1

where 1 m |F|−1, and each ϕj : Zd → [0,k] is qhj -periodic, where q is the least common multiple of and all the primes less than or equal to 2|F|, and h1,...,hm are pairwise incommensurable elements of Zd such that

m

### ∏

hj diam(F)|F|−1. (19)

j=1

In particular, we have the upper bounds

q |F| (20) and

m

### ∑

ϕj k. (21)

j=1

Furthermore, each hj is an integer multiple of an element of F\{0}. Proof. From Theorem 1.7 one has

1A =k1E− ∑

ϕ˜f

f∈F\{0}

where each ϕ˜f : Zd → [0,1] is qf -periodic. We deﬁne an equivalence relation on F\{0} by declaring f ∼ f if f, f are commensurable (namely, f = pf for some rational p). If we let C1,...,Cm be the equivalence classes of this relation, then 1 m |F|−1 and we have a decomposition (18) with

ϕj := ∑

ϕ˜f.

f∈Cj

In particular the ϕj are non-negative, and then from (18) and the non-negativity of 1A we conclude that all the ϕj are also bounded by k, as well as the bound (21). Since each ϕ˜f is qf -periodic, we see on taking least common multiples that ϕj is qhj -periodic for some non-zero hj ∈ Z2 commensurable to the elements of Cj and of magnitude at most

### hj ∏

f∈Cj

f diam(F)|Cj|

(note that f diam(F) for all f ∈ F since 0 ∈ F). In particular we have (19). Since the Cj are pairwise incommensurable, the hj are also pairwise incommensurable. Finally, the bound (20) is clear from deﬁnition of q.

| |
|---|


We have found that the bound (21) is particularly powerful in the level one case k = 1, as it can be used in that case to completely rule out “equidistributed” scenarios in which at least one of the ϕj has values that equidistribute in the unit interval [0,1]. However, in higher level settings it is possible for multiple equidistributed ϕj to coexist, which is what led us to the counterexample constructed in Section

- 2. As another quick application of Theorem 1.7, we obtain an explicit formula for a universal period of


one-dimensional tiles:

Corollary 3.5 (Universal period of one-dimensional tiles). Let F be a ﬁnite subset of Z, and let A ⊂ Z be a set such that 1F ∗1A is -periodic for some 1. We normalize 0 ∈ F. Then A is qn -periodic, where q is the least common multiple of and all the primes less than or equal to 2|F|, and n is the least common multiple of f for all f ∈ F\{0}.

Proof. From Theorem 1.7 we see that 1A is the linear combination of a ﬁnite number of terms, each of which is qn-periodic. The claim follows.

| |
|---|


As ﬁrst observed in [N], an easy application of the pigeonhole principle already gives that all onedimensional tilings are periodic; however, the bound produced is exponential in the diameter diam(F) if done naively. In contrast, the bound here is polynomial in the diameter (for ﬁxed |F|), and further is uniform over all tilings A of an -periodic set by a ﬁxed tile F, whereas the period produced by pigeonhole principle arguments will depend on the choice of tiling. In [S2] it was shown that if the cardinality |F| of the tile is not held ﬁxed, the period of a one-dimensional tiling can grow superpolynomially in the diameter n := diam(F) (in fact a lower bound exp(log2n/4loglogn) is demonstrated for inﬁnitely many n); there is also an exponential lower bound for indecomposable tilings of higher level [S3]. Conversely, the best known upper bound for the period for a tile of diameter n (with no restriction on |F|) is exp(Oε(n1/3+ε)) [B3].

Remark 3.6. In the special case of Corollary 3.5 when 1F ∗1A = 1, the dilation lemma of Tijdeman [T2, Theorem 1] (see also [CM] for an alternate proof) allows one to replace “all the primes less than or equal to 2|F|” with “all the primes dividing |F|”.

#### 4 Weak periodicity of two-dimensional tilings of level one

We now prove Theorem 1.4. Our starting point is the decomposition in Theorem 3.4. Accordingly, let m,ϕ1,...,ϕm,h1,...,hm,q be as in that theorem. If m = 1 then (18) ensures that A is qh1 -periodic, and we are already done. Henceforth we assume m 2, hence |F| 3.

Since there are at most |F|−1 vectors h1,...,hm, and they are all non-zero, one can ﬁnd a vector e˜ ∈ Z2 of size O|F|(1) which is incommensurable to all of the h1,...,hm. Next, let N be the least common multiple of all the determinant magnitudes |hi ∧hj| for 1 i < j m, thus by (8) one has

NZ2 ⊂ hi,hj (22) for all 1 i < j m. We also have the bounds

### N ∏

hi hj

1 i<j m

m

### ∏

(23)

hj )m−1 diam(F)(|F|−1)(|F|−2).

(

j=1

For any x ∈ Z2 and j = 1,...,m, we introduce the one-dimensional functions Px,j : Z → [0,1] by the formula

Px,j(n) := ϕj(x+ne), (24)

where e = qNe˜. These functions enjoy several useful properties: Proposition 4.1 (Properties of Px,j). Let x ∈ Z2.

- (i). One has ∑mj=1Px,j(n) = 0 mod 1 for all n ∈ Z.
- (ii). For each 1 j m, the map n  → Px,j(n) mod 1 is a polynomial of degree at most m−2.
- (iii). For any 1 i < j m, one has supn∈ZPx,i(n)+supn∈ZPx,j(n) 1.


We remark that the polynomiality property (ii) was previously observed in [B2, Lemma 4.3]. The linear forms αm1 mod 1,αm2 mod 1,α(m1+m2) mod 1 implicitly appearing in Section 2 are essentially examples of the polynomials appearing in Proposition 4.1, in the context of higher level tilings. However, we will eliminate this sort of “equidistributed” behavior in the level one case in Proposition 4.4 below.

Proof of Proposition 4.1. If starts with (18) and works modulo 1 to eliminate the 1A and 1E terms, we have m

### ∑

ϕj = 0 mod 1. (25)

j=1

Evaluating this at x+ne we obtain (i).

Now we prove (ii). Let 1 j m. From (22) we see that for any 1 i m distinct from j, that e = qNe˜ ∈ q hi,hj , that is to say we have

e = ai,jqhi +bi,jqhj (26) for some integers ai,j,bi,j. In particular, from the qhi -periodicity of ϕi we have

- ∆e−bi,jqhjϕi = 0

while from the qhj -periodicity of ϕj we have

- ∆e−bi,jqhjϕj = ∆eϕj.


If we then apply the discrete derivative operators ∆e−bi,jqhj for each 1 i m distinct from j in turn to

(25) to eliminate all the ϕi other than ϕj, we conclude that ∆m−1 e ∗ϕj = 0 mod 1.

(Note that the discrete derivative operators only involve convolution with integer-valued functions and are well deﬁned on functions that are only deﬁned modulo 1.) Evaluating this on the line {x+ne : n ∈ Z} using (24), we conclude the one-dimensional identity

∆m−1

1 Px,j = 0 mod 1.

That is to say, the (m−1)th discrete derivative of Px,j mod 1 vanishes. A simple induction on m then shows that Px,j mod 1 is a polynomial of degree at most m−2, giving (ii) as claimed.

Now we prove (iii). Let 1 i < j m. As in (26), we write e as a linear combination (26) of qhi,qhj. In particular, for any n1,n2 ∈ Z one has the identity

(x+n1e)+ai,j(n2 −n1)qhi = (x+n2e)−bi,j(n2 −n1)qhj. Evaluating (21) at this point, we conclude in particular that

ϕi((x+n1e)+ai,j(n2 −n1)qhi)+ϕj((x+n1e)−bi,j(n2 −n1)qhj) 1. Using (24), the qhi -periodicity of ϕi, and the qhj -periodicity of ϕj, we conclude that

Px,i(n1)+Px,j(n2) 1. Taking suprema in n1,n2, we obtain (iii).

| |
|---|


To exploit these properties, we use the following exponential sum estimate5 from analytic number theory.

- Lemma 4.2 (Exponential sum estimate). Let d 1, and let P: Z → R/Z be a nonconstant polynomial of degree at most d whose nonconstant coefﬁcients are rational with denominators having least common multiple Q; in particular P is periodic with period Q. Then one has


Proof. See [S].

Q

### ∑

e2πiP(n) d Q1−d1.

n=1

| |
|---|


We also remark that bounds of this type (but with the gain 1/d replaced by an exponent that decays exponentially in d) can be established by the Weyl differencing (or van der Corput) method; see for instance [T, Lemma 1.1.16].

- Lemma 4.3 (Polynomials only fail to equidistribute when periodic). Let P: Z → R/Z be a polynomial of some degree d that avoids an interval I of positive length in R/Z. Then P is periodic with period at most Od,I(1).


Proof. Since P is not equidistributed6, we see from the Weyl equidistribution theorem that all the nonconstant coefﬁcients of P must be rational. We let Q be the least common multiple of the denominators of these coefﬁcients, then P is periodic with period Q. By the Weierstrass approximation theorem, one can ﬁnd a trigonometric polynomial f (depending only on I) that is periodic with period 1, has mean zero, and is at least 1 outside of I. Then

Q

1 Q

### ∑

f(P(n)) 1.

n=1

- 5We thank Igor Shparlinski for this reference.
- 6We say that a function P: Z → R/Z is equidistributed if we have limN→∞ 2N1+1 ∑Nn=−N F(P(n)) = R/ZF(t) dt for all


continuous F : R/Z → R.

By the pigeonhole principle, we can thus ﬁnd a non-zero integer k = OI(1) such that

Q

1 Q

### ∑

e2πikP(n) I 1.

n=1

Note that the least common multiple of the denominators of kP(n) is d,I Q. Applying Lemma 4.2, we conclude that Q = Od,I(1), giving the claim.

| |
|---|


Let M be the least common multiple of |e˜∧hj| for 1 j m. Let Λ := e,qNMh1 be the lattice generated by e,qNMh1. Note in particular that

Λ ⊂ qZ2 ⊂ Z2. Proposition 4.4 (One-dimensional periodicity in each coset). On each coset x+Λ, the set A∩(x+Λ) is

QmM2Nqhj -periodic for some 1 j m, where Qm depends only on m and QmM2Nqhj ∈ Λ. Proof. From (8) one has

MZ2 ⊂ e ˜,hi for all 1 i m. In particular, for each 1 i m one has

qNMh1 = aiqhi +bie (27) where e = qNe˜ and ai,bi are the integers

h1 ∧e˜ hi ∧e˜

ai := NM

(28) and

h1 ∧hi e˜∧hi

bi := M

. In particular we have

Λ = e,aiqhi

- for all 1 i m. Fix x ∈ Z2. From (27) we have for any integers s,t that


ϕi(x+se+tqNMh1) = ϕi(x+(s+bit)e+taiqhi)

= ϕi(x+(s+bit)e)

= Px,i(s+bit)

thanks to the qhi -periodicity of ϕi, and (24). Also, since q is a multiple of , e is a multiple of q, and E is Z2-periodic, one has

1E(x+se+tqNMh1) = 1E(x). Thus we have the decomposition

1A(x+se+tqNMh1) = 1E(x)−

m

### ∑

Px,j(s+bit). (29)

j=1

Suppose ﬁrst that supn∈ZPx,j(n) = 1 for some 1 j m. Then from Proposition 4.1(iii) we have Px,i(n) = 0 for all other i, hence by Proposition 4.1(i), Px,j takes values in {0,1}. The decomposition (29) then simpliﬁes to

1A(x+se+tqNMh1) = 1E(x)−Px,j(s+bjt) for all s,t ∈ Z. From (27) and the change of variables s := s+bjt this implies that 1A(x+s e+tajqhj) = 1E(x)−Px,j(s )

for all s ,t ∈ Z. In particular, on the coset x+Λ, the function 1A is ajqhj -periodic, and hence M2Nqhj periodic by (28) and the construction of M. Note that this argument also shows that M2Nqhj ∈ Λ.

Now suppose we are in the opposite case that sup

Px,j(n) < 1

n∈Z

- for all 1 j m. From Proposition 4.1(iii) this implies that


sup

Px,i(n) 1/2

n∈Z

for all 1 i m with at most one exception; thus, with at most one exception, Px,i mod 1 takes values in [0,1/2] mod 1. By Proposition 4.1(ii) and Lemma 4.3 this implies that with at most one exception, the Px,i mod 1 are periodic with period Om(1). Using Proposition 4.1(i) and Lemma 4.3, an exception cannot occur. Taking a common denominator, we conclude that there is a positive integer Qm depending only on m, such that the Px,i mod 1 for all 1 i m are Qm -periodic; since all the Px,i have supremum strictly less than 1, we see that the Px,i are also Qm -periodic (note we no longer work modulo 1). From (29) we conclude that on the coset x+Λ, A is QmMNqh1 -periodic. Thus in either case we obtain the proposition.

| |
|---|


We ﬁnally conclude Theorem 1.4.

- Proof of Theorem 1.4. From (19) we can bound


m

### ∏

M

hj e ˜

j=1

|F| diam(F)|F|−1

and then from this and (19), (20), (23) the lattice Λ := qNe˜,qNMh1 has index in Z2 at most qN e ˜ qNM h1 / 2 |F| N2Mdiam(F)|F|−1

|F| diam(F)2(|F|−1)2.

A similar computation shows that the quantity L := QmM2Nq/  is an integer of magnitude at most L |F| M2N

|F| diam(F)(|F|−1)|F|. This establishes Theorem 1.4 (note from an inspection of the arguments that none of the quantities h1,...,hm,L,Λ constructed depends directly on A).

| |
|---|


#### 5 Converting weakly periodic tilings to periodic tilings

A simple pigeonholing argument7 shows that the existence of a weakly periodic tiling implies the existence of a periodic tiling (see, e.g., [B2, Theorem 2.3], [RX, Proposition 2.1]). In this section we introduce a constructive way to convert any weakly periodic tiling to a periodic tiling. This constructive approach allows us to achieve the signiﬁcantly better bound in Theorem 1.5, on the periods of the obtained periodic tiling. This bound is polynomial in the diameter of the tile F (for ﬁxed |F|).

We ﬁrst give a “slicing lemma” that allows one to “slice” the tile F along cosets along which the tiling set A already exhibits some periodicity, while retaining the periodicity of the set being tiled.

- Lemma 5.1 (Slicing lemma). Let  ,k 1 be natural numbers, and let h be a primitive element of Z2. Suppose that F is a ﬁnite subset of Z2, and A is a kh -periodic subset of Z2 such that 1F ∗ 1A is


Z2-periodic. Then for every coset x+ h of h , the function 1F∩(x+ h ) ∗1A is qksZ2-periodic, where q is the least common multiple of and all the primes less than or equal to 2|F|, and s is the least common multiple of the |h∧(f − f )| for all f, f ∈ F with f − f incommensurate with h.

Proof. We may assume that F intersects x+ h , as the claim is trivial otherwise; by relabeling we may then assume x ∈ F. By translating F and x we then may assume that x = 0 and 0 ∈ F. From Lemma

- 3.1(iii) we have 1F ∗1A = 1rF ∗1A


whenever r = 1 mod q. If we strengthen the condition on r to r = 1 mod qk, then for each f ∈ F ∩ h , we have r f − f ∈ qkh ⊂ kh , hence by the kh -periodicity of A we have

(1r(F∩ h ) −1F∩ h )∗1A = 0. Combining the two equations, we see that

1F ∗1A =1F∩ h ∗1A+ ∑

δr f ∗1A

f∈F\ h

and thus

1F∩ h ∗1A =1F ∗1A− ∑

δr f ∗1A

f∈F\ h

whenever r = 1 mod qk. Note that all the terms on the right-hand side are kh -periodic, since 1A is. Averaging over r and using the Arzelá-Ascoli theorem to extract a limit as in the proof of Theorem 1.7, we see that

1F∩ h ∗1A =1F ∗1A− ∑

ϕf

f∈F\ h

for some functions ϕf which are both kh -periodic and qkf -periodic. By (8) and the deﬁnition of s and q, each ϕf is qksZ2-periodic, as is 1F ∗1A, and the claim follows.

7This argument is analogous to Newman’s proof of the one-dimensional periodic tiling conjecture ([N]).

Remark 5.2. The above argument is in fact applicable to any d-dimensional one-periodic tiling of a periodic set. More precisely, it shows that if F ⊂ Zd is ﬁnite, h ∈ Zd is primitive and A ⊂ Zd is a

kh -periodic set such that 1F ∗1A is periodic, then the “slice” 1F∩ h ∗1A can be written as

1F∩ h ∗1A =1F ∗1A− ∑

ϕf,

f∈F\ h

where for any f ∈ F \ h , the function ϕf : Zd → [0,1] is kh,qkf -periodic, for some q(F) ∈ Z.

We now use the slicing lemma to improve the periodicity properties of a tiling. The slicing lemma allows us to reduce the two-dimensional tiling to a collection of one-dimensional tilings, by considering slices (or “cut and project” sets) of both the tile F and the tiling set A. We remark that similar argument was used in [JP] and [GL] in a different context.

Corollary 5.3 (Improving a tiling, I). Let  ,k 1 be natural numbers, and let h be a primitive element of Z2. Suppose that F is a ﬁnite subset of Z2, and A is a kh -periodic subset of Z2 such that 1F ∗1A is

Z2-periodic. Then there exists a qksZ2-periodic set A such that 1F ∗1A = 1F ∗1A , where q,s are as in

- Lemma 5.1. In fact we have the stronger statement


1F ∗1A∩( h +y) = 1F ∗1A ∩( h +y) for any coset h +y of h .

Proof. By applying an invertible linear transformation in SL2(Z) we may assume without loss of generality that the primitive element h is equal to (1,0). For every integer y ∈ Z, we introduce the one-dimensional slices

Fy := {x ∈ Z : (x,y) ∈ F} and

###### Ay := {x ∈ Z : (x,y) ∈ A}.

From Lemma 5.1 we know that for each y, the set 1Fy×{y} ∗1A is qksZ2-periodic, which in particular implies on taking slices that

1Fy ∗1Az = 1Fy ∗1Az+qks for all y,z ∈ Z, that is to say the map z  → 1Fy ∗1Az is periodic in z.

Let Σ denote the collection of all k -periodic subsets of Z; this is a ﬁnite set that contains Az for all z ∈ Z. Introduce an equivalence relation on Σ by declaring B ∼ B if 1Fy ∗1B = 1Fy ∗1B for all y ∈ Z. Thus we have Az+qks ∼ Az for all z ∈ Z. Now arbitrarily place a total ordering on the ﬁnite set Σ, and for each z ∈ Z let A˜z ∈ Σ denote the minimal element in the equivalence class {B ∈ Σ : B ∼ Az}. Then we have A˜z+qks = A˜z ∼ Az for all z ∈ Z. If we then deﬁne the modiﬁed set

A˜ := {(x,z) : z ∈ Z,x ∈ A˜z} then A˜ is qksZ2-periodic, and we have

1Fy×{y} ∗1A˜ = 1Fy×{y} ∗1A

for all y, which on taking horizontal slices implies that

1Fy×{y} ∗1A˜∩(Z×{z}) = 1Fy×{y} ∗1A∩(Z×{z}) for all y,z ∈ Z. Summing in y, we conclude that

1F ∗1A˜∩(Z×{z}) = 1F ∗1A∩(Z×{z}), giving the claim.

| |
|---|


Now we combine this corollary with the argument used to establish Proposition 4.1(ii) to convert weakly periodic tilings to periodic tilings.

- Theorem 5.4 (Improving a tiling, II). Let 1 and m 2 be natural numbers, and let h1,...,hm be pairwise incommensurable elements of Z2. Suppose that F is a ﬁnite subset of Z2, that E is an


Z2-periodic subset of Z2, and A is a tiling of E by F. Suppose that A is weakly periodic, and more speciﬁcally that A is the disjoint union A = A1  ··· Am where each Aj is hj -periodic. Then there exists a MZ2-periodic set A such that 1F ∗1A = 1F ∗1A = 1E, where M is an integer with the bound

m

### ∏

hi )m+|F|(|F|−1)/2diam(F)m|F|(|F|−1)/2.

M |F| (

i=1

Furthermore each 1F ∗1Aj is NjZ2-periodic for some integer Nj with bound

m

### ∏

hi )m−1 hj .

Nj |F| (

i=1

Proof. We can locate an element e˜ ∈ Z2 of magnitude Om(1) which is incommensurable with all of the hi. We deﬁne N to be the least common multiple of the |hi ∧hj| for 1 i < j m, and set e := Ne˜. Observe that

m

### N ∏

### ∏

hi )m−1.

|hi ∧hj| (

1 i<j m

i=1

Let 1 j m. We have the identity

1F ∗1Aj+ ∑

1F ∗1Ai = 1E

i∈{1,...,m}\{j}

To eliminate all the terms besides 1F ∗1Aj we apply discrete differentiation operators as in the proof of Proposition 4.1(ii). From (8) we can write

e = ai,j hi +bi,j hj

for all 1 i m distinct from j and some integers ai,j,bi,j. Then from the periodicity properties of the Ai, Aj we have

∆e−bi,j hj(1F ∗1Ai) = 0

and

∆e−bi,j hj(1F ∗1Aj) = ∆e(1F ∗1Aj); also from the Z2-periodicity of E one has

∆e−bi,j hj1E = 0. Applying each of the discrete derivative operators ∆e−bi,j hj in turn, we conclude that ∆m−1 e (1F ∗1Aj) = 0.

Thus, for any x, the map n  → 1F ∗1Aj(x+ne) is polynomial in n; but it is also bounded, hence constant. Thus 1F ∗1Aj is e -periodic and hj -periodic, hence by (8) it is NMjZ2-periodic for some integer Mj with Mj m hj . We now split hj = kjh j where kj is a natural number and h j is primitive. By Corollary

- 5.3 we see that we can ﬁnd a qjkjsjZ2-periodic set A j such that 1F ∗1Aj = 1F ∗1A


, where qj = NMjCj for some Cj = O|F|(1), and sj is a positive integer with the bound

j

sj ( h j diam(F))|F|(|F|−1)/2. We conclude that qjkjsj = NLj with

Lj |F| hj 1+|F|(|F|−1)/2diam(F)|F|(|F|−1)/2. Summing over j, we have

m

### ∑

1F ∗

1A

= 1F ∗1A = 1E.

j

j=1

In particular this shows that ∑mj=11A

is bounded by 1, that is to say the A j are disjoint. If we set A := mj=1A j, we then have 1F ∗1A = 1F ∗1A = 1E, and A is MZ2-periodic with

j

m

m

### ∏

### ∏

hi )m+|F|(|F|−1)/2diam(F)m|F|(|F|−1)/2

M N

Lj |F| (

j=1

i=1

giving the claim. We can now conclude the proof of Theorem 1.5.

| |
|---|


- Proof of Theorem 1.5. The claim is trivial for |F| = 1, so suppose |F| > 1. By Theorem 1.4, there exist m,h1,...,hm,L obeying the conclusions of that theorem, such that A is the disjoint union of


Lhj -periodic sets for j = 1,...,m. Applying Theorem 5.4 (with replaced by L), we can ﬁnd an LM Z2-periodic set A with 1F ∗1A = 1F ∗1A = 1E, where

m

- 1

- 2(|F|+2)(|F|−1)diam(F)


- 1

- 2|F|(|F|−1)2.


### ∏

hi ) Using the bounds (3), (4), we have

M |F| (

i=1

- 1

- 2(|F|+2)(|F|−1)3diam(F)


- 1

- 2|F|(|F|−1)2.


LM |F| diam(F)|F|(|F|−1)diam(F) The claim follows.

| |
|---|


#### 6 One-periodic tilings

Call a set A one-periodic if A is h -periodic for some non-zero h. For any given tile F of Z2, we consider8 the following question:

Question 6.1. Let F be a ﬁnite tile of Z2. Does there exist a tiling of Z2 by F which is not one-periodic?

The answer to this question is positive for some tiles and negative for others, as the following examples show:

- (i). If F0 is the square {0,1}2, then every tiling of Z2 by F0 can be seen to be either (2,0) -periodic or (0,2) -periodic, and hence the answer to Question 6.1 is negative in this case. More generally,

from [S5, Theorem 19] it follows that the answer to Question 6.1 is negative for any tile of cardinality 4 that contains zero and generates Z2.

- (ii). On the other hand, in Subsection 1.3 it was shown that the four-element tile F1 := {0,2}×{0,1} (which does not generate Z2) admits tilings A of Z2 that are not one-periodic. Note that if A is a tiling of Z2 by F2, then 2A is a tiling of Z2 by F2 := 2F1 +{0,1}2 = {0,4}×{0,2}+{0,1}2. Thus the answer to Question 6.1 is positive for the tiles F1,F2. In particular it is possible to have non-one-periodic tilings even when the tile F contains 0 and generates all of Z2 as an abelian group.
- (iii). If the tile F is collinear (it lies in a one-dimensional afﬁne subspace of R2), then Corollary 3.5 implies that all tilings of Z2 by F are h -periodic for some universal period h that is parallel to the line that F lies in. Hence the answer to Question 6.1 is negative in this case.
- (iv). If the tile F is “connected” in the sense that F + [−12, 12]2 is simply connected, then by [GN, Theorem 5.5], F admits only one-periodic tilings of Z2. Hence the answer to Question 6.1 is negative in this case. This of course contains the ﬁrst part of (i) as a special case.

- (v). From [S5, Theorem 17] it follows that if F has prime order |F| = p then every tiling of Z2 by F is pZ2-periodic, so the answer to Question 6.1 is negative in this case.


We do not have a full classiﬁcation of the tiles F which have a negative answer to Question 6.1. However, the results presented in our paper do at least show that this question is decidable for any given tile, even if one replaces the set Z2 by more general periodic subsets of Z2.

- Theorem 6.2 (Decidability of Question 6.1). There is an algorithm which, when given periodic subset E of Z2 and a ﬁnite set F that tiles E as input9, decides in ﬁnite time whether F admits a non one-periodic tiling of E, or not.


8We thank Mihalis Kolountzakis (private communication) for suggesting this question. 9Note that a periodic subset E of Z2 can be stored using a ﬁnite amount of memory, by ﬁrst storing a pair of generators for

the periodicity lattice, and then storing a coset representative for each of the cosets of that lattice that lie in E.

Proof. Suppose that F is a tile of an Z2 periodic set E. From Theorem 1.4 and Theorem 5.4 we can compute positive integers m,N1,...,Nm and pairwise incommensurable h1,...,hm ∈ Z2, with the property that for every tiling set A of E by F, there exists partitions A = A1  ··· Am and E = E1  ··· Em, where for each 1 j m, Aj is hj -periodic, Ej is NjZ2-periodic, and Aj is a tiling set for Ej by F: 1F ∗1Aj = 1Ej. We write hj = kjh j for a (computable) natural number kj and primitive h j. By Corollary 5.3, we can then compute positive integers M1,...,Mm such that whenever A,A1,...,Am,E1,...,Em are as above, one can ﬁnd an MjZ2-periodic set A j for each j = 1,...,m such that

###### Aj ∩( h j +y) ≡F A j ∩( h j +y)

for all cosets h j +y, where we use A ≡F A to denote the equivalence relation 1F ∗1A = 1F ∗1A . By construction we have m

m

m

### ∑

### ∑

### ∑

1F ∗1A

1F ∗1Aj =

1Ej = 1E.

=

j

j=1

j=1

j=1

Conversely, if for each j = 1,...,m we locate a MjZ2-periodic set A j such that

m

### ∑

1F ∗1A

j

j=1

= 1E (30)

and then for each coset A j ∩( h j +y) we ﬁnd a hj -periodic subset Aj, h

j +y of h j +y such that Aj, h

j +y ≡F A j ∩( h j +y) (31) then the sets

Aj :=

Aj, h

j +y

h j +y∈Z2/ h j

are such that

Aj ≡F A j and hence m

### ∑

1F ∗1Aj = 1E.

j=1

In particular, the Aj are disjoint and their union

m

m

A :=

Aj =

j=1

j=1 y∈ h j ⊥

Aj, h

j +y (32)

tiles E by F. Thus, we have a way of completely describing all the tilings A of E by F: we ﬁrst locate all tuples (A 1,...,A m) of MjZ2-periodic sets A j obeying (30), then for each such tuple, each j = 1,...,m, and each coset h j +y, we choose a hj -periodic subset Aj, h

j +y obeying (31), then the unions (32) give all the possible tilings of E by F.

Note that there are only ﬁnitely many MjZ2-periodic subsets of Z2 (in fact there are 2M2j many), so there are only ﬁnitely many possible tuples (A 1,...,A m) that can arise in this fashion. For each such tuple,

the identity (30) can be veriﬁed or disproved in ﬁnite time. Hence we can completely enumerate all the possible tuples (A 1,...,A m) that can arise in the above construction. Similarly, for each coset h j +y and any ﬁxed choice of A j, the set of all hj -periodic subsets Aj, h

j +y of h j +y obeying (31) is also ﬁnite and can be enumerated in ﬁnite time. However, there are inﬁnitely many such cosets, and hence one may potentially need to loop over an inﬁnite number of choices in order to enumerate all possible tilings (cf. the tilings (1), (2)).

Fortunately, for the question of whether there admit non-one-periodic tilings we do not need to exhaust over inﬁnitely many possibilities, and can instead reason as follows. Let us call a slice A j ∩( h j +y) of an MjZ2-periodic set A j by a coset ( h j +y) a chameleon if there exists a hj -periodic subsets Aj, h

j +y of h j +y obeying (31) which is not equal to A j ∩( h j +y), in which case we say that A j contains a chameleon slice. Note that for any given MjZ2-periodic set A j, the slices of A j ∩( h j +y) repeat periodically in y and hence one can determine whether A j contains a chameleon slice or not in ﬁnite time.

Suppose ﬁrst that A arises from a tuple (A 1,...,A m) with the property that at most one of the A j admits a chameleon slice, thus we have some j0 such that A j does not admit a chameleon slice for any j = j0. Then for j = j0, the set Aj, h

j +y is necessarily equal to A j ∩( h j +y) for every y, hence Aj is

necessarily equal to the MjZ2-periodic set A j. Since Aj0 is also hj0 -periodic, we conclude that the set A constructed in (32) is one-periodic in this case.

Now suppose that A arises from a tuple (A 1,...,A m) with the property that there are at least two sets A j

+y2) respectively. Thus for i = 1,2, we may ﬁnd a hji -periodic subset A(i) of h j

,A j

which admit chameleon slices A j

###### ∩( h j

+y1), A j

###### ∩( h j

1

2

1

1

2

2

+yi that is distinct from (A )(i) := A j

+yi such that

###### i ∩ h j

i

i

###### A(i) ≡F (A )(i).

In particular, if we set A := mj=1A j, and let A be the set formed from A by replacing (A )(i) with A(i) for i = 1,2, so that

2

### ∑

(1A(i) −1(A )(i)), then A is equivalent to A :

1A = 1A +

i=1

1A ∗1F = 1A ∗1F = 1E. We claim that A is not one-periodic. Since 1A is MZ2-periodic for some M, it sufﬁces to show that ∑2i=1(1A(i) −1(A )(i)) is not one-periodic. But each summand 1A(i) −1(A )(i) is a non-trivial one-periodic function supported on the coset h j

+yi , and the claim is then evident from the incommensurability of h j

i

and h j

.

1

2

From the above discussion, we conclude that F admits non-one-periodic tilings if and only if there exist MjZ2-periodic sets A j for j = 1,...,m obeying (30) such that at least two of the A j admit chameleon slices. Since we can computably enumerate all the tuples (A 1,...,A m) obeying (30) and test all of them for chameleon slices, the claim follows.

| |
|---|


Informally, the proof of Theorem 6.2 tells us that all the tilings of a given periodic set E by a given

tile F arise from starting with a doubly periodic tiling A = A 1  ··· A m (which is drawn from a ﬁnite list of such tilings) and performing a (possibly inﬁnite) number of “slide moves” in which one or more

slices A j ∩( h j +y) is replaced with an equivalent (one-periodic) set Aj, h

j +y, in the spirit of (1) or (2).

In principle, this should reduce any reasonable question about such tilings to a ﬁnite computation for any ﬁxed choice of E,F, with the existence of non-one-periodic tilings serving as just one representative example of such a question.

#### Acknowledgments

We thank Jarkko Kari for alerting us to the relevant references [K], [KS], [S4]. We also thank Mihalis Kolountzakis for helpful suggestions, and Nishant Chandgotia and several readers of the second author’s blog for further comments and corrections. We have also implemented several suggestions of the anonymous referee.

#### References

[B] R. Berger, The undecidability of the domino problem, Mem. Amer. Math. Soc. Not. 66 (1966), 72. 3

- [B2] S. Bhattacharya, Periodicity and Decidability of Tilings of Z2, Amer. J. Math., 142, (2020), 255–266. 3, 4, 5, 6, 10, 15, 19
- [B3] A. Bíró, Divisibility of integer polynomials and tilings of the integers, Acta Arith. 118 (2005), 117–127. 4, 14


[CM] E. Coven, A. Meyerowitz, Tiling the integers with translates of one ﬁnite set, J. Algebra 212 (1999), no. 1, 161–174. 14

[GN] D. Girault-Beauquier, M. Nivat, Tiling the plane with one tile, In Topology and category theory in computer science (Oxford, 1989), Oxford Sci. Publ., 291–333. Oxford Univ. Press, New York, 1991. 3, 23

[GL] R. Greenfeld, N. Lev, Spectrality and tiling by cylindric domains, Journal of Functional Analysis,

271 (2016), 2808–2821. 20

[GL2] R. Greenfeld, N. Lev, Spectrality of product domains and Fuglede’s conjecture for convex polytopes, Journal d’Analyse Mathematique, 140 (2020) 409–441. 11

- [GR] A. Granville, Z. Rudnick, Torsion points on curves, Equidistribution in number theory, an introduction, 85–92, NATO Sci. Ser. II Math. Phys. Chem., 237, Springer, Dordrecht, 2007. 5
- [GS] B. Grunbaum, G. C. Shephard, Tilings and Patterns. New York: Freeman 1987. 2


[HIPRV] C. D. Haessig, A. Iosevich, J. Pakianathan, S. Robins, L. Vaicunas, Tiling, circle packing and exponential sums over ﬁnite ﬁelds, Anal. Math. 44 (2018), no. 4, 433–449. 10

[HN] B. Helffer, J. Nourrigat, Caractérisation des opérateurs hypoelliptiques homogènes invariants à gauche sur un groupe de Lie nilpotent gradué, Comm. Partial Differential Equations 4 (1979), 899–958. 3

[IMP] A. Iosevich, A. Mayeli, J. Pakianathan, The Fuglede conjecture holds in Zp ×Zp, Anal. PDE 10

(2017), no. 4, 757–764. 10 [IP] A. Iosevich, S. Pedersen, Spectral and tiling properties of the unit cube, Int. Math. Res. Not. IMRN

(1998), no. 16, 819–828. [JP] P. E. T. Jorgensen, S. Pedersen, Spectral pairs in cartesian coordinates, Journal of Fourier Analysis and Applications, 5, (1999), 285–302. 20

- [K] J. Kari, Low-Complexity Tilings of the Plane, preprint. arXiv:1905.04183 3, 26

- [K2] R. Kenyon, Rigidity of planar tilings, Invent. Math. 107 (1992), 637–651. 3

[KL] M. N. Kolountzakis, J. C. Lagarias, Structure of tilings of the line by a function, Duke Math. J. 82

(1996), 653–678. 3 [KL2] M. Kolountzakis, N. Lev, On non-periodic tilings of the real line by a function, Int. Math. Res. Not. IMRN 15 (2016), 4588–4601. 6 [KL3] M. N. Kolountzakis, N. Lev, Tiling by translates of a function: results and open problems, preprint.

arXiv:2009.09410 3, 6

[KS] J. Kari, M. Szabados, An algebraic geometric approach to Nivat’s conjecture Automata, languages, and programming. Part II, 273–285, Lecture Notes in Comput. Sci., 9135, Springer, Heidelberg, 2015 8, 10, 26

[LM] H. Leptin, D. Müller, Uniform partitions of unity on locally compact groups, Adv. Math. 90 (1991), no. 1, 1–14. 3

- [L] B. Liu, Periodic structure of translational multi-tilings in the plane, preprint. arXiv:1809.03440 3, 6

[L2] S. Lang, Division points on curves, Ann. Mat. Pura Appl. 70 (1965), 229–234. 5 [LW] J. C. Lagarias, Y. Wang, Tiling the line with translates of one tile, Invent. Math. 124 (1996), no.

1-3, 341–365. 2, 3 [M] P. McMullen, Convex bodies which tile space by translations, Mathematika 27 (1980), 113–121. 3

- [M2] P. McMullen, Acknowledgement of priority: “Convex bodies which tile space by translation”, Mathematika, 28, (1981), no. 2, 191. 3
- [N] D. J. Newman, Tesselation of integers, J. Number Theory 9 (1977), no. 1, 107–111. 2, 3, 14, 19




[RX] H. Rao, Y. M. Xue, Tiling Z2 with translations of one set, Discrete Mathematics and Theoretical Computer Science, DMTCS, (2006), 8, 129-–140. 19

- [R] R. M. Robinson, Undecidability and nonperiodicity for tilings of the plane, Invent. Math. 12 (1971), 177–209. 3


- [S] S. B. Stechkin, Estimate of a complete rational trigonometric sum, Trudy Mat. Inst. Steklov. 143

(1977), 188–220. Translated in Proc. Steklov Inst. Math. 1 (1980), 201–220. 16

- [S2] J. Steinberger, Tilings of the integers can have superpolynomial periods, Combinatorica 29 (2009), no. 4, 503–509. 14
- [S3] J. Steinberger, Indecomposable tilings of the integers with exponentially long periods, Electron. J. Combin. 12 (2005), Research Paper 36, 20 pp. 14

[SS] S. Szabó, A. Sands, Factoring groups into subsets. Lecture Notes in Pure and Applied Mathematics,

257. CRC Press, Boca Raton, FL, 2009. 3

- [S4] M. Szabados, An Algebraic Approach to Nivat’s Conjecture, TUCS Dissertations No. 234 (2018), Turku Centre for Computer Science. 8, 12, 26
- [S5] M. Szegedy, Algorithms to tile the inﬁnite grid with ﬁnite clusters, Proceedings of the 39th Annual Symposium on Foundations of Computer Science (FOCS ’98), IEEE Computer Society, Los Alamitos, CA, (1998), 137–145. 3, 10, 11, 23


- [T] T. Tao, Higher order Fourier analysis, Graduate Studies in Mathematics, 142. American Mathematical Society, Providence, RI, (2012). 16


- [T2] R. Tijdeman, Decomposition of the integers as a direct sum of two subsets, Number theory (Paris, 1992–1993), 261–276, London Math. Soc. Lecture Note Ser., 215, Cambridge Univ. Press, Cambridge, 1995. 10, 14


[V] B. A. Venkov, On a class of Euclidean polyhedra, Vestnik Leningrad Univ. Ser. Math. Fiz. Him. 9

(1954), 11–31. 3 [WV] H. A. G. Wijshoff, J. van Leeuwen, Arbitrary versus periodic storage schemes and tessellations of the plane using one type of polyomino, Inform. and Control 62 (1984), 1–25. 3

###### AUTHORS

Rachel Greenfeld UCLA Department of Mathematics Los Angeles, CA 90095-1555 greenfeld [at] math.ucla [dot] edu https://www.math.ucla.edu/~greenfeld

Terence Tao UCLA Department of Mathematics Los Angeles, CA 90095-1555 tao [at] math.ucla [dot] edu https://www.math.ucla.edu/~tao

