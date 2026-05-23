arXiv:1608.05705v1[math.CO]19Aug2016

EXACT RAMSEY NUMBERS OF ODD CYCLES VIA NONLINEAR OPTIMISATION

MATTHEW JENSSEN†, JOZEF SKOKAN†‡

Abstract. For a graph G, the k-colour Ramsey number Rk(G) is the least integer N such that every k-colouring of the edges of the complete graph KN contains a monochromatic copy of G. Let Cn denote the cycle on n vertices. We show that for ﬁxed k ≥ 2 and n odd and suﬃciently large,

Rk(Cn) = 2k−1(n − 1) + 1. This resolves a conjecture of Bondy and Erdo˝s [J. Combin. Th. Ser. B 14 (1973), 46–54] for large n. The proof is analytic in nature, the ﬁrst step of which is to use the regularity method to relate this problem in Ramsey theory to one in nonlinear optimisation. This allows us to prove a stability-type generalisation of the above and establish a surprising correspondence between extremal k-colourings for this problem and perfect matchings in the k-dimensional hypercube Qk.

1. Introduction

One of the most well-known and extensively researched problems in combinatorics is that of determining the Ramsey numbers of graphs, deﬁned as follows. Given graphs G1, G2, . . ., Gk, the Ramsey number R(G1, . . ., Gk) is the least integer N such that any colouring of the edges of the complete graph KN on N vertices with k colours contains a monochromatic copy of Gi in the i-th colour for some i, 1 ≤ i ≤ k. In the case where G1, . . ., Gk are all isomorphic to the graph G, we call R(G1, . . ., Gk) the k-colour Ramsey number of G and denote it by Rk(G). Broadly speaking the philosophy underpinning Ramsey theory is that large, potentially highly disordered structures must contain ordered substructures.

Ramsey theory owes its name to the seminal paper of Frank Ramsey [Ram30] where it is shown that Ramsey numbers are ﬁnite. The oldest and most famous examples of Ramsey numbers are those involving cliques. The systematic study of such Ramsey numbers began with a paper of Erd˝os and Szekeres [ES35] who considered the problem of determining R2(Kk), where Kk denotes the clique on k vertices. Erd˝os and Szekeres [ES35] and Erd˝os [Erd47] showed that 2k/2 ≤ R2(Kk) ≤ 4k. The problem of improving these bounds has gained signiﬁcant notoriety and only small improvements have been made over the last eighty years. In the case where the graphs in question are sparse in some sense (e.g. they have bounded maximum degree), the situation seems somewhat simpler. The cycle on n vertices Cn was one of the earliest subjects in the study of Ramsey numbers of sparse graphs.

![image 1](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile1.png>)

Date: August 22, 2016.

†Department of Mathematics, London School of Economics, Houghton Street, London WC2A 2AE, U.K. E-mail: {m.o.jenssen|j.skokan}@lse.ac.uk.

‡Department of Mathematics, University of Illinois at Urbana-Champaign, 1409 W. Green Street, Urbana, IL 61801, USA.

The behaviour of the Ramsey number R(Cn

) has been studied and fully determined by several authors, including Bondy and Erd˝os [BE73], Faudree and Schelp [FS74], and Rosta [Ros73]. For example it is known that

, Cn

1

2

- 2n − 1, if n ≥ 5 is odd,
- 3n


R2(Cn) =

2 − 1, if n ≥ 6 is even.

![image 2](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile2.png>)

Results such as this one that exactly determine R(G1, G2) for a pair of graphs G1, G2 are by now fairly plentiful. See Radziszowski [Rad94] for an excellent survey of such results. However, in the case where more than two colours are involved such results are still rather rare. The only non-trivial class of graphs for which the k-colour Ramsey number is exactly determined for arbitrary k is that of matchings (a result due to Cockayne and Lorimer [CL75]). In this paper we address the following conjecture attributed to Bondy and Erd˝os [BE73].

Conjecture 1.1. If k ≥ 2 and n > 3 is odd then Rk(Cn) = 2k−1(n − 1) + 1.

Note that the conjecture deals speciﬁcally with the case where n is odd. Odd and even cycles behave rather diﬀerently in this context due to the fact that an even cycle is bipartite whereas an odd cycle is not. We mention that Erd˝os and Graham [EG75] proved the bounds

(1.1) 2k−1(n − 1) + 1 ≤ Rk(Cn) ≤ (k + 2)!n, for all k ≥ 2 and all odd n > 3. In this paper we prove the following. Theorem 1.2. For any ﬁxed k ≥ 2 and odd n suﬃciently large,

Rk(Cn) = 2k−1(n − 1) + 1.

We therefore resolve Conjecture 1.1 for large n. We will in fact prove a stability-type strengthening of this result (see Theorem 3.2 below). Very recently Day and Johnson [DJ16] showed that in the opposite regime, where we ﬁx an odd n and let k be suﬃciently large, one in fact has Rk(Cn) > (n − 1)(2 + ε)k−1 for some ε = ε(n) > 0, and so Conjecture 1.1 is false when n is small with respect to k. The qualiﬁcation that n is suﬃciently large in Theorem 1.2 is therefore necessary, however due the use of compactness arguments in the proof, we obtain no eﬀective bound on how large n must be with respect to k.

In view of Theorem 1.2, let us call a k-colouring of the complete graph on 2k−1(n − 1) vertices which does not contain a monochromatic copy of Cn an extremal k-colouring. The lower bound in (1.1) was established by observing that one can naturally construct extremal k-colourings by induction. Indeed if there exists a k-colouring of the edges of the complete graph Km with no monochromatic Cn, then by joining two such copies of Km by edges of colour k + 1, one obtains a (k + 1)-colouring of K2m with no monochromatic Cn. The base construction, for k = 1, is simply a monochromatic clique of size n − 1. It was believed that all extremal k-colourings come from such a doubling argument. We show that this is not the case, providing a classiﬁcation of extremal k-colourings which exposes a surprising correspondence between extremal k-colourings and perfect matchings in the k-dimensional hypercube Qk.

The ﬁrst breakthrough towards Conjecture 1.1 was made by  Luczak [ Luc99] who used the regularity method to show that the k = 3 case holds asymptotically i.e. that for n odd,

R3(Cn) = 4n + o(n) as n → ∞.

 Luczak’s method of applying regularity in this setting has proven extremely fruitful (see e.g. [F L07a, GRSS07, KSS05,  Luc99,  LSS12]) and has since become a standard tool. We will come to describe the method in more detail as it provides the starting point for the present paper.

Building on  Luczak’s ideas, Kohayakawa, Simonovits and Skokan [KSS05] paired the regularity method with stability arguments to resolve Conjecture 1.1 for k = 3 and n large. The case where k ≥ 4 has since remained open. Progress was made by  Luczak, Simonovits and Skokan [ LSS12] who showed that for k ≥ 4 and odd n,

Rk(Cn) ≤ k2kn + o(n) as n → ∞.

To conclude this section we give a broad overview of the proof method of Theorem 1.2. Let Gn denote the (ﬁnite) class of all cliques that admit a k-colouring with no monochromatic copy of Cn. Determining Rk(Cn) is then equivalent to determining the maximum N such that KN ∈ Gn. Using the regularity method, we relate this problem to ﬁnding the maximum ℓ1-norm of an element in a certain compact subset S of R3k. This allows us to import analytic and topological tools in support of our proof. The relation is such that maximal elements of S correspond to extremal k-colourings for Theorem 1.2. Moreover by classifying the extremal points of S we can classify the extremal k-colourings and prove a stability type strengthening of Theorem 1.2, generalising the main result from [KSS05]. We show that each perfect matching of the hypercube Qk gives rise to a class of extremal k-colourings. On the other hand, any extremal k-colouring must be ‘close’ to one such construction. We defer precise statements to the Section 3. The number of essentially diﬀerent classes of extremal k-colourings is equal to the number of equivalence classes of perfect matchings in Qk with respect to its automorphism group and this number is doubly exponential in k. Such a plethora of extremal constructions is usually forbidding when trying to establish stability type results, we believe that the fact we can overcome this obstacle is largely down to the analytic perspective.

2. Notation and Terminology Let us collect some notation that we use throughout the paper. For k ∈ N, we let [k]

denote the set {1, . . ., k}. For a set S, we let S2 denote the set of all unordered pairs of distinct elements of S.

All graphs considered here will be ﬁnite. For a graph G = (V, E), we let v(G) = |V | and e(G) = |E|. For v ∈ V , we let NG(v) denote the neighbourhood of v in G and let δ(G) denote the minimum degree of G. For X ⊆ V we denote by G[X] the subgraph of G induced by the vertices of X. For disjoint subsets A, B ⊆ V , we denote by G[A, B] the bipartite graph with vertex set A ∪ B and edge set {{a, b} ∈ E : a ∈ A, b ∈ B}, and we let eG(A, B) denote the size of this set. In the case where A = {v} a singleton, we write G[v, B] instead of G[{v}, B]. All subscripts in the above notation may be suppressed if they are clear from the context. At times we may slightly abuse notation by writing v ∈ G and {x, y} ∈ G in lieu of v ∈ V (G) and {x, y} ∈ E(G) respectively.

Let W = w0w1 . . .wℓ be a walk in G (that is a sequence of vertices w0, w1, . . .wℓ such that {wi, wi+1} is an edge of G for all i < ℓ). If all of the wi are distinct then we call W a path of length ℓ. We may also refer to W as a w0wℓ-path to distinguish its endpoints. If all the wi are distinct except w0 = wℓ then we call W a cycle of length ℓ. We will also concatenate walks in the natural way. For example if U = u0 . . .um is a walk in G such that um = w0, we let UW denote the walk u0 . . .umw1 . . .wℓ. If x is a vertex such that {wℓ, x} is an edge of G then we let Wx denote the walk w0 . . .wℓx.

A k-coloured graph is a graph G = (V, E) equipped with some function ϕ : [k] → E. Furthermore, for i ∈ [k], we let Gi denote the subgraph (V, ϕ−1{i}) of G. We call Gi the ith colour class of G. For a digraph F and vertex v ∈ V (F), we let d−(v), d+(v) denote the indegree and outdegree of v respectively.

For x ∈ Rd we let x denote the ℓ1-norm of x i.e. x = di=1|xi|. Furthermore, given ε > 0, we let Bε(x) := {z ∈ Rd : z − x0 < ε}, the open ball of radius ε centred at x. We let supp(x) denote the support of x.

In the statements of theorems and lemmas it will be useful to use the notation α ≪ β to mean that there is an increasing function α(x) so that the statement is valid for 0 < α < α(β). When we need to refer to this function at a later stage, we include the number of the lemma (or theorem) the function appears in as a subscript. For example, δ8.3(x) denotes the implied function δ(x) from Lemma 8.3. Throughout the paper we omit the use of ﬂoor and ceiling symbols where they are not crucial.

3. A Graph Decomposition, Extremal Colourings and Stability

In this section we describe the extremal colourings and give precise statements of the stability results referred to in the Introduction. We also introduce some key concepts and results that will be used throughout the paper and give a more detailed overview of our proof methods. We begin by introducing a way of decomposing an arbitrary k-coloured graph. This decomposition will play a central role for us and is similar to a decomposition introduced in [ LSS12].

- 3.1. A Graph Decomposition. Let G be a k-coloured graph. For each i ∈ [k], we write

Gi = G′i ∪ G′′i , where G′i is the union of the bipartite components of Gi and G′′i is the union of the non-bipartite components of Gi. For each i ∈ [k], write V (G′i) = V0i ∪ V1i where V0i and V1i are the vertex classes of a bipartition of G′i and set V∗i = V (G′′i ). For τ ∈ {0, 1, ∗}k, let Vτ = kj=1 Vτj

j

and note that V (G) =

τ∈{0,1,∗}k

Vτ, a disjoint union.

We call (Vτ : τ ∈ {0, 1, ∗}k) a proﬁle partition of G and we call the corresponding vector (|Vτ| : τ ∈ {0, 1, ∗}k) a proﬁle of G. We will often denote a proﬁle of G by x(G). Note that G may admit multiple proﬁle partitions since we made an arbitrary choice in choosing the bipartition V (G′i) = V0i ∪ V1i for each i ∈ [k].

- 3.2. Extremal Colourings and the Hypercube. For k ∈ N, we let Qk denote the kdimensional hypercube i.e. the graph on vertex set {0, 1}k and edge set consisting of pairs


diﬀering in exactly one coordinate. It will be useful to think of an element τ ∈ {0, 1, ∗}k as a subcube of the k-dimensional hypercube Qk via the correspondence

τ ↔ Q(τ) := {c ∈ {0, 1}k : cj = τj if τj ∈ {0, 1}}.

In other words we think of a coordinate j where τj = ∗ as a ‘missing bit’ and let Q(τ) be the set of all possible ways of ﬁlling in these bits. For example,

if k = 3 and τ = (0, ∗, ∗), then Q(τ) = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1)}. We deﬁne the weight of τ to be the size of the set {i ∈ [k] : τi = ∗} (i.e. the number of missing bits) and denote it by ω(τ). Note that |Q(τ)| = 2ω(τ). In the language of the hypercube, ω(τ) is the dimension of the subcube Q(τ). In particular if ω(τ) = 1, then we think of Q(τ) as an edge of Qk.

We can now describe a class of extremal k-colourings in terms of perfect matchings in Qk. Let M be a perfect matching of Qk. We express each edge of M as an element (of weight 1) of {0, 1, ∗}k. Let G = KN where N = 2k−1(n − 1) and let V (G) = τ∈M Vτ be a partition of V (G) where |Vτ| = n − 1 for all τ ∈ M. For each τ ∈ M, colour all edges in G[Vτ] with the colour i, where i is the coordinate for which τi = ∗. For τ, σ ∈ M, arbitrarily colour the edges between Vτ and Vσ with any colour j for which {σj, τj} = {0, 1} (i.e. edges τ, σ lie in opposite subcubes of Qk of codimension 1 separated by the jth coordinate). It follows that each colour class of such a colouring is the disjoint union of cliques of size n − 1 and a bipartite graph and therefore contains no monochromatic copy of Cn. We call such a colouring a hypercube colouring with clique size n − 1.

If we inductively construct a perfect matching on Qk by taking two perfect matchings on a disjoint pair of subcubes of codimension 1 and consider the associated hypercube colouring, we recover the inductive colourings of Erd˝os and Graham [EG75] described in the Introduction. However for k ≥ 4, not all perfect matchings of Qk decompose as the union of two matchings on a pair of codimension 1 subcubes, and so we obtain some genuinely new colourings. In particular, a novel feature that appears for k ≥ 4 colours is that there exist extremal k-colourings that contain a monochromatic cliques of size n − 1 in all k possible colours.

- 3.3. Stability. In this subsection we state a theorem to the eﬀect that the hypercube colourings considered in the previous subsection are the only extremal k-colourings for our problem. Moreover we assert that almost extremal colourings are in some sense ‘close’ to a hypercube colouring. Let us make this more precise.


- Deﬁnition 3.1. Let G and H be k-coloured graphs with V (H) ⊆ V (G). Let ε > 0, then we say that G is ε-close to H if |Gi△Hi| ≤ εv(G)2 for all i ∈ [k].


Informally we may say that G and H as above are close in edit distance. We may now state the main result of this paper.

Theorem 3.2. Let k ≥ 2, let n1 ≪ η ≪ ε ≪ 1, where n is odd, and let N > (2k−1 − η)n. Then if G = KN is k-coloured with no monochromatic copy of Cn, then N ≤ 2k−1(n−1) and there exists a hypercube colouring H such that G is ε-close to H.

