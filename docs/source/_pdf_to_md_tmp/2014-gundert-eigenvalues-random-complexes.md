## On Eigenvalues of Random Complexes∗

###### Anna Gundert, † Uli Wagner‡ March 25, 2018

# arXiv:1411.4906v3[math.CO]25Aug2015

###### Abstract

We consider higher-dimensional generalizations of the normalized Laplacian and the adjacency matrix of graphs and study their eigenvalues for the Linial–Meshulam model Xk(n,p) of random k-dimensional simplicial complexes on n vertices. We show that for p = Ω(log n/n), the eigenvalues of each of the matrices are a.a.s. concentrated around two values. The main tool, which goes back to the work of Garland, are arguments that relate the eigenvalues of these matrices to those of graphs that arise as links of (k − 2)-dimensional faces. Garland’s result concerns the Laplacian; we develop an analogous result for the adjacency matrix.

The same arguments apply to other models of random complexes which allow for dependencies between the choices of k-dimensional simplices. In the second part of the paper, we apply this to the question of possible higher-dimensional analogues of the discrete Cheeger inequality, which in the classical case of graphs relates the eigenvalues of a graph and its edge expansion. It is very natural to ask whether this generalizes to higher dimensions and, in particular, whether the eigenvalues of the higher-dimensional Laplacian capture the notion of coboundary expansion — a higher-dimensional generalization of edge expansion that arose in recent work of Linial and Meshulam and of Gromov; this question was raised, for instance, by Dotterrer and Kahle. We show that this most straightforward version of a higher-dimensional discrete Cheeger inequality fails, in quite a strong way: For every k ≥ 2 and n ∈ , there is a k-dimensional complex Ynk on n vertices that has strong spectral expansion properties (all nontrivial eigenvalues of the normalised k-dimensional Laplacian lie in the interval [1 − O(1/√n),1 + O(1/√n)]) but whose coboundary expansion is bounded from above by O(log n/n) and so tends to zero as n → ∞; moreover, Ynk can be taken to have vanishing integer homology in dimension less than k.

### 1 Introduction

Eigenvalues of graphs are a classical and well-studied subject, which goes back to a fundamental paper of Kirchhoﬀ [50], in which he used the combinatorial graph Laplacian to analyze electrical networks and formulated his celebrated Matrix-Tree Theorem for the number of spanning trees of a graph (which includes, as the special case of the complete graph, Cayley’s [9] famous formula nn−2 for the number of labeled trees on n vertices).

The eigenvalues of a graph G encode many important properties of G, in particular regarding connectivity and expansion properties of G (the mixing rate of a random walk on G) as well as other quasirandomness properties of G. Because of this, eigenvalues of graphs also play a major role in the design and analysis of algorithms, including heuristic and approximation algorithms for hard graph partitioning problems (spectral partitioning) and Markov Chain Monte Carlo approximation algorithms for hard counting problems. We cannot hope to survey the relevant

∗An extended abstract of this paper appeared at SoCG 2012. Research supported by the Swiss National Science Foundation (SNF Projects 200021-125309 and 200020-138230).

†Universit¨at zu Ko¨ln, Weyertal 86–90, 50923 K¨oln, Germany. anna.gundert@uni-koeln.de. Work on this paper was conducted at the Institut fu¨r Theoretische Informatik, ETH Z¨urich.

‡IST Austria, Am Campus 1, 3400 Klosterneuburg, Austria. uli@ist.ac.at.

literature here and refer the reader to the survey articles and monographs [12, 47, 53, 42, 54, 18, 70] for background and further references.

In the present paper, we consider eigenvalues of higher-dimensional simplicial complexes and, in a nutshell, prove two results: First, generalizing well-known results about random graphs G(n,p), we show (Theorem 2) that the Linial–Meshulam k-dimensional random complexes are asymptotically almost surely (a.a.s.), i.e., with probability tending to 1 as n → ∞, strongly spectrally expanding (their eigenvalues are strongly concentrated around two values). Second, we give a probabilistic construction (Theorem 4) of k-dimensional complexes that are strong spectral expanders but that fail to have the property of coboundary expansion — a generalization of edge expansion that arose in the recent work of Linial and Meshulam [55] and of Gromov [36]. This shows that the most straightforward attempt of generalizing the discrete Cheeger– Buser inequalities to higher-dimensional complexes fails and answers a question raised, e.g., by Dotterrer and Kahle [23]. Before stating these results more precisely, we ﬁrst recall the basic deﬁnitions and terminology.

###### Adjacency Matrix and Laplacians of Graphs

We recall the three (n×n)-matrices commonly associated with a graph1 G = (V,E) on n vertices. The adjacency matrix A = A(G) ∈ {0,1}V ×V has entries deﬁned by Au,v = 1 iﬀ {u,v} ∈ E. The combinatorial Laplacian is deﬁned as L = L(G) := D − A, where D = D(G) ∈ V ×V is the diagonal matrix with entries Dv,v = degG(v), the degrees of the vertices. Both of these are symmetric matrices and hence have a multiset of n real eigenvalues, called the spectrum.

The eigenvalues of A and of L turn out to be quite sensitive to the maximum and minimum degree of G. For graphs with very non-uniform degree distributions, it is often more convenient to consider the normalized Laplacian, which is deﬁned as ∆ = ∆(G) := D−1L = I −D−1A, where I ∈ V ×V is the identity matrix.2

The normalized Laplacian is not symmetric but corresponds to a self-adjoint operator on n with respect to a weighted inner product (see Section 2) and so also has n real eigenvalues. Both versions of the Laplacian are positive semideﬁnite relative to their respective inner products and so have nonnegative eigenvalues, typically listed in increasing order λ1(L) ≤ ... ≤ λn(L) and λ1(∆) ≤ ... ≤ λn(∆). The “all-1” vector 1 = (1,...,1)T satisﬁes L1 = ∆1 = 0, hence λ1(L) =

- λ1(∆) = 0, which is called the trivial eigenvalue. For the adjacency matrix, the eigenvalues are typically listed in decreasing order as µ1(A)≥...≥µn(A). Deﬁne µ(G) := max{µ2(A),|µn(A)|}.


The graph G is connected iﬀ λ2(L) > 0 iﬀ λ2(∆) > 0. More generally, the multiplicity of 0 as an eigenvector of either Laplacian equals the number of connected components of G, and if G is connected, then the second eigenvalue λ2 of either Laplacian controls the edge expansion of the graph (see the discussion below).

###### Eigenvalues of Random Graphs

Let G(n,p) be the binomial random graph on n vertices, for which every edge is included independently with probability p = p(n), and let d = p(n − 1) be the expected average degree. We summarize known concentration results on the spectra of G(n,p) as follows. See Section 2.2 for a more detailed account.

- 1Throughout this paper, we will assume that G is simple, i.e., we do not consider loops or multiple edges.
- 2Strictly speaking, D−1 is deﬁned only if there are no isolated vertices, i.e., if degG(v) > 0 for all v ∈ V , which will be the case of primary interest to us. If there are isolated vertices, we adopt the convention that Dv,v−1 = 0 whenever degG(v) = 0 and retain the deﬁnition ∆ = D−1L. (The second equation ∆ = I − D−1A no longer holds in this case, since ∆ has zero diagonal entries at isolated vertices.)


Sometimes, (e.g., in [13, 12, 16]) a slightly diﬀerent matrix is referred to as the normalized Laplacian, namely L := I − D−1/2AD−1/2. Assuming that there are no isolated vertices, ∆ and L have the same spectra, since ∆x = λx for some λ ∈ and x ∈ V iﬀ L y = λy, where y = D1/2x.

- Theorem 1 ([16, 26, 41]). For every c > 0 and every γ > c there exists a constant C > 0 such that for p ≥ (1 + γ) · log n/n and d = p(n − 1) the following statements hold with probability at least 1 − n−c:


- (i) µ1(A(G(n,p))) ∈ [d − C ·

√

d,d + C ·

√

d] and µ(G(n,p)) ≤ C ·

√

d;

- (ii) 1 − √Cd ≤λ2(∆(G(n,p)))≤...≤λn(∆(G(n,p)))≤1 + √Cd.


For the adjacency matrix (i) even holds for p ≥ γ · log n/n.

One type of application of such results is the analysis of spectral heuristics for algorithms that deal with random instances of NP-hard graph partitioning and related problems, see the discussions in [26, 16].

###### Higher-Dimensional Laplacians

Eckmann [25] introduced a generalization of the graph Laplacian L to higher-dimensional simplicial complexes X to study discrete boundary value problems on such complexes.

More precisely, let X be a ﬁnite simplicial complex and let Ci(X; ), i ∈ , be the vector space of i-dimensional simplicial cochains with real coeﬃcients (we refer to Section 2 for the necessary deﬁnitions). Eckmann deﬁnes three linear operators Ldowni (X), Lupi (X) and Li(X) = Ldowni (X) + Lupi (X) on the space Ci(X; ) and proves a discrete analogue of Hodge theory [39], which implies, in particular, that the subspace Hi(X) := kerLi(X) of so-called harmonic cochains on X is isomorphic to Hi(X; ), the i-th reduced cohomology.

In the case of a 1-dimensional simplicial complex (graph) G, Lup0 (G) coincides with the usual graph Laplacian L(G) discussed previously.

Subsequently, combinatorial Laplacians were applied in a variety of contexts. Dodziuk [19] and Dodziuk and Patodi [21] showed how the continuous Laplacian of a Riemannian manifold can be approximated by the combinatorial Laplacians of a suitable sequence of successively ﬁner triangulations of the manifold.

Kalai [48] used combinatorial Laplacians to prove a higher-dimensional generalization of Cayley’s formula for the number of labeled trees, and further results in this direction, including a generalization of the Matrix-Tree Theorem, were obtained in [1, 24]. For further combinatorial applications, see, e.g., [30, 29, 51, 22]. For further background and references regarding combinatorial Laplacians, see also [43].

We will mostly work with a normalized version of the Laplacian, ∆i(X) = ∆downi (X)+∆upi (X)

(see Section 2 for the deﬁnition) and focus on the operator ∆upk−1(X). Again, for graphs, ∆up0 (G) agrees with the normalized graph Laplacian ∆(G) discussed above.

###### Random Complexes

Linial and Meshulam [55] introduced a higher-dimensional analogue of the binomial random graph model G(n,p). By deﬁnition, the random k-dimensional complex Xk(n,p) has n vertices, a complete (k − 1)-skeleton (i.e., every subset of k of fewer vertices form a face of the complex), and every (k + 1)-element set of vertices is taken as a k-face independently with probability p, which may be constant or, more generally, a function p(n) depending on n.

This model has been studied extensively, and threshold probabilities for several basic topological properties of Xk(n,p) have been determined quite precisely, see e.g. [63, 7, 6, 14, 52, 69].

