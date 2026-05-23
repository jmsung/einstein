arXiv:1105.2712v3[math.AT]8Nov2011

Spectra of combinatorial Laplace operators on simplicial complexes

Danijela Horak

Max Planck Institute for Mathematics in the Sciences, Inselstrasse 22, D-04103 Leipzig, Germany

J¨urgen Jost

Max Planck Institute for Mathematics in the Sciences, Inselstrasse 22, D-04103 Leipzig, Germany Department of Mathematics and Computer Science, Leipzig University, D-04091 Leipzig, Germany Santa Fe Institute for the Sciences of Complexity, Santa Fe, NM 87501, USA

![image 1](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile1.png>)

Abstract

We ﬁrst develop a general framework for Laplace operators deﬁned in terms of the combinatorial structure of a simplicial complex. This includes, among others, the graph Laplacian, the combinatorial Laplacian on simplicial complexes, the weighted Laplacian, and the normalized graph Laplacian. This framework then allows us to deﬁne the normalized Laplace operator ∆upi on simplicial complexes which we then systematically investigate. We study the eﬀects of a wedge sum, a join and a duplication of a motif on the spectrum of the normalized Laplace operator, and identify some of the combinatorial features of a simplicial complex that are encoded in its spectrum.

Keywords: normalized graph Laplacian, combinatorial Laplacian, hypergraph Laplacian, graph Laplacian, simplicial complex

![image 2](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile2.png>)

- 1. Introduction


The study of graph Laplacians has a long and proliﬁc history. It ﬁrst appeared in a paper by Kirchhoﬀ [23], where he analysed electrical networks and stated the celebrated matrix tree theorem. The Laplace operator L of

Preprint submitted to Elsevier November 26, 2024

[23] operates on a real valued function f on the vertices of a graph as Lf(vi) = deg vif(vi) −

f(vj). (1.1)

vi∼vj

In spite of its rather early beginnings this topic did not gain much attention among scientists until the early 1970’s and the work of Fiedler [13], and his results on correlation among the smallest non-zero eigenvalue and the connectivity of a graph. Before Fiedler drew attention to the graph Laplacian, graphs were usually characterized by means of the spectrum of its adjacency matrix, but in the wake of [13], there has been a number of papers ( e.g. [18] ) arguing in favour of the graph Laplacian and its spectrum. For good survey articles on the graph Laplacian the reader is referred to [26] or [28].

In a diﬀerent tradition, the graph Laplacian was generalized to simplicial complexes by Eckmann [12], who formulated and proved the discrete version of the Hodge theorem; this can be formulated as

ker(δi∗δi + δi−1δi∗−1) ∼= H˜i(K, R) where

Li = δi∗δi + δi−1δi∗−1 is the higher order combinatorial Laplacian. Many subsequent papers then studied properties of the higher order combinatorial Laplacian (see [9],[14],[10]), building upon properties of the graph Laplacian. In particular, this operator has been employed extensively in investigating the features of networks related to dynamics and coverings (see [29],[30]). Recently the monograph [21] appeared, where the combinatorial Laplacian is systematically studied in a context of a discrete exterior calculus.

While the graph Laplacian introduced by Kirchhoﬀ naturally appears in his work on electrical ﬂows, for other processes on graphs, like random walks or diﬀusion, a diﬀerent operator appears. This was ﬁrst investigated almost a century after Kirchhoﬀ’s work by Bottema [4] who studied a transition probability operator on graphs that is equivalent to the following version of the graph Laplace operator

1 deg vi v

∆f(vi) = f(vi) −

![image 3](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile3.png>)

i∼vj

f(vj). (1.2)

It took, however, almost another one hundred years until a signiﬁcant advance in the study of this operator ∆, which got to be known by the name

normalized graph Laplacian to distinguish it from the graph Laplacian L and to emphasize the fact that its eigenvalues are in the interval [0, 2]. In contrast to L, ∆ is well suited for problems related to random walks on graphs and graph expanders. For a good introduction to this topic the reader is invited to consult [7] or [16].

The main goals of this paper are a systematic framework that can be used as a starting point for a study of any of the above mentioned versions of the Laplace operator, and the deﬁnition and investigation of the normalized Laplacian on simplicial complexes. The latter is based on the simple observation that the form of the combinatorial Laplacian is tightly connected to the choice of the scalar product on the coboundary vector spaces. On the other hand, the scalar products can be viewed in terms of weight functions. Thus, by controlling the weights, we control the range of the eigenvalues of the Laplace operator. Most importantly, for the normalized Laplacian, the eigenvalues are conﬁned to the range [0, i + 2], where i is the order of the Laplacian. This generalizes the fact that the eigenvalues of the normalized graph Laplacian ∆ are in the interval [0, 2]. We shall analyze the spectrum of this normalized Laplacian and its connection with the combinatorial structure of the simplicial complex. Perhaps somewhat surprisingly, this generality also permits us to gain new insights for its special case, the already extensively studied normalized graph Laplacian.

There have already been several attempts towards the normalization of the combinatorial Laplace operator. In particular, Chung in [5] deﬁned a normalized Laplacian on simplicial complexes as δ∗δ + ρδδ∗, where ρ is a positive constant. However, the spectrum of this operator is not bounded by a constant. Recently, Taszus [31] suggested a normalization of the combinatorial Laplacian via its matrix form D−1/2LiD−1/2, where Li is the matrix corresponding to the operator δ∗δ + δδ∗, where the adjoints are deﬁned with respect to the standard scalar product and D is a diagonal matrix of Li. This operator, too, does not have bounded spectrum. Lu and Pung in [25] considered random walks on hypergraphs, and to that end deﬁned a normalized Laplacian on a uniform hypergraph H as Ls(H) = ∆(GsH), where GsK is a (s − 1)-dual graph (see Deﬁnition 5.2) of a simplicial complex (hypergraph) H. The drawback of this deﬁnition is that it fails to ﬁt into general theory and doesn’t take into account higher order relations among edges of a hypergraph.

As is already clear from Eckmann’s seminal work [12], the Laplacians of a simplicial complex encode its basic topology, that is, its homology groups.

In terms of the spectrum, they are given by the dimensions of the eigensets for the eigenvalue 0. This is the same for all the Laplace operators investigated here. These operators, however, diﬀer in the nonzero part of the spectrum, and thereby encode speciﬁc combinatorial or geometric features of a (perhaps weighted) simplicial complex in addition to its topological aspects. Many combinatorial operations that one can perform on a simplicial complex do not aﬀect its homology; nevertheless, they typically leave characteristic traces in the spectrum of a suitable Laplace operator, and that is what we are trying to explore. In the weighted case, there is additional geometric information that likewise inﬂuences the spectrum. Let us try to explain this aspect from the following perspective. As is well known, from a covering of a set, one can construct a simplicial complex, by letting an i-dimensional simplex corresponds to every intersection of i members of the covering. The Cechˇ cohomology of the covering then is isomorphic the simplicial cohomology of the resulting complex. When, in addition, the set that is covered carries a measure, then we can assign to every simplex in this construction a weight equal to the measure of the corresponding intersection. We thus obtain a weighted simplicial complex, and we can deﬁne a corresponding Laplacian. Its spectrum then reﬂects the geometry of the intersection pattern, and not only its topology. Since such intersection patterns arise in many areas of application, for instance as colocalization patterns of proteins in a cell [] or for many geographical data sets, we wish to propose this Laplacian spectrum as a new tool in data analysis. This will be developed elsewhere, on the mathematical basis of the present paper.

This paper is organized as follows. In Section 2 we give the basic deﬁnitions for simplicial complexes and recall Eckmann’s discrete version of the Hodge theorem. We deﬁne the combinatorial Laplace operator in its full generality and provide explicit expressions. Section 3 starts with the theorem about the number of zeros in the spectrum of the the general Laplace operator. We then discuss the eﬀect of the scalar products on the spectrum and obtain the upper and lower bound on the maximum eigenvalue of the Laplacian. Finally, we state the deﬁnition of the normalized combinatorial Laplace operator, which will be the main object of the remainder of the paper. We calculate the spectrum of the normalized combinatorial Laplacian for some special classes of simplicial complexes in Section 4. In particular, we discuss the spectrum of an i-simplex, of an orientable and a non-orientable circuit, of a path and of a star. In Section 5 we analyse regular, pure simplicial complexes. In Section 6 we discuss the eﬀect of wedges, joins and duplication

of motifs on the spectrum of the normalized combinatorial Laplace operator. In Section 7 we identify the combinatorial features of simplicial complexes that cause the appearance of certain integer eigenvalues in the spectrum of ∆upi . We discuss the occurrence of the eigenvalue i + 2 in the spectrum of ∆upi , and its connection to the chromatic number of the underlying graph of a complex. Furthermore, the relation among the eigenvalue i + 1 and the duplication of vertices is established.

- 2. Notations, deﬁnitions and the combinatorial Laplace operator


An abstract simplicial complex K on a ﬁnite set V is a collection of subsets of V , which is closed under inclusion. An i-face or an i-simplex of K is an element of cardinality i + 1. 0-faces are usually called vertices and 1-faces edges. The collection of all i-faces of simplicial complex K is denoted by Si(K). The dimension of an i-face is i, and the dimension of a complex K is the maximum dimension of a face in K. The faces which are maximal under inclusion are called facets. We say that a simplicial complex K is pure if all facets have the same dimension. Note that there is a natural correspondence of hypergraphs and simplicial complexes in a natural way ( facet of a simplicial complex corresponds to an edge in a hypergraph). For two (i + 1)- simplices sharing an i-face we use the term i-down neighbours, and for two i-simplices which are faces of an (i + 1)- simplex, we say that they are (i + 1)-up neighbours. We say that a face F is oriented if we chose an ordering on its vertices and write [F]. Two orderings of the vertices are said to determine the same orientation if there is an even permutation transforming one ordering into the other. If the permutation is odd, then the orientations are opposite.

In the remainder, K will be an abstract simplicial complex on a vertex set [n] = {1, 2, . . ., n}, when not stated otherwise. The i-th chain group Ci(K, R) of a complex K with coeﬃcients in R is a vector space over ﬁeld R with basis Bi(K, R) = {[F] | F ∈ Si(K)}.

The cochain groups Ci(K, R) are deﬁned as duals of the chain groups, i.e. Ci(K, R) := hom(K, R). The basis of Ci(K, R) is given by the set of functions {e[F] | [F] ∈ Bi(K, R))} such that

e[F]([F′]) =

1 if [F′] = [F] 0 otherwise.

The functions e[F] are also known as elementary cochains. Traditionally, Ci(K, G) for arbitrary group G, are called cochain groups. Inﬂuenced by this naming, we will refer to Ci(K, R) as cochain groups, although we always keep in mind that the Ci(K, R) have the structure of vector spaces. Note that the one-dimensional vector space C−1(K, R) is generated by the identity function on the empty simplex. We deﬁne the simplicial coboundary maps

(δif)([v0, . . ., vi+1]) =

- i+1
- j=0


(−1)jf([v0, . . ., vˆj . . .vi+1]),

where vˆj denotes that the vertex vj has been omitted. The δi are the connecting maps in the augmented cochain complex of K with coeﬃcients in R, i.e., the sequence of vector spaces and linear transformations

. . . ←−−δi+1 Ci+1(K, R) ←−δi Ci(K, R) ←−−δi−1 . . . ← C−1(K, R) ← 0. (2.1)

Alternatively, δi can be viewed as the dual of the boundary map ∂i+1. For a systematic treatment of simplicial homology and cohomology the reader is referred to [20]. It is straightforward to check that δiδi−1 = 0, ergo the image of δi−1 is contained in the kernel of δi and the reduced cohomology group for every i ≥ 0 is

H˜i(K, R) := ker δi/ imδi−1.

After choosing inner products ( , )Ci and ( , )Ci+1 on Ci(K, R) and Ci+1(K, R), respectively, the adjoint δi∗ : Ci+1(K, R) → Ci(K, R) of the coboundary operator δi is deﬁned by

(δif1, f2)Ci+1 = (f1, δi∗f2)Ci, for every f1 ∈ Ci(K, R) and f2 ∈ Ci+1(K, R).

- Deﬁnition 2.1. We deﬁne the following three operators on Ci(K, R):