![image 3](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile3.png>)

Note that Theorem 1.2 follows as an immediate corollary. The k = 3 case of Theorem 3.2 was proved in [KSS05] where the two classes of colourings the authors consider can be viewed as the colourings that arise from the two isomorphism classes of perfect matchings

in Q3. An interesting feature of Theorem 3.2 is that it deals with a wide variety of extremal colourings. Indeed if M1 and M2 are perfect matchings of Qk that lie in distinct equivalence classes under the action of the automorphism group of Qk, then it’s not diﬃcult to show that there are hypercube colourings associated to M1 that are not isomorphic to any hypercube colouring associated to M2. It is also interesting to note that even though we can prove a stability statement around hypercube colourings, the structure of these colourings is not well understood. This is simply due to the fact that the structure of perfect matchings in the hypercube is not well understood. Indeed, even enumerating the perfect matchings (or their equivalence classes) in Qk is a well-studied and diﬃcult problem. Let f(k) be the number of equivalence classes of perfect matchings in Qk. It is clear that f(3) = 2 and so we obtain two essentially diﬀerent extremal 3-colourings as in [KSS05]. Graham and Harary [GH88] showed that f(4)=8 and recently Osterga˚rd¨ and Pettersson [OP13]¨ determined (with a large amount of computer time) f(5), f(6) and f(7). The function f(k) grows rather rapidly; it is amusing to note that already f(7) = 607158046495120886820621 and so we have this many essentially diﬀerent classes of extremal 7-colourings. It was shown in [CGP97] that the number of perfect matchings in Qk is [(1 + o(1))k/e]2k−1 (although this result in fact follows from a theorem in [PL86, p.312]). Since the automorphism group of Qk has size k!2k it follows that f(k) = [(1 + o(1))k/e]2k−1 also.

- 3.4. Proof of Theorem 3.2: An Overview. The regularity method, discussed brieﬂy in the introduction, plays a central role in our proof method. We include an informal discussion of the method here, deferring details until later. We start with a deﬁnition.


- Deﬁnition 3.3. Let F be a connected graph whose largest matching saturates m vertices, then we call F a connected matching of order m. We distinguish a particular matching of largest size MF in F and refer to an edge of MF as a matching edge of F. If in addition


- F is non-bipartite, we call F an odd connected matching of order m.


The idea behind the regularity method is as follows. Suppose that G is a k-coloured complete graph on N vertices. Let G1, . . ., Gk be its colour classes. We apply the multicolour version of the Regularity Lemma [Sze78] and obtain a regular partition of the vertex set V (G) into t + 1 classes V (G) = V0 ∪ . . . ∪ Vt. We construct an auxiliary graph R with vertex set

- 1, ..., t and the edge set formed by pairs {i, j} for which (Vi, Vj) is regular with respect to G1, . . ., Gk. We colour each edge {i, j} in R by the majority colour in the pair (Vi, Vj). The crucial point is that if R contains a monochromatic odd connected matching of order greater than m, then G contains a monochromatic cycle Cℓ where ℓ can take essentially any odd value smaller than mN/t. It follows that if G contains no monochromatic copy of Cn, then R cannot contain a monochromatic odd connected matching of order larger than nt/N. The advantage of this perspective is that forbidding a large connected matching is far more restrictive than forbidding a cycle of a given length. Indeed a cycle is itself an example of a connected matching, and so if a graph contains no connected matching of order greater than m then it contains no cycle of length greater than m. The following theorem of Erd˝os and Gallai [EG59] shows that this is a very strict condition.


- Theorem 3.4. Let m ≥ 3. If G is a graph which contains no cycle of length greater than m, then e(G) ≤ m(v(G) − 1)/2.


- The price one pays is that R is not a complete graph, however it can be chosen to be as dense as one likes. We are now able to state a theorem that is a major stepping stone toward the proof of Theorem 3.2.
- Theorem 3.5. Let k ≥ 2 and let n1 ≪ δ ≪ ε ≪ 1, where n is odd. If G is a k-coloured graph


![image 4](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile4.png>)

with v(G) = 2k−1n and e(G) ≥ (1 − δ) v(2G) containing no monochromatic odd connected matching of order ≥ (1+δ)n, then for any choice of proﬁle x(G) of G, there exists a hypercube

colouring H with proﬁle x(H) satisfying x(G) − x(H) ≤ εn.

The proof of Theorem 3.5 occupies the majority of this paper. In the ﬁnal section we show how Theorem 3.2 follows from 3.5 via combinatorial stability arguments and the regularity method. The outline of the proof of Theorem 3.5 is as follows. Let G be as in the statement of Theorem 3.5 and let x(G) denote a proﬁle of G. Our starting point is to translate the combinatorial constraint of containing no large monochromatic odd connected matching into an analytic constraint on x(G) of the form

- (3.1) F(x(G)) ≤ 0,


where F is a quadratic form which we derive in the next section. We then view (3.1) as a constraint in an optimisation problem where we wish to maximise the objective function x(G) . Recalling that x(G) = v(G), we get a corresponding upper bound on the order of G. It turns out that optimal solutions to this optimisation problem correspond to the proﬁles of hypercube colourings. Solving the optimisation problem is the subject of Sections 5 and 6. In Section 7 we use compactness arguments to show that almost optimal solutions must be close in ℓ1-norm to the proﬁle of a hypercube colouring. We then translate this analytic stability into the, more combinatorial, stability statement of Theorem 3.5. Note that Theorem 3.5 will be applied to a reduced graph like the one described above. The focus of the ﬁnal section is to show that if the proﬁle of this reduced graph is close in ℓ1-norm to the proﬁle of a hypercube colouring, then the original graph is close in edit distance to a hypercube colouring.

4. Deriving the Analytic Constraints

Given a k-coloured graph G, we will show how to translate the combinatorial constraint of containing no large monochromatic odd connected matching into an analytic constraint on the proﬁle of G.

From here on, throughout the paper, we let k ≥ 2 be a ﬁxed integer. Let G be a k-coloured graph. First we distinguish between two types of edges of G. If e ∈ E(G) is coloured with the colour j and lies in a bipartite component of Gj then we call e a bipartite edge. We call e non-bipartite otherwise. Let (Vτ : τ ∈ {0, 1, ∗}k) be a proﬁle partition of G. We make two simple observations regarding the proﬁle partition of a k-coloured graph.

- Observation 4.1. If e ∈ E(G) is a bipartite edge of colour j then it must have endpoints in parts Vτ, Vσ for some τ, σ ∈ {0, 1, ∗}k such that τj = 0 and σj = 1.
- Observation 4.2. If e ∈ E(G) is a non-bipartite edge of colour j then it must have endpoints in parts Vτ, Vσ for some (not necessarily distinct) τ, σ ∈ {0, 1, ∗}k such that τj = σj = ∗.


This motivates the following deﬁnitions.

- Deﬁnition 4.3. We say that σ, τ ∈ {0, 1, ∗}k are distinguishable if {σj, τj} = {0, 1} for some j ∈ [k]. We say that σ and τ are indistinguishable otherwise.


- Deﬁnition 4.4. If σ, τ ∈ {0, 1, ∗}k are such that either (i) σ, τ are distinguishable or (ii)


σj = τj = ∗ for some j ∈ [k], then we say that σ and τ are compatible. We say that σ, τ are incompatible otherwise.

Viewing elements of {0, 1, ∗}k as subcubes of Qk, we may reinterpret these deﬁnitions as follows.

- Lemma 4.5. Let σ, τ ∈ {0, 1, ∗}k. Then σ, τ are distinguishable if and only if Q(τ)∩Q(σ) = ∅. Furthermore, σ, τ are incompatible if and only if |Q(τ) ∩ Q(σ)| = 1. Proof. By the deﬁnition of the sets Q(τ), Q(σ) we have


Q(τ) ∩ Q(σ) = {c ∈ {0, 1}k : cj = τj if τj ∈ {0, 1} and cj = σj if σj ∈ {0, 1}}.

This is empty if and only if there exists a j ∈ [k] such that σj, τj ∈ {0, 1} and σj = τj i.e. if and only if σ, τ are distinguishable. Let T = {i ∈ [k] : σi = τi = ∗}. If σ, τ are indistinguishable then we see that |Q(τ) ∩ Q(σ)| = 2|T|. Therefore |Q(τ) ∩ Q(σ)| = 1 if and only if σ, τ are indistinguishable and T = ∅ i.e. σ, τ are incompatible.

From now on, we let D = {σ, τ} ∈

{0, 1, ∗}k 2

: σ, τ are distinguishable . It will also be convenient to make the following deﬁnition.

- Deﬁnition 4.6. Let α > 0 and let G be a graph such that e(G) ≥ α v(2G) . Then we say that G is α-dense.


This next proposition provides the link between our combinatorial problem and a problem in nonlinear optimisation.

- Proposition 4.7. Let C > 1, 0 < δ < 1 and let n > 1/δ. Suppose that G is a (1− δ)-dense, k-coloured graph with v(G) = Cn, containing no monochromatic odd connected matching of order ≥ (1 + δ)n. Let x be a proﬁle of G and let v = x/n. Then the following hold:


- (1) 



τ∈{0,1,∗}k

vτ

 

2

− 2

{σ,τ}∈D

vσvτ −

τ∈{0,1,∗}k

ω(τ)vτ ≤ δkC2.

- (2) vτ ≤ 1 + 2√δC whenever ω(τ) = 1.

![image 5](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile5.png>)

- (3) vτvσ ≤ 2δC2 whenever σ and τ are incompatible.


Proof. Let us ﬁrst remind ourselves of the graph decomposition discussed in Subsection 3.1.

For each i ∈ [k], we write Gi = G′i ∪ G′′i , where G′i is the union of the bipartite components of Gi and G′′i is the union of the non-bipartite components of Gi. For each i ∈ [k], write V (G′i) = V0i ∪ V1i where V0i and V1i are the vertex classes of a bipartition of G′i and set

V∗i = V (G′′i ). For τ ∈ {0, 1, ∗}k, set Vτ = kj=1 Vτj

. Let x = (|Vτ| : τ ∈ {0, 1, ∗}k) be the proﬁle corresponding to this partition. Let N = v(G) and note that

j

- (4.1) N =


xτ.

τ∈{0,1,∗}k

It follows from Observation 4.1 that the number of bipartite edges in G is at most {σ,τ}∈D xσxτ. Letting e0 denote the number of non-bipartite edges in G we therefore have that

- (4.2) e0 ≥ e(G) −

{σ,τ}∈D

xσxτ.

Since N ≥ 1/δ, we have

- (4.3) e(G) ≥ (1 − δ)

N 2 ≥ (1 − 2δ)

N2 2

![image 6](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile6.png>)

. Combining (4.1), (4.2) and (4.3) gives

- (4.4) e0 ≥

- 1

![image 7](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile7.png>)

- 2


 

τ∈{0,1,∗}k

xτ

 

2

−

{σ,τ}∈D

xσxτ − δN2.

We now ﬁnd a corresponding upper bound for e0. Recall that for τ ∈ {0, 1, ∗}k, the weight ω(τ) of τ is deﬁned to be the size of the set {i ∈ [k] : τi = ∗}.

By assumption, for each i ∈ [k], every connected component of G′′i has no matching on (1 + δ)n vertices and so in particular G′′i has no cycle of length greater than (1 + δ)n. Theorem 3.4 therefore implies that

- (4.5) e(G′′i ) ≤ (1 + δ)

n 2|V∗i|.

![image 8](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile8.png>)

Observe that

- (4.6) |V∗i| =

{τ∈{0,1,∗}k:τi=∗}

xτ.

Since each non-bipartite edge of G belongs to E(G′′i ) for some i, (4.5) and (4.6) provide the upper bound

- (4.7) e0 ≤

k

i=1

e(G′′i ) ≤ (1 + δ)

n 2

![image 9](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile9.png>)

k

i=1

|V∗i| = (1 + δ)

n 2

![image 10](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile10.png>)

τ∈{0,1,∗}k

ω(τ)xτ.

Since ω(τ) ≤ k for all τ ∈ {0, 1, ∗}k by deﬁnition, (4.1) and (4.7) imply the bound

- (4.8) e0 ≤


- 1

![image 11](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile11.png>)

- 2


n 2

ω(τ)xτ.

δnkN +

![image 12](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile12.png>)

τ∈{0,1,∗}k

Recall that v = x/n. Comparing the bounds (4.4) and (4.8) and scaling the resulting inequality by 2/n2 yields

 

τ∈{0,1,∗}k

 

2

vτ

− 2

vσvτ − 2δC2 ≤

ω(τ)vτ + δkC.

τ∈{0,1,∗}k

{σ,τ}∈D

This establishes (1). Notice that if τ ∈ {0, 1, ∗}k is such that ω(τ) = 1, then G[Vτ] is monochromatic with all edges non-bipartite by Observations 4.1 and 4.2. G[Vτ] therefore contains no cycle of length greater than (1 + δ)n and so by Theorem 3.4 and the fact that

- G has at most δ N2 edges missing


n 2

N 2 ≤ e(G[Vτ]) ≤ (1 + δ)

xτ 2 − δ

xτ. It follows that

![image 13](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile13.png>)

vτ2 ≤ (1 + 2δ)vτ + δC2, from which (2) follows. Finally, let us note that by Observations 4.1 and 4.2, if σ, τ are incompatible, then there can be no edges lying between Vσ and Vτ. Since G has at most δ N2 edges missing we must then have

xτxσ ≤ 2δN2 (note that this inequality also accounts for the case where σ = τ) and so (3) follows.

Given a graph G its proﬁle lies in the space R{0,1,∗}k which we will denote by R∗. In view of Proposition 4.7 we deﬁne the function F : R∗ → R by

 

 

2

− 2

xσxτ −

F(x) =

xτ

ω(τ)xτ.

τ∈{0,1,∗}k

τ∈{0,1,∗}k

{σ,τ}∈D

Let us also deﬁne the following subsets of R∗. X(γ): For γ ≥ 0, let X(γ) denote the set of elements x ∈ R∗ satisfying: (X1) F(x) ≤ γ

(X2) xτ ≤ 1 + γ whenever w(τ) = 1. (X3) xτxσ ≤ γ whenever σ and τ are incompatible. (X4) xτ ≥ 0 for all τ.

Now let G be as in the statement of Theorem 3.5 and let x be a proﬁle of G. By the above proposition we have x/n ∈ X(

√

![image 14](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile14.png>)

δk22k) whereas we also have x = 2k−1n. We will show that for δ small, this means that x/n is an element of almost maximal norm in X(

√

![image 15](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile15.png>)

δk22k). We will also show that elements of large norm in X(

√

![image 16](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile16.png>)

δk22k) have a very speciﬁc structure (in fact they resemble the proﬁle of a hypercube colouring) and so this imposes a lot of structure on x. For now we focus our attention on the set X(0) which we denote simply by X. Later on, we use compactness arguments to relate properties of X and X(γ) for γ small.

Our next goal is to classify elements of maximal ℓ1-norm in X. To describe these elements we need a deﬁnition.

- Deﬁnition 4.8. Call a set A ⊆ {0, 1, ∗}k distinguishable if every pair of distinct elements of A are distinguishable and also ω(τ) ≥ 1 for all τ ∈ A.

The requirement that elements have weight at least 1 is for notational convenience later in the paper. Viewing elements of {0, 1, ∗}k as subcubes of Qk, a distinguishable set is simply a collection of disjoint subcubes of Qk (of dimension at least 1). If this collection covers the whole cube we give it a special name.

