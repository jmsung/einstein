Bounded Degree Cosystolic Expanders of Every Dimension

Shai Evra ∗ Tali Kaufman † January 27, 2017

arXiv:1510.00839v3[math.CO]26Jan2017

Abstract

In this work we present a new local to global criterion for proving a form of high dimensional expansion, which we term cosystolic expansion. Applying this criterion on Ramanujan complexes, yields for every dimension, an inﬁnite family of bounded degree complexes with the topological overlapping property. This answer aﬃrmatively an open question raised by Gromov.

# 1 Introduction

Expander graphs have been central objects of study in both computer science and mathematics during the past few decades. Informally, expanders are sparse and highly connected graphs and as such have numerous applications, see [HLW] and [Lub1] and the references therein. In recent years, a new theory of high dimensional expanders has emerged, pioneered by the works of Linial-Meshulam-Wallach [LinM],[MW], and Gromov [Gro] (for a recent survey see [Lub2]). Linial-Meshulam-Wallach and Gromov suggested two, essentially equivalent, generalizations of the notion of graph expansion to higher dimensions (even though both works were in completely diﬀerent research directions).

- 1.1 Gromov’s question


In [Gro], Gromov studied the complexity of embedding simplicial complexes into Euclidean spaces. More speciﬁcally, he considered the following topological overlapping property:

- Deﬁnition 1.1. A d-dimensional simplicial complex X has the c-topological overlapping property, for some c > 0, if for every continuous map f : X → d, there exists a point p ∈ d, whose preimage, f−1(p), intersects at least c-fraction of the d-simplices of X, i.e.,


|{σ ∈ X(d): p ∈ f(σ)}| ≥ c · |X(d)|. (1.1)

A family of d-dimensional simplicial complexes is said to have the topological overlapping property, if there exists c > 0, such that each member of the family has the c-topological overlapping property.

Gromov then proved the remarkable result that, for a ﬁxed d ∈ N, the family of complete ddimensional complexes have the topological overlapping property. This result is a very striking generalization of classical results from convex combinatorics due to Boros-Furedi [BF] (for d = 2)

![image 1](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile1.png>)

∗Hebrew University, ISRAEL. Email: shai.evra@mail.huji.ac.il. Research supported in part by the ERC. †Bar-Ilan University, ISRAEL. Email: kaufmant@mit.edu. Research supported in part by the IRG, ERC and

BSF.

and Barany [Bar] (for d ≥ 3). Gromov then proceeded to give other examples of families of complexes which posses the topological overlapping property (e.g. spherical buildings and random complexes). However, all the examples he provided were of unbounded degree, i.e. the number of faces incident to a single vertex grows with the number of vertices in the complex. This naturally led Gromov to the following question:

Question 1.2 (Gromov). Is there an inﬁnite family of bounded degree d-dimensional simplicial complexes with the topological overlapping property, for arbitrary d ≥ 2?

In a recent work [KKL], Kaufman, Kazhdan and Lubotzky were able to give an aﬃrmative answer to Gromov’s question in dimension two, i.e., they showed that there exists an inﬁnite family of 2-dimensional, bounded degree complexes with the topological overlapping property, see [KKL, Theorem 1.3]. However, their proof method is inherently suited for dimension two.

In this work we give a complete answer to Gromov’s question.

Theorem 1.3. For every d ∈ N, there exist an inﬁnite family of d-dimensional bounded degree complexes with the topological overlapping property.

An immediate application of Theorem 1.3, is an improvement of a result by Gromov and Guth [GG, Theorem 2.2], which gives a high dimensional generalization to a classical result of Kolmogorov and Barzdin [BK].

Corollary 1.4. For every D ≥ 2d + 1, there exists C = C(D) > 0 and an inﬁnite family of ddimensional bounded degree complexes, {Xn}n, which satisﬁes the following: For any embedding of Xn into RD, such that the images of any two non-adjoint simplices of Xn are of distance at least 1, the volume of the 1-neighborhood of the image of Xn is at least C · |Xn|

1

D−d.

![image 2](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile2.png>)

## 1.2 A criterion for the topological overlapping property

Let us start by addressing the question: How can one prove that a certain complex posses a topological overlapping property? In [Gro], Gromov showed that the topological overlapping property is implied by a certain notion of high-dimensional expansion, which we now wish to deﬁne. To do so, we ﬁrst need some notations.

- Deﬁnition 1.5. Let X be a d-dimensional simplicial complex. For any −1 ≤ k ≤ d, deﬁne:

- • X(k) = {σ ∈ X | |σ| = k + 1} - the collection of k-dimensional faces of X.
- • Ck = Ck(X;F2) = {f : X(k) → F2} - the space of k-dimensional F2-cochains of X.
- • δk : Ck → Ck+1, δf(τ) = σ⊂τ f(σ) - the k-dimensional F2-coboundary map of X.
- • Zk = Zk(X;F2) = ker(δk) - the space of k-dimensional F2-cocycles of X.
- • Bk = Bk(X;F2) = Im(δk−1) - the space of k-dimensional F2-coboundaries of X.
- • · : Ck → [0,1], f = σ∈X(k) |{τ∈X(d) | σ⊂τ}| (kd+1+1)·|X(d)| · f(σ) - a k-dimensional norm on Ck.


![image 3](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile3.png>)

We are now in a position to present our ﬁrst notion of high dimensional expansion.

- Deﬁnition 1.6 (Coboundary expanders). Let X be a d-dimensional simplicial complex, and let ǫ > 0. We say that X is an ǫ-coboundary expander, if for every k = 0,1,... ,d − 1,


δ(f) minb∈Bk f + b | f ∈ Ck \ Bk ≥ ǫ. (1.2)

Expkb(X) := min

![image 4](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile4.png>)

The notion of coboundary expansion ﬁrst appeared implicitly in the work [LinM], whose motivation was to generalize to higher dimensional complexes, the phase transition phenomenon of connectivity of random graphs in the Erdos-Reyni model. Later on, Gromov [Gro], came across essentially the same notion of expansion, while studying ﬁberwise complexetiy, and showing that coboundary expansion implies the topological overlapping property.

Unfortunately, up to this date, no bounded degree coboundary expanders are known to exists, so one cannot use Gromov’s result, to answer his question. The problem is that coboundary expansion requires vanishing of F2-cohomology of the complex, a property which is so strong that even certain Ramanujan complexes are known to not satisfy it (see [KKL]).

In order to bypass this problem, we deﬁne a weaker notion of expansion, which we call cosystolic expansion. This notion is strictly weaker than coboundary expansion, since it allows the existence of cocycles which are not coboundaries, as long as they are suﬃciently large.

- Deﬁnition 1.7 (Cosystolic expanders). Let X be a d-dimensional simplicial complex, and let ǫ,µ > 0. We say that X is an (ǫ,µ)-cosystolic expander, if for every k = 0,1,... ,d − 1,


δ(f)

minz∈Zk f + z | f ∈ Ck \ Zk ≥ ǫ (1.3) and

Expkz(X) := min

![image 5](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile5.png>)

Systk(X) := min{ z | z ∈ Zk \ Bk} ≥ µ. (1.4)

In [DKW], the authors strengthen the aforementioned result of Gromov, proving that cosystolic expansion implies the topological overlapping property.

Theorem 1.8 (Gromov’s Topological Overlapping Criterion [DKW]). For every d ∈ N and ǫ,µ > 0, there exist c = c(d,ǫ,µ) > 0, such that if X is a d-dimensional (ǫ,µ)-cosystolic expander, then X has the c-topological overlapping property.

Hence, by Gromov’s topological overlapping criterion, in order to prove Theorem 1.3, one needs to prove the existence of an inﬁnite family of bounded degree cosystolic expanders.

## 1.3 A criterion for cosystolic expansion

The ﬁrst inﬁnite family of bounded degree cosystolic expanders was constructed in [KKL], where it was shown that the 2-dimensional skeletons (see below) of 3-dimensional Ramanujan complexes of suﬃciently large degree are cosystolic expanders.

In this work our intention was to generalize the results of [KKL] to all dimensions. However, the proof method of [KKL] is speciﬁcally designed for the two-dimensional case. Indeed, in order to apply their proof to dimension three or higher, one will need to assume that the graph, whose vertex set is the set of edges in the complex and its edge set is the set of pairs of edges which form a triangle in the complex, is an excellent expander graph. As it turns out, this condition is too strong and does not hold in any Ramanujan complex.

The main novelty of our work is to present a new method for transforming expansion in lower dimension to high dimension in the complex. This allow us to prove our main result, which is a local to global criterion for cosystolic expansion, in all dimensions. To state this criterion, we need to deﬁne the notions of skeletons, links and skeleton expander of a complex.

- Deﬁnition 1.9. Let X be a d-dimensional simplicial complex.


- • For k ≤ d, the k-dimensional skeleton of X, denoted X(k), is the complex obtained by deleting from X all faces of dimension greater then k.


- • For σ ∈ X, the link of the face σ in X, denoted Xσ, is the complex obtained by picking only the faces in X that contains σ, and removing σ from each of these faces. A link is called a proper link of X, if 1 ≤ |σ| ≤ d − 1.
- • A complex X, is said to be an α-skeleton expander, for some α > 0, if its 1-skeleton satisfy the following graph expansion property 1:


∀ A ⊂ X(0), E(A,A) ≤ 4 · ( A 2 + α · A ), (1.5) where E(A,A) ⊂ X(1) are the edges in X with both vertices in A.

We are now ready to state our local to global criterion for cosystolic expansion.

- Theorem 1.10 (Main Theorem). For any d,Q ∈ N and β > 0, there exists ǫ = ǫ(d,β,Q) > 0, µ = µ(d,β) > 0 and α = α(d,β) > 0, such that if X is a d-dimensional complex satisfying:

- • X is Q-bounded degree, i.e. maxv∈X(0) |Xv| ≤ Q.
- • All the proper links of X are β-coboundry expanders.
- • All the proper links of X and X itself are α-skeleton expanders.


Then the (d − 1)-skeleton of X is an (ǫ,µ)-cosystolic expander.

It seems very natural to compare our local to global expansion result, with that of Garland [Gar]. However, other then philosophically, the two results are unrelated, Garland’s work is over R, while ours is over F2. Moreover, the proof method of both results is quite diﬀerent.

1.4 Ramanujan complexes

The well known Ramanujan complexes (see [Lub2]), constructed over a ﬁxed residue ﬁeld, are bounded degree high dimensional complexes, which are excellent skeleton expanders (this follows directly from the Ramanujan property). Their proper links are spherical buildings admitting a strongly transitive action, and it follows from the work of Gromov [Gro] (see also [LMM]) that they are coboundary expanders. Therefore, we are left to prove that their links, i.e., that the spherical buildings, are also good skeleton expanders 2.

- Theorem 1.11. For any d ∈ N and α > 0, there exist q0 = q0(d,α) > 0, such that for any prime power q ≥ q0, all d-dimensional, q-thick spherical buildings admitting a strongly transitive action are α-skeleton expanders.


In conclusion, Ramanujan complexes of suﬃciently large but ﬁxed degree satisﬁes the requirements of Theorem 1.10, which together with Gromov’s topological overlapping criterion (Theorem 1.8), implies the following corollary regarding the expansion of Ramanujan complexes.

Corollary 1.12. For any d ∈ N, there exists q0 = q0(d), such that for any prime power q ≥ q0, there exists µ = µ(d) > 0, ǫ = ǫ(d,q) > 0 and c = c(d,q) > 0, such that if X is the d-dimensional skeleton of a (d + 1)-dimensional q-thick Ramanujan complex, then

![image 6](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile6.png>)

- 1The constant 4 in our deﬁnition of skeleton expansion is unnatural, as it implies a notion strictly weaker then graph expansion. See [KM1] for a more accurate notion of skeleton expansion. However, our notion of skeleton expansion will be suﬃcient for our use here.
- 2After a completion of our paper, Izhar Oppenheim has pointed to us that a similar result to Theorem 1.11, could potentially be deduced from the work of [Opp], as a special case of Theorem 8.12 there. Our proof that exploits the geometric structure of the spherical buildings, allows us to get a proof which is signiﬁcantly shorter.


- • X is an (ǫ,µ)-cosystolic expander.
- • X has the c-topological overlapping property.


Finally, by combining the explicit construction of Ramanujan complexes of [LSV2], with Corollary 1.12, we get an explicit construction of bounded degree cosystolic expanders with the topological overlapping property in every dimension (Theorem 1.3). It is interesting to note that no such random construction, i.e., of bounded degree high dimensional complexes with the topological overlapping property, is currently known.