Our ﬁrst result is a higher-dimensional analogue of Theorem 1. The adjacency matrix of a k-dimensional complex X is denoted by Ak−1 (see Section 2.6 for the precise deﬁnition). Both Ak−1 and the normalized up-Laplacian ∆upk−1 have rows and columns indexed by the (k −1)-faces of X; we assume that X has n vertices and a complete (k − 1)-skeleton, so the matrices have dimension nk × nk . Ak−1 has entries in {0,±1}, and (Ak−1)F,G = ±1 (with appropriate signs) iﬀ F ∪ G is a k-face of X.

- Theorem 2. Let k ≥ 2. For every c > 0 and every γ > c there exists a constant C > 0 with the

following property: Assume p ≥ (k + γ)log(n)/n and let3 d := p(n − k). Then for γA = C ·

√

d and γ∆ = C/

√

d the following statements hold with probability at least 1 − n−c:

- (i) The largest nk−−11 eigenvalues of Ak−1(Xk(n,p)) lie in the interval [d−γA,d+γA], and the remaining n−k1 eigenvalues lie in the interval [−γA,+γA].
- (ii) The smallest nk−−11 eigenvalues of ∆upk−1(Xk(n,p)) are (trivially) zero, and the remaining n−1


k eigenvalues lie in the interval [1−γ∆,1+γ∆]. In particular, H˜k−1(Xk(n,p); ) = 0. For the adjacency matrix (i) even holds for p ≥ γ · log n/n.

Both concentration results are achieved by reducing the higher-dimensional problem to estimates for the eigenvalues of random graphs, i.e., to Theorem 1. For the Normalized Laplacian this is done by applying a fundamental estimate due to Garland [34] that relates the eigenvalues of the higher-dimensional matrix to those of the graphs that arise as links of (k − 2)-dimensional faces. For the generalized adjacency matrix we develop an analogous result (see Section 3).

Compared to the extended abstract [38] of this paper, Theorem 2 contains an improved concentration for the eigenvalues of Ak−1 in intervals of width O(

√

d) around the typical eigenvalues, as opposed to O(√dlog n).

Theorem 2 also applies to any other random model for simplicial complexes with n vertices and complete (k − 1)-skeleton in which the links of (k − 2)-faces are random graphs with distribution G(n−k+1,p). We use this for our second result, a probabilistic construction of a counterexample for a conjectural higher-dimensional discrete Cheeger inequality (Theorem 4 below).

Edge Expansion and the Cheeger Inequality for Graphs

For a graph of arbitrary density, its edge expansion can be deﬁned as follows. Let ε > 0 be a parameter. We say that G = (V,E) is ε-edge expanding if for every S ⊆ V ,

|E(S,V \ S)| |E|

≥ ε ·

min{|S|,|V \ S|} |V |

, (1)

where E(S,V \ S) = {{u,v} ∈ E : u ∈ S,v ∈ V \ S} is the set of edges across the cut (S,V \ S). Moreover, we call the best possible constant ε the edge expansion of G and denote it by ε(G).4 For a survey of the numerous applications of graph expansion in theoretical computer science and connections to other branches of mathematics, we refer to [42].

As mentioned above, the edge expansion of a graph is controlled by the second-smallest eigenvalue of its Laplacian. Here, we state this fact in its simplest form, for d-regular graphs (due to Dodziuk [20], Alon and Milman [4, 3]; Cheeger [10] proved an analogous result for Laplacians on Riemannian manifolds.). A version for non-regular graphs, with a slightly diﬀerent notion of edge expansion, can be found, e.g., in [12].

- Theorem 3 (Discrete Cheeger Inequality). Let G = (V,E) be a d-regular graph, and let λ2 =


- λ2(∆(G)) be the second-smallest eigenvalue of its normalized Laplacian. Then the edge expansion ε(G) satisﬁes


λ2 ≤ ε(G) ≤ 8λ2.

- 3Thus, d is the expected degree of any (k − 1)-face F in Xk(n, p), i.e., the expected number of k-faces incident to F.
- 4Note that (1) is equivalent, to the more common condition that |E(S, V \ S)| ≥ 2ε · d · |S| for all S ⊆ V with


|S| ≤ |V |/2, where d = 2|E|/|V | is the average degree. Thus, ε(G) = 2h(G), where h(G) := min{|E(S,Vd|S|\S)| : S ⊆ V, |S| ≤ |V |/2} is the (normalized) Cheeger constant of G.

The inequality on the left-hand side is proved fairly easily by expressing the characteristic function 1S ∈ V of a subset S ⊆ V as a linear combination of eigenvectors of the Laplacian ∆. We will refer to this as “the easy part of the Cheeger inequality.” The harder part is the inequality on the right-hand side. For a short proof see, e.g., [5].

We remark that even the easy part of the Cheeger inequality is very useful. For instance, essentially all explicit constructions of constant-degree expanders [60, 33, 57, 61, 67] prove a lower bound on the edge expansion of the constructed graphs by analyzing their eigenvalues.

###### Higher-Dimensional Expansion

Recently, a higher-dimensional analogue of edge-expansion of graphs, coboundary expansion (more precisely, 2-coboundary expansion), arose in the recent work of Gromov [36] and of Linial, Meshulam and Wallach [55, 63]. The precise deﬁnition will be given in Section 2. (For further related results, see, also [27, 49, 64, 62, 23].)

It is natural to ask whether there is a higher-dimensional analogue of the discrete Cheeger inequality; this question was raised explicitly, e.g., by Dotterrer and Kahle [23]. As our second result we show, by a simple probabilistic construction, that the most straightforward attempt at a higher-dimensional Cheeger inequality fails, even for the “easy part”. In higher dimensions, spectral expansion (an eigenvalue gap for the Laplacian) does not imply 2-coboundary expansion:

- Theorem 4. For every k > 1 there is an inﬁnite family of k-dimensional complexes (Ynk)n∈ , where Ynk has n vertices, that is spectrally but not coboundary expanding in dimension k.


More precisely, all nontrivial eigenvalues of ∆upk−1(Ynk) are 1 ± O(1/√n), but every Yn con-

tains a cochain a ∈ Ck−1(Yn; 2) of normalized Hamming weight [a] ≥ 12 − o(1) with δa = O(log n/n). Furthermore, Yn can be chosen such that Hi(Yn; ) = 0 for all i ≤ k − 1.

For a graph G and any abelian group , H˜0(G; ) = 0 iﬀ G is connected. In higher dimensions, however, it is well-known that the vanishing of a cohomology group may depend on the choice of coeﬃcients. A basic example for this is the real projective plane P2 for which H˜1( P2; ) = 0 but H˜1( P2; 2) = 2. In general, H˜1(Y ; ) = 0 iﬀ Y is ε-expanding, with respect to a given norm on -cochains, for some small ε > 0 that may depend on Y . Thus, the point of Theorem 4 is that there is an inﬁnite family of examples whose coboundary expansion tends to zero (as fast as log n/n) while the spectral expansion is bounded away from zero (in fact, equal to 1 ± O(1/√n)).

Compared to the extended abstract [38] of this paper, the probabilistic construction behind

Theorem 4 has been adapted to also allow for Hk−1(Yn; ) to be trivial. To inﬂuence the random behaviour we choose two probabilities p,q ≥ C ·log(n)/n for suitably large C with q = o(p). The construction then covers a whole range of parameters:

|fk(Yn) − p2 k+1 n | ≤ o(1)p2 k+1 n , δa = O

q p

,

while all nontrivial eigenvalues ∆upk−1(Yn) lie in the interval [1−γ,1+γ] with γ = O 1/ (p/2)n .

The concentration of eigenvalues is essentially optimal, as one can show5 that ∆upk−1(X) always has a non-trivial eigenvalue λ with 1 − λ ≥ k/dmax · (n − dmax)/(n − k), where dmax is the maximal degree of a k-face in X, and the expected degree in Yn is O((p/2)n).

In the extremal case q = C · log(n)/n and p = 1, we achieve a coboundary expansion of order O(log(n)/n) and eigenvalue concentration in [1 − O(1/√n),1 + O(1/√n)].

Of course it is just as natural to ask whether the other (“non-easy”) part of the Cheeger inequality has a simple higher-dimensional generalization. Even though any simplicial complex with non-zero 2-coboundary expansion has to have non-zero spectral expansion, it has been shown that also for this part of the Cheeger inequality no straight-forward generalization can

5This can be shown analogously to the corresponding bound (2) for graphs, see Preliminaries.

hold in higher dimensions: There is an inﬁnite family of simplicial k-balls Xn with spectral expansion O(1/log(n)log(k)) and coboundary expansion Ω(1/log(n)), see [68]. To the best of our knowledge, it is an open question whether there are complexes with coboundary expansion bounded away from zero and spectral expansion tending to zero.

###### Related Work

A recent article by Steenbergen, Klivans and Mukherjee [68] also presents a class of counterexamples for the most straightforward attempt at a higher-dimensional Cheeger inequality – an explicit construction for an inﬁnite family of simplicial k-balls Xn whose spectral expansion is bounded away from zero, while the coboundary expansion tends to zero. Here, the non-trivial eigenvalues of ∆upk−1(Xn) are bounded below by a constant depending on the dimension k, while the coboundary expansion of Xn is of order 1/Θ(log(n)). In the same article, the authors present the counterexample for simple higher-dimensional generalizations of the other (“non-easy”) part of the Cheeger inequality mentioned above.

Chung [11] studies a higher Laplacian for hypergraphs that is closely related6 to the com-

binatorial Laplacian Lk−1 = Lupk−1 + Ldownk−1 . In [11, Section 7], she proves a somewhat weaker concentration result for eigenvalues of random hypergraphs, namely, essentially, that for constant

p and any ε > 0, the eigenvalues of Lk−1(Xk(n,p)) are concentrated in an interval of width O(n1/2+ε). She also states, without proof, that the proof methods for random graphs can be extended to yield the sharp bound of O(√pn).

The probabilistic construction of the examples in Theorem 4 is well-known in the study of quasirandomness for hypergraphs, see, e.g., the discussion in [35, Section 5]. In [11, Section 8], it is asserted, again without proof, that the eigenvalues of the combinatorial Laplacian of these examples are concentrated in an interval of width O(√pn), but we are not aware of a proof appearing in the literature.

Hoﬀman, Kahle and Paquette prove closely related results in their preprint [41]. They improve previous results on eigenvalues of random graphs and achieve precise information about the constant factor in the threshold. Using a result by Zuk˙ [71], which is a strengthening of Garland’s estimate, they obtain as an immediate corollary that for p ≥ (2 + ε)lognn, the fundamental group of the random 2-complex X2(n,p) a.a.s. has Property (T).

Using a weaker combinatorial notion of higher-dimensional expansion, but the same notion of Laplacian spectra, Parzanchevski, Rosenthal and Tessler show a version of a higher-dimensional Cheeger inequality [66]. While 2-coboundary expanding complexes also possess this weaker notion of expansion, the converse is not true (see, e.g., [37], where an extension of their result is presented).