- Deﬁnition 4.9. Call a distinguishable set A ⊆ {0, 1, ∗}k a decomposition if τ∈A Q(τ) = {0, 1}k.


Let us quickly record a simple result concerning distinguishable sets which will become useful later.

- Lemma 4.10. Let D ⊂ {0, 1, ∗}k be a distinguishable set. Then


2ω(τ) ≤ 2k,

τ∈D

with equality if and only if D is a decomposition.

Proof. This is simply the observation that a distinguishable set D is a collection of disjoint subcubes of Qk and so the sum of their sizes τ∈D 2ω(τ) is bounded by the size of Qk. Moreover we have equality if and only if these subcubes cover all of Qk i.e. D is a decomposition.

We deﬁne the following subset of R∗. O: Let O denote the set of elements x ∈ R∗ satisfying:

- (O1) supp(x) is a decomposition where ω(τ) = 1 or 2 for all τ ∈ supp(x).
- (O2) For all τ ∈ supp(x), if ω(τ) = 1 then xτ = 1 and if ω(τ) = 2 then xτ = 2.


It is easy to check that O ⊆ X. The next proposition asserts that O is the set of elements of maximal ℓ1-norm in X.

- Proposition 4.11. If x ∈ X, then x ≤ 2k−1 with equality if and only if x ∈ O.


We note that the ‘if’ statement in the above proposition is immediate. Indeed if x ∈ O then supp(x) is a decomposition so that τ∈supp(x) 2ω(τ) = 2k by Lemma 4.10. Moreover 2ω(τ) = 2xτ for all τ ∈ supp(x) by (O2).

- Deﬁnition 4.12. If x ∈ X is such that x = supz∈X z then we say that x is an optimal point of X.


We note that since X is compact, optimal points of X exist. The proof of Proposition 4.11 is split over the next two sections.

5. Compressions and a Spherical Constraint

In this section we make the ﬁrst steps towards a proof of Proposition 4.11. Broadly speaking we apply the combinatorial technique of ‘shifting’ or ‘compression’ to transform the complicated non-linear constraint in the deﬁnition of X = X(0) into a spherical constraint which is much more amenable to analysis. In Section 6 we apply optimisation tools to this transformed problem. We begin with a simple lemma concerning elements of {0, 1, ∗}k.

- Lemma 5.1. If σ, τ ⊆ {0, 1, ∗}k are indistinguishable and compatible and ω(τ) = 1, then Q(τ) ⊆ Q(σ). In particular if ω(σ) = 1 also, then σ = τ.


Proof. Since σ, τ are indistinguishable and compatible we have |Q(τ)∩Q(σ)| ≥ 2 by Lemma 4.5. However, |Q(τ)| = 2 and so it follows that Q(τ) ⊆ Q(σ). If ω(σ) = 1 also, then clearly Q(σ) = Q(τ) i.e. σ = τ.

- Deﬁnition 5.2. Let x ∈ R∗. If all pairs of (not necessarily distinct) elements of supp(x) are compatible, then we say that x has compatible support.


Let us note that condition (X3) (with γ = 0) in the deﬁnition of the set X is simply the condition that elements of X have compatible support. In particular, if x ∈ X and τ ∈ {0, 1, ∗}k has weight 0, then xτ = 0 since τ is not compatible with itself.

The following lemma establishes an important property of optimal points. For τ ∈ {0, 1, ∗}k we let eτ ∈ R∗ denote the standard unit vector whose entries are all 0 except the entry labelled τ which is 1.

- Lemma 5.3. Let x ∈ X be an optimal point then F(x) = 0.


Proof. Suppose for contradiction that F(x) < 0. Assume ﬁrst that there exists τ ∈ supp(x) with ω(τ) ≥ 2. By the continuity of F we may choose α > 0 small enough so that F(x + αeτ) < 0. Let x′ = x + αeτ. Since supp(x′) = supp(x) it is clear that x′ ∈ X. However,

x′ = x + α > x contradicting the fact that x is optimal.

We may assume then that supp(x) consists only of elements of weight 1 and therefore is a distinguishable set by Lemma 5.1 and the fact that x has compatible support. It follows from the deﬁnition of F that

(x2τ − xτ) < 0,

F(x) =

τ∈supp(x)

and so xτ < 1 for some τ ∈ supp(x). As before there exists some α > 0 suﬃciently small so that F(x + αeτ) < 0. Let x′ = x + αeτ. If we pick α small enough so that x′τ = xτ + α ≤ 1 also, then again we have x′ ∈ X with x′ > x contradicting the optimality of x.

We now describe the transformations alluded to at the beginning of this section. They will be of great use in simplifying our analysis of optimal points of X.

- Deﬁnition 5.4. Let x ∈ R∗ and let π, ρ ∈ {0, 1, ∗}k be distinct. We deﬁne the (π, ρ)compression of x, denoted x(π, ρ), as follows:


- • If ω(ρ) ≥ 2, or if ω(ρ) ≤ 1 and xπ + xρ < 1, then let x(π, ρ) be the vector x′ with coordinates: x′π = 0, x′ρ = xπ + xρ and x′τ = xτ for all τ ∈ {0, 1, ∗}k\{π, ρ}.
- • If ω(ρ) ≤ 1 and xπ + xρ ≥ 1 then let x(π, ρ) be the vector x′ with coordinates: x′π = xπ + xρ − 1, x′ρ = 1 and x′τ = xτ for all τ ∈ {0, 1, ∗}k\{π, ρ}.


If x(π, ρ) = x then we say that x is (π, ρ)-compressed.

Let x ∈ X be an optimal point, we will be interested in instances where x(π, ρ) is also an optimal point of X. We observe that if x ∈ R∗ and π, ρ ∈ {0, 1, ∗}k are distinct then

x(π, ρ) = x . However, if x ∈ X then it does not follow in general that x(π, ρ) ∈ X.

For reasons that will become clear, we only consider (π, ρ)-compressions in the case where π and ρ are indistinguishable. It will therefore be useful to associate to each point x ∈ X, the digraph D(x) = (V (x), E(x)) where V (x) = supp(x) and

E(x) = {(π, ρ) : π, ρ are distinct, indistinguishable and x(π, ρ) ∈ X}.

In particular if x ∈ X is (π, ρ)-compressed, where π and ρ are distinct and indistinguishable, then (π, ρ) ∈ E(x). We draw attention to the fact that edges of D(x) only occur between indistinguishable pairs. Conversely, the following lemma shows that, when x ∈ X is optimal, at least one edge occurs between any indistinguishable pair in D(x).

Lemma 5.5. Let x ∈ X be optimal and suppose that π, ρ ∈ V (x), are indistinguishable and distinct. Then one of the following holds:

- (i) x is (π, ρ)-compressed, xρ = 1, ω(ρ) = 1, ω(π) ≥ 2 and (ρ, π) ∈/ E(x),
- (ii) x is (ρ, π)-compressed, xπ = 1, ω(π) = 1, ω(ρ) ≥ 2 and (π, ρ) ∈/ E(x),
- (iii) (ρ, π) and (π, ρ) both lie in E(x). Proof. Recall that


 

 

2

− 2

xσxτ −

F(x) =

xτ

ω(τ)xτ,

τ∈{0,1,∗}k

τ∈{0,1,∗}k

{σ,τ}∈D

where D is the set of unordered distinguishable pairs from {0, 1, ∗}k. Since π, ρ are indistinguishable, the term xρxπ does not appear in the sum {σ,τ}∈D xσxτ. We may therefore express F(x) in the form

 

 

2

− Axρ − Bxπ − C,

- (5.1) F(x) =


xτ

τ∈{0,1,∗}k

where A, B and C do not depend on xρ or xπ and A, B ≥ 0. Suppose that A ≥ B and let x′ = x(π, ρ). Let us show that (π, ρ) ∈ E(x) i.e. x′ ∈ X. By (5.1) we have F(x′) ≤ F(x) and so x′ satisﬁes (X1) in the deﬁnition of X. By the deﬁnition of (π, ρ)-compression it is clear that x′ also satisﬁes (X2) and (X4). Since ρ ∈ supp(x), we also have supp(x′) ⊆ supp(x). Since x has compatible support the same is true for x′ i.e. x′ satisﬁes (X3) and so x′ ∈ X. Note that since compressions preserve the ℓ1-norm, x′ is also an optimal point of X.

In the case A = B, an identical argument shows that (ρ, π) ∈ E(x) also, and so (iii) holds. Suppose then that A > B. In this case, looking again at (5.1), we see that if x is not (π, ρ)-

compressed then we in fact have F(x′) < F(x) = 0, contradicting Lemma 5.3. We conclude that x is (π, ρ)-compressed. Suppose ω(ρ) ≥ 2, then by the deﬁnition of (π, ρ)-compression we have xπ = x′π = 0 contradicting the fact that π ∈ supp(x) and so ω(ρ) = 1. Since π and ρ are compatible, indistinguishable and distinct, it follows from Lemma 5.1 that ω(π) ≥ 2. Let x′′ = x(ρ, π). It follows that x′′ρ = 0 and x′′π = xρ +xπ and so by (5.1), F(x′′) > F(x) = 0. We conclude that x′′ ∈/ X i.e. (ρ, π) ∈/ E(x). The fact that xρ = 1 follows from the fact

that ω(ρ) = 1 and x is (π, ρ)-compressed. Thus (i) holds, and similarly if A < B then (ii) holds.

We obtain the following immediate corollary. Corollary 5.6. Let x ∈ X be an optimal point and suppose that I is an independent set in

- D(x). Then I is a distinguishable set.


- Deﬁnition 5.7. We call an optimal point x ∈ X compressed if it is (π, ρ)-compressed for all (π, ρ) ∈ E(x).


We now show that compressed optimal points of X exist. In fact we show that given any optimal point of x ∈ X we may obtain a compressed optimal point by applying a ﬁnite number of compressions to x. The simpler structure of compressed optimal points will make it easier to bound their ℓ1-norm which is the goal of Proposition 4.11.

- Lemma 5.8. Compressed optimal points of X exist.


Proof. Let x be an arbitrary optimal point of X and deﬁne a sequence x0, x1, x2, . . . of elements of X recursively as follows: Set x0 = x. Having chosen x0, . . ., xt, if xt is compressed then stop the sequence at xt. If not, then there exists (π, ρ) ∈ E(xt) such that xt is not (π, ρ)-compressed. By Lemma 5.5, we must therefore have that x(π, ρ) and x(ρ, π) are both optimal points of X. Note that by the deﬁnition of D(xt), ρ and π are indistinguishable and {π, ρ} ⊆ supp(xt). Since xτ has compatible support, it follows from Lemma 5.1 that either ω(π) ≥ 2 or ω(ρ) ≥ 2. If ω(ρ) ≥ 2 then set xt+1 = x(π, ρ), if not (so that ω(π) ≥ 2) set xt+1 = x(π, ρ). In either case xt+1 is an optimal point of X satisfying |V (xt+1)| = |V (xt)|−1. Since 0 ≤ |V (x)| ≤ 3k for all x ∈ X it follows that the sequence must terminate in at most 3k steps.

Having discovered compressed optimal points, we now explore some of their properties. First we need a deﬁnition.

- Deﬁnition 5.9. A star is a digraph with vertex set {ρ, π1, . . ., πm} (for some m ≥ 0) and edge set {(ρ, π1), . . ., (ρ, πm)}. We refer to ρ as the root of the star and we call π1, . . ., πm leaves. Note that we have included the possibility of a star with no leaves.


- Lemma 5.10. Let x ∈ X be a compressed optimal point, then D(x) is a disjoint union of stars. Moreover if ρ is a root of positive outdegree then ω(ρ) ≥ 2 and if π is a leaf then ω(π) = 1 and xπ = 1. Proof. It suﬃces to prove the following:


- (1) If (ρ, π) ∈ E(x) then ω(ρ) ≥ 2, ω(π) = 1, xπ = 1 and (π, ρ) ∈/ E(x).
- (2) If (ρ1, π), (ρ2, π) ∈ E(x) then ρ1 = ρ2.


Suppose that (ρ, π) ∈ E(x), in particular ρ and π are indistinguishable. If (π, ρ) ∈ E(x) also, then since x is compressed we have by deﬁnition that x(ρ, π) = x = x(π, ρ). However, from the deﬁnition of compression we see that the only way we can have x(ρ, π) = x(π, ρ) is if ω(π) = ω(ρ) = 1. But then by Lemma 5.1, π = ρ, a contradiction. We conclude that (π, ρ) ∈/ E(x) and so (1) follows from Lemma 5.5.

Suppose now that (ρ1, π), (ρ2, π) ∈ E(x). By (1) we know that ω(π) = 1 and ω(ρi) ≥

- 2 for i = 1, 2. By Lemma 5.1 it follows that Q(π) ⊆ Q(ρ1) ∩ Q(ρ2) and so ρ1, ρ2 are


indistinguishable by Lemma 4.5. If ρ1 = ρ2 then by Lemma 5.5 we have that either (ρ1, ρ2) ∈

- E(x) or (ρ2, ρ1) ∈ E(x), but this contradicts (1). Given a compressed optimal point x ∈ X let

L(x) = {τ ∈ V (x) : d−(τ) > 0} and

R(x) = V (x)\L(x). By Lemma 5.10, L(x) and R(x) are the set of leaves and the set of roots of D(x) respectively.

- Lemma 5.11. Let x ∈ X be a compressed optimal point. Then

F(x) =

τ∈R(x)

x2τ + (2d+(τ) − ω(τ))xτ .

Proof. Lemma 5.10 shows that for any indistinguishable pair π, ρ ∈ V (x), where π = ρ, exactly one of (π, ρ) and (ρ, π) is in E(x) and so

F(x) =

τ∈V (x)

x2τ + 2

(σ,τ)∈E(x)

xσxτ −

τ∈V (x)

ω(τ)xτ.

By Lemma 5.10 we may write

(σ,τ)∈E(x)

xσxτ =

ρ∈R(x)

xρ

 

π:(ρ,π)∈E(x)

xπ

  =

ρ∈R(x)

d+(ρ)xρ.

Moreover by Lemma 5.10 we have τ∈L(x)(x2τ − ω(τ)xτ) = 0. The result follows.

The key feature here is that for a compressed optimal point x, the constraint equation F(x) = 0 is spherical. This allows us to more easily apply standard optimisation techniques and this will be the concern of the next section. For now it will be useful for us to establish some degree conditions on the vertices of D(x) for a compressed optimal point x ∈ X.

- Lemma 5.12. Let x ∈ X be a compressed optimal point, then d+(σ) ≤ 2ω(σ)−1 for all σ ∈ V (x).




Proof. Suppose that ρ ∈ V (x) is such that d+(ρ) > 0. By Lemma 5.10, ρ is the root of a star in D(x). Let L be the set of leaves of this star (so in particular |L| = d+(ρ) and ω(π) = 1 for all π ∈ L). Note that L is an independent set in D(x) and therefore it is a distinguishable set by Corollary 5.6. Note further that for each π ∈ L, ρ and π are indistinguishable and compatible and hence Q(π) ⊆ Q(ρ) by Lemma 5.1. It follows that

|Q(π)| ≤ |Q(ρ)| = 2ω(ρ).

2d+(ρ) =

π∈L

We can now bootstrap, using the previous two lemmas to establish a much stronger degree condition. The idea behind the proof of the following lemma is readily explained however it is notationally laborious. The idea is that if x ∈ X is a compressed optimal point and a star in D(x) with root ρ has > ω(ρ) leaves, then one can contradict the optimality of x by replacing this star with a collection of stars whose roots have less weight. First let us generalise an earlier notation.