- (i) i-dimensional combinatorial up Laplace operator or simply i-up Laplace operator

Lupi (K) := δi∗δi,

- (ii) i-dimensional combinatorial down Laplace operator or i-down Laplace operator


Ldowni (K) := δi−1δi∗−1,

- (iii) i-dimensional combinatorial Laplace operator or i-Laplace operator


Li(K) := Lupi (K) + Ldowni (K) = δi∗δi + δi−1δi∗−1. Since

δi−1 ←−−−−→δi∗−1

δi ←−−→δi∗

Ci(K, R)

Ci−1(K, R),

Ci+1(K, R)

all three operators are well deﬁned. Moreover, it follows directly from the deﬁnition that Lupi (K), Ldowni (K) and Li(K) are self-adjoint, non-negative and compact operators. Hence their eigenvalues are real, non-negative, and can be characterized by the Courant-Fischer-Weyl min-max principle.

- Theorem 2.1 (Min-max theorem). Let Vk denote a k-dimensional subspace of V , and assume A : V → V is a compact, self adjoint operator of a Hilbert space V . Then

λk = min

Vk

max

g∈Vk

(Ag, g) (g, g)

![image 4](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile4.png>)

= max

Vm−k+1

min

g∈Vm−k+1

(Ag, g) (g, g)

![image 5](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile5.png>)

, (2.2)

where λ1 ≤ . . . ≤ λm are the eigenvalues of A.

For any operator A acting on a Hilbert space, we denote the weakly increasing rearrangement of its eigenvalues by s(A) = (λ0, . . ., λm) and write s(A) =◦ s(B), when the multisets s(A) and s(B) diﬀer only in their multiplicities of zero (this is is an equivalence relation). We denote a union of multisets by ∪◦.

We now state the discrete version of the Hodge theorem and provide its proof for the sake of completeness.

- Theorem 2.2 (Eckmann 1944 ). For an abstract simplicial complex K, ker Li(K) ∼= H˜i(K, R).


Proof. Since δiδi−1 = 0 and δi∗−1δi∗ = 0, then

imLdowni (K) ⊂ ker Lupi (K), (2.3) imLupi (K) ⊂ ker Ldowni (K). (2.4)

Thus,

ker Li(K) = ker δi∗δi ∩ ker δi−1δi∗−1

= ker δi ∩ ker δi∗−1

= ker δi ∩ (imδi−1)⊥ ∼= H˜i(K, R).

![image 6](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile6.png>)

![image 7](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile7.png>)

![image 8](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile8.png>)

![image 9](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile9.png>)

Due to (2.3) and (2.4), λ is a non-zero eigenvalue of Li(K) if and only if it is an eigenvalue of Lupi (K) or Ldowni (K). Therefore,

s(Li(K)) =◦ s(Lupi (K)) ∪◦ s(Ldowni (K)). (2.5)

As a direct consequence of the fact that s(AB) =◦ s(BA), for operators A and B on suitably chosen Hilbert spaces, we get the following equality, which was pointed out to us by Johannes Rauh.

s(Lupi (K)) =◦ s(Ldowni+1 (K)). (2.6)

- From (2.5) and (2.6) we conclude that each of the three families of multisets


{s(Li(K)) | −1 ≤ i ≤ d}, {s(Lupi (K)) | −1 ≤ i ≤ d} or {s(Ldowni (K)) | 0 ≤ i ≤ d}

determines the other two. Therefore, it suﬃces to consider only one of them. In the remainder of the paper, we will omit the argument K in s(Li(K)), s(Lupi (K)), Lupi (K), Ldowni (K), Si(K) etc when it is clear which simplicial complex we investigate or when we state our results for a general simplicial complex K.

For explicit expressions for up and down Laplacians, we have to ﬁx scalar products on the cochain groups. To that end, we introduce the weight function and additional notation.

- Deﬁnition 2.2. The weight function w is an evaluation function on the set of all faces of K


dim K

Si(K) → R+.

w :

i=−1

The weight of a face F is w(F).

For any choice of the inner product on the space Ci(K, R), where elementary cochains form an orthogonal basis, there exists a weight function w, such that

(f, g)Ci =

w(F)f([F])g([F]).

F∈Si(K)

Furthermore, there is a one-to-one correspondence between weight functions and possible scalar products on cochain groups Ci(K, R), such that elementary cochains are orthogonal. In the remainder we will interchangeably use the terms weights, weight function and scalar product.

- Deﬁnition 2.3. Let F¯ = {v0, . . ., vi+1} be an (i + 1)-face of a complex K and let F = {v0, . . ., vˆk, . . ., vi+1} be an i-face of F¯. Then the boundary of the oriented face [F¯] is


∂[F¯] =

k

(−1)k[v0, . . ., vˆk, . . ., vi+1],

and the sign of [F] in the boundary of [F¯] is denoted by sgn([F], ∂[F¯]) and is equal to (−1)k.

By abuse of notation, we will write ∂F¯ to denote the set of all i-faces of F¯. The i-up Laplace operator is given by

w(F¯) w(F)

(Lupi f)([F]) =

![image 10](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile10.png>)

F ¯∈Si+1: F∈∂F¯

w(F¯) w(F)

f([F])+

![image 11](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile11.png>)

F′∈Si:F =F′, F,F′∈∂F¯

sgn([F],∂[F¯])sgn([F′],∂[F¯])f([F′]),

and the expression for the i-down Laplace operator is

w(F) w(E)

(Ldowni f)([F]) =

![image 12](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile12.png>)

E∈∂F

f([F])+

F′:F∩F′=E

w(F′) w(E)

sgn([E],∂[F])sgn([E],∂[F′])f([F′]).

![image 13](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile13.png>)

When dealing with linear operators it is often more convenient to study their matrix form. Hence we give the following expressions for the (e[F], e[F′])-th

and the (e[F], e[F])-th entry of Lupi and Ldowni , where F = F′

w(F¯) w(F)

[F],e[F′]) = sgn([F], ∂[F¯]) sgn([F′], ∂[F¯])

(Lupi )(e

,

![image 14](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile14.png>)

w(F¯) w(F)

(Lupi )(e

,

[F],e[F]) =

![image 15](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile15.png>)

F ¯∈Si+1, F∈∂F¯

w(F′) w(E)

[F],e[F′]) = sgn([E], ∂[F]) sgn([E], ∂[F′])

(Ldowni )(e

,

![image 16](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile16.png>)

w(F) w(E)

(Ldowni )(e

[F],e[F]) =

.

![image 17](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile17.png>)

E∈∂F

The Laplace operator L of a simplicial complex K is uniquely determined by a weight function wK on the faces of K. Thus, we write L(K, wk).

- Remark 2.1. From the explicit expressions of Laplace operators it is evident


that Lupi is uniquely determined by its restriction on the (i + 1)-skeleton of K, whereas Ldowni is determined by its i-skeleton. Therefore, when studying Lupi (or Ldowni ), it suﬃces to observe pure (i + 1)(or i)-simplicial complexes.

Let Di be the matrix corresponding to the operator δi, DiT its transpose and Wi the diagonal matrix representing the scalar product on Ci, then the Lupi and Ldowni operators are expressed as

Lupi = Wi−1DiTWi+1Di, and

Ldowni = Di−1Wi−−11DiT−1Wi, respectively. Therefore, the combinatorial Laplace operator analysed by Duval, Reiner [11], Friedmann [14] and others [29],[9], is the combinatorial Laplace operator Li for the identity matricesas weight matrices Wi (−1 ≤ i ≤ dimK), i.e. Li(K, wK), where wK ≡ 1. In the remainder of the paper, this version of the Laplace operator will be denoted by Li. The graph Laplacian (1.1) studied by Kirchhoﬀ [23], Fiedler [13], Grone and Merris [18] and many others is a special case of Li, in fact it is equal to Lup0 . The normalized graph Laplace operator (1.2) investigated by Chung, Yau, Grigoryan and others, see [6] and [2], is equal to Lup0 for W1 being the matrix with diagonal entries equal to the edge weights and W0 the diagonal degree matrix, that is the weight function on a vertex v is w(v) = deg v.

Therefore, the combinatorial Laplacian L(K, wK), as deﬁned here, uniﬁes all Laplace operators studied so far and provides a general framework for a systematic study of diﬀerent versions of Laplacians.

Our goal in this paper is to deﬁne the higher dimensional analogue of the normalized graph Laplacian and to investigate its properties. However, we will state our results in full generality whenever possible, and emphasize which results do not depend on the choice of the scalar products, and which are the consequence of suitably chosen weights.

- 3. The normalized combinatorial Laplacian: deﬁnition and basic properties


In this section we derive an upper and a lower bound for the maximal

eigenvalue of Lupi , introduce the normalized combinatorial Laplacian ∆upi , and state and prove its basic properties. We emphasize its advantages compared to the other choices of weights.

Let λm and λ0 be the maximl and the minimal eigenvalue of Lupi (K, wK), respectively. As the Laplace operator is positive deﬁnite, λ0 is always larger or equal to zero. The exact number of zero eigenvalues in the spectrum of

Lupi and Ldowni is given in the following theorem.

- Theorem 3.1. The multiplicity of the eigenvalue zero in


- (i) s(Lupi ) is dimCi −

- i
- j=0


(−1)i+j(dimCj − dimH˜j),

or equivalently

dim Ci +

d−i

j=1

(−1)j(dim Ci+j − dimH˜i+j).

- (ii) s(Ldowni ) is


- i−1
- j=0


dimH˜i −

(−1)i+j−1(dim Cj − dimH˜j).

Proof. The following are short exact sequences that split

0 → ker δi → Ci → imδi → 0, 0 → imδi−1 → ker δi → H˜i → 0.

This is a direct consequence of the fact that imδi and H˜i are projective modules (for details on projective modules and splitting exact sequences the reader is referred to [8]). Therefore,

dimCi = dimker δi + dimimδi, (3.1) and

dim ker δi = dimH˜i + dimimδi−1. (3.2)

- From (3.1) and (3.2)


dimimδi =

- i
- j=0


(−1)i+j(dimCj − dim H˜j).

The number of zeros in the spectrum of Lupi is equal to the dimension of its kernel, thus

dimker Lupi = dimker δi = dimCi −

- i
- j=0


(−1)j+i(dimCj − dimH˜j).

The expression (3.1) for the number of zeros in s(Lupi ) is easily obtained by using the Euler characteristic and the equality χ = dj=−1(−1)i dimCi =

- j=−1(−1)i dim H˜i. As for Ldowni , the following holds dimker Ldowni = dimker δi∗−1 = dim Ci − dimimδi−1


d

- i−1
- j=0


(−1)j+i−1(dimCj − dimH˜j).

= dimCi −

![image 18](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile18.png>)

![image 19](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile19.png>)

![image 20](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile20.png>)

![image 21](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile21.png>)

The number of zero eigenvalues in spectra of various Laplace operators, as expected, does not depend on a choice of the scalar products on the cochain vector spaces.

- Remark 3.1. If a simplicial complex is (i+1)-dimensional, then the number of


zero eigenvalues in the spectrum of Lupi (K) is dimCi −dimCi+1 +dimH˜i+1, whereas there are exactly dimCi+1−dimH˜i+1+dimH˜i zeros in the spectrum

of Ldowni+1 . Next we introduce the degree of a simplex F.

- Deﬁnition 3.1. The degree of an i-face F of K is equal to the sum of the weights of all simplices that contain F in its boundary, i.e.


w(F¯).

deg F =

F ¯∈Si+1(K):F∈∂F¯

The upper bound on s(Lupi ) follows from the subsequent discussion. We have

(Lupi f, f) = (δif, δif) (3.3a)

f(∂[F¯]) e[F¯],

f(∂[F¯]) e[F¯]) (3.3b)