In another recent article, Lu and Peng [56] study a rather diﬀerent kind of Laplacian for random complexes. Speciﬁcally, given a k-dimensional complex X on a vertex set V and a parameter s ≤ k+12 , they consider an auxiliary weighted graph on the vertex set Vs in which I,J ∈ Vs are connected by an edge of weight w if I ∩ J = ∅ and I and J are contained in precisely w common k-faces of X. Lu and Peng study the normalized Laplacian of this auxiliary weighted graph. However, this Laplacian seems to capture the topology of X only in a limited way. For instance, in the case k = 2 and s = 1, any two 2-dimensional complexes on n vertices that have a complete 1-skeleton and are d-regular (every edge is contained in d triangles) yield the same auxiliary graph, even though the topologies of these complexes (as measured by real cohomology groups and the usual Laplacian, say) may be very diﬀerent.

6One diﬀerence is that Chung’s Laplacian operates not just on cochains, i.e., skew-symmetric functions on oriented simplices, but on arbitrary real-valued functions.

### 2 Preliminaries

##### 2.1 More on Eigenvalues of Graphs

It is known that the spectrum of the normalized Laplacian ∆ is contained in the interval [0,2], and that λn(∆) = 2 iﬀ G has a nontrivial bipartite connected component [12, Lemma 1.7]. Moreover, if G has no isolated vertices then λn−1(∆) ≥ n−n1.

If G is d-regular, i.e., degG(v) = d for all v ∈ V (where d may depend on n), then L = d·I −A = d·∆, and so the spectra of A, L, and ∆ are equivalent (up to scaling and linear shifts): λi(L) = d · λi(∆) and µi(A) = d − λi(L), 1 ≤ i ≤ n. In particular, µ1(A) = d, µ2(A) < d iﬀ G is connected, and µn(A) = −d iﬀ G has a nontrivial bipartite connected component.

For µ(G) = max{µ2(A),|µn(A)|}, it is not hard to show that for every d-regular graph

µ(G) ≥ d · (n − d)/(n − 1) (2) (see, e.g., [42, Claim 2.8]). Hence µ(G) ≥ Ω(

√

d) for d ≤ 0.99n, say, which shows that the concentration results for the eigenvalues of random graphs are essentially optimal. For constant d, one has the sharper Alon-Boppana bound µ(G) ≥ 2√d − 1 · (1 − O(1/log2 n)), see [65, 28].

A d-regular graph G is called a Ramanujan graph if it meets this bound for the spectral gap, i.e., if µ(G) ≤ 2√d − 1. It is a deep result due to Lubotzky, Phillips and Sarnak [57] and independently to Margulis [61] that for every ﬁxed number d with d − 1 prime, there exist Ramanujan graphs on n vertices for inﬁnitely many n (and moreover, these graphs can be explicitly constructed). Recently, the existence of bipartite Ramanujan graphs with arbitrary degree and arbitrary number of vertices has been established by Marcus, Spielman and Srivastava [58, 59].

##### 2.2 Eigenvalues of Random Graphs

In the introduction, Theorem 1 summarizes known results on the concentration of eigenvalues for random graphs G(n,p). Here we want to explain the corresponding references in more detail. For the normalized Laplacian the situation is simple: Building on the results for the adjacency matrix and relating the spectrum of ∆(G(n,p)) to that of A(G(n,p)), Coja-Oghlan [16] proved the result for the normalized Laplacian for probabilities p ≥ C ·log(n)/n with a suitable constant C. For p (log n)2/n this was also shown by Chung, Lu and Vu [13]. A recent preprint by Hoﬀman, Kahle and Paquette [41] gives the precise result allowing all constants C > 1 (and even C > 21 when considering only the giant component of G(n,p)).

For the adjacency matrix the situation in the literature is more involved: Fu¨redi and Koml´s [32] showed that for constant p a.a.s. µ(G(n,p)) = O(

√

d), where d = p(n−1) is the expected average degree. Their method of proof, the so-called trace method, can be adapted to cover the range

ln(n)7

7

n ≤ p ≤ 1 − ln(n)

n (see [15]). Feige and Ofek [26] extended the result to values of p as small as C · log n/n, but their proof requires an upper bound on p. They used methods of Friedman, Kahn, and Szemer´edi [31], who proved that µ(G) = O(

√

d) holds a.a.s. for random d-regular graphs with constant d. The most precise result is again by Hoﬀman, Kahle and Paquette [41], who show that µ(G(n,p)) = O(

√

d) a.a.s. for p ≥ γ log(n)/n for all γ > 0. More precisely, in [41] it is shown that a.a.s.

√

