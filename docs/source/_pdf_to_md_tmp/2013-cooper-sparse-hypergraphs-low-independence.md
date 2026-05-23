arXiv:1312.0813v4[math.CO]23Jul2014

# Sparse hypergraphs with low independence number

Jeﬀ Cooper ∗ Dhruv Mubayi † October 30, 2018

Abstract

Let K4(3) denote the complete 3-uniform hypergraph on 4 vertices. Ajtai, Erd˝os, Komlo´s, and Szemere´di (1981) asked if there is a function ω(d) → ∞ such that every 3-uniform, K4(3)-free hypergraph H with N vertices and average degree d has independence number at least dN1/2ω(d). We answer this question by constructing a 3-uniform, K4(3)-free hypergraph with independence number at most 2dN1/2. We also provide counterexamples to several related conjectures and improve the lower bound of some hypergraph Ramsey numbers.

![image 1](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile1.png>)

![image 2](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile2.png>)

## 1 Introduction

A k-uniform hypergraph H is a pair H = (V, E), where V is the vertex set and E ⊂ Vk is the edge set. We refer to the edge set of the hypergraph by H and the vertex set by V (H). The degree of a vertex in V (H) is the number of edges containing that vertex. An independent set in a hypergraph is a subset of V (H) which contains no edge of H. The independence number of H, denoted α(H), is the maximum size of an independent set in H. Tura´n [18] showed that α(G) ≥ dN+1 for any graph G with N vertices and average degree d. Spencer [17] extended Tura´n’s result to hypergraphs by showing that for all k ≥ 1 there is a ck so that every (k + 1)-uniform hypergraph H with average degree d satisﬁes α(H) ≥ ckdN

![image 3](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile3.png>)

.

![image 4](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile4.png>)

1/k

When G is a graph, Tura´n’s bound can be improved if G is forbidden from containing a ﬁxed subgraph. Ajtai, Koml´os, and Szemer´edi [3] showed that if G is triangle-free,

