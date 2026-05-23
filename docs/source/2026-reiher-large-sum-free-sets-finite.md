---
type: source
kind: paper
title: Large sum-free sets in finite vector spaces II
authors: Christian Reiher, Sofia Zotova
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2604.02894v1
source_local: ../raw/2026-reiher-large-sum-free-sets-finite.pdf
topic: general-knowledge
cites:
---

# arXiv:2604.02894v1[math.CO]3Apr2026

## LARGE SUM-FREE SETS IN FINITE VECTOR SPACES II.

CHRISTIAN REIHER AND SOFIA ZOTOVA

Abstract. Answering a question of Leo Versteegen, we prove that for n ě 3 every sum-free set A Ď Fn5 with |A| ě 28 ¨ 5n´3 is either contained in the union of two parallel hyperplanes, or isomorphic to Λ ˆ Fn´3

5 , where Λ Ď F35 denotes a certain sum-free set of size 28 discovered by Vsevolod Lev and Leo Versteegen.

§1 Introduction

A subset A of an abelian group G is called sum-free if there are no solutions of x ` y “ z with x,y,z P A. The study of such sets has a long history, which can be traced back to work of Issai Schur [14] motivated by Fermat’s last theorem.

Given a finite abelian group G we write sf0pGq for the maximum cardinality of a sum-free subset of G. Building on earlier work by many researchers, the determination of this group invariant was completed by Ben Green and Imre Ruzsa [4]. Once sf0pGq is known, one can ask further for a classification of the collection

SFĂ0pGq “ tA Ď G: A is sum-free and |A| “ sf0pGqu of all maximum sum-free sets. The solution of this problem was completed by Balasubramanian, Prakash, and Ramana [1]. The next natural question is to determine the largest possible size sf1pGq of a sum-free set A Ď G that it not contained in any set from SFĂ0pGq.

In an early contribution, Davydov and Tombak [2] solved this problem for binary vector spaces, where it has connections to coding theory. We have sf0pFn2q “ 2n´1 for every n ě 1 and the only maximum sum-free sets are affine hyperplanes not containing the origin. For n ď 3 all sum-free subsets can be covered by such hyperplanes, while for n ě 4 Davydov and Tombak proved sf1pFn2q “ 5 ¨ 2n´4.

For ternary vector spaces, the analogous problem was solved by Vsevolod Lev [9]. The maximum sum-free subsets of Fn3 are again affine hyperplanes not passing through the origin, so they have size 3n´1. In the nontrivial case n ě 3 the main result of [9] states sf1pFn3q “ 5 ¨ 3n´3.

Continuing this line of research, Vsevolod Lev [10], followed by Leo Versteegen [15], initiated the investigation of sf1pFn5q. Perhaps interestingly, for all primes p ě 7 and all dimensions n ě 1

2020 Mathematics Subject Classification. 11B13, 11B30, 11P70. Key words and phrases. sum-free sets, finite vector spaces.

1

the invariant sf1pFnpq has been determined in the meantime (see [13] and the references therein), so p “ 5 is the last open case. It is well known that sf0pFn5q “ 2 ¨ 5n´1 and that the only maximum sum-free subsets of Fn5 are sets of the form H Y p´Hq, where H denotes an affine hyperplane not containing the origin (cf. Fact 2.3). A sum-free set A Ď Fn5 is called normal if it is a subset of such a set. Thus sf1pFn5q is the largest cardinality of a non-normal sum-free subset of Fn5. Since all sum-free subsets of F5 are normal, this invariant is only interesting for n ě 2. Leo Versteegen [15] showed sf1pF25q “ 5 and based on his analysis it is easy to classify all extremal examples.

Theorem 1.1. If a sum-free set A Ď F25 with |A| ě 5 is not normal, then it is isomorphic to one of the two sets displayed in Figure 1.1.

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(a)

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(b)

Figure 1.1. Non-normal sum-free sets of size 5

Here and throughout this work F25 is drawn as a p5 ˆ 5q-grid whose 25 boxes represent the points of F25. For the sake of symmetry, we let the coordinates in F5 run from ´2 to 2, so that the origin p0,0q corresponds to the box in the centre. The five elements of our non-normal

sum-free sets are indicated by circles. Moreover, two subsets of F25 are said to be isomorphic if they agree up to a change of coordinates, i.e., if they are in the same orbit of the natural

action of AutpF25q on the subsets of F25.

For n ě 3 the upper bounds sf1pFn5q ă 1.5 ¨ 5n´1 and then sf1pFn5q ď 6 ¨ 5n´2 were obtained in [10, Theorem 3] and [15, Theorem 1.4], respectively. As to lower bounds, a correspondence between Vsevolod Lev and Leo Versteegen led the latter to the following configuration.

- Definition 1.2. Let Λ Ď F35 be the set Λ “ tp1,0q,p´1,0q,p0,1q,p0,´1qu ˆ F5 ¨Y tp´1,2,0q,p´1,2,1q,


p2,1,1q,p2,1,2q,p1,´2,0q,p1,´2,´1q,p´2,´1,´1q,p´2,´1,´2qu. For n ě 3 a subset of Fn5 isomorphic to Λ ˆ Fn´3

5 is called a VL-set.

Our choice of terminology reflects the coincidental fact that, up to symmetry, Vsevolod Lev and Leo Versteegen have the same initials. It is not difficult to verify that Λ is sum-free, but not normal. The same holds, more generally, for all VL-sets, which proves the lower bound sf1pFn´3

5 q ě 28 ¨ 5n´3. Our main result asserts that this construction is optimal.

- Theorem 1.3. For every n ě 3 we have sf1pFn5q “ 28 ¨ 5n´3. Moreover, every sum-free

set A Ď Fn´3

5 of size |A| ě 28 ¨ 5n´3 is either normal or a VL-set.

§2 Preliminaries

- 2.1. Kneser’s theorem. Given two subsets A and B of an abelian group G we write A ` B “ ta ` b: a P A and b P Bu


for their sum set. So A is sum-free if and only if pA ` Aq X A “ ∅. We need a general lower bound on the cardinalities of such sum sets due to Kneser [7,8]. Its formulation involves the concept of the symmetry set of an arbitrary subset X Ď G, which is defined by

SympXq “ tg P G: g ` X “ Xu. Clearly, this set is a subgroup of G and X is a union of cosets of SympXq.

- Theorem 2.1 (Kneser). If A and B denote two finite nonempty subsets of an abelian group G and K “ SympA ` Bq, then


|A ` B| ě |A ` K| ` |B ` K| ´ |K|.

The right side is clearly a multiple of |K| and, if G is finite, so is |G|. Therefore, Kneser’s theorem immediately implies the following result, which could also be proved in a much more direct manner.

Corollary 2.2. If two subsets A and B of a finite abelian group G satisfy |A| ` |B| ą |G|, then A ` B “ G.

Later on, we shall encounter more substantial applications of Kneser’s theorem. To illustrate the general idea, we quickly derive the well-known formula for sf0pFn5q from this result.

Fact 2.3. If A,B,C Ď Fn5 are three nonempty subsets satisfying pA ` Bq X C “ ∅, then

|A| ` |B| ` |C| ď 6 ¨ 5n´1 .

In particular, we have sf0pFn5q “ 2 ¨ 5n´1 for every natural number n.

Proof. Consider the symmetry set K “ SympA`Bq. This is a linear subspace of Fn5 and A ` B is a union of translates of K. Since A ` B is disjoint to the nonempty set C, the dimension of K can be at most n ´ 1, whence |K| ď 5n´1. Moreover, Kneser’s theorem yields

5n ě |A ` B| ` |C| ě |A ` K| ` |B ` K| ´ |K| ` |C| ě |A| ` |B| ` |C| ´ 5n´1 and the desired upper bound |A| ` |B| ` |C| ď 6 ¨ 5n´1 follows.

In the special case A “ B “ C this tells us |A| ď 2 ¨ 5n´1 for every sum-free subset A Ď Fn5, which proves the upper bound sf0pFn5q ď 2 ¨ 5n´1. In the other direction, for any affine hyperplane H not passing through the origin the sum-free set H Yp´Hq exemplifies the lower

bound sf0pFn5q ě 2 ¨ 5n´1. □

- 2.2. Proof of Theorem 1.1. In this subsection, we classify the maximum non-normal


sum-free subsets of F25. The main step towards this goal is the following lemma of Leo Versteegen [10, Lemma 3.1], which we quote in a coordinate-free way.

- Lemma 2.4. If A Ď F25 is sum-free and |A| ě 5, then at least three elements of A are contained in a line not passing through the origin. □


Proof of Theorem 1.1. Let A Ď F25 be a non-normal sum-free set of size |A| ě 5. By

- Lemma 2.4, we can suppose without loss of generality that p´1,1q,p0,1q,p1,1q P A. These three points are drawn as circles in Figure 2.1a. All their sums, differences, and halves are indicated by crosses, because they cannot belong to the sum-free set A anymore.


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(a)

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(b)

Figure 2.1

Since the set A fails to be normal, it cannot be covered by F5 ˆ t´1,1u and, therefore, one of p˘1,´2q needs to be in A. For reasons of symmetry we can suppose p1,´2q P A. As shown

- in Figure 2.1b, this excludes several further points from A. Altogether, the only points whose status is currently unknown are p´2,1q and p´1,´1q.


Each of them could be in A, but due to p´1,´1q ´ p´2,1q “ p1,´2q they cannot be in A

at the same time. This proves |A| “ 5 and that A is isomorphic to one of the two sets in Figure 1.1. Both of these configurations are indeed sum-free. □

- 2.3. Overview. As the proof of Theorem 1.3 is fairly long, we want to break it into three major steps, that are mostly independent of each other. The central idea is that given a dense


sum-free set A Ď Fn5 and a linear epimorphism φ: Fn5 ÝÑ Fm5 onto a low-dimensional space, the associated function

|A X φ´1pxq| 5n´3

fφA: Fm5 ÝÑ Rě0 , x ÞÝÑ

has non-trivial properties, which can then be used to deduce structural information on A. For instance, we shall see later that if m “ 1, |A| ě 28 ¨ 5n´3, and the support of fφA has size at most three, then A has to be normal (see Lemma 5.5). When m “ 2 some properties such functions fφA need to have are gathered in the following concept (cf. Lemma 5.10).

- Definition 2.5. A function f : F25 ÝÑ Rě0 is said to be fishy if


- (F1) }f}1 ě 28, }f}8 ď 5,
- (F2) there is no X Ď F25 such that fpXq “ ř

PPX fpPq is half of an odd integer,

- (F3) and for all P,Q P F25 and all ε P t´1,1u with fpPq,fpQq,fpP ` εQq ą 0 we have fpPq ` fpQq ` rfpP ` εQqs ď 6.


Here the 1-norm and the infinity norm of f are defined by }f}1 “ ř

PPF25 |fpPq| and }f}8 “ max

(

␣|fpPq|: P P F25

, respectively; since f ě 0, the absolute value signs could be omitted. Three examples of fishy functions relevant to our classification of the extremal configurations (i.e., the VL-sets) are shown in Figure 2.2. Empty boxes in these figures indicate that the corresponding function attains the value 0.

| |2| | | |
|---|---|---|---|---|
| | |5| |2|
| |5| |5| |
|2| |5| | |
| | | |2| |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(a) fα

|1|1|1|1|1|
|---|---|---|---|---|
|1|1|1|1|1|
| |4| |4| |
|1|1|1|1|1|
|1|1|1|1|1|


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(b) fβ

Figure 2.2. Three functions

|1|1| |1|1|
|---|---|---|---|---|
|1| |4| |1|
| |4| |4| |
|1| |4| |1|
|1|1| |1|1|


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(c) fγ

The first major step towards Theorem 1.3 is the following result on fishy functions.

- Proposition 2.6. If f : F25 ÝÑ Rě0 is fishy and }f}8 ą 3, then either the support of f can be covered by three parallel lines or f is, modulo some automorphism of F25, one of the three functions depicted in Figure 2.2. More explicitly, this means that there are an automorphism φ of F25 and a letter τ P tα,β,γu such that f “ fτ ˝ φ.

By means of Kneser’s theorem, this can be shown to have the following consequence on sum-free sets.

- Proposition 2.7. If for some n ě 3 a sum-free set A Ď Fn5 has size |A| ě 28 ¨ 5n´3 and some affine subspace T of Fn5 with codimension 2 satisfies |A X T| ą 3 ¨ 5n´3, then A is normal or a VL-set.


