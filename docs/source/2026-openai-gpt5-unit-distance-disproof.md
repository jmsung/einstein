---
type: source
kind: paper
title: OpenAI gpt-5 disproves a discrete-geometry conjecture (unit-distance bound)
authors: OpenAI
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: openai-release
source_url: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
source_local: ../raw/2026-openai-gpt5-unit-distance-disproof.pdf
topic: agentic-harness
cites:
---

# Planar Point Sets with Many Unit Distances

OpenAI

Abstract

For a ﬁnite planar set P, let ν(P) be the number of unordered unit-distance pairs in P, and let ν(n) be the maximum of ν(P) over all n-point planar sets. We prove that, for some ﬁxed δ > 0, one has ν(n) ≥ n1+δ for inﬁnitely many n. This disproves the well-known unit distance conjecture from [Erd46].

The construction passes through an inﬁnite unramiﬁed tower of totally real number ﬁelds with 3-power Galois groups of growing degree, in which a ﬁxed set of rational primes splits completely. After adjoining i, these ﬁelds produce high-dimensional lattices with many elements whose images under every complex embedding have absolute value 1. Golod–Shafarevich theory ensures existence of an inﬁnite such tower, even after a quotient step making the prescribed Frobenius classes trivial. A crucial property of the construction is that all resulting discriminants and class numbers are at most exponential in the extension degree.

## 1 Main Result

For a ﬁnite set P ⊂ R2, let ν(P) = #{{x,y} ⊂ P : |x−y| = 1} and ν(n) = max|P|=n ν(P). The planar unit-distance problem goes back to Erdős [Erd46], who conjectured that there should be an absolute constant C such that, for all suﬃciently large n,

ν(n) ≤ n1+C/log logn. (1)

The same 1946 paper also introduced the distinct-distances problem, later resolved up to logarithmic factors by Guth–Katz [GK15]. An elementary upper bound is ν(n) = O(n3/2): the Euclidean unit-distance graph is K2,3-free, since two unit circles meet in at most two points, and the Kővári–Sós–Turán theorem applies [KST54]. The best known upper bound ν(n) = O(n4/3) is due to Spencer–Szemerédi–Trotter [SST84]; Székely later gave a short crossing-number proof of this incidence bound [Sze97].

It is useful to compare this with the same question for other norms on R2, a direction studied systematically by Brass [Bra96]. If the unit ball has a ﬂat segment, one can arrange quadratically many unit distances, so the interesting normed-plane analogues usually impose strict convexity or genericity. Székely’s crossing-number argument extends to strictly convex norms, again giving O(n4/3), and Valtr constructed a strictly convex norm for which this exponent is attained [Sze97, Val05]. Related work of Eisenbrand–Pach–Rothvoß–Sopher on convexly independent subsets of Minkowski sums gave the corresponding O(m2/3n2/3 + m + n) upper bound, with later matching lower bounds by Bílka–Buchin–Fulek–Kiyomi–Okamoto–Tanigawa– Tóth [EPRS08, BBF+10]; Brass–Moser–Pach give a broader survey [BMP05]. For Baire-generic norms the behavior is now known much more sharply. Matoušek proved O(nlog nlog log n) for

most planar norms [Mat11]. For each ﬁxed d ≥ 2, Alon–Bucić–Sauermann proved that a comeagre set of norms on Rd has at most d2nlog2 n unit distances on every n-point set [ABS25]. A matching lower bound (d2 − o(1))nlog2 n was then shown by Greilhuber–Schildkraut–Tidor to hold for all norms on Rd [GST25]. These results provided evidence in favor of Erdős’s conjecture, which was widely believed to be true prior to our work. However we disprove the unit distance conjecture; our main theorem is as follows.

- Theorem 1.1. There exists an absolute constant δ > 0 and inﬁnitely many positive integers n for which ν(n) ≥ n1+δ.


We note that a similar, stronger conjecture posed in [EF97] concerns point sets P ⊂ R2 such that every point x ∈ P has at least k equidistant neighbors in P, at a distance dx that may depend on x. Theorem 1.1 also refutes the predicted bound k ≤ no(1): along our sequence the unit-distance graph has average degree nΩ(1), and a graph of average degree at least 2k contains a subgraph of minimum degree at least k.

The construction can be viewed as a high-dimensional analogue of the arithmetic behind Erdős’s classical square-grid lower bound. In the Gaussian integers Z[i], a product of many rational primes q ≡ 1 (mod 4) has many representations of the form zz¯. Geometrically, these representations give many lattice vectors of the same length. Our construction replaces Q(i) by K = L(i), where L is a totally real ﬁeld whose degree tends to inﬁnity. The nontrivial automorphism c of K/L plays the role of complex conjugation: under every complex embedding of K, c becomes ordinary complex conjugation.

The proof separates into an arithmetic part and a geometric part. The arithmetic part builds ﬁelds L in which a ﬁxed set of rational primes splits completely. These split primes give many ideal factorizations in K = L(i); after a class-group pigeonhole, they produce many elements u ∈ K× with uc(u) = 1. Under every complex embedding these elements have absolute value

- 1, so they become candidate unit translations. The class-group loss is harmless because the


ﬁelds have bounded root discriminant rd(F) = |DF|1/[F:Q]. Minkowski’s theorem then gives class numbers at most exponential in the ﬁeld degree.

The bounded root discriminants are obtained at the same time as the prescribed splitting. We use an unramiﬁed pro-3 tower over a cyclic cubic ﬁeld. Chebotarev supplies rational primes whose Frobenius classes can be made trivial in every later layer. Shafarevich’s relation-rank estimate and Golod–Shafarevich theory keep the resulting quotient tower inﬁnite. This is the Hajir–Maire class-ﬁeld-tower method, in an unramiﬁed pro-3 setting; see Remark 3.1.

Section 2 proves the geometric criterion: given suitable number ﬁelds and split primes, it constructs the planar point sets by embedding norm-one elements into a high-dimensional Minkowski lattice, cutting by a product of discs, and projecting to one complex coordinate. Section 3 then constructs the required ﬁelds using the unramiﬁed pro-3 tower. Appendix A collects the numberﬁeld conventions and citations used below.

### Statement on AI Use

This problem was solved in a completely automated fashion. Our internal model was given an AI-written statement of the problem, and its output was sent to an AI grading pipeline, which indicated high conﬁdence that the solution was correct. It was only after this point that in-

ternal human researchers and mathematicians began to examine the solution carefully. After preliminary AI-assisted veriﬁcation and rewriting, a draft was sent to external mathematicians, including several number theory experts, who conﬁrmed the proof’s correctness (and have already simpliﬁed and strengthened the argument). The present manuscript is a human-edited exposition of the autonomously produced solution, with references, reorganized proofs, and additional explanatory material added afterward.

The original AI-written prompt given to the internal model was:

Prompt. Let P ⊂ R2 be a ﬁnite set of distinct points. Deﬁne

