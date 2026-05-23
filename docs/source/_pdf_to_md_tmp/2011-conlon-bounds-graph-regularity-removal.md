arXiv:1107.4829v1[math.CO]25Jul2011

Bounds for graph regularity and removal lemmas

David Conlon∗ Jacob Fox†

Abstract

We show, for any positive integer k, that there exists a graph in which any equitable partition of its vertices into k parts has at least ck2/ log∗ k pairs of parts which are not ǫ-regular, where c,ǫ > 0 are absolute constants. This bound is tight up to the constant c and addresses a question of Gowers on the number of irregular pairs in Szemer´edi’s regularity lemma.

In order to gain some control over irregular pairs, another regularity lemma, known as the strong regularity lemma, was developed by Alon, Fischer, Krivelevich, and Szegedy. For this lemma, we prove a lower bound of wowzer-type, which is one level higher in the Ackermann hierarchy than the tower function, on the number of parts in the strong regularity lemma, essentially matching the upper bound. On the other hand, for the induced graph removal lemma, the standard application of the strong regularity lemma, we ﬁnd a diﬀerent proof which yields a tower-type bound.

We also discuss bounds on several related regularity lemmas, including the weak regularity lemma of Frieze and Kannan and the recently established regular approximation theorem. In particular, we show that a weak partition with approximation parameter ǫ may require as many as 2Ω(ǫ

−2) parts. This is tight up to the implied constant and solves a problem studied by Lov´asz and Szegedy.

# 1 Introduction

Originally developed by Szemere´di as part of his proof of the celebrated Erd˝os-Tura´n conjecture on long arithmetic progressions in dense subsets of the integers [39], Szemere´di’s regularity lemma [40] has become a central tool in extremal combinatorics. Roughly speaking, the lemma says that the vertex set of any graph may be partitioned into a small number of parts such that the bipartite subgraph between almost every pair of parts behaves in a random-like fashion.

Given two subsets X and Y of a graph G, we write d(X,Y ) for the density of edges between X and Y . The pair (X,Y ) is said to be (ǫ,δ)-regular if for some α and all X′ ⊂ X and Y ′ ⊂ Y with |X′| ≥ δ|X| and |Y ′| ≥ δ|Y |, we have α < d(X′,Y ′) < α + ǫ. In the case where δ = ǫ, we say that the pair (X,Y ) is ǫ-regular. By saying that a pair of parts is random-like, we mean that they are (ǫ,δ)-regular with ǫ and δ small, a property which is easily seen to be satisﬁed with high probability by a random bipartite graph. We will also ask that the diﬀerent parts be of comparable size, that is, that the partition

- V (G) = V1 ∪ ... ∪ Vk be equitable, that is, ||Vi| − |Vj|| ≤ 1 for all i and j.


![image 1](<2011-conlon-bounds-graph-regularity-removal_images/imageFile1.png>)

∗St John’s College, Cambridge CB2 1TP, United Kingdom. E-mail: d.conlon@dpmms.cam.ac.uk. Research supported by a Royal Society University Research Fellowship.

†Department of Mathematics, MIT, Cambridge, MA 02139-4307. E-mail: fox@math.mit.edu. Research supported by a Simons Fellowship and NSF grant DMS-1069197.

The regularity lemma now states that for each ǫ,δ,η > 0, there is a positive integer M = M(ǫ,δ,η) such that the vertices of any graph G can be equitably partitioned V (G) = V1 ∪...∪VM into M parts where all but at most an η fraction of the pairs (Vi,Vj) are (ǫ,δ)-regular. We shall say that such a partition is (ǫ,δ,η)-regular and simply ǫ-regular in the case ǫ = δ = η. For more background on the regularity lemma, see the excellent surveys by Komlo´s and Simonovits [27] and Ro¨dl and Schacht [33]. Use of the regularity lemma is now widespread throughout graph theory. However, one of the earliest applications, the triangle removal lemma of Ruzsa and Szemere´di [36], remains the standard example. It states that for any ǫ > 0 there exists δ > 0 such that any graph on n vertices with at most δn3 triangles can be made triangle-free by removing ǫn2 edges. It easily implies Roth’s theorem [34] on 3term arithmetic progressions in dense sets of integers, and Solymosi [37] showed that it further implies the stronger corners theorem of Ajtai and Szemere´di [1], which states that any dense subset of the integer grid contains the vertices of an axis-aligned isosceles triangle. This result was extended to all graphs in [17, 3]. The extension, known as the graph removal lemma, says that given a graph H on h vertices and ǫ > 0 there exists δ > 0 such that any graph on n vertices with at most δnh copies of H can be made H-free by removing ǫn2 edges.

One disadvantage of applying the regularity lemma to prove this theorem is the bounds that it gives for the size of δ in terms of ǫ. The proof of the regularity lemma yields a bound of tower-type for the number of pieces in the partition. When this is applied to graph removal, it gives a bound for δ−1 which is a tower of twos of height polynomial in ǫ−1. Surprisingly, any hope that a better bound for the regularity lemma might be found was put to rest by Gowers [22], who showed that there are graphs for which a tower-type number of parts are required in order to obtain a regular partition.

To be more precise, the proof of the regularity lemma shows that M(ǫ,δ,η) can be taken to be a tower of twos of height proportional to ǫ−2δ−2η−1. Gowers’ result, described in [13] as a tour de force, is a lower bound, with c = 1/16, on M(1 − δc,δ,1 − δc) which is a tower of twos of height proportional to δ−c. As Gowers notes, it is an easy exercise to translate lower bounds for small δ and large ǫ into lower bounds for large δ and small ǫ which are also of tower-type. However, the natural question, discussed by Szemere´di [40], Komlo´s and Simonovits [27], and Gowers [22], of determining the dependency of M(ǫ,δ,η) on η, which measures the fraction of allowed irregular pairs, has remained open. This is the ﬁrst problem we will address here, showing that the dependence is again of tower-type.

This does not mean that better bounds cannot be proved for the graph removal lemma. Recently, an alternative proof was found by the second author [18], allowing one to show that δ−1 may be taken to be a tower of twos of height O(log ǫ−1), better than one could possibly do using regularity. Though this remains quite far from the lower bound of ǫ−O(logǫ−1), it clears a signiﬁcant hurdle.

The second major theme of this paper is a proof of the induced graph removal lemma which similarly bypasses a natural obstacle. Let H be a graph on h vertices. The induced graph removal lemma, proved by Alon, Fischer, Krivelevich, and Szegedy [5], states that for any ǫ > 0 there exists δ > 0 such that any graph on n vertices with at most δnh induced copies of H may be made induced H-free by adding or deleting at most ǫn2 edges.

This result, which easily implies the graph removal lemma, does not readily follow from the same

technique used to prove the graph removal lemma, mainly because of the possibility of irregular pairs in the regularity partition. To overcome this issue, Alon, Fischer, Krivelevich, and Szegedy [5] developed a strenghthening of Szemere´di’s regularity lemma. Roughly, it gives an equitable partition

- A and an equitable reﬁnement B of A such that A and B are both regular, with the guaranteed regularity of B allowed to depend on the size of A, and the edge density between almost all pairs of parts in B close to the edge density between the pair of parts in A that they lie in. The proof of the strong regularity lemma involves iterative applications of Szemere´di’s regularity lemma. This causes the upper bound on the number of parts in B to grow as a wowzer function, which is one level higher in the Ackermann hierarchy than the tower function. In order to get an improved bound for its various applications, one may hope that an improved bound of tower-type could be established. We show that no such bound exists. In fact, we will show that a seemingly weaker statement requires wowzer-type bounds. On the other hand, we give an alternative proof of the induced graph removal lemma, allowing one to show that δ−1 may be taken to be a tower of twos of height polynomial in ǫ−1, better than one could possibly achieve using the strong regularity lemma. We also make progress on determining bounds for various related regularity lemmas, including the Frieze-Kannan weak regularity lemma [19, 20] and the regular approximation theorem, due independently to Lov´asz and Szegedy [29] and to Ro¨dl and Schacht [32]. We discuss all these contributions in more detail in the sections below.

- 1.1 The number of irregular pairs


The role of η in the regularity lemma is to measure how many pairs of subsets in the partition are regular. If a partition into k pieces is (ǫ,δ,η)-regular, then there will be at most η k2 irregular pairs in the partition. Szemere´di [40] wrote that it would be interesting to determine if the assertion of the regularity lemma holds when we do not allow any irregular pairs. This question remained unanswered for a long time until it was observed by Lov´asz, Seymour, Trotter, and Alon, Duke, Lefmann, Ro¨dl, and Yuster [3] that irregular pairs can be necessary. The simple example of the half-graph shows that this is indeed the case. The half-graph is a bipartite graph with vertex sets A = {a1,... ,an} and

- B = {b1,... ,bn} in which (ai,bj) is an edge if and only if i ≤ j. Any partition of this graph into M parts will have Ω(M) irregular pairs. In other words, M(ǫ,δ,η) must grow at least linearly in η−1. However, the number of irregular pairs, or, in other words, the dependence of M(ǫ,δ,η) on η−1 with ǫ and δ ﬁxed, has not been well understood despite being asked several times, including by Komlo´s and Simonovits [27] and, more explicitly, by Gowers [22]. This problem and related problems have continued to attract interest (see, e.g., [26], [30]). The linear bound obtained from the half-graph appears to be the only bound in the literature for this problem. For ﬁxed constants ǫ and δ and each M, we give a construction in which any partition into M parts has at least cM2/log∗ M irregular parts, where c > 0 is an absolute constant, and this is tight apart from the constant c. The iterated logarithm log∗ n is the number of times the logarithm function needs to be applied to get a number which is at most 1. That is, log∗ x = 0 if x ≤ 1 and otherwise log∗ x = 1 + log∗(log x) denotes the iterated logarithm. In other words, the dependence on η in


M(ǫ,δ,η) is indeed a tower of twos of height proportional to Θ(η−1).

- Theorem 1.1 There are absolute constants c,ǫ,δ > 0 such that for every k there is a graph in which every equitable partition of the graph into k parts has at least ck2/log∗ k pairs of parts which are not (ǫ,δ)-regular. In other words, M(ǫ,δ,η) is at least a tower of twos of height cη−1.


We prove Theorem 1.1 with ǫ = 21, δ = 2−500, and c = 2−700, and we make no attempt to optimize constants. The proof of Theorem 1.1 can be easily modiﬁed to obtain the same result with ǫ tending

![image 2](<2011-conlon-bounds-graph-regularity-removal_images/imageFile2.png>)

to 1 at the expense of having δ and c tending to 0.

In the important special case where ǫ = δ = η, we let M(ǫ) = M(ǫ,δ,η). Gowers [22] gave two diﬀerent constructions giving lower bounds on M(ǫ). The ﬁrst construction is simpler, but the lower bound it gives is a tower of twos of height only logarithmic in ǫ−1. The second construction gives a lower bound which is a tower of twos of height ǫ−1/16, but is more complicated. Theorem 1.1 also gives a lower bound on M(ǫ) which is a tower of twos of height polynomial in ǫ−1, in fact linear in ǫ−1, and the construction is a bit simpler. Unfortunately, the proof that it works, which builds upon Gowers’ simpler ﬁrst proof, is still rather complicated and delicate.

We give a rough idea of how the graph G used to prove Theorem 1.1 is constructed. The graph G has a sequence of vertex partitions P1,... ,Ps, with Pi+1 a reﬁnement of Pi for 1 ≤ i ≤ s−1, and the number of parts of Pi+1 is roughly exponential in the number of parts of Pi. For each i, 1 ≤ i ≤ s − 1, we pick a random graph Gi with vertex set Pi, where each edge is picked independently with probability pi. For every two vertex subsets X,Y ∈ Pi of G which are adjacent in Gi, we take random vertex partitions X = XY1 ∪XY2 and Y = YX1 ∪YX2 into parts of equal size, with each of these parts the union of parts of Pi+1. Then, for d = 1,2, we add the edges to G between XYd and YXd. We will show that with positive probability the graph G constructed above has the desired properties for Theorem 1.1. In fact, in Theorem 3.1, we will show that it has the stronger property that any (ǫ,δ,η)-regular vertex partition of G is close to being a reﬁnement of Ps. A novelty of our construction, not present in the constructions of Gowers, is the use of the random graphs Gi, which allow us to control the number of irregular pairs. Instead, for every pair of parts X,Y in Pi, Gowers [22] introduces or deletes some edges between them so as to make the pair of parts far from regular. To prove the desired result, we ﬁrst establish several lemmas on the edge distribution in G. The construction is general enough and Theorem 3.1 strong enough that we also use it to establish a wowzer-type lower bound for the strong regularity lemma, as described in the next subsection.

## 1.2 The strong regularity lemma

Before stating the strong regularity lemma, we next deﬁne a notion of closeness between an equitable partition and an equitable reﬁnement of this partition. For an equitable partition A = {Vi|1 ≤ i ≤ k} of V (G) and an equitable reﬁnement B = {Vi,j|1 ≤ i ≤ k,1 ≤ j ≤ ℓ} of A, we say that B is ǫ-close to A if the following is satisﬁed. All 1 ≤ i ≤ i′ ≤ k but at most ǫk2 of them are such that for all

- 1 ≤ j,j′ ≤ ℓ but at most ǫℓ2 of them |d(Vi,Vi′) − d(Vi,j,Vi′,j′)| < ǫ holds. This notion roughly says


that B is an approximation of A. We are now ready to state the strong regularity lemma of Alon, Fischer, Krivelevich, and Szegedy [5].

- Lemma 1.1 (Strong regularity lemma) For every function f : N → (0,1) there exists a number S = S(f) with the following property. For every graph G = (V,E), there is an equitable partition A of the vertex set V and an equitable reﬁnement B of A with |B| ≤ S such that the partition A is f(1)-regular, the partition B is f(|A|)-regular, and B is f(1)-close to A.


The upper bound on S, the number of parts of B, that the proof gives is of wowzer-type, which is one level higher in the Ackermann hierarchy than the tower function. The tower function is deﬁned by T(1) = 2, and T(n) = 2T(n−1) for n ≥ 2. The wowzer function W(n) is deﬁned by W(1) = 2 and W(n) = T(W(n − 1)). For reasonable choices of the function f, which is the case for all known applications, such as those for which 1/f is an increasing function which is at least a constant number of iterations of the logarithm function, the upper bound on S(f) is at least wowzer in a power of ǫ = f(1). Recall that M(ǫ), the number of parts required for Szemere´di’s regularity lemma, grows as a tower of height a power of ǫ−1. The precise upper bound on the number of parts in the strong regularity lemma is deﬁned as follows. Let W1 = M(ǫ) and Wi+1 = M(2f(Wi)/Wi2). The proof of the strong regularity lemma [5] shows that S(f) = 512ǫ−4Wj with j = 64ǫ−4 satisﬁes the required property.

For a partition P : V (G) = V1 ∪ ... ∪ Vk of the vertex set of a graph G, the mean square density of P is deﬁned by

d2(Vi,Vj)pipj,

q(P) =

i,j

where pi = |Vi|/|V (G)|. This function plays an important role in the proof of Szemere´di’s regularity lemma and its variants.

The strong regularity lemma gives a regular partition A, and a reﬁnement B which is much more regular and is close to A. For equitable partitions A and B with B a reﬁnement of A, the condition B is ǫ-close to A is equivalent, up to a polynomial change in ǫ, to q(B) ≤ q(A)+ǫ. Indeed, if B is ǫ-close to A, then q(B) ≤ q(A) + O(ǫ), while if q(B) ≤ q(A) + ǫ, then B is O(ǫ1/4)-close to A. A version of this statement is present in Lemma 3.7 of [5]. As it is suﬃicent and more convenient to work with mean square density instead of ǫ-closeness, we do so from now on.

Note that in the strong regularity lemma, without loss of generality we may assume f is a (monotonically) decreasing function. Indeed, this can be shown by considering the decreasing function f′(k) := min1≤i≤k f(k). From the above discussion, it is easy to see that the strong regularity lemma has the following simple corollary, with a similar upper bound.

- Corollary 1.1 Let ǫ > 0 and f : N → (0,1) be a decreasing function. Then there exists a number S = S(f,ǫ) such that for every graph G there are equitable partitions A,B of the vertex set of G with |B| ≤ S, q(B) ≤ q(A) + ǫ, and B is f(|A|)-regular.


We prove a lower bound for the strong regularity lemma of wowzer-type, which essentially matches the upper bound. Maybe surprisingly, our construction further shows that much less than what is required

from the strong regularity lemma already gives wowzer-type bounds. In particular, even for Corollary

- 1.1, which appears considerably weaker than the strong regularity lemma, we get a wowzer-type lower bound. Note that in Corollary 1.1, B is not required to be a reﬁnement of A. In this case we could have q(B) being close to q(A) but the edge densities between the parts in these partitions are quite diﬀerent from each other, i.e., these partitions are not close to each other.


- Theorem 1.2 Let 0 < ǫ < 2−100 and f : N → (0,1) be a decreasing function with f(1) ≤ 2−100ǫ6. Deﬁne Wℓ recursively by W1 = 1, Wℓ+1 = T 2−70ǫ5/f(Wℓ) , where T is the tower function. Let


- W = Wt−1 with t = 2−20ǫ−1. Then there is a graph G such that if equitable partitions A,B of the vertex set of G satisfy q(B) ≤ q(A) + ǫ and B is f(|A|)-regular, then |A|,|B| ≥ W.


We have the following corollary (by replacing ǫ by ǫ1/7), which is a simple to state lower bound of wowzer-type.

- Corollary 1.2 For 0 < ǫ < 2−700, there is a graph G such that if equitable partitions A,B of the vertex set of G satisfy |B| ≥ |A|, q(B) ≤ q(A) + ǫ and B is ǫ/|A|-regular, then |B|,|A| are bounded below by a function which is wowzer in Ω(ǫ−1/7).


## 1.3 Induced graph removal

Let H be a ﬁxed graph on h vertices and let G be a graph with o(nh) copies of H. To prove the graph removal lemma, we need to prove that all copies of H can be removed from G by deleting o(n2) edges. The standard approach is to apply the regularity lemma to the graph G to obtain an ǫ-regular vertex partition (with an appropriate ǫ) into a constant number of parts M(ǫ). Then delete edges between pairs of parts (Vi,Vj), including i = j, if the pair is not ǫ-regular or the density between the pair is small. It is easy to see that there are few deleted edges. Furthermore, if there is a copy of H in the remaining subgraph, then the edges go between pairs of parts which are ǫ-regular and not of small density. A counting lemma then shows that in such a case the number of copies of H is Ω(nh) in the remaining subgraph, and hence in G as well. But this would contradict the assumption that G has

- o(nh) copies of H, so all copies of H must already have been removed. Recall that the induced graph removal lemma [5] is the analogous statement for induced subgraphs, and it is stronger than the graph removal lemma. It states that for any graph H on h vertices and ǫ > 0 there is δ = δ(ǫ,H) > 0 such that if a graph G on n vertices has at most δnh induced copies of H, then we can add or delete ǫn2 edges of G to obtain an induced H-free graph. One well-known application of the induced graph removal lemma is in property testing. This is an active area of computer science where one wishes to quickly distinguish between objects that satisfy a property from objects that are far from satisfying that property. The study of this notion was initiated by Rubinﬁeld and Sudan [35], and subsequently Goldreich, Goldwasser, and Ron [21] started the investigation of property testers for combinatorial objects. One simple consequence of the induced graph removal lemma is a constant time algorithm for induced subgraph testing with one-sided error (see [2] and its references). A graph on n vertices is ǫ-far from being induced H-free if at least ǫn2


edges need to be added or removed to make it induced H-free. The induced graph removal lemma implies that there is an algorithm which runs in time Oǫ(1) which accepts all induced H-free graphs, and rejects any graph which is ǫ-far from being induced H-free with probability at least 2/3. The algorithm samples t = 2δ−1 h-tuples of vertices uniformly at random, where δ is picked according to the induced graph removal lemma, and accepts if none of them form an induced copy of H, and

- otherwise rejects. Any induced H-free graph is clearly accepted. If a graph is ǫ-far from being induced H-free, then it contains at least δnh copies of H, and the probability that none of the sampled h-tuples forms an induced copy of H is at most (1 − δ)t < 1/3. Notice that the running time as a function of ǫ depends on the bound in the induced graph removal lemma, and the proof using the strong regularity lemma gives a wowzer-type dependence. It is tempting to try the same approach using Szemere´di’s regularity lemma to obtain the induced graph removal lemma. However, there is a signiﬁcant problem with this approach, which is handling the pairs between irregular pairs. To get around this issue, Alon, Fischer, Krivelevich, and Szegedy [5] developed the strong regularity lemma. Because of its applications, including those in graph property testing, it has remained an intriguing problem to improve the bound in the induced graph removal lemma. This problem has been discussed in several papers by Alon and his collaborators [2], [6], [8]. The main result discussed in this subsection addresses this problem, improving the bound on the number of parts in the induced graph removal lemma from wowzer-type to tower-type. The tower function ti(x) is deﬁned by t0(x) = x and ti+1(x) = 2ti(x). We say that ti(x) is a tower in x of height i.


- Theorem 1.3 For any graph H on h vertices and 0 < ǫ < 1/2 there is δ > 0 with δ−1 a tower in h of height polynomial in ǫ−1 such that if a graph G on n vertices has at most δnh induced copies of H, then we can add or delete ǫn2 edges of G to obtain an induced H-free graph.


The following lemma is an easy corollary of the strong regularity lemma which was used in [5] to establish the induced graph removal lemma.

- Lemma 1.2 For each 0 < ǫ < 1/3 and decreasing function f : N → (0,1/3) there is δ′ = δ′(ǫ,f) such that every graph G = (V,E) with |V | ≥ δ′−1 has an equitable partition V = V1 ∪ ... ∪ Vk and vertex subsets Wi ⊂ Vi such that |Wi| ≥ δ′|V |, each pair (Wi,Wj) with 1 ≤ i ≤ j ≤ k is f(k)-regular, and all but at most ǫk2 pairs 1 ≤ i ≤ j ≤ k satisfy |d(Vi,Vj) − d(Wi,Wj)| ≤ ǫ.


In fact, Lemma 1.2 is a little bit stronger than the original version in [5] in that each set Wi is f(k)-regular with itself. The original version follows from the strong regularity lemma by taking the partition V = V1 ∪ ... ∪ Vk to be the partiton A in the strong regularity lemma, and the subset Wi to be a random part Vij ⊂ Vi of the reﬁnement B of A in the strong regularity lemma. From this slightly stronger version, the proof of the induced graph removal lemma is a bit simpler and shorter. Indeed, with f(k) = 41hǫh, which does not depend on k, if there is a mapping φ : V (H) → {1,... ,k} such that for all adjacent vertices v,w of H, the edge density between Wφ(v) and Wφ(w) is at least ǫ, and for all distinct nonadjacent vertices v,w of H, the edge density between Wφ(v) and

![image 3](<2011-conlon-bounds-graph-regularity-removal_images/imageFile3.png>)

Wφ(w) is at most 1 − ǫ, then a standard counting lemma shows that G contains at least δnh induced copies of H, where δ = (ǫ/4)(h2)δ′h. Hence, we may assume that there is no such mapping φ. We then delete edges between Vi and Vj if the edge density between Wi and Wj is less than ǫ, and one adds the edges between Vi and Vj if the density between Wi and Wj is more than 1 − ǫ. The total number of edges added or removed is at most 5ǫn2, and no induced copy of H remains. Replacing ǫ by ǫ/8 in the above argument gives the induced graph removal lemma.

We ﬁnd another proof of Lemma 1.2 with a better tower-type bound. This in turn implies, by the argument sketched above, the tower-type bound for the induced graph removal lemma stated in Theorem 1.3.

The starting point for our approach to Lemma 1.2 is a weak regularity lemma due to Duke, Lefmann and Ro¨dl [15]. This lemma says that for a k-partite graph, between sets V1,V2,... ,Vk, there is an ǫ-regular partition of the cylinder V1 × ··· × Vk into a relatively small number of cylinders K = W1 × ··· × Wk, with Wi ⊂ Vi for 1 ≤ i ≤ k. The deﬁnition of an ǫ-regular partition here is that all but an ǫ-fraction of the k-tuples (v1,... ,vk) ∈ V1 ×···×Vk are in ǫ-regular cylinders, where a cylinder W1 × ··· × Wk is ǫ-regular if all k2 pairs (Wi,Wj), 1 ≤ i < j ≤ k, are ǫ-regular in the usual sense.

In the same way that one derives the strong regularity lemma from the ordinary regularity lemma, we show how to derive a strong version of this lemma. We will refer to this strengthening, of which

- Lemma 1.2 is a straightforward consequence, as the strong cylinder regularity lemma. It will also be convenient if, in this lemma, we make the requirement that a cylinder be regular slightly stronger, by asking that each Wi be regular with itself. That is, we say that a cylinder W1 × ··· × Wk is strongly ǫ-regular if all pairs (Wi,Wj) with 1 ≤ i,j ≤ k are ǫ-regular. A partition K of the cylinder V1×···×Vk into cylinders K = W1 × ··· × Wk, with Wi ⊂ Vi for 1 ≤ i ≤ k, is then said to strongly ǫ-regular if all but an ǫ-fraction of the k-tuples (v1,... ,vk) ∈ V1 × ··· × Vk are in strongly ǫ-regular cylinders. Let P : V = V1 ∪ ··· ∪ Vk be a partition of the vertex set of a graph and K be a partition of the cylinder V1 × ··· × Vk into cylinders. For each K = W1 × ··· × Wk, with Wi ⊂ Vi for 1 ≤ i ≤ k, we let Vi(K) = Wi. We then deﬁne the partition Q(K) of V to be the reﬁnement of P which is the common reﬁnement of all the parts Vi(K) with i ∈ [k] and K ∈ K. The strong cylinder regularity lemma is now as follows.
- Lemma 1.3 For 0 < ǫ < 1/3, positive integer s, and decreasing function f : N → (0,ǫ], there is S = S(ǫ,s,f) such that the following holds. For every graph G, there is an integer s ≤ k ≤ S, an equitable


partition P : V = V1 ∪ ... ∪ Vk and a strongly f(k)-regular partition K of the cylinder V1 × ··· × Vk into cylinders satisfying that the partition Q = Q(K) of V has at most S parts and q(Q) ≤ q(P) + ǫ. Furthermore, there is an absolute constant c such that letting s1 = s and si+1 = t4 ((si/f(si))c), we may take S = sℓ with ℓ = 2ǫ−1 + 1.

In order to prove this lemma, we need, in addition to the Duke-Lefmann-R¨dl regularity lemma, a lemma showing that for each ǫ > 0 there is δ > 0 such that every graph G = (V,E) contains a vertex subset U with |U| ≥ δ|V | which is ǫ-regular with itself, where, crucially, δ−1 is bounded above by a tower function of ǫ−1 of absolute constant height. While seemingly standard, we do not know of such a result in the literature.

- Lemma 1.2 follows from Lemma 1.3 by considering a random cylinder K in the cylinder partition K, with each cylinder picked with probability proportional to its size, and letting Wi = Vi(K).


## 1.4 Frieze-Kannan weak regularity lemma

Frieze and Kannan [19], [20] developed a weaker notion of regularity which is suﬃcient for certain applications and for which the dependence on the approximation ǫ is much better. It states the existence of a vertex partition into a small number of parts for which the number of edges across any two vertex subsets is within ǫn2 of what is expected based on the edge densities between the parts of the partition and the intersection sizes of the vertex subsets with these parts.

- Lemma 1.4 (Frieze-Kannan weak regularity lemma) For each ǫ > 0 there is a positive integer


k(ǫ) such that every graph G = (V,E) has an equitable vertex partition V = V1 ∪...∪Vk with k ≤ k(ǫ) satisfying that for all subsets A,B ∈ V , we have

