# arXiv:1704.02866v1[math.CO]10Apr2017

## Stability in the Erdo˝s–Gallai Theorem on cycles and paths, II∗

Zolta´n Fu¨redi† Alexandr Kostochka‡ Ruth Luo§ Jacques Verstra¨ete¶

April 11, 2017

Abstract

The Erd˝s–Gallai Theorem states that for k ≥ 3, any n-vertex graph with no cycle of length

at least k has at most 12(k−1)(n−1) edges. A stronger version of the Erd˝s–Gallai Theorem was given by Kopylov: If G is a 2-connected n-vertex graph with no cycle of length at least k, then

- e(G) ≤ max{h(n,k,2),h(n,k, k−21 )}, where h(n,k,a) := k−2a + a(n − k + a). Furthermore, Kopylov presented the two possible extremal graphs, one with h(n,k,2) edges and one with h(n,k, k−21 ) edges.

In this paper, we complete a stability theorem which strengthens Kopylov’s result. In particular, we show that for k ≥ 3 odd and all n ≥ k, every n-vertex 2-connected graph G with no cycle of length at least k is a subgraph of one of the two extremal graphs or

- e(G) ≤ max{h(n,k,3),h(n,k, k−23)}. The upper bound for e(G) here is tight.


Mathematics Subject Classiﬁcation: 05C35, 05C38. Keywords: Tura´n problem, cycles, paths.

### 1 Introduction

One of the basic Tur´n-type problems is to determine the maximum number of edges in an n-vertex graph with no k-vertex path. Erd˝s and Gallai [3] in 1959 proved the following fundamental result on this problem.

Theorem 1.1 (Erd˝s and Gallai [3]). Fix n,k ≥ 2. If G is an n-vertex graph that does not contain a path with k vertices, then e(G) ≤ 21(k − 2)n.

When n is divisible by k − 1, the bound is best possible. Indeed, the n-vertex graph whose every component is the complete graph Kk−1 has 12(k − 2)n edges and no k-vertex paths. Also, if H is an n-vertex graph without a k-vertex path Pk, then by adding to H a new vertex v adjacent to all vertices of H we obtain an (n + 1)-vertex graph H with e(H) + n edges that contains no cycle of length k + 1 or longer. Then Theorem 1.1 follows from another theorem of Erd˝s and Gallai:

∗This paper started at SQuaRES meeting of the American Institute of Mathematics. †Alfre´d R´enyi Institute of Mathematics, Hungary. E-mail: zfuredi@gmail.com. Research was supported in part

by grant K116769 from the National Research, Development and Innovation Oﬃce NKFIH, by the Simons Foundation Collaboration Grant #317487, and by the European Research Council Advanced Investigators Grant 267195.

‡University of Illinois at Urbana–Champaign, Urbana, IL 61801 and Sobolev Institute of Mathematics, Novosibirsk 630090, Russia. E-mail: kostochk@math.uiuc.edu. Research of this author is supported in part by NSF grant DMS1266016 and by grants 15-01-05867 and 16-01-00499 of the Russian Foundation for Basic Research.

§University of Illinois at Urbana–Champaign, Urbana, IL 61801. E-mail: ruthluo2@illinois.edu. ¶Department of Mathematics, University of California at San Diego, 9500 Gilman Drive, La Jolla, California

92093-0112, USA. E-mail: jverstra@math.ucsd.edu. Research supported by NSF Grant DMS-1101489.

#### C A B

Figure 1: H14,11,3.

- Theorem 1.2 (Erd˝s and Gallai [3]). Fix n,k ≥ 3. If G is an n-vertex graph that does not contain a cycle of length at least k, then e(G) ≤ 12(k − 1)(n − 1).

The bound of this theorem is best possible for n − 1 divisible by k − 2. Indeed, any connected n-vertex graph in which every block is a Kk−1 has 21(k − 1)(n − 1) edges and no cycles of length at least k. In the 1970’s, some reﬁnements and new proofs of Theorems 1.1 and 1.2 were obtained by Faudree and Schelp [4, 5], Lewin [9], Woodall [10], and Kopylov [8] – see [7] for more details. The strongest version was proved by Kopylov [8]. His result is stated in terms of the following graphs. Let n ≥ k and 1 ≤ a < 12k. The n-vertex graph Hn,k,a is as follows. The vertex set of Hn,k,a is the union of three disjoint sets A,B, and C such that |A| = a, |B| = n − k + a and |C| = k − 2a, and the edge set of Hn,k,a consists of all edges between A and B together with all edges in A ∪ C (Fig. 1 shows H14,11,3). Let

h(n,k,a) := e(Hn,k,a) =

k − a 2

+ a(n − k + a).

For a graph G, let c(G) denote the length of a longest cycle in G. Observe that c(Hn,k,a) < k: Since |A ∪ C| = k − a, any cycle D of at length at least k has at least a vertices in B. But as

- B is independent and 2a < k, D also has to contain at least k + 1 neighbors of the vertices in B, while only a vertices in A have neighbors in A. Kopylov [8] showed that the extremal 2-connected


n-vertex graphs with no cycles of length at least k are G = Hn,k,2 and G = Hn,k,t: the ﬁrst has more edges for small n, and the second — for large n.

