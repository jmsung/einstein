arXiv:1612.07048v3[math.OC]4Dec2017

SPECTRAHEDRAL SHADOWS

CLAUS SCHEIDERER

Abstract. We show that there are many (compact) convex semi-algebraic sets in euclidean space that are not spectrahedral shadows. This gives a negative answer to a question by Nemirovski, resp. it shows that the Helton-Nie conjecture is false.

Introduction

Semideﬁnite programming is a far-reaching generalization of linear programming. While a linear program optimizes a linear function over a polyhedron, a semideﬁnite program optimizes it over a convex region described by symmetric linear matrix inequalities. Under mild conditions, semideﬁnite programs can be solved in polynomial time up to any prescribed accuracy. They have numerous applications in applied mathematics, engineering, control theory and so forth (see [1, Chapter 1]).

The feasible regions of semideﬁnite programs are called spectrahedral shadows, or also semideﬁnitely (or SDP) representable sets. These are the sets K ⊆ Rn that can be written

m

n

K = ξ ∈ Rn: ∃η ∈ Rm A +

ηjCj 0 (1)

ξiBi +

j=1

i=1

where m ≥ 0, A, Bi, Cj are real symmetric matrices of the same size and M 0 means that M is positive semideﬁnite. Any representation as in (1) is called a semideﬁnite representation of K.

There has been considerable interest in characterizing spectrahedral shadows by their geometric properties. Essentially, this is the question of what problems in optimization can be modeled as semideﬁnite programs. Nemirovski [19] in his 2006 plenary address at ICM Madrid remarked: “A seemingly interesting question is to characterize SDP-representable sets. Clearly, such a set is convex and semialgebraic. Is the inverse also true? (...) This question seems to be completely open.” Helton and Nie ([11, p. 790]) conjectured that the answer is in fact yes, i.e., that every convex semi-algebraic set in Rn is a spectrahedral shadow.

Although the general question has so far been elusive, many results have been obtained in support of the Helton-Nie conjecture. The class of spectrahedral shadows is known to be closed under taking linear images or preimages, ﬁnite intersections, or convex hulls of ﬁnite unions ([11], [24]). It is also closed under convex duality respectively polarity, and under taking topological closures. Helton and Nie ([11], [12]) gave a series of suﬃcient conditions for semideﬁnite representability of a convex

![image 1](<2016-scheiderer-spectrahedral-shadows_images/imageFile1.png>)

2010 Mathematics Subject Classiﬁcation. Primary 90C22, secondary 14P05. Key words and phrases. Spectrahedral shadows, semideﬁnite representations, semideﬁnite pro-

gramming, Helton-Nie conjecture, moment relaxation, convex algebraic geometry, real algebraic geometry.

1

semi-algebraic set K, in terms of curvature conditions for the boundary. Roughly, their results are saying that when K is compact and its boundary is suﬃciently nonsingular and has strictly positive curvature, then K is a spectrahedral shadow. Netzer [21] proved that the interior of a spectrahedral shadow is again a spectrahedral shadow, and more generally, that removing suitably parametrized families of faces from a spectrahedral shadow results again in a spectrahedral shadow. By applying the criteria of Helton-Nie, Netzer and Sanyal [23] showed that smooth hyperbolicity cones are spectrahedral shadows. Scheiderer [36] showed that closed convex hulls of one-dimensional semi-algebraic sets are always spectrahedral shadows, and that the Helton-Nie conjecture is true for subsets of the plane.

In addition there are plenty of further results on semideﬁnite representations for particular kinds of sets. See, for example, [6], [7], [9], [14], [22], [25], [26], [29], [30], [35], and see [20], [3], [19], [4, ch. 6] or [1, ch. 2, 4 and 5] for surveys on semideﬁnite representation.

An important general technique for constructing semideﬁnite representations was introduced by Lasserre [17], and independently by Parrilo [27]. It is based on a dual relaxation principle and is generally known as the moment relaxation method. Starting with a (basic closed) semi-algebraic set S ⊆ Rn, it produces outer approximations of the convex hull of S that have explicit semideﬁnite representations. When S is compact, these approximations can be made arbitrarily close. Under favorable conditions, moment relaxation is known to become exact, meaning that a suitable such approximation coincides with the convex hull of S, up to taking closures.

In this paper we exhibit, for the ﬁrst time, non-trivial conditions that are necessary for semideﬁnite representability. They are based on semideﬁnite duality, and they imply that there are no more closed spectrahedral shadows than those obtainable from exact moment relaxation in a generalized sense. We then use arguments from algebraic geometry, in particular properties of smooth morphisms of varieties, to show that these conditions are indeed non-trivial, and to produce concrete examples of convex sets that fail to be spectrahedral shadows. Among them are natural prominent sets like the cone of non-negative forms of ﬁxed degree in R[x1,...,xn], in every case where this cone is diﬀerent from the sums of squares cone (Corollary 4.25). In fact, for every semi-algebraic set S ⊆ Rn of dimension at least two we prove that there exist polynomial maps ϕ: Rn → Rm for which the closed convex hull of ϕ(S) in Rm has no semideﬁnite representation. This is in marked contrast to the case where S has dimension one, when it is known that the closed convex hull of S is always a spectrahedral shadow [36].

For optimization, our results imply that there exist natural semi-algebraic optimization problems that cannot be modeled exactly as semideﬁnite programs. For example, the problem of minimizing a general polynomial of degree d ≥ 4 in n ≥ 3 variables (or of degree d ≥ 6 in n = 2 variables) over the unit ball in Rn is of this sort.

The paper is organized as follows. In Section 2 we recall and generalize the moment relaxation construction, arriving at general suﬃcient conditions for semideﬁnite representability. In Section 3 we show that the conditions obtained in Section 2 are also necessary. The main result is Theorem 3.4. In Section 4 we

present concrete constructions of closed convex sets that violate the necessary conditions from Section 3, and we give a few explicit examples. Finally, Section 5 contains a number of open questions.

Acknowledgement. The elegant construction for the proof of Proposition 3.2 was suggested by Christoph Hanselka. I am most grateful to him for his kind permission to include his argument here. I am also indebted to Tim Netzer for comments on a ﬁrst preliminary version.

1. Preliminaries and notation

- 1.1. A symmetric matrix A ∈ Symd(R) is said to be positive semideﬁnite (psd), denoted A 0, if all its eigenvalues are non-negative. If in addition all eigenvalues are nonzero then A is positive deﬁnite, written A ≻ 0. The canonical inner product

on Symd(R) is denoted A,B = tr(AB), for A, B ∈ Symd(R). The set Sym+d(R) = {A ∈ Symd(R): A 0} is a closed convex cone in Symd(R), self-dual with respect to the inner product. The same terminology applies when the ﬁeld R of real numbers is replaced by a real closed ﬁeld R.

- 1.2. A set K ⊆ Rn is called a spectrahedron if there exist d ≥ 1 and M0,...,Mn ∈

Symd(R) such that K = {ξ ∈ Rn: M0 + ni=1 ξiMi 0}. The set K is said to be a spectrahedral shadow (or to have a semideﬁnite representation) if there exists

a spectrahedron S ⊆ Rm for some m and a linear map f : Rm → Rn such that

- K = f(S). Spectrahedra have also been called LMI-sets or LMI-representable sets. In the


plane, spectrahedra are characterized by the former Lax conjecture, which has been proved by Helton-Vinnikov [13] in 2007. In higher dimension there exist only conjectural characterizations of spectrahedra (so-called generalized Lax conjecture).

Spectrahedral shadows have as well occured under various diﬀerent names, such as projected spectrahedra, SDP representable sets or lifted-LMI representable sets. These sets are convex and semi-algebraic, but so far no other restrictions were known.

- 1.3. For V a vector space over a ﬁeld k we denote the dual space of V by V

∨

= Homk(V,k). Let V be a ﬁnite-dimensional R-vector space. By a (convex) cone C in V we mean a non-empty set C ⊆ V with C + C ⊆ C and aC ⊆ C for all real numbers a ≥ 0. Given any set M ⊆ V let conv(M) denote the convex hull of M, and let cone(M) be the convex cone generated by M (consisting of all ﬁnite linear combinations of elements of M with non-negative coeﬃcients). Moreover, M∗ ⊆ V

∨

= HomR(V,R) denotes the (closed convex) cone dual to M, i.e. M∗ = {λ ∈ V

∨

: ∀x ∈ M λ(x) ≥ 0}. When M is a semi-algebraic set then so are conv(M) and cone(M), by Carath´eodory’s lemma, and also M∗.

- 1.4. Given a ﬁeld k, a k-algebra is a commutative ring A with a ﬁxed ring homomorphism k → A. The k-algebra A is said to be ﬁnitely generated if it is ﬁnitely generated as a ring over k. The ideal in a ring A generated by a family of elements