## 1.5 Organization of the paper

In section 2 we review some basic deﬁnition related to simplicial complexes, norms, links, skeletons and high dimensional expansions. In section 3 we prove the local to global criterion for cosystolic expansion (Theorem 1.3). In section 4 we prove a one sided mixing lemma for the 1-skeletons of regular complexes. In section 5 we review the deﬁnition of spherical buildings and show that they are good skeleton expanders. Finally, in section 6, we prove that Ramanujan complexes satisﬁes the conditions of Theorem 1.3, hence their skeletons are therefore examples of bounded degree complexes with the topological overlap property.

## 1.6 Acknowledgments

The authors are grateful to David Kazhdan and Alex Lubotzky for useful discussions and advices, and for Ron Rosenthal for many valuable improvements for this paper. The ﬁrst author would like to especially thank Alex Lubotzky for introducing, teaching and encouraging him to work on this problem, without which this work would not have been possible. We also thank the ERC, and BSF for their support. This work is part of the Ph.D. thesis of the ﬁrst author at the Hebrew University of Jerusalem, Israel.

# 2 Preliminaries on complexes and expansions

In this section we present the basic deﬁnitions and properties of simplicial complexes with norms, as well as notions of high-dimensional expansions.

## 2.1 Complexes

Throughout this paper we shall use the following notations regarding simplicial complexes:

A simplicial complex, X, over a set of vertices, V , is family of subsets of V , X ⊂ 2V , which is closed under inclusions, i.e. if F ∈ X and E ⊂ F then E ∈ X (note that the empty-set is always a face in any complex). Call the elements of X, faces or simplices. The dimension of a simplex F ∈ X, is deﬁned as dim(F) = |F| − 1, and the dimension of the entire complex is deﬁned as the maximal dimension of a simplex in it, i.e. dim(X) = maxF∈X dim(F). A complex is said to be pure if all its maximal faces are of the same dimension.

For convenience sake, by a k-face we mean a k-dimensional face of the complex, and by a d-complex we will always mean a ﬁnite d-dimensional pure simplicial complex.

Let X be a d-complex. For any −1 ≤ k ≤ d, denote by X(k) the collection of k-faces in X, and by Ck = Ck(X;F2) = {f : X(k) → F2} the space of k-cochains. As usual, denote by

δ = δk : Ck → Ck+1, (δf)(τ) =

f(σ) (2.1)

σ⊂τ

the k-coboundry map, and by Bk = Bk(X,F2) = Im(δk−1) and Zk = Zk(X,F2) = ker(δk) the spaces of k-coboundries and k-cocycles, respectively. Recall that δk ◦ δk−1 = 0, hence Bk ⊂ Zk.

Since we are working over F2, any k-cochain is an indicator function of a subset of k-faces, and vice versa, any subset of k-faces deﬁnes a k-cochain, i.e. {f : X(k) → F2} ∼= {A ⊂ X(k)}, where f  → supp(f) and A  → 1A. So, from now we will identify each subset of k-faces, A ⊂ X(k), with the following k-cochain f = 1A ∈ Ck.

- Deﬁnition 2.1 (Norm). Deﬁne the following norm on the space of cochains:


· = · k : Ck → [0,1], A =

w(σ) where w(σ) = |{F ∈ X(d)|σ ⊂ F}|

![image 7](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile7.png>)

d+1

|σ| · |X(d)|

σ∈A

(2.2)

Note that for any −1 ≤ k ≤ d, and any A,B ∈ Ck (i.e. A,B ⊂ X(k)), then:

- • A = 0 if and only if A = ∅, and A = 1 if and only if A = X(k).
- • A ∪ B ≤ A + B with equality if and only if A and B are disjoint.


- Deﬁnition 2.2 (Container). Let X be a d-complex and let −1 ≤ k ≤ r ≤ d. For any A ∈ Ck, deﬁne Γr(A) ∈ Cr to be the following r-cochain,


Γr(A) = {F ∈ X(r)|∃ σ ∈ A, σ ⊂ F}. (2.3) Lemma 2.3. Let X be a d-complex and let −1 ≤ k ≤ r ≤ d. Then for any A ∈ Ck,

r + 1 k + 1 · A . (2.4)

A ≤ Γr(A) ≤

Proof. First note that for any σ ∈ X(k), then

Γr({σ}) =

w(τ) =

σ⊂τ∈X(r)

1 |X(d)|

=

![image 8](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile8.png>)

1 |X(d)|

![image 9](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile9.png>)

τ∈X(r) σ⊂τ

F∈X(d) σ⊂F

1

1

1 |X(d)|

=

![image 10](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile10.png>)

![image 11](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile11.png>)

![image 12](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile12.png>)

d+1 r+1

d+1 r+1

τ∈X(r) σ⊂τ⊂F

F∈X(d) τ⊂F

F∈X(d) σ⊂F

d−k r−k d+1 r+1

d+1 k+1 · dr−−kk

r + 1 k + 1 · w(σ) (2.5)

=

w(σ) =

![image 13](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile13.png>)

![image 14](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile14.png>)

d+1 r+1

So, for any A ∈ Ck, on the one hand,

Γr(A) =

Γr({σ}) ≤

σ∈A

σ∈A

Γr({σ}) =

σ∈A

r + 1 k + 1 · w(σ) =

r + 1 k + 1 · A . (2.6)

On the other hand, since each τ ∈ Γr(A) contains at most k r+1+1 k-faces, i.e. τ can belong to at most k r+1+1 of the Γr({σ}), hence, from the previous calculation we get,

r + 1 k + 1 · A =

σ∈A

which ﬁnishes the proof.

Γr({σ}) ≤

r + 1 k + 1 ·

Γr({σ}) =

σ∈A

r + 1 k + 1 · Γr(A) , (2.7)

![image 15](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile15.png>)

![image 16](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile16.png>)

![image 17](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile17.png>)

![image 18](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile18.png>)

## 2.2 Links

Next we introduce the notion of a link of complex, which is a combinatorial analogue of a unit sphere in the complex. Thus, the links will serve us as local views of the complex.

- Deﬁnition 2.4 (Link). Let X be a d-complex and let σ ∈ X. The link of σ in X is deﬁned as the following (d − |σ|)-complex,

Xσ = {τ ∈ X|σ ⊔ τ ∈ X}. (2.8)

For any −1 ≤ k ≤ d − |σ|, denote by Cσk = Ck(Xσ,F2) the space of k-cochains of Xσ, by  · σ =  · kσ : Cσk → [0,1] the norm associated to the complex Xσ, and by δσ = δσk : Cσk → Cσk+1 the k-coboundry map.

Let us observe the following cases of degenerate links of a d-complex:

- • The link of the unique (−1)-face, the empty set ∅ ∈ X(−1), is the entire complex, X∅ = X.
- • The link of a (d − 1)-face is a 0-complex, i.e. a collection of isolated vertices.


So, in order to avoid these degenerate cases, by a proper link we mean a link of a face σ of dimension 0 ≤ dim(σ) ≤ d − 2.

- Deﬁnition 2.5 (Localization and lifting). Let X be a d-complex and let σ ∈ X. Deﬁne the following maps between the original complex, X, and the link complex, Xσ:


- • The ﬁrst map, called the localization (w.r.t. σ), takes a cochain of the original complex, and restrict only to the faces which contains σ, and then delete σ from each of them, producing a cochain of the link. Concretely,

Iσ : C∗ → Cσ∗−|σ|, Iσ(A) := {τ ∈ Xσ | τ ⊔ σ ∈ A}. (2.9)

- • The second map, called the lifting (w.r.t. σ), takes a cochain of the link complex, and adds σ to each face in it, producing a cochain of the original complex. Concretely,


Iσ : Cσ∗ → C∗+|σ|, Iσ(A) := {τ ⊔ σ ∈ X | τ ∈ A}. (2.10) Let us mention a few immediate observations about the localization and lifting operators. Let X be a d-complex, σ ∈ X, |σ| ≤ k ≤ d, A ∈ Cσk−|σ| and A′ ∈ Ck. Then the following holds:

Iσ ◦ Iσ(A) = A (2.11) Iσ ◦ Iσ(A′) = {τ ∈ A′ | σ ⊂ τ} (2.12)

δ ◦ Iσ(A) = Iσ ◦ δσ(A) (2.13)

The following three Lemmas 2.6, 2.7 and 2.8, describes some relations between the localization and lifting operators and the global and local norms of the complex (i.e. the norms of the original complex X and its links Xσ, for any σ ∈ X).

- Lemma 2.6. Let X be a d-complex and let σ ∈ X. For any 0 ≤ k ≤ d − |σ|, and any A ∈ Ck − |σ|σ, then,


Iσ(A) = |σ| + k + 1 k + 1 · w(σ) · A σ. (2.14)

Proof. Denote by, w = wX, the weight function of the original complex, and by, wσ = wXσ, the weight function of the link. In the language of links, the weight norm is interpreted as w(τ) = |Xτ(d−|τ|)|

(d|+1τ| )·|X(d)| (and similarly for wσ). Since the norm of a cochain is deﬁne by extending linearly the weight function, it is suﬃce to show the claim for A which is a singleton. So, for any τ ∈ Xσ(k) and A = {τ} ∈ Cσk, we have

![image 19](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile19.png>)

|(Xσ)τ(d − |σ| − |τ|)| d−|σ|+1

w(σ) · A σ = w(σ) · wσ(τ) = |Xσ(d − |σ|)|

·

![image 20](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile20.png>)

![image 21](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile21.png>)

d+1

|σ| · |X(d)|

|τ| · |Xσ(d − |σ|)|

= |Xσ∪τ(d − |σ ∪ τ|)|

= |Xσ(d − |σ|)|

|Xσ∪τ(d − |σ ∪ τ|)| d−|σ|+1

·

![image 22](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile22.png>)

![image 23](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile23.png>)

![image 24](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile24.png>)

d+1

|σ| · d−||στ||+1 · |X(d)|

d+1

|σ| · |X(d)|

|τ| · |Xσ(d − |σ|)|

d+1 |σ∪τ| d+1

1

· Iσ(A) , (2.15)

· w(σ ∪ τ) =

=

![image 25](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile25.png>)

![image 26](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile26.png>)

|σ| · d−||στ||+1

|σ|+|τ| |τ|

which ﬁnishes the proof.

![image 27](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile27.png>)

![image 28](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile28.png>)

![image 29](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile29.png>)

![image 30](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile30.png>)

- Lemma 2.7. Let X be a d-complex,σ ∈ X and let |σ| ≤ k ≤ d.

- 1. For any A,B ∈ Cσk−|σ|, then A σ ≤ B σ if and only if Iσ(A) ≤ Iσ(B) .
- 2. If A ∈ Ck, B ∈ Cσk−|σ| and A ≤ A + Iσ(B) , then Iσ(A) σ ≤ Iσ(A) + B σ.


Proof. 1. Follows immediately from Lemma 2.6.

- 2. First note that, every face of Iσ(B) contains σ, i.e. for any σ  ⊂ τ, τ ∈ A ⇔ τ ∈ A+Iσ(B). Combining this observation with equation (2.12), we get


A − IσIσ(A) =

τ∈A σ ⊂τ

w(τ) =

τ∈A+Iσ(B) σ ⊂τ

w(τ) = A + Iσ(B) − IσIσ(A + Iσ(B)) .

(2.16) Using now the assumption that A ≤ A + Iσ(B) , imply that

IσIσ(A) ≤ IσIσ(A + Iσ(B)) . (2.17) Finally applying fact 1. on the last inequality, together with equation (2.11), yields

Iσ(A) σ ≤ Iσ(A + Iσ(B)) σ = Iσ(A) + B σ (2.18) which ﬁnishes the proof.

![image 31](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile31.png>)

![image 32](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile32.png>)

![image 33](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile33.png>)

![image 34](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile34.png>)

- Lemma 2.8. Let X be a d-complex, 0 ≤ j ≤ k ≤ d, and let A ∈ Ck. Then


k + 1 j + 1 · A =

Iσ(Iσ(A)) . (2.19)

σ∈X(j)

Proof. By the deﬁnition of the norm and Fubini’s Theorem,

σ∈X(j)

Iσ(Iσ(A)) =

w(τ) =

σ∈X(j) σ⊂τ∈A

k + 1 j + 1 · w(τ) =

k + 1 j + 1 ·  A .

w(τ) =

τ∈A σ⊂τ

τ∈A

