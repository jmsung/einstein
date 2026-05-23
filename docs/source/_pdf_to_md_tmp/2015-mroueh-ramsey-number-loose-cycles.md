arXiv:1504.03668v1[math.CO]14Apr2015

The Ramsey number of loose cycles versus cliques

Ar`es M´eroueh∗ March 9, 2021

Abstract

Recently Kostochka, Mubayi and Verstra¨ete [6] initiated the study of the Ramsey numbers of uniform loose cycles versus cliques. In particular they proved that R(C3r,Knr) = θ˜(n3/2) for all ﬁxed r ≥ 3. For the case of loose cycles of length ﬁve they proved that R(C5r,Knr) = Ω((n/ log n)5/4) and conjectured that R(C5r,Knr) = O(n5/4) for all ﬁxed r ≥ 3. Our main result is that R(C53,Kn3) = O(n4/3) and more generally for any ﬁxed l ≥ 3 that R(Cl3,Kn3) = O(n1+1/⌊(l+1)/2⌋).

We also explain why for every ﬁxed l ≥ 5, r ≥ 4, R(Clr,Knr) = O(n1+1/⌊l/2⌋) if l is odd, which improves upon the result of CollierCartaino, Graber and Jiang [3] who proved that for every ﬁxed r ≥ 3, l ≥ 4, we have R(Clr,Knr) = O(n1+1/(⌊l/2⌋−1)).

# 1 Introduction

- A loose cycle of length l is a hypergraph made of l edges e1, e2, .. ., el such that, for any i,j, if j = i + 1 (mod n) or j = i − 1 (mod n) then |ei ∩ ej| = 1 and otherwise ei ∩ ej = ∅. For brevity, we shall denote by Cl such a hypergraph. An r-uniform loose cycle of length l is a loose cycle


of length l whose edges all have size r. We shall denote by Clr such a hypergraph. This is one of the possible generalizations of graph cycles, and

indeed corresponds to a cycle in the graph sense when r = 2. An r-uniform clique of order n is an r-uniform hypergraph on n vertices where all the sets of r vertices form an edge. We shall denote by Knr such a hypergraph.

The Ramsey number of an r-uniform loose cycle of length l versus an runiform clique of order n, denoted by R(Clr,Knr), is the least integer m such that whenever the edges of Kmr are coloured red and blue then Kmr either contains a red Clr (that is, a copy of Clr all of whose edges are coloured red) or a blue Knr (that is, a copy of Knr all of whose edges are coloured blue). Determining the order of magnitude of R(Cl2,Kn2) is a classical problem in

![image 1](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile1.png>)

∗Department of Pure Mathematics and Mathematical Statistics, Centre for Mathematical Sciences, Wilberforce Road, Cambridge, CB3 0WB, UK. E-mail: a.j.meroueh@dpmms.cam.ac.uk.

graph theory. The best lower bound on R(Cl2,Kn2) is due to Bohman and Keevash [1]. They proved that R(Cl2,Kn2) = Ω(n1+1/(l−2)/log(n)). For l even, the best upper bound is due to Caro, Li, Rousseau and Zhang [2]; they proved that R(Cl2,Kn2) = O((n/log(n))1+1/(l/2−1)). For l odd, the best upper bound is due independently to Li and Zang [7] and to Sudakov [10]. They proved that R(Cl2,Kn2) = O(n1+1/⌊l/2⌋/log(n)1/⌊l/2⌋). In the light of this, in subsequent discussion we shall refer to n1+1/(⌊(l−1)/2⌋) as “the graph bound”.

Recently Kostochka, Mubayi and Verstrae¨te initiated the study of R(Clr,Knr) for r ≥ 3. In [6] they proved the following theorems.

- Theorem 1.1 (Kostochka, Mubayi and Verstrae¨te [6]). There exist constants a,br > 0 such that

a

n3/2

![image 2](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile2.png>)

(log n)3/4 ≤ R(C33,Kn3) ≤ b3n3/2, and for r ≥ 4,

n3/2 (log n)3/4+o(1) ≤ R(C3r,Knr) ≤ brn3/2. For loose cycles of length ﬁve, they proved the following.

![image 3](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile3.png>)

- Theorem 1.2 (Kostochka, Mubayi and Verstrae¨te [6]). There exist constants cr > 0 such that


R(C5r,Knr) ≥ cr

n log n

![image 4](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile4.png>)

5/4

.

They also provided a more general lower bound of the form R(Clr,Knr) = Ω(n1+1/(3l−1)) for any ﬁxed r and l. They made the following conjecture. Conjecture 1.3 (Kostochka, Mubayi and Verstrae¨te [6]). For any ﬁxed r ≥ 3 we have

R(C5r,Knr) = O(n5/4). Collier-Cartaino, Graber and Jiang [3] proved the following.

- Theorem 1.4 (Collier-Cartaino, Graber and Jiang [3]). For any ﬁxed r ≥ 3 and l ≥ 4 there exist constants br,l such that


R(Clr,Knr) ≤ br,ln1+1/(⌊l/2⌋−1). For l even, they are able to improve this bound by a polylogarithmic

factor. We notice that this proves that the graph bound holds for R(Clr,Knr) when l is even but falls short when l is odd. We also notice that for r = 3

and l = 5 this says that R(C53,Kn3) = O(n2). Our main result is the following.

- Theorem 1.5. There exists a constant c3,5 such that R(C53,Kn3) ≤ c3,5n4/3 and more generally for any ﬁxed l ≥ 3 there exists a constant c3,l such that R(Cl3,Kn3) ≤ c3,ln1+1/⌊(l+1)/2⌋.

For l = 3 notice that this follows from Theorem 1.1. We believe that this result is interesting for two reasons. First, it brings the bound of O(n2) on R(C53,Kn3) due to Collier-Cartaino, Graber and Jiang down to O(n4/3), a bound much closer to Conjecture 1.3. Secondly, the bound we obtain beats the best known upper bound on R(Cl2,Kn2) i.e., the graph bound, for each l ≥ 3 by an order of magnitude. In fact, we would expect that one should be able to prove that for every ﬁxed r ≥ 3, l ≥ 3, there exist ǫr,l > 0 and cr,l > 0 such that R(Clr,Knr) ≤ cr,ln1+1/⌊(l−1)/2⌋−ǫr,l. Thus Theorem 1.1 settles this question for l = 3 and r ≥ 3, while Theorem 1.5 settles it for r = 3 and l ≥ 4. However for r ≥ 4 and l ≥ 4 the methods we use do not seem to generalize in a straightforward way (See Section 8 for more details.) The proof of Theorem 1.5 relies on generalizing various ideas found in [3], [6], [7] and [10] together with some new ones of our own. Let us now state our second result.

- Theorem 1.6. For any ﬁxed r ≥ 3, l ≥ 5, there exists cr,l > 0 such that R(Clr,Knr) ≤ cr,ln1+1/⌊l/2⌋ when l is odd.


The main point of Theorem 1.6 is that it essentially proves that the graph

bound also holds for R(Clr,Knr) when l is odd, thus completing the result of Theorem 1.4. We made no attempt at improving this by a polylogarithmic

factor as we do not believe the exponent to be correct. We shall only sketch the proof of Theorem 1.6 as most of the ideas necessary to prove it will already have been developed to prove Theorem 1.5. This sketch also serves to highlight how we can beat the graph bound if r = 3.

# 2 Notation and Tools

In this section we review some basic notation and deﬁnitions related to hypergraphs. We also state a few results which we will need in order to prove Theorem 1.5.

For a,b ∈ N, [b] denotes the set {1,2,... ,b} and [a,b] denotes the set {a,a + 1,... ,b}.

A hypergraph H = (A,B) is is a pair of ﬁnite sets A, B such that B is a set of subsets of A. The elements of A will be referred to as the vertices of H and those of B as the edges of H. For a given hypergraph H = (A,B) we let V (H) denote the set of vertices (that is, A) and let E(H) denote the set of edges (that is, B). Often when it is clear that say u, v are vertices of V , we shall write uv to mean the edge {u,v}. A hypergraph H is said to be r-uniform if all the elements of B have the same size r. We shall also call an r-uniform hypergraph an r-graph, for short. Notice that when r = 2 we

get the classical deﬁnition of a loopless graph. If a,b are two integers with a < b then an [a,b]-graph means a hypergraph whose edges each have size lying in [a,b].

Given v ∈ V (H) the degree of v in H, denoted by d(v), is the number of edges of H containing v. The average degree of H, denoted by d, is the quantity ( v∈V (H) d(v))/n.

Given a hypergraph H and a subset X of V (H), a subhypergraph of H is

- a hypergraph with vertex X ⊆ V (H) and set of edges a subset of E(H) made of edges contained in X. Given X ⊆ V (H), the induced subhypergraph of H on vertex set X, denoted by H[X], is the hypergraph (X,{e ∈ E(H) : e ⊆ X}). A hypergraph H not containing (an isomorphic copy of) a hypergraph F as a subhypergraph is said to be F-free.

Given two hypergraph H1 and H2 we shall let H1 + H2 denote the hypergraph with vertex set V (H1) ∪ V (H2) and set of edges E(H1) ∪ E(H2).

A hypergraph H is said to be simple if for all e,f ∈ E(H), if e = f then |e ∩ f| ≤ 1. Notice that loose cycles as deﬁned in Section 1 are simple hypergraphs, whereas r-uniform cliques for r ≥ 3 and n ≥ r + 1 are not.

A path of length l is a hypergraph P such that E(P) = {e1,e2,... ,el} and for all i = j, if i < j then ei ∩ ej = ∅ unless i ≤ l − 1 and j = i + 1, in which case we require ei ∩ ej = ∅. We also require all the edges of the path to have size at least 2. If P is a simple path of length l and a ∈ e1\e2 and

- b ∈ el\el−1 then we say that P joins a to b. A hypergraph H is said to be k-vertex-colourable (or k-colourable for


brevity) if there exists a map c : V (H) −→ [k] such that for any e ∈ E(H) there exist a,b ∈ e such that c(a) = c(b). This condition on c makes it a proper colouring: we remark this because later we shall also refer to any map f : V (H) −→ [k] as a colouring. Suppose V (H) is totally ordered by some ordering <. A path P = {e1,e2,... ,el} of H is said to be increasing if a ≤ b whenever a ∈ ei and b ∈ ej for some i, j with i < j. Pluh´ar [8] proved the following.

- Proposition 2.1 (Pluh´ar [8]). A hypergraph H is k-colourable if and only if there exists a total ordering < of V (H) for which there is no increasing simple path of length k in H.


Thus, in particular, if H contains no simple path of length k then H is k-colourable.

A set X ⊆ V (H) is said to be independent in H if no edge of H is contained in X. The independence number of H, denoted by α(H), is the maximal size of an independent subset of V (H). An easy observation is that if H is k-colourable then α(H) ≥ |V (H)|/k. The following well-known result of Spencer [9] gives another way of bounding the independence number of a hypergraph. It is an analogue of Tura´n’s Theorem [11] for r ≥ 3.

- Proposition 2.2 (Spencer [9]). Let H be an r-uniform hypergraph with

average degree d. Then α(H) ≥ 0.5n/d

1

![image 5](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile5.png>)

r−1.

The reason why we are interested in bounding the independence number of a hypergraph is that bounding R(Cl3,Kn3) from above is clearly equivalent to bounding the independence number of Cl3-free 3-graphs from below.

- 3 Light and Heavy Pairs


Throughout this section and the next ones, l denotes a ﬁxed integer which is at least 3.

In this section we introduce the concept of light and heavy pairs of vertices in a 3-graph H. These ﬁrst appeared in the proof of the upper bound of Theorem 1.1 in [6]. We generalize the ideas found there as they will be equally useful when looking at Cl3-free 3-graphs.

- Deﬁnition 3.1. Let H be a 3-graph. A pair ab of vertices of H is called light in H if it is contained in less than 2l−2 edges of H. It is called heavy in H otherwise. We let Plight(H) be the set of all the pairs which are light in H and Pheavy(H) the set of all the pairs which are heavy in H.
- Deﬁnition 3.2. Let H be a 3-graph. An edge e of H is called heavy if it contains a pair which is heavy in H. Otherwise, it is called light. We let Eheavy(H) be the set of heavy edges of H and Elight(H) the set of light ones.
- Deﬁnition 3.3. Let H be a 3-graph. The reduced hypergraph of H, denoted by H∗, is the hypergraph with vertex set V (H) and set of edges Elight(H) ∪ Pheavy(H).


Observe that H∗ is a [2,3]-graph.

- Lemma 3.4. Let H be a 3-graph. If H +H∗ contains a Cl then H contains a Cl3.

Proof. Let C be a Cl in H+H∗. Let A be the set of edges of C which belong to E(H) and let B be the set of edges of H which belong to Pheavy(H). If B = ∅ then C is already a Cl3 in H and there is nothing to prove. If B = ∅ then let uv ∈ B. We have |V (C)\{u,v}| = l + |A| − 2 ≤ 2l − 3. Therefore since uv is contained in 2l − 2 edges of H at least one of them, call it e, doesn’t meet V (C)\{u,v}. Then if we remove uv from C and add e we obtain a Cl in H + H∗ with one less edge lying in Pheavy(H). Repeat this operation until B = ∅.

![image 6](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile6.png>)

![image 7](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile7.png>)

![image 8](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile8.png>)

![image 9](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile9.png>)

- Lemma 3.5. Let H be a Cl3-free 3-graph. Then there exist l−2 hypergraphs


H1, H2,..., Hl−2 with vertex set V (H) such that E(H) = li−=12 E(Hi) and for each i ∈ [l − 2], each edge of Hi contains a light pair in Hi.

Proof. Suppose to the contrary that there exists a Cl3-free 3-graph H for which the conclusion of the lemma does not hold. Let J0 = H and let G0 be the 2-graph with vertex set V (H) and set of edges Pheavy(H). For i ∈ [l−2], let Hi be the hypergraph with vertex set V (H) and edges those elements of E(Ji−1) containing an element of Plight(Ji−1). Let Ji be the hypergraph with vertex set V (H) and edges those elements of E(Ji−1) such that the three pairs of vertices that they contain all belong to E(Gi−1). Finally, let Gi be the 2-graph with vertex set V (H) and set of edges Pheavy(Hi).

We shall now prove by induction on k the claim that for k ∈ [0,l − 3], Gl−3−k contains a Ck2+3. First consider the base case k = 0. By our assumption on H, E(H) = li−=12 E(Hi) and therefore E(Jl−2) = ∅ since E(H) = li−=12 E(Hi)∪E(Jl−2). Let x1x2x3 ∈ E(Jl−2). By deﬁnition of Jl−2, the pairs x1x2, x2x3 and x3x1 are heavy in Jl−3 so that Gl−3 contains the C32 formed by these three pairs. Suppose now that the induction hypothesis holds for some k ∈ [0,l − 4] and let us prove it holds for k + 1. Let C = x1x2 ... xk+3 be a Ck2+3 in Gl−3−k. Since the pair xk+3x1 is heavy in Jl−3−k, it is contained in at least 2l − 2 edges of Jl−3−k. One of these therefore does not meet any vertex of C other than xk+3 and x1 since |C| ≤ l − 1; let xk+3x1y be such an edge. The pairs xk+3y and yx1 are then heavy in Jl−3−(k+1) by deﬁnition of Jl−3−k. It is also clear that the pairs x1x2, x2x3, .. ., xk+2xk+3, being heavy in Jl−3−k, are also heavy in Jl−3−(k+1). Thus x1x2 ··· xk+3y is a Ck2+4 in Gl−3−(k+1), as required. This ﬁnishes the proof of the claim.

So there exists a Cl2 in Pheavy(H). By Lemma 3.4 there exists a Cl3 in H, which is a contradiction.

![image 10](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile10.png>)

![image 11](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile11.png>)

![image 12](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile12.png>)

![image 13](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile13.png>)

Let us remark that the quantity l−2 in Lemma 3.5 is by no means tight, but since we do not care about the constant implicit in Theorem 1.5, this shall be enough for our purposes. Indeed, in the rest of this paper we shall not seek to optimize the constants appearing in the various lemmas. The next lemma will play a very important role in our argument.

- Lemma 3.6. Let H be a 3-graph. Then Elight(H) is the union of at most


- 6l − 11 simple hypergraphs.

Proof. Let G be the 2-graph with vertex set Elight(H) and where e is joined to f by an edge if |e∩f| = 2. Then this graph has maximum degree at most

- 6l − 12 (for if e ∈ Elight(H) has degree at least 6l − 11 in this hypergraph then one of the 3 pairs of vertices contained in e is contained in at least 2l−3 edges of H other than e and hence is a heavy pair in H, a contradiction). Therefore there exists a proper vertex colouring of G on 6l−11 colours; now clearly each colour class of this colouring forms a simple hypergraph with vertex set V (H).


![image 14](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile14.png>)

![image 15](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile15.png>)

![image 16](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile16.png>)

![image 17](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile17.png>)

The idea of Lemma 3.6 essentially appears in the proof of Lemma 7.7 of

[3]. Without delving into the details, let us point out that the diﬀerence here is that the authors of [3] were only seeking a large simple subhypergraph of some carefully chosen Cl-free hypergraph, whereas in our case the fact that each edge of Elight(H) is contained in one of the simple hypergraphs given by Lemma 3.6 is vital.

# 4 Extenders

In a Cl2-free 2-graph, the neighbourhood of a vertex v contains no path of length l−2, hence is (l−2)-colourable by Proposition 2.1, and so contains an

independent set of size at least |Γ(v)|/(l − 2). Furthermore, there is always a vertex whose neighbourhood is at least as large as the average degree d of the graph. Thus an elementary argument to ﬁnd a large independent set in a Cl2-free 2-graph is, provided d is large, to ﬁnd it as a subset of a neighbourhood of a vertex of large degree and, if d is small, to apply Tura´n’s Theorem [11] which guarantees the existence of an independent set of size at least n/(1 + d) where n is the number of vertices of the 2-graph in question. For 3-graphs, the situation is a bit more complicated. Extenders, which are introduced in Deﬁnition 4.1 below, will play the same role as the neighbourhood of a vertex in the argument we just gave. The various lemmas of this section are aimed at proving that extenders satisfy all the properties that are required to make the argument work, and we shall use some ideas from [6].

- Deﬁnition 4.1. A pair (X,Y ) of disjoint subsets of V (H) is called an extender if


- 1. For any u,v ∈ X with u = v and any set S ⊆ V (H)\({u,v} ∪ Y ) of size at most 2l−5 there exists a simple path of length two in H joining u to v and which contains no element of S;
- 2. |Y | ≤ 2|X|.


The size of the extender (X,Y ) is deﬁned to be |X|.

Thus an extender is a generalization of the neighbourhood of a vertex in a 2-graph in the sense that, if v is a vertex of a 2-graph G, then by letting X = Γ(v) and Y = {v} we see that (X,Y ) certainly satisﬁes the requirement of being an extender. The diﬀerence for a 3-graph is that Y will typically have size much larger than one and also that proving that large extenders exist is not as straighforward as in the 2-graph case. The following is an easy corollary to Lemma 3.4.

- Lemma 4.2. Let H be a Cl3-free 3-graph and let (X,Y ) be an extender in H. Then for any u,v ∈ X with u = v, there does not exist a simple path of length l − 2 in (H + H∗)[V (H)\Y ] joining u to v.


Proof. If there were such a path P, then if we let S = V (P)\{u,v}, clearly |S| ≤ 2l − 5 and so there exists a simple path of length two joining u to v and containing no other vertex of P; thus it forms a Cl in H + H∗. But then by Lemma 3.4 H contains a Cl3, a contradiction.

![image 18](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile18.png>)

![image 19](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile19.png>)

![image 20](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile20.png>)

![image 21](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile21.png>)

The next lemma proves that in a Cl3-free 3-graph H there exists an extender of size at least a constant times the average degree of H.

- Lemma 4.3. Let H be a Cl3-free 3-graph of average degree d. Then there exists an extender (X,Y ) such that |X| ≥ d/(24l2).


Proof. Let H1, H2, . .. , Hl−2 be hypergraphs such that E(H) = li−=12 E(Hi) and for each i, each edge of Hi contains a pair that is light in Hi. Such a collection of hypergraphs exists by Lemma 3.6. By the pigeonhole principle there exists i ∈ [l − 2] such that |E(Hi)| ≥ |E(H)|/(l − 2). We may assume without loss of generality that i = 1. For j = 1,2,3 let H1j be the hypergraph with vertex set V (H) and consisting of those edges of H1 containing precisely j light pairs in H1. We consider two diﬀerent cases.

- Case 1: |E(H11)| ≥ |E(H1)|/2. Each edge of H11 gives two pairs (x,e) of a vertex v and an edge e of H1 such that v is contained in the (unique) light pair of H1 contained in e. Therefore there exists a vertex v contained in the light pair of at least 2|E(H11)|/n edges of H11. But 2|E(H11)|/n ≥ |E(H1)|/n ≥ E(H)/(n(l − 2)) = d/(3(l − 2)). List these edges as vxiyi:

- i = 1,... ,m, m ≥ d/(3(l − 2)), so that the pairs vxi are light and the pairs vyi are heavy in H1. In particular, no yi can occur as xj for any
- j. As the pairs vxi are light, at least m/(2l − 3) of the xi’s are pairwise distinct; so we let X be a set of m/(2l − 3) pairwise distinct xi’s and let Y be {v} ∪ {yi : xi ∈ X}. We claim that the pair (X,Y ) is an extender. It is clear that |Y | ≤ 2|X|, so let us check that the ﬁrst condition holds. Let xi,xj ∈ X. Let S ⊆ V (H)\({xi,xj} ∪ Y ), |S| ≤ 2l − 5. If yi = yj then {vxiyi,vxjyj} forms a required path of length two. If yi = yj then since xjyi is heavy in H there exists z ∈ V (H)\(S ∪ {v,xi}) such that yixjz ∈ E(H). Then {vxiyi,yixjz} forms the required path of length two.


- Case 2: |E(H12) ∪ E(H13)| ≥ |E(H1)|/2. Each edge of E(H12) ∪ E(H13) deﬁnes at least one pair (v,e) of a vertex v and an edge e of H1 such that v belongs to two light pairs of e. Thus there exists a vertex v contained in two light pairs of at least |E(H1)|/(2n) ≥ d/(6(l − 2)) edges of H1. List these edges as vxiyi, 1 ≤ i ≤ m;m ≥ d/(6(l−2)), so that the pairs vxi and vyi are light for all i. The fact that these pairs are light implies that we may ﬁnd at least m/(4l − 7) pairs xiyi which are pairwise disjoint; without loss of generality the pairs xiyi are pairwise disjoint for i ∈ [1,⌈m/(4l − 7)⌉]. We let X = {xi : i ∈ [⌈m/(4l − 7)⌉]} and we let Y = {v} ∪ {yi : i ∈ [⌈m/(4l − 7)⌉]}. It is clear that |Y | ≤ 2|X| and for any i = j and any


S ⊆ V (H)\({xi,xj}∪Y ), {vxiyi,vxjyj} is a path of length two not meeting S which joins xi to xj.

![image 22](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile22.png>)

![image 23](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile23.png>)

![image 24](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile24.png>)

![image 25](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile25.png>)

We are now ready to prove Lemma 4.4, which is the main result of this section. It says that if (X,Y ) is an extender, then X contains a large independent set in H∗. Observe that being independent in H∗ is stronger than being independent in H, i.e. that any set independent in H∗ is also independent in H. This is because any edge of H contains an edge of H∗. The reason why we wish to ﬁnd an independent set in H∗ rather than merely H is that in the proof of Theorem 1.5 we will seek an independent set in H which is made of subsets of several disjoint extenders (X1,Y1), (X2,Y2),. ..(for a suitable deﬁnition of “disjoint”), and so we shall need not only that each subset of each extender is independent in H but also that there are no edges between these subsets. This is where the extra information given by the lemma will be useful.

- Lemma 4.4. Let H be a Cl3-free 3-graph and let (X,Y ) be an extender in H. Then X contains a subset Z which

- 1. is independent in H∗;
- 2. has size at least |X|/(l − 2).


- Proof of Lemma 4.4. By Lemma 4.2 H∗[X] contains no simple path of length l − 2 and hence by Proposition 2.1 is (l − 2)-colourable. Hence X contains a set Z which is independent in H∗ and has size at least |X|/(l − 2).


![image 26](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile26.png>)

![image 27](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile27.png>)

![image 28](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile28.png>)

![image 29](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile29.png>)

- 5 Neighbourhoods of Extenders


In a Cl2-free 2-graph, the ith neighbourhood of a vertex v (that is, the vertices at distance precisely i from v) is also (l − 2)-colourable provided

- i ≤ ⌊(l − 1)/2⌋ (see Erd¨os, Faudree, Rousseau and Schelp [4]). The argu-


ments of [7] and [10] use this in order to bound R(Cl2,Kn2). Likewise, the ith neighbourhood of an extender, if carefully deﬁned, will be useful in the

proof of Theorem 1.5.

- Deﬁnition 5.1. Let H be a 3-graph and let (X,Y ) be an extender in H. Let S ⊆ V (H), X ∪ Y ⊆ S. For i ∈ N and v ∈ S\(X ∪ Y ), the distance between


v and (X,Y ) within S, denoted by dS(v,(X,Y )), is the minimal length of a simple path P in H∗[S\Y ] joining v to a vertex x of X.

The ith neighbourhoud of (X,Y ) within S, denoted by ΓS,i(X,Y ), is the set {v ∈ V (H)\Y : dS(v,(X,Y )) = i}. We also let ΓS,0(X,Y ) = X. Finally, we deﬁne ΓS,≤i(X,Y ) to be j∈[0,i] ΓS,j(X,Y ).

So the ith neighbourhood of (X,Y ) within S, for i ≥ 1, consists of those vertices of S which do not lie in X and which can be joined to a vertex of

X by a path of H∗[S] of length i which does not meet Y , but by no such path of length less than i. Notice that a key element of this deﬁnition is that we are looking at paths in H∗, not H. Our motivation for introducing neighbourhoods of extenders is the following lemma, which plays the same role for neighbourhoods of extenders as Lemma 4.4 does for extenders. Again the stronger statement that ΓS,i(X,Y ) contains a large independent set in H∗ rather than H will be necessary in the proof of Theorem 1.5.

Lemma 5.2. Let H be a 3-uniform, Cl3-free hypergraph. Let (X,Y ) be an extender in H. Let S ⊆ V (H), X ∪ Y ⊆ S. Let i ∈ [m − 1] where

m = ⌊(l − 1)/2⌋ and m ≥ 2. Then ΓS,i(X,Y ) contains a set Z which

- 1. is independent in H∗;
- 2. is such that |Z| ≥ |ΓS,i(X,Y )|/bl where bl = (6l − 10)m−1 · (2m − 1)2m−1 · (l − 2)32m−1.


Let us point out that the parameter S in the deﬁnition of the ith neighbourhood of an extender plays no important role in this lemma. It will only be required later on in the proof of Theorem 1.5. What the proof of Lemma 5.2 actually shows is that amongst n vertices each joined to X by a path in H∗ of length i not meeting Y , we may ﬁnd n/bl vertices which form an independent set in H∗, where bl is a constant whose value does not matter to us.

- Proof of Lemma 5.2. For the sake of clarity, the proof will contain several subclaims.


By Lemma 3.6, Elight(H) can be partitioned into 6l − 11 simple hypergraphs which we denote by H1, H2, .. ., H6l−11. Furthermore let H0 = Pheavy(H). Thus H∗ is a [2,3]-graph whose set of edges is partitioned by the simple hypergraphs H0, H1, H2,.. ., H6l−11.

For each v ∈ ΓS,i(X,Y ) let Pv be a simple path of length i in H∗[S\Y ] which joins v to some vertex xv of X. For the rest of the proof, the choice of Pv and xv is ﬁxed for each v ∈ ΓS,i(X,Y ). We also ﬁx an enumeration of the edges of P as E(Pv) = {f1v,f2v,... ,fiv} with xv ∈ f1v and v ∈ fiv and fkv ∩ fkv+1 = ∅ for all k ∈ [i − 1], as well as an enumeration of the vertices of P as V (P) = {xv1,xv2,... ,xv|V (P)|} so that xv1 = xv and xv|V(P)| = v, and if xvr ∈ fjv, xvs ∈ fkv with j < k then r ≤ s. It is easy to see that both of the enumerations we just described exist and are unique, because the path Pv is simple and its edges have size no more than 3.

The type of Pv is the tuple (tk)ik=1 which is such that for each k ∈ [i],

fkv ∈ Htk. Clearly for any v, Pv has one of (6l−10)i possible types. Therefore we have our ﬁrst claim.

- Claim 5.3. There exists a subset Z1 of ΓS,i(X,Y ) of size at least |ΓS,i(X,Y )|/(6l− 10)i such that all the paths Pv for v ∈ Z1 are of the same type.


- Since all the paths Pv for v ∈ Z1 have the same type, it is clear that they contain the same number of vertices, and we denote by p this quantity, so p ≤ 2i +1. Let c : V (H) −→ [2i + 1] be a (not necessarily proper) colouring of the vertices of V (H). We say that a path Pv for v ∈ Z1 is rainbow with respect to c if c(xvk) = k for all k ∈ [p]. Our second claim is the following.
- Claim 5.4. There exists a colouring c : V (H) −→ [2i + 1] and a subset Z2 of Z1 of size at least |Z1|/(2i + 1)2i+1 such that Pv is rainbow with respect to c for all v ∈ Z2.

- Proof of Claim 5.4. Let c be the colouring obtained by attributing to each vertex of H one of the 2i + 1 possible colours uniformly at random and independently of other vertices. Then for any v ∈ Z1 the probability that Pv is rainbow with respect to c is precisely 1/(2i+1)p ≥ 1/(2i+1)2i+1. Thus the expected number of vertices v such that Pv is rainbow with respect to c is at least |Z1|/(2i + 1)2i+1 and so there exists a choice of c and of Z2 such that the claim holds.


![image 30](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile30.png>)

![image 31](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile31.png>)

![image 32](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile32.png>)

![image 33](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile33.png>)

In order to prove that ΓS,i(X,Y ) contains a large independent set in H∗, we wish to apply Proposition 2.1, in the same way as we did in the proof of lemma 4.4 above. Ideally we would like to say that “ΓS,i(X,Y ) cannot contain a simple path P of length l − 2 since otherwise some subpath of P, call it P′, would join two vertices a, b of ΓS,i(X,Y ) such that there is a subpath Pa′ of Pa and a subpath Pb′ of Pb, such that P′ +Pa′ +Pb′ forms a Cl, a contradiction”. There are several diﬃculties which prevent us from doing this directly, however (What happens if Pa′ and Pb′ meet each other more than once? What happens if Pa′ or Pb′ meets P′ more than once? How do we ensure that Pa′ +Pb′+P′ has length l?) The fact that the paths Pv for v ∈ Z2 are rainbow goes a long way towards resolving these problems. Indeed, notice that if u,v ∈ Z2 then V (Pu) ∩ V (Pv) = {xui : xui = xvi ,i ∈ [p]} since Pv and Pu are rainbow. This would guarantee in the discussion above, for example, that Pa and Pb intersect P only once each. But this is not enough,

- as the main problem we are faced with is to guarantee that Pa′ +Pb′ +P′ has length l. This is why we introduce the class of an edge of H∗[Z2] in what follows.


Order the vertices of H arbitrarily and let < be the chosen total ordering. Given e ∈ E(H∗[Z2]), let a be the smallest vertex under < which is contained in e and let b be the largest one. The class of e is the tuple (mk)pk=1 whose coordinates take values in {0,1,2} such that mk = 0 if xak < xbk, mk = 1 if xak = xbk and mk = 2 if xak > xbk. So there are 3p ≤ 32i+1 possible classes for an element of E(H∗[Z2]), and for each possible class t of an element of E(H∗[Z2]) we let Jt be the hypergraph with vertex set Z2 and whose edges are all the elements of E(H∗[Z2]) of type t. Our third claim is the following.

- Claim 5.5. For each element t of {0,1,2}p, Jt is (l − 2)-colourable.


- Proof of Claim 5.5. By Proposition 2.1 it is enough to show that Jt does not contain an increasing simple path of length l − 2 with respect to <. Suppose, to the contrary, that it did contain such a path P. Let a be the smallest vertex of P and b the largest one (with respect to <). Write E(P) = {e1,e2,... ,el−2} with a ∈ e1, b ∈ el−2 and ej ∩ ej+1 = ∅ for each


- j ∈ [l−3]. For each j ∈ [l−3] let uj be the vertex of P belonging to ej ∩ej+1. Furthermore let u0 = a, ul−2 = b.


Recall that by deﬁnition of Jt, each of e1, e2,.. ., el−2 has class t. Suppose that Pu0 and Pu1 do not intersect. Then, since e1 has type t, we have mk = 0 or mk = 2 for any k ∈ [i]. Let k ∈ [i]. If mk = 0 then we know, since each of e1, e2, ... , el−2 has class t, that xuk0 < xuk1 < ··· < xkul−2. Likewise, if mk = 2 we then know that xuk0 > xuk1 > ··· > xkul−2. So in either case, for any k ∈ [p], the xukj’s, j ∈ [0,l − 2], are pairwise distinct. But, since the paths Pu0,Pu1,... ,Pul−2 are rainbow with respect to c, this implies that Pu0 ∩Puj = ∅ for all j ∈ [l−2]. Thus in particular Pu0 ∩Pul−2i−2 = ∅. Hence Pu0 + {e1,e2,... ,el−2i−2} + Pul−2i−2 is a simple path of length l − 2 in H∗ not meeting Y and joining two vertices of X, a contradiction to Lemma 4.2.

Thus we may assume that Pu0 and Pu1 do intersect in some vertex. This means that some entry of t is equal to one; let q be largest such that tq = 1, and let h be largest such that xuq0 ∈ fhu0. Let A = {fhu0,fhu+10 ,... ,fiu0}, B = {fhul−2i+2h−2,fhu+1l−2i+2h−2,... ,fiul−2i+2h−2} and D = {e1,e2,... ,el−2i+2h−2}. We shall now prove that C := A + D + B is a Cl in H + H∗, which is a contradiction by Lemma 3.4 and thus ﬁnishes the proof of the claim. Let W = V (A) ∩ V (B). To prove that C is a Cl it is enough to prove that W = {xuq0}, since the rainbow property of Pu0 and Pul−2i+2h−2 implies that A and B only intersect D in u0 and ul−2i+2h−2 respectively. Since tq = 1 we have xuq0 = xuq1, xuq1 = xuq2, . .. , xuql−2i+2h−3 = xuql−2i+2h−2 and so xqu0 = xuql−2i+2h−2. Thus xuq0 ∈ W. Suppose now that there exists u ∈ W,

- u = xuq0. So u = xuw0 for some w = q. If w > q then as tw = 1 we either have xuw0 < xuw1 < ... < xuwl−2i+2h−2 or xuw0 > xuw1 > ... > xuwl−2i+2h−2 and so either way xuw0 = xlw−2i+2h−2. But then as the paths Pu0 and Pul−2i+2h−2 are rainbow, xuw0  ∈ W, a contradiction. Thus w < q. Then w ∈ fhu0 since w < q, w ∈ A and xuq0 ∈ fhu0. Also w ∈ fhul−2i+2h−2 by the rainbow property of Pu0 and Pul−2i+2h−2. Hence {xuq0,xuw0} ⊆ fhu0 ∩ fhul−2i+2h−2 and so |fhu0 ∩ fhul−2i+2h−2| ≥ 2. Notice also that fhu0 = fhul−2i+2h−2 (if not then by deﬁnition of q this can only happen if xuq0 ∈ fhu+10 and this contradicts the deﬁnition of h). But fhu0 and fhul−2i+2h−2 belong to the same simple


hypergraph Hj (for some j) since Pu0 and Pul−2i+2h−2 are of the same type, and this is a contradiction. The claim is proved.

![image 34](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile34.png>)

![image 35](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile35.png>)

![image 36](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile36.png>)

![image 37](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile37.png>)

Since Jt is (l − 2)-colourable for any class t, we see that H∗[Z2] is (l − 2)32i+1-colourable, since any edge of H∗[Z2] belongs to Jt for some t and there are at most 32i+1 values of t. We therefore have the following.

- Claim 5.6. Z2 contains a set Z of size at least |Z2|/(l − 2)32i+1 which is independent in H∗.


Lemma 5.2 is now proved.

![image 38](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile38.png>)

![image 39](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile39.png>)

![image 40](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile40.png>)

![image 41](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile41.png>)

# 6 Proof of Theorem 1.5

Before proving Theorem 1.5 in earnest, let us brieﬂy explain how one might ﬁnd a large independent set in a Cl2-free 2-graph. Let m = ⌊(l − 1)/2⌋. As mentioned at the beginning of Section 4, a simple bound on the independence number of a Cl2-free 2-graph G can be found by considering the average degree d of G. However, when l ≥ 5, we can do better. Indeed in a “typical” 2-graph G of average degree d, we expect the mth neighbourhood of a vertex to have size about dm. This is why, if d is large, it might be a better idea to seek an independent set in Γm(v) rather than Γ(v) (since Γm(v) is (l − 2)colourable), and when d is small to still apply Tura´n’s theorem as explained in Section 4. This in itself is not a valid argument, obviously, since it is not the case that |Γm(v)| ≥ dm (for some v) in every graph. But, if the mth neighbourhood of a vertex is bounded in G, then it is a better idea to look

- at the ith neighbourhood of a vertex for 1 ≤ i ≤ m−1. In fact, both [7] and [10] either ﬁnd a large independent set which is the union of large subsets of ith neighbourhoods of vertices (where some care is needed to make sure that there is no edge between these sets), or ﬁnd an induced subgraph of G of small average degree, where one can then apply Tura´n’s Theorem to ﬁnd a large independent set. We adopt the same strategy, and are able to improve upon the graph bound because we are able to put ourselves in the position of applying Proposition 2.2 with r = 3 rather than Tura´n’s Theorem. The main diﬃculty for hypergraphs is to introduce useful deﬁnitions of what is meant by a “neighbourhood” and this was the subject of the previous sections.


Let H be a Cl3-free 3-graph on n vertices. The statement of Theorem

- 1.5 is equivalent to proving that the independence number of H is at least a constant times n(m+1)/(m+2) where m = ⌊(l − 1)/2⌋, and this is what we shall prove. Let us notice that if l = 3 or l = 4, i.e. m = 1, then the theorem can be proved as follows: either H contains an extender of size at least n2/3 hence contains an independent set of size at least n2/3/(l − 2) by Lemma 4.4 or has average degree no more than 24l2n2/3 by Lemma 4.3 and hence contains an independent set of size at least 0.5n/(24l2n2/3)1/2 = n2/3/(4√6l) by Proposition 2.2 with r = 3. Thus henceforth we shall assume l ≥ 5 and so m ≥ 2.


![image 42](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile42.png>)

Notice that for every extender (X,Y ) in H such that |X| ≥ n2/(m+2) and every S ⊆ V (H) containing X ∪ Y , we may assume that there exists an integer i ∈ [0,m − 2] such that |ΓS,i+1(X,Y )| ≤ n1/(m+2)|ΓS,i(X,Y )| for

otherwise we have |ΓS,m−1(X,Y )| ≥ n(m+1)/(m+2) and so by Lemma 5.2 we can ﬁnd an independent set of size at least n(m+1)/(m+2)/bl in H.

Consider the following procedure producing a sequence ((Xk,Yk))k∈[t] of extenders of H, a sequence (Sk)k∈[t+1] of subsets of H, and a sequence (ik)k∈[t] of elements of [0,m − 2].

- • Initially, we let S1 = V (H). If there is no extender (X,Y ) in H with |X| ≥ n2/(m+2) then we STOP. Otherwise we let (X1,Y1) be an extender in H with |X1| ≥ n2/(m+2), and we let i1 be the least i ∈ [0,m − 2] such that |ΓS1,i+1(X1,Y1)| ≤ n1/(m+2)|ΓS1,i(X1,Y1)|.
- • Having obtained sequences ((Xj,Yj))j∈[k], (Sj)j∈[k] and (ij)j∈[k], we let


 .

 

Yj ∪ ΓSj,≤ij+1(Xj,Yj)

Sk+1 = V (H)\

j∈[k]

If there is no extender (X,Y ) in H[Sk+1] with |X| ≥ n2/(m+2) then we STOP. Otherwise, we let (Xk+1,Yk+1) be such an extender. This is clearly an extender in H, as H[Sk+1] is a subhypergraph of H. We let ik+1 be the least i ∈ [0,m − 2] such that |ΓSk+1,i+1(Xk+1,Yk+1)| ≤ n1/(m+2)|ΓSk+1,i(Xk+1,Yk+1)|.

Clearly, this procedure must terminate. The sequence produced has the following important property.

For every k1,k2 ∈ [t] with k1 < k2, Yk1 ∪ ΓSk

1,≤ik1+1(Xk1,Yk1) ∩ ΓSk

2,ik2(Xk2,Yk2) = ∅. (1)

Suppose ﬁrst that |St+1| ≥ n/2. Then H[St+1] contains no extender of size at least n2/(m+2). By Lemma 4.3 this implies that the average degree of H[St+1] is no more than 24l2n2/(m+2). Hence by Proposition

- 2.2 α(H[St+1]) ≥ 0.5(n/2)/(24l2n2/(m+2))1/2 = n(m+1)/(m+2)/(8√6l). But clearly α(H) ≥ α(H[St+1]) and so we are done.


![image 43](<2015-mroueh-ramsey-number-loose-cycles_images/imageFile43.png>)

So we may assume that that |St+1| ≤ n/2. We shall ﬁnd a large set which is independent in H∗ (rather than H). As mentioned above in Section 4 such

- a set is also independent in H. The reason why we look for an independent set in H∗ rather than H is that neighbourhoods of extenders are deﬁned in terms of paths in H∗ rather than H. Let


(Yk ∪ ΓSk,≤ik+1(Xk,Yk)) .

T =

k∈[t]

Since St+1 ≤ n/2 we have |T| ≥ n/2. For each k ∈ [t], by the deﬁnition of ik we have |ΓSk,ik(Xk,Yk)| ≥ |ΓSk,i(Xk,Yk)| for any i ≤ ik and |ΓSk,ik(Xk,Yk)| ≥ |ΓSk,ik+1(Xk,Yk)|/n1/(m+2). Thus,

|ΓSk,ik(Xk,Yk)| ≥ |Yk ∪ ΓSk,≤ik+1(Xk,Yk)| /((m + 2)n1/(m+2))

(Recall that by deﬁnition of an extender, |Yk| ≤ 2|Xk|.) By Lemma 5.2 (Lemma 4.4 when ik = 0), for every k ∈ [t], ΓSk,ik(Xk,Yk) contains a set Zk of size at least |ΓSk,ik(Xk,Yk)|/bl which is independent in H∗. Let Z = ∪k∈[t]Zk, so that |Z| ≥ |T|/(bl(m+2)n1/(m+2)) ≥ n(m+1)/(m+2)/(2bl(m+2)). We shall ﬁnd W ⊆ Z of size at least |Z|/22m−1 which is independent in H∗, and this shall ﬁnish the proof of Theorem 1.5.

Let v ∈ Z. Then v ∈ Zk for some k ∈ [t]. Suppose ik ≥ 1. Then as

- v ∈ ΓSk,ik(Xk,Yk), there exists a simple path Pv in H∗[Sk] which joins v to an element of Xk, which is disjoint from Yk, and which has length ik. As in the proof of Lemma 5.2, we select one such path Pv for each v ∈ W and ﬁx our choice for the rest of the proof. If ik = 0 we let Pv = {v}. Let


- c : V (H) −→ {blue,red} be a (not necessarily proper) 2-colouring of the vertices of H. We say that Pv is well-coloured by c if the colour given to v is red and the colour of any other vertex of Pv is blue. If c is a colouring obtained by randomly and uniformly assigning the colour blue or red to each


vertex of H, independently of other vertices, then the probability that Pv is well-coloured is clearly (1/2)|V (Pv)|, which is at least (1/2)2ik+1. Therefore by a mere expectation argument there exists a colouring c and W ⊆ Z with |W| ≥ |Z|/22m−1 such that for each v ∈ W, Pv is well-coloured.

Let us check that W is independent in H∗. Indeed suppose to the contrary that it isn’t. Let e ∈ H∗[W]. As each Zk is independent in H∗, e meets at least two distinct Zk’s. Let k1 be minimal such that e ∩ Zk1 = ∅. Let

- k2 > k1 be such that e∩Zk2 = ∅. Let a ∈ e∩Zk1 and let b ∈ e∩Zk2. By definition of k1 and the fact that Sk1 ⊇ Sk1+1 ⊇ Sk1+2 ⊇ ··· , we have e ⊆ Sk1, in other words e ∈ E(H∗[Sk1]). By (1) we have that e ∩ Yk1 = ∅ (Indeed,


(1) implies that that all the elements of e not lying in ΓSk

1,ik1(Xk1,Yk1) do not lie in Yk1.) Thus in fact e ∈ E(H∗[Sk1\Yk1]).

We now consider two diﬀerent cases: ik1 = 0 and ik1 ≥ 1. Consider ﬁrst the case ik1 = 0. Since e joins b to a ∈ Xk1 and e ∈ E(H∗[Sk1\Yk1]), we have b ∈ ΓSk

1,≤1(Xk1,Yk1). This is a contradiction to (1) given that

- b ∈ ΓSk


2,k2(Xk2,Yk2). Hence we may assume that ik1 ≥ 1. In this case, as Pa is well-coloured by c, its sole red vertex is a, and since e ⊆ W, all its vertices are coloured red. Hence Pa ∩ e = {a}, so that the path Pa + e is simple. But then Pa+e, being a simple path in H∗[Sk1\Yk1] of length ik1 +1 joining b to an element of Xk1, shows that b ∈ ΓSk

1,≤ik1+1(Xk1,Yk1). This is a contradiction to (1) and ﬁnishes the proof of Theorem 1.5.

# 7 Proof of Theorem 1.6

Here we shall give a sketch of the proof of Theorem 1.6. Let r, l be ﬁxed integers with r ≥ 2 and l odd, l ≥ 5. Let H be a Clr-free r-graph on n vertices.

The ﬁrst step of the proof is to show that there exists a Cl-free [2,r]-

graph H′ such that V (H′) = V (H), α(H) ≥ α(H′) and E(H′) can be partitioned into a constant number of simple hypergraphs. We shall use the same reduction ideas as in Lemma 7.5 and Lemma 7.6 of [3], but we go one step further by partitioning E(H′) into simple hypergraphs. A sunﬂower S with core C is a collection S of sets such that e,f ∈ S and e = f implies e ∩ f = C. If |S| = p and |C| = a then we say that S is an (a,p)-sunﬂower. The Sunﬂower Lemma is the following statement.

Proposition 7.1 (P. Erd¨os, R. Rado [5]). Let F be a collection of sets of size at most r. If |F| ≥ r!(p − 1)r then F contains a sunﬂower with p members.

To ﬁnd H′, one can now proceed as follows. Suppose H contains an (a,rl)-sunﬂower S for a ≥ 2. Let C be the core of S. Remove all the edges of H containing C and then add C to H. It can be checked that this does not increase the independence number of H or create a Cl. Repeat this procedure until no (a,rl)-sunﬂower exists in H with a ≥ 2. Call the resulting hypergraph H′.

Clearly no pair of vertices of H′ is contained in r!(rl−1)r edges of H′ else by Proposition 7.1 H′ would contain an (a,rl)-sunﬂower with a ≥ 2. This implies that the graph with vertex set E(H′) where e and f are adjacent if |e ∩ f| ≥ 2, has maximal degree less than r2 r!(rl − 1)r, and hence by the same argument as in Lemma 3.6 we see that E(H′) can be partitioned into 2 r r!(rl−1)r simple hypergraphs, which we denote by H1′, H2′, . .., Hp′, where p = 2 r r!(rl − 1)r.

Since α(H) ≥ α(H′), it is enough to ﬁnd in H′ an independent set of size at least a constant times nm/(m+1) where m = ⌊l/2⌋. We shall proceed

- as in the proof of Theorem 1.5. Extenders are deﬁned in the same way as before, except that now we

require |Y | ≤ (r−1)|X|. In a simple [2,r]-graph there is always an extender (X,Y ) of size at least d/r where d is the average degree of the [2,r]-graph in question (consider the neighbourhood of a vertex of maximal degree in the hypergraph). Hence in any subhypergraph of H′ there is an extender of size

- at least a constant times the average degree of that subhypergraph, because its edges can be partitioned into a constant number of simple hypergraphs.


The ith neighbourhood of an extender within a set S is deﬁned as before except that we regard (H′)∗ as being equal to H′ (Because “H′ is already reduced”.) Thus as before, for an extender (X,Y ), if 0 ≤ i ≤ m − 1 then ΓS,i(X,Y ) contains a large independent set in H′. To see why, it suﬃces to follow the argument of Lemma 5.2 where the hypergraphs H0, H1, . .., H6l−11 are replaced by H1′, H2′, . .. , Hp′ and H∗ by H′. Here we modify the deﬁnition of the type of a path Pv slightly: for Pu and Pv to be of the same type, we require as before that corresponding edges along Pu and Pv belong to the same simple hypergraph but we now also require that they have the

same size. This only aﬀects the bound obtained on |Z| in Lemma 5.2 by a constant factor.

Finally we proceed as in Section 6, but with diﬀerent parameters. Namely, an extender (X,Y ) is added to the sequence if |X| ≥ n1/(m+1), and ik+1 is the least i ∈ [0,m − 2] such that |ΓSk+1,i+1(Xk+1,Yk+1)|

≤ n1/(m+1)|ΓSk+1,i(Xk+1,Yk+1)| (As before, it is easy to see that we may assume without loss of generality that ik+1 exists.) If |St+1| ≥ n/2, then H′[St+1] is a [2,r]-graph of average degree no more than a constant times n1/(m+1). By applying Proposition 2.2 with r = 2 to the 2-graph with vertex set St+1 and set of edges {{u,v} ⊆ St+1 : ∃e ∈ H′[St+1] s.t. {u,v} ⊆ e} we ﬁnd an independent set of size at least a constant times nm/(m+1) in H′. If |St+1| ≤ n/2 then we follow the rest of the proof of Theorem 1.5 (where (H′)∗ = H′); no Zk can contain an edge of H′ by Lemma 5.2 (and Lemma 4.4) and the existence of an edge of H′ containing vertices from two distinct Zk’s again eventually implies a violation of (1).

# 8 Further Remarks

We mentioned in the introduction that we believe that one should be able, for any ﬁxed r ≥ 3 and l ≥ 3, to beat the graph bound for R(Clr,Knr) by an order of magnitude. However, the obvious generalization of the methods we use fails for r ≥ 4 and l ≥ 4. An example of a 4-uniform hypergraph where our attempts fail is the following. Let V (H) = [2n] and let E(H) = {{i,i+n,j,j+n} : i,j ∈ [n],i = j}. It is clear that this hypergraph contains no loose cycle since any two of its edges meet in 0 or 2 vertices. Naturally, this hypergraph does contain a very large independent set, but there are no useful extenders in this hypergraph, so there is no obvious argument which can make use of Proposition 2.2. It might still be possible to improve upon the graph bound for some speciﬁc values of r and l, but as no straighforward generalization seems possible we did not cover this here. The ﬁrst natural case to consider is R(C54,Kn4), where we do not know how to beat the graph bound of O(n3/2).

# 9 Acknowledgement

The author wishes to thank Andrew Thomason for his very helpful comments and advice which resulted in a much better presentation of this paper.

# References

- [1] T. Bohman, P. Keevash: The early evolution of the H-free process, Inventiones Mathematicae 181 (2010), 291–336.


- [2] Y. Caro, Y. Li, C. Rousseau and Y. Zhang, Asymptotic bounds for some bipartite graphs: complete graph Ramsey numbers, Discrete Mathematics 220 (2000), 51–56.
- [3] C. Collier-Cartaino, N. Graber and T. Jiang, Linear Tur´an numbers of r-uniform linear cycles and related Ramsey numbers, arXiv:1404.5015v2 (2014).
- [4] P. Erd¨os, R. Faudree, C. Rousseau and R. Schelp, On cycle-complete graph Ramsey numbers, Journal of Graph Theory 2 (1978), 53-64.
- [5] P. Erd¨os, R. Rado: Intersection theorems for systems of sets, Journal of the London Mathematical Society, Second Series 35 (1) (1960), 85–90.
- [6] A. Kostochka, D. Mubayi and J. Verstrae¨te, Hypergraph Ramsey numbers: triangles versus cliques, Journal of Combinatorial Theory Series A 120 (2013), 1491–1507.
- [7] Y. Li, W. Zang, The independence number of graphs with forbidden cycle and Ramsey numbers, Journal of Combinatorial Optimization 7

(2003), 353–359.

- [8] A. Pluh´ar, Greedy colorings of uniform hypergraphs, Random Structures and Algorithms 35 (2009), 216–221.
- [9] J. Spencer, Tura´n’s theorem for k-graphs, Discrete Mathematics 2 (2)

(1972), 183–186.

- [10] B. Sudakov, A note on odd cycle-complete graph Ramsey numbers, The Electronic Journal of Combinatorics 9 (2002), #N1.
- [11] P. Tura´n, On an extremal problem in graph theory, Mat. Fiz. Lapok 48


(1941), 436–452.

