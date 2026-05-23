DISCRETE ANALYSIS, 2019:4, 20 pp. www.discreteanalysisjournal.com

## arXiv:1810.12791v2[math.CO]9May2019

# Logarithmic bounds for Roth’s theorem via almost-periodicity

###### Thomas F. Bloom Olof Sisask

Received 30 October 2018; Published 10 May 2019

Abstract: We give a new proof of logarithmic bounds for Roth’s theorem on arithmetic progressions, namely that if A ⊆ {1,2,...,N} is free of three-term progressions, then |A| N/(logN)1−o(1). Unlike previous proofs, this is almost entirely done in physical space using almost-periodicity.

##### 1 Introduction

We shall prove here the following version of Roth’s theorem on arithmetic progressions.1 Theorem 1.1. Let r3(N) denote the largest size of a subset of {1,2,...,N} with no non-trivial three-term arithmetic progressions. Then

N

r3(N)

(logN)1−o(1).

Roth [9] proved this with a denominator of loglogN in the 1950s, laying the foundation for using harmonic analysis to tackle problems of an additive nature in rather arbitrary sets of integers. Subsequent improvements were made by Heath-Brown [7] and Szemerédi [14], increasing the denominator to (logN)c for some positive constant c, and then by Bourgain [3, 4], obtaining such a bound with c = 12 −o(1) and then c = 23 −o(1). Sanders [11, 10] then proved this with c = 34 −o(1) and was then the ﬁrst to reach the logarithmic barrier in the problem, obtaining c = 1−o(1). The best bounds currently known were then given by the ﬁrst author [2],

r3(N)

(loglogN)4 logN

N.

Sanders’s result [10] had a power of 6 in place of the 4 here, but the two techniques were quite orthogonal: [2] proceeds by getting structural information about the spectrum of the indicator function of a set A with few three-term progressions,

1For details of the asymptotic notation we use, see the next section.

c 2019 Thomas F. Bloom and Olof Sisask

cb Licensed under a Creative Commons Attribution License (CC-BY) DOI: 10.19086/da.7884

whereas [10] employed a result on the almost-periodicity of convolutions [6] due to Croot and the second author, coupling this with a somewhat intricate combinatorial thickening argument on the physical side.

This article presents a fairly simple proof of logarithmic bounds for Roth’s theorem, showing that they follow quite directly from almost-periodicity results along the lines of [6]. Our focus is on clarity of exposition, and we therefore do not take steps to optimise the power of the loglogN term that we would obtain.

Some of the ideas in the present paper have been inspired by the authors’ ongoing work on super-logarithmic bounds for Roth’s theorem. In particular, there is a close relationship between Lp norms of convolutions considered in this paper and the higher additive energies of the set of large Fourier coefﬁcients used in the work of Bateman and Katz [1] achieving super-logarithmic bounds in Roth’s theorem over Fn3.

##### 2 Notation, main theorem, and outline of proof Notation for averaging and counting

The argument proceeds by studying high Lp-norms of the convolution 1A ∗1A of the indicator function of a set A with itself. We use the following conventions for these objects. Let G be a ﬁnite abelian group and let f,g : G → C be functions. We deﬁne the convolution f ∗g : G → C by

f ∗g(x)=∑

f(y)g(x−y).

y

In considering Lp-norms on subsets of G, it will be convenient to sometimes use sums and to sometimes use averages. To distinguish between these, we write, for B ⊆ G,

f p p(B) = ∑

|f(x)|p and f L pp(B) = Ex∈B|f(x)|p,

x∈B

where Ex∈B = |B1| ∑x∈B. If we write just f p then we mean f Lp(G). As usual f ∞ = supx∈G|f(x)|. We also write

f,g = ∑

###### f(x)g(x).

x∈G

Finally, if A ⊆ B ⊆ G, we write 1B for the indicator function of B, and µB for both the function 1B/|B| and for the measure µB(A) = |A|/|B|; this latter quantity is known as the relative density of A in B. In the case B = G, this is known simply as the density of A.

Where we have chosen discrete normalisations, the reader who is used to ‘compact normalisations’ should ﬁnd comfort in the fact that much of what we shall consider is normalisation-independent. For example, regardless of normalisationconvention, the function 1A ∗µB is always

1A ∗µB(x) = Et∈B1A(x−t).

We shall count three-term arithmetic progressions (3APs) across various sets. For A,B,C ⊆ G, with 2·B := {2x : x ∈ B}, we write

T(A,B,C)= ∑

1A(x)1B(y)1C(z) = 1A ∗1C,12·B

x,y,z x+z=2y

for the number of 3APs in G with starting point in A, mid-point in B and end-point in C. If A = B = C we write just T(A). Note that this counts also trivial 3APs, where x = y = z.

###### Main theorem

Our main theorem, then, is the following.

- Theorem 2.1 (Roth’s theorem, counting version). Let G be a ﬁnite abelian group of odd order, and let A ⊆ G be a set of density α > 0. Then


T(A) exp −Cα−1(log2/α)C |A|2

where C > 0 is an absolute constant. In particular, if α (loglog|G|)C/log|G| then A contains a non-trivial three-term arithmetic progression.

This immediately implies Theorem 1.1, by embedding a subset of {1,...,N} into G = Z/(2N +1)Z in the natural way, so that a (non-trivial) 3AP found in the set in G is also a (non-trivial) 3AP in the original set.

To prove Theorem 2.1, we employ a density increment strategy following the framework of Roth [9].

###### Density increments

Starting with A ⊆ G of density α, we show that if A has few 3APs then there is a structured part B ⊆ G — in some cases a genuine subgroup — such that some translate of A has increased density on B:

µB((A−x)∩B) (1+c)α

where c > 0. Such a condition is succinctly summarised by 1A ∗ µB ∞ (1+c)α. We then repeat the argument with G replaced by B and A replaced by A2 := (A−x)∩B: if A2 has few 3APs, then we ﬁnd a new structured piece and a new, denser subset, and repeat the argument. This cannot go on for too long, since the densities can never increase beyond 1. At this point we will have shown that some translate of A has many 3APs, which by translation-invariance of 3APs implies that A itself does.

###### Outline of argument

Finding the structured piece B and the appropriate translate of A relies on an almost-periodicity result for convolutions that says that 1A ∗1A is approximately translation-invariant in Lp by something like a large subgroup. How we apply this depends on which of two cases we are in. If 1A ∗1A p is small, where p ≈ log(1/α), then the L2p-almost-periodicity result is particularly efﬁcient, and has as a straightforward consequence that if T(A) deviates much from α|A|2 then it must have a density increment on some subgroup-like object B. If, on the other hand, 1A ∗1A p is large, then, by Lp-almost-periodicity, we see that 1A ∗1A ∗µB p must also be large for some group-like B, from which a density increment is immediate.