d(Vi,Vj)|A ∩ Vi||B ∩ Vj| ≤ ǫ|V |2.

e(A,B) −

1≤i,j≤k

The weak regularity lemma has a number of algorithmic applications. Frieze and Kannan [20] used the weak regularity lemma to give constant-time approximation algorithms for some general problems in dense graphs, a special case being the Max-Cut of a graph. Recently, Bansal and Williams [12] used the weak regularity lemma to obtain a faster combinatorial algorithm for Boolean matrix multiplication. The importance of the weak regularity lemma is further discussed in the citation of the recent Knuth Prize to Kannan.

As there are several applications of the weak regularity lemma to fundamental algorithmic problems, we would like to know the correct bounds on the number of parts for the weak regularity lemma. The proof of the weak regularity lemma [20] shows that we may take k(ǫ) = 2O(ǫ−2). If this upper bound could be improved, it would lead to faster algorithms for several problems of interest. Lov´asz and Szegedy [29] studied the problem of estimating the minimum number of parts k(ǫ) required for the weak regularity lemma, proving a lower bound on k(ǫ) of the form 2Ω(ǫ−1). Here we close the gap by proving a new lower bound which matches the upper bound.

- Theorem 1.4 For each ǫ > 0, there are graphs for which the minimum number of parts in a weak regular partition with approximation ǫ is 2Ω(ǫ−2).


A careful analysis of the proof of Theorem 1.4 shows that the number of parts required in the weak regularity lemma with approximation ǫ is at least 2−2−60ǫ−2 for 0 < ǫ ≤ 2−50. In fact, the theorem yields a stronger result, since we do not here require that the partition be equitable.

While the number of parts in the weak regularity lemma is 2Θ(ǫ−2), the proof obtains the partition as an overlay of only O(ǫ−2) sets. As discussed in [29], in some applications, such as in [4], this can be treated as if there were only about O(ǫ−2) classes, which makes the weak regularity lemma quite eﬃcient. It was shown in [4], and is also implied by Theorem 1.4, that the partition cannot be the overlay of fewer sets.

## 1.5 The regular approximation lemma

Another strengthening of Szemere´di’s regularity lemma came from the study of graph limits by Lov´asz and Szegedy [29], and also from work on the hypergraph generalization of the regularity lemma by Ro¨dl and Schacht [32]. This regularity lemma, known as the regular approximation lemma [33], provides an arbitrary precision for the regularity as a function of the number of parts of the partition if an ǫ-fraction of the edges are allowed to be added or removed.

For a function g : N → (0,1), a partition of the vertex set into k parts is g-regular if all pairs of distinct parts in the partition are g(k)-regular.

- Lemma 1.5 (Regular approximation lemma) For every ǫ > 0, positive integer s and decreasing function g : N → (0,1), there is an integer T = T(g,ǫ,s) so that given a graph G with n vertices, one can add-to/remove-from G at most ǫn2 edges and thus get a graph G′ that has a g-regular equitable partition of order k for some s ≤ k ≤ T.


Lov´asz and Szegedy [29] state that the regular approximation lemma is equivalent to the strong regularity lemma, Lemma 1.1. It is not diﬃcult to deduce Lemma 1.5 from the strong regularity lemma, see [9] or [33] for details. Unlike the original graph limit approach, this proof of the regular approximation lemma gives explicit bounds and yields a polynomial time algorithm for ﬁnding the partition and the necessary edge modiﬁcations. In the other direction, by applying Lemma 1.5 with 1/g a tower in the 1/f from Lemma 1.1, letting A be the g-regular partition of G′, and then using Szemere´di’s regularity lemma to get a reﬁnement B of A which is an f(A)-regular partition of G, it is easy to deduce the strong regularity lemma.

The major caveat here is the additional use of Szemere´di’s regularity lemma in deducing the strong regularity lemma from the regular approximation lemma. Due to the additional use of Szemere´di’s regularity lemma, it does not rule out the possibility that the wowzer-type upper bound on T in the regular approximation lemma can be improved to tower-type. Maybe surprisingly, we indeed make such an improvement.

- Theorem 1.5 For ǫ > 0, positive integer s and a decreasing function g : N → (0,1), let δ(t) =


3

min(g(t)

32t2 ,ǫ/2). Let t1 = s and for i ≥ 1 let ti+1 = tik(δ(ti)), where k is as in the weak regularity lemma, so k(α) = 2O(α−2). Let T0 = tj with j = 4ǫ−2. Then the regular approximation lemma holds with T = 16T0/δ(T0)2. In other words, the regular approximation lemma holds with a tower-type bound.

![image 4](<2011-conlon-bounds-graph-regularity-removal_images/imageFile4.png>)

It is usually the case that 1/g(t) in the regular approximation lemma is at most a tower of constant height in ǫ−1 and t, and in this case the upper bound T on the number of parts is only a tower of height polynomial in ǫ−1. Only in the unusual case of 1/g being of tower-type growth does the number of parts needed in the regular approximation lemma grow as wowzer-type.

Alon, Shapira, and Stav [9] give a proof of the regular approximation lemma which yields a polynomial time algorithm for ﬁnding the partition and the necessary edge modiﬁcations. Similarly, our new proof

can be made algorithmic with a polynomial time algorithm for ﬁnding the partition and the necessary edge modiﬁcations. Making the proof algorithmic is essentially the same as done in [9], so we do not include the details.

A partition of a graph satisfying the weak regularity lemma, Lemma 1.4, is called a weak ǫ-regular partition. Tao showed [41] (see also [33]), by iterating the weak regularity lemma, that one obtains the following regularity lemma which easily implies Szemere´di’s regularity lemma with the usual towertype bounds.

- Lemma 1.6 For all ǫ > 0, positive integers s and functions δ : N → (0,1), there is a T0 such that every graph has an equitable vertex partition P into t ≥ s parts which is weak ǫ-regular, an equitable vertex reﬁnement Q into at most T0 parts which is weak δ(t)-regular, and q(Q) ≤ q(P) + ǫ.


Let t1 = s, and for i ≥ 1, let ti+1 = tik(δ(ti)), where k is as in the weak regularity lemma. Recall k(ǫ) is exponential in ǫ−2. Then T0 in Lemma 1.6 is given by T0 = tj with j = ǫ−1. In particular, if δ−1 is bounded above by a tower of constant height, then T0 in Tao’s regularity lemma grows as a tower of height linear in ǫ−1.

Our proof of Theorem 1.5 shows that the regular approximation lemma is equivalent to Tao’s regularity lemma with similar bounds. In fact, we show that T in the regular approximation lemma can be taken to be T = 16T0/δ(T0)2, where T0 = T0(δ,ǫ0,s) is the bound on the number of parts in Tao’s regularity lemma, δ(t) = min(g(t)

3

32t2 ,ǫ/2), and ǫ0 = (ǫ/2)2. As Tao’s regularity lemma is a simple consequence of the regular approximation lemma and an application of the weak regularity lemma, it suﬃces to show how to deduce the regular approximation lemma from Tao’s regularity lemma.

![image 5](<2011-conlon-bounds-graph-regularity-removal_images/imageFile5.png>)

The proof starts by applying Tao’s regularity lemma with δ and ǫ0 as above. For each pair (X,Y ) of parts in Q, where X ⊂ A and Y ⊂ B with A,B parts of P, we randomly add/delete edges between X,Y with a certain probability so that the density between X and Y is about the same as the density between A and B. We show that in doing this we have made every pair (A,B) of parts of P g(t)regular with t = |P|. Since q(Q) ≤ q(P) + ǫ0, the edge density d(X,Y ) between most pairs (X,Y ) of parts of Q is close to the edge density d(A,B) between A and B, and few edges are changed to obtain a graph G′ for which the partition P is g-regular.

We next brieﬂy discuss lower bounds for the regular approximation lemma. In the case g is a (small) constant function, a tower-type lower bound follows from Theorem 1.1. If g is at least a tower function, we get a lower bound of wowzer-type from Theorem 1.2 and the fact that the strong regularity lemma follows from the regularity approximation lemma with an additional application of Szemere´di’s regularity lemma as discussed earlier. One could likely come up with a construction giving a general lower bound essentially matching Theorem 1.5, but as the already mentioned interesting cases discussed above are handled by Theorems 1.1 and 1.2, we do not include such a construction.

Organization

In the next section, we prove some useful tools for establishing lower bounds for Szemere´di’s regularity lemma and the strong regularity lemma. In Section 3, we give a general construction and use it to prove Theorem 1.1 which addresses questions of Szemere´di and Gowers on the number of irregular

pairs in Szemere´di’s regularity lemma. In Section 4, we use the general construction to prove Theorem

- 1.2, which gives a wowzer-type lower bound on the number of parts of the two partitions in the strong regularity lemma. In Section 5, we prove the strong cylinder regularity lemma and use it to prove a tower-type upper bound on the induced graph removal lemma. In Section 6, we prove a tower-type upper bound on the number of parts in the regular approximation lemma. In Section 7, we prove a tight lower bound on the number of parts in the weak regularity lemma. These later sections, Sections 5, 6 and 7, are largely independent of earlier sections and of each other. The interested reader may therefore skip forward without fear of losing the thread. We ﬁnish with some concluding remarks. This includes a discussion showing that in the regularity lemma, the condition that the parts in the partition are of equal size does not aﬀect the bounds by much. We also discuss an early version of Szemere´di’s regularity lemma, and a recent result of Malliaris and Shelah which shows an interesting connection between irregular pairs in the regularity lemma and the appearance of half-graphs. Throughout the paper, we systematically omit ﬂoor and ceiling signs whenever they are not crucial for the sake of clarity of presentation. We also do not make any serious attempt to optimize absolute constants in our statements and proofs.


# 2 Tools

Suppose S = S1 + ··· + Sn is the sum of n mutually independent random variables, where for each i, Pr[Si = 1] = p and Pr[Si = 0] = 1 − p. The sum S has a binomial distribution with parameters p and n, and has expected value pn. A Chernoﬀ-type estimate (see Theorem A.1.4 in [10]) implies that for a > 0,

Pr[S − pn > a] < e−2a2/n (1) By symmetry, we also have Pr[S − pn < −a] < e−2a2/n and hence Pr[|S − pn| > a] < 2e−2a2/n.

We start by proving a couple of lemmas on the edge distribution of random bipartite graphs with diﬀerent part sizes. Consider the random bipartite graph B = B(m,M) with parts [m] and [M] formed by each vertex i ∈ [m] having exactly M/2 neighbors (we assume M is even) in [M] picked uniformly at random and independently of the choices of the neighborhoods for the other vertices in [m].

The following lemma shows that, with high probability, certain simple estimates on the number of common neighbors or nonneighbors of any two vertices in B(m,M) hold.

- Lemma 2.1 Let M ≥ m be positive integers with M ≥ 220 even, and 0 < µ < 1/2 be such that m ≥ 2µ−2 log M. Then, with probability at least 1 − M−2, the random bipartite graph B = B(m,M) has the following properties:


- • for any distinct j,j′ ∈ [M], the number of i for which j and j′ are either both neighbors of i or both nonneighbors of i is less than (21 + µ)m.


![image 6](<2011-conlon-bounds-graph-regularity-removal_images/imageFile6.png>)

- • for any distinct i,i′ ∈ [m], the number of common neighbors of i and i′ and the number of common nonneighbors of i and i′ in [M] are both less than 4 1 + M−1/4 M.


![image 7](<2011-conlon-bounds-graph-regularity-removal_images/imageFile7.png>)

Proof: Fix distinct j,j′ ∈ [M]. For each i ∈ [m], the probability that i is adjacent to both j,j′ or nonadjacent to both j,j′ is (M2 − 1)/(M − 1) < 21, and these events are independent of each other. Therefore, by (1), the probability that the number of i for which j and j′ are either both neighbors of

![image 8](<2011-conlon-bounds-graph-regularity-removal_images/imageFile8.png>)

![image 9](<2011-conlon-bounds-graph-regularity-removal_images/imageFile9.png>)

- i or both nonneighbors of i is at least (12 + µ)m is at most e−2(µm)2/m = e−2µ2m ≤ M−4. As there are M


![image 10](<2011-conlon-bounds-graph-regularity-removal_images/imageFile10.png>)

2 choices for j,j′, and 12M−2 ≥ M−4 M2 , by the union bound we have that B has the ﬁrst desired property with probability at least 1 − 12M−2. As the hypergeometric distribution is at least as concentrated as the corresponding binomial distribution (for a proof, see Section 6 of [25]), we can apply (1) to conclude that for each ﬁxed pair i,i′ ∈ [m] of distinct vertices the probability that the number of common neighbors of i and i′ is at least 14 + M−1/4 M is at most e−2(M−1/4M)2/M = e−2M1/2. Similarly, for each ﬁxed pair i,i′ ∈ [m] of distinct vertices the probability that the number of common nonneighbors of i and i′ in [M] is at least 4 1 + M−1/4 M is at most e−2M1/2.

![image 11](<2011-conlon-bounds-graph-regularity-removal_images/imageFile11.png>)

![image 12](<2011-conlon-bounds-graph-regularity-removal_images/imageFile12.png>)

![image 13](<2011-conlon-bounds-graph-regularity-removal_images/imageFile13.png>)

![image 14](<2011-conlon-bounds-graph-regularity-removal_images/imageFile14.png>)

- As there are m2 choices for i,i′ and 12M−2 ≥ 2e−2M1/2 m2 , by the union bound we have that B has the second desired property with probability at least 1 − 21M−2. Hence, with probability at least


![image 15](<2011-conlon-bounds-graph-regularity-removal_images/imageFile15.png>)

![image 16](<2011-conlon-bounds-graph-regularity-removal_images/imageFile16.png>)

- 1 − M−2, B has both desired properties, which completes the proof. ✷


The next lemma shows that the edges in B(m,M) are almost surely uniformly distributed between large vertex subsets.

- Lemma 2.2 Let M and m be positive integers with M even. With probability at least 1 − M−1, for any U1 ⊂ [m] and U2 ⊂ [M] with |U1| = u1 and |U2| = u2, we have


- 1

![image 17](<2011-conlon-bounds-graph-regularity-removal_images/imageFile17.png>)

- 2


![image 18](<2011-conlon-bounds-graph-regularity-removal_images/imageFile18.png>)

|eB(U1,U2) −

u1u2| ≤ f, (2) where

em u1

eM u2

f = f(u1,u2) = u1u2 u1 ln

+ u2 ln

.

![image 19](<2011-conlon-bounds-graph-regularity-removal_images/imageFile19.png>)

![image 20](<2011-conlon-bounds-graph-regularity-removal_images/imageFile20.png>)

Proof: For ﬁxed subsets U1 ⊂ [m] and U2 ⊂ [M], the random variable eB(U1,U2), which has mean 12|U1||U2|, despite not satisfying a binomial distribution, still satisﬁes the estimate (1) for the corresponding binomial distribution with parameters 1/2 and |U1||U2|. Indeed, note that eB(U1,U2) is the sum of the degrees of the vertices of U1 in U2, and these |U1| degrees are identical independent random variables, each satisfying a hypergeometric distribution. By Theorem 4 in Section 6 of [25], the expected value of the exponential of a random variable with a hypergeometric distribution is at most the expected value of the exponential of the random variable with the corresponding binomial distribution. Substituting this estimate into the proof of (1) shows that the Chernoﬀ estimate also holds for eB(U1,U2). Hence, the probability (2) doesn’t hold for a particular pair U1,U2 is less than

![image 21](<2011-conlon-bounds-graph-regularity-removal_images/imageFile21.png>)

- 2e−2f/(u1u2). By the union bound, the probability that there is a pair of subsets U1 ⊂ [m] and U2 ⊂ [M] not satisfying (2) is at most


m

M

u1=1

u2=1

m u1

M u2

2e−2f/(u1u2) ≤

=

m

M

u1=1

u2=1

m

M

2

u1=1

u2=1

em u1

![image 22](<2011-conlon-bounds-graph-regularity-removal_images/imageFile22.png>)

u1 eM u2

![image 23](<2011-conlon-bounds-graph-regularity-removal_images/imageFile23.png>)

u2

2e−2f/(u1u2)

em u1

![image 24](<2011-conlon-bounds-graph-regularity-removal_images/imageFile24.png>)

−u1 eM u2

![image 25](<2011-conlon-bounds-graph-regularity-removal_images/imageFile25.png>)

−u2

≤ M−1.

✷

From the bipartite graph B, we construct equitable partitions (Ai,Bi)mi=1 of [M], by letting Ai denote the set of neighbors of vertex i ∈ [m] in graph B. From Lemmas 2.1 and 2.2, we have the following corollary.

- Corollary 2.1 Suppose M ≥ m are positive integers with M ≥ 220 even, and 0 < µ < 1/2 is such that m ≥ 2µ−2 log M. There is a bipartite graph B with parts [m] and [M], with each vertex in [m] of degree M/2 with the following properties. The estimate (2) holds for all U1 ⊂ [m] and U2 ⊂ [M] with |U1| = u1 and |U2| = u2, and B satisﬁes the two properties in the conclusion of Lemma 2.1.


The next lemma is a useful consequence of the equitable partitions (Ai,Bi)mi=1 behaving randomly. Given a vector λ ∈ RM and 1 ≤ q < ∞, write ||λ||q for Mi=1 |λi|q

1/q

and ||λ||∞ for max1≤i≤M |λi|.

- Lemma 2.3 Let M be a positive even integer, 0 < µ < 1/2, and (Ai,Bi)mi=1 be a sequence of partitions satisfying the conclusion of Corollary 2.1. Suppose that 0 < σ,τ,α are such that σ,τ < 1, α < 1/2, and


- 1

![image 26](<2011-conlon-bounds-graph-regularity-removal_images/imageFile26.png>)

- 2 − µ)(1 − σ2) >


τ 2

(

+ 2(1 − τ)α(1 − α).

![image 27](<2011-conlon-bounds-graph-regularity-removal_images/imageFile27.png>)

Then for every sequence λ = (λ1,... ,λM) of nonnegative real numbers which are not all zero with ||λ||2 = σ||λ||1, there are at least τm values of i for which min(ai,bi) > α||λ||1, where ai = j∈A

λj and bi = j∈B

i

λj.

i

Proof: Note that by multiplying each λj by 1/||λ||1, we may assume without loss of generality that ||λ||1 = 1. For distinct j,j′ ∈ [M], let (j,j′)i denote that j and j′ lie in diﬀerent sets in the partition (Ai,Bi). Since for any distinct j,j′ ∈ [M], the number of i for which (j,j′)i holds is at least (21 −µ)m, we have

![image 28](<2011-conlon-bounds-graph-regularity-removal_images/imageFile28.png>)

- 1

![image 29](<2011-conlon-bounds-graph-regularity-removal_images/imageFile29.png>)

- 2 − µ)m j


λjλj′ ≥ (

(j,j′)i

- 1

![image 30](<2011-conlon-bounds-graph-regularity-removal_images/imageFile30.png>)

- 2 − µ)m(1 − σ2), (3)


- 1

![image 31](<2011-conlon-bounds-graph-regularity-removal_images/imageFile31.png>)