d) for all unit vectors x,y such that x ⊥ 1. (3) This, together with n1 A1,1 = 2|nE| ∈ [d − O(

| Ax,y | = O(

√

√

d)], which follows from a straightforward application of a Chernoﬀ bound, gives the result as stated in Theorem 1 (see e.g. [26, Lemma 2.1] or Lemma 12 in this paper).

d),d + O(

We remark that both parts of Theorem 1 can be extended to very sparse random graphs G(n,p) with p = Θ(1/n) (for which they fail to hold as stated) by passing to a suitable large core subgraph, see [16, 26, 41]. Moreover, analogous results are also known for other random graph models, including random d-regular graphs (see above) and random graphs with prescribed expected degree sequences [13, 17].

##### 2.3 Simplicial Complexes and Cohomology

A (ﬁnite, abstract) simplicial complex X is a ﬁnite set system that is closed under taking subsets, i.e. F ⊆ G ∈ X implies F ∈ X. The sets in X are called simplices or faces of X. The dimension of a face F is dim(F) := |F| − 1. We denote the set of i-dimensional faces of X by Xi. The dimension of X is the maximum dimension of any of its faces. The 0-dimensional faces are called vertices. Formally, these are singletons (one-element sets) but in this context we will usually identify the singleton {v} with its unique element v.

A k-dimensional simplicial complex is pure if all maximal simplices in X have dimension k. We deﬁne the degree of a face F as deg(F) = |{G ∈ Xk : F ⊆ G}|. The link of F in X is lk(F,X) := {G ∈ X : F ∪ G ∈ X,F ∩ G = ∅}. We denote by Knk the complete k-dimensional complex on n vertices, i.e. Knk = {F ⊆ [n] : |F| ≤ k + 1}.

Orientations and Incidence Numbers

Throughout we assume that we have ﬁxed a linear ordering on the vertex set V := X0 of X, and we consider the faces of X with the orientations given by the order of their vertices. Formally, consider an i-simplex F = {v0,v1,...,vi} ∈ Xi, where v0 < v1 < ... < vi. For an (i − 1)-simplex G ∈ Xi−1, we deﬁne the oriented incidence number [F : G] by setting [F : G] := (−1)j if G ⊆ F and F \ G = {vj}, 0 ≤ j ≤ i, and [F : G] := 0 if G  ⊆ F. In particular, for every vertex v ∈ X0 and the unique empty face ∅ ∈ X−1, we have [v : ∅] = 1.

Cohomology

Let X be a ﬁnite simplicial complex and let be an Abelian group (we will mostly be concerned with the cases = 2 and = , respectively). We denote by Ci(X; ) the group Xi of functions from Xi to , which are called i-dimensional cochains of X with coeﬃcients in . In particular, since ∅ is the unique empty face of X, we have C−1(X; ) ∼= . It is convenient to deﬁne Ci(X; ) := 0 for i < −1 or i > dimX. The characteristic functions eF of faces F ∈ Xi form a basis of Ci(X; ). They are called elementary cochains.

The coboundary map δi: Ci(X; ) → Ci+1(X, ) is the linear map given by (δif)(F) :=

[F : G] · f(G)

G∈Xi

for f ∈ Ci(X; ), −1 ≤ i < dimX, and δi = 0 otherwise.

It is an easy but central observation that the composition δi ◦ δi−1 = 0, which means that Bi(X; ) := imδi−1 ⊆ Zi(X; ) := kerδi. The elements of Bi(X; ) and Zi(X; ) are called i-dimensional coboundaries and cocycles, respectively. Since Bi(X; ) ⊆ Zi(X; ), we can form the quotient group H˜i(X; ) := Zi(X; )/Bi(X; ), the i-th (reduced) cohomology group of X with coeﬃcients in .

##### 2.4 Norms on Cochains and Expansion

We now describe a very general deﬁnition of expansion for simplicial complexes, which was introduced in [36] (with a slightly diﬀerent normalization and under the name inverse (co)ﬁlling norm).

Let X be a ﬁnite simplicial complex. Assume that every cochain group Ci(X; ) is equipped with a pseudonorm   ·  , taking real values and satisfying f =   − f and f + g ≤ f + g for all f,g ∈ Ci(X; ). We will focus on the following two cases.

- 1. -cochains with weighted 2-norm: Assume that we are given a weight function w with


nonnegative real values on the simplices of X. Deﬁne by f,g := F∈X

w(F)f(F)g(F) a weighted inner product on Ci(X; ). Observe that the inner products obtained in this way

i

are characterized by the condition that the elementary cochains be pairwise orthogonal. We then consider the corresponding weighted 2-norm f = f 2 := f,f .

###### 2. 2-cochains with weighted Hamming norm: Let w be as before and deﬁne the weighted

Hamming norm on Ci(X; 2) by f := F∈X

i:f(F)=1 w(F).

The idea is to deﬁne a notion of i-dimensional expansion that provides lower bounds for the norm of the coboundary δi−1(f) ∈ Ci(X; ) of (i − 1)-dimensional cochains f ∈ Ci−1(X; ). However, we cannot deﬁne such a lower bound in terms of the norm f of f, since the set Bi−1(X; ) is always contained in the kernel of the coboundary operator δ = δi−1. Thus, the right comparison measure is the distance of a cochain f from this trivial part of the kernel. That is, we deﬁne, for f ∈ Ci−1(X; ),

[f] := min{ f + δi−2g : g ∈ Ci−2(X; )}.

###### Coboundary Expansion for Arbitrary Coeﬃcients

Suppose every cochain group Ci(X; ) is equipped with a pseudonorm · as above. We say that X is ε-expanding in dimension i (with respect to and the given norm) if

δf ≥ ε · [f]

for all f ∈ Ci−1(X; ). The best possible ε is called the i-dimensional expansion of X. Note that, in particular, H˜i−1(X; ) = 0 if X has i-dimensional expansion ε > 0.

For an inﬁnite family of k-dimensional complexes (Xn)n∈ (where k is ﬁxed and independent of n) we say that the family (Xn) is expanding in dimension i (with respect to and the given norm) if the i-dimensional expansion of all Xn is bounded away from zero.

###### 2-Coboundary Expansion

Now we focus on the case of 2-coeﬃcients. Deﬁne a weight function by w(F) := 1/|Xi| for F ∈ Xi (whenever |Xi| > 0). In this setting, the normalized Hamming weight of a 2-cochain f ∈ Ci−1(X; 2) is just the number of faces in the support of f divided by the number of all (i − 1)-faces of X.

If X is is ε-expanding in dimension i with respect to this norm, we also say that X is 2coboundary ε-expanding in dimension i.

Note that in the case i = 1 of graphs, there are just two 0-dimensional coboundaries, namely the constant functions 0 and 1 on the set V = X0 of vertices. Moreover, a 0-dimensional cochain f ∈ C0(X; 2) is in bijective correspondence with its support S = {v ∈ V : f(v) = 1} ⊆ V , and

[f] = min{|S|V|,||V \S|}. Thus, 1-dimensional 2-coboundary expansion corresponds precisely to the deﬁnition (1) of edge expansion discussed in the introduction.

A basic observation in this context is that complete complexes are 2-coboundary expanding in all dimensions. This was observed independently by Gromov [36], Linial, Meshulam and Wallach [55, 63] and Newman and Rabinovich [64]:

Proposition 5. The complete complex Knk has i-dimensional 2-coboundary expansion 1 for all i ∈ {0,1,...,k}.

From this, standard Chernoﬀ bounds immediately imply that a.a.s., Xk(n,p) is 2-coboundary expanding in dimension k and Hk−1(Xk(n,p); 2) = 0 if p > C log n/n for a suitable constant C. Much of the work in [55, 63] is devoted to reﬁning this argument to obtain the optimal constant C = k for the threshold.

Dotterrer and Kahle [23] prove results analogous to Proposition 5 for some other complexes, speciﬁcally for skeleta of crosspolytopes and for complete multipartite complexes. They also

explicitly raise the question whether there is some higher-dimensional analogue of the Cheeger inequality. The most straightforward attempt at such an inequality would be to relate 2coboundary expansion and eigenvalue gaps of higher-dimensional Laplacians, which we discuss next.

##### 2.5 Matrices and their spectra

A symmetric real (n×n)-matrix has a multiset of n real eigenvalues, called its spectrum, and n has an orthonormal basis of corresponding eigenvectors.

We recall the variational characterization of eigenvalues:

Theorem 6 (Courant-Fischer Theorem, see e.g. [44, Theorem 4.2.11]). Let M ∈ n×n be a symmetric matrix with eigenvalues λ1 ≤ λ2 ≤ ... ≤ λn, and let k be a given integer with 1 ≤ k ≤ n. Then

Mx,x x,x and

λk = min

max

x =0,x∈ n x⊥w1,w2,...,wn−k

w1,w2,...,wn−k∈ n

Mx,x x,x

λk = max

min

.

x =0,x∈ n x⊥w1,w2,...,wk−1

w1,w2,...,wk−1∈ n

For a matrix M we denote ist 2-norm by M = maxx =0 Mx / x , which for a symmetric matrix M equals the in absolute value largest eigenvalue of M.

##### 2.6 Higher-Dimensional Laplacians and Adjacency Matrices

We introduce generalizations of the graph Laplacians and the adjacency matrix for a k-dimensional complex in all dimensions 0 ≤ i ≤ k − 1. Later on, we will only be concerned with these matrices in dimension k − 1.

###### Adjacency matrices

- For a ﬁnite k-dimensional simplicial complex X and 0 ≤ i ≤ k−1 we deﬁne the adjacency matrix Ai = Ai(X) by


(Ai(X))F,G = −[F ∪ G : F][F ∪ G : G] = [F : F ∩ G][G : F ∩ G] if F ∼ G, 0 otherwise,

where F,G ∈ Xi and we write F ∼ G if F and G share a common (i − 1)-face F ∩ G and F ∪ G ∈ Xi+1. Figure 1 illustrates the case i = 1. An entry A1(X)e,e is non-zero exactly if the two edges e and e share a common vertex and the triangle e ∪ e is contained in X. The sign of A1(X)e,e is then determined by the orientations of the two edges.

#### e

#### e e e

+1 +1 −1 −1

e

e e e

Figure 1: Signs of non-zero entries A1(X)e,e . The arrows represent the orientations of edges.

Note that the matrix A0(X) agrees with the adjacency matrix of the graph (X0,X1) because [{u,v} : u][{u,v} : v] = −1 for all vertices u,v ∈ X0. The motivation for the signs in higher dimensions will hopefully become clear later on.

###### Weighted Laplacians

Following the exposition in [43], we begin by deﬁning a general weighted Laplacian. Suppose we are given a nonnegative weight function w on the faces of a ﬁnite simplicial complex X and that the spaces Ci(X; ) are equipped with the weighted inner product and the corresponding weighted 2-norm as described above.

The elementary cochains eF, F ∈ Xi, form an orthogonal basis of Ci(X; ). With respect to these bases, the coboundary map δi: Ci(X; ) → Ci+1(X; ) is given by the following |Xi+1| × |Xi|-matrix (for which we abuse notation and again use the symbol δ):

(δi(X))F,G = [F : G].

Consider the transpose map δi∗: Ci+1(X; ) → Ci(X; ) of δi(X) with respect to the given inner product. This transpose is determined by the condition that δi∗f,g = f,δig for all f ∈ Ci+1(X; ) and g ∈ Ci(X; ). More explicitly,

- w(F)

- w(G)


(δi∗f)(G) =

[F : G]f(F)

F∈Xi+1

for f ∈ Ci+1(X; ) and G ∈ Xi.

For example, in the case of unit weights w(F) = 1 for all F ∈ X, we get the standard inner product on Ci(X; ), and δi∗ = ∂i+1 coincides with the usual boundary map given on elementary cochains by ∂i+1(eF) = G∈X

[F : G]eG, F ∈ Xi+1. In general, for arbitrary weights w on X, we deﬁne the weighted Laplacian by

i

Ldowni := δi−1δi∗−1, Lupi := δi∗δi, Li := Ldowni + Lupi .

Note that all three maps Ldowni ,Lupi ,Li are self-adjoint and positive semideﬁnite (with respect to the given weighted inner product) linear operators on Ci(X; ).

In general, setting Hi = Hi(X; ) := kerLi = kerLdowni ∩ kerLupi = kerδi∗−1 ∩ Zi(X; ), one gets a Hodge decomposition of Ci(X; ) into pairwise orthogonal subspaces

Ci(X; ) = Hi ⊕ Bi(X; ) ⊕ im(δi∗), (4) (see [25, 43]); in particular, Hi ∼= Hi(X; ).

###### Spectra of Lupi and Spectral Expansion

Observe that, trivially, Bi(X; ) ⊆ kerLupi . Thus, every f ∈ Bi(X; ) is an eigenvector of Lupi with eigenvalue zero. We call these the trivial eigenvectors of Lupi and the trivial part of its spectrum. Thus, the nontrivial eigenvalues of Lupi are, by deﬁnition, the eigenvalues of the restriction of Lupi to the orthogonal complement (with respect to the given weighted inner product) (Bi(X; ))⊥.

By the variational deﬁnition of eigenvalues, the minimal nontrivial eigenvalue of Lupi is given by

 Lupi f,f f,f

δif 2 f 2

min

= min

.

f⊥Bi(X; )

f⊥Bi(X; )

Thus, we see that the minimal nontrivial eigenvalue of Lupi is at least ε2 iﬀ X has (i + 1)dimensional expansion at least ε with respect to the given weighted 2-norms on real cochains. In this case, we will also say that X is spectrally expanding in dimension i.

We focus on the operator Lupi , more precisely we consider Lupk−1 for k-dimensional complexes because it corresponds to coboundary expansion with respect to real coeﬃcients and the 2-norm.

The spectra of the other two maps are related: By the Hodge decomposition (4) the spectrum of Li is determined by the spectra of Ldowni and Lupi . For any linear map A, the spectra of AA∗ and A∗A diﬀer only in the multiplicity of 0; in particular, this holds for the spectra of Lupi and Ldowni+1 . Nevertheless, as we cover only Lupk−1 for k-dimensional complexes, our results do not yield corresponding statements on Lk−1.

###### Combinatorial Laplacians

The combinatorial Laplacian Li = Ldowni + Lupi corresponds to the special case of the standard inner product f,g = f∈X

f(F)g(F), that is, the case of unit weights w(F) = 1 for all F ∈ X. Thus, Lupi = Lupi (X) = ∂i+1δi.

i

Recall that the matrix corresponding to the coboundary map δi with respect to the orthogonal basis of elementary cochains is, by abuse of notation, also denoted by δi = δi(X), and its transpose δiT corresponds to the boundary map ∂i+1. The combinatorial Laplacian Lupi can be expressed as the matrix δiTδi.

We can now motivate the signs in the deﬁnition of the adjacency matrix Ai(X): Recall that for a graph G the combinatorial Laplacian satisﬁes L(G) = D(G) − A(G). If we let Di(X) denote the diagonal matrix with entry DiF,F = |{H ∈ Xi+1 : F ⊂ H}| for F ∈ Xi, we also have Lupi (X) = Di(X) − Ai(X).

###### Normalized Laplacians

Suppose that X is a pure k-dimensional simplicial complex. The normalized Laplacian ∆i = ∆downi +∆upi is the special case of the weighted Laplacian obtained by taking the weight function w(F) := deg(F). That is, the corresponding weighted inner product is

f,g =

deg(F)f(F)g(F).

F∈Xi

Let δi∗ be the adjoint of δi with respect to this weighted inner product. Thus,

- deg(F)

- deg(G)


(δi∗f)(G) =

[F : G]f(F).

F∈Xi+1

Note that we have deg(F) > 0 for every F ∈ X, since we assume that X is pure. The normalized Laplacian is then ∆upi = ∆upi (X) = δi∗δi.

With respect to the basis of elementary cochains, the map ∆upi corresponds to the matrix Wi−1δiTWi+1δi, where Wi(X) denotes the diagonal matrix with entry WiF,F = deg(F). As Wk−1 = Dk−1 and Wk = I, for i = k − 1 we can write ∆upk−1 as the matrix Dk−−11Lupk−1 = I − Dk−−11Ak−1.

###### Eigenvalues of the Complete Complex

As an example we consider the spectra of the three matrices Lupk−1(Knk), ∆upk−1(Knk) and Ak−1(Knk) for the complete complex Knk. First recall the following well-known (and easily veriﬁable) lemma:

- Lemma 7. For a complex X with complete (k − 1)-skeleton, the space B(k−1)(X) = imδk−2 has dimension nk−−11 . A basis is given by δk−2eF : 1 ∈/ F ∈ k [−n]1 . For the complete complex Knk, the space imδk∗−1(Knk) is n−k1 -dimensional and has δk∗−1eF :1 ∈ F ∈ k [+1n] as a basis.
- Lemma 8. The eigenvalues of the combinatorial Laplacian Lupk−1(Knk) are 0 with multiplicity n−1 k−1 and n with multiplicity n−k1 . The normalized Laplacian ∆upk−1(Knk) has eigenvalues 0 with


multiplicity nk−−11 and n−nk with multiplicity n−k1 . The eigenvalues of Ak−1(Knk) are n − k with multiplicity nk−−11 and −k with multiplicity n−k1 .

Proof. Because Knk is (n − k)-regular, it suﬃces to consider the spectrum of Lupk−1(Knk). The following equality is contained implicitly in [48] and follows from a straightforward calculation

using the matrix representations of the Laplacians:

Lupk−1(Knk) + Ldownk−1 (Knk) = nI.

Any non-zero element of kerLdownk−1 (Knk) = kerδk∗−2(Knk) = imδk∗−1(Knk) is hence an eigenvector of Lupk−1 with eigenvalue n. Naturally, any non-zero element of kerLupk−1(Knk) = Zk−1(Knk) = Bk−1(Knk) is an eigenvector of Lupk−1 with eigenvalue 0. By Lemma 7 imδk∗−1(Knk) and Bk−1(Knk) have dimensions n−k1 and nk−−11 , respectively. As these add up to nk , the dimension of Ck−1(Knk), we have determined the complete spectrum.

| |
|---|


### 3 Garland’s Estimate Revisited

In [34] Garland studies the normalized Laplacian ∆upi (X). His main result regards a conjecture of Serre’s on the cohomology of certain groups. As a technical lemma, he proves a bound for

the nontrivial eigenvalues of ∆upi (X) in terms of the eigenvalues of the Laplacian on links of lower-dimensional faces (see also [8] for a very clear exposition).

We state the result for the case of ∆upk−1(X) and the links of (k−2)-dimensional faces F ∈ Xk−2. In this case, lkF = lk(F,X) is a graph and the normalized Laplacian ∆up0 (lkF) agrees with the usual normalized graph Laplacian ∆(lkF). Furthermore, we show an analogous result for the generalized adjacency matrix Ak−1(X).

For a combinatorial application of Garland’s ideas (to clique complexes of graphs) see [2]. Garland’s estimate was subsequently further strengthened and extended. In particular, Zuk˙ [71] proved that if a 2-dimensional complex X satisﬁes λ2(∆(lk(v,X))) > 1/2 for all vertex links, then the fundamental group of X has Kazhdan’s Property (T).

##### Normalized Laplacian

Theorem 9 ([34], see also [8, Theorem 1.5,1.6]). Let X be a pure k-dimensional complex and let ∆upk−1 = ∆upk−1(X) be its normalized Laplacian. Denote by , the weighted inner product on Ck−1(X; ) that is deﬁned by f,g = F∈X

deg(F)f(F)g(F). Assume that for all F ∈ Xk−2 λmin ≤ λ2(∆(lkF)) ≤ λn−k+1(∆(lkF)) ≤ λmax.

k−1

Then for all f ∈ Bk−1(X)⊥ (where the orthogonal complement is taken with respect to , ) (1 + kλmin − k) f,f ≤ ∆upk−1f,f ≤ (1 + kλmax − k) f,f . Hence, all nontrivial eigenvalues of ∆upk−1 on Bk−1(X)⊥ lie in [1 + kλmin − k,1 + kλmax − k].

We remark that Garland only states the lower bound. The upper bound follows directly from the proof, which we reproduce here in our notation. The main idea of the proof is to present the normalized Laplacian as a sum of matrices each of which has non-zero entries only on the link of some (k − 2)-face. These matrices then correspond to the Laplacians of the links.

For a pure k-dimensional simplicial complex X, ﬁx a face F ∈ Xk−2 of dimension k − 2. Let ρF be the diagonal |Xk−1| × |Xk−1|-matrix deﬁned by

(ρF)G,H =

1 if G = H and F ⊂ G, 0 otherwise.

We set ∆upk−,F1 (X) := ρF∆upk−1(X)ρF and for f ∈ Ck−1(X) furthermore deﬁne fF ∈ C0(lkF) by fF({u}) = [F ∪ {u} : F]f(F ∪ {u}).

Lemma 10. Let X be a pure k-dimensional complex.

- a) F∈X