![image 5](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile5.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois at Chicago, Chicago, IL 60607, USA; email: jcoope8@uic.edu

†Department of Mathematics, Statistics, and Computer Science, University of Illinois at Chicago, Chicago IL 60607, USA; research supported in part by NSF grant DMS-1300138; email: mubayi@uic.edu

then

N d

1 100

log d. (1) Ajtai, Erd˝os, Koml´os, and Szemer´edi [1] subsequently showed that if t ≥ 4 and G is Kt-free, then α(G) ≥ ctNd log log d.

α(G) ≥

![image 6](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile6.png>)

![image 7](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile7.png>)

![image 8](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile8.png>)

Let H be a (k + 1)-uniform hypergraph with N vertices and average degree d. Ajtai, Koml´os, Pintz, Spencer, and Szemer´edi [2] showed that there exists a positive constant ck such that if H contains no 2, 3, or 4 cycles, then

N d1/k

α(H) ≥ ck

![image 9](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile9.png>)

log1/k d. (2)

Applications of (2) have been found in number theory [3], discrete geometry [12], coding theory [14], and Ramsey theory [4]. Ajtai, Erd˝os, Koml´os and Szemer´edi asked if, like in the graph case, (2) could also be extended to other families of hypergraphs.

Question 1 (Ajtai-Erdo˝s-Koml´os-Szemer´edi [1]). Is there a function ω(d) → ∞ such that if a 3-uniform hypergraph H contains no K4(3) (or even K4−(3)), then α(H) ≥

N

d1/2ω(d)?

![image 10](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile10.png>)

We construct hypergraphs which negatively answer this question, even in the K4−(3) case. The construction is presented in Section 2. In Section 3, we generalize this construction to k-uniform hypergraphs and disprove several conjectures related to Question 1. We also discuss an application to hypergraph Ramsey numbers.

## 2 3-uniform construction

In this section, we answer Question 1 by constructing a K4−(3)-free, 3-uniform hypergraph H with independence number at most 2N/d1/2. The hypergraph H is constructed from

the complete bipartite graph Kn,n with vertex classes [n] and [n]. The vertices of H correspond to edges in the graph, while the edges of H correspond to 3-edge paths which open in the increasing direction:

V (H) = [n] × [n] E(H) = {{ab, ac, db ∈ [n] × [n] : c > b, d > a}.

H is clearly 3-uniform, contains N = n2 vertices, and has average degree d = 3(n−1)2/4. For v ∈ V (H), consider the link graph Lv = {uw : uvw ∈ E(H)}. The components of Lv are either stars (when v is in the role of ac) or a bipartite graph (when v is in the role of ab). K4−(3), on the other hand, contains a vertex whose link graph contains a triangle, so H must be K4−(3)-free.

Let S ⊂ V (H). If |S| ≥ 2n, then the edges in Kn,n corresponding to the vertices in S contain a cycle on at least four vertices. The smallest vertex on this cycle is contained in a 3-edge path which opens in the increasing direction, and this path corresponds to an edge in H. Therefore, α(H) < 2n < 2N/d1/2.

## 3 Related problems and conjectures

### 3.1 Ramsey numbers for 3-uniform tight paths

Our construction also provides the correct order of magnitude for some new 3-uniform Ramsey numbers. Let F be a 3-uniform hypergraph. Recall that the Ramsey number r(F, t) is the smallest n so that every red-blue coloring of the edges of Kn(3) contains a red F or a blue complete Kt(3). Let Ps denote the 3-uniform hypergraph with vertex set [s + 2] and edge set {{i, i + 1, i + 2} : i ∈ [s]}. Ps is called the 3-uniform tight path. Results of Phelps and Ro¨dl [16] imply that the Ramsey number of P2 satisﬁes

r(P2, t) = Θ(t2/ log t).

It is easy to prove that for ﬁxed s, we have ex(n, Ps) = O(n2) and this immediately implies that

r(Ps, t) = O(t2). Indeed, if we have a Ps-free 3-uniform hypergraph on csn vertices (cs large), then its average degree is at most c′sn, so it has an independent set of size at least t = c′′sn1/2.

We now show that the construction in Section 2 contains no P4, which improves the lower bound of r(Ps, t) for s ≥ 4. The order of magnitude of r(P3, t) remains open. Theorem 2. Fix s ≥ 4. Then r(Ps, t) = Θ(t2).

Proof. We only need to prove the lower bound, which follows by observing that the hypergraph H in Section 2 contains no P4. Recall that every link graph of H has one component that is a complete bipartite graph and all of its other components are stars; further, the pairs of vertices which form edges in the bipartite component appear in exactly one edge of H. On the other hand, the link graph of each of the degree 3 vertices in P4 contains a 3-edge path and one of the pairs of vertices which form an edge in this path is contained in two edges of P4.

![image 11](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile11.png>)

![image 12](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile12.png>)

![image 13](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile13.png>)

![image 14](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile14.png>)

### 3.2 Generalization to k-uniform hypergraphs

The construction in Section 2 starts with a bipartite graph and builds a hypergraph whose edges correspond to 3-edge paths in the graph. In this section, we generalize this method by starting with a multipartite hypergraph and building a new hypergraph whose edges correspond to some ﬁxed hypergraph. The resulting hypergraphs provide counterexamples to various conjectures concerning k-uniform hypergraphs.

- 3.2.1 Chromatic number of k-uniform hypergraphs

A proper coloring of a hypergraph H is a partition of V (H) into independent sets. The chromatic number of H, denoted χ(H), is the minimum number of parts needed in a proper coloring of H. Erd˝os and Lova´sz [9] showed that every (k+1)-uniform hypergraph with maximum degree ∆ has χ(H) ≤ ck∆1/k. Strengthening (2), Frieze and the second author [11] showed that every (k + 1)-uniform linear hypergraph with maximum degree ∆ satisﬁes χ(H) ≤ c′k(log ∆∆ )1/k. In [10, 11], the same authors conjectured a stronger positive answer to the question of Ajtai, Erd˝os, Koml´os, and Szemer´edi.

![image 15](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile15.png>)

Conjecture 3 (Frieze-Mubayi [10, 11]). If F is a (k + 1)-uniform hypergraph and H is an F-free (k + 1)-uniform hypergraph with maximum degree ∆, then χ(H) ≤ cF(∆/ log ∆)1/k.

Let Tk be the k-uniform hypergraph with k + 1 edges e1, . . ., ek, f where for all i = j we have ei ∩ ej = S and f ⊃ ei − S for some S with |S| = k − 1. In other words, k edges share the same set of k −1 points and the last edge contains the remaining vertex from each of the k edges. A k-uniform hypergraph has independent neighborhoods if it contains no copy of Tk. Bohman, Frieze, and the second author [5] conjectured a weaker version of Conjecture 3: if H is a 3-uniform hypergraph with maximum degree ∆ and independent neighborhoods, then χ(H) = o(∆1/2).

The construction in Section 2 shows that both of these conjectures are false for 3uniform hypergraphs. We now generalize that construction to disprove these conjectures for k-uniform hypergraphs.

- 3.2.2 Construction from positive strong k-simplices


Fix k ≥ 2. A k-simplex is a collection of k + 1 sets with empty intersection, every k of which have nonempty intersection. A strong k-simplex Sk, introduced in [15], is the k-uniform hypergraph with vertex set {v1, v1′, . . . ., vk, vk′ } and edge set {e, e1, . . ., ek}

where e = {v1, . . ., vk} and ei = e ∪ {vi′} − vi (e is called the central edge). Given disjoint sets X1, . . ., Xk with each Xi ∼= [n], a positive strong k-simplex Sk+ is a k-partite strong simplex satisfying vi, vi′ ∈ Xi and vi′ > vi for each i = 1, . . ., k.

Let X1, . . ., Xk be disjoint sets each isomorphic to [n]. Deﬁne the (k + 1)-uniform hypergraph Hk with vertex set X1 × · · · × Xk and edge set

Hk = {A ⊂ X1 × · · · × Xk : A ∼= Sk+}. For example, H2 corresponds to the construction in Section 2.

Fix a k-uniform hypergraph Fk. The Zarankiewicz number z(n, Fk) is the maximum number of edges in a k-partite k-uniform hypergraph with parts of size n that contains no copy of Fk. Since copies of Sk+ correspond to edges of Hk,

α(Hk) ≤ z(n, Sk+). We may thus use the following lemma below to bound α(Hk). Lemma 4. Fix k ≥ 2. Then z(n, Sk+) ≤ 2knk−1.

Proof. We proceed by induction on k. The base case k = 2 follows from Section 2. For the induction step, suppose we are given a k-partite H ⊂ X1 × · · · × Xk with |H| > 2knk−1, where each Xi ∼= [n]. For a vertex v in a k-uniform hypergraph H, deﬁne its link to be the (k − 1)-uniform hypergraph Lv = {S ⊂ V (H) : v  ∈ S, S ∪ {v} ∈ H}. For a set of vertices T, let dH(T) denote the number of edges containing T.

For each v ∈ X1, let Lv be the link (k − 1)-uniform hypergraph of v. Let Av ⊂ Lv comprise those (k − 1)-sets T with dH(T) = 1 and Bv = Lv − Av.

Let Bv+ be the set of all S ∈ Bv such that there exists v′ > v with S ∈ Lv′. We will ﬁnd x ∈ X1 with |Bx+| > 2(k − 1)nk−2 and then apply induction. Now

dH(S) − nk−1 =

|Bv+| =

(dH(S) − 1) ≥

S∈X2×···×Xk: dH(S)≥2

S∈X2×···×Xk: dH(S)≥2

v∈X1

|Bv| − nk−1.

v∈X1

Thus

2knk−1 < |H| =

|Lv| =

v∈X1

|Av| +

v∈X1

|Bv| ≤ nk−1 +

|Bv|

v∈X1

v∈X1

|Bv+|.

≤ 2nk−1 +

v∈X1

Consequently, there exists x ∈ X1 with |Bx+| > 2(k − 1)nk−2. Apply induction to Bx to obtain a copy of Sk+−1 in X2 × · · · × Xk. To form Sk+, begin by enlarging each edge

of Sk+−1 with x. Add another edge by enlarging the central edge e by some other vertex y ∈ X1 with y > x. Note that y exists since e ∈ Bx+ and dH(e) > 1. We have thus obtained a copy of Sk+, where e ∪ {x} is the central edge.

![image 16](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile16.png>)

![image 17](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile17.png>)

![image 18](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile18.png>)

![image 19](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile19.png>)

Notice Hk has N = nk vertices and maximum degree ∆ ≤ (k + 1)nk. By Lemma 4,

nk ((k + 1)nk)1/k ≤ 2k(k + 1)1/k

N ∆1/k

α(Hk) ≤ 2knk−1 = 2k(k + 1)1/k

,

![image 20](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile20.png>)

![image 21](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile21.png>)

and

∆1/k 2k(k + 1)1/k

.

χ(Hk) ≥

![image 22](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile22.png>)

Recall that Tk+1 is the (k + 1)-uniform hypergraph with k + 2 edges e1, . . ., ek+1, f where for all i = j, ei ∩ ej = S and f ⊃ ei − S for some S with |S| = k. Suppose Sk,+1, . . ., Sk,k+ +1 satisfy Sk,i+ ∩Sk,j+ = S, for i = j and |S| = k. Since each strong k-simplex is positive, they must share a single central edge. Thus the edges in (Sk,+1∪· · ·∪Sk,k+ +1)−S share a single vertex and so do not form a positive strong k-simplex. Therefore Hk does not contain any copy of Tk+1, disproving Conjecture 3 and the weaker conjecture of [5].

- 3.2.3 c-sparse hypergraphs


A hypergraph is c-sparse if every vertex subset S spans at most c|S|2 edges. By Spencer’s extension of Tura´n’s bound, every c-sparse hypergraph H with N vertices satisﬁes α(H) ≥ c′k√N. Phelps and Ro¨dl [16] improved this to α(H) ≥ c′k√N log N for linear 3-uniform hypergraphs. In 1986, de Caen (see [7]) conjectured that a similar improvement holds even for c-sparse hypergraphs (observe that linear implies 21-sparse). Conjecture 5 (De Caen [7]). For every positive c, there is a function ω(N) → ∞ such that every c-sparse 3-uniform hypergraph H with N vertices satisﬁes α(H) ≥ ω(N)√N.

![image 23](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile23.png>)

![image 24](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile24.png>)

![image 25](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile25.png>)

![image 26](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile26.png>)

Recently, Kostochka, the second author, and Verstra¨ete [13] posed a stronger version of de Caen’s conjecture: for every positive c, there is a function ω(N) → ∞ such that every c-sparse 3-uniform hypergraph H with N vertices and average degree d satisﬁes α(H) ≥ ω(N)dN

.

![image 27](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile27.png>)

1/2

Observe that the construction in Section 2 is 1-sparse, so S2 immediately provides a counterexample to Conjecture 5 and the conjecture of [13]. However, for k ≥ 3, Hk is not c-sparse for any constant c, so one may ask whether or not for k ≥ 3 and every positive c there is a function ω(N) → ∞ such that every c-sparse (k +1)-uniform hypergraph H with N vertices satisﬁes α(H) ≥ ω(N)N1/k. The next section provides a counterexample to this generalization of de Caen’s conjecture.

- 3.2.4 Construction from special k-clusters


A k-cluster, introduced in [15], is a collection of k + 1 sets with empty intersection whose union has size at most 2k. The family of special k-clusters Dk is the k-uniform hypergraph family that is deﬁned inductively as follows: D2 = {D2}, where D2 is the path with three edges. For k ≥ 3, Dk is the family of k-uniform hypergraphs which can be constructed as follows: begin with any Dk−1 ∈ Dk−1, which is assumed inductively to have 2(k − 1) vertices and two disjoint edges a and b. Then Dk is a member of Dk if it can be formed by adding two new vertices x, y to Dk−1, enlarging all edges of Dk−1 by including x, and enlarging a by including y. Thus Dk has 2k vertices and k + 1 edges, two of which are disjoint. We will use Dk to denote an arbitrarily chosen member of Dk.

Following the construction from Section 3.2.2, deﬁne the (k + 1)-uniform hypergraph Jk with vertex set X1 × · · · × Xk and edge set

Jk = {A ⊂ X1 × · · · × Xk : A ∼= Dk}. Lemma 6. Fix k ≥ 2 and Dk ∈ Dk. Then z(n, Dk) ≤ knk−1.

Proof. We proceed by induction on k. For the base case k = 2, observe that D2 is the path with 3 edges. If H is a bipartite graph with more than 2n edges, then H contains a cycle with at least four edges, which contains a copy of D2. For the induction step, suppose we are given k-partite H with |H| > knk−1 with parts X1, . . ., Xk each of size n. For each v ∈ X1, deﬁne Lv, Av, and Bv as in the proof of Lemma 4. Then

knk−1 < |H| =

|Lv| =

v∈X1

|Bv| ≤ nk−1 +

|Av| +

v∈X1

v∈X1

|Bv|. (3)

v∈X1

Consequently, there exists x ∈ X1 with |Bx| > (k − 1)nk−2. Let Dk−1 be the member of Dk−1 that gives rise to Dk in the inductive construction of Dk. Apply induction to Bx to obtain a copy of Dk−1 in Bx. To form Dk, begin by enlarging each edge of Dk−1 with x. Add another edge by enlarging one of the two disjoint edges a, b of Dk−1 (say a) by some other vertex y ∈ X1. Note that y exists since a ∈ Bx. We have thus obtained a copy of Dk, where a ∪ {y} and b ∪ {x} are the disjoint edges.

![image 28](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile28.png>)

![image 29](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile29.png>)

![image 30](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile30.png>)

![image 31](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile31.png>)

By Lemma 6, α(Jk) ≤ knk−1, so it suﬃces to show that Jk is 22k2−2k−1-sparse. Let S ⊂ V (Jk). The vertex set of a copy of Dk is determined by the two disjoint edges in Dk. There are at most 2kk k−1 possibilities for the remaining k − 1 edges. Therefore we may associate every pair of vertices in S to at most 2kk k−1 edges in the subgraph induced by S. Since every edge corresponds to at least one pair of vertices, the number

of edges in S is at most

k−1 |S| 2

2k k

2−2k−1|S|2. This disproves the generalization of de Caen’s conjecture to k-uniform hypergraphs.

< 22k

## 4 Concluding remarks

- • Hk is a counterexample to Conjecture 3 with N vertices and maximum degree Θ(N). Sparser counterexamples with fN vertices and maximum degree N can be constructed by taking the disjoint union of f copies of Hk.
- • Benny Sudakov suggested the following generalization of H2 to (k + 1)-uniform hypergraphs, which provides a denser counterexample to Conjecture 3 for k ≥ 3. Let G be the (k + 1)-uniform hypergraph with vertex set [n] × [n] and edge set

{(x1, y1), (x1, y2), (x2, y2), . . ., (xk, y2) : y2 < y1, xi < xi+1 for i ∈ [k − 1]}. In other words, each edge corresponds to an L with k points on its base. It is not hard to see that G has maximum degree Θ(nk), independence number Θ(n), and contains no copy of Tk+1.

- • For 1 < r < k + 1, say that a (k + 1)-uniform hypergraph is (c, r)-sparse if every vertex subset S spans at most c|S|r edges. A partial Steiner (k + 1, k)-system is a (k + 1)-uniform hypergraph with every k vertices in at most one edge. Such a system has average degree at most nk−1 and, by [13], has independence number at least c′(nlog n)1/k for some positive c′. This result cannot be extended to the larger class of (c, k)-sparse (k+1)-uniform hypergraphs, as shown by the following (c, 3)-sparse 4-uniform hypergraphs with independence number O(n1/3).


Let F be the set of 3-partite 3-uniform hypergraphs with four edges such that one of the edges is contained in the union of the other three. Then it is an easy exercise to show (by induction on n for example) that z(n, F) = O(n), so our general construction provides a 4-uniform, (c, 3)-sparse hypergraph H(F) on n3 vertices with α(H(F)) = O(n) (for (c, 3)-sparse, use the argument in Section

- 3.2.4).

We remark that, in addition, H(F) contains no K163(4) for the vertex set of a copy of K163(4) would correspond to a set of 163 = 1 + 3!(4 − 1)3 3-uniform edges, and by the Erd˝os-Rado sunﬂower lemma, these edges would contain a sunﬂower C of size

- 4. But the 4 vertices in H(F) corresponding to the edges of C cannot form an edge in H(F) since not one of them is contained in the union of the other three.


- • Deﬁne the 3-uniform hypergraphs F5 = {abc, abd, cde} and C3 = {abc, cde, efa}. The authors [6] recently answered Question 1 positively if, in addition to K4−(3), F5 and C3 are also forbidden. It would be interesting to answer Question 1 if only K4−(3) and C3 are forbidden.


## 5 Acknowledgments

We would like to thank the referees for carefully reading our manuscript and providing thoughtful feedback.

## References

- [1] M. Ajtai, P. Erd˝os, J. Koml´os, and E. Szemer´edi, On Tur´n’s theorem for sparse graphs, Combinatorica 1 (1981), no. 4, 313–317. MR 647980 (83d:05052)
- [2] M. Ajtai, J. Koml´os, J. Pintz, J. Spencer, and E. Szemer´edi, Extremal uncrowded hypergraphs, J. Combin. Theory Ser. A 32 (1982), no. 3, 321–335. MR 657047 (83i:05056)
- [3] M. Ajtai, J. Koml´os, and E. Szemer´edi, A dense inﬁnite Sidon sequence, European J. Combin. 2 (1981), no. 1, 1–11. MR 611925 (83f:10056)
- [4] N. Alon, T. Jiang, Z. Miller, and D. Pritikin, Properly colored subgraphs and rainbow subgraphs in edge-colorings with local constraints, Random Structures Algorithms 23 (2003), no. 4, 409–433. MR 2016871 (2004i:05106)
- [5] T. Bohman, A. Frieze, and D. Mubayi, Coloring H-free hypergraphs, Random Structures Algorithms 36 (2010), no. 1, 11–25. MR 2591044 (2011e:05081)
- [6] J. Cooper and D. Mubayi, List coloring triangle-free hypergraphs, (submitted)

(2013).

- [7] D. de Caen, The current status of Tur´n’s problem on hypergraphs, Extremal problems for ﬁnite sets (Visegra´d, 1991), Bolyai Soc. Math. Stud., vol. 3, Ja´nos Bolyai Math. Soc., Budapest, 1994, pp. 187–197. MR 1319162 (95m:05127)
- [8] R. A. Duke, H. Lefmann, and V. Ro¨dl, On uncrowded hypergraphs, Proceedings of the Sixth International Seminar on Random Graphs and Probabilistic Methods in Combinatorics and Computer Science, “Random Graphs ’93” (Pozna´n, 1993), vol. 6, 1995, pp. 209–212. MR 1370956 (96h:05146)


- [9] P. Erd˝os and L. Lova´sz, Problems and results on 3-chromatic hypergraphs and some related questions, Inﬁnite and ﬁnite sets (Colloq., Keszthely, 1973; dedicated to P. Erd˝os on his 60th birthday), Vol. II, North-Holland, Amsterdam, 1975, pp. 609–

627. Colloq. Math. Soc. J´nos Bolyai, Vol. 10. MR 0382050 (52 #2938)

- [10] A. Frieze and D. Mubayi, On the chromatic number of simple triangle-free triple systems, Electron. J. Combin. 15 (2008), no. 1, Research Paper 121, 27. MR 2443136 (2009j:05170)
- [11] , Coloring simple hypergraphs, Journal of Combinatorial Theory. Series B (to appear).

![image 32](<2013-cooper-sparse-hypergraphs-low-independence_images/imageFile32.png>)

- [12] J. Koml´os, J. Pintz, and E. Szemer´edi, A lower bound for Heilbronn’s problem, J. London Math. Soc. (2) 25 (1982), no. 1, 13–24. MR 645860 (83i:10042)
- [13] A. Kostochka, D. Mubayi, and J. Verstraete, On independent sets in hypergraphs, Random Structures Algorithms (to appear).
- [14] H. Lefmann, Sparse parity-check matrices over GF(q), Combin. Probab. Comput. 14 (2005), no. 1-2, 147–169. MR 2128087 (2006b:94064)
- [15] D. Mubayi, An intersection theorem for four sets, Adv. Math. 215 (2007), no. 2, 601–615. MR 2355601 (2008m:05295)
- [16] K. T. Phelps and V. Ro¨dl, Steiner triple systems with minimum independence number, Ars Combin. 21 (1986), 167–172. MR 846690 (87j:05038)
- [17] J. Spencer, Tur´n’s theorem for k-graphs, Discrete Math. 2 (1972), 183–186. MR 0297614 (45 #6668)
- [18] P. Tura´n, On an extremal problem in graph theory (in hungarian), Math. Fiz. Lapok 48 (1941), 436–452.