(2.20)

## 2.3 Skeletons

Here we deﬁne the notions of skeletons of a complex, which are basically what we get when we forget about the higher dimensional faces of the given complex.

- Deﬁnition 2.9 (Skeleton). Let X be a d-complex and let 0 ≤ k ≤ d. Then the k-skeleton of X is deﬁned as the following k-complex,


X(k) = {τ ∈ X|dim(τ) ≤ k}. For example, the 1-skeleton of a complex is simply its underlying graph.

Note that for any d-complex X, and any 0 ≤ t ≤ k ≤ d, the spaces of t-cochains of the complex and its k-skeleton, are the same, and for t < k, the t-coboundary operators of the complex and its k-skeleton, are also the same. On the other hand, the norms of the complex and its k-skeleton, might be quite diﬀerent. However, if the complex is of bounded degree, then the norms of X and X(k) are proportional.

- Lemma 2.10. Let t ≤ k ≤ d, Q ∈ N and let X be a d-complex which is Q-bounded degree at dimension k, i.e. maxσ∈X(k) |Xσ(d − |σ|)| ≤ Q. Then for any A ∈ Ct,


d + 1 k + 1 · A X (2.21)

1 Q · k d−−tt

· A X ≤ A X(k) ≤ Q ·

![image 39](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile39.png>)

Proof. Denote by, w = wX, the weight function of the original complex, and by, wk = wX(k), the weight function of the skeleton. Since the norm of a cochain is deﬁne by extending linearly the weight function, it is suﬃce to show the claim for A which is a singleton, i.e. it suﬃce to prove for any σ ∈ X(t),

d + 1 k + 1 · w(σ) (2.22)

1 Q · k d−−tt

· w(σ) ≤ wk(σ) ≤ Q ·

![image 40](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile40.png>)

Next note that, since the complex is pure and of Q-bounded degree at dimension k, then 1

· |X(k)| ≤ |X(d)| ≤ Q · |X(k)|. (2.23)

![image 41](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile41.png>)

d+1 k+1

Similarly, since that for any σ ∈ X(t), the link, Xσ, is pure and of Q-bounded degree at dimension k − t − 1, then

1

· |Xσ(k − t − 1)| ≤ |Xσ(d − t − 1)| ≤ Q · |Xσ(k − t − 1)|. (2.24)

![image 42](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile42.png>)

d−t k−t

we get that for any σ ∈ X(t),

d−t k−t · Q · |Xσ(d − t − 1)|

wk(σ) = |Xσ(k − t − 1)| k+1 t+1 · |X(k)|

d + 1 k + 1 · Q · w(σ), (2.25)

≤

=

![image 43](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile43.png>)

![image 44](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile44.png>)

k+1 t+1 · |X(d)|

and

w(σ) = |Xσ(d − t − 1)| d+1 t+1 · |X(d)|

≤

![image 45](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile45.png>)

which ﬁnishes the proof.

Q · k d+1+1 · |Xσ(k − t − 1)| d+1 t+1 · |X(k)|

=

![image 46](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile46.png>)

d − t k − t · Q · wk(σ), (2.26)

Next, we deﬁne a property of graph expansion for a complex, called skeleton expansion, which says that the 1-skeleton of the complex satisﬁes a form of weak mixing behavior.

- Deﬁnition 2.11 (Skeleton expander). Let X be a d-complex and let α > 0. Call X an αskeleton expander, if for any A ⊂ X(0), then

E(A,A) ≤ 4 · ( A 2 + α · A ) (2.27)

- where E(A,A) ⊂ X(1) are the edges in X with both vertices in A.


In section §4, we prove a one sided mixing Lemma for the skeleton of a regular complex, which gives a criterion for skeleton expansion in terms of non trivial eigenvalues.

2.4 High dimensional expansion

Here we present diﬀerent notions concerning high dimensional expansion for simplicial complexes, which arose in the works of Linial-Meshulam-Wallach [LinM], [MW] and Gromov [Gro].

- Deﬁnition 2.12 (Coboundary and cocycle expansion). Let X be a d-complex and 0 ≤ k < d. Deﬁne the k-dimensional cobonudary expansion parameter of X to be:

Expkb(X) = min{

δ(A)

![image 51](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile51.png>)

minb∈Bk A + b | A ∈ Ck \ Bk}. (2.28) Deﬁne the k-dimensional cocycle expansion parameter of X to be:

Expkz(X) = min{

δ(A) minz∈Zk A + z | A ∈ Ck \ Zk}. (2.29)

![image 52](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile52.png>)

Let us spell out what both expansion parameters says in the special case of graphs. In the graph case d = 1 and k = 0, the coboundaries are just V and ∅, and the cocycles are the unions of connected components of the graph. The cobonudary expansion parameter is equal to the Cheeger constant of the entire graph (up to some normalization), while the cocycle expansion parameter is equal to the minimum of the Cheeger constants in each connected component of the graph. So, a large cocycle expansion parameter imply that each connected component of the graph is a good expander on its own, however the graph itself can be disconnected, in particular not an expander.

Let us recall the deﬁnition of coboundary expanders, from the introduction.

- Deﬁnition 2.13 (Coboundary expander). A d-complex, X, is said to be an ǫ-coboundry expander, for some ǫ > 0, if Expkb(X) ≥ ǫ, for any 0 ≤ k ≤ d − 1.


The notion of coboundary expansion was ﬁrst originate in the work of [LinM], in connection to vanishing of cohomology. (The actual term, coboundary expansion, later came from [DK]). Recall that for any 0 ≤ k ≤ d, each k-coboundary is a k-cocycle, i.e. Bk(X;F2) ⊂ Zk(X;F2), and the k-th cohomology of X (in F2-coeﬃcients) is the quotient space

Hk(X;F2) = Zk(X;F2)/Bk(X;F2). (2.30) It is a simple exercise to see that the following equivalences holds:

Expkb(X) > 0 ⇔ Zk(X;F2) = Bk(X;F2) ⇔ Hk(X;F2) = 0. (2.31)

Furthermore, if the k-th cohomology is trivial, hence any k-cocycle is a k-coboundary, then the k-coboundary and k-cocycle expansion parameters are equivalent:

Hk(X;F2) = 0 ⇒ Expkb(X) = Expkz(X). (2.32) All in all we get the following equivalent characterization for coboundary expansion:

Expkb(X) ≥ ǫ ⇔ Expkz(X) ≥ ǫ and Zk = Bk. (2.33)

As noted by Gromov (see also [DKW]), this notion of vanishing of cohomology is too strong for some application, since the existence of a cocycle which is not a coboundary, is acceptable just as long as it is not too small. This is where the deﬁnition of cosystoles comes into play.

- Deﬁnition 2.14 (Cosystoles). Let X be a d-complex and 0 ≤ k ≤ d−1. Deﬁne the k-cosystole of X to be the minimal size of a k-cococycle which is not a k-coboundary, i.e.

Systk(X) = min{ z | z ∈ Zk(X,F2) \ Bk(X,F2)}. (2.34) Finally, we recall the deﬁnition of cosystolic expanders from the introduction.

- Deﬁnition 2.15 (Cosystolic expander). A d-complex X is said to be an (ǫ,µ)-cosystolic expander, for some ǫ,µ > 0, if Expkz(X) ≥ ǫ and Systk(X) ≥ µ, for any 0 ≤ k ≤ d − 1.


- Remark 2.16. In recent years, the notion of cosystoles (and its close cousin, systoles) over F2, have found applications in the ﬁeld of quantum error correcting codes (see [GL] and [EOT]), where good lower bounds on the systoles and cosystoles give rise to quantum codes with good parameters.


## 2.5 Minimal cochains

Let us now introduce the following notions of minimal and locally minimal cochains, which we will need later on to prove our local to global cosystolic expansion criterion.

- Deﬁnition 2.17 (Mininmal and locally minimal). A cochain A ∈ Ck is said to be minimal if A = min{ A + b | b ∈ Bk(X,F2)}. (2.35)


A cochain A ∈ Ck is said to be locally minimal if for any ∅ = σ ∈ X, the localization of A w.r.t. σ, Iσ(A), is a minimal cochain in the link Xσ.

Note that a d-complex, X, is an ǫ-coboundary expander if and only if for any 0 ≤ k ≤ d−1, any minimal k-cochain, A ∈ Ck, satisﬁes δ(A) ≥ ǫ · A .

- Lemma 2.18. If A ∈ Ck is a minimal cochain, then A is a locally minimal cochain. Proof. Let ∅ = σ ∈ X and let γ ∈ Cσk−1−|σ|. From the minimality of A, equation (2.13), and

- Lemma 2.7 part 1, we get that A ≤ A + δIσ(γ) = A + Iσδσ(γ) ⇒ Iσ(A) σ ≤ Iσ(A) + δσ(γ) σ. (2.36)


This proves that A is locally minimal.

![image 53](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile53.png>)

![image 54](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile54.png>)

![image 55](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile55.png>)

![image 56](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile56.png>)

- Lemma 2.19. If A is a minimal cochain and A′ ⊂ A, then A′ is also a minimal cochain.


Proof. First note that, since A\A′ and A′ are disjoint, A = A\A′ + A′ . Next note that, since the sum of two cochains is equal to their symmetric diﬀerence, for any cochain c ∈ Ck,

(A + c) \ (A′ + c) = ((A \ c) ∪ (c \ A)) \ ((A′ \ c) ∪ (c \ A′)) ⊂

⊂ ((A \ c) \ (A′ \ c)) ∪ ((c \ A) \ (c \ A′)) = ((A \ c) \ (A′ \ c)) ⊂ A \ A′ (2.37) where in the second to last step, the equality follows from the fact that A′ ⊂ A. Hence,

A + c − A′ + c ≤ (A + c) \ (A′ + c) ≤ A \ A′ = A − A′ (2.38) Now, if c ∈ Bk is a coboundry, then by the minimality of A we get,

A′ = A′ − A + A ≤ A′ − A + A + c ≤ A′ + c (2.39) where the last inequality is (2.38), which ﬁnishes the proof.

![image 57](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile57.png>)

![image 58](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile58.png>)

![image 59](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile59.png>)

![image 60](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile60.png>)

# 3 Cosystolic expansion criterion

In this section we prove the following local to global cosystolic expansion criterion. The following result is slightly stronger Theorem 1.10 from the introduction.

- Theorem 3.1. For any d ∈ N, β > 0 and Q ∈ N, there exists ǫ = ǫ(d,β,Q) > 0, µ = µ(d,β) > 0 and α = α(d,β) > 0, such that if X is a d-complex satisfying:

- • The complex X is Q-bounded degree, i.e. maxv∈X(0) |Xv| ≤ Q.
- • The link Xσ is a β-coboundry expander, for any σ ∈ X, 1 ≤ |σ| ≤ d − 1.
- • The link Xσ is an α-skeleton expander, for any σ ∈ X, 0 ≤ |σ| ≤ d − 1.


Then for any 0 ≤ k ≤ d − 2 and any 0 ≤ r ≤ d − 1,

Expkz(X) ≥ ǫ and Systr(X) ≥ µ (3.1) In particular, the (d − 1)-skeleton of X is an (ǫ,µ)-cosystolic expander.

In order to prove Theorem 3.1 we follow [KKL] strategy, who noticed that the following (co)isoperimetric inequality for small cochains imply cosystolic expansion.

- Theorem 3.2. For any d ∈ N and β > 0, there exists ¯ǫ = ǫ¯(d,β),µ¯ = µ¯(d,β) > 0 and α = α(d,β) > 0, such that if X is a d-complex satisfying:


- • The link Xσ is a β-coboundry expander, for any σ ∈ X, 1 ≤ |σ| ≤ d − 1.
- • The link Xσ is an α-skeleton expander, for any σ ∈ X, 0 ≤ |σ| ≤ d − 1.


Then for any 0 ≤ k ≤ d − 1, A ∈ Ck is locally minimal and A ≤ µ¯ =⇒ δ(A) ≥ ǫ¯· A (3.2)

- Remark 3.3. Note that Theorem 3.2, unlike Theorem 3.1, does not require any bounded degree assumption. This simple fact, makes Theorem 3.2 useful also for unbounded degree complexes, as was shown in [LLR], who proved that for any d ∈ N, there exists d-dimensional coboundary expanders, which are of bounded degree at dimension d − 1, i.e., every (d − 1)-face is contained in a bounded number of d-faces. (The work [LLR] is a generalization of [LubM]).


- Remark 3.4. The constants in Theorem 3.1, are


