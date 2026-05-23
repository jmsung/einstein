arXiv:1301.1028v2[math.CO]14Jan2013

Ramanujan Complexes and High Dimensional Expanders∗

Alexander Lubotzky

Einstein Institute of Mathematics Hebrew University Jerusalem 91904 ISRAEL alex.lubotzky@mail.huji.ac.il

Abstract

Expander graphs in general, and Ramanujan graphs in particular, have been of great interest in the last three decades with many applications in computer science, combinatorics and even pure mathematics. In these notes we describe various eﬀorts made in recent years to generalize these notions from graphs to higher dimensional simplicial complexes.

# Contents

- 0 Introduction 2
- 1 Ramanujan Graphs 3

- 1.1 Eigenvalues and expanders . . . . . . . . . . . . . . . . . . . . . . 3
- 1.2 Bruhat-Tits trees and representation theory of PGL2 . . . . . . . 6
- 1.3 Explicit constructions . . . . . . . . . . . . . . . . . . . . . . . . 8


- 2 Ramanujan complexes 11

- 2.1 Bruhat-Tits buildings and Hecke operators . . . . . . . . . . . . 11
- 2.2 Representation theory of PGLd . . . . . . . . . . . . . . . . . . . 14
- 2.3 Explicit construction of Ramanujan complexes . . . . . . . . . . 16


- 3 High dimensional expanders 19


- 3.1 Simplicial complexes and cohomology . . . . . . . . . . . . . . . 19
- 3.2 F2-coboundary expansion . . . . . . . . . . . . . . . . . . . . . . 20


![image 1](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile1.png>)

∗This paper is based on notes prepared for the Takagi Lectures, Tokyo 2012.

- 3.3 The Cheeger constant . . . . . . . . . . . . . . . . . . . . . . . . 22
- 3.4 Spectral gap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- 3.5 The overlap property . . . . . . . . . . . . . . . . . . . . . . . . . 25


# 0 Introduction

Expander graphs are highly connected ﬁnite sparse graphs. These graphs play a fundamental role in computer science and combinatorics (cf. [Lub94, HLW06], and the references within) and in recent years even found numerous applications in pure mathematics ([Lub12]). Among these graphs, Ramanujan graphs stand out as optimal expanders (at least from the spectral point of view). The theory of expanders and Ramanujan graphs has led to a very fruitful interaction between mathematics and computer science (and between mathematicians and computer scientists). In the early days, deep mathematics (e.g. Kazhdan property (T) and Ramanujan conjecture) has been used to construct expanders and Ramanujan graphs. But recently, the theory of computer science pays its debt to mathematics and expanders start to appear more and more also within pure mathematics.

The fruitfulness of this theory calls for a generalization to high dimensional theory. Here the theory is much less developed. The goal of these notes is to describe some of these eﬀorts and to call the attention of the mathematical and computer science communities to this challenge. We strongly believe that a beautiful and useful theory is waiting for us to be explored.

Most of the notes will be dedicated to the story of Ramanujan complexes. These generalizations of Ramanujan graphs, which has been developed in [CSŻ03, Li04, LSV05a, LSV05b, Sar07] became possible by the signiﬁcant development of the theory of automorphic forms in positive characteristic and especially the work of L. Laﬀorgue [Laf02]. In §1, we will describe the classical theory of Ramanujan graphs, in a way which will pave the way for a smooth presentation in §2, of the much more complicated theory of Ramanujan complexes.

The situation with high dimensional expanders is more chaotic. Here it is not even agreed what should be the “right” deﬁnition. Several generalizations of the concept of expander graph have been suggested, which are not equivalent. It is not clear at this point which one is more useful. Each has its own charm and part of the active research on this subject is to understand the relationships between the various deﬁnitions.

We describe these activities brieﬂy in §3. It can be expected (and, in fact, I hope!) that these notes will not be up to date by the time they will appear in press...

Acknowledgement. The author is indebted to Konstantin Golubev, Gil Kalai, Tali Kaufman, Roy Meshulam and Uli Wagner for many discussions regarding the material of these notes. I am especially grateful to Ori Parzanchevski, whose help and advice in preparing these notes have improved them signiﬁcantly.

This work was supported by ERC, ISF and NSF. Some of this work was carried out while the author visited Microsoft Research laboratory in Cabridge, Ma. We are grateful for the warm hospitality and support. We are also grateful for the Mathematical Society of Japan for the invitation to deliver the Takagi lectures, the hospitality and the valuable remarks we received from the audience.

# 1 Ramanujan Graphs

In this chapter we will survey Ramanujan graphs, which are optimal expanding graphs from a spectral point of view. The material is quite well known by now and has been described in various places ([LPS88, Sar90, Lub94, Val97]). We present it here in a way which will pave the way for the high dimensional generalization - the Ramanujan complexes - which will come in the next chapter.

- 1.1 Eigenvalues and expanders


Let X = (V,E) be a ﬁnite connected k-regular graph, k ≥ 3, with a set V of n vertices, and adjacency matrix A = AX, i.e. A is an n × n matrix indexed by the vertices of X and Aij is equal to the number of edges between i and j (which is either 0 or 1 if X is a simple graph).

Deﬁnition 1.1.1. The graph X is called Ramanujan if for every eigenvalue λ of the symmetric matrix A, either λ = ±k (“the trivial eigenvalues”) or |λ| ≤ 2√k − 1.

![image 2](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile2.png>)

Recall that k is always an eigenvalue of A (with the constant vector/function as an eigenfunction) while −k is an eigenvalue of A iﬀ X is bi-partite, i.e. the vertices of X can be divided into two disjoint sets Y and Z and every edge e in E, has one endpoint in Y and one in Z. In this case, the eigenfunction is 1 on Y and −1 on Z.

Ramanujan graphs have been deﬁned and constructed in [LPS88] (see also [Mar88] and see [Sar90, Lub94, Val97] for more comprehensive treatment). The importance of the number 2√k − 1 comes from Alon-Boppana Theorem which asserts that for any ﬁxed k, no better bound can be obtained on the non-trivial eigenvalues of an inﬁnite sequence of ﬁnite k-regular graphs.

![image 3](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile3.png>)

Theorem 1.1.2 (Alon-Boppana (cf. [LPS88, Nil91])). For a ﬁnite connected k-regular graph X, denote

µ1 (X) = max{λ| λ an eigenvalue of A and λ = k} µ0 (X) = max{|λ||λ an eigenvalue of A and λ = k}

µ(X) = max{|λ||λ an eigenvalue of A and λ = ±k}. If {Xi}∞i=1 is a sequence of such graphs with |Xi| → ∞, then liminf i→∞

√

![image 4](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile4.png>)

µ(Xi) ≥ 2

k − 1.

The hidden reason for the number 2√k − 1 is: All the ﬁnite connected k-regular graphs are covered by the k-regular tree, T = Tk. Let AT be the adjacency operator of T, i.e., for every function f on the vertices of T and for every vertex x of it,

![image 5](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile5.png>)

AT (f)(x) =

f (y)

y∼x

namely, AT sums f over the neighbors of x. Then AT deﬁnes a self adjoint operator L2 (T) → L2 (T).

Proposition 1.1.3 ([Kes59]). The spectrum of AT is −2√k − 1,2√k − 1 .

![image 6](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile6.png>)

![image 7](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile7.png>)

Of course, k is not an eigenvalue of AT as the constant function is not in L2. It is even not in the spectrum (unless k = 2, in which case Tk is a Cayley graph of the amenable group Z, but this is a diﬀerent story). But, k is necessarily an eigenvalue for all the adjacency operators induced on the ﬁnite quotients Γ\T, where Γ is a discrete cocompact subgroup of Aut(T). Similarly, −k is an eigenvalue of the ﬁnite quotient Γ\T if it is bi-partite (which happens if Γ = π1 (Γ\T) preserves the two-coloring of the vertices of T). Now, Ramanujan graphs are the “ideal objects” having their non-trivial spectrum as good as the “ideal object” T.

There is another way to characterize Ramanujan graphs. These are the graphs which satisfy the “Riemann hypothesis”, i.e. all the poles of the Ihara zeta function associated with the graph lie on the line ℜ(s) = 12. See [Lub94, §4.5] and especially the works of Ihara [Iha66], Sunada [Sun88] and Hashimoto [Has89].

![image 8](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile8.png>)

The work of Ihara showed the close connection between number theoretic questions and the combinatorics of some associated graphs. While it was Satake [Sat66] who showed how the classical Ramanujan conjecture can be expressed in a representation theoretic way. These works have paved the way to the explicit constructions of Ramanujan graphs to be presented in §1.2 and §1.3.

Ramanujan graphs have found numerous applications in combinatorics, computer science and pure mathematics. We will not describe these but rather refer the interested readers to the thousands references appearing in google scholar when one looks for Ramanujan graphs.

We should mention however their main application and original motivation: expanders.

Deﬁnition 1.1.4. For X a k-regular graph on n vertices, denote:

n · |E (A,V \A)| |A||V \A|

h (X) = min

![image 9](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile9.png>)

0<|A|<|V |

where E (A,V \A) is the set of edges from A to its complement. We call h (X) the Cheeger constant of X.

- Remark 1.1.5. In most references, the Cheeger constant is deﬁned as


|E (A,V \A)| |A|

![image 10](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile10.png>)

.

h(X) = min

![image 11](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile11.png>)

0<|A|≤|V |/2

Clearly h (X) ≤ h (X) ≤ 2h (X). For our later purpose, it will be more convenient to work with h (X).

![image 12](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile12.png>)

![image 13](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile13.png>)

- Deﬁnition 1.1.6. The graph X is called ε-expander (for 0 < ε ∈ R) if h (X) ≥ ε.


Expander graphs are of great importance in computer science. Ramanujan graphs give outstanding expanders due to the following result:

- Theorem 1.1.7 ([Tan84, Dod84, AM85, Alo86]). For X as above,


h2 (X)

8k ≤ k − µ1 (X) ≤ h (X). In particular, Ramanujan k-regular graphs are ε-expanders with ε = k−2√k − 1 (or if one prefers the more standard notation h (X) ≥ k2 −

![image 14](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile14.png>)

![image 15](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile15.png>)

√k − 1).

![image 16](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile16.png>)

![image 17](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile17.png>)

![image 18](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile18.png>)

- A very useful result in many applications is the following Expander Mixing Lemma:

- Proposition 1.1.8. For X = (V,E) as above and for every two subsets A and


- B of V ,


k |A||B| |V |

![image 19](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile19.png>)

≤ µ0 (X) |A||B|.

E (A,B) −

![image 20](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile20.png>)

Note that k|A|V|||B| is the expected number of edges between A and B if X would be a “random k-regular graph”. So, if µ0 (X) is small, e.g. if X is Ramanujan, it mimics various properties of random graphs. This is one of the characteristics which make them so useful.

![image 21](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile21.png>)