###### Asymptotic notation

We employ both Vinogradov notation X Y and the ‘constantly changing constant’. Thus, any statement involving one or more expressions of the form Xi Yi should be considered to mean “There exist absolute constants Ci > 0 such that a true statement is obtained when Xi Yi is replaced by Xi CiYi.” Similarly, any sequence of statements involving unspeciﬁed constants c,C should be read with the understanding that there exist positive constants to make the statements true, and that these constants may change from instance to instance. Generally the expectation will be that c 1 and C 1, a device intended to guide the reader.

##### 3 The ﬁnite ﬁeld argument

As is customary, we begin with a proof in the ﬁnite ﬁeld case, as there are very few technical hurdles here. Our goal is the following density increment result.

- Theorem 3.1. If A ⊆ Fnq has density α and T(A) α2 |A|2 then there is a subspace V with codimension α α−1 such that 1A ∗µV ∞ 54α.


The notation X α Y here means that X (log(2/α))CY. We prove this result by considering two possibilities: µA ∗1A 2m is small for some large m, and µA ∗1A 2m is large

for some large m. It clearly sufﬁces to show that both possibilities (combined with T(A) α3/2) lead to a suitable density increment.

We will require the following almost-periodicity result. While it is not explicitly given in the literature, the deduction from the almost-periodicity results proved by Croot and the second author [6] is routine, and is given in an appendix.

- Theorem 3.2. Let p 2 and ε ∈ (0,1). Let G = Fnq be a vector space over a ﬁnite ﬁeld and suppose A ⊆ G has |A| α|G|. Then there is a subspace V G of codimension


d pε−2log(2/ε)2log(2/α) such that, for each t ∈ V,

µA ∗1A ∗µV −µA ∗1A p ε µA ∗1A 1p//22 +ε2.

- Lemma 3.3. Suppose A ⊆ Fnq has density α and T(A) α2 |A|2. If m log(2/α) is such that µA ∗1A 2m 10α,


then there is a subspace V with codimension α mα−1 such that 1A ∗µV ∞ 54α. Proof. Apply Theorem 3.2 with p = 4m and ε = α1/2/100 to get a subspace V of the required codimension such that

µA ∗1A ∗µV −µA ∗1A 4m ε µA ∗1A 12/m2 +ε2

α 100

α−1/2 µA ∗1A 12/m2 +1 α/8

by our assumption on µA ∗1A 2m. Now, if 1/r+1/4m = 1, Hölder’s inequality gives µA ∗1A ∗1−2·A ∗µV −µA ∗1A ∗1−2·A ∞ 1−2·A r µA ∗1A ∗µV −µA ∗1A 4m

= α2−1/4m/8

α2/4. Since µA ∗1A ∗1−2·A(0) α2/2 by assumption, this means that

1A ∗1A ∗1−2·A ∗µV(0) = 1A ∗1A ∗µV,12·A 4 3α3.

It remains to convert this upper bound on the average into a lower bound for 1A ∗µV ∞. There are a number of ways to do this, either in Fourier space or physical space; here we present a particularly short method using purely physical arguments.

Suppose that 1A ∗µV ∞ (1+c)α, and let f = (1+c)−1α−11A ∗µV, so that 0 f 1. In particular,

1−c 1+c

0 (1− f)∗(1− f) = f ∗ f −2 f 1 +1 = (1+c)−2α−21A ∗1A ∗µV −

.

It follows that

(1−c2)α2 1A ∗1A ∗µV(x) for all x. In particular, taking the inner product with 12·A implies

- 3

- 4


α3,

(1−c2)α3 1A ∗1A ∗µV,12·A

and choosing c = 1/4, say, gives a contradiction.

| |
|---|


On the other hand, if µA ∗ 1A 2m is very large, then this directly implies a large density increment, without any assumptions on T(A).

- Lemma 3.4. If µA ∗1A 2m 10α, then there is a subspace V of codimension α mα−1 such that 1A ∗µV ∞ 5α.


Proof. Applying Theorem 3.2 as in the proof of Lemma 3.3, but with p = 2m, there is a subspace V of the required codimension such that

α 100

α−1/2 µA ∗1A 1m/2 +1 . It follows that

µA ∗1A ∗µV −µA ∗1A 2m

α 100

α−1/2 µA ∗1A 1m/2 +1 µA ∗1A 2m −

µA ∗1A ∗µV 2m µA ∗1A 2m −

α 100

α−1/2 µA ∗µA 12/m2 +1

by nesting. Since µA ∗1A 2m 10α, this is at least 5α, say. Hence

1A ∗µV ∞ µA ∗1A ∗µV ∞ µA ∗1A ∗µV 2m 5α, and we have a density increment.

| |
|---|


The two preceding lemmas together immediately imply Theorem 3.1. A routine iterative application of this theorem then proves the ﬁnite ﬁeld version of Theorem 2.1: we can increase the density as in the theorem at most Clog(1/α) times before reaching 1, and so a translate of A must have plenty of 3APs on some subspace of codimension α α−1.

##### 4 Bohr sets and Lp-almost-periodicity

Following Bourgain [3], the role played by subspaces in the density increment argument above will in general groups be played by Bohr sets, whose basic theory we review below. For proofs of these results, one may consult [15]. Throughout, G will be a ﬁnite abelian group, and we write G = {γ : G → C× : γ a homomorphism} for the dual group of G, the group operation being pointwise multiplication of functions.

Deﬁnition 4.1 (Bohr sets). For a subset Γ ⊆ G and a constant ρ 0, we write

Bohr(Γ,ρ) = {x ∈ G : |γ(x)−1| ρ for all γ ∈ Γ}

and call this a Bohr set. Denoting it by B, we call rk(B) := |Γ| the rank of B and ρ its radius.2 We shall often need to narrow the radius: if τ 0, we write Bτ = Bohr(Γ,τρ). If furthermore B = Bohr(Λ,δ) where Λ ⊇ Γ and δ ρ, then we write B B and say that B is a sub-Bohr set of B; note that this implies that B ⊆ B as sets.

Lemma 4.2 (Size estimates). If B is a Bohr set of rank d and radius ρ 2, then

- (i) |B| (ρ/2π)d|G|,
- (ii) |Bτ| (τ/2)3d|B| for τ ∈ [0,1].


One deﬁcit of Bohr sets compared to subspaces is that the number of 3APs in a Bohr set B need not be approximately |B|2 — the trivial upper bound — as it would be for a subspace. The standard work-around for this is to work with pairs (B,B ) of Bohr sets where B is a radius-narrowed copy of B. Provided B is regular, deﬁned as follows, one then has T(B,B ,B) ≈ |B||B |, matching the trivial upper bound.