= (

F ¯∈Si+1(K)

F ¯∈Si+1(K)

f(∂[F¯])2w(F¯) (3.3c)

=

F ¯∈Si+1(K)

w(F¯), (3.3d)

f([F])2

≤ (i + 2)

F ¯∈Si+1(K):F∈∂F¯

F∈Si(K)

where (3.3d) is obtained by using the Cauchy-Schwarz inequality. In terms of degrees the last inequality can be restated as

(Lupi f, f) ≤ (i + 2)

f([F])2 deg F. (3.4)

F∈Si(K)

By dividing (3.4) by(f, f) we get (Lupi f, f) (f, f) ≤ (i + 2) F∈Si(K)

f([F])2 deg F F∈Si(K) f([F])2w(F)

. (3.5)

![image 22](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile22.png>)

![image 23](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile23.png>)

Replacing f in (3.5) with the eigenfunction fm, corresponding to the largest eigenvalue λmax of Lupi gives

fm([F])2 deg F F∈Si(K) fm([F])2w(F)

λmax ≤ (i + 2) F∈Si(K)

. (3.6)

![image 24](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile24.png>)

Therefore, if

w(F) = deg F, (3.7)

for every F ∈ Si(K), then λmax ≤ i + 2 and the eigenvalues of Lupi are in the interval [0, i + 2].

- Deﬁnition 3.2. Let w be a weight function on K which satisﬁes (3.7) for every face of simplicial complex K, which is not a facet (dimF < dimK), then the Laplace operator deﬁned on the cochain complex of K is called the weighted normalized combinatorial Laplace operator. If additionally, the weights of the facets of K are equal to 1, then the obtained operator is


called the normalized combinatorial Laplace operator and is denoted by ∆upi . We will keep the same notation for the weighted normalized combinatorial Laplacian, emphasizing that we are considering its weighted version.

If (3.7) does not hold, we derive a bound on the maximal eigenvalue of the Laplacian Lupi from the inequality (3.6), i.e.

maxF∈S

i(K) deg F minF∈S

. (3.8)

λm ≤ (i + 2)

![image 25](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile25.png>)

i(K) w(F)

i(K) w(F) stands for the minimal non-zero weight over all i-faces F of K. The inequality (3.8) in the case of the combinatorial Laplacian Lupi reduces to

Here minF∈S

deg F, (3.9) which for i = 0 becomes exactly

λm ≤ (i + 2) max

F∈Si(K)

λm ≤ 2 max

deg v.

v∈S0(G)

This is the well-known bound on the maximal eigenvalue of Lup0 (see [1]). Another upper bound of the spectrum of Lupi was obtained by Duval and Reiner in [11] as a part of more general study, i.e.

λm ≤ n, (3.10)

where n is the number of vertices of the complex K. The inequality (3.9) is sharper than (3.10) for large values of n and small values of i. In particular, if maxF∈S

deg F < n/(i + 2), then the estimate (3.9) is sharper, otherwise it is (3.10). We sum up our results in the following theorem.

i

- Theorem 3.2. The spectrum of Lupi is bounded from above by:

- (i) i + 2, if Lupi = ∆upi ,
- (ii) (i + 2) maxF∈S

i(K) deg F, if Lupi = Lupi ,

- (iii) (i+2) maxF∈S


i(K) deg F/ minF∈S

i(K) w(F), for all other choices of scalar products.

In the following theorems we present some lower bounds on λmax.

- Theorem 3.3. Without loss of generality, let K be a pure simplicial complex of dimension i+1, L(K, wK) the Laplace operator with the weight function wK, λmax the maximal eigenvalue in the spectrum of Lupi (K, wK), and

voli(K) = F∈S

i

deg F, then

- (i) dimCi/(dimCi+1 − dimHi+1) ≤ λmax, if Lupi = ∆upi ,
- (ii) voli(K)/(dimCi+1 − dim Hi+1) ≤ λmax, if Lupi = Lupi ,
- (iii) voli(K)/(maxF∈S


i

w(F)(dimCi+1 − dimHi+1)) ≤ λmax, for all other

choices of scalar products. Proof. The sum of all eigenvalues is equal to the trace of the Laplace matrix, i.e. F∈S

i F ¯:F∈F¯

w(F¯)

![image 26](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile26.png>)

w(F). Together with Theorem 3.1, this yields the inequality

F∈Si F ¯:F∈F¯

w(F¯) w(F)

![image 27](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile27.png>)

![image 28](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile28.png>)

dimCi+1 − dimHi+1 ≤ λmax, (3.11) which proves the theorem.

![image 29](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile29.png>)

![image 30](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile30.png>)

![image 31](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile31.png>)

![image 32](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile32.png>)

- Theorem 3.4. Let K be a pure (i + 1)-dimensional simplicial complex and let λmax denote the maximum eigenvalue of the operator Lupi (K, w), then


(i + 1)D Nd ≤ λmax, (3.12)

D d

+

![image 33](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile33.png>)

![image 34](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile34.png>)

where D, d are maximal degree, weight, respectively over all i-simplices and N is the minimal number of (i + 1)-faces which are incident to an i-simplex of degree D.

Proof. Assume F is an i-simplex of maximal degree with the minimal number of incident (i+1)-faces, i.e. there exist exactly N (i+1)-simplices which con-

tain F as a facet and F ¯:F∈F¯ w(F¯) = D. Let f = Nk=1 sgn([F], ∂[F¯k])e[F¯k], then we obtain

(δi∗f,δi∗f) (f,f)

λmax ≥

![image 35](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile35.png>)

 

N

w(F¯k) w(E)

1 D

sgn([F],∂[F¯k])

sgn([E],∂[F¯k])

≥

![image 36](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile36.png>)

![image 37](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile37.png>)

E∈∂F¯k

k=1

1 D

(e[F],e[F])

=

![image 38](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile38.png>)

  

N

w(F¯k) w(E)

1 D

sgn([F],∂[F¯k])

sgn([E],∂[F¯k])

+

![image 39](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile39.png>)

![image 40](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile40.png>)

E∈∂F¯k: E =F

k=1

N

w2(F¯k) w(E)

1 D

D w(F)

+

=

![image 41](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile41.png>)

![image 42](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile42.png>)

![image 43](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile43.png>)

k=1 E∈∂F¯k: E =F

N

i + 1 dD

D w(F)

w2(F¯k)

+

≥

![image 44](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile44.png>)

![image 45](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile45.png>)

k=1

D2 N

i + 1 dD

D d

≥

+

![image 46](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile46.png>)

![image 47](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile47.png>)

![image 48](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile48.png>)

 

N

w(F¯k) w(E)

sgn([F],∂[F¯k])

sgn([E],∂[F¯k])

e[E],

e[E]

![image 49](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile49.png>)

E∈∂F¯k

k=1

  

D

w(F¯k) w(E)

sgn([F],∂[F¯k])

sgn([E],∂[F¯k])

e[E],

e[E]

![image 50](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile50.png>)

E∈∂F¯k: E =F

k=1

The inequalities above are a consequence of the variational characterization of eigenvalues (Theorem 2.1), and of the Cauchy-Schwarz inequality.

![image 51](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile51.png>)

![image 52](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile52.png>)

![image 53](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile53.png>)

![image 54](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile54.png>)

The previous result for L(K, wK) = L generalizes Proposition 8.2. from [11] and its proof. As another special case of Theorem 3.4 we obtain the following lower bounds for the maximal eigenvalue of the normalized Laplacian.

- Corollary 3.5.


i + 1

D ≤ λmax, (3.13) where D is the maximal degree over all i simplices, and λmax the maximal eigenvalue of ∆upi .

1 +

![image 55](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile55.png>)

- Remark 3.2 (Negative Weights). If negative weights in the deﬁnition of the weight function are allowed , then bilinear forms (inner products) on cochain


vector spaces are no longer positive deﬁnite. With arbitrary weights, Lupi acts on functions on i-simplices

1 w(F) ¯

sgn([F], ∂[F¯])f(∂[F¯]).

∆upi f([F]) =

![image 56](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile56.png>)

F∈Si+1 F∈∂F¯

This approach enables us to use negative weights, but it also deprives us of the structure of the cohomology of simplicial complexes. The eigenvalues need no longer be real nor non-negative. Here, however, we do not pursue the study of Laplacians with negative weights.

- 4. Circuits, paths, stars and their spectrum


In this section we calculate the spectrum of the up (down) normalized Laplace operator for some classes of simplicial complexes.

Theorem 4.1. Let K be an (n − 1)-dimensional simplex. Then s(∆upi (K)) consists of the eigenvalue n/(n−i−1) with multiplicity ni+1−1 and the eigenvalue zero with multiplicity n−i 1 .

Proof. We will prove that the function f ∈ Ci(K, R),

sgn([F], ∂[F¯]) if F is facet of (i + 1)-face F¯ 0 otherwise,

f[F¯]([F]) =

is an eigenfunction of ∆upi (K) for the eigenvalue n/(n − i − 1). It is not diﬃcult to see that there are exactly ni+1−1 linearly independent functions of this form. We have to check that the equality

n n − i − 1

(∆upi f[F¯])[F] =

f([F])

![image 57](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile57.png>)

holds for every i-dimensional face F of K. We distinguish three cases:

# (i) F is an arbitrary facet of F¯. Then,

- w(E¯)

![image 58](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile58.png>)

- w(F)


(∆upi f[F¯])([F]) =

f[F¯]([F])

E ¯∈Si+1: F∈∂E¯

- w(E¯)

![image 59](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile59.png>)

- w(F)


sgn([F],∂[E¯])sgn([F′],∂[E¯])f[F¯]([F′])

+

F′∈Si(L): (∃E¯∈Si+1(L))F,F′∈∂E¯

1 n − i − 1 ¯

=

f[F¯](F)

![image 60](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile60.png>)

- E∈Si+1:
- F∈∂E¯


1 n − i − 1

sgn([F],∂[E¯])sgn([F′],∂[E¯])f[F¯]([F′])

+

![image 61](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile61.png>)

F′∈Si(L): (∃E¯∈Si+1(L))F,F′∈∂E¯

i + 1 n − i − 1

sgn([F],∂[F¯])

= f[F¯]([F]) +

![image 62](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile62.png>)

n n − i − 1

f([F]).

=

![image 63](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile63.png>)

# (ii) F and F¯ have i vertices in common, i.e. they intersect in a face of dimension i − 1.

Then by deﬁnition f([F]) = 0. Let v0, v1, . . ., vi+2 ∈ [n] be arbitrary vertices of L ordered increasingly. Without loss of generality, assume 0 ≤ j < k < l ≤ i + 2, F¯ = [v0, . . ., vˆl, . . ., vi+2] and [F] = [v0, . . ., vˆj, . . ., vˆk, . . ., vi+2]. Then there exist exactly two i-faces F1 and F2 in the boundary of F¯ and two (i + 1)-simplices F¯1 and F¯2 of L, such that F, F1 ∈ ∂F¯1 and F, F2 ∈ ∂F¯2. In particular, F1 = [v0, . . ., vˆk, . . ., vˆl, . . ., vi+2], F2 = [v0, . . ., vˆj, . . ., vˆl, . . ., vi+2] and F¯1 = [v0, . . ., vˆk, . . ., vi+2], F¯2 = [v0, . . ., vˆj, . . ., vi+2]. Now it is straightforward to calculate

(∆upi f[F¯])([F]) = 0 + sgn([F], ∂[F¯1]) sgn([F1], ∂[F¯1])f[F¯])([F1])

+ sgn([F], ∂[F¯2]) sgn([F2], ∂[F¯2])f[F¯])([F2]) = sgn([F], ∂[F¯1]) sgn([F1], ∂[F¯1]) sgn([F1], ∂[F¯])

+ sgn([F], ∂[F¯2]) sgn([F2], ∂[F¯2]) sgn([F2], ∂[F¯])

= (−1)j(−1)l−1(−1)k + (−1)k−1(−1)l−1(−1)j

= 0.

# (iii) F and F¯ have less than i vertices in common.

Then there are no faces in the boundary of F¯ which are (i+1)-up neighbours of F. This implies that ∆upi f([F]) = 0, which completes the proof.

![image 64](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile64.png>)

![image 65](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile65.png>)

![image 66](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile66.png>)

![image 67](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile67.png>)

In the remainder of this section, we calculate the spectrum of circuits, paths and stars.