β (d + 2) · 2d+2

1 3(d + 2)2d+3 ·

µ :=

![image 61](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile61.png>)

![image 62](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile62.png>)

The constants in Theorem 3.2, are

d 2d+1

1 Q

, ǫ := min{

![image 63](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile63.png>)

- 1

![image 64](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile64.png>)

- 2d+1 . (3.3)


,µ}, α := µ1+

µ¯ :=

1 3(d + 2)2d+3 ·

![image 65](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile65.png>)

β (d + 2) · 2d+2

![image 66](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile66.png>)

d 2d+1

1 3·

, ¯ǫ :=

![image 67](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile67.png>)

β (d + 2) · 2d+2

![image 68](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile68.png>)

d

- 1

![image 69](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile69.png>)

- 2d+1 . (3.4)


, α := µ1+

We note that we made no attempt to optimize the constants in this work.

## 3.1 Sketch of the proof of Theorem 3.2

Before diving into the proof of Theorem 3.2, which require us to deﬁne a few new technical notions, we would like to provide a proof sketch.

Fix a locally minimal cochain, A ∈ Ck. We deﬁne the notion of fat faces with respect to A in the complex, which essentially says that a face is fat if the localization of A with respect to that face, is large. Consider the coboundaries of the localization of A with respect to the fat faces, and note that these ”local” coboundaries are large by the assumption that the links are cobundary expanders. The main idea of the proof is that each such ”local” coboundary, is either an actual coboundary in the original complex, or it contains a fat face of smaller dimension. This last claim, is the content of Proposition 3.11, where the term Lη(A,i) essentially stands for the sub-cochain of elements in A which contains a fat i-faces, and Υη(A) stands for the error term. This error term is negligible due to the skeleton expansion assumption (Proposition 3.12). So, iterating Proposition 3.11, we get that either δ(A) is large, or that there is a fat (−1)-face. But the unique (−1)-face is fat precisely when A is large, which ﬁnishes the proof.

## 3.2 Fat machinery

In order to prove the (co)isoperimetric inequality (Theorem 3.2), we ﬁrst construct a ”fatmachinery” which allow us to move calculations from higher to lower dimensions in the complex.

- Deﬁnition 3.5 (Fat faces). Fix a cochain A ∈ Ck and 0 < η < 1. Deﬁne inductively the i-cochain of fat faces, w.r.t. A and η, i = 0,... ,k, by


Sηk(A) = A and Sηi−1(A) = {σ ∈ X(i − 1)| Iσ(Sηi(A)) σ ≥ η2k−i} (3.5) For i = −1,0,... ,k, call the elements of Sηi(A) fat faces (w.r.t. A and the fatness constant η).

The following Lemma shows that the sizes of the cochains of fat faces is bounded by the size of the original cochain (up to some constant).

- Lemma 3.6. Let X be a d-complex, −1 ≤ i ≤ k ≤ d, A ∈ Ck and 0 < η < 1. Then, Sηi(A) ≤ η−2k−i · A (3.6)


Proof. For any, −1 ≤ j ≤ k − 1, and any fat j-face, σ ∈ Sηj(A), by applying Lemma 2.6 on the cochain Iσ(Sηj+1(A)) ∈ Cσ0, we get

Iσ(Iσ(Sηj+1(A))) (j + 2) · Iσ(Sηj+1(A)) σ

η−2k−j−1 j + 2 · Iσ(Iσ(Sηj+1(A))) (3.7)

≤

w(σ) =

![image 70](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile70.png>)

![image 71](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile71.png>)

Hence, combining this with Lemma 2.8,

η−2k−j−1 j + 2 ·

Sηj(A) =

w(σ) ≤

![image 72](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile72.png>)

σ∈Sηj(A)

σ∈Sηj(A)

Iσ(Iσ(Sηj+1(A))) = η−2k−j−1 · (Sηj+1(A)) (3.8)

Hence, by iterating on equation (3.8) for j = i,... ,k − 1, we get,

Sηi(A) ≤ η−2k−i−1 · (Sηi+1(A)) ≤ η−(2k−i−1+2k−i−2) · (Sηi+2(A)) ≤ ...

k−1

j=i 2k−j Sηk(A) = η−2k−i+1 · A ≤ η−2k−i · A (3.9) which ﬁnishes the proof.

... ≤ η−

![image 73](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile73.png>)

![image 74](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile74.png>)

![image 75](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile75.png>)

![image 76](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile76.png>)

From Lemma 3.6, we get the following consequence, which says that for a small cochain the unique (−1)-face is a non-fat face. (This simple fact will serve as the ﬁnishing argument in the proof of Theorem 3.2).

- Corollary 3.7. Let X be a d-complex, k ≤ d, A ∈ Ck and 0 < η < 1. If A < η2k+1 then the unique (−1)-face, the empty set is not a fat face, i.e. ∅  ∈ Sη−1(A).


Proof. Note that the empty set has the following interesting property: ”A local view by ∅ is everything”, i.e. for any Y ⊂ X then I∅(Y ) = Y and   ·  ∅ =   ·  . So, from Lemma 3.6 and the assumption on the size of A, we get

I∅(Sη0(A)) ∅ = Sη0(A) ≤ η−2k · A < η2k (3.10) hence, by deﬁnition, the empty set is not a fat face.

![image 77](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile77.png>)

![image 78](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile78.png>)

![image 79](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile79.png>)

![image 80](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile80.png>)

Next, we deﬁne the cochain of degenerate faces, which intuitively one should think of as the error-term when one is trying to move from higher dimension to lower dimension.

- Deﬁnition 3.8 (Degenerate faces). Fix a cochain A ∈ Ck and 0 < η < 1. A dead-end is a pair of two equal sized fat faces, (σ,σ′), whose intersection is a codimension-1 non-fat face, i.e.


|σ| = |σ′| = |σ ∩ σ′| + 1, σ,σ′ ∈ Sη∗(A), σ ∩ σ′  ∈ Sη∗−1(A) (3.11)

A face p ∈ X is said to be degenerate if it contains a dead-end in it, and deﬁne Υη(A) ∈ Ck+1 to be the cochain of all (k + 1)-faces which are degenerate.

Next, we deﬁne the notion of a fat ladder.

- Deﬁnition 3.9 (Fat ladders). Fix a cochain A ∈ Ck and 0 < η < 1. For any fat i-face, σ ∈ Sηi(A), deﬁne the k-cochain of fat-ladders of A, siting on σ, to be


Lη(A,σ) = {t ∈ A|∃ σ = σi ⊂ ... ⊂ σk = t, σj ∈ Sηj(A), ∀ j = i,... ,k} (3.12) Deﬁne the k-cochain of i-fat-ladders of A, by Lη(A,i) = σ∈Si

η(A) Lη(A,σ).

The next lemma essentially says that if inside a (k + 1)-face you have a fat ladder and a fat k-face, then you can either go down to a deeper ladder, or you contain a dead end, which makes the ambient face degenerate.

- Lemma 3.10. Let X be a d-complex, −1 ≤ i ≤ k ≤ d, A ∈ Ck and 0 < η < 1. Let σ ∈ Sηi(A), t ∈ Lη(A,σ), t′ ∈ A and t,t′ ⊂ p ∈ X(k + 1). Then, either t′ ∈ Lη(A,t′ ∩ σ) or p ∈ Υη(A).


Proof. By deﬁnition, there exists σ = σi ... σk = t, where all σj are fat. Deﬁne σk′ = t′ and σj′−1 = t′ ∩ σj = σj′ ∩ σj for any j = i,... ,k. If all the σj′ are fat, and since t′ ∩ σ = σi′−1 ⊂ ... ⊂ σk′ = t′, so by removing repetitions if needed (σj′ = σj′+1) we get that t′ ∈ Lη(A,t′ ∩ σ). Otherwise, there is a non-fat σj′, and w.l.o.g. we may assume j is maximal, i.e. σj′+1 is fat, and since that σj+1  ⊂ t′ (otherwise σj′ = σj+1 is fat), we get that |σj+1| = |σj′+1| = |σj+1 ∩σj+1|−1, hence p ∈ Υη(A).

![image 81](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile81.png>)

![image 82](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile82.png>)

![image 83](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile83.png>)

![image 84](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile84.png>)

## 3.3 Proof of Theorem 3.2

The following Proposition is the heart of the ”fat machinery” which will allow us to move calculations from higher to lower dimensions.

- Proposition 3.11. Let k < d ∈ N, 0 < η < 1, 0 < β and let X be a d-complex such that for


any σ ∈ X, 1 ≤ |σ| ≤ d − 1, the link, Xσ, is a β-coboundary expander. Then for any locally minimal k-cochain, A ∈ Ck, and any 0 ≤ i ≤ k,

β

· Lη(A,i) ≤ δ(A) + (k + 2) · Lη(A,i − 1) + Υη(A) (3.13)

![image 85](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile85.png>)

k+2 i+1

Proof. Let us evaluate the following expression, R =

Iσ ◦ δσ ◦ Iσ(Lη(A,σ)) ⊂ X(k + 1). (3.14)

σ∈Si(A)

On the one hand, since A is locally minimal, then Iσ(A) is minimal, and Iσ(Lη(A,σ)) ⊂ Iσ(A), so by Lemma 2.19 , Iσ(Lη(A,σ)) is also minimal. So, by the assumption that all the proper links of X are β-coboundry expanders, we get that for any σ ∈ Sηi(A) ⊂ X(i),

β · Iσ(Lη(A,σ)) σ ≤ δσ ◦ Iσ(Lη(A,σ)) σ. (3.15)

Note that Lη(A,σ) ⊂ {τ ∈ X(k)|σ ⊂ τ}, hence by equation (2.12), Iσ◦Iσ(Lη(A,σ)) = Lη(A,σ). Combining this with equation (3.15), Lemma 2.7 part 1, and the fact that each element of R

contains at most ki+1+2 faces from Sηi(A) ⊂ X(i), we get

k + 2 i + 1 · R . (3.16)

Iσ◦δσ ◦Iσ(Lη(A,σ)) ≤

β· Lη(A,i) ≤

β· Lη(A,σ) ≤

σ∈Sηi (A)

σ∈Sηi (A)

On the other hand, for any σ ∈ Sηi(A) and any p ∈ Iσ ◦ δσ ◦ Iσ(Lη(A,σ)), one of the following three possibilities must occur:

- 1. All the k-faces in p which belongs to A, contains σ, and they are all from Lη(A,σ). In this case p ∈ δ(A).
- 2. All the k-faces in p which belongs to A, contains σ, but not all of them are from Lη(A,σ). In this case there is some t′ ∈ A \ Lη(A,σ) such that σ ⊂ t′ ⊂ p. Now, since p ∈ Iσ ◦ δσ ◦ Iσ(Lη(A,σ)), there must be at least one t ∈ Lη(A,σ) such that t ⊂ p. So, by Lemma 3.10 we get that p ∈ Υη(A).
- 3. There is a k-face in p which belongs to A, and it does not contain σ. In this case there is some, t′ ∈ A, such that σ  ⊂ t′ ⊂ p. Like before, since p ∈ Iσ ◦ δσ ◦ Iσ(Lη(A,σ)), there must be at least one t ∈ Lη(A,σ) such that t ⊂ p. And again by Lemma 3.10 we get that either p ∈ Υη(A), or t′ ∈ Lη(A,t′ ∩σ) ⊂ Lη(A,i−1), i.e. p is a (k+1)-face which contains a k-face from Lη(A,i − 1), hence by deﬁnition 2.2 p ∈ Γk+1(Lη(A,i − 1)).


In conclusion we get that

R ⊂ δ(A) ∪ Γk+1(Lη(A,i − 1)) ∪ Υη(A). (3.17) Combining equation (3.16) and (3.17), together with Lemma 2.3, yields

β

· Lη(A,i) ≤ R ≤ δ(A) + (k + 2) · Lη(A,i − 1) + Υη(A) (3.18)

![image 86](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile86.png>)

k+2 i+1

which ﬁnishes the proof.

![image 87](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile87.png>)

![image 88](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile88.png>)

![image 89](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile89.png>)

![image 90](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile90.png>)

The following Proposition gives an eﬀective bound on the cochain of degenerate faces in terms of the skeleton expansion and the fatness constant.

- Proposition 3.12. Let k < d ∈ N, 0 < η < 1, 0 < α ≤ η2k+1 and let X be a d-complex such


that for any σ ∈ X, 0 ≤ |σ| ≤ d − 1, the link, Xσ, is an α-skeleton expander. Then for any k-cochain A ∈ Ck,