P 2

: p − q 2 = 1

ν(P) = {p,q} ∈

and, for each integer n ≥ 1, ν(n) = maxP⊂R2 |P|=n

ν(P).

Resolve Erdős’s planar unit-distance problem completely: ν(n) ≤ n1+O(1/log logn) as n → ∞? Equivalently, determine whether there exist absolute constants C > 0 and N ∈ N such that ν(n) ≤ n1+C/log logn for every integer n ≥ N. Here log denotes the natural logarithm, and N may be taken large enough that log log n > 0. The hidden constant in O(1/log log n) is absolute and independent of P and n.

A complete solution must prove exactly one of the following. Aﬃrmative resolution. Prove that there exist absolute constants C > 0 and N ∈ N such that every set P ⊂ R2 of n ≥ N distinct points satisﬁes ν(P) ≤ n1+C/log logn.

Negative resolution. Prove that no such constants exist. Equivalently, prove that for every C > 0 and every N ∈ N, there are an integer n ≥ N and a set P ⊂ R2 of n distinct points such that ν(P) > n1+C/log logn.

Pairs are unordered, the distance is the usual Euclidean distance in R2, and the asymptotic assertion is for all suﬃciently large integers n, not merely inﬁnitely many n.

Partial progress does not count unless it implies one of the two resolutions above. In particular, improved bounds such as O(n4/3−ε), better constants in the n4/3 bound, ﬁnite veriﬁcation, special cases, structural reductions, or heuristic evidence are insuﬃcient unless they prove the full Erdős bound or disprove it.

We emphasize that the ﬁnal paragraph of the prompt does not reﬂect the mathematical value of partial progress. Certainly any bound O(n4/3−ε) would be a major advance over the estimate from Spencer–Szemerédi–Trotter [SST84], which has stood since 1984 with only constant-factor improvements [ÁP22].

Below we also reproduce verbatim the original solution output by the internal model, before any automated grading or rewriting was performed.

Final Response from Internal Model.

I will use a standard form of the Golod-Shafarevich argument with prescribed splitting. I write rd(L) = |DL|1/[L:Q]. For a ﬁnitely generated pro-p group G, let d(G) and r(G) denote the minimal numbers of generators and relations and let Φ(G) be its Frattini subgroup. I shall use the following two standard facts. First, if (g1,...,gk ∈ Φ(G)), then the quotient of G by the closed normal subgroup generated by the gi has the same generator rank and

relation rank at most r(G)+k. Second, a ﬁnite pro-p group with d generators and r relations satisﬁes r > d2/4. I use p = 3 in the tower construction (this avoids all dyadic inﬁnite-prime issues). Let be large. Choose distinct primes r1,...,r ≡ 1 (mod 3) among the ﬁrst such primes, and let Li be the cyclic cubic subﬁeld of Q(ζr

). Put D = i ri and M = L1 ···L . Thus Gal(M/Q) (Z/3Z) . If χi is a cubic character of conductor ri, let F be the cyclic cubic subﬁeld corresponding to the character χ1 ···χ . By the conductor-discriminant formula, |DF| = D2. Indeed the two non-trivial characters of F both have conductor D. Similarly, every character of M is of the form i χa

i

i , ai ∈ 0,1,2, and its conductor is the product of those ri with ai = 0. Hence each ri occurs in 2 · 3 −1 of the non-trivial characters, so

i

−1

= |DF|[M:F].

|DM| = D2·3

Thus M/F is everywhere unramiﬁed. All these ﬁelds are totally real. Consequently, if G is the Galois group of the maximal unramiﬁed pro-3 extension of F, then

d(G) ≥ − 1. (1)

(We have the elementary abelian unramiﬁed extension M/F.) Since F is a totally real cubic ﬁeld and does not contain ζ3, Shafarevich’s relation-rank estimate for the unramiﬁed pro-3 group gives

r(G) ≤ d(G) + C0 (2)

with an absolute constant C0 (any linear bound with an absolute constant would suﬃce here). Also

- 2

- 3


log rd(F) =

log D = O( log ). (3)

Let E/F be the ﬁnite elementary abelian extension corresponding to G/Φ(G). Put d = d(G) and

d2 100

t =

.

By Chebotarev, choose distinct rational primes q1,...,qt, avoiding 3D, which split completely in the normal closure over Q of E(i). Then each qb ≡ 1 (mod 4), each qb splits completely in F, and for every prime v of F above qb the Frobenius element in G lies in Φ(G). There are 3t such primes v. Quotient G by the closed normal subgroups generated by these Frobenius elements. By the group-theoretic observation above, the quotient has generator rank d and at most r(G) + 3t relations; for large, (2) gives r(G) + 3t < d2/4. Hence this quotient is inﬁnite. In it the decomposition groups at all primes above the qb’s are trivial (the extensions are unramiﬁed), so the qb’s split completely. Taking a descending chain of open normal subgroups gives an inﬁnite tower

F = F0 ⊂ F1 ⊂ F2 ⊂ ···

of ﬁnite unramiﬁed extensions in which every qb splits completely. Since the extensions have 3-power Galois groups, all ﬁelds in the tower are totally real. Write fj = [Fj : Q]; then fj → ∞ and rd(Fj) = rd(F). Now set Kj = Fj(i), with complex conjugation c. The relative discriminant of adjoining i divides (4), so

rd(Kj) ≤ 2, rd(F) =: A . (4) We shall use the elementary bound: if [L : Q] = n and rd(L) ≤ A, then

h(L) ≤ C(A)n, log C(A) = O(log A + log log(3A)). (5) Indeed, Minkowski gives an integral ideal of norm X ≤ (C

√

A)n in every ideal class. The number of ideals of norm m is at most the n-fold divisor function dn(m), and

dn(m) ≤ CnX(1 + log X)n−1/(n − 1)!,

m≤X

which is exponential in n when log X = OA(n). From (4),(5) we get h(Kj) ≤ Hfj , log H = O( log ). (6)

Let Q = tb=1 qb. For ﬁxed j, each qb has fj degree-one primes in Fj, and each of these splits in Kj into a conjugate pair Ps,cPs. Thus there are m = tfj such pairs. For = ( s) ∈ 0,1m put

A =

cPs.

###### Ps

s=1

s=0

At least 2m/h(Kj) of these ideals lie in the same ideal class. Fix one element η in such a ﬁbre. For every in the ﬁbre choose α ∈ Kj∗ with

(α ) = A A−η 1, and deﬁne

u = α /c(α ).

For every complex embedding σ of Kj, σ(cα) = σ(α), hence |σ(u )| = 1. The ﬁnite valuations of u are supported above Q and are in −2,0,2, so Q2u ∈ OKj. At the prime Ps the valuation is 2( s − ηs), so the u ’s are distinct. By (6), for large,

2tfj

h(Kj) ≥ exp(γfj), γ := tlog 2 − log H > 0, (7) where Uj denotes this set of elements. Embed Kj in Vj = Cf