We also need to address certain functions f : F35 ÝÑ Rě0. Prior to stating the relevant result, we introduce further notation and terminology. For every point P “ px,yq P F25 we write

LP “ Lx,y “ ␣px,y,zq: z P F5

(

for its preimage with respect to the projection F35 ÝÑ F25 to the first two coordinates. This is a line in F35 parallel to the third coordinate axis. Given any function f : F35 ÝÑ R we call the function g: F25 ÝÑ R defined by gpPq “ fpLPq the standard projection of f.

Definition 2.8. Consider a function f : F35 ÝÑ Rě0 with support I and standard projection g such that

- (A1) }f}8 ď 1,
- (A2) g is fishy,
- (A3) and if ε P t´1,1u, P,Q P F35, and P ` εQ P I, then fpPq ` fpQq ď 1.

We call f acceptable if in addition there exists a special point P‹ P F25 such that

- (A4) gpP‹q ą 2.8 and gp´P‹q ą 2.5,
- (A5) |LP

‹

X I| “ 3,

- (A6) and for all Q P F25 with gpQq,gpP‹ ` Qq ą 0 and gpQq ` gpP‹ ` Qq ą 2.2 we have


‹`Q X I| “ 3. Here is our main result on acceptable functions.

|LQ X I| ` |LP

- Proposition 2.9. For every acceptable function f : F35 ÝÑ Rě0 there exists a line L Ď F35 such that fpLq ą 3.


Combined with Proposition 2.7 and another application of Kneser’s theorem this will eventually lead us to the following statement.

- Proposition 2.10. Let A Ď Fn5 be a sum-free set of size |A| ě 28¨5n´3, where n ě 3. If there exists an affine subspace T of Fn5 with codimension 2 such that |AXT|`|AXp´Tq| ą 28¨5n´4, then A is normal or a VL-set.


We conclude this section by explaining why this result implies our main theorem.

Proof of Theorem 1.3 assuming Proposition 2.10. We will establish the following statement by induction on n ě 2.

Every sum-free set A Ď Fn5 of size |A| ě 28 ¨ 5n´3 is normal or VL.

The base case, n “ 2, amounts to the fact that every sum-free set A Ď F25 with at least six elements is normal, which is a simple consequence of Theorem 1.1. In the inductive step from n ´ 1 to n we consider any sum-free set A Ď Fn5 of size |A| ě 28 ¨ 5n´3, where n ě 3. Notice that every two-dimensional subspace E ď Fn5 contains 24 nonzero vectors, while each nonzero v P Fn5 is contained in the same number of two-dimensional subspaces E. So because of 0 R A an averaging argument yields a two-dimensional subspace E ď Fn5 such that

|A X E| ě R

V ě R

V “ 6.

24|A| 5n ´ 1

24 ¨ 28 125

By Theorem 1.1 the sum-free subset A X E of E is normal and, hence, there is a onedimensional space L ď E intersecting A in a set of the form A X L “ tv,´vu. We now want to find a hyperplane H such that L ď H ď Fn5 and |A X H| is large. Since all vectors in Fn5 ∖ L are in the same number of such hyperplanes, another averaging argument provides a hyperplane H satisfying

|A X H| ě 2 ` Rp|A| ´ 2qp5n´1 ´ 5q 5n ´ 5

V ě 2 `

p28 ¨ 5n´3 ´ 2q ¨ p5n´1 ´ 5q 5n ą 2 ` 28 ¨ 5n´4 ´

38 25 ą 28 ¨ 5n´4 .

Since the last inequality is strict, the induction hypothesis applied in H shows that A X H is a normal subset of H. This means that there exists an affine hyperplane T in H such that A X H Ď T Y p´Tq. Now T satisfies the hypothesis of Proposition 2.10 and, consequently, A is normal or a VL-set. □

Organisation. We will prove Proposition 2.6 in Section 3 and Proposition 2.9 in Section 4. The derivation of Propositions 2.7 and 2.10 will then be carried out in Section 5. We conclude with some open problems in Section 6.

§3 Fishy functions Throughout this section, which is dedicated to the proof of Proposition 2.6, we denote for

every j P F5 the jth row of F25, i.e., the set F5 ˆ tju by Rj. For reasons that will become apparent later, we require the following observation.

- Lemma 3.1. If I Ď F25 has size at least 9 and the complement of I ´ I contains two linearly independent vectors, then I is contained in the union of three parallel lines.


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(a)

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(b)

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(c)

Figure 3.1 Proof. As the statement is invariant under affine maps, we can assume that p0,1q and p1,0q are not in I ´ I. This means that no two elements of I are horizontally or vertically adjacent. Therefore, each row contains at most two members of I. By the box principle and translation invariance, we can suppose that with the possible exception of R´2 all rows contain exactly two elements of I and that p0,˘1q are in R0 X I. This situation is depicted in Figure 3.1a, where members of I are represented as circles and the crosses indicate boxes that are certainly not in I—because they are neighbours of boxes in I.

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(a)

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(b)

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(c)

Figure 3.2

One of the two non-adjacent members of R1 X I needs to be p0,1q. For R´1 the same argument gives p0,´1q P I and we reach the situation drawn in Figure 3.1b. By symmetry

about the second coordinate axis, we can suppose that the second element of R1 X I is p2,1q (see Figure 3.1c). Next, one of the two non-adjacent elements of R2 XI has to be p1,2q, which brings as into the situation drawn in Figure 3.2a.

If p´2,´2q P I, then I is contained in a union of three translates of xp1,´1qy and we are done (see Figure 3.2b). So suppose p´2,´2q R I from now on, which causes I to be disjoint to the line xp1,1qy. If I fails to be coverable by three translates of this line, then p´1,2q and p2,´1q are in I, and we arrive at the contradiction |I| ď 8 (see Figure 3.2c). □

The four boxes, where the function fα from Figure 2.2a attains the value 2, are on a common line through the origin. In cases where we reach the outcome f – fα of Proposition 2.6, the next lemma will help us to identify these values 2.

- Lemma 3.2. If f denotes a fishy function and a point P P F25 satisfies fpPq,fp2Pq ą 0, then fp´2Pq ` fp´Pq ` fpPq ` fp2Pq ď 8.


Moreover, equality can only hold if fp´2Pq “ fp´Pq “ fpPq “ fp2Pq “ 2.

5 . Four applications of (F3) with ε “ 1 reveal

Proof. Suppose first that fpλPq is positive for every λ P Fˆ

fpPq ` fp2Pq ` fp´2Pq ď 6, fp´Pq ` fp2Pq ` fpPq ď 6, fpPq ` fp´2Pq ` fp´Pq ď 6, fp´Pq ` fp´2Pq ` fp2Pq ď 6.

By adding these estimates and dividing by 3 we obtain fp´2Pq`fp´Pq`fpPq`fp2Pq ď 8. Moreover, if this holds with equality, then the previous four inequalities hold with equality as well and fp´2Pq “ fp´Pq “ fpPq “ fp2Pq “ 2 follows.

If exactly one of fp´Pq, fp´2Pq vanishes, our claim follows from the first or second of the above estimates. In the remaining case, fp´Pq “ fp´2Pq “ 0, we exploit that (F3) implies 2fpPq ` fp2Pq ď 6. □

We call F25 “ tP1,...,P25u a nonincreasing enumeration for a function f : F25 ÝÑ Rě0 if fpP1q ě fpP2q ě ¨¨¨ ě fpP25q.

The two lemmata that follow will allow us to derive upper bounds on }f}1 “ ř25

i“1 fpPiq for certain fishy functions f.

- Lemma 3.3. Let F25 “ tP1,...,P25u be a nonincreasing enumeration for a fishy function f. If the support of f cannot be covered by three parallel lines and f fails to be isomorphic to fα, then


- (i) fpP4q ` fpP5q ď 5,
- (ii) fpP1q ` ¨¨¨ ` fpP5q ď 20,
- (iii) and fpP1q ` ¨¨¨ ` fpP6q ă 22.5.


Proof. It suffices to prove part (i), because then fpP1q ` fpP2q ` fpP3q ď 3}f}8 ď 15 yields (ii). Moreover fpP6q ď fpP5q ď 12

fpP4q ` fpP5q˘ “ 2.5 and (F2) lead to fpP6q ă 2.5, so that (iii) follows as well.

`

Assume for the sake of contradiction that fpP4q`fpP5q ą 5. By (F3) applied to P “ Q “ P4 and ε “ ´1 we have fp0,0q “ 0. Similarly,

if i,j P r5s are distinct, then fpPi ˘ Pjq “ 0. (3.1)

In particular, the set S “ tP1,...,P5u is sum-free. By Lemma 2.4 we can therefore suppose without loss of generality that p´1,1q,p0,1q,p1,1q P S. In Figure 3.3a elements of S are drawn as circles and boxes P satisfying fpPq “ 0 are marked by crosses.

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


(a)

| | | | |ą 0|
|---|---|---|---|---|
| | | |P5| |
| | | | | |
| | | | | |
| | |T| |T|


(b)

| | | | |ą 0|
|---|---|---|---|---|
|T| | |P5|T|
| | | | | |
|T|T| | |T|
|T| |T|T|T|


(c)

Figure 3.3

fpP4q ` fpP5q˘ ą 2.5 and (F3) we have

`

We now start to analyse the set T “ tP1,...,P4u. By fpP4q ě 12

fp2Pq “ 0 for each P P T . (3.2) Thus ´2P P T would imply fpPq “ f

`

2p´2Pq˘ “ 0, which is absurd. This proves

´2P R T whenever P P T . (3.3)

Since the support of f cannot be covered by three rows, we can assume by symmetry that fp2,2q ą 0. This implies p1,1q R T, so that only the possibility p1,1q “ P5 remains.

Thus p´1,1q,p0,1q P T and (3.3) entails p0,´2q,p2,´2q R T. The current situation is shown

- in Figure 3.3b. If one of the seven points p´2,1q,p2,1q,p´2,´1q,p´1,´1q,p2,´1q,p´2,´2q,p1,´2q


belonged to T, then (3.1) would lead to the contradiction fp2,2q “ 0. In Figure 3.3c these seven points are marked by a crossed out T. So there remain only three candidates for the remaining two elements of T.

First Case: p´1,´2q P T

- Due to (3.1) and p´1,´2q ` p1,1q “ p0,´1q we have fp0,´1q “ 0, so T is given by the


circles in Figure 3.4a. The remaining crosses in this figure follow from (3.1) and (3.2). So the two parallel lines xp2,1qy and p1,0q ` xp2,1qy are disjoint to the support of f. Consequently, the support of f can be covered by three parallel lines.

ą 0

P5

(a)

| | | | |ą 0|
|---|---|---|---|---|
| | | |P5| |
| | | | | |
| | | | | |
| | | | | |


(b)

| | | | |2|
|---|---|---|---|---|
| |5|5|2| |
| | | | | |
| |2|5|5| |
|2| | | | |


(c)

Figure 3.4

Second Case: p´1,´2q R T

Now p0,´1q and p1,´1q are the two remaining elements of T (recall Figure 3.3c). As indicated in Figure 3.4b, (3.1) excludes some further points from the support of f. In view of (F3), }f}8 ď 5, and fp2,2q ą 0 we have

fp2,1q ` fp0,´1q ď 5, fp´2,1q ` fp1,´1q ď 5, fp´1,1q ` fp2,´1q ď 5, fp0,1q ` fp´2,´1q ď 5.

Furthermore, Lemma 3.2 reveals

fp1,1q ` fp2,2q ` fp´2,´2q ` fp´1,´1q ď 8. Adding these estimates and taking our knowledge about the support of f into account we infer }f}1 ď 4 ¨ 5 ` 8 “ 28. So equality needs to hold throughout.

In particular, Lemma 3.2 reveals fp1,1q “ fp2,2q “ fp´2,´2q “ fp´1,´1q “ 2. We also know fp2,1q ` fp0,´1q “ 5, whence fp2,1q ` fp0,´1q ` rfp2,2qs “ 7 ą 6. Due to (F3) this yields fp2,1q “ 0 and, hence, fp0,´1q “ 5. Repeating this argument three further times we see that f is the function visualised in Figure 3.4c. Up to an appropriate automorphism of F25 this function agrees with fα (see Figure 2.2a). □

- Lemma 3.4. Given a fishy function f : F25 ÝÑ Rě0 set

S “ ␣

P P F25: fpPq ą 2