Deﬁnition 4.3 (Regularity). We say that a Bohr set B of rank d is regular if

|B1+τ| |B|

1−12d|τ|

1+12d|τ|

whenever |τ| 1/12d.

Note in particular that if B is regular, then |B+Bc/rk(B)| 2|B|, for example. Importantly, regular Bohr sets are in plentiful supply, a fact that we use frequently:

Lemma 4.4. If B is a Bohr set, then there is a τ ∈ [12,1] for which Bτ is regular.

Let us now assume that G has odd order, so that the map x  → 2x is injective on G. The square-root map is then well-deﬁned on G, and we write γ1/2 for the unique element in G such that (γ1/2)2 = γ. We extend this to sets via Γ1/2 = {γ1/2 : γ ∈ Γ}. Deﬁnition 4.5 (Set-dilation of Bohr sets). If B = Bohr(Γ,ρ) is a Bohr set, we write 2·B for the Bohr set Bohr(Γ1/2,ρ).

Note that this is compatible with the notation for set-dilation: 2·B = {2x : x ∈ B}.

- Lemma 4.6. If B is a Bohr set and τ 0, then (2·B)τ = 2·(Bτ).


In particular, if B is regular, then so is 2·B.

We shall use the following almost-periodicity result for convolutions that works relative to Bohr sets. While it does not explicitly appear in the literature, it is not a far cry from the combination of the almost-periodicity ideas of [6] with the Chang–Sanders lemma on large spectra as in [5, 13]. The main differences are the presence of an L1-norm (as opposed to an L0-type estimate in [6]) and that the Lp-norms are restricted to a Bohr set. We delay the proof of this (and some generalisations) to Section 6.

2Γ,ρ cannot necessarily be read off from the set itself, but are considered part of the deﬁning data.

- Theorem 4.7 (Lp-almost-periodicity relative to a Bohr set). Let m 1 and ε,δ ∈ (0,1). Let A,L be subsets of a ﬁnite abelian group G, with η := |A|/|L| 1, and let B ⊆ G be a regular Bohr set of rank d and radius ρ. Suppose |A+S| K|A| for a


subset S ⊆ Bτ, where Bτ is regular and τ (cδ)2m/dlog(2/δη). Then there is a regular Bohr set T Bτ of rank at most d +d and radius at least ρτδη1/2/d2d , where

d mε−2log2(2/δη)log(2K)+log(1/µBτ(S)), such that, for each t ∈ T,

µA ∗1L(·+t)−µA ∗1L L2m(B) ε f 1L/m2(B) +ε2−1/m f 1L/1(2Bm) +δ. In particular,

µA ∗1L ∗µT −µA ∗1L L2m(B) ε f 1L/m2(B) +ε2−1/m f 1L/1(2Bm) +δ.

##### 5 The main argument

We can now describe the main argument. As mentioned in the previous section, we shall work with a pair (B,B ) of Bohr sets, regularity ensuring that B+B ≈ B. We shall correspondingly have a pair (A,A ) of sets, with A ⊆ B and 2·A ⊆ B , each of relative density at least α. There will then be two cases:

- • If µA ∗1A L2m(B ) 10α, then we apply L2m(B )-almost-periodicity to get that µA ∗1A ∗µT L2m(B ) is large for some Bohr set T, from which a density increment is immediate.
- • If µA ∗1A L2m(B ) 10α, then the L4m(B )-almost-periodicity result is particularly efﬁcient, giving a large Bohr set B such that µA ∗1A ∗ µT,µ2·A ≈ µA ∗1A,µ2·A . Assuming that the number of 3APs across (A,A ,A) is small, say


µA ∗1A,µ2·A 14α, this tells us that the same thing is true with an extra convolution with µT, which quickly leads to a density increment.

###### Large Lp-norm of convolution implies density increment

Here we expand upon the ﬁrst case above, namely the one in which

µA ∗1A L2m(B ) 10α.

- Proposition 5.1. Let G be a ﬁnite abelian group of odd order, let B ⊆ G be a regular Bohr set, and let B 2·B be regular of rank d and radius ρ. If A ⊆ B is a set of relative density at least α with


µA ∗1A L2m(B ) 10α

for some m ∈ N, then there is a regular Bohr set T B of rank at most d + d and radius at least ραCm/d3, where d mα−1log(2/α)3, such that 1A ∗µT ∞ 5α.

Proof. Let ε = cα1/2, δ = cα and apply Theorem 4.7 with these parameters to the convolution µA ∗1A, with the Bohr set B in place of B, and τ = (cα)Cm/d chosen so that S := B τ is regular. We then have that

|A+S| |B+B τ| |B+B2τ| |B1+2τ| 2|B| α 2 |A|,

by Lemma 4.6 and regularity, allowing us to take K = 2/α. This gives us a Bohr set T B of the required rank and radius such that

µA ∗1A ∗µT −µA ∗1A L2m(B ) ε µA ∗1A 1L/m2(B ) +ε2−1/m µA ∗1A 1L/1(2Bm ) +δ. Now, we may assume that µA ∗1A L1(B ) = µA ∗1A ∗µB (0) < 5α, as otherwise we are done (with T = B ). Thus

µA ∗1A ∗µT L2m(B ) µA ∗1A L2m(B ) −ε µA ∗1A 1L/m2(B ) −ε2−1/m(5α)1/2m −δ. By nesting of Lp-norms, the right-hand side here is at least

µA ∗1A 1L/2m2(B ) µA ∗1A 1L/2m2(B ) −ε −ε2(5α/ε2)1/2m −δ

(10−c√10−c√5−c)α,

by our choice of ε and δ. Thus, provided the constants in these parameters are chosen appropriately, we are done, as µA ∗1A ∗µT L2m(B ) 1A ∗µT ∞.

| |
|---|


###### Small Lp-norm of convolution and few 3APs implies density increment

Here we expand upon how to argue in the case

µA ∗1A L2m(B ) 10α.

- Proposition 5.2. Let G be a ﬁnite abelian group of odd order, let B ⊆ G be a regular Bohr set, and let B be a regular Bohr set of rank d and radius ρ with B ⊆ Bc/rk(B). Let A ⊆ B and 2·A ⊆ B be sets of relative densities at least α. If


µA ∗1A L2m(B ) 10α for some m Clog(2/α), then either

- (i) (Many 3APs) T(A,A ,A) 4 1α|A||A |, or

- (ii) (Density increment) there is a regular Bohr set T B of rank at most d +Cmα−1log(2/α)3, and radius at least cραCm/d3, such that 1A ∗µT ∞ 2 3α.