ai ∈ A (i ∈ I) is denoted ai: i ∈ I .

We use standard terminology for algebraic varieties, that we brieﬂy recall. Generally, we use the language of schemes. See 1.5 below for informal rephrasings of the most important concepts in non-technical language. Note however that it would be most cumbersome and awkward to formulate parts of Section 4 in such language, which is why we will not make such an attempt.

Our ﬁelds k will be real closed ﬁelds, and in particular they have characteristic zero. All our k-varieties will be aﬃne, and we assume them to be reduced but not necessarily irreducible. Thus, an aﬃne k-variety V is the spectrum of a reduced ﬁnitely generated k-algebra A, and A = k[V ] = Γ(V,OV ) is the aﬃne coordinate ring of V . As usual, V (k) = Homk(A,k) is the set of k-rational points of V . Given ξ ∈ V (k), the local ring of V at ξ is denoted OV,ξ. By mV,ξ we invariantly denote both the maximal ideal of OV,ξ and its preimage in k[V ]. Given a morphism φ: V → W of aﬃne k-varieties, the associated homomorphism k[W] → k[V ] of kalgebras is denoted φ∗. Given a ﬁeld extension K/k we write VK := V ×k Spec(K) for the base ﬁeld extension of V , and similarly φK : VK → WK for the base ﬁeld extension of φ. Upon identifying K[V ] = k[V ] ⊗k K we have φ∗K = φ∗ ⊗ 1 for the induced map K[Y ] → K[X].

- 1.5. To make the paper more accessible to readers who are not familiar with the basic notions of algebraic geometry, here are some explanations. Let k be either be the ﬁeld R of real numbers or a real closed extension thereof, and let k be an algebraic closure of k. Informally speaking, an aﬃne k-variety can be thought of as a subset V ⊆ kn (for some n) that can be described by polynomial equations with coeﬃcients in k, and that is equipped with the k-Zariski topology (the closed subsets of which are the aﬃne k-varieties contained in V ). Given a second aﬃne k-variety

![image 2](<2016-scheiderer-spectrahedral-shadows_images/imageFile2.png>)

![image 3](<2016-scheiderer-spectrahedral-shadows_images/imageFile3.png>)

- W ⊆ km, a morphism φ: V → W of k-varieties corresponds to a map V → W given component-wise by k-polynomials. Associated with V is its aﬃne coordinate ring


![image 4](<2016-scheiderer-spectrahedral-shadows_images/imageFile4.png>)

k[V ] = k[x1,...,xn]/IV , where IV is the ideal of polynomials vanishing identically on V . Associated with φ is the (“pull-back”) ring homomorphism φ∗: k[W] → k[V ] induced by φ in the obvious way. The set of k-rational points of V is V (k) := kn∩V . Given ξ ∈ V (k), let mV,ξ = {f ∈ k[V ]: f(ξ) = 0}, a maximal ideal of k[V ]. The local ring of V at ξ is by deﬁnition the localization OV,ξ = k[V ]m

V,ξ

of k[V ] at its maximal ideal mV,ξ. Given a ﬁeld extension K/k, the base ﬁeld extension VK of V is the aﬃne K-variety in Kn deﬁned by the same k-polynomials as V , and it has coordinate ring K[V ] = k[V ] ⊗k K.

![image 5](<2016-scheiderer-spectrahedral-shadows_images/imageFile5.png>)

For example, aﬃne n-space is the aﬃne k-variety An = kn and has k[An] = k[x1,...,xn] = k[x] and An(k) = kn. Given ξ ∈ kn, the local ring OAn,ξ is the ring of fractions fg with f, g ∈ k[x] and g(ξ) = 0.

![image 6](<2016-scheiderer-spectrahedral-shadows_images/imageFile6.png>)

![image 7](<2016-scheiderer-spectrahedral-shadows_images/imageFile7.png>)

- 1.6. When V is an aﬃne variety over k = R, we will always equip the set V (R) of R-rational points with the euclidean topology (induced by V (R) ⊆ Rn if V ⊆ An is a closed subvariety). This topology is independent of the choice of a closed embedding V ⊆ An. A subset S ⊆ V (R) is called semi-algebraic if it can be written as a ﬁnite boolean combination of sets of the form {ξ ∈ V (R): f(ξ) > 0} with f ∈ R[V ].
- 1.7. Let V be an aﬃne k-variety, and let L ⊆ k[V ] be a k-linear subspace of


ﬁnite dimension. Let S•L = d≥0 SdL be the symmetric k-algebra over L, and let S•L → k[V ] be the natural k-homomorphism induced by the inclusion L ⊆ k[V ].

The associated morphism of aﬃne k-varieties will be denoted ϕL : V → AL, where AL := Spec(S•L) is the aﬃne space with coordinate ring S•L. In plainer terms, upon ﬁxing a linear basis g1,...,gm of L, we may identify ϕL with the map V → Am given by ξ  → (g1(ξ),...,gm(ξ)). Note that AL(k) = L

= Homk(L,k), the linear space dual to L, so that on k-rational points the map ϕL : V (k) → L

∨

sends ξ ∈ V (k) to the evaluation map L → k at ξ.

∨

2. Sufficient conditions for semidefinite representability

Let V be an aﬃne R-variety. Given a semi-algebraic subset S ⊆ V (R) we write P(S) = {f ∈ R[V ]: f ≥ 0 on S}.

- 2.1. We start by informally recalling the moment relaxation construction, due to Lasserre [17] and independently Parrilo [27]. Let L ⊆ R[V ] be a linear subspace


with dim(L) = m < ∞, and let ϕL: V → AL ∼= Am be the associated morphism, see 1.7. Assume that S ⊆ V (R) is a basic closed semi-algebraic set, say S = {ξ ∈ V (R): hi(ξ) ≥ 0 (i = 1,...,r)} where h1,...,hr ∈ R[V ]. We are trying to ﬁnd a semideﬁnite representation of the convex hull K of ϕL(S) in AL(R) = L

∨ ∼= Rm, or at least an approximate such representation.

Without any serious restriction we can assume 1 ∈/ L. Fix a sequence W0,...,Wr of ﬁnite-dimensional linear subspaces of R[V ]. Any f ∈ L1 := R1 + L ⊆ R[V ] that has a representation f = s0 + ri=1 sihi with si a sum of squares of elements of Wi (i = 0,...,r) is obviously non-negative on S. So the set of all such f is a convex cone C = C(W0,...,Wr), contained in L1 ∩ P(S). By construction, the dual cone C∗ ⊆ L

let λ′ ∈ L

1 has an explicit semideﬁnite representation. For λ ∈ L

∨

∨

∨

1 be deﬁned by λ′|L = λ and by λ′(1) = 1. The set K′ = K′(W0,...,Wr) of all λ ∈ AL(R) = L

for which λ′ ∈ C∗ is a closed spectrahedral shadow that contains K. Enlarging the spaces Wi, or adding more inequalities hi to the description of S, results in K′ getting smaller, and therefore becoming a closer approximation to K. Of particular interest is the case where C = L1 ∩ P(S). This condition is usually rephrased by saying that the linear polynomials non-negative on ϕL(S) (i.e. the elements of L1 ∩ P(S)) have weighted sum of squares representations of uniformly bounded degrees (the “degree bounds” being given by the subspaces Wi). The moment relaxation is exact in this case, which means that K′ = K, the closure of K. Therefore, under the assumption C = L1 ∩ P(S), the closure K is a spectrahedral shadow.

∨

![image 8](<2016-scheiderer-spectrahedral-shadows_images/imageFile8.png>)

![image 9](<2016-scheiderer-spectrahedral-shadows_images/imageFile9.png>)

We now generalize this procedure, to arrive at a general suﬃcient condition for semideﬁnite representability. First two auxiliary lemmas.

- Lemma 2.2. Let V be an aﬃne R-variety, and let S ⊆ V (R) be a semi-algebraic set. Let L ⊆ R[V ] be a ﬁnite-dimensional linear subspace with 1 ∈/ L, and write

L1 := R1 + L.

- (a) ϕL(S) is a semi-algebraic subset of L

∨

.

- (b) The closed convex hull conv(ϕL(S)) of ϕL(S) in L

![image 10](<2016-scheiderer-spectrahedral-shadows_images/imageFile10.png>)

∨

consists of all λ ∈ L

∨

that satisfy λ′(g) ≥ 0 for every g ∈ L1 ∩ P(S).

- (c) The closed conic hull cone(ϕL(S)) of ϕL(S) in L


![image 11](<2016-scheiderer-spectrahedral-shadows_images/imageFile11.png>)

∨

consists of all λ ∈ L

∨

that satisfy λ(g) ≥ 0 for every g ∈ L ∩ P(S). Proof. In (b), λ′ ∈ L

∨

1 denotes the extension of λ ∈ L

∨