(

and T “ ␣

P P F25: fpPq ą 1

(

. If |S| ě 6 and fpTq ą 25, then the support of f is contained in three parallel lines. Proof. Since f is fishy, we have

T X pS ` Sq “ T X pS ´ Sq “ ∅. (3.4) In particular, the set S is sum-free and by Theorem 1.1 it has to be normal. Consequently, we can suppose S Ď R1 Y R´1. The sets

A “ ␣

x P F5: px,1q P S

(

and B “ ␣

x P F5: px,´1q P S

(

satisfy |A| ` |B| “ |S| ě 6 which by Corollary 2.2 implies A ´ B “ pA ´ Aq Y pB ´ Bq “ B ´ A “ F5 . Together with (3.4) this leads to T Ď R1 Y R´1. Now for each x P F5 the estimate ÿ

iPF5

`

fpi,1q ` fpi ´ x,´1q˘ “ fpR1q ` fpR´1q ě fpTq ą 25

leads to some i P F5 such that fpi,1q`fpi´x,´1q ą 5. Because of pi,1q ´ pi ´ x,´1q “ px,2q and (F3) this implies fpx,2q “ 0. As x was arbitrary, this shows that the support of f is disjoint to R2 and, for the same reason, it is disjoint to R´2 as well. In other words, the support of f is contained in the union of the three parallel lines R´1, R0, and R1. □

After these preparations, we can establish Proposition 2.6 under the additional assumption }f}8 ą 4.

- Lemma 3.5. If f is fishy, }f}8 ą 4, and the support of f cannot be covered by three parallel lines, then f is isomorphic to fα, i.e., we have f “ fα ˝ φ for some automorphism φ of F25. Proof. Arguing indirectly we assume that f is a counterexample. Fix a nonincreasing enumeration F25 “ tP1,...,P25u and denote the support of f by I. Without loss of generality we can suppose P1 “ p1,0q. So fp1,0q ą 4, and (F3) implies for every point px,yq P F25 that


if px,yq,px ` 1,yq P I, then fpx,yq ` fpx ` 1,yq ď 1. (3.5)

In particular, we have p0,0q,p2,0q R I. For each row Rj let ϱj “ maxtfpi,jq: i P F5u be the largest value f attains on that row. Using (3.5) one easily checks for every j P F5 that

|if<br><br>|then|
|---|---|
||Rj X I| “ 1<br>|Rj X I| “ 2<br>|Rj X I| “ 3<br>|Rj X I| “ 4<br>|Rj X I| “ 5<br>|fpRjq ď ϱj ď 5, fpRjq ď 2ϱj ď 10, fpRjq ď ϱj ` 1 ď 6, fpRjq ď 2, fpRjq ă 2.5.<br><br>|


Table 1. Upper bounds on fpRjq if fp1,0q ą 4

Notice that for the last row averaging (3.5) over all x P F5 only yields fpRjq ď 2.5, but due to (F2) this cannot hold with equality. In fact, such rows can be ruled out entirely.

- Claim 3.6. There is no row completely contained in I.

Proof. Due to p0,0q R I we have R0 Ę I. So if our claim fails, we can assume, without loss of generality, that R2 Ď I. Because of 2R1 “ R2 and p1,0q ´ R´2 “ R2 we have ϱ1 ă 2.5 as well as ϱ´2 ă 1. So in view of Table 1 we obtain the upper bounds

fpR´2q ă 2.5, fpR1q ă 5, and fpR2q ă 2.5. They lead to the lower bounds

min

␣

- fpR0q,fpR´1q( ě 28 ´ p2.5 ` 10 ` 5 ` 2.5q “ 8

and

- fpR1q ě 28 ´ p2.5 ` 10 ` 10 ` 2.5q “ 3,


which by another application of Table 1 imply |R0 XI| “ |R´1 XI| “ 2 and |R1 XI| P t1,2,3u. But now

23 ă 28 ´ fpR2q ´ fpR´2q ď fpR0q ` fpR´1q ` fpR1q ď maxtfpP1q ` ¨¨¨ ` fpP6q,fpP1q ` ¨¨¨ ` fpP5q ` 1u

contradicts Lemma 3.3. □ Now we will study the subset T “ ␣

Q P F25: fpQq ą 1

(

of I.

- Claim 3.7. We have 18 ` |T| ď fpTq.


Proof. A simple case distinction using (3.5) and Claim 3.6 discloses

fpRjq ` |T X Rj| ď 2 ` fpT X Rjq for every j P F5. Summing this over all five rows we obtain

28 ` |T| ď }f}1 ` |T| ď 10 ` fpTq, and our claim follows. □

- Claim 3.8. We have |T| ě 8 and fpTq ě 26.


Proof. The previous claim and }f}8 ď 5 imply 18 ` |T| ď 5|T|, whence |T| ě 5. This allows us to estimate the sum fpTq more carefully with the help of Lemma 3.3, so that we arrive at

18 ` |T| ď `

fpP1q ` ¨¨¨ ` fpP5q˘ ` p|T| ´ 5qfpP6q ď 20 ` 2.5p|T| ´ 5q,

i.e., |T| ě 7. However, |T| “ 7 would require that we have the equality fpP6q “ 2.5, which contradicts (F2). Finally, |T| ě 8 and Claim 3.7 entail fpTq ě 26. □

Now Lemma 3.4 yields fpP6q ď 2, which enables us to refine our analysis of Claim 3.7 even further. We thereby find

18 ` |T| ď fpTq ď 2 ¨ 5 ` fpP3q ` 5 ` 2p|T| ´ 5q “ 5 ` 2|T| ` fpP3q,

whence fpP3q ě 13 ´ |T|. Since P2 and P3 are in T, they cannot be in R0 simultaneously, so we can assume without loss of generality that

fp0,1q ě 13 ´ |T|. (3.6) We distinguish three cases according to the cardinality of T.

First Case: |T| “ 8

Now (3.6) and }f}8 ď 5 lead to fp0,1q “ fp1,0q “ 5. Consequently, no two boxes in I can be adjacent vertically or horizontally. Moreover, fpTq ď 5 ` 2|T| ` fpP3q “ 26 ă 28 ď fpIq yields |I| ě |T| ` 1 ě 9. So by Lemma 3.1 I can be covered by three parallel lines and we are done.

Second Case: |T| “ 9

This time (3.6) reads fp0,1q ě 4. Recall that we started with fp1,0q ě 4. Owing to (F3) this implies that a box that is vertically or horizontally adjacent to a box in T cannot belong to I. In particular, each column and each row contains at most two boxes from T. Due to |T| “ 9 there are four rows and four columns each of which contain exactly two boxes from T and no further boxes from I. Consequently, all boxes from I ∖ T need to be in the remaining column and in the remaining row, whence |I ∖ T| ď 1. It follows that no two boxes

from I are vertically or horizontally adjacent and Lemma 3.1 tells us again that I can be covered by three parallel lines.

Third Case: |T| ě 10

Since no box horizontally adjacent to a box in T can belong to I, this is only possible if T “ I consists of exactly 10 boxes, two from each row. Moreover, (3.6) yields fp0,1q ě 3. Together with T “ I and (F3) this implies that no two boxes in I can be vertically adjacent, and a final application of Lemma 3.1 shows that I is contained in the union of three parallel lines. □

The next result explains how the function fγ enters our classification.

Lemma 3.9. If f : F25 ÝÑ Rě0 is fishy, 3 ă }f}8 ď 4 and there are at least four points P P F25 with fpPq ě 3, then either the support of f can can be covered by three parallel lines or f is isomorphic to fγ.

Proof. By Lemma 3.3 the set U “ tP P F25: fpPq ě 3u has size at most four, so only the case |U| “ 4 is interesting. Suppose without loss of generality that fp1,0q “ }f}8 ą 3, which entails that p0,0q and p2,0q are not in the support I of f, and p´2,0q R U. Moreover, (F3) implies

fpx,yq ` fpx ` 1,yq ď 2 whenever fpx,yq,fpx ` 1,yq ą 0. (3.7)

- Claim 3.10. No row is completely contained in I.


Proof. Assume for the sake of contradiction that R´2 Ď I. Due to 2R´1 “ R´2, R0´R2 “ R´2, and R´2 `R0 “ R´2 we have U Ď R0 YR1. Since no two boxes in U are horizontally adjacent, we can suppose without loss of generality that U “ tp´1,0q,p1,0q,p´1,1q,p1,1qu.

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


Figure 3.5. Circles indicate boxes Q with fpQq ą 2.5.

As indicated in Figure 3.5, this excludes twelve points from I. Due to }f}8 ď 5, fp2,´2q ą 0, and (F3) we have

fp1,0q ` fp´1,2q ď 5.

Arguing similarly, we also find

fp1,´1q ` fp´1,1q ď 5, fp´1,0q ` fp1,2q ď 5, fp´1,´1q ` fp1,1q ď 5.

Moreover, (3.7) yields fpR´2q ď 5 by averaging. Adding all these estimates, we derive the contradiction 28 ď }f}1 ď 5 ¨ 5 “ 25. □

Assuming from now on that I cannot be covered by three lines, Lemma 3.3 tells us fpPq ď 2 for every P P F25 ∖ U. Now a quick case analysis using (3.7) discloses

fpRjq ď 2|Rj X U| ` 4 (3.8) for every j P F5. Summing this over all j P F5 we infer

28 ď }f}1 ď 2|U| ` 20 “ 28.

Thus (3.8) holds with equality for every j P F5. This requires fpPq “ 4 for every P P U and another application of Lemma 3.3 discloses fpPq ď 1 for all P P F25 ∖ U. Consequently, the five values f attains in each row are, in some order, either

(i) 4, 4, 0, 0, 0, (ii) 4, 1, 1, 0, 0,

(iii) or 1, 1, 1, 1, 0.

|1|1| |1|1|
|---|---|---|---|---|
| | | | | |
| | | |4| |
| | | | | |
| | | | | |


(a)

|1|1| |1|1|
|---|---|---|---|---|
|1| |4| |1|
| | | |4| |
| | | | | |
| | | | | |


(b)

Figure 3.6

|1|1| |1|1|
|---|---|---|---|---|
|1| |4| |1|
| |4| |4| |
|1| |4| |1|
|1|1| |1|1|


(c)

Because of |U| “ 4, the set M of all indices j P F5 such that Rj is of type (iii) satisfies 1 ď |M| ď 3. Together with 0 R M this leads to some j P F5 ∖ M such that 2j P M. We can suppose without loss of generality that j “ 1 has these properties and, moreover, that fp0,2q “ 0. Now the restriction of f to R2 is the function we see in Figure 3.6a.

5 it follows from fp2x,2q ą 0 that fpx,1q ă 2.5. Since R1 is not of type (iii), this leaves only one possibility for the restriction of f to R1, drawn in Figure 3.6b. Using (F3) all but four boxes can now be shown not to be in U and only the possibility

For every x P Fˆ

U “ tp1,0q,p´1,0q,p0,1q,p0,´1qu

remains. It is now clear that f vanishes on the boxes marked by crosses in Figure 3.6c and f “ fγ follows. □

We are now sufficiently prepared for the main result of this section.

Proof of Proposition 2.6. Let f : F25 ÝÑ Rě0 be a fishy function with }f}8 ą 3 whose support I cannot be covered by three parallel lines and which is not isomorphic to fα. We need to show that f is isomorphic either to fβ or to fγ.

Without loss generality we can suppose

fp1,0q ą 3.

We keep more flexibility, however, if we do not confine ourselves to the more restrictive assumption fp1,0q “ }f}8 at this point. Lemma 3.5 discloses

}f}8 ď 4. (3.9)

Now (F3) tells us for every point px,yq P F25 that if px,yq,px ` 1,yq P I, then fpx,yq ` fpx ` 1,yq ď 2, (3.10)

which yields p0,0q,p2,0q R I. Setting ϱj “ maxtfpi,jq: i P F5u for every j P F5 we deduce from (3.9) and (3.10) that

