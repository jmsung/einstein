---
type: source
kind: paper
title: Geometric vs Algebraic Nullity for Hyperpaths
authors: Joshua Cooper, Grant Fickes
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2107.01500v4
source_local: ../raw/2021-cooper-geometric-algebraic-nullity-hyperpaths.pdf
topic: general-knowledge
cites:
---

arXiv:2107.01500v4[math.CO]4Mar2022

# Geometric vs Algebraic Nullity for Hyperpaths

Joshua Cooper Grant Fickes March 8, 2022

Abstract

We consider the question of how the eigenvarieties of a hypergraph relate to the algebraic multiplicities of their corresponding eigenvalues. Speciﬁcally, we (1) fully describe the irreducible components of the zero-eigenvariety of a loose 3-hyperpath (its “nullvariety”), (2) use recent results of Bao-Fan-Wang-Zhu to compute the corresponding algebraic multiplicity of zero (its “nullity”), and then (3) for this special class of hypergraphs, verify a conjecture of Hu-Ye about the relationship between the geometric (multi-)dimension of the nullvariety and the nullity.

## 1 Introduction

We begin with two questions:

- 1. What is the combinatorial meaning of the multiplicity of the zero eigenvalue of a (hyper)graph?
- 2. What is the relationship between the various notions of “multiplicity” for an eigenvalue?


One may combine these two questions by asking, “What is the combinatorial meaning of each notion of the multiplicity of the zero eigenvalue of (hyper)graphs?” For the Laplacian matrix L(G) = D(G)−A(G) of a graph, in the 1970s, Fiedler showed that the multiplicity – in both the algebraic and geometric senses – of the zero eigenvalue is equal to the number of components of G. Thus it is natural to ask this same question about the seemingly simpler adjacency matrix A(G), and indeed considerable attention has been given to Question 1 (e.g., [4, 6, 7, 11, 13]). Because A(G) is real symmetric and therefore diagonalizable, the answer to Question 2 is simple for a graph, however: they agree.

In contrast, these questions are nearly untouched for hypergraphs. The ﬁrst question has been investigated for some special graphs – for example, [1] implicitly provides an algorithm for computing the algebraic multiplicity of zero as an eigenvalue of a hyperpath. In a related vein, [2] analyzes which eigenvectors corresponding to the zero eigenvalue of a subgraph of

- G are also such “null eigenvectors” for G. The second question is also almost entirely unexplored for hypergraphs, and Sturmfels observed (see [8]) that the relatively straightforward


linear eigenspaces of matrices become complicated “eigenvarieties” when one passes to adjacency tensors/hypermatrices to study hypergraphs. Hu and Ye [8] take up this matter in earnest and pose a conjecture about the relationship between the (multi-)dimension of such varieties and their multiplicities as roots of a hypermatrix’s characteristic polynomial; these are natural choices for analogizing “geometric” and “algebraic” multiplicity, respectively, and the conjecture is an attempt to generalize the fact that the geometric multiplicity of a matrix eigenvalue is bounded above by its algebraic multiplicity. Another notable contribution [5] by Fan-Bao-Huang investigated properties of the eigenvariety associated with the spectral radius of a hypergraph (and, more generally, certain hypermatrices/tensors).

The aforementioned Hu-Ye Conjecture can be stated as follows; deﬁnitions follow below. Let am(λ) be the algebraic multiplicity of λ as an eigenvalue of the hypermatrix M. Let Vλ1, . . ., Vλκ denote the irreducible components of Vλ, the eigenvariety correponding to λ. Conjecture 1.1 ([8]). For any order-k hypermatrix M, deﬁne

gm(λ) :=

κ

j

dim(Vλj)(k − 1)dim(V

λ )−1

j=1

Then gm(λ) ≤ am(λ).

Here we verify this for the zero eigenvalue of a simple class of 3-uniform hypergraphs – sometimes called “loose paths” or “linear hyperpaths” – by obtaining an explicit description of the irreducible components of their nullvarieties, using this to obtain a generating function that encodes said irreducible components’ dimensions, using results from [1] to obtain an explicit expression for the multiplicity of zero as a root of their characteristic polynomials, and comparing the resulting quantities to conﬁrm the conjecture in this special case.

We brieﬂy deﬁne the multilinear algebra and spectral hypergraph theory terminology and notation used throughout the paper. More detailed information and references can be found in [3, 5]. An order-k hypermatrix1 M over a ring R is a k-dimensional array of values Mi

1···ik ∈

- R (usually R = C), which we often identify with the function M : (i1, . . ., ik)  → Mi


1···ik. A hypermatrix is cubical if the ij, j = 1, . . ., k, all belong to the same index set I, in which case we say that its dimension is |I|, and a cubical hypermatrix is symmetric if, for every permutation σ of I and i = (i1, . . ., ik) ∈ Ik, Mi = Mσ(i), where σ(i) = (σ(i1), . . ., σ(ik)). An order-k cubical hypermatrix M of dimension n over R gives rise to a homogeneous k-form Mxk, where x = (x1, . . ., xn), given by i∈[n]k Mixi, where xi denotes kj=1 xi

if i = (i1, . . ., ik). The symmetric hyperdeterminant det(M) of a symmetric hypermatrix M over R = C[{xi}i∈[n]k] is the unique monic irreducible polynomial over R which vanishes if and only if ∇(Mxk) = 0 for some nonzero vector x ∈ Cn. The identity hypermatrix I of rank k and order n is the function so that I(i1, . . ., ik) = 1 if i1 = · · · = ik and 0 otherwise. Write λM for the hypermatrix whose i entry is λMi for each valid multi-index i. Then the characteristic polynomial of M is φM(λ) := det(λI − M) ∈ C[λ]. The (homogeneous)

j

![image 1](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile1.png>)

1Variously known as a “tensor” in some literature.

spectrum of M is the multiset of roots of φM(λ); the elements λ of the adjacency spectrum of M are referred to as eigenvalues of M, and any nonzero x so that ∇[(M − λI)xk] = 0 is a corresponding eigenvector. The set of all eigenvectors corresponding to an eigenvalue λ of a hypermatrix M of dimension n is its λ-eigenvariety Vλ. Then Vλ is an aﬃne algebraic variety in Cn; indeed, since the equations deﬁning eigenvectors are homogeneous, Vλ can also be viewed as a projective variety, although we adhere to the aﬃne perspective presently. The multiplicity of λ as a root of φM(λ) is its algebraic muliplicity, and the dimension of the variety Vλ is its geometric multiplicity. Since the 0-eigenvariety of a matrix M – i.e., a hypermatrix of order k = 2 – is its nullspace, we refer to the 0-eigenvariety as the nullvariety of M. We also refer to the algebraic multiplicity of 0 as the nullity of M.

A (uniform) hypergraph H of rank k is a pair (V, E), where E ⊂ Vk . The adjacency hypermatrix of a hypergraph H is the symmetric hypermatrix A(H) : V k → C so that A(H)v

1···vk is 1/(k − 1)! if {v1, . . ., vk} ∈ E(H) and 0 otherwise. The k-form p(x1, . . ., xk) = A(H)xk is sometimes known as the Lagrangian polynomial of H; the coordinate ∂p/∂xi of ∇A(H)xk is (k times) the Langrangian polynomial of the link of vertex vi in H, i.e., the hypergraph whose edges are {e \ {xi}|vi ∈ e ∈ E(H)}. We will often abuse notation slightly and refer to the multilinear algebraic properties of A(H) by describing them as properties of H instead. For example, the (adjacency) spectrum of a hypergraph H is the spectrum of A(H), the nullvariety of H is the nullvariety of A(H), and φH(λ) := φA(H)(λ). A loose hyperpath Pnk is the k-uniform hypergraph on n edges {e1, . . ., en} so that, for i = j, |ei ∩ej| is 1 if |i − j| = 1 and 0 otherwise. We label the vertex set V (Pnk) with {v1, . . ., v(k−1)n+1} so that ej = {v(k−1)(j−1)+1, . . ., v(k−1)j+1} for j ∈ [n].

Throughout, we also write V(S) for the aﬃne variety over C deﬁned as the zero locus of the set of polynomials S, and V(p) for V({p}). We write S for the ideal generated by a set of polynomials S, and call S irredundant if S′ = S when S′ S is any proper subset. Also, given p ∈ C[x1, . . ., xm] and a vector c ∈ Cm, we will sometimes say “c satisﬁes p” if p(c) = 0.

In the next section, we enumerate the irreducible components of the nullvariety of Pn3 and capture their count and the quantity gm(0) as a generating function. The following section repeats this exercise, but for the nullity am(0) of Pn3 – in fact, more generally Pnk for k ≥ 3. The last section compares these two functions of n, verifying the Hu-Ye Conjecture for the zero eigenvalue of Pn3.