|Uj| ≥

j by choosing one embedding from each conjugate pair, and let Λj = Q−2OKj

in this Minkowski embedding. Then Uj ⊂ Λj, and every coordinate of every u ∈ Uj has modulus 1. Fix R > 1/2. Let W ⊂ Vj be the product of the discs |z| ≤ R. Write b = πR2, and let a = a(R) be the area of overlap of two radius-R discs whose centres are distance 1; put ρR = a/b, so ρR → 1 as R → ∞. For a coset y + Λj, set Xy = (y+Λj)∩W, and let Dy be the number of directed pairs (x,x+u) with x,x+u ∈ Xy and u ∈ Uj. Averaging over the torus Vj/Λj gives

, EDy = |Uj|af

bf

j

j

E|Xy| =

.

covol(Λj)

covol(Λj)

Hence some coset satisﬁes Dy ≥ |Uj|ρfRj|Xy|. Choose R so large that log ρR > −γ/2. For this coset, writing X = Xy, (7) yields

j/2|X|. (8)

Dy ≥ eγf

Project X to the ﬁrst complex coordinate. This projection is injective on a coset of Λj: if two points have the same ﬁrst coordinate, their diﬀerence is an element of Kj with one conjugate equal to zero, hence is zero. Let Pj ⊂ C R2 be the projected set and nj = |Pj| = |X|. Each directed pair counted in (8) projects to a unit segment, since the ﬁrst coordinate of u has modulus 1. For ﬁxed ordered endpoints the diﬀerence (hence u) is unique, so an unordered segment is counted at most twice. Therefore

- 1

- 2


j/2,nj. (9)

ν(Pj) ≥

eγf

Finally, if 0 = λ ∈ Λj, then β = Q2λ is a nonzero algebraic integer, and for the chosen embeddings

fj

≥ Q−2f

j/Q(β)|1/2Q−2f

|σr(λ)| = |NK

.

j

j

r=1

Thus some coordinate of λ has modulus at least Q−2. A packing argument in the polydisc W gives

nj ≤ (CRQ2)2fj = eBf

j (10) with B independent of j. Also (8) and Dy ≤ n2j imply nj ≥ eγf

j/2, so nj → ∞. Combining

(9) and (10), and absorbing the factor 1/2 for large j, we obtain

γ 4B

ν(Pj) ≥ n1+j δ, δ =

> 0. (11)

Given arbitrary C0 > 0 and N, choose j so large that nj ≥ N and C0/log log nj < δ. Then

ν(nj) ≥ ν(Pj) > nj1+C0/log lognj. Thus no universal constants C,N can satisfy the proposed upper bound.

The remainder of the paper explains the above proof in more detail.

## 2 Planar Point Sets from Number Fields

Assuming the existence of the admissible ﬁelds deﬁned below, we construct planar point sets with many unit distances. Section 3 supplies the ﬁelds.

Deﬁnition 2.1. An admissible datum consists of:

- • a totally real number ﬁeld L of degree f = [L : Q];
- • the CM ﬁeld K = L(i), with nontrivial automorphism c over L (see Deﬁnition A.4);
- • a positive integer t, the number of selected rational primes;
- • distinct rational primes q1,...,qt, each congruent to 1 (mod 4) and splitting completely in L (see Deﬁnition A.2 for the deﬁnition of splitting).


Put Q = tb=1 qb. In the geometric part we also write D = Q2 for the corresponding ﬁxed denominator.

Each qb gives many conjugate prime-ideal pairs in K = L(i). Since qb splits completely in L, it gives f prime ideals q of L, each with residue ﬁeld OL/q =∼ Fqb. Since qb ≡ 1 (mod 4), the polynomial x2 + 1 splits over this residue ﬁeld, so each q splits in K. Hence the ﬁxed rational primes give m = tf conjugate pairs of prime ideals of K:

{Ps,cPs}, s = 1,...,m. (2)

- Proposition 2.2. Let L,K,t,q1,...,qt,Q be an admissible datum in the sense of Deﬁnition 2.1. Suppose h(K) ≤ Hf for some real H > 0. Then there is a set U ⊂ Q−2OK such that every


u ∈ U satisﬁes NK/L(u) = 1, where, for K = L(i), the relative norm is NK/L(u) = uc(u). Every u ∈ U also satisﬁes |σ(u)| = 1 for every complex embedding σ : K → C. Moreover, |U| ≥ exp{(tlog 2 − log H)f}.

Proof. For each binary vector ε = (εs) ∈ {0,1}m, choose one prime from each conjugate pair in

- (2) and set


Aε =

cPs.

#### Ps

εs=1

εs=0

These 2m ideals need not be principal, but they occupy only h(K) ideal classes. Thus some ﬁber of ε  → [Aε] ∈ Cl(K) has size at least 2m/h(K). Fix one vector η in such a ﬁber; for every ε in the same ﬁber, AεA−η 1 is principal, so choose αε ∈ K× with (αε) = AεA−η 1, and set uε = αε/c(αε). Then uεc(uε) = 1, so NK/L(uε) = 1. Since L is totally real, c becomes ordinary complex conjugation under every complex embedding of K. Therefore

|σ(uε)| =

σ(αε) σ(αε)

= 1. (3)

Let U be the set of all uε’s obtained from this ﬁber. The principal ideal of uε is

AεAη−1 c(AεA−η 1)

(uε) =

.

Therefore, at the chosen primes, vPs(uε) = 2(εs − ηs), vcPs(uε) = −2(εs − ηs). (4)

The displayed ideal identity and (4) show that all poles of uε have order at most 2 and lie above the qb’s. Since QOK has valuation 1 at each such prime, Q2uε ∈ OK. So uε ∈ Q−2OK.

By (4), distinct ε’s give distinct valuation vectors, hence distinct elements uε. Therefore

2tf h(K) ≥ exp{(tlog 2 − log H)f}.

|U| ≥

| |
|---|


Set γ := tlog 2 − log H. The following result is the geometric part of the proof: a sequence of admissible ﬁelds with the same split rational primes and γ > 0 already gives the desired planar point sets.

- Theorem 2.3. Suppose there is a sequence of admissible data (Lj,Kj = Lj(i),q1,...,qt), with the same rational primes q1,...,qt, degrees fj = [Lj : Q] → ∞, and a constant H > 0, independent of j, such that h(Kj) ≤ Hfj and γ := tlog 2 − log H > 0. Then there is a constant δ > 0 and inﬁnitely many n such that ν(n) ≥ n1+δ.


For the proof of Theorem 2.3, ﬁx one admissible datum in the sequence and suppress the index j. Thus f = [L : Q], K = L(i), and the primes qb and their product Q are ﬁxed. Proposition 2.2 gives |U| ≥ eγf, where γ = tlog 2 − log H. Put D = Q2, so that U ⊂ D−1OK. The next two subsections construct the corresponding ﬁnite planar set.