|if|then<br><br>|
|---|---|
||Rj X I| “ 1<br>|Rj X I| “ 2<br>|Rj X I| “ 3<br>|Rj X I| “ 4<br>|Rj X I| “ 5<br>|fpRjq ď ϱj ď 4, fpRjq ď 2ϱj ď 8, fpRjq ď ϱj ` 2 ď 6, fpRjq ď 4, fpRjq ď 5.<br><br>|


Table 2. Upper bounds on fpRjq if fp1,0q ą 3

- Claim 3.11. If Q P F25 satisfies fpQq ą 3, then ´2Q R I.


Proof. It suffices to show p´2,0q R I; assuming contrariwise that fp´2,0q ą 0, we conclude fpx,yq ` fpx ` 2,yq ď 5 for all px,yq P F25 from (F3). Together with (3.10) and Table 2 this shows that if fpRjq ą 5 holds for some row Rj, then |Rj X I| “ 3 and ϱj ą 3. Moreover, even in this case we have fpRjq ď 6.

As our claim holds trivially if f is isomorphic to fγ, Lemma 3.9 tells us that the set

M “ tj P F5: fpRjq ą 5u has size at most three. On the other hand,

28 ď ÿ

fpRjq ď 6|M| ` 5p5 ´ |M|q “ 25 ` |M|

jPF5

implies |M| ě 3. Thus we have equality throughout and the numbers fpR´2q,...,fpR2q are, in some order, 5,5,6,6,6. Both indices j with fpRjq “ 5 satisfy ϱj ă 3 by Lemma 3.9 and, therefore, |Rj X I| P t2,5u. It cannot be the case that |Rj X I| “ 2 holds for both of them, because then every row contains a box P with fpPq ą 2.5, contrary to Lemma 3.3. So we can assume, without loss of generality, that fpR2q “ 5 and R2 Ď I. But now 2R1 “ R2 yields ϱ1 ă 2.5, which requires fpR1q “ 5 and R1 Ď I. Another repetition of this argument, this time using 2R´2 “ R1, yields a contradiction. □

- Claim 3.12. If some row is a subset of I, then f is isomorphic to fβ (see Figure 2.2b).


Proof. Since p0,0q R I, we can suppose, without loss generality, that R2 Ď I, which according to Table 2 implies fpR2q ď 5. Owing to

p1,0q ´ R´2 “ R2 , 2R1 “ R2 , ´2R´1 “ R2 , and Claim 3.11 we have

ϱ´2 ă 2, ϱ1 ă 2.5, and ϱ´1 ď 3, (3.11) whence

fpR´2q ď 5, fpR1q ď 5, and fpR´1q ď 6. Improving the third bound we contend that

fpR´1q ď 5. (3.12) Otherwise, due to ϱ´1 ď 3, Table 2 yields |R´1 X I| “ 2. Writing R´1 X I “ tP,Qu with fpPq ě fpQq we could conclude from 2fpPq ě fpPq ` fpQq ą 5 that fp2Pq “ fpP ` Qq “ 0. Since 2P and P ` Q are distinct points in R´2, this shows |R´2 X I| ď 3, which together with ϱ´2 ă 2 entails fpR´2q ă 4. Thus we get the contradiction

28 ď }f}1 “ fpR´2q ` fpR´1q ` fpR0q ` fpR1q ` fpR2q ă 4 ` 6 ` 8 ` 5 ` 5 “ 28.

Having thereby proved (3.12) we observe that 28 ď }f}1 “ fpR´2q ` fpR´1q ` fpR0q ` fpR1q ` fpR2q ď 5 ` 5 ` 8 ` 5 ` 5 “ 28

holds with equality. So in view of (3.11) and Table 2 the rows R1 and R´2 are also contained in I. Because of 2R´1 “ R´2 this entails ϱ´1 ă 2.5, so that R´1 Ď I holds as well.

Summarising we have Rj Ď I and fpRjq “ 5 for every nonzero j P F5. This equality in Table 2 is only possible if f always attains the value 1 on these four rows. Together with fpR0q “ 8 this shows f “ fβ. □

We can henceforth suppose

Rj Ę I for every j P F5 . (3.13) Concerning the set

S “ ␣

(

Q P F25: fpQq ą 2

this has the following consequence.

- Claim 3.13. We have 8 ` 2|S| ď fpSq. Proof. A quick case analysis based on (3.10) and (3.13) shows


fpRjq ` 2|S X Rj| ď 4 ` fpS X Rjq (3.14) for every j P F5. By summing these five inequalities we obtain

28 ` 2|S| ď }f}1 ` 2|S| ď 20 ` fpSq, which implies our claim. □

In view of }f}8 ď 4 the previous claim implies 8 ` 2|S| ď fpSq ď 4|S|, whence |S| ě 4. In the special case |S| “ 4 we need to have the equality fpP1q “ fpP2q “ fpP3q “ fpP4q “ 4 and Lemma 3.9 implies f – fγ. Assuming from now on that this is not the case, we have |S| ě 5. The case |S| “ 5 itself is impossible, for then Lemma 3.3 and Claim 3.13 would imply the contradiction 18 ď fpSq ď 3 ¨ 4 ` 5 “ 17. More generally, we obtain

8 ` 2|S| ď fpSq ă 4 ` 4 ` fpP3q ` 5 ` 2.5p|S| ´ 5q, whence

15 ´ 2fpP3q ă |S|. (3.15) In particular, we have |S| ě 8. By (F3) the set S is also sum-free and, hence, normal.

First Case: 3 ă fpP3q ď 4

Let L Ď F25 be a line satisfying S Ď L Y p´Lq. The box principle allows us to suppose that the set F “ L X tP1,P2,P3u has at least size 2. The set S1 “ `

S Y p´Sq˘ X L satisfies

|S1| ě 12|S| ě 4. Due to |F| ` |S1| ě 6 and Corollary 2.2 the sets F ` S1 and F ´ S1 are the entire lines L ` L and L ´ L, respectively. As they need to be disjoint to I, we can cover I by three translates of L.

Second Case: fpP3q ď 3

Now (3.15) tells us |S| ě 10. Recall that fpPq ą 2 holds for every P P S. Using (3.10) we infer that S “ I contains exactly two boxes from each row. In particular, the normality of S implies that I consists of two parallel lines. □

We conclude this section with another lemma on fishy functions, that will assist us later when proving Propositions 2.9 and 2.10.

Lemma 3.14. Let f : F25 ÝÑ Rě0 be a fishy function with support I. If }f}8 ď 3, then for every point P P F25 with fpPq ą 2.8 and fp´Pq ą 2.5 there exists a point Q with

Q,P ` Q P I and fpQq ` fpP ` Qq ą 2.2.

Proof. Assume contrariwise that fp1,0q ą 2.8, fp´1,0q ą 2.5, but fpx,yq ` fpx ` 1,yq ď 2.2 for all px,yq P F25 with px,yq,px ` 1,yq P I. Now for every j P F5 we find that

|if|then<br><br>|
|---|---|
||Rj X I| “ 1<br>|Rj X I| “ 2<br>|Rj X I| “ 3<br>|Rj X I| “ 4<br>|Rj X I| “ 5<br>|fpRjq ď 3, fpRjq ď 6, fpRjq ď 5.2, fpRjq ď 4.4, fpRjq ă 5.5.<br><br>|


Table 3. Maximal values for fpRjq

Due to fpR0q ď 6 we can suppose, without loss of generality, that fpR1q ě 14

`}f}1 ´ fpR0q˘ ě 41p28 ´ 6q “ 5.5. By Table 3 this yields |R1 X I| “ 2 and we can assume that

R1 X I “ tp1,1q,p´1,1qu.

The four points Q marked by circles in Figure 3.5 satisfy fpQq ą 2.5. Due to Lemma 3.3 they are the only such points and by (F3) the boxes marked by crosses in Figure 3.5 are not in I—they are sums or differences of boxes marked by circles. This entails fpR´1q ă 5 and fpR2q ă 5, and we reach the contradiction

28 ď }f}1 ă 3 ¨ 6 ` 2 ¨ 5 “ 28. □

§4 Acceptable functions

This entire section deals with the proof of Proposition 2.9. Let f : F35 ÝÑ Rě0 denote an acceptable function with support I, standard projection g, and special point P‹. Assume for the sake of contradiction that fpLq ď 3 holds for every line L Ď F35. When applied to the lines Lx,y this tells us }g}8 ď 3. Since g is fishy, we have gp0,0q ď 2. Thus the special point P‹ cannot be the origin and we can suppose that it is either p1,0q or p´1,0q. We prefer not to commit ourselves to one of these two alternatives, because in this manner we keep the current situation symmetric with respect to the reflection x ÞÝÑ ´x, which offers some advantages.

For each point Q “ px,yq P F25 we set IQ “ Ix,y “ ␣

(

z P F5: px,y,zq P I

.

We will often use that (A1) implies gpQq ď |IQ| for every Q P F25. Similarly, this assumption reveals fpx,y,zq ě gpx,yq´p|Ix,y|´1q whenever z P Ix,y. Since the group of affine permutations of F5 acts transitively on the three-element subsets of F5, we can suppose by (A5) that

“ t´1,0,1u, (4.1) which has the following consequence.

IP

‹

- Claim 4.1. If fpx,y,zq ě 0.2, δ P t´1,1u, and η P t´1,0,1u, then px ` δ,y,z ` ηq R I.

Proof. Write P‹ “ pε,0q with ε P t´1,1u. From (A4) and δεη P t´1,0,1u “ IP

‹

we conclude fpx,y,zq ` fpε,0,δεηq ě 0.2 ` `

gpP‹q ´ 2

˘ ą 1. Due to (A3) applied with δε here in place of ε there it follows that the point

px,y,zq ` δεpε,0,δεηq “ px ` δ,y,z ` ηq is indeed not in I. □

Denoting the support of g by J we can now reformulate (A6) in a more concrete manner.

- Claim 4.2. If px,yq,px`1,yq P J and gpx,yq`gpx`1,yq ą 2.2, then there exists some a P F5 such that


‚ either Ix,y “ tau and Ix`1,y “ ta ´ 2,a ` 2u ‚ or Ix,y “ ta ´ 2,a ` 2u and Ix`1,y “ tau.

Proof. Since P‹ is either p´1,0q or p1,0q, there exists a point Q such that ␣