Υη(A) ≤ (k + 2) · 2k+4 · η · A . (3.19)

Proof. For any t ≤ d and any t-cochain Y , denote by E(Y,Y ) the (t+1)-cochain of (t+1)-faces which contains at least two diﬀerent t-faces from Y , and let Γk+1(Y ) ∈ Ck+1 be as in Lemma

- 2.3. Then, by the deﬁnition of the fat-degenerate faces, we get


k−1

Γk+1(Iσ(E(Iσ(Sηi+1(A)),Iσ(Sηi+1(A))))) (3.20)

Υη(A) =

i=−1 σ∈X(i)\Sηi (A)

So, by Lemma 2.3, we get

k−1

Υη(A) ≤

i=−1 σ∈X(i)\Sηi (A)

k + 2 i + 2 · Iσ(E(Iσ(Sηi+1(A)),Iσ(Sηi+1(A)))) (3.21)

From the skeleton expansion, we get for any σ ∈ X(i),

E(Iσ(Sηi+1(A)),Iσ(Sηi+1(A))) σ ≤ 4 · Iσ(Sηi+1(A)) σ · ( Iσ(Sηi+1(A)) σ + α) (3.22)

Now, by the Lemma 2.6, we can multiply both sides by |σ k| · w(σ), and get

Iσ(E(Iσ(Sηi+1(A)),Iσ(Sηi+1(A)))) ≤ 4 · Iσ(Iσ(Sηi+1(A))) · ( Iσ(Sηi+1(A)) σ + α) (3.23) Next, if σ ∈ X(i) \ Sηi(A), then by the deﬁnition of fat faces,

Iσ(E(Iσ(Sηi+1(A)),Iσ(Sηi+1(A)))) ≤ 4 · Iσ(Iσ(Sηi+1(A))) · (η2k−i + α) (3.24) Summing this over all non-fat i-faces,

Iσ(E(Iσ(Sηi+1(A)),Iσ(Sηi+1(A)))) ≤ 4(η2k−i+α)·

Iσ(Iσ(Sηi+1(A)))

σ∈X(i)\Sηi (A)

σ∈X(i)\Sηi (A)

Iσ(Iσ(Sηi+1(A))) = 4(η2k−i + α) · (i + 2) · Sηi+1(A) (3.25)

≤ 4(η2k−i + α) ·

σ∈X(i)

where the last equality follows from Lemma 2.8. Applying Lemma 3.6, we get

σ∈X(i)\Sηi (A)

Iσ(E(Iσ(Sηi+1(A)),Iσ(Sηi+1(A)))) ≤ 4(i+2)·(η2k−(i+1) +α·η−2k−(i+1))· A (3.26)

Combining equations (3.21) and (3.26) together, we get

k−1

k + 2 i + 2 · 4(i + 2) · (η2k−(i+1) + α · η−2k−(i+1)) · A

Υη(A) ≤

i=−1

k−1

k−1

k + 2 i + 2 · (i + 2) ·(η2k−k+α·η−2k−0)· A ≤ 4(k + 2) ·

k + 1 i + 1 ·(η+α·η−2k)· A

≤ 4 ·

i=−1

i=−1

≤ (k + 2) · 2k+3 · (η + α · η−2k) · A ≤ (k + 2) · 2k+3 · 2η · A (3.27) which ﬁnishes the proof.

![image 91](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile91.png>)

![image 92](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile92.png>)

![image 93](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile93.png>)

![image 94](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile94.png>)

Finally, we are able to prove the isoperimetric inequality for small cochains (Theorem 3.2). Proof of Theorem 3.2. Deﬁne the following constants,

ck0 2

ǫ¯ (k + 2)2k+4

β (k + 2) · 2k+2

, µ¯ := η2k+1 and α := η2k+1+1. (3.28)

, ǫ¯ :=

, η :=

c0 :=

![image 95](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile95.png>)

![image 96](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile96.png>)

![image 97](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile97.png>)

Note that by deﬁnition Lη(A,k) = A, and if A ≤ µ¯ = η2k+1, then by Corollary 3.7 the only (−1)-face, the empty set, is non fat (w.r.t. A and η), and hence Lη(A,−1) = 0. Therefore, for any constant c ≤ 1 we get,

k

k

ci−1(c· Lη(A,i) − Lη(A,i−1) ) ≤

ck · A =

(c· Lη(A,i) − Lη(A,i−1) ). (3.29)

i=0

i=0

Note that c0 ≤ 1 and that (k + 2) · c0 ≤ (ki+1+2β )

, for any 0 ≤ i ≤ k. So, by applying Proposition 3.11 on equation (3.29), with the constant c0, we get

![image 98](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile98.png>)

1 k + 2 ·

ck0 · A ≤

![image 99](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile99.png>)

k

β

·  Lη(A,i)  −(k +2) · Lη(A,i −1) ) ≤ δ(A) + Υη(A) . (3.30)

(

![image 100](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile100.png>)

k+2 i+1

i=0

Combining this with Proposition 3.12, we get

δ(A) ≥ (ck0 − (k + 2)2k+4 · η) · A = ǫ¯· A , (3.31) which ﬁnishes the proof.

![image 101](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile101.png>)

![image 102](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile102.png>)

![image 103](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile103.png>)

![image 104](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile104.png>)

## 3.4 Proof of Theorem 3.1

The fact that a coisoperimetric inequality for small cochains (Theorem 3.2), implies a cosystolic expansion (Theorem 3.1), was ﬁrst shown in [KKL, § 4], but for the sake of being self-contained we add here their argument.

- Proposition 3.13. [KKL, Proposition 2.5] Let X be a d-complex, and deﬁne Q = maxv∈X(0) |Xv|. Let 0 ≤ k ≤ d. Then for any A ∈ Ck, there exists γ ∈ Ck−1, which satisﬁes:


- 1. The cochain A + δ(γ) is locally minimal.
- 2. A + δ(γ) ≤ A .
- 3. γ ≤ Q · A .


Proof. First note that N(A) := k d+1+1 ·|X(d)|· A is a non-negative integer. We prove the claim by induction on N(A). In the base case N(A) = 0, then A = ∅ ∈ Ck is the empty k-cochain, and the claim holds for γ = ∅ ∈ Ck−1 the empty (k − 1)-cochain. Assume the claim holds for all cochains A′ ∈ Ck such that N(A′) < N(A), i.e. such that A′ < A .

If A is locally minimal, then the claim holds for γ = ∅ ∈ Ck−1 the empty (k − 1)-cochain. Otherwise, there exist ∅ = σ ∈ X, and some c ∈ Cσk−1−|σ|, such that

Iσ(A) + δσ(c) σ < Iσ(A) σ (3.32) Denote c′ = Iσ(c) ∈ Ck−1. Then by equation (2.13) and Lemma 2.7 part 2, we get

A + δ(c′) < A . (3.33)

So, N(A + δ(c′)) < N(A), and since both are natural numbers, then N(A + δ(c′)) ≤ N(A) − 1. By the induction assumption there exist γ′ ∈ Ck−1, such that:

- 1. (A + δ(c′)) + δ(γ′) = A + δ(c′ + γ′) is a locally minimal cochain,
- 2. A + δ(c′ + γ′) ≤ A + δ(c′) < A , and
- 3. γ′ ≤ Q · A + δ(c′) ≤ Q · ( A − (kd+1+1)1·|X(d)|).


![image 105](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile105.png>)

Hence by taking γ = γ′ + c, and noting that c ≤ (kd+1+1)Q·|X(d)| (since c ⊂ Xσ and |Xσ| ≤ Q), we get that γ ≤ γ′ + c ≤ Q · A , which ﬁnishes the proof.

![image 106](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile106.png>)

![image 107](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile107.png>)

![image 108](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile108.png>)

![image 109](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile109.png>)

![image 110](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile110.png>)

Now, using Proposition 3.13 and the isoperimetric inequality for small cochains (Theorem 3.2), we are able to prove the cosystolic expansion criterion (Theorem 3.1). Proof of Theorem 3.1. Let µ¯ and ǫ¯be the constants from Theorem 3.2 and let Q = maxv∈X(0) |Xv|. Deﬁne ǫ = min{µ,¯ Q1 } and µ = µ¯.

![image 111](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile111.png>)

We begin by proving the cocycle expansion. Let A ∈ Ck. First note that if δ(A) ≥ µ, and since A ≤ 1 for any cochain, then

δ(A) ≥ µ ≥ ǫ ≥ ǫ · A (3.34)

So, let us assume δ(A) ≤ µ, and let γ ∈ Ck, be as in Proposition 3.13 apply on the cochain δ(A). Then δ(A) + δ(γ) = δ(A + γ) is a locally minimal cochain and δ(A + γ) ≤ δ(A) ≤ µ. By Theorem 3.2 and the fact that δ ◦ δ = 0 we get that

0 = δ(δ(α + γ)) ≥ ¯ǫ · δ(α + γ) ⇒ δ(α + γ) = 0. (3.35) So, A + γ ∈ Zk, and hence γ = A + (A + γ) ∈ {A + z | z ∈ Zk}. Now, by Proposition 3.13 part

(3), γ ≤ Q · δ(A) , and we get

1 Q · γ ≥ ǫ · γ = ǫ · A + (A + γ) ≥ ǫ · min

δ(A) ≥

A + z (3.36)

![image 112](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile112.png>)

z∈Zk

which gives us the cocycle expansion Expkz(X) ≥ ǫ.

Next we prove the cosystolic bound. Let A ∈ Zk \ Bk (if no such cocycle exists there is nothing to prove). By Proposition 3.13, let A′ = A + δ(γ) be such that A′ is locally minimal and A′ ≤ A . Note that since A ∈ Zk \ Bk and δ(γ) ∈ Bk then A′ ∈ Zk \ Bk also. If

A′ ≤ µ = µ¯, then by Theorem 3.2 and the fact that A′ is a cocycle, we get 0 = δ(A′) ≥ ¯ǫ · A′ ⇒ A′ = 0 (3.37)

which is a contradiction since, 0 ∈ Bk, and A′ is not in Bk. So, A ≥ A′ ≥ µ, which gives us the cosystolic bound Systk(X) ≥ µ.

![image 113](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile113.png>)

![image 114](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile114.png>)

![image 115](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile115.png>)

![image 116](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile116.png>)

# 4 Skeleton mixing lemma

The purpose of this section is to prove a one sided mixing lemma for the 1-skeleton of a regular complex (see below), i.e. giving a spectral criterion for skeleton-expansion.

- Remark 4.1. We note that mixing behavior, spectral gaps and random walks of high dimensional complexes, are subjects that have been already intensively studied in several works (see [EGL], [GS], [GW], [KM1], [KM2], [KR], [Opp] [Par], [PRT], [PR] and [Ros]). The mixing Lemma that we present here, is much simpler then the ones appearing in the above mentioned works, and it is actually a result about partite-regular graph, rather then complexes.


- Deﬁnition 4.2 (Regular complex). A d-complex X, is said to be regular if it satisﬁes:


- • There exist a partition of the vertices X(0) = di=0 Vi, such that X(d) ⊂ di=0 Vi.
- • For any I ⊂ J ⊂ [d] := {0,1,... ,d}, there exist kIJ ∈ N, such that each p ∈ X ∩ i∈I Vi, is contained in exactly kIJ faces from X ∩ j∈J Vj.


For example, in the simplest case where X is of dimension 1, i.e. a graph, then X is a regular complex if and only if X is a bipartite biregular graph.

- Remark 4.3. Note that if X is a regular complex, then so does all of its links and skeletons. Next, we deﬁne what is the ”second eigenvalue” of the 1-skeleton of a regular complex.


- Deﬁnition 4.4 (Non-trivial eigenvalue). Let X be a regular d-complex. For any 0 ≤ i < j ≤ d, deﬁne the (i,j)-type induced bipartite graph to be X(i,j) = (Vi Vj,X(1) ∩ Vi × Vj). Denote by λ(X(i,j)) its normalized second largest eigenvalue. Deﬁne the normalized largest non-trivial eigenvalue of (the 1-skeleton of) X to be


λ(X) := max

λ(X(i,j)).

i =j

Let us now state the one sided mixing lemma for the 1-skeleton of a regular complex.

- Proposition 4.5. Let X be a regular complex, and let λ(X) be its normalized largest non-trivial eigenvalue. Then, for any A,B ⊂ X(0),


d + 1 d

![image 117](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile117.png>)

) · ( A · B + λ(X) · A · B ) (4.1)