### 2.1 Choosing a Window and Projecting

After an admissible datum is ﬁxed, the set U supplied by Proposition 2.2 gives many norm-one elements that will serve as translations in a Minkowski lattice. We choose a random translate of this lattice, keep the points inside a product of discs, and count pairs whose diﬀerence lies in U.

For each real embedding of L, choose one extension σr : K → C, r = 1,...,f, and use the Minkowski map

Φ : K −→ V = Cf, Φ(x) = (σ1(x),...,σf(x)).

We identify the fractional ideal D−1OK with the lattice Λ = Φ(D−1OK) ⊂ V , and also write U for its image Φ(U) ⊂ Λ.

The boundedness condition below is an Archimedean one. For z = (z1,...,zf) ∈ V , put z ∞ = max1≤r≤f |zr|, and let BR = {z ∈ V : z ∞ ≤ R}. Thus BR is a product of f radius-R discs.

For a coset a + Λ, deﬁne Xa = (a + Λ) ∩ BR, Na = |Xa|, and Ea = #{(x,x ) ∈ Xa2 : x − x ∈ U}.

Thus Na counts the bounded-norm lattice points in the lattice coset, while Ea counts the ordered pairs among them whose diﬀerence is one of our norm-one translations.

Let b(R) = πR2 be the area of one radius-R disc, let a(R) be the overlap area of two radius-R discs whose centers are distance 1 apart – the coordinatewise size of each translation in U by (3)

– and set ρR = a(R)/b(R). Then ρR → 1 as R → ∞.

- Lemma 2.4. Choose R > 1/2 so large that log ρR > −γ/2. Then some nonempty coset a + Λ satisﬁes Ea ≥ eγf/2Na.

Proof. Averaging over a ∈ V/Λ with respect to Haar probability measure, the standard unfolding identity gives

Ea[Na] =

vol(BR) covol(Λ)

=

b(R)f covol(Λ)

.

For a ﬁxed u ∈ U, the pairs with x −x = u correspond to points in (a+Λ)∩BR ∩(BR −u). By (3), every coordinate of this Minkowski-space translation has absolute value 1. Hence vol(BR ∩ (BR − u)) = a(R)f. Summing over u ∈ U and averaging over the torus gives

Ea[Ea] = |U|a(R)f covol(Λ)

= |U|ρfR Ea[Na].

If every nonempty coset had Ea < |U|ρfRNa, then integrating over all cosets would contradict the preceding identity; empty cosets contribute zero to both sides. Thus some nonempty coset

has Ea ≥ |U|ρfRNa. Using |U| ≥ eγf and the choice of R gives Ea ≥ eγf/2Na.

| |
|---|


Fix a coset supplied by Lemma 2.4, and write X = Xa and N = |X|. Any one of the chosen complex coordinates may now be used to obtain a planar set. For concreteness, let π1 : V → C be the ﬁrst-coordinate projection, corresponding to the embedding σ1, and put P = π1(X) ⊂ C R2.

- Lemma 2.5. The map π1 : X → C is injective. Moreover, ν(P) ≥ 21eγf/2|P|.


Proof. If x,x ∈ X and π1(x) = π1(x ), then x−x = Φ(D−1β) for some β ∈ OK, with σ1(β) = 0. Because σ1 is a ﬁeld embedding, β = 0, so x = x . Thus |P| = |X| = N.

Each ordered pair counted by Ea has the form (x,x + u), with u ∈ U, and it projects to an ordered unit-distance pair because |π1(x + u) − π1(x)| = |π1(u)| = 1. Injectivity of π1 on X

shows that distinct ordered pairs in X2 give distinct ordered planar pairs. Since each unordered unit segment has at most two orientations,

2ν(P) ≥ Ea ≥ eγf/2|P|.

| |
|---|


### 2.2 The Size Bound

- Lemma 2.5 gives many unit distances relative to the ﬁeld degree. To turn this into a statement about n = |P|, we need a uniform exponential upper bound for the number of points that can ﬁt in the ﬁnite window. This is a packing estimate in the Archimedean sup norm.
- Lemma 2.6. Let n = |P|. Then n ≤ eBf, where B = 2log(4RD).


Proof. Since π1 is injective on X, it is enough to bound |X|. If x = x in X, write x − x = Φ(D−1β), with β ∈ OK \ {0}. Then

f

|σr(D−1β)| = D−f|NK/Q(β)|1/2 ≥ D−f,

r=1

because the algebraic norm of a nonzero algebraic integer is a nonzero integer. Hence some coordinate diﬀers by at least D−1, so X is D−1-separated in the sup norm.

The open polydiscs of sup-norm radius D−1/2 centered at the points of X are pairwise disjoint and all lie in BR+D−1/2. Comparing volumes,

|X| π(D−1/2)2 f ≤ π(R + D−1/2)2 f. Therefore

|P| = |X| ≤ (1 + 2RD)2f ≤ (4RD)2f = eBf.

| |
|---|


Proof of Theorem 2.3. For each j, Lemmas 2.4, 2.5, and 2.6 give a planar set Pj, with nj = |Pj|, such that

- 1

- 2


njeγfj/2, nj ≤ eBfj.

ν(Pj) ≥

Also nj → ∞. Indeed, every ordered pair counted by Ea is determined by its two endpoints, so Ea ≤ n2j, while Lemma 2.4 gives Ea ≥ eγfj/2nj. Thus nj ≥ eγfj/2.

From nj ≤ eBfj, we obtain fj ≥ log nj/B. Hence

- 1

- 2


- 1

- 2


n1+j γ/(2B). Set δ = γ/(4B) > 0. Since nj → ∞, the factor 1/2 is absorbed for all suﬃciently large j, and ν(Pj) ≥ nj1+δ.

njeγfj/2 ≥

ν(Pj) ≥

| |
|---|


## 3 Producing the Fields

It remains to produce ﬁelds satisfying the hypotheses of Theorem 2.3. The construction starts from a cyclic cubic ﬁeld F, builds an inﬁnite unramiﬁed pro-3 quotient tower over it, and uses Chebotarev to choose ﬁxed rational primes qb that split completely in every ﬁnite layer. Because the tower is unramiﬁed, root discriminants stay bounded; after adjoining i, the class-number estimate below gives the uniform exponential bound needed in the geometric criterion.

Remark 3.1. The class-ﬁeld-theoretic construction is a specialization of the Hajir–Maire method for building T-split S-ramiﬁed p-towers [HM01, Section 2]. In the present proof S is empty, so the tower is unramiﬁed, and T is the set of primes of F above the selected rational primes qb. The Frobenius-killing step below is the same tower-cutting mechanism developed further by Hajir, Maire, and Ramakrishna [HMR21]: choose primes whose Frobenius classes lie in the Frattini subgroup, impose those Frobenius elements as new relations, and retain enough Golod– Shafarevich deﬁciency for the quotient tower to remain inﬁnite.