Deﬁnition 5.13. Let σ ∈ {0, 1, ∗}k and let W = {i ∈ [k] : σi = ∗}. Then for S ⊆ W deﬁne Q(σ; S) = {τ ∈ {0, 1, ∗}k : τi ∈ {0, 1} for i ∈ W\S and τi = σi otherwise}.

Note that elements of Q(σ; S) are pairwise distinguishable and that Q(σ; ∅) is simply the set Q(σ). We may think of Q(σ; S) as a decomposition of Q(σ) into ‘parallel’ subcubes of dimension |S|.

- Lemma 5.14. Let x ∈ X be a compressed optimal point, then d+(σ) ≤ ω(σ) for all σ ∈ V (x).


Proof. By Lemma 5.10 we may write V (x) = S1 ∪ . . . ∪ Sq, a disjoint union where each Si is

the vertex set of a star in D(x). Suppose that there exists σ ∈ V (x) such that d+(σ) > ω(σ). Without loss of generality assume σ is the root of S1. By Lemma 5.11 we then have that ω(σ) < d+(σ) ≤ 2ω(σ)−1 and so ω(σ) ≥ 3. Without loss of generality assume that σ1 = σ2 = ∗. By Lemma 5.10 we have xτ = 1 for all τ ∈ L(x) and so

- (5.2) x = |L(x)| +

τ∈R(x)

xτ.

We proceed by modifying x, being careful to stay within the set X. Take π ∈ Q(σ; {1, 2}) and note that ω(π) = 2. Consider now the element x′ ∈ R∗ deﬁned as follows. Let x′π = xσ, x′τ = 1 for all τ ∈ Q(σ; {1}), x′τ = xτ for all τ ∈ S2 ∪ . . . ∪ Sq and x′τ = 0 otherwise. We now check that x′ ∈ X. Clearly x′τ ≤ 1 whenever ω(τ) = 1. Note that supp(x′) = {π} ∪ Q(σ; {1}) ∪ S2 ∪ . . . ∪ Sq. Now, if τ ∈ {π} ∪ Q(σ; {1}) we have Q(τ) ⊆ Q(σ) and since σ ∈ S1, we know that σ, and hence also τ, is distinguishable from each element of S2 ∪. . .∪Sk. Since τ1 = ∗ for each τ ∈ {π}∪Q(σ; {1}) we see that {π}∪Q(σ; {1}) contains no incompatible pairs. It follows that x′ has compatible support. Finally, note that by a calculation similar to that in the proof of Lemma 5.11 we have

F(x′) = x2σ + 2xσ +

τ∈R(x)\{σ}

- (5.3) x2τ + 2d+(τ) − ω(τ) xτ

= F(x) − (2d+(σ) − ω(σ) − 2)xσ.

Recalling that d+(σ) > ω(σ) we have 2d+(σ)−ω(σ) > ω(σ) ≥ 3. Since σ ∈ supp(x), we also have xσ > 0 and so (5.3) implies that F(x′) < F(x) = 0. Thus we do indeed have x′ ∈ X. Note that

- (5.4) x′ = |L(x)| − d+(σ) + |Q(σ; {1})| +


xτ,

τ∈R(x)

and observe that d+(σ) ≤ 2ω(σ)−1 = |Q(σ; {1})| by Lemma 5.11. It now follows from (5.2) and (5.4) that x′ ≥ x , and so x′ is an optimal point of X. However we have shown that F(x′) < 0 contradicting Lemma 5.3.

Gathering all the information we have obtained on compressed optimal points, we show that a proof of the following proposition is almost enough to deduce Proposition 4.11. Let us remind ourselves that in the deﬁnition of a distinguishable set (Deﬁnition 4.8), we require all elements of the set to have weight at least 1.

- Proposition 5.15. Let D ⊆ {0, 1, ∗}k be a distinguishable set and let ∆ = {dτ : τ ∈ D} be a set of integers satisfying 0 ≤ dτ ≤ ω(τ) for all τ ∈ D, and dτ = 0 whenever ω(τ) = 1. Suppose that x ∈ R∗ is a vector with supp(x) = D satisfying


- (1)

τ∈D

x2τ + (2dτ − ω(τ))xτ = 0,

- (2) xτ ≤ 1 whenever ω(τ) = 1.


Then

xτ ≤ 2k−1 −

dτ. Furthermore we have equality only if x ∈ O and ∆ = {0}.

τ∈D

τ∈D

A proof of Proposition 5.15 will be the focus of the next section, for now we note that it has the following corollary Corollary 5.16. O is the set of compressed optimal points of X. In particular, if x ∈ X then x ≤ 2k−1.

Proof. Let x ∈ X be a compressed optimal point. Note that R(x) is an independent set in the digraph D(x) and hence by Corollary 5.6, R(x) is a distinguishable set. Set ∆ = {d+(τ) : τ ∈ R(x)} and let x′ be the element of R∗ supported on R(x) such that x′τ = xτ for all τ ∈ R(x). Note that by Lemmas 5.3, 5.11, 5.14 and by the deﬁnition of the set X, we have that ∆ and x′ satisfy the conditions in the statement of Proposition 5.15. Assuming

- Proposition 5.15, it therefore follows that


- (5.5)


xτ ≤ 2k−1 −

d+(τ),

τ∈R(x)

τ∈R(x)

- with equality only if x′ ∈ O and d+(τ) = 0 for all τ ∈ R(x). The latter condition implies


- that x′ = x and so we have equality in (5.5) only if x ∈ O. By Lemma 5.10,


d+(τ),

x =

xτ +

τ∈R(x)

τ∈R(x)

and so it follows that x ≤ 2k−1 with equality only if x ∈ O. The result follows by noting that for all z ∈ O, z = 2k−1 and z is compressed.

It is now clear that Proposition 4.11 would follow if we could also prove the following. Proposition 5.17. If x ∈ X is an optimal point, then x is compressed.

We prove Proposition 5.17 in Section 7.

6. Constrained Optimisation and a proof of Proposition 5.15

In this section we prove Proposition 5.15 thus ﬁnalising the main stepping stone toward a proof of Proposition 4.11. We use standard tools from the theory of convex optimisation to exploit the spherical constraint found in the previous section. This will lead us to consider the possible distributions of weights in distinguishable sets which we optimise over in a separate argument. The main tools that we borrow are the Karush-Kuhn-Tucker (KKT) conditions along with Slater’s constraint qualiﬁcation. Below is a statement of the result we use, phrased to match our needs (see [BV04, p. 244] for a detailed account).

- Theorem 6.1 (KKT + Slater’s Condition). Let f, g1, . . ., gr : Rm → R be convex, diﬀerentiable functions and let


S = {x ∈ Rm : gi(x) ≤ 0 for i = 1, . . ., r}.

Suppose that there exists an x0 ∈ Rm such that gi(x0) < 0 for i = 1, . . ., r. Then if x∗ ∈ S is such that

f(x∗) = sup

f(x), then there exist λ1, . . ., λr ∈ R such that

x∈S

- (i) ∇f(x∗) = ri=1 λi∇gi(x∗),
- (ii) λi ≥ 0, i = 1, . . ., r,
- (iii) λigi(x∗) = 0, i = 1, . . ., r.


In view of the statement of Proposition 5.15 it is natural to apply Theorem 6.1 to establish the following.

- Lemma 6.2. Let α1, . . ., αm be integers where αi = 1 for i = 1, . . ., ℓ, (0 ≤ ℓ ≤ m) and let x1, . . ., xm be real numbers satisfying


- (i) mi=1(x2i − αixi) ≤ 0,
- (ii) xi ≤ 1 for i = 1, . . ., ℓ.


If mi=1 αi2 > m, then

 

 ,

![image 17](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile17.png>)

m

m

m

1 2

αi2

xi ≤ ℓ +

αi + (m − ℓ)

![image 18](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile18.png>)

i=1

i=ℓ+1

i=ℓ+1

![image 19](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile19.png>)

- with equality only if xi = 1 for i ≤ ℓ and xi = 21 αi + (m1−ℓ) mi=ℓ+1 αi2 for i > ℓ.


![image 20](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile20.png>)

![image 21](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile21.png>)

If instead mi=1 αi2 ≤ m, then

 ,

 

![image 22](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile22.png>)

m

m

m

- 1

![image 23](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile23.png>)

- 2


αi2

xi ≤

αi + m

i=1

i=1

i=1

![image 24](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile24.png>)

with equality only if xi = 21 αi + m1 mi=1 αi2 for all i. Proof. Note ﬁrst that if αi = 0 for all i (so in particular ℓ = 0) then inequality (i) implies

![image 25](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile25.png>)

![image 26](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile26.png>)

- that xi = 0 for all i in which case there’s nothing to prove. Suppose then that this is not the case and deﬁne functions f, g1, . . ., gℓ+1 : Rm → R as follows. Let f(x) = mi=1 xi, gi(x) = xi − 1 for i = 1, . . ., ℓ and gℓ+1(x) = mi=1(x2i − αixi). Note that the functions just deﬁned are all convex and diﬀerentiable. Let x0 = (α1/2, . . ., αm/2), the centre of the spherical region described by (ii) and observe that gi(x0) < 0 for i = 1, . . ., ℓ + 1. Let S = {x ∈ Rm : gi(x) ≤ 0 for i = 1, . . ., ℓ + 1}. S is compact and f is continuous hence we may pick x∗ ∈ S such that


f(x∗) = sup

f(x).

x∈S

Let x∗ = (x1, . . ., xm). By Theorem 6.1, there exist real numbers λ1, . . ., λℓ and Λ such that the following hold (for notational convenience we deﬁne λj = 0 for j > ℓ):

- (1) Λ(2xi − αi) + λi = 1 for all i,


- (2) Λ ≥ 0 and λi ≥ 0 for all i,
- (3) Λ ( mi=1(x2i − αixi)) = 0 and λi(xi − 1) = 0 for all i.


We consider three cases depending on the value of Λ. First let us suppose that Λ = 0. In this case, by (1) we must have λi = 1 for all i. Recalling that λj = 0 for j > ℓ by deﬁnition, we must also have ℓ = m and so αi = 1 for all i. Moreover, it follows from (3) that xi = 1 for all i and so we’re done.

By (2), we may now assume that Λ > 0 and so we may rewrite (1) as

- 1

![image 27](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile27.png>)

- 2


- (6.1) xi =


1 − λi Λ

+ αi for all i.

![image 28](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile28.png>)

Moreover, mi=1(x2i − αixi) = 0 by (3) which by (6.1) gives

- (6.2)

1 Λ2

![image 29](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile29.png>)

m

i=1

(1 − λi)2 =

m

i=1

αi2.

Now, note that for i ≤ ℓ we have αi = 1 and xi ≤ 1 and so by (6.1) we have

- (6.3) 1 − Λ ≤ λi for i ≤ ℓ.

If Λ < 1 then by (6.3) we have λi > 0 for i ≤ ℓ and so by (3), xi = 1 for i ≤ ℓ and so in fact by (6.1)

1 − Λ = λi for i ≤ ℓ. Recalling that αi = 1 for i ≤ ℓ and λi = 0 for i > ℓ by deﬁnition, (6.2) then gives

- (6.4)

1 Λ

![image 30](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile30.png>)

=

![image 31](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile31.png>)

1 m − ℓ

![image 32](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile32.png>)

m

i=ℓ+1

αi2.

From (6.1) it now follows that

xi =

- 1

![image 33](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile33.png>)

- 2


 αi +

![image 34](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile34.png>)

1 m − ℓ

![image 35](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile35.png>)

m

i=ℓ+1

αi2

  for i > ℓ,

and so

m

i=1

xi = ℓ +

- 1

![image 36](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile36.png>)

- 2


 

m

i=ℓ+1

αi + (m − ℓ)

![image 37](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile37.png>)

m

i=ℓ+1

αi2

 .

Recalling that Λ < 1, it follows from (6.4) that mi=1 αi2 > m.

It remains to consider the case where Λ ≥ 1. Recall that if λi > 0 for some i then xi = 1 by (3) and so Λ = 1 − λi by (6.1). However this contradicts the assumption that Λ ≥ 1 and so we conclude that λi = 0 for all i. It follows from (6.2) that

- (6.5)


![image 38](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile38.png>)

m

1 Λ

1 m

αi2,

=

![image 39](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile39.png>)

![image 40](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile40.png>)

i=1

so that by (6.1),

 αi +

  for all i.

![image 41](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile41.png>)

m

- 1

![image 42](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile42.png>)

- 2


1 m

αi2

xi =

![image 43](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile43.png>)

i=1

The result follows, noting that by (6.5) we have mi=1 αi2 ≤ m in this case. We are almost ready to prove Proposition 5.15, but ﬁrst we need the following inequality.

- Lemma 6.3. Let α1, . . ., αm be integers ≥ 2 then


![image 44](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile44.png>)

m

m

αi2 ≤

αi + m

i=1

i=1

m

2α

,

i

i=1

and equality holds if only if αi = 2 for all i. Proof. Let α = (α1, . . ., αm). We induct on the value of Sα := mi=1(2α

i−2 − 1). If Sα = 0, then αi = 2 for all i, so that

![image 45](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile45.png>)

m

m

m

2α

αi2 = 4m =

αi + m

.

i

i=1

i=1

i=1

Suppose then that Sα > 0 so that αj ≥ 3 for some j ∈ [m]. Without loss of generality assume that j = 1. Deﬁne a new sequence of integers α′ = (α1′ , . . ., αm′ +1), as follows: Let α1′ = α2′ = α1 − 1 and αi′ = αi−1 for i = 3, 4, . . ., m + 1. Note that αi′ ≥ 2 for all i and Sα′ = Sα − 1 and so by the inductive hypothesis

- (6.6)

m+1

i=1

αi′ + (m + 1)

![image 46](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile46.png>)

m+1

i=1

αi′2 ≤

m+1

i=1

2α

′

i,

Note that

- (6.7)

m+1

i=1

2α

′

i =

m

i=1

2α

i

and

m+1

i=1

αi′ −

m

i=1

αi = α1 − 2 > 0, and also

- (6.8) (m + 1)

m+1

i=1

αi′2 − m

m

i=1

αi2 =

m

i=1

αi2 + (m + 1)(α12 − 4α1 + 2) ≥

m

i=1

αi2 − (m + 1),

where in the last inequality we used the fact that α2 − 4α + 2 ≥ −1 for α ≥ 3. Note that since αi ≥ 2 for all i, we certainly have that mi=1 αi2 > m + 1. It follows then from (6.8) that

- (6.9) (m + 1)


m

m+1

αi2. Combining (6.6), (6.7), and (6.9) we have

αi′2 > m

i=1

i=1

![image 47](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile47.png>)

m

m

αi2 <

αi + m

i=1

i=1

![image 48](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile48.png>)

m+1

m+1

m+1

′

2α

αi′ + (m + 1)

αi′2 ≤

i =

i=1

i=1

i=1

m

2α

i

i=1

as required. Note the strict inequality, and so we only have equality in the case where αi = 2 for all i.

Proof of Proposition 5.15. Consider ﬁrst the case where τ∈D(ω(τ) − 2dτ)2 > |D|. Suppose that ℓ elements of D have weight 1 and let D′ = {τ ∈ D : ω(τ) ≥ 2}. Note that by

Lemma 4.10 we have τ∈D 2ω(τ) ≤ 2k and hence

- (6.10)

τ∈D′

2ω(τ) ≤ 2k − 2ℓ.

Applying Lemma 6.2, recalling that 0 ≤ dτ ≤ w(τ) for all τ ∈ D, that dτ = 0 whenever ω(τ) = 1 and using (6.10) and Lemma 6.3 we have