( “ ␣px,yq,px ` 1,yq(

Q,P‹ ` Q

.

Now (A6) tells us |Ix,y| ` |Ix`1,y| “ 3. As both summands are positive, this means that either we have |Ix,y| “ 1 and |Ix`1,y| “ 2, or it is the other way around. In the first case, we write Ix,y “ tau with an appropriate element a P F5. Owing to gpx ` 1,yq ď 2 we have gpx,yq ą 2.2 ´ 2 “ 0.2 and, therefore, Claim 4.1 implies a ´ 1,a,a ` 1 R Ix`1,y, which in turn leads to Ix`1,y “ ta ´ 2,a ` 2u. The case that |Ix,y| “ 2 and |Ix`1,y| “ 1 is treated similarly. □

These claims lead to a symmetric strengthening of (4.1).

- Claim 4.3. We have I1,0 “ I´1,0 “ t´1,0,1u.

Proof. Owing to (4.1) and |I´P

‹

| ě rgp´P‹qs “ 3 it suffices to show ´2,2 R I´P

‹

. By Lemma 3.14 applied to the fishy function g and to P “ P‹ we find some Q P F25 satisfying Q,P‹ ` Q P J and gpQq ` gpP‹ ` Qq ą 2.2. Due to Claim 4.2 there exists some a P F5 such that

‚ either IQ “ tau and IP

‹`Q “ ta ´ 2,a ` 2u ‚ or IQ “ ta ´ 2,a ` 2u and IP

‹`Q “ tau. In the first case, we have

fpQ,aq ` fpP‹ ` Q,a ¯ 2q ě gpQq ` gpP‹ ` Qq ´ 1 ą 1 for both signs and, therefore, (A3) yields

p´P‹,˘2q “ pQ,aq ´ pP‹ ` Q,a ¯ 2q R I , i.e., ˘2 R I´P

‹

. The second case is analogous. □ Since g fulfills (F3), we have

gpx,yq ` gpx ` 1,yq ď 3 whenever px,yq,px ` 1,yq P J . (4.2)

Moreover, (A4) and (F3) yield p´2,0q,p0,0q,p2,0q R J, whence gpR0q ď 6. Thus the average of gpRjq over all j P F5 ∖ t0u is at least 5.5. The conjunction of our next three claims shows, however, that gpRjq ą 5.5 can only occur for some j ‰ 0, if |Rj X J| “ 3.

- Claim 4.4. If Rj Ď J holds for some j P F5, then gpRjq ă 5.5.


Proof. Assume for the sake of contradiction that R1 Ď J and gpR1q ą 5.5. Without loss of generality we can suppose

gp0,1q ` gp1,1q ą 2.2, (4.3) so that Claim 4.2 gives two possibilities concerning the sets I0,1 and I1,1. By applying a suitable automorphism of F35, which is either of the form px,y,zq ÞÝÑ px,y,z ´ ayq or of the form px,y,zq ÞÝÑ p´x ` y,y,z ´ ayq for some a P F5, we can suppose further that I0,1 “ t0u

and I1,1 “ t´2,2u. Notice that fp0,1,0q,fp1,1,2q,fp1,1,´2q ą 0.2. Thus the boxes of R1 corresponding to x “ 0 and x “ 1 are structured as in Figure 4.1a. Next, Claim 4.1 leads to the seven crosses we see in the squares for x “ ´1 and x “ 2. If for some z P F5 we had fp´2,1,zq ě 0.2, then Claim 4.1 would yield further crosses in those two squares, so that a contradiction to R1 Ď J would arise. This explains the five entries in the square for x “ ´2.

|0 2<br><br>ă 0.2|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>|ą 0.2|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>|
|---|---|---|---|---|---|---|---|---|---|
|ă .| | | | | | | | | |
|ă 0.2| | | |ą 0.2| | | | | |
|ă 0.2| | | | | | | | | |
|ă 0.2| | | | | |ą 0.2| | | |


´2 ´1 0 1 2

(a)

| |´2<br><br>´1<br><br>0<br>1<br>2<br>|ą 0.2|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>|ą 0.2|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>|
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
|ă 0.2| | | |ą 0.2| | | |ă 0.2| |
|ă 0.2| | | | | | | | | |
| | | | | | |ą 0.2| | | |


´2 ´1 0 1 2

(b)

Figure 4.1. Internal structure of R1

So we have gp´2,1q ă 1 and, consequently, gp´1,1q ą gpR1q´gp´2,1q´4 ą 0.5. Without loss of generality we can therefore suppose fp´1,1,2q ą 0.2. As shown in Figure 4.1b, Claim 4.1 yields three further crosses in the left square. Moreover, fp2,1,0q ě 0.2 is impossible, for then Claim 4.1 would lead to the contradiction p´2,1q R J.

Observe that there are only eight boxes in Figure 4.1b without crosses. Because of

p´2,1,´1q ´ p´1,1,´2q “ p´1,0,1q P I property (A3) yields

fp´2,1,´1q ` fp´1,1,´2q ď 1. So altogether we get the contradiction

gpR1q ă 1 ` 4 ` 2 ¨ 0.2 “ 5.4. □ Using (4.2), Claim 4.4, and }g}8 ď 3 we find for every j P F5 that

|if|then|
|---|---|
||Rj X J| “ 1<br><br>|Rj X J| “ 2<br><br>|Rj X J| “ 3<br><br>|Rj X J| “ 4<br><br>|Rj X J| “ 5<br><br><br>|fpRjq ď 3, fpRjq ď 6, fpRjq ď 6, fpRjq ď 6, fpRjq ă 5.5.|


In particular, we have

Table 4. Maximal values for gpRjq

gpRjq ď 6 for every j P F5 . (4.4) We plan to improve the second and fourth row of our table, starting with the easier task.

- Claim 4.5. If j P F5 ∖ t0u and |Rj X J| “ 2, then gpRjq ă 5.5.

Proof. The argument is very similar to the proof of Lemma 3.14. Assume contrariwise that, without loss of generality, |R1 X J| “ 2 but gpRjq ą 5.5. We can suppose further that R1 X J “ tp´1,1q,p1,1qu, so that we again reach Figure 3.5 with the same meaning of circles and crosses. As there, an argument involving Lemma 3.3 discloses gpR2q,gpR´1q ă 5 and we again reach the contradiction 28 ď }g}1 ă 2 ¨ 5 ` 3 ¨ 6 “ 28. □

Rows with exactly four boxes in J are less easy to analyse. It will be convenient from now on to denote by Rj not only the subset F5 ˆ tju of F25 but also the subset F5 ˆ tju ˆF5 of F35.

- Claim 4.6. We have gpRjq ă 5.5 for every j P F5 with |Rj X J| “ 4.


Proof. Suppose for the sake of contradiction that R1 X J “ R1 ∖ tp2,1qu, but gpR1q ą 5.5.

- Due to (4.2) this yields gp´2,1q ` gp´1,1q ą 2.5 and gp0,1q ` gp1,1q ą 2.5. (4.5)


By Claim 4.2 and the first estimate we can suppose that the boxes p´2,1q and p´1,1q are structured as in Figure 4.2a or 4.2b.

| |´2<br><br>´1<br><br>0<br>1<br>2<br>|ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>|ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
|ą 0.5| | | |ą 0.5| | | | |
| | | | | | | | | |
| | |ą 0.5| | | |ą 0.5| | |


´2 ´1 0 1 2

(a)

|ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>| |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | |ą 0.5| | | | | | |
| | | | | | | | | |
|ą 0.5| | | | | | | | |


´2 ´1 0 1 2

(b)

Figure 4.2

In the left case, Claim 4.1 yields the four crosses in the square corresponding to x “ 0. Then, Claim 4.2 and the second estimate in (4.5) give the remaining entries of Figure 4.2a.

- In Figure 4.2b, however, Claim 4.1 only yields three crosses in the middle square and it

remains unclear whether |I0,1| “ 1 or |I0,2| “ 1. Thus we get two subcases and, without loss of generality, one of the two situations shown in Figure 4.3a and 4.3b occurs.

- In Figure 4.3b the four green boxes form a subset A of the line p´2,1,´2q ` xp1,0,2qy


and thus we have fpAq ď 3, which yields the contradiction gpR1q ď fpAq ` 2 ď 5. For

this reason only the two cases depicted in Figure 4.2a or 4.3a are possible. As the automorphism px,y,zq ÞÝÑ p´x ´ y,y,zq exchanges these two cases and preserves our assumptions on the row R0, we can suppose without loss generality that R1 is structured as in Figure 4.2a.

|ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>|ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>| |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | |ą 0.5| | | |ą 0.5| | |
| | | | | | | | | |
|ą 0.5| | | |ą 0.5| | | | |


´2 ´1 0 1 2

(a)

ą 0.5

ą 0.5

- 0
- 1
- 2


- 0
- 1
- 2


- 0
- 1
- 2


- 0
- 1
- 2


ą 0.5

ą 0.5 ą 0.5

´1

´1

´1

´1

´2

´2

´2

´2

ą 0.5

´2

´1

0

1

2

(b)

Figure 4.3

In order to make further progress, we study the entire function f and not just its restriction to R1. The entries in R0 of Figure 4.4 are justified by (A1), (A4), and Claim 4.3. If Q,Q1 P R1 are among the six boxes with fpQq,fpQ1q ą 0.5, then (A3) yields Q ` Q1 R I. This leads to the crosses in R2 of Figure 4.4. The crosses in R´1 are found similarly, using R´1 “ R0 ´ R1.

- 0

1

- 1

2

- 2


- ´1 ´2

- 0
- 1
- 2


´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


- ´2


´2

ą 0.5

ą 0.5

- 0
- 1
- 2


ą 0.5

ą 0.5

´1

- ´1 ´2

- 0
- 1
- 2


´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


- ´2


´2

ą 0.5

ą 0.5

ą 0.5

ą 0.5

ą 0.5

ą 0.5

- ´1 ´2

- 0
- 1
- 2


´1

- 0
- 1
- 2


- ´2


ą 0.5

ą 0.5

- 0
- 1
- 2


- 0
- 1
- 2


- 0
- 1
- 2


- 0
- 1
- 2


´1

´1

´1

´1

´1

´2

´2

´2

´2

´2

´1

0

Figure 4.4

Next, the four green boxes form a subset B of the line p0,1,0q ` xp1,´1,0qy, whence

fpBq ď 3. Due to (4.4) and Figure 4.4 we have

fpR´2 ∖ Bq ď 6, fpR´1 ∖ Bq ď 5, fpR0 ∖ Bq ď 5, and fpR1 ∖ Bq ď 5.

As indicated by different colours, the eight boxes in R2 ∖ B without crosses can be grouped into four pairs whose difference is of the form p˘1,0,˘1q. So Claim 4.1 implies

$

fp´2,2,2q ` fp´1,2,1q ď 1, fp´2,2,´2q ` fp´1,2,´1q ď 1, fp0,2,2q ` fp1,2,1q ď 1, fp0,2,´2q ` fp1,2,´1q ď 1.

’&

(4.6)

’%

The addition of these four estimates yields fpR2 ∖ Bq ď 4 and altogether we obtain

28 ď }f}1 ď fpBq ` ÿ

fpRj ∖ Bq ď 3 ` 6 ` 5 ` 5 ` 5 ` 4 “ 28,

jPF5

which means that equality holds throughout.

In particular, this shows fpPq “ 1 for the fifteen boxes P P pR1 Y R0 Y R´1q ∖ B which are known to satisfy fpPq ą 0, and that we have fpR´2q “ 6. Using R´2 “ R´1`R´1 “ R´1´R1 and (A3) we can now show that, as indicated in Figure 4.5, many boxes are not in R2 X I.

- 0

1

- 1

2

- 2


- ´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


- ´2


´2

- 0
- 1
- 2


1

1

ą 0.5

1

´1

- ´1 ´2

- 0
- 1
- 2


´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


- ´2


´2

1

1

1

1

ą 0.5

1

- ´1 ´2

- 0
- 1
- 2


´1

- 0
- 1
- 2


- ´2


1

1

1

1

´1

1

- ´1 ´2

- 0
- 1
- 2


´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


´2

´1

- 0
- 1
- 2


- ´2


1

1

- 0
- 1
- 2


- 0
- 1
- 2


- 0
- 1
- 2


- 0
- 1
- 2


´2

´1

´1

´1

´1

´2

´2

´2

´2

´1

0

Figure 4.5

There remain ten boxes in R2 without crosses. Similar to (4.6) we can form four pairs of boxes differing by p˘1,0,˘1q. This yields 6 “ fpR´2q ď fp´1,´2,0q ` fp1,´2,0q ` 4, wherefore fp1,´2,0q “ 1. We now obtain the contradiction that the four blue boxes form a subset C of the line p0,´1,0q ` xp1,´1,0qy with fpCq “ 4. □

Let us summarise what we know about the “rich” rows Ry whose index y is in the set Ψ “ ␣

(

5 : gpRyq ą 5.5

y P Fˆ

.

If y P Ψ, then Claims 4.4–4.6 imply |RyXJ| “ 3. Among the three boxes in Ry X J there need to be two horizontally adjacent ones, i.e., there is some x P F5 such that px,yq and px ` 1,yq are in J. By (4.2) we have gpx,yq ` gpx ` 1,yq ď 3 and thus the remaining box px1,yq in Rj X J satisfies gpx1,yq ą 2.5. Combined with gp1,0q ą 2.5 this yields px1 ˘ 1,yq R J, whence x1 “ x ` 2.

- Claim 4.7. If y P Ψ, then 2y R Ψ.


Proof. Assume contrariwise that 1,2 P Ψ. By 1 P Ψ and the above discussion, we can suppose without loss of generality that gp0,1q ą 2.5. As indicated in Figure 4.6a, the fishiness of g implies that sums and differences of p1,0q, p´1,0q, and p0,1q cannot be in J. The boxes p˘2,1q, on the other hand, are in J. Because of p˘2,2q ´ p0,1q “ p˘2,1q P J we need to have gp˘2,2q ă 2.5. Thus the box px,2q P R2 satisfying gpx,2q ą 2.5 can only be p´1,2q or p1,2q, and without loss of generality we can suppose gp1,2q ą 2.5 (see Figure 4.6b).

|ă 2.5| | | |ă 2.5|
|---|---|---|---|---|
|ą 0| |ą 2.5| |ą 0|
| |ą 2.5| |ą 2.5| |
| | | | | |
| | | | | |


| | | |ą 2.5| |
|---|---|---|---|---|
| | |ą 2.5|ď 2| |
| |ą 2.5| |ą 2.5| |
| | |ă 2.5| | |
| | | | | |


(a)

(b)

Figure 4.6

We have now found four boxes Q satisfying gpQq ą 2.5 and by Lemma 3.3 there are no further such boxes. In particular, this proves gp0,´1q ă 2.5 and ´2 R Ψ, i.e.,

gpR´2q ă 5.5. Moreover, p2,´1q “ 2 ¨ p1,2q entails gp2,´1q “ 0. Next, we contend gp´2,1q ` gp´2,´1q ` gp1,0q ď 6.

Due to }g}8 ď 3 this is trivial if one of the summands on the left side vanishes. In the remaining case, we appeal to p´2,1q ` p´2,´1q “ p1,0q and the fact that g is fishy.

Finally, gp´2,1q ` gp2,1q “ gpR1q ´ gp0,1q ą 5.5 ´ 3 ą 2.2 and (A6) imply

gp2,1q ď |I2,1| ď 2. Adding everything, we arrive first at