k−2

∆upk−,F1 (X) = ∆upk−1(X) + (k − 1)I.

- b) For u,v ∈ V (lkF) let Fu = F ∪ {u} and Fv = F ∪ {v}. Then (∆upk−,F1 (X))Fu,Fv = [Fu : F][Fv : F](∆(lkF))u,v. So, for f ∈ Ck−1(X), ∆upk−,F1 (X)f,f = ∆(lkF)fF,fF .


- c) If f ∈ Bk−1(X)⊥ then fF ∈ 1⊥.


Proof. a) Observe that ∆upk−,F1 (X) is obtained by replacing by 0 all entries of ∆upk−1(X) that are contained in a row or column corresponding to some G with F G. The non-zero entries of ∆upk−1(X) lie on the diagonal or correspond to faces G,H ∈ Xk−1 that share a common (k − 2)-face and for which G ∪ H ∈ Xk. Hence, every non-zero entry (∆upk−1(X))G,H with G = H is contained in exactly one summand and the diagonal entries, which are 1, are each contained in exactly k summands.

- b) First consider u = v with F∪{u,v} ∈ X. Straightforward calculations show that degX(Fu) =

deglkF(u) and that furthermore [Fu,v : Fu][Fu,v : Fv] = −[Fu : F][Fv : F] where Fu,v stands for F ∪ {u,v}. Hence,

(∆upk−,F1 (X))Fu,Fv =

[Fu,v : Fu][Fu,v : Fv] degX(Fu)

= −

[Fu : F][Fv : F] deglkF(u)

= [Fu : F][Fv : F](∆(lkF))u,v.

If F ∪ {u,v} ∈/ X, the corresponding entry is 0 in both matrices. For the diagonal entries we get

(∆upk−,F1 (X))Fu,Fu = 1 = [Fu : F][Fu : F]∆(lkF)u,u.

- c) Let f ∈ Bk−1(X)⊥. Then G∈X


deg(G)f(G)[G : F] = f,δk−2eF = 0 and therefore

k−1

deglkF(v)fF({v}) =

fF,1 =

deg(Fv)[Fv : F]f(Fv) = 0.

v∈V (lk F)

v∈V (lk F)

| |
|---|


The statements of Lemma 10 can easily be combined to prove Garland’s estimate: Proof of Theorem 9. Let f ∈ Bk−1(X)⊥. Then

∆upk−,F1 (X)f,f =

∆(lkF)fF,fF ,

F∈Ff

F∈Xk−2

where Ff = {F ∈ Xk−2|F ⊂ G for some G with f(G) = 0}. Now, since f ∈ Bk−1(X)⊥, we have fF ∈ 1⊥ and fF = 0 for F ∈ Ff. As furthermore F∈F

fF,fF = k f,f ,

f

∆upk−,F1 (X)f,f ≤ kλmax f,f . By Lemma 10 we have furthermore

kλmin f,f ≤

F∈Xk−2

∆upk−,F1 (X)f,f − (k − 1) f,f , which concludes the proof.

∆upk−1(X)f,f =

F∈Xk−2

| |
|---|


##### Adjacency Matrix

We now turn to the generalized adjacency matrix Ak−1(X). The same methods as above can be applied to achieve a result of similar nature (Proposition 13). However, this only enables us to cover vectors from Bk−1(X)⊥. Controlling the behaviour on this space suﬃced for the normalized Laplacian, where Bk−1(X) is always a subspace of the eigenspace of zero. For the generalized adjacency matrix we know much less about its eigenspaces, in particular we do not know of any trivial eigenvalues.

This is analogous to the situation for graphs, where 1, the all-ones vector, which is known to be the ﬁrst eigenvector of the Laplacian (with eigenvalue 0), is not necessarily an eigenvector of

the adjacency matrix. In [26] Feige and Ofek, considering the adjacency matrix of random graphs G(n,p), show that for p large enough the ﬁrst eigenvector can in some sense be replaced by 1. Following their strategy, we show that controlling the behaviour of the generalized adjacency matrix Ak−1(X) on the two spaces Bk−1(X) and Bk−1(X)⊥ suﬃces to give concentration results for the spectrum of Ak−1(X).

The results of this section together will yield the following theorem which can be considered as an analogue of Garland’s Theorem 9 for the generalized adjacency matrix Ak−1(X).

Theorem 11. Let X be a k-dimensional simplicial complex with n vertices and complete (k−1)skeleton and let Ak−1 = Ak−1(X) be its generalized adjacency matrix. Fix a positive value d and let u = (1/√n − k + 1)1. Suppose that we have for all F ∈ Xk−2:

- (i) | A(lkF)u,u − d| ≤ f(n),
- (ii) | A(lkF)u,w | ≤ g(n) for all w⊥1 with w = 1 and
- (iii) | A(lkF)w,w | ≤ h(n) for all w⊥1 with w = 1. Let ϕ(n) = f(n) + g(n) + h(n). Then:


- (a) | Ak−1b,b − d| ≤ k · ϕ(n) for all b ∈ Bk−1(X) with b = 1,
- (b) | Ak−1b,z | ≤ k · ϕ(n) for all z ∈ Bk−1(X)⊥ and b ∈ Bk−1(X) with b = z = 1 and
- (c) | Ak−1z,z | ≤ k · h(n) for all z ∈ Bk−1(X)⊥ with z = 1.


Hence, the largest nk−−11 eigenvalues of Ak−1 lie in the interval [d − kϕ(n),d + 2kϕ(n) + kh(n)], and the remaining n−k1 eigenvalues lie in the interval [−k(ϕ(n) + h(n)),kh(n)].

The following lemma explains the connection of Conclusions (a), (b) and (c) with the spectrum

of Ak−1(X). It is a generalization of [26, Lemma 2.1], which gives the a corresponding statement for graphs and deals with a single vector u, here replaced by the subspace B, and is then used

with u = √1n1. We will use B = Bk−1(X). Note that Bk−1(X) = Bk−1(Knk) if X has a complete (k − 1)-skeleton.

Lemma 12. Let X be a k-dimensional simplicial complex with n vertices and complete (k − 1)skeleton, let Ak−1 = Ak−1(X) be its generalized adjacency matrix and let B be an nk−−11 -dimensional subspace of Ck−1(X). Suppose we have:

- (i) 0 ≤ f1(n) ≤ Ak−1b,b ≤ f2(n) for all b ∈ B with b = 1,
- (ii) | Ak−1b,z | ≤ g(n) for all z ∈ B⊥ and b ∈ B with b = z = 1 and
- (iii) | Ak−1z,z | ≤ h(n) for all z ∈ B⊥ with z = 1.


Then the largest nk−−11 eigenvalues of Ak−1 lie in the interval [f1(n),f2(n) + g(n) + h(n)], and the remaining n−k1 eigenvalues lie in the interval [−(g(n) + h(n)),h(n)].

Proof of Lemma 12. Write A = Ak−1. Let v be an arbitrary unit vector. Then there are unit vectors b ∈ B, z ∈ B⊥ and −1 ≤ α,β ≤ 1 such that v = αb + βz and α2 + β2 = 1. Because A is symmetric, we get

Av,v = α2 Ab,b + 2αβ Ab,z + β2 Az,z . Using (i),(ii) and (iii) as well as αβ ≤ 1/2 and 0 ≤ α,β ≤ 1, we can conclude that