- Theorem 1.3 (Kopylov [8]). Let n ≥ k ≥ 5 and t = 12(k − 1) . If G is an n-vertex 2-connected graph with c(G) < k, then


e(G) ≤ max{h(n,k,2),h(n,k,t)} (1) with equality only if G = Hn,k,2 or G = Hn,k,t.

### 2 Main results

##### 2.1 A previous result

Recently, three of the present authors proved in [6] a stability version of Theorems 1.2 and 1.3 for n-vertex 2-connected graphs with n ≥ 3k/2, but the problem remained open for n < 3k/2 when k ≥ 9. The main result of [6] was the following:

- Theorem 2.1 (Fu¨redi, Kostochka, Verstra¨ete [6]). Let t ≥ 2 and n ≥ 3t and k ∈ {2t + 1,2t + 2}. Let G be a 2-connected n-vertex graph c(G) < k. Then e(G) ≤ h(n,k,t − 1) unless

- (a) k = 2t + 1, k = 7, and G ⊆ Hn,k,t or
- (b) k = 2t + 2 or k = 7, and G − A is a star forest for some A ⊆ V (G) of size at most t.


Note that

h(n,k,t) − h(n,k,t − 1) =

n − t − 3 if k = 2t + 1, n − t − 5 if k = 2t + 2.

The paper [6] also describes the 2-connected n-vertex graphs with c(G) < k ≤ 8 for all n ≥ k.

2.2 The essence of the main result

Together with [6], this paper gives a full description of the 2-connected n-vertex graphs with c(G) < k and ‘many’ edges for all k and n. Our main result is:

- Theorem 2.2. Let t ≥ 4 and k ∈ {2t + 1,2t + 2}, so that k ≥ 9. If G is a 2-connected graph on n ≥ k vertices and c(G) < k, then either e(G) ≤ max{h(n,k,t − 1),h(n,k,3)} or


- (a) k = 2t + 1 and G ⊆ Hn,k,t or
- (b) k = 2t + 2 and G − A is a star forest for some A ⊆ V (G) of size at most t.
- (c) G ⊆ Hn,k,2.


Figure 2: Hn,k,t(k = 2t + 1),Hn,k,t(k = 2t + 2),Hn,k,2;

ovals denote complete subgraphs of order t, t, and k − 2 respectively. Note that the case n < k is trivial and the case k ≤ 8 was fully resolved in [6].

##### 2.3 A more detailed form of the main result

In order to prove Theorem 2.2, we need a more detailed description of graphs satisfying (b) in the theorem that do not contain ‘long’ cycles.

![image 1](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile1.png>)

![image 2](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile2.png>)

![image 3](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile3.png>)

![image 4](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile4.png>)

- C


![image 5](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile5.png>)

![image 6](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile6.png>)

![image 7](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile7.png>)

![image 8](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile8.png>)

![image 9](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile9.png>)

![image 10](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile10.png>)

![image 11](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile11.png>)

![image 12](<2017-fredi-stability-erd-s-gallai-theorem_images/imageFile12.png>)

Figure 3: Classes G2(n,k), G3(n,k) and G4(n,10).

Let G1(n,k) = {Hn,k,t,Hn,k,2}. Each G ∈ G2(n,k) is deﬁned by a partition V (G) = A ∪ B ∪ C and two vertices a1 ∈ A, b1 ∈ B such that |A| = t, G[A] = Kt, G[B] is the empty graph, G(A,B) is a complete bipartite graph, and N(c) = {a1,b1} for every c ∈ C. Every member of G ∈ G3(n,k) is deﬁned by a partition V (G) = A ∪ B ∪ J such that |A| = t, G[A] = Kt, G(A,B) is a complete bipartite graph, and

— G[J] has more than one component,

— all components of G[J] are stars with at least two vertices each,

— there is a 2-element subset A of A such that N(J) ∩ (A ∪ B) = A ,

— for every component S of G[J] with at least 3 vertices, all leaves of S have degree 2 in G and are adjacent to the same vertex a(S) in A .

The class G4(n,k) is empty unless k = 10. Each graph H ∈ G4(n,10) has a 3-vertex set A such that H[A] = K3 and H − A is a star forest such that if a component S of H − A has more than two vertices then all its leaves have degree 2 in H and are adjacent to the same vertex a(S) in A. These classes are illustrated below:

We can reﬁne Theorem 2.2 in terms of the classes Gi(n,k) as follows:

- Theorem 2.3. (Main Theorem) Let k ≥ 9, n ≥ k and t = 2 1(k − 1) . Let G be an n-vertex 2-connected graph with no cycle of length at least k. Then e(G) ≤ max{h(n,k,t − 1),h(n,k,3)} or G is a subgraph of a graph in G(n,k), where


- (1) if k is odd, then G(n,k) = G1(n,k) = {Hn,k,t,Hn,k,2};
- (2) if k is even and k = 10, then G(n,k) = G1(n,k) ∪ G2(n,k) ∪ G3(n,k);
- (3) if k = 10, then G(n,k) = G1(n,10) ∪ G2(n,10) ∪ G3(n,10) ∪ G4(n,10).


Since every graph in G2(n,k) ∪ G3(n,k) and many graphs in G4(n,k) have a separating set of size

- 2 (see Fig. 3), the theorem implies the following simpler statement for 3-connected graphs:


Corollary 2.4. Let k ∈ {2t+1,2t+2} where k ≥ 9. If G is a 3-connected graph on n ≥ k vertices and c(G) < k, then either e(G) ≤ max{h(n,k,t−1),h(n,k,3)} or G ⊆ Hn,k,t or k = 10 and G is a subgraph of some graph H ∈ G4(n,10) such that each component of H − A has at most 2 vertices.

### 3 The proof idea

##### 3.1 Small dense subgraphs

First we deﬁne some more graph classes. For a graph F and a nonnegative integer s, we denote by K−s(F) the family of graphs obtained from F by deleting at most s edges.

- Let F0 = F0(t) denote the complete bipartite graph Kt,t+1 with partite sets A and B where |A| = t

- and |B| = t+1. Let F0 = K−t+3(F0), i.e., the family of subgraphs of Kt,t+1 with at least t(t+1)−t+3 edges.

Let F1 = F1(t) denote the complete bipartite graph Kt,t+2 with partite sets A and B where |A| = t

- and |B| = t+2. Let F1 = K−t+4(F1), i.e., the family of subgraphs of Kt,t+2 with at least t(t+2)−t+4 edges.

- Let F2 denote the family of graphs obtained from a graph in K−t+4(F1) by subdividing an edge a1b1 with a new vertex c1, where a1 ∈ A and b1 ∈ B. Note that any member H ∈ F2 has at least |A||B| − (t − 3) edges between A and B and the pair a1b1 is not an edge.
- Let F3 = F3(t,t ) denote the complete bipartite graph Kt,t with partite sets A and B where |A| = t and |B| = t . Take a graph from K−t+4(F3), select two non-empty subsets A1, A2 ⊆ A with |A1 ∪ A2| ≥ 3 such that A1 ∩ A2 = ∅ if min{|A1|,|A2|} = 1, add two vertices c1 and c2, join them to each other and add the edges from ci to the elements of Ai, (i = 1,2). The class of obtained graphs is denoted by F(A,B,A1,A2). The family F3 consists of these graphs when |A| = |B| = t, |A1| = |A2| = 2 and A1 ∩ A2 = ∅. In particular, F3(4) consists of exactly one graph, call it F3(4).


Graph F4 has vertex set A∪B, where A = {a1,a2,a3} and B := {b1,b2,...,b6} are disjoint. Its edges are the edges of the complete bipartite graph K(A,B) and three extra edges b1b2, b3b4, and b5b6 (see Fig. 4 below). Deﬁne F 4 as the (only) member of F(A,B,A1,A2) such that |A| = |B| = t = 4, A1 = A2, and |Ai| = 3. Let F4 := {F4,F 4}, which is deﬁned only for t = 4.

Figure 4: Graphs F3(4),F4, and F 4.

Deﬁne F(k) := F0, if k is odd, F1 ∪ ··· ∪ F4, if k is even.

- 3.2 Proof idea




For our proof, it will be easier to use the stronger induction assumption that the graphs in question contain certain dense graphs from F(k). We will prove the following slightly stronger version of Theorem 2.3 which also implies Theorem 2.2.

Theorem 2.3 Let t ≥ 4, k ∈ {2t + 1,2t + 2}, and n ≥ k. Let G be an n-vertex 2-connected graph with no cycle of length at least k. Then e(G) ≤ max{h(n,k,t − 1),h(n,k,3)} or

- (a) G ⊆ Hn,k,2, or
- (b) G is contained in a graph in G(n,k) − {Hn,k,2}, and G contains a subgraph H ∈ F(k).


The method of the proof is a variation of that of [6]. Also, when n is close to k, we use Kopylov’s disintegration method. We take an n-vertex graph G satisfying the hypothesis of Theorem 2.3 , and iteratively contract edges in a certain way so that each intermediate graph still satisﬁes the hypothesis. We consider the ﬁnal graph of this process Gm on m vertices and show that Gm satisﬁes Theorem 2.3 . Two results from [6] will be instrumental. The ﬁrst is:

- Lemma 3.1 (Main lemma on contraction [6]). Let k ≥ 9 and suppose F and F are 2-connected graphs such that F = F /xy and c(F ) < k. If F contains a subgraph H ∈ F(k), then F also contains a subgraph H ∈ F(k).

This lemma shows that if Gm contains a subgraph H ∈ F(k), then the original graph G also contains a subgraph in F(k). The second result (proved in Subsection 4.5 of [6]) is:

- Lemma 3.2 ([6]). Let k ≥ 9, and let G be a 2-connected graph with c(G) < k and e(G) > h(n,k,t− 1). If G contains a subgraph H ∈ F(k), then G is a subgraph of a graph in G(n,k) − {Hn,k,2}.


We will split the proof into the cases of small n and large n. The following observations can be obtained by simple calculations (for t ≥ 4):

|k|h(n,k,3) ≥ h(n,k,t − 1)|h(n,k,2) ≥ h(n,k,t − 1)|
|---|---|---|
|2t + 1<br><br>2t + 2<br><br><br>|If and only if n ≤ k + (t − 5)/2 If and only if n ≤ k + (t − 3)/2<br><br>|If and only if n ≤ k + t/2 − 1 If and only if n ≤ k + t/2|