gpR´1q ` gpR0q ` gpR1q ă 6 ` 3 ` 3 ` 2 ` 2.5 “ 16.5, and then at the contradiction

28 ď }g}1 ă 16.5 ` 6 ` 5.5 “ 28. □

- Claim 4.8. There exists some y P Ψ such that gpR2yq ě 5.


Proof. If Ψ is empty, we get the contradiction 28 ď }g}1 ă 6 ` 4 ¨ 5.5 “ 28. So there is some y P Ψ and, since we are otherwise done, we can assume gpR2yq ă 5. By Claim 4.7 applied to ´2y instead of y we obtain p´2yq R Ψ. But now

gpR´yq “ }g}1 ´ gpR0q ´ gpR´2yq ´ gpRyq ´ gpR2yq ą 28 ´ 6 ´ 5.5 ´ 6 ´ 5 “ 5.5 shows ´y P Ψ and due to

gpR´2yq “ }g}1 ´ gpR0q ´ gpR´yq ´ gpRyq ´ gpR2yq ą 28 ´ 6 ´ 6 ´ 6 ´ 5 “ 5 the desired property is possessed by ´y. □

We proceed with some assumptions that can be made without loss of generality. Owing to

- Claim 4.8 we can suppose gpR1q ą 5.5 and gpR2q ě 5. (4.7)


By Claim 4.7 applied to y “ 1 and y “ ´2 we also have ˘2 R Ψ, i.e.,

maxtgpR2q,gpR´2qu ă 5.5. (4.8) Because of }g}8 ě 28 this implies

gpR´1q ` gpR0q ` gpR1q ą 17. (4.9)

Due to 1 P Ψ we can suppose gp0,1q ą 2.5, which immediately justifies all the big crosses in Figure 4.7 except for the one in p0,´2q. In order to see p0,´2q R J we subtract from (4.9) the upper bounds

gpR0q ď 6, gp´2,1q ` gp2,1q ď 3,

gp´2,´1q ` gp2,´1q ď 3,

the latter two of which follow from (4.2). This yields gp0,1q ` gp0,´1q ą 5 and because of p0,´1q ´ p0,1q “ p0,´2q we have indeed p0,´2q R J.

Having thereby explained the big crosses in Figure 4.7 we take a closer look at the row R1. Due to gp´2,1q ` gp2,1q “ gpR1q ´ gp0,1q ą 5.5 ´ 3 “ 2.5 Claim 4.2 allows us to suppose, without loss of generality, that the internal structure of the boxes p´2,1q and p2,1q is as suggested by Figure 4.7. The seven small crosses in R´1 are then deduced from (A3), using L2,´1 “ L´1,0 ´ L2,1 as well as L´2,´1 “ L1,0 ´ L´2,1.

Notice that (4.9) yields gp´2,´1q ` gp2,´1q ą 17 ´ 6 ´ 6 ´ 3 “ 2, whence p´2,´1,2q, p´2,´1,´2q, and p2,´1,0q are in I. Similarly, if Q, Q1 are two distinct ones among the six boxes of the form p˘2,˘1,zq belonging to I, then (4.9) yields fpQq`fpQ1q ą 17´4¨1´4¨3 “ 1, whence Q ˘ Q1 R I. This argument leads to the remaining small crosses in Figure 4.7. The meaning of the colours is soon going to become clear.

| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |ą 2.5| | |ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>|
| | | | | | | | | |
|ą 0.5| | | | | | | | |
| | | | | | | | | |
| | | | | | | |ą 0.5| |
| | |0 5|´2<br><br>´1<br><br>0<br>1<br>2<br>| |0 5|´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
| | |ą .| | |ą .| | | |
| | |ą 0.5| | |ą 0.5| | | |
| | |ą 0.5| | |ą 0.5| | | |
| | | | | | | | | |
|ą 0|´2<br><br>´1<br><br>0<br>1<br>2<br>| | | | | | |´2<br><br>´1<br><br>0<br>1<br>2<br>|
| | | | | | | | | |
| | | | | | | |ą 0| |
| | | | | | | | | |
|ą 0| | | | | | | | |
| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


- 0

1

- 1

2

- 2


´1

´2

´2

´1

0 Figure 4.7

Roughly speaking, our strategy for concluding the argument is to estimate g on boxes in R2 until we reach a contradiction.

- Claim 4.9. We have gp´1,2q ă 1.5.


Proof. In Figure 4.7 the yellow and orange boxes form subsets A and B of the lines

p0,0,2q ` xp1,´2,0qy and p0,0,´2q ` xp1,´2,0qy,

respectively. This proves fpAq ` fpBq ď 6, which together with ÿ

`

Ry ∖ pA Y Bq˘ ď 3 ` gp2,´2q ` 4 ` 6 ` 4 “ 17 ` gp2,´2q

f

yPF5∖t2u

yields

17 ` gp2,´2q˘ “ 5 ´ gp2,´2q. So if contrary to our claim gp´1,2q ą 1.5 holds, (4.8) entails

gpR2q ´ gp´1,2q ě 28 ´ 6 ´ `

gp2,´2q ě 5 ` gp´1,2q ´ gpR2q ą 5 ` 1.5 ´ 5.5 “ 1,

whence gp1,0q`gp´1,2q`rgp2,´2qs ą 2.5`1.5`2 “ 6. But due to p1,0q´p´1,2q “ p2,´2q this contradicts (F3). □

Next we study the ‘right half’ of R2.

- Claim 4.10. We have gp1,2q ` gp2,2q ă 2.5.


Proof. By subtracting gpR´1q ` gpR0q ` gp´2,1q ď 6 ` 6 ` 1 “ 13 from (4.9) we obtain gp0,1q ` gp2,1q ą 4. Since g is fishy, this implies gp2,2q ď 1. Assuming from now on that the claim fails, (A6) tells us |I2,2| “ 1 and |I1,2| “ 2.

| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |0 5<br><br>ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| |´2<br><br>´1<br><br>0<br>1<br>2<br>|
|---|---|---|---|---|---|---|---|---|---|
| | | | | | |ą .| | | |
| | | | | | | | | | |
| | | | | | | | |ą 0.5| |
| | | | | | | | | | |
| |´2<br><br>´1<br><br>0<br>1<br>2<br>| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br><br><br>|
| | | | | | | | | | |
|ą 0.5| | | |ą 0.5| | | | | |
| | | | |ą 0.5| | | | | |
| | | | |ą 0.5| | | |ą 0.5| |
| | |0 5|´2<br><br>´1<br><br>0<br>1<br>2<br>| | |0 5|´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
| | |ą .| | | |ą .| | | |
| | |ą 0.5| | | |ą 0.5| | | |
| | |ą 0.5| | | |ą 0.5| | | |
| | | | | | | | | | |
| |´2<br><br>´1<br><br>0<br>1<br>2<br>| | | | | | | |´2<br><br>´1<br><br>0<br>1<br>2<br>|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


2

1

0

´1

´2

´2

´1

0

1

2

Figure 4.8

Because of 0 R I1,2 Claim 4.2 implies that the unique element of I2,2 cannot be `2 or ´2. Suppose next that I2,2 “ t0u, which by Claim 4.2 implies I1,2 “ t´2,2u. Together with

p1,2,2q ` p1,2,´2q “ p2,´1,0q P I

and (A3) this leads to the contradiction gp1,2q “ fp1,2,2q ` fp1,2,´2q ď 1.

Without loss of generality it remains to discuss the case I2,2 “ t´1u, whence I1,2 “ t1,2u. By the failure of our claim the three boxes P P pL1,2 Y L2,2q X I satisfy fpPq ą 0.5 (see Figure 4.8). Using L2,2 ´ L2,1 “ L0,1 and (A3) we infer I0,1 Ď t´2,´1,0u, which together with gp0,1q ą 2.5 entails fp0,1,zq ą 0.5 for all z P t´2,´1,0u. Now p2,´2q R J follows from L2,´2 “ L2,2 ` L0,1 “ L´1,0 ´ L2,2 and (A3). Moreover, p1,´2,2q “ p0,1,0q ` p1,2,2q cannot be in I. This explains the new crosses in R´2 we drew in Figure 4.8.

Because of (4.2) they lead to gpR´2q ď 4, which combined with (4.4) and (4.8) gives the contradiction

28 ď }g}1 ă 4 ` 6 ` 6 ` 6 ` 5.5 “ 27.5. □

We are now ready to complete the proof of Proposition 2.10. By (4.7) and Claim 4.10 we have gp´2,2q ` gp´1,2q ą 2.5. Together with Claim 4.9 this proves gp´2,2q ą 1. We also have gp´1,2q ą 0, because gp´2,2q ą 2.5 and gp0,1q implied gp´2,1q “ 0, which would contradict fp´2,1,0q ą 0.

| |´2<br><br>´1<br><br>0<br>1<br>2<br>|ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
|ą 0.5| | | | | | | | | |
|ą 0.5| | | | | | | | | |
| | | | | | | | | | |
| |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |0 5<br><br>ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>| | |ą 0.5|´2<br><br>´1<br><br>0<br>1<br>2<br>|
| | | | |ą .| | | | | |
|ą 0.5| | | | | | | | | |
| | | | | | | | | | |
| | | | |ą 0.5| | | |ą 0.5| |
| | |0 5|´2<br><br>´1<br><br>0<br>1<br>2<br>| | |0 5|´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
| | |ą .| | | |ą .| | | |
| | |ą 0.5| | | |ą 0.5| | | |
| | |ą 0.5| | | |ą 0.5| | | |
| | | | | | | | | | |
| |´2<br><br>´1<br><br>0<br>1<br>2<br>| | | | | | | |´2<br><br>´1<br><br>0<br>1<br>2<br>|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | | |´2<br><br>´1<br><br>0<br>1<br>2<br>| | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


- 0

1

- 1

2

- 2


´1

´2

´2

´1

0 Figure 4.9

Now (A6) tells us |I´2,2| “ 2 and |I´1,2| “ 1. By Claim 4.2 we can suppose, without loss of generality, that I´1,2 “ t2u and I´2,2 “ t´1,0u. Using L0,1 “ L´2,2 ´ L´2,1 we find L0,1 “ t´2,1,2u. The current situation is drawn in Figure 4.9. Its four green boxes form a subset D of the line p0,1,2q`xp1,´1,1qy. So we have fpDq ď 3. It is plain that fpRy∖Dq ď 5

holds for y P t´1,0,1u. Moreover, Claim 4.10 and (4.8) show fpR2 ∖ Dq ă 2 ` 2.5 “ 4.5 and fpR´2 ∖ Dq ă 5.5, respectively. So altogether the contradiction

28 ď fpDq ` ÿ

fpRy ∖ Dq ă 3 ` 5.5 ` 3 ¨ 5 ` 4.5 “ 28

yPF5

arises and Proposition 2.10 is proved. §5 Applications of Kneser’s theorem

- 5.1. Hyperplanes. In this subsection we study dense sum-free sets contained in the union of a small number of parallel hyperplanes.


- Lemma 5.1. If for some n ě 2 a sum-free set A Ď Fn5 of size |A| ą 5n´1 can be covered by two parallel hyperplanes, then it is normal.

Proof. Suppose that for some hyperplane H ď Fn5, vector v P Fn5 ∖ H, and scalars λ,µ P F5 we have

A Ď pλv ` Hq Y pµv ` Hq.

Due to |A| ą |H| the sets Aλ “ A X pλv ` Hq and Aµ “ A X pµv ` Hq are nonempty. The group Fˆ

5 acts by multiplication on the two-element subsets of F5, with three orbits represented by t0,1u, t1,2u, and t1,´1u. We can therefore suppose that tλ,µu is one of these three sets. In the last case, A is clearly normal, so it suffices to show that the first two cases lead to contradictions.