Proof. Either we are in the ﬁrst case of the proposition, or

µA ∗1A,µ2·A 14α.

We now apply Theorem 4.7 to µA ∗1A with parameters 2m, ε = cα1/2, δ = cα, the Bohr set B in place of B, and S = B τ with τ = (cα)Cm/d, giving us a Bohr set T B τ of the required rank and radius such that

µA ∗1A ∗µT ∗µT −µA ∗1A L4m(B ) ε µA ∗1A 1L/2m2(B ) +ε2−1/2m µA ∗1A 1L/1(4Bm ) +δ.

3 2α (or else increment) as in the previous

By assumption and choice of parameters, and assuming that µA ∗1A L1(B )

argument, we thus have that

µA ∗1A ∗µT ∗µT −µA ∗1A L4m(B ) cα,

where the positive constant c may be chosen as small as we wish. Thus, letting q be such that 1/q+1/4m = 1, Hölder’s inequality yields

| µA ∗1A ∗µT ∗µT,µ2·A  − µA ∗1A,µ2·A  |

1 µB (2·A ) 12·A Lq(B ) µA ∗1A ∗µT ∗µT −µA ∗1A L4m(B ) µB (2·A )−1/4mcα cα1−1/4m.

Since m Clog(2/α), this is at most 2cα. Picking c small enough thus gives that

µA ∗1A ∗µT ∗µT,µ2·A 2 1α. There is thus some x ∈ 2·A ⊆ B ⊆ Bc/rk(B) such that

µA ∗1A ∗µT ∗µT(x) 2 1α. We are then done by the following lemma.

| |
|---|


- Lemma 5.3. Let B ⊆ G be a regular Bohr set and let A ⊆ B be a set of relative density α > 0. Let λ ∈ [0,1], and suppose T ⊆ Bτ where τ λ2/rk(B). If


µA ∗1A ∗µT ∗µT(x) (1−2λ2)α for some x ∈ Bτ, then 1A ∗µT ∞ (1+λ)α. Proof. Suppose 1A ∗ µT ∞ (1 + λ)α. Let F = (11A+∗λµ)Tα , so that 0 F 1B1+τ. In particular, we have the pointwise inequality

0 (1B1+τ −F)∗(1B1+τ −F) = F ∗F −2F ∗1B1+τ +1B1+τ ∗1B1+τ. Thus

F ∗F(x) 2F ∗1B1+τ(x)−1B1+τ ∗1B1+τ(x) (5.1) for every x. We now use regularity to estimate the right-hand side for x ∈ Bτ. Indeed,

|F∗1B1+τ(x)−F∗1B1+τ(0)| F ∞∑

|1B1+τ(y−x)−1B1+τ(y)| |B1+2τ \B| τd|B|,

y

where d := rk(B), since B is regular, and furthermore

### F∗1B1+τ(0)=∑F =|B|/(1+λ).

The second term in (5.1) can be bounded trivially: 1B1+τ ∗1B1+τ(x) |B1+τ| (1+cτd)|B|,

again by regularity. Renormalising (5.1) and picking the implied constant in the bound for τ in the hypothesis small enough, we thus have

µA ∗1A ∗µT ∗µT(x) 2(1+λ)−(1+cλ2)(1+λ)2 α, where c > 0 is as small a ﬁxed constant as we like. Picking c = 1/2, say, makes this bigger than (1−2λ2)α, as desired. Remark 5.4. There are several variants of this type of result, converting deviations to increments. Perhaps the most standard one uses Fourier analysis, which gives a slightly better λ-dependence, but this is of no relevance in our application.

| |
|---|


###### The iteration

Combining the previous two propositions immediately yields the following. Proposition 5.5. Let G be a ﬁnite abelian group of odd order, let B ⊆ G be a regular Bohr set, and let B 2·B be regular of rank d and radius ρ with B ⊆ Bc/rk(B). Let A ⊆ B and 2·A ⊆ B be sets of relative densities at least α. Then either

- (i) (Many 3APs) T(A,A ,A) 14α|A||A |, or

- (ii) (Density increment) there is a regular Bohr set T B of rank at most d +Cα−1log(2/α)4, and radius at least cραClog(2/α)/d3, such that 1A ∗µT ∞ 32α.


If not for the fact that we need to work with the two copies of the set A here, one living in a slightly narrower Bohr set than the other, we could just iterate this proposition to yield the theorem. This is where the following ‘two scales’ lemma of Bourgain’s [3] comes in: it converts a single set A in a Bohr set to two copies of roughly the original density living inside narrower Bohr sets (or else we have a density increment). The lemma is now fairly standard, but we include the proof for completeness.

- Lemma 5.6. Let B be a regular Bohr set of rank d, let A ⊆ B have relative density at least α, and let B ,B ⊆ Bcα/d. Then either


- (i) there is an x ∈ B such that 1A ∗µB (x) 34α and 1A ∗µB (x) 4 3α, or

- (ii) 1A ∗µB ∞ 98α or 1A ∗µB ∞ 98α.


Proof. Picking the constant c in the radius-narrowing small enough, regularity yields

|1A∗µB∗µB (0)−1A∗µB(0)| |B 1|Et∈B ∑

|1B(x+t)−1B(x)| 16 1 α,

x

and similarly for B . Since 1A ∗µB(0) = µB(A) = α, this implies that

Ex∈B 1A ∗µB (x)+1A ∗µB (x) (2− 18)α,

and so there exists x ∈ B such that 1A ∗µB (x)+1A ∗µB (x) (2− 81)α. With such an x, if we are not in the second case of the conclusion then

1A ∗µB (x) (2− 18)α − 98α = 34α,

and similarly for B , and so we are done. Proposition 5.7 (Main iterator). Let G be a ﬁnite abelian group of odd order, let B ⊆ G be a regular Bohr set rank d and radius ρ, and let A ⊆ B be a set of relative density at least α. Then either

| |
|---|


- (i) (Many 3APs) T(A) exp(−Cdlog(d/α))|A|2, or
- (ii) (Density increment) there is a regular Bohr set T B of rank at most d +Cα−1log(2/α)4, and radius at least cραClog(2/α)/d5, such that 1A ∗µT ∞ 8 9α.


Proof. Increasing α if necessary, we may assume that µB(A) = α. Let B(1) = Bcα/d and B(2) = B(c1/)d, with small constants c picked so that these are regular. Applying Lemma 5.6 with these sets, we are either done, obtaining a density increment with T

being B(1) or B(2), or else we ﬁnd an x such that 1A∗µB(i)(x) 34α for i = 1,2. In the latter case, we deﬁne A(i) = (A−x)∩B(i), so that µB(i)(A(i)) 4 3α, and, moreover by Lemma 4.2,