## 2 Null Variety for Rank-3 Loose Hyperpaths

We examine the “geometric multiplicity” of the zero eigenvalue for a hypergraph H, or more accurately, the multiset of dimensions of irreducible components of the corresponding nullvariety. Our strategy will be as follows. First, we describe the ideal whose zero locus is the nullvariety, generated by the Lagrangian polynomials of the links of all vertices. Each of the degree-one vertices contributes a polynomial to the ideal which is a simple product of variables. Thus, the vanishing of these monomials reduces to the vanishing of each of their

constituent variables, one at a time. Considering the set of possible vanishing monomials – which correspond to vertices/coordinates where portions of the nullvariety are zero – results in substantial simpliﬁcation of the set of polynomials in the ideal. Thus, taking the union of all such vanishing set possibilities gives a decomposition of the nullvariety into simpler subvarieties. We then analyze these subvarieties to show that they are irreducible. Next, it is necessary to identify which such irreducible subvarieties are maximal in order to obtain an irredundant list of irreducible components. Finally, we describe the multiset of these components’ dimensions by counting the number of polynomials determining them, leading to an expression for gm(0). As a warm-up, and for completeness, we start with the one-edge and two-edge hyperpaths.

### 2.1 Small Cases

- Proposition 2.1. The 3-uniform hyperedge H = P13 has three irreducible components of dimension 1, and gm(0) = 3.

Proof. Let the vertices of H be v1, v2, v3. Given a null vector x, if the adjacency tensor of H is A = A(H), then the i-th component of Ax2 is given by {i,j,k}∈E(H) xjxk = x1x2x3/xi. Since x is a null vector, we have x1x2 = x1x3 = x2x3 = 0, and we consider the variety V0 ⊂ C3 in three-dimensional aﬃne space deﬁned by these equations. If p, q are polynomials, then V(p, q) = V(p) ∩ V(q) and V(pq) = V(p) ∪ V(q). Therefore, we have the following.

V(x1x2, x1x3, x2x3) = V(x1x2) ∩ V(x1x3) ∩ V(x2x3)

= [V(x1) ∪ V(x2)] ∩ [V(x1) ∪ V(x3)] ∩ [V(x2) ∪ V(x3)]

This is equal to the union over all choices of V(xi) ∩ V(xj) ∩ V(xk) = V(xi, xj, xk) where i ∈ {1, 2}, j ∈ {1, 3}, and k ∈ {2, 3}. Thus, maximal subvarieties of V0 correspond to minimal sets {i, j, k} given these conditions, i.e.,

[V(x1) ∪ V(x2)] ∩ [V(x1) ∪ V(x3)] ∩ [V(x2) ∪ V(x3)] = V(x1, x2) ∪ V(x1, x3) ∪ V(x2, x3). Since V(xi, xj) is the xk-axis, V0 is the union of three lines.

![image 2](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile2.png>)

![image 3](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile3.png>)

![image 4](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile4.png>)

![image 5](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile5.png>)

- Proposition 2.2. If H = P23, then V0 has one component of dimension 1 and another of dimension 3, so that gm(0) = 13.


Proof. Let the vertices of H be v1, v2, v3, v4, v5. Let x be a null vector. The equations deﬁning V0 ⊂ C5 are x1x3 = x2x3 = x1x2 + x4x5 = x3x4 = x3x5. Decompose this system as follows:

V0 = V(x1x3, x2x3, x3x4, x3x5) ∩ V(x1x2 + x4x5). In the ﬁrst conjunct, we have intersections of unions, namely V(x1x3, x2x3, x3x4, x3x5) = [V(x1) ∪ V(x3)]∩[V(x2) ∪ V(x3)]∩[V(x3) ∪ V(x4)]∩[V(x3) ∪ V(x5)] .

Expand the expression on the right to obtain the union over all choices of V(xi) ∩ V(xj) ∩ V(xk) ∩ V(xℓ) = V(xi, xj, xk, xℓ) where i ∈ {1, 3}, j ∈ {2, 3}, k ∈ {3, 4}, and ℓ ∈ {3, 5}. The union {i,j,k,ℓ} V(xi, xj, xk, xℓ) is the union over the minimal sets {i, j, k, ℓ} of this form, i.e.,

[V(x1) ∪ V(x3)] ∩ [V(x2) ∪ V(x3)] ∩ [V(x3) ∪ V(x4)] ∩ [V(x3) ∪ V(x5)]

=V(x3) ∪ V(x1, x2, x4, x5).

The second variety has dimension four, while the ﬁrst variety is the x3 axis. It remains to intersect each such set with V(x1x2 +x3x4). Note that V(x1, x2, x4, x5) ⊆ V(x1x2 +x4x5), so that intersection yields V(x1, x2, x4, x5). The intersection of V(x1x2 + x4x5) and V(x3) gives V(x1x2 + x4x5, x3), which is a three-dimensional variety. Thus,

V0 = V(x1, x2, x4, x5) ∪ V(x1x2 + x4x5, x3), which is the union of a one-dimensional and a three-dimensional irreducible component.

![image 6](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile6.png>)

![image 7](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile7.png>)

![image 8](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile8.png>)

![image 9](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile9.png>)

### 2.2 General 3-uniform case

We now generalize the above approach to all 3-uniform loose hyperpaths. Deﬁne pk to be xk−2xk−1 + xk+1xk+2 for some integer k. For integer n ≥ 1, deﬁne A′n := {2k + 1 : 1 ≤ k ≤ n − 1}, and let An = A′n \ {3, 2n − 1}. Deﬁne Fn be the collection of “Fibonacci subsets” of

- A′n, i.e., sets containing at least one of each two consecutive elements: Fn = {S ⊂ A′n : ∀k ∈ [n − 2], (2k + 1 ∈ S) ∨ (2k + 3 ∈ S)}


Let S be any element of Fn. We say that a set of polynomials B ⊂ {xi : i ∈ [2n + 1]} ∪ {pi : i ∈ A′n} is S-admissible if it can be obtained in the following manner. Deﬁne Ui, i = 1, 2, 3, 4, in the following way.

- 1. U1 = {xi : i ∈ S}
- 2. U2 =

 



{x1, x2} if x3 ∈/ U1, x5 ∈ U1 {x1} or {x2} if {x3, x5} ⊆ U1 {p3} if x3 ∈ U1, x5 ∈/ U1

- 3. U3 =

 



{x2n, x2n+1} if x2n−1 ∈/ U1, x2n−3 ∈ U1 {x2n} or {x2n+1} if {x2n−3, x2n−1} ⊆ U1 {p2n−1} if x2n−1 ∈ U1, x2n−3 ∈/ U1

- 4. U4 = a∈A


 

∅ if {xa−2, xa+2} ⊆ U1 {xa+1} if xa−2 ∈ U1, xa+2 ∈/ U1 {xa−1} if xa−2 ∈/ U1, xa+2 ∈ U1 {pa} if {xa−2, xa+2} ⊆ {xj : j ∈ A′n} \ U1



Note that the only choices that do not depend only on S arise from cases of U2 and U3. If we let Ui denote the collection of all allowable Ui, i = 2, 3, then TS = {U1 ∪ U2 ∪ U3 ∪ U4 : U2 ∈ U2, U3 ∈ U3} is the collection of S-admissible sets. We also remark that for each B ∈ TS, B ⊆ C[x1, . . ., x2n+1]. Deﬁne IB as the ideal in C[x1, . . ., x2n+1] generated by the polynomials in B. Furthermore, let In denote the collection of all such ideals generated by S-admissible sets in Fn, i.e.,

In = {IB : B ∈ TS for some S ∈ Fn}. Before proceeding, we note the following useful fact.

- Proposition 2.3 (Prop. 5.20 in [9]). If V and W are irreducible aﬃne varieties over an algebraically closed ﬁeld, then V × W is as well.


In fact, the way we will often use Proposition 2.3 is: if I ⊂ C[x1, . . ., xn] and J ⊂ C[y1, . . ., ym] are prime ideals and I′, J′ are the ideals they generate in C[x1, . . ., xn, y1, . . ., ym], respectively, then I′ + J′ is also a prime ideal, and V(I′ + J′) = V(I) × V(J). The following lemma establishes that the ideals in In are prime.

- Lemma 2.4. For n ≥ 3 and each IB ∈ In, IB is a prime ideal in C[x1, . . ., x2n+1], and B is an irredundant set of generators for it.