Suppose first that λ “ 0 and µ “ 1. Since A is sum-free, we have pA0 ` A1q X A1 “ ∅. But now 5n´1 “ |H ` v| ě |A0 ` A1| ` |A1| ě |A0| ` |A1| “ |A| contradicts our assumption on the size of A.

The case λ “ 1 and µ “ 2 is similar, the contradiction being

5n´1 “ |H ` 2v| ě |A1 ` A1| ` |A2| ě |A1| ` |A2| “ |A|. □ Our remaining applications of Kneser’s theorem factorise through the following result.

- Lemma 5.2. Let X,Y,Z Ď Fℓ5 be three nonempty sets satisfying pX ` Y q X Z “ ∅. If there exists an integer t such that |X| ` |Y | ą p25 ´ tq5ℓ´2 and |Z| ą t ¨ 5ℓ´2, then t is not


divisible by 5 and there exists a hyperplane K ď Fℓ5 together with positive integers a, b such that a ` b ` rt{5s “ 6, and X, Y , Z can be covered by a, b, rt{5s translates of K, respectively.

Proof. Since Z ‰ ∅ implies X ` Y ‰ Fℓ5, the symmetry set K “ SympX ` Y q is a proper linear subspace of Fℓ5. Moreover, the fact that the sum set X ` Y is a union of translates of K implies that it is even disjoint to Z ` K and, therefore, Kneser’s theorem reveals

5ℓ ě |X ` Y | ` |Z ` K| ě |X ` K| ` |Y ` K| ` |Z ` K| ´ |K|. (5.1)

Now suppose for the sake of contradiction that dimpKq ď ℓ ´ 2, so that not only |Z ` K| but also t¨5ℓ´2 is divisible by |K|. For this reason, |Z| ą t¨5ℓ´2 entails |Z `K|´|K| ě t¨5ℓ´2 and (5.1) leads to the contradiction

p25 ´ tq5ℓ´2 ě |X ` K| ` |Y ` K| ě |X| ` |Y |. We have thereby shown that K is a hyperplane. Define the positive integers a, b, and c by |X ` K| “ a|K|, |Y ` K| “ b|K|, and |Z ` K| “ c|K|.

Clearly, X, Y , and Z can be covered by a, b, and c translates of K, respectively. Moreover, (5.1) shows a ` b ` c ď 6, while the lower bounds

25 ´ t 5 and

|X| ` |Y | |K|

a ` b ě

ą

|Z| |K|

t 5

ą

c ě

are clear. For these reasons, t cannot be divisible by 5 and the equalities a ` b ` c “ 6 as well as c “ rt{5s hold. □

Corollary 5.3. If three nonempty sets X,Y,Z Ď Fℓ5 satisfy pX ` Y q X Z “ ∅ and

|X| ` |Y | ` |Z| ą 26 ¨ 5ℓ´2 , then there exists a linear epimorphism φ: Fℓ5 ÝÑ F5 such that |φpXq| ` |φpY q| ` |φpZq| “ 6. Proof. Setting t “ r|Z|{5ℓ´2s ´ 1 we have

pt ` 1q5ℓ´2 ě |Z| ą t ¨ 5ℓ´2 and

|X| ` |Y | ą `

26 ´ pt ` 1q˘

5ℓ´2 “ p25 ´ tq5ℓ´2 .

Thus Lemma 5.2 delivers a hyperplane K ď Fℓ5 and integers a, b, c such that a ` b ` c “ 6 and X, Y , Z can be covered by a, b, c translates of K, respectively. Now any linear epimorphism φ: Fℓ5 ÝÑ F5 with kernel K satisfies |φpXq| ` |φpY q| ` |φpZq| ď a ` b ` c “ 6. Finally, 5.2 ¨ 5ℓ´1 ă |X| ` |Y | ` |Z| ď p|φpXq| ` |φpY q| ` |φpZq|q5ℓ´1 shows that this needs to hold with equality. □

Theorem 1.1 yields an analogue of Lemma 5.1 concerning sum-free sets that can be covered by six translates of a subspace with codimension 2.

- Lemma 5.4. If A Ď Fn5 denotes a sum-free set of size |A| ą 5n´1 and there exists a linear epimorphism φ: Fn5 ÝÑ F25 such that |φpAq| ď 6, then A is normal.


Proof. Let us write AP “ φ´1pPq X A for every P P F25. By averaging there exists a point P P φpAq such that |AP| ą 16|A| ą 0.5¨5n´2. Now Corollary 2.2 yields AP ´AP “ kerpφq, whence p0,0q R φpAq. Similarly, we have |AP| ` |AQ| ě |A| ´ 4 ¨ 5n´2 ą 5n´2 for all distinct points P,Q P φpAq, which leads to AP˘Q “ ∅. For these reasons, φpAq is sum-free.

Moreover, |A| ą 5n´1 implies φpAq ě 6 and by Theorem 1.1 φpAq is normal. If L Ď F25

denotes any line with φpAq Ď L Y p´Lq, then the affine hyperplane H “ φ´1pLq satisfies A Ď H Y p´Hq. □

Under a slightly more restrictive density assumption on A, we can now extend Lemma 5.1 to sets coverable by three parallel hyperplanes.

- Lemma 5.5. If for some n ě 2 a sum-free set A Ď Fn5 of size |A| ě 28 ¨ 5n´3 can be covered by three parallel hyperplanes, then it is normal. Proof. Again we suppose


A Ď pλv ` Hq Y pµv ` Hq Y pνv ` Hq,

where H ď Fn5 denotes a hyperplane, v P Fn5 ∖H, and λ,µ,ν P F5 are distinct. By Lemma 5.1 it suffices to treat the case that

Aλ “ A X pλv ` Hq, Aµ “ A X pµv ` Hq, and Aν “ A X pνv ` Hq

are nonempty. By multiplicative symmetry, we only need to consider the cases that tλ,µ,νu is one of t1,2,´2u, t0,1,´1u, or t0,1,2u.

First Case: Either tλ,µ,νu “ t1,2,´2u or tλ,µ,νu “ t0,1,´1u.

Without loss of generality, we can now suppose λ “ µ ` ν. By Corollary 5.3 applied to H instead of Fℓ5 and to the sets X “ Aµ ´ µv, Y “ Aν ´ νv, Z “ Aλ ´ λv we get a certain linear epimorphism φ: H ÝÑ F5. Now the linear epimorphism ψ: Fn5 ÝÑ F25 defined by ψph ` ξvq “ pφphq,ξq for all h P H and ξ P F5 satisfies

|ψpAq| “ |φpXq| ` |φpY q| ` |φpZq| “ 6 and Lemma 5.4 implies the normality of A.

Second Case: We have tλ,µ,νu “ t0,1,2u. Since A0 is a sum-free subset of H, Fact 2.3 tells us |A0| ď 2 ¨ 5n´2, whence

2p2|A1| ` |A2|q ` p|A0| ` 2|A2|q “ 4|A| ´ 3|A0| ě p4 ¨ 5.6 ´ 3 ¨ 2q5n´2 ą 3 ¨ p5.2 ¨ 5n´2q. This shows that

2|A1| ` |A2| ą 5.2 ¨ 5n´2 or |A0| ` 2|A2| ą 5.2 ¨ 5n´2 .

Claim 5.6. If 2|A1| ` |A2| ą 5.2 ¨ 5n´2, then A is normal.

Proof. Arguing as in the first case, Corollary 5.3 leads to a linear epimorphism ψ: Fn5 ÝÑ F25 such that kerpψq ď H and 2|ψpA1q| ` |ψpA2q| “ 6. As in the proof of Lemma 5.4 one shows p0,0q R ψpAq and P ˘ Q R ψpAq for all distinct P,Q P ψpA1 Y A2q. So if either |ψpA1q| ě 3 or |ψpA2q| ě 3, then ψpAq X ψpHq “ ∅ and we reach the contradiction A0 “ ∅. In other words, we have |ψpA1q| “ |ψpA2q| “ 2 and |ψpA0q| ď 2 follows. Now |ψpAq| ď 6 and Lemma 5.4 imply that A is normal. □

It remains to discuss the case |A0| ` 2|A2| ą 5.2 ¨ 5n´2. As before, we find a linear epimorphism ψ: Fn5 ÝÑ F25 satisfying kerpψq ď H and |ψpA0q| ` 2|ψpA2q| “ 6, and observe that only the case |ψpA0q| “ |ψpA2q| “ 2 is possible. This yields

2|A1| ` |A2| “ 2|A| ´ 2|A0| ´ |A2| ě p2 ¨ 5.6 ´ 2 ¨ 2 ´ 2q5n´2 “ 5.2 ¨ 5n´2 and, unless this holds with equality, Claim 5.6 implies the normality of A. So we can suppose |A0| “ 2 ¨ 5n´2, which means that ψ´1pPq Ď A holds for both points P P ψpA0q. As this leads to |ψpA1q| ď 2, we again have |ψpAq| ď 6 and A is normal by Lemma 5.4. □

- 5.2. VL-sets. The goal of this subsection is to establish a connection between the three


special fishy functions fα, fβ, and fγ appearing in Proposition 2.6 and VL-sets. We commence with the three dimensional case.

Lemma 5.7. Given a sum-free set A Ď F35, let Ix,y “ tz P F5: px,y,zq P Au for every planar point px,yq P F25. If there exists a letter τ P tα,β,γu such that |Ix,y| “ fτpx,yq holds for every px,yq P F25, then A is isomorphic to Λ.

Proof. Beginning with the case τ “ α we need to study the two-element sets I´1,2, I2,1, I1,´2, and I´2,´1. The main point is that

U “ tpx,´2x,yq: x,y P F5u

is a two-dimensional subspace of F35 and A X U is a sum-free subset of U of size 8. Thus there exists a line L Ď U such that A X U Ď L Y p´Lq. As L cannot be parallel to L0,0, we can assume without loss of generality that L “ tpx,´2x,2x ` 2q: x P F5u, which leads to

I´1,2 “ t0,1u, I2,1 “ t1,2u, I1,´2 “ t´1,0u, I´2,´1 “ t´2,´1u, and A “ Λ.

Next we consider the case τ “ β, i.e., |Ix,y| “ fβpx,yq for all px,yq P F25. The missing element of I1,0 can be supposed to be 0. For each point px,yq P F5ˆFˆ

5 we have pIx,y`I1,0qXIx`1,y “ ∅ and, consequently, Ix,y “ Ix`1,y. In other word, there exists for every y P Fˆ

5 a constant cy P F5 such that Ix,y “ tcyu holds for every x P F5. Due to pI0,y `I1,´yqXI1,0 “ ∅ we have c´y “ ´cy

for every y P Fˆ

5 . An appropriate automorphism of F35 allows us to suppose c1 “ c´1 “ 0 and c2 P t0,1,2u. The case c2 “ 0 is impossible due to pI0,1 ` I0,1q X I0,2 “ ∅. Finally, I´1,0 X t0u “ pI´1,0 ` I1,1q X I0,1 “ ∅ yields I´1,0 “ Fˆ

5 .

Now the structure of A becomes more transparent when we project this set not into the x-y-plane but rather into the x-z-plane. That is, we consider the function h: F25 ÝÑ Rě0 defined by hpx,zq “ |ty P F5: px,y,zq P Au| for all px,zq P F25. For both cases of c2, this function is displayed in Figure 5.1. It is now immediate that h is isomorphic to fα, whence A is isomorphic to Λ.

| | | |5| |
|---|---|---|---|---|
| | |5| | |
|2|2| |2|2|
| | |5| | |
| |5| | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(a) c2 “ 1

| | | | |5|
|---|---|---|---|---|
| | |5| | |
|2|2| |2|2|
| | |5| | |
|5| | | | |


- 0
- 1
- 2


´1

´2

´2 ´1 0 1 2

(b) c2 “ 2

Figure 5.1. The function h

Let us finally address the case τ “ γ. Arguing as in the previous case, we can suppose I1,0 “ I0,1 “ Fˆ

5 and prove the existence of some a P F5 such that Ix,y “ tau holds for the twelve points px,yq P F25 with fγpx,yq “ 1. Due to pI´1,´2`I2,2qXI1,0 “ ∅ we have a “ 0 but now the contradiction pI2,1 ` I1,2q X I´2,´2 ‰ ∅ arises. Thus the last case is impossible. □

Our next goal is to extend this result to higher dimensions. As explained in §2.3 with every sum-free set A Ď Fn5 and every linear epimorphism φ: Fn5 ÝÑ F25 we associate the function

|A X φ´1pPq| 5n´3 .

fφA: F25 ÝÑ Rě0 , P ÞÝÑ

It will also be convenient to set AφP “ A X φ´1pPq for every P P F25. We would like to point out an obvious consequence of Corollary 5.3

Corollary 5.8. Let a sum-free set A Ď Fn5 and a linear epimorphism φ: Fn5 ÝÑ F25 be given. If for some P,Q,R P F25 and ε P t´1,1u with R “ P ` εQ we have

‚ fφApPq,fφApQq,fφApRq P t1,2,3,4u ‚ and fφApPq ` fφApQq ` fφApRq “ 6,

then K “ SympAφPq “ SympAφQq “ SympAφRq is a pn ´ 3q-dimensional subspace of kerpφq and for each X P tP,Q,Ru the set AφX is a union of fφApXq translates of K. □

- Lemma 5.9. Let A Ď Fn5 be sum-free. If there exists a linear epimorphism φ: Fn5 ÝÑ F25 such that fφA “ fτ holds for some letter τ P tα,β,γu, then A is a VL-set.

Proof. We commence with the case τ “ α, where our main task is to analyse the sets Aφ´1,2, Aφ2,1, Aφ1,´2, and Aφ´2,´1. Since

p´1,2q ` p2,1q “ p1,´2q, p2,1q ` p1,´2q “ p´2,´1q, and

fφAp´1,2q ` fφAp2,1q ` fφAp1,´2q “ fφAp2,1q ` fφAp1,´2q ` fφAp´2,´1q “ 6, Corollary 5.8 tells us that all four of them have the same symmetry set

K “ SympA´1,2q “ SympA2,1q “ SympA1,´2q “ SympA´2,´1q, which is a hyperplane in kerpφq. Furthermore, each of our four sets is a union two translates of K. Altogether, A is a union of 28 translates of K and thus isomorphic to a set of the form B ˆ Fn´3

5 , where B Ď F35 is a sum-free set satisfying the hypothesis of Lemma 5.7 for τ “ α. So B is isomorphic to Λ and A is a VL-set.

The cases τ “ β and τ “ γ are similar. □

5.3. Fishy projections. The next result connects the study of sum-free sets to our work on fishy functions.

- Lemma 5.10. For every sum-free set A Ď Fn5 of size |A| ě 28 ¨ 5n´3 and every linear epimorphism φ: Fn5 ÝÑ F25 the function fφA is fishy. Proof. Set f “ fφA. Property (F1) follows from


|A|

5n´3 ě 28 and from the fact that

}f}1 “