cα d2

cα d

3d

3d

|A| and |A(2)|

|A(1)|

###### |A|.

Note that by translation-invariance of three-term progressions, T(A) T A(1),A(2),A(1) ,

and if this quantity is at least 163 α|A(1)||A(2)| then we are in the ﬁrst case of the conclusion. If not, apply Proposition 5.5 with B(1) in place of B, B = 2·B(2), which is regular by Lemma 4.6, and A(1), A(2) in place of A, A , respectively. We must then be in the second case of the conclusion of that lemma, giving us the Bohr set T required in the conclusion, since

1A ∗µT ∞ 1A(1) ∗µT ∞ 32 · 43α = 98α. It is now straightforward to iterate this to prove our main theorem.

| |
|---|


- Theorem 5.8. Let G be a ﬁnite abelian group of odd order, and let A ⊆ G be a set of density at least α. Then T(A) exp −Cα−1log(1/α)C |A|2.


Proof. We deﬁne a sequence of Bohr sets B(i) of rank di and radius ρi, and corresponding subsets A(i) of relative densities αi, starting with B(0) = Bohr({1},2) = G and A(0) = A. Having deﬁned B(i) and A(i), we apply Proposition 5.7 to these sets. If

we are in the ﬁrst case of the conclusion, we exit the iteration, and if we are in the second case, say with 1A(i) ∗µT(x) 98αi, we deﬁne B(i+1) = T and A(i+1) = (A(i) −x)∩T. We thus have

i log(2/α)4, ρi+1 ρiαClog(2/α)/di5, αi+1 8 9αi.

di+1 di +Cα−1

Since the densities are increasing exponentially and can never be bigger than 1, the procedure must terminate with some set A(k) with k log(1/α). By summing the geometric progression, the ﬁnal rank satisﬁes dk α−1log(2/α)4, and the ﬁnal radius satisﬁes ρk exp −Clog(2/α)3 . Having exited the iteration, we thus have

T(A) T A(k) exp(−Cdklog(dk/α))|A(k)|2 exp −Cα−1log(2/α)7 |A|2, by Lemma 4.2, as desired.

| |
|---|


##### 6 Lp-almost-periodicity with more general measures

In this section we record some results on the Lp-almost-periodicity of convolutions, including a proof of Theorem 4.7. These results have their origins in [6], but since we require a couple of slight twists in the fundamentals of the arguments, we give an essentially self-contained treatment. Our presentation is at a somewhat greater level of generality than needed for the current application; we expect this to be useful for future applications, however, as well as being conceptually illuminating, perhaps. The ﬁrst few results are phrased in terms of an arbitrary group G, which we view as a discrete group with the discrete σ-algebra when discussing measures.3

Thus when we work with Lp norms restricted to some measure µ on G, we have

f L pp(µ) =∑

µ(x)|f(x)|p.

x

We take as our deﬁnition of convolution

f ∗g(x)=∑

f(y)g(y−1x),

y

and, for a k-tuple a = (a1,...,ak), we write µ a = Ej∈[k]1{aj}. The following moment-type estimates were essentially proved in [6].

3It is clear that everything extends naturally to locally compact groups, but we have no need for this generality here.

Lemma 6.1. Let m,k 1. Let A,L be ﬁnite subsets of a group G, let µ be a measure on G, and denote

f = µA ∗1L ·(1−µA ∗1L). If a ∈ Ak is sampled uniformly at random, then, provided k Cm/ε2,

E µ a ∗1L −µA ∗1L 2Lm2m(µ) ε2m f mLm(µ) +ε4m−2 f L1(µ). We include a proof in Appendix B in order to cater for the differences from [6].

- Deﬁnition 6.2 (Translation operator). Given a function f on a group G, and an element t ∈ G, we write τt f for the function on G deﬁned by

τt f(x) = f(tx). Similarly, if µ is a measure on G, we write τtµ for the measure given by τtµ(X) = µ(tX). Thus

Ex∼τtµ f(x) = Ex∼µ f(t−1x).

- Deﬁnition 6.3. Let ν,µ be two measures on a group G. We say that ν µ if ν(X) µ(X) for every measurable X, that is, if Eν f Eµ f

for every integrable f 0.

- Deﬁnition 6.4 (S-invariant pairs of measures). Let ν,µ be two measures on a group G, and let S ⊆ G. We say that (ν,µ) is S-invariant if τtν µ for every t ∈ S.


A prototypical example is the pair (1B1−τ,1B) for a Bohr set B, which is Bτ-invariant. Of course the pair (1G,1G) is G-invariant. (Here 1X(A) = |A∩X|.)

In the following proof, if X is a subset of a group then we write X⊗k for the kth Cartesian power of X, in order to distinguish it from the product set Xk = X ·X ···X.

- Theorem 6.5. Let m,n 1, ε ∈ (0,1). Let A,L,S be ﬁnite subsets of a group G, and suppose (ν,µ) is an (S−1S)n-invariant pair of measures on G. Suppose |S·A| K|A|. Then there is a subset T ⊆ S, |T| 0.99K−Cmn2/ε2|S|, such that, for every t ∈ (T−1T)n,


τt(µA ∗1L)−µA ∗1L L2m(ν) ε f 1L/m2(µ) +ε2−1/m f 1L/1(2µm)/n1−1/m.

The main differences between this and the results in [6] lie in the restriction of the norms and in the slight extra care to give an L1-norm rather than an L0-type estimate. Proof. Let ε0 = ε/2n. By Lemma 6.1 applied with k = Cm/ε02, we get that if a ∈ A⊗k is sampled uniformly then with probability at least 0.99,

µ a ∗1L −µA ∗1L L2m(µ) ε0 f 1L/m2(µ) +ε02−1/m f 1L/1(2µm). Let us call tuples a ∈ A⊗k satisfying this bound good, so that

P a∈A⊗k( a is good) 0.99.

Now let us write ∆(S) = {(t,...,t) ∈ S⊗k}, and let us identify elements t ∈ S with the corresponding tuple in ∆(S). Deﬁne, for each a ∈ ∆(S)·A⊗k,

T a = {t ∈ S : t−1 a is good} ⊆ S.

We now claim two things: ﬁrstly, that (T−1

a ·T a)n is a set of almost-periods for any a; secondly, that |T a| is large on average. We begin with the second claim: for each t ∈ S,

P a∈∆(S)·A⊗k(t−1 a is good) = P a∈t−1∆(S)·A⊗k( a is good)

|A|k |∆(S)·A⊗k|

P a∈A⊗k( a is good) 0.99K−k,

since ∆(S)·A⊗k ⊆ (S·A)⊗k, and so

E a∈∆(S)·A⊗k|T a|= ∑

