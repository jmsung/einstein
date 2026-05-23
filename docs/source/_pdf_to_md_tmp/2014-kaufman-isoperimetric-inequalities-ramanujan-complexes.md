arXiv:1409.1397v1[math.CO]4Sep2014

Isoperimetric Inequalities for Ramanujan Complexes and Topological Expanders∗

Tali Kaufman † David Kazhdan ‡ Alexander Lubotzky §

June 29, 2018

Abstract

Expander graphs have been intensively studied in the last four decades. In recent years a high dimensional theory of expanders has emerged, and several variants have been studied. Among them stand out coboundary expansion and topological expansion. It is known that for every d there are unbounded degree simplicial complexes of dimension d with these properties. However, a major open problem, formulated by Gromov [9], is whether bounded degree high dimensional expanders exist for d ≥ 2.

We present an explicit construction of bounded degree complexes of dimension d = 2 which are topological expanders, thus answering Gromov’s question in the aﬃrmative. Conditional on a conjecture of Serre on the congruence subgroup property, inﬁnite sub-family of these give also a family of bounded degree coboundary expanders.

The main technical tools are new isoperimetric inequalities for Ramanujan Complexes. We prove linear size bounds on F2 systolic invariants of these complexes, which seem to be the ﬁrst linear F2 systolic bounds. The expansion results are deduced from these isoperimetric inequalities.

![image 1](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile1.png>)

∗The results of this paper were announced in [12]. †Bar-Ilan University, ISRAEL. Email: kaufmant@mit.edu. Research supported in part by the Alon Fellowship,

IRG, ERC and BSF.

‡Hebrew University, ISRAEL. Email: kazhdan.david@gmail.com. Research supported in part by the NSF, BSF and ERC.

§Hebrew University, ISRAEL. Email: alexlub@math.huji.ac.il. Research supported in part by the ERC, NSF and ISF.

# Contents

- 1 Introduction 3
- 2 Coboundary expansion and overlapping 7

- 2.1 Expansion of graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 2.2 Coboundary expansion of simplicial complexes . . . . . . . . . . . . . . . . . . . . . 8
- 2.3 Notions of minimality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


- 3 Buildings and Ramanujan complexes 11

- 3.1 Spherical buildings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 3.2 Bruhat-Tits buildings and Ramanujan complexes . . . . . . . . . . . . . . . . . . . . 14


- 4 From Isoperimetric inequalities to topological expanders 16
- 5 Expansion of 1-cochains in 2-dimensional Ramanujan complexes 18

- 5.1 Proof of Theorem 1.9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

6 Expansion of i-cochains in 3-dimensional Ramanujan complexes 21

- 6.1 Proof of Theorem 1.8 for the case i = 0 . . . . . . . . . . . . . . . . . . . . . . . . . 21 6.2 Proof of Theorem 1.8 for the case i = 1 . . . . . . . . . . . . . . . . . . . . . . . . . 22


- 7 Expansion of 2-cochains in 3-dimensional Ramanujan complexes 27
- 8 Coboundary expanders and the congruence subgroup property 34


# 1 Introduction

A classical result of Boros and Fu¨redi [3] (for d = 2) and B´ara´ny [1] (for general d ≥ 2) asserts that there exists ǫd > 0 such that given any set of n points in Rd, there exists z ∈ Rd which is contained in at least ǫd-fraction of the d+1 n simplicies determined by the set. Gromov [9] changed the perspective of this result by strengthening and generalizing it in the following way.

Deﬁnition 1.1. Let X be a d-dimensional pure simplicial complex with a set X(0) of vertices and denote by X(d) the set of d-dimensional faces.

- 1. We say that X has the ǫ-geometric overlapping property, for some 0 < ǫ ∈ R, if for every f : X(0) → Rd, there exists a point z ∈ Rd which is covered by at least ǫ-fraction of the images of the faces in X(d) under f˜. Here, f˜ is the (unique) aﬃne extension of f.
- 2. We say that X has the ǫ-topological overlapping property, if the same conclusion holds for every continuous extension f˜: X → Rd of f.
- 3. A family of d-dimensional simplicial complexes is a geometric (resp. topological) expander if all of them have the ǫ-geometric (resp. topological) overlapping property for the same ǫ > 0.


Barany’s theorem is, therefore, the statement that, for every d, ∆n(d) - the complete d-dimensional simplicial complex on n vertices of dimension d are geometric expanders. Gromov proved the remarkable result, saying that they are also topological expanders (The reader is encouraged to think about the case d = 2 to see how non-trivial is this result and even somewhat counter intuitive!) Moreover, he went ahead and showed that various other families of simplicial complexes (of ﬁxed dimension d) have the topological overlapping property, e.g., spherical buildings (see [9], [20]).

All the examples shown by Gromov are of simplicial complexes of unbounded degrees, i.e., the number of d-faces containing a ﬁxed vertex (or even the number of d faces containing a (d−1)-face) is unbounded along the family. He suggested [9, p.422] that 2-dimensional Ramanujan complexes (see below) coming from a ﬁxed local non-archimedean ﬁeld F, form a family of bounded degree topological expanders ”if such at all exist...” in his words. He showed that they have a weaker property, namely, the conclusion of Deﬁnition 1.1(2) holds if f˜ is k to 1 on faces, for some ﬁxed k. Even the question of existence of families which are bounded degree geometric expanders for general d was left open in [9].

The later question, i.e. the question of existence of families of simplicial complexes of bounded degree with the geometric overlapping property was resolved by Fox, Gromov, Laﬀorgue, Naor, and Pach [7] in a satisfactory way (and in several ways). They showed, for example, the following result.

- Theorem 1.2. Let d ≥ 2 and ﬁx a suﬃciently large prime power q: If F is a local non-archimedean ﬁeld of residual degree q, then the Ramanujan complexes quotients of the Bruhat-Tits building associated with PGLd+1(F) are d-dimensional bounded degree geometric expanders.


However, they also left open the question of existence of bounded degree topological expanders.

In [19] a model of random 2-dimensional complexes of bounded edge degree is presented. These complexes are shown to be topological expanders, but they, also, have unbounded (vertex) degree.

In this paper we show, for the ﬁrst time, the existence of bounded degree 2-dimensional topological expanders. We fell short from proving that Ramanujan complexes of dimension 2 are themselves topological expanders, but we prove:

- Theorem 1.3. Fix a suﬃciently large prime power q and let F = Fq((t)). Let {Xa}a∈A be the family of 3-dimensional non-partite Ramanujan complexes obtained from the Bruhat-Tits building


associated with PGL4(F) [22]. For each such Xa, let Ya = Xa(2) - the 2-skeleton of Xa. Then, the family of 2-dimensional simplicial complexes {Ya}a∈A is an inﬁnite family of bounded degree topological expanders.