E(A,B) ≤ 2(

![image 118](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile118.png>)

- where E(A,B) ⊂ X(1) are the edges in X with vertices from both A and B. Note that in the 1-dimensional case, such a Mixing Lemma is already known.


- Lemma 4.6. [EGL, Corollary 3.4] Let G = (V1 V2,E) be a bipartite biregular graph, and let λ(G) be its normalized second largest eigenvalue. Then, for any A ⊂ V1 and any B ⊂ V2,


![image 119](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile119.png>)

|B| |V2|

|B| |V2|

|A| |V1|

|E(A,B)| |E(X)|

|A| |V1|

−

| ≤ λ(G) ·

|

(4.2)

![image 120](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile120.png>)

![image 121](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile121.png>)

![image 122](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile122.png>)

![image 123](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile123.png>)

![image 124](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile124.png>)

This bipartite mixing lemma will imply the general skeleton mixing lemma.

Proof of Proposition 4.5. First note that since X is a regular complex, and let X(0) = di=0 Vi be the partition, then for any I ⊂ [d] and A ⊂ X ∩ i∈I Vi,

= |A| · kI[d] |X ∩ i∈I Vi| · kI[d]

= |A| |X ∩ i∈I Vi|

|{F ∈ X(d)|σ ∈ F}| |X(d)|

d + 1 |I|

· A =

(4.3)

![image 125](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile125.png>)

![image 126](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile126.png>)

![image 127](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile127.png>)

σ∈A

In particular, for any i,j ∈ [d] and any A ⊂ Vi,B ⊂ Vj,

|A| |Vi|

|B| |Vj|

|E(A,B)| |X(1) ∩ Vi × Vj|

1

- 1

![image 128](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile128.png>)

d+1

- 2


1

, B =

, and E(A,B) =

(4.4)

A =

![image 129](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile129.png>)

![image 130](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile130.png>)

![image 131](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile131.png>)

![image 132](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile132.png>)

![image 133](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile133.png>)

d+1 1

d+1 1

So restating Lemma 4.6 in terms of the complex norm, we get for any A ⊂ Vi,B ⊂ Vj,

2

d+1 1

E(A,B) ≤

![image 134](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile134.png>)

d+1 2

A · B + λ(X(i,j))

d+1

- 1

![image 135](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile135.png>)

d+1

- 2


≤ 2(

![image 136](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile136.png>)

A · B

λ(X) d + 1 · A · B ) (4.5)

d + 1 d

![image 137](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile137.png>)

) · ( A · B +

![image 138](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile138.png>)

![image 139](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile139.png>)

Now, let A,B ⊂ X(0), and denote Ai = A ∩ Vi and Bi = B ∩ Vi for any 0 ≤ i ≤ d. Since X is partite, E(A,B) = i =j E(Ai,Bj), hence

E(A,B) =

i =j

d + 1 d

) ·

E(Ai,Bj) ≤ 2(

![image 140](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile140.png>)

λ(X) d + 1

( Ai · Bj +

![image 141](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile141.png>)

i =j

![image 142](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile142.png>)

Ai · Bj ) (4.6)

Similarly, since A = i Ai and B = j Bj, then

i =j

Ai · Bj ≤ (

i

Ai ) · (

j

Bj ) = A · B (4.7)

Next, note that for any N non-negative numbers x1,... ,xN ∈ R≥0, one has

N

N

x2i (4.8)

xi)2 ≤ N · max

(x2i ) ≤ N ·