- Deﬁnition 4.1. A pure simplicial complex L of dimension i is called an ipath of length m iﬀ there is an ordering of its i-simplices F1 < F2 < . . . < Fm, such that Fi and Fj are (i − 1)-down neighbours iﬀ | j − l |= 1. When Fm coincides with F1, we say that L is an i-circuit of length (m−1). The vertices in the intersection mj=1−1 Fj are called centers of L.


(a) 2-circuit of length 6 with an empty center

(b) 2-circuit of length 6 with one vertex in a center

(c) 2-path of length 3

![image 68](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile68.png>)

(d) 2-star of length 3

Figure 1: Examples of circuits, paths and stars

Note that the simplicial complexes in Figures 1(b) and 1(c) have one central vertex, i.e. a center. Before we proceed to calculate s(∆upi ) of these complexes, we recall the deﬁnition of orientability.

- Deﬁnition 4.2. Let K be a pure (i + 1)-dimensional simplicial complex. We say that K is orientable iﬀ it is possible to assign an orientation to all (i + 1)-faces of K in such a way that any two simplices that intersect in an i-face induce a diﬀerent orientation on that face. We say that such simplices are oriented coherently.


Note that if an i + 1-dimensional simplicial complex is orientable, then any of its i + 1-faces has at most one i-down neighbour.

Choosing an orientation on (i + 1)-faces of the orientable simplicial complex K is equivalent to choosing a basis Bi+1(K) of the vector space Ci+1(K, R) consisting of elementary (i + 1)-chains [F¯] that are oriented coherently.

For the subsequent calculations, the following obvious result (see e.g. [15]) will be useful.

Lemma 4.2. If two matrices M and P commute, i.e., MP = PM, and if λ is a simple eigenvalue of P, then its corresponding eigenvector v is also an eigenvector of M.

Let p˜be a permutation of the elements of a basis Bi(K) of Ci(K, R), for an arbitrary simplicial complex K, and let p¯ be the permutation of elementary cochains of dimension i induced by p˜. Denote the linear extension of p¯ on Ci(K, R) by p. Then we have the following equivalences

p˜([F]) = [F] ⇔ p¯(e[F]) = e[F] ⇔ p(e[F]) = e[F].

To simplify the notation, we will designate any of the maps p˜, p¯, p by p. It will be clear from the argument of p which one is used. Furthermore, we will write p(F) to denote the i-face which is uniquely determined by the mapping p([F]). To prove that p and ∆downi commute, it is necessary to check if p∆downi e[F] = ∆downi pe[F] holds for every i-face F. Since

w(F) w(E)

p∆downi e[F] =

p(e[F])

![image 69](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile69.png>)

E∈∂F

+

F′∈Si(K): (∃E∈Si−1(K))F∩F′=E

w(F) w(E)

sgn([E],∂[F])sgn([E],∂[F′])p(e[F′]),

![image 70](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile70.png>)

# and

w(p(F)) w(p(E))

∆downi pe[F] =

![image 71](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile71.png>)

p(E)∈∂p(F)

w(p(F)) w(p(E))

+

p(F′)∈Si(K): (∃p(E)∈Si−1(K)) p(F)∩p(F′)=p(E)

ep([E])

sgn(p([E]),∂p([F]))sgn(p([E]),∂p([F′]))ep([F′]),

![image 72](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile72.png>)

# it suﬃces to show

w(F) w(E)

![image 73](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile73.png>)

E∈∂F

w(p(F)) w(p(E))

=

![image 74](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile74.png>)

p(E)∈∂p(F)

(4.1)

# and

w(p(F)) w(p(E))

w(F) w(E)

sgn(p([E]),∂p([F]))sgn(p([E]),∂p([F′])) =

sgn([E],∂[F])sgn([E],∂[F′]) (4.2)

![image 75](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile75.png>)

![image 76](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile76.png>)

for every F and F′ which are (i − 1)-down neighbours in K and every elementary i-cochain e[F].

- Theorem 4.3. Let K be an orientable i-circuit of length m. Then the eigenvalues of ∆downi (K) are i − cos(2πj/m), j = 0, 1, . . .m − 1.


Proof. Let F1 < F2 < . . . < Fm be the ordering of i-simplices of K satisfying the conditions of Deﬁnition 4.1. Moreover, let [F1], [F2], . . ., [Fm] be a choice of coherent orientation on them. Let p : Ci(K, R) → Ci(K, R) be a map given by p([Fk]) = [Fk+1], for 1 ≤ k < m and p([Fm]) = [F1]. It is not diﬃcult to check that

p∆downi = ∆downi p (4.3) In particular, equality (4.1) is satisﬁed since the weights of all i-faces are equal to 1 and w(F)/w(E) = w(pF)/w(pE). Equality (4.2) holds because i-faces of K are coherently oriented, which gives the equalities sgn([E], ∂[F]) sgn([E], ∂[F′]) =

−1 and sgn([pE], ∂[pF]) sgn([pE], ∂[pF′]) = −1, where F and F′ are (i − 1)down neighbours of K and E is their intersecting face. Hence (4.3) is true.

Let P be the matrix associated to the mapping p. P is a permutation matrix and its characteristic polynomial is λm − 1 = 0. Eigenvectors of P are Uθ = (1, θ, θ2, . . .θm−1)T, where θ is the m-th root of unity. Thus, the eigenfunctions of the map p are uθ([Fk]) = θk−1.

With Lemma 4.2, we can now easily calculate the eigenvalues of ∆downi . Let Ek := Fk−1 ∩ Fk for 2 ≤ k ≤ m − 1 and let Em := Fm ∩ F1. We have

w(Fk) w(E)

w(Fk) w(Ek)

∆downi uθ([Fk]) =

θk−1 +

sgn([Ek],∂[Fk])sgn([Ek],∂Fk−1)θk−2

![image 77](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile77.png>)

![image 78](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile78.png>)

E∈Si−1(L): E∈∂Fk

w(Fk) w(Ek+1)

sgn([Ek+1],∂[Fk])sgn([Ek+1],∂[Fk+1])θk

+

![image 79](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile79.png>)

- 1

![image 80](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile80.png>)

- 2


- 1

![image 81](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile81.png>)

- 2


2 2

+ i − 1)θk−1 −

θk−2 −

θk

