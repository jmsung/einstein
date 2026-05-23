arXiv:1503.03855v2[math.CO]20Mar2015

Hypergraph Ramsey numbers: tight cycles versus cliques

Dhruv Mubayi∗ Vojtech Ro¨dl†

March 23, 2018

Abstract

For s ≥ 4, the 3-uniform tight cycle Cs3 has vertex set corresponding to s distinct points on a circle and edge set given by the s cyclic intervals of three consecutive points. For ﬁxed s ≥ 4 and s  ≡ 0 (mod 3) we prove that there are positive constants a and b with

2 logt.

2at < r(Cs3,Kt3) < 2bt

The lower bound is obtained via a probabilistic construction. The upper bound for s > 5 is proved by using supersaturation and the known upper bound for r(K43,Kt3), while for s = 5 it follows from a new upper bound for r(K53−,Kt3) that we develop.

# 1 Introduction

A k-uniform hypergraph H (k-graph for short) with vertex set V (H) is a collection of kelement subsets of V (H) (when k = 3 we will sometimes refer to a 3-graph as a triple system). Write Knk for the complete k-graph with vertex set of size n (when k = 2 we omit the superscript for Kn and other well-known graphs). Given k graphs F,G, the Ramsey number r(F,G) is the minimum n such that every red/blue coloring of Knk results in a monochromatic red copy of F or a monochromatic blue copy of G. In this paper we consider hypergraph Ramsey number of cycles versus complete graphs.

Let Cs denote the cycle of length s. For ﬁxed s ≥ 3 the Ramsey number r(Cs,Kt) has been extensively studied. The case s = 3 is one of the oldest questions in graph Ramsey theory and it is known that

r(C3,Kt) = Θ(t2/log t). (1)