(

1≤i≤N

i=1

i=1

Applying this for N = (d + 1)2 and xi = Ai · Bj , we get

![image 143](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile143.png>)

![image 144](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile144.png>)

![image 145](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile145.png>)

Ai · Bj ≤ (d + 1)2 ·

Ai · Bj ≤ (d + 1) · A · B (4.9)

i,j

i,j

which ﬁnishes the proof.

In particular, since 2(d+1d ) ≤ 4 for any d ∈ N, we get the following.

![image 146](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile146.png>)

- Corollary 4.7. Let X be a regular d-complex. Then X is an λ(X)-skeleton expander.


![image 147](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile147.png>)

![image 148](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile148.png>)

![image 149](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile149.png>)

![image 150](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile150.png>)

# 5 Spherical buildings

The object of this section is to introduce the notion of spherical buildings, and to show that they are good skeleton expanders.

## 5.1 Deﬁnition of spherical buildings

Here we give a deﬁnition of spherical buildings, and list some of their properties which we shall use. For more on buildings we refer to [AB].

Before deﬁning a building, let us ﬁrst deﬁne the notion of a chamber complex.

- Deﬁnition 5.1 (Chamber complex). A d-dimensional simplicial complex, X, is said to be a chamber complex, if it is pure (i.e. all maximal faces are d-dimensional), and for any two maximal faces C,C′ ∈ X(d), there is a sequence of d-faces, C = C1,... ,Cn = C′, such that for each i = 1,... ,n − 1, the intersection Ci ∩ Ci+1 is a (d − 1)-face.


For a d-dimensional chamber complexes, call a d-face a chamber, call a (d−1)-face a panel, and call a sequence as above, C = C1,... ,Cn = C′, a gallery from C to C′.

A chamber complex, X, is said to be thin if each panel is contained in exactly 2 chambers, and it is said to be q-thick, q > 1, if each panel is contained in exactly q + 1 chambers. By a thick chamber complex, we mean q-thick for some q > 1.

Then, one way to deﬁne a building is as follows (for the equivalence for the more common deﬁnition, see [AB, Theorem 4.131]).

- Deﬁnition 5.2 (Building). A building is a thick chamber complex together with a family of subcomplexes, called apartments, which satisfy the following axioms:


- • Each apartment is a thin chamber complex.
- • Any two faces in the complex are contained in a common apartment.
- • Any two apartments have an isomorphism which ﬁxes their intersection.


A building is said to be spherical/aﬃne/hyperbolic if it is ﬁnite/locally ﬁnite/otherwise, respectively.

Let us note that if B is a d-dimensional building (i.e. a d-dimensional chamber complex which satisfy the axioms of the building), then each apartment of B is also d-dimensional.

- Remark 5.3. Throughout this paper we only concerns ourselves with buildings which are simplicial complexes. However, it should be mentioned that buildings can also be poly-simplicial complexes (just by allowing chamber complexes to be such).


Let us present an example of a spherical building.

Example 5.4. [AB, § 4.3] Let q be a prime power, d ∈ N, and denote V = Fdq. Consider the simplicial complex, P(V ), whose vertices are the proper (i.e. not {0} or V ) subspaces of V , and

his faces are the ﬂags of subspaces in V , i.e. {0} < W1 < ... < Wt < V . Then P(V ) is a (d − 2)-dimensional q-thick spherical building. Moreover, the group PGLd(Fq) acts on P(V ) in a strongly transitive way (see below).

Next, we wish to list some basic properties of spherical buildings, for the complete proofs we refer to [AB].

- Lemma 5.5. For any d ∈ N deﬁne θd := max{2d · (d + 1)!,192 · 11!}. Then each apartment in a d-dimensional spherical building is of size at most θd.


Proof. By [AB, Theorem 4.131] each apartment in a spherical building is a spherical Coxeter complex, and by [AB, § 1.3,1.5.6] the spherical Coxeter complexes were completely classiﬁed, and θd is taken to be the maximal size of all such possible complexes.

![image 151](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile151.png>)

![image 152](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile152.png>)

![image 153](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile153.png>)

![image 154](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile154.png>)

- Corollary 5.6. For any d,q ∈ N deﬁne θd := max{2d · (d + 1)!,192 · 11!} and Qd,q := ((d + 1) · (q + 1))θd. Then each d-dimensional q-thick spherical building is of size at most Qd,q.


Proof. Let C0 some chamber in the building. Since the building is d-dimensional and q-thick, we get that C0 has at most (d + 1) · (q + 1) chambers of gallery distance at most 1 from C0. Iterating this fact we get that there are at most ((d+1)·(q+1))n chambers of gallery distance at most n from C0. Since each chamber in the building is contained in some apartment containing C0, and since the distance of two chambers inside the apartment is at most the size of the apartment, which by Lemma 5.5 is at most θd, the claim is proven.

![image 155](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile155.png>)

![image 156](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile156.png>)

![image 157](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile157.png>)

![image 158](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile158.png>)

- Remark 5.7. The bound ((d+1)·(q +1))θd on the size of the spherical building is by no mean tight, since we are not trying to optimize the constants in this work.


Deﬁnition 5.8 (Type function). A d-dimensional complex, X, is said to admit a (d + 1)-type function on the vertices if there is a function τX : X(0) → [d] := {0,1,... ,d}, such that, setting Vi := τX−1({i}) for i = 0,... ,d, then X(0) = di=0 Vi and X(d) ⊂ di=0 Vi.

- Lemma 5.9. [AB, Proposition 4.6] Let B be a d-dimensional building. Then B admits a (d + 1)-type function on its vertices.
- Lemma 5.10. [AB, Proposition 4.9] Let B be a building and let σ ∈ B be any face in it. Then the link, Bσ, is also a building.
- Lemma 5.11. [AB, Proposition 4.40] Let B be a building and let A be an apartment in it. Then A is gallery convex, i.e. for any two chambers in A, C,C′ ∈ A, and any gallery from C to C′ in the building B, C = C0,... ,Cn = C′, which is of minimal length among all possible galleries from C to C′, then the gallery sits completely inside the apartment A, i.e. C0,... ,Cn ∈ A.
- Lemma 5.12. [AB, Proposition 5.122 (2)] Let B be a spherical building and let C be a chamber


in B. For any apartment containing C, A, there is a unique chamber in A, denoted CAop, which is of maximal gallery distance from C.

Next we deﬁne a notion of a building which posses many symmetries.

Deﬁnition 5.13 (Strongly transitive action). A building, B, is said to posses a strongly transitive action, if there exist a group of automorphisms on the building, G ≤ Aut(B), such that:

- • G preserves the (d + 1)-type function of the building as deﬁned in Lemma 5.9.
- • For any two pairs, (C1,A1) and (C2,A2), of a chamber, Ci, and an apartment containing the chamber, Ai, i = 1,2, there exists g ∈ G, such that g(C1) = C2 and g(A1) = A2.


- Lemma 5.14. Let B be a d-dimensional building and G a group that acts strongly transitively on it. Then B is a regular complex (as deﬁned in §4).


Proof. By Lemma 5.9, there exists a type-function τB : B(0) → [d], i.e. if Vi := τB−1({i}) ⊂ B(0), i = 0,... ,d, then B(0) = di=0 Vi and B(d) ⊂ di=0 Vi. Now, let I ⊂ J ⊂ [d] be two type sets, and let σ,σ′ ∈ B ∩ i∈I Vi be two I-type faces. Choosing two chambers, C and C′, which contains σ and σ′ respectively, and by the second property of the strong transitivity there exists g ∈ G such that g(C) = C′. Also by the ﬁrst property of the strong transitivity, g preserves the types of τB, hence g(σ) = σ′. Since g is an automorphism, the J-type faces containing σ are mapped bijectively to the J-type faces containing σ′, in particular they are of the same cardinality, proving that the building is regular.

![image 159](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile159.png>)

![image 160](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile160.png>)

![image 161](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile161.png>)

![image 162](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile162.png>)

Throughout this section we shall make use of the following notion from group theory.

Deﬁnition 5.15 (Stabilizer). Let X be any simplicial complex and G ≤ Aut(X) a group of automorphisms on X. For any σ ∈ X, deﬁne the stabilizer of σ in G to be the following subgroup of G:

Gσ = stabG(σ) = {g ∈ G | g(σ) = σ}.

- Lemma 5.16. Let B be a building and G a group that acts strongly transitively on it. Then for any face, σ ∈ B, and any apartment containing it, A, every Gσ-orbit in B passes through the apartment A, i.e. for any τ ∈ B there exists g ∈ Gσ such that g(τ) ∈ A.

Proof. Let C ∈ A be a maximal face containing σ, and let C′ ∈ B be a maximal face containing τ. By the second axiom of the building, there exists an apartment A′ which contains both C and C′. By the strong-transitivity, there exists g ∈ G such that g(C) = C and g(A′) = A. On the one hand, g preserves the type function, hence g(σ) = σ, i.e. g ∈ stabG(σ). On the other hand, g(A′) = A, in particular g(τ) ⊂ g(C′) ∈ A, as needed.

![image 163](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile163.png>)

![image 164](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile164.png>)

![image 165](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile165.png>)

![image 166](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile166.png>)

- Lemma 5.17. Let B be a building which posses a strongly transitive action, and let σ ∈ B. Then the link Bσ also posses a strongly transitive action.


Proof. Let G ≤ Aut(B) be the group that acts strongly transitive on B. deﬁne Gσ = stabG(σ) the stabilizer of σ in G, then Gσ admits an action on the link, i.e. Gσ ≤ Aut(Bσ). The action of Gσ is type-preserving since the action of G is. Any pair of a chamber and an apartment containing it inside Bσ, (C,A), can be lifted to a pair of a chamber and an apartment containing it inside B, (C,˜ A˜). Let (C,A) and (C′,A′), be two pairs, where each pair contains a chamber and an apartment containing that chamber, inside Bσ. Lifting them to such pairs in B, (C,˜ A˜) and (C˜′,A˜′), then there is g ∈ G, such that (g(C˜),g(A˜)) = (C˜′,A˜′), and since both pairs contains σ, then g ∈ Gσ, and hence g(C) = C′ and g(A) = A′, which ﬁnishes the proof.

![image 167](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile167.png>)

![image 168](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile168.png>)

![image 169](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile169.png>)

![image 170](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile170.png>)

## 5.2 Expansion of spherical buildings

It was ﬁrst observed by Gromov [Gro] that spherical buildings are coboundary expanders (see [LMM] for a simpliﬁed proof).

- Theorem 5.18. For any d ∈ N, there exist βd > 0, such that any d-dimensional spherical building is a βd-coboundary expander.

The purpose of this subsection is to prove that the spherical buildings of suﬃciently large thickness are good skeleton expanders.

- Theorem 5.19. Let X be a d-dimensional q-thick spherical building which posses a strongly transitively action. Then X is an √θdq-skeleton expander, where θd := max{2d ·(d+1)!,192·11!}.


![image 171](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile171.png>)

![image 172](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile172.png>)

The strategy for proving Theorem 5.19 is as follows: First, we deﬁne a property for bipartite graphs (symmetric-convex), and show that such graphs have good bound on their second largest eigenvalue. Second, we show that the type-induced graphs of a spherical building which posses a strongly transitively action satisfy this property. Finally, by applying Corollary 4.7 we get the skeleton expansion.

Deﬁnition 5.20 (Symmetric convex graph). Let X = (V1 V2,E) be a bipartite graph, let G ≤ Aut(X) be a group that acts by graph automorphisms on X, and let θ ∈ N. For any vertex

- v in X, denote by, Gv = stabG(v) = {g ∈ G|g(v) = v}, its stabilizer. Say that X is a θ-symmetric-convex graph, if for any v ∈ V1, then:


- 1. The number of Gv-orbits in X is at most θ.
- 2. There is a unique Gv-orbit of vertices in V1 of maximal distance from v, and a unique Gv-orbit of vertices in V2 of maximal distance from v.
- 3. For any vertex u, which is not of maximal distance from v, the number of neighbors w of u such that dist(v,w) < dist(v,u), is at most θ.


- Proposition 5.21. Let X be a bipartite (k,k′)-biregular θ-symmetric-convex connected graph, then the normalized second largest eigenvalue of X is bounded by,


1 √

λ(X) ≤ θ · max{

![image 173](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile173.png>)

![image 174](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile174.png>)

k

1 √

k′} (5.1)

,

![image 175](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile175.png>)

![image 176](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile176.png>)

Proof. Let A = AX ∈ End(CV (X)) be the adjacency operator of X, and let Spec(A) = {λn,... ,λ2,λ1} be its set of eigenvalues. Let us recall some basic facts (see [EGL, § 3]): Since X is an undirected graph the operator A is self-adjoint, hence Spec(A) ⊂ R. Since X is bipartite, then λn−i+1 = −λi for any i = 1,... ,n. Finally, since X is (k,k′)-biregular, then λ1 =

√

![image 177](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile177.png>)

k · k′.

Note that any eigenvectors of the eigenvalues, λn,λ1, are non-zero on every vertex, and if f2 ∈ CV(X) is an eigenvector of λ2, there most exist v ∈ V1, such that f2(v) = 0.

Fix such a vertex v ∈ V1, let K = stabG(v) be its stabilizer in G, and deﬁne the following directed-multi-graph X¯ = X/K as follows: The vertices of X¯ are the K-orbits of the vertices of X, i.e. [u] = {k(u)|k ∈ K} for some u ∈ V (X), and the number of edges in X¯ from [u] to [w] is equal to the number of edges in X between the vertex u and the set of vertices {k(w)|k ∈ K} (note that this is independent of the choice of u). Finally, let A¯ ∈ End(CV (X¯)) be the adjacency operator of X¯, and let Spec(A¯) ⊂ C be its set of eigenvalues. By the deﬁnition of X¯ and A¯, we get that for any u ∈ V (X) and any [w] ∈ V (X¯),

A¯[u],[w] =

Au,w. (5.2)

w∈[w]

Note that since X¯ is directed, a priori there is no reason for all the eigenvalues of A¯ to be real, however, if λ is an eigenvalue of A¯, and f ∈ CV(X¯) is an eigenvector of λ, then deﬁning f′ ∈ CV(X) by f′(u) = f([u]), we get that for any u ∈ V (X),

A¯[u],[w]f([w]) = Af¯ ([u]) = λ · f([u]) = λ · f′(u) (5.3)

Af′(u) =

Au,wf′(w) =

[w]∈V (X¯)

w∈V (X)

hence, f′ is an eigenvector of A with eigenvalue λ. In particular, Spec(A¯) ⊂ Spec(A) ⊂ R (5.4)

On the other hand, if λ ∈ Spec(A), with an eigenvector f ∈ CV (X) such that f(v) = 0, then deﬁning f¯∈ CV(X¯) by f¯([u]) = |K1 | k∈K f(k(u)), we get f¯ ≡ 0, such that for any [u] ∈ V (X¯),

![image 178](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile178.png>)

A¯f¯([u]) =

1 |K| k∈K

=

![image 179](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile179.png>)

A¯[u],[w]f¯([w]) =

[w]∈V (X¯)

Au,wf(k(w)) =

![image 180](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile180.png>)

w∈V (X)

1 |K| k∈K

A¯[u],[w]

Af(k(w))

![image 181](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile181.png>)

[w]∈V (X¯)

1 |K| k∈K

1 |K| k∈K

λ · f(k(u)) = λ · f¯([u]) (5.5)

Af(k(u)) =

![image 182](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile182.png>)

hence f¯ is an eigenvector of A¯ with eigenvalue λ. In particular,

λn, λ2, λ1 ∈ Spec(A¯) ⊂ R (5.6) and by applying the trace formula for A¯2, we get

λ2 = tr(A¯2) (5.7)

λ22 + 2 · k · k′ = λ2n + λ22 + λ21 ≤

λ∈Spec(A¯)

Finally, let us use the properties of the symmetric-convex graph: By property 1 the number of vertices in X¯ is at most θ. By property 2 in each of the two parts of X¯, there is a unique vertex, [vi], i = 1,2, of maximal distance from [v], and since X is (k,k′)-biregular, so does X¯, and hence [v1],[v2] has at most k · k′ directed 2-paths starting and ending with them. By property 3 for any other vertex [u] in X¯, [u] = [v1],[v2], the number of directed 2-paths starting and ending with [u] is at most θ · max{k,k′}, since such a 2-path corresponds to a a following 2-path in X, u ∼ w ∼ u′ = k(u) for some vertex w and k ∈ K, so either dist(v,u) < dist(v,w) in which case there are at most θ such possible u′ = k(u) (note dist(v,u) = dist(v,k(u))), or dist(v,u) > dist(v,w) in which case there are at most θ such possible w. All in all we get that

tr(A¯2) =

#{directed 2-paths starting and ending with [u]} ≤ 2·k·k′+(θ−2)·θ·max{k,k′}

[u]∈X¯

(5.8) Combining this with (5.2), we get

λ22 ≤ tr(A¯2) − 2 · k · k′ ≤ θ2 · max{k,k′} (5.9) and noting that λ(X) = λλ2

= √λk2·k′, ﬁnishes the proof.

![image 183](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile183.png>)

![image 184](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile184.png>)

![image 185](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile185.png>)

![image 186](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile186.png>)

![image 187](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile187.png>)

![image 188](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile188.png>)

![image 189](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile189.png>)

1

The following Proposition shows that the type-induced bipartite graphs of the spherical buildings are symmetric-convex, with a constant θ that depends only on the dimension of the building (and not on its thickness!).

Proposition 5.22. Let B be a d-dimensional q-thick spherical building which posses a strongly transitive action. Let i = j ∈ [d] and let B(i,j) be the (i,j)-type induced bipartite biregular graph of B. Then B(i,j) is an θd-symmetric-convex graph with both regularity degrees at least q + 1, where θd := max{2d · (d + 1)!,192 · 11!}.

Proof. Let v be a vertex in the building, Gv = stabG(v), and let A be some ﬁxed apartment that contains v.

First, let us prove the claim on the regularity degrees: By Lemma 5.14, B is a regular

complex, hence B(i,j) is a bipartite biregular graph. Assume v is of i-type, so it most be contained in some panel of j-cotype, σ, (i.e. the σ contain a vertex of each type except j), and

by the q-thickness σ is contained in q +1 chambers, C0,... ,Cq, each of which contains a unique j-type vertex, u0,... ,uq, which is a neighbour of v in the graph B(i,j) (and of course the same reasoning apply when replacing i and j).

- 1) By Lemma 5.16, the number of Gv-orbits is bounded by the size of an apartment in the

building, which, by Lemma 5.5, is bounded by θd.

- 2) Let C be some chamber in A which contains v. By Lemma 5.12 there is a unique chamber


CAop ∈ A of maximal gallery distance from C in A, and let e = {v1,v2} ⊂ Cop be (the unique) edge of type {i,j} inside it. Now, since gallery distance is coarser then graph distance (any

gallery path contains in it a graph path), then v1 and v2 are the two farthest vertices from v (w.r.t. the graph metric of B(i,j)), of type i and j respectively, inside the apartment A. On the other hand, since Gv is a collection of automorphisms, hence preserves distances, and by Lemma 5.12, there is a unique chamber, CAop′, of maximal gallery distance from C, in each apartment A′, we get that for any two apartments A′, A′′, there is some k ∈ Gv such that k(CAop′) = CAop′′. So, [v1] is the unique Gv-orbit in Vi of maximal distance vertices from v, and similarly [v2] is the unique Gv-orbit in Vj of maximal distance vertices from v.

3) Since u is not of maximal distance from v, there is some neighbour w∗ of u such that dist(v,u) < dist(v,w∗). Now by the axiom of the building let A be an apartment that contains both v and the edge (u,w∗). Let w1,... ,wn be all the vertices in B(i,j), which are neighbours of u and satisfy dist(v,wi) < dist(v,u) for any i = 1,... ,n. Then, any minimal path from v to

- w∗ which passes through u, most also pass through some wi. Hence, since gallery distance is coarser then graph distance, any minimal gallery in the building from a maximal face containing {v}, to a maximal face containing {u,w∗}, most also pass through a maximal face containing {u,wi} for some i. Now, if A is an apartment containing v and {u,w∗}, then by Lemma 5.11 all these minimal galleries lies in A, in particular all w1,... ,wn lies in A, i.e. n ≤ |A| ≤ θd (where the last inequality is Lemma 5.5).


![image 190](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile190.png>)

![image 191](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile191.png>)

![image 192](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile192.png>)

![image 193](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile193.png>)

Finally, by combining Propositions 5.21, 5.22 and Corollary 4.7, we are able to prove that spherical buildings are good skeleton expanders (Theorem 5.19).

- Proof of Theorem 5.19. By Proposition 5.22, each type induced bipartite graph, B(i,j), of the building is θd-symmetric-convex. By Proposition 5.21, each B(i,j) has a normalized largest nontrivial eigenvalue at most √θdq. Finally applying Corollary 4.7 we get that the building is an √θdq-skeleton expander.


![image 194](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile194.png>)

![image 195](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile195.png>)

![image 196](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile196.png>)

![image 197](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile197.png>)

![image 198](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile198.png>)

![image 199](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile199.png>)

![image 200](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile200.png>)

![image 201](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile201.png>)