P a∈∆(S)·A⊗k(t−1 a is good) 0.99K−k|S|. This was the second claim; we turn now to showing the ﬁrst.

t∈S

Fix any a and let T = T a, and for brevity write g = µA ∗1L. Then, by deﬁnition, for t ∈ T we have

τt(µ a ∗1L)−g L2m(µ) ε0 f 1L/m2(µ) +ε02−1/m f 1L/1(2µm). (6.1) Now let t1,...,tn ∈ T−1T. Then

τt1···tng−g L2m(ν) τt1···tng−τtng L2m(ν) + τtng−g L2m(ν) = τt1···tn−1g−g L2m(τt−1

ν) + τtng−g L2m(ν). Carrying on in this way, we have

n

τt1···tng−g L2m(ν) τt1g−g L2m(τr1ν) +···+ τtng−g L2m(τrnν), (6.2) where rj ∈ (T−1T)n−j. Consider one of the summands here, with r = rj and t = tj = s−1

1 s2 for some elements si ∈ T. We have

1 s2g−τs2(µ a ∗1L) L2m(τrν) + τs2(µ a ∗1L)−g L2m(τrν). The ﬁrst term here equals

τtg−g L2m(τrν) τs−1

g−τs1(µ a ∗1L) L2m(τrs−1

ν), and so, since T ⊆ S and (ν,µ) is (S−1S)n-invariant, both of these terms can be bounded as in (6.1). Thus τt1···tng−g L2m(ν) 2n ε0 f 1L/m2(µ) +ε02−1/m f 1L/1(2µm) ,

2 s1

which proves the claim that the set (T−1T)n is a set of almost-periods for µA ∗1L. Letting a be some tuple for which T = T a has size at least 0.99K−k|S| yields the theorem. We now bootstrap this in a standard way using Fourier analysis, making use of the following local version of Chang’s

| |
|---|


lemma on large spectra due to Sanders [12]. Lemma 6.6 (Chang–Sanders). Let δ,ν ∈ (0,1]. Let G be a ﬁnite abelian group, let B = Bohr(Γ,ρ) ⊆ G be a regular Bohr set of rank d and let X ⊆ B. Then there is a set of characters Λ ⊆ G and a radius ρ with

|Λ| δ−2log(2/µB(X)) and ρ ρνδ2/d2log(2/µB(X)) such that

|1−γ(t)| ν for all γ ∈ Specδ(µX) and t ∈ Bohr(Γ∪Λ,ρ ).

Theorem 6.7 (Lp-almost-periodicity relative to Bohr-compatible measures). Let m 1 and ε,δ ∈ (0,1). Let A,L be subsets of a ﬁnite abelian group G with η := |A|/|L| 1, let B ⊆ G be a regular Bohr set of rank d and radius ρ, and let (ν,µ) be an rB-invariant pair of measures on G, where r Clog(2/δη). Suppose |A+S| K|A| for a subset S ⊆ B. Then there is a regular Bohr set B B of rank at most d +d and radius at least ρδη1/2/d2d , where

d mε−2log2(2/δη)log(2K)+log(1/µB(S)), such that, for each t ∈ B ,

µA ∗1L(·+t)−µA ∗1L L2m(ν) ε f 1L/m2(µ) +ε2−1/m f 1L/1(2µm) +δ ν 1 1/2m.

Proof. We could deduce a version of this from Theorem 6.5 as stated, working with an intermediate measure ν2 for which (ν,ν2) and (ν2,µ) are invariant, but for a cleaner statement we instead argue directly, picking up where the proof of that theorem left off. Indeed, say we have followed that argument with parameters m, n = (r−1)/2 and ε/2, thus obtaining a set T ⊆ S with

µB(T) 0.99K−Cmr2/ε2µB(S) such that, for each s ∈ nT −nT,

τsg−g L2m(ν) ε := 12ε f 1L/m2(µ) + 12ε2−1/m f 1L/1(2µm),

where again g = µA ∗1L. Let us then write σ = µT(n) ∗µ−(nT), where µX(n) represents the n-fold convolution µX ∗···∗µX. By the triangle inequality, we then have

g∗σ −g L2m(ν) Etj∈T τsg−g L2m(ν) ε ,

where we have written s = t1+···+tn−tn+1−···−t2n in the expectation. We also want this estimate to hold for any translate τtν of ν with t ∈ B, which follows from (ν,µ) being (2n+1)B-invariant: for any t1,...,tn ∈ T −T and t ∈ B, the bound (6.2) holds with ν replaced by τ−t(ν), and the ﬁnal measures appearing thereafter in the proof are still dominated by µ, by (2n+1)B-invariance, meaning that also

τt(g∗σ)−τtg L2m(ν) ε holds for all t ∈ B.

Now we carry out the Fourier-bootstrapping in a standard way. By the triangle inequality, we have that, for any t ∈ B, τtg−g L2m(ν) τtg−τt(g∗σ) L2m(ν) + τt(g∗σ)−g∗σ L2m(ν) + g∗σ −g L2m(ν), which, by the above, is at most

2ε + τt(g∗σ)−g∗σ L2m(ν). The last term here is at most

ν 1 1/2m τt(g∗σ)−g∗σ L∞(G),

and it is in bounding this that we shall need to pick t carefully. Indeed, apply Lemma 6.6 to T ⊆ B with parameter δ = 1/2 to get a regular Bohr set B B of rank at most d +d and radius at least ρδη1/2/d2d , where

d log(2/µB(T)) mn2ε−2log(2K)+log(1/µB(S)) such that

|1−γ(t)| δη1/2 for all γ ∈ Spec1/2(µT) and t ∈ B .

Taking t ∈ B , then, we have by the Fourier inversion formula that

τt(g∗σ)−g∗σ L∞ Eγ∈ G| µA(γ)|| 1L(γ)|| µT(γ)|2n|γ(t)−1|, (6.3)

and we bound the terms in this average according to whether γ ∈ Spec1/2(µT) or not. If γ ∈ Spec1/2(µT) then |γ(t)−1| δη1/2, and if not then | µT(γ)|2n 1/4n δη1/2/2, provided we pick n = 2 logδ−1η−1 . Thus (6.3) is at most twice

δ Eγ∈ G| µA(γ)|| 1L(γ)|, which, by Cauchy-Schwarz and Parseval’s identity, is at most

δη1/2Eγ∈ G| µA(γ)|| 1L(γ)| δη1/2 Eγ∈ G| µA(γ)|2

1/2

Eγ∈ G| 1L(γ)|2

1/2

###### = δ,

recalling that η = |A|/|L|. Putting all these estimates together and replacing δ by δ/2, we are done.

| |
|---|