Before elaborating on the method of proof, let us start by relating the above mentioned results to the notion of coboundary expanders as (essentially) been deﬁned by Linial and Meshulam [15] in a completely diﬀerent context. Their motivation was to generalize to complexes the Erdos-Re`yni theory of random graphs.

To introduce this and to present the main technical results of this paper we need few notations: Let X be a pure d-dimensional simplicial complex (i.e., every maximal simplex is d-dimensional). For i ≤ d, let X(i) be the set of i-cells of X and for σ ∈ X(i), denote c(σ) = |{τ ∈ X(d)|σ ⊆ τ}| and w(σ) = c(σ)

(di+1+1)|X(d)|. This weight function on X(i) deﬁnes a ”norm” on Ci = Ci(X,F2) = {f : X(i) → F2} by ||α|| = σ∈α w(σ), where α ∈ Ci is considered also as the subset {σ ∈ X(i) | α(σ) = 0} of X(i). As usual δ = δi : Ci → Ci+1 is the coboundary map δ(α)(σ) = τ⊆σ,|τ|=i α(τ) for α ∈ Ci and σ ∈ X(i + 1). As δi ◦ δi−1 = 0, Bi ⊆ Zi where Bi = Im(δi−1) (resp. Zi = Ker(δi)) is the space of i-coboundaries (resp. i-cocycles).

![image 2](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile2.png>)

Deﬁnition 1.4. .

- 1. (F2-coboundary expansion) For i = 0,1,··· ,d − 1, denote

ǫi(X) := min{

||δiα|| ||[α]||

![image 3](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile3.png>)

| α ∈ Ci \ Bi}

When [α] = α + Bi and ||[α]|| = min{||γ|| | γ ∈ [α]}.

- 2. (F2-cocycle expansion) For i = 0,1,··· ,d − 1, denote

ǫ˜i(X) := min{

||δiα|| ||{α}||

![image 4](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile4.png>)

| α ∈ Ci \ Zi}

When {α} = α + Zi and ||{α}|| = min{||γ|| | γ ∈ {α}}.

- 3. (coﬁlling constant) The i-th coﬁlling constant of X, 0 ≤ i ≤ d − 1, is


1 ||β||

µi(X) =: max0 =β∈Bi+1{

minα∈Ci,δα=β||α||}

![image 5](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile5.png>)

.

If {Xj}j∈J is a family of d-dimensional simplicial complexes with ǫi(Xj) ≥ ǫ (resp. ǫ˜i(Xj) ≥ ǫ) for some ǫ > 0 and every 0 ≤ i ≤ d − 1 and j ∈ J, we say that this is a family of coboundary (resp. cocycle) expanders. Note that {Xj}j∈J is a family of cocycle expanders iﬀ there exists M ∈ R such that µi(Xj) ≤ M for every i = 0,··· ,d − 1 and j ∈ J.

As B0 = {0,1}, one easily checks that ǫ0 = ǫ0(X) is the normalized Cheeger constant of the 1skeleton of X, so the ǫi’s deserve to be considered as a generalization of the notion of expansion of graphs. Meshulam and Wallach [23] on one hand and Gromov [9] on the other hand showed that ∆n(d) form a family of coboundary expanders. But, also in these works the existence of coboundary expanders of bounded degree remained open.

and that if ǫi(X) > 0 then Hi(X,F2) = 0, in which case µi = ǫ1

It is easy to see that µi = ǫ1˜

.

![image 6](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile6.png>)

![image 7](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile7.png>)

i

i

A family of coboundary expanders is therefore a family with bounded ﬁlling norms, but not vise versa. Also, for d-dimensional coboundary expanders the F2 cohomology vanish for every i < d. Ramanujan complexes are in general not coboundary expanders. In fact we will show:

- Proposition 1.5. Let d ≥ 2, F = Fq((t)) and B = A˜d(F) the Bruhat-Tits building associated with PGLd+1(F). Then, B has inﬁnitely many quotients X which are Ramanujan complexes with both H1(X,F2) and H2(X,F2) non-zero.


- Proposition 1.5 should be compared with a well known result of Garland [8] asserting that for such X, the real i-cohomology always vanish, i.e., Hi(X,R) = 0, for every i < d.


- A deep result of Gromov [9] asserts that coboundary expanders are topological expanders. While there are several methods to prove geometric overlapping ([7],[25]), this is essentially the only known method to prove topological overlapping. As Proposition 1.5 shows, Ramanujan complexes, in general, are not coboundary expanders (see further discussion in Section 3.2 and in Section 8).


By the same reason, the Ya’s of Theorem 1.3 are not coboundary expanders. We are still able to show that they are topological expanders due to two reasons. First, the following result [14] which extends Gromov’s criterion to the cases where the cohomology does not necessarily vanish. Unfortunately, we need some more notations.

- Deﬁnition 1.6. For a ﬁnite d-dimensional simplicial complex X and 1 ≤ i ≤ d − 1 denote systi(X) = min{||α|| | α ∈ Zi(X,F2) \ Bi(X,F2)}.


(Write systi(X) = ∞ if Hi(X,F2) = 0.) This is the i-cohomological systole of X over F2.

- Theorem 1.7. Given 0 < µ,η ∈ R, and d ∈ N, there exists c = c(d,µ,η) > 0 such that if X is a ﬁnite pure simplicial complex of dimension d satisfying:


- 1. For every 0 ≤ i ≤ d − 1, µi(X) ≤ µ.
- 2. For every 0 ≤ i ≤ d − 1, systi(X) ≥ η.


Then X has the c-topological overlapping property.

In diﬀerent words, cocycle expanders with large systole are topological expanders.

- A proof of Theorem 1.7 is given in [14].


Thus, to prove Theorem 1.3, it suﬃces to prove that the Ya’s of Theorem 1.3 satisfy both conditions

(1) and (2) of Theorem 1.7. To this end we will prove the following isoperimetric result(s):

- Theorem 1.8. Fix q ≫ 0. Let F be a local ﬁeld of residue degree q, B = A˜3(F) the 3-dimensional Bruhat-Tits building associated with PGL4(F). Then there exist η0,η1,η2,ǫ0,ǫ1,ǫ2 all greater than 0 such that: if X is a non-partite Ramanujan quotient of B = A˜3(F) and α ∈ Ci(X,F2), 0 ≤ i ≤ 2, a locally minimal cochain with ||α|| ≤ ηi then ||δi(α)|| ≥ ǫi||α||.


The concept of locally minimal cochain is quite central in our work, but too technical to be deﬁned in the introduction - see Deﬁnition 2.4 below. We believe that the above six constants can be made to be independent of q, but as of now we know this only for some of them.

- Theorem 1.8 is best possible: it is not true without the assumption that ||α|| is small. As mentioned before, the Ramanujan complexes are in general not coboundary expanders: For i = 1 or i = 2 (but not for i = 0), it is possible to ﬁnd a locally minimal α ∈ Ci \ Bi with δi(α) = 0.

It is interesting to observe that in order to prove that the Ya’s of Theorem 1.3 are topological expanders we have to prove the above isoperimetric results for the Xa’s. Of course at level i = 0,1, Ya and Xa are the same, but for i = 2, δ2 is zero on C2(Ya,F2) but non-zero on C2(Xa,F2). We refer the reader to Section 4 to see how the information on Xa helps to deduce the desired result for Ya.

Our main technical result is Theorem 1.8. Before proving this theorem, we will give a ”baby version” of it for 2-dimensional Ramanujan complexes. This case is easier (for reasons to be understood in Section 6 and Section 7) though still far from trivial, and the main ideas of the proof of Theorem 1.8 show up already there. It also has some independent interest (see Corollary 1.10 below and the discussion following it). In this case we can also give a very sharp estimates on the constants, which are also independent of q:

- Theorem 1.9. Given ǫ0 > 0, there exists q(ǫ0) ∈ N and 0 < ǫ ∈ R such that: Let X be a 2 dimensional Ramanujan complex, a quotient of the Bruhat-Tits building of PGL3(Fq((t))) with


- q ≥ q(ǫ0). Let α ∈ C1(X,F2) be a locally minimal 1-cochain, with ||α|| < 4(1+1ǫ


0). Then ||δ1(α)|| ≥ ǫ||α||.

![image 8](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile8.png>)

Every locally minimal α ∈ C1(X,F2) satisﬁes ||α|| ≤ 21 (see Section 2.3). So, the theorem says that if α has slightly less than half of the maximal number of edges of a locally minimal cochain,

![image 9](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile9.png>)

its coboundary is ”large”. This is essentially best possible, as we will show (Proposition 3.5) that there are non-zero locally minimal cochains α with δ(α) = 0.

The above isoperimetric results and their proofs give various (mod 2) systolic inequalities. These seem to be the ﬁrst linear lower bound on cohomological systole. Such lower bounds are of importance for quantum error correcting codes. They are needed for the estimate of the distance of the so called CSS-quantum codes [24, 32, 10]. For example we have:

Corollary 1.10. Given ǫ0 > 0, there exists q(ǫ0) ∈ N such that: If X is a non-partite Ramanujan complex of dimension 2, a quotient of the Bruhat-Tits building of PGL3(Fq((t))) with q ≥ q(ǫ0), and α ∈ Z1(X,F2) \ B1(X,F2), i.e., a 1-cocycle which represents a non-trivial cohomology class, then ||α|| ≥ 4(1+1ǫ

0).

![image 10](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile10.png>)

Ramanujan complexes of dimension 2 are in many ways non-archimedean analogue of 2-dimensional manifolds, i.e. Riemann surfaces. It is interesting to compare the systolic behavior. For arithmetic hyperbolic surfaces, the 1-homological systole is logarithmic and by Poincare duality the same holds for the 1-cohomological systole. But, for the Ramanujan complexes the 1-homological systole is logarithmic and the 1-chomological systole is linear!

See more in Section 7 where such linear lower bounds are proved also for 2-cocycles of 3-dimensional complexes.

The paper is organized as follows. In Section 2 we introduce the basic cohomological notations (over F2), and the (local)-minimality of cochains. In Section 3, we review the spherical and aﬃne buildings and the properties of Ramanujan complexes. In Section 4 we show how, assuming Theorem 1.8, one can prove Theorem 1.3, leaving the (quite technical) proof of Theorem 1.8 to Sections 6 (cases i = 0,1) and 7 (case i = 2). To illustrate ﬁrst the main ideas of the proof of Theorem 1.8 in an easier case, we give in Section 5 a proof of Theorem 1.9. In Section 8 we show that our results combined with Serre’s conjecture [31] on the congruence subgroup property give bounded degree 2-dimensional coboundary expanders. Serre’s conjecture has been proven in most cases, but unfortunately, not in the cases we need here. In fact, what we need is only the vanishing of H1(Γ,F2) for suitable congruence subgroups, which is a corollary of Serre’s conjecture, and possibly easier than it. See Section 8 for more.

# 2 Coboundary expansion and overlapping

In this section we review some notations and results on general simplicial complexes.

## 2.1 Expansion of graphs

Let X = (V,E) be a ﬁnite connected graph, A = AX its adjacency matrix and ∆ its Laplacian, i.e., ∆ : L2(X) → L2(X) is deﬁned by ∆(f)(v) = deg(v)f(v) − y∼v f(y) where the sum is over the neighbors of v. If X is k-regular then ∆ = kI − A. It is well known that the eigenvalues of ∆ (and A) are intimately connected with expansion properties of X. Let us mention a variant which we need, due to Alon and Milman [18, Prop 4.2.5].

- Proposition 2.1. Let λ1(X) be the smallest positive eigenvalue of ∆. Then, for every subset


- W ⊆ V ,


- 1. |E(W,W¯ )| ≥ |W|V||W|¯ |λ1(X), where E(W,W¯ ) denotes the set of edges from W to its complement W¯ .

![image 11](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile11.png>)

- 2. The Cheeger constant h(X) satisﬁes: h(X) := minW⊆V min|E((W,|WW|¯,|W)¯| |) ≥ λ1(2X).

![image 12](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile12.png>)

![image 13](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile13.png>)

- 3. If X is k-regular then E(W) := E(W,W) = 12(k|W| − E(W,W¯ )) ≤ 21(k − ||WV¯||λ1(X))|W|.


![image 14](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile14.png>)

![image 15](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile15.png>)

![image 16](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile16.png>)

We will also need the following variant for bipartite bi-regular graphs, whose proof can be found for example in [6].

- Proposition 2.2. (Mixing Lemma for bipartite bi-regular graphs) Let X = (V ′,V ′′,E) be a bipartite (k′,k′′)-bi-regular ﬁnite graph. Then, for every subsets A ⊆ V ′, B ⊆ V ′′,


√

![image 17](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile17.png>)

k′k′′|A||B| |V ′||V ′′|

![image 18](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile18.png>)

|E(A,B)| −

| ≤ λ(X) |A||B|,

![image 19](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile19.png>)

![image 20](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile20.png>)

where λ(X) is the second largest eigenvalue of the adjacency matrix of X.

## 2.2 Coboundary expansion of simplicial complexes

Let us now pass to the higher dimensional case, so from now on X will be a ﬁnite d-dimensional simplicial complex with a set of vertices V = X(0). Namely, X is a set of subsets of V with F1 ∈ X and F2 ⊆ F1 implies F2 ∈ X and max{|F| |F ∈ X} = d + 1. For F ∈ X, dim(F) := |F| − 1, and X(i) denotes the set of cells of dimension i, i.e., those F with |F| = i + 1. So, X(−1) = {∅}. By X(i) we denote the i-skeleton of X, i.e., X(i) = ∪j≤iX(j). We say that X is a pure complex if all maximal cells (facets) in X are of the same dimension. All the simplicial complexes dealt in this paper are pure. Let Ci = Ci(X,F2) be the space of i-cochains, i.e., {f : X(i) → F2}. It will be sometimes convenient to think of α ∈ Ci as a collection of i-cells and we will denote its cardinality by |α|.

For σ ∈ X(i), we denote

and

c(σ) := |{τ ∈ X(d)|σ ⊆ τ}| (1)

w(σ) :=

c(σ)

. (2)

![image 21](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile21.png>)

d+1 i+1 |X(d)|

Note that σ∈X(i) w(σ) = 1. The weight function w on X(i) deﬁnes a norm on Ci(X,F2) by

||α|| :=

w(σ), (3)

σ∈α

where again we consider α as a collection of i-cells. Note that ||α|| ≤ 1. Let δ = δi : Ci → Ci+1 be the coboundary map, i.e., for σ ∈ X(i + 1)

δi(α)(σ) =

α(τ).

τ⊆σ, dimτ=i

Note that as we are working over F2, we can ignore the issue of orientation. It is easy to see that δi+1 ◦ δi = 0. Denote Bi = Bi(X,F2) and Zi = Zi(X,F2) the i-coboundaries (Imδi−1) and the i-cocycles (Kerδi), respectively. Then, Bi ⊆ Zi and Hi = Hi(X,F2) = Zi/Bi is the (reduced) i-cohomology group over F2.

## 2.3 Notions of minimality

Given a pure simplicial complex X of dimension d and τ a simplex of X, the link Xτ of X at τ is the set of all sets of the form σ \ τ, where σ ∈ X and τ ⊆ σ. Then, Xτ is a complex, with set of vertices X(0) \ τ, of dimension dim(X) − dim(τ) − 1. In particular, for a vertex v, the link Xv of v is of dimension d − 1. A cochain α ∈ Ci(X,F2) deﬁnes a cochain αv ∈ Ci−1(Xv,F2), by αv(σ \ {v}) = α(σ) for every σ ∈ X(i) containing v.

Throughout this paper we assume that our simplicial complexes are homogenous in the following sense: the structure of Xv is independent of v, i.e., the links of all the vertices are isomorphic. In particular |Xv(d − 1)| is independent of v. Under this assumption we have:

- Lemma 2.3. For α ∈ Ci(X,F2), ||α|| = |X1(0)| v∈X


||αv||.

![image 22](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile22.png>)

0

Proof. By our assumption |X(d)| = d+11 |X(0)||Xv(d − 1)|. Now

![image 23](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile23.png>)

cXv(σ)

||αv|| =

w(σ) =

(4)

![image 24](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile24.png>)

d i |Xv(d − 1)|

v∈X(0) σ∈αv

v∈X(0) σ∈αv

v∈X(0)

(i + 1)cX(σ)|X(0)| d i (d + 1)|X(d)|

cX(σ)

(5)

=

=

![image 25](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile25.png>)

![image 26](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile26.png>)

d i

d+1

|X(0)||X(d)|

![image 27](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile27.png>)

σ∈α

σ∈α v∈σ

cX(σ) d+1 i+1 |X(d)|

= |X(0)|

= |X(0)| · ||α||. (6)

![image 28](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile28.png>)

σ∈α

![image 29](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile29.png>)

![image 30](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile30.png>)

![image 31](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile31.png>)

![image 32](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile32.png>)

Let us now discuss few notions of minimality.

- Deﬁnition 2.4. .


- 1. A cochain α ∈ Ci(X,F2) is called minimal if it is of minimal norm in its class modulo Bi(X,F2), i.e., ||α|| ≤ ||α + δi−1γ|| for every γ ∈ Ci−1. This is equivalent to ||α|| = dist(α,Bi) where the distance between a vector α and a subspace W is deﬁned as dist(α,W) = min{||γ|| | α + γ ∈ W}.
- 2. A cochain α ∈ C0(X,F2) will be called locally minimal if it is minimal while for i ≥ 1, α ∈ Ci(X,F2) is called locally minimal if for every vertex v of X, αv is a minimal (i − 1)cochain in Ci−1(Xv,F2).


Every minimal cochain is locally minimal, but not every locally minimal cochain is minimal[2]. To prove coboundary expansion, one can, in principle, consider only minimal cochains. But, in our work, it is crucial that Theorem 1.8 is proved for the more general case of locally minimal cochain. This is used in an essential way in Section 4 to deduce topological expansion for the Ya’s of Theorem 1.3 from the isoperimetric inequalities proved for the Xa’s. Every α ∈ Ci is equivalent modulo Bi to a locally minimal one, in fact, even one which is not too far from it.

- Proposition 2.5. Assume X is a ﬁnite homogeneous pure d-dimensional complex. In particular, every v ∈ X(0) lies in m(i) i-simplicies. Then:


- 1. For every α ∈ Ci(X,F2), there exists a locally minimal α′ ∈ Ci(X,F2) with α′ ≡ αmod Bi(X,F2)),

||α′|| ≤ ||α|| and α′ = α + δi−1(γ) where γ ∈ Ci−1(X,F2) with ||γ|| ≤ c||α||, where c = d+1−i

![image 33](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile33.png>)

i+1 m(i − 1).

- 2. If for some i ≤ d, c(σ) (see Equation (1) in Section 2.2) is constant on the simplicies σ ∈ X(i),


then for α ∈ Ci(X,F2), ||α|| is the normalized counting norm, i.e., ||α|| = |X|α(i|)|. If α is also locally minimal, then for every vertex v ∈ X(0), if we consider αv as a set of (i-1)- cells in

![image 34](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile34.png>)

Xv(i − 1), we have |αv| ≤ |Xv(2i−1)|. Note, if X is homogenous them c(v) is constant on vertices but not necessarily so for i-cells.

![image 35](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile35.png>)

Proof. If α is locally minimal there is nothing to prove. If not, then for some v, ||αv+γ|| < ||αv|| for some γ ∈ Bi−1(Xv,F2). Deﬁne γ˜ ∈ Ci(X,F2) by γ˜(σ) = 0 if v ∈/ σ and γ˜(σ) = γ(σ \ {v}) if v ∈ σ, where σ ∈ X(i). One can easily check that γ˜v = γ. As γ ∈ Bi−1(Xv,F2), we have γ˜ ∈ Bi(X,F2), in fact, if γ = δi−2(η) for some η ∈ Xv(i−2), then γ˜ = δi−1(˜η). Now, replace α by α+ ˜γ. By doing so, α + γ˜ ≡ α(mod Bi(X,F2)). Moreover, ||α + γ˜|| < ||α||. It is clear that ||(α + γ˜)v|| < ||αv||, but some care is needed (and we can not just apply Lemma 2.3) as γ˜ also inﬂuences other vertices. But, adding γ˜ changes the value of α only on simplicies which contain the vertex v, and on them it decreases their contribution to the norm of α, i.e.,

w(σ) <

w(σ),

v∈σ∈α

v∈σ∈α+˜γ

and hence ||α + γ˜|| < ||α||.

The above process terminates since ||α|| can get only ﬁnitely many values, so eventually we replace α by a locally minimal cochain in the same class modulo Bi(X,F2). In fact, the process terminates after at most di+1+1 |X(d)| · ||α|| steps, since for every i-cochain in Ci(X,F2), its norm is an integral multiply of 1

(di+1+1)|X(d)|. In each step the local change is by γ˜ = δ(˜η), and the norm of η˜ is at most m(i−1)

![image 36](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile36.png>)

(d+1i )|X(d)|. The number of steps is at most di+1+1 |X(d)|·||α|| and so the total change γ is of norm at most d+1i+1−im(i−1)||α||.

![image 37](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile37.png>)

![image 38](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile38.png>)

For the proof of the second part, note ﬁrst that w(σ) is constant on X(i) and σ∈X(i) w(σ) = 1 and hence the norm on Ci(X,F2) is simply the normalized counting norm. Now, we also have

that all the (i − 1)-cells of Xv have the same weight in Xv. If α ∈ Ci(X,F2) is locally minimal and for some v ∈ X(0), αv contains more than half of the (i − 1)-cells of Xv, then for some τ ∈ Xv(i − 2), αv contains more than half of the (i − 1)-cells in Xv containing τ. This implies that ||αv + δi−2(τ)|| < ||αv|| in contradiction to the minimality of αv, i.e., in contradiction to the local minimality of α.

![image 39](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile39.png>)

![image 40](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile40.png>)

![image 41](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile41.png>)

![image 42](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile42.png>)

# 3 Buildings and Ramanujan complexes

In this section we review some notations and results on buildings and their quotients and prepare some technical results to be used later. We start with spherical buildings.

## 3.1 Spherical buildings

Let W = Frq be an r-dimensional vector space over the ﬁnite ﬁeld of order q. Denote by S(r,q) the spherical building associated with PGLr(Fq), i.e., the ﬂag complex of Frq. This is the simplicial complex whose vertices are all the non-zero proper subspaces of W, and i + 1 such subspaces u0,··· ,ui form an i-cell if u0 < u1 < ··· < ui. This is a ﬁnite simplicial complex of dimension

- r − 2, which is known to be homotopic to a bouquet of (r − 2)-dimensional spheres. In particular,


Hi(S(r,q),F2) = 0 for every i = 1,··· ,r − 3. It was shown by Gromov that these complexes have the overlapping properties [9, p. 457], showing along the way that they are coboundary expanders.

Theorem 3.1. There exists some constant ǫ(r) > 0 such that ǫi(S(r,q)) ≥ ǫ(r) for every i = 0,··· ,r − 1 and every prime power q.

For a proof of Theorem 3.1 see [20]. We will need only the case r = 4 and i = 1. But, we will need few more facts on S(r,q) for small values of r. Let S(r,q)(1) be the 1-skeleton of S(r,q), i.e., the graph whose vertices are the non-zero proper subspaces of Frq with two such subspaces are incidence iﬀ one is contained in the other. For r = 3 this is the well studied ”points versus lines graph” of the projective plane. This is a (q + 1)-regular graph whose eigenvalues (of the adjacency matrix) are ±(q + 1) and ±

√q, the later with high multiplicity. In particular, these are Ramanujan graphs (of unbounded degree). For r > 3, S(r,q)(1) is not regular anymore. Let us look closely at the case r = 4.

![image 43](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile43.png>)

Let Z = S(4,q)(1) be the 1-skeleton of the spherical building of F4q, i.e., Z is the graph whose set of vertices is M = M1 ∪ M2 ∪ M3 where Mi is the set of subspaces of F4q of dimension i. Note that

q4−1

q−1 ·qq3−−11

|M1| = |M3| = qq4−−11 = q3 + q2 + q + 1 while |M2| =

q+1 ∼ q4. Two vertices are connected by an edge if one subspace is contained in the other. One easily checks that every vertex in M1 (resp. M3) is connected with q2 + q + 1 vertices in M2 and with q2 + q + 1 vertices in M3 (resp. M1), so its degree is 2(q2 +q +1). On the other hand, the degree of a vertex in M2 is 2(q +1), half of them go to M1 and half to M3.

![image 44](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile44.png>)

![image 45](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile45.png>)

![image 46](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile46.png>)

![image 47](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile47.png>)

The following technical lemma will be needed in Section 7.

- Lemma 3.2. Let T = T1 ∪ T2 ∪ T3 ⊆ M be a subset of the vertices of Z with Ti ⊆ Mi. Assume


that with every t ∈ T, a set of edges E(t), coming from t, is given and let E˜ = t∈T E(t). Assume also

- • |T1|,|T3| ≤ q2.75 and |T2| ≤ q3.7.
- • for t ∈ T1 ∪ T3, |E(t)| > q1.8 and for t ∈ T2, |E(t)| > q0.9.


Then,

|E(T,T)| |E˜|

= oq(1). (7)

![image 48](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile48.png>)

I.e, there exists ǫ(q) with ǫ(q) → 0 when q → ∞, s.t. for every choice of T and {E(t)|t ∈ T} as above, |E(|T,TE˜| )| ≤ ǫ(q).

![image 49](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile49.png>)

Proof. As Z is a 3-partite graph, E(T,T) = E(T1,T2) ∪ E(T2,T3) ∪ E(T1,T3). It suﬃces to prove (7) for each E(Ti,Tj) separately. We can therefore consider the graphs Zi,j, 1 ≤ i < j ≤ 3 where Zi,j is the bipartite graph whose vertices are Mi ∪ Mj and the adjacency relation is as in Z. Note that Z1,2 and Z2,3 are isomorphic and to prove the result for one is like to prove the result for the other. So, we will prove it only for Z1,2 and Z1,3.

Lemma 3.3.

- 1. Let A be the adjacency matrix of the graph Z1,3. Then its eigenvalues are ±(q2 +q+1), each with multiplicity 1, and ±q with high multiplicity.
- 2. Let A be the adjacency matrix of the graph Z1,2. Then, its largest eigenvalue is (q + 1)(q2 + q + 1) and the other eigenvalues are either ± q2 + q or 0.


![image 50](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile50.png>)

![image 51](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile51.png>)

BBt 0 0 BtB

0 B Bt 0

and hence A2 =

Proof. The matrix A has a block form A =

. The

eigenvalues of BtB and BBt are the same up to multiplicities of zeros. It suﬃces therefore to analyze BtB. This is the adjacency matrix of the graph Y with vertex set M1 and two subspaces u and w in M1 are connected by t edges if in the original graph there are t paths of length 2 from u to w. Let us now consider separately the two cases.

- (1) In Z1,3, a subspace u goes to itself in q2 + q + 1 2-paths according to its degree in Z1,3. While if u = w, then u and w are contained in q + 1 subspaces of dimension 3. Hence, BBt = (q2 + q + 1)I + (q + 1)(I − J) = q2I + (q + 1)J, where J is the all 1’s matrix. Now J acts as the

zero matrix on L20(M1) = {f : M1 → R| u∈M1 f(u) = 0} and as |M1|I on the constant functions. Thus, the eigenvalues of BtB are q2 + (q + 1)(q3 + q2 + q + 1) = (q2 + q + 1)2 and q2 as claimed,

and the same for BBt.

- (2) This time B and Bt are not square matrices but the argument is similar. In Z1,2 a subspace u in M1 is connected to itself in q2 + q + 1 2-paths. Two diﬀerent 1-dimensional subspaces are inside a unique two dimensional subspace and hence BBt = (q2 + q + 1)I + (J − I) = (q2 + q)I + J.


Arguing as in part one we deduce that the eigenvalues of BBt are (q2 + q + 1)(q + 1) and (q2 + q). Thus, the eigenvalues of A are either ± (q2 + q + 1)(q + 1), ± q2 + q or 0.

![image 52](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile52.png>)

![image 53](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile53.png>)

![image 54](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile54.png>)

![image 55](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile55.png>)

![image 56](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile56.png>)

![image 57](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile57.png>)

We are ready now to apply Proposition 2.2 for the graphs Z1,3 and Z1,2. Let us start with G = Z1,3. I.e., A = T1, B = T3 and by Lemma 3.3 (1), λ(G) = q. Note, k′ = k′′ = q2 + q + 1 ≈ q2 and V ′ = V ′′ ≈ q3. By Proposition 2.2,

q2|A||B| q3

+ q |A||B| = |A||B| q

![image 58](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile58.png>)

![image 59](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile59.png>)

+ q |A||B|.

E(A,B) ≤

![image 60](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile60.png>)

![image 61](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile61.png>)

On the other hand, up to a factor of 2, we have |E˜| ≃

|E(t)| ≥ q1.8|A| + q1.8|B|.

t∈T1∪T3

Let us separate into two cases: |A| < |B| and |A| ≥ |B|. In the ﬁrst case,

|B2|

![image 62](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile62.png>)

q + q |B||B| q1.8|B|

|E(A,B)| |E˜|

= |B| q2.8

1 q0.8

![image 63](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile63.png>)

≤

+

.

![image 64](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile64.png>)

![image 65](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile65.png>)

![image 66](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile66.png>)

![image 67](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile67.png>)

As |B| = |T3| was assumed to be less than q2.75, the ratio goes to 0 with q → ∞ as needed. The second case, i.e., |A| ≥ |B| is symmetric.

Let us now consider the second graph G = Z1.2, A = T1, B = T2, k′ = q2 + q + 1, k′′ = q + 1, V ′ ≈ q3, V ′′ ≈ q4 and by Lemma 3.3(2), λ(G) ≤ 2q. Thus,

![image 68](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile68.png>)

q3|A||B| q7

+ 2q |A||B| = |A||B| q2

![image 69](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile69.png>)

![image 70](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile70.png>)

E(A,B) ≤

+ 2q |A||B|.

![image 71](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile71.png>)

![image 72](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile72.png>)

![image 73](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile73.png>)

while

|E˜| ≃

|E(t)| ≥ q1.8|A| + q0.9|B|.

t∈T1∪T2

Again, we separate the evaluation to two cases: q1.8|A| < q0.9|B| and q1.8|A| ≥ q0.9|B|. In the ﬁrst case |A| < q−0.9|B|, Thus:

q−0.9|B|2

![image 74](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile74.png>)

q2 + 2q q−0.9|B||B| q0.9|B|

|E(A,B)| |E˜|

= |B| q3.8

2q q1.35

![image 75](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile75.png>)

≤

+

.

![image 76](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile76.png>)

![image 77](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile77.png>)

![image 78](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile78.png>)

![image 79](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile79.png>)

As |B| < q3.7, this goes to 0 when q → ∞. The second case we consider is when q1.8|A| ≥ q0.9|B|, so |B| ≤ q0.9|A|. Thus,

q0.9|A|2

![image 80](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile80.png>)

q2 + 2q q0.9|A||A| q1.8|A|

2q1.45 q1.8

= |A| q2.9

|E(A,B)| |E˜|

![image 81](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile81.png>)

≤

+

.

![image 82](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile82.png>)

![image 83](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile83.png>)

![image 84](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile84.png>)

![image 85](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile85.png>)

As |A| < q2.75, this goes to 0 when q → ∞. Lemma 3.2 is now proven.

![image 86](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile86.png>)

![image 87](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile87.png>)

![image 88](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile88.png>)

![image 89](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile89.png>)

## 3.2 Bruhat-Tits buildings and Ramanujan complexes

Let us move now to the Bruhat-Tits buildings. Let F be a non-archimedean local ﬁeld, i.e., F is either a ﬁnite extension of Qp or F = Fq((t)), O its valuation ring, m the unique maximal ideal in O, π - a generator of m (”uniformaizer”), so m = πO and O/m = Fq. The Bruhat-Tits building

- B = A˜d(F) is an inﬁnite simplicial complex deﬁned as follows. An O-lattice L of V = Fd+1 is a ﬁnitely generated O-submodule of V which spans V . Two such lattices L1 and L2 are equivalent if there exists 0 = t ∈ F such that tL1 = L2. The vertices of A˜d(F) are the equivalence classes of these lattices and [L0],[L1],··· ,[Li] form an i-cell if there exist representatives L′i ∈ [Li] s.t. πL′0 < L′i < ··· < L′2 < L′1 < L′0. This is a contractible simplicial complex of dimension d, upon which the group G = PGLd+1(F) acts and the action is transitive on the vertices. The 1-skeleton B(1) of B is a k-regular graph where k equals the number of non-zero proper subspaces of Fdq+1


(d+1)2

(so for d = 1, B is the (q + 1)-regular tree and for general d, k = di=1 d+1i q ≈ q

4 ). In fact, the link of every vertex v of B is isomorphic to the spherical building S(d + 1,q), which is a ﬁnite simplicial complex of dimension d− 1. The local properties of B can be read, therefore, from S(d + 1,q). For example, every (d − 1)-cell in B is contained in exactly (q + 1) d-cells of B.

![image 90](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile90.png>)

The vertices of B come with a coloring τB in Z/(d + 1)Z, deﬁned as follows. Take an O-basis

- B for a representative L′ of [L] and denote τ([L]) = val(detB)(mod(d + 1)). This is well deﬁned and no adjacent vertices have the same color. This coloring is preserved by the action of G0 = PSLd+1(F) · PGLd+1(O), which is a normal subgroup of index d + 1 in G, but not by that of G. Still, τ induces a coloring on the oriented edges of B: τ([L1],[L2]) = τ([L1])−τ([L2])(mod(d+1)), and this coloring of the edges is preserved by G. The coloring of the (oriented) edges deﬁnes d ”Hecke operators” A1,··· ,Ad as follows: For f ∈ L2(B(0)),


Ai(f)(x) = {f(y)|(x,y) ∈ B(1),τ((x,y)) = i}.

The operators Ai are normal (though not self adjoint) and commute with each other, hence can be diagonalized simultaneously.

Every cocompact discrete subgroup Γ of G acts on B and X = Γ\B is a ﬁnite complex. For simplicity we will assume that for every vertex x of B and every 1 = γ ∈ Γ, dist(γx,x) > 2. This ensures that there are no ramiﬁcations and Γ\B is indeed a simplicial complex. This can always be achieved by replacing Γ by a ﬁnite index subgroup (and by a congruence one if Γ is arithmetic).

Since G (and hence Γ) preserves the coloring of the oriented edges, the operator Ai is well deﬁned also on L2(X(0)). In [21], the ﬁnite complex X is called Ramanujan if the ”non trivial spectrum” of (A1,··· ,Ad) on L2(X(0)) (which is a subset of Cd) is contained in the spectrum of (A1,··· ,Ad) acting on L2(B(0)) - see there for exact deﬁnitions. The trivial spectrum consists, in general, of at most d eigenvalues. More precisely, if ΓG0 is of index r in G then Γ\B has r ”trivial eigenvalues” (see [21, Section 2.3 and Proposition 6.7]. For example, for d = 1, it has either two trivial eigenvalues, if Γ\B is a bipartite graph, or just one, if it is not. Similarly, if Γ ≤ G0, there are d + 1 trivial eigenvalues or just one if ΓG0 = G. To avoid the trouble of handling the trivial eigenvalues, we will work all the time with ”non-partite Ramanujan complexes”, i.e., those obtained by lattices Γ with ΓG0 = G. By [21, Theorem 7.1] there are inﬁnitely many such ﬁnite quotients

- X = Γ\B. What is important for us here is the following: A1 + ··· + Ad is acting on L2(X(0)) exactly as


(d+1)2

the adjacency matrix of the graph X(1) which is a k-regular graph with k ∼ q

4 . From the deﬁnition of Ramanujan complexes we deduce [21]:

![image 91](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile91.png>)

- Corollary 3.4. If X is a non-partite Ramanujan complex, a quotient of B = A˜d(F), d ≥ 1, as above, then the second largest eigenvalue of the adjacency matrix of X(1) is bounded from above by


√

√

(d+1)2

d+1 ⌊d+12 ⌋

8 and thus λ1(X(1)) ≥ k − (d + 1)d+1

k ≤ (d + 1)d+1q

![image 92](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile92.png>)

![image 93](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile93.png>)

k, (see Proposition 2.1) so as graphs, for q large w.r.t. d, X(1) is almost a Ramanujan graph. If d = 2 an improved bound is known: λ1(X(1)) ≥ k − 6

![image 94](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile94.png>)

![image 95](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile95.png>)

√

![image 96](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile96.png>)

k.

From spectral point of view, Ramanujan complexes are excellent high dimensional expanders, but they are not necessarily ”coboundary expanders” in the sense of Deﬁnition 1.4. Indeed, if ǫi(X) > 0 then Hi(X,F2) = 0 but we have the following.

- Proposition 3.5. For every d ≥ 1 and every prime power q, there are inﬁnitely many Ramanujan complexes X, quotients of A˜d(Fq((t))), with H1(X,F2) = 0.


Proof. As shown in [21], for F = Fq((t)), and for every ﬁxed d, there is an arithmetic lattice Γ0 < PGLd+1(F) with inﬁnitely many congruence normal subgroups Γi ✁ Γ0 such that Γ0/Γi ≃ PSLd+1(qsi) with si → ∞, and Γi\A˜d(F) is a Ramanujan complex.

Let S2 be the 2-Sylow subgroup of PSLd+1(qsi) and Γ˜i its preimage in Γ0. Then, X = Γ˜i\B, being a quotient of a Ramanujan complex, is also Ramanujan. But,

Γ˜i/([Γ˜i,Γ˜i]Γ˜2i) ։ S2/([S2,S2]S22) = {0}.

As B is contractible,

H1(X,F2) = H1(Γ˜i\B,F2) = H1(Γ˜i,F2) = Γ˜i/([Γ˜i,Γ˜i]Γ˜2i) = {0}, and the proposition is proved.

![image 97](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile97.png>)

![image 98](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile98.png>)

![image 99](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile99.png>)

![image 100](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile100.png>)

A similar result hold also for the second cohomology group.

- Proposition 3.6. For every d ≥ 2 and every prime power q, there exist Ramanujan complexes X, quotients of A˜d(Fq((t))) with H2(X,F2) = 0.


We will prove ﬁrst a purely group theoretic result which may be of independent interest.

- Proposition 3.7. Let Γ be a discrete group, Γˆ its proﬁnite completion and Γpˆ its pro-p completion.


(We do not assume that Γ is residually ﬁnite nor residually-p, so Γ may not inject into Γˆ or Γpˆ). Then

- 1. If H2(Γˆ,Fp) = 0 then H2(Γ,Fp) = 0.
- 2. If H2(Γpˆ,Fp) = 0 then H2(Γ,Fp) = 0.


Proof. As it is well known, for every discrete or proﬁnite group G, H2(G,Fp) classiﬁes equivalent classes of central (continuous) extensions E of G by Fp ( [30, Theorem 6.8.4])

1 → Fp → E → G → 1. (8) Now, H2(G,Fp) = 0 means that every central extension as (8) splits. Assume there is a non-splitting extension

1 → Fp → E −→η Γˆ → 1. (9)

Let E0 = {(a,b) ∈ Γ × E| i(a) = η(b)} where i : Γ → Γˆ is the natural map from Γ to its proﬁnite completion. This gives rise to an extension

1 → Fp → E0 −→π Γ → 1. (10)

where π(a,b) = a for (a,b) ∈ E0. Indeed, π is an epimorphism as for every a ∈ Γ, there exists b ∈ E with η(b) = i(a) since η is an epimorphism from E onto Γ.ˆ Moreover, ker(π) = {(a,b) ∈ E0| a = e} = {(e,b)| η(b) = eΓˆ} ≃ Fp. We claim that (10) is not a splitting sequence. Otherwise, there exists π′ : Γ → E0 with π ◦ π′ = idΓ. Thus, there exists π′ : Γˆ → Eˆ0. But, it it easy to see that Eˆ0 ≃ E and such π′ would split (9), a contradiction. This proves (1). The proof of (2) is similar, replacing proﬁnite completion by pro-p completion.

![image 101](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile101.png>)

![image 102](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile102.png>)

![image 103](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile103.png>)

![image 104](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile104.png>)

We can now prove Proposition 3.6:

Proof. Let Γ = Γ˜i be as in the proof of Proposition 3.5. As shown there Γ has a non-trivial ﬁnite quotient of 2-power order. Thus, its pro-2 completion is not the trivial group. It is also not a free pro-p group since Γ has property(T) (note d + 1 ≥ 3) and hence Γ/[Γ,Γ] is ﬁnite. Thus a minimal presentation of the ﬁnitely generated pro-2 group Γˆ2 requires at least one relation and hence by [30, Theorem 7.8.3] H2(Γˆ2,F2) = 0. We can apply now Proposition 3.7 to deduce that H2(Γ,F2) = 0. As in the proof of Proposition 3.5, we can conclude that H2(X,F2) = 0.

![image 105](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile105.png>)

![image 106](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile106.png>)

![image 107](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile107.png>)

![image 108](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile108.png>)

We formulate Proposition 3.5 and Proposition 3.6 in the way which is most interesting for us, i.e., showing that Ramanujan complexes are not necessarily coboundary expanders. But, in fact, the proofs show that for every cocompact lattice Γ in PGLd+1(F), d ≥ 2, has a ﬁnite index subgroup Γ′ with H1(Γ′,F2) = 0 and H2(Γ′,F2) = 0. We do not know if analogues results are valid for Hi, for i ≥ 3 (and d ≥ i). Our proofs of Proposition 3.5 and Proposition 3.6 use the explicit group theoretic interpretation of the ﬁrst and second cohomology groups. No such explicit interpretation is known for Hi, i ≥ 3.

# 4 From Isoperimetric inequalities to topological expanders

In this section we show that the isoperimetric inequalities of Theorem 1.8 imply Theorem 1.3. The connection is via (an extended version of) Gromov’s Theorem, Theorem 1.7.

So, we ﬁx now a very large prime power q and write F = Fq((t)), B = A3(F) the 3-dimensional Bruhat-Tits building associated with PGL4(F), X a non-partite Ramanujan quotient of B and

- Y = X(2), the 2-skeleton of X. In [22], it was shown that there are inﬁnitely many such X’s with |X| → ∞. Our goal is to show that the 2-dimensional simplicial complex Y has the ǫ-topological overlapping property for some ǫ > 0, depending maybe on q, but not on X or Y . This will prove Theorem 1.3 and answers Gromov’s question in the aﬃrmative as every vertex of Y is contained in at most O(q5) 2-cells.


To this end, we should show now that Y satisﬁes the assumption of Theorem 1.7. Here d = 2 and we have to show that µi(Y ), i = 0,1 are bounded from above and systi(X), i = 0,1 are bounded from below.

Let us start with the systole. As Y (1) = X(1) is connected, H0(Y,F2) = 0 and so syst0(Y ) = ∞ and this case is trivial. The argument for syst1(Y ) is more involved. Here, it is possible that H1(Y,F2) = H1(X,F2) is non zero (see Proposition 3.5). So, let α ∈ Z1(Y,F2) \ B1(Y,F2). If α is not locally minimal, then by Proposition 2.5(1) we can replace it by a locally minimal α′ with ||α′|| ≤ ||α|| and α′ ≡ α(mod Bi), so α′ is also in Z1(Y,F2) \ B1(Y,F2). Thus, to prove the lower bound on syst1(Y ), we can assume α is locally minimal and we claim now that ||α|| > η1, for the η1 of Theorem 1.8. If not, then by that theorem, ||δ1(α)|| ≥ ǫ1||α||. But, α ∈ Z1, so δ1(α) = 0 and hence α = 0, in contradiction to the assumption that α ∈/ B1.

We now turn to prove upper bounds on the ﬁlling norms µ0 and µ1 of Y . Let β ∈ Bi+1(Y,F2), i = 0 or i = 1, so β = δi(α) for some α ∈ Ci(X,F2). We claim that one can choose such α with

2 − i i + 2

1 ηi+1

||α|| ≤ µi||β||, µi = max(

,

m(i)) (11)

![image 109](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile109.png>)

![image 110](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile110.png>)

where ηi+1 is the one from Theorem 1.8 and m(i) is the one from Proposition 2.5, i.e., the number of i-cells containing a vertex. To see this, assume ﬁrst ||β|| > ηi+1. As we always have ||α|| ≤ 1, (11) clearly holds, so assume ||β|| ≤ ηi+1. Apply Proposition 2.5(1) for Y whose dimension is 2 and for i + 1: we can replace β by a locally minimal β′ with β′ ≡ β( mod Bi+1), so β′ is also a coboundary, ||β′|| ≤ ||β||, so ||β′|| ≤ ηi+1 and furthermore β′ = β + δi(γ) where γ ∈ Ci(X,F2) with ||γ|| ≤ ci||β|| when ci = 2i+2−im(i). Here m(i) is 1 when i = 0 and O(q4) for i = 1.

![image 111](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile111.png>)

As β′ is locally minimal in Ci+1(Y,F2) = Ci+1(X,F2) 1 and ||β′|| ≤ ηi+1, Theorem 1.8 implies that ||δi+1(β′)|| ≥ ǫi+1||β′||. But, β′ ∈ Bi+1(Y,F2) = Bi+1(X,F2) ⊆ Zi+1(X,F2) so δi+1(β′) = 0 and hence β′ = 0. Thus, β = δi(γ) and again (11) is valid and Theorem 1.3 is proved.

Remark 4.1. The reader should note that in order to prove that µ1 is bounded from above, we have used δ2 : C2(X,F2) → C3(X,F2), i.e., we have used the 3-dimensional complex X even though our result is for the 2-dimensional complex Y . This is the crucial point which enables us to prove Theorem 1.3 for Y , while we do not know the topological overlapping property for 2-dimensional Ramanujan complexes.

We ﬁnally note that the method of proof gives also a systolic inequity for X as above:

- Corollary 4.2. Let X be a non-partite Ramanujan complex of dimension 3 as above. Then for i = 0,1,2, systi(X) ≥ νi for some constants νi > 0.


![image 112](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile112.png>)

1Note that the norms in Ci+1(Y, F2) and Ci+1(X, F2) are the same since every 2-cells of X is contained in exactly (q + 1) 3-cells of X

Proof. For i = 0, H0(X) = 0 and there is nothing to prove and for i = 1, syst1(X) = syst1(Y ) where Y = X(2) and this was proved above. For i = 2, we can argue in a similar way as before: if α ∈ Z2 \ B2 (such α can exist - see Proposition 3.6) we can replace it by a locally minimal one α′ and argue as before to deduce that ||α′|| ≥ η2.

![image 113](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile113.png>)

![image 114](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile114.png>)

![image 115](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile115.png>)

![image 116](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile116.png>)

# 5 Expansion of 1-cochains in 2-dimensional Ramanujan complexes

In this section we prove Theorem 1.9. We note that in this case every vertex (edge) is in a constant number of triangles so the norm (on vertices or on edges) is the normalized counting norm. It will be easier therefore to work here simply with the counting norm |α| and in the end of the proof ”to translate” the result to ||α||.

## 5.1 Proof of Theorem 1.9

So X is a Ramanujan complex of dimension 2. Every vertex v has degree Q = 2(q2 +q+1) and the link Xv at any vertex v is the ”lines versus points” graph of the projective plane P2(Fq), which is a (q + 1)-regular bipartite graph on 2(q2 + q + 1) points. The cochain α can be thought of as a set of edges of X such that |αv| ≤ Q2 for every v, since α is locally minimal (see Proposition 2.5 (2)).

![image 117](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile117.png>)

- Lemma 5.1. For i = 0,1,2,3 denote by ti, the number of triangles of X which contain exactly i edges from α. Then,


- 1. t1 + 2t2 + 3t3 = (q + 1)|α|.
- 2. |δ1(α)| = t1 + t3.
- 3. v∈X(0) |EXv(αv,αv)| = 2t1 + 2t2.


![image 118](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile118.png>)

Here we consider αv, which is the set of edges of α touching v, as a set of vertices of the link Xv. By αv we denote its complement there and EXv(αv,αv) the set of edges from αv to αv.

![image 119](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile119.png>)

![image 120](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile120.png>)

![image 121](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile121.png>)

Proof. For (1) we recall that every edge lies on q + 1 triangles and a triangle which contributes to ti contains i edges from α. Part (2) is simply the deﬁnition of δ1(α), which is the set of all triangles containing an odd number of edges from α. For (3) we argue as follows.

If △ = {v0,v1,v2} is a triangle of X, then it contributes an edge at Xvk ({vk} = {vi,vj,vk}\{vi,vj}). This is the edge between ei,k = (vi,vk) and ej,k = (vj,vk) when we consider ei,k and ej,k as vertices of Xvk. This edge will be in EXv

(αvk,αvk) if and only if exactly one of {ei,k,ej,k} is in α. A case by case analysis of the four possibilities shows that if △ has either 0 or 3 edges from α then △ does not contribute anything to the left hand sum. On the other hand, if it has either 1 or 2 edges, it contributes 2 to the sum. This proves the lemma.

![image 122](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile122.png>)

k

![image 123](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile123.png>)

![image 124](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile124.png>)

![image 125](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile125.png>)

![image 126](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile126.png>)

Fix now a small ǫ > 0 to be determined later and deﬁne:

- Deﬁnition 5.2. A vertex v of X is called thin w.r.t. α if |αv| < (1 − ǫ)Q2 and thick otherwise (recall that by our local minimality assumption, |αv| ≤ Q2 for every v). Denote


![image 127](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile127.png>)

![image 128](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile128.png>)

- • W = {v ∈ V = X(0)| ∃e ∈ α with v ∈ e}.
- • R = {v ∈ W| v thin}.
- • S = {v ∈ W| v thick} = W \ R.


Let r = v∈R |αv| and s = v∈S |αv|.

- Lemma 5.3. r + s = 2|α|

Proof. Every edge in α contributes 2 to the left hand side.

![image 129](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile129.png>)

![image 130](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile130.png>)

![image 131](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile131.png>)

![image 132](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile132.png>)

- Lemma 5.4.

- 1. For every v ∈ V , |EXv(αv,αv)| ≥ 12(q + 1 −

![image 133](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile133.png>)

![image 134](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile134.png>)

√q)|αv|.

![image 135](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile135.png>)

- 2. If v is thin, then |EXv(αv,αv)| ≥ (1+2ǫ)(q + 1 −


![image 136](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile136.png>)

![image 137](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile137.png>)

√q)|αv|.

![image 138](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile138.png>)

Proof. As mentioned in Section 3.1, the link Xv is the ”line versus points” graph of the projective plane. It is a (q + 1)-regular graph whose eigenvalues are ±(q + 1) and ±

√q. Hence, λ1(Xv) = (q + 1) −

![image 139](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile139.png>)

√q. Part 1 now follows from Proposition 2.1, and similarly part 2.

![image 140](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile140.png>)

![image 141](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile141.png>)

![image 142](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile142.png>)

![image 143](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile143.png>)

![image 144](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile144.png>)

We can deduce

- Lemma 5.5. 2t1 + 2t2 ≥ (q + 1 −


√q)r.

√q)|α| + 2ǫ(q + 1 −

![image 145](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile145.png>)

![image 146](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile146.png>)

![image 147](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile147.png>)

Proof.

2t1 + 2t2 =

v∈W

EXv(αv,αv) =

EXv(αv,αv) +

EXv(αv,αv) (12)

![image 148](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile148.png>)

![image 149](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile149.png>)

![image 150](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile150.png>)

v∈R

v∈S

√q)|αv| +

√q)|αv| (13)

(1 + ǫ) 2

- 1

![image 151](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile151.png>)

- 2


(q + 1 −

(q + 1 −

≥

![image 152](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile152.png>)

![image 153](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile153.png>)

![image 154](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile154.png>)

v∈R

v∈S

√q)r +

√q)s (14)

(1 + ǫ) 2

- 1

![image 155](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile155.png>)

- 2


(q + 1 −

(q + 1 −

=

![image 156](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile156.png>)

![image 157](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile157.png>)

![image 158](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile158.png>)

√q)(r + s) +

√q)r (15)

- 1

![image 159](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile159.png>)

- 2


ǫ 2

(q + 1 −

(q + 1 −

=

![image 160](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile160.png>)

![image 161](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile161.png>)

![image 162](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile162.png>)

√q)r (16)

√q)|α| +

ǫ 2

(q + 1 −

= (q + 1 −

![image 163](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile163.png>)

![image 164](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile164.png>)

![image 165](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile165.png>)

- In the ﬁrst equation we have used Lemma 5.1, part (3) and in the last one Lemma 5.3. The


- inequality follows from Lemma 5.4.


![image 166](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile166.png>)

![image 167](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile167.png>)

![image 168](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile168.png>)

![image 169](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile169.png>)

- Lemma 5.6. t1 − 3t3 ≥ 2ǫ(q + 1 −

![image 170](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile170.png>)

√q)r −

![image 171](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile171.png>)

√q|α|.

![image 172](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile172.png>)

- Proof. Subtract equation (1) in Lemma 5.1 from the equation obtained in Lemma 5.5.


![image 173](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile173.png>)

![image 174](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile174.png>)

![image 175](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile175.png>)

![image 176](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile176.png>)

Our goal now is to show that r, the contribution of the thin edges is at least some ﬁxed fraction of |α|. This will prove that for q large enough t1 ≥ cq|α| and this will give the theorem. Up to now we have used only the local structure of X, the links. Now we will use the global structure, the fact that its 1-skeleton is almost a Ramanujan graph.

- Lemma 5.7. The total number of edges in X(1) between the thick vertices is bounded as follows:


1 (1 − ǫ)2(1 + ǫ0)

|EX(1)(S)| ≤ |α|(

+

![image 177](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile177.png>)

12q (1 − ǫ)Q

).

![image 178](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile178.png>)

Proof. Recall, that by Corollary 3.4, the second largest eigenvalue of the adjacency matrix of X(1) is bounded from above by 6q. So λ1(X(1)) ≥ Q − 6q = 2q2 − 4q + 1. Note now that every vertex in S touches at least (1 − ǫ)Q2 edges of α, hence |S| ≤ (12−|αǫ)|Q

= (14−|αǫ)|Q. Proposition 2.1 implies therefore (when |X(0)| = n)

![image 179](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile179.png>)

![image 180](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile180.png>)

![image 181](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile181.png>)

![image 182](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile182.png>)

2

|E(S)| ≤

≤

≤

![image 183](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile183.png>)

|S| n

- 1

![image 184](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile184.png>)

- 2


λ1(X(1)))|S| (17)

(Q −

![image 185](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile185.png>)

![image 186](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile186.png>)

![image 187](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile187.png>)

![image 188](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile188.png>)

|S| n

|S| n

) + 6q|S| n

- 1

![image 189](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile189.png>)

- 2


- 1

![image 190](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile190.png>)

- 2


(Q −

(Q − 6q))|S| =

(Q(1 −

)|S| (18)

![image 191](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile191.png>)

![image 192](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile192.png>)

![image 193](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile193.png>)

(Q|S| n

4|α| (1 − ǫ)n

- 1

![image 194](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile194.png>)

- 2


- 1

![image 195](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile195.png>)

- 2


+ 6q)|S| ≤

+ 6q)|S| (19)

(

![image 196](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile196.png>)

![image 197](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile197.png>)

0) means |α| ≤ 8(1+Qnǫ

Note now that the assumption ||α|| ≤ 4(1+1ǫ

0) and hence,

![image 198](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile198.png>)

![image 199](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile199.png>)

4|α| (1 − ǫ)Q

2Q 8(1 − ǫ)(1 + ǫ0)

|E(S)| ≤ (

+ 3q)

![image 200](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile200.png>)

![image 201](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile201.png>)

1 (1 − ǫ)2(1 + ǫ0)

= |α|(

![image 202](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile202.png>)

12q (1 − ǫ)Q

+

).

![image 203](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile203.png>)

![image 204](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile204.png>)

![image 205](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile205.png>)

![image 206](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile206.png>)

![image 207](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile207.png>)

Proof. (of Theorem 1.9) We can now ﬁnish the proof of Theorem 1.9. Choose ǫ > 0 such that

0)+(1−12ǫq)Q < 1−ξ < 1, for some ξ > 0. This now means by Lemma 5.7 that at most (1 − ξ) of the edges in α are between two thick vertices, namely, for at least ξ|α| edges, one of their endpoints is thin. This implies that r ≥ ξ|α|. Plugging this in Lemma 5.6, we get t1 ≥ (2ǫ(q + 1 −

1

(1−ǫ)2(1+ǫ0) < 1 and then assume that q is suﬃciently large such that (1−ǫ)21(1+ǫ

![image 208](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile208.png>)

![image 209](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile209.png>)

![image 210](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile210.png>)

√q)|α|. Again, if q is large

√q)ξ −

![image 211](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile211.png>)

![image 212](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile212.png>)

![image 213](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile213.png>)

enough this means that |δ1(α)| ≥ t1 ≥ ǫ1q|α|. Now for β ∈ C2(X,F2), ||β|| = |X|β(2)| |. For α ∈ C1(X,F2), ||α|| = (2q|+1)X(2)|α||. Thus, ||δ1(α)|| = |δX1((2)α)| ≥ ǫ1q|α| |X(2)| = ǫ1(qq·3+1)|X(2)|X(2)|·||α| || ≥ ǫ2||α|| for ǫ2 = 3q+1q ǫ1 ≥ 2ǫ1. Theorem 1.9 is now proved.

![image 214](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile214.png>)

![image 215](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile215.png>)

![image 216](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile216.png>)

![image 217](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile217.png>)

![image 218](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile218.png>)

![image 219](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile219.png>)

![image 220](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile220.png>)

![image 221](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile221.png>)

![image 222](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile222.png>)

![image 223](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile223.png>)

The proof is eﬀective. One can estimate ǫ2 and how large should be q, in term of ǫ0. It is independent of q provided q is large enough.

Let us mention that along the way we have proved two facts which are worth formulating separately.

- Corollary 5.8. In the notations and assumptions as above. For every ǫ > 0, if q ≥ q(ǫ) ≫ 0, then we have:


- 1. If α ∈ B1(X,F2) is a locally minimal coboundary with ||α|| < 4(1+1 ǫ) then α = 0.

![image 224](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile224.png>)

- 2. If α ∈ Z1(X,F2) \ B1(X,F2), then ||α|| > 4(1+1 ǫ), In particular, every representative of a non-trivial cohomology class has linear size support.


![image 225](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile225.png>)

This is the systolic inequality promised in Corollary 1.10 of the introduction. Note that by Proposition 3.5, there are indeed cases with H1(X,F2) = {0} so the second item of Corollary 5.8 is a non-vacuous systolic result. Such results are of potential interest also for quantum error-correcting codes (see [10],[32] and the references therein).

# 6 Expansion of i-cochains in 3-dimensional Ramanujan complexes

In this section we prove Theorem 1.8 for the cases i = 0 and i = 1. Let us start with the easier case - vertex expansion.

## 6.1 Proof of Theorem 1.8 for the case i = 0

The case i = 0 of Theorem 1.8 is nothing more than the standard result asserting that X(1) the 1-skeleton of X is an expander graph. But, some care is needed here since the edges of X(1), when considered as edges of a graph get equal weights, but when considered as edges of the 3dimensional complex X, have diﬀerent weights. In fact, a black edge, i.e., one corresponding to the 1 or 3 dimensional subspace in F4q, when we look at the links of its vertices, has Θ-times the weight of a white edge (an edge which corresponds to a 2-dimensional subspace of F4q) when Θ = c

(31)q·(21)q (21)q·(21)q

b 1

= q2q++1q+1 ≈ q since a 1 or 3 dimensional subspace is contained in cb1 = 31 q · 21 q maximal ﬂags in F4q, while a 2-dimensional subspace only in cw1 = 21 q · 21 q such ﬂags.

cw1 =

![image 226](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile226.png>)

![image 227](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile227.png>)

![image 228](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile228.png>)

Let α ∈ C0(X,F2) be a locally minimal 0-cochain of X, i.e., a minimal cochain (see Section 2.3). So, α is a subset of the X(0) - the set of vertices of X - containing at most half of the vertices (since all the vertices have the same weight). By Corollary 3.4, λ1(X(1)) ≥ k − 44

√

![image 229](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile229.png>)

k where k is the degree of the k-regular graph X(1), so k ≈ q4. Now, Proposition 2.1 implies that

|δ0(α)| = |E(α,α¯)| ≥

In terms of norms:

|α||α¯| |X(0)|

(q4 − 44q2) ≥

![image 230](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile230.png>)

- 1

![image 231](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile231.png>)

- 2


(q4 − 44q2)|α|. (20)

c0

||α|| = |α| ·

![image 232](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile232.png>)

4 1 |X(3)|

(21)

where c0 is the number of 3-cells of X containing a vertex v. This number is independent of v, equal to the number of maximal ﬂags in F4q and it is approximately q6. On the other hand, if β := δ0(α), β = βb + βw where βb (resp. βw) is the set of black (resp. white) edges of β, then

1

(cb1|βb| + cw1 |βw|) =

||δ0(α)|| = ||β|| =

![image 233](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile233.png>)

4 2 |X(3)|

Combining, (22), (20) and (21) we deduce:

(q + 1)2

(q + 1)2

(Θ|βb| + |βw|) ≥

|β| =

![image 234](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile234.png>)

![image 235](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile235.png>)

4 2 |X(3)|

4 2 |X(3)|

(q + 1)2

|δ0(α)|(22)

![image 236](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile236.png>)

4 2 |X(3)|

(q + 1)2

(q + 1)2

|δ0(α)| ≥

||δ0(α)|| ≥

![image 237](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile237.png>)

![image 238](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile238.png>)

4 2 |X(3)|

4 2 |X(3)|

(q + 1)2

- 1

![image 239](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile239.png>)

- 2


(q4 − 44q2)|α| =

![image 240](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile240.png>)

4 2 |X(3)|

4 1 |X(3)|

- 1

![image 241](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile241.png>)

- 2


(q4 − 44q2)

c0 ||α|| ≥ ǫ0||α||(23)

![image 242](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile242.png>)

Case i = 0 of Theorem 1.8 is proven, with η0 = 1 and ǫ0 independent of q, since c0 ≈ q6.

## 6.2 Proof of Theorem 1.8 for the case i = 1

The main idea of the proof is similar to the one that was shown in Section 5 for 1-cochains in Ramanujan complexes of dimension 2, but here edges have diﬀerent weights, so more care is needed. Let α ∈ C1(X,F2) be a 1-cochain of a 3-dimensional non-partite Ramanujan Complex X. The cochain α is a collection of edges of two types: black and white as described in Section 3. The black (resp. white) ones, when considered as vertices in the links of their end points, correspond to subspaces of dimension 1 or 3 (resp. 2) in F4q and such an edge is contained in (q2 + q + 1)(q + 1) (resp. (q + 1)2) pyramids. We denote by αb the set of black edges of α and by αw the set of white edges of α.

2

2+q+1)(q+1)

(42)|X(3)| (resp. w(ew) = (q+1)

The weight of a black (resp. white) edge is w(eb) = (q

(42)|X(3)|). Denote Θ = w(e

![image 243](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile243.png>)

![image 244](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile244.png>)

b)

w(ew) = q2q++1q+1 ≈ q. The norm of α is therefore

![image 245](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile245.png>)

![image 246](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile246.png>)

(q + 1)2

(Θ|αb| + |αw|).

||α|| =

![image 247](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile247.png>)

4 2 |X(3)|

It will be convenient in this section to use also the following norm of α:

↑ α ↑= Θ|αb| + |αw|.

If v is a vertex of X, then as before αv is the set of edges of α with one endpoint in v, and αbv (resp. αwv ) are the black (resp. white) ones. They give a 0-cochain αv ∈ C0(Xv,F2) whose norm is

(q2 + q + 1)(q + 1)

|αbv| +

||αv|| =

![image 248](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile248.png>)

3 1 |Xv(2)|

Again, we denote

(q + 1)2

|αwv | =

![image 249](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile249.png>)

3 1 |Xv(2)|

(q + 1)2

(Θ|αbv| + |αwv |).

![image 250](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile250.png>)

3 1 |Xv(2)|

↑ αv ↑= Θ|αbv| + |αwv |. Note that |Xv(2)| depends only on q, in fact, |Xv(2)| = (q3 + q2 + q + 1)(q2 + q + 1)(q + 1) ≈ q6.

Since α is locally minimal, for every vertex v, αv is a minimal cochain of C0(Xv,F2), i.e., αv is minimal in the coset αv + B0(Xv,F2), i.e., ||αv|| ≤ ||αv + 1Xv(0)||. This means that Θ|αbv| + |αwv | ≤

- 1

![image 251](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile251.png>)

- 2(Θ1bX


v(0) + 1wX

v(0)). The righthand side is easily determined:

1bX

v(0) =

4 1 q

+

4 3 q

= 2(q3 + q2 + q + 1) ≈ 2q3.

1wX

v(0) =

(q3 + q2 + q + 1)(q2 + q + 1) (q + 1) ≈ q4.

4 2 q

=

![image 252](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile252.png>)

Thus, Θ|αbv| + |αwv | ≤ 21(Θ2 41 q + 42 q) ≈ 32q4. Denote Q = Θ2 41 q + 42 q ≈ 3q4, so ↑ αv ↑≤ Q2 .

![image 253](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile253.png>)

![image 254](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile254.png>)

![image 255](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile255.png>)

- Lemma 6.1. For i = 0,1,2,3 denote by ti, the number of triangles of X which contain exactly i edges from α. Then,


- 1. t1 + 2t2 + 3t3 = 2(q + 1) ↑ α ↑.
- 2. |δ1(α)| = t1 + t3.
- 3. v∈X(0) |EXv(αv,αv)| = 2t1 + 2t2.


![image 256](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile256.png>)

Proof. For (1) we recall that the number of of triangles that contain a certain black edge is 2 31 q. The number of triangles that contain a certain white edge is 2(q + 1). A triangle that contributes

to ti contain i-edges from α. Thus:

t1+2t2+3t3 = 2

3 1 q

3 1 q|αb|+2(q+1)|αw| = 2(q+1)(

q + 1|αb|+|αw|) = 2(q+1)(Θ|αb|+|αw|) = 2(q+1) ↑ α ↑

![image 257](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile257.png>)

Part (2) follows from the deﬁnitions.

For (3): If △ = {v0,v1,v2} is a triangle of X, then it contributes an edge at Xvk ({vk} = {vi,vj,vk}\{vi,vj}). This is the edge between ei,k = (vi,vk) and ej,k = (vj,vk) when we consider ei,k and ej,k as vertices of Xvk. This edge will be in EXv

(αvk,αvk) if and only if exactly one of {ei,k,ej,k} is in α. A case by case analysis of the four possibilities shows that if △ has either 0 or 3 edges from α then △ does not contribute anything to the left hand sum. On the other hand, if it has either 1 or 2 edges, it contributes 2 to the sum. This proves the lemma.

![image 258](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile258.png>)

k

![image 259](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile259.png>)

![image 260](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile260.png>)

![image 261](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile261.png>)

![image 262](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile262.png>)

Fix now a small ǫ > 0 to be determined later and deﬁne:

- Deﬁnition 6.2. A vertex v of X is called thin w.r.t. α if ↑ αv ↑< (1 − ǫ)Q2 and thick otherwise (recall that by our local minimality assumption, ↑ αv ↑≤ Q2 for every v). Denote


![image 263](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile263.png>)

![image 264](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile264.png>)

- • W = {v ∈ V = X(0)| ∃e ∈ α with v ∈ e}.
- • R = {v ∈ W| v thin}.
- • S = {v ∈ W| v thick} = W \ R.


Let r = v∈R ↑ αv ↑ and s = v∈S ↑ αv ↑.

- Lemma 6.3. r + s = 2 ↑ α ↑

Proof. Every edge in αb contributes 2Θ to the left hand side and every edge of αw contributes 2 to the left hand side. So, r + s = 2Θ|αb| + 2|αw| = 2 ↑ α ↑.

![image 265](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile265.png>)

![image 266](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile266.png>)

![image 267](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile267.png>)

![image 268](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile268.png>)

- Lemma 6.4.


- 1. For every v ∈ V , |EXv(αv,αv)| ≥ (q + 1 −

![image 269](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile269.png>)

√12q) ↑ αv ↑.

![image 270](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile270.png>)

- 2. If v is thin, then |EXv(αv,αv)| ≥ (1 + ǫ)(q + 1 −


√12q) ↑ αv ↑.

![image 271](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile271.png>)

![image 272](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile272.png>)

Proof. Recall (see Section 3.1 and the notations there) that the link graph Xv is a 3-partite graph with parts M1,M2,M3, αv = T1 ∪ T2 ∪ T3 where Ti ⊆ Mi. We have,

4 1 q ≈ q3,

|M1| = |M3| =

while

4 2 q ≈ q4.

|M2| =

Assume now |Ti| = wi|Mi|. In the graph Z1,2: k′ = q2 + q + 1, k′′ = q + 1, the largest eigenvalue is (q + 1)(q2 + q + 1) ≈ q32, the second largest eigenvalue is q2 + q ≈ q + 1. In the graph Z1,3: k′ = k′′ = q2 + q + 1 ≈ q2, the largest eigenvalue is q2 + q + 1 ≈ q2, the second largest eigenvalue is

![image 273](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile273.png>)

![image 274](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile274.png>)

![image 275](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile275.png>)

- q. Using now Proposition 2.2 we have:


q32|T1||T2| q72

![image 276](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile276.png>)

![image 277](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile277.png>)

+ (q + 1) |T1||T2| =

E(T1,T2) ≤

![image 278](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile278.png>)

![image 279](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile279.png>)

1 q3

![image 280](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile280.png>)

(q|T1| · |T2|) + (q + 1) |T1||T2|.

![image 281](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile281.png>)

q23|T3||T2| q72

![image 282](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile282.png>)

![image 283](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile283.png>)

E(T3,T2) ≤

+ (q + 1) |T3||T2| =

![image 284](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile284.png>)

![image 285](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile285.png>)

q2|T1||T3| q3

1 q3

![image 286](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile286.png>)

+ q |T1||T3| =

E(T1,T3) ≤

![image 287](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile287.png>)

![image 288](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile288.png>)

1 q3

![image 289](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile289.png>)

(q|T3| · |T2|) + (q + 1) |T3||T2|.

![image 290](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile290.png>)

![image 291](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile291.png>)

(q|T1| · q|T3|) + q |T1||T3|.

Thus, |EXv(αv,αv)| ≤ q13(q|T1|·|T2|+q|T1|·q|T3|+q|T3|·|T2|)+(q+1)( |T1||T2|+ |T3||T2|+ |T1||T3|). Now using the Maclaurin’s inequality (yz + yw + zw) ≤ 31(y + z + w)2 we get

![image 292](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile292.png>)

![image 293](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile293.png>)

![image 294](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile294.png>)

![image 295](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile295.png>)

![image 296](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile296.png>)

1 q3 ·

1 3

(q|T1| + |T2| + q|T3|)2 + (q + 1)( |T1||T2| + |T3||T2| + |T1||T3|()24) ≤

![image 297](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile297.png>)

![image 298](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile298.png>)

![image 299](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile299.png>)

|EXv(αv,αv)| ≤

![image 300](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile300.png>)

![image 301](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile301.png>)

1 3 ↑ αv ↑2 +3√q( q|T1| · |T2| + q|T3| · |T2| + q|T1| · q|T3|) (25)

1 q3 ·

![image 302](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile302.png>)

![image 303](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile303.png>)

![image 304](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile304.png>)

![image 305](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile305.png>)

1 3 ↑ αv ↑2 + 3q ↑ αv ↑ . (26)

1 q3 ·

![image 306](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile306.png>)

≤

![image 307](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile307.png>)

![image 308](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile308.png>)

Since the degree of a vertex in M2 is 2(q + 1) while for a vertex in M1 ∪ M3 it is 2(q + 1)Θ, we obtain

|EXv(αv,αv)| ≥ 2(q+1) ↑ αv ↑ −q13 ·23 ↑ αv ↑2 −2√3q ↑ αv ↑= (2(q+1)−q13 ·23 ↑ αv ↑ −

√12q) ↑ αv ↑.

![image 309](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile309.png>)

![image 310](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile310.png>)

![image 311](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile311.png>)

![image 312](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile312.png>)

![image 313](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile313.png>)

![image 314](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile314.png>)

![image 315](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile315.png>)

Moreover, since ↑ αv ↑≤ Q2 ≈ 32q4 we get: |EXv(αv,αv)| ≥ (2(q + 1) − q13 · 32 · 32q4 −

![image 316](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile316.png>)

![image 317](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile317.png>)

√12q) ↑ αv ↑,

√12q) ↑ αv ↑≥ (q + 1 −

![image 318](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile318.png>)

![image 319](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile319.png>)

![image 320](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile320.png>)

![image 321](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile321.png>)

![image 322](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile322.png>)

![image 323](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile323.png>)

- and Part 1 of the lemma is proved.

- Now, if v is thin then ↑ αv ↑≤ (1 − ǫ) · Q2 = (1 − ǫ) · 32q4; so in this case:


![image 324](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile324.png>)

![image 325](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile325.png>)

|EXv(αv,αv)| ≥ (2(q + 1) − q13 · 32 · (1 − ǫ) · 32q4 −

![image 326](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile326.png>)

![image 327](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile327.png>)

![image 328](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile328.png>)

![image 329](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile329.png>)

√12q) ↑ αv ↑≥ (1 + ǫ)(q + 1 −

![image 330](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile330.png>)

√12q) ↑ αv ↑,

![image 331](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile331.png>)

- and Part 2 of the lemma is also proved.


![image 332](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile332.png>)

![image 333](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile333.png>)

![image 334](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile334.png>)

![image 335](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile335.png>)

We can deduce the following inequality √12q) ↑ α ↑ +ǫ(q + 1 −

√12q)r.

- Lemma 6.5. 2t1 + 2t2 ≥ 2(q + 1 −


![image 336](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile336.png>)

![image 337](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile337.png>)

Proof. 2t1 + 2t2 =

v∈W

EXv(αv,αv) =

EXv(αv,αv) +

EXv(αv,αv) (27)

![image 338](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile338.png>)

![image 339](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile339.png>)

![image 340](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile340.png>)

v∈R

v∈S

![image 341](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile341.png>)

![image 342](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile342.png>)

≥

(1 + ǫ)(q + 1 − 12q) ↑ αv ↑ +

(q + 1 − 12q) ↑ αv(28)↑

v∈R

v∈S

![image 343](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile343.png>)

![image 344](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile344.png>)

= (1 + ǫ)(q + 1 − 12q)r + (q + 1 − 12q)s (29) = (q + 1 − 12q)(r + s) + ǫ(q + 1 − 12q)r (30) = 2(q + 1 − 12q) ↑ α ↑ +ǫ(q + 1 − 12q)r (31)

![image 345](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile345.png>)

![image 346](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile346.png>)

![image 347](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile347.png>)

![image 348](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile348.png>)

- In the ﬁrst equation we have used Lemma 6.1, part (3) and in the last one Lemma 6.3. The


- inequality follows from Lemma 6.4. √12q)r − 2√12q ↑ α ↑.


![image 349](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile349.png>)

![image 350](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile350.png>)

![image 351](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile351.png>)

![image 352](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile352.png>)

- Lemma 6.6. t1 − 3t3 ≥ ǫ(q + 1 −


![image 353](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile353.png>)

![image 354](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile354.png>)

- Proof. Subtract equation (1) in Lemma 6.1 form the equation obtained in Lemma 6.5.


![image 355](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile355.png>)

![image 356](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile356.png>)

![image 357](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile357.png>)

![image 358](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile358.png>)

Our next goal now is to show the existence of η1 > 0, such that for every α with ||α|| ≤ η1, the contribution r of the thin edges, is at least some ﬁxed fraction of ↑ α ↑. This will prove that for q large enough t1 ≥ cq ↑ α ↑, and the case i = 1 of Theorem 1.8 will follow with a constant ǫ1, which is independent of q (for all q ≫ 0). Indeed,

4 2 |X(3)|

cq2 ↑ α ↑ 4|X(3)|

q · t1(α) 4|X(3)|

1 4|x(3)|

(q + 1)(t1(α) + t3(α)) 4 3 |X(3)|

(q + 1)2 · cq2||α|| ≥ ǫ1||α||,

≥

·

≥

||δ1(α)|| =

=

![image 359](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile359.png>)

![image 360](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile360.png>)

![image 361](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile361.png>)

![image 362](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile362.png>)

![image 363](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile363.png>)

for a suitable constant ǫ1 ≥ 0 Up to now we have used only the local structure of X. Now we will use the global structure; the fact that its 1-skeleton is an almost Ramanujan graph. Recall, that by Corollary 3.4, the second largest eigenvalue of the adjacency matrix of X(1) is bounded from above by (d + 1)d+1

√

![image 364](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile364.png>)

k ≈ 44 q4 = 44q2. Now the degree of a vertex is k ≈ q4 so

![image 365](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile365.png>)

λ1(X(1)) ≥ q4 − 44q2. Note now that for every vertex in S we have ↑ αv ↑≥ (1 − ǫ)Q2 . So, every v ∈ S either touches at least (1−ǫ)q

![image 366](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile366.png>)

3

4

2 white edges or at least (1−ǫ)q

2 black edges. Let us denote by Sb the vertices in which the ﬁrst case occurs and by Sw the vertices in which the second case occurs (it could be that both cases occur at v). Then |Sb| ≤ 2|α

![image 367](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile367.png>)

![image 368](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile368.png>)

w|

b|

(1−ǫ)q3/2 and |Sw| ≤ 2|α

(1−ǫ)q4/2. Thus, |Sb ∪ Sw| ≤ |Sb| + |Sw| ≤ 2q|α

![image 369](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile369.png>)

![image 370](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile370.png>)

w|

b|

(1−ǫ)q·q3/2 + 2|α

(1−ǫ)q4/2 = (1−ǫ2)q4/2(q|αb| + |αw|) ≤ (1−4ǫ)q4 ↑ α ↑. Hence |S| ≤ (14−↑αǫ)↑q4. Let n := |V | = |X(0)|, we have,

![image 371](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile371.png>)

![image 372](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile372.png>)

![image 373](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile373.png>)

![image 374](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile374.png>)

![image 375](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile375.png>)

|E(S)| ≤

≤

≤

![image 376](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile376.png>)

|S| n

- 1

![image 377](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile377.png>)

- 2


(q4 −

λ1(X(1)))|S| (32)

![image 378](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile378.png>)

![image 379](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile379.png>)

![image 380](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile380.png>)

![image 381](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile381.png>)

) + 44q2|S| n

|S| n

|S| n

- 1

![image 382](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile382.png>)

- 2


- 1

![image 383](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile383.png>)

- 2


(q4 −

(q4 − 44q2))|S| =

(q4(1 −

)|S| (33)

![image 384](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile384.png>)

![image 385](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile385.png>)

![image 386](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile386.png>)

(q4|S| n

4 ↑ α ↑ (1 − ǫ)n

- 1

![image 387](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile387.png>)

- 2


- 1

![image 388](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile388.png>)

- 2


+ 44q2)|S| ≤

+ 44q2)|S| (34)

(

![image 389](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile389.png>)

![image 390](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile390.png>)

2

(42)|X(3)| ↑ α ↑ and |X(3)| ≈ n·4q6, we have,

Note that we assumed that ||α|| ≤ η1. As ||α|| = (q+1)

![image 391](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile391.png>)

![image 392](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile392.png>)

↑ α ↑≤

3 2

η1q4n.

![image 393](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile393.png>)

Hence,

|E(S)| ≤

≤ (

≤ (

432η1q4n (1 − ǫ)n

- 1

![image 394](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile394.png>)

- 2


![image 395](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile395.png>)

+ 44q2)|S| (35)

(

![image 396](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile396.png>)

3η1q4 (1 − ǫ)

4 ↑ α ↑ (1 − ǫ)q4

+ 128q2)

(36)

![image 397](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile397.png>)

![image 398](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile398.png>)

512 (1 − ǫ)q2

12η1 (1 − ǫ)2

) ↑ α ↑ (37)

+

![image 399](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile399.png>)

![image 400](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile400.png>)

Thus, |E(S)| ≤ ((112−ηǫ1)2 + (1−512ǫ)q2)(Θ|αb| + |αw|). Thus, for q ≫ 0, only a small fraction (less than µ = (1−12ǫ)q0.1) of the black edges are between thick vertices and even a smaller fraction of the white ones. Namely, all the rest have at least one thin end vertex. This implies that

![image 401](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile401.png>)

![image 402](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile402.png>)

![image 403](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile403.png>)

- r ≥ (1 − µ)Θ|αb| + (1 − µ)|αw| = (1 − µ) ↑ α ↑. Theorem 1.8 is now proved also for i = 1. Let us mention that along the way we have proved two facts which are worth formulating separately.


- Corollary 6.7. In the notations and assumptions as above. If q ≫ 0, then we have:


- 1. If α ∈ B1(X,F2) is a locally minimal coboundary with ||α|| < q11.1 then α = 0.

![image 404](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile404.png>)

- 2. If α ∈ Z1(X,F2) \ B1(X,F2) then ||α|| > η1. In particular, for a ﬁxed q, every representative of a non-trivial cohomology class has linear size support.


Proof. The ﬁrst item follows immediately since δ(α) = 0. For the second item we observe that every α ∈ Z1, can be replaced by a locally minimal representative α′ with ||α′|| ≤ ||α|| and α′ = α(mod B1). Applying now Theorem 1.8 for α′, we deduce the result.

![image 405](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile405.png>)

![image 406](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile406.png>)

![image 407](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile407.png>)

![image 408](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile408.png>)

- Remark 6.8. In our proof of the Theorem ǫ1 turns out to be independent of q (provided q ≫ 0), but


η1 does depend on q (we choose η1 ≈ q11.1). One can improve the proof to make also η1 independent of q by considering the ”black skeleton” of X, i.e., the subgraph of X(1) consisting of the black edges and only them.

![image 409](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile409.png>)

Note that by Proposition 3.5, there are indeed cases with H1(X,F2) = {0}, so the second item of

- Corollary 6.7 is a non-vacuous systolic result. Such results are of potential interest for quantum error-correcting codes (see [10],[32] and the references therein).


We move now to the third case, i.e., i = 2, in which we have to prove 2-expansion. This case is by far more diﬃcult (and we have to overcome along the way the diﬃculties of the case i = 1, but also much more.) This will be the topic of the next section.

# 7 Expansion of 2-cochains in 3-dimensional Ramanujan complexes

In this section we prove the case i = 2 of Theorem 1.8. We prove that for q ≫ 0, exists ǫ′′ > 0 such that if α ∈ C2(X,F2) is locally minimal with |α| < q3|X(0)| then |δ(α)| ≥ ǫ′′q|α|. This indeed will

prove the theorem: recall that every 2-cell is contained in q + 1 pyramides and altogether there are approximately q6|X(0)| pyramides. Thus,

(q + 1)|α|

≈ c′ |α| q5|X(0)|

||α|| ≈

,

![image 410](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile410.png>)

![image 411](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile411.png>)

4 3 q6|X(0)|

and ||δ(α)|| = q6|δ|X(α(0))| |. Hence, we can deduce the result with µ3 = cq′′2 and ǫ3 independent of q (provided q ≫ 0).

![image 412](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile412.png>)

![image 413](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile413.png>)

First recall again that the link Xv of every vertex v of X is the 2-dimensional spherical building S(4,q). The vertices of Xv are of two types: the one corresponding to subspaces of dimensions 1 and 3 of F4q, the black vertices, and the other type corresponding to subspaces of dimension 2, which we call the white vertices. A black vertex is of degree 2(q2 + q + 1), while a white one is of degree 2(q + 1). There are approximately q3 black vertices and approximately q4 white ones.

Given a vertex v, an edge e of X, with v ∈ e, gives a unique vertex in Xv, which can be black or white, and we then call e black or white, accordingly.

We start with local considerations. Since α ∈ C2(X,F2) is locally minimal, for every edge e of X, |αe| ≤ |Xe2(0)|. Indeed, α being locally minimal means that for every vertex v of X, αv ∈ C1(Xv,F2) is minimal and in particular, it is locally minimal as a cochain of Xv. Thus, at every vertex w of Xv αv contains at most half of the edges around w. This exactly means that the number of triangles in α containing e is at most half of all the triangles containing e.

![image 414](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile414.png>)

For i = 0,··· ,4 we denote by ti the number of pyramides (3-cells) in X which contain exactly i triangles of α.

- Lemma 7.1.


- 1. e∈X(1) |αe| = 3|α|.
- 2. t1 + 2t2 + 3t3 + 4t4 = (q + 1)|α|.


Proof. The ﬁrst item follows from the fact that every triangle has three edges. The second is because every triangle is contained in exactly q + 1 pyramides.

![image 415](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile415.png>)

![image 416](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile416.png>)

![image 417](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile417.png>)

![image 418](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile418.png>)

Lemma 7.2. e∈X(1) EXe(αe,αe) = 3t1 + 4t2 + 3t3.

![image 419](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile419.png>)

Proof. Recall that αe can be considered as a set of vertices in the (q + 1)-regular graph Xe, which is the link of X at e. If P is a pyramid with one triangle from α, then for 3 out of the 6 edges of P, |αe| = 1 and for 3 of them |αe| = 0. The ﬁrst 3 contributes, each, 1 to the left hand side and the later have no contribution. If P has 2 triangles from α, then for one edge |αe| = 2 but this edge contributes nothing to the LHS, since P represents then an edge of Xe from αe to αe. For 4 other edges of P, |αe| = 1 and each contributes 1 to the LHS. For the last edge, |αe| = 0 and clearly no contribution to the LHS. A similar consideration justiﬁes the claim about the 3t3 contribution (or by duality to t1). Pyramids with either 0 or 4 triangles from α contributes nothing to the LHS.

![image 420](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile420.png>)

![image 421](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile421.png>)

![image 422](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile422.png>)

![image 423](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile423.png>)

- Deﬁnition 7.3. (Thin/thick edge) An edge e ∈ X(1) is called thin if |αe| ≤ |Xe(0)|0.9 and thick otherwise. Denote:


- R (resp. S) - the set of thin (resp. thick) edges.


- r := e∈R |αe|.
- s := e∈S |αe|. So, by Lemma 7.1, r + s = 3|α|.


The link graph Xe of every edge e of X is either the ”points versus lines graph” of the projective plane P2(q) over Fq or the complete (q + 1)-bipartite graph on 2(q + 1) vertices. Indeed, if e is a white edge, Xe is the complete bipartite (q + 1)-regular graph on 2(q + 1) vertices. While if e is black, Xe is the ”points versus lines” graph of the projective plane of Fq, i.e., (q + 1)-regular bipartite on 2(q2 + q + 1) vertices. When e is a thick/thin edge of X, we will also consider it as thick/thin vertex of Xv, for v ∈ e. In either case, just as with the 2-dimensional complexes studied in Section 5, λ1(Xe) ≥ q + 1 −

√q. The next lemma follows from Proposition 2.1.

![image 424](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile424.png>)

- Lemma 7.4.

- 1. For every e ∈ X(1), EXe(αe,αe) ≥ 12(q + 1 −

![image 425](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile425.png>)

![image 426](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile426.png>)

√q)|αe|.

![image 427](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile427.png>)

- 2. If e is thin then EXe(αe,αe) ≥ (q + 1 − q0.9)|αe|.


![image 428](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile428.png>)

Proof. The ﬁrst item is deduced directly from Proposition 2.1. For the second item, assume ﬁrst that e is white. In this case Proposition 2.1 gives:

EXe(αe,αe) ≥

![image 429](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile429.png>)

2(q + 1) − (2(q + 1))0.9 2(q + 1)

![image 430](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile430.png>)

(q+1−

√q)|αe| = (1−

![image 431](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile431.png>)

1 (2(q + 1))0.1

![image 432](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile432.png>)

)(q+1−

√q)|αe| ≥ (q+1−q0.9)|αe|,

![image 433](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile433.png>)

as q is large. Similarly this is also true for black edges.

![image 434](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile434.png>)

![image 435](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile435.png>)

![image 436](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile436.png>)

![image 437](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile437.png>)

Combining Lemmas 7.2 and 7.4 we get:

- Lemma 7.5. 3t1 + 4t2 + 3t3 ≥ 32(q + 1)|α| + (q+1)2 r − 3q0.9|α|. Proof.


![image 438](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile438.png>)

![image 439](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile439.png>)

3t1 + 4t2 + 3t3 =

≥

≥

EXe(αe,αe) +

EXe(αe,αe) (38)

![image 440](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile440.png>)

![image 441](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile441.png>)

e∈R

e∈S

√q)s + (q + 1 − q0.9)r (39)

- 1

![image 442](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile442.png>)

- 2


(q + 1 −

![image 443](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile443.png>)

(q + 1) 2

3 2

r − 3q0.9|α|. (40)

(q + 1)|α| +

![image 444](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile444.png>)

![image 445](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile445.png>)

![image 446](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile446.png>)

![image 447](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile447.png>)

![image 448](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile448.png>)

![image 449](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile449.png>)

Subtracting twice Lemma 7.1(2) from the equation proved in Lemma 7.5 we get:

- Lemma 7.6. t1 − 3t3 − 8t4 ≥ −(q+1)2 |α| + (q+1)2 r − 3q0.9|α|.


![image 450](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile450.png>)

![image 451](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile451.png>)

Thus, in order to prove Theorem 1.8, it will suﬃce to prove that r > (1 + ǫ′)|α| for some ǫ′ (independent of q) when q is large. I.e., more than 31 of the contribution to α comes from thin edges. It is interesting to compare this with the proof in Section 5 for dim X = 2, where we had only to show that r ≥ ǫ|α|. This is what makes the current proof more diﬃcult.

![image 452](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile452.png>)

Let us now use a global argument.

Deﬁnition 7.7. (Thin/thick vertex) A vertex v ∈ X(0) is called a thin vertex if in its link, Xv, there are less than q2.75 thick black vertices and less than q3.7 thick white vertices. Otherwise it is called a thick vertex. Let S0 denote the set of thick vertices, and R0 - the thin ones.

For every v ∈ X(0), our cochain α deﬁnes a 1-cochain αv ∈ C1(Xv,F2).

- Lemma 7.8.

- 1. If v is a thick vertex then |αv| ≥ q42.55.

![image 453](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile453.png>)

- 2. The number of thick vertices is at most q64|.α55| , i.e., |S0| ≤ q64|.α55| .

![image 454](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile454.png>)

![image 455](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile455.png>)

- 3. |S0| ≤ q16.n55, where n := |X(0)|.


![image 456](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile456.png>)

Proof. (1) If v is a thick vertex than it lies on either at least q2.75 black thick edges or on at least q3.7 white thick edges. A black (resp. white) thick edge is contained in at least (2(q2 + q + 1))0.9 (resp. (2(q + 1))0.9) triangles. The same triangle can be counted twice according to its two edges

which touch v, but in any case it means that there are at least q42.55 edges in αv.

![image 457](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile457.png>)

- (2) By (1), every thick vertex touches at least q42.55 triangles from α. A triangle touches 3 vertices, so it can be counted at most 3 times. Hence |S0| ≤ q64|.α55| .

![image 458](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile458.png>)

![image 459](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile459.png>)

- (3) follows from the fact that |α| ≤ q3n.


![image 460](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile460.png>)

![image 461](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile461.png>)

![image 462](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile462.png>)

![image 463](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile463.png>)

As X(1) is ”almost” a Ramanujan graph we can prove:

- Lemma 7.9. For q ≫ 0, |E(S0,S0)| ≤ q192.1|α|.


![image 464](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile464.png>)

√

Proof. The graph X(1) is a k-regular graph with k = 3i=1 4i q ≈ q4 and λ1(X(1)) ≥ k −44

![image 465](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile465.png>)

k (see

√

![image 466](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile466.png>)

Corollary 3.4). Thus, by Proposition 2.1, |E(S0,S0)| ≥ Sn0(k − 44

![image 467](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile467.png>)

![image 468](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile468.png>)

k)|S0|. Hence, |E(S0,S0)| =

![image 469](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile469.png>)

- 1

![image 470](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile470.png>)

- 2


![image 471](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile471.png>)

(k|S0| − |E(S0,S0)|) (41)

√

![image 472](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile472.png>)

|S0| n

- 1

![image 473](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile473.png>)

- 2


(k − 44

![image 474](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile474.png>)

(k|S0| −

≤

k)|S0|) (42)

![image 475](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile475.png>)

√

![image 476](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile476.png>)

![image 477](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile477.png>)

= |S0| 2

|S0| n

) + |S0| n

44

![image 478](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile478.png>)

(k(1 −

k) (43)

![image 479](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile479.png>)

![image 480](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile480.png>)

![image 481](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile481.png>)

√

![image 482](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile482.png>)

(k|S0| n

+ |S0| n

= |S0| 2

44

![image 483](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile483.png>)

k) (44)

![image 484](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile484.png>)

![image 485](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile485.png>)

![image 486](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile486.png>)

√

|S0| 2

(k|S0| n

+ 44

![image 487](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile487.png>)

≤

k) (45)

![image 488](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile488.png>)

![image 489](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile489.png>)

Now by Lemma 7.8, |E(S0,S0)| ≤ q34|.α55| (q4q16.55 + 44q2) ≤ 19q2|.α1|.

![image 490](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile490.png>)

![image 491](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile491.png>)

![image 492](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile492.png>)

![image 493](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile493.png>)

![image 494](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile494.png>)

![image 495](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile495.png>)

![image 496](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile496.png>)

Thus, for q large enough, only small proportion of the triangles in α have two (or more) thick vertices. Indeed, the total number of edges between thick vertices is bounded by q202.1|α| and on every edge there are at most q2 + q + 1 triangles from α. So we have the following corollary, from which we conclude that almost every triangle of α has at most one thick vertex.

![image 497](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile497.png>)

- Corollary 7.10. There are at most q200.1|α| triangles with 2 or 3 thick vertices. Now we show that almost all the triangles in α have at least one thin edge.


![image 498](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile498.png>)

- Lemma 7.11.

- 1. The number of triangles of α with at least one thin edge is at least (1 − oq(1))|α|.
- 2. The fraction of triangles of α with 3 thin vertices and at most one thin edge is oq(1).


Both parts of the lemma follow from the following result:

- Lemma 7.12. Let v be a thin vertex of X, Xv its link, and αv the 1-cochain of Xv induced by α. Let Sv be the subset of Xv(0) of the thick vertices of Xv, i.e., the ones corresponding to the thick edges of X coming out of v. Then:


|E(Sv,Sv)| |αv|

= oq(1).

![image 499](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile499.png>)

Namely, the probability of an edge of αv on Xv(1) coming from a vertex in Sv to stay at Sv is going to zero as q → ∞.

Proof. The link Xv is isomorphic to S(4,q), so Sv can be considered as a subset of M = M1∪M2∪M3 of the subspaces of F4q, where Mi is the set of subspaces of dimension i. Let Ti = Sv ∩ Mi. As v is a thin vertex of X, Deﬁnition 7.7 implies that |T2| < q3.7 and |T1 ∪ T3| < q2.75. On the other hand, every w ∈ Sv corresponds to a thick edge e of X. Hence, by Deﬁnition 7.3, e lies on at least |Xe(0)|0.9 triangles from α, or in other words αv has at least (deg (w))0.9 edges coming out of w.

- Now, if w ∈ T1 ∪ T3, deg(w) = 2(q + 1), while if w ∈ T2, deg(w) = 2(q2 + q + 1), thus all the assumptions of Lemma 3.2 are satisﬁed and our lemma follows.


![image 500](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile500.png>)

![image 501](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile501.png>)

![image 502](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile502.png>)

![image 503](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile503.png>)

Let us spell out the meaning of the last lemma. Lemma 7.12 says that if e is a thick edge of X containing a thin vertex v, and △ is a triangle in α containing e, then the second edge of △ touching v, is most likely thin (with probability 1 − oq(1)).

We next show that Lemma 7.11 follows from Lemma 7.12.

Proof. (of Lemma 7.11) As we saw above in Corollary 7.10, almost all the triangles of α have at least one thin vertex and hence, by Lemma 7.12 and the remark afterwards, at least one of the edges of the triangle adjacent to it is thin (with probability 1−oq(1)). This proves Lemma 7.11(1). Similarly, consider the triangles of α with three thin vertices and at most one thin edge, namely, those with three thin vertices and at least two thick edges. Each such a triangle △ contributes 1 to |E(Sv,Sv)| for a vertex v that is between its two thick edges (using the notations of Lemma 7.11). Thus the total number T of such triangles is bounded by v∈R

|E(Sv,Sv)|, where R0 is the set of thin vertices. By Lemma 7.11, we have that |E(|Sαv,Sv)|

0

v| = oq(1). Thus, T ≤ v∈R0 |E(Sv,Sv)| ≤ v∈R0 oq(1)|αv| ≤ oq(1) · 3|α|. I.e., the fraction of triangles of α with 3 thin vertices and at least

![image 504](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile504.png>)

two thick edges is oq(1). This proves Lemma 7.11(2).

![image 505](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile505.png>)

![image 506](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile506.png>)

![image 507](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile507.png>)

![image 508](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile508.png>)

Let now state a general observation about any cochain β ∈ C2(X,F2). Such β induces two cochains on the link Xv of every vertex v: One is βv1 = βv ∈ C1(X,F2) that we have used so far, and the other is βv2 ∈ C2(Xv,F2) which is deﬁned just by restricting β to the triangles of Xv, when we recall that the link of v is the set of simplicies τ of X s.t. v ∈/ τ and τ ∪ {v} is also a simplex of X. The next proposition follows from the deﬁnitions.

Proposition 7.13. If β ∈ C2(X,F2) then

1 4

1 4

|δ1βv1 + βv2| ≥

|δ1βv1| −

|δ2β| =

(

![image 509](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile509.png>)

![image 510](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile510.png>)

v∈X(0)

v∈X(0)

|βv2|) =

v∈X(0)

1 4

(q + 1) 4 |β|.

|δ1βv1|) −

(

![image 511](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile511.png>)

![image 512](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile512.png>)

v∈X(0)

Proof. Recall that δ2β is the set of 3-cells of X which contains an odd number of triangles from β. The ﬁrst equality is just summing up over the vertices v of X, the number of such 3-cells of δ2β touching v is indeed the same as the number of triangles in δ1βv1 + βv2. Note that the last sum is modulo 2. The inequality follows for the subadditivity of the norm |·|. The last equality follows from the fact that every triangle of X is inside q + 1 pyramids and hence v∈X(0) |βv2| = (q + 1)|β|.

![image 513](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile513.png>)

![image 514](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile514.png>)

![image 515](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile515.png>)

![image 516](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile516.png>)

We are now ready to complete the proof of Theorem 1.8. Recall that by Proposition 3.1 there exists 0 < ǫ(4) such that for every minimal 1-cochain ϕ of S(4,q), ||δ1(ϕ)|| ≥ 3ǫ(4)||ϕ||. Now, since every edge in S(4,q) is contained in q + 1 triangles, it follows that |δ1(ϕ)| ≥ ǫ(4)(q + 1)|ϕ|.

Write our α as γ0 + γ1 + γ2 + γ3 where γi is the subset of all the triangles of α which have exactly i thick vertices. Assume ﬁrst that |γ0| > ǫ100(4)|α|. This means that ǫ100(4) fraction of the triangles of α have no thick vertex. For such a triangle, almost surely, (when q ≫ 0), at least 2 edges are thin (Lemma 7.11(2)). In addition, we know that almost every triangle of α has at least one thin edge (Lemma 7.11(1)). Thus, r > (1 + ǫ100(4) − oq(1))|α| and Lemma 7.6 now ﬁnishes the proof.

![image 517](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile517.png>)

![image 518](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile518.png>)

![image 519](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile519.png>)

Assume therefore that |γ0| < ǫ100(4)|α|. Note that by Corollary 7.10, |γ2 + γ3| ≤ q200.1|α|. Thus,

![image 520](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile520.png>)

![image 521](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile521.png>)

ǫ(4) 100 |α| −

20 q0.1|α| ≥ (1 −

ǫ(4) 50

|γ1| = |α − γ0 − γ2 − γ3| ≥ |α| −

)|α|, for q ≫ 0. On the other hand, as in Proposition 7.13,

![image 522](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile522.png>)

![image 523](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile523.png>)

![image 524](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile524.png>)

1 4

|δ2(γ1)| ≥

(

![image 525](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile525.png>)

1 4

|δ1γ11,v + γ12,v|) ≥

(

![image 526](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile526.png>)

v∈X(0)

1 4

|δ1γ11,v + γ12,v|) ≥

(

![image 527](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile527.png>)

v∈S0

1 4 v∈S

|δ1γ11,v|) −

![image 528](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile528.png>)

v∈S0

0

|γ12,v|,

where S0 is the set of thick vertices.

Now note: by our assumption, α is locally minimal, i.e., α1v is minimal (i.e. closest possible to B1(Xv,F2) in its coset), the same is true for γ11,v, as the later is a subset of α1v and hence also minimal. Thus,

|δ1γ11,v| ≥

v∈S0

ǫ(4)(q + 1)|γ11,v| = ǫ(4)(q + 1)

v∈S0

v∈S0

|γ11,v| = ǫ(4)(q + 1)|γ1|.

The last equality is true since every triangle of γ1 has a unique thick vertex. Let us now evaluate v∈S

|γ12,v|. Note that γ12,v gives 1 only to pyramids containing v as well as another thick vertex, and just one like that. Thus, v∈S

0

|γ12,v| is bounded by twice the number of

0

pyramids with two thick vertices. Recall that by Lemma 7.9, E(S0,S0) < q202.1|α|. Every pyramids with two thick vertices contains an edge from E(S0,S0). On such an edge there are at most 2(q2 + q + 1) triangles and on each triangle (q + 1) pyramids. This implies that

![image 529](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile529.png>)

20

|γ12,v| < 2

q2.1|α| · 2(q2 + q + 1) · (q + 1) ≤ 100q0.9|α|. Putting the last three inequalities together we get that,

![image 530](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile530.png>)

v∈S0

1 4

ǫ(4)(q + 1)|γ1| − 25q0.9|α|. Finally we can compute:

|δ2(γ1)| ≥

![image 531](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile531.png>)

|δ2α| = |δ2(γ0 + γ1 + γ2 + γ3)| (46) ≥ |δ2(γ1)| − |δ2(γ0)| − |δ2(γ2 + γ3)| (47) ≥

ǫ(4) 100 |α| − (q + 1)

20 q0.1|α| (48)

1 4

ǫ(4)(q + 1)|γ1| − 25q0.9|α| − (q + 1)

![image 532](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile532.png>)

![image 533](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile533.png>)

![image 534](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile534.png>)

We used here the fact that for every β ∈ C2(X,F2), |δ2β| ≤ (q + 1)|β|, and also that we are now under the assumption that |γ0| < ǫ100(4)|α| and |γ2 + γ3| < q200.1|α|.

![image 535](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile535.png>)

![image 536](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile536.png>)

Now, |γ1| ≥ (1 − ǫ50(4))|α| and altogether

![image 537](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile537.png>)

|δ2α| ≥

ǫ(4) 50

1 4

ǫ(4)(q+1)(1−

![image 538](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile538.png>)

![image 539](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile539.png>)

ǫ(4) 100 |α|−25q0.9|α|−(q+1)

20 q0.1 |α| ≥ ǫ(4)(q+1)|α|(

1 4−

ǫ(4) 200 −

)|α|−(q+1)

![image 540](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile540.png>)

![image 541](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile541.png>)

![image 542](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile542.png>)

![image 543](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile543.png>)

1 100

)−50q0.9|α|

![image 544](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile544.png>)

As ǫ(4)(14 − ǫ200(4) − 1001 ) ≥ 0.2ǫ(4) we get:

![image 545](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile545.png>)

![image 546](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile546.png>)

![image 547](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile547.png>)

|δ2α| ≥ 0.2ǫ(4)(q + 1)|α| − 50q0.9|α| ≥ 0.1ǫ(4)(q + 1)|α|. for q suﬃciently large and Theorem 1.8 is proved.

- Remark 7.14. Theorem 1.8 was proved with ǫ0,ǫ1,ǫ2 that are absolute constant independent of q


(provided q ≫ 0). So are µ0 and µ1, but µ2 = cq′′2 depends on q. It is interesting and somewhat useful to know if µ2 can be made to be independent of q.

![image 548](<2014-kaufman-isoperimetric-inequalities-ramanujan-complexes_images/imageFile548.png>)

We have the following systolic corollary:

- Corollary 7.15. For q ≫ 0, if α ∈ C2(X,F2) represents a non-trivial 2-cohomology class than |α| ≥ q3|X(0)|.


# 8 Coboundary expanders and the congruence subgroup property

Theorem 1.7 implies that coboundary expanders are topological expanders. Theorem 1.3 gives, for d = 2, a family {Ya} of topological expanders. But, our family falls short of being a family of coboundary expanders. In fact, Proposition 1.5 shows that for many of them H1(Ya,F2) = 0 which violates the expansion property. On the other hand, our proofs of Theorem 1.3 shows that this is the only obstacle i.e., these complexes that we construct for the proof of Theorem 1.3 (i.e., the 2-skeletons of 3-dimensional non-partite Ramanujan complexes) would be coboundary expanders if their ﬁrst cohomology over F2 would vanish. Indeed, we prove their cocycle expansion; If H1 = 0, this is the same as coboundary expansion for Ya. The goal of this short section is to explain that, assuming a very special case of a conjecture of Serre [31], inﬁnitely many of the examples we constructed have indeed vanishing 1-cohomology. Hence they form an inﬁnite family of bounded degree 2-dimensional coboundary expanders.

Let us recall the following standard deﬁnitions: Let k be a global ﬁeld, i.e., a ﬁnite extension of Q or a ﬁeld of transcendental degree 1 over Fq in the positive characteristic case, O the ring of integers of k, S a ﬁnite set of valuations of k including all the archimedean ones, and OS = {x ∈ k|ν(x) ≥ 0,∀ν ∈/ S}-the ring of S-integers. Let G be a simply connected, connected, simple algebraic group deﬁned over k with a k-embedding G ֒→ GLn and G(OS) = G GLn(OS). We say that G(OS) has the congruence subgroup property if the ”congruence kernel”: C(G,S) = Ker( G(OS) → G( OS)) is ﬁnite, where ( . ) denotes the propﬁnite completion. The reader is referred to [31] [26], [28] for details and history of this problem. Serre [31] conjectured that this is indeed the case if S-rank(G) ≥ 2, i.e., if v∈S kv-rank(G) ≥ 2.

We are interested in the Cartwright-Steger arithmetic lattice - the CS-lattice. This discrete cocompact subgroup of PGLd(Fq((t))) is an arithmetic group (see [4] and [22] for a detailed construction and [17] for an exposition) and its S-rank is d − 1. In particular, the case used in this paper for Theorem 1.3 is d = 4, so the S-rank equals 3, and it is covered by Serre’s conjecture. While Serre’s conjecture has been proven for ”most” cases, the special case of the CS-lattices is still open (see [26], [28] for a survey of the current knowledge). Let us say ﬁrst, that assuming Serre’s conjecture for the CS-lattice, the congruence kernel is not just ﬁnite, but actually trivial. Indeed,

in this case the Margulis-Platonov conjecture (on the ﬁnite index subgroups of G(k)) is known to hold ([29],[28]) and as explained in [26] if C(G,S) is ﬁnite, it is also central and isomorphic to the metaplectic kernel of G with respect to k and S. This metaplectic kernel has been computed by Prasad and Rapinchuk [27] and in our case is trivial.

Assume now that the Serre’s Conjecture indeed holds in our case, where d = 4 and q a ﬁxed large odd prime power q = pr. Then for the CS-lattice Γ = G(OS), G(OS) = G( OS). The simplicial complexes used for the proof of Theorem 1.3 are Xa = Γa\B when B = A3(Fq((t))) and where Γa are congruence subgroups of Γ, and Xa are non-partite. As explained in [22], Γa can be taken to be a principle congruence subgroup of the form Γ(I) = Ker(G(OS) → G(OS/I)) when I ⊳OS. Moreover Theorem 7.1 there ensures that for every suﬃciently large e there exists an irreducible polynomial f(x) of degree e, so that if I = (f(x)) is the ideal generated by f(x), XI = Γ(I)\B is non-partite. Now, the assumption that G(OS) = G( OS) implies that for such an I, Γ(I) = Kvf × v =vf G(OS,v), where for a valuation v of k, OS,v is the v-completion of OS, vf is the valuation associated with f(x) and Kvf is the normal subgroup of G(OS,vf), Kvf = Ker(G(OS,vf) → G(OS,vf/f(x)OS,vf)). The group Kvf is a pro-p group and each of G(OS,v) is an extension of a pro-p group by a quasi-simple ﬁnite group. As p is odd, it follows that [ Γ(I), Γ(I)] Γ(I)2 = Γ(I), i.e., Γ(I) has no quotient that is abelian of order 2. The same holds therefore for Γ(I). Hence, H1(Γ(I),F2) = 0. Now, as the building B is contractible, it follows that H1(XI,F2) = 0. Finally, YI, the 2-skeleton of XI, satisﬁes H1(YI,F2) = H1(XI,F2) and so H1(YI,F2) = 0 as promised. We can summarize:

- Corollary 8.1. Assume that for some large odd prime power q, the Cartwright-Steger arithmetic


lattice of PGL4(Fq((t))) satisﬁes the congruence subgroup property (as predicted by Serre’s conjecture). Then there exists an inﬁnite family of bounded degree 2-dimensional coboundary expanders.

- Remark 8.2. In fact, a much weaker assumption than Serre’s Conjecture is needed. Namely, Serre predicts that C = C(G,S) is trivial (in our case). We only need that C/[C,C]C2 is trivial.


Acknowledgments. The authors are grateful to G. Kalai, N. Linial, R. Meshulam, E. Mossel,

- S. Mozes, A. Rapinchuk, J. Solomon and U. Wagner for useful discussions and advice. We thank also the ERC, ISF, BSF and NSF for their support.


# References

- [1] I. B´ara´ny. A generalization of Carathe´odorys theorem, Discrete Mathematics, 40(2):141-152, 1982.
- [2] R. Ben Ari, U. Vishne, Homology of 2-dimensional complexes and internal partitions, preprint.
- [3] E. Boros and Z. Fu¨redi. The number of triangles covering the center of an n-set, Geometriae Dedicata, 17(1):69-77, 1984.
- [4] D.I. Cartwright and T. Steger. A family of A˜n-groups, Israel Journal of Mathematics, 103(1):125-140, 1998


- [5] D. Dotterrer and M. Kahle. Coboundary expanders, Journal of Topology and Analysis, 4: 499–514, 2012.
- [6] S. Evra, K. Golubev and A. Lubotzky Mixing properties and the chromatic number of Ramanujan complexes, arXiv:1407.7700, 2014.
- [7] J. Fox, M. Gromov, V. Laﬀorgue, A. Naor, and J. Pach. Overlap properties of geometric expanders, Journal fr die reine und angewandte Mathematik 671: 49–83, 2012.
- [8] H. Garland. p-adic curvature and the cohomology of discrete subgroups of p-adic groups, The Annals of Mathematics, 97(3):375-423, 1973.
- [9] M. Gromov. Singularities, expanders and topology of maps. part 2: From combinatorics to topology via algebraic isoperimetry, Geometric and Functional Analysis, 20(2):416-526, 2010.
- [10] L. Guth and A. Lubotzky Quantum error-correcting codes and 4-dimensional arithmetic hyperbolic manifolds, Journal of Mathematical Physics, to appear, arXiv:1310.5555, 2013.
- [11] S. Hoory, N. Linial, and A. Wigderson. Expander graphs and their applications, Bulletin of the American Mathematical Society, 43(4):439-562, 2006.
- [12] T. Kaufman, D. Kazhdan and A. Lubotzky. Ramanujan Complexes and bounded degree topological expanders, FOCS 2014, to appear.
- [13] T. Kaufman and A. Lubotzky. High dimensional expanders and property testing, ITCS 2014: 501-506.
- [14] T. Kaufman, U. Wagner. In preparation.
- [15] N. Linial and R. Meshulam. Homological connectivity of random 2-complexes, Combinatorica, 26(4):475-487, 2006.
- [16] A. Lubotzky. Expander graphs in pure and applied mathematics, Bull. Amer. Math. Soc, 49:113162, 2012.
- [17] A. Lubotzky. Ramanujan Complexes and High Dimensional Expanders, Japanese Journal of Mathematics, to appear, arXiv:1301, 2013.
- [18] A. Lubotzky. Discrete Groups, Expanding Graphs and Invariant Measures, volume 125 of Progress in Mathematics. Birkhauser, 1994.
- [19] A. Lubotzky and R. Meshulam. Random Latin squares and 2-dimensional expanders, arXiv:1307.3582, 2013.
- [20] A. Lubotzky, R. Meshulam and S. Mozes. Expansion of building-like complexes, arXiv:1407.6303, 2014.
- [21] A. Lubotzky, B. Samuels, and U. Vishne. Ramanujan complexes of type A˜d, Israel Journal of Mathematics, 149(1):267-299, 2005.
- [22] A. Lubotzky, B. Samuels, and U. Vishne. Explicit constructions of Ramanujan complexes of type A˜d, Eur. J. Comb., 26(6):965-993, 2005.


- [23] R. Meshulam and N.Wallach. Homological connectivity of random k-dimensional complexes, Random Structures and Algorithms, 34(3):408-417, 2009.
- [24] D.A. Meyer, M.H. Freedman and F. Luo. Z2-systolic freedom and quantum codes, Mathematics of Quantum Computation, 287–320, 2002.
- [25] O. Parzanchevsky. Mixing in high-dimensional expanders, arXiv:1310.6477, 2013.
- [26] G. Prasad and A. Rapinchuk. Computation of the metaplectic kernel, Inst. Hautes Etudes´ Sci. Publ. Math. No. 84 , 91-187, 1997.
- [27] G. Prasad and A. Rapinchuk. Developments on the congruence subgroup problem after the work of Bass, Milnor and Serre, arXiv:0809.1622.
- [28] Raghunathan, M. S. The congruence subgroup problem, Proc. Indian Acad. Sci. Math. Sci. 114,no. 4, 299-308, 2004.
- [29] A. Rapinchuk and Y. Segev. Valuation-like maps and the congurence subgroup property, Invent. math. 144, 571-607, 2001.
- [30] L. Ribes and P. Zalesskii. Proﬁnite groups, Ergebnisse der Mathematik und ihrer Grenzgebiete.

3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics], 40. Springer-Verlag, Berlin, xiv+435 pp, 2000.

- [31] J.P. Serre, Le probleme des groupes de congruence pour SL2, Annals of Mathematics, 92(3), 489–527, 1970.
- [32] G. Zemor, On Cayley graphs, surface codes, and the limits of homological coding for quantum error correction, Coding and Cryptology, second international workshop IWCC, LNCS 5557:259–273, 2009.