Proof. First, since polynomial rings over C are UFDs, primality is equivalent to irreducibility throughout. Note that the generators of IB are a ﬁnite collection of variables and polynomials of the form pk for some odd integer(s) k. Let X = {xi : xi ∈ IB} and X′ = {x1, . . ., x2n+1}\X. Furthermore, let K = {pk : pk ∈ IB}. By Proposition 2.3, it suﬃces to show the primality of the ideal generated by K in the ring C[X′], since the variables appearing in K are disjoint from those of X. The base case |K| = 1 holds if and only if the polynomial in K is irreducible. Let i ∈ Z so that pi ∈ K. It is easy to see that pi = xi−2xi−1 +xi+1xi+2 is irreducible. Fix an integer k ≥ 1 and suppose that the result holds for all K′ with |K′| = k. Let |K| = k +1 and let pi be any element of K. By the induction hypothesis, K \ {pi} generates a prime ideal. From here we split into the following two cases.

- Case 1: The variables of pi are disjoint from those of K \ {pi}. As noted above, pi generates a prime ideal in C[xi−2, xi−1, xi+1, xi+2], so it also generates a prime ideal in C[X]. Moreover, the induction hypothesis gives that K \ {pi} generates a prime ideal in C[X′\{xi−2, xi−1, xi+1, xi+2}], further implying that K\{pi} generates a prime ideal in C[X] by Proposition 2.3.
- Case 2: Some variables of pi also occur as variables of polynomials in K \ {pi}. Since i is odd, i − 1 and i + 1 are even. Moreover, the variables xi−1 (and xi+1) appear in no other polynomial of K, since pi, pi−2 ∈ K (respectively, pi and pi+2) implies both i and i − 2 (respectively, i and i + 2) are outside the set B used to generate the original ideal IB, contradicting that B is generated by a Fibonacci subset of A′n. Therefore, the only overlap in variables comes from xi−2 and xi+2.


Let X be the collection of variables in pi that also appear in polynomials of K \ {pi}. Deﬁne Y := {xi−2, xi−1, xi+1, xi+2}\X, and let Z be the collection of variables in polynomials of K except the variables contained in X. Deﬁne a collection of new variables X′ := {x′m : xm ∈ X}. Let the polynomial p′i be pi evaluated at the variables of X′ and Y , where each input variable matches the index of the existing variable. Let I be the ideal generated by K \ {pi}. The induction hypothesis gives that I is prime. The ideal p′i is prime because p′i is irreducible. Proposition 2.3 gives the primality of the ideal generated by I + p′i . Let σ : C[X ∪ Z] × C[X′ ∪ Y ] → C[X ∪ Y ∪ Z] be the quotient homomorphism σ : f  → f +  {xi − x′i : xi ∈ X} . Clearly, σ is surjective, so Proposition 3.34b in [9] (that surjective homomorphisms preserve primality) completes the proof of primality.

The second claim, that B is irredundant, is straightforward to check from the conditions deﬁning Ui, i = 1, . . ., 4: with respect to the variable ordering

x1 ≺ x3 ≺ · · · ≺ x2n+1 ≺ x2 ≺ x4 ≺ · · · ≺ x2n, the set B is triangular (its ≺-main variables are distinct), so form a basis of IB = B .

![image 10](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile10.png>)

![image 11](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile11.png>)

![image 12](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile12.png>)

![image 13](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile13.png>)

If we let Wn denote the collection of aﬃne varieties generated by ideals of In, i.e., Wn := I∈I

V(I), then the previous lemma implies that all varieties in Wn are irreducible. However, some of these varieties may not be inclusion-maximal, so they are not irreducible components, a matter we address presently.

n

- Lemma 2.5. Let IV denote the ideal in In which generates the variety V . Furthermore, let ΘV denote the collection of all maximal sets of consecutive odd-indexed xi ∈ IV whose indices are contained in A′n. Then, the variety V ∈ Wn is inclusion-maximal if and only if ΘV does not contain a set with odd cardinality m ≥ 3.


Proof. Suppose ﬁrst that there exists an odd m ≥ 3 so that X := {xa, xa+2, . . ., xa+2(m−1)} ∈ ΘV . Let B be the generating set for IV which corresponds to an S-admissible set for some

- S ∈ Fn. If a > 3, then the maximality of X implies xa−2 ∈/ IV , giving that xa−1 ∈ IV by condition (4) in the deﬁnition of S-admissible. On the other hand, if a = 3, then condition


(2) gives the presence of either x1 or x2 in IV . In either case, there exists q1 ∈ N so that xq

2 ∈ IV ∩ {xa+2m−1, xa+2m}. Now, deﬁne X′ := {xq

- 1 ∈ IV ∩ {xa−2, xa−1}. Similarly, there exists q2 so that xq


2} ∪ {xa+2, xa+6, . . ., xa+2(m−2)}, which is well-deﬁned since |X| is odd, and, let P′ = {pa, pa+4, . . ., pa+2(m−1)}. Note that |X′| = |P′|+1, so that |B| > |(B\X′)∪P′|. Inspection shows that (B \ X′) ∪ P′ is an S-admissible set for some S ∈ Fn. Moreover, if every polynomial in B yields 0 when evaluated at a tuple (c1, c2, . . ., c2n+1) ∈ C2n+1, then (c1, c2, . . ., c2n+1) is also a common zero of all polynomials in (B \ X′) ∪ P′, since all polynomials of P′ evaluate to zero if those of X ∪ {xq

, xq

1

2} ⊆ B do as well. Then V is not maximal.

, xq

1

It remains to establish the converse. If n ≤ 3, it is straightforward to check that the varieties in Wn are maximal. Suppose now that n ≥ 4 and that V ∈ Wn is not maximal, so there exists V ′ ∈ Wn with V V ′. Let B and B′ be the admissible sets which generate IV and IV′ respectively, meaning B and B′ also generate V and V ′. Since V ⊂ V ′, if values for

x1, . . ., x2n+1 are chosen so that all polynomials in B are zero, then all the polynomials in B′ are also zero for the same choice of values for x1, . . ., x2n+1. By the deﬁnition of admissible sets, B and B′ are each minimal generating sets of their respective ideals, and additionally B ∩ B′ ∈/ {B, B′}, i.e., neither is a subset of the other.

Next, we establish the following claim regarding the inclusion of single-variable monomials between B and B′. Let i ∈ [2n − 1]. Claim 2.6. If xi ∈/ B, then xi ∈/ B′.

Proof of claim. Suppose i ∈ [2n − 1] and xi ∈/ B. Let c = (c1, . . ., c2n+1) ∈ V . If ci = 0, then xi ∈/ B′, as otherwise c  ∈ V ′, contradicting that V ⊂ V ′. Suppose now that ci = 0. The following cases construct another point c′ so that c′ ∈ V with c′i = 0, again obtaining a contradiction to V ⊂ V ′.

- Case 1: i ∈ {1, 2, 2n, 2n + 1}. Without loss of generality, suppose i = 1, and note that the only polynomials of any admissible set in which x1 occurs are x1 and p3, and, in this case, x1  ∈ B. If p3 ∈ B, deﬁne c′ so that c′i = ci for i  ∈ {1, 2}, but c′1 = 1 and c′2 = −x4x3. The choice of c′2 gives p3(c′) = 0. Since p3 ∈ B implies x2 ∈/ B, c′ ∈ V . If p3 ∈/ B, deﬁne c′ so that c′j = cj for j = 1, but c′1 = 1. All polynomials of B are satisﬁed by c′.
- Case 2: 3 ≤ i ≤ 2n − 1 and i odd. Note that the only possible polynomials containing xi are pi−2, pi+2, and xi. By assumption, xi ∈/ B, leaving only pi−2 and pi+2. Deﬁne c′ so that c′j = cj for j  ∈ {i − 1, i, i + 1} and c′i = 1. If pi−2 ∈ B (resp. pi+2 ∈ B), deﬁne c′i−1 = −xi−4xi−3 (resp. c′i+1 = −xi+4xi+3), so that pi−2(c′) = 0 (resp. pi+2(c′) = 0). The existence of pi−2 ∈ B (resp. pi+2) implies xi−1 ∈/ B (resp. xi+1 ∈/ B). Clearly, pi is the only other polynomial containing either xi−1 or xi+1, but xi ∈/ B implies xi−2, xi+2 ∈ B, further giving that pi ∈/ B. Therefore, all polynomials of B are satisﬁed by c′.
- Case 3: 3 ≤ i ≤ 2n−1 and i even. Note that the only possible polynomials containing xi are pi−1, pi+1, and xi. By assumption, xi ∈/ B, leaving only pi−1 and pi+1. If xi−1, xi+1 ∈ B, then pi−1, pi+1 ∈/ B, so deﬁning c′j = cj for j = i and c′i = 1 yields a c′ satisfying all polynomials of B. Suppose now that not both of xi−1 and xi+1 are in B. Condition (1) gives that at least one of xi−1 and xi+1 are in B, so B cannot contain both of pi−1 and pi+1. Without loss of generality, suppose pi−1 ∈ B, giving that xi+1 ∈/ B. In this case, deﬁne c′ so that c′j = cj for j  ∈ {i, i + 1, i + 2}, c′i = 1, and c′i+1 = −ci−3ci−2. Then pi−1(c′) = 0, so the only other polynomial containing xi+1 is pi+3. If c′i+1 = 0, then we already have c′ ∈ V . Suppose now that c′i+1 = 0. If pi+3 ∈/ B, then take c′i+2 = ci+2, and c′ ∈ V . Otherwise, take c′i+2 = −ci+4ci+5/c′i+1. In this case, xi+3, pi+3 ∈ B gives that xi+2 ∈/ B. Furthermore, xi+3 ∈ B also implies pi+1 ∈/ B, meaning pi+3 is the only polynomial of B containing xi+2. Therefore, in this case, c′ ∈ V . ♦