The main almost-periodicity theorem used in this paper, Theorem 4.7, is a simple corollary of this, using the regularity of Bohr sets through the following lemma. Using regularity at this point is somewhat inefﬁcient quantitatively, adding an extra loglog to our ﬁnal bound for Roth’s theorem, but it allows for simpler statements.

Lemma 6.8. Let B be a regular Bohr set of rank d, let δ ∈ [0,1], and suppose τ cδ p/d. Then, for any F : G → C and p 1,

F p(B) F p(B1−τ) +δ F ∞(B)|B|1/p. Proof. By the triangle inequality

1−τ) F p ∞(B)|B\B1−τ|. It follows from regularity that |B\B1−τ| τd|B|, and so the result follows if we choose c small enough.

F p p(B) − F p p(B

| |
|---|


It is now a short matter to deduce Theorem 4.7, the almost-periodicity result with all the Lp-norms being relative to the same Bohr set.

Proof of Theorem 4.7. Let r = Clog(2/δη) and apply Theorem 6.7 to A and L with parameters m, ε, δ/2, the Bohr set Bτ in place of B and the rBτ-invariant pair of measures ν = 1B1−rτ, µ = 1B. This gives a Bohr set T Bτ of the required rank and radius such that, for each t ∈ T,

µA ∗1L(·+t)−µA ∗1L 2m(B1−rτ) ε f 1 m/2(B) +ε2−1/m f 1 1/(2Bm) + 21δ|B|1/2m.

Since τ c(δ/2)2m/dr, the main claim follows from Lemma 6.8. The ‘in particular’ then follows by averaging and the triangle inequality.

| |
|---|


##### 7 Concluding remarks

In some sense, it should not be altogether surprising that the almost-periodicity arguments of [6] can be used to prove logarithmic bounds for Roth’s theorem, as these results were used to reach this barrier in several other related problems, already in [6] but also in [5]. Being able to do this rests on using the more elaborate moment-bounds present in [6] (or in this paper) for the random sampling, rather than the more usual Khintchine-type bounds.

###### The number of loglogs

C

The argument presented in this paper gives a bound of r3(N)/N (loglogN)

logN with C = 7. One of these loglogs is caused by applying Bohr-set regularity to an Lp norm with p large, which makes for clean statements but is otherwise quite wasteful. Circumventing this and taking into account some further optimisations allows one to reduce this C, but not to below 4, which is the best bound currently known [2].

##### A Almost-periodicity results

The following result is [6, Corollary 1.4]

Theorem A.1. Let p 2 and ε ∈ (0,1) be parameters. Let G be a ﬁnite abelian group and let A,L ⊆ G be ﬁnite subsets with |A| α|G|. Then there is a set T ⊆ S with |T| (α/2)O(pε−2)|G| such that

µA ∗1L(·+t)−µA ∗1L p ε µA ∗1L 1p//22 +ε2 for each t ∈ T −T.

For completeness we include the following short deduction of the almost-periodicity result used in the ﬁnite ﬁeld argument.

Proof of Theorem 3.2. Let k 1 be some parameter to be chosen later, and let T be the set of almost-periods provided by Theorem A.1. It follows that

µA ∗1L ∗µ −µA ∗1L p kε µA ∗1L 1p//22 +kε2,

where µ := µT(k−)T is the k-fold convolution µT−T ∗···∗µT−T. Thus, for any t ∈ Fnq,

µA ∗1L(·+t)−µA ∗1L p 2kε µA ∗1L 1p//22 +2kε2

+ µA ∗1L ∗µ(·+t)−µA ∗1B ∗µ p.

This last term is bounded above by

Eγ∈ G| µA(γ)|| 1L(γ)|| µT−T(γ)|k|γ(t)−1|,

and so if t ∈ V := Specη(µT−T)⊥ := {γ ∈ G : | µT−T(γ)| η}⊥ then this is at most

2ηk|A|−1/2|L|1/2 2ηkK1/2.

If we choose η = 1/2, say, and k ≈ Clog(2K/ε), then this implies that for t ∈ V,

µA ∗1L(·+t)−µA ∗1L p 2kε µA ∗1L 1p//22 +4kε2.

The proof is complete since dimSpec1/2(µT−T) log(1/µ(T)) by Chang’s theorem.

##### B Central moments of the binomial distribution

Here we prove Lemma 6.1, a version of the sampling lemma at the heart of the probabilistic approach to almost-periodicity. As mentioned before, it is a variant of results from [6].

- Lemma B.1. Let m,k 1. Let A,L be ﬁnite measure subsets of a σ-ﬁnite locally compact group G, let µ be a σ-ﬁnite Borel measure on G, and denote

f = µA ∗1L ·(1−µA ∗1L). If a ∈ Ak is sampled uniformly at random, then, provided k Cm/ε2,

E µ a ∗1L −µA ∗1L 2Lm2m(µ) ε2m f mLm(µ) +ε4m−2 f L1(µ).

Note that the measures of A and L, the σ-ﬁniteness, and the convolutions are with respect to (left) Haar measure µG on G. Thus

f ∗g(x) = f(y)g(y−1x)dµG(y). The function µ a ∗1L is to be interpreted as

µ a ∗1L(x) = Ej∈[k]1L(a−1

j x).

We remark that although introducing the function f might seem cumbersome, it turns out to be somewhat natural. Note for example that if A = L is a subgroup, the right-hand side is actually 0, since then µA ∗1A = 1A.

To prove this lemma, we shall use the following bounds for the central moments of the binomial distribution. These are surely standard, but we include a self-contained proof as we have not been able to locate a readily available reference. (We note that they follow from general results on iid random variables, but only after some calculation.)

- Lemma B.2. Let p ∈ [0,1] and m,n ∈ N. If X is a Bin(n, p) random variable, with q = 1− p, then E|X −np|2m mmax(m2m−1npq,em−1(mnpq)m).


In particular, if Z = X/n and n 4m/δ, we have

E|Z − p|2m δm(pq)m +δ2m−1pq.

The particular constants here could be improved, but are of no consequence to us. Before proving this, let us see how it implies Lemma B.1.

- Proof of Lemma B.1. Fix x ∈ G. For a = (a1,...,ak) sampled uniformly from Ak, we have


µ a ∗1L(x) = Ej∈[k]1L(a−1

j x). This is an average of k Bernoulli random variables 1L(a−1

j x), each with parameter p = E1L(a−1

j x) = µA ∗1L(x).

The sum of these k Bernoulli random variables is a binomial random variable, and so Lemma B.2 (with n = k) implies that E|µ a ∗1L(x)−µA ∗1L(x)|2m ε2m f(x)m +ε2m−1 f(x).

Integrating over all x ∈ G with respect to µ and swapping orders of integration using Fubini–Tonelli yields the result.

To prove the above moment bounds, we use a few standard facts about a binomially distributed random variable X ∼ Bin(n, p). Throughout, let

n

n j

#### ∑

µr = E(X −np)r =

pjqn−j(j−np)r.

j=0

The moment generating function of X −np is

∞

µktk k!

= qe−tp + petq n.

#### ∑

k=0

We note that µr 0 provided p 1/2. Furthermore, formal manipulation of the above power series yields, as noted in [8, §5.5], the recurrence

r−2

r−2

r−1 j

r−1 j

#### ∑

#### ∑

µr = npq

µj − p

µj+1 (B.1)

j=0

j=0

for r 2, which, together with the initial conditions µ0 = 1, µ1 = 0 can be used to compute these moments. We use it to bound the moments as follows.

- Proposition B.3 (Polynomial bound for central moments). For p 1/2, the r-th central moment of a Bin(n, p) random variable satisﬁes

µr νr(npq), where νr(x) is a polynomial deﬁned recursively by ν0 = 1, ν1 = 0 and

νr = x

r−2

∑

j=0

r−1 j

νj.

Proof. For p 1/2, all the moments are non-negative, and so (B.1) yields

µr npq

r−2

∑

j=0

r−1 j

µj.

The claim thus follows by induction.

| |
|---|


The polynomials νr so deﬁned give the best upper bound possible for µr that is a polynomial in npq and otherwise uniform in p. We can describe them fairly explicitly:

- Proposition B.4 (Explicit description of the polynomials νr). For r 0,


νr = ∑

S2(r,k)xk

k 0

where S2(r,k) is a 2-associated Stirling number of the second kind, deﬁned as the number of partitions of a set of size r into k parts, each of size at least 2. In particular, νr has degree r/2 and, if r 1, no constant term.

For clarity surrounding edge cases, we take S2(0,0) = 1 and S2(r,0) = 0 = S2(0,k) for r,k 1. To prove the proposition, we note the following recurrence for S2(r,k).

Lemma B.5. For r 0 and k 1,

r−2

#### ∑

S2(r,k) =

j=0

r−1 j

S2(j,k−1).

Proof. For r 1 the result is trivial, so assume r 2. We consider the partitions of [r] into k parts, each of size 2. We count these according to how many elements 1 is placed with. If the part containing 1 is to have size n+1, there are r−n1 choices for the other elements to place with 1, and S2(r−1−n,k−1) ways to partition the remaining elements into k−1 parts, each of size at least 2. Summing up all these (disjoint) ways yields the result.

| |
|---|


Proof of Proposition B.4. The recursion in Lemma B.5 shows immediately that the sequence pr = ∑k 0S2(r,k)xk satisﬁes the recursion deﬁning νr. Since the initial conditions also match, the sequences are the same.

| |
|---|


We next use this combinatorial description to place an upper bound on νr. Proposition B.6 (Upper bound for νr). For x 0,

ν2m mmax em−1(mx)m,m2m−1x . Proof. By Proposition B.4,

m

#### ∑

S2(2m,k)xk.

ν2m =

k=1

Using the crude bounds

S2(2m,k) k2m/k! ek−1k2m−k e−1m2m(e/m)k, valid for 1 k m, we have

ν2m e−1m2m

m

#### ∑

(xe/m)k e−1m2m+1max(xe/m,(xe/m)m).

k=1

Rearranging, this completes the proof.

| |
|---|


One could of course be more careful here in order to obtain better constants, but we have no need for it, opting instead for uniform bounds.

- Proof of Lemma B.2. The ﬁrst claim follows immediately from combining Proposition B.3 and Proposition B.6. The second one follows from the ﬁrst upon replacing the maximum by a sum.


| |
|---|


##### Acknowledgements

The ﬁrst-named author was supported by both the Heilbronn Institute for Mathematical Research, Bristol, UK, and a postdoctoral grant funded by the Royal Society while this work was completed. The second-named author was supported by The Swedish Research Council grant 2013-4896. The authors would like to thank the Harvard CMSA for its hospitality during its Combinatorics and Complexity programme, where part of this work was carried out.

##### References

- [1] Bateman, M. and N. H. Katz “New bounds on cap sets” J. Amer. Math. Soc. 25 (2012): 585–613. 2
- [2] Bloom, T. F. “A quantitative improvement for Roth’s theorem on arithmetic progressions” J. Lond. Math. Soc. (2) 93

(2016): 643–663. 1, 16

- [3] Bourgain, J. “On triples in arithmetic progression” Geom. Funct. Anal. 9 (1999): 968–984. 1, 5, 10
- [4] Bourgain, J. “Roth’s theorem on progressions revisited” J. Anal. Math. 104 (2008): 155–192. 1
- [5] Croot, E., Łaba, I. and O. Sisask “Arithmetic progressions in sumsets and Lp-almost-periodicity” Combin. Probab. Comput. 22 (2013): 351–365. 6, 15
- [6] Croot, E. and O. Sisask “A probabilistic technique for ﬁnding almost-periods of convolutions” Geom. Funct. Anal. 20

(2010): 1367–1396. 2, 4, 6, 11, 12, 15, 16, 17

- [7] Heath-Brown, D. R. “Integer sets containing no arithmetic progressions” J. London Math. Soc. 35 (1987): 385–394. 1
- [8] Kendall, M. G. “The advanced theory of statistics” volume 1, second edition, 1945. 18
- [9] Roth, K. F. “On certain sets of integers” J. London Math. Soc. 28 (1953): 104–109. 1, 3
- [10] Sanders, T. “On Roth’s theorem on progressions” Ann. of Math. 174 (2011): 619–636. 1, 2
- [11] Sanders, T. “On certain other sets of integers” J. Anal. Math. 116 (2012): 53–82. 1
- [12] Sanders, T. “Additive structures in sumsets” Math. Proc. Cambridge Philos. Soc. 144 (2008): 289–316.13
- [13] Schoen, T. and O. Sisask “Roth’s theorem for four variables and additive structures in sums of sparse sets” Forum Math. Sigma 4 (2016): e5 (28 pages). 6
- [14] Szemerédi, E. “Integer sets containing no arithmetic progressions” Acta Math. Hungar. 56 (1990): 155–158. 1
- [15] Tao, T., and V. Vu. Additive Combinatorics, 1st ed. Cambridge University Press, 2006. 5


###### AUTHORS

Thomas F. Bloom Department of Pure Mathematics and Mathematical Statistics University of Cambridge Cambridge, UK tb634@cam.ac.uk

Olof Sisask Department of Mathematics Uppsala University Sweden olof.sisask@math.uu.se