τ∈D

xτ ≤ ℓ +

- 1

![image 49](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile49.png>)

- 2


 

τ∈D′

(ω(τ) − 2dτ) + |D′|

![image 50](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile50.png>)

τ∈D′

(ω(τ) − 2dτ)2



- (6.11) 

≤ ℓ +

- 1

![image 51](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile51.png>)

- 2


 

τ∈D′

ω(τ) + |D′|

![image 52](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile52.png>)

τ∈D′

ω(τ)2

  −

τ∈D

- (6.12) dτ

≤ ℓ +

τ∈D′

2ω(τ)−1 −

τ∈D

- (6.13) dτ

≤ 2k−1 −

τ∈D

- (6.14) dτ.

We analyse the conditions for equality to hold. For equality to hold in (6.12) it must be the case that for all τ ∈ D, either dτ = 0 or dτ = ω(τ). By Lemma 6.3, for equality to hold in

- (6.13) it must be the case that ω(τ) = 2 for all τ ∈ D′. It now follows from Lemma 6.2 that for equality to also hold in (6.11), we must have xτ = 1 whenever ω(τ) = 1, xτ = 2 for all τ ∈ D′ such that dτ = 0 and xτ = 0 for all τ ∈ D′ such that dτ = ω(τ). However, since each xτ is non-zero by assumption we conclude that dτ = 0 for all τ ∈ D i.e. ∆ = {0}. Finally, for equality to hold in (6.14) we must have equality in (6.10) and so D is a decomposition by Lemma 4.10. It follows that x ∈ O.


It remains to consider the case where τ∈D(ω(τ) − 2dτ)2 ≤ |D|. By Lemma 6.2 and Lemma 4.10 we then have

τ∈D

xτ ≤

- 1

![image 53](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile53.png>)

- 2 |D| +


τ∈D

ω(τ) −

τ∈D

dτ

≤

1 2 |D| +

![image 54](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile54.png>)

τ∈D

2ω(τ)−1 −

τ∈D

dτ

≤ 2k−1 −

τ∈D

- (6.15) dτ.


For equality to hold in (6.15), we must have that |D| = 2k−1 and so D is a decomposition consisting only of elements of weight 1. It follows that dτ = 0 and xτ ≤ 1 for all τ ∈ D. If equality holds throughout the above, we then have that xτ = 1 for all τ ∈ D and so x ∈ O.

7. Analytic and Combinatorial Stability

In this section we prove Proposition 5.17 thus concluding our proof of Proposition 4.11. Note that Proposition 4.11 classiﬁes the optimal points of X. We use compactness arguments to prove a result to the eﬀect that ‘almost optimal’ points of X must be close (in ℓ1 norm) to a genuine optimal point of X. Furthermore, compactness allows us to derive similar properties for X(γ) when γ is small. We then investigate what implications this has in our original combinatorial setting and complete the proof of Theorem 3.5.

Proof of Proposition 5.17. Let H be the matrix with rows and columns indexed by {0, 1, ∗}k where

Hστ =

1 if σ, τ are indistinguishable, 0 if σ, τ are distinguishable.

Note that in particular, all diagonal entries of H are equal to 1. Let w = (−ω(τ) : τ ∈ {0, 1, ∗}k) ∈ R∗, then for x ∈ R∗ we may write

F(x) = wTx + xTHx.

Suppose now that x ∈ X is an optimal point. By the proof of Lemma 5.8, there is a ﬁnite sequence x = x0, x1, . . ., xm of distinct optimal points of X where xm is compressed, and for i = 0, . . ., m−1, xi+1 = xi(πi, ρi) for some indistinguishable pair πi, ρi ∈ supp(xi). Moreover we know that ω(ρi) ≥ 2 and that πi ∈/ supp(xi+1) for all i.

Suppose that x is not compressed so that m ≥ 1. Let y = xm−1, z = xm and let π = πm−1, ρ = ρm−1. Since z = y(π, ρ), it follows from the deﬁnition of compression that z = y + α(eρ − eπ) for some α > 0. Let p = eπ − eρ. It follows, by the Taylor expansion of

- F, that


- (7.1) F(y) = F(z + αp) = F(z) + αpT∇F(z) + α2pTHp.


Recall that F(y) = F(z) = 0 by Lemma 5.3. Furthermore by direct calculation we also have pTHp = 0. It follows from (7.1) that pT∇F(z) = 0 i.e.

∂F ∂xπ

∂F ∂xρ

- (7.2)


(z) =

(z).

![image 55](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile55.png>)

![image 56](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile56.png>)

Let Iρ be the set of elements of {0, 1, ∗}k that are indistinguishable from ρ excluding ρ itself. Deﬁne Iπ similarly. From the deﬁnition of F we have

- (7.3)

∂F ∂xρ

![image 57](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile57.png>)

(z) = 2zρ + 2

τ∈Iρ

zτ − ω(ρ).

Since z is a compressed optimal point we have z ∈ O by Corollary 5.16. Since ω(ρ) ≥ 2 and ρ ∈ supp(z) we conclude that in fact ω(ρ) = 2 and so zρ = 2. Moreover since supp(z) is a distinguishable set we conclude that zτ = 0 for all τ ∈ Iρ. It follows from (7.3) that ∂F ∂xρ(z) = 2 and hence from (7.2) that

![image 58](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile58.png>)

- (7.4)


∂F ∂xπ

zτ − ω(π) = 2.

(z) = 2zπ + 2

![image 59](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile59.png>)

τ∈Iπ

Since z ∈ O we know that for all τ ∈ supp(z), ω(τ) = 1 or 2 and zτ = ω(τ) . Let w1, w2 be the number of elements of Iπ ∩supp(z) with weights 1, 2 respectively. Since π ∈/ supp(z), we can then infer from (7.4) that

- (7.5) 2w1 + 4w2 − ω(π) = 2. We also know that supp(z) is a decomposition and so
- (7.6) Q(π) =

τ∈supp(z)

(Q(τ) ∩ Q(π)) =

τ∈Iπ∩supp(z)

(Q(τ) ∩ Q(π)) ⊆

τ∈Iπ∩supp(z)

Q(τ).

The second equality comes from the fact that Q(τ) ∩ Q(π) = ∅ whenever τ and π are distinguishable. Comparing the cardinality of the sets in (7.6) yields

- (7.7) 2ω(π) ≤

τ∈Iπ∩supp(z)

2ω(τ) = 2w1 + 4w2.

Note also that ρ ∈ Iπ∩supp(z) and ω(ρ) = 2 so that w2 ≥ 1. Using (7.5), this last observation implies that ω(π) ≥ 2 whereas combining (7.5) and (7.7) we have

- (7.8) 2ω(π) − ω(π) ≤ 2w1 + 4w2 − ω(π) = 2


We deduce that ω(π) = 2 and so we have equality throughout (7.8), in particular we have equality in (7.7) and so also in (7.6). Note that |Q(π)| = |Q(ρ)| since ω(π) = ω(ρ) = 2. Recalling that ρ ∈ Iπ ∩supp(z) equality in (7.6) would therefore imply that Q(π) = Q(ρ) i.e. π = ρ. This is a contradiction and so x must be compressed.

Proposition 4.11 has the following corollary that says an almost optimal point of X must be close in norm to an actual optimal point of X. Proposition 7.1. Let η ≪ ε. If x ∈ X satisﬁes x > 2k−1 −η, then there exists an x∗ ∈ O

such that x − x∗ < ε. Proof. Consider the set

X˜ := X

Bε(x∗).

x∗∈O

X˜ is compact and so supz∈X˜ z = x ˜ for some x˜ ∈ X˜. By the deﬁnition of X˜, x˜ ∈/ O and so by Proposition 4.11, x ˜ = 2k−1 − η for some η > 0. It follows that if x ∈ X satisﬁes

x > 2k−1 − η then x ∈/ X˜ and so x ∈ Bε(x∗) for some x∗ ∈ O. The following lemma allows us to relate properties of X and X(γ) for γ small.

- Lemma 7.2. Let γ ≪ η. If x ∈ X(γ), then there exists x0 ∈ X for which x − x0 < η.


Proof. Let (γi)i∈N be a strictly decreasing sequence tending to 0, and let Xi = X(γi) for i ∈ N. Then X1, X2, . . . is a decreasing sequence of compact sets i.e. Xi+1 ⊆ Xi for i ∈ N. Consider the set

U =

Bη(z),

z∈X

an open set containing X. Note that (Xi\U)i∈N is also a decreasing sequence of compact sets and also

∞

∞

(Xi\U) =

Xi U = X\U = ∅.

i=1

i=1

By Cantor’s Intersection Theorem (see [Rud76, Theorem 2.36, p.38]) it follows that Xm\U = ∅ for some m ∈ N. In other words, if x ∈ X(γm) then x ∈ U so that x ∈ Bη(x0) for some x0 ∈ X. The result follows by taking γ ≤ γm.

Corollary 7.3. Let γ ≪ ε. If x ∈ X(γ) satisﬁes x = 2k−1, then there exists an x∗ ∈ O such that x − x∗ < ε.

Proof. Given ε > 0, let η = min{η7.1(ε/2), ε/2} and suppose that γ ≤ γ7.2(η). Suppose that x ∈ X(γ) satisﬁes x = 2k−1. By Lemma 7.2 there exists an x0 ∈ X such that x0 −x < η and so x0 > x −η = 2k−1−η. It follows from Proposition 7.1 that there exists an x∗ ∈ O such that x0 − x∗ < ε/2 and so

x − x∗ ≤ x − x0 + x0 − x∗ < η + ε/2 ≤ ε.

Let

O∗ = {x ∈ O : ω(τ) = 1 for all τ ∈ supp(x)}. In words, O∗ is the set of all elements x ∈ R∗ such that x is supported on a perfect matching of Qk and all non-zero entries of x are equal to 1. We can also view O∗ as the set of proﬁles of hypercube colourings normalised by clique size. Our aim is to use the stability-type statement of Corollary 7.3 to prove Theorem 3.5 in the following form.

- Theorem 7.4. Let n1 ≪ δ ≪ ε ≪ 1. If G is a (1 − δ)-dense, k-coloured graph with v(G) = 2k−1n, containing no monochromatic odd connected matching of order ≥ (1 + δ)n, then for any choice of proﬁle x(G) of G, there exists some x∗ ∈ O∗ such that


![image 60](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile60.png>)

x(G)/n − x∗ < ε.

First we need the following two colour Ramsey type result which is a direct consequence of the more general Theorem 1.8 in [B LS+12].

- Lemma 7.5. Let n1 ≪ δ ≪ ε. If H is a (1−δ)-dense, 2-coloured graph with v(H) ≥ (32 +ε)n, then H contains a monochromatic connected matching of order ≥ (1 + δ)n.


![image 61](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile61.png>)

![image 62](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile62.png>)

Proof of Theorem 7.4. Given ε > 0, let γ = γ7.3(ε) and δ′ = δ7.5(ε). Suppose that δ < min{γ2k−22−4k, δ′2−2k} and that n ≥ max{n7.5(δ′), δ−1}. Let G be a k-coloured graph

- as in the statement of Theorem 7.4. Let x(G) be any choice of proﬁle for G and let the corresponding proﬁle partition be (Vτ : τ ∈ {0, 1, ∗}k). Note that x(G)/n = 2k−1 and by


√

![image 63](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile63.png>)

δk22k) ⊆ X(γ). By Corollary 7.3 there exists an element x∗ ∈ O such that