There is no easy method to construct Ramanujan graphs. Let us better be more precise here: There are many ways to get for a ﬁxed k ﬁnitely many k-regular Ramanujan graphs (see [Lub94, Chapter 8]), but there is essentially only one known way to get, for a ﬁxed k, inﬁnitely many k-regular Ramanujan graphs. The current state of the art is, that for every k ∈ N of the form k = pα+1 where p,α ∈ N and p prime, there are inﬁnitely many k-regular Ramanujan graphs but for all other k’s this is still open:

Open Problem 1.1.9. Given k which is not of the form pα + 1, are there inﬁnitely many k-regular Ramanujan graphs?

We stress that this problem is open for every single k like that (e.g. k = 7) and it is not known if such graphs exist, let alone an explicit construction.

In the next subsection we will describe the Bruhat-Tits tree and present the basic theory that will enable us in the following subsection to get explicit constructions of Ramanujan graphs.

- 1.2 Bruhat-Tits trees and representation theory of PGL2


- Let F be a local ﬁeld (e.g. F = Qp the ﬁeld of p-adic numbers, or a ﬁnite extension of it, or F = Fq ((t)) the ﬁeld of Laurent power series over the ﬁnite ﬁeld Fq) with ring of integers O (e.g. O = Zp or O = Fq [[t]]), maximal ideal


- m = πO where π is a ﬁxed uniformizer, i.e., an element of O with valuation ν (π) = 1 (e.g. π = p or π = t, respectively), so k = O/m is a ﬁnite ﬁeld of order


q. Let G = PGL2 (F) and K = PGL2 (O), a maximal compact subgroup of G. The quotient space G/K is a discrete set which can be identiﬁed as the set of vertices of the regular tree of degree q + 1 in the following way:

Let V = F2 be the two dimensional vector space over F. An O-submodule L of V is called an O-lattice if it is ﬁnitely generated as an O-module and spans V

over F. Every such L is of the form L = Oα+Oβ where {α,β} is some basis of V over F. The standard lattice is the one with {α,β} = {e1,e2}, where {e1,e2} is the standard basis of V .

Two O-lattices L1 and L2 are said to be equivalent if there exists 0 = λ ∈ F such that L2 = λL1. The group GL2 (F) acts transitively on the set of Olattices and its center Z, the group of scalar matrices, preserves the equivalent classes. Hence G = PGL2 (F) acts on these classes, with K = PGL2 (O) ﬁxing the equivalent class of the standard lattice x0 = [L0], L0 = Oe1 + Oe2. So, G/K can be identiﬁed with the set of equivalent classes of lattices. Two classes [L1] and [L2] are said to be adjacent if there exists representatives L′1 ∈ [L1] and L′2 ∈ [L2] such that L′1 ⊆ L′2 and L

′

2/L′1 ≃ k (= O/m). This symmetric relation (since πL′2 ⊆ L′1 and L′1/πL′2 ≃ k) deﬁnes a structure of a graph.

- Theorem 1.2.1 (cf. [Ser80, p. 70]). The above graph is a (q + 1)-regular tree.


The q + 1 neighbors of [L0] correspond to the q + 1 subspaces of co-dimension 1 of the two dimensional space L0/πL0 ∼= k2. We can therefore identify them with P1 (k), the projective line over k.

Let us now shift our attention for a moment to the unitary representation theory of G. Let C = Cc (K\G/K) denote the set of bi-K-invariant functions on G with compact support. This is an algebra with respect to convolution:

f1 ∗ f2 (x) = ˆ

G

f1 (xg)f2 g−1 dg.

The algebra C is commutative (see [Lub94, Chapter 5] and the references therein). If H is a Hilbert space and ρ : G → U (H) a unitary representation of G, then ρ induces a representation ρ of the algebra C by:

![image 22](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile22.png>)

ρ(f) = ˆ

![image 23](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile23.png>)

G

f (g)ρ(g)dg.

Let HK be the space of K-invariant vectors in H. Then ρ(f) HK ⊆ HK and so HK,ρ is a representation of C. A basic claim is that if ρ is irreducible and HK = {0} then ρ is irreducible, in fact, as C is commutative Schur’s Lemma

![image 24](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile24.png>)

![image 25](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile25.png>)

![image 26](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile26.png>)

implies that dimHK = 1. So dimHK = 0 or 1, in the second case we say that ρ is K-spherical (or unramiﬁed or of class one). We will be interested only in these representations. Such a representation ρ is uniquely determined by ρ. Let us understand now what is the algebra C.

![image 27](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile27.png>)

Let δ be the characteristic function of the subset K (π0 01)K of G. By its deﬁnition δ ∈ C. In fact, it turns out that C is generated as an algebra by δ and hence every K-spherical irreducible subrepresentation (H,ρ) of G is determined by the action of δ on the one dimensional space HK, i.e. by the eigenvalue of this action.

![image 28](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile28.png>)

![image 29](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile29.png>)

![image 30](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile30.png>)

![image 31](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile31.png>)

Let us note now that C also acts on L2 (G/K) in the following way: If f1 ∈ C and f2 ∈ L2 (G/K) we think of both as functions on G and we can then look at f2 ∗ f1 ∈ L2 (G/K) (check!)

Spelling out the meaning of that for f1 = δ, one can see (the reader is strongly encouraged to work out this exercise!):

![image 32](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile32.png>)

Claim 1.2.2. Let f be a function deﬁned on the vertices of the tree G/K and let δ be the operator δ : L2 (G/K) → L2 (G/K) deﬁned by δ (f) = f ∗ δ. Then for every x ∈ G/K

![image 33](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile33.png>)

δ (f)(x) =

f (y).

y∼x

Namely, δ is nothing more then the adjacency operator (whose name in the classical literature is Hecke operator).

Let now Γ be a cocompact discrete subgroup of G = PGL2 (F) (for simplicity assume also that Γ is torsion free). Then Γ\G/K is, on one hand a quotient of the (q + 1)-regular tree and, on the other hand, a quotient of the compact space Γ\G. Hence, this is nothing more than a ﬁnite (q + 1)-regular graph. Moreover, the discussion above shows that the spectral decomposition of the adjacency matrix of this ﬁnite graph (and in particular its eigenvalues) is intimately connected with the spectral decomposition of L2 (Γ\G) as a unitary G-representation. More precisely, in every irreducible K-spherical subrepresentation ρ of L2 (Γ\G), there is a K-invariant function f, i.e. a function in L2 (Γ\G/K). As explained above the one dimensional space spanned by f is a representation space ρ for C, which means that f is an eigenvector for the adjacency operator δ of the ﬁnite graph Γ\G/K. Moreover, every eigenvector f of δ in L2 (Γ\G/K) is obtained like that (we can look at the G-subspace spanned by f, thinking of it as a K-invariant function in L2 (Γ\G).)

![image 34](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile34.png>)

The list of K-spherical irreducible unitary representations of PGL2 (F) is well known (see [Lub94, Theorem 5.4.3] and the references therein). There are representations of two kinds:

- (a) The tempered representations - these are the K-spherical irreducible representations (H,ρ) with the following property: There exists 0 = u,v ∈ H such that φ : G → C deﬁned by φ(g) = ρ(g)u,v (the coeﬃcient function of ρ w.r.t. u and v) is in L2+ε (G) for every ε > 0. The K-spherical


- representations with this property are also called in this case “the principal series” and they are characterized by the property that the associated eigenvalue λ of δ (as a generator of C acting on the one dimensional space HK) satisﬁes |λ| ≤ 2√q.
- (b) The non-tempered representations - these are the representations for which the above λ satisﬁes 2√q < |λ| ≤ q + 1 .


![image 35](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile35.png>)

![image 36](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile36.png>)

The above description explains why and how the representation of G = PGL2 (F) on L2 (Γ\G) is crucial for understanding the combinatorics of the graph Γ\G/K. In fact we have (see [Lub94, Corollary 5.5.3]:

- Theorem 1.2.3. Let Γ be a cocompact lattice in G = PGL2 (F). Then Γ\G/K is a Ramanujan graph if and only if every irreducible K-spherical Gsubrepresentation of L2 (Γ\G) is tempered, with the exception of the trivial representation (which corresponds to λ = q+1) and the possible exception of the sign representation (the non trivial one dimensional representation sg : G → {±1}) which corresponds to λ = − (q + 1) and which appears in L2 (Γ\G) iﬀ Γ\G/K is bipartite.


Proving that Γ’s as in the last theorem indeed exist is a highly nontrivial issue which we discuss in the next section. This will lead to (explicit) constructions of Ramanujan graphs.

- Remark 1.2.4. In case Γ is a non-uniform lattice in G = PGL2 (F) (which exists only if char(F) > 0) one can develop also a theory of Ramanujan diagrams (cf. [Mor94b]) which is also of interest even for computer science (see [Mor95]).


- 1.3 Explicit constructions


In this section we will quote the deep results which imply that various graphs are Ramanujan and then we will show how to use them to get explicit constructions of such graphs.

Let k be a global ﬁeld, i.e. k is a ﬁnite extension of Q or of Fp (t). Let O be the ring of integers of k, S a ﬁnite set of valuations of k (containing all the archimedean ones if char(k) = 0) and OS the ring of S-integers (= {x ∈ k |ν (x) ≥ 0,∀ν ∈/ S}). Let G be a k-algebraic semisimple group with a ﬁxed embedding G ֒→ GLm. A general result asserts that

Γ = G (OS) := G (k) GLm (OS) is a lattice (= discrete subgroup of ﬁnite covolume) in

G (kν) where kν is the completion of k w.r.t. the valuation ν. In some cases (few of these will be described below) G (kν) is compact for every ν ∈ S except of one ν0 ∈ S. In such a case the projection of Γ to G (kν

ν∈S

), which is also denoted by Γ, is called

0

). The arithmetic lattice Γ comes with a system of congruence subgroups deﬁned for every 0 = I ⊳ OS as:

an arithmetic lattice in G (kν

0

Γ(I) = Γ ker(GLm (OS) → GLm (OS/I)). If G (kν

) ≃ PGL2 (F) (or more generally PGLd (F) - see Chapter 2) where F is a local ﬁeld as in §1.2, we get the arithmetic groups we are interested in. We can now state:

0

- Theorem 1.3.1. Let Γ(I)⊳Γ be a congruence subgroup of an arithmetic lattice


Γ of G = PGL2 (F) as above. Then every inﬁnite dimensional K-spherical irreducible subrepresentation of L2 (Γ(I)\G) is tempered.

The only possible ﬁnite dimensional K-spherical representations are the trivial one and the sg representation. From Theorem 1.2.3 we can now deduce:

Corollary 1.3.2. The graph Γ(I)\G/K is Ramanujan.

- Theorem 1.3.1 is a very deep result whose proof is a corollary of various works by some of the greatest mathematicians of the 20th century. It is based in particular on the solution of the so called “Peterson-Ramanujan conjecture”. (In characteristic 0, in two steps: by Eichler for weight two modular forms which is the relevant case for us, and by Deligne in general. In positive characteristic by Drinfeld). Then one needs to combine it with the Jacquet–Langlands correspondence. The reader is referred to [Lub94] for more and in particular to the Appendix there by J. Rogawski which gives the general picture.


The last result give explicit graphs in the mathematical sense of explicit, but it also paves the way for an explicit construction, in the computer science sense, of Ramanujan graphs. We will present the ones constructed in [LPS88].

When G = PGL2 (F), all the arithmetic lattices in G are obtained via quaternion algebras. Namely, let D be a quaternion algebra deﬁned over k and G = D×/Z, i.e. the invertible quaternions modulo the central ones. If D splits over ν0 ∈ S (i.e. D ⊗ kν

)) while it is ramiﬁed over all ν ∈ S\ {ν0} (i.e. D ⊗ kν is a division algebra in which case (D⊗kν)×/Z(D⊗kν) is a compact group) then G (OS) gives rise to an arithmetic lattice in G (kν

0 ≃ M2 (kν

0

). Such lattices (and their congruence subgroups) can be used for the construction of arithmetic lattices.

) = PGL2 (kν

0

0

Let us take a very concrete example: Let D be the classical Hamilton quaternion algebra; so D is spanned over Q by 1,i,j and k with i2 = j2 = k2 = −1 and ij = −ji = k. It is well known that it is ramiﬁed over R and over Q2 while splits over Qp for every odd prime p, and that G (R) = H×/R× ≃ SO(3) while G (Qp) = M2(Qp)×/Q×p ≃ PGL2 (Qp). Fix such a prime p and set S = {νp,ν∞}. Then OS = Z p 1 = p an a ∈ Z,n ∈ N , and as explained above, D Z p 1 is a discrete subring of D (R) × D (Qp), while

![image 37](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile37.png>)

![image 38](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile38.png>)

![image 39](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile39.png>)

])×/Z ֒→ SO (3) × PGL2 (Qp)