### 3.1 Auxiliary Results for the Field Construction

We ﬁrst state the number-theoretic results used directly in the construction. A rational prime means a prime number in Z. A prime of a number ﬁeld means a nonzero prime ideal in its ring of integers, so one rational prime can have several primes of F above it. Appendix A records the conventions and references behind these results.

The ﬁrst proposition is the cyclotomic calculation that creates the base ﬁeld. The conductor language is recalled in Deﬁnition A.5. The general tool is the conductor–discriminant formula: if a ﬁnite abelian ﬁeld L/Q has character group X, then |DL| = ψ∈X f(ψ), where f(ψ) is the conductor of the character ψ. The exact calculation is needed not only to bound a discriminant. It lets us compare the discriminants of M and F; equality |DM| = |DF|[M:F] forces the relative discriminant of M/F to be trivial, hence shows that M/F is unramiﬁed. This is what later gives a large elementary abelian quotient of the unramiﬁed pro-3 Galois group.

- Proposition 3.2. Let r1,...,r be distinct rational primes congruent to 1 mod 3. For each i, let Li be the cyclic cubic subﬁeld of Q(ζri), and put M = L1 ···L . Let χi be a cubic Dirichlet character of conductor ri, and let F ⊂ M be the cyclic cubic ﬁeld cut out by χ = χ1 ···χ in the sense of Deﬁnition A.5. Then the ﬁelds Li are totally real and linearly disjoint,


Gal(M/Q) =∼ (Z/3Z) , Gal(M/F) =∼ (Z/3Z) −1,

and, writing D = i ri, |DF| = D2. Moreover, M/F is everywhere unramiﬁed.

Proof. The standard cyclotomic facts are that Li is totally real, has conductor ri, and is ramiﬁed only at ri. Since the ramiﬁed rational primes are disjoint, the Li’s are linearly disjoint, giving the displayed Galois group for M/Q. The product character χ cuts out a cyclic cubic subﬁeld F ⊂ M, and the quotient Gal(M/F) has rank − 1.

Set D = i ri. The conductor–discriminant formula gives |DF| = D2, |DM| = D2·3 −1 = |DF|[M:F].

The tower discriminant formula for the relative discriminant (Deﬁnition A.6) says

|DM| = |DF|[M:F] NF/Q(dM/F).

The equality above therefore forces dM/F = OF, so there is no ﬁnite ramiﬁcation in M/F. Both ﬁelds are totally real, so there is no inﬁnite ramiﬁcation either. Hence M/F is everywhere unramiﬁed. For background and references, see Proposition A.11, [Was97, Chapter 3, especially Theorem 3.11], and [Neu99, Chapter VI].

| |
|---|


The next proposition is the group-theoretic step that lets us impose splitting conditions without destroying the tower. If G is a ﬁnitely generated pro-p group, its Frattini subgroup is Φ(G) =

M M, where M runs over maximal proper open subgroups of G; equivalently Φ(G) = Gp[G,G]. It consists of the “non-generators” of G: quotienting by elements in Φ(G) does not lower the minimal number of generators, though it does add relations. Write d(G) for the minimal number of topological generators, and r(G) for the minimal number of relations in a pro-p presentation.

- Proposition 3.3. Let G be a ﬁnitely generated pro-p group. Then d(G) = dimFp G/Φ(G). If g1,...,gk ∈ Φ(G) and N is their closed normal closure, then d(G/N) = d(G) and r(G/N) ≤ r(G) + k. For deﬁnitions and references, see Proposition A.8; in particular [RZ10, Section 2.8], [Koc02, Theorem 4.10], [DdSMS99, Proposition 1.9(ii)].

We will apply the preceding proposition after choosing Frobenius elements that lie in Φ(G). The next result is the relation-counting criterion that proves inﬁnitude once the relation rank is small compared with the generator rank.

- Proposition 3.4 (Golod–Shafarevich inequality). If a ﬁnite nontrivial pro-p group has generator rank d and relation rank r, then r > d2/4. Equivalently, a nontrivial ﬁnitely generated pro-p group with r ≤ d2/4 is inﬁnite. See Proposition A.9, [GS64, GS65], and [Koc02, Chapter 11].
- Proposition 3.5 (Shafarevich relation-rank estimate). Let F be a totally real cubic ﬁeld, so ζ3 ∈/ F, and let G = Gal(Fur,3/F) be the Galois group of its maximal everywhere-unramiﬁed pro-3 extension, in the sense of Deﬁnition A.3. Then r(G) ≤ d(G)+C0 for an absolute constant C0. See Proposition A.10, [Sha63, Sha66], and [NSW08, Chapter X, Section 10].

We use Chebotarev to ﬁnd rational primes that are already split at the ﬁnite level E(i). Complete splitting in the normal closure of E(i) over Q simultaneously gives the three properties needed below: the congruence qb ≡ 1 (mod 4), complete splitting in F, and trivial Frobenius in the Frattini quotient G/Φ(G). The last property is what lets us kill the corresponding Frobenius elements without decreasing the generator rank of the pro-3 tower.

- Proposition 3.6 (Chebotarev density theorem). Let G = Gal(Fur,3/F), and let E/F be the ﬁnite extension corresponding to the Frattini quotient G/Φ(G). For any positive integer t, and after excluding any prescribed ﬁnite set of rational primes, there exist distinct rational primes q1,...,qt which split completely in the normal closure over Q of E(i). For each such prime qb, qb ≡ 1 (mod 4) and qb splits completely in F, and every prime v | qb of F has Frobenius class trivial in G/Φ(G). Hence a Frobenius representative at v lies in Φ(G). For references, see Proposition A.12, [Neu99, Chapter VII, Section 13], and [Tsc26].


- Proposition 3.7. There is an absolute constant Cclass > 0 such that every number ﬁeld K satisﬁes h(K) ≤ max{2,rd(K)}Cclass[K:Q]. The constant Cclass is absolute: it is independent of the ﬁeld K, its degree, and its signature. For ﬁelds with rd(K) ≥ 2, this is simply h(K) ≤

- rd(K)O([K:Q]) = |DK|O(1). This is the class-number consequence of Minkowski’s ideal-class bound used in Proposition A.13; see also [Neu99, Chapter I, Section 5] and [Lan94, Chapter V].


3.2 The Field Construction

We now assemble the results from Subsection 3.1. The parameter counts the auxiliary cyclic cubic ﬁelds in the initial compositum. It will give t 2 split rational primes, while the constant H in the class-number bound below has log H = O( log ).

- Proposition 3.8. For all suﬃciently large integers , set t = ( − 1)2/100 . Then one can ﬁnd a number ﬁeld F, distinct rational primes q1,...,qt ﬁxed independently of j, and ﬁelds Fj with F0 = F, satisfying the following properties. Write fj = [Fj : Q] and Kj = Fj(i).