deﬁned by λ′(1) = 1, see

- 2.1. (a) follows from the Tarski-Seidenberg theorem, and (b), (c) are consequences of convex duality.


- Lemma 2.3. Let A be an R-algebra, let U ⊆ A be a linear subspace with dim(U) < ∞, and let UU be the linear subspace of A spanned by all products uu′ (u, u′ ∈ U). Then the cone ΣU2, consisting of all ﬁnite sums of squares of elements of U, is a spectrahedral shadow in UU.


Proof. Choose a linear basis u1,...,un of U. The linear map f : Symn(R) → UU, (aij)  → i,j aijuiuj satisﬁes ΣU2 = f(Sym+n(R)), which shows the claim.

We keep ﬁxing an aﬃne R-variety V , a semi-algebraic set S ⊆ V (R) and a ﬁnite-dimensional linear subspace L ⊆ R[V ]. As before write L1 = L + R1.

- Proposition 2.4. Let φi: Xi → V (i = 1,...,m) be ﬁnitely many morphisms of aﬃne R-varieties. For every i = 1,...,m let Ui ⊆ R[Xi] be a ﬁnite-dimensional linear subspace, and assume that the following two conditions hold:


- (1) S ⊆ φi(Xi(R)) for i = 1,...,m;
- (2) for every f ∈ L1 ∩P(S) there exists i ∈ {1,...,m} such that φ∗i (f) ∈ R[Xi] is a sum of squares of elements of Ui (in R[Xi]).


![image 12](<2016-scheiderer-spectrahedral-shadows_images/imageFile12.png>)

Then conv(ϕL(S)), the closed convex hull of ϕL(S) in AL(R) = L

, is a spectrahe-

∨

dral shadow. Proof. Write C := L1 ∩ P(S), which is a closed convex cone in L1. For a given

- index i ∈ {1,...,m} let Ci ⊆ L1 be the cone of all f ∈ L1 for which φ∗i (f) is a sum of squares of elements of Ui in R[Xi]. By Lemma 2.3, and since linear preimages of spectrahedral shadows are again spectrahedral shadows, Ci is a spectrahedral shadow in L1. By condition (1), elements of Ci are non-negative on S, which means Ci ⊆ C. Therefore C = mi=1 Ci by (2), and hence we have C∗ = mi=1 Ci∗


for the dual cones. For every index i the cone Ci∗, being the dual cone to a spectrahedral shadow cone, is itself a spectrahedral shadow. So it follows that C∗ is a spectrahedral shadow in L

1. For the convex hull K := conv(ϕL(S)) ⊆ L

∨

: λ′ ∈ C∗}, see Lemma 2.2(b). So K is the preimage of the spectrahedral shadow C∗ under the aﬃne-linear map L

![image 13](<2016-scheiderer-spectrahedral-shadows_images/imageFile13.png>)

we have K = {λ ∈ L

∨

∨

![image 14](<2016-scheiderer-spectrahedral-shadows_images/imageFile14.png>)

1, λ  → λ′, and hence is a spectrahedral cone, as asserted.

# → L

∨

∨

- Corollary 2.5. If, in Proposition 2.4, condition (2) is only required to hold for


![image 15](<2016-scheiderer-spectrahedral-shadows_images/imageFile15.png>)

every f ∈ L ∩ P(S), then cone(ϕL(S)), the closed convex cone generated by ϕL(S), is a spectrahedral shadow.

Proof. The proof is completely analogous to the proof of 2.4, deﬁning the respective cones C and Ci to be subcones of L instead of L1, and applying Lemma 2.2(c).

The following examples and remarks illustrate Proposition 2.4. Remarks 2.6.

1. Proposition 2.4 can be seen as a generalization of the moment relaxation construction. To explain this, assume that we are in the situation of 2.1, in particular

- S = {ξ ∈ V (R): hi(ξ) ≥ 0 (i = 1,...,r)} with hi ∈ R[V ]. Let X be the aﬃne R-variety obtained by formally adjoining square roots of h1,...,hr to R[V ], i.e.


R[X] = R[V ][t1,...,tr]/ t2i − hi, i = 1,...,r , and let φ: X → V be the natural map. Then clearly φ(X(R)) = S. If subspaces Wi ⊆ R[V ] as in 2.1 have been found such that the suﬃcient exactness condition from 2.1 is satisﬁed, i.e. if L1 ∩ P(S) = C(W0,...,Wr) (in the notation of 2.1), this implies that for every f ∈ L1 ∩ P(S) the pull-back φ∗(f) ∈ R[X] is a sum of squares in R[X] of elements from the subspace U := φ∗(W0)+ ri=1 φ∗(Wi)√hi of R[X]. So under this assumption, the conditions of Proposition 2.4 are fulﬁlled with m = 1 and these particular choices of φ and U.

![image 16](<2016-scheiderer-spectrahedral-shadows_images/imageFile16.png>)

- 2. Conversely, the more general construction of a semideﬁnite representation in

- Proposition 2.4 is achieved essentially by reduction to a construction of moment relaxation type, as in 2.1. We leave it to the reader to make this statement precise.

3. The proof of Proposition 2.4 is constructive in the following sense. If the morphisms φi: Xi → V as well as the linear subspaces Ui ⊆ R[Xi] are given explicitly, we can deduce from this data an explicit semideﬁnite representation of conv(ϕL(S)).

![image 17](<2016-scheiderer-spectrahedral-shadows_images/imageFile17.png>)

Example 2.7. Let C be a nonsingular aﬃne curve over R for which C(R) is compact. Let L ⊆ R[C] be a ﬁnite-dimensional linear subspace, and consider the associated map ϕL : C(R) → AL(R) = L

∨

. By [36, Corollary 4.4] there exists a ﬁnite-dimensional linear subspace U ⊆ R[C] such that every f ∈ L + R1 that is non-negative on C(R) is a sum of squares of elements from U. Using this fact,

- Proposition 2.4 applies with m = 1 and φ: X → C the identity map of C, showing

that the convex hull of ϕL(C(R)) in L

∨

is a spectrahedral shadow. (This consequence was already drawn in [36].)

- Remark 2.8. Later (Remark 3.7 below) we’ll see that it is not enough in Proposition 2.4 to replace condition (2) by the weaker condition that every f ∈ L1 ∩ P(S) becomes a sum of squares in one of the R[Xi]. Rather, it is essential that such sum of squares representations exist in a uniform way.


3. Necessary conditions for semidefinite representability

In the previous section we stated suﬃcient conditions for semideﬁnite representability. We now show that these conditions are also necessary. In the sequel let x = (x1,...,xn) be a tuple of variables. We start by recalling one form of duality in semideﬁnite programming (see [28]):

- Proposition 3.1. Let M1,...,Mn ∈ Symd(R), write M(ξ) = ni=1 ξiMi for ξ ∈ Rn, and let C = {ξ ∈ Rn: M(ξ) 0} be the associated spectrahedral cone. Assume that M(ξ0) ≻ 0 for some ξ0 ∈ Rn. Then the dual cone of C has the following semideﬁnite representation:


C∗ = B,M1 ,..., B,Mn : B ∈ Symd(R), B 0 ⊆ Rn.

- Proposition 3.2. Assume that S ⊆ Rn is a semi-algebraic set for which the closed conical hull cone(S) ⊆ Rn of S is a spectrahedral shadow. Then there exists a morphism φ: X → An of aﬃne R-varieties, together with a ﬁnite-dimensional Rlinear subspace U of R[X], such that S ⊆ φ(X(R)) and the following holds: For every homogeneous linear polynomial f ∈ R[x] with f ≥ 0 on S, the pull-back φ∗(f) ∈ R[X] is a sum of squares of elements from U.




![image 18](<2016-scheiderer-spectrahedral-shadows_images/imageFile18.png>)

Our original proof for Proposition 3.2 (see version 1 of arXiv:1612.07048) was non-constructive and used a compactness argument for the real spectrum. The following explicit construction is much more elegant and transparent. It was suggested by Christoph Hanselka, who kindly agreed that his argument may be included here. Independently, the original approach may still have its merits, as we plan to demonstrate in follow-up work.

Proof. Let C = cone(S), the convex cone generated by S in Rn. We may assume that Rn is aﬃnely spanned by S. By assumption, C is the linear image of a

![image 19](<2016-scheiderer-spectrahedral-shadows_images/imageFile19.png>)

spectrahedron T ⊆ RN under a linear map π: RN → Rn, for some N. We may assume that T is a cone, and we may replace RN by the linear hull of T. Then

- T can be represented by a homogeneous linear matrix inequality that is strictly feasible. So we can assume that there are integers d ≥ 1 and m ≥ 0, together with


linear matrix pencils M(x) = ni=1 xiMi, N(y) = mj=1 yjNj in Symd(R), such that

T = (ξ,η) ∈ Rn × Rm: M(ξ) + N(η) 0},