= (

![image 82](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile82.png>)

θ−1 + θ 2

= θk−1(i −

)

![image 83](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile83.png>)

2πj m

= θk−1(i − cos(

)).

![image 84](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile84.png>)

It is straightforward to check that a similar equality holds for k = 1 and

- k = m. Thus, λj = i−cos(2πj/n), where j = 0, 1, . . .m−1 are the eigenvalues of ∆downi (K).


![image 85](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile85.png>)

![image 86](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile86.png>)

![image 87](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile87.png>)

![image 88](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile88.png>)

- Remark 4.1. The eigenvalues of an orientable i-circuit depend only on its length, thus there are diﬀerent combinatorial structures which give the same eigenvalues of ∆downi . For example, 1, 1.5, 1.5, 2.5, 2.5, 3 are the eigenvalues


of ∆down2 of both simplicial complexes, in Figure 1(b), and the simplicial complex in Figure 1(a).

A similar analysis can be carried out for a non-orientable i-circuit of length m. In that case we deﬁne p to be p([Fk]) = [Fk+1], for 1 ≤ k < m and p([Fm]) = −[F1]. The remaining calculations are carried out as in Theorem

- 4.3. Thus,


- Theorem 4.4. Let K be a non-orientable i-circuit of length m. Then the


eigenvalues of ∆downi (K) are i − sin(2πj/m) for m even and i + cos(2πj/m) for m odd, where j = 0, 1, . . .m − 1.

- Corollary 4.5. Eigenvalues of ∆downi (K) of an i-path K of length m are λk = i − cos(πk/m), for k = 0, . . ., m − 1


Proof. Since there are no self-intersections of dimension (i − 1) in an i-path, every path is orientable. From Theorem 4.3, we conclude that in the spectrum of the i-th down Laplacian of an i-circuit of length 2m, all eigenvalues appear twice, except (i − 1) and (i + 1). In particular, λk = i − cos(kπ/m) = i − cos((2m − k)π/m) = λ2m−k, for k = 0 and k = m. Let φ = exp(ikπ/m) (where here i = √

![image 89](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile89.png>)

−1 should not be confused with the same symbol i for the order of the Laplace operator), then the eigenvector corresponding to λk is uk = (1, exp(ikπ/m, . . ., exp(i(2m − 1)kπ/m)T.

The function vk = uk + u2m−k is the eigenvector for the eigenvalue λk as well

π(2m−k)

πk

πk

πk

vk(m) = ei

m + ei

m = ei

m + e−i

m .

![image 90](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile90.png>)

![image 91](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile91.png>)

![image 92](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile92.png>)

![image 93](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile93.png>)

It is now a straightforward calculation to see that the ﬁrst m entries of vk, for every k = 0, 1, . . .m − 1, constitute the eigenvectors of K for the eigenvalue i − cos(πk/m).

![image 94](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile94.png>)

![image 95](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile95.png>)

![image 96](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile96.png>)

![image 97](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile97.png>)

This idea generalizes to paths with self-intersections of dimension (i−1), but then it is necessary to distinguish among orientable and non-orientable paths. The eigenvalues of a star are described in the following theorem.

- Theorem 4.6. Let K be a simplicial complex consisting of m i-simplices assembled in a star like formation, i.e., all simplices have one (i − 1)-face in


common. Then the non-zero eigenvalues of ∆downi (K) are i with multiplicity (m − 1) and (i + 1) with multiplicity 1.

Proof. Let Fk, k ∈ {1, . . ., m}, be an i-dimensional face of K and let k Fk = E. Let p : Bi(K, R) → Bi(K, R) be a permutation, such that p([Fk]) = [Fk+1]. Since Fk∩Fj = E, for any two i-faces of K, we can ﬁx the orientations on the Fk such that they induce the same orientation on E. Now it is easy to check that

p∆downi = ∆downi p. Let θ denote an m-th root of unity diﬀerent from 1 and u the eigenvector of p corresponding to it. Then we obtain

w(Fk) w(E)

w(F) w(E)

∆downi uθ([Fk]) =

θk−1 +

![image 98](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile98.png>)

![image 99](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile99.png>)

E,E∈∂Fk

F,F =Fk

1 m

(1 + θ + . . . + θm−1)

=iθk−1 +

![image 100](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile100.png>)

=iθk−1.

uθ([F])

Thus, uθ is an eigenfunction of ∆downi (K) corresponding to the eigenvalue i. The case when θ = 1 results in the eigenvalue k + 1.

![image 101](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile101.png>)

![image 102](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile102.png>)

![image 103](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile103.png>)

![image 104](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile104.png>)

- 5. Regular simplcial complexes


In this section we analyse the spectrum of the normalized Laplacian of a regular simplicial complex, as deﬁned in [27].

- Deﬁnition 5.1. A simplicial complex K is i-regular iﬀ all its i-faces have the same degree.


Note that a regular graph is a 0-regular simplicial complex. To characterize the eigenvalues of regular simplicial complexes, we introduce the notion of i-dual graph and i-path connected simplicial complexes.

- Deﬁnition 5.2. Let K be a simplicial complex. Then a graph GK with the vertex set V = {Fj | Fj ∈ Si(K)} and the edge set E = {(Fj, Fl) | Fj ∩ Fl ∈ Si−1(K)} is called an i-dual graph of K. Note that in graph theory dual graphs are called line graphs.


- Deﬁnition 5.3. A simplicial complex K is i-path connected iﬀ for any two i-faces F1, F2 of K there exists an i-path connecting them.


- Remark 5.1. The deﬁnition of i-path connectedness is diﬀerent from the deﬁnition of i-connected simplicial complexes in [24].


(a) 2-path connected simplicial complex and its 2dual graph

(b) Simplicial complex which is not 2-connected and its 2-dual graph

- Figure 2: Examples of i-path connected simplicial complexes and their dual graphs


From now on, until the end of this section, we assume K to be i+1-path connected.

- Theorem 5.1. Let K be an orientable i-regular simplicial complex, with i-simplices of degree r, and GK its (i+1)-dual graph. Then for r = 1(r = 2)


(i + 2) 2

µk,

λk =

![image 105](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile105.png>)

where the λ’s are the eigenvalues of ∆downi+1 and the µ’s the eigenvalues of ∆up0 (GK), both ordered non-decreasingly. If r = 1, then the only eigenvalue of ∆downi+1 is λ1 = (i + 2).

Proof. Assume r > 1. Since the complex K is orientable, we can choose an orientation on the (i + 1)-simplices of K, s.t. sgn([E], ∂[F]) sgn([E], ∂[F′] = −1, where F and F′ are (i + 1)-simplices and E their intersecting face of dimension i. Such oriented simplices uniquely determine a basis Bi+1 of Ci+1. Hence, the matrix of the operator ∆downi+1 with respect to Bi is equal to (i + 2)/rI − 1/rA, where A = (aij) and aij = 1 if the (i + 1)-simplices Fi and Fj are i-down neighbours. Assume GK is the (i + 1)-dual graph of K,

then GK is regular as well, and the degree of its vertices is (r − 1)(i + 2). Furthermore, the adjacency matrix of GK equals A. Thus

(2 − r)(i + 2) r

(r − 1)(i + 2) r

∆up0 (GK), therefore

∆downi+1 =

I +

![image 106](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile106.png>)

![image 107](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile107.png>)

(2 − r)(i + 2) r

(r − 1)(i + 2) r

λk =

+

µk.

![image 108](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile108.png>)

![image 109](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile109.png>)

The eigenvalue 0 is in s(∆up0 (GK)), thus (2 − r)(i + 2)/r must be in the spectrum of ∆downi+1 (K). Since the operator ∆downi+1 is positive deﬁnite (2 − r)(i + 2)/r ≥ 0, then 2 ≥ r. Together with the assumption at the beginning r > 1, we conclude that r must be equal to 2 (another way to see that r ≤ 2 is from a deﬁnition of orientable simplcial complexes). Finally,

(i + 2) 2

µk.

λk =

![image 110](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile110.png>)

If r = 1, then ∆downi+1 = (i + 2)I and its only eigenvalue is i + 2.

![image 111](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile111.png>)

![image 112](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile112.png>)

![image 113](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile113.png>)

![image 114](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile114.png>)

In other words, the i-up spectrum of the normalized Laplacian of orientable (i + 1)-dimensional pseudomanifolds is uniquely determined by the normalized spectrum of its dual graph.

From the previous theorem we obtain the following corollary.

- Corollary 5.2. Let K be an i-regular, orientable, simplicial complex, with eigenvalue i + 2, then the spectrum of ∆downi+1 is symmetric about (i + 2)/2.


- Theorem 5.3. Let K be an i-regular simplicial complex, with i-simplices of degree r, let GK be its (i + 1)-dual graph and i + 2 ∈ s(∆downi+1 ). Then


(r − 1)(i + 2) r

λk = i + 2 −

µn−k,

![image 115](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile115.png>)

where the λ’s are the eigenvalues of ∆downi+1 and the µ’s the eigenvalues of ∆up0 (GK) both ordered non-deacreasingly, and n is the number of vertices of GK.

Proof. Since i+2 ∈ s(∆downi+1 (K)), according to Theorem 7.1 we can choose an orientation on the (i+1)-simplices of K, s.t. sgn([E], ∂[F]) sgn([E], ∂[F′] = 1,

for every i-down neighbours F and F′, where F ∩ F′ = E and dimE = i. The matrix of the operator ∆downi+1 is

where A = (aij), and

i + 2 r

∆downi+1 =

![image 116](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile116.png>)

I +

1 r

A, (5.1)

![image 117](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile117.png>)

aij =

1 if F and F′ are i- down neighbours 0 otherwise.

Since the degree of every vertex in the dual graph GK is (r − 1)(i + 2), then

(r − 1)(i + 2) r

∆up0 (GK).

∆downi+1 = (i + 2)I −

![image 118](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile118.png>)

![image 119](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile119.png>)

![image 120](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile120.png>)

![image 121](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile121.png>)

![image 122](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile122.png>)

- Remark 5.2. The eigenvalues of ∆downi+1 are non-negative, hence (i+ 2) −(r −


1)(i + 2)/rµn−k ≥ 0, and

r r − 1 ≥ µn, (5.2)

![image 123](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile123.png>)

where µn is the maximal eigenvalue of ∆up0 (GK). Inequality (5.2) is always satisﬁed for r = 2.

- 6. Constructions and their eﬀect on the spectrum: wedges, joins and duplication of motifs


- 6.1. Wedges Let (Xi)i∈I be a family of topological spaces and xi ∈ Xi, then the wedge


sum i Xi is the quotient of their disjoint union by the identiﬁcation xi ∼ xj,

- for all i, j ∈ I, i.e.


i

Xi :=

i

Xi / {xi ∼ xj | i, j ∈ I}.

For the purposes of this paper we deﬁne a combinatorial wedge sum, which is in many ways similar to the above wedge sum.

- Deﬁnition 6.1. For simplicial complexes K1 and K2 with vertex sets [n] and [m], respectively, and k-simplices F1 = {v0, . . ., vk} in Sk(K1) and F2 = {u0, . . ., uk} in Sk(K2), the combinatorial k-wedge sum of K1 and K2 is an abstract simplicial complex on the vertex set [m + n − k − 1], such that


k} ∈ K2}, where ui

, . . ., ui

, . . ., vi

k} ∈ K1 or if {ui

, . . ., vi

k} | {vi

K1 ∨k K2 := {{vi

0

0

0

for the other values of vi

:= ul if vi

= vl, ui

:= vi

+ k + 1 if vi

> n and ui

:= vi

j

j

j

j

j

j

j

. This deﬁnition generalizes in an obvious way to the k-wedge sum of arbitrary many simplicial complexes.

j

It is not diﬃcult to check that K1 ∨k K2 is a simplicial complex, too.

- Remark 6.1. The combinatorial wedge sum K1 ∨k K2 can also be viewed as K1 ⊔ K2 / {F1 ∼ F2},


where ∼ is an equivalence relation which identiﬁes the faces F1 and F2. The combinatorial k-wedge sum among graphs is a common notion in graph theory, although it is called by many diﬀerent names: the combinatorial 0wedge sum of graphs is also known as vertex amalgamation [19], coalescence [17] and join [2], whereas the combinatorial 1-wedge sum of graphs is called edge amalgamation.

Note that K1 ∨k K2, for arbitrary k, and the wedge sum of K1 and K2 as topological spaces have isomorphic homology groups. From the homological point of view it is impossible to distinguish among k-wedge sums for diﬀerent values of k as well as among diﬀerent choices of the base points. However, combinatorially, they are clearly diﬀerent, see e.g. the two wedge sums in Figure 3. Consequently, in a combinatorial k-wedge sum of simplicial complexes, it is important which complexes are identiﬁed as well as the dimension of these complexes. The following theorem gives the ﬁrst characterization of the eﬀect of the wedge sum on the spectrum of the Laplacian.

Theorem 6.1.

s(∆upi (K1 ∨k K2)) =◦ s(∆upi (K1)) ∪◦ s(∆upi (K2))

- for all i, k with 0 ≤ k < i.


Proof. Since K1 and K2 are identiﬁed by a face of dimension k, then obviously, Ci(K1 ∨k K2, R) = Ci(K1, R) ⊕ Ci(K2, R) for every i > k. Thus, the coboundary mapping δi : Ci(K1 ∨k K2, R) → Ci+1(K1 ∨k K2, R) will map Ci(Kj, R) to Ci+1(Kj, R), j = 1, 2 and the same holds for the adjoint δi∗.

![image 124](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile124.png>)

![image 125](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile125.png>)

![image 126](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile126.png>)

![image 127](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile127.png>)

![image 128](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile128.png>)

- Figure 3: The homology groups of the two spaces on the right are isomorphic, nonetheless these complexes are combinatorially diﬀerent.


The operator ∆upi is uniquely determined by the i and (i + 1)-faces of K. Hence its non-zero eigenvalues depend only on the structure of the (i + 1)faces of K. By abuse of notation, let Si+1(K) determine a pure (i + 1)dimensional subcomplex of K, whose facet set is Si+1(K). Then, there exist k1, . . ., km−1 < i, and simplicial complexes K1, . . ., Km, such that

Km, (6.1) i.e.

Si+1(K) = K1 ∨k1

K2 ∨k2

. . . ∨km−1

s(∆upi (K)) =◦ s(∆upi (K1)) ∪◦ . . . ∪◦ s(∆upi (Km)).

Therefore, when studying ∆upi , it is useful to determine if K can be represented as a combinatorial k-wedge sum of simplicial complexes and if so, how many of them there are. One possible way to answer this question is via the (i + 1)-dual graph of K. The number of complexes in the wedge sum (6.1) is exactly the number of connected components of the (i + 1)-dual graph of K. It is also equal to the number of (i + 1)-path connected components.

- Remark 6.2. If K is an (i+ 1)- path connected simplicial complex, it cannot be decomposed into a combinatorial k-wedge (k < i) of simplicial complexes.


We collect the above observations in the following proposition. Proposition 6.2. The following statements are equivalent.

- (i) Si+1(K) ∼= K1 ∨k1

K2 ∨k2

. . . ∨km−1

Km, where k1, . . ., km−1 < i and K1, . . ., Km are simplicial complexes.

- (ii) The (i + 1)-dual graph GK of K has m connected components.


- (iii) The number of (i + 1)-path connected components of K is equal to m.


The analysis on the combinatorial wedge sum above does not depend on the choice of the scalar products. Hence Theorem 6.1 and Proposition

- 6.2 hold for the general Laplace operator L as well. In the remainder of this section we investigate the eﬀect of the k-wedge sum for i = k on the spectrum of the (weighted) normalized combinatorial Laplacian ∆upi .


- Theorem 6.3. Let K1 and K2 be simplicial complexes, for which the spectra of ∆upi (K1) and ∆upi (K2) both contain the eigenvalue λ, and let f1, f2 be their corresponding eigenfunctions. If an i-wedge K := (K1 ∨i K2) is obtained by identifying i-faces F1 and F2, for which f1([F1]) = f2([F2]), then the spectrum of ∆upi (K) contains the eigenvalue λ, too. Proof. We will prove that


g([F]) =

- f1([F]) for every F which is an i-face of K1 diﬀerent from F1
- f2([F]) for every F which is an i-face of K2


is an eigenfunction of ∆upi (K) corresponding to the eigenvalue λ. For an i-dimensional face F of K1 diﬀerent from F1, the following equality holds

- ∆upi (K) |K1−F1 f1([F]) = λf1([F]).

Similar is true when F ∈ Si(K2), F = F2, i.e.

- ∆upi (K) |K2−F2 f2([F]) = λf2([F]).


Let wK

and wK

denote the weight functions on the complexes K1, K2 respec-

1

2

tively. Since we investigate ∆upi , the weights of the i-simplices are uniquely determined by the weights of the (i+1)-simplices and the incidence relations

among them. Thus, for the weight (degree) of the simplex F = F1 = F2, we have wK(F) = wK

(F1)+wK

(F2), whereas the weights of all other simplices

1

1

# from K1 or K2 will remain the same in K. Hence ∆upi (K)f([F]) =

1 wK1(F1) + wK2(F2) ¯

wK1(F¯)sgn([F],∂[F¯])f(∂[F¯])

![image 129](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile129.png>)

F∈Si+1(K1)

1 wK1(F1) + wK2(F2) ¯

wK2(F¯)sgn([F],∂[F¯])f2(∂[F¯])

+

![image 130](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile130.png>)

F∈Si+1(K2)

wK1(F1) wK1(F1) + wK2(F2)

1 wK1(F1) ¯

wK1(F¯)sgn([F],∂[F¯])f(∂[F¯])

=

![image 131](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile131.png>)

![image 132](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile132.png>)

F∈Si+1(K1)

1 wK2(F2) ¯

wK2(F2) wK1(F1) + wK2(F2)

wK2(F¯)sgn([F],∂[F¯])f2(∂[F¯])

+

![image 133](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile133.png>)

![image 134](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile134.png>)

F∈Si+1(K2)

wK2(F2) wK1(F1) + wK2(F2)

wK1(F1) wK1(F1) + wK2(F2)

λf1([F]) +

λf2([F])

=

![image 135](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile135.png>)

![image 136](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile136.png>)

= λf([F]).

![image 137](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile137.png>)

![image 138](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile138.png>)

![image 139](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile139.png>)

![image 140](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile140.png>)

This also includes the case when either f1 or f2 is identically equal to zero.

- Remark 6.3. The previous theorem will hold for the weighted normalized Laplacian if the weight function wK : k Sk(K) → R+ is


 

- wK1(F) if F is a face of K1 and dimF > i
- wK2(F) if F is a face of K2 and dimF > i


wK(F) =

wK1(F¯1) +

wK2(F¯2) if F is a face of K and dimF ≤ i

F ¯1∈K1: F∈∂F¯1

F ¯2∈K2: F∈∂F¯2



Example 6.1. Let σ1 be an i-simplex, then s(∆downi (σ)) =◦ s(∆upi−1(σ)) =◦ {i + 1}. A function which is equal to 1 on every oriented simplex in the

boundary of [σ] will be an eigenfunction of ∆downi corresponding to (i + 1). According to Theorem 6.3, an (i−1)-wedge of any number of i-simplices will possess the eigenvalue (i + 1), as long as we are able to orient them such that any two simplices whose intersection is of dimension i induce the same orientation on their intersecting face. For an alternative proof of this claim see Theorem 7.2.

Theorem 6.3 identiﬁes some of the eigenvalues of the combinatorial wedge sum. However, the results obtained by using the interlacing theorem for simplicial maps, as shown in the next theorem, are more comprehensive.

- Theorem 6.4. Let µ1, . . ., µm be the eigenvalues of ∆upi (K1∪K2) and λ1, . . ., λm−1 the eigenvalues of ∆upi (K), where K := (K1 ∨i K2), then


µi ≤ λi ≤ µi+1

- for every 0 ≤ i ≤ m − 1.


Proof. Let F1 and F2 be i-faces which are identiﬁed in an i-wedge sum K, and let f : K1 ∪ K2 → K1 ∨F1∼F2 K2 be a map, which identiﬁes the vertices of F1 with the vertices of F2, and is the identity on the remaining vertices of

- K1 ∪ K2. Furthermore, f is a simplicial map. The interlacing theorem for simplicial maps (see [22]) gives


µi ≤ λi ≤ µi+k, where k =| Si(K1 ∪ K2) | − | Si(K) |.

![image 141](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile141.png>)

![image 142](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile142.png>)

![image 143](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile143.png>)

![image 144](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile144.png>)

Thus the spectrum of ∆upi of the union of two simplicial complexes majorizes the spectrum of their i-wedge sum.

- Remark 6.4. The wedge sums of graphs and its eﬀect on the spectrum of the normalized graph Laplacian have already been analysed in [2], and the spectrum of the combinatorial graph Laplacian was analysed in [17]. These are special cases of the general theory presented here.


- 6.2. Joins


Let K1 and K2 be simplicial complexes on the vertex sets [n] and [m], respectively. The join K1 ∗ K2 is a simplicial complex on the vertex set [m + n], whose faces are F1 ∗ F2 := {v0, . . ., vk, n + u0, . . ., n + ul} , where

- F1 = {v0, . . ., vk} is a simplex in K1 and F2 = {u0, . . ., ul} a simplex in K2. The cochain groups of K1 ∗ K2 are


Ci

Ci(K1 ∗ K2, R) =

i1+i2+1=i

(K1, R) ⊗ Ci

(K2, R),

1

2

and the coboundary map δi is deﬁned as the graded derivation δi(f ⊗ g) = δf ⊗ g + (−1)|f|f ⊗ δg,

where f ⊗ g ∈ Ci(K1 ∗ K2, R) and |f| denotes the order of a cochain group which contains f.

A natural scalar product on a tensor product of Hilbert spaces is

(f1 ⊗ g1, f2 ⊗ g2) = (f1, f2)Ci1(K1)(g1, g2)Ci2(K2), (6.2) where f1, f2 ∈ Ci

(K1), g1, g2 ∈ Ci

(K2). A more general product is (f1 ⊗ g1, f2 ⊗ g2) = p(i1)(f1, f2)Ci1(K1)q(i2)(g1, g2)Ci2(K2), (6.3)

1

2

where p : {0, 1, . . ., dimK1} → R+ and q : {0, 1, . . ., dimK2} → R+ are positive, real valued functions. In terms of the weight functions, this is

(F2). (6.4) An elementary calculation yields

(F1)q(dimF2)wK

1∗K2(F1 ⊗ F2) = p(dimF1)wK

wK

2

1

p(|f|) p(|f|−1)

q(|g|) q(|g|−1)

δi∗(f ⊗ g) =

δ∗f ⊗ g +

(−1)|f|f ⊗ δ∗g. (6.5)

![image 145](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile145.png>)

![image 146](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile146.png>)

Then the following result holds.

- Theorem 6.5.


s((δi∗δi + δi−1δi∗−1)(K1 ∗ K2)) =◦

Pλ

λi∈s((δi∗1δi1+δi1−1δi∗1−1)(K1)) µj∈s((δi∗2δi2+δi2−1δi∗2−1)(K2))

λi + Qµ

i

where i1 + i2 + 1 = i, and

and

Proof.

p(i1 + 1)/p(i1) if λi ∈ s(Lupi1 (K1)), p(i1)/p(i1 − 1) if λi ∈ s(Ldowni1 (K1)),

 

Pλ

=

i



q(i2 + 1)/q(i2) if µj ∈ s(Lupi2 (K2)), q(i2)/q(i2 − 1) if µj ∈ s(Ldowni2 (K2)).

 

Qµ

=

j



µj, (6.6)

j

q(|g|) q(|g|−1)

p(|f|+1) p(|f|)

δ∗δf ⊗ g + (−1)|f|+1

δf ⊗ δ∗g (6.7)

δi∗δi(f ⊗ g) =

![image 147](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile147.png>)

![image 148](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile148.png>)

p(|f|) p(|f|−1)

q(|g|+1) q(|g|)

+ (−1)|f|

δ∗f ⊗ δg +

f ⊗ δ∗δg

![image 149](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile149.png>)

![image 150](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile150.png>)

q(|g|) q(|g|−1)

p(|f|) p(|f|−1)

δδ∗f ⊗ g + (−1)|f|

δf ⊗ δ∗g (6.8)

δiδi∗(f ⊗ g) =

![image 151](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile151.png>)

![image 152](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile152.png>)

q(|g|) q(|g|−1)

p(|f|) p(|f|−1)

δ∗f ⊗ δg +

f ⊗ δδ∗g

+ (−1)|f|−1

![image 153](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile153.png>)

![image 154](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile154.png>)

Addition of (6.7) and (6.8) gives

(δi∗δi + δiδi∗)(f ⊗ g) =

p(|f|+1) p(|f|) Lup|f|(K1) +

p(|f|) p(|f|−1)Ldown|f| (K1) f ⊗ g (6.9)

![image 155](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile155.png>)

![image 156](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile156.png>)

q(|g|+1) q(|g|) Lup|g|(K2) +

q(|g|)

q(|g|−1)Ldown|g| (K2) g. From the last equation we immediately deduce

+ f ⊗

![image 157](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile157.png>)

![image 158](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile158.png>)

s((δi∗δi + δi−1δi∗−1)(K1 ∗ K2)) =◦

Pλ

λi∈s(Li1(K1)) µj∈s(Li2(K2))

λi + Qµ

µj. (6.10)

i

j

![image 159](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile159.png>)

![image 160](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile160.png>)

![image 161](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile161.png>)

![image 162](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile162.png>)

- Remark 6.5. Proposition 4.9. in [11] treats the special case of Theorem 6.5 where the functions p and q are identically equal to 1. In that case, the eigenvalues of these complexes satisfy


s((δi∗δi + δi−1δi∗−1)(K1 ∗ K2)) =◦

λi + µj. (6.11)

λi∈s((δi∗1δi1+δi1−1δi∗1−1)(K1)) µj∈s((δi∗2δi2+δi2−1δi∗2−1)(K2))

In [11], it is assumed that the weight functions on the cochain spaces of K1 and K2 are equal to the identity, which yields the combinatorial Laplacian.

The next theorem provides necessary conditions on p and q for the Laplace operator deﬁned on K1 ∗ K2 to be normalized.

- Theorem 6.6. Let wK


and wK

be the weight functions on K1 and K2, resp., such that L(K1, wK

1

2

) and L(K2, wK

) are the normalized Laplace operators. Without loss of generality, assume dim K1 ≤ dim K2. If p(i + 1)/p(i) + q(j + 1)/q(j) = 1 for every i < dimK1 and j < dim K2, then s(Lupi (K1 ∗

1

2

- K2, pwK


qwK

)) ⊂ [0, i + 2], or in other words L(K1 ∗ K2, pwK

qwK

) is the normalized Laplacian.

1

2

1

2

Proof. We check for which values of p and q the weight function of a join K1 ∗ K2 satisﬁes the normalizing condition (3.7). For arbitrary F1 ∈ K1 and

- F2 ∈ K2, we have


deg F1 ⊗ F2 =

w(F)

F∈Si+1(K1∗K2): F1⊗F2∈∂F

wK1∗K2(F1 ⊗ F¯2)

wK1∗K2(F¯1 ⊗ F2) +

=

F ¯2:F2∈∂F¯2

F ¯1:F1∈∂F¯1

p(dimF¯1)wK1(F¯1)q(dimF2)wK2(F2)

=

F ¯1:F1∈∂F¯1

p(dimF1)wK1(F1)q(dimF¯2)wK2(F¯2)

+

F ¯2:F2∈∂F¯2

=p(dimF1 + 1)q(dim F2)deg F1wK2(F2) + p(dimF1)q(dimF2 + 1)deg F2wK1(F1)

=(p(dim F1 + 1)q(dimF2) + p(dimF1)q(dimF2 + 1))wK1(F1)wK2(F2) Thus, the weight function wK

1∗K2 satisﬁes (3.7) iﬀ

(p(i + 1)q(j) + p(i)q(j + 1)) = p(i)q(j), for every i, j.

![image 163](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile163.png>)

![image 164](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile164.png>)

![image 165](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile165.png>)

![image 166](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile166.png>)

The following corollary is a direct consequence of Theorem 6.6 and Theorem 6.5.

) and L(K2, wK

- Corollary 6.7. Let dimK1 = d1 and dim K2 = d2 and let L(K1, wK


1

, and denote L(K1 ∗ K2, wK

) be normalized Laplace operators. Assume wK

1∗K2 := wK

wK

2

1

2

1∗K2) by ∆(K1 ∗ K2), then s(∆downd

1+d2+1(K1 ∗ K2)) =◦

λi + µj, (6.12)

λi∈s(∆downd1 (K1)) µj∈s(∆downd2 (K2))

or equivalently

1+d2(K1 ∗ K2)) =◦

s(∆upd

λi + µj.

λi∈s(∆upd

- 1−1(K1)) µj∈s(∆upd
- 2−1(K2))


Proof. For F1 ∈ K1 and F2 ∈ K2 we have deg F1 ⊗ F2 =

(F¯1)wK

(F2) +

wK

2

1

F ¯1:F1∈∂F¯1

(F¯2).

(F1)wK

wK

2

1

F ¯2:F2∈∂F¯2

If neither F1 nor F2 is a facet of K1, K2, then the degree of F1 ⊗ F2 is 2wK

(F2). Therefore, (3.7) does not hold. Consequently, the Laplace operator determined by this function will not be the normalized Laplace operator of the join K1 ∗ K2. However, if F1 or F2 is a facet, then deg F1 ⊗ F2 = wK

(F1)wK

2

1

(F1)wK

(F2). Thus, wK

1∗K2 coincides with the weight function determining ∆upi (K1 ∗ K2), for i = d1 + d2 + 1. Together with (6.11), this yields (6.12).

1

2

![image 167](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile167.png>)

![image 168](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile168.png>)

![image 169](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile169.png>)

![image 170](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile170.png>)

As a direct consequence of Corollary 6.7 and the fact that s(∆up−1(K)) = {1} we get the following corollary. Corollary 6.8. If K is simplicial complex of dimension d, and v ∗K a cone over K, then

s(∆upd (v ∗ K)) =◦

1 + λi

λi∈s(∆upd−1(K))

- Remark 6.6 (Direct product of graphs). Direct products of graphs can be treated similarly as joins of simplicial complexes. The direct product of two graphs G1 and G2 is the simplicial complex G of dimension 1 with C1(G) = C1(G1) ⊗ C0(G2) ⊕ C0(G1) ⊗ C1(G2) and C0(G) = C0(G1) ⊗ C0(G2). Then, by applying the same principle as in Theorem 6.5, we obtain


p(1) p(0)

q(1) q(0)

s(Lup0 (G1 × G2)) =◦

λi +

µj,

![image 171](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile171.png>)

![image 172](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile172.png>)

λi∈s(Lup0 (G1)) µj∈s(Lup0 (G2))

where p(0), p(1) and q(0), q(1) are, as before, parameters of a scalar product. This was proven by Fiedler [13] for the special case when p = q ≡ 1 and by Grigoryan in [16] for the case of the normalized graph Laplacian for p, q with p(1)/p(0) + q(1)/q(0) = 1.

Note that the extension of the direct product to higher dimensions would lead to a cubical (instead of simplicial) complexes.

6.3. Duplication of motifs

Let K be a simplicial complex on the vertex set [n] and S a collection of simplices in K. The closure Cl S of S is the smallest subcomplex of K that contains each simplex in S. The star St S of S is the set of all simplices in K that have a face in S. The link lkS of S is Cl St S − St Cl S.

If the subcomplex Σ of K on the vertices v0, . . ., vk contains all of K’s faces on those vertices, then it is called a motif :

- Deﬁnition 6.2. A subcomplex Σ of a simplicial complex K is a k-motif iﬀ:

- (i) (∀F1, F2 ∈ Σ) F1, F2 ⊂ F ∈ K ⇒ F ∈ Σ
- (ii) dimlkΣ = k. In fact, as a consequence of Theorem 6.1 for i < k we obtain


s(∆upi (K)) =◦ s(∆upi (K − StΣ)) ∪◦ s(Cl StΣ). Therefore, it is meaningful to investigate the eﬀect of the duplication of a k-motif on the spectrum of ∆upi only if i = k. Remark 6.7. If K is an (i + 1)-path connected simplicial complex, then any motif satisfying (i) in Deﬁnition 6.2 will have a link of dimension i.

Let u0, . . ., um be vertices of lkΣ. By the deﬁnition of the link, these vertices are diﬀerent from those in the motif Σ (ui = vj, for every 0 ≤ i ≤ m and 0 ≤ j ≤ k). Let Σ′ denote a simplicial complex on the vertices v0′, . . ., vk′ , which is isomorphic to Σ. And let f : vi′  → vi be a simplicial isomorphism among these complexes. Then KΣ := K ∪ {{vi′

0

, . . ., vi′

l

, uj

1

, . . ., uj

s} | {vi

0

, . . ., vi

l

, uj

1

, . . ., uj

s} ∈ K}.

Proposition 6.9. KΣ is a simplicial complex and Cl St Σ is isomorphic to Cl St Σ′.

Proof. Elementary.

![image 173](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile173.png>)

![image 174](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile174.png>)

![image 175](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile175.png>)

![image 176](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile176.png>)

- Deﬁnition 6.3. We say that the simplicial complex KΣ is obtained from the simplicial complex K by the duplication of the i-motif Σ.


- Remark 6.8. It could be argued that it is Cl St Σ that we duplicate rather than Σ alone. This point of view will be very helpful in the sequel, but we will refer to duplication as the duplication of the motif Σ, since this is consistent with previous work on the duplication of motifs of graphs (see [2]).


Σ lkΣ

Σ‘

Σ lkΣ

Figure 4: Duplication of motif Σ

- Theorem 6.10. Let n be the number of i-simplices in St Σ. Then there exist n linearly independent functions f1, . . ., fn, satisfying


∆upi (K)fj([F]) = λjfj([F]),

for every F ∈ Si(St Σ) and some real values λj. The doubling of the motif Σ produces a simplicial complex KΣ with the eigenvalues λj and the eigenfunctions gj which agree with fj on StΣ and −fj on St Σ′ and are zero elsewhere.

Proof. It is trivial to check that ∆upi (Cl St Σ) and ∆upi (KΣ) coincide on St Σ. Let ∆upi (Cl St Σ) |St Σ be the restriction of the operator ∆upi (Cl St Σ) on St Σ. Let λ1, . . ., λn be the eigenvalues of ∆upi (Cl St Σ) |St Σ and f1, . . .fn the corresponding eigenfunctions. Then

 

fj([F]) for F inSt Σ −fj([F]) forF inSt Σ′ 0 otherwise

gj([F]) =



is an eigenfunction of ∆upi (KΣ) with eigenvalue λj. Without loss of generality, assume that the labelling of the vertices of Σ is v0, . . ., vk and the vertices of Σ′ is v0′, . . ., vk′ , and they are chosen such that v0 < . . . < vk < v0′, < . . . < vk′ . Enumerate the vertices of lkΣ with u1, . . ., um such that

v0 < . . . < vk < v0′, < . . . < vk′ < u1 < . . . < um. Then,

∆upi fj([F]) = ∆upi (Cl St Σ) |St Σ fj([F]) = λjfj([F]), and

∆upi (−fj)([F′]) = ∆upi (Cl St Σ) |St Σ −fj([F′]) = −λjfj([F′]),

for all F ∈ Si(Σ) and F′ ∈ Si(Σ′). Furthermore, assume that [u1, . . .ui+1] is a face of lkΣ, then

∆upi fj([u1, . . .ui+1]) =

(−1)1fj(∂[vj, u1, . . ., ui+1])

vj,[vj,u1,...,ui+1]∈Si+1(Cl St Σ)

(−1)1(−fj)(∂[vj′, u1, . . ., ui+1])

+

vj′ ,[vj′ ,u1,...,ui+1]∈Si+1 Cl St Σ′

= 0.

Since the functions fj are 0 on the boundary of those (i+1)-simplices that are neither in Cl St Σ nor in Cl St Σ′, we omit them from the discussion. Hence

the λj’s are the eigenvalues of ∆upi (KΣ). As a simple consequence of Theorem 6.10 we have the following corollary.

![image 177](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile177.png>)

![image 178](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile178.png>)

![image 179](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile179.png>)

![image 180](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile180.png>)

- Corollary 6.11. If the spectrum of the simplicial complex Cl St Σ contains the eigenvalue λ, with an eigenfunction f that is identically equal to zero on lkΣ, then the spectrum of KΣ will contain the eigenvalue λ as well.


Theorem 6.10 is an improved and generalized version of Theorem 2.3 from [2], which was stated for the case of the normalized graph Laplacian ∆up0 . The duplication of the motif Σ will leave a speciﬁc trace in the spectrum of the resulting simplicial complex KΣ. In particular, if λ1, . . ., λn are the eigenvalues of ∆upi (Cl St Σ) |St Σ, then after duplicating the motif Σ, m times, the spectrum of the resulting complex will contain (m−1) instances of every eigenvalue λj.

It is not always straightforward to calculate the eigenvalues of ∆upi (Cl St Σ) |St Σ; therefore we prove a theorem about interlacing of the λj and the eigenvalues µj of ∆upi (Cl StΣ). With the notation of Theorem 6.10, we have

- Theorem 6.12. The following inequality holds


µi ≤ λi ≤ µi+|S

i(lk Σ)|,

where | Si(lkΣ) | denotes the number of i-simplices in the link of a motif Σ. Proof. The matrix ∆upi (Cl St Σ) |St Σ is obtained from the matrix ∆upi (Cl StΣ) by deleting | Si(lkΣ) | rows and columns. Thus, the interlacing inequality follows directly from the Cauchy interlacing theorem.

![image 181](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile181.png>)

![image 182](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile182.png>)

![image 183](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile183.png>)

![image 184](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile184.png>)

- Remark 6.9. Theorem 6.10 and Corollary 6.11 will hold for any choice of the weight function satisfying (3.7).


7. Eigenvalues in the spectrum of ∆upi and the combinatorial properties they encode

One of the main advantages of the normalized combinatorial Laplace operator is the fact that the spectrum of any simplicial complex K is bounded from above by a constant. The eigenvalues of ∆upi (K) are in the interval [0, i+ 2]. As this is not the case for the spectrum of the combinatorial Laplacian L, or for any other known type of the combinatorial Laplace operator L, it seems impossible to assign combinatorial properties to the presence of a particular eigenvalue in the spectrum of L and L. Nonetheless, the global properties of the spectrum of Li relate to the combinatorial properties of the complex. For instance, the spectrum of certain combinatorially suitable complexes is proved to be integer (see [9],[11]).

Returning to the normalized Laplacian, the appearance of the eigenvalue 2 in the spectrum of the normalized graph Laplacian ∆up0 means that the underlying graph is bipartite (see [7]), while the eigenvalue 1 is produced by duplication of motifs (see [2]). In the following, we characterize some of the integer eigenvalues in the spectrum of ∆upi .

- 7.1. Eigenvalue i + 2


Without loss of generality assume K is an (i+1)-path connected simplicial complex on the vertex set [n]. As shown earlier, the following inequality holds

f(∂[F¯])2w(F¯) (7.1a)

(∆upi (K)f, f) =

F ¯∈Si+1(K)

f([F])2w(F). (7.1b)

≤(i + 2)

F∈Si(K)

The equality in (7.1b) is reached iﬀ there exists a function f ∈ Ci(K, R), which satisﬁes

sgn([Fj], ∂[F¯])f([Fj]) = sgn([Fk], ∂[F¯])f([Fk]),

for every F¯ in Si+1 and Fj, Fk ∈ ∂F¯. Thus |f([F])| must be constant for every F ∈ Si(K). Assume further that |f([F])|= 1, then for every F ∈ ∂F¯, f([F]) is equal either to sgn([F], ∂[F¯]) or to −sgn([F], ∂[F¯]). Now it is possible to consider f as a choice of orientation on the (i + 1)-faces of K.

- Theorem 7.1. The existence of a function f satisfying the equality in (7.1b) is equivalent to the existence of an orientation on the (i + 1)-simplices of K, for which any two (i + 1)-simplices intersecting in a common i-face induce the same orientation on the intersecting simplex (This condition is opposite to the condition of coherently oriented simplices).


- Theorem 7.2. For an i-connected simplicial complex K the following statements are equivalent


- 1. Spectrum ∆upi (K) contains the eigenvalue i + 2,
- 2. There are no (i + 1)-orientable circuits of odd length nor (i + 1)-non orientable circuits of even length in K.


Proof. (1) ⇒ (2) proceeds by contradiction: Assume that there exists an (i + 1)-orientable circuit of odd length, whose i-simplices F1, . . ., F2n+1 are ordered increasingly, as suggested in Deﬁnition 4.1. Then it is possible to orient these simplices in such a way that every two neighbouring simplices induce diﬀerent orientations on their intersecting face. Denote these oriented simplices by [F1], . . ., [F2n+1]. In order to have the same orientation induced on the intersecting face, we reverse the orientation of every simplex [Fk], for k even. Thus, [Fl] and −[Fl+1] induce the same orientation on [Fl ∩ Fl+1],

- for every 1 ≤ l ≤ 2n. However, [F1] and [F2n+1] remain coherently oriented, which contradicts Theorem 7.1. The analysis for the case of (i + 1)-nonorientable circuits is analogous.

(2) ⇒ (1): Let F1 be an arbitrary (i + 1)-face of K. Consider its positive orientation [F1] and call it an initial oriented face. Let [Fi

1i2...in] be an (i+1)face of K which shares an i-face with [Fi

1i2...in−1] and both faces induce the same orientation on their intersecting face. Now, assume the opposite: The eigenvalue i+2 is not in the spectrum of ∆upi , i.e. it is not possible to choose an orientation on the (i + 1)-faces of K, which satisﬁes the conditions of Theorem 7.1. This means that after some number of steps in the construction above, two faces [Fi

1i2...in], [Fi

1i2...im] which are the same, but diﬀerently oriented are obtained. Obviously, there exists a circuit containing [Fi

1i2...in], which does not admit an orientation as in Theorem 7.1. This is possible only in the case when a circuit is orientable and odd or non-orientable and even. This is a contradiction, hence i + 2 is contained in the spectrum of ∆upi .

![image 185](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile185.png>)

![image 186](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile186.png>)

![image 187](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile187.png>)

![image 188](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile188.png>)

The spectrum of the normalized graph Laplacian contains the eigenvalue

- 2 iﬀ the chromatic number of the underlying graph is 2. However, in general,


such a connection between the chromatic number and the boundary eigenvalue in the spectrum of the normalized combinatorial Laplace operator only holds in one direction.

Theorem 7.3. If the chromatic number of the 1-skeleton of the simplicial complex K is i + 2, then i + 2 is contained in s(∆upi (K)).

Proof. Let I0, . . ., Ii+1 be disjoint sets of vertices of K, such that every simplex of K contains at most one point of each set. Thus, there are no vertices of F¯ ∈ Si+1(K) which are contained in the same Ij. To avoid notational complications we relabel the vertices of K: instead of v ∈ Ij (v ∈ {1, . . ., n}) we write in + v. Therefore, we have

v ∈ Ij, u ∈ Ik and j < k ⇒ v < u.

The function f, deﬁned as f([v0, . . ., vˆj, . . ., vi+1]) = (−1)j ([v0, . . ., vi+1], is an (i + 1)-simplex of K whose vertices are ordered increasingly, i.e. v0 < . . . < vi+1) is the eigenfunction of ∆upi (K) corresponding to the eigenvalue i + 2, i.e.

f(∂[F¯]) deg F

∆upi f([F]) = F ¯:F∈∂F¯

![image 189](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile189.png>)

=(i + 2)f([F]).

![image 190](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile190.png>)

![image 191](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile191.png>)

![image 192](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile192.png>)

![image 193](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile193.png>)

- 7.2. Eigenvalues (i + 1) and 1 As a special case of Theorem 6.10 we consider a motif Σ consisting of


only one vertex.

- Corollary 7.4. When we duplicate an i- motif Σ consisting of one vertex which is the center of neither an (i+1)-orientable odd circuit nor an (i+1)non-orientable even circuit, then we produce the eigenvalue (i + 1) in the spectrum of KΣ.


Proof. Let v0 = Σ and let the 0-simplices of lkΣ be u1, . . ., uk. In Cl StΣ all (i + 1)-simplices must contain v1. Since v1 is neither a center of an (i + 1)orientable odd circuit nor a center of an (i + 1)-non-orientable even circuit,

by Theorem 7.2, i + 2 ∈ s(Cl St Σ). From Theorem 7.1, it follows that there is a function f ∈ Ci(Cl St Σ, R), s.t.

sgn([F1], ∂[F¯])f([F1]) = . . . = sgn([Fi+2], ∂[F¯])f([Fi+2]) for every F¯ ∈ Si+1(Cl St Σ) and each of its i-faces. Let g be a function which coincides with f on oriented i-faces of St Σ, with −f on oriented i-faces of St Σ′ and is zero elsewhere. We will now show that g is an eigenfunction of ∆upi (KΣ) associated to the eigenvalue (i + 1). Let F be an arbitrary i-face of St Σ, then

∆upi (ClStΣ) |St Σ g([F]) =

![image 194](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile194.png>)

=

![image 195](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile195.png>)

=

![image 196](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile196.png>)

=(i + 1)

1 w(F) ¯

sgn(F,∂F¯)g(∂[F¯])

F∈Si+1(Cl St Σ)

1 w(F) ¯

sgn([Fj],∂[F¯])f([Fj])

sgn([F],∂[F¯])

Fj∈∂F¯ Fj∈/lk Σ

F∈Si+1(Cl St Σ)

1 w(F) ¯

sgn([F],∂[F¯])(i + 1)sgn([F],∂[F¯])f([F])

F∈Si+1(Cl St Σ)

1 w(F) ¯

f([F])

![image 197](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile197.png>)

F∈Si+1(Cl St Σ)

=(i + 1).

# The same analysis holds for i-faces of StΣ′. Let F be an i-faces of Cl St Σ − St Σ, then

∆upi (ClStΣ) |St Σ f([F]) =

=

=

= 0,

# where Fj is a face of F¯.



1 w(F)

sgn([F],∂[F¯])g(∂[F¯])

![image 198](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile198.png>)

F ¯∈Si+1(Cl St Σ)

 

sgn([F],∂[F¯])g(∂[F¯])

+

F ¯∈Si+1(Cl St Σ′)



 

1 w(F)

g([Fj]) +

(i + 1)

g([Fj])

![image 199](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile199.png>)

F ¯∈Si+1(Cl St Σ)

F ¯∈Si+1(Cl St Σ′)

 

 

1 w(F)

f([Fj]) +

−f([Fj])

(i + 1)

![image 200](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile200.png>)

Fj′∈Si(St Σ′)

Fj∈Si(St Σ)

![image 201](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile201.png>)

![image 202](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile202.png>)

![image 203](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile203.png>)

![image 204](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile204.png>)

This theorem is a generalization of the vertex doubling eﬀect on the normalized graph Laplacian ∆up0 discussed in [2].

In the graph case, the eigenvalue 1 plays a very important role, since its multiplicity is usually signiﬁcantly higher than other eigenvalues in graphs obtained from real world data, see [3]. For the Laplace operator on higher dimensional simplicial complexes, the role of the eigenvalue 1 is partially transferred to the eigenvalue (i + 1) in higher dimensions, as shown above. Nevertheless, the next theorem gives a characterization of the eigenvalue 1 in the spectrum of ∆upi .

Theorem 7.5. Let K be a simplicial complex with an eigenvalue i+2 in the spectrum of ∆upi and let GiK be its i-dual graph. Then,

1 ∈ s(∆up0 (GiK)) ⇔ 1 ∈ s(∆upi (K)).

Proof. The multiplicity of the eigenvalue 1 in the spectrum of ∆upi (K) is equal to the dimension of the kernel of the adjacency matrix Aupi of the i-faces of K. Its entries are

sgn([F], ∂[F¯]) sgn([F′], ∂[F¯]) F, F′ are (i + 1)-up neighbours 0 otherwise

(Aupi )[F],[F′] =

Due to Theorem 7.1, it is possible to orient the (i + 1)-simplices of K such that sgn([F], ∂[F¯]) sgn([F′], ∂[F¯]) is always positive. Consequently, all entries of the matrix Aupi will be positive. The adjacency matrices of GiK and Aupi are the same, hence the dimension of the kernel of Aupi is equal to the multiplicity of the eigenvalue 1 in the spectrum of the normalized graph Laplacian of the graph GiK.

![image 205](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile205.png>)

![image 206](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile206.png>)

![image 207](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile207.png>)

![image 208](<2011-horak-spectra-combinatorial-laplace-operators_images/imageFile208.png>)

Acknowledgements

We thank Frank Bauer and Johannes Rauh for useful suggestions. This work was supported by a PhD fellowship of the International Max-Plank Research School ”Mathematics in the Sciences” for the ﬁrst author. The second author was supported by the ERC Advanced Grant FP7-267087 and the Volkswagen Foundation.

References

- [1] W. N. Anderson and T. D. Morley. Eigenvalues of the Laplacian of a graph. Linear and Multilinear Algebra, 18(2):141–145, 1985.


- [2] A. Banerjee and J. Jost. On the spectrum of the normalized graph Laplacian. Linear Algebra Appl, 428(11-12):3015–3022, June 2008.
- [3] A. Banerjee and J. Jost. Graph spectra as a systematic tool in computational biology. Discrete Appl. Math, 157(10):2425–2431, May 2009.
- [4] O. Bottema. Uber¨ die Irrfahrt in einem Straßennetz. Math. Z, 39(ISSN 1432-1823):137–145, 1935.
- [5] F Chung. The Laplacian of a hypergraph. Expanding graphs: Proc. DIMACS Ser. Discrete Math. Theoret. Comput. Sci, pages 21–36, 1993.
- [6] F Chung. A Combinatorial Laplacian with Vertex Weights. J. Combin. Theory Ser. A, 75(2):316–327, August 1996.
- [7] F. R. K. Chung. Spectral Graph Theory (CBMS Regional Conference Series in Mathematics, No. 92). American Mathematical Society, 1996.
- [8] P. M. Cohn. Basic Algebra. Springer, 2002.
- [9] X. Dong and M.L. Wachs. Combinatorial Laplacian of the matching complex. Electron. J. Combin, 9(1):1–11, 2002.
- [10] A. M. Duval, C. J. Klivans, and J. L. Martin. Simplicial matrix-tree theorems. Trans. Amer. Math. Soc., 361(11):6073–6114, June 2009.
- [11] A.M. Duval and V. Reiner. Shifted simplicial complexes are Laplacian integral. Trans. Amer. Math. Soc., 354(11):4313–4344, 2002.
- [12] B. Eckmann. Harmonische Funktionen und Randwertaufgaben in einem Komplex. Comment. Math. Helv., 17(1):240–255, December 1944.
- [13] M. Fiedler. Algebraic Connectivity of Graphs. Czechoslovak Math. J, 23(2):298–305, 1973.
- [14] Joel Friedman. Computing betti numbers via combinatorial laplacians. In In Proc. 28th Ann. ACM Sympos. Theory Comput, pages 386–391, 1996.
- [15] J. V. Greenman. Symmetry , graphs and eigenvalues. The Mathematical Gazette, 61(417):195–200, 1977.


- [16] A. Grigoryan. Analysis on Graphs, Lecture Notes. University of Bielefeld,, 2009.
- [17] R. Grone and R. Merris. Coalescence, majorization, edge valuations and the laplacian spectra of graphs. Linear and Multilinear Algebra, 27(2):139–146, May 1990.
- [18] R. Gronef and R. Merris. Laplacian spectrum of a graph. SIAM J. Matrix Anal. Appl., 11(2):218–238, 1990.
- [19] Jonathan L. Gross and Thomas W. Tucker. Topological graph theory. Courier Dover Publications, 2001.
- [20] A. Hatcher. Algebraic Topology. Cambridge University Press, 2002.
- [21] A.N. Hirani. Discrete Exterior Calculus. PhD thesis, California Institute of Technology, Pasadena, California, May 2003.
- [22] D. Horak. Interlacing theorems for normalized combinatorial Laplacian of simplicial complexes. in preparation, 2011.
- [23] G. Kirchhoﬀ. Uber¨ die Auﬂo¨sung der Gleichungen, auf welche man bei der Untersuchung der linearen Verteilung galvanischer Stro¨me gef¨uhrt wird. Ann. Phys. Chem., 72:497–508, 1847.
- [24] D. Kozlov. Combinatorial Algebraic Topology. Springer, 2007.
- [25] L. Lu and X. Peng. High-ordered random walks and generalized laplacians on hypergraphs. In In Proc. Algorithms and Models for the WebGraph, 2011.
- [26] R. Merris. Laplacian matrices of graphs: a survey. Linear Algebra Appl., 197-198:143–176, January 1994.
- [27] F Meunier. Combinatorial Stokes formulae. European J. Combin, 29(1):286–297, January 2008.
- [28] B. Mohar. The Laplacian spectrum of graphs. Graph theory, combinatorics, and applications, 2:871–898, 1991.
- [29] A. Muhammad and M. Egerstedt. Control Using Higher Order Laplacians in Network Topologies. Mathematical Theory of Networks and Systems, Kyoto, Japan, pages 1024–1038, 2006.


- [30] A. Tahbaz-Salehi and A. Jadbabaie. Distributed Coverage Veriﬁcation in Sensor Networks Without Location Information. IEEE Trans. Automat. Contro, 55(8):1837–1849, 2010.
- [31] C. Taszus. Higher order Laplace Beltrami Spectra of Networks. Master’s thesis, FriedrichSchillerUniversitt Jena Fakultt fr Mathematik und Informatik, 2010.