# 6 Ramanujan complexes

Ramanujan complexes were deﬁned in [LSV1], and were explicitly constructed in [LSV2]. They are ﬁnite quotients of Bruhat-Tits buildings of type A˜, which exhibits excellent spectral properties. For more on Ramanujan complexes, we refer the readers for the survey [Lub2].

The object of this section is to show that Ramanujan complexes of suﬃciently large degree satisﬁes the requirement of Theorem 3.1, namely: Theorem 6.1. Let X be a d-dimensional q-thick Ramanujan complex. Then:

- • The complex X is Qd,q-bounded degree, where Qd,q is as in Corollary 5.6.
- • Each proper link of X is a βd-link coboundry expander, where βd is as in Theorem 5.18.
- • Each proper link of X is a √θdq-skeleton expander, where θd is as in Theorem 5.19.


![image 202](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile202.png>)

![image 203](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile203.png>)

- • X itself is a 2d · q−(d−1)/2-skeleton expander. Before proving the Theorem we shall need the following Lemma.


- Lemma 6.2. Any proper link of a Ramanujan complex is a spherical building which posses a strongly transitive action.


Proof of Lemma 6.2. First, since a Ramanujan complex is a quotient of an aﬃne building of type A˜, any link of a Ramanujan complex is a link of the covering aﬃne building. Second, since an A˜-type building posses a strongly transitive action, then by Lemmas 5.10 and 5.17, each link of it is also a building which posses a strongly transitive action. Finally, since an aﬃne building is locally ﬁnite, then each proper link of it is ﬁnite, hence a spherical building.

![image 204](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile204.png>)

![image 205](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile205.png>)

![image 206](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile206.png>)

![image 207](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile207.png>)

- Proof of Theorem 6.1. The ﬁrst three claims follows from Lemma 6.2 together with Corollary 5.6, Theorem 5.18 and Theorem 5.19. We are left to show that X itself is an excellent skeleton expander. Using the notation of [Lub2, Section 2.1], the adjacency operator of the type induced graph X(i,j) is the Hecke operator Aj−i restricted to that graph, hence by [Lub2, Remark 2.1.5],


λ(X) ≤ max

λ(Ai) ≤ max

1≤i≤d

1≤i≤d

d i

−(d−1)

i(d−i) 2

q−

≤ 2dq

2 (6.1)

![image 208](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile208.png>)

![image 209](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile209.png>)

Combining this with Corollary 4.5, proves that X is a (2d · q−(d−1)/2)-skeleton expander.

![image 210](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile210.png>)

![image 211](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile211.png>)

![image 212](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile212.png>)

![image 213](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile213.png>)

Consequentially, combining the above Theorem 6.1, together with Theorems 3.2, 3.1 and 1.8, give us the following high dimensional expansion properties for Ramanujan complexes of suﬃciently large degree (this is Corollary 1.12 from the introduction, together with the coisoperimetric inequality for small cochains).

- Corollary 6.3. For any d,q ∈ N, there exists q0 = q0(d) > 0, µ = µ(d) > 0, ǫ¯ = ǫ¯(d) > 0, ǫ = ǫ(d,q) > 0 and c = c(d,q) > 0, such that if X is the d-dimensional skeleton of a (d + 1)dimensional q-thick Ramanujan complex with q ≥ q0, then:


- • If A is a locally minimal cochain of X and A ≤ µ, then δ(A) ≥ ǫ¯· A .
- • X is an (ǫ,µ)-cosystolic expander.
- • X posses the c-topological overlapping property.


Finally, by [LSV2, Theorem 1.1], we get that for any 2 ≤ d ∈ N and any prime power q, there exist an inﬁnite family of d-dimensional q-thick Ramanujan complexes. Moreover, these Ramanujan complexes are constructed explicitly. Hence, by applying Corollary 6.3 on the Ramanujan complexes constructed in [LSV2], we get an aﬃrmative answer to Gromov’s question from the introduction (Theorem 1.3).

As mentioned in the introduction, as an immediate application of Theorem 1.3, we get:

Corollary 6.4 (Corollary 1.4). For any D ≥ 2d + 1, there exists C = C(D) > 0 and an inﬁnite family of d-dimensional bounded degree complexes, {Xn}n, which satisﬁes the following: For any embedding of Xn into RD, such that the distance between the images of any two non adjacent simplices of Xn is at least 1, then the volume of the 1-neighborhood of the image of Xn, is at least C · |Xn|

1

D−d. Proof of Corollary 6.4. Combine Theorem 1.3 with [GG, Proposition 2.5].

![image 214](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile214.png>)

![image 215](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile215.png>)

![image 216](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile216.png>)

![image 217](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile217.png>)

![image 218](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile218.png>)

The original result [GG, Theorem 2.2] gave the slightly weaker result that, for any ǫ > 0, there exists an inﬁnite family of d-dimensional complexes, {Xn}n, whose degree might depends of ǫ (but not on |Xn|), and the lower bound on the volume of the 1-neighborhood is C·|Xn|

1

D−d−ǫ. The reader is referred to [GG] to learn more on the work of Kolmogorov and Barzdin, and its generalization to higher dimensions.

![image 219](<2015-evra-bounded-degree-cosystolic-expanders_images/imageFile219.png>)

We close this work with the following concluding remarks:

- Remark 6.5. Theorem 6.1 and Corollary 6.3 holds for any ﬁnite quotient of a Bruhat-Tits building of large degree, not just for Ramanujan complexes. To prove this generalization, one needs only to prove that the underlying graph of any ﬁnite quotient of a Bruhat-Tits building of large degree, is a good expander graph. This can be done by using Oh’s explicit property (T) [Oh], to get explicit bounds on the second eigenvalue of such a graph.


- Remark 6.6. Note that for a d-dimensional Ramanujan complexes of suﬃciently large degree, we were only able to prove that their (d − 1)-skeletons are cosystolic expanders. Following [Lub2, Conjecture 3.2.4], we suspect that the Ramanujan complexes themselves (and in fact all ﬁnite quotients of Bruhat-Tits buildings) are cosystolic expanders. In contrast, in [KKL, Proposition 1.5] it was shown that not all Ramanujan complexes of suﬃciently large degree are coboundary expanders, i.e. cosystolic expansion is the best one could hope for in general.


# References

[AB] P. Abramenko, K. S. Brown, Buildings Theory and Applications, Graduate Texts in Mathematics 248, Springer.

[Bar] I. Barany, A generalization of Carathodorys theorem, Discrete Mathematics 40(2): 141-152, (1982).

[BF] E. Boros, Z. Furedi, The number of triangles covering the center of an n-set, Geometriae Dedicata 17(1): 69-77, (1984).

[BK] Y. M. Barzdin, A. N. Kolmogorov, On the realization of nets in 3-dimensional space, Probl. Cybernet, 8: 261-268, (1967). See also Selected Works of A.N. Kolmogorov, Kluwer Academic Publishers, 3: 194-202,245, (1993).

[DK] D. Dotterrer, M. Kahle, Coboundary expanders, Journal of Topology and Analysis, 4(4): 499-514, (2012).

[DKW] D. Dotterrer, T. Kaufman, U. Wagner, On Expansion and Topological Overlap, LIPIcs-Leibniz International Proceedings in Informatics. Vol. 51. Schloss Dagstuhl-Leibniz-Zentrum fuer Informatik, (2016).

[EGL] S. Evra, K. Golubev, A. Lubotzky, Mixing properties and the chromatic number of Ramanujan complexes, International Mathematics Research Notices, 2015(22): 11520-11548, (2015).

[EOT] L. Eldar, M. Ozols, K. F. Thompson, Upper Bounds on Systoles of HighDimensional Expanders Using Quantum Codes, arXiv preprint arXiv:1610.07478,

(2016).

[FGLNP] J. Fox, M. Gromov, V. Laﬀorgue, A. Naor, J. Pach, Overlap properties of geometric expanders, Journal fr die reine und angewandte Mathematik, 671: 49-83,

(2012).

[Gar] H. Garland, p-Adic curvature and the cohomology of discrete subgroups of p-adic groups, Annals of Mathematics, 375-423, (1973).

[Gro] M. Gromov, Singularities, Expanders and Topology of Maps. Part 2: from Combinatorics to Topology Via Algebraic Isoperimetry, Geometric and Functional Analysis, 20(2): 416-526, (2010).

[GG] M. Gromov, L. Guth, Generalizations of the KolmogorovBarzdin embedding estimates, Duke Mathematical Journal, 161(13): 2549-2603, (2012).

[GL] L. Guth, A. Lubotzky, Quantum error correcting codes and 4-dimensional arithmetic hyperbolic manifolds, Journal of Mathematical Physics 55.8: 082202,

(2014).

[GS] A. Gundert, M. Szedlk, Higher dimensional discrete Cheeger inequalities, Proceedings of the thirtieth annual symposium on Computational geometry, ACM,

(2014).

[GW] A. Gundert, U. Wagner, On Laplacians of random complexes, Proceedings of the twenty-eighth annual symposium on Computational geometry, ACM, 151-160,

(2012). [HLW] S. Hoory, N. Linial, A. Wigderson, Expander graphs and their applications, Bulletin of the American Mathematical Society, 43(4): 439-561, (2006).

[KKL] T. Kaufman, D. Kazhdan, A. Lubotzky, Isoperimetric Inequalities for Ramanujan Complexes and Topological Expanders, Geometric and Functional Analysis 26(1): 250-287, (2016).

- [KM1] T. Kaufman, D. Mass, High Dimensional Combinatorial Random Walks and Colorful Expansion, arXiv preprint arXiv:1604.02947, (2016).
- [KM2] T. Kaufman, D. Mass, Walking on the Edge and Cosystolic Expansion, arXiv preprint arXiv:1606.01844, (2016).


[KR] A. Knowles, R. Rosenthal, Eigenvalue conﬁnement and spectral gap for random simplicial complexes, arXiv preprint arXiv:1509.02034, (2015).

- [Lub1] A. Lubotzky, Expander graphs in pure and applied mathematics, Bulletin of the American Mathematical Society, 49(1): 113-162, (2012).
- [Lub2] A. Lubotzky, Ramanujan complexes and high dimensional expanders, Japanese Journal of Mathematics, 9(2): 137-169, (2014).


[LinM] N. Linial, R. Meshulam, Homological connectivity of random 2-complexes, Combinatorica, 26(4): 475-487, (2006).

[LubM] A. Lubotzky, R. Meshulam, Random Latin squares and 2-dimensional expanders, Advances in Mathematics 272 : 743-760, (2015).

[LMM] A. Lubotzky, R. Meshulam, S. Mozes, Expansion of building-like complexes, Groups, Geometry, and Dynamics, 10(1): 155-175, (2016).

[LSV1] A. Lubotzky, B. Samuels, U. Vishne, Ramanujan complexses of type Ad, Israel Journal of Mathematics, 149: 267-300, (2005).

[LSV2] A. Lubotzky, B. Samuels, U. Vishne, Explicit construction of Ramanujan complexes of type Ad, European Journal of Combinatorics, 26(6): 965-993, (2005).

[LLR] A. Lubotzky, Z. Luria, R. Rosenthal, Random Steiner systems and bounded degree coboundary expanders of every dimension, arXiv preprint arXiv:1512.08331,

(2015). [MW] R. Meshulam, N. Wallach, Homological connectivity of random k-dimensional complexes, Random Structures & Algorithms 34(3): 408-417, (2009).

[Oh] H. Oh, Uniform pointwise bounds for matrix coeﬃcients of unitary representations and applications to Kazhdan constants, Duke mathematical journal, 113(1): 133-192, (2002).

[Opp] I. Oppenheim, Isoperimetric Inequalities for Local Spectral Expanders and Topological Expanders, arXiv preprint, arXiv:1501.04940, (2015).

[Par] O. Parzanchevski, Mixing in high-dimensional expanders, arXiv preprint, arXiv:1310.6477, (2013).

[PRT] O. Parzanchevski, R. Rosenthal, R. J. Tessler, Isoperimetric inequalities in simplicial complexes, Combinatorica 1-33, (2012).

[PR] O. Parzanchevski, R. Rosenthal, Simplicial complexes: spectrum, homology and random walks, Random Structures & Algorithms, (2016).

[Pin] M.S. Pinsker, On the complexity of a concentrator, 7th International Teletraﬃc Conference, Stockholm, 4: 1-318, (1973).

[Ros] R. Rosenthal, Simplicial branching random walks and their applications, arXiv preprint, arXiv:1412.5406, (2014).