such that C = π(T) where π(ξ,η) = ξ, and such that there exists (ξ,η) ∈ Rn × Rm with M(ξ) + N(η) ≻ 0.

![image 20](<2016-scheiderer-spectrahedral-shadows_images/imageFile20.png>)

Consider the closed subvariety X of An × Am × Symd deﬁned over R whose C-points are the triples (ξ,η,A), where A is a symmetric d × d-matrix satisfying

n

m

A2 =

ξiMi +

ηjNj.

i=1

j=1

We shall denote the coordinate functions on X by x1,...,xn; y1,...,ym; (zµν)1≤µ,ν≤d = (x,y,Z)

with zµν = zνµ for 1 ≤ µ, ν ≤ d. Let φ: X → Am be the projection φ(ξ,η,A) = ξ. Then φ(X(R)) = π(T) = C, since a real symmetric matrix is psd if and only if it is the square of some real symmetric matrix. Let U ⊆ R[X] be the linear subspace spanned by the coeﬃcient functions zµν = zνµ (1 ≤ µ,ν ≤ d) of Z. We claim that the assertion of 3.2 holds with these choices of φ and U.

![image 21](<2016-scheiderer-spectrahedral-shadows_images/imageFile21.png>)

To see this, let f = ni=1 aixi be a linear homogeneous polynomial in R[x] = R[x1,...,xn] with f ≥ 0 on S (and hence f ≥ 0 on C). So the tuple (a,0) = (a1,...,an; 0,...,0) ∈ Rn × Rm lies in the dual cone T∗ of T. Since the linear matrix inequality is strictly feasible, there exists B ∈ Symd(R) with B 0 such that ai = B,Mi (1 ≤ i ≤ n) and 0 = B,Nj (1 ≤ j ≤ m), by Proposition 3.1. Let V ∈ Symd(R) with B = V 2. Then, as an element of R[X], φ∗(f) is equal to

![image 22](<2016-scheiderer-spectrahedral-shadows_images/imageFile22.png>)

n

n

B,Nj yj = B, M(x) + N(y) = V 2,Z2 = ZV ,ZV .

B,Mi xi +

j=1

i=1

This means that

d

(ZV )µν 2 is a sum of squares in R[X] from the linear subspace U ⊆ R[X]. Combining Propositions 2.5 and 3.2, we therefore get:

φ∗(f) =

µ, ν=1

- Theorem 3.3. Let S ⊆ Rn be a semi-algebraic set, and let C = cone(S) be the convex cone in Rn generated by S. The closure C is a spectrahedral shadow if and only if there exists a morphism φ: X → An of aﬃne R-varieties, together with an R-linear subspace U ⊆ R[X] of ﬁnite dimension, such that


![image 23](<2016-scheiderer-spectrahedral-shadows_images/imageFile23.png>)

- (1) S ⊆ φ(X(R)),
- (2) for every homogeneous linear polynomial f ∈ R[x1,...,xn] with f ≥ 0 on S, the pull-back φ∗(f) ∈ R[X] is a sum of squares of elements from U.


![image 24](<2016-scheiderer-spectrahedral-shadows_images/imageFile24.png>)

Proof. The second condition is necessary for C to be a spectrahedral shadow by

- Proposition 3.2, and it is suﬃcient by 2.5.


Instead of working with convex cones we may also dehomogenize and derive a non-homogeneous version from Theorem 3.3. Alternatively, we could as well have worked in an inhomogeneous setting from the beginning:

- Theorem 3.4. Let S ⊆ Rn be a semi-algebraic set, and let K = conv(S) be its convex hull in Rn. The closure K is a spectrahedral shadow if and only if there exists a morphism φ: X → An of aﬃne R-varieties and an R-linear subspace U ⊆ R[X] of ﬁnite dimension such that


![image 25](<2016-scheiderer-spectrahedral-shadows_images/imageFile25.png>)

- (1) S ⊆ φ(X(R)),
- (2) for every (inhomogeneous) linear polynomial f ∈ R[x] with f ≥ 0 on S, the element φ∗(f) of R[X] is a sum of squares of elements from U.


![image 26](<2016-scheiderer-spectrahedral-shadows_images/imageFile26.png>)

Proof. If there exist φ and U satisfying (1) and (2), K has a semideﬁnite representation by Proposition 2.4. Conversely, assume that K has a semideﬁnite representation, and let K1 = {1} × K ⊆ R × Rn = Rn+1. Since K1 is a spectrahedral shadow, it is easy to see that cone(K1) is a spectrahedral shadow in Rn+1. Hence the closure of cone(K1) is a spectrahedral shadow as well. Clearly, this last cone coincides with C1, where C1 is the convex cone in Rn+1 generated by S1 = {1}×S. Now we can apply the “only if” part of Theorem 3.3 to S1 and C1 and deduce the converse in Theorem 3.4.

![image 27](<2016-scheiderer-spectrahedral-shadows_images/imageFile27.png>)

![image 28](<2016-scheiderer-spectrahedral-shadows_images/imageFile28.png>)

![image 29](<2016-scheiderer-spectrahedral-shadows_images/imageFile29.png>)

![image 30](<2016-scheiderer-spectrahedral-shadows_images/imageFile30.png>)

![image 31](<2016-scheiderer-spectrahedral-shadows_images/imageFile31.png>)

- Remark 3.5. In 3.4 we may sharpen conditions (1) and (2) further. Assume we are given a morphism φ: X → An and a linear subspace U ⊆ R[X] as in 3.4. From


(1) we deduce that there exists a semi-algebraic set M ⊆ X(R) with φ(M) = S and with dim(M) = dim(S) (use a semi-algebraic section S → X(R) of φ over S). Let

- X′ be the Zariski closure of M in X, and let U′ ⊆ R[X′] be the image of U under R[X] → R[X′]. Then (1) and (2) hold as well for the restriction φ′: X′ → An of φ and for U′. Therefore, we can achieve in addition that dim(X) = dim(S). On the other hand, condition (1) can be replaced by either K = φ(X(R)) (to make it seemingly stronger), or by K ⊆ conv(φ(X(R))) (to make it seemingly weaker). Note that the inclusion φ(X(R)) ⊆ K holds for any φ satisfying (2). Indeed, given


![image 32](<2016-scheiderer-spectrahedral-shadows_images/imageFile32.png>)

![image 33](<2016-scheiderer-spectrahedral-shadows_images/imageFile33.png>)

![image 34](<2016-scheiderer-spectrahedral-shadows_images/imageFile34.png>)

any ξ ∈ Rn, ξ ∈/ K, there exists f ∈ R[x] linear with f|S ≥ 0 and f(ξ) < 0, so (2) implies ξ ∈/ φ(X(R)).

![image 35](<2016-scheiderer-spectrahedral-shadows_images/imageFile35.png>)

- 3.6. In the next section we need to work not only over the ﬁeld R of real numbers, but also over real closed extension ﬁelds R ⊇ R. Given an aﬃne R-variety V and a semi-algebraic set M ⊆ V (R), the base ﬁeld extension of M to R is denoted MR (see [5, Section 5.1]). If M is described by a ﬁnite boolean combination of inequalities fi > 0 (with fi ∈ R[V ]), the set MR ⊆ V (R) is described by the same system of inequalities.


- Remark 3.7. Let φ: X → V be a morphism of aﬃne R-varieties, let L ⊆ R[V ] and U ⊆ R[X] be ﬁnite-dimensional linear subspaces, and let S ⊆ V (R) be a semi-algebraic set. Assume that the following condition holds:


(∗) For every f ∈ L with f ≥ 0 on S, the pull-back φ∗(f) ∈ R[X] is a sum of squares of elements of U.

Then the extension of (∗) to any real closed ﬁeld extension R of R holds as well. More precisely, any f ∈ LR = L ⊗ R ⊆ R[V ] with f ≥ 0 on SR ⊆ V (R) becomes a sum of squares of elements of UR = U ⊗ R in R[X], by the Tarski principle.

In particular, any f ∈ L ⊗ R with f ≥ 0 on SR becomes a sum of squares in R[X]. We remark that this last conclusion would fail in general if in (∗) we had

only required that φ∗(f) is a sum of squares in R[X]. For instance, taking φ to be the identity of X = V = A2 and S the unit disk would give counter-examples: Every f ∈ R[x1,x2] with f ≥ 0 on S can be written f = p + (1 − x21 − x22)q with sums of squares p, q ∈ R[x1,x2], but the analogous statement fails over any proper real closed extension R of R (see [33] and [34]). Rather, one needs that uniform sums of squares expressions exist as in (∗), to guarantee that the condition is stable under real closed ﬁeld extension.

The following version is essentially identical with the “only if” part of Theorem

- 3.4, but will be more convenient in the next section. Let V be an aﬃne R-variety,