−g(n) − h(n) ≤ Av,v ≤ f2(n) + g(n) + h(n).

Hence, all eigenvalues of A are contained in [−g(n) − h(n),f2(n) + g(n) + h(n)]. Now, let µ1 ≤ µ2 ≤ ... ≤ µ(nk) be the eigenvalues of A. Applying (i) and (iii) we get

µ(n−k1) ≤ max

Az,z ≤ h(n) and µ(n−k1)+1 ≥ min

Ab,b ≥ f1(n),

z∈B⊥, z =1

b∈B, b =1

by the variational characterization of eigenvalues (Theorem 6), since dimB⊥ = n−k1 .

| |
|---|


The proof of Theorem 11 makes up the remainder of this section and is divided into two parts. We ﬁrst deal with Conclusion (c) and then turn to Conclusions (a) and (b).

##### Conclusion (c) - Behaviour on Bk−1(X)⊥

We address Conclusion (c) with the same methods that we used to prove Garland’s Theorem 9.

- Proposition 13. Let X be a k-dimensional complex and let Ak−1 = Ak−1(X) be its generalized adjacency matrix. Assume that for all F ∈ Xk−2 and for all w ∈ C0(lkF) with w⊥1


| A(lkF)w,w | ≤ h(n) w,w .

Then for all z ∈ Bk−1(X)⊥ (where the orthogonal complement is taken with respect to the standard, non-weighted inner product)

| Ak−1z,z | ≤ k · h(n) z,z .

Proof. For any face F ∈ Xk−2 set AFk−1 := ρFAk−1ρF, the matrix obtained from Ak−1 by replacing all rows and columns corresponding to (k − 1)-faces not containing F by all-zero rows/columns.

Similar as in Lemma 10, straightforward calculations show:

- a) F∈X

k−2

AFk−1 = Ak−1,

- b) (AFk−1)F∪{u},F∪{v} = [F ∪ {u} : F][F ∪ {v} : F]A(lkF)u,v for F ∈ Xk−2 and u,v ∈ V (lkF) and hence AFk−1f,f = A(lkF)fF,fF for any f ∈ Ck−1(X).


As z ∈ Bk−1(X)⊥ implies zF ∈ 1⊥ also with respect to the non-weighted inner product, this proves the proposition:

| Ak−1z,z | = |

F∈Xk−2

AFk−1z,z | ≤

| A(lkF)zF,zF | ≤ k · h(n) z,z .

F∈Xk−2

| |
|---|


As explained above, in contrast to the Laplacian, for the adjacency matrix we are also interested in the behaviour on Bk−1(X). For this space, we can not apply a proof similar to the one above because f ∈ Bk−1(X) does not imply that fF is constant for every F ∈ Xk−2. (For

- a k-dimensional complex with complete (k − 1)-skeleton, the basis vectors δk−2eF are a simple counterexample.)


##### Conclusions (a) and (b) - Behaviour on Bk−1(X)

- For b ∈ Bk−1(X) we have Ak−1(X)b = Dk−1(X)b. If the complex X was regular, i.e. all (k − 1)faces would have the same degree d, Bk−1(X) would be a subspace of the eigenspace of d.


The random complex Xk(n,p) is not regular but with high probability the degrees of all (k − 1)-faces lie close to the expected average degree d = p(n − 1). For an arbitrary complex we can ﬁx any positive value d and study the divergences of the degrees from d by considering the diagonal matrix E(X) = Dk−1(X) − dI which has entries E(X)F,F = degX(F) − d. Then Ak−1(X)b = E(X)b + db for b ∈ Bk−1(X).

It will turn out that our main task is to control the behaviour of E(X)b for all b ∈ Bk−1(X). We manage to reduce this to a question on the links of (k − 2)-faces: Proposition 14 relates

E(X)b for every b ∈ Bk−1(X) to the values E(X)δk−2eF for F ∈ Xk−2, to the behaviour of E(X) on the coboundaries of elementary cochains. These values in turn match the values

E(lkF)1 on the corresponding links.

- Proposition 14. Let X be a k-dimensional complex with vertex set [n] and complete (k − 1)skeleton. Fix some positive value d and let E = E(X) = Dk−1(X) − dI. Assume that for all F ∈ Xk−2 we have


EδeF ≤ f(n) δeF . Then for all b ∈ Bk−1(X)

Eb ≤ k · f(n) b .

Remark 15. Proposition 14 also holds if E is replaced by any diagonal |Xk−1| × |Xk−1|-matrix.

The proof of Proposition 14 is deferred to the end of this section. Here is how we use it to address Conclusions (a) and (b). Proposition 16. Let X be a k-dimensional simplicial complex with n vertices and complete (k − 1)-skeleton. Fix some postive value d and suppose that we have

(deglk(F)(v) − d)2 = E(lkF)1 2 ≤ f(n)2(n − k + 1)

v∈V (lk F)

for all F ∈ Xk−2. Then

- (i) | Ak−1b,b − d| ≤ k · f(n) for all b ∈ Bk−1(X) with b = 1 and
- (ii) | Ak−1b,z | ≤ k · f(n) for all b ∈ Bk−1(X), z ∈ Bk−1(X)⊥ with b = z = 1.


Proof. As deg(F ∪ {v}) = deglkF(v) for v ∈/ F, we have EδeF 2 =

(deg(H) − d)2 =

(deglkF(v) − d)2 ≤ f(n)2(n − k + 1).

H⊃F

v/∈F

By Proposition 14 we hence have Eb ≤ k · f(n) b for all b ∈ Bk−1(X). Now, let b ∈ Bk−1(X) and z ∈ Bk−1(X)⊥. As Ak−1b = Dk−1b = db + Eb, we get

| Ak−1b,b − d b 2| ≤ b · Eb ≤ k · f(n) b 2 and

| Ak−1b,z | ≤ | Eb,z | ≤ z · Eb ≤ k · f(n) z b .

| |
|---|


To conclude the proof of Theorem 11 we are missing a small lemma:

- Lemma 17. Let G be a graph with n vertices with adjacency matrix A = A(G) and let u = √1n1. Fix a positive value d. Assume that


- (i) | Au,u − d| ≤ f(n),
- (ii) | Au,w | ≤ g(n) for all w⊥1 with w = 1 and
- (iii) | Aw,w | ≤ h(n) for all w⊥1 with w = 1. Then E(G)1 2 = v∈V (deg(v) − d)2 ≤ (f(n) + g(n) + h(n))2n. Proof. We have E(G)1 = (ndJ − A)1 ≤ n dJ − A · 1 and the conditions above imply


- d nJ − A ≤ f(n) + g(n) + h(n).


| |
|---|


###### Proof of Proposition 14

The proof of Propositon 14 is based on the observations in the following lemma. Its proof will use the following simple consequence of the Cauchy-Schwarz inequality:

2

a2i. (5)

###### ≤ |I|

ai

i∈I

i∈I

- Lemma 18. Let X be a k-complex with vertex set [n] and complete (k − 1)-skeleton and let


- b ∈ Bk−1(X). For every (k − 2)-face F ∈ Xk−2 deﬁne


Then

hb(F) :=

[F ∪ {v} : F]b(F ∪ {v}).

v/∈F

- a) b(H) = n1 F⊂H,F∈X

k−2

[H : F]hb(F) for H ∈ Xk−1,

- b) Eb,Eb ≤ nk2 F∈Xk−2 hb(F)2 EδeF,EδeF ,

- c) F∈X


hb(F)2 ≤ k(n − k + 1) b,b . Proof. a) As X has a complete (k − 1)-skeleton, we have b ∈ Bk−1(X) = Bk−1(Knk) and

k−2

δk−1(Knk)b = 0. Thus, for any H ∈ Xk−1 and v ∈/ H: 0 = (δk−1(Knk)b)(H ∪ {v}) = [H ∪ {v} : H]b(H) +

[H ∪ {v} : F ∪ {v}]b(F ∪ {v}).

F⊂H

Note that −[H ∪{v} : H][H ∪{v} : F ∪{v}] = [H : F][F ∪{v} : F]. Thus, we can rearrange: b(H) = −[H∪{v} : H]

[H∪{v} : F∪{v}]b(F∪{v}) =

[H : F][F∪{v} : F]b(F∪{v}).

F⊂H

F⊂H

Summing over all v ∈/ H and adding additional multiples of b(H), we get

n · b(H) =

[H : F][F ∪ {v} : F]b(F ∪ {v}) + k · b(H)

v/∈H F⊂H

[F ∪ {v} : F]b(F ∪ {v}) =

=

[H : F]

F⊂H

v/∈F

[H : F]hb(F).

F⊂H

- b) By a) and inequality (5) and because EδeF,EδeF = H⊃F E(H)2 for F ∈ Xk−2:

Eb,Eb =

H∈Xk−1

E(H)2b(H)2 =

1 n2 H∈X

k−1

E(H)2

F⊂H

[H : F]hb(F)

2

≤

k n2 H∈X

k−1

E(H)2

F⊂H

hb(F)2 =

k n2 F∈X

k−2

hb(F)2 EδeF,EδeF .

- c) Again by inequality (5):


hb(F)2 ≤

F∈Xk−2

b(F ∪ {v})2

(n − k + 1) ·

F∈Xk−2

v/∈F

= (n − k + 1) ·

H∈Xk−1

k · b(H)2 = k(n − k + 1) b,b .

| |
|---|


The statements of Lemma 18 together yield Proposition 14: Proof of Propositon 14. Let b ∈ Bk−1(X). As δeF = √n − k + 1 for F ∈ Xk−2, by Lemma 18: Eb,Eb ≤

k n2 F∈X

k n2 F∈X

hb(F)2 EδeF,EδeF ≤

hb(F)2f(n)2 δeF,δeF

k−2

k−2

(n − k + 1)2 n2 · f(n)2 b,b ≤ k2 · f(n)2 b,b .

≤ k2 ·

| |
|---|


### 4 The Spectra of Random Complexes

In this section, we prove Theorem 2, the concentration result on the spectra of the normalized Laplacian and the generalized adjacency matrix of random complexes Xk(n,p). The basic idea is to reduce the statement to a question on the links of (k − 2)-faces by applying Theorems 9 and 11. Since for every (k − 2)-face F, the link lk(F,Xk(n,p)) is a random graph with the same distribution as G(n − k + 1,p), we can then apply results on the eigenvalues of random graphs. For convenience, we repeat Theorem 2:

Theorem 2. Let k ≥ 2. For every c > 0 and every γ > c there exists a constant C > 0 with the following property: Assume p ≥ (k + γ)log(n)/n and let d := p(n − k). Then for γA = C ·

√

d and γ∆ = C/

√

d the following statements hold with probability at least 1 − n−c:

- (i) The largest nk−−11 eigenvalues of Ak−1(Xk(n,p)) lie in the interval [d−γA,d+γA], and the remaining n−k1 eigenvalues lie in the interval [−γA,+γA].
- (ii) The smallest nk−−11 eigenvalues of ∆upk−1(Xk(n,p)) are (trivially) zero, and the remaining n−1