In the case of large n we will contract an edge such that the new graph still has more than h(n−1,k,t−1) edges. In order to apply induction, we also need the number of edges to be greater than h(n − 1,k,3). To guarantee this, we pick the cutoﬀs for the two cases n ≤ k + (t − 1)/2 and n > k + (t − 1)/2 (therefore n − 1 > k + (t − 3)/2).

### 4 Tools

##### 4.1 Classical theorems

- Theorem 4.1 (Erd˝s [2]). Let d ≥ 1 and n > 2d be integers, and


n+1 2

n − d 2

n − 1 2

+ d2,

n,d = max

+

2

2

.

Then every n-vertex graph G with δ(G) ≥ d and e(G) > n,d is hamiltonian.

- Theorem 4.2 (Chv´tal [1]). Let n ≥ 3 and G be an n-vertex graph with vertex degrees d1 ≤ d2 ≤

... ≤ dn. If G is not hamiltonian, then there is some i < n/2 such that di ≤ i and dn−i < n−i.

- Theorem 4.3 (Kopylov [8]). If G is 2-connected and P is an x,y-path of vertices, then c(G) ≥ min{ ,d(x,P) + d(y,P)}.


- 4.2 Claims on contractions A helpful tool will be the following lemma from [6] on contraction.


- Lemma 4.4 ([6]). Let n ≥ 4 and let G be an n-vertex 2-connected graph. For every v ∈ V (G), there exists w ∈ N(v) such that G/vw is 2-connected.

For an edge xy in a graph H, let TH(xy) denote the number of triangles containing xy. Let T(H) = min{TH(xy) : xy ∈ E(H)}. When we contract an edge uv in a graph H, the degree of every x ∈ V (H) − u − v either does not change or decreases by 1. Also the degree of u ∗ v in H/uv is at least max{dH(u),dH(v)} − 1. Thus

dH/uv(w) ≥ dH(w) − 1 for any w ∈ V (H) and uv ∈ E(H). Also dH/uv(u ∗ v) ≥ dH(u) − 1. (2) Similarly,

T(H/uv) ≥ T(H) − 1 for every graph H and uv ∈ E(H). (3)

We will use the following analog of Lemma 3.3 in [6].

- Lemma 4.5. Let h be a positive integer. Suppose a 2-connected graph G is obtained from a 2connected graph G by contracting edge xy into x ∗ y chosen using the following rules:


- (i) one of x,y, say x is a vertex of the minimum degree in G ;
- (ii) TG (xy) is the minimum among the edges xu incident with x such that G /xu is 2-connected. (Such edges exist by Lemma 4.4). If G has at least h vertices of degree at most h, then either G = Kh+2 or


- (a) G also has a vertex of degree at most h, and
- (b) G has at least h + 1 vertices of degree at most h + 1.


Proof. Since G is 2-connected, h ≥ 2. Let V≤s(H) denote the set of vertices of degree at most s in H. Then by (2), each v ∈ V≤h(G) − x ∗ y is also in V≤h+1(G ). Moreover, then by (i),

x ∈ V≤h+1(G ). (4)

Thus if x ∗ y ∈/ V≤h(G), then (b) follows. But if x ∗ y ∈ V≤h(G), then by (2), also y ∈ V≤h+1(G ). So, again (b) holds.

If V≤h−1(G) = ∅, then (a) holds by (2). So, if (a) does not hold, then each v ∈ V≤h(G) − x ∗ y has degree h + 1 in G and is adjacent to both x and y in G . (5)

- Case 1: |V≤h(G)−x∗y| ≥ h. Then by (4), dG (x) = h+1. This in turn yields NG (x) = V≤h(G)+y. Since G is 2-connected, each v ∈ V≤h(G) − x ∗ y is not a cut vertex. Furthermore, {x,v} is not a cut set. If it was, because y is a common neighbor of all neighbors of x, all neighbors of x must be in the same component as y in G − x − v. It follows that


for every v ∈ V≤h(G) − x ∗ y, G /vx is 2-connected. (6)

If uv ∈/ E(G) for some u,v ∈ V≤h(G), then by (6) and (i), we would contract the edge xu rather

than xy. Thus G [V≤h(G) ∪ {x,y}] = Kh+2 and so either G = Kh+2 or y is a cut vertex in G , as claimed.

- Case 2: |V≤h(G) − x ∗ y| = h − 1. Then x ∗ y ∈ V≤h(G). This means dG (x) = dG (y) = h + 1 and NG [x] = NG [y]. So by (5), there is z ∈ V (G) such that NG [x] = NG [y] = V≤h(G) ∪ {x,y,z}. Again (6) holds (for the same reason that NG [x] ⊆ NG [y]). Thus similarly vu ∈ E(G ) for every v ∈ V≤h(G) − x ∗ y and every u ∈ V≤h(G) + z. Hence G [V≤h(G) ∪ {x,y,z}] = Kh+2 and either G = Kh+2 or z is a cut vertex in G , as claimed.


- 4.3 A property of graphs in F(k) A useful feature of graphs in F(k) is the following.

Lemma 4.6. Let k ≥ 9 and n ≥ k. Let F be an n-vertex graph contained in Hn,k,t with e(F) > h(n,k,t − 1). Then F contains a graph in F(k).

Proof. Assume the sets A,B,C to be as in the deﬁnition of Hn,k,t. We will use induction on n.

