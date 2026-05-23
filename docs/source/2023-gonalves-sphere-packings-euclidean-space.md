---
type: source
kind: paper
title: Sphere Packings in Euclidean Space with Forbidden Distances
authors: Felipe Gonçalves, Guilherme Vedana
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2308.03925v4
source_local: ../raw/2023-gonalves-sphere-packings-euclidean-space.pdf
topic: general-knowledge
cites:
---

# arXiv:2308.03925v4[math.NT]21Feb2025

## SPHERE PACKINGS IN EUCLIDEAN SPACE WITH FORBIDDEN DISTANCES

FELIPE GONC¸ALVES AND GUILHERME VEDANA

Abstract. We study the sphere packing problem in Euclidean space where we impose additional constraints on the separations of the center points. We prove that any sphere packing in dimension 48, with spheres of radii r, such that no two centers x1 and x2 satisfy b

4 3 ă 21r|x1 ´ x2| ă b

5 3, has center density less or equal than p3{2q24. Equality occurs for periodic packings if and only if the packing is given by a 48-dimensional even unimodular extremal lattice. This shows that any of the lattices P48p,P48q,P48m and P48n are optimal for this constrained packing problem, and gives evidence towards the conjecture that extremal lattices are optimal unconstrained sphere packings in 48 dimensions. We also provide results for packings up to dimension d ď 1200, where we impose constraints on the distance between centers and on the minimal norm of the spectrum, showing that even unimodular extremal lattices are again uniquely optimal. Moreover, in the one-dimensional case, where it is not at all clear that periodic packings are among those with largest density, we nevertheless give a condition on the set of constraints that allows this to happen, and we develop an algorithm to find these periodic configurations by relating the problem to a question about dominos.

Contents

- 1. Introduction 2

- 1.1. Motivation 2
- 1.2. Main results 3


- 2. Further main results 6

- 2.1. One-dimensional sphere packings 11
- 3. Generalities 12


- 3.1. Proof of Theorem 3. 16
- 4. One-dimensional packings and dominos 18
- 5. Proof of Theorem 6 22
- 6. Constructions via modular forms 24
- 7. Proof of Theorem 1 31
- 8. Proof of Theorem 4 32
- 9. Proof of Theorems 2 and 5 38 Acknowledgements 39 References 39


Date: February 24, 2025.

1. Introduction

The notorious Sphere Packing Problem asks a simple question: What is the best way of stacking higher-dimensional oranges1 in a higher-dimensional supermarket? It is not too surprising that in dimension 3, an optimal configuration arises when oranges (or cannonballs, which are not so juicy) are arranged in a hexagonal close packing, where laminated layers of spheres are assembled according to a suitable translation of the hexagonal lattice (fitting new spheres in the deep holes of the previous layer). What is remarkable is that this problem was proposed by Kepler around 1611 and was only solved in 1998 by Hales, in his famous large computer-assisted proof [18]. Recently, in 2016, the problem in dimensions 8 and 24 was solved by Viazovska et al. [10, 27], introducing a remarkable new construction using quasi-modular forms to define certain smooth auxiliary functions f8 and f24 satisfying certain sign constraints in physical and frequency space to solve the problem.2 To the best of our knowledge, there are only two other instances where Viazovska’s technique was used to construct auxiliary functions that were indeed used in the solution of some kind of optimization problem: (1) in the solution of a 12-dimensional uncertainty principle by the Cohn and Gonc¸alves [9] (best constant and function); (2) in the proof of the universality of the E8 and Leech lattices by Cohn, Kumar, Miller, Radchenko and Viazovska [11].

- 1.1. Motivation. We systematically study a new type of constrained sphere packing problem, where we forbid certain short distances between centers of spheres. We are then able to solve exactly this problem when the forbidden set is the complement of a finite collection of square roots of even integers. The main questions driving/inspiring the problems we study and solve in this manuscript are the following:


‚ What other ‘natural’ discrete geometry problems can be solved using Viazovska’s

modular forms construction technique?

‚ Can we embed the functions f8 and f24 found by Viazovska in a larger family of functions tfdu8|d in such a way that these work as auxiliary functions that solve some kind of dual optimization problem of the question above?

Our answer: Packings with forbidden distances and Theorems 3 and 4.

We now comment about our answer. First of all, the idea of creating a larger family of functions tfdu8|d that contains Viazovska’s functions was already explored in the interesting papers [25, 15]. However, in these two papers, no geometrical optimization problem was solved, and the functions they generate are not related to ours. Also, it is worth pointing out that, as we shall see in the proof of Theorem 4, there are several constraints our functions tHdu8|d satisfy. The troublesome part is to show that certain sign conditions are met, and these do not follow from positivity of Fourier coefficients (as in [15], conjecturally), since they indeed change sign in our case. To overcome this,

1The authors’ common favorite fruit. 2Viazovska received the Fields medal in 2022 for her accomplishments.

we came up with a numerical procedure, inspired by the one in [10], and so our proof is unavoidably computer-assisted. Secondly, at first glance, one might say that imposing additional constraints in a sphere packing, such as forbidding certain distances, is esoteric or unnatural. However, from the coding theory perceptive (sphere packings in Fmq ), this question has been asked already, studied to some extent and has applications. To the best of our knowledge, we believe we were the first to consider this question in Euclidean space; nevertheless, in coding theory, codes with forbidden distances have been the object of study in many occasions. See, for instance, [1, 2, 14, 16]. In Euclidean space, a cousin problem of the sphere packing problem is the chromatic number of Rd, and in this venue mathematicians have considered already the version with forbidden distances; see, for instance, [4, 24, 21]. Thirdly, there are a bunch of unexpected features coming from our study that might drive further research, such as the following:

♡ The functions tHdu8|d we create in the proof of Theorem 4 have several curious properties that we have verified with a computer up to d “ 1200, but they lack proper mathematical explanation. Proving these properties propagate in every dimension 8|d would allow us to extend Theorem 4 to every dimension;

♡ The one-dimensional case we study in Section 2.1 is a very intriguing combinatorial/geometric problem that seems hard to analyze. The natural question here is to know when the best packing can be taken to be periodic, and we do provide a partial answer when the complement of the forbidden set is finite or has finitely many accumulation points (so to speak);

♡ Perhaps the most interesting contribution of our manuscript is Theorem 1, which we single out. It turns out that in dimension 48, the constraints we need to impose are rather simple and nice, and we show that extremal lattices are optimal. Moreover, it is conjectured that extremal lattices are optimal unconstrained sphere packings in dimension 48, so one can also see Theorem 1 as further evidence to Conjecture 1.

♡ Since the submission of this paper, there have been further results on this topic that we would like to highlight. In [5], Boyvalenkov and Cherkashin find the largest kissing number with forbidden distances in dimension 48 - a configuration avoiding the set p´1{3,´1{6q Y p1{6,1{3q. The related energy problem is investigated in [7]. Moreover, and most surprisingly, in [6], Boyvalenkov, Cherkashin and Dragnev find several types of distance avoiding optimal spherical codes in S15,S21,S22 and S23, via the linear programming method.

- 1.2. Main results. As a prototype example of the kind of problem we will be concerned with, imagine that we are trying to place solid disks of diameter 1 in R2, so to obtain the largest possible density. However, we require that either two disks kiss each other or their centers are far apart, say, with a distance not smaller than λ ą 1. As λ slowly increases, we expect to see a transition between disks being allowed to ‘freely’ move around and disks clumping together. Indeed, we show in Proposition 10 that as λ Ñ 8, the best


arrangement is when three disks are placed on the vertices of an equilateral triangle of side length 1 (kissing each other) and the circuncenters of these triangles are placed in a hexagonal lattice of side length approximately λ. In this paper we study a generalized version of this problem, where an arbitrary set of distances may be forbidden.

We say that a sphere packing P “ X ` rBd (Bd is the unit ball in Rd and X the set of centers) avoids a set A Ă p1,8q if |x1 ´x2| R 2rA for all distinct x1,x2 P X (A is a set of forbidden distances). For instance, for the problem described in the previous paragraph, the set A would be the interval p1,λq. A periodic sphere packing is one where X “ Λ`Y , Λ is a lattice of minimal norm at least 2r and Y Ă Rd{Λ is a nonempty finite set. A lattice packing is when #Y “ 1. A lattice is even and unimodular if it has even squared norms and determinant 1. Such lattice is said to be extremal if its minimal norm squared is equal to 2 ` 2td{24u (see Section 2 for more information). We now state the first main result of this paper.

Theorem 1. Any even unimodular extremal lattice in R48 achieves maximal sphere packing density among all sphere packings that avoid the interval ´b

3,b

¯. Moreover, we have uniqueness among all periodic packings: if P “ Λ`Y `rBd is some periodic sphere packing in R48 that avoids this interval and has maximal density, then

4

5 3

?

6

2r pΛ ` Y q is an even unimodular extremal lattice.

Our result shows that any of the lattices P48p,P48q,P48m and P48n are optimal for this constrained packing problem. The first two lattices have a canonical construction as 2-neighbors of code lattices of extremal ternary codes (see [12, p. 195] and [22] for the other two).

- Conjecture 1. Any extremal lattice in dimension 48 has maximal sphere packing density among all possible sphere packings.

This conjecture is backed by the fact that no other better configuration is known. Perhaps an ‘easier’ to prove conjecture is that extremal lattices in 48 dimensions are the best lattice packings. We believe Theorem 1 could be used together with a computerassisted method to reduce the amount of cases needed to be checked and show that P48p produces the best lattice packing; however, new ideas are needed here. Below, we state a bold conjecture, which serves more as a research direction, as we have no numerical evidence towards it.

- Conjecture 2. Let L ă R48 be a lattice with minimal norm


?

### 6. If there is x P L with ?

?

8 ă |x| ă

10, then L has covolume ą 1.

This conjecture in conjunction with Theorem 1 implies that extremal lattices in R48 are the best lattice sphere packings. To see this, given any lattice L, normalize it so it has minimal norm

?

?

?

6. If there is no point x P L such that

8 ă |x| ă

10, we then use Theorem 1; if such a point exists, we use the conjecture.

- Theorem 1 will follow from Theorems 3 and 4, where we develop a new linear program-

ming method, similar to the Cohn and Elkies linear programming bound [8, Theorem 3.1], and a generalization of Viazovska’s modular function technique [10, 27] to find the desired ‘magic’ function. It turns out that if we allow ourselves to impose an extra condition on the spectrum of a given periodic configuration, one can prove a result similar to Theorem 1 in every dimension d multiple of 8 not congruent to 16 modulo 24 up to d “ 1200.

Define the forbidden set

Ad “ p1,a1 ` 2{adq Y pa1 ` 2{ad,a1 ` 4{adq Y ... Y papld ´ 2q{ad,ald{adq, where

ad “ 2 ` 2Z

d 24

^ and ld “ ad ` 4ˆZ

d ´ 4 12

^ ´ Z

d 24

^˙. (1) Our second main result is the following.

- Theorem 2. Let 8 ď d ď 1200, where d is divisible by 8 but d ı 16 mod 24. Let P “ Λ ` Y ` rBd be some periodic sphere packing that avoids the set Ad and such that the minimal norm of Λ˚ is larger than 2r?cd, where cd is given in Table 1. Then


denspPq ď volpBdqˆ?ad 2

˙d .

?ad

Moreover, in case #Y “ 1 then equality occurs if and only if

2r Λ is an even unimodular extremal lattice.

Indeed, Theorem 1 can be seen as a particular case of Theorem 2 since c48 “ 0 (hence we no longer need to assume that P is periodic) and A48 “ p1,a4{3qYpa4{3,a5{3q, but the first interval can be removed because of a sign condition on the magic function of Theorem

- 4 . Theorem 2 will follow from Theorem 3 (new linear programming bounds), Theorem 4 (magic contructions with modular forms) and Theorem 5 (equivalent to Theorem 2). As


in dimension 48, one could reduce Ad further for all d by understanding the sign changes of the functions in Theorem 4. However, there seems to be no particular interesting pattern, and the set Ad would be rather complicated and given by a table other than a simple formula. Appealing to simplicity, we decided for the above form. The dimensions d ” 16 mod 24 had to be excluded from our result since (for some unknown reason) the ‘magic’ function we construct in these dimensions failS to satisfy some of the properties in Theorem 4; for instance, their Fourier transform is nonpositive outside a neighborhood of the origin (although having positive mass). However, we believe it is possible to fix these issues if we impose more forbidden distances (see the more general Conjecture 3).

A classical result shows that extremal lattices may only exist up to dimension d ď 2 ˆ 105, but extending our results to such high dimensions seems out of reach with the present computational power on Earth, although we do believe they hold in all available dimensions (Conjecture 3). Indeed, d ď 1200 is an artifact of the computer-assisted

part in this paper, but we believe it can be improved a little bit with cleverer/optimized algorithms.

- Theorem 2 puts forward a general framework and gives some kind of explanation to why


one is only able to solve the sphere packing problem via linear programming in dimensions 8 and 24. We have now constructed a family of constrained problems, all amenable to linear programming methods and exact solutions via constructions with modular forms, which characterize extremal lattices as having optimal density among sphere packings avoiding certain distances. It is worth pointing out that the E8 and Leech lattices are the only extremal latttices in dimensions 8 and 24, that c8 “ c24 “ 0 and A8 “ A24 “ H. Hence, all the constraints we impose disappear in these dimensions, and we recover Viazovska’s results. Curiously, the same set of (unscaled) distances t

?

?m,

m ` 1,...,?nu appeared in a recent paper by Naslund on chromatic numbers of Rd [21]. Other remarks about our results are addressed in Section 2.

2. Further main results

We say that the set P “ X` 12Bd is a sphere packing of Rd (associated to a set X Ă Rd) if |x ´ y| P t0u Y r1,8q for all x,y P X, where Bd :“ ty P Rd : |y| ď 1u is the unit ball and | ¨ | is the Euclidean norm. For a sphere packing P, we define its density by

volpP X tQdq volptQdq

denspPq :“ limsup

,

tÑ`8

‰d

where Qd :“ “´21, 12

is the unit cube. The setup is as follows.

|Main Problem. Let K Ă r1,`8q be a bounded subset such that 1 P K. Consider the following family of sphere packings:<br><br>PdpKq :“ ␣<br><br>X ` 21Bd : @x,y P X we have |x ´ y| P t0u Y K Y psuppKq,8q(<br><br>.<br><br>The role of K here is to prescribe the short distances between the centers of a sphere packing. We say a sphere packing P is K-admissible if P P PdpKq. What are the properties of K-admissible sphere packings P that achieve maximal density? More precisely, if we let<br><br>∆dpKq :“ sup<br><br>PPPdpKq<br><br>denspPq,<br><br>we then want to study K-admissible sphere packings P such that denspPq “ ∆dpKq. Alternatively, letting A “ p1,suppKqszK, we then want to find a sphere packing of maximal density that avoids A; that is, no distance between centers belongs to A.|
|---|


For now on, we will stick with the formulation using K rather than A (prescribing rather than forbidding), as it fits better our scheme of results and constructions.

We now introduce some known facts about lattices. A (full rank) lattice Λ Ă Rd is a discrete subgroup of pRd,`q that contains d linear independent vectors. We let

ℓpΛq :“ t|λ| : λ P Λzt0uu

denote the lengths of Λ and minℓpΛq denote its minimal norm. Given a lattice Λ one can associate a sphere packing

1 r

Λ ` 12Bd pwith r “ minℓpΛqq and show that

PΛ :“

volp2rBdq volpRd{Λq

denspΛq :“ denspPΛq “

.

We say that a lattice Λ is K-admissible if the packing PΛ above is K-admissible, that is, if

ℓpΛq minℓpΛq

Ă K Y psuppKq,8q.

?

An even unimodular lattice Λ is one such that volpRd{Λq “ 1 and ℓpΛq Ă t

2n : n ě 1u (such lattices are integral and self-dual). These lattices have been widely studied and classified in the literature. It is known that they can only exist in dimensions multiple of 8 and, due to a classical theorem of Voronoi, that there are only finitely many of them in each dimension (modulo symmetries). It is known that (see [12, p. 194, Cor. 21])

pminℓpΛqq2 ď ad :“ 2Z

^ ` 2.

d 24

An even unimodular lattice attaining the above bound is called extremal . The E8, E82,D16` and Leech lattices are the only even unimodular extremal lattices up to dimension 24. In dimensions 32 and 40, there are more than 107 and 1051 of such lattices, respectively; however, in dimension 48, there are (so far) only 4 known lattices: P48p,P48q,P48m and P48n (see Nebe [22]). Moreover, it is known that extremal lattices cannot exist in sufficiently large dimensions [20] (as modular forms with several vanishing Fourier coefficients and very large weight necessarily have negative coefficients). The current best bound is due to Jenkins and Rouse [19], and it states that

dmax :“ suptrankpΛq : Λ is an even unimodular extremal latticeu ď 163264. Indeed, one can show that for any β ą 0, there exists D such that there is no even unimodular lattice of rank d ą D and minimal squared norm larger than ad ´ β. For more information on extremal lattices, see [26].

We now state three other main results of this paper. The first is an analogue of the Cohn and Elkies linear programming bound for ∆dpKq.

- Theorem 3. Let K Ă r1,`8q be bounded and such that 1 P K. Define


`12Bd

˘

Fp0q Fpp0q

∆LPd pKq :“ vol

inf

,

where the infimum is taken over all nonzero functions F P L1pRdq X CpRdq such that : Fpxq ď 0 for |x| P K Y psuppKq,8q and Fppxq ě 0 for all x.

Then

∆dpKq ď ∆LPd pKq.

- Theorem 4. Let 8 ď d ď 1200, where d is divisible by 8 but d ı 16 mod 24. Define ld as in (1) and

Kd “

1

?adt

?ad,

?

ad ` 2,

?

ad ` 4,...,aldu.

Also let cd be given by Table 1 (cd “ 0 if d “ 8,24,48). Then there exists a nonzero radial function H : Rd Ñ R of Schwartz class such that:

‚ Hpxq ď 0 if |x|2 ą ld; ‚ Hppxq ě 0 if |x| ą cd; ‚ Hpxq “ Hppxq “ 0 if |x|2 P tad,ad ` 2,...u;

‚ t|x|2 : Hpxq “ 0 and |x|2 ą ld´u “ tld,ld ` 2,...u; ‚ t|x|2 : Hppxq “ 0 and |x|2 ą cdu “ tad,ad ` 2,...u

Moreover, if d “ 48 we additionally have that t|x|2 : Hpxq ă 0u X p0,10q “ p6,8q.

In the theorem above, |x|2 ą ld´ means that |x|2 ą ld ´ ϵd for some small ϵd ą 0. We note that one can indeed build functions H for all dimensions congruent to 16 modulo 24 using the same techniques of Theorem 4. However it turns out that Hppxq ď 0 for

- |x| ą opadq (numerically), although Hpxq ď 0 for |x|2 ą ld and Hp0q “ Hpp0q ą 0. One should also notice that the numbers cd seem to satisfy (for small d)


cd “ ad ´ 2 ´ Op1q if d ” 8 mod 24 and cd “ ad ´ 6 ´ Op1q if d ” 0 mod 24. Also, in fact, cd is an approximation from the right of the last simple root of Hppxq. All these facts give a heuristic explanation why we only get results free from spectral conditions in dimensions 8,24 and 48 (hence a result for all sphere packings, periodic or not). It goes as follows: Experimentally, the Op1q in cd is less than 1 for small d and cd increases with d on each equivalence class modulo 24, which means that if d ě 72, then ad ě 8, and so cd ě 1. Thus Hp would never be nonnegative. For d “ 8,24,48, we have cd “ 0 ´ Op1q ă 0. Thus Hp ě 0 (see Figure 1). For the remaining small dimensions not equal to 16 modulo 24, which are, d “ 32 and d “ 56, we have c32 “ 2 ´ Op1q and c56 “ 4 ´ Op1q, which are positive, and so Hp is not nonnegative.

- Theorem 5. Let d, ad, Kd and cd be as in Theorem 4. Let P “ Λ ` Y ` 12Bd be some


?cd. Then

Kd-admissible periodic sphere packing such that minℓpΛ˚q ą

denspPq ď volpBdqˆ?ad 2

˙d .

In case #Y “ 1, equality above occurs if and only if ?adΛ is an even unimodular extremal lattice. We conclude that if d P t8,24,48u, then

∆dpKdq “ ∆LPd pKdq “ volpBdqˆ?ad

˙d .

2

0 8 0 1.5880 8 0 3.5850 8 1.4710 5.5790 8 3.3760 7.5720 8 5.1550 9.5630 8 5.4650 11.554 8 7.4160 13.543 8 9.3400 15.530 8 11.214 17.514 8 11.462 19.495 8 13.429 21.469 8 15.384 23.426 8 17.323 23.537 8 19.234 25.533 8 19.458 27.530 8 21.433 29.558 8 23.403 31.519 8 25.358 33.515 8 27.305 37.454 8 29.244 39.891 8 31.483 42.000 8 39.277 44 8 46 46 8 48 48 8 50 50 8 52 52 8 54 54 8 56 56 8 58 58 8 60 60 8 62 62 8 64 64 8 66 66 8 68 68 8 70 70 8 72 72 8 74 74 8 76 76 8 78 78 8 80 80 8 82 82 8 84 84 8 86 86 8 88 88 8 90 90 8 92 92 8 94 94 8 96 96 8 98 98 8 100

Table 1. Values of cd for d “ 8,16,24,...,1200. One should read it left to right top to bottom. From dimension d “ 536 onwards, computational time was too high, and we simply took cd “ ad ´ 2, which can be verified much faster. For d ă 536, the numbers cd give a good rational approximation of the last sign change of the function s ÞÑ Hpp

?sq from Theorem 4. These numbers can also be found in the ancillary file cnumbers on the arXiv submission of this paper (arXiv.org:2308.03925)

- 0 2 4 6 8 10
- 1


?sqeπs for d “ 8 (black), d “ 24 (blue) and d “ 48 (red), normalized so Hpp0q “ 1.

Figure 1. This is a plot of the functions s ÞÑ Hpp

Note that if d P t8,24,48u, then cd “ 0, and this shows that even unimodular extremal lattices maximize density for the among all Kd-admissible sphere packings (periodic or

- 0
- 1


0 2 4 6 8 10 Figure 2. This is a plot of the functions s ÞÑ Hpp

?sqeπs for d “ 72 (red) and d “ 80 (blue), normalized so Hpp0q “ 1. For d “ 80, we have multiplied the function by ps ` 1q2 for aesthetic reasons.

not). Since K8 “ K24 “ t1u, the packing problem in these dimensions is unconstrained, and the E8 and Leech lattices are the only extremal lattices in these dimensions, this shows they have maximal density. The above theorem puts the results of [10, 27] in a larger family of packing problems that can be solved by linear programming methods and construction via modular forms. The fact that for d “ 48 we have Hpxq ă 0 for

?

?

?

- 6 ă |x|2 ă 8, allows us to enlarge K48 to ?16pr


10q and deduce Theorem 1. The same enlargement is possible in every dimension d; that is, we could fill Kd between a couple of its points and prove a slightly stronger result. However, for simplicity, we left the statement as it is.

8s Y

6,

One could ask if it is possible to extend Theorems 4 and 5 to all dimensions d ď 163264. For this, one would need to greatly optimize the numerical procedure we explain in the proof of Theorem 4, and use specialized software and several days of running time to increase 1200 to something of the order of 10000. Rough experimental estimations show that the running time we have for the proof of Theorem 4 is roughly Op1.1d{8q-secs, so it seems the complexity of our algorithm is increasing exponentially. Even if one manages to reduce this ratio to (being generous) 1.001, reaching d « 170000 seems unreasonable.

One could also ask if we could prove Theorem 5 with no assumption on the minimal norm on Λ˚. That might be possible, but we believe it to be impossible via the linear programming approach that we use with the same set Kd. The functions H computed in Theorem 4 are in a way unique, and one could actually show they are by extending

the interpolation formulas of [11] to all dimensions multiple of 8. The issue is that the functions Hppxq of Theorem 4 do have a simple zero very near |x|2 “ cd and so have negative values in the region 0 ă |x|2 ă cd. However, it might be possible to remove the condition on Λ˚ by enlarging ld and finding the corresponding ‘magic’ functions. We have tried this approach in small dimensions, replacing ld by ld `δ, for some small even δ ą 0, although unsuccessfully. It might be the case that δ needs to be very large; however, that greatly complicates the modular form constructions. We leave this question for future work. Nevertheless, we expect this δ to exist because when δ “ 8, the only Kd-admissible lattices with minimal norm ?ad are integral even lattices, and such lattices are less dense than extremal ones.

- Conjecture 3. Let Λ Ă Rd be an even unimodular lattice with minimal norm ?a, for some even integer a. Then for some even l ą a, we have that Λ has maximal density


?

?

?a,

among any ?1at

a ` 2,...,

lu-admissible sphere packing; that is,

∆d ˆ

lu˙ “ denspΛq.

?

?

?a,

1

?at

a ` 2,...,

If this conjecture is true in dimension d, then for 2 ď a ď ad, one could define Lpa,dq “ l, where l is the smallest such that Conjecture 3 is true. We already know that Lp2,8q “ 2,Lp4,24q “ 4, and we have shown that, Lp6,48q ď 10. We believe (and it is somewhat believed in the community) that Lp6,48q “ 6 and that extremal lattices maximize density with no constraints in dimension 48. It would be also interesting to find Lp2,16q and Lp2,24q and show that the lattices E82,D16` and all the 24-dimensional Niemeier lattices with root are optimal.

Another curious question is: Is there a finite K such that Z2 is K-admissible and with maximal density?3 If so, how small #K can be?

- 2.1. One-dimensional sphere packings. Unconstrained one-dimensional sphere packings are trivial to construct as unit intervals tile the line. However, finding optimal one-dimensional K-admissible sphere packings for an arbitrary given set K seems to be a difficult question. Here, we are concerned with periodicity: When can we make sure that there exists some optimal one-dimensional packing which is periodic? Unfortunately, greedy choice usually does not give an optimal construction. By greedy choice, we mean


one starts with some configuration YNi“1pai ` Iq for a1 ă a2 ă ... ă aN (with I “ r0,1s) and then takes an interval aN`1 ` I with aN`1 ě 1 ` aN as small as possible so that YNi“`11pai `Iq still is K-admissible. For example, first consider the case where K “ t1,αu for some α ą 2. Then greedy choice gives the packing P where one puts two unit intervals glued together, and then a gap of length α´1, and the repeats this configuration periodically. One can see this is optimal by noting that, in any given K-admissible packing, the 3This problem has a negative answer for dimensions 4 or higher because by the Four Squares Theorem and scale invariance, the checkerboard lattice will always be K-admissible whenever Zd is, but it is a denser lattice.

distance between the centers of any unit interval and the second one after it must be at least 1`α. This means that an interval of size Np1`αq contains at most 2N unit intervals, which shows that ∆1pt1,αuq ď 2{p1 ` αq, and this is attained by P. However, this strategy does not produce the best packing in general. For instance, if K “ t1,α,βu with 2α ě β ą 2α´1 ą α, then greedy choice gives the packing Pβ “ I`p1`βqZ`t0,1u, which has density 2{p1`βq. This is not optimal since Pα “ I `αZ has density 1{α ą 2{p1`βq. In Lemma 15, we completely solve this problem for all choices of α and β.

In Proposition 7, we show that when K is a compact set, then optimal packings for ∆dpKq always exist. However it is not guaranteed that they are periodic, as this is not even known in the unconstrained case. Nevertheless, we expect them to be periodic in the one-dimensional case. The following result proves this in the ‘almost’ finite case.

Theorem 6. Let K Ă r1,8q be a compact set such that 1 P K. Assume that K has no accumulation points from the left and only finitely many accumulation points from the right. Moreover, let K1 be its set of accumulation points and assume that pK1 ` K1q X K1 “ H. Then there exists a K-admissible periodic sphere packing P of R such that denspPq “ ∆1pKq.

In particular, optimal periodic K-admissible packings exist whenever K is finite. However, optimal periodic packings will also exist in the (illustrative) case

?

2,e,πu ` t10´nuně1.

K “ t1,

- Conjecture 4. Let K Ă r1,8q be a compact set such that 1 P K. Then there exists a K-admissible periodic sphere packing of R with maximal density.


A compact set K can be classified by its sequence of derived sets; that is, K,K1,K2,K3,...,

where S1 is the set of points p P S such that pp´ε,p`εqXSztpu ‰ H for any ε ą 0 (the accumulation points of S). Theorem 6 solves the above conjecture for the case K1 “ H (i.e., K is finite) and deals with the case K2 “ H (i.e., K1 is finite) under the condition that points only accumulate from the right and no accumulation point is a sum of two others.

We believe that Conjecture 4 could be very hard to prove, perhaps even false, as this is equivalent to (when suppKq P K) a generalization of Theorem 13 (which is about linear domino tilings) for an infinite compact sets of symbols Σ and domino pieces D Ă Σ˚ˆΣ˚.

3. Generalities

In this section, we establish some basic facts about sphere packing with forbidden distances. Throughout this section, K Ă r1,8q will always be a bounded set such that 1 P K, and the word sphere will be used to denote any x ` 21Bd for some x P Rd.

- Proposition 7. Assume K is compact. Then there exists a packing P P PdpKq such that denspPq “ ∆dpKq.

Proof. The proof is exactly the same as for unconstrained sphere packings [17]. Let pPnqně1 be a maximizing sequence of sphere packings such that denspPnq is increasing and converges to ∆dpKq. By Proposition 8, we can assume that each Pn is knZd periodic for some integer kn ą 0 such that kn Õ 8 and that Pn maximizes the number of spheres one can put inside knQd. Using Hausdorff’s topology for compact sets and a standard Cantor’s diagonal argument, we can assume that pPnqně1 converges locally to some packing P, which is K-admissible since K is compact. By maximality, the number of spheres of Pn inside kmQd must not be much smaller than that of Pm (the error must be bounded by the surface area of the boundary of kmQd). We obtain

volpPnXkmQdq{volpkmQdq ą volpPmXkmQdq{volpkmQdq`Op1{kmq “ denspPmq`Op1{kmq for all n ą m, where Op1{kmq comes from the spheres that touch the boundary of kmQd. Taking n Ñ 8, we obtain volpP X kmQdq{volpkmQdq ě denspPmq ` Op1{kmq. Taking m Ñ 8, we conclude that denspPq ě ∆dpKq, which finishes the proof. □

- Proposition 8. Any K-admissible sphere packing can be approximated by a periodic one.


In particular, if Nt denotes the maximum number of spheres one can put inside tQd such that the configuration is K-admissible, then

Ntvolp12Bdq volptQdq

“ ∆dpKq.

lim

tÑ8

Proof. Let P “ X ` 21Bd be a K-admissible sphere packing. Then Prt “ X X tQd ` pt ` suppKqqZd ` 12Bd is K-admissible, periodic and

volpP X tQdq volptQdq

denspPrtq “

p1 ` Op1{tqq.

- 1

- 2


We obtain limsuptÑ8 denspPrtq “ denspPq. Let δt “ Ntvolp

Bdq

volptQdq . The same periodization argument shows that limsuptÑ8 δt ď ∆dpKq. However, if P “ X `tZd is a K-admissible periodic sphere packing, by maximality, we must have that #pX X tQdq ď Nt; hence,

δt ě denspPq ` Op1{tq,

where Op1{tq accounts for boundary intersections. We obtain liminftÑ8 δt ě ∆dpKq. This finishes the lemma. □

Lemma 9. For any compact K, there is a countable set Kr such that ∆dpKq “ ∆dpKrq. Proof. Since K is compact, there is a packing P “ X ` 21Bd such that denspPq “ ∆dpKq. Since X is countable, we can write X “ tx1,x2,...u. Define the set

K0 “ tα P K : |xi ´ xj| “ α for some i ă ju.

Define Kr :“ K0 Yt1,maxpKqu. Then, Kr Ă K is a countable subset such that maxpKq “ maxpKrq, and by construction, P is Kr-admissible. We have

∆dpKrq ď ∆dpKq “ denspPq ď ∆dpKrq. This concludes the proof. □

Define

ndpKq :“ maxt#X : X Ă Rd and |x ´ y| P K for all x,y P X with x ‰ yu. Since K is bounded, it is clear that X is finite and any maximal set X (which always exist) can be placed inside a sphere of radii suppKq. For instance, if K “ t1u, then ndpKq “ d ` 1, and this is realized by the pd ` 1q-simplex. Let kissd denote the kissing number of Rd-that is, the largest number of equal size spheres that can touch a central sphere with no overlapping. Then it is easy to see that

ndpr1,2sq ě 1 ` kissd.

- Conjecture 5. For all d, we have ndpr1,2sq “ 1 ` kissd.


Trivially, this is attained for d “ 1. It seems to be the case for d “ 2 and unlikely to be false for d “ 3. It turns out that the number ndpKq can be extracted from a constrained packing problem if one sets Kλ “ K Y tλu and sends λ Ñ 8.

Proposition 10. Let K Ă r1,8q be bounded with 1 P K and let Kλ “ K Y tλu. Then

λd∆dpKλq “ ndpKq∆d

lim

λÑ8

dpKq¨∆d

Proof. First, we claim that ∆dpKλq ě n

pβ`λqd , where β “ supK. In order to do that, we will construct a packing Pλ that is Kλ-admissible and show that denspPλq ě n

dpKq¨∆d

pβ`λqd . The packing Pλ will not necessarily have maximal density; however it will have a nice structure which makes it easy to estimate its density. Let Y Ă βBd be a maximal cluster of K-admissible points attaining #Y “ ndpKq. Let PĂλ “ Xλ`β`2λBd be an unconstrained periodic sphere packing (with spheres of diameter β ` λ) such that denspPĂλq ą ∆d ´ ε. Define the packing

Pλ “ Xλ ` Y ` 12Bd We claim Pλ is Kλ admissible. To see this note that if xλ ` y and x1λ ` y1 are two points in Xλ ` Y , then their distance is ě λ if xλ ‰ x1λ. If xλ “ x1λ, then their distance is

- |y ´ y1| P K. We obtain


### #ppXλ ` Y q X tQdqvolp12Bdq volptQdq “ lim

denspPλq “ lim

tÑ8

### #pXλ X pt ´ 2β ´ 1qQdqndpKqvolpβ`2λBdq pβ ` λqdvolptQdq

tÑ8

ndpKqdenspPĂλq pβ ` λqd

ndpKqp∆d ´ εq pβ ` λqd

“

ą

.

Since both PĂλ and Pλ are periodic, equality between limits above is justified. Letting ε Ñ 0 proves our claim.

dpKq¨∆d

Now we claim that ∆dpKλq ď n

λd . Let Y ` 12Bd be a periodic Kλ-admissible sphere packing such that denspYλq ą ∆dpKλq´ε. We can assume that λ ą 2β. Define an equivalence relation in Y by saying that y1 „ y2 if |y1 ´ y2| ď β. This is an equivalence relation since if y1 „ y2 and y2 „ y3 but |y1 ´ y3| ą β, then |y1 ´ y3| ě λ, but triangle inequality shows that |y1 ´ y3| ď 2β ă λ, a contradiction. Let Yr “ try1s,ry2s,...u be these equivalence classes, where the yj’s are representatives of each class. Observe that |yi´yj| ě λ if i ă j, that the set ryjs has only distances in K and is contained in yj`βBd. Thus, #ryjs ď ndpKq. We obtain

### #pY X tQdqvolp21Bdq volptQdq ď limsup

∆dpKλq ´ ε ă lim

tÑ8

volp21BdqřryjsXtQd‰H #ryjs volptQdq ď

tÑ8

#pty1,y2,...u X pt ` 2βqQdqvolpλ2Bdq volptQdq ď

ndpKq λd

limsup

tÑ8

ndpKq λd

∆d. Letting ε Ñ 0 finishes the proof. □

Observe that we have actually proven the stronger result ndpKq ¨ ∆d pβ ` λqd

ndpKq ¨ ∆d λd

ď ∆dpKλq ď

.

In particular, in conjunction with Theorem 3, we have the new linear program to produce upper bounds for kissing numbers.

Corollary 11. Let λ ě 4. Let F : Rd Ñ R be a continuous L1-function such that Fp ě 0 and Fpxq ď 0 if 1 ă |x| ă 2 or if |x| ą λ. Then

Fp0q Fpp0q

p2 ` λqd ∆d

volp12Bdq.

1 ` kissd ď

The structure of the best configuration for d “ 2, K “ r1,2s Y tλu and large λ will look like Figure 3.

As a proof of concept, we now prove that this linear program is sharp for d “ 1. In this case, we have the inequality 3 ď p2 ` λqFp0q{Fpp0q. Define the following symmetric set

ďN

Eλ “

### r3n ´ 1{2,3n ` 1{2s

n“´N

Figure 3. Best configuration for d “ 2 and K “ r1,2s Y t4u.

with N “ tpλ´1q{6u. Then it is easy to see that Fλ “ 1E

(where ‹ is the convolution operator) is positive definite and Fλpxq “ 0 if |x| ą λ or if 1 ă |x| ă 2, since Eλ ` Eλ “ Y2nN“´2Nr3n ´ 1,3n ` 1s. Moreover, Fλp0q{Fpλp0q “ 1{volpEλq “ 1{p1 ` 2Nq „ 3{λ. We conclude that limλÑ8p2 ` λqFλp0q{Fpλp0q “ 3, proving the bound is sharp.

λ‹1E

λ

- 3.1. Proof of Theorem 3. In view of Proposition 8, it suffices to consider just periodic


sphere packings P “ Y `Λ` 12Bd. Assume first F is of Schwartz class. We apply Poisson summation to obtain

2

p#Y qFp0q ě ÿ

ÿ

ÿ

ÿ

p#Y q2Fpp0q volpRd{Λq

1 volpRd{Λq

Fpλ ` y ´ y1q “

e2πiy¨ξ

Fppξq

ě

.

ˇ

ˇ

y,y1PY

ξPΛ˚

yPY

λPΛ

Rearranging terms, we deduce that denspPq ď volp21BdqFp0q{Fpp0q. In the unconstrained packing problem one could now, by a standard convolution approximation argument,

show the same inequality holds when F is only continuous and L1. However, this trick does not work for constrained sphere packings, since convolutions destroy K-admissibility of functions. Instead, we give below a direct proof based on a new trick involving the Fe´jer kernel.

Let A be a full rank matrix such that Λ “ A ¨ Zd and let fΛpxq “ ÿ

Fpx ` λq.

λPΛ

Then we see that fΛ is Λ´periodic, that the summation above converges a.e. and that fΛ P L1pRd{Λq. Note also that

fΛ ˝ Apxq “ ÿ

F ˝ Apx ` kq.

kPZd

Observe that fΛ ˝ A P L1pRd{Zdq and pfΛ ˝ Aq^pαq “ |detpAq|´1Fp ˝ A´Jpαq, where volpRd{Λq “ |detpAq| and we use J for transpose. For N a positive integer, consider the N-th F´ejer kernel

˙e2πiα¨x “ Nd

ˆ

˙2 1|x

ˆ1 ´

źd

dpxq ÿ

źd

sinpπNxjq N sinpπxjq

|αj| N

FNpxq “ 1Q

j|ă1{2

j“1

j“1

αPZd |α|8ăN

Denote by ‹ the convolution operator. It is well known that the FN is an approximate identity, that is, FN ‹ Gpxq Ñ Gpxq as N Ñ 8, for any x and any bounded continuous function G. The nice bit is that if G is Zd-periodic, then convolution simply multiplies Fourier coefficients. Routine computations show that

ˆ1 ´

˙e2πiα¨x,

ÿ

źd

|αj| N

1 volpRd{Λq

Fp ˝ A´Jpαq

pfΛ ˝ Aq ‹ FNpxq “

j“1

αPZd |α|8ăN

### is indeed a trigonometric polynomial. We conclude that

ÿ

p#Y q2

pfΛ ˝ Aq ‹ FNpA´1py ´ y1qq ě

volpRd{ΛqFpp0q

y,y1PY

However, letting m :“ maxy‰y1 |y ´ y1|`suppKq`maxxPRd{Λ |x|, the left-hand side above is equal to

ż

ÿ

FNpxqpfΛ ˝ Aq`

˘

A´1py ´ y1q ´ x

### dx

Qd

y,y1PY

ż

ÿ

1 |detpAq|

FNpA´1xqfΛ py ´ y1 ´ xqdx

“

Rd{Λ

y,y1PY

ż

ÿ

ÿ

1 volpRd{Λq

FNpA´1xqFpy ´ y1 ´ x ` λqdx

ď

Rd{Λ

y,y1PY

λPΛ |λ|ďm

“ ÿ

ÿ

FN ‹ pF ˝ AqpA´1py ´ y1 ` λqq

y,y1PY

λPΛ |λ|ďm

ÝÝÝÑNÑ8 ÿ

ÿ

pF ˝ AqpA´1py ´ y1 ` λqq

y,y1PY

λPΛ |λ|ďm

ÿ

“ ÿ

Fpy ´ y1 ` λq

y,y1PY

λPΛ |λ|ďm

### ď #Y ¨ Fp0q.

The limit above is justified because we have a finite sum. The theorem follows. □

4. One-dimensional packings and dominos

We now focus on the one-dimensional case and we ask for the existence of periodic packings with the maximal density. Let I “ r0,1s be the unit interval. We begin with the observation that we can restrict our attention to packings of the half-line r0,8q only; that is,

dens`pPq,

∆1pKq “ sup

PPP1pKq and PĂr0,8q

where dens`pPq “ limsuptÑ8 volpP Xr0,tsq{t. Indeed, if P Ă p´8,8q is a K-admissible periodic packing, then

denspPq ď maxtdens`pP X R`q,dens`pP X R´qu.

Now note that for any K-admissible packing of r0,8q, we can assume that I starts at 0 and so the packing can be uniquely described as a sequence

w “ a1a2...ak..., where aj P KYpsuppKq,8q represent the distance between consecutive centers of intervals in the packing. From now on, we assume that suppKq P K, and we set N :“ rsuppKqs. Hence, we can always assume that aj P K for all j since otherwise, we can reduce that distance without destroying K-admissibility and obtain a denser packing. For simplicity, we just write P`pKq for K-admissible packings of r0,8q with distances between adjacent centers of intervals drawn from K that start with I touching 0.

A word will be a finite ordered sequence of elements of the alphabet Σ “ K. For instance, w “ a1a2...ak is a word of length #w “ k. It will be useful to consider the empty word, denoted by ∅, which has no elements and has length #∅ “ 0. We can also define the norm of w by

ÿk

|w| “

ai. We denote by Σ˚ the set of all finite words. We will now construct a domino set D by DK :“ ␣pw,w1q P Σ˚ ˆ Σ˚ :#w “ #w1 “ N and any subword s of ww1 satisfies |s| P K Y psuppKq,8q(

i“1

.

Thus, DK Ă Σ˚ ˆ Σ˚. Here, ww1 is the concatenated word. A linear domino tiling from DK is an infinite word

γ “ w1w2w3... where pwi,wi`1q is a domino piece from DK. We let T pDKq be the set of domino tiling built this way. Given a tiling γ P T pDKq, we let

#pw1...wtq |w1....wt|

denspγq “ limsup

.

tÑ8

We say γ is periodic if for some n we have wi`n “ wi for all i. Proposition 12. There is a canonical bijection between P P P`pKq ÞÑ γP P T pDKq. This bijection maps periodic to periodic and satisfies

dens`pPq “ denspγPq.

Proof. Indeed, given a packing P P P`pKq, we can write P as (infinite) sequence a1a2..., with aj P K. We then break this sequence into pieces of the form wm`1 “ amN`1...apm`1qN, for m P Zě0, which are words belonging to Σ˚. By construction, the pairs pwm,wm`1q P DK, and then we can associate P to the tiling w1w2.... P T pKq. Clearly, this map is injective. To show it is surjective, let γ “ w1w2... P T pKq be any tiling. Then, by the choice of N, the packing P whose sequence of distances between consecutive centers is given by the concatenation w1w2w3... belongs to P`pKq, and its image is the tiling γ. This establishes a bijection between P`pKq and T . Moreover, it is easy to check that P is periodic if and only if γP is and that dens`pPq “ denspγPq holds for any packing P P P`pKq. □

In general, we define a linear domino game as a tuple pΣ,Dq, where Σ is a set of symbols and D Ă Σ˚ ˆ Σ˚ are domino pieces, where Σ˚ is the set of all finite words in the alphabet Σ. The set of linear domino tilings T pDq are those infinite words such that γ “ w1w2w3..., where pwi,wi`1q P D for all i. We say that a map f : Σ˚ Ñ R` is a norm function when it satisfies the following properties:

- (a) For any w1,w2,w3 P Σ˚, the function k ě 0 ÞÑ #pw1w

k 2w3q

fpw1w2kw3q is monotone;

- (b) The function k ą 0 ÞÑ #pw

k 2q

fpw2kq is a positive constant;

- (c) For any ϵ ą 0, there is δ ą 0 such that if w1 is a sub-word of w with #w´#w1 ď ϵ, then |fpwq ´ fpw1q| ď δ.


Note that if f is a norm function, then

### #pw2kq ` Op1q fpw2kq ` Op1q

#pw2kq ` Op1q

#pw1w2kw3q fpw1w2kw3q

#w2 fpw2q

“

“

` Op1{kq

“

fpw2q

#w2 #pw2kq ` Op1q

- as k Ñ 8. For a norm function f and a linear domino tiling γ “ w1w2w3... P T pDq, we let


#pw1....wtq fpw1....wtq

densfpγq “ limsup

.

tÑ8

In particular, densfpβββ...q “ f#pββq. This is a generalization of the scenario described before by taking f “ | ¨ | and D “ DK.

Theorem 13. Let Σ be a set of symbols and D Ă Σ˚ ˆ Σ˚ be a finite domino set. Let f : Σ˚ Ñ R` be a norm function. Assume that supγPT pDq densfpγq P p0,8q. Then there exists a periodic linear domino tiling γ P T pDq, with period ď #D, such that

densfpγq “ sup

densfpαq.

αPT pDq

The following corollary is an immediate consequence of the above theorem by using Σ “ K and f “ | ¨ |.

Corollary 14. If K is finite, then there exists a periodic K-admissible sphere packing of R of maximal density.

In order to prove Theorem 13, we need to introduce some terminology. Let V :“ tw P Σ˚ : Dw1 s.t. pw,w1q P D or pw1,wq P Du. We then can define a directed graph by G “ pV,Dq, with vertex set V and directed edges D. From now on, in G, we only consider directed paths (i.e., finite sequences of the form γ “ w1...wm such that pwj,wj`1q P D for any j). We say that the path length of γ is m. We also say that γ is a closed path when pwm,w1q P D and open otherwise. An atom is a simple closed path (closed and with no self-intersections).

Proof of Theorem 13. Since D is finite, then V is finite and the set of atoms A is also finite. First, we claim that for any closed path β “ w1...wm in G, it holds that

#β fpβq

#α fpαq

ď max

.

αPA

The inequality is trivial if β is an atom. Assume by induction the claim is true if the path length of β is ď M. For m “ M ` 1 and β not an atom, then β must have some selfintersection (i.e., there exist 1 ď i ă j ď M ` 1 such that wi “ wj). Let v1 “ w1...wi´1,

- v2 “ wi...wj´1 and v3 “ wj...wM`1. Then v1,v2,v3 P Σ˚, v1v3 and v2 are closed paths in G with path lengths ď M (note that we may have v1 or v3 the empty word, but not both

at the same time). By monotonicity hypothesis and the induction hypothesis, we deduce

#β fpβq

“

#pv1v2v3q fpv1v2v3q

ď max"

#pv1v3q fpv1v3q

,

#v2 fpv2q

* ď max

αPA

#α fpαq as desired. Let now ε ą 0 be sufficiently small and γ “ w1w2w3... P T pDq be such that densfpγq ` ε ą supαPT pDq densfpαq ą ε. Let mn Ò 8 be a sequence such that

densfpγq “ lim

nÑ8

#pw1...wm

nq fpw1...wm

nq

.

Since #D is finite, there exists a word w which appears infinitely many times in the sequence of γ. We may assume such word is w1 since the properties of f imply that

lim

nÑ8

#pw1...wm

nq fpw1...wm

nq

“ lim

nÑ8

#pwi...wm

nq fpwi...wm

nq for any i. For each n, we fix a path γpw

mn,wq in G from wm

n

to w (such a path exists since

- w appears infinitely many times in γ). By removing atoms, we may assume that γpw


mn,wq

mn,wq has path length at most the cardinality of D. Since D is finite, we have just finitely many simple paths γpw

is simple, so that γpw

mn,wq “ Op1q. Let γp˚w

mn,wq, so #γpw

mn,wq be the path γpw

γp˚w

mn,wq “ wm

mn,wq without the endpoints wm

and w, so that γpw

mn,wqw1.

n

n

γp˚w

mn,wq is a closed path. We can now use the properties of f to conclude lim

### Hence, w1...wm

n

γp˚w

mn,wqq fpw1...wm

### #pw1...wm

#pw1...wm

nq fpw1...wm

n

“ lim

“ densfpγq.

γp˚w

mn,wqq

nq

nÑ8

nÑ8

n

1...wmnγp˚wm

n,wqq fpw1...wmnγp˚wm

However, #pw

n,wqq ď maxαPA f#pααq. This concludes the proof. □

Figure 4. A visualization of the graph G for K “ t1,2,βu and 3 ă β ď 4 via higher-dimensional embedding.

The proof of Theorem 13 does not work for an arbitrary compact 1 P K Ă r1,8q since it strongly relied on the fact that the graph G (or the domino set D) was finite, so that any closed path could be decomposed into atoms, and hence, in this case, the atoms control the value ∆1pKq. Nevertheless, our proof describes an algorithm to find optimal

- K-admissible sphere packings in the case K is finite. We now analyse the case when K has 3 elements.


Lemma 15. Let 1 ă α ă β and K “ t1,α,βu with 1 ă α ă β. If β ď 2, the periodic packing 1111... has maximal density. If β ą 2, we have the following cases:

| |conditions on α,β<br><br>|a periodic packing of maximal density|
|---|---|---|
|1|α “ 2 and β ď 3<br><br>|1111...|
|2|α “ 2 and 3 ă β<br><br>|11β11β...|
|3|α ‰ 2 and β ď 1 ` α<br><br>|1α1α...|
|4|α ‰ 2, 1 ` α ă β ď 2α and 2α ď β ` 1|αα... (and 1β1β... if 2α “ β ` 1)<br><br>|
|5<br><br>|α ‰ 2, 1 ` α ă β ď 2α and 2α ą β ` 1<br><br>|1β1β...|
|6|α ‰ 2 and 2α ă β<br><br>|1β1β...|


Proof of Lemma 15. Let P P P`pKq be a K-admissible periodic packing and let γ be its sequence of distances. We have two cases: the one in which β does not appear in γ and the second one in which β appears infinitely many times in γ. In the second case, using the graph language, we break γ into simple closed paths with endpoints β, and we try maximize the density of such paths.

- Case 1. It is trivial.


- Case 2. If β ď 4, in the first case (β does not appear in γ), we must have γ “ 222... whose density is 1/2. In the second case, the densest path is β11, with density 3{p2 ` βq which gives the packing β11β11.... Since 3{p2 ` βq ě 1{2, the result follows. Now, if β ą 4, for the first case, there is no periodic packing, and for the second one, the densest path is again β11.
- Case 3. For the first case, 1α1α... is the densest possibility. For the second, the paths βp1α1qk for k Ñ 8 have increasing density, and they converge to 1α1α..., which is the densest periodic packing in this case.
- Case 4. In this case, the pairs p1,1q and p1,αq cannot be consecutive distances. For the first case, we case the sequence αα... with density 1{α. For the second case, we have the paths βαk for k ě 1 and β1. The densest packing is αα.... If 2α “ β ` 1, then 1β1β... has also maximal density.
- Case 5. By the same arguments as in Case 4, we deduce that the densest packing is 1β1β....
- Case 6. We have to consider just the second case. Since the pairs p1,1q, p1,αq and pα,αq cannot be consecutive distances, the densest path is β1, which provides the packing β1β1.... □


5. Proof of Theorem 6 Let K1 “ tα1,...,αNu the set of limit points of K. We can then write K as follows:

ďN

␣

(

K “ Kp Y

αj ` λjk : k ě 1

,

j“1

where Kp :“ tα1,...,αN,β1,...,βMu, with 1 P Kp, and such that

- (i) αi ` αj R tαr : 1 ď r ď Nu;
- (ii) 0 ă λjk ă 2δ for any j,k, where δ :“ min

1ďiăjďN

|αi ´ αj|;

- (iii) For any fixed j, we have λjk Ó 0 when k Ñ 8;
- (iv) βM “ maxK.


We will show that under such conditions, for every packing P P P`pKq, one can construct another one Pr with dens`pPrq ě dens`pPq and such that the set of distances of Pr lies in a finite set Kr Ă K. Thus, by Lemma 9 and Corollary 14, there exists a K-admissible periodic sphere packing of maximal density.

For γ P K and 1 ď i,r ď N, we set J pγ,αi,rq :“ ts ě 1 : γ ` αi ` λrs P K Y pβM,8qu and M pγ,αi,rq :“ supJ pγ,αi,rq.

Observe that, for fixed i,j, we may have αj ` λjk ` αi “ αw for some w. In this case, the index k with such property is unique because of (ii). Therefore, we may write kpj,iq to

denote precisely this index k, whenever it exists. Observe also that if M pγ,αi,rq “ 8, then γ ` αi is an accumulation point and either γ ` αi “ αw for some w or γ ` αi ě βM.

˘ “ 8 if and only if αj `λjk `αi ě βM. Our first step is to ask how large Mpγ,αi,rq can be when it is finite.

`

αj ` λjk,αi,r

In particular, if k ‰ kpi,jq, then M

- Step 1. We claim that there is C ą 0 such that for all 1 ď i,j,r ď N and k ě 1,

with k ‰ kpi,jq, we have M

`

αj ` λjk,αi,r

˘ ď C whenever it is finite. Indeed, assume by contradiction this does not happen. Then, for each C P Z` there is s “ spCq ě C, k ě 1 (k ‰ kpi,jq) and 1 ď i,j,r ď N such that αj ` λjk ` αi ` λrs P K Y pβM,8q but M

`

αj ` λjk,αi,r

˘ ă 8. Thus, as s Ñ 8, some triple pi,j,rq is repeated infinitely often, and we choose such triple. If k “ kpCq “ Op1q, then for some k0 ‰ kpi,jq, we have that αj `λjk

0

`αi P K YpβM,8q is an accumulation point and M

`

αj ` λjk

0

,αi,r

˘ ă 8. Since k0 ‰ kpi,jq, we have that αj `λjk

0

`αi ě βM, but this is absurd since we would have that M

`

αj ` λjk

0

,αi,r

˘ “ 8, which is not the case. Thus, k “ kpCq is unbounded, and so αj `αi P K YpβM,8q is an accumulation point. Condition (i) implies that αj `αi ě βM, and again we reach a contradiction since this implies that M

`

αj ` λjk,αi,r

˘ “ 8 for all k.

- Step 2. Let C ą 0 be the constant from the previous step. Enlarge C if necessary so that we also have


C ě Mpγ,αi,rq for all γ P Kp and 1 ď i,r ď N such that Mpγ,αi,rq ă 8. Define the set Kr by

ďN

␣

( Ă K.

Kr :“ Kp Y

αj ` λjk; 1 ď k ď C

j“1

Let P “ d1d2d3... P P`pKq be a packing where di P K. By an inductive argument, we will replace di by dri ď di, with dri P Kr, in such a way that Pr “ dr1dr2... P P`pKrq Ă P`pKq. This clearly implies that dens`pPrq ě dens`pPq.

We start with the base case. If d1 P Kr, there is nothing to prove. Assume we have d1 R Kr; hence, d1 R Kp. Therefore, we have d1 “ αi ` λis for some 1 ď i ď N and s ą C. We claim that Mpd2,αi,iq “ 8. Indeed, if it were finite, then Mpd2,αi,iq ď C, and hence, s ď C, a contradiction. Therefore, Mpd2,αi,iq “ 8; hence, d2 ` αi ` λit P K Y pβM,8q for infinitely many indices t. Therefore, we must have d2 ` αi P K Y pβM,8q. We now claim that we can replace d1 “ αi ` λis by dr1 :“ αi. In other words, we must verify that dr1 is compatible with d2,...,d1`rβ

Ms. This is the reason why we considered the more general sets Jpγ,αi,rq with r ‰ i. Since d2 ` αi P K Y pβM,8q, it follows that dr1 is compatible with d2. If αi`d2 ě βM, then αi`d2`...`dw ě βM for any w ě 3; hence, dr1 satisfies all the required compatibility conditions. Assume we have αi ` d2 ă βM. Since αi`d2`λit P KYpβM,8q for infinitely many t, it must be the case in which αi`d2 “ αr for some r. We claim that Mpd3,αr,iq “ 8. Indeed, if it were ă 8, then Mpd3,αr,iq ď C, and, hence s ď C, a contradiction. Therefore, we have αr ` d3 ` λit P K Y pβM,8q for infinitely many t, and hence, αi `d2 `d3 “ αr `d3 P K YpβM,8q which proves dr1 is also compatible with d3. If αr ` d3 ě βM, then we are done. Otherwise, we apply the same

procedure to show that dr1 is compatible with d4, and so on. By repeating this process at most rβMs times, we conclude that, indeed, it is possible to replace d1 by dr1 “ αi.

Assume that we have replaced d1,...,dn by dr1,...,drn P Kr. If dn`1 P Kr, then we are done. If not, we repeat the same procedure as for d1, but now for both the right- and the left-hand side of dn`1. This completes the induction argument. Observe that dn ‰ drn precisely when dn “ αi ` λik, for k ą C, and in this case, we took drn “ αi ă dn. This process does not reduce the density of the packing. □

- Remark 1. The main idea of this proof was to take a packing of maximal density and reduce to the finite case by replacing the distances close enough to an accumulation point by this point. Such technique relies a lot on the structure of the set K (existence of left or right limit points and the arithmetic structure of K1). As the complexity of K grows, such technique becomes very hard to implement. Nevertheless, the above proof gives an algorithm to find the best packing in such a case.


6. Constructions via modular forms

In this section, we present some constructions via modular forms that generalize the ones in [9, 10, 27] to all dimensions divisible by 4.

Throughout the rest of the paper, we will always use z for a variable in the upper-half plane H “ tx ` it : x P R,t ą 0u. We will use the convention q “ e2πiz and r “ eπiz for z P H. We will be handling holomorphic modular forms f : H Ñ C over the principal congruence subgroups

ΓpNq “ tγ P SL2pZq : γ ” Id pmod Nqu

(note Γp1q “ SL2pZq). A holomorphic modular form of weight k for a subgroup Γ ă Γp1q is a holomorphic function f : H Ñ C invariant by the slash operation

˜a b c d

¸

f|kγpzq :“ pcz ` dq´kfˆ

˙ “ fpzq, for all z P H and γ “

az ` b cz ` d

P Γ,

and such that

f|kγpzq “ Op1q as Imz Ñ 8. We denote by MkpΓq for the space of holomorphic modular forms f : H Ñ C of weight k for Γ. We simply write Mk for MkpSL2pZqq. We let

˜1 1 0 1

¸ and S “

˜0 ´1

¸.

T “

1 0

If T2 P Γ, then any f P MkpΓq has a Fourier r-series of the form fpzq “ ÿ

anrn.

ně0

The Eisenstein series E4pzq “ 1 ` 240 ÿ

σ3pnqqn and E6pzq “ 1 ´ 504 ÿ

σ5pnqqn,

ně1

ně1

are classical examples of modular forms in M4 and M6, respectively. It is easy to see that Mk is trivial if k is odd or if k ă 4 is nonzero, while M0 contains only constants. Indeed, a fundamental result is that

à

Mj “ CrE4,E6s. We will also need Ramanujan’s cusp form of weight 12 ∆pzq “

jPZ

E43pzq ´ E62pzq 1728 “ q ź

p1 ´ qnq24 P M12,

ně1

which clearly never vanishes for z P H. We will also need the Jacobi theta functions defined by

Θ00pzq “ ÿ

, Θ10pzq “ ÿ

and Θ01pzq “ ÿ

rpn`1{2q

2

2

2

rn

p´1qnrn

.

nPZ

nPZ

nPZ

We define their fourth powers by U “ Θ400, V “ Θ410 and W “ Θ401. These are modular forms of weight 2 that satisfy the Jacobi identity U “ V ` W

and the transformation laws U|2T “ W, V |2T “ ´V, W|2T “ U, U|2S “ ´U, V |2S “ ´W, W|2S “ ´V.

The functions U,V,W are examples of modular forms of weight 2 for Γp2q. Another fundamental result is that

à

MjpΓp2qq “ CrU,V,Ws.

jPZ

Indeed, MkpΓp2qq, for even k ě 2, coincides with the space of homogeneous polynomials of degree k{2 in any two of the U,V,W. Finally, we let

E2pzq “ 1 ´ 24 ÿ

σ1pnqqn

ně1

be the quasimodular Eisenstein series of weight 2. It satisfies the transformation rules E2pz ` 1q “ E2pzq and E2p´1{zqz´2 “ E2pzq `

6 πiz

.

We define the space of holomorphic quasimodular forms of weight k and depth p over a subgroup Γ by

àp

MkďppΓq “

E2jMk´2jpΓq. (2)

j“0

We again omit Γ when Γ “ SL2pZq. For more details about all these modular forms we recommend [28].

The following proposition is key to build admissible functions for the linear programming bounds we have developed.

Proposition 16. Let Λ Ă R be finite, with 0 P Λ and such that ´1{λ P Λ whenever λ P Λ and λ ‰ 0. Let

ppsq “ ÿ

aλeπisλ

λPΛ

be a trigonometric polynomial. Let ε P t´1,1u, d ě 1 be an integer and f : H Ñ C be analytic. Suppose that

- (a) We have ż 1

0

|fpitq|t´d{2dt ă 8;

- (b) There is δ ą 0 such that for any c ą 0, we have fpzq “ Ocpeπδℑzq

if ℑz ą c ą |ℜz|;

- (c) For all λ P Λzt0u and z P H, we have aλfpz ´ λq “ ´εa´1{λpz{iqd{2´2fp´1{z ` 1{λq;
- (d) For all z P H, we have ÿ


aλfpz ´ λq “ εa0pz{iqd{2´2fp´1{zq.

λPΛ

Then the function

hpsq “ ppsqż 8i

fpzqeπizsdz, defines an analytic function for ℜs ą 0 that extends to an continuous function in ℜs ě 0, and satisfies the identity hpsq

0

ż i

aλfpz ´ λqpeπizs ` εpi{zqd{2eπip´1{zqsqdz ` a0 ż i

“ ÿ

fpzqpeπizs ` εpi{zqd{2eπip´1{zqsqdz.

λ

0

λPΛ λą0

(3)

if ℜs ě 0. In particular, the function Fpxq “ hp|x|2q belongs to L1pRdq X C8pRdq and Fppxq “ εFpxq.

Proof. Conditions (a) and (b) guarantee that hpsq is analytic in the region ℜs ą δ. The analyticity of hpsq for 0 ă ℜs ă 2δ and continuity of hpsq for ℜs “ 0 follows straightforwardly by identity (3) and condition (b). The fact that Fpxq defines a radial

- L1-function and Fppxq “ εFpxq follows by identity (3), condition (a) and the fact that


- x P Rd Ñ peπiz|x|2 ` εpi{zqd{2eπip´1{zq|x|2q is a eigenfunction of the Fourier transform in Rd with eigenvalue ε. It remains to prove identity (3). By analytic continuation (and condition (b)), it is enough to prove it for ℜs ą δ. We then have


aλ ż λ`8i

hpsq “ ÿ

fpz ´ λqeπizsdz

λ

λPΛ

eπizsdz ` a0 ż i

fpz ´ λqeπizsdz ` ż 8i

aλ ż i

` ÿ

“ ÿ

aλfpz ´ λq˘

fpzqeπizsdz

0

i

λ

λPΛ

λPΛ λ‰0

where in the second line above, we applied condition (b) to split the integral from λ to i and i to 8i. We obtain

hpsq

ˆaλ ż i

### fpz ` 1{λqeπizsdz˙

fpz ´ λqeπizsdz ` a´1{λ ż i

“ ÿ

´1{λ

λ

λPΛ λą0

` a0 ż 8i

εpz{iqd{2´2fp´1{zqeπizsdz ` a0 ż i

fpzqeπizsdz

i

0

ż i

“ ÿ

`

˘

aλfpz ´ λqeπizsdz ` a´1{λfp´1{z ` 1{λqeπip´1{zqsz´2

### dz

λ

λPΛ λą0

` a0 ż i

˘

`

εpi{zqd{2eπip´1{zqs ` eπizs

### fpzqdz

0

dz ` a0 ż i

ż i

“ ÿ

˘

˘

`

aλfpz ´ λq`

εpi{zqd{2eπip´1{zqs ` eπizs

eπizs ` εpi{zqd{2eπip´1{zqs

fpzqdz,

0

λ

λPΛ λą0

where in the first equality, we have applied condition (d) and that Λ is closed by λ Ñ ´1{λ, in the second equality, we used the change of variables z Ñ ´1{z, and in the last, we have applied condition (c). □

- Remark 2. It is straightforward to show that if we strengthen condition (a) to ż 1


|fpitq|t´kdt ă 8;

0

for all k ą 0, then BxαF P L1pRdq for all multi-indexes α P Zd`, and since Fp “ εF, we conclude that F is of Schwartz class.

This integral transform was used by Viazovska et al. in [10, 27] for ppsq “ sin2pπs{2q to build the magic functions for the packing problem, and also by Radchenko and Viazovska in [23], for ppsq “ sinpπsq, to construct Fourier interpolation formulae with ?n-nodes.

For our purposes, we wish to investigate the case when ppsq “ sin2pπs{2q. The following lemmas generalize the constructions in [10, 27] to all dimensions multiple of 4.

- Remark 3. To make computations simpler we will, from now on, adopt the nonstandard notation that


fTpzq “ f|kTpzq “ fpz ` 1q and fSpzq “ f|kSpzq “ fp´1{zqz´k,

whenever it can be inferred from the context that f has weight k; that is, f P MkďppΓq, for some Γ, k and p.

- Lemma 17 (Γp2q-construction). Let d ě 4 be an integer divisible by 4. Let l ě d{12 be an even integer and set


k “ 2 ´ d{2 ` 6l and ε “ p´1qd{4`1. Consider the following linear operator 4

L : φ P MkpΓp2qq ÞÑ pφT ` φS ´ φ, rr0sφS, rrsφS,..., rrlsφSq. Then any function in the vector space

1 ∆l{2 kerpLq

Fd,l :“

satisfies all conditions in Proposition 16 for ε, d and ppsq “ sin2pπ2sq. In particular, for any f P Fd,l, we have an associated radial Schwartz function Ff : Rd Ñ C such that Fxf “ εFf and

Ffpxq “ sin2pπ2|x|2qż 8i

2 dz

fpzqeπiz|x|

i if |x|2 ą l.

0

Proof. We will show that all conditions in Proposition 16 are satisfied for ppsq “ sin2pπ2sq. First, observe that if f P Fd,l, then condition (a) in Proposition 16 is equivalent to

ż 8i

|f|kSpzq||z|6l|dz| ă 8. This is true because f “ φ{∆l{2 and

i

φSpzq ∆l{2pzq

z6lf|kS “

,

and so we conclude the Fourier expansion of z6lf|kS starts at r. Condition (b) in Proposition 16 is trivial since f is 2-periodic and has Fourier expansion starting at r´l. A simple computation shows that condition (d) implies (c) under the 2-periodicity of f. Using the modular properties of ∆pzq, we see that condition (d) in Proposition 16 is equivalent to

φ “ φS ` φT,

- 4We recall the bracket notation for the coefficient of a power series: if fpxq “ ř


ně0 anxn, then rxnsf “ an is the coefficient of the term xn.

which holds true. □

- Remark 4. It is worth pointing out that by the fact that (see [13, Remark after Theorem 8.4] and [11, Equation (2.13)])


MkpΓp2qq “ Mk ‘ UMk´2 ‘ V Mk´2 ‘ U2Mk´4 ‘ V 2Mk´4 ‘ UV WMk´6,

routine computations show that the kernel of φ ÞÑ φT ` φS ´ φ in MkpΓp2qq coincides with

pU ´ V qMk´2 ‘ pU2 ´ V 2qMk´4,

which has dimension rk{6s for k ě 6, but is trivial otherwise. One can also show that

dimFd,l “ R

V ´

l 2 ´ Z

^.

d ´ 4 12

k 6

l 2 “

- Lemma 18 (Γp1q-construction). Let d ě 4 be an integer divisible by 4. Let l ě d{12 be an even integer and set


k “ 2 ´ d{2 ` 6l and ε “ p´1qd{4. Consider the following linear operator:

L : ψ P Mkď`22 ÞÑ prq0sψ, rq1sψ,..., rql{2sψq. Then any function in the vector space

1 ∆l{2pz2 kerpLqSq,

Gd,l :“

where z2 kerpLqS :“ tz ÞÑ z2ψ|k`2Spzq : ψ P kerpLqu, satisfies all conditions in Proposition 16 for ε, d and ppsq “ sin2pπ2sq. In particular, for any g P Gd,l, we have an associated radial Schwartz function Gg : Rd Ñ C such that Gxg “ εGg and

Ggpxq “ sin2pπ2|x|2qż 8i

2 dz

gpzqeπiz|x|

i if |x|2 ą l.

0

Proof. We will show that all conditions in Proposition 16 are satisfied for ppsq “ sin2pπ2sq. Conditions (a) and (b) follow in a similar manner as in the proof of Lemma 17. Setting

g “ ψ|kS{∆l{2, condition pcq for g is then equivalent to ψ|kST´1 “ εp´1qd{4ψ|kSTS,

which is true since ψ is 1-periodic, εp´1qd{4 “ 1 and ST´1pSTSq´1 “ T. Condition pdq for g is equivalent to

ψrpzq ´ 21pψrpz ` 1q ` ψrpz ´ 1qq “ ψpzq,

where ψrpzq “ ψ|kSpzq. However, simple computations show that this equation holds true for any function ψ P Mkď`22 using the characterization (2) and the functional equation of E2pzq. □

- Remark 5. It is not hard to show any function g P Gd,l has an q-expansion of the form


ÿ8

anqn,

g “

n“´l{2

where an is a quadratic polynomial in z for n ě 1, but affine for n “ ´l,...,0. The following lemma is reminiscent of the numerical method employed in [10].

- Lemma 19 (Effective tail bounds). Let PpX,Y,Zq and QpX,Y,Zq be homogeneous polynomials of degree k{2 and k ` 2, respectively, where k is even. Let |P| and |Q| denote the homogeneous polynomials derived from P and Q, where each coefficient is replaced by its absolute value. Assume that Q has no power of X larger than 2. Define the following holomorphic modular forms:


φ “ PpU,V,Wq and ψ “ QpE2,E4,E6q.

Let φM and ψM denote the tail of their respective r-series and q-series from the pM `1qterm onward. Let

φS “ PpUS,VS,WSq

and pφSqM be the tail of the r-series of the above function from the rM`1-term Furthermore, letting w “ ´πiz and

w2ψS “ w2QppE2qS,E4,E6q, denote by pw2ψSqM the tail of the q-series above from the qM`1-term. Finally, let RMpp,jq “ ÿ

pn ` 1qpe´πpn´jq and SMpp,jq “ ÿ

pn ` 1qpe´2πpn´jq.

nąM

nąM

Then for j ď M ` 1 , t ě 1, r “ e´πt and q “ r2, we have:

- (1) |φMpitq| ď |P|p8,8,8qRMp3k2´2,jqrj;

- (2) |ψMpitq| ď |Q|p24,240,504qSMp5k`410,jqqj;

- (3) |pφSqMpitq| ď |P|p8,8,8qRMp3k2´2,jqrj;

- (4) |pw2ψSqMpitq| ď 13|Q|p24,240,504q|SMp5k`410,jqqj.


Proof. First we prove (1). Observe that by Jacobi’s four-square theorem, the coefficient of rn in the r-series of each of the functions U,V and W is bounded by 8pn ` 1q2. Also note that whenever we multiply m power series

ř

rn for j “ 1,...,m, the coefficient of rn in the product is bounded by pn ` 1qa

### ně0pn ` 1qa

j

1`...`am`m´1. We deduce that the coefficient of rn in the r-series of φ is bounded by |P|p8,8,8qpn ` 1qp3k´2q{2. Since t ě 1, we have 0 ď r ď e´π. This easily implies item (1). The same argument shows item (3). Essentially the same argument shows item (2) by realizing that the coefficient of qn in

the q-series of each of the functions E2,E4 and E6 are bounded by 24pn`1q2, 240pn`1q4 and 504pn ` 1q6, respectively. We deduce that the coefficient of qn in the q-series of ψ is bounded by |Q|p24,240,504qpn ` 1qa`b`c`k`1, where a ` b ` c is maximal among nonnegative integers a,b and c such that 2a`4b`6c “ k`2 and 0 ď a ď 2. Greedy choice shows that the sum a`b`c is maximized (or bounded by) when pa,b,cq “ p2,pk´2q{4,0q, and thus, the coefficient of qn is bounded by |Q|p24,240,504qpn ` 1qp5k`10q{4. This proves item (2). Finally, item (4) is more nuanced since we have the presence of w. Let

QpX,Y,Zq “ Q0pY,Zq ` XQ1pY,Zq ` X2Q2pY,Zq, so that |Qp24,240,504q| “ |Q0|p240,504q ` 24|Q1|p240,504q ` 242|Q2|p240,504q and w2ψS “ w2Q0pE4,E6q ` pw2E2 ´ 6wqQ1pE4,E6q ` pwE2 ´ 6q2Q2pE4,E6q

“ Qw2 ` p´12Q2E2 ´ 6Q1qw ` 36Q2.

For z “ it and t ě 1, we have π ď w “ πt ď 71r, and we obtain

|pw2ψSqMpitq|

ď p71rq2|Q|p24,240,504qSMp5k`410,j ` 1qqj`1 ` 71rp288|Q2|p240,504q ` 6|Q1|p240,504qqSMp54k,j ` 1{2qqj`1{2 ` 36|Q2|p240,504qSMp5k´410,jqqj

ď pe492π|Q|p24,240,504q ` e7πp288|Q2|p240,504q ` 6|Q1|p240,504qq

` 36|Q2|p240,504qqSMp5k`410,jqqj ă p11|Q0|p240,504q ` 283|Q1|p240,504q ` 7283|Q2|p240,504qqSMp5k`410,jqqj ă 13|Q|p24,240,504qSMp5k`410,jqqj

This proves item (4). □ 7. Proof of Theorem 1 We assume Theorem 4. Let d “ 48 and K “ ?16pr

?

?

?

10uq. Let Λ Ă R48 be an even unimodular extremal lattice. In particular, Λ is self-dual and ℓpΛq “ t

8sYt

6,

?

?

8,...u. It is trivial to see Λ is K-admissible and that

6,

denspΛq “ volpB48qˆ?

˙48 “

p3π{2q24 24! Consider Fpxq “ Hp

6 2

?

6xq, with H as in Theorem 4 for d “ 48. Poisson summation over Λ shows that Hp0q “ Hpp0q ą 0. The properties of H imply that F satisfies all conditions of Theorem 3, and hence,

“ volpB48qˆ?

˙48 .

Fp0q Fpp0q

6 2

denspΛq ď ∆dpKq ď volp12B48q

This shows that equality above is attained and Λ is optimal; that is, ∆dpKq “ denspΛq.

Now we prove uniqueness among all periodic packings. We follow the same strategy

as in [8, Section 8]. Let P “ L ` Y ` 12Bd be an optimal admissible periodic packing for some lattice L and a set of translations Y “ tv1,...,vMu. By Poisson Summation,

2

ÿM

ÿ

ÿM

ÿ

1 |L|

Fppyq

e2πiyv

Fpx ` vj ´ vlq “

,

j

ˇ

ˇ

yPL˚

j“1

xPL

j,l“1

from which we derive

1

|L|Fpp0qM2.

MFp0q ě

?

6L| “ M and that tx ` vj ´ vl : x P L, 1 ď j,l ď Mu is contained in the set of zeros of F. By Theorem

Since P is optimal, we have equality above, from which we derive that |

?

?

?

?

- 4, we deduce that t


10,...u. By [8, Lemma 8.2], we conclude that the subgroup G of R48 generated by the set

6|x ` vj ´ vl| : x P L, 1 ď j,l ď Mu Ă t0,

6,

8,

?

6pL ` Y q is an even integral lattice with minimal norm ě

?

### 6. It also follows that the volume |G| “

?

N, for some integer N, and hence, G has at most one point per unit of volume in R48. However, since |

?

?

?

6

6L| “ M, the packing

6pL ` Y q `

2 Bd has one sphere per unit of volume. Therefore, G has exactly one point per unit volume, which implies that N “ 1, G is unimodular and G “

?

6pL ` Y q. Therefore, G must be an extremal lattice.

This finishes the proof of Theorem 1. □ 8. Proof of Theorem 4

Let 8 ď d ď 1200 be a multiple of 8, a “ ad , l “ ld, c “ cd and K “ Kd “ ?1at

?

?

?a,

lu. In what follows, we set k “ 2 ´ d{2 ` 6l (which is congruent to 2 modulo 4), ε “ ´1,

a ` 2,...,

^,

l 2 ´ Z

d ´ 4 12

b “

w “ ´πiz, r “ eπiz and q “ r2. We will abuse notation and write upzq “ Oprkq if for some C ą 0, we have |upzq| ď C|z|Ce´πkℑz for ℑz ą C.

The assertions below were done with rational arithmetic via PARI/GP [3] computer algebra system. Below, we will make certain claims, and we will indicate precisely how to prove them. This proof is computer assisted; hence, the necessary ancillary files can be found with the arXiv submission of this paper (arXiv:2308.03925).

- Step 1. We apply Lemma 17 and compute a basis for the vector space Fd,l collected as a row vector of functions


rf1,...,fbs “ ∆´l{2rφ1,φ2,...,φbs, where dimFd,l “ b and

Φ “ rφ1,φ2,...,φbs “ Wl`1pMφΘJqJ, Mφ P Qbˆpk{2´lq,

Θ “ rWj´1V k{2´l´jsj“1,...,k{2´l.

We use the symbol J for transpose. Θ is a row vector of basis functions for Mk´2l´2pΓp2qq. It is easy to show that any function in ∆l{2Fd,l must be divisible by Wl`1, and this is the reason why we have isolated it in Φ. To make sure Φ is uniquely defined (and so Mφ) we normalize φj so that

φj “ r2pj´1q ` Opr2bq.

- Step 2. We apply Lemma 18 and then proceed to find a basis rg1,...,gcs “ ∆´l{2rw2pψ1qS,...,w2pψcqSs,

collected as a row vector, for the subspace of functions g P Gd,l, with g “ w2ψS{∆l{2, and such that

rwrjspw2∆´l{2ψSq “ 0 for j P t´l,...,´au. By the choice of l and a, it turns out that c “ b for all cases, we have computed (the proof that these dimensions coincide for all d is lengthy and not worth to include here since we are doing this numerically anyways). Here, we set

Ψ “ rψ1,ψ2,...,ψbs “ pMψEJqJ, Mψ P Qbˆpk`6q{4,

E “ rE2iE4jE6ns2i`4j`6n“k`2

j“0,...,pk`2q{4

.

E is a row vector of size pk ` 6q{4 that contains the basis functions for Mk`2 (for each j “ 0,..,pk ` 2q{4, the tuple pi,nq is given by i “ ppk ` 2q{2 ´ 2jq mod 3 and n “ pk ` 2 ´ 2i ´ 4jq{6). To make sure that Ψ is uniquely defined, we impose that

w2pψjqS “ r2pj´1q ` Opr2bq for j “ 1,...,b.

- Step 3. We now solve a linear system of homogeneous equations and set φ “ VφMφΘJ and ψ “ VψMψEJ,


where Vφ and Vψ are row vectors of size b (the solutions) that enforce the following r-expansion shapes:

lÿ´a

ÿl

pαn ` αn1 wqrn ` Oprl`1q,

´w2ψS ´ φ “

αnrn `

n“0

n“l´a`1

ÿl

pβn ` βn1 wqrn ` Oprl`1q,

´w2ψS ` φ “

n“l´a`1

for some αn,αn1 ,βn,βn1 P Q. Recall that by Remark 5, rw2rjsp´w2ψSq “ 0 for j ď 0. Note also that, by construction, we already have that αn,αn1 ,βn,βn1 vanish for odd n in the range 0 ď n ď l. More precisely, given all the previous constraints, Vφ and Vψ are

solutions of the homogeneous equations

rw0rjsp´w2ψS ` φq “ 0

for j P t0,2,...,l ´ au. It turns out that Vφ and Vψ are uniquely defined modulo scaling. We then define the row vectors

Cφ “ nVφMφ and Cψ “ nVψMψ,

where we choose n P Z so that Cφ and Cψ are vectors of integers where gcdpCφ YCψq “ 1 and the first nonzero coordinate of Cφ is positive. In this way, Cφ and Cψ are uniquely defined. For instance, for d “ 48, we have

Cφ “ 27 ˆ 38 ˆ r29393,117572,307819,511955,539410,362729,152114,36480,3840s Cψ “ r565675,7394933,´38880096,44550063,41316945,´107522880,39169185,

40077567,´32756064,5294597,790075s.

These vectors cannot be simplified much further nor have some easy to guess combinatorial formula since, for instance, the 8th entry of Cψ is divisible by the large prime 4453063 and 7th entry of Cφ is divisible by the prime 4003. Experimentally, large primes are often found in the vectors Cφ and Cψ as dimension grows. A list of all vectors Cφ and Cψ for each dimension d ď 1200 multiple of 8 can be found on the ancillary files in the arXiv submission of this paper (a file named Cvectors).

- Step 4. We use Lemmas 17 and 18 to create a radial Schwartz function H : Rd Ñ R and obtain the integral representations

Hpxq “ sin2pπ2|x|2qż 8

0

´π2t2ψSpitq ´ φpitq ∆l{2pitq

e´πt|x|

2

dt

Hppxq “ sin2pπ2|x|2qż 8

0

´π2t2ψSpitq ` φpitq ∆l{2pitq

e´πt|x|

2

dt, that hold for |x|2 ą l. This shows that

Hpxq “ Hppxq “ 0 for |x|2 P tl ` 2,l ` 4,...u.

However, if we let g “ ´∆´l{2w2ψS and f “ ∆´l{2φ, then, by construction, the rjcoefficient of g ´f is a rational number for j “ ´l,...,´a. Similarly, by construction, the rj-coefficient of g ` f vanishes for j “ ´l,...,´a. A straightforward computation shows also that Hpxq “ Hppxq “ 0 for |x|2 P ta,a ` 2,...u, and the integral representation of Hppxq above converges for |x|2 ą a ´ 2.

- Step 5. From now on, we assume that d ı 16 mod 24. We claim that


- (i) |π2ψpitq| ă ´φSpitq for t ě 1;
- (ii) |π2t2ψSpitq| ă φpitq for t ě 1.


Notice that for |x|2 ą a ´ 2, we have

“ ż 8

dt ` ż 8

Hppxq sin2pπ2|x|2q

´π2t2ψSpitq ` φpitq ∆l{2pitq

´π2ψpitq ´ φSpitq ∆l{2pitq

2{t dt td{2 ą 0,

e´πt|x|

e´π|x|

2

1

1

by conditions (i) and (ii). This implies that Hppxq ě 0 for |x|2 ą a ´ 2 and vanishes exactly at |x|2 P ta,a ` 2,a ` 4,...u if |x|2 ą a ´ 2. Similarly, for |x|2 ą l, we have

dt ` ż 8

“ ż 8

´π2ψpitq ` φSpitq ∆l{2pitq

Hpxq sin2pπ2|x|2q

´π2t2ψSpitq ´ φpitq ∆l{2pitq

2{t dt td{2 ă 0,

e´πt|x|

e´π|x|

2

1

1

and so Hpxq ď 0 for |x|2 ą l and vanishes exactly at |x|2 P tl,l`2,l`4,...u if |x|2 ą l´ε, for some small ε ą 0.

- Step 6. To prove the claims (i) and (ii) in Step 5, we introduce the following notation:


For a given u “ ř

ně0 anpwqrn, we write

ÿN

ÿN

anpwqrn ` rl`10 and puqtrunc “

anpwqrn ´ rl`10.

puqtrunc “

n“0

n“0

Recall from Lemma 19 that RN and SN{2 are the corresponding tail sums. We will choose N ě l ` 10n, with n ě 1, to be the first integer such that the quantity

max"abspCφqΘJ|r“0RNpp3k ´ 2q{2,l ` 10q,13abspCψqEJ|q“0SN{2pp5k ` 10q{4,l{2 ` 5q* is less than 1. Above, abspvq, for a vector v, is simply the same vector with each coordinate replaced by its absolute value. By Lemma 19, this guarantees that

pφqtrunc ď φ ď pφqtrunc, pφSqtrunc ď φS ď pφSqtrunc, pψqtrunc ď ψ ď pψqtrunc, pw2ψSqtrunc ď w2ψS ď pw2ψSqtrunc,

for z “ it, w “ πt and t ě 1. A list of all N’s for each dimension d can be found on the ancillary files in the arXiv version of this paper (a file named Nnumbers). For instance, for d “ 48, we have N “ 130.

To prove that condition (i) is satisfied, first we verify that5

- (I) Cφ ě 0,

since it directly shows that φpitq ą 0 for t ą 0, which implies that (since k{2 is odd) φSpitq ă 0 for t ą 0. Next, we show that6

- (II) pψqtrunc has only nonnegative coefficents in its q-expansion,

which proves that ψpitq ą 0 for t ě 1 and that ´π2ψpitq ă ´φSpitq for t ě 1. Next, we use Sturm’s method (which can be done via exact rational arithmetic evaluations) on the variable r to show that the polynomial

- (III) ´π22pψqtrunc ´ pφSqtrunc ą 0 for 0 ă r ă γ2,


- 5We still do not fully know why this happens, but it is true for every case we have computed. 6Another mystery, but it is true for every case we have computed.


where we use π2 “ rπ10ms10´m for m “ 20,40,...,100 and γ2 “ re´π10m1s10´m1 for m1 “ 2,5,8,11, where we select pm,m1q according to necessity (for large dimensions, more precision is sometimes required). From now on, whenever we apply Sturm’s method in the range 0 ă r ă γ2, we will select γ2 as before. This shows that π2ψpitq ă ´φSpitq for t ě 1, and proves that condition (i) holds.

- Step 7. For condition (ii), we write

pw2ψSqtrunc ` pφqtrunc “ r1,w,w2srP0pe´wq,P1pe´wq,P2pe´wqsJ ´pw2ψSqtrunc ` pφqtrunc “ r1,w,w2srQ0pe´wq,Q1pe´wq,Q2pe´wqsJ,

where the Pi’s and Qi’s are polynomials with integer coefficients and degree at most N. Note that P2pe´wq “ pψqtruncpitq and Q2pe´wq “ ´pψqtruncpitq ´ e´wpl`10q, so ´Q2 and P2 have only positive coefficients. We then set x “ e´w and

w1pxq “

ÿN

n“1

p1 ´ xqn n

and w2pxq “

ÿN

n“1

p1 ´ xqn

n `

p1 ´ xqN`1 pN ` 1qx

,

and note that w1pxq ă w ă w2pxq for 0 ă x ă 1. We then conclude that condition (ii) is implied by the two conditions below:

- (IV) r1,wjpxq,w1pxq2srP0pxq,P1pxq,P2pxqsJ ą 0 for all j P t1,2u and 0 ă x ă γ2;
- (V) r1,wjpxq,w2pxq2srQ0pxq,Q1pxq,Q2pxqsJ ą 0 for all j P t1,2u and 0 ă x ă γ2. Both can now be verified using Sturm’s method.


- Step 8. The proof that Hppxq ą 0 for c ă |x|2 ă a ´ 2 is more involved. Let vpwq “


´w2ψS ` φ and ∆´l{2 “ ř

ně´l δl,nrn. For s “ |x|2 ą a ´ 2, we have Hppxq sin2pπ2|x|2q

“ ż 8

e´πtsdt ` ż 8

vpπtq ∆l{2pitq

´π2ψpitq ´ φSpitq ∆l{2pitq

e´π|x|

2{tt´d{2dt

1

1

vpπtqˆ ÿN

δl,ne´nπt˙e´πtsdt ` ż 8

vpπtqˆ ÿ

δl,ne´nπt˙e´πtsdt

“ ż 8

1

1

nąN

n“´l

` ż 8

´π2ψpitq ´ φSpitq ∆l{2pitq

e´πs{tt´d{2dt.

1

In this way, the last two integrals above converge absolutely for s “ |x|2 ą 0, while the first integral extends to a meromorphic function of s P C with possible poles s “ a ´ 2,a ´ 4,...,2,0. Since Hppxq is entire in the variable s, the above representation now holds in the region ℜs P p0,8qzt2,4,...,,a ´ 2u. In particular, since δl,n ě 0, vpπtq ą 0 and ´π2ψpitq ´ φSpitq ą 0 for t ě 1, we obtain the following inequality in the range s ą 0:

vpπtqˆNÿ´l´2

δl,ne´nπt˙e´πtsdt,

ą żr8

Hppxq sin2pπ2|x|2q

1

n“´l

where by rş

we mean the meromorphic extension of the function defined by this integral. Now let Apwq be such that vpwq ´ Apwq “ Oprlq. Then the right-hand side above is

δl,ne´nπt˙e´πtsdt

pvpπtq ´ ApπtqqˆNÿ´l´2

δl,ne´nπt˙e´πtsdt ` ż 8

ApπtqˆNÿ´l´2

żr8

1

1

n“´l

n“´l

ApπtqˆNÿ´l´2

δl,ne´nπt˙e´πtsdt

ą żr8

1

n“´l

δl,ne´nπt˙e´πtsdt

p´pw2ψSqtruncpitq ` pφqtruncpitq ´ ApπtqqˆNÿ´l´2

` ż 8

1

n“´l

p´pw2ψSqtruncpitq ` pφqtruncpitqqˆNÿ´l´2

δl,ne´nπt˙e´πtsdt,

“ żr8

1

n“´l

for s ą 0. After a change of variables w “ πt, we conclude that

ˆ 2Nÿ´l´2

pmpwqe´mw˙e´wsdw

ą żr8

πHppxq sin2pπ2|x|2q

π

m“´a`2

for s ą 0, where

p´pw2ψSqtruncpitq ` pφqtruncpitqqˆNÿ´l´2

### δl,ne´nπt˙ “:

2Nÿ´l´2

pmpwqe´mw.

m“´a`2

n“´l

Let now M “ tp2N ´ l ´ 2q{2mu with m “ 4,3,2,1,0 (depending on precision). Let

- A1pwq “

Mÿ´1

m“´a`2

pmpwqe´mw ` e´Mww2rw2sppMpwqq

- A2pwq “ ´A1pwq `


2Nÿ´l´2

pmpwqe´mw.

m“´a`2

Let x “ e´w. We then show that

(VI) r1,wjpxq,w2pxq2srrw0sA2,rw1sA2,rw2sA2sJ ą 0 for all j P t1,2u and 0 ă x ă γ2. This proves that

ą żr8

πHppxq sin2pπ2|x|2q

A1pwqe´wsdw. (4) Let now R be the following ‘rationalization’ operator

π

Ppsq “ ÿci,j,nπie´πjsn ÞÑ RpPqpsq :“ ÿ

rci,j,nsn,

where rci,j,n “ minα,βPt1,2utci,j,nπαi γβju and π1,π2,γ1,γ2 are rational approximations of π and γ “ e´π such that

π1 ă π ă π2 and γ1 ă γ ă γ2. Usually these rational approximations are taken to be m-digit truncations (in base 10) from below and above, with m P t10,15,20,...,50u depending on the required precision. Observe now that if ppwq is a quadratic polynomial with coefficients in Qrπs, then we

obtain that eπs ż 8

ppwqe´mwe´swdw

π

“ e´πm ż 8

ppw ` πqe´ps`mqwdw

0

ÿ2

j!rwjspppw ` πqq ps ` mqj`1

“ e´πm

j“0

“ e´πmps ` mq3rw0spppw ` πqq ` ps ` mq2rw1spppw ` πqq ` 2ps ` mqrw2spppw ` πqq

ps ` mq4 ě

Rpe´πmrw1spppw ` πqqq ps ` mq2 `

### Rpe´πmps ` mqrw0spppw ` πqqq ps ` mq2

`

Rp2e´πmps ` mqrw2spppw ` πqqq ps ` mq4 “: Bmrpspsq.

We deduce that (4) is bounded from below by

e´πsˆ Mÿ´1

Bmppmqpsq ` BMpw2rw2sppMpwqqq˙ “: e´πsQpsq,

m“´a`2

where Qpsq is a rational function with rational coefficients. Finally, we write Q “ Qnum{Qden, for polynomials Qnum and Qden and obtain that Hppxq ą 0 for c ă |x|2 ă a´2 holds true if the following condition is satisfied

(VII) Qdenpsqśa{2´1

j“0 ps ´ 2jq´2 has only nonnegative coefficients and Qnumpsq ą 0 for

c ă s ă a ´ 2. This can be checked by Sturm’s method again. Notice that since we have used only strict inequalities, this shows that t|x|2 : Hppxq “ 0 and |x| ą cdu “ tad,ad ` 2,...u.

We then check that conditions (I), (II), (III), (IV), (V), (VI) and (VII) are satisfied using rational arithmetic only, producing in this way a mathematical proof. The necessary algorithm to check this positivity conditions can be found in the ancillary files in the arXiv submission of this paper (a file named Postest; please also read the file Readme).

- Step 9. Finally, for d “ 48, it remains to show the claim that t|x|2 : Hpxq ă 0uXp0,10q “ p6,8q. The method is exactly the same as the one employed on Step 8, except we start from


Hpxq and ´w2ψS ´ φ and show, after essentially the same procedure, that the resulting rational function Qpsq divided by ps ´ 6qps ´ 8q is positive in the interval 0 ă s ă 10.

This finishes the proof of Theorem 4. □

9. Proof of Theorems 2 and 5

Noting that Ad “ p1,suppKdqszKd, we conclude that a packing P is K-admissible if and only if it avoids Ad. Thus, Theorems 2 and 5 are equivalent. The proof of Theorem

- 5 follows directly from Theorem 4. Let P “ Λ ` Y ` 12Bd be a Kd-admissible periodic


?adxq

sphere packing. Poisson summation over Λ ` Y ´ Y with the function Fpxq “ Hp

and H as in Theorem 4 shows that Hp0q#Y ě ÿ

ě Hpp0qad´d{2p#Y q2

ÿ

ÿ

ÿ

2

1 volpRd{Lq

˚

Fpx`y´y1q “

e2πiy¨x

Fppx˚qˇ

,

ˇ

volpRd{Lq

y,y1PY

x˚PL˚

xPL

yPY

hence, denspPq ď volpBdq´?

¯d, which is attained by any even unimodular extremal lattice. Poisson summation implies that equality is attained for a lattice packing (#Y “ 1) if and only if for every v P Λ˚, we have |v|2 P tad,ad ` 2,...u. Then, as in the proof of Theorem 1, one shows that ?adΛ is an even unimodular extremal lattice. □

ad 2

Acknowledgements

The authors thank Jo˜ao P. Ramos, Henry Cohn and Danlyo Radchenko for fruitful discussions on the elaboration of this paper. The first author acknowledges support from the following funding agencies: The Office of Naval Research GRANT14201749 (award number N629092412126), The Serrapilheira Institute (Serra-2211-41824), FAPERJ (E26/200.209/2023) and CNPq (309910/2023-4). The second author acknowledges the support of CNPq (141446/2023-4) and FAPERJ (E-26/202.492/2022) scholarships.

Conflict of interest None. Data availability statement Ancillary files with code and data are available in the

arXiv submission of this paper: arXiv:2308.03925 [math.NT]. References

- [1] L. Bassalygo, G. Cohen and Zemor´ , Codes with forbidden distances, Discrete Mathematics 213 (2000), 3-11.
- [2] L.A. Bassalygo, V.A. Zinoviev, V.V. Zyablov, M.S. Pinsker, G.Sh. Poltyrev, Bounds for codes with unequal protection of two message sets, Problemy Peredachi Informatsii 15 (3) (1979) 40-49.
- [3] C. Batut, K. Belabas, D. Benardi, H. Cohen, and M. Olivier, User’s Guide to PARI-GP, version 2.11.1 (2018).
- [4] A. V. Berdnikov, Estimate for the chromatic number of euclidean space with several forbidden distances, Mathematical Notes 99 (2016), no. 5, 774-778.
- [5] P. Boyvalenkov and D. Cherkashin, The kissing number in 48 dimensions for codes with certain forbidden distances is 52 416 000, Results in Mathematics 8 (2025), no. 3,
- [6] P. Boyvalenkov, D. Cherkashin and P. Dragnev, Universal optimality of T-avoiding spherical codes and designs, arXiv:2501.13906.
- [7] P. Boyvalenkov and P. Dragnev, Energy of codes with forbidden distances in 48 dimensions, arXiv:2412.07577.
- [8] H. Cohn and N. Elkies, New upper bounds on sphere packings I. Ann. of Math. (2) 157 (2003), no. 2, 689–714.
- [9] H. Cohn and F. Gonc¸alves, An optimal uncertainty principle in twelve dimensions via modular forms. Invent. Math. 217 (2019), no. 3, 799–831.
- [10] H. Cohn, A. Kumar, S. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24. Ann. of Math. (2) 185 (2017), no. 3, 1017–1033.


- [11] H. Cohn, A. Kumar, S. Miller, D. Radchenko, and M. Viazovska, Universal optimality of the E8 and Leech lattices and interpolation formulas. Annals of Mathematics (to appear).
- [12] J. H. Conway , N. J. A. Sloane, Sphere Packings, Lattices and Groups, Springer New York, NY, 1999.
- [13] M. Eichler and D. Zagier, The Theory of Jacobi Forms, Progress in Mathematics 55, Birkh¨user Boston, Inc., Boston, MA, 1985.
- [14] H. Enomoto, P. Frankl, N. Ito and K. Nomura, Codes with Given Distances, Graphs and Combinatorics 3 (1987), 25-38.
- [15] A.S. Feigenbaum, P.J. Grabner and D.P. Hardin, Eigenfunctions of the Fourier transform with specified zeros, Mathematical Proceedings of the Cambridge Philosophical Society 171 (2021),

(2), 329-367.

- [16] P. Frankl, Orthogonal vectors in the n-dimensional cube and codes with missing distances, Combinatorica 6 (1986), 279-285.
- [17] H. Groemer, Existenzs¨tze f¨ur Lagerungen im Euklidischen Raum, Math. Z. 81 (1963), 260-278.
- [18] T. C. Hales, A proof of the Kepler conjecture, Annals of Mathematics 162 (3), (2005), 1065-1185.
- [19] P. Jenkins and J. Rouse, Bounds for coefficients of cusp forms and extremal lattices, Bull. London Math. Soc., 43 (2011), no. 5, 927-938.
- [20] C. L. Mallows, A. M. Odlyzko and N.J.A. Sloane, Upper Bounds for Modular Forms, Lattices, and Codes, Journal of Algebra 36 (1975), 68-76.
- [21] E. Naslund, The chromatic number of with multiple forbidden distances, Mathematika 69 (2023), Issue 3, 692-718.
- [22] G. Nebe, A fourth extremal even unimodular lattice of dimension 48, Discrete Math. 331 (2014), 133-136.
- [23] D. Radchenko and M. Viazovska, Fourier interpolation on the real line. Publ.math.IHES 129, 51–81 (2019).
- [24] A. M. Raigorodskii, The Borsuk problem and the chromatic numbers of some metric spaces, Uspekhi Mat. Nauk 56 (2001), no. 1(337), 107-146.
- [25] L. Rolen and I. Wagner, A note on Schwartz functions and modular forms, Archiv der Mathematik, 115 (2020), 35-51.
- [26] R. Scharlau and R. Schulze-Pillot, Extremal Lattices, Algorithmic Algebra and Number Theory (1999), Springer, Berlin, Heidelberg, p 139-170.
- [27] M. Viazovska, The sphere packing problem in dimension 8. Ann. of Math. (2) 185 (2017), no. 3, 991–1015.
- [28] D. Zagier, Elliptic modular forms and their applications, in The 1-2-3 of Modular Forms, Universitext, Springer-Verlag, New York, 2008, pp. 1–103.


The University of Texas at Austin, 2515 Speedway, Austin, TX 78712, USA & IMPA - Instituto de Matematica´ Pura e Aplicada, Rio de Janeiro, 22460-320, Brazil. Email address: felipe.ferreiragoncalves@austin.utexas.edu

IMPA - Instituto de Matematica´ Pura e Aplicada, Rio de Janeiro, 22460-320, Brazil. Email address: guilherme.israel@impa.br