and let L ⊆ R[V ] be a ﬁnite-dimensional linear subspace. Let ϕL : V → AL ∼= An (n = dim(L)) be the associated morphism, see 1.7.

- Corollary 3.8. With V and L as above, let S ⊆ V (R) be a semi-algebraic set. Assume that conv(ϕL(S)), the closed convex hull in AL(R) = L

![image 36](<2016-scheiderer-spectrahedral-shadows_images/imageFile36.png>)

∨

, is a spectrahedral shadow. Then there exists a morphism φ: X → V of aﬃne R-varieties, together with a ﬁnite-dimensional linear subspace U ⊆ R[X], such that S ⊆ φ(X(R)) and the following holds:

For every real closed ﬁeld R ⊇ R and every f ∈ LR + R1 ⊆ R[V ] with f ≥ 0 on SR, the pull-back φ∗R(f) under φR: XR → VR is a sum of squares of elements from U ⊗ R in R[X] ⊗ R = R[X].

(The converse is true as well, covered by Proposition 2.4.)

Proof. By 3.4 there exists a morphism ψ: Y → AL of aﬃne R-varieties, together with a ﬁnite-dimensional subspace W ⊆ R[Y ], such that, for every f ∈ R1+L with f ≥ 0 on S, the pull-back ψ∗(f) ∈ R[Y ] is a sum of squares of elements from W. Let X be the ﬁbered product of V and Y over AL, let φ: X → V be the canonical morphism, and let U ⊆ R[X] be the pull-back of W under X → Y . Then the condition in 3.8 is satisﬁed for R = R. By Tarski-Seidenberg, the condition holds over any real closed extension R as well (see also Remark 3.7).

It may not be obvious immediately, but the necessary condition for semideﬁnite representability found in Theorems 3.3 resp. 3.4 is quite restrictive. In the next section we’ll elaborate on this in more detail.

4. Constructing examples

We use properties of smooth morphisms of algebraic varieties, together with a weak version of generic smoothness, to construct examples of convex sets that have no semideﬁnite representation.

- 4.1. Let k be a ﬁeld. Recall that a morphism φ: X → Y of algebraic k-varieties is smooth at x ∈ X if there exist aﬃne open sets U = Spec(A) ⊆ X and V = Spec(B) ⊆ Y with x ∈ U and φ(U) ⊆ V such that A is (via φ) B-isomorphic to B[x1,...,xn]/(f1,...,fm), where m ≤ n and det(∂fi/∂xj)1≤i,j≤m is a unit in OX,x. It is equivalent that φ is ﬂat at x and that the ﬁbre φ−1(φ(x)) is geometrically regular at x over the residue ﬁeld of φ(x), see [8, 17.5.1]. The smooth locus of φ, i.e. the set of points x ∈ X at which φ is smooth, is Zariski open in X.


We will use the following weak version of generic smoothness (compare [10, Lemma III.10.5]):

- Proposition 4.2. Let φ: X → Y be a dominant morphism between irreducible k-varieties where char(k) = 0. Then there exists a non-empty Zariski open subset


- U ⊆ X such that φ|U : U → Y is smooth. The following result is contained in [8, 17.5.3] as a particular case:

- Proposition 4.3. Let φ: X → Y be a morphism of algebraic k-varieties. Let ξ ∈ X(k), and write A = OX,ξ, B = OY,φ(ξ). Then φ is smooth at ξ if and only if


- A is isomorphic over B to a power series algebra B[[t1,...,tm]].


(Here, of course, hat denotes completion of a local ring.) From 4.3 we deduce the following observation:

Lemma 4.4. Let φ: X → Y be a morphism of algebraic k-varieties, and assume that φ is smooth at ξ ∈ X(k). If f ∈ OY,φ(ξ) is such that φ∗(f) is a sum of squares in OX,ξ, then f is a sum of squares in OY,φ(ξ).

Proof. Indeed, if an element of a ring B becomes a sum of squares in B[[t1,...,tm]], it was already a sum of squares in B.

4.5. We shall present two constructions. Each will give us concrete examples of convex semi-algebraic sets without semideﬁnite representation. For both, the reasoning will be based on the following technical lemma. We will repeatedly assume that data is given as follows:

(∗) V is an aﬃne R-variety, L ⊆ R[V ] is a ﬁnite-dimensional linear subspace, ϕL: V → AL ∼= Am (m = dim(L)) is the associated morphism (see 1.7), and S ⊆ V (R) is a semi-algebraic set. Moreover, V ′ is an irreducible component of V and S′ ⊆ S ∩ V ′(R) is a semi-algebraic set, Zariski-dense in V ′.

(Note that some of the technicalities in (∗) and in 4.6 arise since we want to cover sets S as well whose Zariski closure has several irreducible components. Otherwise we could have assumed V ′ = V and S′ = S.)

- Lemma 4.6. Assume that (∗) as in 4.5 is given. If conv(ϕL(S)) is a spectrahedral shadow in AL(R), there exists a morphism ψ: W → V ′ of aﬃne R-varieties, together with ξ ∈ W(R), such that the following hold:


![image 37](<2016-scheiderer-spectrahedral-shadows_images/imageFile37.png>)

- (1) W(R) is Zariski dense in W,
- (2) ψ(ξ) ∈ S′,
- (3) ψ is smooth at ξ,
- (4) for every real closed ﬁeld R ⊇ R and every f ∈ LR +R1 ⊆ R[V ] with f ≥ 0 on SR, the pull-back ψR∗ (f) ∈ R[W] is a sum of squares in R[W].


In (4) we have written LR = L ⊗ R, which is a ﬁnite-dimensional R-linear subspace of R[V ] ⊗ R = R[V ].

Proof. By Corollary 3.8, there exists a morphism φ: X → V of aﬃne R-varieties with S ⊆ φ(X(R)) such that, for every real closed R ⊇ R and every f ∈ LR +R1 ⊆ R[V ] with f ≥ 0 on SR, the pull-back φ∗R(f) is a sum of squares in R[X]. Using the argument of Remark 3.5, we can ﬁnd a closed irreducible subvariety X′ of X satisfying φ(X′) ⊆ V ′ and dim(X′) = V ′, for which S′∩φ(X′(R)) is Zariski dense in

- V ′. The restriction φ′: X′ → V ′ of φ is a dominant morphism between irreducible R-varieties of the same dimension. By Proposition 4.2, there is a non-empty open


aﬃne subset W of X′ such that the restriction φ′|W : W → V ′ of φ′ is smooth. Writing Z = X′ W we have dim(Z) < dim(V ′), so the set φ′(Z(R)) is not Zariski

dense in V ′. Therefore S′ ∩ φ′(W(R)) is still Zariski dense in V ′. In particular, we can ﬁnd ξ ∈ W(R) such that η := φ′(ξ) lies in S′. Then it is clear that (1)–(4) are satisﬁed for ψ := φ′|W : W → V ′ and ξ.

The ﬁrst construction is very easy and works for convex hulls of suitable sets of dimension ≥ 3. First recall:

- Lemma 4.7. Let A be a regular local R-algebra, let p1,...,pd be a regular system of parameters of A. If f(x1,...,xd) is a form in d variables over R that is not a sum of squares of forms, then f(p1,...,pd) ∈ A is not a sum of squares in A.


The proof uses the associated graded ring of A, see [31], proof of Proposition 6.1.

- Proposition 4.8. Assume that (∗) as in 4.5 is given. If for every η ∈ S′ there exists f ∈ L + R1 ⊆ R[V ] with f|S ≥ 0 such that f is not a sum of squares in


OV,η, then the closed convex hull conv(ϕL(S)) in AL(R) ∼= Rdim(L) fails to be a spectrahedral shadow.

![image 38](<2016-scheiderer-spectrahedral-shadows_images/imageFile38.png>)

Proof. Assume that the closed convex hull is a spectrahedral shadow. Then there exists a morphism ψ: W → V ′ together with a point ξ ∈ W(R) as in Lemma 4.6. Let η = ψ(ξ) ∈ S′, and choose f ∈ L + R1 for the given η as in the hypothesis. On the one hand, ψ∗(f) ∈ R[W] should be a sum of squares in R[W], by property (4) of ψ in 4.6. On the other hand, since ψ is smooth at ξ, this contradicts Lemma 4.4, by the choice of f.

- Example 4.9. Let x = (x1,x2,x3) and put L = {f ∈ R[x]: deg(f) ≤ 6, f(0) = 0}, a linear subspace of R[x] with dim(L) = 83. For every ξ ∈ R3 there exists f ∈ L+R1