Γ = D(Z[

1 p

![image 40](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile40.png>)

is a cocompact lattice. Moreover, Jacobi’s classical theorem tells us that there are 8 (p + 1) solutions to the equation: x20 + x21 + x22 + x23 = p with (x0,x1,x2,x3) ∈ Z4. Assume now p ≡ 1 (mod 4). In this case three of the xi are even and one is odd. If we agree to take those with x0 odd and positive we have a set Σ of p + 1 solutions which come in pairs α1,α1,...,αs,αs where s = p+12 and where we consider α as an integral quaternion α = x0 + x1i + x2j + x3k, α = x0 − x1i − x2j − x3k so αi = αi = p. These p + 1 elements give p + 1 elements in G (Qp). Moreover, each αi (and αi) when considered as an element of PGL2 (Qp) takes the standard Zp-lattice in Qp×Qp (see §1.2) to an immediate neighbor in the tree and αi = α−i 1. One can deduce (see [Lub94, Corollary 2.1.11]) that the group Λ = α1,α1,...,αs,αs is a free group on s = p+12 generators acting simply transitive on the Bruhat-Tits (q + 1)-regular tree T. One can therefore identify this tree with the Cayley graph of Λ with respect to Σ = {αi |i = 1,...,s}. As Λ is also a lattice in PGL2 (Qp), it is of ﬁnite index in Γ. One can check (using “strong approximation” or directly) that if q is another prime with q ≡ 1 (mod 4) then Γ(2q)\T = Cay (Λ/Λ∩Γ(2q);Σ). Spelling out the meaning of this, one gets the following explicit construction of Ramanujan graphs, which are usually referred to as the LPS-graphs.

![image 41](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile41.png>)

![image 42](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile42.png>)

![image 43](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile43.png>)

![image 44](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile44.png>)

![image 45](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile45.png>)

![image 46](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile46.png>)

![image 47](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile47.png>)

![image 48](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile48.png>)

![image 49](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile49.png>)

![image 50](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile50.png>)

- Theorem 1.3.3 ([LPS88], see [Lub94, Theorem 7.4.3]). Let p and q be diﬀerent prime numbers with p ≡ q ≡ 1 (mod 4). Fix ε ∈ Fq satisfying ε2 = −1. For each αi = (x0,x1,x2,x3), i = 1,...,s in the set Σ above, take the matrix


x0 + εx1 x2 + εx3 −x2 + εx3 x0 − εx1 ∈ PGL2 (Fq)

αi =

and Σ = { αi |i = 1,...,s}. Let H be the subgroup of PGL2 (Fq) generated by Σ and Xp,q = Cay H; Σ , the Cayley graph of H with respect to Σ. Then:

- (a) Xp,q is a (p + 1)-regular Ramanujan graph.
- (b) If pq = −1, i.e. p is not a quadratic residue modulo q then H =


![image 51](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile51.png>)

PGL2 (Fq) and Xp,q is a bi-partite graph, while if pq = 1, H = PSL2 (Fq) and Xp,q is not.

![image 52](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile52.png>)

The main motivation for the construction of Ramanujan graphs has been expanders, but the LPS graphs turned out to have various other remarkable properties like high girth and high chromatic numbers (simultaneously!). See ([LPS88, Lub94, Sar90, Val97]) for more.

In [Mor94a], Morgenstern constructed, for every prime power q, inﬁnitely many (q + 1)-regular Ramanujan graphs. This time by ﬁnding an arithmetic lattice in PGL2 (Fq ((t))) acting simply transitive on the Bruhat-Tits tree. Another such a construction is given (somewhat hidden) in [LSV05a] as a special case of Ramanujan complexes (to be discussed in the next chapter). These last mentioned Ramanujan graphs are also edge transitive and not merely vertex transitive (see [KL12]).

# 2 Ramanujan complexes

This Chapter is devoted to the high-dimensional version of Ramanujan graphs, the so called Ramanujan complexes. These are (d − 1)-dimensional simplicial complexes which are obtained as quotients of the Bruhat-Tits building Bd associated with PGLd (F), F a local ﬁeld, just like the Ramanujan graphs were obtained as quotients of the Bruhat-Tits tree of PGL2 (F). What enables this, is the work of Laﬀorgue [Laf02] which extended to general d, the “Ramanujan conjecture” for GLd in positive characteristic, proved ﬁrst by Drinfeld [Dri88] for d = 2 (the work of Drinfeld was the basis for the Ramanujan graph constructed by Morgenstern [Mor94a]). We will start in §2.1 with the basic deﬁnitions and results about buildings and will present the associated Hecke operators, generalizing the Hecke operator (=adjacency matrix) which appeared in Chapter 1. We will present the analogue of Alon-Boppana Theorem and deﬁne Ramanujan complexes. In §2.2 we will survey shortly the representation theory of PGLd (F) and just as in Theorem 1.2.3, we will show that representation theory is relevant for the combinatorics of Γ\Bd. Then in §2.3, we will present explicit constructions of Ramanujan complexes.

We will follow mainly [LSV05a] and [LSV05b], where the reader can ﬁnd precise references for the results mentioned here. The reader is also referred to [Bal00, CSŻ03, Li04, Sar07] for related material.

- 2.1 Bruhat-Tits buildings and Hecke operators


- Let K be any ﬁeld. The spherical complex Pd−1(K) associated with Kd is the simplicial complex whose vertices are all the non-trivial (i.e. not {0} and not Kd) subspaces of Kd. Two subspaces W1 and W2 are on the same 1-edge if either W1 ⊆ W2 or W2 ⊆ W1, and {W0,...,Wr} is an r-cell if every pair Wi,Wj form an edge (i.e. Pd−1(K) is a “clique complex”). It can be shown that this happens iﬀ after some reordering W0 ⊆ W1 ⊆ ... ⊆ Wr. When K = Fq, a ﬁnite ﬁeld of order q, P1 (Fq) is just a set of q +1 points, which can be identiﬁed with the projective line over Fq. For d = 3, P2 (K) is the (q + 1)-regular graph with 2 q2 + q + 1 vertices of “points” versus “lines” of the projective plane. In general, Pd−1(K) is a (d − 2)-dimensional simplicial complex.


We now describe B = Bd (F), the aﬃne Bruhat-Tits building of type Ad−1 associated with F. Here F is a local ﬁeld with O, π and m as in §1.2 and O/m = Fq. An O-lattice in V = Fd is a ﬁnitely generated O-submodule L of V

such that L contains an F-basis of V . Two lattices L1 and L2 are equivalent if L1 = λL2 for some 0 = λ ∈ F. The vertices of B are the equivalence classes of O-lattices in V , and two distinct equivalent classes [L1] and [L2] are adjacent in B if there exist representatives L′1 ∈ [L1] and L′2 ∈ [L2] s.t. πL′1 ⊆ L′2 ⊆ L′1. The r-simplices of B (r ≥ 2) are the subsets {[L0],...,[Lr]} such that all pairs [Li] and [Lj] are adjacent. It can be shown that {[L0],...,[Lr]} forms a simplex if and only if there exist representatives L′i ∈ [Li] such that after reordering the indices, πL′r ⊆ L′0 ⊆ ... ⊆ L′r. The complex B is therefore of dimension

d − 1 = rankF (PGLd (F)). This is a special case of the Bruhat-Tits building associated with a reductive group over F. The next theorem is also a special case which generalizes Theorem 1.2.1:

- Theorem 2.1.1. The complex Bd (F) is contractible. The link of each vertex is isomorphic to Pd−1 (Fq).


The vertices of B come with a natural coloring (“type”). Let τ : B0 → Z/dZ be deﬁned as follows: Let Od ⊆ V be the standard lattice in V . For any lattice L, there exists g ∈ GL (V ) = GLd (F) such that L = g Od . Deﬁne τ ([L]) = ν (det(g))(mod d) where ν is the valuation of F, e.g. for F = Fq ((t)), ν ∞i=m aiti = m when m ∈ Z and am = 0.

The group GLd (F) acts transitively on the O-lattices in V and its center preserves the equivalence classes. As the action preserves inclusions, G = PGLd (F) acts on the building B. It acts transitively on B0 - the vertices - without preserving their colors, but PSLd (F) does preserves them. The stabilizer of the (equivalence class of the) standard lattice is K = PGLd (O). Hence B0 can be identiﬁed with G/K. To every directed edge (x,y) ∈ B1 one can associate the color τ (y) − τ (x) ∈ Z/dZ. The color of edges is preserved by PGLd (F). Let us now deﬁne d − 1 operators - the Hecke operators - as follows: For 1 ≤ k ≤ d − 1, f ∈ L2 B0 and x ∈ B0,

(Akf)(x) = f (y) (2.1)

where the summation is over the neighbors y of x such that τ (y) − τ (x) = k ∈ Z/dZ. This really amounts to a sum over the sublattices of L containing πL, whose projection in L/πL is of codimension k there. Note that Ak commutes with the action of PGLd (F). One can show that these operators are bounded, normal and commute with each other. But in general they are not self-adjoint. In fact, A∗k = Ad−k so Ak + Ad−k is self-adjoint. Moreover ∆ = dk−=11 Ak is the adjacency operator of the 1-skeleton of B. For d = 2, we only have A1 = A∗1 which is indeed the adjacency operator of the tree. As the operators Ak commute with each other they can be diagonalized simultaneously. Their common spectrum is therefore a subset Σd of Cd−1.

- Theorem 2.1.2. Let S = (z1,...,zd) ∈ Cd |zi| = 1 and di=1 zi = 1 and


k(d−k)

σ : (z1,...,zd)  → (λ1,...,λd−1) where λk = q

2 σk (z1,...,zd). Here σk is the kth elementary symmetric function, i.e. σk (z1,...,zd) =

![image 53](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile53.png>)

.

1 ·...·zi

zi

k

ii<...<ik

Then σ (S) is equal to Σd, the simultaneous spectrum of A1,...,Ad−1 acting on L2 B0 .

Note that indeed λk = λd−k as had to be expected, since Ak = A∗d−k. Also for d = 2,

![image 54](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile54.png>)

1 z

- 1

![image 55](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile55.png>)

- 2 z +


Σ2 = σ (S) = q

![image 56](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile56.png>)

z ∈ C,|z| = 1 = [−2√q,2√q]

![image 57](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile57.png>)

![image 58](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile58.png>)

which shows that Theorem 2.1.2 is a generalization of Proposition 1.1.3.

Ramanujan (q + 1)-regular graphs were deﬁned as the ﬁnite quotients of B2 = Tq+1 whose “non-trivial” eigenvalues are all in Σ2. Similarly we will deﬁne Ramanujan complexes as quotients of Bd whose “non-trivial” eigenvalues are in Σd. Let us describe ﬁrst the trivial eigenvalues: Recall that for d = 2 we have two such: (q + 1) and − (q + 1). They appear in all the ﬁnite quotients Γ\B2 when Γ preserves the colors of the vertices (and only q + 1 appears in all the ﬁnite quotients).

So, assume Γ ≤ PGLd (F) is a cocompact lattice preserving the colors of the vertices of B0. So, τ is well deﬁned on X = Γ\B0. For a dth root of unity ξ, deﬁne fξ : X → C by fξ (x) = ξτ(x). Now, Akfξ (x) sums over the neighbors of x of color τ (x) + k (mod d) and there are k d q vertices like that (where k d q denotes the number of subspaces of codimension k in Fdq). Hence Akfξ (x) =

d k q ξτ(x)+k = k d q ξkfξ (x). Thus, for every ξ ∈ C with ξd = 1, we get a simultaneous “trivial” eigenvalue [d1]q ξ1,..., k d q ξk,..., d− d1 q ξd−1 . These are the d trivial eigenvalues. Again, for d = 2, we get [21]q · 1 = q + 1 and [21]q (−1) = − (q + 1). We can now deﬁne

- Deﬁnition 2.1.3. A Ramanujan complex (of type Ad−1) is a ﬁnite quotient X = Γ\Bd satisfying: every simultaneous eigenvalue (λ1,...,λk,...,λd−1) of (A1,...,Ak,...,Ad−1) satisﬁes: either (λ1,...,λd−1) is one of the d trivial


eigenvalues (i.e. (λ1,...,λd−1) = [d1]q ξ1,..., d− d1 q ξd−1 for some dth root of unity ξ) or (λ1,...,λd−1) ∈ Σd, described in Theorem 2.1.2.

In the case of d = 2, we saw the Alon-Boppana Theorem (Theorem 1.1.2) which shows that the Ramanujan bounds are the strongest one can hope from an inﬁnite family of (q + 1)-regular graphs (for a ﬁxed q). The following theorem is a strong high dimensional version.

- Theorem 2.1.4 ([Li04, Theorem 4.3]). Let Xi be a family of ﬁnite quotients of Bd with unbounded injective radius (recall that the injective radius of a quotient π : B → Γ\B is the maximal r such that π is an isomorphism when restricted


![image 59](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile59.png>)

to any ball of radius r in B). Then specX

(A1,...,Ad−1) ⊇ Σd.

i

This shows that the best we can hope for the Xi’s is to be Ramanujan. Note that specX

(A1,...,Ad−1) is a ﬁnite set for every i. Let us end this section with the following remark:

i

- Remark 2.1.5. The trivial eigenvalues of (A1,...,Ad−1) are (λ1,...,λd−1) =


[d1 ]q ξ1,..., d− d1 q ξd−1 . So for Ak, |λk| = k d q ≈ qk(d−k) while the Ramanujan bound gives:

d k

k(d−k) 2

k(d−k) 2

|σk (z1,...,zk)| ≤

q

|λk| ≤ q

![image 60](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile60.png>)

![image 61](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile61.png>)

so for d ﬁxed and q large, the Ramanujan bound is approximately the square root of the trivial eigenvalue.

In §1.1 we mentioned that Ramanujan graphs can bee characterized by the fact that their zeta functions satisfy the Riemann hypothesis. Recently there have been some eﬀorts to associate zeta functions to higher dimensional complexes with the hope to give a similar characterization for Ramanujan complexes of dimension 2. See [DH06, Sto06, KLW10]. It will be nice if this theory could be extended also to higher dimensions.

- 2.2 Representation theory of PGLd


In this section we will describe some basic results from the representation theory of PGLd (F), F a local ﬁeld. For a more comprehensive survey see [Car79]. We will give only those results which are needed for our combinatorial application. The goal is to get a high dimensional generalization of Theorem 1.2.3, i.e., a representation theoretic formulation of Ramanujan complexes.

- Let G = PGLd (F) and K = PGLd (O), O the ring of integers of F. An irreducible unitary representation (H,ρ) of G is called K-spherical if the space of


K-ﬁxed points HK is non-zero. In this case dimHK = 1. Let C = Cc (K\G/K) be the algebra of compactly supported bi-K-invariant functions from G to C, with multiplication deﬁned by convolution

f1 ∗ f2 (x) = ˆ

G

f1 (xg)f2 g−1 dg.

The algebra C is called the Hecke algebra of G. Let πk = diag (π,π,...,π,1,1,...,1) ∈ GLd (F) with det ( πk) = πd−k, where π is the uniformizer of F. Denote by πk the image of πk in PGLd (F) and let Ak be the characteristic function of KπkK. Clearly {Ak}dk−=11 ⊆ C (note π0 = πd = Id). Less trivial is the fact that C is commutative and is freely generated as a commutative algebra by A1,...,Ad−1 (cf. [Mac79, Chap. V ]). Every irreducible unitary representation (H,ρ) of G gives rise to a representation of C on HK and when HK = {0}, this last representation is in fact given by a homomorphism w : C → C, f · v0 = w (f)v0 for f ∈ C. The representation ρ is uniquely determined by w (cf. [LSV05a, Prop. 2.2] ) and w is determined by the (d − 1)tuple (w (A1) ,...,w (Ad−1)) ∈ Cd−1. Let us put this in a somewhat more known formulation: a more common parametrization of the irreducible spherical representations of GLd (F) (and hence also of PGLd (F)) is by their Satake parametrization (z1,...,zd) ∈ (C×)d/Sym(d). This parametrization is related but not the same as the one we discuss here. Let us just mention here that

- (a) A representation of GLd (F) with Satake parameters (z1,...,zk) factors through PGLd (F) iﬀ di=1 zi = 1.
- (b) If (H,ρ) is an irreducible spherical representation of PGLd (F) with Satake parameters (z1,...,zd) then w (Ak) in the notation above is given by


k(d−k)

2 σk (z1,...,zd) where σk is the kth elementary symmetric function on d variables, σk (z1,...,zd) =

w (Ak) = q

![image 62](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile62.png>)

.

1 · ... · zi

zi

k

ii<...<ik

- (c) An irreducible representation (H,ρ) is called tempered, if there exists 0 = v,u ∈ H such that the coeﬃcient function ψ (g) = ρ(g)v,u is in L2+ε (G) for every ε > 0. These are exactly the representations which are weakly contained (in the sense of the Fell topology) in the representation of G on L2 (G). If such a representation is also K-spherical then it is weakly contained in the representation of G on L2 (G/K) = L2 (B0). In terms of Satake parameters, ρ is tempered iﬀ |zi| = 1 for all i.


The reader is referred to more information in [LSV05a] and for the general theory in [Car79]. At this point, especially in light of (b) and (c) the reader may start to guess the connection to Ramanujan complexes. Let us spell it out explicitly.

- Let L0 = Oe1 + ... + Oed be the standard O-lattice in V = Fd and [L0] its equivalence class, which corresponds to K under the identiﬁcation G/K = B0.


Let Ωk be the set of neighbors of color k of [L0]. Then πk−1K ∈ G/K = B0 is one of these neighbors and K (as a subgroup of G) acts transitively on Ωk so that

Kπk−1K = yK where the union is over all yK ∈ Ωk. Multiplying from the left by an arbitrary g ∈ G, we see that the neighbors of the vertex gK forming

an edge of color k with it, are exactly {gyK}yK∈Ωk. It follows that the operator Ak deﬁned in (2.1) in §2.1, can be expressed as follows: Identifying L2 B0 = L2 (G/K) with the right K-invariant functions in L2 (G), and assuming that K has Haar measure one, for f ∈ L2 B0 , and gK ∈ B0

ˆ

(Akf)(gK) =

f (gyK) =

f (gz)dz

yK

yK∈Ωk

yK∈Ωk

(2.2)

f (gz)dz = ˆ

= ˆ

kK z−1 dz = (f ∗ Ak)(gK)

f (gz)1Kπ

Kπk−1K

G

where Ak at the right hand side of equation (2.2) is the characteristic function of KπkK, as deﬁned in this section. No confusion should occur here as eq. (2.2) shows that the Hecke operators of §2.1 and the Hecke operators of §2.2 are essentially the same thing! When C = Cc (K\G/K) acts on L2 (G/K), Ak acts as the adjacency operators summing over all the neighbors with edges of color k.

We can now use this to deduce the main goal of this subsection (see [LSV05a, Prop. 1.5])

- Proposition 2.2.1. Let Γ be a cocompact lattice of PGLd (F). Then Γ\B is a Ramanujan complex if and only if every irreducible spherical inﬁnite dimensional G-subrepresentation of L2 (Γ\PGLd (F)) is tempered.


Sketch of proof. Assume every irreducible spherical inﬁnite dimensional subrepresentation of H = L2 (Γ\PGLd (F)) is tempered. As Γ is cocompact, H is

a direct sum of irreducible representations. Let f ∈ L2 (Γ\G/K) be a nontrivial simultaneous eigenfunction of the Hecke operators Ak with Akf = λkf. As PSLd (F) has no nontrivial ﬁnite dimensional representations, every ﬁnite dimensional representation of PGLd (F) factors through PGLd(F)/PSLd(F) ≃ F×/(F×)d. Since F× ≃ Z × O×, we have F×/O×(F×)d ≃ Z/dZ and since f is ﬁxed by K, if f lies in a ﬁnite dimensional G-subspace, it correspond to one of the d trivial eigenvalue. If f spans an inﬁnite dimensional G-space, then it is tempered, its Satake parameters (z1,...,zd) satisfy zi = 1 and |zi| = 1. The corresponding eigenvalues of Ak are, as explained in point (b) above, in Σd as deﬁned in §2.1.

In the other direction: If H1 is an irreducible spherical inﬁnite dimensional subrepresentation of L2 (Γ\G), then its unique (up to scalar) K-ﬁxed vector f is a simultaneous eigenvector of all the Ak’s where Akf = λkf. By assumption (λ1,...,λd−1) ∈ Σd, from which we deduce that the Satake parameters zi all satisfy |zi| = 1 and the representation is tempered.

![image 63](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile63.png>)

![image 64](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile64.png>)

![image 65](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile65.png>)

![image 66](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile66.png>)

So, once again, as we saw for Ramanujan graphs, the problem of constructing Ramanujan complexes moves from combinatorics to representation theory. In the next subsection, we will describe how deep results in the area of automorphic forms lead to such combinatorial constructions.

- 2.3 Explicit construction of Ramanujan complexes


We will start with a general result which gives a lot of Ramanujan complexes. We then continue to present an explicit construction.

Let us ﬁrst recall some notations and add a few more: Let k be a global ﬁeld of characteristic p > 0 and D a division algebra of degree d over k. Denote by G the k-algebraic group D×/k×, and ﬁx an embedding of G into GLn for some

- n. Let T be the ﬁnite set of valuations of k for which D does not split. We assume that for every ν ∈ T, Dν = D ⊗k kν is a division algebra. Let ν0 be


, so that G (F) ≃ PGLd (F), and denote S = T {ν0}. For OS = {x ∈ k |ν (x) ≥ 0 ∀ν ∈/ S} the ring of S-integers in k, G (OS) := G (k) GLn (OS) embeds diagonally as a discrete subgroup of ν∈S G (kν). As G (kν) is compact for ν ∈ T, projecting G (OS) into G (kν

a valuation of k which is not in T and F = kν

0

) = G (F) ≃ PGLd (F) gives an embedding of G (OS) as a discrete subgroup in PGLd (F), which we denote by Γ. In fact, by a general result on arithmetic subgroups, Γ is a cocompact lattice in PGLd (F). Thus if B = Bd (F) is the Bruhat-Tits building associated with PGLd (F), then Γ\B is a ﬁnite complex. The same is true when we mod B by any ﬁnite index subgroup of Γ. In particular, if 0 = I ⊳ OS is an ideal, then the congruence subgroup Γ(I) := ker G (OS) → G (OS/I) is of ﬁnite index in Γ and Γ(I)\B is a ﬁnite simplicial complex covered by B.

0

- Theorem 2.3.1. For Γ and I as above, Γ(I)\B is a Ramanujan complex.


A word of warning: if d is not a prime then there are ideals in Oν0

= {x ∈ k |ν (x) ≥ 0 ∀ν = ν0} (so they may disappear in OS!) which give nonRamanujan complexes. We refer to [LSV05a] for this delicate point as well as for a proof of Theorem 2.3.1. We will not try to explain the proof, but rather give few hints about it. The Theorem is proved there by going from local to global. By Proposition 2.2.1 above, Γ(I)\B is Ramanujan iﬀ every inﬁnite dimensional irreducible spherical subrepresentation ρ0 of L2 (Γ(I)\PGLd (F)) is tempered. One shows that such ρ0 is a local factor at ν0 of an automorphic adelic subrepresentation ρ′ of L2 G (k)\G (A) where A is the ring of adeles of k. By using the Jacquet–Langlands correspondence, one can replace ρ′ by a suitable subrepresentation ρ of L2 (PGLd (k)\PGLd (A)). Then one appeals to the work of Laﬀorgue [Laf02] (for which he got the Fields medal!) which is an extension to general d of the “Ramanujan conjecture” proved by Drinfeld for

- d = 2. This last result says that for various adelic automorphic representations,


the local factors are tempered. This can be applied to ρ to deduce that our ρ0 is tempered and hence Γ(I)\B is Ramanujan.

The description of the complexes we gave is pretty abstract but it can be made very explicit in some cases. To this end we will make use (following [LSV05b]) of a remarkable arithmetic lattice Γ constructed by Cartwright and Steger [CS98]. This lattice has the following amazing property: It acts simply transitively on the vertices of the building Bd. Such lattices are rare; for example in characteristic zero such lattices exist only for ﬁnitely many d’s (see [MSG12])). Let us describe their (somewhat technical) construction:

We start with the global ﬁeld k = Fq (y), whose valuations are νg for every irreducible polynomial g in Fq [y], and the minus degree valuation, ν1

(f/g) =

![image 67](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile67.png>)

y

deg g −degf. Let Fqd be the ﬁeld extension of Fq of degree d and φ a generator of the Galois group Gal(Fqd/Fq) ≃ Z/dZ. Fix a basis ξ0,...,ξd−1 of Fqd over Fq

with ξi = φi (ξ0). Let D be the k-algebra with basis ξizj di,j−=01 and relations zξi = φ(ξi)z and zd = 1+y. Then D is a division algebra which ramiﬁes at T =

and splits at all other completions of k (see [LSV05b, Prop. 3.1]). That is, Dν

ν1+y,ν1

![image 68](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile68.png>)

y

= D ⊗k Fq y 1

= D ⊗k Fq ((1 + y)) and Dν

= D ⊗k kν

![image 69](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile69.png>)

1 y

1+y

1+y

![image 70](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile70.png>)

are division algebras, while Dν ≃ Md (kν) for ν ∈/ T. In particular, G (kν) ≃ PGLd (kν) for ν ∈/ T, where we recall that G denotes the k-algebraic group D×/k×.

For ν0 we take the valuation νy, which is given explicitly by νy (amym + ... + anyn) = m (am = 0, m ≤ n). The completion of k at ν0 is F = kν

= Fq ((y)), the ﬁeld of Laurent polynomials over Fq. The ring of integer of F is O = Fq [[y]], and we recall that Bd0 ≃ PGLd(F)/PGLd(O). We now have S = ν1+y,ν1

y

,νy , and the ring of S-integers in k is OS =

![image 71](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile71.png>)

y

Fq 1+ 1y,y, y1 . As explained above, embedding G (k) in some GLn (k) gives rise to Γ = G (OS) = G (k) GLn (OS), which embeds as a cocompact arithmetic lattice in G (F) ≃ PGLd (F).

![image 72](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile72.png>)

![image 73](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile73.png>)

Until now we have followed the general construction described in the beginning of this section. In what follows we describe the Cartwright-Steger group, a subgroup of Γ which acts simply transitively on Bd0. The deﬁnition of Γ = G (OS) involves a choice of an embedding of G (k) in GLn (k). It turns out that this embedding can be chosen so that Γ is simply D(OS)×/OS×, where D (OS) stands for the OS-algebra having the OS-basis

ξizj di,j−=01 , and again the relations zξi = φ(ξi)z and zd = 1 + y (see [LSV05b, Prop. 3.3]). Note that as zd = 1+y and 1+y is invertible in OS, z is invertible in D (OS). Let b = 1 − z−1 ∈ D (OS), and note that b is also invertible, since it divides 1 − z−d = 1+yy and y ∈ OS×. Also note that Fqd is a subring of D (OS) spanned by the ξi’s. For every u ∈ F×q

![image 74](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile74.png>)

denote bu = ubu−1 ∈ D (OS)×. The element bu depends only on the coset of u in F×

d

qd/F×q , since Fq ⊆ Z (D (OS)). Denoting by bu the image of bu in Γ = D(OS)×/OS×, this gives us a set of q

d−1 q−1

![image 75](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile75.png>)

![image 76](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile76.png>)

elements Σ1 = bu u ∈ F×qd/F×q in Γ. Let Λ = Σ1 . This is the promised Cartwright-Steger group.

![image 77](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile77.png>)

- Theorem 2.3.2 ([CS98], cf. [LSV05b, Prop. 4.8]). The group Λ acts simply transitively on the vertices of Bd (F).


The set Σ1 = bu u ∈ F×qd/F×q takes the “initial vertex” x0 of the building (i.e. the equivalence class of the standard lattice) to the set of its neighbors x with τ (x) = 1 (i.e. the neighboring vertices of color 1, for which the connecting edge also has color 1). These correspond to the codimension one subspaces of Fdq and indeed there are q

![image 78](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile78.png>)

d−1 q−1 such (on which the ﬁnite group F×

qd/F×q acts transitively!) Now, for i = 2,...,d − 1, let Σi = {γ ∈ Λ |τ ((x0,γx0)) = i}, i.e., the subset of Λ of those elements which takes x0 to a neighbor of color i. As Λ acts simply transitively |Σi| = [di ]q where [di ]q is the number of subspaces of Fdq of codimension i. Let Σ = di=1−1 Σi. One can deduce now that the 1-skeleton of Bd can be identiﬁed with Cay (Λ;Σ).

![image 79](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile79.png>)

Now for every 0 = I ⊳ OS, we can deﬁne Λ (I) as Λ (I) = ker Λ → G (OS/I) . This deﬁnes a complex Λ (I)\Bd which by Theorem 2.3.1 is a Ramanujan complex.

Observe now that the building B is a clique complex, namely, a set of i + 1 vertices forms a simplex if and only if every two vertices in it form a 1-edge. In particular, the full structure of the complex is determined by the 1-skeleton. The same is true for the quotients Λ (I)\Bd (at least for large enough quotients, since the map Bd → Λ (I) \Bd is a local isomorphism, moreover the injective radius of Λ (I)\Bd grows logarithmically w.r.t. its size). So, these complexes are the Cayley complexes of the group Λ/Λ(I) with respect to the set of generators Σ, or more precisely, their images in Λ/Λ(I). Recall that a Cayley complex of a group H w.r.t. a symmetric set of generators Σ is the simplicial complex for which a subset ∆ of H is a simplex iﬀ a−1b ∈ Σ for every a,b ∈ ∆. This is the clique complex determined by Cay (H;Σ).

To make all this explicit also in the computer science sense, one needs to identify the quotients Λ/Λ(I). This is carried out using the Strong Approximation Theorem. When I is a prime ideal of OS, we get that OS/I is a ﬁnite ﬁeld of order qe for some e. The group Λ/Λ(I) is then a subgroup of PGLd (Fqe) containing PSLd (Fqe). Various choices of ideals I can be made to make sure that any of the subgroups H between PSLd (Fqe) and PGLd (Fqe) can occur. Note that the quotient PGLd(Fqe)/PSLd(Fqe) is a cyclic group of order dividing d. The resulting graphs are therefore t-partite for some t | d, just as in case d = 2 where we have had bi-partite and non-bipartite. We skip the technical details and give only a corollary (see Theorem 1.1 and Algorithm 9.2 in [LSV05b]).

- Theorem 2.3.3. Let q be a given prime power, d ≥ 2 and e ≥ 1. Assume qe ≥ 4d2. Every subgroup H, with PSLd (Fqe) ≤ H ≤ PGLd (Fqe), has an


(explicit) set Σ of [d1 ]q + ... + d− d1 q generators, such that the Cayley complex of H w.r.t. Σ is a Ramanujan complex covered by Bd (F) when F = Fq ((y)).

We mention in passing that the construction in this subsection is of interest even for d = 2 (in spite of the fact that we have already seen other constructions of Ramanujan graphs in the previous chapter) since for d = 2, F×

q2/F×q acts transitively on all the q+1 neighbors of the standard lattice. From this one can deduce that the resulting Ramanujan graphs are edge transitive and not merely vertex transitive, as is always the case for Cayley graphs. This extra symmetry plays a crucial role in an application to the theory of error correcting codes (see [KL12]).

We hope that the higher Ramanujan complexes will also bear some fruits in combinatorics like their one dimensional counterparts. For ﬁrst steps in this direction see [LM07] and [KL].

# 3 High dimensional expanders

In Deﬁnition 1.1.6 we presented the deﬁnition of expanding graphs. In recent years several suggestions have been proposed as to what should be the “right” deﬁnition of “expander” for higher dimensional simplicial complexes. In this chapter we will bring some of these as well as few results about the relations between them. This area is still in its primal state, and we can expect more developments. The importance of expanding graphs suggests that studying expanding simplicial complexes will also turn out to be very fruitful.

- 3.1 Simplicial complexes and cohomology


A ﬁnite simplicial complex X is a ﬁnite collection of subsets of a set X(0), called the set of vertices of X, which is closed under taking subsets. The sets in X are called simplices or faces and we denote by X(i) the set of simplices of X of dimension i, which are the sets of X of size i + 1. So X(−1) is comprised of

the empty set, X(0) - of the vertices, X(1) - the edges, X(2) - the triangles, etc. Throughout this discussion we will assume that X(0) = {v1,...,vn} is the set of vertices and we ﬁx the order v1 < v2 < ... < vn among the vertices. Now, if F ∈ X(i) we write F = {vj

. If G ∈ X(i−1), we denote the oriented incidence number [F : G] by (−1)ℓ if F\G = {vj

i} with vj

< ... < vj

< vj

,...,vj

1

0

0

i

ℓ} and 0 if G F. In particular for every vertex v ∈ X(0) and for the unique face ∅ ∈ X(−1), [v : ∅] = 1.

If F is a ﬁeld then Ci (X,F) is the F-vector space of the functions from X(i) to F. This is a vectors space of dimension X(i) over F where the characteristic functions eF F ∈ X(i) serve as a basis. The coboundary map δi : Ci (X,F) → Ci+1 (X,F) is given by:

[F : G] f (G)

(δif)(F) =

G∈X(i)

so if f = eG for some G ∈ X(i), δieG is a sum of all the simplices of dimension i + 1 containing G with signs ±1 according to the relative orientations.

It is well known and easy to prove that δi ◦ δi−1 = 0. Thus Bi (X,F) = imδi−1 - “the space of i-coboundaries” is contained in Zi (X,F) = kerδi - the i-cocycles and the quotient Hi (X,F) = Zi(X,F)/Bi(X,F) is the i-th cohomology group of X over F.

In a dual way one can look at Ci (X,F) - the F-vector space spanned by the simplices of dimension i. Let ∂i : Ci (X,F) → Ci−1 (X,F) be the boundary map deﬁned on the basis element F by: ∂F = G∈X(i−1) [F : G] · G, i.e. if F = {vj

i} then ∂iF = it=0 (−1)t {vj

i}. Again ∂i ◦ ∂i+1 = 0 and so the boundaries Bi (X,F) = im∂i+1 are inside the cycles Zi (X,F) = ker∂i and Hi (X,F) = Zi(X,F)/Bi(X,F) gives the i-th homology group of X over F. As F is a ﬁeld, it is not diﬃcult in this case to show that Hi (X,F) ≃ Hi (X,F). Sometimes, it is convenient to identify Ci (X,F) and Ci (X,F) by assigning F to eF.

,...,vj

,..., vj

,...,vj

0

0

t

The i-th laplacian of X over F is deﬁned as the linear operator ∆i : Ci (X,F) → Ci (X,F) given by ∆i = ∂i+1δi + δi−1∂i. The operator ∂i+1δi is sometimes denoted (for clear reasons!) ∆upi , while ∆downi = δi−1∂i. In fact, ∂i+1 is the dual of δi and so the eigenvalues of ∆upi and ∆downi+1 diﬀer only by the multiplicity of zero. Note that what is customarily called the laplacian of a graph is actually the upper 0-laplacian:

∆up0 f (x) = deg (x) f (x) −

f (y).

y∼x

- 3.2 F2-coboundary expansion


It seems that the ﬁrst deﬁnition of higher dimensional expansion was given by Linial-Meshulam [LM06], Meshulam-Wallach [MW09] and Gromov [Gro10] (see also [DK10, GW12, SKM12, NR12]) as follows

- Deﬁnition 3.2.1. For a simplicial complex X, the F2-coboundary expansion of X in dimension i is


Ei (X) = min

δi−1f [f]

![image 80](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile80.png>)

f ∈ Ci−1 (X,F2)\Bi−1 (X,F2) .

In other papers this notion is referred to as “cohomological expansion”, “coboundary expansion”, or “combinatorial expansion”. Let us explain the notation here: F2 is the ﬁeld of order two, for f ∈ Ci−1 (and similarly for δf ∈ Ci), f is simply the number of (i − 1)-simplices F for which f (F) = 0. Finally, [f] is the coset f + Bi−1 (X,F2) and

[f] = min{ g |g ∈ [f]} = min f + δi−2h h ∈ Ci−2 (X,F2) .

One can see that [f] is the minimal distance of f from Bi−1 (X,F2) in the Hamming metric, and in particular that [f] = 0 iﬀ f ∈ Bi−1 (X,F2). Some authors prefer to normalize the expansion as follows:

δi−1f /|X(i)| [f] /|X(i−1)|

f ∈ Ci−1 (X,F2)\Bi−1 (X,F2) .

Ei (X) = min

![image 81](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile81.png>)

Let us explain why this artiﬁcially looking deﬁnition exactly gives expander graphs in the one dimensional case: If X is a graph then B0 = imδ−1 is the one dimensional space containing two functions, the zero function 0 and the constant function on all the vertices of X. Now, if f ∈ C0 (X,F2) then f is nothing more than the characteristic function χA of some subset A ⊆ X(0), in which case [f] = f + B0 (X,F2) = {χA,χA} where A is the complement of A in

![image 82](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile82.png>)

![image 83](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile83.png>)

- X(0). Thus [f] = min |A|, A . Finally δf is nothing more than the size


![image 84](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile84.png>)

- of E A,A , i.e., the set of edges between A and A. We can now see that the


![image 85](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile85.png>)

![image 86](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile86.png>)

F2-coboundary expansion E1 (X) (which is the only relevant dimension in this case) is exactly h (X) as in Remark 1.1.5. Very few results have been proven so far about this concept. Here is one of them (see [MW09, Gro10])

![image 87](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile87.png>)

Proposition 3.2.2. The complete complex ∆[n−1], the simplicial complex on n vertices where every subset is a face, has F2-coboundary expansion Ei ∆[n−1] ≥

n i+1, 1 ≤ i ≤ n − 1. Equivalently, Ei ∆[n−1] ≥ 1 (in fact, it converges to 1 when n grows to ∞).

![image 88](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile88.png>)

- Remark 3.2.3. One should note that X has positive F2-coboundary expansion in dimension i if and only if Hi−1 (X,F2) = 0: If Zi−1 (X,F2) = Bi−1 (X,F2) then δf = 0 for every f ∈ Ci−1\Bi−1, while if f ∈ Zi−1 (X,F2)\Bi−1 (X,F2) then δf = 0 and [f] = 0. This vanishing of Hd−1 (X,F2) in the graph case, d = 1, is the vanishing of H0 (X,F2) which exactly means that the graph X is connected. Indeed, it is clear that an ε-expander graph is connected.


Most of the known results on coboundary expansion refer to complexes X of dimension d whose d − 1 skeleton is complete (i.e. every subset of X(0) of size

d is a face in the complex). See [LM06, MW09, Gro10, DK10, Wag11, GW12] for various results, mainly on random complexes.

As far as we know there is no known family of higher dimensional Z2-coboundary expanders of bounded degree (i.e. where the number of faces is linear in the number of vertices). It is natural to suggest that the Ramanujan complexes of §2 (and even more generally, all ﬁnite quotients of higher dimensional BruhatTits buildings of simple groups of rank ≥ 2 over local ﬁelds) are such. But this is not the case in general. For example, let Γ be any cocompact lattice in PGL3 (F) where F is a local ﬁeld and assume Γ/[Γ,Γ]Γ2 is non-trivial (i.e. Γ has a non-trivial abelian quotient of 2-power order - by [Lub87] every lattice has such a sublattice of ﬁnite index) then H1 (Γ\B,F2) = 0 (since B - the Bruhat-Tits building of PGL3 (F) is contractible) and so by Remark 3.2.3 the F2-coboundary expansion of X = Γ\B in dimension 2 is 0. It might be that the vanishing of the cohomology is the only obstruction. Another possible way to circumvent this is to use instead the notion of Gromov of “ﬁlling”: The ﬁlling of X (in dimension i) is

f + Zi−1 δi−1f

f ∈ Ci−1 (X,F2)\Zi−1 (X,F2) . When Hi−1 (X,F2) vanishes, the ﬁlling and the F2-coboundary expansion are related by νi (X) = E 1

νi (X) = max

![image 89](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile89.png>)

−1

δi−1f f+Bi−1

. When Hi−1 (X,F2) does

i(X) = min

![image 90](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile90.png>)

![image 91](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile91.png>)

f∈Ci−1\Bi−1

not vanish, Ei (X) is zero (see 3.2.3), but νi (x) is always ﬁnite since δi−1f = 0 for f ∈/ Zi−1. For example, the Cheeger constant h vanishes for a disconnected

![image 92](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile92.png>)

graph, while ν 1

1(x) is the mediant (or “freshman sum”) of the Cheeger constants of the connected components of the graph, and it is always positive. We present the following conjecture:

![image 93](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile93.png>)

Conjecture 3.2.4. Let B be the Bruhat-Tits building associated with PGLd (F), F a local ﬁeld and d ≥ 3. There exists a constant ν = ν (d,F) such that νi (X) ≤ ν for every ﬁnite quotient X of B.

Even special cases of this conjecture (e.g. the case d = 3 and q, the residue ﬁeld

- of F, large) are of importance in coding theory as shown in [KL].


- 3.3 The Cheeger constant


The Cheeger constant h (X) for a graph X is deﬁned in Deﬁnition 1.1.4 above (see also Remark 1.1.5 there). One may argue what should be the right deﬁnition of h (X) when X is a higher dimensional simplicial complex. Let us follow here the deﬁnition given in [PRT12]:

- Deﬁnition 3.3.1. For a d-dimensional simplicial complex X, denote


h (X) = min

d

X(0)=

i=0

X(0) |F (A0,...,Ad)| |A0| · ... · |Ad|

![image 94](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile94.png>)

Ai

where the minimum is over all the partitions of X(0) into nonempty sets A0,...,Ad and F (A0,...,Ad) denotes the set of d-dimensional simplices with exactly one vertex in each Ai.

For d = 1, it coincides with Deﬁnition 1.1.4. But, in a way, this deﬁnition keeps the spirit of the mixing lemma (Proposition 1.1.8): h (X) measures the number of “edges” (i.e. d-faces) “between” (i.e. with a single representative in each of) the Ai. The quantity |F (A0,...,Ad)| is “normalized” by multiplying it by |X(0)|

d i=0|Ai|. This deﬁnition works well when X has a complete (d − 1)-skeleton (see more in §3.5), but as noted in [PRT12] it gives zero whenever X(d−1) is not complete (If G = {v0,...,vd−1} ∈/ X(d−1) take Ai = {vi} for i = 0,...,d − 1 and Ad = X(0)\G. Then F (A0,...,Ad) = ∅). In [PRT12], the authors call the diﬀerence

![image 95](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile95.png>)

X(d) |A0| · ... · |Ad| n d+1

(3.1)

|F (A0,...,Ad)| −

![image 96](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile96.png>)

the discrepancy of A0,...,Ad, and they bound this value, and the constant

- h (X), in terms of the spectrum of the laplacian. This brings us to our next subject.

3.4 Spectral gap

In §1 we saw that the notion of expander can be described by means of the eigenvalues of the adjacency matrix A of the graph. For a k-regular graph X, the matrix A is nothing more than A = kI−∆up0 where ∆up0 is the 0-dimensional upper laplacian of X over F = R as deﬁned in §3.1. We can translate Theorem 1.1.7 to deduce that a family of k-regular graphs {Xt}t∈I is a family of expanders

- iﬀ there exists ε > 0 such that every eigenvalue λ of ∆up0 Z0(X,R)


= ∆0

Z0(X,R) satisﬁes λ ≥ ε (the last is equality is since ∆downi (Zi (X,R)) = δi−1∂i (ker∂i) =

- 0). Note that Z0 (X,R) = f : X(0) → R x∈X(0) f (x) = 0 . It is therefore natural to generalize and to deﬁne


- Deﬁnition 3.4.1. Let X be a simplicial complex of dimension d and 0 ≤ i ≤


d − 1. We denote λi (X) = minSpec ∆i

and we say that X has spectral gap λi (X) in dimension i. We write λ(X) for λd−1 (X).

Zi(X,R)

It is natural to expect that just like in graphs where there is a direct connection between the Cheeger constant and the spectral gap, something like that should happen in the higher dimensional case, but examples presented in [PRT12] show that there exist simplicial complexes with λ(X) = 0 while h (X) > 0. The mystery has been revealed recently in [PRT12] where it is shown that the right generalization of the Cheeger inequalities is:

- Theorem 3.4.2 ([PRT12]). Let X be a ﬁnite d-dimensional complex with a complete (d − 1)-skeleton. If k is the maximal degree of a (d − 1)-cell, then

d 1 − d−1 |X(0)|

![image 97](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile97.png>)

2

![image 98](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile98.png>)

8k

h2 (X) − (d − 1)k ≤ λ(X) ≤ h (X).

The reader may note that this Theorem, when specialized to d = 1, gives exactly Theorem 1.1.7.

A similar generalization is obtained in [PRT12] for the expander mixing lemma (Proposition 1.1.8 above). Given any two sets of vertices A,B ⊆ V , the mixing lemma for graphs bounds the deviation of |E (A,B)| from its expected value in a random k-regular graph, in terms of the spectral invariant µ0. From the perspective of the simplicial laplacian, µ0 is the spectral radius of kI − ∆0

Z0(X,R)

,

i.e. the maximal absolute value of its eigenvalues. The following generalization then holds for higher dimensional complexes:

- Theorem 3.4.3 ([PRT12]). Let X be a ﬁnite d-dimensional complex with a complete (d − 1)-skeleton. Let k be the average degree of a (d − 1)-cell, and deﬁne


µ0 (X) = max |γ| γ ∈ Spec kI − ∆d−1

Zd−1(X,R)

Then for every disjoint sets of vertices A0,...,Ad,

.

k |A0| · ... · |Ad| X(0) ≤ µ0 (X)(|A0| · ... · |Ad|)

d d+1

.

|F (A0,...,Ad)| −

![image 99](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile99.png>)

![image 100](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile100.png>)

Again, when specializing to d = 1 this gives the original expander mixing lemma for graphs, except for the additional assumption that the sets of vertices are disjoint. The reader is referred to [PRT12] for the proofs of Theorems 3.4.2 and

- 3.4.3. So far, the results are under the assumption of full (d − 1)-skeleton but a work on the general situation is in progress. It is natural to suggest some extension of Alon-Boppana theorem (Theorem


- 1.1.2) to this high dimensional case (see also Theorem 2.1.4). In [PR12] it is shown that the high dimensional analogue of Alon-Boppana indeed holds in several interesting cases (for example, for quotients of an inﬁnite complex with nonzero spectral gap), but that it can also fail. The reader is referred to that interesting work for more details.


The most important work so far on the spectral gap of complexes is the seminal work of Garland [Gar73]. As this work has been described in many placed (e.g. [Bor73, Zuk96, GW12]) we will not elaborate on it here. We just mention that Garland proved Serre’s conjecture that Hi (X,R) = 0 for every 1 ≤ i ≤ d − 1 where X is a ﬁnite quotient of the Bruhat-Tits building of a simple group of rank d ≥ 2 over a local ﬁeld F. He did this by proving a bound on the spectral

gaps which depends only d and F (the i-th cohomology group over R vanishes iﬀ the corresponding spectral gap λi is nonzero). It is still not clear what is the relation between the coboundary expansion and the spectral gap. See [GW12, SKM12] where some complexes are presented with λi (X) arbitrarily small while Ei (X) is bounded away from zero, and also the other way around.

- 3.5 The overlap property


An interesting “overlap” property for complexes, which is closely related to expanders, was deﬁned by Gromov [Gro10], and was further studied in [FGL+10, MW11, Kar12]. We need ﬁrst some notation: Let X be a ddimensional simplicial complex and ϕ : X(0) → Rd an injective map. The map ϕ can be extended uniquely to a simplicial mapping ϕ from X (considered now as a topological space in the obvious way) to Rd (i.e. by extending ϕ aﬃnely to the edges, triangles, etc.) This will be called a geometric extension. The map ϕ can be extended in many diﬀerent ways to a continuous map ϕ from the topological simplicial complex X to Rd, such ϕ will be called topological extensions.

- Deﬁnition 3.5.1. Let X be a d-dimensional simplicial complex and 0 < ε ∈ R. We say that X has ε-geometric overlap (resp. ε-topological overlap) if for every injective map ϕ : X(0) → Rd and a geometric (resp. topological) extension ϕ : X → Rd, there exists a point z ∈ Rd such that ϕ−1 (z) intersects at least ε · X(d) of the d-dimensional simplices of X.


To digest this deﬁnition, let us spell out what does this means for expander graphs: Let ϕ : X(0) → R be an injective map and ϕ any continuous extension

of it to the graph. Let z ∈ R be a point such that 2 1 X(0) of the images of the vertices are above it (and call L ⊆ X(0) this set of vertices) and the rest are below it. Then ϕ−1 (z) intersects all the edges of E L,L (= the set of edges going from L to its complement). If X is an ε-expander k-regular graph, then

![image 101](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile101.png>)

![image 102](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile102.png>)

- X(1) = |X(0)|k


|X(0)|

2 = 2εk X(1) . Thus X has the ε

2 while E L,L ≥ 2ε |L| ≈ 2ε

![image 103](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile103.png>)

![image 104](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile104.png>)

![image 105](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile105.png>)

![image 106](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile106.png>)

![image 107](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile107.png>)

![image 108](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile108.png>)

2k-topological overlapping property.

![image 109](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile109.png>)

The reader should notice however that this property is not equivalent to expander. In fact, it does not even imply that the graph X is connected. It can be a union of a large expanding graph and a small connected component. Still, this property captures the nature of expansion especially in the higher dimensional case.

It is interesting to mention that while it is trivial to prove that the complete graph is an expander, it is a non-trivial result that the higher dimensional complete complexes have the overlap property. This was proved for the geometric overlap in [BF84] for dim 2 and in [Bár82] for all dimensions. For the topological overlap, this was proved in [Gro10] (see also [MW11, Kar12]).

The main result of [FGL+10] asserts that there even exist simplicial complexes of bounded degree with the geometric overlapping property. They prove it by two methods: probabilistic and constructive. The constructive examples are the Ramanujan complexes which were discussed in length in §2 (but under the assumption that q is large enough w.r.t. d). In fact, the proof there is valid for all the ﬁnite quotients of B = B (PGLd (F)) and not only to the Ramanujan ones (again assuming q >> d). It is quite likely that the same result holds also for the other Bruhat-Tits buildings of simple groups of rank ≥ 2.

In all these results the following theorem of Pach plays a crucial role:

- Theorem 3.5.2 ([Pac98]). For every d ≥ 1, there exists cd > 0 such that for every d + 1 disjoint subsets P1,...,Pd+1 of n points in general position in Rd, there exists z ∈ Rd and subsets Qi ⊆ Pi with |Qi| ≥ cd |Pi| such that every d-dimensional simplex with exactly one vertex in each Qi, contains z.


Let us show now, following [PRT12] how to deduce the geometric overlap property from Pach’s theorem and the mixing lemma, when we have a “concentration of the spectrum”. Let X be a d-dimensional complex on n vertices, with a complete (d − 1) skeleton. For an arbitrary injective map ϕ : X(0) → Rd we can divide ϕ X(0) to (d + 1)-disjoint sets P0,...,Pd, each of order (approximately)

n d+1. By Pach’s theorem there is a point z ∈ Rd and subsets Qi ⊆ Pi of sizes |Qi| = c

![image 110](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile110.png>)

dn

d+1, such that z belongs to every d-simplex formed by representatives from Q0,...,Qd. This means that for the geometric extension ϕ : X → Rd, ϕ−1 (z) intersects every simplex in F ϕ−1 (Q0),...,ϕ−1 (Qd) . Turning to the mixing lemma (Theorem 3.4.3 above), if the average degree of a (d − 1)-cell in

![image 111](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile111.png>)

X is k, and Spec ∆d−1

⊆ [k − ε,k + ε], then

Zd−1(X,R)

k |Q0|...|Qd| n − ε (|Q0|...|Qd|)

d d+1

F ϕ−1 (Q0),...,ϕ−1 (Qd) ≥

![image 112](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile112.png>)

![image 113](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile113.png>)

d kcd d + 1 − ε ·

cdn d + 1

=

![image 114](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile114.png>)

![image 115](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile115.png>)

Since this applies to every ϕ : X(0) → Rd, the quotient by Xd = d+1k nd gives a lower bound for the geometric expansion of X:

![image 116](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile116.png>)

d

cdn d+1

kcd d+1 − ε

cdd ed+1

ε (d + 1) k

![image 117](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile117.png>)

![image 118](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile118.png>)

.

cd −

≥

overlap(X) ≥

![image 119](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile119.png>)

![image 120](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile120.png>)

![image 121](<2012-lubotzky-ramanujan-complexes-high-dimensional_images/imageFile121.png>)

|Xd|

This is used in [PRT12] to establish the overlap property for random complexes in the Linial-Meshulam model [LM06]: It is shown that if the expected degree of a (d − 1)-cell grows logarithmically in the number of vertices then the complexes have geometric overlap asymptotically almost surely.

While bounds on the spectrum give some geometric overlap properties, it is much more diﬃcult to get the topological overlap property. The only result known to us is the following Theorem of Gromov (see [MW11] for a simpliﬁed proof; though still highly non-trivial):

- Theorem 3.5.3. If X has normalized F2-coboundary expansion Ei (X) ≥ εi for all 1 ≤ i ≤ d then X has the ε-topological overlap property for some ε = ε (ε1,...,εd,d) > 0.


Still, we do not know any example of higher dimensional complexes of bounded degree with the F2-coboundary expansion property. It is tempting to conjecture that the ﬁnite quotients X of a ﬁxed high-rank Bruhat-Tits building of dimension d, with trivial cohomology over F2, form such a family. We end with this question which seems fundamental for further progress.

# References

[Alo86] N Alon. Eigenvalues and expanders. Combinatorica, 6(2):83–96, 1986.

[AM85] N. Alon and V.D. Milman. λ1, isoperimetric inequalities for graphs, and superconcentrators. Journal of Combinatorial Theory, Series B, 38(1):73–88, 1985.

[Bal00] C.M. Ballantine. Ramanujan type buildings. Canadian Journal of Mathematics, 52(6):1121–1148, 2000.

[Bár82] I. Bárány. A generalization of Carathéodory’s theorem. Discrete Mathematics, 40(2):141–152, 1982.

[BF84] E. Boros and Z. Füredi. The number of triangles covering the center of an n-set. Geometriae Dedicata, 17(1):69–77, 1984.

[Bor73] A. Borel. Cohomologie de certains groupes discrets et laplacien padique. Séminaire Bourbaki, Exposé, 437:12–35, 1973.

[Car79] P. Cartier. Representations of p-adic groups: a survey. In Automorphic forms, representations and L-functions, volume 33 of Proceedings of Symposia in Pure Mathematics, pages 111–155, 1979.

[CS98] D.I. Cartwright and T. Steger. A family of A˜n-groups. Israel Journal of Mathematics, 103(1):125–140, 1998.

[CSŻ03] D.I. Cartwright, P. Solé, and A. Żuk. Ramanujan geometries of type A˜n. Discrete mathematics, 269(1):35–43, 2003.

[DH06] A. Deitmar and J.W. Hoﬀman. The Ihara–Selberg zeta function for PGL3 and Hecke operators. International Journal of Mathematics, 17(02):143–155, 2006.

[DK10] D. Dotterrer and M. Kahle. Coboundary expanders. arXiv preprint arXiv:1012.5316, 2010.

[Dod84] J. Dodziuk. Diﬀerence equations, isoperimetric inequality and transience of certain random walks. Trans. Amer. Math. Soc, 284, 1984.

[Dri88] V.G. Drinfel’d. The proof of Peterson’s conjecture for GL(2) over a global ﬁeld of characteristic p. Functional Analysis and its Applications, 22(1):28–43, 1988.

[FGL+10] J. Fox, M. Gromov, V. Laﬀorgue, A. Naor, and J. Pach. Overlap properties of geometric expanders. arXiv preprint arXiv:1005.1392, 2010.

[Gar73] H. Garland. p-adic curvature and the cohomology of discrete subgroups of p-adic groups. The Annals of Mathematics, 97(3):375–423, 1973.

[Gro10] M. Gromov. Singularities, expanders and topology of maps. part 2: From combinatorics to topology via algebraic isoperimetry. Geometric and Functional Analysis, 20(2):416–526, 2010.

[GW12] A. Gundert and U. Wagner. On laplacians of random complexes. In Proceedings of the 2012 symposuim on Computational Geometry, pages 151–160. ACM, 2012.

[Has89] K. Hashimoto. Zeta functions of ﬁnite graphs and representations of p-adic groups. Automorphic forms and geometry of arithmetic varieties., pages 211–280, 1989.

[HLW06] S. Hoory, N. Linial, and A. Wigderson. Expander graphs and their applications. Bulletin of the American Mathematical Society, 43(4):439–562, 2006.

[Iha66] Y. Ihara. On discrete subgroups of the two by two projective linear group over p-adic ﬁelds. Journal of the Mathematical Society of Japan, 18(3):219–235, 1966.

[Kar12] R. Karasev. A simpler proof of the Boros–Füredi–Bárány–Pach– Gromov theorem. Discrete & Computational Geometry, pages 1–4, 2012.

[Kes59] H. Kesten. Symmetric random walks on groups. Transactions of the

American Mathematical Society, 92(2):336–354, 1959. [KL] T. Kaufman and A. Lubotzky. In preparation. [KL12] T. Kaufman and A. Lubotzky. Edge transitive Ramanujan graphs

and symmetric LDPC good codes. In Proceedings of the 44th symposium on Theory of Computing, pages 359–366. ACM, 2012.

[KLW10] M.H. Kang, W.C.W. Li, and C.J. Wang. The zeta functions of complexes from PGL(3): a representation-theoretic approach. Israel Journal of Mathematics, 177(1):335–348, 2010.

[Laf02] L. Laﬀorgue. Chtoucas de Drinfeld et correspondance de Langlands. Inventiones mathematicae, 147(1):1–241, 2002.

[Li04] W.C.W. Li. Ramanujan hypergraphs. Geometric and Functional Analysis, 14(2):380–399, 2004.

- [LM06] N. Linial and R. Meshulam. Homological connectivity of random 2-complexes. Combinatorica, 26(4):475–487, 2006.
- [LM07] A. Lubotzky and R. Meshulam. A Moore bound for simplicial complexes. Bulletin of the London Mathematical Society, 39(3):353–358, 2007.


[LPS88] A. Lubotzky, R. Phillips, and P. Sarnak. Ramanujan graphs. Combinatorica, 8(3):261–277, 1988.

- [LSV05a] A. Lubotzky, B. Samuels, and U. Vishne. Ramanujan complexes of type A˜d. Israel Journal of Mathematics, 149(1):267–299, 2005.
- [LSV05b] A. Lubotzky, B. Samuels, and U. Vishne. Explicit constructions of


ramanujan complexes of type A˜d. Eur. J. Comb., 26(6):965–993, August 2005.

[Lub87] A. Lubotzky. On ﬁnite index subgroups of linear groups. Bulletin of the London Mathematical Society, 19(4):325–328, 1987.

[Lub94] A. Lubotzky. Discrete Groups, Expanding Graphs and Invariant

Measures, volume 125 of Progress in Mathematics. Birkhauser, 1994. [Lub12] A. Lubotzky. Expander graphs in pure and applied mathematics.

Bull. Amer. Math. Soc, 49:113–162, 2012. [Mac79] I.G. Macdonald. Symmetric functions and Hall polynomials. Clarendon Press Oxford, 1979.

[Mar88] G.A. Margulis. Explicit group-theoretical constructions of combinatorial schemes and their application to the design of expanders and concentrators. Problemy Peredachi Informatsii, 24(1):51–60, 1988.

- [Mor94a] M. Morgenstern. Existence and explicit constructions of q+1 regular Ramanujan graphs for every prime power q. Journal of Combinatorial Theory, Series B, 62(1):44–62, 1994.
- [Mor94b] M. Morgenstern. Ramanujan diagrams. SIAM Journal on Discrete Mathematics, 7(4):560–570, 1994.


[Mor95] M. Morgenstern. Natural bounded concentrators. Combinatorica, 15(1):111–122, 1995.

[MSG12] A. Mohammadi and A. Salehi Golseﬁdy. Discrete subgroups acting transitively on vertices of a Bruhat–Tits building. Duke Mathematical Journal, 161(3):483–544, 2012.

[MW09] R. Meshulam and N. Wallach. Homological connectivity of random kdimensional complexes. Random Structures & Algorithms, 34(3):408– 417, 2009.

[MW11] J. Matoušek and U. Wagner. On Gromov’s method of selecting heavily covered points. Arxiv preprint arXiv:1102.3515, 2011.

[Nil91] A. Nilli. On the second eigenvalue of a graph. Discrete Mathematics, 91(2):207–210, 1991.

[NR12] I. Newman and Y. Rabinovich. On multiplicative λ-approximations and some geometric applications. In Proceedings of the Twenty-Third Annual ACM-SIAM Symposium on Discrete Algorithms, pages 51– 67. SIAM, 2012.

[Pac98] J. Pach. A Tverberg-type result on multicolored simplices. Computational Geometry, 10(2):71–76, 1998.

[PR12] O. Parzanchevski and R. Rosenthal. Simplicial complexes: spectrum, homology and random walks. ArXiv preprint arXiv:1211.6775, 2012.

[PRT12] O. Parzanchevski, R. Rosenthal, and R.J. Tessler. Isoperimetric inequalities in simplicial complexes. arXiv preprint arXiv:1207.0638, 2012.

[Sar90] P. Sarnak. Some applications of modular forms, volume 99. Cambridge University Press, 1990.

[Sar07] A. Sarveniazi. Explicit construction of a Ramanujan (n1,n2,...,nd−1)-regular hypergraph. Duke Mathematical Journal, 139(1):141–171, 2007.

[Sat66] I. Satake. Spherical functions and ramanujan conjecture. In Proc. Sympos. Pure Math, volume 9, pages 258–264, 1966.

[Ser80] J.P. Serre. Trees, translated from French by John Stillwell. Springer Verlag, 1980.

[SKM12] J. Steenbergen, C. Klivans, and S. Mukherjee. A Cheeger-type inequality on simplicial complexes. arXiv preprint arXiv:1209.5091, 2012.

[Sto06] C.K. Storm. The zeta function of a hypergraph. The Electronic Journal of Combinatorics, 13(R84):1, 2006.

[Sun88] T. Sunada. Fundamental groups and laplacians. Geometry and Analysis on Manifolds, pages 248–277, 1988.

[Tan84] R.M. Tanner. Explicit concentrators from generalized n-gons. SIAM Journal on Algebraic and Discrete Methods, 5:287, 1984.

[Val97] A. Valette. Graphes de Ramanujan et applications. Astérisque, 245:247–276, 1997.

[Wag11] U. Wagner. Minors in random and expanding hypergraphs. In Proc. 27th Ann. Symp. Comput. Geom.(SoCG), pages 351–360, 2011.

[Zuk96] A. Zuk. La propriété (T) de Kazhdan pour les groupes agissant sur les polyedres. Comptes rendus de l’Académie des sciences. Série 1, Mathématique, 323(5):453–458, 1996.