- Case 1: k = 2t + 1. If n = k, then F ∈ K−t+3(Hk,k,t) because h(k,k,t) − h(k,k,t − 1) − 1 = t − 3. Thus, since Hk,k,t ⊇ F0(t), F contains a subgraph in F0. Suppose now the lemma holds for all k ≤ n < n. If δ(F) ≥ t, then each v ∈ V (F) − A is adjacent to every u ∈ A. Hence F contains Kt,n−t. If δ(F) < t, then since A is dominating and n > 2t, there is v ∈ V (F)−A with dF(v) ≤ t−1. Then F − v ⊆ Hn−1,k,t, and we are done by induction.
- Case 2: k = 2t + 2. Let C = {c1,c2}. If n = k then as in Case 1, e(Hk,k,t) − e(F) ≤ h(k,k,t) − h(k,k,t − 1) − 1 = t − 4,


i.e., F ∈ K−t+4(Hk,k,t). Since F1(t) ⊆ Hk,k,t, F contains a subgraph in F1. Suppose now the lemma holds for all k ≤ n < n. If δ(F) < t, then there is v ∈ V (F) − A with dF(v) ≤ t − 1. Then

- F − v ⊆ Hn−1,k,t, and we are done by induction.


Finally, suppose δ(F) ≥ t. So, each v ∈ B is adjacent to every u ∈ A and each of c1,c2 has at least t − 1 neighbors in A. Since |B ∪ {c1}| ≥ n − t − 1 ≥ t + 2, F contains a member of K−1(F1(t)). Thus F contains a member of F1 unless t = 4, n = 2t + 3 and c1 has a nonneighbor x ∈ A. But then c1c2 ∈ E(F), and so F contains either F3(4) or F 4.

5 Proof of Theorem 2.3

- 5.1 Contraction procedure


If n > k, we iteratively construct a sequence of graphs Gn,Gn−1,...Gm where |V (Gj)| = j. In [6], the following Basic Procedure (BP) was used:

At the beginning of each round, for some j : k ≤ j ≤ n, we have a j-vertex 2-connected graph Gj with e(Gj) > h(j,k,t − 1).

- (BP1) If j = k, then we stop.
- (BP2) If there is an edge uv with TGj(uv) ≤ t − 2 such that Gj/uv is 2-connected, choose one such edge so that

- (i) TGj(uv) is minimum, and subject to this
- (ii) uv is incident to a vertex of minimum possible degree. Then obtain Gj−1 by contracting uv.


- (BP3) If (BP2) does not hold, j ≥ k + t − 1 and there is xy ∈ E(Gj) such that Gj − x − y has at least 3 components and one of the components, say H1 is a Kt−1, then let Gj−t+1 = Gj − V (H1).
- (BP4) If neither (BP2) nor (BP3) occurs, then we stop.


Remark 5.1. By deﬁnition, (BP3) applies only when j ≥ k+t−1. As observed in [6], if j ≤ 3t−2, then a j-vertex graph Gj with a 2-vertex set {x,y} separating the graph into at least 3 components cannot have TGj(uv) ≥ t − 1 for every edge uv. It also was calculated there that if 3t − 1 ≤ j ≤ 3t, then any j-vertex graph G with such 2-vertex set {x,y} and TG (uv) ≥ t − 1 for every edge uv has at most h(j,k,t − 1) edges and so cannot be Gj.

In this paper, we also use a quite similar Modiﬁed Basic Procedure (MBP): start with a 2connected, n-vertex graph G = Gn with e(G) > h(n,k,t − 1) and c(G) < k. Then

- (MBP0) if δ(Gj) ≥ t, then apply the rules (BP1)–(BP4) of (BP) given above;
- (MBP1) if δ(Gj) ≤ t − 1 and j = k, then stop;
- (MBP2) otherwise, pick a vertex v of smallest degree, contract an edge vu with the


minimum TGj(vu) among the edges vu such that Gj/vu is 2-connected, and set Gj−1 = Gj/uv.

##### 5.2 Proof of Theorem 2.3 for the case n ≤ k + (t − 1)/2

Apply to G the Modiﬁed Basic Procedure (MBP) starting from Gn = G. By Remark 1, (BP3) was never applied, since k + (t − 1)/2 < k + t − 1. Therefore at every step, we only contracted an edge. Denote by Gm the terminating graph of (MBP). Then Gj is 2-connected and c(Gj) ≤ c(G) < k for each m ≤ j ≤ n. By construction, after each contraction, we lose at most t − 1 edges. It follows that e(Gm) > h(m,k,t − 1).

If m > k, then the same argument as in [6] gives us the following structural result:

- Lemma 5.1 ([6]). Let m > k ≥ 9 and n ≥ k.


- • If k = 10, then Gm ⊆ Hm,k,t.
- • If k = 10, then Gm ⊆ Hm,k,t or Gm ⊇ F4.


If k = 10 and Gm ⊇ F4, then Gm contains a subgraph in F(k). Otherwise, by Lemma 4.6, again Gm has a subgraph in F(k). Next, undo the contractions that were used in (MBP). At every step for m ≤ j ≤ n, by Lemma 3.1, Gj contains some subgraph H ∈ F(k). In particular, G = Gn contains such a subgraph. Thus by Lemma 3.2, we get our result. So, below we assume