k eigenvalues lie in the interval [1−γ∆,1+γ∆]. In particular, H˜k−1(Xk(n,p); ) = 0. For the adjacency matrix (i) even holds for p ≥ γ · log n/n.

Observe that Bk−1(Knk) ⊆ ker∆upk−1(Xk(n,p)) because Xk(n,p) has a complete (k − 1)skeleton, so the multiplicity of 0 as an eigenvalue of ∆upk−1(Xk(n,p)) is at least nk−−11 .

Proof of Theorem 2. Let c > 0 and let γ > c. For F ∈ k [−n]1 , the link lkF = lk(F,Xk(n,p)) is a random graph G(n−k +1,p). By Theorem 1 (and (3) in Section 2.2) we can hence choose C > 0

such that for p ≥ (k + γ)log(n)/n the following holds with probability at least 1 − n−c−k+1:

- (i) | Ax,y | ≤ C

√

d for all unit vectors x,y with x ⊥ 1 and n−1k+1 A1,1 ∈ [d−C

√

d,d+C

√

d].

- (ii) All nontrivial eigenvalues of ∆(lkF) are contained in the interval [1−C/(k


√

√

d)]. We ﬁrst focus on the adjacency matrix: A union bound yields that for p ≥ (k + γ)log(n)/n:

d),1+C/(k

√

√

d for some x ⊥ 1,y ≤ n−c.

Pr ∃F ∈ Xk−2 : |n−1k+1 A1,1 − d| > C

d or | Ax,y | > C

√

d), and hence the desired concentration bounds, are fulﬁlled with probability at least 1 − n−c. Note that so far by Theorem 1 it would have suﬃced to choose p ≥ γ log(n)/n.

This implies that the conditions of Theorem 11 with f(n),g(n),h(n) = O(

Now consider the normalized Laplacian. Again, a union bound gives for p ≥ (k + γ)log(n)/n

√

√

d)] ≥ 1 − n−c.