We will often use the above claim in contrapositive form, i.e., if xi ∈ B′, then xi ∈ B.

Suppose the polynomial pa is an element of B′ \B. Thus, xa−2 ∈ B \B′ or xa−1 ∈ B \B′ by condition (4). The same conclusion can be drawn of xa+1 or xa+2. Without loss of generality, there are three cases: xa−2, xa+2 ∈ B \ B′ and xa−1, xa+1  ∈ B \ B′, xa−1, xa+1 ∈ B \ B′, and xa−1, xa+2 ∈ B \ B′. Suppose, by way of contradiction, that ΘV does not contain a set of odd cardinality greater than 1.

Case 1: {xa−2, xa+2} ⊂ B \ B′ and xa−1, xa+1  ∈ B \ B′. Since B′ is an admissible set, then xa ∈ B′, further implying xa ∈ B by the above claim. Let Ma be the element of ΘV containing xa. By assumption, |Ma| is even. If MaL denotes the subset of variables in Ma with indices less than a and MaR denotes the subset of variables in Ma with indices greater than a, then exactly one of |MaL| and |MaR| is odd. Without loss of generality, suppose |MaR| is odd, and let xa+2q be the variable of largest index in Ma. Clearly q ≥ 1.

Since xa+2m ∈ B for all 0 ≤ m ≤ q, we have that xa+2m+1 ∈/ B for each 0 ≤ m ≤ q −1 by condition (4). The above claim gives that xa+2m+1 ∈/ B′ for each 0 ≤ m ≤ q − 1. Therefore, xa+2, xa+3  ∈ B′, so pa+4 ∈ B′ by condition (4), so xa+6  ∈ B′. Repeating this argument,

- B′ \ B contains polynomials pi for i ∈ {a, a + 4, a + 8, . . ., a + 2(q − 1)}, since |MaR| odd implies q odd. Furthermore, xa−2, xa+2, xa+6, . . ., xa+2q ∈/ B′. If a + 2(q + 1) ≤ 2n − 1, then xa+2q being the variable with maximum index in Ma implies xa+2(q+1) ∈/ B. The above claim gives xa+2(q+1) ∈/ B′, and this together with xa+2q ∈/ B′ contradicts condition (1). Therefore, a + 2q = 2n + 1. Since xa+2(q−1), xa+2q ∈ B, then exactly one of x2n and x2n+1 are not in B. Without loss of generality, suppose x2n ∈/ B. By the above claim, we have that x2n ∈/ B′. This together with xa+2q ∈/ B′ contradicts condition (3), completing the case.


- Case 2: {xa−1, xa+1} ⊆ B \ B′. By the deﬁnition of an admissible set, we have xa ∈/ B (as otherwise implies xa−2 ∈/ B and xa+2 ∈/ B, giving that pa ∈ B, a contradiction). The absence of xa in B further implies that xa ∈/ B′ by the above claim. If 3 < a < 2n − 1, then {xa−2, xa+2} ⊆ B. If a = 3 or a = 2n − 1, suppose without loss of generality that a = 3, in which case xa+2 ∈ B. For any a, there exists xj with j ∈ {a + 2, a − 2} so that

- 3 ≤ j ≤ 2n − 1 and xj ∈ B. The presence of pa ∈ B′ requires xj ∈/ B′. This together with xa ∈/ B′ contradicts the deﬁnition of an admissible set.


- Case 3: Without loss of generality, {xa−1, xa+2} ⊆ B \ B′. Suppose that 3 < a < 2n − 1. Since B′ is an admissible set, xa+2 ∈/ B′ implies xa ∈ B′, so xa ∈ B by the above claim. Furthermore, {xa, xa−1} ⊂ B implies xa−2 ∈/ B, giving that xa−2 ∈/ B′, again by the above claim. Let Ma be the element of ΘV containing xa. We have that xa is the variable with smallest index in Ma, since xa−2 ∈/ B. Let xa+2q be the variable with largest index in Ma. Since |Ma| is even, we have that q ≥ 1 is odd. Therefore, applying the argument from case


- 1 completes this case as well.


Since this considers all cases, this completes the proof that, if V is not maximal, then B contains a maximal odd order collection of monomials with consecutive indices in A′n.

![image 14](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile14.png>)

![image 15](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile15.png>)

![image 16](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile16.png>)

![image 17](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile17.png>)

Let Jn denote the collection of all ideals in In which generate inclusion-maximal irre-

ducible varieties. Furthermore, deﬁne Tn to be the subcollection of S∈F

TS containing all admissible sets which generate ideals in Jn. Lastly, deﬁne Fˆn to be the subcollection of Fn containing all Fibonacci subsets of A′n which give rise to at least one admissible set in Tn, i.e., subsets S of A′n = {3, 5, . . ., 2n − 1} so that at least one of every two consecutive elements of A′n belong to S, and so that maximal intervals of A′n contained in S are either a single element or have even length.

n

- Theorem 2.7. If H = Pn3 for some n ≥ 3, then the null variety V0 of H can be written ∪J∈JnV(J), where Jn is as deﬁned above and each J ∈ Jn is an irreducible component of V0.


Proof. Recall that the hyperpath H has exactly 2n + 1 vertices, and we label them with {v1, . . ., v2n+1} so that the j-th edge is ej = {v2(j−1)+1, . . ., v2j+1} for j = 1, . . ., n.

In constructing the equations that deﬁne V0, there are n − 1 vertices giving rise to equations of the form pk = 0, while the other n + 2 vertices give equations of the form xixj = 0. We begin by considering the variety deﬁned by all polynomials of the second form. Let xi

for 1 ≤ k ≤ n + 2 be the n + 2 polynomials of this form. Then

xj

k

k

n+2

n+2

k}nk=1+2 =

V(xi

(V(xi

) ∪ V(xj

V {xi

xj

) =

)).

xj

k

k

k

k

k

k=1

k=1

Let ℓk ∈ {ik, jk} for each 1 ≤ k ≤ n + 2, so that

n+2

(V(xi

) ∪ V(xj

)) =

k

k

{ℓk}nk=1+2

k=1

k}nk=1+2).