Proposition 4.7, we have that x(G)/n ∈ X(

- (7.9) x(G)/n − x∗ < ε.


Suppose that x∗ ∈ O\O∗, then xτ = 2 for some τ ∈ {0, 1, ∗}k such that ω(τ) = 2. It follows from (7.9) that x(G)τ = |Vτ| > (2 − ε)n ≥ (3/2 + ε)n. Let H = G[Vτ]. By the deﬁnition of Vτ, H is a 2-coloured graph. Moreover since G has at most δ v(2G) ≤ δ′ v(2H) edges missing, the same is true for H. It follows by Lemma 7.5 that H contains a monochromatic connected matching of order ≥ (1 + δ′)n > (1 + δ)n. However, by the deﬁnition of Vτ = V (H), any monochromatic component of H is contained in a non-bipartite monochromatic component of G. Thus G contains a monochromatic odd connected matching of order > (1+δ)n contrary to assumption. We conclude that x∗ ∈ O∗.

8. The Regularity Method

In this section we discuss the tools and results we need from the regularity method. Our starting point is Szemer´edi’s Regularity Lemma [Sze78] which we discuss brieﬂy now.

Let G be a graph and let A, B be disjoint subsets of V (G). We call dG(A, B) :=

eG(A, B) |A||B|

![image 64](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile64.png>)

the density of the pair (A, B). For δ > 0, we say that the pair (A, B) is δ-regular with respect to G if, for every A′ ⊆ A and B′ ⊆ B satisfying |A′| ≥ δ|A| and |B′| ≥ δ|B|, we have

|dG(A′, B′) − dG(A, B)| < δ.

If, for d > 0, we also have that |NG(a) ∩ B| ≥ d|B| for all a ∈ A and |NG(b) ∩ A| ≥ d|A| for all b ∈ B, then we say that (A, B) is (δ, d)-super-regular with respect to G. If the graph G is clear from the context we may omit it from the above notation. The following is a version of Szemer´edi’s Regularity Lemma that appears as Theorem 1.18 in [KS96].

- Theorem 8.1 (Multicolour Regularity Lemma). For all δ > 0 and k, ℓ ∈ N there exists L = L(δ, k, ℓ) and M = M(δ, k, ℓ) such that the following holds. For all k-coloured graphs G on at least M vertices, V (G) may be partitioned into sets V0, V1 . . ., Vt such that


- • ℓ ≤ t ≤ L;
- • |V0| < δv(G) and |V1| = |V2| = . . . = |Vt|;
- • apart from at most δ 2 t exceptional pairs, the pairs (Vi, Vj), 1 ≤ i < j ≤ t, are δ-regular with respect to Gs for s = 1, . . ., k.


We now state some technical lemmas related to  Luczak’s method of connected matchings. First we need a deﬁnition. (It might be useful at this point to recall Deﬁnition 3.3.)

- Deﬁnition 8.2. Let δ, d ∈ [0, 1] and q, m ≥ 1 be integers.


- • Let F be a graph on vertex set [q] and let U1, . . ., Uq be disjoint sets of size m. We call a graph H on vertex set i∈[q] Ui a (δ, m)-regular blow-up of F if whenever {i, j} ∈ E(F), we have that (Ui, Uj) is a δ-regular pair.
- • If in addition to the above, d(Ui, Uj) ≥ d for each edge {i, j} of Fm then we say that H has minimum density d.
- • Suppose that F is a connected matching and H is a (δ, m)-regular blow-up of F with


minimum density d. If for each matching edge {i, j} of F, the pair (Ui, Uj) is in fact (δ, d)-super-regular in H, then we say that H is a (δ, d, m)-super-regular blow-up of F.

Versions of the following two lemmas abound in the literature (e.g. [KSS05], [ Luc99]), but here we give statements tailored to our needs. However since they are not new, we defer their proofs to the Appendix.

- Lemma 8.3. Let q ≥ 4 and suppose that m1 ≪ δ ≪ d. Let F be a connected matching of order q such that every vertex of F is incident to a matching edge and let H be a (δ, d, m)super-regular blow-up of F. Then the following holds:


![image 65](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile65.png>)

If i, j ∈ V (F) and there is an ij-path of length r in F, then for every pair of vertices u ∈ Ui, w ∈ Uj, there exists a uw-path of length ℓ in H for each 3q ≤ ℓ ≤ (1 − 6δ)qm such that ℓ ≡ r (mod 2).

- Lemma 8.4. Let q ≥ 4 and let m1 ≪ δ ≪ d. Let F be an odd connected matching of order q and suppose that H is a (δ, m)-regular blow-up of F with minimum density d. Then H contains a cycle of length ℓ for each odd 3q ≤ ℓ ≤ (1 − 6δ)qm.


![image 66](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile66.png>)

We borrow the following fact.

- Fact 8.5. ([GRSS07, Lemma 9]). Let H be a (1−δ)-dense graph on t vertices. Then H has

a subgraph H′ such that v(H′) ≥ (1 −

√

![image 67](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile67.png>)

δ)t and δ(H′) ≥ (1 − 2

√

![image 68](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile68.png>)

δ)t. We will also need the following two standard facts whose proofs we omit it here.

- Fact 8.6. Let 0 < δ ≤ 1/2 and let (A, B) be a δ-regular pair with density d. Suppose that A′ ⊆ A, B′ ⊆ B such that |A′| ≥ (1 − δ)|A|, |B′| ≥ (1 − δ)|B|. Then (A′, B′) is 2δ-regular with density d′ > d − δ. Moreover, if (A, B) is in fact (δ, β)-super-regular for some β > 0, then (A′, B′) is (2δ, β − δ)-super-regular.
- Fact 8.7. Let 0 < δ ≤ 1/2 and let (A, B) be a δ-regular pair with density d. Then there exist A′ ⊆ A, B′ ⊆ B such that |A′| = (1−δ)|A|, |B′| = (1−δ)|B| and (A′, B′) is (2δ, d − 2δ)super-regular.


9. Proof of Main Theorem

In this ﬁnal section we prove our main result Theorem 3.2, and therefore also Theorem 1.2. The idea is to invoke Theorem 7.4 to show that the proﬁle of a certain reduced graph is close in ℓ1-norm to the proﬁle of a hypercube colouring. We then translate this information to show that the original graph is close in edit distance to a hypercube colouring.

The stability-type methods of this section require some care due to the plethora of extremal constructions. Luckily hypercube colourings share enough common features for these methods to be viable and surprisingly we require no case analysis.

First let us state a result which is a corollary of a classical theorem of Bondy [Bon71].

- Theorem 9.1. Let G be a graph on at least 3 vertices with minimum degree > v(G)/2, then


- G is pancyclic i.e. G contains cycles of all lengths 3 ≤ ℓ ≤ v(G). Proof of Theorem 3.2. Let 0 < ε < 2−4k, let


- (9.1) η < δ ≤ min

1 9

![image 69](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile69.png>)

δ72.4(ε), δ8.3

1 k

![image 70](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile70.png>)

, δ8.4

1 k

![image 71](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile71.png>)

,

let n0 ≥ max{n7.4(δ), δ−1/2} and let L = L8.1(δ, k, 2kn0). Let n be odd with

- (9.2) n ≥ max{Lm8.3(δ), Lm8.4(δ), M8.1(δ, k, 2kn0)}. Finally let G be a k-coloured copy of KN where N > (2k−1 − η)n and assume that (†) G contains no monochromatic copy of Cn.


Applying Theorem 8.1 to G we obtain a partition of V (G) into sets V0, V1 . . ., Vt

such that

0

- (i) 2kn0 ≤ t0 ≤ L;
- (ii) |V0| < δN and |V1| = |V2| = . . . = |Vt

0|;

- (iii) apart from at most δ t


2 exceptional pairs, the pairs (Vi, Vj), 1 ≤ i < j ≤ t0, are δ-regular with respect to Gs for s = 1, . . ., k.

0

It follows that for i ∈ [t0],

- (9.3) m := |Vi| ≥

(1 − δ)N t0

![image 72](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile72.png>)

.

We construct a reduced graph R0 with vertex set {1, ..., t0} and edge set formed by pairs

- {u, w} for which (Vu, Vw) is δ-regular with respect to Gi for i = 1, . . ., k. It follows from (iii) of the above that R0 is (1 − δ)-dense. Fact 8.5 allows us to ﬁnd a subgraph R ⊆ R0


satisfying v(R) ≥ (1 −

√

![image 73](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile73.png>)

δ)t0 and δ(R) ≥ (1 − 2

√

![image 74](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile74.png>)

δ)t0. Let t = v(R) and assume without loss of generality that V (R) = {1, . . ., t}. We k-colour R by colouring an edge {u, w} with the least colour i for which

- (9.4) dG

i

(Vu, Vw) ≥

1 k

![image 75](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile75.png>)

. Let t′ = t/2k−1 and note that by (9.3) and the deﬁnition of t,

- (9.5) mt′ ≥ (1 − 2

√

![image 76](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile76.png>)

δ)n. Suppose that R contains a monochromatic odd connected matching F of order q ≥ (1+3

√

![image 77](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile77.png>)

δ)t′. Then G contains a monochromatic (δ, m)-regular blow-up of F with minimum density d for some d ≥ 1/k by (9.4). Note that since t0 ≤ L we have m ≥ m8.4(δ) by (9.3) and (9.2). It follows from Lemma 8.4 that G contains a monochromatic copy of Cn since n is odd and

3q ≤ 3L ≤ n ≤ (1 − 6δ)(1 + 3

√

![image 78](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile78.png>)

δ)mt′ ≤ (1 − 6δ)qm,

contradicting (†). We conclude that R contains no such odd connected matching. Let (Wτ : τ ∈ {0, 1, ∗}k) be a proﬁle partition of R and let x(R) = (|Wτ| : τ ∈ {0, 1, ∗}k) be the corresponding proﬁle. It follows by Theorem 7.4 that there exists x∗ ∈ O∗ such that

- (9.6) x(R)/t′ − x∗ < ε.

This tells us a lot about the structure of R, indeed it is ‘close to’ a hypercube colouring. The aim is to use this fact to eventually say the same for G. By the deﬁnition of O∗ we have that

supp(x∗) = M ⊆ {0, 1, ∗}k,

for some perfect matching M of the hypercube Qk and x∗τ = 1 for all τ ∈ M. Let W = R

τ∈M

Wτ.

We will treat W as a ‘leftover set’ of vertices of R and study only the structure of R\W. Note that by (9.6) we have

- (9.7) (1 − ε)t′ < |Wτ| < (1 + ε)t′ for all τ ∈ M,


and so by removing at most 2εt′ vertices from each part Wτ, where τ ∈ M, and absorbing these removed vertices into W, we may assume that these parts Wτ all have the same size > (1 − ε)t′. Note that even after this absorption we have

|W| = t −

|Wτ| < t − 2k−1(1 − ε)t′ = εt.

τ∈M

We make a couple of observations regarding the colouring of R with respect to these vertex classes. For j ∈ [k] we let

Ij = {τ ∈ M : τj = ∗}.

- Lemma 9.2. Let τ ∈ Ij. Then R[Wτ] is monochromatic in the colour j and has minimum


√

![image 79](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile79.png>)

degree at least (1 − 2k+1

δ)|Wτ|.

Proof. By the deﬁnition of the proﬁle partition, for each colour i = j, each pair v, w ∈ Wτ must lie in the same vertex class in an induced bipartite subgraph of Ri. It follows that if

- {v, w} ∈ E(R) then it cannot receive the colour i and hence must receive colour j. Since


√

![image 80](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile80.png>)

δ(R) ≥ (1 − 2

δ)t we have δ(R[Wτ]) ≥ |Wτ| − 1 − 2

√

√

![image 81](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile81.png>)

![image 82](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile82.png>)

δt ≥ (1 − 2k+1

δ)|Wτ| where for the last inequality we used (9.7).

- Deﬁnition 9.3. Let σ, τ ∈ {0, 1, ∗}k. We denote the set {i ∈ [k] : {σi, τi} = {0, 1}} by ∆(σ, τ). We call |∆(σ, τ)| the distance between σ and τ and denote it by d(σ, τ).


- Lemma 9.4. Let σ, τ ∈ M be distinct, then


- (i) Each edge of R[Wσ, Wτ] receives a colour from the set ∆(σ, τ);
- (ii) R[Wσ, Wτ] has minimum degree ≥ (1 − 2k+1


√

![image 83](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile83.png>)

δ)|Wσ|, in particular R[Wσ, Wτ] is connected and contains a perfect matching.

Proof. Let σ ∈ Ij, τ ∈ Iℓ. Suppose that j = ℓ. By the deﬁnition of the proﬁle partition, for each colour i ∈/ ∆(σ, τ), each pair v ∈ Wσ, w ∈ Wτ must lie in either the same vertex class in an induced bipartite subgraph of Ri or they lie in diﬀerent connected components of Ri. It follows that if {v, w} ∈ E(R) then it must receive a colour from ∆(σ, τ). Similarly, if j = ℓ then each edge of R[Wσ, Wτ] must receive a colour from ∆(σ, τ) ∪ {j}. However, by Lemma 9.2, R[Wτ] and R[Wσ] are both monochromatic in the colour j and both have minimum degree at least (1 − 2k+1

√

![image 84](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile84.png>)

δ)|Wσ| > |Wσ|/2 (recall that |Wσ| = |Wτ|). It follows, by Theorem 9.1 for example, that R[Wτ] and R[Wσ] are both Hamiltonian and non-bipartite. Using (9.7), we deduce that if an edge of R[Wσ, Wτ] receives the colour j, then R contains a monochromatic odd connected matching in the colour j of order at least

√

![image 85](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile85.png>)

|Wσ| + |Wτ| − 2 ≥ 2(1 − ε)t′ − 2 ≥ (1 + 3

δ)t′,

which we showed previously was not the case. Part (i) of the lemma follows. If v ∈ Wτ then, since δ(R) ≥ (1 − 2√δ)t, we have

![image 86](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile86.png>)

√

√

![image 87](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile87.png>)

![image 88](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile88.png>)

δt ≥ (1 − 2k+1

δ)|Wσ|. Similarly if w ∈ Wσ, then |N(w)∩Wτ| ≥ (1−2k+1

|N(v) ∩ Wσ| ≥ |Wσ| − 2

√

√

![image 89](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile89.png>)

![image 90](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile90.png>)

δ)|Wσ|. Since 1−2k+1

δ > 1/2, it follows that R[Wσ, Wτ] is connected and (e.g. by Hall’s theorem) contains a perfect matching.

Let Γ denote the k-coloured multigraph on vertex set M where we have an edge between σ and τ in each colour j for which R[Wσ, Wτ] contains an edge of colour j. Note that since δ(R) > (1 − 2

√

√

![image 91](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile91.png>)

![image 92](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile92.png>)

δ)t and |Wσ| = |Wτ| > (1 − ε)t′ > 2

δt, R[Wσ, Wτ] always contains an edge. Let Γ∗ denote the subgraph of Γ where we keep only those edges that occur as the unique edge between a given pair of vertices in Γ. Recall that for j ∈ [k], Γj, Γ∗j denote the jth colour class of Γ, Γ∗ respectively.

Lemma 9.5. For each j ∈ [k], the vertices of Γ∗j can be covered by a matching Tj ⊆ Γ∗j and the set Ij. Moreover Ij is a set of isolated vertices in Γj.

Proof. Fix j ∈ [k]. If σ ∈ Ij then σ is an isolated vertex in Γj by Lemma 9.4(i). If σ ∈/ Ij then we may assume without loss of generality that σj = 0. Let σ′ be the element of {0, 1, ∗}k such that σj′ = 1 and σi′ = σi for all i = j. Let H be the graph on M with edge set {{ρ, π} : ∆(ρ, π) = {j}}. By Lemma 9.4(i) we have H ⊆ Γ∗j. The neighbours of σ in H are precisely those elements of M that are indistinguishable from σ′ i.e. those elements of M (viewed as edges of Qk) that intersect Q(σ′). Since M is a perfect matching of Qk, and |Q(σ′)| = 2, there are either 1 or 2 such elements of M. It follows that H is the disjoint union of cycles (where we consider an edge a cycle) and the independent set Ij. Since H is bipartite with bipartition {τ ∈ M : τj = 0 or ∗} ∪ {τ ∈ M : τj = 1}, the cycles in H are all even. The result follows.

Let j ∈ [k], then for each {σ, τ} ∈ Tj (Tj as in the statement of Lemma 9.5), we may ﬁx a

monochromatic perfect matching Mστj in the colour j in R[Wσ, Wτ] by Lemmas 9.4(ii) and 9.5. Let

Mστj .

Tj =

{σ,τ}∈Tj

and note that Tj is a matching in R, monochromatic in the colour j, which covers the vertex set τ∈/I

Wτ. The following corollary hints at an important common feature of all hypercube colourings.

j

Corollary 9.6. Given j ∈ [k] and ρ ∈ M\Ij, there exists π ∈ M such that R[Wρ, Wπ] contains a monochromatic connected perfect matching in the colour j whose matching edges

are edges of Tj.

Proof. Since ρ ∈/ Ij, by Lemma 9.5 there must exist π ∈ M such that {ρ, π} is an edge of Tj ⊆ Γ∗j. By the deﬁnition of Γ∗, we have that R[Wρ, Wπ] is monochromatic in the colour j. The result follows from the deﬁnition of Tj and Lemma 9.4(ii).

It will be useful to prune the sets Vi for i ∈ R in such a way that if {x, y} is an edge of the matching Tj then Gj[Vx, Vy] is super-regular. Lemma 9.7. For each i ∈ R there exists Vi′ ⊆ Vi such that

- (i) |Vi′| = (1 − 2kδ)m for all i ∈ R,
- (ii) Gj[Vx′, Vy′] is 2k+1δ-regular with density ≥ k+11 for all j ∈ [k], {x, y} ∈ Rj,

![image 93](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile93.png>)

- (iii) Gj[Vx′, Vy′] is (2k+1δ, k+11 )-super-regular for all j ∈ [k], {x, y} ∈ Tj.


![image 94](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile94.png>)

Proof. For i ∈ R we deﬁne a sequence of subsets Vi0, . . ., Vik of Vi recursively. Let Vi0 := Vi for all i ∈ R. Suppose that for all i ∈ R we have found Viℓ ⊆ Vi with the following properties.

- (a) |Viℓ| ≥ (1 − 2ℓδ)m for all i ∈ R,
- (b) Gj[Vxℓ, Vyℓ] is 2ℓδ-regular with density ≥ 1/k − 2ℓδ for all j ∈ [k], {x, y} ∈ Rj,
- (c) Gj[Vxℓ, Vyℓ] is (2ℓδ, 1/k − 2ℓ+1δ)-super-regular for all j ∈ [ℓ], {x, y} ∈ Tj. By Fact 8.7, for each edge {u, w} in the matching Tℓ+1 (so in particular {u, w} ∈ Rℓ+1) there exists Vuℓ+1 ⊆ Vuℓ and Vwℓ+1 ⊆ Vwℓ such that |Vuℓ+1| = (1 − 2ℓδ)|Vuℓ|, |Vwℓ+1| = (1 − 2ℓδ)|Vwℓ|


and Gℓ+1[Vuℓ+1, Vwℓ+1] is (2ℓ+1δ, 1/k − 2ℓ+2δ)-super-regular. If i is not incident to any edge of Tℓ+1 then simply set Viℓ+1 = Viℓ. Note that by (a), for all i ∈ R,

|Viℓ+1| ≥ (1 − 2ℓδ)|Viℓ| ≥ (1 − 2ℓδ)2m ≥ (1 − 2ℓ+1δ)m. For j ∈ [k] and {x, y} ∈ Rj, by (b) and Fact 8.6 we have that Gj[Vxℓ+1, Vyℓ+1] is 2ℓ+1δ-regular with density ≥ 1/k − 2ℓ+1δ. Using (c) and Fact 8.6, it also follows that Gj[Vxℓ+1, Vyℓ+1] is (2ℓ+1δ, 1/k − 2ℓ+2δ)-super-regular for all j ∈ [ℓ], {x, y} ∈ Tj. We have shown that the sets Viℓ+1, i ∈ R, satisfy (a)-(c) (with ℓ replaced by ℓ + 1). The result follows by letting Vi′ be any subset of Vik of size (1 − 2kδ)m for all i ∈ R and appealing to Fact 8.6, noting that

- 1/(k + 1) ≤ 1/k − 2k+2δ.

Given σ ∈ M, let

Wσ =

i∈Wσ

Vi′ ⊆ V (G), and let

W = V (G)

τ∈M

Wτ.

As with W, we think of W as a small leftover set of vertices. Let m′ := (1−2kδ)m and note that by (9.5), m′t′ ≥ (1 − 3

√

![image 95](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile95.png>)

δ)n and so by (9.7) (9.8) | Wτ| ≥ (1 − ε)m′t′ ≥ (1 − 2ε)n for all τ ∈ M. We also have (9.9) | W| ≤ N − 2k−1(1 − ε)m′t′ = N − (1 − ε)(1 − 2kδ)mt ≤ 2εN. Where for the last inequality we recalled (9.3).

We can now establish our ﬁrst piece of structure on the graph G. We show that almost all of V (G) can be covered by 2k−1 monochromatic cliques of equal size. First we make a quick deﬁnition.

Deﬁnition 9.8. If τ ∈ {0, 1, ∗}k has weight 1, we let c(τ) denote the unique element of i ∈ [k] for which τi = ∗.

Lemma 9.9. For all σ ∈ M, G[ Wσ] is monochromatic in the colour c(σ).

Proof. Suppose that G[ Wσ] contains an edge {x, y} of colour j = c(σ) (so that σ ∈/ Ij). By Corollary 9.6 there exists τ ∈ M such that Rj[Wσ, Wτ] contains a connected perfect matching, F, whose matching edges are edges of Tj. Let q := v(F), then by (9.7) we have

- 2(1 − ε)t′ ≤ q ≤ 2(1 + ε)t′. By Lemma 9.7 we see that Gj[ Wσ, Wτ] contains a spanning (2k+1δ, 1/(k + 1), m′)-super-regular blow-up of F (with the Vi′ playing the role of the Ui in


- Deﬁnition 8.2). Suppose that x ∈ Va′ and y ∈ Vb′, then a and b lie on the same side of the bipartition of the connected graph F and so F contains an ab-path of even length. Note that m′ ≥ n8.3(δ), by (9.3) and (9.2). We may therefore apply Lemma 8.3 to deduce that Gj[ Wσ, Wτ] contains a path of length n − 1 joining x and y since n − 1 ≡ 0 (mod 2) and


- (9.10) (1 − 6 · 2kδ)qm′ ≥ 2(1 − 6 · 2kδ)(1 − ε)m′t′ ≥ n − 1 ≥ 3L ≥ 3q,


where we used (9.1), (9.2) and (9.8). Together with the edge {x, y} this creates a monochromatic copy of Cn in G, contrary to assumption (†).

Our aim now is to say something about the edges of G lying between W and the rest of the graph (see Lemma 9.12 below). With the multigraph Γ in mind, we make the following deﬁnition.

- Deﬁnition 9.10. Let M′ be a perfect matching of Qk and let ϕ : M → M′ be a bijection such that c(ϕ(τ)) = c(τ) for all τ ∈ M. Suppose that Ψ is a k-coloured multigraph on vertex set M. We call ϕ an admissible labelling of Ψ if for all σ, τ ∈ M, the edges between σ, τ in Ψ only take colours from the set ∆(ϕ(σ), ϕ(τ)).


Note that by Lemma 9.4(i) the identity map ι : M → M is an admissible labelling of Γ. The following Lemma gives a useful way of generating new admissible labellings of Γ. For τ ∈ {0, 1, ∗}k, such that τj = ∗, we let τj := (τ1, . . ., τj−1, 1 − τj, τj+1, . . ., τk) i.e. τj denotes τ with the jth coordinate ﬂipped.

- Lemma 9.11. Let ϕ be an admissible labelling of Γ. Let j ∈ [k] and let C be the vertex set

of a component of Γj such that τj = ∗ for all τ ∈ C. Let ϕ′ be the function on M given by ϕ′(τ) = ϕ(τ)j for all τ ∈ C, ϕ′(τ) = ϕ(τ) otherwise. Then ϕ′ is an admissible labelling of Γ.

Proof. First note that by the deﬁnition of ϕ′ and the fact that ϕ is admissible, each element of ϕ′(M) has weight 1 and c(ϕ′(τ)) = c(ϕ(τ)) = c(τ) for all τ ∈ M. Let us check that the image of ϕ′ is a perfect matching of Qk (i.e. a distinguishable set of size 2k−1). It suﬃces to show that if σ, τ ∈ M are distinct, then ϕ′(σ), ϕ′(τ) are distinguishable (i.e. ∆(ϕ′(σ), ϕ′(τ)) = ∅). We do this by considering an edge between σ and τ in Γ and showing that if it has the colour

- i then i ∈ ∆(ϕ′(σ), ϕ′(τ)). Note that this in fact suﬃces to show that ϕ′ is admissible. Suppose then that there is an edge between σ, τ in Γ in the colour i. Since ϕ is admissible


we have i ∈ ∆(ϕ(σ), ϕ(τ)). Suppose that i = j then by the deﬁnition of ϕ′, ϕ′(τ)i = ϕ(τ)i and ϕ′(σ)i = ϕ(σ)i and so i ∈ ∆(ϕ′(σ), ϕ′(τ)) also. Suppose then that i = j, so that either σ, τ ∈ C or σ, τ ∈ M\C. If σ, τ ∈ C, then ϕ′(τ)i = 1 − ϕ(τ)i, ϕ′(σ)i = 1 − ϕ(σ)i and if σ, τ ∈ M\C, then ϕ′(τ)i = ϕ(τ)i, ϕ′(σ)i = ϕ(σ)i. In either case i ∈ ∆(ϕ′(σ), ϕ′(τ)).

The following lemma allows us to associate each vertex in W to some class Wσ in G.

- Lemma 9.12. Let v ∈ W. Then there exists σ ∈ M such that G[v, Wσ] is monochromatic in the colour c(σ).


Proof. Suppose otherwise, then for each σ ∈ M there exists a u ∈ Wσ such that the edge {v, u} receives a colour jσ = c(σ). We augment the multigraph Γ in the following way. We add the vertex v to Γ and for each σ ∈ M we add an edge between v and σ in the colour jσ. Let us call this augmented multigraph Γ+.

- Claim 9.13. Γ+ contains a monochromatic odd cycle.


Proof of Claim. Suppose otherwise and choose an admissible labelling ϕ of Γ that minimises the function

|{τ ∈ M : jτ = i and ϕ(τ)i = 1}|.

S(ϕ) =

i∈[k]

Suppose that S(ϕ) > 0, then there exists a colour j ∈ [k] and an element σ ∈ M for which

- jσ = j and ϕ(σ)j = 1. Let C denote the component of Γj containing the vertex σ and note that by the deﬁnition of admissibility C is bipartite with parts {τ ∈ C : ϕ(τ)j = 0} and {τ ∈ C : ϕ(τ)j = 1}. Note that since C is connected in Γj this is the unique bipartition of C. Since Γ+j is bipartite by assumption we must therefore have that ϕ(τ)j = 1 for all τ ∈ C such that jτ = j. Let ϕ′ denote the function on M given by ϕ′(τ) = ϕ(τ)j for all τ ∈ C, ϕ′(τ) = ϕ(τ) otherwise. By Lemma 9.11, ϕ′ is an admissible labelling of Γ, however S(ϕ′) < S(ϕ) contradicting the minimality of ϕ. We conclude that S(ϕ) = 0 i.e.


- (9.11) For all i ∈ [k], τ ∈ M, if jτ = i then ϕ(τ)i = 0.


Since ϕ(M) is a perfect matching of Qk, there must exist ρ ∈ M such that the edge ϕ(ρ) is incident to the vertex (1, 1, . . ., 1) (formally Q(ϕ(ρ)) contains (1, 1, . . ., 1)). Without loss of generality suppose ϕ(ρ) = (∗, 1, . . ., 1). However, whatever value jρ takes, we contradict

- (9.11). This concludes the proof of the claim.

Suppose that Γ+ contains a monochromatic odd cycle in the colour j. Since Γj is bipartite and Γ+j is not, there must exist σ, τ ∈ M such that σ, τ lie in opposite parts of the bipartition of a connected component in Γj and the edges {v, σ}, {v, τ} both have colour j in Γ+. By the deﬁnition of Γ+, there exist vertices u ∈ Wσ, w ∈ Wτ such that {v, u} and {v, w} both have colour j in G and j = c(σ) or c(τ) i.e. σ, τ ∈/ Ij. Suppose that u ∈ Va′ and w ∈ Vb′ then by Lemmas 9.4(ii) and 9.5 and the deﬁnition of Tj, a and b lie in opposite parts of a bipartite connected matching, F, in Rj whose matching edges span F and are edges of Tj (in particular there is an ab-path of odd length in F). Moreover we may assume that F spans the vertex sets Wσ, Wτ in Rj and so by (9.7), 2(1 − ε)t′ ≤ v(F) ≤ v(R) ≤ L. By Lemma 9.7, we have a (2k+1δ, 1/(k +1), m′)-super-regular blow-up of F in Gj. By Lemma 8.3 (using inequalities as in (9.10) and noting that n − 2 is odd) there exists a path of length n − 2 joining u and w in Gj. This together with the edges {v, u}, {v, w} forms a monochromatic copy of Cn in G contrary to assumption (†). This concludes the proof of Lemma 9.12.

Using Lemma 9.12 we may deﬁne a function f : W → M where f(v) is an element of M such that G[v, Wf(v)] is monochromatic in the colour c(f(v)). For each τ ∈ M, let Uτ = Wτ ∪ f−1({τ}). By (9.8), (9.9), (9.3) and Lemma 9.9 we have that

- (9.12) δ(Gc(τ)[Uτ]) ≥ (1 − 2k+1ε)|Uτ| for all τ ∈ M.


Note that the sets Uτ, τ ∈ M, partition the vertex set of G and so if N ≥ 2k−1(n − 1) + 1 then by the pigeonhole principle there exists σ ∈ M such that |Uσ| ≥ n. However, by (9.12) and Theorem 9.1, it follows that Uσ contains a monochromatic copy of Cn in the colour c(σ), contrary to assumption (†). We therefore have that N ≤ 2k−1(n−1). Note that at this point we have done enough to prove Theorem 1.2.

It remains to show that G is close in edit distance to a hypercube colouring. Recall that | W| ≤ 2εN and so there are at most 2εN2 edges of G incident to W. We now aim to show that G\ W is close to a hypercube colouring. Recall that we have partitioned the vertex set of G\ W into the monochromatic, equally sized cliques { Wτ : τ ∈ M}. For σ ∈ M, we showed that | Wσ| ≥ (1 − 2ε)n and Wσ is monochromatic in the colour c(σ). First note that

- at most 2εn vertices of G\ Wσ have more than 2εn neighbours in Wσ in the colour c(σ) else we immediately ﬁnd a monochromatic Cn in the colour c(σ) in G. It follows that there are


at most 2εnN edges leaving the clique Wσ in the colour c(σ). Over all τ ∈ M, there are therefore at most 2kεnN < 3εN2 edges in total leaving a clique Wτ in the colour c(τ).

Let Φ now be the multigraph on vertex set M where we have an edge between σ and τ in the colour j for each j ∈/ {c(σ), c(τ)} for which G[ Wσ, Wτ] contains a matching of two edges in the colour j. First we observe that to complete the proof it suﬃces to show that there exists an admissible labelling ϕ of Φ (recall Deﬁnition 9.10). Indeed suppose that this is the case, then since ϕ is admissible, for each pair of distinct σ, τ ∈ M and each j ∈/ ∆(ϕ(σ), ϕ(τ)) ∪ {c(σ), c(τ)}, we have that Gj[ Wσ, Wτ] contains no matching of two edges and hence contains at most | Wσ| < n edges in total. It follows that there is a hypercube colouring H associated to the perfect matching ϕ(M) of Qk, where H has vertex set V (G)\ W, such that for each i ∈ [k],

2k−1 2 ≤ 6εN2.

|Gi△Hi| ≤ 2εN2 + |(G\ W)i△Hi| ≤ 2εN2 + 3εN2 + n

The 2εN2 term accounts for edges of Gi incident to W, the 3εN2 term accounts for edges of

- Gi leaving a clique Wτ where c(τ) = i, and the n 2

k−1

2 term accounts for edges of Gi lying between pairs Wτ, Wσ for which i ∈/ ∆(ϕ(σ), ϕ(τ)) ∪ {c(σ), c(τ)}. We have thus shown that G is 6ε-close to H. It remains to show that we have the desired labelling of Φ.

Claim 9.14. Φ contains no monochromatic odd cycle. Proof of Claim. Suppose otherwise and let σ1 . . .σℓ be an odd cycle in Φ in the colour j. This allows us to ﬁx a matching of size two in graphs Gj[ Wσ

i

, Wσ

i+1

] for i = 1, . . ., ℓ (where σℓ+1 := σ1). Let S be the subset of vertices of G saturated by these matchings and note that |S| < 2k+1. We ﬁrst aim to build a short even path in Gj with endpoints in Wσ

1

and Wσ

ℓ

. Let x ∈ S ∩ Wσ

1

and suppose that for some 2 ≤ r < ℓ there exists y ∈ Wσ

r

such that

- Gj contains an xy-path Pr of length r − 1 + 2L(r − 2) where |Pr ∩ S ∩ Wσ


r| = 1 and Pr ∩ S ∩ Wσ

= ∅ for r < s ≤ ℓ (note that this does indeed hold for r = 2). We may then pick w ∈ Wσ

s

r ∩S and z ∈ Wσ

r+1 ∩S such that {w, z} is an edge of Gj[ Wσ

, Wσ

] and w = y

r

r+1

(here we are using that we have a matching of size two available to us by the deﬁnition of Φ). By the deﬁnition of Φ, σr is not in Ij and so by Corollary 9.6 there exists π ∈ M such that Rj[Wσ

, Wπ] contains a connected perfect matching, F, whose matching edges are edges of Tj. By Lemma 9.7 we see that Gj[ Wσ

r

, Wπ] contains a spanning (2k+1δ, 1/(k + 1), m′)-superregular blow-up of F where 2(1 − ε)t′ ≤ v(F) ≤ 2(1 + ε)t′ by (9.7). Moreover w and y lie in the same part in the bipartition of this blow-up. By calculations similar to those made previously, we may apply Lemma 8.3 to deduce that Gj[ Wσ

r

, Wπ] contains an yw-path Q of length 2L. Moreover, since |Pr ∪ S| ≤ 2kL and using Fact 8.6 it is easy to ensure that Q only intersects Pr ∪ S at its endpoints. It follows that Pr+1 := PrQz is an xz-path of length r+2L(r−1) where |Pr+1∩S∩ Wσ

2

= ∅ for r+1 < s ≤ ℓ. It follows by recursion that there exists u ∈ Wσ

r+1| = 1 and Pr+1∩S∩ Wσ

s

and an xu-path Pℓ of length p := ℓ − 1 + 2L(ℓ − 2) and |Pℓ ∩ S ∩ Wσ

ℓ

ℓ| = 1. Note that the length of Pℓ is even. Finally, let {v, t} ⊆ S be an edge in Gj[ Wσ

] where v ∈ Wσ

and v = u. If x = t then applying Lemma 8.3 as above we ﬁnd a uv-path Q0 in the colour j of length n − p − 1 intersecting Pℓ ∪ S only at its endpoints. It follows that PℓQ0x is a monochromatic copy of

, Wσ

1

ℓ

ℓ

Cn contradicting (†). Similarly, if x = t, we ﬁnd a uv-path Q1 of length 2L and a tx-path Q2 of length n − p − 2L − 1 both in the colour j so that PℓQ1tQ2 is a monochromatic copy of Cn contradicting (†).

We now construct an admissible labelling of Φ recursively. Suppose that M′ is a perfect

matching of Qk and that ψ : M → M′ is some bijection. Let σ, τ ∈ M and suppose there is an edge f in Φ between σ and τ with colour j not in ∆(ψ(σ), ψ(τ)). We will call such an edge ‘bad’ (with respect to ψ).

Let {f1, . . ., ft} be the set of edges of Φ that are bad with respect to the identity map ι : M → M and note that ι is an admissible labelling of Φ\{f1, . . ., ft}. Suppose now that ϕi is an admissible labelling of Φi := Φ\{f1, . . ., fi} for some 1 ≤ i ≤ t. Suppose that fi is bad with respect to ϕi and that fi has colour j and lies between σ, τ ∈ M. Note that j ∈/ {c(σ), c(τ)} by the deﬁnition of Φ. Moreover by the admissibility of ϕi we have c(σ) = c(ϕi(σ)) and c(τ) = c(ϕi(τ)). Since fi is bad it follows that we must have ϕi(σ)j = ϕi(τ)j ∈ {0, 1}. Let us show that σ, τ lie in separate components of Φij (the jth colour class of Φi). Suppose otherwise and take a path in Φij joining σ and τ. Since ϕi is admissible for Φi and ϕi(σ)j = ϕi(τ)j this path must have even length. It follows that fi completes this path to a monochromatic odd cycle in Φ contradicting Claim 9.14. Let C then denote the component of Φij containing τ (so that σ ∈/ C). Let ϕi−1 be the function on M given by ϕi−1(τ) = ϕi(τ)j for all τ ∈ C, ϕi−1(τ) = ϕi(τ) otherwise. By Lemma 9.11, ϕi−1 is an admissible labelling of Φi. Since

j ∈ ∆(ϕi(σ), ϕi(τ)j) = ∆(ϕi−1(σ), ϕi−1(τ)),

we also have that ϕi−1 is an admissible labelling of Φi−1. If fi is not bad with respect to ϕi we simply let ϕi−1 = ϕi. Running this recursion to the end we obtain an admissible labelling ϕ0 of Φ as required.

Concluding Remarks. A simple adaptation of the proof method in this paper proves the following generalisation of Theorem 1.2.

Theorem 9.15. For all k ≥ 3 there exists Nk such that the following holds. If Nk ≤ n1 ≤ n2 . . . ≤ nk are all odd then

) = 2k−1(nk − 1) + 1.