m = k. (7)

Since c(Gk) < k, Gk does not have a hamiltonian cycle. Denote the vertex degrees of Gk d1 ≤ d2 ≤ ... ≤ dk. By Theorem 4.2, there exists some 2 ≤ i ≤ t such that di ≤ i and dk−i < k − i. Let r = r(Gk) be the smallest such i.

Because Gk has r vertices of degree at most r, similarly to [2],

e(Gk) ≤ r2 +

k − r 2

.

For k = 2t + 1, r2 + k−2r > h(n,k,t − 1) only when r = t or r < (t + 4)/3, and for k = 2t + 2, when r = t or r < (t + 6)/3. If r = t, then repeating the argument in [6] yields:

- Lemma 5.2 ([6]). If r(Gk) = t then Gk ⊆ Hk,k,t.


Then by Lemma 4.6, Lemma 3.1, and Lemma 3.2, G ⊆ Hn,k,t and contains some subgraph in F(k). So we may assume that

if k = 2t + 1 then r < (t + 4)/3, and if k = 2t + 2 then r < (t + 6)/3. (8)

Our next goal is to show that G contains a large “core”, i.e., a subgraph with large minimum degree. For this, we recall the notion of disintegration used by Kopylov [8].

Deﬁnition: For a natural number α and a graph G, the α-disintegration of a graph G is the process of iteratively removing from G the vertices with degree at most α until the resulting graph has minimum degree at least α+1. This resulting subgraph H = H(G,α) will be called the α-core of G. It is well known that H(G,α) is unique and does not depend on the order of vertex deletion.

- Claim 5.3. The t-core H(G,t) of G is not empty.


Proof of Claim 5.3: We may assume that for all m ≤ j < n, graph Gj was obtained from Gj+1 by contracting edge xjyj, where dGj+1(xj) ≤ dGj+1(yj). By Rule (MBP2), dGj+1(xj) = δ(Gj+1), provided that δ(Gj+1) ≤ t − 1.

By deﬁnition, |V≤r(Gk)| ≥ r. So by Lemma 4.5 (applied several times), for each k+1 ≤ j ≤ k+t−r, because each Gj is not a complete graph (otherwise it would have a hamiltonian cycle),

δ(Gj) ≤ j − k + r − 1 and |V≤j−k+r(Gj)| ≥ j − k + r. (9) To show that

δ(Gj) ≤ t − 1 for all k ≤ j ≤ n, (10) by (9) and (8), it is enough to observe that

t − 1 2

δ(Gj) ≤ j − k + r − 1 ≤ (n − k) + r − 1 ≤

t + 6 3 − 1 =

- 5t + 3

- 6


+

< t.

We will apply a version of t-disintegration in which we ﬁrst manually remove a sequence of vertices and count the number of edges they cover. By (10) and (MBP2), dGn(xn−1) = δ(Gn) ≤ n−k+r−1. Let vn := xn−1. Then G − vn is a subgraph of Gn−1. If xn−2 = xn−1 ∗ yn−1 in Gn−1, then let vn−1 := xn−2, otherwise let vn−1 := yn−1. In both cases, dG−vn(vn−1) ≤ n−k +r −2. We continue

in this way until j = k: each time we delete from G − vn − ... − vj+1 the unique survived vertex vj that was in the preimage of xj−1 when we obtained Gj−1 from Gj. Graph G − vn − ... − vk+1 has r ≥ 2 vertices of degree at most r. We additionally delete 2 such vertices vk and vk−1. Altogether, we have lost at most (r + n − k − 1) + (r + n − k − 2) + ... + r + 2r edges in the deletions.

Finally, apply t-disintegration to the remaining graph on k−2 ∈ {2t−1,2t} vertices. Suppose that the resulting graph is empty.

- Case 1: n = k. Then

e(G) ≤ r + r + t(2t − 1 − t) +

t 2

,

where r+r edges are from vk and vk−1, and after deleting vk and vk−1, every vertex deleted removes at most t edges, until we reach the ﬁnal t vertices which altogether span at most 2 t edges. For k = 2t + 1,

h(k,k,t − 1) − e(G) ≥

2t + 1 − (t − 1) 2

+ (t − 1)2 − r + r + t(2t − 1 − t) +

t 2

= t + 2 − 2r,

which is nonnegative for r < (t + 3)/3. Therefore e(G) ≤ h(k,k,t − 1), a contradiction. Similarly, if k = 2t + 2,

e(G) ≤ r + r + t(2t − t) +

t 2

,and

h(k,k,t − 1) − e(G) ≥

2t + 2 − (t − 1) 2

+ (t − 1)2 − [r + r + t(2t − t) +

t 2

] = t + 4 − 2r, which is nonnegative when r < (t + 6)/3.

- Case 2: k < n ≤ k + (t − 1)/2. Then for k = 2t + 1,


e(G) ≤ (r + n − k − 1) + (r + n − k − 2) + ... + r + 2r + t(2t − 1 − t) +

≤ (t − 1) + (t − 1) + ... + (t − 1) + h(k,k,t − 1)

= (t − 1)(n − k) + h(k,k,t − 1)

= h(n,k,t − 1), where the last inequality holds because r + n − k − 1 ≤ t − 1. Similarly, for k = 2t + 2,

t 2