- (P1) The base ﬁeld F is totally real, cyclic cubic over Q, does not contain ζ3, and has controlled root discriminant log rd(F) = O( log ).
- (P2) The ﬁelds form an inﬁnite tower F = F0 ⊂ F1 ⊂ F2 ⊂ ···

such that each Fj/F is ﬁnite Galois, everywhere unramiﬁed, and has 3-group Galois group. Moreover fj → ∞.

- (P3) Every Fj is totally real, and the root discriminant is constant: rd(Fj) = rd(F).
- (P4) Each qb, 1 ≤ b ≤ t, satisﬁes qb ≡ 1 (mod 4) and splits completely in every Fj.
- (P5) There is a constant H , independent of j, such that

rd(Kj) ≤ 2rd(F), h(Kj) ≤ Hfj , log H = O( log ).

- (P6) The contribution from the split primes dominates the class-number loss: tlog 2−log H > 0.


Proof. We build the tower in four steps. We ﬁrst construct F and a large elementary abelian unramiﬁed 3-extension above it. We then impose the splitting conditions by passing to an inﬁnite quotient G of the maximal unramiﬁed pro-3 group. The ﬁnite layers of that quotient give the ﬁelds Fj, and the last step checks the class-number and numerical bounds.

- Step 1: construct F and the initial generator lower bound. Choose r1,...,r to be the ﬁrst rational primes with ri ≡ 1 (mod 3). Let Li be the cyclic cubic subﬁeld of Q(ζri), and put M = L1 ···L . Let χi be a cubic Dirichlet character of conductor ri. Let F be the cyclic cubic ﬁeld cut out by the character χ = χ1 ···χ . The conductor language and the phrase “cut out” are explained in Deﬁnition A.5; the cyclotomic calculation itself is Proposition 3.2. Applying that proposition, F is a totally real cyclic cubic ﬁeld, M/F is everywhere unramiﬁed, and


Gal(M/F) =∼ (Z/3Z) −1.

Since F is totally real, it does not contain the non-real root of unity ζ3. Because M/F is an everywhere-unramiﬁed 3-extension, the Galois group of the maximal everywhere-unramiﬁed pro-3 extension, G = Gal(Fur,3/F), has a quotient (Z/3Z) −1, and so

d(G) ≥ − 1. (5)

This lower bound is what makes the later choice t = ( − 1)2/100 compatible with the Golod– Shafarevich relation count.

Writing D = i ri, Proposition 3.2 also gives |DF| = D2. Since the ri are the ﬁrst primes congruent to 1 mod 3, the prime number theorem in arithmetic progressions [Dav00] gives

log rd(F) =

1 3

- 2

- 3 i


log |DF| =

log ri = O( log ). (6)

This is the required root-discriminant bound for the base ﬁeld. Together with the previous paragraph, this proves property P1. The same bound will be used to prove property P5 after the ﬁnite layers are constructed.

- Step 2: construct an inﬁnite quotient with trivial selected Frobenius classes. Shafarevich’s relationrank estimate (Proposition 3.5) gives


r(G) ≤ d(G) + C0 (7) for an absolute constant C0, because F is totally real cubic and ζ3 ∈/ F.

Let E/F be the Frattini quotient extension corresponding to G/Φ(G), and put d = d(G) and t = ( − 1)2/100 . By Proposition 3.6, choose distinct rational primes q1,...,qt, avoiding 3D, with the stated splitting and Frattini-trivial Frobenius properties. We now pass to a quotient in which the selected Frobenius elements are trivial, so that the selected primes split in all later layers.

There are exactly

k = #{v ⊂ OF : v | qb for some b} = 3t

such primes v of F, because each qb splits completely in the cubic ﬁeld F. Choose one Frobenius representative σv ∈ G for each of these primes, and let

N = σv : v | qb for some b G

be their closed normal closure. Set G = G/N. This adds at most k = 3t relations. Since these representatives lie in Φ(G), the Frattini quotient identity from Proposition 3.3 gives d(G) = d, while the relation count is bounded by

3d2 100

r(G) ≤ r(G) + k = r(G) + 3t ≤ d + C0 +

.

For , hence d, suﬃciently large, the right side is < d2/4. By Golod-Shafarevich, again as stated in Proposition 3.4, G is inﬁnite. Thus G is inﬁnite, and the selected Frobenius classes are trivial in it. These two facts produce the inﬁnite tower in property P2 and the complete splitting in property P4.

- Step 3: extract the tower and prove prescribed splitting. Choose a descending chain G = H0 ⊃ H1 ⊃ H2 ⊃ ···

of open normal subgroups with indices tending to inﬁnity, and let Fj be the corresponding ﬁxed ﬁelds. Then Fj/F is ﬁnite Galois, everywhere unramiﬁed, and has 3-group Galois group; since the indices tend to inﬁnity, fj → ∞. This proves property P2.

Since trivial Frobenius is equivalent to complete splitting (Deﬁnition A.7), the quotient makes the selected Frobenius classes trivial, so each qb splits completely in every Fj: the Frobenius is already trivial in G, hence also in each ﬁnite quotient corresponding to Fj/F. The congruence qb ≡ 1 (mod 4) was built into the Chebotarev choice. This proves property P4.

The layers remain totally real: if a real place became complex in Fj/F, the decomposition group at that inﬁnite place would have order 2, impossible inside a 3-group. Finite unramiﬁed extensions preserve root discriminant, so rd(Fj) = rd(F). This proves property P3.

- Step 4: prove the class-number and numerical bounds. Finally put Kj = Fj(i). The relative discriminant dKj/Fj divides 4OFj, so


|DKj| = |DFj|2 NFj/Q(dKj/Fj) ≤ |DFj|24fj.

Taking 2fj-th roots, since [Kj : Q] = 2fj, gives rd(Kj) ≤ 2rd(F). Also, because qb ≡ 1 (mod 4) and qb splits completely in Fj, each prime v | qb of Fj splits in Kj = Fj(i), as required for the construction of Section 2. The class-number estimate in Proposition 3.7 therefore gives

h(Kj) ≤ (2rd(F))Cclass[Kj:Q] = Hfj , H = (2rd(F))2Cclass. Thus log H = O(log rd(F)) = O( log ). This proves property P5. Finally, the explicit choice of t gives

t =

( − 1)2 200

( − 1)2 100 ≥

for all suﬃciently large . Combining this quadratic lower bound for t with log H = O( log ) gives tlog 2 − log H > 0 for all suﬃciently large , which proves property P6.

| |
|---|


Proof of Theorem 1.1. Choose large enough that Proposition 3.8 applies and γ := tlog 2 − log H > 0. Then the ﬁelds Lj = Fj and ﬁxed rational primes qb satisfy the hypotheses of Theorem 2.3. Hence there is δ > 0 and a sequence of planar sets Pj, nj = |Pj| → ∞, with ν(Pj) ≥ n1+j δ for all suﬃciently large j. Since ν(nj) is the maximum over all nj-point planar sets, ν(nj) ≥ ν(Pj) ≥ n1+j δ. The integers nj tend to inﬁnity, so this gives inﬁnitely many n.