with f ≥ 0 on R3 such that f is not a sum of squares in OA3,ξ (the ring of formal power series in x1−ξ1, x2−ξ2, x3−ξ3). Indeed, this follows from 4.7, e.g. by taking f = p(x1−ξ1,x2−ξ2,x3−ξ3) where p is any ternary sextic form that is psd but not a sum of squares (for instance the Motzkin form). Let ϕ = ϕL: A3 → AL ∼= A83 be the Veronese type embedding associated with L. For any semi-algebraic set S ⊆ R3 with non-empty interior, it follows from Proposition 4.8 that the closed convex hull of ϕ(S) in R83 has no semideﬁnite representation.

- Example 4.10. Similarly, let x = (x1,x2,x3,x4) and L = {f ∈ R[x]: deg(f) ≤ 4, f(0) = 0}. Then dim(L) = 69. Using psd, non-sos quartic forms in four variables


and proceeding similarly as in 4.9, we ﬁnd that the closed convex hull of ϕL(S) in R69 is not a spectrahedral shadow, for any semi-algebraic set S ⊆ R4 with nonempty interior.

- Remark 4.11. The reasoning used in the preceding examples was still very coarse. With a ﬁner look we arrive at constructions that are considerably more parsimonious. For example, if in 4.9 we work with the Motzkin form p, we can ﬁnd a linear subspace L ⊆ R[x] of dimension dim(L) = 27 such that p(x−ξ) ∈ R1+L for every ξ ∈ R3, resulting in an embedding R3 → R27 with the property of 4.9. Similarly, if


in 4.10 we work with the Choi-Lam form p(x) = x21x22+x22x23+x23x21+x44−4x1x2x3x4, we can ﬁnd a linear subspace of dimension 19 with the desired property.

- Remark 4.12. The construction of convex sets without semideﬁnite representation via Proposition 4.8 did not employ the full strength of the “only if” part of


- Theorem 3.4. Indeed, it wasn’t used anywhere that pull-backs of non-negative linear polynomials are uniformly sums of squares in R[X] (see Remark 3.7). In turn,


the argumentation in 4.9– 4.11 applies only to convex hulls of sets of dimension at least three. We now reﬁne the construction. This will provide us with convex hulls of two-dimensional sets without a semideﬁnite representation.

- 4.13. Let R be a real closed ﬁeld containing R. In the sequel, we always denote by


- B the convex hull of R in R, so B = {a ∈ R: ∃n ∈ N −n < a < n}. Note that B is a valuation ring (called the canonical valuation ring of R), with ﬁeld of fractions R, maximal ideal mB = {a ∈ R: ∀n ∈ N |na| < 1} and residue ﬁeld B/mB = R. The reduction map B → B/mB = R will be denoted a  → a. Nonzero elements in mB will be called inﬁnitesimals of R.


![image 39](<2016-scheiderer-spectrahedral-shadows_images/imageFile39.png>)

An example is given by the ﬁeld R = q≥1 R((t1/q)) of Puiseux series with real coeﬃcients (see [2, Section 2.6]). The sign of 0 = f = m≥m

cmtm/q ∈ R with cm ∈ R and cm

0

, and the valuation (or order) of f is o(f) = m

= 0 is the sign of cm

0

0

q . The valuation ring B resp. its maximal ideal mB consists of all f ∈ R with o(f) ≥ 0 resp. o(f) > 0.

0

![image 40](<2016-scheiderer-spectrahedral-shadows_images/imageFile40.png>)

Let V be an aﬃne R-variety. We write B[V ] := R[V ]⊗B (tensor product over R).

If φ: X → V is a morphism of aﬃne R-varieties, then φ∗R (resp. φ∗B) denotes the induced homomorphism R[V ] → R[X] (resp. B[V ] → B[X]). Given ξ ∈ V (R), let

MV,ξ ⊆ B[V ] be the kernel of the evaluation map B[V ] → B, f  → f(ξ). We start with several auxiliary results. The following lemma is straightforward:

- Lemma 4.14. Let V be an aﬃne R-variety, let ξ ∈ V (R), and let R, B as in 4.13. Then for every N ≥ 1 the natural map

OV,ξ/(mV,ξ)N ⊗ B → B[V ]/(MV,ξ)N of B-algebras is an isomorphism.

- Lemma 4.15. Let R, B be as in 4.13, and let X be an aﬃne R-variety for which

X(R) is Zariski dense in X. If g1,...,gr ∈ R[X] are such that ri=1 gi2 lies in B[X], then gi ∈ B[X] for every i.

Proof. We can assume gi = 0 for every i. Let f := ri=1 gi2. There is 0 = c ∈ R such that cgi ∈ B[X] for every i and cgj = 0 in (B/mB)[X] = R[X] for at least one

![image 41](<2016-scheiderer-spectrahedral-shadows_images/imageFile41.png>)

index j. It follows that c2f ∈ B[X], and moreover c2f = i(cgi)2 is nonzero in (B/mB)[X] = R[X], since X(R) is Zariski dense in X. Hence c ∈/ mB, which means

![image 42](<2016-scheiderer-spectrahedral-shadows_images/imageFile42.png>)

![image 43](<2016-scheiderer-spectrahedral-shadows_images/imageFile43.png>)

that 1c ∈ B, and so indeed gi ∈ B[X] for every index i.

![image 44](<2016-scheiderer-spectrahedral-shadows_images/imageFile44.png>)

- Lemma 4.16. Let R, B be as in 4.13, and let φ: X → V be a morphism of aﬃne R-varieties. Assume that X(R) is Zariski dense in X, and that φ is smooth at ξ ∈ X(R). If f ∈ B[V ] and N ≥ 1 are such that f is not a sum of squares in B[V ] modulo (MV,φ(ξ))N, then φ∗R(f) ∈ R[X] is not a sum of squares in R[X].


Proof. Write η = φ(ξ). By Proposition 4.3, the smoothness assumption implies that the completed local ring OX,ξ is OV,η-isomorphic to a power series ring over OV,η. In particular, this implies that φ∗: OV,η/(mV,η)N → OX,ξ/(mX,ξ)N has a retraction, i.e. there is a homomorphism ρ: OX,ξ/(mX,ξ)N → OV,η/(mV,η)N for which the composition ρ ◦ φ∗ is the identity on OV,η/(mV,η)N. Tensoring with B

and using Lemma 4.14 gives the commutative diagram B[V ] φ

∗

B B[X]

![image 45](<2016-scheiderer-spectrahedral-shadows_images/imageFile45.png>)

![image 46](<2016-scheiderer-spectrahedral-shadows_images/imageFile46.png>)

![image 47](<2016-scheiderer-spectrahedral-shadows_images/imageFile47.png>)

B[V ]/(MV,η)N B[X]/(MX,ξ)N whose bottom map has a retraction. From the hypothesis it therefore follows that φ∗B(f) ∈ B[X] cannot be a sum of squares in B[X]. By Lemma 4.15, φ∗R(f) is not a sum of squares in R[X] either.

![image 48](<2016-scheiderer-spectrahedral-shadows_images/imageFile48.png>)

- Lemma 4.17. Let R, B be as in 4.13, let V be an aﬃne R-variety, and let ξ ∈ V (R)


be a nonsingular R-point. If u1,...,ud ∈ R[V ] form a regular parameter sequence of V at ξ, there is an isomorphism

B[V ]/(MV,ξ)N ∼= B[x1,...,xd]/ x1,...,xd N

of B-algebras which makes the cosets of ui and xi correspond to each other, for i = 1,...,d.

Proof. Clear from the isomorphism R[[x1,...,xd]] → OV,ξ sending xi to ui, and from Lemma 4.14.

The next result is a key observation. For R = R a proper real closed ﬁeld extension of R, it implies that there exist polynomials f ∈ B[x1,x2] with f ≥ 0 on R2 such that f is not a sum of squares in B[x1,x2]/ x1,x2 N, for N suﬃciently large. Note that any such f is a sum of squares in R[[x1,x2]], and hence in R[x1,x2]/ x1,x2 N for all N [32].

- Proposition 4.18. Let f ∈ R[x0,x] = R[x0,...,xn] be homogeneous of degree d, and assume that f is not a sum of squares in R[x0,x]. Let R, B be as in 4.13. If ǫ > 0 is an inﬁnitesimal in R, the polynomial f(ǫ,x) ∈ B[x] is not a sum of squares in B[x] x1,...,xn d+1B[x].

Proof. Assume we have an identity f(ǫ,x) + g(x) = j pj(x)2 where g(x) ∈ x d+1B[x] and pj(x) ∈ B[x]. Replacing x by ǫx yields

ǫdf(1,x) + g(ǫx) =

j

pj(ǫx)2. (∗)

The left hand side is divisible by ǫd in B[x]. By Lemma 4.15, the polynomial qj(x) := ǫ−d/2pj(ǫx) ∈ R[x] lies in B[x] for every j. Putting g′(x) = ǫ−(d+1)g(ǫx) we have g′(x) ∈ B[x], therefore dividing (∗) by ǫd gives

f(1,x) + ǫg′(x) =

j