e(G) ≤ (r + n − k − 1) + (r + n − k − 2) + ... + r + 2r + t(2t − t) +

t 2

≤ (n − k)(t − 1) + h(k,k,t − 1)

= h(n,k,t − 1). This contradiction completes the proof of Claim 5.3. For the rest of the proof of Theorem 2.3 , we will follow the method of Kopylov in [8] to show that

- G ⊆ Hn,k,2. Let G∗ be the k-closure of G. That is, add edges to G until adding any additional


edges creates a cycle of length at least k. In particular, for any non-edge xy of G∗, there is an (x,y)-path in G∗ with at least k − 1 edges.

Because G has a nonempty t-core, and G∗ contains G as a subgraph, G∗ also has a nonempty t-core (which contains the t-core of G). Let H = H(G∗,t) denote the t-core of G∗. We will show that

H is a complete graph. (11) Indeed, suppose there exists a nonedge in H. Choose a longest path P of G∗ whose terminal vertices

- x ∈ V (H) and y ∈ V (H) are nonadjacent. By the maximality of P, every neighbor of x in H is

in P, similar for y. Hence dP(x) + dP(y) = dH(x) + dH(y) ≥ 2(t + 1) ≥ k, and also |P| = k − 1 (edges). By Kopylov’ Theorem 4.3, G∗ must have a cycle of length at least k, a contradiction.

Therefore H is a complete subgraph of G∗. Let = |V (H)|. Because every vertex in H has degree at least t + 1, ≥ t + 2. Furthermore, if ≥ k − 1, then G∗ has a clique K of size at least k − 1. Because G∗ is 2-connected, we can extend a (k − 1)-cycle of K to include at least one vertex in G∗ − H , giving us a cycle of length at least k. It follows that

t + 2 ≤ ≤ k − 2, (12)

and therefore k− ≤ t. Apply a weaker (k− )-disintegration to G∗, and denote by H the resulting graph. By construction, H ⊆ H .

- Case 1: There exists v ∈ V (H ) − V (H). Since v ∈/ V (H), there exists a nonedge between a vertex in H and a vertex in H − H. Pick a longest path P with terminal vertices x ∈ V (H ) and

y ∈ V (H). Then dP(x) + dP(y) ≥ (k − + 1) + ( − 1) = k, and therefore c(G∗) ≥ k.

- Case 2: H = H . Then




e(G∗) ≤ 2

+ (n − )(k − ) = h(n,k,k − ).

If 3 ≤ (k − ) ≤ t − 1, then e(G) ≤ max{h(n,k,3),h(n,k,t − 1)}, so by (12), k − = 2, and H is the complete graph with k − 2 vertices. Let D = V (G∗) − V (H). If there is an edge xy in G∗[D], then because G∗ is 2-connected, there exist two vertex-disjoint paths, P1 and P2, from {x,y} to H such that P1 and P2 only intersect {x,y} ∪ H at the beginning and end of the paths. Let a and b be the terminal vertices of P1 and P2 respectively that lie in H. Let P be any (a,b)-hamiltonian path of H. Then P1 ∪ P ∪ P2 + xy is a cycle of length at least k in G∗, a contradiction.

Therefore D is an independent set, and since G∗ is 2-connected, each vertex of D has degree 2. Suppose there exists u,v ∈ D where N(u) = N(v). Let N(u) = {a,b},N(v) = {c,d} where it is possible that b = c. Then we can ﬁnd a cycle C of H that covers V (H) which contains edges ab and cd. Then C − ab − cd + ua + ub + vc + vd is a cycle of length k in G∗. Thus for every v ∈ D, N(v) = {a,b} for some a,b ∈ H. I.e., G∗ = Hn,k,2, and thus G ⊆ Hn,k,2.

##### 5.3 Proof of Theorem 2.3 for all n

We use induction on n with the base case n ≤ k + (t − 1)/2. Suppose n ≥ k + t/2 and for all k ≤ n < n, Theorem 2.3 holds. Let G be a 2-connected graph G with n vertices such that

e(G) > max{h(n,k,t − 1),h(n,k,3)} and c(G) < k. (13)

Apply one step of (BP). If (BP4) was applied (so neither (BP2) nor (BP3) applies to G), then Gm = G (with Gm deﬁned as in the previous case). By Lemmas 5.1, 4.6, and 3.2, the theorem holds.

Therefore we may assume that either (BP2) or (BP3) was applied. Let G− be the resulting graph. Then c(G−) < k, and G− is 2-connected.

- Claim 5.4. e(G−) > max{h(|V (G−)|,k,t − 1),h(|V (G−)|,k,3)}. (14)


Proof. If (BP2) was applied, i.e., G− = G/uv for some edge uv, then e(G−) ≥ e(G) − (t − 1) > h(n − 1,k,t − 1) ≥ h(n − 1,k,3),

so (14) holds. Therefore we may assume that (BP3) was applied to obtain G−. Then n ≥ k + t − 1 and e(G) − e(G−) = t+12 − 1. So by (13),

e(G−) > h(n,k,t − 1) −

t + 1 2

+ 1. (15)

The right hand side of (15) equals h(n − (t − 1),k,t − 1) + t2/2 − 5t/2 + 2 which is at least h(n − (t − 1),k,t − 1) for t ≥ 4, proving the ﬁrst part of (14).