![image 1](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile1.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL 60607, Email:mubayi@uic.edu. Research partially supported by NSF grants DMS-0969092 and DMS-1300138

†Department of Mathematics and Computer Science, Emory University, Atlanta, GA 30322, Email:rodl@mathcs.emory.edu. Research partially supported by NSF grants DMS-1102086 and DMS1301698

The upper bound was proved by Ajtai-Koml´os-Szemere´di [1] and the lower bound was proved by Kim [9]. More recently, Bohman-Keevash [3] and independently Fiz PontiverosGriﬃths-Morris [8] proved a lower bound that is asymptotically within a factor of 4 of the best upper bound due to Shearer [13]. The next case r(C4,Kt) seems substantially more diﬃcult and the best known upper and lower bounds are O(t2/log2 t) and Ω(t3/2/log t), respectively. An old open problem of Erd˝os asks whether there is a positive ǫ for which r(C4,Kt) = O(t2−ǫ). For larger cycles, the best known bounds can be found in [2, 14]. The order of magnitude of r(Cs,Kt) is not known for any ﬁxed s ≥ 4.

There are several natural ways to extend the deﬁnition of cycle to hypergraphs. Two possibilities are to consider loose cycles and tight cycles. The 3-uniform loose triangle T33 has 3 edges that have pairwise intersections of size one and have no point in common. A recent result due to Kostochka-Mubayi-Verstrae¨te [10] is that there are positive constants c1,c2 with

c1t3/2 (log t)3/4

< r(T33,Kt3) < c2t3/2.

![image 2](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile2.png>)

The authors in [10] conjectured that r(T33,Kt3) = o(t3/2). For longer loose cycles, the gap between the upper and lower bound is much greater.

For s ≥ k, the tight cycle Csk is the k-graph with vertex set Zs (integers modulo s) and edge set

{{i,i + 1,... ,i + k − 1} : i ∈ Zs}.

We can view the vertex set of Csk as s points on a circle and the edge set as the s circular subintervals each containing k consecutive vertices. In this note we investigate the

hypergraph Ramsey number r(Cs3,Kt3) for ﬁxed s ≥ 5 and large t.

When s ≡ 0 (mod 3) the tight cycle Cs3 is 3-partite, and in this case it is trivial to observe that r(Cs3,Kt3) grows like a polynomial in t. Determining the growth rate of this polynomial appears to be a very diﬃcult problem. We focus on the case s  ≡ 0 (mod 3). In this regime we show that the Ramsey number is exponential in t.

Theorem 1.1 Fix s ≥ 5 and s  ≡ 0 (mod 3). There are positive constants a and b such that

2at < r(Cs3,Kt3) < 2bt2 logt.

Our upper bounds for s ≥ 7 are proved by observing that the well-known supersaturation phenomenon in extremal hypergraph theory can be naturally extended to hypergraph Ramsey problems. This observation may be of independent interest. Our upper bound for s = 5 is by proving an upper bound for r(K53−,Kt3) that matches (apart from constants in the exponent) the best bound for r(K43,Kt3). We do this by showing that the method of Conlon-Fox-Sudakov [5] applies to a particular graph in the ordered setting.

# 2 Lower bound construction

Our proof is based on the following random construction.

Consider the random graph G = G(n,1/2) with vertex set [n]. Form the (random) triple system H = H(n) where V (H) = [n] and for i < j < k, we have ijk ∈ H iﬀ ij,ik ∈ G and jk  ∈ G.

Claim. If Cs3 ⊂ H(n), then 3|s. Proof of Claim. Assume that V (Cs3) = {v1,... ,vs}, the edge set is {vivi+1vi+2 : i ∈ [s]}, where indices are taken modulo s, and v1 = mini vi. We will prove by induction on i that

vivi+1  ∈ G iﬀ i ≡ 2 (mod 3).

This is true for 1 ≤ i ≤ 3 as v1v2v3 ∈ H(n) so v1v2 ∈ G and v2v3  ∈ G. As v2v3v4 ∈ H(n) we must have v4 < min{v2,v3} and hence v3v4 ∈ G. Now suppose that i ≡ 0 (mod 3), the statement is true for i − 2,i − 1, and i and let us show it for i + 1,i + 2,i + 3. Since vi−1vivi+1 ∈ H(n) and vi−1vi  ∈ G, we have vi+1 < min{vi−1,vi} and vivi+1 ∈ G. Together with vivi+1vi+2 ∈ H(n) this gives vi+1vi+2 ∈ G and vi+1 < vi+2. Next, vi+1vi+2vi+3 ∈ H(n) implies that vi+2vi+3  ∈ G and vi+1 < min{vi+2,vi+3}. Finally, vi+2vi+3vi+4 ∈ H(n) and vi+2vi+3  ∈ G implies that vi+3vi+4 ∈ G. As v1vs−1vs ∈ H(n) and v1 = mini vi we also have vs−1vs  ∈ G. Consequently, s − 1 ≡ 2 (mod 3) as desired.

![image 3](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile3.png>)

![image 4](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile4.png>)

![image 5](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile5.png>)

![image 6](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile6.png>)

A set T of t vertices in [n] is an independent set in H(n) iﬀ no triple of T is an edge of H(n). Let T be such an independent set in H(n) and S be a partial Steiner triple system with vertex set T. It is well-known that such S exist with |S| = (1+o(1))t2/6. Since T is an independent set, all triples of S are absent in H(n). As no two triples of S share two points, the probability that all triples of S are absent in H(n) is at most (7/8)|S| < (7/8)t2/7. So the probability that there exists a t-set T that is independent in H(n) is at most

n t

(7/8)t2/7 < 1

- as long at t > clog n for some constant c > 0. We conclude that there exists an H = H(n) with α(H) < clog n, and consequently for ﬁxed s  ≡ 0 (mod 3), there is a constant c > 0 such that


R(Cs3,Kt3) > 2ct.

# 3 Supersaturation

Given a hypergraph H and vertex v ∈ V (H), we say that w ∈ V (H) is a clone of v if no edge contains both v and w and for every e ∈ H, v ∈ e if and only if (e ∪ {w}) \ v ∈ H. Given a triple system F and a vertex v in F, let F(v) be the triple system obtained from F by replacing v with two clones v1,v2.

- Theorem 3.1 Let F be a triple system with f vertices and v ∈ V (F). Then r(F(v),Kt3) < (r(F,Kt3))f.


Proof. Let m = r(F,Kt3) and n = mf. Given a red/blue coloring of Kn3, we will ﬁnd a red copy of F or a blue copy of Kt3. Assume that there is no blue copy of Kt3. For every m-set of vertices, we either ﬁnd a blue copy of Kt3 or a red copy of F by deﬁnition of m. Consequently, we may assume that the number of red copies of F is at least m n / m n−−ff = (n)f/(m)f > f− n1 since n = mf. To each red copy of F associate the f −1 vertices in this copy that do not play the role of v. By the pigeonhole principle, we obtain two red copies of F with the same copy of F − v, and this yields a red copy of F(v).

![image 7](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile7.png>)

![image 8](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile8.png>)

![image 9](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile9.png>)

![image 10](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile10.png>)

A blowup of F is a a hypergraph obtained by successively applying the cloning operation. In particular, if each vertex is cloned p times, then denote the obtained blowup as F(p). By applying Theorem 3.1 repeatedly, we obtain the following easy corollary.

Corollary 3.2 Fix a k-graph F and an integer p ≥ 2. There exists c = c(F,p) such that

r(F(p),Kt3) < (r(F,Kt3))c.

Conlon-Fox-Sudakov [5] proved that r(K43,Kt3) = 2O(t2 logt) and it is an easy exercise to see that for s ≥ 6, we have Cs3 ⊂ K43(s). In other words, there is a homomorphism from Cs3 to K43(s). Consequently, Corollary 3.2 implies the upper bound in Theorem 1.1 for s ≥ 6. One can check that there is no homomorphism from C53 to K43 so we cannot apply the same argument for C53. Clearly

r(C53,Kt3) < r(K53,Kt3) < 2O(t3 logt)

where the last inequality was proved in [5]. In the next section we will improve this bound, and this will yield an alternative proof for all s ≥ 5.

# 4 K53 minus an edge

In this section we use the arguments from [5] to prove that

r(K53−,Kt3) = 2O(t2 logt) (2)

where K53− is the triple system obtained from K53 by deleting one edge. Since C53 ⊂ K53− we immediately obtain the upper bound in Theorem 1.1 for C53.

Given an ordering of the vertices v1 < v2 < ··· and an ordered graph F<, deﬁne the vertex online ordered Ramsey number of F< as follows: Consider the following game, played by two players, builder and painter: at step i + 1 a new vertex vi+1 is revealed; then, for every existing vertex vj, j = 1,... ,i, builder decides, in order, whether to draw the edge vjvi+1; if he does expose such an edge, painter has to color it either red or blue immediately. The

vertex on-line ordered Ramsey number r(F<,Kt) is then deﬁned as the minimum number of edges that builder has to draw in order to force painter to create a red ordered F< (the ordering is deﬁned by the order in which the vertices are exposed) or a blue Kt (since all edges are present in Kt, the ordering of its vertices does not matter). Vertex online ordered Ramsey numbers were studied recently in [4].

Let K4− be the ordered graph with four vertices v1 < v2 < v3 < v4 and all edges except v3v4. In other words, it is a copy of K4 with the “last” edge deleted. Our main result is the following.

- Theorem 4.1 In the vertex on-line ordered Ramsey game, builder has a strategy which


ensures a red K4− or a blue Kt−1 using at most ℓ = O(t2) vertices, a = O(t2) red edges, and m = O(t3) total edges.

Using this result, we immediately obtain the following Theorem which was proved in the unordered setting in ([5], Theorem 2.1). The ordered setting we consider here requires essentially no changes to the proof, so we do not repeat the argument.

Theorem 4.2 Suppose in the vertex on-line ordered Ramsey game that builder has a strategy which ensures a red K4− or a blue Kt−1 using at most ℓ vertices, a red edges, and in total m edges. Then, for any 0 < α < 1/2, the Ramsey number r(K53−,Kt3) satisﬁes

r(K53−,Kt3) = O(ℓα−a(1 − α)a−m).

Using α = 1/t and plugging in the values for ℓ,a,m from Theorem 4.1 into Theorem 4.2 yields (2).

Proof of Theorem 4.1. The idea of the proof is almost identical to Lemma 2.2 in [5], except that the conclusion one obtains is a bit stronger. In order to apply it to our situation, we need to make a few adjustments. The proof is based on deﬁning builder’s strategy which ensures a red graph K4− or a blue Kt−1 in the required number of steps. During the game, builder chooses the vertices one by one and exposes some edges one by one (in the way we will describe below) between the last chosen, say vi+1, and the previously chosen vertices v1,... ,vi. The decision of which edge to expose next will depend on the colors of previously chosen edges. Now we describe the strategy in more detail.

Builder will assign strings consisting of R’s and B’s to each chosen vertex and these strings are expanded during the game in the following way. Assume that the vertices v1,... ,vi have been chosen and edges between these vertices have been exposed. After choosing vi+1, the ﬁrst edge exposed is (always) v1vi+1. Depending on whether painter colors v1vi+1 red or blue the ﬁrst digit in the string assigned to vi+1 will be R or B respectively. For j,

- 2 ≤ j ≤ i, the only reason why the edge vjvi+1 is exposed is that the current labels of vj and vi+1 are identical. Let X1X2 ... Xp with Xp ∈ {R,B} for 1 ≤ q ≤ p be that label. In order to “resolve the tie” between the labels of vj and vi+1 builder relables vi+1 by a new label which is either X1X2 ... XpR or X1X2 ... XpB depending on whether painter colored the edge vjvi+1 red or blue. Builder stops choosing the vertices and exposing the edges once


painter has completed a red graph K4− or blue Kt−1. It remains to show that during the game at most ℓ = O(t2) vertices, at most O(t2) red edges, and at most O(t3) total edges

were exposed.

For a vertex v = vj and color X ∈ {R,B}, write NX(v) for the set of vertices y = vi, i > j that are exposed by builder after v such that painter has colored edge vy with X. In other words, it is the “forward” neighborhood of v in color X. An important observation we will use in the rest of the proof is the following

Fact. If y is the ﬁrst exposed vertex in NX(v), then all edges of the form yz with z ∈ NX(v) \ {y} are drawn by builder (and consequently colored by painter).

It is convenient to use the following two claims in the proof.

- Claim 1. Suppose that |NR(v)| ≥ 2s for some v and s ∈ [t − 1]. Then there is a red K4− within NR(v) ∪ {v}, or a blue Ks within NR(v).

Proof of Claim. Let wa be the ﬁrst chosen vertex in W1 = NR(v). If wa has two red neighbors x < y in W1, then v < wa < x < y is a red ordered K4− as desired. Consequently, wa has at most one vertex in W1 (call it wa′ if it exists) joined to it in red. Let W2 = W1 \ {wa,wa′} so |W2| ≥ 2(s − 1). Note that the Fact implies that all vertices in W2 (including the ﬁrst) are joined to wa (the ﬁrst vertex of W1), by a blue edge. Continuing this process, we either ﬁnd a red K4− or obtain a sequence of proper subsets W1 ⊃ W2 ⊃ ··· ⊃ Ws with |Wj| ≥ 2(s − j + 1) for each j ∈ [s]. The ﬁrst vertex of each Wj for 1 ≤ j ≤ s forms a set that induces a blue Ks within NR(v) as desired.

![image 11](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile11.png>)

![image 12](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile12.png>)

![image 13](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile13.png>)

![image 14](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile14.png>)

- Claim 2. Suppose that 1 ≤ i ≤ t−2 and |NB(v)| ≥ 2 i+12 . Then there is a red K4− within NB(v), or a blue Ki+1 within {v} ∪ NB(v).


Proof of Claim. Let us proceed by induction on i. The base case i = 1 is trivial as |NB(v)| ≥ 2 > 1 and v with the ﬁrst exposed vertex in NB(v) forms a blue K2. Now suppose that the result holds for i − 1 and we wish to prove it for i ≥ 2. Let wa be the ﬁrst chosen vertex in NB(v). By the Fact, all edges of the form wawa′ for wa′ ∈ NB(v)\{wa} have been drawn by builder and hence have been colored, so wa has at least 2 i+12 −1 = 2 2 i +2i−1 neighbors in NB(v)\{wa}. By the pigeonhole principle, either at least 2i of these neighbors are joined to wa with a red edge or at least 2 2 i of these neighbors are joined to wa with a blue edge. In the former case, Claim 1 yields either a red K4− or a blue Ki within NB(v). Together with v this gives a blue Ki+1 as desired. In the latter case, by induction we ﬁnd a blue Ki within NB(v) and together with v this yields a blue Ki+1 as desired.

![image 15](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile15.png>)

![image 16](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile16.png>)

![image 17](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile17.png>)

![image 18](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile18.png>)

Consider the online ordered game where the number of exposed vertices is 2 2 t = 2 t−21 + 2(t − 1). The number of vertices adjacent to the ﬁrst vertex v1 is 2 t−21 + 2(t − 1) so at least 2(t − 1) of them are joined to v1 with a red edge or at least 2 t−21 of them are joined to v1 with a blue edge. In the former case, apply Claim 1 with s = t − 1 and in the latter case, apply Claim 2 with i = t − 2. The claims imply that we ﬁnd a red K4− or a blue Kt−1. It follows from Claim 2 applied with i = t − 2 that the number of vertices chosen is

- at most ℓ ≤ 2 t−21 + 1. Each vertex v is joined to at most three vertices before it in red,


else we have a red K4 (which contains a red K4−), so the number of red edges is at most

- 3ℓ = O(t2). Similarly, each vertex is joined to at most t − 2 vertices before it in blue, else we have a blue Kt−1. Hence m ≤ (t + 1)ℓ = O(t3) as desired.


![image 19](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile19.png>)

![image 20](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile20.png>)

![image 21](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile21.png>)

![image 22](<2015-mubayi-hypergraph-ramsey-numbers-tight_images/imageFile22.png>)

# 5 Concluding remarks

• The arguments we presented that showed r(K53−,Kt3) = 2O(t2 logt) can easily be extended to show that for each ﬁxed s ≥ 4 we have

r(Ks3−,Kt3) = 2O(ts−3 logt). (3)

Note that the best known bound for ﬁxed cliques of size s ≥ 4 is r(Ks3,Kt3) = 2O(ts−2 logt) [5]. Consequently, (3) means that deleting one edge from Ks3 results in a substantially better bound. This leads us to ask the following question.

- Problem 5.1 Let s ≥ 5 be ﬁxed. Is log r(Ks3−1,Kt3) = o(log(r(Ks3−,Kt3))?

• As s gets large, the tight cycle Cs3 becomes sparser, so one might expect that the Ramsey number with Kt3 (for ﬁxed s) decreases as a function of t. We were not able to show this and pose the following problem.

- Problem 5.2 Is the following true? For each ﬁxed s ≥ 4 there exists ǫs such that ǫs → 0 as s → ∞ and


r(Cs3,Kt3) < 2t1+ǫs for all suﬃciently large t.

• To address the problem of determining r(Csk,Ktk) for ﬁxed s > k > 3, we can generalize the construction that we used for k = 3. Consider the random (k − 1)-graph Gk−1 = Gk−1(n,1/2) with vertex set [n]. Form the (random) k-graph H = H(n) where V (H) = [n] and for i1 < i2 < ··· < ik, we have e = {i1,i2,... ,ik} ∈ H iﬀ {i2,... ,ik}  ∈ Gk−1 and all other (k − 1)-subsets of e are in Gk−1. Then the arguments we gave for k = 3 show that Csk ∈ H iﬀ s ≡ 0 (mod k), and the independence number of H is O((log n)1/(k−2)). Consequently, for ﬁxed s > k with s  ≡ 0 (mod k) there is a positive constant ck such that

r(Csk,Ktk) > 2cktk−2 for all t. The best upper bound we are able to obtain (for ﬁxed s > k and all t) is from r(Ksk,Ktk). Deﬁne the tower function by t1(x) = x and ti+1(x) = 2ti(x) for i ≥ 1. Then r(Ksk,Ktk) < tk−1(tds) for all ﬁxed s > k, where ds > 0 depends only on s. Consequently, we have

2cktk−2 < r(Csk,Ktk) < r(Ksk,Ktk) < tk−1(tds). Closing the gap above seems to be a very interesting open problem. In fact, even the ﬁrst case s = k + 1, which is probably the easiest as far as lower bounds are concerned, is

not known to grow like a tower of height k − 1. For example, it is not known whether r(K54,Kt4) = r(C54,Kt4) grows as a double exponential (tower of height 3) in t. Indeed, ﬁnding the minimum s such that r(Ksk,Ktk) grows like a tower of height k − 1 is an open problem raised by Conlon-Fox-Sudakov [6]. They proved that this minimum s is at most ⌈5k/2⌉ − 3 and conjectured that this can be improved to s = k + 1. Recently, a group at a workshop on Graph Ramsey Theory at the American Institute of Mathematics observed that a lower bound for r(Kkk+1,Ktk) can be obtained from a construction that avoids tight paths of appropriate sizes in the ordered setting (they were concerned with the case t = k+2 but the same observation is valid for large t, which is what we are concerned with here). Results of Shapira-Moshkovitz [11] and Milans-Stolee-West [12] provide such a construction and consequently imply that for ﬁxed k ≥ 3 and all t suﬃciently large,

r(Ckk+1,Ktk) = r(Kkk+1,Ktk) > tk−2(bt) for some positive constant b. Indeed, the above results of [11, 12] imply that a lower bound for r(Kkk+1,Ktk) is one more than the size of the poset Jk deﬁned inductively as follows: J1 consists of two chains, one of size 1 and the other of size t − k, and for i ≥ 1, the elements of Ji+1 are the ideals (down sets) of Ji and order is deﬁned by containment. It is an easy exercise to see that J3 contains an antichain of size Ω(t) and consequently that |J4| = 2Ω(t) and then |Jℓ| = tℓ−2(Ω(t)) for all ℓ > 0. Similar results can be proved using the ideas developed much earlier in [7]. This suggests that the growth rate of r(Csk,Ktk) for all ﬁxed s > k is of tower type.

Acknowledgment. The ﬁrst author thanks David Conlon for an informative short conversation about r(K53−,Kt3). Part of the research for this paper was done at the workshop Graph Ramsey Theory sponsored by the American Institute of Mathematics in January 2015. The authors are grateful to AIM for hosting the workshop.

# References

- [1] M. Ajtai, J. Komlo´s and E. Szemere´di: A Note on Ramsey Numbers. J. Comb. Theory Ser. A, 29 (1980) 354–360.
- [2] T. Bohman and P. Keevash, The early evolution of the H-free process, Inventiones Mathematicae, 181 (2010) 291–336.
- [3] T. Bohman and P. Keevash, Dynamic concentration of the triangle-free process, submitted, http://arxiv.org/abs/1302.5963arXiv.1302.5963.
- [4] D. Conlon, J. Fox, C. Lee, and B. Sudakov, Ordered Ramsey numbers, submitted.
- [5] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23 (2010), no. 1, 247–266.
- [6] D. Conlon, J. Fox, and B. Sudakov, An improved bound for the stepping-up lemma, Discrete Applied Mathematics, 161 (2013), 1191-1196.


- [7] D. Duﬀus, H. Lefmann, V. Ro¨dl, Shift Graphs and Lower Bounds on Ramsey Numbers rk(l;r), Discrete Mathematics 137, 1995, p. 177-187.
- [8] G. Fiz Pontiveros, S. Griﬃths, R. Morris, The triangle-free process and R(3,k), submitted, http://arxiv.org/abs/1302.6279 arXiv.1302.6279.
- [9] J.H. Kim, The Ramsey number R(3,t) has order of magnitude t2/log t, Random Structures & Algorithms, 7 (1995) 173–207.
- [10] A. Kostochka, D. Mubayi, J. Verstrae¨te, On independent sets in hypergraphs, Random Structures & Algorithms, 44 224–239.
- [11] G. Moshkovitz and A. Shapira, Ramsey-Theory, Integer Partitions and a New Proof of The Erdos-Szekeres Theorem Advances in Mathematics 262 (2014), 1107-1129
- [12] K. G. Milans, D. Stolee, D. West, Ordered Ramsey theory and track representations of graphs (submitted)
- [13] J.B. Shearer: A note on the independence number of triangle-free graphs II. J. Combintorial Theory Series B, 2 300–307.
- [14] B. Sudakov, A new lower bound for a Ramsey-type problem, Combinatorica 25 (2005), 487–498.