| |
|---|


Remark 3.9. The constants are ﬁxed before the tower level j varies. First choose large enough that the estimates above give γ = tlog 2 − log H > 0. Chebotarev then gives ﬁxed rational primes q1,...,qt, and hence the ﬁxed product Q = b qb. After R is chosen in the averaging argument, these choices determine the ﬁxed constants D = Q2 and B = 2log(4RD). Finally set δ = γ/(4B) > 0. This δ is ﬁxed throughout the inﬁnite tower. Since the degrees [Fj : Q] tend to inﬁnity, the point-set sizes nj produced by Theorem 2.3 also tend to inﬁnity.

## A Background Facts and Citations

This appendix records conventions and references used above. The main theorems are stated in Section 3.1; the entries below supply the surrounding standard language and sources.

### Field and Ramiﬁcation Conventions

- Deﬁnition A.1 (Basic ﬁeld conventions). A number ﬁeld is a ﬁnite extension of Q. A rational prime is a prime number q ∈ Z, while a ﬁnite prime of a number ﬁeld L is a nonzero prime ideal

p ⊂ OL. A ﬁeld L is totally real if every embedding L → C has image in R. See, for example, [Neu99, Chapter I, Sections 1–5].

- Deﬁnition A.2 (Splitting, ramiﬁcation, and unramiﬁed extensions). Let M/F be a ﬁnite extension and let p be a ﬁnite prime of F. In the factorization

pOM =

P|p

Pe(P/p),

the exponent e(P/p) is the ramiﬁcation index. The prime p is unramiﬁed if all these indices are 1, and it splits completely if there are [M : F] primes above it, all unramiﬁed and with residue degree 1. For a rational prime q, complete splitting in L means qOL = p1 ···p[L:Q] and OL/pi =∼ Fq.

Inﬁnite ramiﬁcation concerns Archimedean places: a real place ramiﬁes if it becomes complex. Thus a totally real extension of a totally real ﬁeld has no inﬁnite ramiﬁcation. “Everywhere unramiﬁed” means unramiﬁed at all ﬁnite and inﬁnite places.

- Deﬁnition A.3 (Maximal unramiﬁed pro-p extension). For a number ﬁeld F, Fur,p denotes the compositum of all ﬁnite everywhere-unramiﬁed Galois extensions of F whose Galois groups are ﬁnite p-groups. Its Galois group Gal(Fur,p/F) is a pro-p group, and its ﬁnite quotients correspond to ﬁnite everywhere-unramiﬁed Galois p-group extensions of F.
- Deﬁnition A.4 (CM ﬁelds). A CM ﬁeld is a totally imaginary quadratic extension K/K+ of a totally real ﬁeld. The nontrivial automorphism of K/K+ is denoted c. In this paper K = L(i) with L totally real, and for every complex embedding σ : K → C, σ(c(α)) = σ(α). Consequently, elements u with uc(u) = 1 have |σ(u)| = 1 in every complex embedding.

- Deﬁnition A.5 (Conductors and ﬁelds cut out by characters). For a ﬁnite abelian extension

L/Q, the Kronecker–Weber theorem embeds L in a cyclotomic ﬁeld Q(ζm). The ﬁeld conductor is the least such m. A Dirichlet character χ has conductor f(χ), the least modulus of a primitive Dirichlet character inducing χ.

Choose a common modulus m for a ﬁnite subgroup X of Dirichlet characters, for instance a common multiple of their conductors. Via Gal(Q(ζm)/Q) =∼ (Z/mZ)×, the group X determines the ﬁxed ﬁeld of the common kernel χ∈X kerχ. If X = χ , we say that this ﬁeld is cut out by χ. Thus an order-3 character cuts out a cyclic cubic ﬁeld.

- Deﬁnition A.6 (Discriminants). The absolute discriminant of L is denoted DL. For an extension M/F, the relative discriminant dM/F is an ideal of OF, and the tower formula is


|DM| = |DF|[M:F] NF/Q(dM/F).

Thus dM/F = OF is equivalent to no ﬁnite ramiﬁcation in M/F. The root discriminant is

- rd(L) = |DL|1/[L:Q]. Finite unramiﬁed extensions preserve root discriminant.

- Deﬁnition A.7 (Frobenius elements). Let N/K be a ﬁnite Galois extension and let p be a ﬁnite


prime of K unramiﬁed in N. For a prime P | p of N, the Frobenius element FrobP/p ∈ Gal(N/K) acts on the residue ﬁeld by x  → x|OK/p|. In a nonabelian extension only its conjugacy class is independent of P. The prime p splits completely in N exactly when this Frobenius class is the identity. See [Neu99, Chapter VII, Section 13].

Group-Theoretic and Class-Field References

- Proposition A.8. For a ﬁnitely generated pro-p group G, the Frattini subgroup satisﬁes Φ(G) =

M M = Gp[G,G], where M runs over maximal proper open subgroups. Burnside’s basis theorem gives d(G) = dimFp G/Φ(G). If g1,...,gk ∈ Φ(G) and N is their closed normal closure, then d(G/N) = d(G) and r(G/N) ≤ r(G) + k. See [RZ10, Section 2.8], [Koc02, Theorem 4.10], and [DdSMS99, Proposition 1.9(ii)].

- Proposition A.9 (Golod–Shafarevich inequality). If a ﬁnite nontrivial pro-p group has generator rank d and relation rank r, then r > d2/4. Equivalently, a nontrivial ﬁnitely generated pro-p group with r ≤ d2/4 is inﬁnite. See [GS64, GS65] and [Koc02, Chapter 11].
- Proposition A.10 (Shafarevich relation-rank estimate). Shafarevich’s estimate bounds the relation rank of Galois groups of maximal pro-p extensions with prescribed ramiﬁcation. In the only form used here, if F is totally real cubic, ζ3 ∈/ F, and G = Gal(Fur,3/F), then r(G) ≤ d(G) + C0 for an absolute constant C0. See [Sha63, Sha66] and [NSW08, Chapter X, Section 10].
- Proposition A.11. If r is a rational prime with r ≡ 1 (mod 3), the unique cyclic cubic subﬁeld of Q(ζr) is totally real, has conductor r, and is ramiﬁed only at r. For a ﬁnite abelian extension L/Q with character group X, the conductor–discriminant formula is |DL| = χ∈X f(χ). For

characters with pairwise coprime conductors, f(χ1 ···χm) = i f(χi), ignoring conductor-1 trivial factors. These are standard facts from cyclotomic class ﬁeld theory; see [Was97, Chapter 3, especially Theorem 3.11] and [Neu99, Chapter VI].