V({xℓ

Let L be the collection of all choices of {ℓk}. To facilitate analysis of the sets in L, we construct a graph G, where the vertices of G are labeled with the distinct ℓk, and edges connect ℓk and ℓk′ if and only if xℓ

k}nk=1+2. Based on the structure of H and the vertex labeling given originally, G has the following form.

k′ ∈ {xi

xℓ

xj

k

k

2n + 1

- 1
- 2


2n − 3

5

· · ·

2n − 1

3

2n

An element of L corresponds to a set of vertices in G covering E(G), since the vertices of G are labeled by variable indices, edges are given by pairs of indices in a term of

)), and k 2n=1+1 (V(xi

2n+1

) ∪ V(xj

k=1 (V(xi

) ∪ V(xj

)) is the union of intersections over one term from each element of L.

k

k

k

k

A subset S of vertices in G which is an edge cover must, in particular, cover the edges {3, 5}, {5, 7}, . . ., {2n − 3, 2n − 1}, so no two consecutive elements of A′n are absent from any such set. In particular, S ∩ A′n ∈ Fn. Let XS = {xi : i ∈ S}. Since 3  ∈ S implies

1, 2 ∈ S so that S covers the edges {1, 3} and {2, 3}, if x3  ∈ XS, then x1, x2 ∈ XS. Similarly, if x2n−1  ∈ XS, then x2n, x2n+1 ∈ XS. Note that, for any odd a, if

[(xa−2 = 0) ∨ (xa−1 = 0)] ∧ [(xa+1 = 0) ∨ (xa+2 = 0)] (1)

then pa = 0. Then let P be the set of pa so that (1) is not satisﬁed, and deﬁne B = XS ∪ P. Then, for each i ∈ A′n:

- 1. If i  ∈ S and i − 4  ∈ S, then xi  ∈ B, xi−4  ∈ B, and pi−2 ∈ B.
- 2. If i  ∈ S and i + 4  ∈ S, then xi  ∈ B, xi+4  ∈ B, and pi+2 ∈ B.
- 3. If i  ∈ S and i − 4 ∈ S, then xi  ∈ B, xi−4 ∈ B, and xi−1 ∈ B.
- 4. If i  ∈ S and i + 4 ∈ S, then xi  ∈ B, xi+4 ∈ B, and xi+3 ∈ B.
- 5. If 5  ∈ S and x1  ∈ B, then p3 ∈ B.
- 6. If 2n − 3  ∈ S and x2n+1  ∈ B, then p2n−1 ∈ B.
- 7. If 5 ∈ S and x1 ∈/ B, then x2 ∈ B.
- 8. If 5 ∈ S and x2 ∈/ B, then x1 ∈ B.
- 9. If 2n − 3 ∈ S and x2n ∈/ B, then x2n+1 ∈ B.
- 10. If 2n − 3 ∈ S and x2n+1 ∈/ B, then x2n ∈ B.


Let B be the set of all such B generated by the above conditions. Then, we have that the null variety of H is ∪B∈BV(B), and it is easy to see that this is exactly the same as the construction given by I∈I

V(I). Since Lemma 2.4 gives that each of these ideals are prime, the corresponding varieties are irreducible, giving that I∈I

n

V(I) is a decomposition of V0 into irreducible varieties. Furthermore, Lemma 2.5 determines the inclusion-maximal varieties under the inclusion relation, implying that ∪J∈JnV(J) is a decomposition of V0 into its irreducible components.

n

![image 18](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile18.png>)

![image 19](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile19.png>)

![image 20](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile20.png>)

![image 21](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile21.png>)

- Corollary 2.8. For n ≥ 3, the null variety V0 of Pn3 has dimension 2⌊n/2⌋ + 1.


As an illustration of Theorem 2.7, we list all the ideals that generate irreducible components of V0 for P53:

- x1, x2, x5, x9, p5, p9 x1, x2, x4, x5, x7, x8, x10, x11 x3, x7, x10, x11, p3, p7 x3, x6, x7, x9, x10, p3 x3, x6, x7, x9, x11, p3 x1, x3, x5, x6, x9, p9 x2, x3, x5, x6, x9, p9 x1, x3, x5, x7, x9, x10 x1, x3, x5, x7, x9, x11
- x2, x3, x5, x7, x9, x10 x2, x3, x5, x7, x9, x11


### 2.3 Enumeration of Components by Dimension

From here we work to determine the quantity of irreducible components of V0 of diﬀerent dimensions for each Pn3. Fix an n. Let B ∈ Tn, and let S be such that S ∈ Fˆn with B an S-admissible set. Let U1, U2, U3, U4 be given so that B = U1 ∪ U2 ∪ U3 ∪ U4 as in the

2 if x2n−1 ∈/ U1 1 otherwise

2 if x3 ∈/ U1 1 otherwise

, |U3| =

deﬁnition above. Noting that |U1| = |S|, |U2| =

,

and |U4| = |{a ∈ An : a−2 ∈/ S or a+2 ∈/ S}|, the following computation gives an expression for |B|.

|B| = |S| +

2 if x3 ∈/ U1 1 otherwise

+

2 if x2n−1 ∈/ U1 1 otherwise

+ |{a ∈ An : a − 2 ∈/ S or a + 2 ∈/ S}|

= |S| + 13∈/S + 12n−1∈/S + |(A′n − 2) ∩ S| + |(A′n + 2) ∩ S| − |(A′n − 2) ∩ (A′n + 2) ∩ S|

![image 22](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile22.png>)

![image 23](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile23.png>)

![image 24](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile24.png>)

= |S| + 13∈/S + 12n−1∈/S + |(A′n − 2) ∩ S| + |(A′n + 2) ∩ S| − |An ∩ S|

![image 25](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile25.png>)

![image 26](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile26.png>)

![image 27](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile27.png>)

= |S| + 13∈/S + 12n−1∈/S + |A′n| − |(S − 2) ∩ (S + 2)|

= |S ∩ A| + n + 1 − |S ∩ (S + 4)|

Additionally, let µn(S) denote |TS ∩ Jn|, i.e., the number of irreducible components of V0 generated by sets in TS. It is clear that µn(S) ∈ {1, 2, 4}. All irreducible components generated by sets in TS have dimension 2n + 1 − |B| for some B ∈ TS, since the irreducible components all reside in C[x1, . . ., x2n+1], |B1| = |B2| for all B1, B2 ∈ TS, and the sets B ∈ TS are irredundant by Lemma 2.4. Consider the generating function

y|B|zn.

g(y, z) =

n≥0 S∈Fˆn

Note that g(y, z) does not incorporate the multiplicity µn(S). We ﬁrst consider the expression given by the inner sum, namely

y|B|

gn(y) :=

S∈Fˆn

for a given n ∈ N. Computation gives the following results for small values of n.

- g0(y) = y
- g1(y) = y2
- g2(y) = 2y3


- g3(y) = 3y4
- g4(y) = 3y6 + y4
- g5(y) = y8 + 5y6


We develop a recurrence for gn(y) aided by two new sequences of functions, bn(y) and cn(y), deﬁned in the following way:

y|B|

bn(y) =

S∈Fˆn,{2n−3,2n−1}⊆S

y|B|

cn(y) =

S∈Fˆn,2n−3∈/S,2n−1∈S

For clarity, we deﬁne b0 = b1 = b2 = c0 = c1 = c2 = 0. Otherwise, we have the following small values of the two new sequences.

- b3(y) = y4
- b4(y) = y6
- b5(y) = 2y6


c3(y) = y4 c4(y) = y4 c5(y) = 2y6

Note that, for each S a Fibonacci subset of A′n, at least one of 2n − 3 and 2n − 1 are included in S, so there are three options for {2n−1, 2n−3}∩S. All three can be expressed in terms of bn, cn, and gn. A straightforward (if laborious) case analysis provides the following recurrences for the three sequences of functions. Note that these recurrences are valid only for n ≥ 5.

gn(y) = 2y2gn−2(y) + y4bn−3(y) + y2(y2 − 1)cn−2(y) (2) bn(y) = y2gn−2(y) − y2cn−2(y) cn(y) = y2bn−2(y) + y2cn−2(y)

Recall that g(y, z) is the generating function for gn(y). Analogously, let b(y, z) = n≥0 bn(y)zn and c(y, z) = n≥0 cn(y)zn. The following computations work towards closed forms for b, c, and g.

4

gnzn + 2y2

gn−2zn + y4

bn−3zn + y2(y2 − 1)

cn−2zn

g =

n=0

n≥5

n≥5

n≥5

4

2

gnzn + 2y2z2(g −

gnzn) + y4z3b + y2(y2 − 1)z2c

=

n=0

n=0

- 3y6z4 − 4y5z4 + y4z4 + y4z3 + y2z + y + y4z3b + y2(y2 − 1)z2c 1 − 2y2z2

![image 28](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile28.png>)

- b =

4

n=0

bnzn + y2

n≥5

gn−2zn − y2

n≥5

cn−2zn =

4

n=0

bnzn + y2z2(g −

2

n=0

gnzn) − y2z2c

= y6z4 − 2y5z4 − y3z2 + y2z2g − y2z2c

- c =


- 4


g =

4

cnzn + y2

bn−2zn + y2

cn−2zn =

cnzn + y2z2b + y2z2c

n=0

n=0

n≥5

n≥5

y4z4 + y4z3 + y2z2b 1 − y2z2

c =

![image 29](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile29.png>)

Solving the system for g gives the following.

(y8 − 2 y7 + y6)z6 − (y8 − 2 y7)z5 − (2 y6 − 3 y5 + y4)z4 + (y5 − y4)z3 − y2z − y y4z4 − y4z3 − 2 y2z2 + 1

g = −

![image 30](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile30.png>)

Recall that the exponent on y in g(y, z) is the co-dimension of the irreducible component of V0 for Pn3. Since we are interested in the dimension of these components, we make the following transformation. The dimension of each component is 2n+1 minus its co-dimension. Thus, the function we want is given by h(y, z) = y · g(1/y, y2z), expressible as follows (computations throughout performed by SageMath [12]).

h = −y7z6 + 2y6z6 − y5z6 + y5z4 − 2y4z5 − 3y4z4 + y3z5 + 2y3z4 + y3z3 − y2z3 + yz + 1 y4z4 − y2z3 − 2y2z2 + 1

![image 31](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile31.png>)

To help later with verifying Conjecture 1.1, diﬀerentiating with respect to y gives the following expression and then plugging in y = 2, because

H(z) :=

∂ ∂y

h(y, z)

![image 32](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile32.png>)

y=2

(dimV(B))2dimV(B)−1zn.

=

n≥0 S∈Fˆn

The generating function obtained in this way encodes a lower bound on gm(0) of the conjecture, but four times this function is an upper bound. We get the following expression when substituting y = 2:

−1280z10 + 384z9 + 1136z8 + 192z7 − 224z6 − 132z5 − 20z4 + 20z3 + 8z2 + z 256z8 − 128z7 − 240z6 + 64z5 + 96z4 − 8z3 − 16z2 + 1

![image 33](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile33.png>)

= z + 8z2 + 36z3 + 116z4 + 412z5 + 1088z6 + · · ·

The smallest-magnitude root of the denominator lies in the interval (0.37, 0.371). This implies that the coeﬃcients of H(z) have growth rate in the interval (2.69, 2.71). We upperbound the coeﬃcients {ηn}n≥0 of H(z). Recall that Corollary 2.8 gives that the maximum dimension of an irreducible component of V0 for Pn3 is 2⌊n/2⌋+ 1. Since we counted at most one component for each Fibonacci subset of A′n, there are at most Fn (the n-th Fibonacci number) terms which contribute to ηn. Therefore, ηn is bounded above in the following way, given that φ = (1 + √5)/2:

![image 34](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile34.png>)

φn − (−φ)−n √5 · (n + 1) · 2n

ηn ≤

![image 35](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile35.png>)

![image 36](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile36.png>)

### 2.4 Incorporating Multiplicity

Recall that µn(S) ∈ {1, 2, 4} for S ∈ Fˆn, but the above sums ignore this factor. Note that µn(S) > 1 when either pair {3, 5} or {2n−3, 2n−1} are subsets of S. The sequence bn given above accounts for the subcollection of Fˆn containing both 2n − 3 and 2n − 1, so b is the

generating function where the ymzn coeﬃcient counts the number of irreducible components of codimension m from a hyperpath of length n generated from a given S containing both

- 2n − 3 and 2n − 1. By the symmetry of these Fibonacci subsets, the coeﬃcients of b also count the same quantity, where now the Fibonacci set S contains both 3 and 5. So, 2b counts the {3, 5} ⊆ S and {2n − 3, 2n − 1}  ⊆ S components once, the {2n − 3, 2n − 1} ⊆ S and {3, 5}  ⊆ S components once, and the {3, 5, 2n − 3, 2n − 1} ⊆ S components twice. It only remains to count the {3, 5, 2n − 3, 2n − 1} ⊆ S components one additional time.


We now deﬁne gn′ , b′n, and c′n to have the same conditions on the presence of 2n − 3 and

- 2n − 1 in S as was given for gn, bn, and cn above, but now we require that 3 and 5 be in S, i.e.,


gn′ (y) :=

y|B|

S∈Fˆn 3,5∈S

and analogously for b′n and c′n. We deﬁne all three sequences for n ≥ 0, although some initial values are zero. These modiﬁed sequences satisfy the exact same recurrences as displayed in (2) for n ≥ 5.

Let g′, b′, and c′ be the generating functions with respect to the variable z for the three sequences deﬁned. Then, the generating function b′ counts exactly the {3, 5, 2n−3, 2n−1} ⊆ S components once. Computation gives the following rational expression for g′ and b′:

y6z4 + y4z3 y4z4 − y4z3 − 2 y2z2 + 1 b′ = −

g′ =

![image 37](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile37.png>)

y6z5 − y4z3 y4z4 − y4z3 − 2 y2z2 + 1

![image 38](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile38.png>)

Note that the generating function for g′ counts the same irreducible components as b from above. Therefore, the generating function of gm(0), which incorporates multiplicity (aside from some initial terms), is given by G = g + 2g′ + b′, and is given by the following rational function.

G = −y8z6 + y8z5 + 2y7z6 − 2y7z5 − y6z6 − y6z5 + 4y6z4 − 3y5z4 − y5z3 + y4z4

+ 4y4z3 + y2z + y /(y4z4 − y4z3 − 2y2z2 + 1)

Similarly to the previous subsection, we compute h′ = y·G(1/y, y2z), which is the generating function for the number of irreducible components of dimension given by the exponent on y in V0 for Pn3, if n is the exponent on z.

h′ = −y7z6 + 2y6z6 − y5z6 − y5z5 + y5z4 − 2y4z5 − 3y4z4 + y3z5

+ 4y3z4 + 4y3z3 − y2z3 + yz + 1 /(y4z4 − y2z3 − 2y2z2 + 1).

Computing ∂y∂ h′(y, z)

![image 39](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile39.png>)

y=2

yields the following generating function:

−1280z10 + 128z9 + 1200z8 + 352z7 − 336z6 − 308z5 + 4z4 + 56z3 + 8z2 + z 256z8 − 128z7 − 240z6 + 64z5 + 96z4 − 8z3 − 16z2 + 1

![image 40](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile40.png>)

= z + 8z2 + 72z3 + 140z4 + 812z5 + 1648z6 + 7280z7

+ 18064z8 + 60928z9 + 176576z10 + · · ·

Here the linear and quadratic coeﬃcients are incorrect, however, because incorporation of multiplicity only adjusts for n ≥ 3. Modifying this expression via Propositions 2.1 and 2.2, we obtain

H′(z) = −256z8 + 192z7 + 272z6 − 156z5 − 92z4 + 24z3 + 13z2 + 3z 256z8 − 128z7 − 240z6 + 64z5 + 96z4 − 8z3 − 16z2 + 1

![image 41](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile41.png>)

= 3z + 13z2 + 72z3 + 140z4 + 812z5 + 1648z6 + 7280z7

+ 18064z8 + 60928z9 + 176576z10 + · · ·

## 3 Algebraic Multiplicity of Zero

(λ) (the k-uniform linear hyperpath with n edges). We are given the following by the paper of Bao, Fan, Wang, and Zhu.

Let Dn,k be the algebraic multiplicity of zero in the characteristic polynomial of φPk

n

- Theorem 3.1 ([1]). For n ≥ 2,


n

n(k−1)

(λ) = λ(k−2)(k−1)

φPk

n

s=0

where

fs−1(1) λk−1

λ −

![image 42](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile42.png>)

νn,k(s)

k−1

(λ)(k−1)

φPk

,

n−1

νn,k(s) =

ks(k−2)((k − 1)k−1 − kk−2)(k − 1)(n−s−1)(k−1) if s ∈ [0, n − 1], ks(k−2) if s = n,

and

 

- 0 if i = −1,
- 1 if i = 0,


fi(x) =

= λλk

f(x) = 1−xλ1

k−x if i = 1, fi−1(f(x)) if i > 1.

![image 43](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile43.png>)

![image 44](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile44.png>)

−k



We use these facts to prove the following. We start by proving the following lemma concerning the degree of the zero root in f(x). Lemma 3.2. Let k ≥ 2 be given. Let ds be the degree of the zero root in the rational function fs(1). If s ≥ 1, then ds = 0 if s is even and ds = k if s is odd. Proof. We proceed by induction on s, with the base cases given by s = 1 and s = 2. The deﬁnition of fs(x) includes that f(1) = λλk

k−1, giving that d1 = k. For s = 2, then, f2(1) = f(f(1)) = f

![image 45](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile45.png>)

- λk − 1

![image 46](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile46.png>)

- λk − 2


λk λk − 1

=

.

![image 47](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile47.png>)

Now suppose that the result holds for some s ≥ 1. Consider the value of ds+1. Since composition of functions is associative, fs+1(1) = fs(f(1)) = f(fs(1)). Let qs(x) denote the

denominator of fs(x). Since f(x) = λλk

k−x, we can think of fs+1(1) as λkqs(1) divided by λkqs(1) minus the numerator of fs(1).

![image 48](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile48.png>)

If fs(1) is rational in λ with ds = 0, then the denominator of fs+1(1) will not be divisible by λ, but the degree of λ in the numerator is k. Thus ds+1 = k. On the other hand, if ds = k, then fs(1) is rational in λ with the power of λ in the numerator equal to k. Then, fs+1(1) will have k factors of λ in the numerator after multiplying through by qs(1), but the denominator is the diﬀerence of two polynomials both of which have λ occurring k times as a factor. Factor out the term λk from the denominator and cancel it within fs+1(1). This leaves zero factors of λ in the numerator. In the denominator, we have zero factors of λ if and only if the constant term in qs(1) diﬀers from the coeﬃcient of λk in the numerator of fs(1). This inequality of coeﬃcients is established by the following inductive argument, which need only handle the case of s odd. In fact, we include in the inductive hypothesis as well that the numerator and denominator have no nonzero coeﬃcients of terms of the form

- λj with 0 < j < k.


By deﬁnition, f(1) = λλk

k−1, so the constant term in the denominator (namely, −1) and the coeﬃcient of λk (namely, 1) in the numerator diﬀer, giving the base case. Suppose now that the result holds for some odd i ≥ 1. Let fs(1) have numerator α(λ) + α1λk and denominator β(λ) + β1λk + β2, where α and β are both polynomials of degree greater than k, and α1 = β2. Then, we have the following.

![image 49](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile49.png>)

α(λ) + α1λk β(λ) + β1λk + β2

fs+2(1) = f ◦ f

![image 50](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile50.png>)

 

= f 

 λk λk − α(λ)+α

![image 51](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile51.png>)

1λk β(λ)+β1λk+β2

![image 52](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile52.png>)

β(λ) + β1λk + β2 β(λ) + β1λk + β2 − α(λ)λ−k − α1

= f

![image 53](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile53.png>)

λk λk − β(λ)+β

=

![image 54](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile54.png>)

1λk+β2 β(λ)+β1λk+β2−α(λ)λ−k−α1

![image 55](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile55.png>)

λk(β(λ) + β1λk + β2 − α(λ)λ−k − α1) λk(β(λ) + β1λk + β2 − α(λ)λ−k + α1) − β(λ) − β1λk − β2

=

![image 56](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile56.png>)

From this, we see that the coeﬃcient of λk in the numerator is β2−α1, and the constant term in the denominator is −β2. Since α1 = 1 and β2 = −1 in f(1), we have that the constant term in the denominator ﬂips back and forth between −1 and 1 as the powers of f increase by two. On the other hand, β2 − α1 takes values of the form (−1)(s−1)/2 · (s − 1)/2 for odd s ≥ 1. Then the two desired coeﬃcients are never equal, completing the proof.

![image 57](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile57.png>)

![image 58](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile58.png>)

![image 59](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile59.png>)

![image 60](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile60.png>)

- Corollary 3.3. The multiplicity of the zero root of λk −fs(1) is the same as the multiplicity of zero in fs(1).


Proof. The even case is trivial, because both multiplicities are zero. In the odd case, the ratio of the coeﬃcient of λk in the numerator of fs(1) divided by the constant coeﬃcient in the denominator has absolute value less than 1 except when s = 1. However, in that case

- λk − f(1) = λk − λkλ−k1 = λ2λk−2λk


k−1 . We now use the preceding lemma and corollary to fully describe the nullity of Pnk.

![image 61](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile61.png>)

![image 62](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile62.png>)

![image 63](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile63.png>)

![image 64](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile64.png>)

![image 65](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile65.png>)

![image 66](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile66.png>)

- Theorem 3.4. Let k ≥ 1 and n ≥ 1. Additionally, let u = (k − 1)k−1 and v = kk−2. If Dn,k


denotes the multiplicity of λ in the k-uniform hyperpath characteristic polynomial φPk

(λ), then

n

un ([nk − n + 1]u2 + [nk − 2n + 2]uv − [k + n − 1]v2) + k(−v)n+2 (u + v)2 .

Dn,k =

![image 67](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile67.png>)

Proof. We ﬁrst separate the n = 1 case. Cooper and Dutle [3] showed that D1,k = k(k − 1)k−1−kk−1 = k(u−v). Plugging n = 1 into the suggested formula gives the same expression, verifying the result for the base case. Suppose now that n ≥ 2. From Theorem 3.1, we have

n

νn,k(s)

fs−1(1) λk−1

n(k−1)

k−1

(λ) = λ(k−2)(k−1)

(λ)(k−1)

λ −

φPk

φPk

, (3)

![image 68](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile68.png>)

n

n−1

s=0

so we develop a recurrence that gives Dn,k knowing Dn−1,k. From the preceding formula, we see

Dn,k = (k − 2)un + u · Dn−1,k + Fn,k, where we deﬁne Fn,k to be the multiplicity of the zero root in the simpliﬁed rational function

νn,k(s)

s−1(1) λk−1

n

s=0 λ − f

(taking the parameter to be negative if there are excess powers of

![image 69](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile69.png>)

λ in the denominator). As above, let ds be the multiplicity of the zero root in fs(1). By Lemma 3.2, we have that ds−1 is zero when s − 1 is even, and ds−1 = k when s − 1 is odd. Since the s-th term of the product in (3) is [λ−(k−1)(λk − fs−1(1))]ν

n,k(s), and Corollary 3.3 gives that the degree of the zero root in fs−1(1) and λk − fs−1(1) are the same, we have

n

n

Fn,k = −(k − 1)

νn,k(s) · ds−1.

νn,k(s) +

s=0

s=0

We start by considering the value of the ﬁrst term above. We have the following.

n−1

n

νn,k(s) = νn,k(n) +

νn,k(s)

s=0

s=0

n−1

vs(u − v)un−s−1

= vn +

s=0

1 − u v n 1 − uv

![image 70](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile70.png>)

= vn + (u − v)un−1

![image 71](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile71.png>)

![image 72](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile72.png>)

= un

When considering the second summand in the expression for Fn,k, we split into cases initially based on the parity of n. Starting with n odd, we have the following simpliﬁcation of

n

s=0 νn,k(s) · ds−1:

(n−1)/2

n

νn,k(s) · ds−1 =

νn,k(2s) · k

s=0

s=0

(n−1)/2

v2s(u − v)un−1−2s

= k ·

s=0

(n+1)/2

1 − u v22

![image 73](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile73.png>)

= k(u − v)un−1

![image 74](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile74.png>)

1 − uv22

![image 75](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile75.png>)

k u + v

(un+1 − vn+1)

=

![image 76](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile76.png>)

On the other hand, if n is even, we have the following.

n/2

n

νn,k(s) · ds−1 =

νn,k(2s) · k

s=0

s=0

(n−2)/2

= k · vn + k ·

v2s(u − v)un−1−2s

s=0

(n)/2

1 − u v22

![image 77](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile77.png>)

= k · vn + k(u − v)un−1

![image 78](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile78.png>)

1 − uv22

![image 79](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile79.png>)

k u + v

(un+1 + vn+1)

=

![image 80](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile80.png>)

Thus, for general n, we have

n

νn,k(s) · ds−1 =

s=0

k u + v

![image 81](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile81.png>)

This gives the following closed form for Fn,k.

(un+1 − (−v)n+1).

Fn,k = −(k − 1)un +

k u + v

![image 82](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile82.png>)

(un+1 − (−v)n+1)

Substituting this back into the original expression for Dn,k, we have the following simpliﬁcation.

Dn,k = (k − 2)un + u · Dn−1,k + Fn,k

k u + v

= (k − 2)un + uDn−1,k − (k − 1)un +

![image 83](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile83.png>)

un[(k − 1)u − v] − k(−v)n+1 u + v

= uDn−1,k +

![image 84](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile84.png>)

(un+1 − (−v)n+1)

For n = 1, we noted earlier that D1,k = k(u−v). We continue with the following, completing the proof.

n−2

un[(k − 1)u − v] − k(−v)n+1 u + v

un−i[(k − 1)u − v] − k(−v)n−i+1 u + v

Dn,k = kun−1(u − v) +

ui

+

![image 85](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile85.png>)

![image 86](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile86.png>)

i=1

n−2

un−i[(k − 1)u − v] − k(−v)n−i+1 u + v

= kun−1(u − v) +

ui

![image 87](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile87.png>)

i=0

n−2

n−2

un[(k − 1)u − v] u + v −

kui(−v)n+1−i u + v

= kun−1(u − v) +

![image 88](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile88.png>)

![image 89](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile89.png>)

i=0

i=0

1 − − uv n−1 1 − −uv

un(n − 1)[(k − 1)u − v] u + v −

k(−v)n+1 u + v ·

![image 90](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile90.png>)

= kun−1(u − v) +

![image 91](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile91.png>)

![image 92](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile92.png>)

![image 93](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile93.png>)

![image 94](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile94.png>)

un([nk − n + 1]u2 + [nk − 2n + 2]uv − [k + n − 1]v2) + k(−v)n+2 (u + v)2

=

.

![image 95](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile95.png>)

![image 96](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile96.png>)

![image 97](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile97.png>)

![image 98](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile98.png>)

![image 99](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile99.png>)

The next result applies the above theorem to obtain an asymptotic expression for Dn,k. Corollary 3.5. Let k ≥ 3 be ﬁxed and n ≥ 1. Then limn→∞ n(k−1)Dn,k

= 1. In particular, the fraction of eigenvalues of Pnk which are zero approaches 1/(k − 1) as n → ∞. Proof. We have the following expression for Dn,k, where u = (k − 1)k−1 and v = kk−2:

![image 100](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile100.png>)

n(k−1)+1

un ([nk − n + 1]u2 + [nk − 2n + 2]uv − [k + n − 1]v2) + k(−v)n+2 (u + v)2

Dn,k =

![image 101](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile101.png>)

Noting that k ≥ 2, we ﬁrst show that u > v. We have the following computation.

k

k2 k − 1

(k − 1)k−1 kk−2

k2 4k − 4

k2 k − 1 ·

- u

![image 102](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile102.png>)

- v


1 k

1 4

1 −

≥

=

=

=

.

![image 103](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile103.png>)

![image 104](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile104.png>)

![image 105](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile105.png>)

![image 106](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile106.png>)

![image 107](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile107.png>)

![image 108](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile108.png>)

Note that for k ≥ 2, the function k−k1 k is increasing, so its value for any k ≥ 2 is bounded below by its value when k = 2, namely, 1/4. Furthermore, the rightmost expression is greater

![image 109](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile109.png>)

than one if and only if k2 ≥ 4k − 4, which is true because (k − 2)2 ≥ 0. Therefore, u > v, so u dominates v asymptotically. Then the rational expression is asymptotically the same as a ratio of two polynomials just in the variable u, from which it follows that

Dn,k [n(k − 1) + 1]un

lim

= 1.

![image 110](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile110.png>)

n→∞

Since k is constant, this gives the desired result. The second claim in the proof follows because (see [10]) the total number of eigenvalues (counted with algebraic multiplicity) is N(k−1)N, where N is the number of vertices; in this case, N = n(k−1)+1 and, as n → ∞,

- n(k − 1)n(k−1)+1

![image 111](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile111.png>)

- n(k − 1)n(k−1)+2


n(k − 1)n(k−1)+1 (n(k − 1) + 1)(k − 1)n(k−1)+1 ∼

1 k − 1

=

.

![image 112](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile112.png>)

![image 113](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile113.png>)

![image 114](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile114.png>)

![image 115](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile115.png>)

![image 116](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile116.png>)

![image 117](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile117.png>)

From this, we observe the following lower bound for Dn,3 when n ≥ 12. Dn,3 ≥

4n 7

(5n + 3)

![image 118](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile118.png>)

## 4 Conjecture Veriﬁcation

Theorem 4.1. Let V01, . . ., V0κ denote the irreducible components of V0 for Pn3. For n ≥ 1, Dn,3 ≥ κi=1 dim(V0i)(2)dim(V0i)−1. Proof. Recall the following bounds on Dn,3 and ηn, where ηn is the zn coeﬃcient of the generating function H(z) found in Section 2.

4n 7

Dn,3 ≥

(5n + 3)

![image 119](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile119.png>)

φn − (−φ)−n √5 · (n + 1) · 2n It is easy to check that 4(φn + 1) ≤ 2n for any n ≥ 7. Furthermore,

ηn ≤

![image 120](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile120.png>)

![image 121](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile121.png>)

4√5 7 · 2n ≤

√5 7 · 2n ·

![image 122](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile122.png>)

![image 123](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile123.png>)

5n + 3 n + 1 4(φn + 1) ≥ 4(φn − (−φ)−n)

2n ≤

![image 124](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile124.png>)

![image 125](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile125.png>)

![image 126](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile126.png>)

Combining the inequalities shows that Dn,3 ≥ 4ηn for n ≥ 12: 4(φn − (−φ)−n) ≤

√5 7 · 2n ·

![image 127](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile127.png>)

5n + 3 n + 1 4 ·

![image 128](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile128.png>)

![image 129](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile129.png>)

2n

φn − (−φ)−n √5 · (n + 1) ≤

7 · (5n + 3) 4 ·

![image 130](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile130.png>)

![image 131](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile131.png>)

![image 132](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile132.png>)

φn − (−φ)−n √5 · (n + 1) · 2n ≤

4n 7 · (5n + 3)

![image 133](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile133.png>)

![image 134](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile134.png>)

![image 135](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile135.png>)

Therefore, this gives us that the conjecture holds for n ≥ 12, since gm(0) ≤ 4ηn. The following table computes values for n < 12 exactly, completing the proof.

![image 136](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile136.png>)

n 1 2 3 4 5 6 7 8 9 10 11

![image 137](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile137.png>)

![image 138](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile138.png>)

Dn,3 3 35 151 891 3983 19795 88071 407531 1792063 7993155 34740791 gm(0) 3 13 72 140 812 1648 7280 18064 60928 176576 509376

![image 139](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile139.png>)

![image 140](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile140.png>)

![image 141](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile141.png>)

![image 142](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile142.png>)

![image 143](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile143.png>)

![image 144](<2021-cooper-geometric-algebraic-nullity-hyperpaths_images/imageFile144.png>)

## 5 Conclusion

We have shown how to compute the multiplicities of the zero eigenvalue of linear hyperpaths of rank 3 and the dimensions of the irreducible components of the corresponding nullvarieties. This enables us to compute gm(0) and am(0) so that they can be compared in order to verify the Hu-Ye conjecture in this special case. The above analysis can be extended by straightforward generalization to higher rank hyperpaths. Furthermore, some of the issues encountered in carrying out this analysis invite new questions:

- 1. In general, linear hypertrees have many of the properties taken advantage of above for hyperpaths. Therefore, we ask: can these methods be used to answer Conjecture 1.1 for this much more general class of hypergraphs?
- 2. The set of vertices/coordinates where hypergraphs’ nullvectors are zero is combinatorially interesting and plays an integral role in our classiﬁcation of irreducible components. For example, it is not hard to see that these vertex sets are transversals of the hypergraph’s edge set when it is any hypertree. What is possible to say in general about these sets and their relation to the nullvariety’s components?
- 3. We have made no attempt to understand eigenvarieties corresponding to nonzero eigenvalues λ, nor have we attempted to compute their algebraic multiplicities. Doing so would require answering: what are the rest of the root multiplicities of the characteristic polynomials of linear hyperpaths, and how does the structure of non-zero eigenvarieties diﬀer from the nullvariety?
- 4. Is Conjecture 1.1 tight? The quantity proposed for gm(λ) is perhaps not the maximum function of the multiset of eigenvariety component dimensions which still provides a lower bound on am(λ).


## 6 Acknowledgement

The authors wish to thank Fan Chung for so much of the inspiration that paved the road to this subject, and to the organizers of the December 2019 TSIMF conference for creating the occasion to honor her and continue her work.

## References

- [1] Yan-Hong Bao, Yi-Zheng Fan, Yi Wang, and Ming Zhu. A combinatorial method for computing characteristic polynomials of starlike hypergraphs. J. Algebraic Combin., 51(4):589–616, 2020.
- [2] Gregory J. Clark and Joshua N. Cooper. On the adjacency spectra of hypertrees. Electron. J. Combin., 25(2):Paper No. 2.48, 8, 2018.


- [3] Joshua Cooper and Aaron Dutle. Spectra of uniform hypergraphs. Linear Algebra Appl., 436(9):3268–3292, 2012.
- [4] Dragosˇ M. Cvetkovi´c and Ivan M. Gutman. The algebraic multiplicity of the number zero in the spectrum of a bipartite graph. Mat. Vesnik, 9(24):141–150, 1972.
- [5] Yi-Zheng Fan, Yan-Hong Bao, and Tao Huang. Eigenvariety of nonnegative symmetric weakly irreducible tensors associated with spectral radius and its application to hypergraphs. Linear Algebra Appl., 564:72–94, 2019.
- [6] Stanley Fiorini, Ivan Gutman, and Irene Sciriha. Trees with maximum nullity. Linear Algebra Appl., 397:245–251, 2005.
- [7] Ivan Gutman and Bojana Borovi´canin. Nullity of graphs: an updated survey. Zb. Rad. (Beogr.), 14(22)(Selected topics on applications of graph spectra):137–154, 2011.
- [8] Shenglong Hu and Ke Ye. Multiplicities of tensor eigenvalues. Commun. Math. Sci., 14(4):1049–1071, 2016.
- [9] James S. Milne. Algebraic geometry (v6.02), 2017. Available at www.jmilne.org/math/.
- [10] Liqun Qi. Eigenvalues of a real supersymmetric tensor. J. Symbolic Comput., 40(6):1302–1324, 2005.
- [11] Irene Sciriha. A characterization of singular graphs. Electron. J. Linear Algebra, 16:451– 462, 2007.
- [12] The Sage Developers. SageMath, the Sage Mathematics Software System (Version 9.2),

2021. https://www.sagemath.org.

- [13] Long Wang and Xianya Geng. Proof of a conjecture on the nullity of a graph. Journal of Graph Theory, 95(4):586–593, 2020.


Joshua Cooper, Department of Mathematics, University of South Carolina, Columbia, SC 29208 USA

E-mail address, Joshua Cooper: cooper@math.sc.edu

Grant Fickes, Department of Mathematics, University of South Carolina, Columbia, SC 29208 USA

E-mail address, Grant Fickes: gfickes@email.sc.edu