We now show that also e(G−) > h(n − (t − 1),k,3). Indeed, for k = 2t + 1,

e(G−) − h(n − (t − 1),k,3) >

t + 2 2

+ (t − 1)(n − t − 2) −

t + 1 2

+ 1

2t − 2 2

+ 3(n − (t − 1) − (2t − 2)) ≥ 0 when n ≥ 3t. Similarly, for k = 2t + 2,

−

e(G−) − h(n − (t − 1),k,3) >

t + 3 2

+ (t − 1)(n − t − 3) −

t + 1 2

+ 1

−

2t − 1 2

+ 3(n − (t − 1) − (2t − 1)) > 0 when n ≥ 3t + 1.

Thus if n ≥ 3t + 1, then (14) is proved. But if n ∈ {3t − 1,3t} then by Remark 5.1, no graph to which (BP3) applied may have more than h(n,k,t − 1) edges.

By (14), we may apply induction to G−. So G− satisﬁes either (a) G− ⊆ H|V (G−)|,n,2, or (b) G− is contained in a graph in G(n,k) − H|V (G−)|,k,2 and contains a subgraph H ∈ F(k). Suppose ﬁrst

that G− satisﬁes (b). If (BP3) was applied to obtain G− from G, then because G− contains a subgraph H ∈ F(k) and G− ⊆ G, G also contains H. If (BP2) was applied, then by Lemma 3.1, G contains a subgraph H ∈ F(k). In either case, Lemma 3.2 implies that G is a subgraph of a graph in G(n,k) − Hn,k,2.

So we may assume that (a) holds, that is, G− is a subgraph of H|V (G−)|,n,2. Because δ(G−) ≤ 2, δ(G) ≤ 3, and so G has edges in at most 2 ≤ t−2 triangles. Therefore (BP2) was applied to obtain G−, where G/uv = G−. Let D be an independent set of vertices of G− of size (n − 1) − (k − 2) with N(D) = {a,b} for some a,b ∈ V (G−). Since TG−(xa),TG−(xb) ≤ 1 for every x ∈ D, we have that TG(uv) ≤ 2 with equality only if T(G) = 2 where T(G) = minxy∈E(G) TG(xy).

We want to show that TG(uv) ≤ 1. If not, suppose ﬁrst that u ∗ v ∈ D ⊆ V (G−). Then there exists x ∈ D − u ∗ v, and x and u ∗ v are not adjacent in G−. Therefore x was not in a triangle

with u and v in G, and hence TG(xa) = TG−(xa) ≤ 1, so the edge xa should have been contracted instead. Otherwise if u ∗ v ∈/ D, at least one of {a,b}, say a, is not u ∗ v. If T(G) = 2, then for

every x ∈ D ⊆ V (G), TG(xa) = 2, therefore each such edge xa was in a triangle with uv in G. Then TG(uv) ≥ |D| = (n − 1) − (k − 2) ≥ k + t/2 − 1 − k + 2 ≥ 3, a contradiction.

Thus TG(uv) ≤ 1 and e(G) ≤ 2 + e(G−) ≤ 2 + h(n − 1,k,2) = h(n,k,2). But for n ≥ k + t/2, we have h(n,k,t − 1) ≥ h(n,k,2), a contradiction.

Acknowledgment. The authors thank Zolt´n Kir´ly for helpful comments.

### References

- [1] V. Chv´tal, On Hamilton’s ideals. J. Combinatorial Theory Ser. B 12 (1972), 163–168.
- [2] P. Erd˝s, Remarks on a paper of P´sa, Magyar Tud. Akad. Mat. Kutat´ Int. K¨zl. 7 (1962), 227–229.
- [3] P. Erd˝s and T. Gallai, On maximal paths and circuits of graphs, Acta Math. Acad. Sci. Hungar. 10 (1959), 337–356.
- [4] R. J. Faudree and R. H. Schelp, Ramsey type results, Inﬁnite and Finite Sets, Colloq. Math. J. Bolyai 10, (ed. A. Hajnal et al.), North-Holland, Amsterdam, 1975, pp. 657–665.
- [5] R. J. Faudree and R. H. Schelp, Path Ramsey numbers in multicolorings, J. Combin. Theory Ser. B 19 (1975), 150–160.
- [6] Z. Fu¨redi, A. Kostochka, and J. Verstra¨ete. Stability in the Erd˝s–Gallai Theorem on cycles and paths, JCTB 121 (2016), 197–228.
- [7] Z. Fu¨redi and M. Simonovits, The history of degenerate (bipartite) extremal graph problems, Bolyai Math. Studies 25 pp. 169–264, Erd˝s Centennial (L. Lov´sz, I. Ruzsa, and V. T. S´s, Eds.) Springer, 2013. Also see: arXiv:1306.5167.
- [8] G. N. Kopylov, Maximal paths and cycles in a graph, Dokl. Akad. Nauk SSSR 234 (1977), 19–21. (English translation: Soviet Math. Dokl. 18 (1977), no. 3, 593–596.)


- [9] M. Lewin, On maximal circuits in directed graphs. J. Combinatorial Theory Ser. B 18 (1975), 175–179.
- [10] D. R. Woodall, Maximal circuits of graphs I, Acta Math. Acad. Sci. Hungar. 28 (1976), 77–80.