- Proposition A.12 (Chebotarev density theorem). Chebotarev’s density theorem implies that, after excluding ﬁnitely many bad primes, inﬁnitely many rational primes split completely in any prescribed ﬁnite Galois extension of Q. Applied to the normal closure over Q of E(i), where E/F is the Frattini quotient extension corresponding to G/Φ(G), it gives the primes used in Proposition 3.6. See [Neu99, Chapter VII, Section 13] and [Tsc26].
- Proposition A.13. Minkowski’s ideal-class bound, combined with the elementary divisorfunction bound for the number of ideals of a given norm, gives h(K) ≤ max{2,rd(K)}O([K:Q]),




with an absolute implicit constant. Equivalently, when rd(K) ≥ 2, h(K) ≤ |DK|O(1). See [Neu99, Chapter I, Section 5] and [Lan94, Chapter V].

## References

[ABS25] Noga Alon, Matija Bucić, and Lisa Sauermann. Unit and distinct distances in typical norms. Geometric and Functional Analysis, 35:1–42, 2025.

[ÁP22] Péter Ágoston and Dömötör Pálvölgyi. An improved constant factor for the unit distance problem. Studia Scientiarum Mathematicarum Hungarica, 2022.

[BBF+10] Ondřej Bílka, Kevin Buchin, Radoslav Fulek, Masashi Kiyomi, Yoshio Okamoto, Shin-ichi Tanigawa, and Csaba D. Tóth. A tight lower bound for convexly independent subsets of the Minkowski sums of planar point sets. Electronic Journal of Combinatorics, 17(1):Note 35, 2010.

[BMP05] Peter Brass, William O. J. Moser, and János Pach. Research Problems in Discrete Geometry. Springer, New York, 2005.

[Bra96] Peter Brass. Erdős distance problems in normed spaces. Computational Geometry, 6(4):195– 214, 1996.

[Dav00] Harold Davenport. Multiplicative Number Theory, volume 74 of Graduate Texts in Mathematics. Springer, New York, third edition, 2000. Revised by Hugh L. Montgomery.

[DdSMS99] John D. Dixon, Marcus P. F. du Sautoy, Avinoam Mann, and Dan Segal. Analytic Pro-p Groups, volume 61 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, second edition, 1999.

[EF97] Paul Erdős and Peter C. Fishburn. Minimum planar sets with maximum equidistance counts. Computational Geometry, 7(4):207–218, 1997.

[EPRS08] Friedrich Eisenbrand, János Pach, Thomas Rothvoß, and Nir B. Sopher. Convexly independent subsets of the Minkowski sum of planar point sets. Electronic Journal of Combinatorics, 15(1):Note 8, 2008.

[Erd46] Paul Erdős. On sets of distances of n points. American Mathematical Monthly, 53(5):248–250, 1946.

[GK15] Larry Guth and Nets Hawk Katz. On the Erdős distinct distances problem in the plane. Annals of Mathematics, 181(1):155–190, 2015.

- [GS64] E. S. Golod and I. R. Shafarevich. On the class ﬁeld tower. Izv. Akad. Nauk SSSR Ser. Mat., 28(2):261–272, 1964. English translation: Amer. Math. Soc. Transl. (2) 48 (1965), 91–102.
- [GS65] E. S. Golod and I. R. Shafarevich. On class ﬁeld towers. In Fourteen Papers on Logic, Algebra, Complex Variables and Topology, volume 48 of American Mathematical Society Translations, Series 2, pages 91–102. American Mathematical Society, Providence, RI, 1965. English translation of the 1964 Russian paper.


[GST25] Josef Greilhuber, Carl Schildkraut, and Jonathan Tidor. More unit distances in arbitrary norms. Bulletin of the London Mathematical Society, 57(9):2885–2901, 2025.

[HM01] Farshid Hajir and Christian Maire. Asymptotically good towers of global ﬁelds. In Carles Casacuberta, Rosa Maria Miró-Roig, Joan Verdera, and Sebastià Xambó-Descamps, editors, European Congress of Mathematics, Vol. II (Barcelona, 2000), volume 202 of Progress in Mathematics, pages 207–218. Birkhäuser, Basel, 2001.

[HMR21] Farshid Hajir, Christian Maire, and Ravi Ramakrishna. Cutting towers of number ﬁelds. Annales Mathématiques du Québec, 45(2):321–345, 2021.

[Koc02] Helmut Koch. Galois Theory of p-Extensions. Springer Monographs in Mathematics. Springer, Berlin, Heidelberg, 2002.

[KST54] Tamás Kővári, Vera T. Sós, and Pál Turán. On a problem of K. Zarankiewicz. Colloquium Mathematicum, 3:50–57, 1954.

[Lan94] Serge Lang. Algebraic Number Theory, volume 110 of Graduate Texts in Mathematics. Springer, New York, second edition, 1994.

[Mat11] Jiří Matoušek. The number of unit distances is almost linear for most norms. Advances in Mathematics, 226(3):2618–2628, 2011.

[Neu99] Jürgen Neukirch. Algebraic Number Theory, volume 322 of Grundlehren der mathematischen Wissenschaften. Springer, Berlin, Heidelberg, 1999. Translated from the German by Norbert Schappacher; with a foreword by G. Harder.

[NSW08] Jürgen Neukirch, Alexander Schmidt, and Kay Wingberg. Cohomology of Number Fields, volume 323 of Grundlehren der mathematischen Wissenschaften. Springer, Berlin, Heidelberg, second edition, 2008.

[RZ10] Luis Ribes and Pavel Zalesskii. Proﬁnite Groups, volume 40 of Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. Springer, Berlin, Heidelberg, second edition, 2010.

[Sha63] Igor R. Shafarevich. Extensions à points de ramiﬁcation donnés (en russe). Publications Mathématiques de l’IHÉS, 18:71–92, 1963.

[Sha66] Igor R. Shafarevich. Extensions with given points of ramiﬁcation. American Mathematical Society Translations, Series 2, 59:128–149, 1966. English translation by J. W. S. Cassels; title also cited as “Extensions with prescribed ramiﬁcation points”.

[SST84] Joel H. Spencer, Endre Szemerédi, and William T. Trotter. Unit distances in the Euclidean plane. In Béla Bollobás, editor, Graph Theory and Combinatorics, pages 293–303. Academic Press, London, 1984. Proceedings of the Cambridge Conference, 1983.

[Sze97] László A. Székely. Crossing numbers and hard Erdős problems in discrete geometry. Combinatorics, Probability and Computing, 6(3):353–358, 1997.

[Tsc26] N. Tschebotareﬀ. Die Bestimmung der Dichtigkeit einer Menge von Primzahlen, welche zu einer gegebenen Substitutionsklasse gehören. Mathematische Annalen, 95(1):191–228, 1926.

[Val05] Pavel Valtr. Strictly convex norms allowing many unit distances and related touching questions. Manuscript, 2005.

[Was97] Lawrence C. Washington. Introduction to Cyclotomic Fields, volume 83 of Graduate Texts in Mathematics. Springer, New York, second edition, 1997.