Pr ∀F ∈ Xk−2 : 1 − C/(k

d) ≤ λ2(∆(lkF)) ≤ λn−k+1(∆(lkF)) ≤ 1 + C/(k

For every (k − 1)-face H ∈ [nk] of Xk(n,p), the random variable deg(H) is binomially distributed with parameters (n − k) and p. So, for n large enough, the complex Xk(n,p) is pure with probability at least 1 − n−c. Hence, also the conditions of Theorem 9 are fulﬁlled with probability at least 1 − n−c.

| |
|---|


Remark 19. Note that that the preceding proof works for any random distribution Xk(n,p) on k-dimensional simplicial complexes with n vertices and complete (k − 1)-skeleton with the

property that the link lk(F,Xk(n,p)) of every F ∈ k [−n]1 is a random graph with distribution G(n − k + 1,p).

### 5 Spectral vs. Coboundary Expansion

In this section, we prove Theorem 4. As mentioned in the introduction, the examples are obtained by a probabilistic construction.

###### Basic Construction

Denote by Y k(n,p) the random k-dimensional simplicial complex with vertex set V = [n] and complete (k − 1)-skeleton obtained as follows: Randomly choose a map a: Vk → 2 by setting a(F) = 1 with probability 1/2 and a(F) = 0 otherwise, independently for each F ∈ Vk . Thus, the support of a has the same distribution as the (k − 1)-faces of the Linial-Meshulam random complex Xk−1(n,1/2).

Call H ∈ k V+1 “good” iﬀ H contains an even number of (k − 1)-faces F with a(F) = 1. Every good H is added as a k-face to Y k(n,p) independently with probability p. Note that, by construction, a is a 2-cocycle in the complex Y k(n,p), i.e., a ∈ Zk−1(Y k(n,p); 2).

(Vk)

For any ﬁxed b ∈ Ck−1(Y k(n,p); 2) =

2 , the expected normalized Hamming distance between b and the randomly chosen a equals 1/2. Since there are fewer than 2(k−n1) coboundaries b ∈ Bk−1(Y k(n,p); 2) and nk independent random choices for the entries of a, a straightforward application of a Chernoﬀ bound (see, e.g., [45, Theorem 1], [46, Theorem 2.1]) plus a union bound implies that, a.a.s., a has normalized Hamming distance 1/2 − o(1) from any coboundary, i.e.,

[a] ≥ 1/2 − o(1). In particular, a.a.s. H˜k−1(Y k(n,p), 2) = 0.

Note that for H ∈ k V+1 , the probability that H is a k-face of Y k(n,p) equals p/2. However, in contrast to the model Xk(n,p/2), the decisions for diﬀerent k-faces that share some (k−1)-face are not independent. Nevertheless, we can still easily analyze the links of (k−2)-faces in Y k(n,p):

Lemma 20. For every (k−2)-face H ∈ (Y k(n,p))k−2 = k V−1 , the random graph lk(H,Y k(n,p)) has the distribution G(n − k + 1,p/2). Proof. First note that it suﬃces to consider the case p = 1, because lk(H,Y k(n,p)) carries the distribution attained by taking every edge in lk(H,Y k(n,1)) independently with probability p.

For simplicity, we write Y instead of Y k(n,1). Let U := V \ H. For e ∈ U2 , consider the event that e ∈ lk(H,Y ), i.e., that H ∪ e ∈ Y . We need to show that these events are mutually independent. To see this, choose and ﬁx, for each e ∈ U2 , an arbitrary (k − 1)-simplex Fe with

- e ⊆ Fe ⊆ H ∪e; we call these the “undecided” (k −1)-simplices, and let D := Vk \{Fe: e ∈ U2 } be the set of remaining, “decided” (k − 1)-simplices. Note that, by construction, each k-simplex


of the form H ∪ e, e ∈ U2 , contains exactly one undecided (k − 1)-simplex Fe and that these are pairwise distinct. Fix a map r: D → 2 and condition upon the event that r is the restriction of

a to D. For each e ∈ U2 , we have e ∈ lk(H,Y ) iﬀ a(Fe) = F∈D,F⊂H∪e r(F). For a ﬁxed r, the (conditional) probability of this happening is 1/2, and the values a(Fe) are mutually independent

since the Fe are pairwise distinct. Thus, for any set of edges e1,...,e ∈ U2 and for any ﬁxed r, we get the conditional probability Pr[∀i : ei ∈ lk(H,Y ) | a|D = r] = (1/2) . Since this holds for all choices of r, it also holds unconditionally, which proves the lemma.

| |
|---|


For p ≥ (k+γ)log(n)/n with γ > 0 we can thus, by this lemma and Remark 19, proceed as in the proof of Theorem 2 to show that there exists γ∆ = O(1/√pn) such that a.a.s. the nontrivial part of the spectrum of ∆upk−1(Y k(n,p)) lies in the interval [1 − γ∆,1 + γ∆].

###### Modiﬁcation

We have so far shown the existence of an inﬁnite family of k-dimensional complexes that is spectrally but not 2-coboundary expanding. However, the complexes constructed have nontrivial cohomology groups H˜k−1(Y, 2), and hence also H˜k−1(Y, ) = 0, because a is a 2-cocycle by construction.

To change this we can add a second round to our experiment and randomly add possible further k-simplices as follows: After constructing Y k(n,p), we add each H ∈ k V+1 independently with some probability q. We denote the obtained random complex by Zk(n,p,q). Thus, Zk(n,p,q) is the union of Y k(n,p) and the Linial-Meshulam random complex Xk(n,q). We assume that p,q ≥ C · log(n)/n for some suitably chosen C.

To analyze the 2-coboundary expansion of Z = Zk(n,p,q), we ﬁrst argue that Z, a.a.s., contains at least p2(1 − o(1)) k+1 n many k-faces:

fk(Zk(n,p,q)) ≥ p2(1 − o(1)) k+1 n . Applying the second moment method it is not hard to see that the number of good k-faces, after choosing a, is at least 21(1−o(1)) k+1 n with probability tending to 1. A Chernoﬀ bound then tell us that a.a.s. fk(Y k(n,p)) ≥ p2(1 − o(1)) k+1 n . As Y k(n,p) is a subcomplex of Z, this yields the desired bound. With a similar argument, also applying a Chernoﬀ bound, we get that a.a.s.

|δa| ≤

q 2

(1 − o(1))

n k + 1

.

As we have [a] ≥ 1/2 − o(1) with the same probability as before, we see that a.a.s.

δa a

q p

ε(Z) ≤

= O

= o(1),

if q = o(p). In the extremal case q = C · log(n)/n and p = 1, we achieve ε(Z) = O(log(n)/n).

Furthermore, since Z has Xk(n,q) as a subcomplex, we know that the groups H˜k−1(Z, 2) and H˜k−1(Z, ) are a.a.s. trivial if q ≥ C · log n/n for C suﬃciently large (see [40, 55, 63]).

For the analysis of the spectrum of ∆upk−1(Z), we can again consider the links of (k − 2)-faces.

For H ∈ k V−1 , the random graph lk(H,Z) is the union of lk(H,Y k(n,p/2)) and lk(H,Zk(n,q)). Hence, it has the distribution G(n−k+1,r) with r = p/2+q−pq/2, the union of G(n−k+1,p/2)

and G(n − k + 1,q). As r ≥ p/2, we see that also for this construction, a.a.s., the nontrivial part of the spectrum of the normalized Laplacian ∆upk−1(Z) lies in the interval [1 − γ∆,1 + γ∆] with γ∆ = O(1/√rn).

###### Acknowledgements

The second author is grateful to Roy Meshulam for helpful discussions during which, in particular, he learned about Garland’s results. We would also like to thank Matt Kahle and the referees of this paper and of the extended abstract for helpful comments.

### References

- [1] R. M. Adin. Counting colorful multi-dimensional trees. Combinatorica, 12(3):247–260, 1992.
- [2] R. Aharoni, E. Berger, and R. Meshulam. Eigenvalues and homology of ﬂag complexes and vector representations of graphs. Geom. Funct. Anal., 15(3):555–566, 2005.
- [3] N. Alon. Eigenvalues and expanders. Combinatorica, 6(2):83–96, 1986.
- [4] N. Alon and V. D. Milman. λ1, Isoperimetric inequalities for graphs, and superconcentrators. J. Combin. Theory Ser. B, 38(1):73–88, 1985.
- [5] N. Alon, O. Schwartz, and A. Shapira. An elementary construction of constant-degree expanders. Combin. Probab. Comput., 17(3):319–327, 2008.
- [6] L. Aronshtam, N. Linial, T.  Luczak, and R. Meshulam. Collapsibility and vanishing of top homology in random simplicial complexes. Discrete Comput. Geom., 49:317–334, 2013.
- [7] E. Babson, C. Hoﬀman, and M. Kahle. The fundamental group of random 2-complexes. J. Amer. Math. Soc., 24(1):1–28, 2011.
- [8] A. Borel. Cohomologie des certains groupes discrets et Laplacien p-adique. In S´eminaire Bourbaki, Expose´ 437, volume 431 of Lecture Notes in Math., pages 12–35. Springer, 1973.
- [9] A. Cayley. A theorem on trees. Quart. J. Pure Appl. Math., 23:376–378, 1889. Collected Mathematical Papers Vol. 13, Cambridge Univ. Press, 1897, 26–28.
- [10] J. Cheeger. A lower bound for the smallest eigenvalue of the Laplacian. In Problems in analysis (Papers dedicated to Salomon Bochner, 1969), pages 195–199. Princeton Univ. Press, Princeton, N. J., 1970.
- [11] F. Chung. The Laplacian of a Hypergraph, volume 10 of DIMACS Ser. Discrete Math. Theoret. Comput. Sci., pages 21–36. Amer. Math. Soc., 1993.
- [12] F. Chung. Spectral graph theory, volume 92 of CBMS Reg. Conf. Ser. Math. Amer. Math. Soc., 1997.
- [13] F. Chung, L. Lu, and V. Vu. The spectra of random graphs with given expected degrees. Internet Math., 1(3):257–275, 2003.
- [14] D. Cohen, A. Costa, M. Farber, and T. Kappeler. Topology of random 2-complexes. Discrete Comput. Geom., 47:117–149, 2012.
- [15] A. Coja-Oghlan. Spectral techniques, semideﬁnite programs, and random graphs. Habilitationsschrift, 2005.
- [16] A. Coja-Oghlan. On the Laplacian eigenvalues of Gn,p. Combin. Probab. Comput., 16(6):923– 946, 2007.
- [17] A. Coja-Oghlan and A. Lanka. The spectral gap of random graphs with given expected degrees. Electron. J. Combin., 16(1):R138, 2009.
- [18] D. Cvetkovi´c, P. Rowlinson, and S. Simi´c. An introduction to the theory of graph spectra, volume 75 of London Math. Soc. Stud. Texts. Cambridge Univ. Press, Cambridge, 2010.
- [19] J. Dodziuk. Finite-diﬀerence approach to the Hodge theory of harmonic forms. Amer. J. Math., 98(1):79–104, 1976.


- [20] J. Dodziuk. Diﬀerence equations, isoperimetric inequality and transience of certain random walks. Trans. Amer. Math. Soc., 284(2):787–794, 1984.
- [21] J. Dodziuk and V. K. Patodi. Riemannian structures and triangulations of manifolds. J. Indian Math. Soc. (N.S.), 40(1-4):1–52 (1977), 1976.
- [22] X. Dong and M. L. Wachs. Combinatorial Laplacian of the matching complex. Electron. J. Combin., 9(1):Research Paper 17, 11, 2002.
- [23] D. Dotterrer and M. Kahle. Coboundary expanders. J. Topol. Anal., 4(4):499–514, 2012.
- [24] A. M. Duval, C. J. Klivans, and J. L. Martin. Simplicial matrix-tree theorems. Trans. Amer. Math. Soc., 361(11):6073–6114, 2009.
- [25] B. Eckmann. Harmonische Funktionen und Randwertaufgaben in einem Komplex. Comment. Math. Helv., 17:240–255, 1945.
- [26] U. Feige and E. Ofek. Spectral techniques applied to sparse random graphs. Random Structures Algorithms, 27(2):251–275, 2005.
- [27] J. Fox, M. Gromov, V. Laﬀorgue, A. Naor, and J. Pach. Overlap properties of geometric expanders. J. Reine Angew. Math., 671:49–83, 2012.
- [28] J. Friedman. Some geometric aspects of graphs and their eigenfunctions. Duke Math. J., 69(3):487–525, 1993.
- [29] J. Friedman. Computing Betti numbers via combinatorial Laplacians. Algorithmica, 21(4):331–346, 1998.
- [30] J. Friedman and P. Hanlon. On the Betti numbers of chessboard complexes. J. Algebraic Combin., 8(2):193–203, 1998.
- [31] J. Friedman, J. Kahn, and E. Szemer´edi. On the second eigenvalue of random regular graphs. In Proc. 21st Ann. ACM Symp. Theor. Comput., STOC ’89, pages 587–598, New York, 1989. ACM.
- [32] Z. Fu¨redi and J. Koml´s. The eigenvalues of random symmetric matrices. Combinatorica, 1(3):233–241, 1981.
- [33] O. Gabber and Z. Galil. Explicit constructions of linear-sized superconcentrators. J. Comput. System Sci., 22(3):407–420, 1981.
- [34] H. Garland. p-adic curvature and the cohomology of discrete subgroups of p-adic groups. Ann. of Math. (2), 97(3):375–423, 1973.
- [35] W. T. Gowers. Quasirandomness, counting and regularity for 3-uniform hypergraphs. Combin. Probab. Comput., 15(1-2):143–184, 2006.
- [36] M. Gromov. Singularities, expanders and topology of maps. Part 2: From combinatorics to topology via algebraic isoperimetry. Geom. Funct. Anal., 20(2):416–526, 2010.
- [37] A. Gundert and M. Szedl´k. Higher dimensional discrete cheeger inequalities. Journal Comput. Geom., 6(2), 2015.
- [38] A. Gundert and U. Wagner. On Laplacians of random complexes. In Proc. 28th Ann. Symp. Comput. Geom. (SoCG), pages 151–160, 2012.
- [39] W. V. D. Hodge. The Theory and Applications of Harmonic Integrals. Cambridge Mathematical Library. Cambridge Univ. Press, Cambridge, 1989.


- [40] C. Hoﬀman, M. Kahle, and E. Paquette. The threshold for integer homology in random d-complexes. Preprint, arXiv:1308.6232, 2013.
- [41] C. Hoﬀman, M. Kahle, and E. Paquette. Spectral gaps of random graphs and applications to random topology. Preprint, arXiv:1201.0425, 2014.
- [42] S. Hoory, N. Linial, and A. Wigderson. Expander graphs and their applications. Bull. Amer. Math. Soc. (N.S.), 43(4):439–561 (electronic), 2006.
- [43] D. Horak and J. Jost. Spectra of combinatorial Laplace operators on simplicial complexes. Advances in Mathematics, 244:303 – 336, 2013.
- [44] R. A. Horn and C. R. Johnson. Matrix Analysis. Cambridge University Press, 1985.
- [45] S. Janson. On concentration of probability. In B. Bollob´s, editor, Contemporary Combinatorics, volume 10 of Boly. Soc. Math. Stud., pages 289–301. Springer, 2002.
- [46] S. Janson, T.  Luczak, and A. Rucin´ski. Random Graphs. Wiley-Intersci. Ser. in Discrete Math. Optim. Wiley, 2000.
- [47] M. Jerrum. Counting, sampling and integrating: algorithms and complexity. Lectures Math. ETH Zu¨rich. Birkh¨user, Basel, 2003.
- [48] G. Kalai. Enumeration of Q-acyclic simplicial complexes. Israel J. Math., 45:337–351, 1983.
- [49] R. N. Karasev. A Simpler Proof of the Boros-Fu¨redi-B´r´ny-Pach-Gromov Theorem. Discrete Comput. Geom., 47(3):492–495, 2012.
- [50] G. Kirchhoﬀ. Ueber die Auﬂ¨sung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Str¨me gefu¨hrt wird. Ann. Phys., 148(12):497–508, 1847.
- [51] W. Kook, V. Reiner, and D. Stanton. Combinatorial Laplacians of matroid complexes. J. Amer. Math. Soc., 13(1):129–148, 2000.
- [52] D. Kozlov. The threshold function for vanishing of the top homology group of random d-complexes. Proc. Amer. Math. Soc., 138(12):4517–4527, 2010.
- [53] M. Krivelevich and B. Sudakov. Pseudo-random graphs. In More sets, graphs and numbers, volume 15 of Bolyai Soc. Math. Stud., pages 199–262. Springer, 2006.
- [54] D. A. Levin, Y. Peres, and E. L. Wilmer. Markov chains and mixing times. Amer. Math. Soc., 2009.
- [55] N. Linial and R. Meshulam. Homological connectivity of random 2-complexes. Combinatorica, 26(4):475–487, 2006.
- [56] L. Lu and X. Peng. Loose Laplacian spectra of random hypergraphs. Random Structures Algorithms, 41(4):521–545, 2012.
- [57] A. Lubotzky, R. S. Phillips, and P. Sarnak. Ramanujan graphs. Combinatorica, 8(3):261–277, 1988.
- [58] A. W. Marcus, D. A. Spielman, and N. Srivastava. Interlacing families I: Bipartite Ramanujan graphs of all degrees. Ann. of Math., 182(1):307–325, 2015.
- [59] A. W. Marcus, D. A. Spielman, and N. Srivastava. Interlacing Families IV: Bipartite Ramanujan Graphs of All Sizes. Preprint, arXiv:1505.08010, 2015.


- [60] G. A. Margulis. Explicit constructions of expanders. Problemy Peredaˇci Informacii, 9(4):71– 80, 1973.
- [61] G. A. Margulis. Explicit group-theoretic constructions of combinatorial schemes and their applications in the construction of expanders and concentrators. Problemy Peredachi Informatsii, 24(1):51–60, 1988.
- [62] J. Matousˇek and U. Wagner. On Gromov’s Method of Selecting Heavily Covered Points. Discrete Comput. Geom., 52(1):1–33, 2014.
- [63] R. Meshulam and N. Wallach. Homological connectivity of random k-dimensional complexes. Random Structures Algorithms, 34(3):408–417, 2009.
- [64] I. Newman and Y. Rabinovich. On multiplicative λ-approximations and some geometric applications. In Proc. 23rd Ann. ACM-SIAM Symp. Discrete Algorithms. SIAM, 2011.
- [65] A. Nilli. On the second eigenvalue of a graph. Discrete Math., 91(2):207–210, 1991.
- [66] O. Parzanchevski, R. Rosenthal, and R. J. Tessler. Isoperimetric inequalities in simplicial complexes. Combinatorica, pages 1–33, 2015.
- [67] O. Reingold, S. Vadhan, and A. Wigderson. Entropy waves, the zig-zag graph product, and new constant-degree expanders. Ann. of Math. (2), 155(1):157–187, 2002.
- [68] J. Steenbergen, C. Klivans, and S. Mukherjee. A Cheeger-type inequality on simplicial complexes. Adv. in Appl. Math., 56:56–77, 2014.
- [69] U. Wagner. Minors in random and expanding hypergraphs. In Proc. 27th Ann. Symp. Comput. Geom. (SoCG), pages 351–360, 2011.
- [70] X.-D. Zhang. The Laplacian eigenvalues of graphs: a survey. Preprint, arXiv:1111.2897v1, 2011.
- [71] A. Zuk.˙ La propri´et´e (T) de Kazhdan pour les groupes agissant sur les poly`edres. C. R. Acad. Sci. Paris, 323:453–458, 1996.