qj(x)2,

an identity in B[x]. Reducing coeﬃcient-wise modulo mB implies that f(1,x) is a sum of squares in R[x], contradicting the hypothesis.

- Proposition 4.19. Assume that (∗) as in 4.5 is given, and assume that R ⊇ R,


- R = R is a real closed ﬁeld with canonical valuation ring B (4.13). For every η ∈ S′ assume that there exists f ∈ LB + B1 ⊆ B[V ] with f ≥ 0 on SR such that f is not a sum of squares in B[V ]/(MV,η)N for some N ≥ 1. Then the closed convex hull conv(ϕL(S)) in AL(R) ∼= Rdim(L) is not a spectrahedral shadow.


![image 49](<2016-scheiderer-spectrahedral-shadows_images/imageFile49.png>)

(Here LB := L ⊗ B ⊆ R[V ] ⊗ B = B[V ].)

Proof. Assume that the closed convex hull is a spectrahedral shadow. Then there exists ψ: W → V ′ together with ξ ∈ W(R), as in Lemma 4.6. Let η = ψ(ξ) ∈ S′, and choose f ∈ LB+B1 for the given η as in 4.19. On the one hand, ψR∗ (f) ∈ R[W] should be a sum of squares in R[W], by property (4) of ψ in 4.6. On the other hand, ψR∗ (f) is not a sum of squares in R[W] by Lemma 4.16. This contradiction proves Proposition 4.19.

Example 4.20. Let x = (x1,x2), and put L = {f ∈ R[x]: deg(f) ≤ 6, f(0) = 0}, a linear subspace of R[x] of dimension 27. Consider the associated embedding φL: A2 → AL ∼= A27. If S ⊆ R2 is any semi-algebraic set with non-empty interior, the closed convex hull of ϕL(S) in R27 is not a spectrahedral shadow. Indeed, choose a sextic form p ∈ R[x0,x1,x2] that is psd but not a sum of squares, and let 0 = ǫ be an inﬁnitesimal of R. Given ξ ∈ S, the polynomial f := p(ǫ,x1 − ξ1,x2 − ξ2) ∈ B[x1,x2] lies in LB +B1, and f is not a sum of squares in B[x]/(MA2,ξ)7 by Proposition 4.18 and Lemma 4.17. It follows from Proposition 4.19 that conv(ϕL(S)) has no semideﬁnite representation.

![image 50](<2016-scheiderer-spectrahedral-shadows_images/imageFile50.png>)

Remark 4.21. Similar to Remark 4.11, we can arrive at examples of smaller dimension when we take a ﬁner look. For instance, consider the Motzkin form p = x61 + x40x22 + x20x42 − 3x20x21x22 in R[x0,x1,x2]. This form is psd but not a sum of squares. Let L ⊆ R[x,y] be the linear space spanned by the 14 monomials xi (1 ≤ i ≤ 6), yi (1 ≤ i ≤ 4) and xiyj (i,j = 1,2). For any semi-algebraic set

- S ⊆ R2 with non-empty interior, the closed convex hull of ϕL(S) in R14 fails to be a spectrahedral shadow. Indeed, for any choice of ǫ, ξ1, ξ2 ∈ B, the polynomial f := p(ǫ, x1 − ξ1, x2 − ξ2) ∈ B[x1,x2] lies in LB + B1. So we can argue as in 4.20.


A reasoning as in Examples 4.20 or 4.21 can also be applied to aﬃne R-varieties V diﬀerent from An, thanks to the following lemma:

Lemma 4.22. Let R, B be as in 4.13, and assume R = R. Let V be an aﬃne Rvariety, let Vreg ⊆ V be its smooth locus, let η ∈ Vreg(R), and let q1,...,qn ∈ B[V ] be a regular parameter sequence for OV

R,η. Moreover let f ∈ R[x0,...,xn] be a form that is psd but not a sum of squares. If ǫ = 0 is any inﬁnitesimal in R, then f(ǫ,q1,...,qn) ∈ B[V ] is psd on V (R), but is not a sum of squares in B[V ]/(MV,η)N for N ≥ deg(f) + 1.

Proof. Put p := f(ǫ,q1,...,qn). It is clear that p ≥ 0 on V (R). Let x = (x1,...,xn). We have an isomorphism B[x]/ x N →∼ B[V ]/(MV,η)N for every N ≥ 1, that sends xi to qi for i = 1,...,n (Lemma 4.17). It maps the residue class of f(ǫ,x) to the residue class of p. By Proposition 4.18, this element (in either ring) is not a sum of squares when N > deg(f).

Summing up, we can conclude:

- Theorem 4.23. Let S ⊆ Rm be any semi-algebraic set with dim(S) ≥ 2. Then, for some k ≥ 1, there exists a polynomial map ϕ: S → Rk such that the closed convex hull of ϕ(S) in Rk has no semideﬁnite representation.


Proof. Let V ⊆ Am be the Zariski closure of S. Fix a point ξ ∈ S ∩ Vreg(R) such that dimξ(S) ≥ 2 and S contains an open neighborhood of ξ in V (R). Let p1,...,pn ∈ R[V ] (n ≥ 2) be a regular sequence of parameters for OV,ξ. Let

x = (x1,...,xn), y = (y1,...,yn) be tuples of variables, let f ∈ R[t,x] be a form in n + 1 variables that is psd but not a sum of squares, and put d = deg(f). We can write

d

gi(x)hd−i(t,y)

f(t,x + y) =

i=0

where gi ∈ R[x] and hi ∈ R[t,y] are forms of degree i (i = 0,...,d). There is a Zariski open neighborhood U ⊆ Vreg of ξ such that, for any η ∈ U(R), the sequence pi − pi(η) (i = 1,...,n) is a regular sequence of parameters for OV,η. Let L ⊆ R[V ] be a ﬁnite-dimensional linear subspace that contains gi(p1,...,pn) for i = 1,...,d, and choose a real closed ﬁeld R that properly contains R. For any a = (a0,...,an) ∈ Bn+1, the element

d

gi(p1,...,pn)hd−i(a0,...,an)

qa := f(a0,p1 + a1,...,pn + an) =

i=0

lies in LB + B1 ⊆ B[V ] and satisﬁes qa ≥ 0 on V (R). Let η ∈ U(R), and put a = (ǫ, −p1(η), ..., −pn(η)) ∈ Bn+1 where ǫ = 0 is inﬁnitesimal in R. Then qa ∈ B[V ] is non-negative on V (R), and qa is not a sum of squares in B[V ]/(MV,η)d+1 by Lemma 4.22. By Proposition 4.19, this shows that conv(ϕ(S)) is not a spectrahedral shadow.

![image 51](<2016-scheiderer-spectrahedral-shadows_images/imageFile51.png>)

The previous examples already indicate that convex hulls of Veronese sets typically fail to be spectrahedral shadows. Speciﬁcally, we have:

- Corollary 4.24. Let n, d be positive integers with n ≥ 3 and d ≥ 4, or with n = 2 and d ≥ 6. Let m1,...,mN be the non-constant monomials of degree ≤ d

in (x1,...,xn) (so N = n+nd − 1). Then for any semi-algebraic set S ⊆ Rn with non-empty interior, the closed convex hull of

v(S) := m1(ξ),...,mN(ξ) : ξ ∈ S in RN fails to be a spectrahedral shadow. Proof. Hilbert [15] showed that there exists a psd form f of degree d in n + 1 variables. So it suﬃces to apply Propositions 4.18 and 4.19.

For positive integers n, d let Σn,2d (resp. Pn,2d) denote the cone of all degree 2d forms in R[x1,...,xn] that are sums of squares of forms (resp. that are positive semideﬁnite).

- Corollary 4.25. The psd cone Pn,2d is a spectrahedral shadow only in the cases where Pn,2d = Σn,2d, i.e. only for 2d = 2 or n ≤ 2 or (n,2d) = (3,4).


Proof. It is well-known and easy to see that the dual Σ∗n,2d of the sos cone is a spectrahedral cone. Therefore Σn,2d, being closed, is a spectrahedral shadow. Let n, d be such that Σn,2d = Pn,2d. By Hilbert’s theorem [15] quoted before, this happens precisely when 2d = 2 or n ≤ 2 or (n,2d) = (3,4). The dual cone Pn,∗ 2d can be identiﬁed with the convex (or conical) hull of the image of the degree 2d Veronese map

vn,2d: Rn → RN, ξ  → ξα |α|=2d where N = n+2n−d1−1 is the number of monomials of degree 2d in (x1,...,xn). By

- 4.24, a suitable aﬃne hyperplane section of this cone fails to be a spectrahedral


shadow. So Pn,∗ 2d itself cannot be a spectrahedral shadow, and therefore neither can be Pn,2d.

5. Some open questions

There are many obvious questions that remain open at this point. Here are some that we consider as being particularly natural.