R(Cn

, . . ., Cn

1

k

The oﬀ diagonal case has been well-studied: Erd˝os et al. [EFRS76] determined the value of R(Cn, Cℓ

, Cℓ

) and R(Cn, Cℓ

, Cℓ

, Cℓ

) for ℓi ﬁxed and n suﬃciently large. In a similar vein, Skokan [ABS13] determined the value of R(Cn, Cℓ

1

2

1

2

3

- as a corollory to a more general result in the study of Ramsey goodness, Allen, Brightwell and


, . . ., Cℓ

) for ℓi ﬁxed and odd satisfying ℓi > 2i for 1 ≤ i ≤ k and n suﬃciently large. In [F L07b], Figaj and  Luczak asymptotically determine the Ramsey number of a triple of large cycles with any ﬁxed combination of parities for the cycle lengths. In the case where not all of the cycles have the same parity, Ferguson [Fer15a, Fer15b, Fer15c] strengthened the asymptotic results of [F L07b] to exact results. It would be interesting to extend the methods of the present paper to such a mixed parity setting. More generally, we would like to investigate whether the analytic approach presented here has wider applications in Ramsey theory.

1

k

Acknowledgements. We would like to thank Julia B¨ottcher for helpful discussions and comments.

References

[ABS13] P. Allen, G. Brightwell, and J. Skokan. Ramsey-goodness—and otherwise. Combinatorica, 33(2):125–160, 2013. [BE73] J. A. Bondy and P. Erdo˝s. Ramsey numbers for cycles in graphs. J. Combinatorial Theory Ser. B, 14:46–54, 1973. [B LS+12] F. Benevides, T.  Luczak, A. Scott, J. Skokan, and M. White. Monochromatic cycles in 2-coloured

graphs. Combinatorics, Probability and Computing, 21(1-2):57–87, 2012. [Bon71] JA Bondy. Pancyclic graphs i. Journal of Combinatorial Theory, Series B, 11(1):80–84, 1971. [BV04] S. Boyd and L. Vandenberghe. Convex optimization. Cambridge University Press, Cambridge,

2004. [CGP97] LH Clark, JC George, and TD Porter. On the number of l-factors in the n-cube. Congressus Numerantium, pages 67–70, 1997. [CL75] E. J. Cockayne and P. J. Lorimer. The Ramsey number for stripes. J. Austral. Math. Soc., 19:252– 256, 1975. [DJ16] A. N. Day and J. R. Johnson. Multicolour Ramsey Numbers of Odd Cycles. ArXiv e-prints, February 2016, 1602.07607. [EFRS76] P. Erdo˝s, R. J. Faudree, C. C. Rousseau, and R. H. Schelp. Generalized ramsey theory for multiple colors. Journal of Combinatorial Theory, Series B, 20(3):250–264, 1976. [EG59] P. Erdo˝s and T. Gallai. On maximal paths and circuits of graphs. Acta Math. Acad. Sci. Hungar, 10:337–356 (unbound insert), 1959.

[EG75] P. Erdo˝s and R. L. Graham. On partition theorems for ﬁnite graphs. In Inﬁnite and ﬁnite sets (Colloq., Keszthely, 1973; dedicated to P. Erdo˝s on his 60th birthday), Vol. I, pages 515–527. Colloq. Math. Soc. J´anos Bolyai, Vol. 10. North-Holland, Amsterdam, 1975.

[Erd47] P. Erdo˝s. Some remarks on the theory of graphs. Bulletin of the American Mathematical Society, 53(4):292–294, 1947. [ES35] P. Erdo˝s and G. Szekeres. A combinatorial problem in geometry. Compositio Mathematica, 2:463– 470, 1935.

- [Fer15a] D. Ferguson. The ramsey number of mixed-parity cycles i. arXiv preprint arXiv:1508.07154, 2015.
- [Fer15b] D. Ferguson. The ramsey number of mixed-parity cycles ii. arXiv preprint arXiv:1508.07171, 2015.
- [Fer15c] D. Ferguson. The ramsey number of mixed-parity cycles iii. arXiv preprint arXiv:1508.07176, 2015.


- [F L07a] A. Figaj and T.  Luczak. The Ramsey number for a triple of long even cycles. J. Combin. Theory Ser. B, 97(4):584–596, 2007.
- [F L07b] A. Figaj and T.  Luczak. The Ramsey number for a triple of large cycles. ArXiv e-prints, September 2007, 0709.0048.


[FS74] R. J. Faudree and R. H. Schelp. All Ramsey numbers for cycles in graphs. Discrete Math., 8:313– 329, 1974. [GH88] N. Graham and F. Harary. The number of perfect matchings in a hypercube. Applied Mathematics Letters, 1(1):45–48, 1988. [GRSS07] A. Gy´arf´s, M. Ruszink´, G. N. Sa´rk¨ozi, and E. Szemer´edi. Three-color Ramsey numbers for paths. Combinatorica, 27(1):35–69, 2007.

[KS96] J. Koml´os and M. Simonovits. Szemer´edi’s regularity lemma and its applications in graph theory. In Combinatorics, Paul Erdo˝s is eighty, Vol. 2 (Keszthely, 1993), volume 2 of Bolyai Soc. Math. Stud., pages 295–352. J´anos Bolyai Math. Soc., Budapest, 1996.

[KSS05] Y. Kohayakawa, M. Simonovits, and J. Skokan. The 3-colored Ramsey number of odd cycles. In Proceedings of GRACO2005, volume 19 of Electron. Notes Discrete Math., pages 397–402 (electronic), Amsterdam, 2005. Elsevier.

[ LSS12] T.  Luczak, M. Simonovits, and J. Skokan. On the multi-colored Ramsey numbers of cycles. J. Graph Theory, 69(2):169–175, 2012.

[ Luc99] T.  Luczak. R(Cn,Cn,Cn) ≤ (4 + o(1))n. J. Combin. Theory Ser. B, 75(2):174–187, 1999. [OP13]¨ P. RJ Osterga˚rd¨ and V. H. Pettersson. Enumerating perfect matchings in n-cubes. Order, pages

1–15, 2013. [PL86] Michael D Plummer and La´szl´ Lov´asz. Matching theory, volume 29. Elsevier, 1986. [Rad94] S. P. Radziszowski. Small Ramsey numbers. Electron. J. Combin., 1:Dynamic Survey 1, 30 pp.

(electronic), 1994. [Ram30] F. P. Ramsey. On a Problem of Formal Logic. Proc. London Math. Soc., S2-30(1):264, 1930. [Ros73] V. Rosta. On a Ramsey-type problem of J. A. Bondy and P. Erdo˝s. I, II. J. Combinatorial Theory

Ser. B, 15:94–104; ibid. 15 (1973), 105–120, 1973. [Rud76] W. Rudin. Principles of Mathematical Analysis. International series in pure and applied mathematics. McGraw-Hill, 1976.

[Sze78] E. Szemer´edi. Regular partitions of graphs. In Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.

Appendix A. Proof of Lemmas 8.3 and 8.4 We use the following simple property of regular pairs which appears as Lemma 5 in [F L07b].

Lemma A.1. Let 1/m ≪ δ ≪ d and let G = (V1, V2) be a (δ, d)-super-regular pair with |V1| = |V2| = m. Then for each pair u ∈ V1, w ∈ V2, G contains a uw-path of length ℓ for each odd 3 ≤ ℓ ≤ 2(1 − 5δ)m.

- Lemma 8.3. Let q ≥ 4 and suppose that m1 ≪ δ ≪ d. Let F be a connected matching of order q such that every vertex of F is incident to a matching edge and let H be a (δ, d, m)super-regular blow-up of F. Then the following holds:


![image 96](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile96.png>)

If i, j ∈ V (F) and there is an ij-path of length r in F, then for every pair of vertices

- u ∈ Ui, w ∈ Uj, there exists a uw-path of length ℓ in H for each 3q ≤ ℓ ≤ (1 − 6δ)qm such that ℓ ≡ r (mod 2).


Proof. Take i, j ∈ V (F) and let u ∈ Ui, w ∈ Uj. Let T be a spanning tree of F which includes every matching edge of F. Note that T contains a closed walk W = y0 . . .yp, where y1 = yp = i and W covers each edge of T exactly twice, in particular p = 2(q − 1) (note that q = v(F)). Using basic properties of regular pairs we can ﬁnd a path W = w0 . . . wp in H where u = w0 and wt ∈ Uy

for all t. Let P = x0 . . .xr be a path of length r in F where x0 = i, xr = j. Again, using basic properties of regular pairs we can ﬁnd a path P = v0 . . .vr in H where v0 = wp, vr = w, vt ∈ Ux

t

for all t and P intersects W only in the vertex wp. Letting Q = W P, it follows that Q is a uw-path in H of length r + p = r + 2(q − 1) ≡ r (mod 2). Suppose that {a, b} is a matching edge of F so that (Ua, Ub) is (δ, d)-super-regular in H. Note that Q visits each set Ui in H at most 3 times and so there exist Ua′ ⊆ Ua\Q, Ub′ ⊆ Ub\Q such that |Ua′| = |Ub′| = m − 3. Note that (Ua′, Ub′) is certainly (2δ, d/2)-super-regular by Fact 8.6. By construction, we may pick consecutive vertices wt, wt+1 of W (and hence Q) such that wt ∈ Ua, wt+1 ∈ Ub. By super-regularity we may then pick vertices ua ∈ N(wt+1) ∩ Ua′, ub ∈ N(wt) ∩ Ub′ such that {ua, ub} is an edge of H. Applying Lemma A.1 to (Ua′, Ub′) and vertices ua, ub, it follows that we can ﬁnd a qtqt+1-path in H which intersects Q only at its endpoints and we can choose this path to have any odd length 1 ≤ ℓ ≤ 2(1 − 5δ)(m − 3) + 2. Note that letting such a path replace the edge {qt, qt+1} in Q does not change the parity of the length of Q. Applying the same argument to each matching edge of F we see that H contains uw-paths of each

t

length r + 2(q − 1) ≤ ℓ ≤ r + 2(q − 1) + 2q · 2(1 − 6δ)m for which ℓ ≡ r (mod 2). The result follows.

![image 97](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile97.png>)

- Lemma 8.4. Let q ≥ 4 and let m1 ≪ δ ≪ d. Let F be an odd connected matching of order q and suppose that H is a (δ, m)-regular blow-up of F with minimum density d. Then H contains a cycle of length ℓ for each odd 3q ≤ ℓ ≤ (1 − 6δ)qm


![image 98](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile98.png>)

Proof. Since F is non-bipartite it contains an odd cycle C. Since the largest matching in F has q/2 edges it follows that |C| ≤ q + 1. Let T ⊆ F be a minimal tree that contains every matching edge of F. It is easy to show that T must have < 2q vertices. Let W be a closed walk in T which traverses each edge of T precisely twice (so in particular W has even length). Since W and C must intersect, we can augment the walk W by C to obtain a closed walk W′ = x1 . . . xpx1 in F where p is odd and p ≤ 3q by the above. Note that by Facts 8.6 and 8.7, we can ﬁnd H′ ⊆ H such that H′ is a (2δ, d/2, (1−δ)m)-super-regular blowup of F. Let Uj denote the vertex class of H′ corresponding to the vertex j in F for each j ∈ V (F). Using basic properties of regular pairs, we can ﬁnd an odd cycle D = v1 . . . vpv1 in H′ where vj ∈ Ux

for all j.

j

Suppose that {a, b} is a matching edge of F so that (Ua, Ub) is (2δ, d/2)-super-regular. By construction, we may pick consecutive vertices vt, vt+1 of D such that vt ∈ Ua, vt+1 ∈ Ub. Note that D visits each set Ui in H at most 3 times. We may therefore apply Lemma A.1 as we did in the proof of Lemma 8.3 to ﬁnd a vtvt+1-path Q in H′ such that Q intersects D only

- at its endpoints and we can choose Q to have any odd length 1 ≤ ℓ ≤ 2(1−5δ)[(1−δ)m−3]+2. Applying the same argument to each matching edge of F we see that H contains an odd cycle of each odd length p ≤ ℓ ≤ p + 2q · 2(1 − 6δ)m. The result follows.


![image 99](<2016-jenssen-exact-ramsey-numbers-odd_images/imageFile99.png>)