|φ´1pPq|

5n´3 “ 5 is fulfilled for every P P F25. Since for every X Ď F25 the number 5n´3fpXq is an integer, (F2) holds as well.

fpPq ď

Proceeding with (F3) we consider two points P,Q P F25 and a sign ε P t´1,1u such that P, Q, and R “ P ` εQ are in the support of f. Setting t “ 5rfpRqs ´ 5 we have

|AφR| “ 5fpRq ¨ 5n´4 ą t ¨ 5n´4 . Since t is divisible by 5, Lemma 5.2 yields

|AφP| ` |AφQ| ď p25 ´ tq5n´4 “ p6 ´ rfpRqsq5n´3 , whence fpPq ` fpQq ď 6 ´ rfpRqs. □

Proof of Proposition 2.7. Let φ: Fn5 ÝÑ F25 be a linear epimorphism mapping T to some point P P F25. By Lemma 5.10 the function f “ fφA is fishy. Since

|A X T| 5n´3 ą 3,

}f}8 ě fpPq “

Proposition 2.6 tells us that either the support of f can be covered by three parallel lines or f is isomorphic to one of the functions fα, fβ, or fγ. In the former case, A can be covered by three parallel hyperplanes and Lemma 5.5 informs us that A is normal. In the latter case, Lemma 5.9 applies and A is a VL-set. □

Proof of Proposition 2.10. Fix a linear epimorphism φ: Fn5 ÝÑ F25 sending T to some point P‹ P F25 and, consequently, ´T to ´P‹. By Lemma 5.10 the function g “ fφA is fishy and our hypothesis on T translates to

|A X T| ` |A X p´Tq|

5n´3 ą 5.6, (5.2) so we can suppose without loss of generality that gpP‹q ą 2.8. If }g}8 ą 3, then Proposition 2.7 implies immediately that A has the desired form, so it suffices to treat the case }g}8 ď 3 in the sequel. Now (5.2) implies gp´P‹q ą 5.6 ´ 3 ą 2.5.

gpP‹q ` gp´P‹q “

Claim 5.11. For every point Q P F25 such that gpQq,gpP‹`Qq ą 0 and gpQq`gpP‹`Qq ą 2.2 there exists a hyperplane KQ ď kerpφq such that each of AφP

and AφQ Y AφP

‹`Q can be covered

‹

by three translates of KQ. Proof. We pick arbitrary points vP

P φ´1pP‹q and vQ P φ´1pQq. Now Lemma 5.2 applied to kerpφq instead of Fℓ5, the sets,

‹

` vQq, Y “ vQ ´ AφQ , Z “ AφP

X “ AφP

´ vP

‹`Q ´ pvP

, and to t “ 14 yields the desired hyperplane KQ. □

‹

‹

‹

Because of gpP‹q ą 2.8 and }g}8 ď 3 Lemma 3.14 shows that the assumption of Claim 5.11 is satisfied for at least one point Q and, consequently, there exists a hyperplane K ď kerpφq such that AφP

is contained in the union of three translates of K. Assume for the sake of contradiction that K is not uniquely determined by this property. Since any two nonparallel affine hyperplanes in kerpφq intersect in a pn ´ 4q-dimensional affine subspace of kerpφq, this yields |AφP

‹

| ď 3 ¨ 3 ¨ 5n´4 and we get the contradiction gpP‹q ď 1.8.

‹

This proves KQ “ K for all points Q P F25 satisfying the hypothesis of Claim 5.11. Let π: F35 ÝÑ F25 be the projection to the first two coordinates, i.e., the map px,y,zq ÞÝÑ px,yq, choose a linear epimorphism ψ: Fn5 ÝÑ F35 with kernel K such that φ “ π ˝ ψ, and define

|A X ψ´1pPq| 5n´3

f : F35 ÝÑ Rě0 by fpPq “

for every P P F35. Owing to φ “ π ˝ ψ we have ψ´1pLPq “ φ´1pPq for every P P F25 and, therefore, g is the standard projection of f.

We contend that f is acceptable. The properties (A2) and (A4)–(A6) have already been addressed. Moreover, (A1) is clear and (A3) follows easily from Corollary 2.2.

Now Proposition 2.9 delivers a line L Ď F35 such that fpLq ą 3. The affine subspace U “ ψ´1pLq of Fn5 has codimension 2 and satisfies |A X U| “ fpLq ¨ 5n´3 ą 3 ¨ 5n´3. Owing to Proposition 2.7 it follows that A is either normal or a VL-set. □

§6 Concluding remarks The notation for sum-free sets employed in the introduction suggests the following hierarchy of sum-free sets introduced in [13, Definition 1.2]. Definition 6.1. Let G be a finite abelian group. Starting with

SF0pGq “ tA Ď G: A is sum-freeu

we define by recursion on k the numbers and sets ‚ sfkpGq “ maxt|A|: A P SFkpGqu, ‚ SFĂkpGq “ tA P SFkpGq: |A| “ sfkpGqu, ‚ SFk`1pGq “ tA P SFkpGq: there is no B P SFĂkpGq with A Ď Bu.

This is to some extent inspired by a similarly defined hierarchy for intersecting set systems, which has a vast literature (see e.g., [3,5,6,11]). As we have already pointed out, SFĂ0pGq is known for every finite abelian group G (see [1]). Research on sf1pGq has so far mainly focused on vector spaces over finite fields. In fact, prior to this work sf1pFnpq and even SFĂ1pFnpq were known for all p ‰ 5, so that Theorem 1.3 solves the last open problem of its kind. It would of course be interesting if one could determine sf1pGq for broader classes of abelian groups as well.

For k ě 2 some discussion on sfkpFnpq can be found in [12,13]. Here we would only like to point out that if p denotes a prime number with p ě 11 and p ” ´1 pmod 3q, then for n ě 2 there are sets A P SFĂ1pFnpq such that there are two distinct vectors x,y P Fnp not belonging to A Y pA ` Aq Y pA ´ Aq.

Thus the only reason why A Y txu and A Y tyu fail to be sum-free is that 2x and 2y are in A. In the situations we have in mind x ` y P A and x ´ y R A hold as well, and the sum-free set A Y tx,yu ∖ t2x,x ` y,2yu exemplifies sf2pFnpq “ sf1pFnpq ´ 1, which is, perhaps, a bit underwhelming. The same kind of construction shows sf1pFnpq “ sf0pFnpq ´ 1 whenever p ” 1 pmod 3q.

sfkpFnpq˘kPN0 is interesting (see [2,12]). It is not difficult to check Λ Y pΛ ` Λq Y pΛ ´ Λq “ F35 and thus there is some reason to believe that the investigation of sf2pFn5q will lead to new insights as well.

`

For p “ 2 and p “ 3, on the other hand, the entire hierarchy

The following related group invariant has been introduced by Vsevolod Lev [9]. Call a subset X of an abelian group G aperiodic if SympXq “ t0u. If there exists an aperiodic, inclusion-wise maximal sum-free subset of G, we denote the largest size that such a set can have by tpGq; otherwise, we simply set tpGq “ 0. Whenever p ‰ 5 the numbers tpFnpq are known (see [2,9,12]), while our understanding of the case p “ 5 is very limited. Clearly, we have tpF5q “ 0 and Theorem 1.1 shows tpF25q “ 5. Moreover, the aperiodicity of Λ implies tpF35q “ 28, but for n ě 4 the determination of tpF45q is open.

Acknowledgement. The second author would like to thank Leo Versteegen for introducing her to this topic and some early discussions.

References

- [1] R. Balasubramanian, G. Prakash, and D. S. Ramana, Sum-free subsets of finite abelian groups of type III, European J. Combin. 58 (2016), 181–202, DOI10.1016/j.ejc.2016.06.001. MR3530628 Ò1, 39
- [2] A. A. Davydov and L. M. Tombak , , 25

- (1989), no. 4, 11–23 (Russian); English transl., Problems Inform. Transmission 25 (1989), no. 4, 265–275
- (1990). MR1040020 Ò1, 40


- [3] P. Erdős, C. Ko, and R. Rado, Intersection theorems for systems of finite sets, Quart. J. Math. Oxford Ser. (2) 12 (1961), 313–320, DOI10.1093/qmath/12.1.313. MR140419 Ò39
- [4] B. Green and I. Z. Ruzsa, Sum-free sets in abelian groups, Israel J. Math. 147 (2005), 157–188, DOI10.1007/BF02785363. MR2166359 Ò1
- [5] J. Han and Y. Kohayakawa, The maximum size of a non-trivial intersecting uniform family that is not a subfamily of the Hilton-Milner family, Proc. Amer. Math. Soc. 145 (2017), no. 1, 73–87, DOI10.1090/proc/13221. MR3565361 Ò39
- [6] A. J. W. Hilton and E. C. Milner, Some intersection theorems for systems of finite sets, Quart. J. Math. Oxford Ser. (2) 18 (1967), 369–384, DOI10.1093/qmath/18.1.369. MR219428 Ò39
- [7] M. Kneser, Abschätzung der asymptotischen Dichte von Summenmengen, Math. Z. 58 (1953), 459–484, DOI10.1007/BF01174162 (German). MR56632 Ò3
- [8] , Ein Satz über abelsche Gruppen mit Anwendungen auf die Geometrie der Zahlen, Math. Z. 61

(1955), 429–434, DOI10.1007/BF01181357 (German). MR68536 Ò3

- [9] V. F. Lev, Large sum-free sets in ternary spaces, J. Combin. Theory Ser. A 111 (2005), no. 2, 337–346, DOI10.1016/j.jcta.2005.01.004. MR2156218 Ò1, 40
- [10] , Large sum-free sets in Zn5, J. Combin. Theory Ser. A 205 (2024), Paper No. 105865, 9, DOI10.1016/j.jcta.2024.105865. MR4700167 Ò1, 2, 4

- [11] J. Polcyn and A. Ruciński, A hierarchy of maximal intersecting triple systems, Opuscula Math. 37 (2017), no. 4, 597–608, DOI10.7494/OpMath.2017.37.4.597. MR3647803 Ò39


- [12] Chr. Reiher, On Lev’s periodicity conjecture, Bull. Lond. Math. Soc. 57 (2025), no. 5, 1496–1511, DOI10.1112/blms.70043. MR4913163 Ò39, 40
- [13] Chr. Reiher and S. Zotova, Large sum-free sets in finite vector spaces I., available at arXiv:2408.11232. Submitted. Ò2, 39
- [14] I. Schur, Über die Kongruenz xm ` ym ” zm pmod pq, Deutsche Math. Ver. 25 (1916), 114–117. Ò1
- [15] L. Versteegen, The structure of large sum-free sets in Fnp, available at arXiv:2303.00828. Ò1, 2


Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany Email address: christian.reiher@uni-hamburg.de

Mathematisches Institut, Universität Bonn, Bonn, Germany Email address: s87szoto@uni-bonn.de