- 5.1. What is the smallest dimension of a convex semi-algebraic set without semidefinite representation? The smallest dimension that we realize in this paper is 14 (see


- 4.21). A more technical construction gives examples of dimension 11. We expect that the true answer should be much less. Is it three? Recall that the Helton-Nie conjecture has been proved for subsets of R2 [36].
- 5.2. Consider the necessary and suﬃcient condition 3.3 (or 3.4) for semideﬁnite representability. Although we use it to construct counter-examples to the HeltonNie conjecture, it seems that in concrete cases, the condition is often hard to decide.


For a prominent example let Cn ⊆ Symn(R) be the copositive cone, consisting of all symmetric matrices A such that xtAx ≥ 0 for all x ∈ (R+)n (see [16] for a recent survey). For n ≥ 5 it is not known whether Cn is a spectrahedral shadow ([4, p. 135]). We were unable to apply criterion 3.3 to decide this question.

Therefore we ask: What are alternative characterizations of spectrahedral shadows that are easier to work with?

- 5.3. The results of Helton and Nie [11], [12] guarantee the existence of a semideﬁnite representation in a wide range of cases. Speciﬁcally, if a compact convex semi-algebraic set K ⊆ Rn fails to have a semideﬁnite representation, their results imply that the boundary of K must have a singular point, or must have zero curvature somewhere ([11], conclusions, p. 790).


The counter-examples to the Helton-Nie conjecture constructed in this paper are typically (closed) convex hulls of low-dimensional sets in high-dimensional euclidean space. In particular, their boundaries have singularities. It seems to be an open question whether there exist counter-examples with smooth boundary.

- 5.4. The generalized Lax conjecture (see [37] for an overview) asserts that the


hyperbolicity cone in Rn of any hyperbolic form f(x1,...,xn) is a spectrahedral cone. For n = 3 this is in fact a theorem, proved by Helton-Vinnikov [13] in 2007 in a signiﬁcantly stronger form. For n ≥ 4 however, it is not even known in general whether every hyperbolicity cone is a spectrahedral shadow, although this holds when the cone is smooth (Netzer-Sanyal [23]). Can one decide whether hyperbolicity cones are spectrahedral shadows using results of this paper?

References

- [1] M. Anjos, J. B. Lasserre (eds): Handbook on Semideﬁnite, Conic and Polynomial Optimization. Springer, New York, 2012.
- [2] S. Basu, R. Pollack, M.-F. Roy: Algorithms in Real Algebraic Geometry. 2nd ed, Algorithms and Computation in Mathematics 10, Springer, Berlin, 2006.
- [3] A. Ben-Tal, A. Nemirovski: Lectures on Modern Convex Optimization. SIAM, Philadelphia, 2001.
- [4] G. Blekherman, P. Parrilo, R. Thomas (eds): Semideﬁnite Optimization and Convex Algebraic Geometry. MOS-SIAM Series on Optimization 13, SIAM, Philadelphia PA, 2013.
- [5] J. Bochnak, M. Coste, M.-F. Roy: Real Algebraic Geometry. Erg. Math. Grenzgeb. (3) 36, Springer, Berlin, 1998.


- [6] J. Gouveia, T. Netzer: Positive polynomials and projections of spectrahedra. SIAM J. Optim. 21, 960–976 (2012).
- [7] J. Gouveia, P. Parrilo, R. Thomas: Theta bodies for polynomial ideals. SIAM J. Optim. 20, 2097–2118 (2010).
- [8] A. Grothendieck: Elements de Ge´ome´trie Alge´brique, Tome 4 (Quatri`eme Partie). Publ. Math. IHES 32, 5–361 (1967).
- [9] F. Guo, C. Wang, L. Zhi: Semideﬁnite representations of non-compact convex sets. SIAM J. Optim. 25, 377–395 (2015).
- [10] R. Hartshorne: Algebraic Geometry. Grad. Texts Math. 52, Springer, New York, 1977.
- [11] W. Helton, J. Nie: Suﬃcient and necessary conditions for semideﬁnite representability of convex hulls and sets. SIAM J. Optim. 20, 759–791 (2009).
- [12] W. Helton, J. Nie: Semideﬁnite representation of convex sets. Math. Program. 122 (Ser. A), 21–64 (2010).
- [13] W. Helton, V. Vinnikov: Linear matrix inequality representations of sets. Comm. Pure Appl. Math. 60, 654–674 (2007).
- [14] D. Henrion: Semideﬁnite representation of convex hulls of rational varieties. Acta Appl. Math. 115, 319–327 (2011).
- [15] D. Hilbert: Uber¨ die Darstellung deﬁniter Formen als Summe von Formenquadraten. Math. Ann. 32, 342–350 (1888).
- [16] J.-B. Hiriart-Urruty, A. Seeger: A variational approach to copositive matrices. SIAM Review 52, 593–629 (2010).
- [17] J. B. Lasserre: Convex sets with semideﬁnite representation. Math. Program. 120 (Ser. A), 457–477 (2009).
- [18] J. B. Lasserre: Moments, Positive Polynomials and Their Applications. Imperial College Press, London, 2010.
- [19] A. Nemirovski: Advances in convex optimization: Conic programming. Int. Cong. Math. vol. I, European Math. Soc., Zu¨rich, 2007, pp. 413-444.
- [20] Yu. Nesterov, A. Nemirovskii: Interior-Point Polynomial Algorithms in Convex Programming. SIAM Studies in Applied Mathematics 13, Philadelphia, 1994.
- [21] T. Netzer: On semideﬁnite representations of non-closed sets. Linear Algebra Appl. 432, 3072–3078 (2010).
- [22] T. Netzer, D. Plaumann, M. Schweighofer: Exposed faces of semideﬁnitely representable sets. SIAM J. Optim. 20, 1944–1955 (2010).
- [23] T. Netzer, R. Sanyal: Smooth hyperbolicity cones are spectrahedral shadows. Math. Program. 153 (Ser. B), 213–221 (2015).
- [24] T. Netzer, R. Sinn: A note on the convex hull of ﬁnitely many projections of spectrahedra. Preprint, arxiv:0908.3386.
- [25] J. Nie: First order conditions for semideﬁnite representations of convex sets deﬁned by rational or singular polynomials. Math. Program. 131 (Ser. A), 1–36 (2012).
- [26] J. Nie, P. Parrilo, B. Sturmfels: Semideﬁnite representation of the k-ellipse. In: Algorithms in Algebraic Geometry, A. Dickenstein, F-O. Schreyer, A. Sommese (eds.), Springer, New York, 2008, pp. 117–132.
- [27] P. Parrilo: Structured semideﬁnite programs and semialgebraic geometry methods in robustness and optimization. Ph. D. Thesis, CalTech, 2000.
- [28] M. V. Ramana: An exact duality theory for semideﬁnite programming and its complexity implications. Math. Prog. 77, 129–162 (1997).
- [29] J. Saunderson, P. A. Parrilo: Polynomial-sized semideﬁnite representations of derivative relaxations of spectrahedral cones. Math. Program., Ser. A 153, 309–331 (2015).
- [30] J. Saunderson, P. A. Parrilo, A. S. Willsky: Semideﬁnite descriptions of the convex hull of rotation matrices. SIAM J. Optim. 25, 1314–1343 (2015).
- [31] C. Scheiderer: Sums of squares of regular functions on real algebraic varieties. Trans. Am. Math. Soc. 352, 1039–1069 (1999).
- [32] C. Scheiderer: On sums of squares in local rings. J. reine angew. Math. 540,205–227 (2001).
- [33] C. Scheiderer: Sums of squares on real algebraic surfaces. Manuscr. math. 119, 395–410

(2006).

- [34] C. Scheiderer: Non-existence of degree bounds for weighted sums of squares representations. J. Complexity 21, 823–844 (2005).
- [35] C. Scheiderer: Convex hulls of curves of genus one. Adv. Math. 228, 2606–2622 (2011).


- [36] C. Scheiderer: Semideﬁnite representation for convex hulls of real algebraic curves. Preprint, 2012, arxiv:1208.3865, SIAM J. Applied Algebra and Geometry (to appear).
- [37] V. Vinnikov: LMI representations of convex semialgebraic sets and determinantal representations of algebraic hypersurfaces: Past, present, and future. In: Mathematical Methods in Systems, Optimization, and Control, H. Dym, M. C. de Oliveira, M. Putinar (eds.), Springer Basel, pp. 325-349 (2012).
- [38] H. Wolkowicz, R. Saigal, L. Vandenberghe (eds.): Handbook of Semideﬁnite Programming. Theory, Algorithms, and Applications. Kluwer, Boston, 2000.


Fachbereich Mathematik und Statistik, Universitat¨ Konstanz, 78457 Konstanz, Germany

E-mail address: claus.scheiderer@uni-konstanz.de