- 2 − µ)m(||λ||1 − ||λ||22) = (


λj(1 − λj) = (

where the sum is over all ordered triples (j,j′,i) with j,j′ distinct and j and j′ lie in diﬀerent sets in the partition (Ai,Bi). We have the identity

λjλj′ = 2

(j,j′)i

i

aibi.

Since ai +bi = 1, we have aibi ≤ 1/4 and if min(ai,bi) ≤ α, then aibi ≤ α(1 −α). So if min(ai,bi) ≤ α for all but less than τm values of i, then

τ 2

λjλj′ <

m + 2(1 − τ)mα(1 − α).

![image 32](<2011-conlon-bounds-graph-regularity-removal_images/imageFile32.png>)

(j,j′)i

Comparing with (3) and dividing by m, this contradicts the supposition, and completes the proof. ✷ As usual, G(n,p) denotes the random graph on n vertices chosen by picking each pair of vertices as an edge randomly and independently with probability p. We ﬁnish this section with a few standard lemmas on the edge distribution in G(n,p).

- Lemma 2.4 In G(n,p), with probability at least 1 − n−2, every pair of disjoint vertex subsets U1 and U2 satisfy

|e(U1,U2) − pu1u2| ≤

√g, (4) where u1 = |U1|, u2 = |U2| and, for u1 ≤ u2, g = g(u1,u2) = 2u1u22 ln neu

![image 33](<2011-conlon-bounds-graph-regularity-removal_images/imageFile33.png>)

![image 34](<2011-conlon-bounds-graph-regularity-removal_images/imageFile34.png>)

2

.

Proof: For ﬁxed sets U1 and U2, the quantity e(U1,U2) is a binomial distributed random variable with parameters u1u2 and p. By (1), we have that the probability (4) does not hold is less than

- 2e−2g/(u1u2). By the union bound, the probability that there are disjoint sets U1 and U2 for which (4) does not hold is at most


n

u2=1

u2

u1=1

n u2

n − u2 u1

2e−2g/(u1u2) ≤

n

u2=1

u2

u1=1

ne u2

![image 35](<2011-conlon-bounds-graph-regularity-removal_images/imageFile35.png>)

u2 ne u1

![image 36](<2011-conlon-bounds-graph-regularity-removal_images/imageFile36.png>)

u1

2e−2g/(u1u2)

≤

n

u2=1

u2

u1=1

2

ne u2

![image 37](<2011-conlon-bounds-graph-regularity-removal_images/imageFile37.png>)

−2u2

≤ n−2.

The result follows. ✷

- Lemma 2.5 In G(n,p), with probability at least 1 − n−2, every vertex subset U satisﬁes


u 2 | ≤

√g, (5)

|e(U) − p

![image 38](<2011-conlon-bounds-graph-regularity-removal_images/imageFile38.png>)

where u = |U| and g = g(u) = 12u3 ln neu .

![image 39](<2011-conlon-bounds-graph-regularity-removal_images/imageFile39.png>)

![image 40](<2011-conlon-bounds-graph-regularity-removal_images/imageFile40.png>)

Proof: For ﬁxed U, the quantity e(U) is a binomially distributed random variable with parameters

- 2 and p. By (1), we have that the probability (5) does not hold is less than 2e−2g/(u2). By the union


- u


bound, the probability that there is a vertex subset U for which (5) does not hold is at most

n

u=2

n u

n

2e−2g/(u2) ≤

u=2

ne u

![image 41](<2011-conlon-bounds-graph-regularity-removal_images/imageFile41.png>)

n

u

2e−2g/(u2) ≤ 2

u=2

ne u

![image 42](<2011-conlon-bounds-graph-regularity-removal_images/imageFile42.png>)

−(u+1)

≤ n−2.

✷

Combining the estimates from the previous two lemmas, we can bound the probability in G(n,p) that there are two not necessarily disjoint subsets with large edge discrepancy between them.

- Lemma 2.6 In G(n,p), the probability that there are integers u1 and u2 with u1 ≤ u2 and not necessarily disjoint vertex subsets U1 and U2 with |U1| = u1 and |U2| = u2 such that


√

![image 43](<2011-conlon-bounds-graph-regularity-removal_images/imageFile43.png>)

h, (6)

|e(U1,U2) − pu1u2| > 5

where h = h(u1,u2) = u1u22 ln neu

, is at most 2n−2.

![image 44](<2011-conlon-bounds-graph-regularity-removal_images/imageFile44.png>)

2

Proof: For sets U1 and U2, letting U1′ = U1 \ U2, U2′ = U2 \ U1, and U = U1 ∩ U2, we have

e(U1,U2) = e(U1′,U2) + 2e(U) + e(U,U2′). We have that the bounds in Lemmas 2.4 and 2.5 hold with probability at least 1−2n−2. Hence, using the triangle inequality, and |U1′| ≤ u1, |U| ≤ u1, |U2′| ≤ u2, we have

√

![image 45](<2011-conlon-bounds-graph-regularity-removal_images/imageFile45.png>)

![image 46](<2011-conlon-bounds-graph-regularity-removal_images/imageFile46.png>)

![image 47](<2011-conlon-bounds-graph-regularity-removal_images/imageFile47.png>)

|e(U1,U2) − pu1u2| ≤ 2 g(u1,u2) + 2 g(u1) + pu1 ≤ 5

h

with probability at least 1 − 2n−2. Here the extra pu1 factor comes from the fact that degenerate edges are not counted in e(U). ✷

# 3 A general graph construction

In this section, we will deﬁne a nonuniform random graph G = (V,E) which, assuming certain estimates, has the property that any suﬃciently regular partition of its vertex set is close to being a reﬁnement of a particular partition of G into many parts. As this particular partition has many parts, this will imply that any suﬃciently regular partition will have many parts. After deﬁning G, we will prove that certain useful estimates on the edge distribution of G hold with positive probability. We will use these estimates to show that G has the desired property.

## 3.1 Deﬁning graph G

Following Gowers [22], we attempt to reverse engineer the proof of Szemere´di’s regularity lemma to show that the upper bound is essentially best possible. The proof of the regularity lemma follows a sequence of reﬁnements of the vertex set of the graph until we arrive at a regular partition, with the number of parts in each partition exponentially larger than in the previous partition. We build a sequence of partitions of the vertex set, and then describe how the edges of G are distributed between the various parts of the partition. To show that any (suﬃciently) regular partition Z of V (G) requires many parts, we show that Z is roughly a reﬁnement of the partitions we constructed in deﬁning G.

Let m1 ≥ 2200 be a positive integer and ρ = 2−20. For 2 ≤ i ≤ s, let mi = mi−1ai−1, where ai−1 = 2⌊ρm

9/10

i−1 ⌋. Suppose pi ≥ mi−1/10 for 1 ≤ i ≤ s − 1. The vertex set V has a sequence of equitable partitions P1,... ,Ps, where Pj is a reﬁnement of Pi for

- j > i deﬁned as follows. The number of parts of Pi is mi. For each set X in partition Pi, we pick


an equitable partition of X into ai parts, and let Pi+1 be the partition of V with mi+1 = miai parts consisting of the union of these partitions of parts of Pi.

For 1 ≤ i ≤ s − 1, let Gi be a uniform random graph on Pi with edge probability pi. That is, the vertices of the graph are the mi pieces of the partition and we place edges independently with probability pi. In practice, we will make certain speciﬁc assumptions about the edge distribution of Gi but these will hold with high probability in a random graph. For example, we shall assume that every vertex in Gi has degree at least pimi/2.

For each X,Y ∈ Pi with (X,Y ) an edge of Gi, we have an equitable partition QXY : X = XY1 ∪ XY2 into two parts, where XYj is a union of some of the parts in Pi+1 for j = 1,2. For each X ∈ Pi, we shall choose the partitions QXY with Y adjacent to X in Gi to satisfy the properties of Corollary 2.1 with µ = 2ρ1/2 = 2−9. Note that this is possible since we are taking M = ai and m ≥ pimi/2 ≥ m9i/10/2, so m ≥ 2µ−2 log M, as required. We ﬁnish the construction of G by deﬁning which pairs of vertices are adjacent. Vertices u,v ∈ V are adjacent in G if there is i, 1 ≤ i ≤ s − 1, an edge (X,Y ) of Gi, and j ∈ {1,2} with u ∈ XYj ,v ∈ YXj . An equivalent way of deﬁning the graph G is as follows. For 1 ≤ j < i, let Gj,i denote the graph with vertex set Pi, where X,Y ∈ Pi is an edge of Gj,i if there are X′,Y ′ ∈ Pj that are adjacent in Gj, and d ∈ {1,2} with X ⊂ XY′d′ and Y ⊂ YX′d′. For 1 < i ≤ s, let Gi denote the graph on Pi whose edge set is the union of the edge sets of G1,i,... ,Gi−1,i. Finally, two vertices u,v ∈ V are adjacent in G if there is an edge (X,Y ) of Gs with u ∈ X and v ∈ Y . Note that G1 is simply the empty graph on P1. We say that a subset Z β-overlaps another set X if |X ∩ Z| ≥ β|Z|, that is, if a β-fraction of Z is in

- X. A set Z is β-contained in a partition P of V if there is a set X ∈ P such that Z β-overlaps X. An equitable partition Z of V is a (β,υ)-reﬁnement of a partition P of V if, for at least (1 − υ)|Z| sets Z ∈ Z, the set Z is (1 − β)-contained in P. In particular, when β = υ = 0, this notion agrees with the standard notion of reﬁnement. That is, Z is a reﬁnement of P is equivalent to Z being a (0,0)-reﬁnement of P. Our main result, from which Theorem 1.1 easily follows, now says that for an appropriate choice of


pi, every regular partition of G must be close to a reﬁnement of Ps−1. In the proof of Theorem 1.1, Theorem 3.1 will be used only in the case a = s − 1. However, for the lower bound on the strong regularity lemma in Theorem 1.2, we will need to apply Theorem 3.1 for various values of a. This is why the parameter a is introduced.

- Theorem 3.1 Let ν = 3 i s=1−1 pi, and suppose pi > 210ηm21 for 1 ≤ i ≤ a, 1 − 27ν > ǫ, β = 20m−1 3/2, δ < β/4, and υ = 5m1−1/2. With positive probability, the random graph G has the following property. Every (ǫ,δ,η)-regular equitable partition of G is a (β,υ)-reﬁnement of Pa.


## 3.2 Edge distribution in G

Having deﬁned the (random) graph G, we now show that with positive probability G satisﬁes certain properties (see Lemma 3.11) concerning its edge distribution which we will use to prove Theorem 1.1. Note that G is determined by the Gi. For some of the desired properties, it will be enough to show

that the edges in each Gi are suﬃciently uniform. For other properties, we will need to consider how the edge distribution between the various Gi interact with each other. In bounding the probabilities of certain events, we will often consider the probability of the event given Gi is picked at random conditioned on the event that Gj with j < i are already chosen.

In the random graph G(n,p) on n vertices with each edge taken with probability p independently of the other edges, the expected degree of each vertex is p(n−1), and the following simple lemma shows that with high probability no vertex will have degree which deviates much from this quantity. We will assume throughout this subsection that n ≥ m1 ≥ 2200.

- Lemma 3.1 The probability that in the random graph G(n,p) there is a vertex v whose degree satisﬁes |deg(v) − pn| > n3/4 is at most e−n1/2.

Proof: For a ﬁxed vertex v, its degree deg(v) follows a binomial distribution with parameters n − 1 and p. Note that if |deg(v)−pn| > n3/4 then also |deg(v)−p(n−1)| > n3/4−1. From the Chernoﬀ-type estimate (1), we get that the probability |deg(v)−pn| > n3/4 is at most 2e−2(n3/4−1)2/(n−1) ≤ n1e−n1/2. As there are n vertices, from the union bound, we get the probability that there is a vertex v with |deg(v) − pn| > n3/4 is at most e−n1/2. ✷

![image 48](<2011-conlon-bounds-graph-regularity-removal_images/imageFile48.png>)

For X ∈ Pi, we will use N(X) to denote the neighborhood of X in graph Gi, that is, the set of Y ∈ Pi such that (X,Y ) is an edge of Gi. We have the following corollary of Lemma 3.1.

Corollary 3.1 Let E1 be the event that there is i, 1 ≤ i ≤ s−1, such that Gi has a vertex X with degree |N(X)| satisfying ||N(X)| − pimi| > m3i/4. The probability of event E1 is at most π1 := i s=1−1 e−m

1/2

i .

- Lemma 3.2 Suppose ν = 3 i s=1−1 pi ≤ 1/2. For 2 ≤ i ≤ s − 1, let E2i be the event that Gi has less than 14pim2i edges which are not edges of Gi. Let E2 be the event that none of the events E2i,


![image 49](<2011-conlon-bounds-graph-regularity-removal_images/imageFile49.png>)

- 2 ≤ i ≤ s − 1, occurs. The probability π2 of event E2 is at most π1 + i s=2−1 e−p2im2i/24, where π1 is deﬁned in Corollary 3.1.


Proof: If event E1 does not occur, given ν ≤ 1/2, then the number of edges of Gi is at most

pj + m−j 1/4

 

- i−1
- j=1


ν 4

m2i/2 ≤

m2i ≤ m2i/8.

![image 50](<2011-conlon-bounds-graph-regularity-removal_images/imageFile50.png>)

Each of the remaining at least m2i − 81m2i ≥ m2i/3 unordered pairs of parts of Pi has probabilty pi of being an edge of Gi, independently of each other. The expected number of edges of Gi which are not edges of Gi is therefore at least pim

![image 51](<2011-conlon-bounds-graph-regularity-removal_images/imageFile51.png>)

- 2 i

![image 52](<2011-conlon-bounds-graph-regularity-removal_images/imageFile52.png>)

- 3 = pim


2 i

2 i

4 + pim

12 . By (1), the probability of event E2i given the number of edges of Gi is at most m2i/8 is at most e−2(pim2i/12)2/(m2i/3) = e−p2im2i/24. Summing over all i, the probability of event E2 given E1 does not occur is at most i s=2−1 e−p2im2i/24. We thus have that the probability of E2 is at most π2. ✷

![image 53](<2011-conlon-bounds-graph-regularity-removal_images/imageFile53.png>)

![image 54](<2011-conlon-bounds-graph-regularity-removal_images/imageFile54.png>)

In a graph G with vertex subsets U,W, we let dG(U,W) denote the fraction of pairs in U × W which are edges of G. If U = {u} consists of a single vertex u, we let dG(u,W) = dG(U,W). If the underlying graph G is clear, we will sometimes write d(U,W) for dG(U,W). The following lemma shows that there is a low probability that the density between a vertex and certain vertex subsets is large.

- Lemma 3.3 Let E3 be the event that there is i, 1 ≤ i ≤ s −2, and distinct X,Y ∈ Pi, d ∈ {1,2}, and

v ∈ XY3−d, such that (X,Y ) is an edge of Gi but not an edge of Gi, and dG(v,YXd) > ν. The probability of event E3 is at most π3 := i s=1−2 j s=−i1+1 mimje−4p2jmj/mi.

Proof: If (X,Y ) is an edge of Gi but not an edge of Gi, then none of the edges of G between XY3−d and YXd come from the edges of any Gj with j ≤ i. So for event E3 to occur, there must be 1 ≤ i < j ≤ s − 1, X,Y ∈ Pi with (X,Y ) an edge of Gi, and X′ ∈ Pj with X′ ⊂ XY3−d, such that dGj(X′,Y ∗) > 3pj, where Y ∗ denotes the set of Y ′ ∈ Pj with Y ′ ⊂ YXd.

Fix for now i, 1 ≤ i ≤ s − 2, and j with i + 1 ≤ j ≤ s − 1. Fix also an edge (X,Y ) of Gi which is not an edge of Gi and d ∈ {1,2}. Fix a set X′ ∈ Pj with X′ ⊂ XY3−d and as before let Y ∗ denote the set of all Y ′ ∈ Pj with Y ′ ⊂ YXd. The probability that dGj(X′,Y ∗) > 3pj is by (1) at most e−2(2pj|Y∗|)2/|Y ∗| = e−4p2jmj/mi, since |Y ∗| = 2mmj

![image 55](<2011-conlon-bounds-graph-regularity-removal_images/imageFile55.png>)

i

. Summing over all possible choices of i, j, (X,Y ), d, and X′ ∈ Pj with X′ ⊂ XY3−d, by the union bound we have the probability of event E3 is at most

s−2

i=1

s−1

j=i+1

2m2i ·

mj 2mi

![image 56](<2011-conlon-bounds-graph-regularity-removal_images/imageFile56.png>)

e−4p2jmj/mi = π3.

✷

Note that the condition that (X,Y ) is an edge of Gi but not of Gi is necessary, since it guarantees that none of the edges in Gj with j ≤ i contributes to the edges between XY3−d and YXd in G. If (X,Y ) was an edge of Gi, then we would have a complete bipartite graph between X and Y and hence dG(v,YXd) = 1.

The codegree codeg(u,v) of two vertices u and v is the number of vertices w which are connected to both u and v. A second useful fact about G(n,p) is that with high probability the codegree of any two vertices u and v is roughly p2n.

- Lemma 3.4 The probability that in the random graph G(n,p) there are distinct vertices u and v with |codeg(u,v) − p2n| > n3/4 is at most e−n1/2.


Proof: For ﬁxed distinct vertices u and v, the codegree codeg(u,v) is binomially distributed with parameters n − 2 and p2. Note that if |codeg(u,v) − p2n| > n3/4 then |codeg(u,v) − p2(n − 2)| > n3/4 − 2. By Chernoﬀ’s inequality (1), the probability that |codeg(u,v) − p2n| > n3/4 is at most

- 2e−2(n3/4−2)2/(n−2) ≤ n−2e−n1/2. Using the union bound over all n2 choices of u and v yields the result. ✷ We have the following corollary of Lemma 3.4.


- Corollary 3.2 Let E4 be the event that there is i, 1 ≤ i ≤ s − 1, such that Gi has vertices X,Y ∈ Pi


with codegree satisfying |codeg(X,Y ) − p2imi| > m3i/4. The probability of event E4 is at most π4 = s−1 i=1 e−m

1/2

i .

- For X ∈ Pi, let U(X) = Y∈N(X) Y . The following three lemmas will be used to prove Lemma 3.8, which bounds the probability that there is i, 1 ≤ i ≤ s − 1, X ∈ Pi, and a vertex v  ∈ X such that dG(v,U(X)) > ν. The proof, which puts together the next three lemmas, makes sure that it is unlikely that any Gj contributes too much to the density between v and U(X).


- Lemma 3.5 Fix 1 ≤ i < s. The probability that there is a pair of distinct sets X,Y ∈ Pi which satisfy

dGi(Y,N(X)) > 2pi is at most π5i := 2e−m

1/2

i .

Proof: From Lemma 3.1, we know that |N(X)| ≥ pimi − m3i/4 ≥ 3pimi/4 for all X ∈ Pi with probability at least 1 − e−m

1/2

i . Also, by Lemma 3.4, we have codeg(X,Y ) ≤ p2i mi + m3i/4 ≤ 3p2imi/2 for all distinct X,Y ∈ Pi in graph Gi with probability at least 1−e−m

1/2

i . The number of edges between

Y and N(X) in Gi is just the codegree codeg(X,Y ) of X and Y in Gi. Therefore, dGi(Y,N(X)) = codeg(X,Y )/|N(X)|. Hence, with probability at least 1 − 2e−m

1/2

i , we have

dGi(Y,N(X)) =

codeg(X,Y ) |N(X)|

![image 57](<2011-conlon-bounds-graph-regularity-removal_images/imageFile57.png>)

≤

3p2imi/2 3pimi/4

![image 58](<2011-conlon-bounds-graph-regularity-removal_images/imageFile58.png>)

= 2pi.

✷

- Lemma 3.6 Fix 1 < i < s. Suppose every vertex of Gi has degree at most νimi/2, where νi =


- 3 j<i pj. The probability that there is a pair of distinct sets X,Y ∈ Pi which satisfy dGi(Y,N(X)) > νi


1/2

i + m2i e−νip2imi/4.

is at most π5′i := e−m

Proof: Note that Gi is determined by G1,... ,Gi−1. We show that, conditioning on Gi has maximum degree at most νimi/2, the random graph Gi is such that the probability that there are distinct sets X,Y ∈ Pi which satisfy dGi(Y,N(X)) > νi is at most e−m

1/2

i + m2i e−νip2imi/4.

Fix for now X,Y ∈ Pi. Let U be the neighborhood of Y in Gi. By assumption |U| ≤ νimi/2. The expectation of |N(X) ∩ U| is at most piνimi/2. The probability that |N(X) ∩ U| > 3piνimi/4 is by (1) at most

e−2(piνimi/4)2/|U| ≤ e−2(νipimi/4)2/(νimi/2) = e−νip2imi/4. By Lemma 3.1, we know that |N(X)| ≥ 3pimi/4 for all X ∈ Pi with probability at least 1 − e−m

1/2

i . Therefore, using the union bound, with probability at least

1/2 i

− m2i e−νip2imi/4, we have

1 − e−m

dGi(Y,N(X)) = |N(X) ∩ U| |N(X)|

(3νipimi/4) (3pimi/4)

= νi, for all X,Y ∈ Pi. ✷

≤

![image 59](<2011-conlon-bounds-graph-regularity-removal_images/imageFile59.png>)

![image 60](<2011-conlon-bounds-graph-regularity-removal_images/imageFile60.png>)

### Lemma 3.7 Fix 1 ≤ i < j < s. Suppose every vertex of Gi has degree at least pimi/2. Let E be the event that there is a set X ∈ Pi and a set Y ∈ Pj with Y  ⊂ X with more than 2pj|N(X)|mmj

neighbors

![image 61](<2011-conlon-bounds-graph-regularity-removal_images/imageFile61.png>)

i

- Y ′ in Gj with Y ′ ⊂ U(X). The probability of event E is at most π5ij := mimje−p2jpimj.


Proof: The number of Y ′ ∈ Pj with Y ′ ⊂ U(X) is |N(X)|mmji . The probability that a given Y has at least 2pj|N(X)|mmji neighbors Y ′ in Gj with Y ′ ⊂ U(X) is, by (1), at most

![image 62](<2011-conlon-bounds-graph-regularity-removal_images/imageFile62.png>)

![image 63](<2011-conlon-bounds-graph-regularity-removal_images/imageFile63.png>)

2

/ |N(X)|mmj

mj mi

2 j|N(X)|mmj

e−2 pj|N(X)|

i = e−2p

![image 64](<2011-conlon-bounds-graph-regularity-removal_images/imageFile64.png>)

![image 65](<2011-conlon-bounds-graph-regularity-removal_images/imageFile65.png>)

![image 66](<2011-conlon-bounds-graph-regularity-removal_images/imageFile66.png>)

i .

As there are at most mjmi such pairs X,Y , we have by the union bound, the probability of event E is at most

2 j|N(X)|mmj

mimje−2p

i ≤ mimje−p2jpimj.

![image 67](<2011-conlon-bounds-graph-regularity-removal_images/imageFile67.png>)

✷ From the previous three lemmas, we get the next lemma.

### Lemma 3.8 Consider the event E5 that there is i, 1 ≤ i ≤ s − 1, X ∈ Pi, and vertex v  ∈ X with dG(v,U(X)) > ν. The probability of event E5 is at most π5 := π1+ i s=1−1 π5i+ i s=2−1 π5′i+ 1≤i<j<s π5ij.

Proof: We look at edges in G between U(X) and Y for X ∈ Pi and Y ∈ Pj, distinguishing three diﬀerent cases, namely j = i, j < i and j > i. For event E5 to occur at least one of the following events occurs:

- • There is 1 ≤ i < s and distinct sets X,Y ∈ Pi with dGi(Y,N(X)) > 3pi.
- • There is 1 < i < s and distinct sets X,Y ∈ Pi which satisfy dGi(Y,N(X)) > νi = j<i 3pj.
- • There is 1 ≤ i < j < s and sets X ∈ Pi and Y ∈ Pj with Y  ⊂ X with dGj(Y,U(X)) > 3pj.


The ﬁrst case is covered by Lemma 3.5, the second by Lemma 3.6 and the third by Lemma 3.7. For Lemmas 3.6 and 3.7 to be applicable, it is enough to know also that for any i and any X ∈ Pi, |N(X) − pimi| ≤ mi3/4 ≤ pimi/4. But this is just the event that E1 does not occur. From Corollary 3.1, we know this holds with probability at least 1 − π1.

Therefore, putting everything together, the probability of event E5 is at most

π1 +

s−1

s−1

π5′i +

π5ij.

π5i +

i=2

i=1

1≤i<j<s

✷

### Lemma 3.9 Fix 1 < i ≤ s − 1. Let E6,i be the event that there is X ∈ Pi such that X has more than ν|N(X)| neighbors Y in Gi with Y ∈ N(X). Let E6 be the event that at least one of the events E6,i occurs for 1 < i ≤ s − 1. Then, the probability of event E6 is at most π6 := π1 + i s=2−1 mie−3ν2pimi/8.

Proof: Let us assume that event E1 does not occur. Then every vertex in Gi has degree at least

- 3

![image 68](<2011-conlon-bounds-graph-regularity-removal_images/imageFile68.png>)

- 4pimi. Moreover, for every X ∈ Pi, its number of neighbors in Gi is at most 


pj + m−j 1/4

- i−1
- j=1


- 1

![image 69](<2011-conlon-bounds-graph-regularity-removal_images/imageFile69.png>)

- 2


5 12

νmi ≤

ν(mi − 1).

mi ≤

![image 70](<2011-conlon-bounds-graph-regularity-removal_images/imageFile70.png>)



Furthermore, the graphs Gi and Gi are still independently chosen given the degree conditions imposed on them by E1 not occuring. Fix for now X ∈ Pi. Then, the expected fraction of elements of N(X) which are neighbors of X in Gi is at most ν/2. Therefore, given |N(X)|, the probability that the number of neighbors of X in Gi is more than ν|N(X)| is, by (1) and the fact that a hypergeometric distribution is at least as concentrated as the corresponding binomial distribution, at most e−2(ν|N(X)|/2)2/|N(X)| = e−ν2|N(X)|/2. By the union bound and the assumption that the degree of X in Gi is at least 34pimi, the probability of event E6,i given that E1 does not occur is at most mie−3ν2pimi/8. Therefore, adding over all i, we get that the probability of event E6 is at most π1 + i s=2−1 mie−3ν2pimi/8 = π6, as required. ✷

![image 71](<2011-conlon-bounds-graph-regularity-removal_images/imageFile71.png>)

- Lemma 3.10 Let E7 be the event that there is i, 1 ≤ i ≤ s − 1, and vertex subsets U1,U2 ⊂ Pi of Gi with |U1| = u1, |U2| = u2, and u1 ≤ u2 such that

|e(U1,U2) − piu1u2| > 5

√

![image 72](<2011-conlon-bounds-graph-regularity-removal_images/imageFile72.png>)

h, (7)

where h = h(u1,u2) = u1u22 ln muie

![image 73](<2011-conlon-bounds-graph-regularity-removal_images/imageFile73.png>)

2

. The probability of event E7 is at most π7 := i s=1−1 2m−i 2.

Proof: By Lemma 2.6, for each i, the probability that there are subsets U1,U2 ⊂ Pi such that (7) fails is at most 2m−i 2. By the union bound, the probability of event E7 is at most i s=1−1 2mi−2. ✷ We gather the previous lemmas into one result, which shows that with positive probability the edge distribution of G has certain desirable properties.

- Lemma 3.11 Suppose ν = 3 i s=1−1 pi ≤ 1/2. With probability at least 1/2, the graph G has the following properties for all i, 1 ≤ i ≤ s − 1.


- • The degree of every vertex in graph Gi diﬀers from pimi by at most m3i/4 and the codegree of every pair of distinct vertices diﬀers from p2imi by at most m3i/4.
- • The number of edges of Gi not in Gi is at least pim2i/4.
- • For all X ∈ Pi and vertex v  ∈ X, we have dG(v,U(X)) ≤ ν.
- • For all distinct X,Y ∈ Pi, d ∈ {1,2}, and v ∈ XY3−d, such that (X,Y ) is an edge of Gi but X and Y are not adjacent in Gi, we have dG(v,YXd) ≤ ν.
- • For all X ∈ Pi, X has at most ν|N(X)| neighbors Y in Gi with Y ∈ N(X).


- • For all vertex subsets U1,U2 ⊂ Pi of graph Gi with |U1| = u1, |U2| = u2, and u1 ≤ u2,


√

![image 74](<2011-conlon-bounds-graph-regularity-removal_images/imageFile74.png>)

|e(U1,U2) − piu1u2| ≤ 5

h, where h = h(u1,u2) = u1u22 ln muie

.

![image 75](<2011-conlon-bounds-graph-regularity-removal_images/imageFile75.png>)

2

Proof: By Corollaries 3.1, 3.2 and Lemmas 3.2, 3.3, 3.8, 3.9, 3.10 and the union bound, the probability that at least one Eh, 1 ≤ h ≤ 7, occurs is at most 7h=1 Pr[Eh] ≤ 7h=1 πh. Using the estimates ρ = 2−20, m1 ≥ 2200, mr = mr−1ar−1 for 2 ≤ r ≤ s, where ar−1 = 2⌊ρm

9/10

r−1 ⌋, and pi ≥ m−i 1/10 for 1 ≤ r ≤ s − 1, it is easy to verify that each πh ≤ 1/14 and hence the probability that none of these events occur, i.e., G has the desired properties, is at least 1/2. ✷

For the rest of the proof of Theorem 3.1, we suppose that G has the properties described in Lemma

- 3.11.


## 3.3 Regular partitions are close to being reﬁnements

Let θ = m1−1/2, ζ = ω = 20θ, β = mζ

, and γ = 1 − ω. Suppose for contradiction that there is an equitable partition Z : V = Z1 ∪ ... ∪ Zk of the vertex set of G such that all but at most ηk2 ordered pairs (Zj,Zℓ) of parts are (ǫ,δ)-regular, but Z is not a (β,υ)-reﬁnement of Pa.

![image 76](<2011-conlon-bounds-graph-regularity-removal_images/imageFile76.png>)

1

The two main lemmas for the proof are Lemmas 3.14 and 3.15, which show that if Zj satisﬁes certain conditions, then there are at least θ−1ηk pairs (Zj,Zℓ) that are not (ǫ,δ)-regular. The rest of the proof, Theorem 3.2, shows that there are at least θk Zj which satisfy the conditions of Lemmas 3.14 or 3.15. Together, we get at least θ−1ηk · θk = ηk2 ordered pairs (Zj,Zℓ) which are not (ǫ,δ)-regular, which completes the proof.

- Since P1 is a partition into m1 parts, then, by the pigeonhole principle, each Zj is m1


-contained in P1. We call Zj ripe with respect to r if Zj is β-contained in Pr but not (1 − β)-contained in Pr. That is, Zj is ripe if there is X ∈ Pr containing a β-fraction of it but no X ∈ Pr containing a (1 − β)-fraction of it. Let ψ = 220β. We call Zj shattered with respect to r if Zj is (1−β)-contained in Pr, but at least a ψ-fraction of Zj is contained in subsets X ∩Zj with X ∈ Pr+1 and |X ∩Zj| < β|Zj|. The sense here is that Zj is shattered by the partition Pr+1 if Zj is almost completely contained in some X ∈ Pr but it is not well-covered by Pr+1.

![image 77](<2011-conlon-bounds-graph-regularity-removal_images/imageFile77.png>)

1

We say that a subset X ⊂ V (β,γ)-supports the partition Z if at least a γ-fraction of the elements of X are in sets Zj which β-overlap X. That is, a γ-fraction of the elements of X are in sets Zj for which |X ∩ Zj| ≥ β|Zj|.

- Lemma 3.12 Each of the m1 sets in the partition P1 (β,1 − βm1)-supports Z.


Proof: Let X ∈ P1. At most a β-fraction of V is in sets of the form X ∩ Zj with |X ∩ Zj| < β|Zj|. Hence, as |X| = |V |/m1, at most a βm1-fraction of X belongs to Zi which do not β-overlap X. ✷

Let Si denote the set of X ∈ Pi which (β,γ)-support Z. We will let κi = ||SPi|

i|. Let Wi denote the set

![image 78](<2011-conlon-bounds-graph-regularity-removal_images/imageFile78.png>)

- of X ∈ Pi for which |N(X) ∩ Si| ≤ κi|N(X)|/4.


- Lemma 3.13 For 1 ≤ i ≤ s − 1 with κi > 100p−i 2m−i 1 ln(mie), we have |Wi| ≤ 100p−i 2 ln(κi−1e).

Proof: In graph Gi, the number e(Wi,Si) of pairs in Wi × Si which are edges is at most κi/4 times the sum of the degrees of the vertices in Wi. Since, by Lemma 3.11, every vertex has degree at most 2pi|Pi| in Gi, we have e(Wi,Si) ≤ |Wi| · (κi/4) · 2pi|Pi| = pi|Si||Wi|/2. Hence, by Lemma 3.11,

pi|Si||Wi|/2 ≤ |e(Wi,Si) − pi|Wi||Si|| ≤ 5

√

![image 79](<2011-conlon-bounds-graph-regularity-removal_images/imageFile79.png>)

h,

where h = u1u22 ln muie

![image 80](<2011-conlon-bounds-graph-regularity-removal_images/imageFile80.png>)

2

, and u1 = min(|Wi|,|Si|) and u2 = max(|Wi|,|Si|). By squaring both sides, substituting u1u2 = |Wi||Si| and simplifying, we have u1 ≤ 100p−i 2 ln muie

![image 81](<2011-conlon-bounds-graph-regularity-removal_images/imageFile81.png>)

2

. If u1 = |Si| = κimi, then

κimi = u1 ≤ 100p−i 2 ln

mie

![image 82](<2011-conlon-bounds-graph-regularity-removal_images/imageFile82.png>)

u2 ≤ 100p−i 2 ln(mie), contradicting our assumption. Hence, u1 = |Wi|, and |Wi| ≤ 100p−i 2 ln(κ−i 1e). ✷ The following simple proposition demonstrates the hereditary nature of supporting sets.

Proposition 3.1 Suppose Y ∈ Pi is such that Y (β,γ)-supports the partition Z. Then, for each X ∈ Pi distinct from Y and d ∈ {1,2}, YXd (β/4,1/4)-supports the partition Z.

Proof: We will use the fact γ ≥ 7/8. The sum of |Zt ∩ YXd| over all Zt which β-overlap Y but do not β/4-overlap YXd is at most |Y |/4. Since Y (β,γ)-supports the partition, the sum of |Zt ∩ YXd| over all Zt which β/4-overlaps YXd is at least

|YXd| − (1 − γ)|Y | − |Y |/4 ≥ |Y |/8 = |YXd|/4. Hence YXd (β/4,1/4)-supports the partition Z. ✷ The following lemma shows that if Zj satisﬁes certain conditions, then there are many (at least θ−1ηk)

- Zℓ such that (Zj,Zℓ) is not (ǫ,δ)-regular.


- Lemma 3.14 Suppose X ∈ Pi \ Wi, κi = |Si|/|Pi| ≥ 1/2, Zj is shattered with respect to i, and Zj (1 − β)-overlaps X. There are at least θ−1ηk sets Zℓ ∈ Z for which (Zj,Zℓ) is not (ǫ,δ)-regular.


Proof: Since Zj is shattered with respect to i and Zj (1−β)-overlaps X, then |X ∩Zj| ≥ (1−β)|Zj|, but the sum of |X′ ∩ Zj| over all X′ ∈ Pi+1 with |X′ ∩ Zj| < β|Zj| is at least ψ|Zj|.

Let Zj′ = X ∩ Zj, so |Zj′| ≥ (1 − β)|Zj|. For each X′ ∈ Pi+1 with X′ ⊂ X and |X′ ∩ Zj| < β|Zj|, let λX′ = |X′ ∩Zj′|/|Zj|, so each λX′ < β, i.e., β > ||λ||∞. Also, ||λ||1 ≥ ψ −β follows from the facts that |X ∩ Zj| ≥ (1 − β)|Zj| and the sum of |X′ ∩ Zj| over all X′ ∈ Pi+1 with |X′ ∩ Zj| < β|Zj| is at least ψ|Zj|. Therefore,

2

||λ||∞ ||λ||1

β ψ − β

1 220 − 1

σ2 = ||λ||2 ||λ||1

< 2−19.

≤

<

=

![image 83](<2011-conlon-bounds-graph-regularity-removal_images/imageFile83.png>)

![image 84](<2011-conlon-bounds-graph-regularity-removal_images/imageFile84.png>)

![image 85](<2011-conlon-bounds-graph-regularity-removal_images/imageFile85.png>)

![image 86](<2011-conlon-bounds-graph-regularity-removal_images/imageFile86.png>)

- By Lemma 2.3 with α = 1/8, µ = 2ρ1/2 = 2−9, σ < 2−9, and τ = 1 − 2−5, we have that the number

of Y ∈ N(X) for which

|Zj ∩ XY1 |,|Zj ∩ XY2 | ≥ α||λ||1|Zj| ≥ α(ψ − β)|Zj| (8) is at least (1 − 2−5)|N(X)|, where N(X) is the neighborhood of X in graph Gi.

- By Lemma 3.11, the number of Y ∈ N(X) which are also adjacent to X in Gi is at most ν|N(X)|. Also, since X  ∈ Wi, we have |N(X)∩Si| ≥ κi|N(X)|/4. Therefore, the number of Y ∈ Si with (X,Y ) an edge of Gi but not an edge of Gi, and (8) is satisﬁed is at least


(1 − 2−5)|N(X)| − |N(X) \ Si| − ν|N(X)| > (κi/4 − 2−5 − ν)|N(X)| ≥ |N(X)|/16.

Fix such a Y , and let Ud = Zj ∩ XYd for d ∈ {1,2}, so |U1|,|U2| ≥ α(ψ − β)|Zj|. Since Y ∈ Si, we have Y (β,γ)-supports Z. By Proposition 3.1, YXd (β/4,1/4)-supports Z. By Lemma 3.11, for each vertex v ∈ XY3−d, we have d(v,YXd) ≤ ν. In particular, d(U3−d,YXd) ≤ ν. Let Rd be the union of all

- Zℓ ∩ YXd such that Zℓ β/4-overlaps YXd, so Rd is a subset of YXd of cardinality at least |YXd|/4. Hence, d(U3−d,Rd) ≤ 4ν.


For Zℓ which β/4-overlaps YXd, let Zℓ′ = Rd ∩Zℓ, so |Zℓ′| ≥ β|Zℓ|/4. We next show that there are many Zℓ′ which satisfy

d(U3−d,Zℓ′) ≤ 8ν. (9)

Indeed, the union of the Zℓ′ which do not satisfy (9) has cardinality at most 21|Rd|, so at least 1/2 of Rd consists of the union of Zℓ′ which satisfy (9). The number of ℓ which satisfy (9) is at least

![image 87](<2011-conlon-bounds-graph-regularity-removal_images/imageFile87.png>)

- 1

![image 88](<2011-conlon-bounds-graph-regularity-removal_images/imageFile88.png>)

- 2|Rd|/|Zℓ| ≥


=

- 1

![image 89](<2011-conlon-bounds-graph-regularity-removal_images/imageFile89.png>)

- 2


(|YXd|/4)/|Zℓ|

1 16|Y |/|Zℓ| =

1 16

k/mi,

![image 90](<2011-conlon-bounds-graph-regularity-removal_images/imageFile90.png>)

![image 91](<2011-conlon-bounds-graph-regularity-removal_images/imageFile91.png>)

where in the last equality we used |Y | = |V |/mi and |Zℓ| = |V |/k. For each Zℓ′ which satisﬁes (9), we have d(Ud,Zℓ′) = 1 since (X,Y ) is an edge of Gi and, therefore, the density of edges between XYd and YXd is 1. Hence

d(Ud,Zℓ′) − d(U3−d,Zℓ′) ≥ 1 − 8ν ≥ ǫ.

Since also |Ud|,|U3−d| ≥ α(ψ − β)|Zj| ≥ δ|Zj|, and |Zℓ′| ≥ β4|Zℓ| ≥ δ|Zℓ|, we have in this case (Zj,Zℓ) is not (ǫ,δ)-regular.

![image 92](<2011-conlon-bounds-graph-regularity-removal_images/imageFile92.png>)

Since the number of such Y is at least |N(X)|/16, we have that the number of pairs (Zℓ,YXd) such that Zℓ β/4-overlaps YXd and (Zj,Zℓ) is not (ǫ,δ)-regular is at least 16 1 k/mi (|N(X)|/16) ≥ 2−9pik, where we used |N(X)| ≥ 12pimi from Lemma 3.11. As Zℓ β/4-overlaps YXd in each such pair, a given

![image 93](<2011-conlon-bounds-graph-regularity-removal_images/imageFile93.png>)

![image 94](<2011-conlon-bounds-graph-regularity-removal_images/imageFile94.png>)

- Zℓ is in at most 4β−1 such pairs. Hence, the number of Zℓ for which (Zj,Zℓ) is not (ǫ,δ)-regular is at least 2−11βpik ≥ θ−1ηk. ✷


Like Lemma 3.14, the next lemma shows that if Zj satisﬁes certain conditions, then there are at least θ−1ηk Zℓ such that (Zj,Zℓ) is not (ǫ,δ)-regular.

- Lemma 3.15 Suppose X ∈ Pi\Wi, κi ≥ 1/2, Zj is ripe with respect to i, and Zj β-overlaps X. Then there are at least θ−1ηk sets Zℓ ∈ Z for which (Zj,Zℓ) is not (ǫ,δ)-regular.


Proof: Since Zj is ripe with respect to i, |X ∩ Zj| < (1 − β)|Zj|. Therefore, letting U′ = Zj \ X, we have |U′| ≥ β|Zj|. By Lemma 3.11, for each vertex v of G which is not in X, we have d(v,U(X)) ≤ ν. Since X  ∈ Wi, we have

|N(X) ∩ Si| ≥ κi|N(X)|/4 ≥ |N(X)|/8. (10) So

d(v,

Y ) ≤ 8ν. (11)

Y ∈N(X)∩Si

Fix for this paragraph Y ∈ N(X) ∩ Si. Since Zj β-overlaps X, there is d = d(j,Y ) ∈ {1,2} such that Zj β/2-overlaps XYd . Let UY = Zj ∩ XYd , so |UY | ≥ β2|Zj| and d(UY ,YXd) = 1. As Y ∈ Si, we have Y (β,γ)-supports Z. By Proposition 3.1, YXd (β/4,1/4)-supports Z.

![image 95](<2011-conlon-bounds-graph-regularity-removal_images/imageFile95.png>)

- For Y ∈ N(X)∩Si, let RY denote the set of vertices y which are in YXd with d = d(j,Y ), and y is also in a Zℓ which β/4-overlaps YXd, so


1 4|YXd| =

1 8|Y | = |V |

|RY | ≥

. (12)

![image 96](<2011-conlon-bounds-graph-regularity-removal_images/imageFile96.png>)

![image 97](<2011-conlon-bounds-graph-regularity-removal_images/imageFile97.png>)

![image 98](<2011-conlon-bounds-graph-regularity-removal_images/imageFile98.png>)

8mi

Let R = Y∈N(X)∩S

i

RY . We have

|V | 8mi ≥ 2−6|N(X)|

|V | mi ≥ 2−6

pimi 2 ·

|R| ≥ |N(X) ∩ Si|

![image 99](<2011-conlon-bounds-graph-regularity-removal_images/imageFile99.png>)

![image 100](<2011-conlon-bounds-graph-regularity-removal_images/imageFile100.png>)

![image 101](<2011-conlon-bounds-graph-regularity-removal_images/imageFile101.png>)

|V | mi

= 2−7pi|V |, (13)

![image 102](<2011-conlon-bounds-graph-regularity-removal_images/imageFile102.png>)

- where we used (12), (10), and |N(X)| ≥ pimi/2. By (11) and (12), we have for v  ∈ X,


d(v,R) ≤ 26ν. (14)

- By (14), we have d(U′,R) ≤ 26ν. For Zℓ which β/4-overlaps YXd for some Y ∈ N(X) ∩ Si and d = d(j,Y ), let ZℓY = Zℓ ∩ YXd, so |ZℓY | ≥ (β/4)|Zℓ|. By deﬁnition, for each Y ∈ N(X) ∩ Si, RY is the union of the sets ZℓY . We next show that there are many ZℓY which satisfy


d(U′,ZℓY ) ≤ 27ν. (15)

Indeed, the union of the ZℓY which do not satisfy (15) has cardinality at most 12|R|, so at least 1/2 of R consists of the union of ZℓY which satisfy (15). The number of pairs (ℓ,Y ) which satisfy (15) is at least

![image 103](<2011-conlon-bounds-graph-regularity-removal_images/imageFile103.png>)

- 1

![image 104](<2011-conlon-bounds-graph-regularity-removal_images/imageFile104.png>)

- 2|R|/|Zℓ| ≥


- 1

![image 105](<2011-conlon-bounds-graph-regularity-removal_images/imageFile105.png>)

- 2


2−7pi|V |/|Zℓ| = 2−8pik.

- where we used (13) and |Zℓ| = |V |/k. Since for each such ℓ, we have Zℓ β/4-overlaps YXd, each such ℓ is in at most 4β−1 of the pairs (ℓ,Y ) we just counted. Hence, the number of ℓ for which there is Y such that (15) holds is at least 2−10βpik.


- By (15) and d(UY ,ZℓY ) = 1, we have d(UY ,ZℓY ) − d(U′,ZℓY ) ≥ 1 − 27ν > ǫ,


and as |UY |,|U′| ≥ β2|Zj| ≥ δ|Zj| and |ZℓY | ≥ β4|Zℓ| ≥ δ|Zℓ|, we have that (Zj,Zℓ) is not (ǫ,δ)-regular for at least 2−10βpik ≥ θ−1ηk values of ℓ. ✷

![image 106](<2011-conlon-bounds-graph-regularity-removal_images/imageFile106.png>)

![image 107](<2011-conlon-bounds-graph-regularity-removal_images/imageFile107.png>)

The following theorem completes the proof.

- Theorem 3.2 The number of ordered pairs (Zj,Zℓ) which are not (ǫ,δ)-regular is at least ηk2.


Proof: By assumption, Z is not a (β,υ)-reﬁnement of Pa. Hence, the number of parts Zj of partition

- Z which are not (1 − β)-contained in Pa is at least υk. Let i0 be the minimum positive integer for which Pi0 is not a (β,υ)-reﬁnement of Z. As, by assumption, Pa is not a (β,υ)-reﬁnement of Z, we have 1 ≤ i0 ≤ a.


- Claim 3.1 We have κ1 = 1 and κi ≥ 1/2 for i < i0.


As β = ζ/m1, by Lemma 3.12, each of the m1 parts of partition P1 (β,1 − ζ)-supports Zj. As ζ = ω and γ = 1−ω, it follows that S1 = P1 and κ1 = |S1|/|P1| = 1. From the deﬁnition of i0, for each i < i0, Pi0 is a (β,υ)-reﬁnement of Z. Fix for this paragraph such an i < i0. Hence at most a (β +υ)-fraction of the vertices are in parts Zj ∩ X with X ∈ Pi and Zj ∈ Z and |Zj ∩ X| < (1 − β)|Zj|. In particular, as 1 − β > β and γ = 1 − ω, the fraction of X ∈ Pi which do not (β,γ)-support Z is at most β+ωυ. Hence κi ≥ 1 − β+ωυ ≥ 1/2, which completes the proof of Claim 3.1. Consider the partition Z = Z1 ∪ Z2 ∪ Z3 ∪ Z4 ∪ Z5 ∪ Z6, where Zj ∈ Zh if h is minimum such that Zj satisﬁes property h below.

![image 108](<2011-conlon-bounds-graph-regularity-removal_images/imageFile108.png>)

![image 109](<2011-conlon-bounds-graph-regularity-removal_images/imageFile109.png>)

- 1. There is i < i0 and X ∈ Pi \ Wi such that Zj is shattered with respect to i and (1 − β)-overlaps X or if Zj is ripe with respect to i and β-overlaps X,
- 2. For every X ∈ P1 such that Zj β-overlaps X, X ∈ W1.
- 3. There is i, 1 < i ≤ i0, and X ∈ Wi such that Zj β-overlaps X,
- 4. i0 > 1 and Zj is ripe with respect to i0, and there is X ∈ Wi0 such that Zj β-overlaps X.
- 5. Zj is ripe with respect to i0, and there is X ∈ Pi0 \ Wi0 such that Zj β-overlaps X.
- 6. Zj is (1 − β)-contained in Pi0.


It is not immediately obvious that the above six subfamilies of Z form a partition of Z, so we ﬁrst show that this is indeed the case.

- Claim 3.2 The above six subfamilies form a partition of Z.

As Zj ∈ Zh if and only h is the minimum such that Zj satisﬁes property h, the subfamilies Zh,

- 1 ≤ h ≤ 6, are pairwise disjoint. We thus need to show that each Zj is in at least one Zh. Suppose for contradiction that Zj is in none of the Zh. By property 6, Zj is not (1−β)-contained in Pi0. If Zj is β-contained in Pi0, then Zj is ripe with respect to i0, and there is X ∈ Pi0 such that Zj β-overlaps X. Either every such X ∈ Wi0 or there is such an X  ∈ Wi0, and by properties 2, 4 and 5, we must have in this case Zj is in a Zh for some h ≤ 5. So Zj is not β-contained in Pi0, and noting that every Zj is β-contained in P1, we must have Zj is ripe or shattered with respect to at least one i with
- 1 ≤ i < i0. In particular, there is i < i0 and X ∈ Pi such that Zj is shattered with respect to i and (1 − β)-overlaps X or Zj is ripe with respect to i and β-overlaps X. Since Zj  ∈ Z1, for every such i < i0 and X ∈ Pi, we must have X ∈ Wi. But then Zj ∈ Z2 or Z3. Thus Zj is in at least one of the six subfamilies, completing the claim that that these subfamilies indeed form a partition of Z. As the number of parts Zj of partition Z which are not (1−β)-contained in Pi0 is at least υk, we have


|Z \ Z6| ≥ υk. (16)

Let wi = |Wi|/|Pi|. By Claim 3.1, κ1 = 1 and κi ≥ 1/2 for i < i0. Hence, from Lemma 3.13, we have w1 ≤ 100p−1 2m−1 1 ln(2e) ≤ m1−1/2 and similarly w := 1<i<i

0

wi ≤ m−2 1/2. Here we used pi ≥ m−i 1/10, m1 ≥ 2200, and mi ≥ 2m

1/2

i−1. We next bound the size of Z2. If Zj ∈ Z2, since Zj does not β-overlap any X ∈ P1\W1, and |P1| = m1, then at least a (1 − βm1)-fraction of Zj is contained in sets X ∈ Wi. Hence, the fraction of Zj ∈ Z which satisfy Zj ∈ Z2 is at most (1 − βm1)−1w1 ≤ 2m−1 1/2, i.e., |Z2| ≤ (2m−1 1/2)k. Similarly, the fraction of Zj ∈ Z such that there is 1 < i < i0 and X ∈ Wi for which Zj β-overlaps X is at most β−1m2−1/2. Hence, |Z3| ≤ β−1m−2 1/2k. By Lemmas 3.14 and 3.15, each Zj ∈ Z1 is in at least θ−1ηk pairs (Zj,Zℓ) which are not (ǫ,δ)-regular. We are thus done if |Z1| ≥ θk. So we may suppose |Z1| < θk. We next give a lower bound on κi0.

- Claim 3.3 We have κi0 ≥ 1/2.


Note that if i0 = 1, by Claim 3.1, κ1 = 1. So we may suppose that i0 > 1. In order to give a lower bound on κi0, we next give an upper bound on the union of all sets Zj ∩ X with |Zj ∩ X| < β|Zj| and

- X ∈ Pi0. If Zj is not (1 − β)-contained in Pi0, then it must be shattered or ripe with respect to some i with i < i0, or must have at most ψ|Zj| vertices in parts X ∩ Zj with X ∈ Pi0 and |X ∩ Zj| < β|Zj|. Each Zj which is shattered or ripe with respect to some i with i < i0 is in Z1, Z2, or Z3, and hence the number of such Zj is at most


|Z1 ∪ Z2 ∪ Z3| ≤ θk + (2m−1 1/2)k + β−1m−2 1/2k. (17)

Every set Zj which (1 − β)-overlaps Pi0 has at most a β-fraction of it contained in sets X ∩ Zj with |X ∩Zj| < β|Zj| and X ∈ Pi0. In total, we get that the fraction of vertices which belong to one of the

sets X ∩ Zj with |X ∩ Zj| < β|Zj| and X ∈ Pi0 is at most θ + (2m−1 1/2) + β−1m−2 1/2 + β + ψ. The fraction of sets in Pi0 which do not (β,γ)-support Z is therefore

1 − κi0 ≤ ω−1 θ + (2m−1 1/2) + β−1m−2 1/2 + β + ψ ≤ 1/2. Hence, κi0 ≥ 1/2, which completes Claim 3.3. Noting that κi0 ≥ 1/2, the same argument that bounded |Z3| also gives that

|Z4| ≤ β−1m−2 1/2k. (18) From the bounds (16), (17), (18), we have

|Z5| ≥ |Z \ Z6| − |Z1 ∪ Z2 ∪ Z3| − |Z4| ≥ υk − θk + 2m−1 1/2k + β−1m−2 1/2k − β−1m−2 1/2k ≥ θk.

As κi0 ≥ 1/2, by Lemma 3.15, each Zj ∈ Z5 is in at least θ−1ηk pairs (Zj,Zℓ) which are not (ǫ,δ)regular. Hence, the number of irregular pairs is at least

|Z5|θ−1ηk ≥ ηk2, which completes the proof. ✷

- 3.4 Proof of Theorem 1.1 To prove Theorem 1.1, it suﬃces to prove the following theorem.


- Corollary 3.3 Let ǫ = 1/2, δ = 2−400, η < 2−700, s = ⌊2−600η−1⌋, and k be at most a tower of twos of height s. There is a graph G = (V,E) for which any equitable partition Z of V into at most k parts has at least ηk2 ordered pairs of parts which are not (ǫ,δ)-regular.


Proof: Let m1 = 2200 and pi = max(m−i 1/10,2500η) for 1 ≤ i ≤ s − 1 and consider the graph G given with positive probability by Theorem 3.1. As ν = 3 i s=1−1 pi, we have

ν ≤ 3

s−1

s−1

(mi−1/10 + 2500η) = 3 · 2500η(s − 1) + 3

i=1

i=1

3 2

m−i 1/10 ≤ 3 · 2−100 + 3

![image 110](<2011-conlon-bounds-graph-regularity-removal_images/imageFile110.png>)

p1 < 6p1 < 2−10,

so 1−27ν > ǫ. The ﬁrst inequality uses that the maximum of two nonnegative real numbers is at most their sum. The second inequality uses s = ⌊2−600η−1⌋ and the fact that the sum of m−i 1/10 rapidly converges, and p1 = m1−1/10 = 2−20. Note that as m1 = 2200 > 222

2

1/2

and mi ≥ 2m

i−1 for i > 1, we have |Pi| = mi is greater than a tower of twos of height i + 2 for 1 ≤ i ≤ s. By Theorem 3.1 with a = s − 1, any (ǫ,δ,η)-regular equitable partition of G is a (β,υ)-reﬁnement of Ps−1. In particular, at least one part of Ps−1 contains at least a (1 − β)-fraction of a part from Z. As 1 − β > 1/2, this implies |Z| ≥ 12|Ps−1| > k, which completes the proof. ✷

![image 111](<2011-conlon-bounds-graph-regularity-removal_images/imageFile111.png>)

# 4 Lower bound for the strong regularity lemma

In this section we prove Theorem 1.2, which gives a lower bound on the strong regularity lemma and states the following. Let 0 < ǫ < 2−100 and f : N → (0,1) be a decreasing function with f(1) ≤ 2−100ǫ6. Deﬁne Wℓ recursively by W1 = 1, Wℓ+1 = T 2−70ǫ5/f(Wℓ) , where T is the tower function deﬁned in the introduction. Let W = Wt−1 with t = 2−20ǫ−1. Then there is a graph G such that if equitable partitions A,B of the vertex set of G satisfy q(B) ≤ q(A)+ǫ and B is f(|A|)-regular, then |A|,|B| ≥ W. We next describe the proof of Theorem 1.2. In the ﬁrst subsection, we construct the graph G as a specialization of the construction in Theorem 3.1. The graph G we use to prove Theorem 1.2 has vertex partitions Pi,j with 1 ≤ i ≤ t, and 1 ≤ j ≤ hi satisfying Pi′,j′ is a reﬁnement of Pi,j if i′ = i and j′ > j or if i′ > i. Furthermore, as the number of parts in each successive reﬁnement is roughly exponential in the number of parts in the previous partition, we show in the ﬁrst subsection that |Pt−2,ht−2−2| ≥ W. The edges of G are deﬁned based on certain graphs Gi,j on Pi,j. In Subsection 4.3, we prove a lemma which implies that the construction has the property that

q(Pi,hi) > q(Pi,hi−2) + 2ǫ (19)

for each i < t. Let A and B be equitable partitions of the vertex set of G such that q(B) ≤ q(A) + ǫ and B is f(|A|)regular. Let M1 = 1 and Mℓ = |Pℓ−1,hℓ−1−2| for 1 < ℓ ≤ t − 1. Let r with 1 ≤ r ≤ t − 1 be maximum such that |A| ≥ Mr. Let P′ = Pr,hr−2 and P = Pr,hr. In Subsection 4.1, after deﬁning G, we show that it satisﬁes the hypothesis of Theorem 3.1, and conclude that, as B is an f(|A|)-regular partition of G and f is a decreasing function, it must be close to being a reﬁnement of P. It follows that if |A| ≥ Mt−1 = |Pt−2,ht−2−2| > W, then |B| > W as well, and we are done in this case. Thus we may assume |A| < Mt−1 and hence r ≤ t − 2. In Subsection 4.4 we prove

ǫ 2

q(A) < q(P′) +

. (20)

![image 112](<2011-conlon-bounds-graph-regularity-removal_images/imageFile112.png>)

This follows from a lemma that states that q(P′) is close to the maximum mean square density density over all partitions of the same number of parts as P′. In Subsection 4.2, we use the result that B is close to being a reﬁnement of P to conclude

q(P) ≤ q(B) +

ǫ 2

. (21)

![image 113](<2011-conlon-bounds-graph-regularity-removal_images/imageFile113.png>)

Putting the three estimates (19) (with i = r and noting in this case Pi,hi = P, Pi,hi−2 = P′), (20),

(21) together, we get that

ǫ 2

ǫ 2

> q(P′) + 2ǫ −

> q(A) + ǫ, contradicting the hypothesis of Theorem 1.2, and completing the proof of Theorem 1.2. ✷

q(B) ≥ q(P) −

![image 114](<2011-conlon-bounds-graph-regularity-removal_images/imageFile114.png>)

![image 115](<2011-conlon-bounds-graph-regularity-removal_images/imageFile115.png>)

## 4.1 Construction of G and proof that B is an approximate reﬁnement We will construct the graph G as a special case of the construction in Theorem 3.1.

Let t = 2−20ǫ−1. We have partitions Pℓ,j of the vertex set V for 1 ≤ ℓ ≤ t and 1 ≤ j ≤ hℓ, where hℓ is deﬁned later in the paragraph and Pℓ,j = Pi are the partitions used to construct G in Theorem 3.1 with i = j + d<ℓ hd. We set mℓ,j = |Pℓ,j| = |Pi| = mi, and pℓ,j = pi. As above, let M1 = 1 and

, and pℓ,j = max(m−ℓ,j1/10,230ǫ−4ǫℓ) for

- Mℓ = mℓ−1,hℓ−1−2 for 1 < ℓ ≤ t. Let ǫℓ = f(Mℓ), hℓ = 270ǫ5ǫ


![image 116](<2011-conlon-bounds-graph-regularity-removal_images/imageFile116.png>)

ℓ

- 1 ≤ j ≤ hℓ with j = hℓ − 1, and pℓ,hℓ−1 = max(m−ℓ,j1/10,230ǫ−4ǫℓ,210ǫ). Let m1 = 210ǫ−2, so m1 ≥ 2200. Note that, as each mℓ,j is exponential in a power of mℓ,j−1, we get that Mℓ is at least a tower of 2s of height hℓ. That is, Mℓ ≥ T 2−70ǫ5/f(Mℓ−1) . In particular, by induction, Mℓ ≥ Wℓ, where Wℓ is deﬁned earlier in this section. We will apply Theorem 3.1 to conclude the following corollary which states that any suﬃciently regular


partition of G is roughly a reﬁnement of a particular Pℓ,j. To accomplish this we need to show that the conditions of the theorem hold, which we postpone until after stating the following corollary. We ﬁx G to be a graph satisfying the properties of Lemma 3.11 so that if G also satisﬁes the conditions stated in Theorem 3.1, then it satisﬁes the conclusion of Theorem 3.1.

- Corollary 4.1 Let r ≤ t − 1 be the maximum positive integer for which |A| ≥ Mr, so f(|A|) ≤ f(Mr) = ǫr, and P = Pr,hr. The partition B, which is ǫr-regular, is a (β,υ)-reﬁnement of P with β = 20m−1 3/2 and υ = 5m1−1/2. Note that


hℓ

hℓ

t

t

s−1

m−ℓ,j1/10 + 230ǫ−4ǫℓ

pℓ,j ≤ 210ǫt +

pi =

ν = 3

j=1

j=1

i=1

ℓ=1

ℓ=1

hℓ

t

s−1

t

s−1

m−i 1/10 +

mi−1/10 +

2−40ǫ ≤ 2−9,

230ǫ−4ǫℓ ≤ 210ǫt +

≤ 210ǫt +

i=1

j=1

i=1

ℓ=1

ℓ=1

where we used that the maximum of a set of nonnegative numbers is at most their sum, and substituted in hℓ = 270ǫ5ǫ

9/10

, m1 = 210ǫ−2 ≥ 2200, mi+1 = miai ≥ mi2⌊2−20m

i ⌋, and t = 2−20ǫ−1. We thus have 1 − 27ν ≥ 1/2 ≥ ǫr. Notice if η = ǫr = f(Mr), then, for 1 ≤ i ≤ r and 1 ≤ j ≤ hi, we have

![image 117](<2011-conlon-bounds-graph-regularity-removal_images/imageFile117.png>)

ℓ

pi,j ≥ 230ǫ−4ǫi ≥ 230ǫ−4ǫr = 210ηm21,

where we used m1 = 210ǫ−2. Since β = 20m−1 3/2 = 20 · 2−15ǫ3 and f(1) ≤ 2−100ǫ6, we have δ = ǫr = f(Mr) ≤ f(M1) = f(1) < β/4.

By the above estimates, the conditions of Theorem 3.1 are satisﬁed, and Corollary 4.1 stated above indeed holds. ✷

Note that if r = t − 1 in Corollary 4.1, then |A| ≥ Mt−1 = |Pt−2,ht−2−2| > W, and B is a (β,υ)reﬁnement of P = Pr,hr. As 1 − β > 1/2, this implies |B| ≥ 12|Pr,hr| > W, which completes the proof of Theorem 1.2 in this case. We can therefore assume r < t − 1.

![image 118](<2011-conlon-bounds-graph-regularity-removal_images/imageFile118.png>)

## 4.2 Approximate reﬁnements and mean square density

From Corollary 4.1 and the following lemma, we deduce at the end of this subsection that if P is the partition in Corollary 4.1, then q(P) ≤ q(B) + 2ǫ.

![image 119](<2011-conlon-bounds-graph-regularity-removal_images/imageFile119.png>)

- Lemma 4.1 Suppose G is a graph, P is a vertex partition, and Q is an equitable partition which is a (β,υ)-reﬁnement of P. Then q(P) ≤ q(Q) + 2β + 12υ.


![image 120](<2011-conlon-bounds-graph-regularity-removal_images/imageFile120.png>)

Proof: Let Q′ be the common reﬁnement of P and Q, so q(Q′) ≥ q(P). Let X,Y ∈ Q be such that X,Y are each (1 − β)-contained in P. Let X = X1 ∪... ∪Xr be the partition of X consisting of parts from Q′ with |X1| ≥ (1−β)|X|, and Y = Y1 ∪...∪Ys be the partition of Y consisting of parts from Q′ with |Y1| ≥ (1 − β)|Y |. Let p = d(X1,Y1) and p′ = 1−p1

1q1 d(Xi,Yj)piqj, where pi = ||XXi||, qj = ||YYj|| and the sum is over all pairs (i,j) ∈ [r] × [s] except (i,j) = (1,1). That is, p′ is the weighted average edge density between the pairs of parts except (X1,Y1). We have

![image 121](<2011-conlon-bounds-graph-regularity-removal_images/imageFile121.png>)

![image 122](<2011-conlon-bounds-graph-regularity-removal_images/imageFile122.png>)

![image 123](<2011-conlon-bounds-graph-regularity-removal_images/imageFile123.png>)

s

r

d2(Xi,Yj)piqj ≤ p2p1q1 +

d(Xi,Yj)piqj = p1q1p2 + p′(1 − p1q1)

j=1

i=1

(i,j) =(1,1)

and

d(X,Y ) = pp1q1 + p′(1 − p1q1). Let ǫ = 1 − p1q1, so

r

s

d2(Xi,Yj)piqj − d2(X,Y ) ≤ (1 − ǫ)p2 + p′ǫ − p(1 − ǫ) + p′ǫ 2

i=1

j=1

= ǫ (1 − ǫ)p2 + p′ − 2pp′(1 − ǫ) − p′2ǫ ≤ ǫ (1 − ǫ)p2 + p′ − 2pp′(1 − ǫ) ≤ ǫ ≤ 2β.

The second to last inequality is by noting the right hand side of the third to last line is linear in p′ and must therefore be maximized when p′ = 0 or 1, and the last inequality follows from ǫ = 1 − p1q1 and p1,q1 ≥ 1 − β.

Now for parts X,Y ∈ Q that are not both (1 − β)-contained in P, again letting X = X1 ∪ ... ∪ Xr and Y = Y1 ∪ ... ∪ Ys be the partitions of X and Y consisting of parts from Q′, and letting q denote the edge density between X and Y , and pi = ||XXi||, qj = ||YYj||, we have

![image 124](<2011-conlon-bounds-graph-regularity-removal_images/imageFile124.png>)

![image 125](<2011-conlon-bounds-graph-regularity-removal_images/imageFile125.png>)

s

r

d2(Xi,Yj)piqj − d2(X,Y ) ≤ q − q2 ≤ 1/4.

j=1

i=1

- Since Q is a (β,υ)-reﬁnement of P, at most a 2υ-fraction of the pairs of parts from Q are such that not both parts are (1 − β)-contained in P. Putting together the estimates from the last two paragraphs, we therefore get


1 4 · 2υ.

q(P) ≤ q(Q′) ≤ q(Q) + 2β +

![image 126](<2011-conlon-bounds-graph-regularity-removal_images/imageFile126.png>)

✷

Noting that m1 = 210ǫ−2, β = 20m−1 3/2 < ǫ/8 and υ = 5m−1 1/2 ≤ ǫ/4 in Corollary 4.1, we have the following corollary of Corollary 4.1 and Lemma 4.1.

- Corollary 4.2 If P is the partition in Corollary 4.1, then q(P) ≤ q(B) + 2ǫ.

![image 127](<2011-conlon-bounds-graph-regularity-removal_images/imageFile127.png>)

- 4.3 Mean square densities of the deﬁning partitions

The next lemma shows that the mean square density of each successive partition increases by a constant factor of the edge density of each Gi.

Lemma 4.2 For each i, we have q(Pi+1) ≥ q(Pi) + 2−5pi.

Proof: The fraction of pairs (X,Y ) ∈ Pi×Pi which are edges of Gi and not edges of Gi is at least pi/4 by the second property in Lemma 3.11. For each such pair, the equitable partitions X = XY1 ∪ XY2 , Y = YX1 ∪ YX2 satisfy d(XYd ,YXd) = 1 and d(XYd ,YX3−d) ≤ ν ≤ 1/4 for d = 1,2. Let d1 = d(XY1 ,YX2) and d2 = d(XY2 ,YX1), so

2

i=1

2

j=1

1 4

![image 128](<2011-conlon-bounds-graph-regularity-removal_images/imageFile128.png>)

d2(XYi ,YXj ) − d2(X,Y ) =

- 1

![image 129](<2011-conlon-bounds-graph-regularity-removal_images/imageFile129.png>)

- 2


+

d21 + d22 4 −

![image 130](<2011-conlon-bounds-graph-regularity-removal_images/imageFile130.png>)

- 1

![image 131](<2011-conlon-bounds-graph-regularity-removal_images/imageFile131.png>)

- 2


+

d1 + d2 4

![image 132](<2011-conlon-bounds-graph-regularity-removal_images/imageFile132.png>)

2

≥

1 4 −

![image 133](<2011-conlon-bounds-graph-regularity-removal_images/imageFile133.png>)

(d1 + d2) 4 ≥

![image 134](<2011-conlon-bounds-graph-regularity-removal_images/imageFile134.png>)

1 8

![image 135](<2011-conlon-bounds-graph-regularity-removal_images/imageFile135.png>)

.

As we get this density increment for at least a pi/4-fraction of the pairs (X,Y ) ∈ Pi × Pi, we get a total density increment of at least 18 p4i = 2−5pi. ✷

![image 136](<2011-conlon-bounds-graph-regularity-removal_images/imageFile136.png>)

![image 137](<2011-conlon-bounds-graph-regularity-removal_images/imageFile137.png>)

We have the following corollary, noting that pr,hr−1 ≥ 210ǫ.

Corollary 4.3 For P = Pr,hr and P′ = Pr,hr−2, we have q(P) = q(Pr,hr) ≥ q(Pr,hr−1) + 2−5pr,hr−1 ≥ q(Pr,hr−1) + 2ǫ ≥ q(P′) + 2ǫ.

- 4.4 Quasirandomness and mean square density




The goal of this subsection is to show that if A is a vertex partition of G with |A| ≤ |Pi|, then q(A) is at most q(Pi) + pi plus a small error term. To accomplish this, we show that the graphs used to deﬁne G are quasirandom with small error.

The study of quasirandom graphs began with the papers by Thomason [42] and Chung, Graham, and Wilson [14]. They showed that a large number of interesting graph properties satisﬁed by random graphs are all equivalent. These properties are known as quasirandom properties, and any graph that has one of these properties (and hence all of these properties) is known as a quasirandom graph.

This development was heavily inﬂuenced by and closely related to Szemere´di’s regularity lemma. Furthermore, all known proofs of Szemere´di’s theorem on long arithmetic progressions in dense subsets of the integers use some notion of quasirandomness. For graphs on n vertices with edge density p bounded away from zero, the following two properties are quasirandom properties. The ﬁrst property states that the number of 4-cycles (or, equivalently, the number of closed walks of length 4) in the graph is p4n4 + o(n4). The second property states that all pairs of vertex subsets S,T have edge density roughly p between them, apart from o(n2) edges. This fact, that the number of 4-cycles in a

graph can control the edge distribution, is quite notable. For our purposes, we will need to show that the ﬁrst property implies the second property, with reasonable error estimates. The now standard proof bounds the second largest (in absolute value) eigenvalue of the adjacency matrix of the graph, and then applies the expander mixing lemma, which bounds the edge discrepancy between subsets in terms of the subset sizes and the second largest eigenvalue.

- Lemma 4.3 Suppose G = (V,E) is a graph with n vertices and average degree d, and the number of closed walks of length 4 in G is at most d4 + αn4. For all vertex subsets S and T,

|e(S,T) −

d|S||T|

![image 138](<2011-conlon-bounds-graph-regularity-removal_images/imageFile138.png>)

n | < λ |S||T|, where λ ≤ α1/4n.

![image 139](<2011-conlon-bounds-graph-regularity-removal_images/imageFile139.png>)

Proof: Let A be the adjacency matrix of G, and λ1,λ2,... ,λn be the eigenvalues of A, with |λ1| ≥ |λ2| ≥ ... ≥ |λn|. Let λ = |λ2|. It is easy to check that λ1 ≥ d. Let λ = |λ2|. The number of closed walks of length 4 in G is equal to the trace

Tr(A4) =

n

i=1

λ4i ≥ λ41 + λ4.

As λ1 ≥ d, and the number of closed walks of length 4 is at most d4+αn4, we conclude λ ≤ (αn4)1/4 = α1/4n. The expander mixing lemma (see Section 2.4 of [28]) states that for all vertex subsets S,T, we

have |e(S,T) − d|Sn||T|| < λ |S||T|. This completes the proof. ✷

![image 140](<2011-conlon-bounds-graph-regularity-removal_images/imageFile140.png>)

![image 141](<2011-conlon-bounds-graph-regularity-removal_images/imageFile141.png>)

- A spanning subgraph of graph G is a subgraph of G on the same vertex set V as G. We let Hi be the spanning subgraph of G where vertices u,v ∈ V are adjacent in Hi if and only if there is an edge


(X,Y ) of Gi, and j ∈ {1,2} with u ∈ XYj ,v ∈ YXj . Note that the edge set of G is precisely the union of the edge sets of the Hi, although this is likely not an edge partition. We next use Lemma 4.3 to show that the edges of Hi are uniformly distributed. That is, the edge density in Hi is roughly the same between large vertex subsets of V .

- Lemma 4.4 Let |V | = n. For each i, the graph Hi on vertex set V has the property that for all vertex subsets S and T,


pi 2 |S||T|| < 2m−i 1/80pin |S||T|.

![image 142](<2011-conlon-bounds-graph-regularity-removal_images/imageFile142.png>)

|eHi(S,T) −

![image 143](<2011-conlon-bounds-graph-regularity-removal_images/imageFile143.png>)

Proof: Note that each edge (X,Y ) of Gi gives rise to two complete bipartite graphs, between XYj and YXj with j ∈ {1,2}, in Hi. In particular, each such edge of Gi contributes 2mn

degree in graph Hi to each vertex in X and in Y .

![image 144](<2011-conlon-bounds-graph-regularity-removal_images/imageFile144.png>)

i

We ﬁrst give a lower bound on the average degree d in Hi. From the ﬁrst property in Lemma 3.11, every vertex in Gi has degree diﬀering from pimi by at most m3i/4. Hence, every vertex in Hi has degree diﬀering from pimi2mn

= pin/2 by at most m3i/4 · 2mni = 12m−i 1/4n. Thus, the average degree d of Hi satisﬁes |d − 12pin| ≤ 12mi−1/4n.

![image 145](<2011-conlon-bounds-graph-regularity-removal_images/imageFile145.png>)

![image 146](<2011-conlon-bounds-graph-regularity-removal_images/imageFile146.png>)

![image 147](<2011-conlon-bounds-graph-regularity-removal_images/imageFile147.png>)

i

![image 148](<2011-conlon-bounds-graph-regularity-removal_images/imageFile148.png>)

![image 149](<2011-conlon-bounds-graph-regularity-removal_images/imageFile149.png>)

We next give an upper bound on the number W4 of labeled closed walks of length four in Hi. By counting over the ﬁrst and third vertex of the closed walk, we have W4 = u,v |NHi(u,v)|2, that is, W4 is the sum of the squares of the codegrees over all labeled pairs of vertices of Hi. By the ﬁrst part of Lemma 3.11, if X,Y are distinct parts of partition Pi, then the codegree of X and Y in Gi is at most p2imi +mi3/4. Hence, from Corollary 2.1, if u and v are in diﬀerent parts in the partition Pi, then

1 4

|NHi(u,v)| ≤ (

![image 150](<2011-conlon-bounds-graph-regularity-removal_images/imageFile150.png>)

n mi

+ ai−1/4)(p2i mi + m3i/4)

![image 151](<2011-conlon-bounds-graph-regularity-removal_images/imageFile151.png>)

1 4

= (

![image 152](<2011-conlon-bounds-graph-regularity-removal_images/imageFile152.png>)

+ a−i 1/4)(p2i + m−i 1/4)n.

For each pair of vertices u,v in the same part of Pi, we have u and v have the same neighborhood in Hi and in this case we use the trivial estimate |NHi(u,v)| ≤ n. In total, we get

W4 =

|NHi(u,v)|2 ≤ mi(mi − 1)

u,v

≤ 1 + 5mi−1/20 p4in4/16,

n mi

![image 153](<2011-conlon-bounds-graph-regularity-removal_images/imageFile153.png>)

2

1 4

· (

![image 154](<2011-conlon-bounds-graph-regularity-removal_images/imageFile154.png>)

+ a−i 1/4)(p2i + m−i 1/4)n

2

+ mi

9/10

where we used pi ≥ mi−1/10, ai = 2⌊ρm

i ⌋ with ρ = 2−20 and mi ≥ m1 ≥ 2200. Let

n mi

![image 155](<2011-conlon-bounds-graph-regularity-removal_images/imageFile155.png>)

2

· n2

α = n−4 W4 − d4 ≤ n−4 W4 − (1 − 4m−i 1/4p−i 1)p4i n4/16 ≤ 5m−i 1/20 + 4m−i 1/4p−i 1 p4i/16 ≤ mi−1/20p4i . By the choice of α, we have W4 = d4 + αn4. From Lemma 4.3, we have |e(S,T) −

d|S||T| n | < α1/4n |S||T|.

![image 156](<2011-conlon-bounds-graph-regularity-removal_images/imageFile156.png>)

![image 157](<2011-conlon-bounds-graph-regularity-removal_images/imageFile157.png>)

Substituting in that the average degree d diﬀers from pin/2 by at most m−i 1/4n/2, the bounds α1/4 ≤ m−i 1/80pi, mi−1/4/2 ≤ mi−1/80pi, and |S||T| ≤ n |S||T|, and using the triangle inequality, we have the desired estimate holds on the number eHi(S,T) of edges in Hi between S and T. ✷

![image 158](<2011-conlon-bounds-graph-regularity-removal_images/imageFile158.png>)

We next prove the following lemma which estimates the edge density of G between certain vertex subsets.

- Lemma 4.5 Let X,Y ∈ Pi be distinct with (X,Y ) not an edge of Gi. If also (X,Y ) is not an edge of Gi and A ⊂ X, B ⊂ Y , or if (X,Y ) is an edge of Gi and there is j ∈ {1,2} such that A ⊂ XYj and


- B ⊂ YX3−j, then


n |A||B|

ph 2

< 6m−i+11/80pi+1

dG(A,B) − 1 −

1 −

,

![image 159](<2011-conlon-bounds-graph-regularity-removal_images/imageFile159.png>)

![image 160](<2011-conlon-bounds-graph-regularity-removal_images/imageFile160.png>)

![image 161](<2011-conlon-bounds-graph-regularity-removal_images/imageFile161.png>)

h>i

where n = |V | is the number of vertices of G.

Proof: For i′ ≥ i, let di′ denote the density between A and B of the pairs which are edges of at least one Hℓ with ℓ ≤ i′. In particular, by the choice of A and B, no edges of Hh for h ≤ i go between A and B, and hence di = 0. Furthermore, we have di+1 = dHi+1(A,B). By Lemma 4.4, the number of edges between A and B in Hi+1 satisﬁes

pi+1 2 |A||B| ≤ 2m−i+11/80pi+1n |A||B|. (22)

![image 162](<2011-conlon-bounds-graph-regularity-removal_images/imageFile162.png>)

eHi+1(A,B) −

![image 163](<2011-conlon-bounds-graph-regularity-removal_images/imageFile163.png>)

Let ti = 1 and for i′ > i, let ti′ = i+1≤h≤i′ 1 − p2h . We prove by induction on i′ that for each i′ ≥ i + 1, we have

![image 164](<2011-conlon-bounds-graph-regularity-removal_images/imageFile164.png>)

i′

|di′ − (1 − ti′)| < q

(1 + ph), (23)

h=i+1

where

n |A||B|

q = 2m−i+11/80pi+1

.

![image 165](<2011-conlon-bounds-graph-regularity-removal_images/imageFile165.png>)

![image 166](<2011-conlon-bounds-graph-regularity-removal_images/imageFile166.png>)

In the base case i′ = i + 1, we have the desired estimate (23) from dividing (22) out by |A||B|. So suppose we have established (23) for i′, and we next prove it for i′ + 1, completing the proof of (23) by induction.

Let X′,Y ′ ∈ Pi′ with X′ ⊂ X, Y ′ ⊂ Y , and (X′,Y ′) not an edge of Gi′. If (X′,Y ′) is not an edge of Gi′, letting A′ = X′ ∩ A and B′ = Y ′ ∩ B, or if (X′,Y ′) is an edge of Gi′, and letting j ∈ {1,2} and A′ = XY′j ∩ A and B′ = YX′3−j ∩ B, we have

pi′+1 2 |A′||B′| ≤ 2m−i′+11/80pi′+1n |A′||B′|.

eHi′+1(A′,B′) −

![image 167](<2011-conlon-bounds-graph-regularity-removal_images/imageFile167.png>)

![image 168](<2011-conlon-bounds-graph-regularity-removal_images/imageFile168.png>)

Each such pair X′,Y ′ with (X′,Y ′) not an edge of Gi′ gives rise to a pair (A′,B′), and each such pair with (X′,Y ′) an edge of Gi′ gives rise to two pairs (A′,B′) of this form, one for each j ∈ {1,2}. The number of pairs (X′,Y ′) is 1 − dGi′(X,Y ) (mi′/mi)2. The total number ∆ of such pairs (A′,B′) is therefore

i′(X,Y ) (mi′/mi)2. On the other hand, the sum of |A′||B′| over all such pairs is (1 − di′)|A||B|. Hence, the average value of |A′||B′| over all such pairs (A′,B′) is (1 − di′)|A||B|/∆. By the triangle inequality, summing over all such pairs A′,B′, we have the number of edges E of Hi′+1 between A and B which are not edges of any Hℓ with ℓ ≤ i′ satisﬁes

∆ = 1 − dGi′(X,Y ) + dG

pi′+1 2

2m−i′+11/80pi′+1n |A′||B′|

![image 169](<2011-conlon-bounds-graph-regularity-removal_images/imageFile169.png>)

E −

(1 − di′)|A||B| ≤

![image 170](<2011-conlon-bounds-graph-regularity-removal_images/imageFile170.png>)

A′,B′

≤ 2m−i′+11/80pi′+1n((1 − di′)|A||B|)1/2∆1/2 ≤ 4m−i′+11/80pi′+1n(|A||B|)1/2mi′/mi,

where we used Jensen’s inequality for the concave function f(y) = y1/2.

Hence,

E |A||B|

E |A||B|

− (ti′ − ti′+1)

− (1 − ti′+1) ≤ |di′ − (1 − ti′)| +

|di′+1 − (1 − ti′+1)| = di′(A,B) +

![image 171](<2011-conlon-bounds-graph-regularity-removal_images/imageFile171.png>)

![image 172](<2011-conlon-bounds-graph-regularity-removal_images/imageFile172.png>)

E |A||B|

pi′+1 2

= |di′ − (1 − ti′)| +

−

ti′

![image 173](<2011-conlon-bounds-graph-regularity-removal_images/imageFile173.png>)

![image 174](<2011-conlon-bounds-graph-regularity-removal_images/imageFile174.png>)

pi′+1 2

E |A||B|

pi′+1 2

≤ (1 +

)|di′ − (1 − ti′)| +

(1 − di′) ≤ (1 +

−

![image 175](<2011-conlon-bounds-graph-regularity-removal_images/imageFile175.png>)

![image 176](<2011-conlon-bounds-graph-regularity-removal_images/imageFile176.png>)

![image 177](<2011-conlon-bounds-graph-regularity-removal_images/imageFile177.png>)

pi′+1 2

)|di′ − (1 − ti′)| + 4m−i′+11/80pi′+1n(|A||B|)−1/2mi′/mi

![image 178](<2011-conlon-bounds-graph-regularity-removal_images/imageFile178.png>)

i′

pi′+1 2

(1 + ph) + 4m−i′+11/80pi′+1n(|A||B|)−1/2mi′/mi

≤ q 1 +

![image 179](<2011-conlon-bounds-graph-regularity-removal_images/imageFile179.png>)

h=i+1

i′+1

(1 + ph),

≤ q

h=i+1

which completes the induction proof of (23). As ph ≤ 1, we have (1 + ph) ≤ e. From (23) with i′ = s − 1, we get

s−1

n |A||B|

(1 + ph) < 6m−i+11/80pi+1

(1 − ph) = |ds−1 − (1 − ts−1)| < q

dG(A,B) − 1 −

,

![image 180](<2011-conlon-bounds-graph-regularity-removal_images/imageFile180.png>)

![image 181](<2011-conlon-bounds-graph-regularity-removal_images/imageFile181.png>)

h=i+1

h>i

which completes the proof. ✷ The following lemma is the main result in this subsection, showing that q(A) − q(P′) is small, where the mean square densities are with respect to the graph G.

- Lemma 4.6 For P′ = Pr,hr−2, we have q(A) ≤ q(P′) + 2ǫ.


![image 182](<2011-conlon-bounds-graph-regularity-removal_images/imageFile182.png>)

Proof: Consider the partition A′ which is the common reﬁnement of P′ and A. The number of parts of A′ is at most |P′||A| ≤ |P′|2, and each part of P′ is reﬁned into at most |A| ≤ |P′| parts of A′. Let i be such that Pi = Pr,hr−2 = P′. As A′ is a reﬁnement of P′, in Hj for each j < i between each pair of parts of A′ the edge density is 0 or 1. Noting that A′ is a reﬁnement of A, we have

|A||B| |X||Y |

m−i 2

q(A) − q(Pi) ≤ q(A′) − q(Pi) =

d2(A,B) − d2(X,Y ) . (24)

![image 183](<2011-conlon-bounds-graph-regularity-removal_images/imageFile183.png>)

A,B⊂A′,A⊂X,B⊂Y

X,Y ∈Pi

Note that the summand in the above sum if (X,Y ) is an edge of Gi is 0 as in this case d(A,B) = d(X,Y ) = 1. We have d2(A,B) − d2(X,Y ) ≤ 1 for (X,Y ) an edge of Gi, and the fraction of pairs (X,Y ) which are edges of Gi is at most pi + m−i 1/4. For a pair X,Y ∈ Pi with (X,Y ) not an edge of Gi or Gi, A,B ⊂ A′ with A ⊂ X and B ⊂ Y , we have by Lemma 4.5 and the triangle inequality that

n |A||B|

|d(A,B) − d(X,Y )| ≤ 2 · 6m−i+11/80pi+1

. (25)

![image 184](<2011-conlon-bounds-graph-regularity-removal_images/imageFile184.png>)

![image 185](<2011-conlon-bounds-graph-regularity-removal_images/imageFile185.png>)

Summing over all parts A,B of A′ with A ⊂ X and B ⊂ Y , we have

|A||B| d2(A,B) − d2(X,Y ) ≤

|A||B|2|d(A,B) − d(X,Y )|

A,B⊂A′,A⊂X,B⊂Y

A,B⊂A′,A⊂X,B⊂Y

24m−i+11/80pi+1n |A||B|

![image 186](<2011-conlon-bounds-graph-regularity-removal_images/imageFile186.png>)

≤

A,B⊂A′,A⊂X,B⊂Y

≤ 24m−i+11/80pi+1n2,

where the ﬁrst inequality follows from a2 − b2 = (a + b)(a − b) ≤ 2(a − b) for 0 ≤ a,b ≤ 1, the second inequality is by (25), and the last inequality is by using the Cauchy-Schwarz inequality, noting that

|A||B| = |X||Y | = (n/mi)2,

A,B⊂A′,A⊂X,B⊂Y

and the number of pairs A,B ⊂ A′ satisfying A ⊂ X,B ⊂ Y is at most m2i. Dividing out by |X||Y | = (n/mi)2, we have,

|A||B| |X||Y |

d2(A,B) − d2(X,Y ) ≤ 24m−i+11/80pi+1m2i. (26)

![image 187](<2011-conlon-bounds-graph-regularity-removal_images/imageFile187.png>)

A,B⊂A′,A⊂X,B⊂Y

From the estimate (26), we have from (24) that

ǫ 2

q(A) − q(P′) ≤ pi + m−i 1/4 + 24m−i+11/80pi+1m2i ≤ 3pi ≤

, (27) where we used

![image 188](<2011-conlon-bounds-graph-regularity-removal_images/imageFile188.png>)

pi = max(m−i 1/10,230ǫ−4ǫr), ǫr ≤ ǫ1 = f(1) = 2−100ǫ6, i ≥ h1 − 2 =

ǫ5

270ǫ1 − 2 ≥ 229ǫ−1 and hence mi ≥ (6/ǫ)10. This completes the proof.

![image 189](<2011-conlon-bounds-graph-regularity-removal_images/imageFile189.png>)

✷

# 5 Induced graph removal lemma

The induced graph removal lemma states that for any ﬁxed graph H on h vertices and ǫ > 0, there is δ = δ(ǫ,H) > 0 such that if a graph G on n vertices has at most δnh induced copies of H, then we can add or delete ǫn2 edges of G to obtain an induced H-free graph. The main goal of this section is to prove Theorem 1.3, which gives a bound on δ−1 which is a tower in h of height polynomial in ǫ−1. We in fact prove the key corollary of the strong regularity lemma, Lemma 1.2, with a tower-type bound. This is suﬃcient to prove the desired tower-type bound for the induced graph removal lemma.

We ﬁrst use the weak regularity lemma of Duke, Lefmann, and R¨odl to ﬁnd a large subset of a graph which is ǫ-regular with itself. By iteratively pulling out such subsets and redistributing the set of

leftover vertices, we obtain a partition of any vertex subset into large vertex subsets each of which is ǫ-regular with itself. Then, in Subsection 5.4, we establish Lemma 1.3, the strong cylinder regularity lemma, with a tower-type bound. We show in Subsection 5.5 that the strong cylinder regularity lemma implies the key corollary of the strong regularity lemma, Lemma 1.2, with a tower-type bound. This in turn implies Theorem 1.3.

In this section and the next, we call a pair (A,B) of vertex subsets of a graph ǫ-regular if for all A′ ⊂ A and B′ ⊂ B with |A′| ≥ ǫ|A| and |B′| ≥ ǫ|B|, we have |d(A′,B′) − d(A,B)| ≤ ǫ.

## 5.1 The Duke-Lefmann-Ro¨dl regularity lemma

Given a k-partite graph G = (V,E) with k-partition V = V1 ∪ ... ∪ Vk, we will consider a partition K of the cylinder V1 × ··· × Vk into cylinders K = W1 × ··· × Wk, Wi ⊂ Vi for i = 1,... ,k, and we let Vi(K) = Wi. Recall from the introduction that a cylinder is ǫ-regular if all the k2 pairs of subsets (Wi,Wj), 1 ≤ i < j ≤ k, are ǫ-regular. The partition K is ǫ-regular if all but an ǫ-fraction of the k-tuples (v1,... ,vk) ∈ V1 × ··· × Vk are in ǫ-regular cylinders in the partition K.

The weak regularity lemma of Duke, Lefmann, and Ro¨dl [15] is now as follows. Note that, like the Frieze-Kannan weak regularity lemma, it has only a single-exponential bound on the number of parts, which is much better than the tower-type bound on the number of parts in Szemere´di’s regularity lemma. Duke, Lefmann, and Ro¨dl [15] used their regularity lemma to derive a fast approximation algorithm for the number of copies of a ﬁxed graph in a large graph.

- Lemma 5.1 Let 0 < ǫ < 1/2 and β = β(ǫ) = ǫk2ǫ−5. Suppose G = (V,E) is a k-partite graph with k-partition V = V1 ∪ ... ∪ Vk. Then there exists an ǫ-regular partition K of V1 × ··· × Vk into at most β−1 parts such that, for each K ∈ K and 1 ≤ i ≤ k, we have |Vi(K)| ≥ β|Vi|.

5.2 Finding an ǫ-regular subset

For a graph G = (V,E), a vertex subset U ⊂ V is ǫ-regular if the pair (U,U) is ǫ-regular. The following lemma demonstrates that any graph contains a large vertex subset which is ǫ-regular.

- Lemma 5.2 For each 0 < ǫ < 1/2, let δ = δ(ǫ) = 2−ǫ−(10/ǫ)

4

. Every graph G = (V,E) contains an ǫ-regular vertex subset U with |U| ≥ δ|V |.

- Lemma 5.1 implies that each k-partite graph G = (V,E) with k-partition V = V1 ∪ ... ∪ Vk has a cylinder K which is ǫ-regular in which each part has size |Vi(K)| ≥ ǫk2ǫ−5|Vi|. The proof can be easily modiﬁed to show that if each part of G has the same size, then each part of the ǫ-regular cylinder


K has equal size, which is at least ǫk2ǫ−5|Vi|. This implies that for any graph G = (V,E), if G has at least k vertices, by considering any k vertex disjoint subsets of equal size ⌊|G|/k⌋ ≥ |G|/(2k), and then applying this result, we get the following lemma.

- Lemma 5.3 For each 0 < ǫ < 1/2, any graph G = (V,E) on at least k vertices has an ǫ-regular k-cylinder with parts of equal size, which is at least 21kǫk2ǫ−5|V |.


![image 190](<2011-conlon-bounds-graph-regularity-removal_images/imageFile190.png>)

- The t-color Ramsey number rt(s) is the minimum k such that every t-coloring of the edges of the complete graph Kk on k vertices contains a monochromatic clique of order s. A simple pigeonhole argument (see [23]) gives rt(s) ≤ tts for t ≥ 2.
- Lemma 5.4 For integers s,t ≥ 2, let k = tts. Let G = (V,E) be a graph on at least k vertices, and 0 < α < 1/2. The graph G contains an α-regular s-cylinder with parts of equal size at least

N = 21kαk2α−5|V | such that the density between each pair of parts diﬀers by at most 1/t.

![image 191](<2011-conlon-bounds-graph-regularity-removal_images/imageFile191.png>)

Proof: Note that k = tts ≥ rt(s). By Lemma 5.3, G contains an α-regular k-cylinder U1 × ··· × Uk with parts of equal size at least N. Partition the unit interval [0,1] = I1 ∪ ... ∪ It into t intervals of length 1/t. Consider the edge-coloring of the complete graph on k vertices 1,... ,k for which the color of edge (i,j) is the number a for which the density d(Ui,Uj) ∈ Ia. Since k ≥ rt(s), there is a monochromatic clique of order s in this t-coloring, and the corresponding parts form the desired s-cylinder. ✷

- Lemma 5.5 Suppose α ≤ 1/9 and U1 × ··· × Us is an α-regular cylinder in a graph G = (V,E) with s ≥ 2α−1 parts Ui of equal size and the densities between the pairs of distinct parts lie in an interval of length at most α. Then the set U = U1 ∪ ... ∪ Us is ǫ-regular with itself, where ǫ = 3α1/2.


Proof: Let A,B ⊂ U with |A|,|B| ≥ ǫ|U| and, for 1 ≤ i ≤ s, let Ai = A ∩ Ui and Bi = B ∩ Ui. Suppose d(Ui,Uj) ∈ [γ,γ + α] for 1 ≤ i < j ≤ s. Let A1 be the union of all Ai for which |Ai| ≥ α|Ui|

- and A2 = A \ A1. Similarly, let B1 be the union of all Bi for which |Bi| ≥ α|Ui| and B2 = B \ B1. We have |A2| < α|U| ≤ αǫ−1|A| and |B2| < α|U| ≤ αǫ−1|B|. Let I1 denote the set of all pairs (i,i) with i ∈ [s], I2 the set of all pairs (i,j) ∈ [s] × [s] with i = j, Ai ⊂ A1, and Bj ⊂ B1, and I3 = [s] × [s] \ (I1 ∪ I2). Let D(Ai,Bj) = |d(Ai,Bj) − γ| |A|Ai||||BBj||. We have


![image 192](<2011-conlon-bounds-graph-regularity-removal_images/imageFile192.png>)

D(Ai,Bi) ≤

(i,i)∈I1

(i,i)∈I1

|Bi| |B|

|Ai||Bi| |A||B|

≤ max

![image 193](<2011-conlon-bounds-graph-regularity-removal_images/imageFile193.png>)

![image 194](<2011-conlon-bounds-graph-regularity-removal_images/imageFile194.png>)

i

1 sǫ

|Ui| |B|

≤ max

≤

.

![image 195](<2011-conlon-bounds-graph-regularity-removal_images/imageFile195.png>)

![image 196](<2011-conlon-bounds-graph-regularity-removal_images/imageFile196.png>)

i

If (i,j) ∈ I2, using the triangle inequality and α-regularity,

|d(Ai,Bj) − γ| ≤ |d(Ai,Bj) − d(Ui,Uj)| + |d(Ui,Uj) − γ| ≤ α + α = 2α. Hence,

2α|Ai||Bj| |A||B|

≤ 2α.

D(Ai,Bj) ≤

![image 197](<2011-conlon-bounds-graph-regularity-removal_images/imageFile197.png>)

(i,j)∈I2

(i,j)∈I2

Finally,

|A2| |A|

|Ai||Bj| |A||B|

D(Ai,Bj) ≤

≤ 1 − 1 −

![image 198](<2011-conlon-bounds-graph-regularity-removal_images/imageFile198.png>)

![image 199](<2011-conlon-bounds-graph-regularity-removal_images/imageFile199.png>)

(i,j)∈I3

(i,j)∈I3

|B2| |B|

1 −

![image 200](<2011-conlon-bounds-graph-regularity-removal_images/imageFile200.png>)

< 1 − (1 − αǫ−1)2 ≤ 2αǫ−1.

We have by the triangle inequality |d(A,B) − γ| ≤

D(Ai,Bj)

1≤i,j≤s

D(Ai,Bj)

D(Ai,Bj) +

D(Ai,Bj) +

=

(i,j)∈I3

(i,j)∈I2

(i,j)∈I1

1 sǫ

ǫ 2

+ 2α + 2αǫ−1 ≤

≤

. By the triangle inequality, for any A,B,X,Y ⊂ U each of cardinality at least ǫ|U|, we have |d(A,B) − d(X,Y )| ≤ |d(A,B) − γ| + |γ − d(X,Y )| ≤

![image 201](<2011-conlon-bounds-graph-regularity-removal_images/imageFile201.png>)

![image 202](<2011-conlon-bounds-graph-regularity-removal_images/imageFile202.png>)

ǫ 2

ǫ 2

+

= ǫ.

![image 203](<2011-conlon-bounds-graph-regularity-removal_images/imageFile203.png>)

![image 204](<2011-conlon-bounds-graph-regularity-removal_images/imageFile204.png>)

In particular, this holds for X = Y = U, and hence U is ǫ-regular. ✷ By applying Lemma 5.4 with α = (ǫ/3)2 and s = t = ⌈2α−1⌉, and then applying Lemma 5.5, we obtain

- Lemma 5.2. Note that the proof assumes that the number of vertices of the graph is suﬃciently large, at least k = tts, but we can make this assumption as otherwise we can trivially pick U to consist of a single vertex, which is ǫ-regular. The next lemma shows that if we have an ǫ-regular pair, and add a small fraction of vertices to one part, then the pair is still regular, but with a slightly worse regularity.


- Lemma 5.6 Suppose A and B are vertex subsets of a graph G which form an ǫ-regular pair, and C is a vertex subset disjoint from B of size |C| ≤ β|B|. Then the pair (A,B ∪ C) is α-regular with α = ǫ + √β + β.


![image 205](<2011-conlon-bounds-graph-regularity-removal_images/imageFile205.png>)

Proof: Let A′ ⊂ A and B′ ∪C′ ⊂ B ∪C with B′ ⊂ B, C′ ⊂ C, |A′| ≥ α|A| and |B′ ∪C′| ≥ α|B ∪C|. Note that |A′| ≥ α|A| ≥ ǫ|A| and |B′| = |B′ ∪ C′| − |C′| ≥ α|B ∪ C| − |C| ≥ (α − β)|B| ≥ ǫ|B|. Since the pair (A,B) is ǫ-regular, we have

d(A′,B′) − d(A,B) ≤ ǫ. Also, |C′| ≤ |C| ≤ β|B| ≤ β|B ∪ C| ≤ βα−1|B′ ∪ C′|. Therefore, |d(A′,B′ ∪ C′) − d(A′,B′)| = d(A′,B′) |B′| |B′ ∪ C′|

+ d(A′,C′) |C′| |B′ ∪ C′|

− d(A′,B′)

![image 206](<2011-conlon-bounds-graph-regularity-removal_images/imageFile206.png>)

![image 207](<2011-conlon-bounds-graph-regularity-removal_images/imageFile207.png>)

= d(A′,C′) − d(A′,B′) |C′| |B′ ∪ C′|

|C′| |B′ ∪ C′|

≤ βα−1. We similarly have

≤

![image 208](<2011-conlon-bounds-graph-regularity-removal_images/imageFile208.png>)

![image 209](<2011-conlon-bounds-graph-regularity-removal_images/imageFile209.png>)

|C| |B ∪ C|

≤ β.

|d(A,B ∪ C) − d(A,B)| = |d(A,C) − d(A,B)|

![image 210](<2011-conlon-bounds-graph-regularity-removal_images/imageFile210.png>)

Hence, by the triangle inequality, we have |d(A′,B′ ∪ C′) − d(A,B ∪ C)| is at most d(A′,B′ ∪ C′) − d(A′,B′) + d(A′,B′) − d(A,B) + |d(A,B) − d(A,B ∪ C)| ≤ βα−1 + ǫ + β ≤ α.

Hence, the pair (A,B ∪ C) is α-regular. ✷ By repeatedly pulling out 3ǫ/4-regular sets using Lemma 5.2 until there are at most 100ǫ2 |V | remaining vertices, distributing the remaining vertices among the parts, and using Lemma 5.6 twice in each part, we arrive at the following lemma. It shows how to partition a graph into large parts, each part being ǫ-regular with itself.

![image 211](<2011-conlon-bounds-graph-regularity-removal_images/imageFile211.png>)

- Lemma 5.7 For each 0 < ǫ < 1/2, let δ = δ(ǫ) = 2−ǫ−(20/ǫ)

4

. Every graph G = (V,E) has a vertex partition V = V1 ∪ ... ∪ Vk such that for each i, 1 ≤ i ≤ k, we have |Vi| ≥ δ|V | and Vi is an ǫ-regular set.

- 5.3 Tools


In this subsection, we prove two simple lemmas concerning mean square density which will be useful in establishing and using the strong cylinder regularity lemma.

The ﬁrst lemma, which is rather standard, shows that for any vertex partition P, there is a vertex equipartition P′ with a similar number of parts to P and mean square density not much smaller than the mean square density of P. It is useful in density increment arguments where at each stage one would like to work with an equipartition.

- Lemma 5.8 Let G = (V,E) be a graph, and P : V = V1 ∪ ... ∪ Vk be a vertex partition into k parts. There is an equitable partition P′ of V into t parts such that q(P′) ≥ q(P) − 2kt .


![image 212](<2011-conlon-bounds-graph-regularity-removal_images/imageFile212.png>)

Proof: For an equipartition of V into t parts, we have a certain number of parts of order ⌊|V |/t⌋ and the remaining parts are of order ⌈|V |/t⌉. For each part Vi ∈ P, partition it into parts of order ⌊|V |/t⌋ or ⌈|V |/t⌉ so that there are not too many parts of either order to allow an equipartition of the whole set, with possibly one remaining set of cardinality less than |V |/t. Let Q be this reﬁnement of P. From the Cauchy-Schwarz inequality, it follows that q(Q) ≥ q(P). Let U be the vertices in the remaining parts of Q, so |U| < k|V |/t.

Arbitrarily chop the vertices of U into parts of the desired orders so as to obtain an equipartition P′. We have

2

d2(X,Y )|X||Y | |V |2

- |U|

![image 213](<2011-conlon-bounds-graph-regularity-removal_images/imageFile213.png>)

- |V |


k t ≥ q(P) − 2

k t

- q(P′) ≥ X,Y ∈Q,X,Y ⊂V \U


≥ q(Q) − 1 − 1 −

.

≥ q(Q) − 2

![image 214](<2011-conlon-bounds-graph-regularity-removal_images/imageFile214.png>)

![image 215](<2011-conlon-bounds-graph-regularity-removal_images/imageFile215.png>)

![image 216](<2011-conlon-bounds-graph-regularity-removal_images/imageFile216.png>)

✷

The next lemma is helpful in deducing the induced graph removal lemma from the strong cylinder regularity lemma. Let G = (V,E) and P : V = V1 ∪ ... ∪ Vk be an equipartition, and K be a partition of the cylinder V1 × ··· × Vk into cylinders. For K = W1 × ··· × Wk ∈ K, deﬁne the density d(K) = |W|V1|×···×|Wk|

1|×···×|Vk| . The cylinder K is ǫ-close to P if |d(Wi,Wj) − d(Vi,Vj)| ≤ ǫ for all but at most ǫk2 pairs 1 ≤ i = j ≤ k. if cylinder K is not ǫ-close to P, then

![image 217](<2011-conlon-bounds-graph-regularity-removal_images/imageFile217.png>)

|d(Wi,Wj) − d(Vi,Vj)| > ǫ2k2.

1≤i =j≤k

The cylinder partition K is ǫ-close to P if d(K) ≤ ǫ, where the sum is over all K ∈ K that are not ǫ-close to P. Note that if K is not ǫ-close, then

|d(Wi,Wj) − d(Vi,Vj)| d(K) > ǫ3k2.

K∈K 1≤i =j≤k

Recall that Q(K) is the common reﬁnement of all the parts Vi(K) with i ∈ [k] and K ∈ K.

- Lemma 5.9 Let G = (V,E) and P : V = V1 ∪ ... ∪ Vk be an equipartition with no empty parts, i.e., |V | ≥ k. Let K be a partition of the cylinder V1 × ··· × Vk into cylinders. If Q = Q(K) satisﬁes


- q(Q) ≤ q(P) + ǫ, then K is 21/3ǫ1/6-close to P.


Proof: Let Qi denote the partition of Vi which is the restriction of partition Q to Vi. Since P is an equipartition and |V | ≥ k, then all parts have order at least |Vk| ≥ |2Vk|. Therefore,

![image 218](<2011-conlon-bounds-graph-regularity-removal_images/imageFile218.png>)

![image 219](<2011-conlon-bounds-graph-regularity-removal_images/imageFile219.png>)

ǫ ≥ q(Q) − q(P) =

(q(Qi,Qj) − q(Vi,Vj)) |Vi||Vj| |V |2

![image 220](<2011-conlon-bounds-graph-regularity-removal_images/imageFile220.png>)

1≤i,j≤k

1 4k2 1≤i =j≤k

≥

(q(Qi,Qj) − q(Vi,Vj)) , (28)

![image 221](<2011-conlon-bounds-graph-regularity-removal_images/imageFile221.png>)

i| and pB = ||VB|

i,B∈Qj d2(A,B)pApB with pA = ||VA|

j|, and q(Vi,Vj) = d2(Vi,Vj). Fix for now 1 ≤ i = j ≤ k. For K = W1 × ··· × Wk ∈ K, we have

where q(Qi,Qj) = A∈Q

![image 222](<2011-conlon-bounds-graph-regularity-removal_images/imageFile222.png>)

![image 223](<2011-conlon-bounds-graph-regularity-removal_images/imageFile223.png>)

d(Wi,Wj) = d(A,B) |A| |Wi|

|B| |Wj|

,

![image 224](<2011-conlon-bounds-graph-regularity-removal_images/imageFile224.png>)

![image 225](<2011-conlon-bounds-graph-regularity-removal_images/imageFile225.png>)

and hence, by the triangle inequality,

|B| |Wj|

|A| |Wi|

|d(Wi,Wj) − d(Vi,Vj)| ≤ |d(A,B) − d(Vi,Vj)|

,

![image 226](<2011-conlon-bounds-graph-regularity-removal_images/imageFile226.png>)

![image 227](<2011-conlon-bounds-graph-regularity-removal_images/imageFile227.png>)

where the sums are over all A ∈ Qi with A ⊂ Wi and B ∈ Qj with B ⊂ Wj. Summing over all K ∈ K, we have,

|d(Wi,Wj) − d(Vi,Vj)| d(K) ≤

K=W1×···Wk∈K

K=W1×···Wk∈K

|A| |Wi|

|B| |Wj|

|d(A,B) − d(Vi,Vj)|

d(K)

![image 228](<2011-conlon-bounds-graph-regularity-removal_images/imageFile228.png>)

![image 229](<2011-conlon-bounds-graph-regularity-removal_images/imageFile229.png>)

|d(A,B) − d(Vi,Vj)|pApB

=

A∈Qi,B∈Qj

1/2

 

(d(A,B) − d(Vi,Vj))2 pApB

≤



A∈Qi,B∈Qj

= (q(Qi,Qj) − q(Vi,Vj))1/2 .

where the ﬁrst equality follows by swapping the order of summation and the last inequality is the Cauchy-Schwarz inequality.

Summing over all 1 ≤ i = j ≤ k and changing the order of summation,

(q(Qi,Qj) − q(Vi,Vj))1/2

|d(Wi,Wj) − d(Vi,Vj)| d(K) ≤

K=W1×···Wk∈K 1≤i =j≤k

1≤i =j≤k

1/2

q(Qi,Qj) − q(Vi,Vj)

 k2

≤



1≤i =j≤k

√

![image 230](<2011-conlon-bounds-graph-regularity-removal_images/imageFile230.png>)

k2 · 4k2ǫ = 2ǫ1/2k2,

≤

where the second inequality is the Cauchy-Schwarz inequality and the last inequality uses the estimate (28). By the remark before the lemma, we get that K is 2ǫ1/2 1/3 = 21/3ǫ1/6-close to P. ✷

## 5.4 The strong cylinder regularity lemma

Using the lemmas established in the previous subsections, in this subsection we prove Lemma 1.3, the strong cylinder regularity lemma, with a tower-type bound.

Recall that a k-cylinder W1 × ··· × Wk is strongly ǫ-regular if all pairs (Wi,Wj) with 1 ≤ i,j ≤ k are ǫ-regular. A partition K of V1 × ··· × Vk into cylinders is strongly ǫ-regular if all but ǫ|V1| × ··· × |Vk| vertices (v1,... ,vk) ∈ V1 × ··· × Vk are contained in strongly ǫ-regular cylinders K ∈ K.

We recall the statement of the strong cylinder regularity lemma.

- Lemma 5.10 For 0 < ǫ < 1/3, positive integer s, and decreasing function f : N → (0,ǫ], there is S = S(ǫ,s,f) such that the following holds. For every graph G, there is an integer s ≤ k ≤ S, an equitable


- partition P : V = V1 ∪ ... ∪ Vk and a strongly f(k)-regular partition K of the cylinder V1 × ··· × Vk into cylinders satisfying that the partition Q = Q(K) of V has at most S parts and q(Q) ≤ q(P) + ǫ. Furthermore, there is an absolute constant c such that letting s1 = s and si+1 = t4 ((si/f(si))c), we may take S = sℓ with ℓ = 2ǫ−1 + 1.


Proof: We may assume |V | ≥ S, as otherwise we can let P and Q be the trivial partitions into singletons, and it is easy to see the lemma holds. We will deﬁne a sequence of partitions P1,P2,... of equitable partitions, with Pj+1 a reﬁnement of Pj and q(Pj+1) > q(Pj) + ǫ/2. Let P1 be an arbitrary equitable partition of V consisting of s1 = s parts. Suppose we have already found an equitable partition Pj : V = V1 ∪ ... ∪ Vk with k ≤ sj.

4

Let β(x,ℓ) = xℓ2x−5 as in Lemma 5.1 and δ(x) = 2−x−(20/x)

as in Lemma 5.7. We apply Lemma 5.7 to each part Vi of the partition Pj to get a partition of each part Vi = Vi1 ∪ ... ∪ Vihi of Pi into parts each of cardinality at least δ|Vi|, where δ = δ(γ) and γ = f(k) · β with β = β(f(k),k), such that each part Vih is γ-regular. Note that δ−1 is at most triple-exponential in a polynomial in k/f(k). For each k-tuple ℓ = (ℓ1,... ,ℓk) ∈ [h1] × ··· × [hk], by Lemma 5.1 there is an f(k)-regular partition Kℓ of the cylinder V1ℓ1 × ··· × Vkℓk into at most β−1 cylinders such that, for each K ∈ Kℓ, |Viℓi(K)| ≥ β|Viℓi|. The union of the Kℓ forms a partition K of V1 × ··· × Vk which is strongly f(k)-regular.

Recall that Q = Q(K) is the partition of V which is the common reﬁnement of all parts Vi(K) with i ∈ [k] and K ∈ K. The number of parts of K is at most δ−kβ−1, and hence the number of parts of Q is at most k21/(δkβ). Thus, the number of parts of Q is at most quadruple-exponential in a polynomial in k/f(k). Let Pj+1 be an equitable partition into 4ǫ−1|Q| parts with q(Pj+1) ≥ q(Q)− 2ǫ, which exists by Lemma 5.8. Hence, there is an absolute constant c such that

![image 231](<2011-conlon-bounds-graph-regularity-removal_images/imageFile231.png>)

|Pj+1| ≤ t4 ((k/f(k))c) ≤ sj+1.

If q(Q) ≤ q(Pj) + ǫ, then we may take P = Pj and Q = Q(K), and these partitions satisfy the desired properties. Otherwise, q(Pj+1) ≥ q(Q) − 2ǫ > q(Pj) + 2ǫ, and we continue the sequence of partitions. Since q(P1) ≥ 0, and the mean square density goes up by more than ǫ/2 at each step and is always at most 1, this process must stop within 2/ǫ steps, and we obtain the desired partitions. ✷

![image 232](<2011-conlon-bounds-graph-regularity-removal_images/imageFile232.png>)

![image 233](<2011-conlon-bounds-graph-regularity-removal_images/imageFile233.png>)

## 5.5 A tower-type bound for the key corollary

In the previous subsection, we established the strong cylinder regularity lemma with a tower-type bound. We next use this result to deduce a tower-type bound for Lemma 1.2, which is the key corollary of the strong regularity lemma, and easily implies the induced graph removal lemma as shown below. We recall the statement of Lemma 1.2 below.

- Lemma 5.11 For each 0 < ǫ < 1/3 and decreasing function f : N → (0,ǫ] there is δ′ = δ′(ǫ,f) such that every graph G = (V,E) with |V | ≥ δ′−1 has an equitable partition V = V1 ∪ ... ∪ Vk and vertex subsets Wi ⊂ Vi such that |Wi| ≥ δ′|V |, each pair (Wi,Wj) with 1 ≤ i ≤ j ≤ k is f(k)-regular, and all but at most ǫk2 pairs 1 ≤ i ≤ j ≤ k satisfy |d(Vi,Vj) − d(Wi,Wj)| ≤ ǫ. Furthermore, we may take δ′ = 8S12, where S = (ǫ46,s,f) is deﬁned as in Lemma 5.10 and s = 2ǫ−1.


![image 234](<2011-conlon-bounds-graph-regularity-removal_images/imageFile234.png>)

![image 235](<2011-conlon-bounds-graph-regularity-removal_images/imageFile235.png>)

Proof: Let α = ǫ46, s = 2ǫ−1, and δ′ = 8S12, where S = S(α,s,f) is as in Lemma 5.10. We apply Lemma 5.10 with α in place of ǫ. We get an equipartition P : V = V1 ∪ ... ∪ Vk with s ≤ k ≤ S and a strongly f(k)-regular partition K of V1 × ··· × Vk into cylinders such that the reﬁnement Q = Q(K) of P has at most S = S(α,s,f) parts and satisﬁes q(Q) ≤ q(P) + α. Since |V | ≥ δ′−1 = 8S2, and

![image 236](<2011-conlon-bounds-graph-regularity-removal_images/imageFile236.png>)

![image 237](<2011-conlon-bounds-graph-regularity-removal_images/imageFile237.png>)

- P is an equipartition into k ≤ S parts, the cardinality of each part Vi ∈ P satisﬁes |Vi| ≥ |2VS|. By


![image 238](<2011-conlon-bounds-graph-regularity-removal_images/imageFile238.png>)

- Lemma 5.9, as 21/3α1/6 = ǫ, the cylinder partition K is ǫ-close to P. Hence, at most an ǫ-fraction of the k-tuples (v1,... ,vk) ∈ V1 × ··· × Vk belong to parts K = W1 × ··· × Wk of K that are not ǫ-close to P. Since Q(K) has at most S parts, the fraction of k-tuples (v1,... ,vk) ∈ V1 ×··· ×Vk that belong to parts K = W1 × ··· × Wk of K with |Wi| < 41S|Vi| for at least one i ∈ [k] is at most 41S · S = 41. Therefore, at least a fraction 1 −f(k)−ǫ− 14 > 0 of the k-tuples (v1,... ,vk) ∈ V1 ×··· ×Vk belong to


![image 239](<2011-conlon-bounds-graph-regularity-removal_images/imageFile239.png>)

![image 240](<2011-conlon-bounds-graph-regularity-removal_images/imageFile240.png>)

![image 241](<2011-conlon-bounds-graph-regularity-removal_images/imageFile241.png>)

![image 242](<2011-conlon-bounds-graph-regularity-removal_images/imageFile242.png>)

parts K = W1 × ··· × Wk of K satisfying K is strongly f(k)-regular, |Wi| ≥ 41S|Vi| ≥ δ′|V | for i ∈ [k], and K is ǫ-close to P. Since a positive fraction of the k-tuples belong to such K, there is at least

![image 243](<2011-conlon-bounds-graph-regularity-removal_images/imageFile243.png>)

one such K. This K has the desired properties. Indeed the number of pairs 1 ≤ i = j ≤ k for which |d(Wi,Wj) − d(Vi,Vj)| > ǫ is at most ǫk2 and hence the number of pairs 1 ≤ i ≤ j ≤ k for which |d(Wi,Wj) − d(Vi,Vj)| > ǫ is at most ǫk2/2 + k ≤ ǫk2. This completes the proof. ✷

We next discuss how to obtain the induced graph removal lemma from Lemma 1.2. This is a bit easier to obtain than in [5] because Lemma 1.2 has the additional property that the subsets Wi in the cylinder K are ǫ-regular. We ﬁnish this section by giving this proof and discussing the bound it gives for the induced graph removal lemma, which is a tower in h of height polynomial in ǫ−1. We ﬁrst need the following counting lemma, which is rather standard (see, e.g., Lemma 3.2 in Alon, Fischer, Krivelevich, and Szegedy [5] for a minor variant). We omit the proof.

- Lemma 5.12 If H is a graph with vertices 1,... ,h, and G is a graph with not necessarily disjoint


vertex subsets W1,... ,Wh such that every pair (Wi,Wj) with 1 ≤ i < j ≤ h is γ-regular with γ ≤ 41hηh, |Wi| ≥ γ−1 for 1 ≤ i ≤ h and, for 1 ≤ i < j ≤ k, d(Wi,Wj) > η if (i,j) is an edge of H and

![image 244](<2011-conlon-bounds-graph-regularity-removal_images/imageFile244.png>)

d(Wi,Wj) < 1 − η otherwise, then G contains at least η4 (h2) |W1| × ··· × |Wh| induced copies of H with the copy of vertex i in Wi.

![image 245](<2011-conlon-bounds-graph-regularity-removal_images/imageFile245.png>)

We ﬁnish the section with a quantitative version of Theorem 1.3.

- Theorem 5.1 There is an absolute constant c such that for any graph H on h vertices 1,... ,h and


- 0 < ǫ < 1/2 there is δ > 0 with δ−1 = tj(h) with j = O(ǫ−6) such that if a graph G on n vertices has at most δnh induced copies of H, then we can add or delete ǫn2 edges of G to obtain an induced H-free graph.


2

Proof: Let η = 8ǫ. Let δ = η4 h

δ′h, where δ′ = δ′(η,f) as in Lemma 5.11 and f(k) = 41hηh. If the number of vertices satisﬁes |V | < δ−1/h, then δ|V |h < 1 and there are no induced copies of H, in which case no edges of G need to be modiﬁed. We can therefore assume that |V | ≥ δ−1/h = η4 −h δ′−1. As |V | ≥ δ′−1, we can apply Lemma 5.11 to graph G = (V,E) with η in place of ǫ and f as above. We obtain an equitable partition V = V1 ∪ ... ∪ Vk and vertex subsets Wi ⊂ Vi such that |Wi| ≥ δ′|V | ≥

![image 246](<2011-conlon-bounds-graph-regularity-removal_images/imageFile246.png>)

![image 247](<2011-conlon-bounds-graph-regularity-removal_images/imageFile247.png>)

![image 248](<2011-conlon-bounds-graph-regularity-removal_images/imageFile248.png>)

![image 249](<2011-conlon-bounds-graph-regularity-removal_images/imageFile249.png>)

−h, the cylinder W1 × ··· Wk is strongly f(k)-regular, and all but at most ηk2 pairs 1 ≤ i ≤ j ≤ k satisfy |d(Wi,Wj) − d(Vi,Vj)| ≤ η.

η 4

![image 250](<2011-conlon-bounds-graph-regularity-removal_images/imageFile250.png>)

The above counting lemma shows that if there is any mapping φ : [h] → [k] such that d(Wφ(i),Wφ(j)) > η for (i,j) an edge of H and d(Wφ(i),Wφ(j)) < 1 − η for i,j distinct and nonadjacent in H, then G

contains at least η4 (h2) |W1|×···×|Wh| ≥ δnh induced copies of H. Hence, no such mapping φ exists. That is, for every mapping φ : [h] → [k], there is an edge (i,j) for which d(Wφ(i),Wφ(j)) ≤ η or distinct i,j that are nonadjacent in H with d(Wφ(i),Wφ(j)) ≥ 1 − η.

![image 251](<2011-conlon-bounds-graph-regularity-removal_images/imageFile251.png>)

For each pair (Wi,Wj) for which d(Wi,Wj) ≤ η, delete all edges between Vi and Vj, and for each pair (Wi,Wj) for which d(Wi,Wj) ≥ 1 − η, add all edges between Vi and Vj. Let G′ be this modiﬁcation of G. By the previous paragraph, there are no induced copies of H in G′.

We have left to show that few edge modiﬁcations are made in obtaining G′ from G. If a pair (Wi,Wj) for which edges were modiﬁed satisﬁes |d(Wi,Wj) − d(Vi,Vj)| ≤ η, then the density between the two sets was only changed by at most 2η. The number of 1 ≤ i ≤ j ≤ k for which |d(Wi,Wj)−d(Vi,Vj)| > η is at most ηk2. Since V1,... ,Vk is an equipartition into nonempty parts, at most ηk2 · 4 nk 2 = 4ηn2

![image 252](<2011-conlon-bounds-graph-regularity-removal_images/imageFile252.png>)

edges are changed between such pairs. In total at most 2η n2 +4ηn2 ≤ 5ηn2 < ǫn2 edges were changed in order to obtain G′ from G.

From Lemma 5.11, we have δ′ = 8S12, where S = S(α,s,f) is the function from Lemma 5.10 with α = η46, s = 2η−1 and f(k) = 41hηh. From Lemma 5.10, S(α,s,f) will be at most a tower in h whose height is proportional to η−6. Therefore, by the choice of η and δ in the above proof of the induced graph removal lemma, we indeed get the desired tower-type bound. This also completes the proof of Theorem 1.3. ✷

![image 253](<2011-conlon-bounds-graph-regularity-removal_images/imageFile253.png>)

![image 254](<2011-conlon-bounds-graph-regularity-removal_images/imageFile254.png>)

![image 255](<2011-conlon-bounds-graph-regularity-removal_images/imageFile255.png>)

# 6 Regular approximation lemma

In this section we show how to derive the regular approximation lemma from Tao’s regularity lemma,

- as discussed in Subsection 1.5. The key lemma is Lemma 6.1, which shows how to turn a bipartite graph into a regular pair by changing some edges according to a weak regular partition. We use the notation x = y ± ǫ to denote the fact that y − ǫ ≤ x ≤ y + ǫ. It will be helpful to use the Hoeﬀding-Azuma inequality for concentration of measure. Say that a


random variable X(ω) on an n-dimensional product space Ω = ni=1 Ωi is Lipschitz if changing ω in any single coordinate aﬀects the value of X(ω) by at most one. The Hoeﬀding-Azuma inequality (see, e.g., [10]) provides concentration for these distributions.

- Theorem 6.1 (Hoeﬀding-Azuma Inequality) Let X be a Lipschitz random variable on an ndimensional product space. Then for any t ≥ 0,


t2 2n

P[|X − E[X] | > t] ≤ 2exp −

.

![image 256](<2011-conlon-bounds-graph-regularity-removal_images/imageFile256.png>)

For a bipartite graph across parts A and B, and partitions A : A = A1 ∪ ... ∪ Ar and B : B = B1 ∪... ∪Bs, let q(A,B) = d2(A,B) and q(A,B) = i,j |A|Ai||||BBj||d2(Ai,Bj) be the mean square density across the partitions A and B.

![image 257](<2011-conlon-bounds-graph-regularity-removal_images/imageFile257.png>)

- Lemma 6.1 Let 0 < δ < 1. Suppose A,B are disjoint vertex subsets of a graph with |A| ≥ |B| > 8δ−2


and d(A,B) = η. Suppose further that A : A = A1 ∪ ... ∪ Ar and B : B = B1 ∪ ... ∪ Bs form a weak δ-regular partition of the pair (A,B), i.e., for all S ⊂ A and T ⊂ B, we have

r

s

|Ai ∩ S||Bj ∩ T|d(Ai,Bj) − d(S,T)|S||T| ≤ δ|A||B|.

i=1

j=1

Then, one can add or remove at most δ + (q(A,B) − q(A,B))1/2 |A||B| edges across (A,B) and thus turn it into a 2δ1/3-regular pair satisfying d(A,B) = η ± δ.

Proof: Let αi,j = d(Ai,Bj) − d(A,B). If αi,j ≥ 0, we delete each of the edges connecting Ai and Bj independently with probability d(Aαi,j

i,Bj). If αi,j < 0, we add each of the nonedges between Ai and Bj

![image 258](<2011-conlon-bounds-graph-regularity-removal_images/imageFile258.png>)

with probability −1−dα(Ai,j

i,Bj). Clearly the expected value of d(A,B) after these modiﬁcations is η. By the Hoeﬀding-Azuma inequality, the probability that the new density deviates from η by more than δ is at most

![image 259](<2011-conlon-bounds-graph-regularity-removal_images/imageFile259.png>)

(δ|A||B|)2 2|A|||B|

= 2exp −δ2|A||B|/2 < 1/4. Also, the expected number of edges changed is

2exp −

![image 260](<2011-conlon-bounds-graph-regularity-removal_images/imageFile260.png>)

|αi,j||Ai||Bj| =

|d(Ai,Bj) − d(A,B)||Ai||Bj| = |A||B|

|d(Ai,Bj) − d(A,B)|piqj

i,j

i,j

i,j

1/2

 

(d(Ai,Bj) − d(A,B))2 piqj

= |A||B|(q(A,B) − q(A,B))1/2 ,

≤ |A||B|



i,j

where pi = |Ai|/|A| and qj = |Bj|/|B| and in the inequality we used the Cauchy-Schwarz inequality. By the Hoeﬀding-Azuma inequality, the probability that the number of edges changed deviates by more than δ|A||B| from its expected value is at most

(δ|A||B|)2 2|A||B|

= 2exp −δ2|A||B|/2 < 1/4.

2exp −

![image 261](<2011-conlon-bounds-graph-regularity-removal_images/imageFile261.png>)

Consider now two subsets A′ ⊂ A and B′ ⊂ B. As (A,B) was initially weak δ-regular, the expected value of e(A′,B′) diﬀers from η|A′||B′| by at most δ|A||B|. By the Hoeﬀding-Azuma inequality, we get that the probability that e(A′,B′) deviates from its expected value by more than δ|A||B| is at most

(δ|A||B|)2 2|A′||B′|

≤ 2exp −δ2|A||B|/2 < 2exp {−4|A|} ≤ 2−|A|−|B|−2,

2exp −

![image 262](<2011-conlon-bounds-graph-regularity-removal_images/imageFile262.png>)

where we use |A| ≥ |B| > 8δ−2. As there are 2|A|+|B| choices for (A′,B′), we get that with probability

- at least 3/4, all pairs (A′,B′) are within 2δ|A||B| edges of having edge density η. To recap, we get that with probability at least 1/4 we made at most δ + (q(A,B) − q(A,B))1/2 |A||B| edge modiﬁcations, d(A,B) = η ± δ and all subsets A′ ⊂ A,B′ ⊂ B are within 2δ|A||B| edges from having edge density η. Hence, there is such a choice for these edge modiﬁcations, and we claim that this implies that the pair (A,B) is 2δ1/3-regular. Indeed, otherwise there would be A′ ⊂ A, B′ ⊂ B, with |A′| ≥ 2δ1/3|A|, |B′| ≥ 2δ1/3|B|, and |d(A′,B′)−d(A,B)| > 2δ1/3, which implies that A′,B′ diﬀers by at least 2δ1/3|A′||B′| ≥ (2δ1/3)3|A||B| = 8δ|A||B| edges from having edge density d(A,B), a contradiction. This completes the proof. ✷ We next use Lemma 6.1 to deduce the regular approximation lemma from Tao’s regularity lemma.


3

Proof: Let δ : N → (0,1) be deﬁned by δ(t) = min g(t)

32t2 ,ǫ/2 . Let ǫ0 = (ǫ/2)2. Let T0 = T0(δ,ǫ0,s) be the bound on the number of parts in Tao’s regularity lemma and T = 16T0/δ(T0)2. If the number n of vertices of the graph G satisﬁes n ≤ T, then we can partition G into parts of size one, and the desired conclusion is satisﬁed in this case. Hence, we may assume n > T. By Tao’s regularity lemma, the graph G has an equitable vertex partition P into t ≥ s parts and an equitable vertex reﬁnement

![image 263](<2011-conlon-bounds-graph-regularity-removal_images/imageFile263.png>)

- Q into at most T0 parts which is weak δ(t)-regular such that q(Q) ≤ q(P) + ǫ0.


For each pair of parts (A,B) of partition P, let A and B denote the partitions of A and B given by

- partition Q. Since Q is a weak δ(t)-regular partition, and A and B have cardinality at least ⌊nt ⌋ ≥ 2nt,


![image 264](<2011-conlon-bounds-graph-regularity-removal_images/imageFile264.png>)

![image 265](<2011-conlon-bounds-graph-regularity-removal_images/imageFile265.png>)

3

then the partitions A and B form a weak 4t2δ(t)-regular partition. Note that 4t2δ(t) ≤ g(t)

8 .

![image 266](<2011-conlon-bounds-graph-regularity-removal_images/imageFile266.png>)

Since |A|,|B| ≥ 2nt > 8/δ(t)2, we may apply Lemma 6.1 to the graph between A and B. That is, we may change at most δ(t) + (q(A,B) − q(A,B))1/2 |A||B| edges across A and B and, in so doing,

![image 267](<2011-conlon-bounds-graph-regularity-removal_images/imageFile267.png>)

1/3

3

make (A,B) a g(t)-regular pair, where we used that g(t) = 2 g(t)

. In total, the number of edges we change to obtain a graph G′ which is g-regular with respect to partition P is at most

![image 268](<2011-conlon-bounds-graph-regularity-removal_images/imageFile268.png>)

8

A,B∈P

δ(t) + (q(A,B) − q(A,B))1/2 |A||B| ≤ (δ(t) + ǫ10/2)n2 ≤ ǫn2,

where we used Jensen’s inequality for the concave function h(x) = x1/2, the inequality q(Q) ≤ q(P)+ǫ0, and the bounds δ(t) ≤ ǫ/2, ǫ0 = (ǫ/2)2. To complete the proof, we recall that the number of parts in partition P is at least s and at most T0 = T0(δ,ǫ0,s). ✷

# 7 Frieze-Kannan weak regularity lemma

In this section we prove Theorem 1.4 which provides a lower bound on the weak regularity lemma. For a vertex partition P : V = V1 ∪ ... ∪ Vk of a graph G = (V,E), let

fP(A,B) = fPG(A,B) = e(A,B) −

d(Vi,Vj)|A ∩ Vi||B ∩ Vj|,

1≤i,j≤k

which is the diﬀerence between the number of edges between A and B and the expected number of edges based on the densities across the pairs of parts of the partition and the intersection sizes of A

- and B with the parts. We call a partition P of the vertex set of a graph G = (V,E) weak ǫ-regular if it satisﬁes


|fP(A,B)| ≤ ǫ|V |2

for all A,B ∈ V . Recall that the weak regularity lemma states that for each ǫ > 0 there is a positive integer k(ǫ) such that every graph has an equitable weak ǫ-partition into at most k(ǫ) parts. Moreover, one may take k(ǫ) = 2O(ǫ−2). We will prove that the number of parts required in the weak regularity lemma satisﬁes k(ǫ) = 2Ω(ǫ−2), thus matching the upper bound.

The following simple lemma of Frieze and Kannan (see Lemma 7(a) of [20]) shows that the notion of weak regularity is robust.

- Lemma 7.1 If a partition is weak ǫ-regular, then any reﬁnement of it is weak 2ǫ-regular.


The robustness of weak regularity described by Lemma 7.1 is not shared by the usual notion of regular partition. For example, for any ﬁxed ǫ > 0 and positive integer t, almost surely any partition into t parts of a uniform random graph on suﬃciently many vertices is ǫ-regular, while any partition of the

vertex set into parts of size 2 is not (ǫ,δ,η)-regular with ǫ = 1, δ = η = 1/2. This is because almost surely in any such partition, between most pairs of parts of size 2, there will be at least one edge and at least one nonedge.

What we will actually prove is the stronger result that any weak ǫ-regular partition must have 2Ω(ǫ−2) parts, whether it is equitable or not. The corresponding regularity lemma, which is an immediate corollary of the usual weak regularity lemma, is the following.

- Lemma 7.2 For each ǫ > 0 there is a positive integer k∗(ǫ) such that every graph G = (V,E) has a vertex partition P with at most k∗(ǫ) parts which is weak ǫ-regular.

In the other direction, the equitable version of the weak regularity lemma also follows from Lemma 7.2. This is because of the robustness property discussed in Lemma 7.1 above, that is, any reﬁnement of a weak ǫ-regular partition is a 2ǫ-regular partition. By arbitrarily reﬁning a not necessarily equitable partition into an equitable partition (except for a small fraction of vertices, which we distribute evenly amongst the other parts), we get an equitable weak 3ǫ-partition whose number of parts is only a factor polynomial in ǫ−1 larger.

In order to prove the lower bound for weak regularity, we will need to perform some further reductions. We ﬁrst state a bipartite variant which can easily be shown to be equivalent to Lemma 7.2. For a bipartite graph G = (U,V,E) with |U| = |V | = n, partitions P1 : U = U1 ∪ ... ∪ Uk and P2 : V = V1 ∪ ... ∪ Vk′, and vertex subsets A ⊂ U and B ⊂ V , let

fP1,P2(A,B) = fPG1,P2(A,B) = e(A,B) −

k

i=1

k′

j=1

d(Ui,Vj)|A ∩ Ui||B ∩ Vj|.

We call the pair of partitions P1,P2 weak ǫ-regular with respect to the bipartite graph G if

|fP1,P2(A,B)| ≤ ǫn2 for all A ⊂ U and B ⊂ V .

- Lemma 7.3 For each ǫ > 0 there is a positive integer k′(ǫ) such that every bipartite graph G =


(U,V,E) with parts of equal size has partitions P1 of U and P2 of V each with at most k′(ǫ) parts which form a weak ǫ-regular partition.

To prove Theorem 1.4, it suﬃces to show k′(ǫ) = 2Ω(ǫ−2). Indeed, this follows from the bound k′(ǫ) ≤ k∗(ǫ/2). This inequality follows from ﬁrst considering a single weak ǫ/2-regular partition P for the bipartite graph G into at most k∗(ǫ/2) parts, and then reﬁning it into a partition P′ with at most 2k∗(ǫ/2) parts based on the intersections of the parts of P with U and V . By Lemma 7.1, P′ is a weak ǫ-regular partition. Letting P1 be the parts of P′ in U and P2 be the parts of P′ in V , the pair P1,P2 form a weak ǫ-regular partition, each with at most k∗(ǫ/2) parts, so that k′(ǫ) ≤ k∗(ǫ/2).

To get a lower bound for the weak regularity lemma, we do not need to show the other direction of the equivalence between the weak regularity lemma and Lemma 7.3, that Lemma 7.3 implies the

weak regularity lemma. However, this is rather simple, so we sketch it here. From a graph G we can consider the bipartite double cover of G, which is the tensor product of G with K2. Applying Lemma

- 7.3, we get a pair P1,P2 of partitions of V (G) which form a weak ǫ/2-regular partition with respect to the bipartite double cover of G. Reﬁning the two partitions P1,P2 of V (G), we get by Lemma 7.1 a weak ǫ-regular partition for G, thus establishing k∗(ǫ) ≤ k′(ǫ/2)2. The following technical lemma will allow us to construct a weighted graph rather than a graph. A similar idea is present in the lower bound construction of Gowers [22] for Szemere´di’s regularity lemma. Let W be a [0,1]-valued n × n matrix. We view W as a weighted graph with parts U and V , where U and V denote the set of columns and rows, respectively, of W. Let eW(A,B) = a∈A,b∈B W(a,b) and dW(A,B) = eW|A(||A,BB| ).


![image 269](<2011-conlon-bounds-graph-regularity-removal_images/imageFile269.png>)

- Lemma 7.4 Let M be an n × n matrix with entries in the interval [0,1]. Let G = (U,V,E) be a bipartite random graph with |U| = |V | = n and edges chosen independently given by M and let


θ = 4n−1/2. With probability at least 1 − e−4n, we have |eM(A,B) − eG(A,B)| ≤ θn2 for every pair of sets A ⊂ U, B ⊂ V .

Proof: Given two vertices u ∈ U and v ∈ V , let a(u,v) be the random variable G(u,v) − M(u,v) (where G has been identiﬁed with its adjacency matrix). The mean of a(u,v) is zero for all u,v and the modulus of a(u,v) is at most 1. Hence, by the Hoeﬀding-Azuma inequality (Theorem 6.1), given two sets A ⊂ U and B ⊂ V , the probability that

a(u,v) ≥ θn2

(u,v)∈A×B

is at most 2exp −(θn2)2/(2|A||B|) ≤ 2exp {−8n}. Summing over all A ⊂ U and B ⊂ V , the probability that there are subsets A ⊂ U and B ⊂ V with |eG(A,B) − eM(A,B)| ≥ θn2 is at most 22n · 2e−8n ≤ e−4n. ✷

For partitions P1 : U = U1 ∪ ... ∪ Uk and P2 : V = V1 ∪ ... ∪ Vk′, let

k′

k

dW(Ui,Vj)|Ui ∩ A||Vj ∩ B|.

fP1,P2(A,B) = eW(A,B) −

i=1

j=1

We say that partitions P1,P2 form a weak ǫ-regular partition of W if |fP1,P2(A,B)| ≤ ǫn2 for all subsets A ⊂ U and B ⊂ V .

- Corollary 7.1 Suppose W = (U,V,E) is an edge-weighted graph with weights in [0,1] and |U| = |V | = n. Let G = (U,V,E) be a bipartite random graph with |U| = |V | = n and edges chosen independently given by W and let θ = 4n−1/2. With probability at least 1 − e−4n, every pair of


partitions P1 : U = U1 ∪ ... ∪ Uk and P2 : V = V1 ∪ ... ∪ Vk′ which form a weak ǫ-partition for G also form a weak (ǫ + 2θ)-regular partition for W.

Proof: By Lemma 7.4, with probability at least 1 − e−4n, we have |eG(A,B) − eW(A,B)| ≤ θn2 for every pair of vertex subsets A ⊂ U and B ⊂ V . Suppose this indeed holds. For graph G, we have

k′

k

fPG1,P2(A,B) = eG(A,B) −

dG(Ui,Vj)|A ∩ Ui||B ∩ Vj|.

j=1

i=1

The ﬁrst term is within θn2 of eW(A,B). The second term is the average of eG(A′,B′) over all subsets A′ ⊂ U and B′ ⊂ V with |A′ ∩ Ui| = |A ∩ Ui| for all i and |B′ ∩ Vj| = |B ∩ Vj| for all j, and hence is within θn2 of the corresponding average of eW(A′,B′) over all of the same pairs (A′,B′). By the triangle inequality, for W, we get that for all A ⊂ U and B ⊂ V , we have |fPW

1,P2(A,B)| ≤ |fPG

1,P2(A,B)|+2θn2 ≤ (ǫ+2θ)n2. Hence, P1,P2 also form a weak (ǫ+2θ)-regular partition for W. ✷

From Corollary 7.1 and the previous remarks, to obtain the desired lower bound in Theorem 1.4 on the number of parts in the weak regularity lemma it suﬃces to prove a lower bound of the form 2Ω(ǫ−2) on the number of parts k0(ǫ) in the following weak regularity lemma for weighted bipartite graphs.

- Lemma 7.5 For each ǫ > 0 there is a positive integer k0(ǫ) such that every edge-weighted bipartite graph G = (U,V,E) with weights in [0,1] and parts of equal size has partitions P1 of U and P2 of V each with at most k0(ǫ) parts which form a weak ǫ-regular partition.


- Lemma 7.5 is also known as the weak matrix regularity lemma. This is because it provides, for any n×n matrix with entries in [0,1], partitions of the rows and columns into a bounded number of parts, such that the sum of the entries in any submatrix (which is the product of a set of rows and columns) is within ǫn2 of what is expected based on the intersections with the parts and the density between the parts. Our goal is to construct a bipartite graph G with edge weights in [0,1] which provides a lower bound

of the form k0(ǫ) = 2Ω(ǫ−2). Suppose 0 < ǫ ≤ 2−50. Consider the following weighted bipartite graph G. The graph has parts U and V each of order n = 22−45ǫ−2. Let r = 2−40ǫ−2 and α = 214ǫ. Consider, for

1 ≤ i ≤ r, equitable partitions U = U0i ∪ U1i and V = V0i ∪ V1i picked uniformly and independently at random. For vertices u ∈ U and v ∈ V , let s(u,v) be the number of i ∈ [r] for which there is j ∈ {0,1}

such that u ∈ Uji and v ∈ Vji, and t(u,v) be the number of i ∈ [r] for which there is j ∈ {0,1} such that u ∈ Uji and v ∈ V1i−j, so that s(u,v) + t(u,v) = r. Let W(u,v) = 21 + (s(u,v) − t(u,v))α. We deﬁne the weight w(u,v) between u and v as follows. If 0 ≤ W(u,v) ≤ 1, then w(u,v) = W(u,v), if W(u,v) < 0, then w(u,v) = 0, and if W(u,v) > 1, then w(u,v) = 1.

![image 270](<2011-conlon-bounds-graph-regularity-removal_images/imageFile270.png>)

Call a pair (u,v) ∈ U × V extreme if |W(u,v) − 1/2| > 1/4, and a vertex u ∈ U nice if it is in at most n/8 pairs (u,v) with v ∈ V which are extreme.

- Lemma 7.6 With probability at least 3/4, all but at most e−100n vertices of U are nice.


Proof: Fix a pair (u,v) ∈ U ×V . The event (u,v) is extreme is the same as |s(u,v)−t(u,v)|α > 1/4, or equivalently that |s(u,v)−r/2| > 81α. The number s(u,v) is a sum of r independent variables, with

![image 271](<2011-conlon-bounds-graph-regularity-removal_images/imageFile271.png>)

values 0 or 1 each with probability 1/2, and hence follows a binomial distribution with mean r/2. By Chernoﬀ’s bound (1), the probability that |s(u,v) − r/2| > 81α is less than 2e−2(1/(8α))2/r = 2e−27. Hence, by linearity of expectation, the expected number of extreme pairs (u,v) ∈ U × V is less than 2e−27n2. Therefore, by Markov’s inequality, the probability that there are at least 8e−27n2 extreme pairs (u,v) is less than 1/4. Since any nice vertex is contained in at most n/8 extreme pairs, we see that with probability at least 3/4, all but at most 64e−27n ≤ e−100n vertices in U are nice. ✷

![image 272](<2011-conlon-bounds-graph-regularity-removal_images/imageFile272.png>)

For h ∈ [r], we let sh(u,v) denote the number of i ∈ [r] \ {h} for which there is j ∈ {0,1} such that

- u ∈ Uji and v ∈ Vji, and th(u,v) be the number of i ∈ [r] \ {h} for which there is j ∈ {0,1} such that u ∈ Uji and v ∈ V1i−j, so that sh(u,v) + th(u,v) = r − 1. Let Wh(u,v) = 12 + (sh(u,v) − th(u,v))α. As above, we deﬁne the weight wh(u,v) by wh(u,v) = Wh(u,v) if 0 ≤ Wh(u,v) ≤ 1, wh(u,v) = 0 if Wh(u,v) < 0, and wh(u,v) = 1 if Wh(u,v) > 1.


![image 273](<2011-conlon-bounds-graph-regularity-removal_images/imageFile273.png>)

- Lemma 7.7 Suppose u ∈ Ujh and we are given |wh(u,v)−1/2| ≤ 1/2−α for at least 78n vertices v ∈ V , and we do not yet know the partition V = V0h∪V1h. Then the probability that dw(u,Vjh)−dw(u,V1h−j) ≥ α/2 is at least 1 − 4rn1 .


![image 274](<2011-conlon-bounds-graph-regularity-removal_images/imageFile274.png>)

![image 275](<2011-conlon-bounds-graph-regularity-removal_images/imageFile275.png>)

Proof: Consider the event E that

wh(u,v) −

wh(u,v) ≥ αn/4.

v∈V1h−j

v∈Vjh

Note that the expected value of the left hand side is 0. Recall that a hypergeometric distribution is at least as concentrated as the sum of independent random variables with the same values (for a proof, see Section 6 of [25]). By the Hoeﬀding-Azuma inequality (Theorem 6.1), the probability of event E is at most

(αn/8)2 2n

1 4rn

= 2exp −2−7α2n ≤

2exp −

,

![image 276](<2011-conlon-bounds-graph-regularity-removal_images/imageFile276.png>)

![image 277](<2011-conlon-bounds-graph-regularity-removal_images/imageFile277.png>)

where in the last inequality we use 0 < ǫ ≤ 2−50, r = 2−40ǫ−2, n = 22−45ǫ−2, and α = 214ǫ.

For a ﬁxed u, if |wh(u,v)−12| ≤ 12−α, then w(u,v) = wh(u,v)+α if v is in Vjh and w(u,v) = wh(u,v)−α if v is in V1h−j. For all v, w(u,v) is within α of wh(u,v). Therefore, letting w(u,S) = s∈S w(u,s), we see, since |wh(u,v) − 12| ≤ 12 − α for at least 87n vertices of v, that

![image 278](<2011-conlon-bounds-graph-regularity-removal_images/imageFile278.png>)

![image 279](<2011-conlon-bounds-graph-regularity-removal_images/imageFile279.png>)

![image 280](<2011-conlon-bounds-graph-regularity-removal_images/imageFile280.png>)

![image 281](<2011-conlon-bounds-graph-regularity-removal_images/imageFile281.png>)

![image 282](<2011-conlon-bounds-graph-regularity-removal_images/imageFile282.png>)

- 7

![image 283](<2011-conlon-bounds-graph-regularity-removal_images/imageFile283.png>)

- 8


1 8

- 3

![image 284](<2011-conlon-bounds-graph-regularity-removal_images/imageFile284.png>)

- 4


1 4

α 2

w(u,Vjh) − w(u,V1h−j) ≥

αn + wh(u,Vjh) − wh(u,V1h−j) ≥

n. The result follows. ✷ Call a nice vertex u ∈ U very nice if for each h ∈ [r] and j ∈ {0,1} with u ∈ Ujh, d(u,Vjh) − d(u,V1h−j) ≥ α/2.

αn −

αn −

αn =

![image 285](<2011-conlon-bounds-graph-regularity-removal_images/imageFile285.png>)

![image 286](<2011-conlon-bounds-graph-regularity-removal_images/imageFile286.png>)

![image 287](<2011-conlon-bounds-graph-regularity-removal_images/imageFile287.png>)

- Corollary 7.2 With probability at least 3/4, every nice vertex u is very nice.


Proof: Given u is nice, then for each h ∈ [r], we must have |Wh(u,v) − 1/2| ≤ 1/2 − α for all but at most 78n vertices v ∈ V . The probability that there is a vertex which is nice but not very nice is by Lemma 7.7 at most rn · 4rn1 ≤ 1/4, which completes the proof. ✷ From Lemma 7.6 and Corollary 7.2, we have the following corollary.

![image 288](<2011-conlon-bounds-graph-regularity-removal_images/imageFile288.png>)

![image 289](<2011-conlon-bounds-graph-regularity-removal_images/imageFile289.png>)

- Corollary 7.3 With probability at least 1/2, the graph G has the following properties.

- • The number of vertices in U which are not nice is at most e−100n.
- • Every nice vertex is very nice.


Consider the random bipartite graph B = B(n,r) with vertex parts U and [r] where i ∈ [r] is adjacent to u ∈ U if u ∈ U0i. By Lemma 2.1 with µ = 1/4, as r ≥ 32log n, we have the following proposition.

- Corollary 7.4 With probability at least 3/4, for each pair u,u′ ∈ U, the number of i for which u and u′ both belong to Uji for some j ∈ {0,1} is less than 43r.


![image 290](<2011-conlon-bounds-graph-regularity-removal_images/imageFile290.png>)

Hence, with probability at least 1/4, the graph G satisﬁes the properties in Corollaries 7.3 and 7.4. Fix such a graph G.

Theorem 7.1 No partitions P1 : U1 ∪ ... ∪ Uk of U and P2 : V1 ∪ ... ∪ Vk′ of V with k ≤ n/2 form a weak ǫ-regular partition. As n/2 ≥ 22−46ǫ−2, we therefore have k0(ǫ) > 22−46ǫ−2 for 0 < ǫ ≤ 2−50.

Theorem 7.1 gives a lower bound on the number k0(ǫ) of parts for the weak matrix regularity lemma (Lemma 7.5) with approximation ǫ. Before we prove this theorem, we remark that it has no restriction on the number of parts of partition P2, and further shows that P1 has to be almost the ﬁnest partition (partition into singletons) to obtain a pair of partitions which are weak ǫ-regular.

Proof: Suppose for contradiction that the partitions P1 and P2 are weak ǫ-regular. That is, |fP1,P2(A,B)| ≤ ǫn2 for all subsets A ⊂ U and B ⊂ V .

Fix for now Ut with |Ut| ≥ 2. Call the pair (i,t) ∈ [r] × [k] useful if |Ut ∩ Uji| ≥ |Ut|/32 for j ∈ {0,1}. Let Mt be the number of i ∈ [r] for which the pair (i,t) is useful. The sum

|Ut ∩ U0i||Ut ∩ U1i| ≤ r|Ut|2/32 + Mt|Ut|2/4

St =

i∈[r]

is precisely the number of triples u,u′,i with u,u′ distinct elements of Ut and i ∈ [r] for which u and u′ are not in the same set in the partition U = U0i ∪ U1i. By Corollary 7.4, the sum St is at least 1 4r |U2t| ≥ |Ut|2r/16. Hence,

![image 291](<2011-conlon-bounds-graph-regularity-removal_images/imageFile291.png>)

r|Ut|2/32 + Mt|Ut|2/4 ≥ St ≥ |Ut|2r/16. We thus have Mt ≥ r/8.

Since Mt ≥ r/8 for each t for which |Ut| ≥ 2 and there are at most k parts in partition P1 of order 1, there is an i for which partition i satisﬁes that at least (n−k)/8 ≥ n/16 vertices u ∈ U are in Ut with the pair (i,t) useful. Fix such an i. For each t for which (i,t) is useful and all but at most |Ut|/64 vertices in Ut are nice, for j ∈ {0,1}, let Ut,j be a subset of Ut ∩ Uji of cardinality exactly ⌈|Ut|/64⌉, and Aj denote the union of all such Ut,j. Recall from Corollary 7.3 that there are at most e−100n vertices in U which are not nice. Hence, there are at most 64 · e−100n vertices in U which belong to a Ut for which the pair (i,t) is useful but there are at least |Ut|/64 vertices in Ut which are not nice. Thus, the number of vertices in U which belong to a Ut for which (i,t) is useful and there are at most |Ut|/64 vertices in Ut which are not nice is at least

n 16 − 64e−100n >

n 32

.

![image 292](<2011-conlon-bounds-graph-regularity-removal_images/imageFile292.png>)

![image 293](<2011-conlon-bounds-graph-regularity-removal_images/imageFile293.png>)

We thus have |A0| = |A1| > 32n /64 = 2−11n. Note that, by construction, we have for each t ∈ [k], ℓ ∈ [k′] and T ⊂ V ,

![image 294](<2011-conlon-bounds-graph-regularity-removal_images/imageFile294.png>)

|A0 ∩ Ut||T ∩ Vℓ|d(Ut,Vℓ) = |A1 ∩ Ut||T ∩ Vℓ|d(Ut,Vℓ). Thus, if the partitions P1,P2 form a weak ǫ-regular partition, we would have to have

|e(A0,Vji) − e(A1,Vji)| ≤ 2ǫn2. (29) for j ∈ {0,1}. However, as each u ∈ A0 is in U0i and is very nice, we have

- d(A0,V0i) − d(A0,V1i) ≥ α/2.

Since |A0| > 2−11n and |Vji| = n/2 for j ∈ {0,1}, we have

- e(A0,V0i) − e(A0,V1i) > 2−13αn2.


Similarly,

e(A1,V1i) − e(A1,V0i) > 2−13αn2. Adding the previous two inequalities, we have

e(A0,V0i) − e(A1,V0i) + e(A1,V1i) − e(A0,V1i) > 2−12αn2. (30)

But, by (29) for j ∈ {0,1}, the left hand side of (30) is at most 4ǫn2 in modulus, contradicting the above inequality and α = 214ǫ. This completes the proof. ✷

Remark: While Theorem 7.1 provides for each ǫ only one graph which requires at least 2Ω(ǫ−2) parts in any weak ǫ-regular pair of partitions, it is a simple exercise to modify the proof to show that all blow-ups of G also satisfy this property, thus obtaining an inﬁnite family of such graphs. For a graph G on n vertices and a positive integer t, the blow-up G(t) of G is the graph on nt vertices obtained by replacing each vertex u by an independent set Iu, and a vertex in Iu is adjacent to a vertex in Iv if and only if u and v are adjacent.

# 8 Concluding remarks

- • Weak regularity lemmas without irregular pairs


While proving his famous theorem on arithmetic progressions in dense subsets of the integers, Szemere´di [39] actually developed a regularity lemma which is weaker than what is now commonly known as Szemere´di’s regularity lemma [40]. The following version is a strengthening of the original version, as it guarantees that all pairs, instead of all but an ǫ-fraction of pairs, under consideration are ǫ-regular. The key extra ingredient is an application of Lemma 5.6 to redistribute the small fraction of vertices which are not in regular sets.

- Lemma 8.1 For each 0 < ǫ < 1/2 there are integers k = k(ǫ) and K = K(ǫ) such that the following holds. For every graph G = (V,E), there is an equitable partition V = V1 ∪ ... ∪ Vt into at most k parts such that for each i, 1 ≤ i ≤ t, there is a partition V = Vi1 ∪ ... ∪ Viji, with ji ≤ K, such that for all 1 ≤ i ≤ t and 1 ≤ j ≤ ji the pair (Vi,Vij) is ǫ-regular. Furthermore, k(ǫ) = 2ǫ−C and K(ǫ) = O(ǫ−1), where C is an absolute constant.

Szemere´di [39] originally gave a triple exponential upper bound on the number of parts in the original regularity lemma, whereas it is now known (see [33]) that the correct bound is single exponential. Through iterative applications, the original regularity lemma was used by Ruzsa and Szemere´di [36] to resolve the (6,3)-problem, and by Szemere´di [38] to establish the upper bound on the Ramsey-Tura´n problem for K4. It is a relatively simple exercise to show that Szemere´di’s original regularity lemma implies the Frieze-Kannan weak regularity lemma, but with a bound that is one exponential worse than the tight bound established in the previous section. This can be accomplished by showing that the common reﬁnement of the partitions in the original regularity lemma satisﬁes the Frieze-Kannan weak regularity lemma.

There are a number of notable properties of Lemma 8.1. First, all pairs (Vi,Vij) under consideration in Lemma 8.1 are regular. In contrast, Theorem 1.1 shows that we must allow for many irregular pairs in Szemere´di’s regularity lemma. Second, the bounds are much better than in Szemere´di’s regularity lemma. The bounds on the number of parts is only single-exponential, instead of the tower-type bound which appears in the standard regularity lemma. Furthermore, each of the partitions of V have at most K(ǫ) = O(ǫ−1) parts. Indeed, this can be established by ﬁrst proving any bound on K(ǫ), and then using the following additive property of regularity to combine parts. Namely, applying Lemma 8.1 with any bound on K(ǫ) and with ǫ2/4 in place of ǫ, and, for each i, partitioning V into O(ǫ−1) parts, each part consisting of the union of parts Vij for which d(Vi,Vij) lies in an interval of length at most ǫ/2, the following lemma shows that Vi together with each part of the new partition forms an ǫ-regular pair.

- Lemma 8.2 Let 0 < ǫ < 1 and α = ǫ2/4. Suppose A,B1,... ,Br are disjoint sets satisfying (A,Bi) is α-regular for 1 ≤ i ≤ r and |d(A,Bi) − d(A,Bj)| ≤ ǫ/2 for 1 ≤ i,j ≤ r. Then, letting B = B1 ∪ ... ∪ Br, the pair (A,B) is ǫ-regular.


To save space, we omit the details of how to prove Lemmas 8.1 and 8.2.

Another interesting consequence of Lemma 8.1 is that it implies that every graph on n vertices has an ǫ-regular pair in which one part is of size Ω(ǫn) and the other part has size 2−ǫ−O(1)n. It is well known (see [27]), that one can ﬁnd an ǫ-regular pair in which both parts have size 2−ǫ−O(1)n. In some applications, having one regular pair is suﬃcient (see, e.g., [16], [24], [27]), and one obtains much better bounds than by applying Szemere´di’s regularity lemma. In the other direction, there are graphs (see Theorem 1.4 in [31] for a tight result) for which any ǫregular pair has a part of size 2−ǫ−Ω(1)n. We can nevertheless guarantee that one part is of size Ω(ǫn). It seems likely that having such a large part in a regular pair could be useful in some applications.

By iterative application of Lemma 8.1, one can also obtain a version of the Duke-Lefmann-R¨dl lemma such that all cylinders in the partition are ǫ-regular. In fact, using Lemma 5.7, one can further guarantee that all cylinders in the partition are strongly ǫ-regular, and the bound is still of constant-tower height.

- • A part irregular with no other parts In the proof of Theorem 1.1, we found a graph G such that for any partition into k parts there are

at least θk parts Vi for which there are at least θ−1ηk pairs (Vi,Vj) which are not (ǫ,δ)-regular, where 0 < θ < 1 is a ﬁxed constant. Is it possible to improve this result so that all parts are in ηk irregular pairs? The answer is no, as Lemma 8.1 implies that any graph has an equitable partition into only 2ǫ−O(1) parts in which one part is ǫ-regular with all the other parts.

- • A single regular subset

It would be interesting to determine tight bounds for the size of the largest ǫ-regular subset which can be found in every graph. In Lemma 5.2, we showed that every graph G = (V,E) must contain an ǫ-regular subset U of size at least 2−ǫ−(10/ǫ)

4

|V |. On the other hand, a result of Peng, Ro¨dl and Rucin´ski [31] implies that there are graphs G = (V,E) which contain no ǫ-regular subset of size ǫcǫ−1|V |. We conjecture that the correct bound is single exponential, though the power may be polynomial in ǫ−1.

- • Equitable partitions and not necessarily equitable partitions


In the regularity lemmas considered in this paper, we often assume the partitions we consider are equitable partitions. It is not diﬃcult to see that this assumption is non-essential and the bounds do not change much. Indeed, consider for example the following variant of Szemere´di’s regularity lemma.

Lemma 8.3 For each ǫ,δ,η > 0 there is a positive integer M = M(ǫ,δ,η) for which the following holds. Every graph G = (V,E) has a vertex partition V = V1 ∪ ... ∪ Vk with k ≤ M such that the sum of |Vi||Vj| over all pairs (Vi,Vj) which are not (ǫ,δ)-regular is at most η|V |2.

The key diﬀerence between this version of Szemere´di’s regularity lemma and the usual statement is that the parts of the partition are not necessarily of equal order, and we measure the regularity of the partition by the sum of the products of the sizes of the pairs of parts that are (ǫ,δ)-regular. Szemere´di’s regularity lemma clearly implies Lemma 8.3, as it further speciﬁes that the partition is an equitable partition, and the condition that the sum of |Vi||Vj| over all pairs (Vi,Vj) which are not (ǫ,δ)-regular is at most η|V |2 is then essentially the same as saying that the number of pairs (Vi,Vj) which are not (ǫ,δ)-regular is at most ηk2. To see that Lemma 8.3 implies Szemere´di’s regularity lemma with similar bounds, ﬁrst apply Lemma 8.3, and then randomly reﬁne each part Vi = Vi0∪Vi1∪...∪Viji into parts of size m = 1001 α2|V |/M, where α = min(ǫ,δ,η), except possibly Vi0, which can have size less than m as not necessarily each Vi has cardinality a multiple of m. The total number of remaining vertices, those in V0 = ki=1 Vi0, is less than km ≤ 1001 α2|V |, as there are less than m remaining vertices from each of the k parts Vi. Redistributing the vertices of V0 evenly among the parts of size m, we get a new equitable partition where each part has size between m and at most (1 + 501 α2)m. It is not hard to show using an additional application of the Frieze-Kannan weak regularity lemma, that because we randomly reﬁned each part, almost surely for all pairs (Vh,Vi) which are (ǫ,δ)-regular, all pairs (Vha,Vij) are (2ǫ,2δ)-regular. That is, the regularity between pairs of parts is almost surely inherited between large vertex subsets. It then easily follows that the equitable partition is similar both in the number of parts and the degree of regularity to the original partition from Lemma 8.3.

![image 295](<2011-conlon-bounds-graph-regularity-removal_images/imageFile295.png>)

![image 296](<2011-conlon-bounds-graph-regularity-removal_images/imageFile296.png>)

![image 297](<2011-conlon-bounds-graph-regularity-removal_images/imageFile297.png>)

Because of this equivalence, we get similar lower bounds for regularity lemmas where the partitions are not necessarily equitable partitions. For example, for Lemma 8.3, for some absolute constants ǫ,δ > 0, we get a bound on M(ǫ,δ,η) which is a tower of 2s of height Ω(η−1). Similarly, in Theorem 1.2 and Corollary 1.1 giving lower bounds on the strong regularity lemma, the assumption that B is an equitable partition is not needed.

Finally, as we have already noted in Section 7, it is much easier to show that for the FriezeKannan weak regularity lemma we do not need to assume that the partition is equitable. This is a simple consequence of the robustness of weak regularity under reﬁnement.

- • Irregular pairs and half graphs

A (generalized) half-graph has vertex set A ∪ B with 2n vertices A = {a1,... ,an} and B = {b1,... ,bn}, in which (ai,bj) is an edge if and only if i ≤ j (but the edges within A and B could be arbitrary). As mentioned in the introduction, any partition of a large half-graph into a constant number of parts has some irregular pairs. Malliaris and Shelah [30] recently showed that for each ﬁxed k, every graph on n vertices with no induced subgraph which is a half-graph on 2k vertices has an ǫ-regular partition with no irregular parts and the number of parts is at most ǫ−ck, where ck is single-exponential in k. This shows that any construction forcing irregular pairs in the regularity lemma, like that given in the proof of Theorem 1.1, must contain large half-graphs, of size double-logarithmic in the number of vertices.

- • Distinct regular approximations


- The notion of f-regularity, which appears in the regular approximation lemma, has since appeared elsewhere. Alon, Shapira, and Stav [9] investigate the question of determining if a graph G = (V,E) can have distinct regular partitions. Two equitable partitions U : U = U1 ∪ ... ∪ Uk and V : V = V1 ∪ ... ∪ Vk into k parts are said to be ǫ-isomorphic if there is a permutation π : [k] → [k] such that for all but at most ǫ k2 pairs 1 ≤ i < j ≤ k, |d(Ui,Uj)−d(Vπ(i),Vπ(j))| ≤ ǫ. They prove that for some f(k) = Θ logk11//33 k and inﬁnitely many k, and for every n > n(k), there is a graph on n vertices with two f-regular partitions which are not 1/4-isomorphic. On the other hand, they show that if f(k) ≤ min(1/k2,ǫ/2), then any two equitable partitions of G into k parts which are each f-regular must be ǫ-isomorphic.
- • Multicolor and directed regularity and removal lemmas

The proof of Szemere´di’s regularity lemma has been extended to give multicolor (see [27]) and directed (see [7]) extensions. These imply multicolor and directed generalizations of the graph removal lemma. As discussed in [18], the new proof of the graph removal lemma with a logarithmic tower height extends with a similar bound to these versions as well. Axenovich and Martin [11] recently extended the strong regularity lemma in a similar fashion to give multicolor and directed versions, in order to establish extensions of the induced graph removal lemma. Our proof of the induced graph removal lemma with a tower-type bound similarly extends to give multicolor and directed versions.

- • On proofs of regularity lemmas


![image 298](<2011-conlon-bounds-graph-regularity-removal_images/imageFile298.png>)

As noted by Gowers, the constructions in [22] not only show that the bound in Szemere´di’s regularity lemma is necessarily large, but that, in some sense, the proof is necessary. Any proof must follow a long sequence of successively ﬁner partitions, each exponentially larger than the previous one. While this notion is hard to make precise, it should be clear to anyone who has studied the proof of the regularity lemma and the lower bound construction of Gowers. Theorem 1.1 adds further weight to this conviction. Furthermore, the proof of Theorem 1.2 shows that any proof of the strong regularity lemma requires a long sequence of partitions, each of tower-type larger than the previous partition. That is, the iterated use of Szemere´di’s regularity lemma is required in any proof of the strong regularity lemma.

Acknowledgment. We would like to thank Noga Alon for helpful comments.

Note added. After this paper was written we learned that a variant of Theorem 1.2 was also proved, independently and simultaneously, by Kalyanasundaram and Shapira. In the situation of Corollary 1.2, their theorem gives a lower bound of wowzer-type in log ǫ−1 for the strong regularity lemma.

![image 299](<2011-conlon-bounds-graph-regularity-removal_images/imageFile299.png>)

# References

- [1] M. Ajtai and E. Szemere´di, Sets of lattice points that form no squares, Stud. Sci. Math. Hungar. 9 (1974), 9–11.


- [2] N. Alon, Testing subgraphs in large graphs, Random Structures Algorithms 21 (2002), 359–370.
- [3] N. Alon, R. A. Duke, H. Lefmann, V. Ro¨dl, and R. Yuster, The algorithmic aspects of the regularity lemma, J. Algorithms 16 (1994), 80–109.
- [4] N. Alon, W. Fernandez de la Vega, R. Kannan, and M. Karpinski, Random sampling and approximation of MAX-CSPs, J. Comput. System Sci. 67 (2003), 212–243.
- [5] N. Alon, E. Fischer, M. Krivelevich, and M. Szegedy, Eﬃcient testing of large graphs, Combinatorica 20 (2000), 451–476.
- [6] N. Alon, E. Fischer, and I. Newman, Eﬃcient testing of bipartite graphs for forbidden induced subgraphs, SIAM J. Comput. 37 (2007), 959–976.
- [7] N. Alon and A. Shapira, Testing Subgraphs in Directed Graphs, J. Comput. System Sci. 69 (2004), 354–382.
- [8] N. Alon and A. Shapira, A characterization of easily testable induced subgraphs. Combin. Probab. Comput. 15 (2006), 791–805.
- [9] N. Alon, A. Shapira, and U. Stav, Can a graph have distinct regular partitions? SIAM J. Discrete Math. 23 (2008/09), 278–287.
- [10] N. Alon and J. H. Spencer, The probabilistic method, 3rd ed., Wiley, 2008.
- [11] M. Axenovich and R. Martin, A version of Szemere´di’s regularity lemma for multicolored graphs and directed graphs that is suitable for induced graphs, arXiv: 1106.2871.
- [12] N. Bansal and R. Williams, Regularity lemmas and combinatorial algorithms, Proceedings of the 50th IEEE FOCS (2009), 745–754.
- [13] B. Bollob´s, The work of William Timothy Gowers, Proceedings of the International Congress of Mathematicians, Vol. I (Berlin, 1998). Doc. Math., Extra Vol. I, 1998, 109–118 (electronic).
- [14] F. R. K. Chung, R. L. Graham, R. M. Wilson, Quasi-random graphs, Combinatorica 9 (1989), 345–362.
- [15] R. A. Duke, H. Lefmann, and V. Ro¨dl, A fast approximation algorithm for computing the frequencies of subgraphs in a given graph. SIAM J. Comput. 24 (1995), 598-620.
- [16] N. Eaton, Ramsey numbers for sparse graphs, Discrete Math. 185 (1998), 63–75.
- [17] P. Erd˝os, P. Frankl, and V. Ro¨dl, The asymptotic number of graphs not containing a ﬁxed subgraph and a problem for hypergraphs having no exponent, Graphs Combin. 2 (1986), 113–121.
- [18] J. Fox, A new proof of the graph removal lemma, Ann. of Math. 174 (2011) 561–579.


- [19] A. Frieze and R. Kannan, The regularity lemma and approximation schemes for dense problems, Proceedings of the 37th IEEE FOCS (1996), 12–20.
- [20] A. Frieze and R. Kannan, Quick approximation to matrices and applications, Combinatorica 19

(1999), 175–220.

- [21] O. Goldreich, S. Goldwasser, and D. Ron, Property testing and its applications to learning and approximation, J. ACM 45 (1998), 653–750.
- [22] W. T. Gowers, Lower bounds of tower type for Szemere´di’s uniformity lemma, Geom. Funct. Anal. 7 (1997), 322–337.
- [23] R. L. Graham, B. L. Rothschild, and J. H. Spencer, Ramsey theory, 2nd edition, John Wiley & Sons (1980).
- [24] P. E. Haxell, Partitioning complete bipartite graphs by monochromatic cycles, J. Combin. Theory Ser. B 69, (1997), 210–218.
- [25] W. Hoeﬀding, Probability inequalities for sums of bounded random variables, J. Amer. Statist. Assoc. 58 (1963), 13–30.
- [26] Y. Kohayakawa and V. Ro¨dl, Szemere´di’s regularity lemma and quasi-randomness, in Recent advances in algorithms and combinatorics, CMS Books Math./Ouvrages Math. SMC, 11, Springer, New York, 2003, 289–351.
- [27] J. Komlo´s and M. Simonovits, Szemere´di’s regularity lemma and its applications in graph theory, in Combinatorics, Paul Erd˝os is eighty, Vol. 2 (Keszthely, 1993), Bolyai Soc. Math. Stud. 2, Ja´nos Bolyai Math. Soc., Budapest, 1996, 295–352.
- [28] M. Krivelevich and B. Sudakov, Pseudo-random graphs, in More sets, graphs and numbers, Bolyai Soc. Math. Stud. 15, Springer, Berlin, 2006, 199–262.
- [29] L. Lov´asz and B. Szegedy, Szemere´di’s lemma for the analyst, Geom. Funct. Anal. 17 (2007), 252–270.
- [30] M. Malliaris and S. Shelah, Regularity lemmas for stable graphs, arXiv:1102.3904.
- [31] Y. Peng, V. Ro¨dl, and A. Rucin´ski, Holes in graphs, Electron. J. Combin. 9 (2002), Research Paper 1, 18 pp. (electronic).
- [32] V. Ro¨dl and M. Schacht, Regular partitions of hypergraphs: regularity lemmas, Combin. Probab. Comput. 16 (2007), 833–885.
- [33] V. Ro¨dl and M. Schacht, Regularity lemmas for graphs, in Fete of Combinatorics and Computer Science, Bolyai Soc. Math. Stud. 20, 2010, 287–325.
- [34] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.


- [35] R. Rubinﬁeld and M. Sudan, Robust characterization of polynomials with applications to program testing, SIAM J. Comput. 25 (1996), 252–271.
- [36] I. Z. Ruzsa and E. Szemere´di, Triple systems with no six points carrying three triangles, in Combinatorics (Keszthely, 1976), Coll. Math. Soc. J. Bolyai 18, Volume II, 939–945.
- [37] J. Solymosi, Note on a generalization of Roth’s theorem, in Discrete and computational geometry, Algorithms Combin. Vol. 25, Ed. Ja´nos Pach, Springer, 2003, 825–827.
- [38] E. Szemere´di, On graphs containing no complete subgraph with 4 vertices, Mat. Lapok 23 (1972), 113–116.
- [39] E. Szemere´di, Integer sets containing no k elements in arithmetic progression, Acta Arith. 27

(1975), 299–345.

- [40] E. Szemere´di, Regular partitions of graphs, in Colloques Internationaux CNRS 260 - Proble`mes Combinatoires et The´orie des Graphes, Orsay (1976), 399–401.
- [41] T. Tao, Szemere´di’s regularity lemma revisited, Contrib. Discrete Math. 1 (2006), 8–28.
- [42] A. G. Thomason, Pseudorandom graphs, in Random graphs ’85 (Poznan´, 1985), North-Holland Math. Stud. Vol. 144, North-Holland, Amsterdam, 1987, 307–331.


