arXiv:1309.4518v1[math.CO]18Sep2013

On generalized Ramsey numbers for 3-uniform hypergraphs

Andrzej Dudek∗ Dhruv Mubayi†‡

January 18, 2020

Abstract

The well-known Ramsey number r(t,u) is the smallest integer n such that every Ktfree graph of order n contains an independent set of size u. In other words, it contains a subset of u vertices with no K2. Erdo˝s and Rogers introduced a more general problem replacing K2 by Ks for 2 ≤ s < t. Extending the problem of determining Ramsey numbers they deﬁned the numbers

fs,t(n) = min max{|W| : W ⊆ V (G) and G[W] contains no Ks} ,

where the minimum is taken over all Kt-free graphs G of order n. In this note, we study an analogous function fs,t(3)(n) for 3-uniform hypergraphs. In particular, we show that there are constants c1 and c2 depending only on s such that

c1(log n)1/4

log log n log log log n

![image 1](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile1.png>)

1/2

< fs,s(3)+1(n) < c2 log n.

# 1 Introduction

A hypergraph G is a pair (V,E) such that V = V (G) is a set of vertices and E ⊆ 2V is a set of hyperedges. A k-uniform hypergraph (also called a k-graph) is a hypergraph such

that all its hyperedges have size k. Denote by Kt(k) the complete k-uniform hypergraph of order t. Let the Ramsey number r(k)(t,u) denote the smallest integer n such that any

red-blue coloring of the edges of Kn(k) yields a red copy of Kt(k) or a blue copy of Ku(k). It is well-known due to a result of Ramsey [15] that such numbers are ﬁnite. In other words,

r(k)(t,u) is the smallest integer n such that every Kt(k)-free hypergraph of order n contains an independent set of size u, or equivalently, it contains a u-subset of vertices with no Kk(k). One can consider a more general problem replacing Kk(k) by Ks(k) for some k ≤ s < t. For ﬁxed integers k ≤ s < t let

fs,t(k)(n) = min max{|W| : W ⊆ V (G) and G[W] contains no Ks(k)} ,

![image 2](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile2.png>)

∗Department of Mathematics, Western Michigan University, Kalamazoo, MI 49008, andrzej.dudek@wmich.edu

†Department of Mathematics, Statistics, and Computer Science, University of Illinois at Chicago, Chicago, IL 60607, mubayi@math.uic.edu

‡Research partially supported by NSF grant DMS-0969092

where the minimum is taken over all Kt(k)-free k-uniform hypergraphs G of order n. To prove the lower bound fs,t(k)(n) ≥ a one must show that every Kt(k)-free k-graph of order n contains a subset of a vertices with no copy of Ks(k). To prove the upper bound fs,t(k)(n) < b one must construct a Kt(k)-free k-graph of order n such that every subset of b vertices contains a copy of Ks(k).

As we already observed the problem of determining fs,t(k)(n) extends that of ﬁnding Ramsey numbers. Formally,

r(k)(t,u) = min{n : fk,t(k)(n) ≥ u}.

For graphs (i.e. k = 2) the above function was ﬁrst considered by Erd˝os and Rogers [11] only for t = s+1, which might be viewed as the most restrictive case. Since then the function has been studied by several researchers including Alon, Bollob´s, Dudek, Erd˝os, Gallai, Hind, Krivelevich, Retter, Ro¨dl, Sudakov, and Wolfovitz [1, 3, 6, 7, 8, 9, 13, 14, 18, 19, 20]. All logs in this paper are to the base e. For any s ≥ 3 the best published bounds are of the form

Ω (nlog log n)1/2 = fs,s(2)+1(n) = O (log n)4s2n1/2 , (1) where the lower bound comes from [14] and the upper bound from [6]. However, using the result due to Shearer [17], that an n-vertex Ks-free graph with average degree d has an independent set of size at least

log d log log d

n d

, we can immediately improve the lower bound in (1) to a new bound Ω

Ω

![image 3](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile3.png>)

![image 4](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile4.png>)

1/2

nlog n log log n

. (2)

![image 5](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile5.png>)

Indeed, if there is a vertex of degree at least (log lognlognn)1/2 in a Ks+1-free graph, then its neighborhood is Ks-free and we are done. Otherwise, the average degree is less than (log lognlognn)1/2 and by the Shearer result there is an independent set of size bounded from below by (2).

![image 6](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile6.png>)

![image 7](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile7.png>)

In this note we extend the previous results to 3-uniform hypergraphs and show the following bounds. Theorem 1.1 For all integers 3 ≤ s < t and every n

fs(2)−1,t−1 ⌊ log n⌋ ≤ fs,t(3)(n) ≤ C log n, where C is a positive constant depending only on s.

![image 8](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile8.png>)

In particular, for t = s + 1 the above theorem together with (2) implies that there are positive constants c1 and c2 depending only on s such that

c1(log n)1/4

log log n log log log n

![image 9](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile9.png>)

1/2

< fs,s(3)+1(n) < c2 log n.

# 2 General upper bound

For s ≥ k ≥ 3, we show that there is a Ks(+1k) -free k-graph G such that any subset of its vertices of size C(log n)1/(k−2) (for some C = C(k,s)) contains Ks(k). This will imply that

fs,s(k)+1(n) ≤ C(log n)1/(k−2). (3) Moreover, since for any t ≥ s + 1

fs,t(k)(n) ≤ fs,s(k)+1(n), setting k = 3 will yield the upper bound in Theorem 1.1.

The following construction has some similarities to the approach taken by Conlon, Fox and Sudakov in the proof of Theorem 3.1 in [4]. Let χ : k [−n]1 → [s − k +2] be a coloring of all (k − 1)-tuples chosen uniformly at random from all (s − k + 2)-colorings of k [−n]1 . That means every (k −1)-tuple is colored with one particular color with probability 1/(s−k +2) independently of all other (k−1)-tuples. Now we construct G = G(χ). Let V = {1,2,... ,n} be the vertex set of G. The set of hyperedges consists of all k-tuples e = {u1 < ··· < uk−1 < uk} for which χ(e \ uk) = χ(e \ uk−1).

First observe that G is Ks(+1k) -free. Indeed, let {v1 < v2 < ··· < vs+1} be a set of

vertices inducing a clique Ks(+1k) . Then, in particular, all k-tuples {v1 < ··· < vk−1 < vi} for k ≤ i ≤ s + 1 must be present. Hence, all s − k + 3 of the numbers χ(v1,... ,vk−2,vi), k − 1 ≤ i ≤ s + 1, must be pairwise diﬀerent. Clearly, this gives a contradiction, since we only have s − k + 2 colors.

Now note that with a positive probability, say p, which does not depend on n, any ﬁxed set S = {v1 < v2 < ··· < vs} of vertices will induce Ks(k). Indeed, it suﬃces to observe that if for each {vj1 < ··· < vjk−1} ∈ k− S1

χ(vj1,... ,vjk−1) = jk−1 − k + 2, then every k-tuple of S is present.

Let C(k−1,s,W) be a maximum collection of s-sets of set W such that no (k−1)-set in W is covered more than once. Denote its size by c(k −1,s,W). Due to a result of Ro¨dl [16] (see also Section 4.7 in [2]) it is known that

c(k − 1,s,W)

= 1,

lim

![image 10](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile10.png>)

|W| k−1 / k− s1

|W|→∞

hence, c(k − 1,s,W) = Θ(|W|k−1).

For a ﬁxed subset S ⊆ V of size s let AS be the event that G[S] is a clique of size s. As we already observed

Pr(AS) = p for some 0 < p < 1. Let W of size w be a subset of vertices of V . Thus,

 ≤ Pr  S∈C(k−1,s,W)

Pr  S⊆W

A¯S

A¯S

.

Moreover, since for all diﬀerent S and S′ in C(k−1,s,W), |S∩S′| ≤ k−2, and consequently, all events AS for S ∈ C(k − 1,s,W) are mutually independent. Thus,

Pr  S⊆W

A¯S

Pr(A¯S) = (1 − p)Θ(wk−1)

 ≤

S∈C(k−1,s,W)

and hence, the union bound yields

Pr  W⊆V S⊆W

A¯S

n w

(1 − p)Θ(wk−1) < 1

 ≤

provided that w = Ω((log n)1/(k−2)). Thus, there is a coloring χ and a constant C = C(k,s) such that every subset of C(log n)1/(k−2) of vertices in G(χ) contains a clique of size s, as required.

# 3 Lower bound for 3-graphs

In this section we prove the lower bound from Theorem 1.1. We show that every Kt(3)-free 3-graph G of order n contains a subset of fs(2)−1,t−1(⌊

√log n⌋)

![image 11](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile11.png>)

vertices with no copy of Ks(3). In order to do it, we will adapt the classical approach of Erd˝os and Rado [10] (see also Section 1.2 in [12]) for ﬁnding an upper bound on Ramsey numbers.

Given n, choose m such that

2m2 ≤ n < 2m2+1. (4)

Let G = (V,E) be a Kt(3)-free 3-graph of order n. Denote the complement of E (i.e. the set of all triples which are not in E) by Ec. We will greedily construct a sequence A =

{v1,... ,vm,vm+1} ⊆ V such that for any given pair 1 ≤ i < j ≤ m all triples {vi,vj,vk} with j < k ≤ m + 1 are in E or all of them are in Ec. Assume for a while that we can construct such a sequence A. Let G be a graph on set {v1,... ,vm} such that {vi,vj}, i < j, is an edge if and only if all triples {vi,vj,vk} with j < k ≤ m + 1 are in E. First observe that G is Kt−1-free graph. Otherwise, if S is a set of vertices of G that induces Kt−1, then S ∪ {vm+1} induces a clique Kt(3) in G, a contradiction.

Since G is Kt−1-free, we can ﬁnd a subset W of at least fs(2)−1,t−1(m) vertices with no Ks−1. Now it is not diﬃcult to see that the subhypergraph induced by W in G contains no Ks(3). Otherwise, let S ⊆ W be a set of size s such that G[S] is a clique Ks(3). Moreover, let v ∈ S be a vertex which appears latest in sequence A compared to other vertices in S. Then S \ v ⊆ W induces a clique Ks−1 in G, a contradiction.

We just showed that every Kt(3)-free graph G of order n satisfying (4) has a subhypergraph of order at least

fs(2)−1,t−1(m) with no Ks(3). Since n < 2m2+1, we see that m > √log n as desired.

![image 12](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile12.png>)

It remains to show how to construct sequence A, and this is the argument of Erd˝os and Rado. Pick any vertex v1 of V = V (G). Set V1 = V \ {v1}. Assume that we already picked {v1,... ,vi} and set Vi such that all triples {va,vb,w} with 1 ≤ a < b ≤ i and w ∈ Vi are in E or all are in Ec. Choose any vertex from Vi, say vi+1. Now we show how to deﬁne Vi+1 such that |Vi+1| ≥ (|Vi| − 1)/2i and all triples {va,vb,w} with 1 ≤ a < b ≤ i + 1 and w ∈ Vi+1 are in E or all are in Ec. Let Vi,0 = Vi \ {vi+1}. Suppose we already constructed Vi,j ⊆ Vi,0 such that all triples {va,vi+1,w} with 1 ≤ a ≤ j and w ∈ Vi,j are in E or all are in Ec. If the number of triples {vj+1,vi+1,w} in E with w ∈ Vi,j is at least |Vi,j|/2, then we set

Vi,j+1 = {w : {vj+1,vi+1,w} ∈ E and w ∈ Vi,j}, otherwise we set

Vi,j+1 = {w : {vj+1,vi+1,w} ∈ Ec and w ∈ Vi,j}.

Finally, we put Vi+1 = Vi,i and continue the algorithm until A of size m + 1 is chosen. This is possible, since |Vi| ≥ 1 for all 1 ≤ i ≤ m. Indeed,

|Vm−1| 2m ≥

|Vm−2| 2m2m−1 ≥

|V1| 2m2m−1 ··· 22

n − 1

|Vm−1| − 1 2m−1 ≥

=

|Vm| ≥

2(m+2)(m−1)/2 ≥ 1, since n ≥ 2m2.

![image 13](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile13.png>)

![image 14](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile14.png>)

![image 15](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile15.png>)

![image 16](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile16.png>)

![image 17](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile17.png>)

# 4 Concluding remarks

It seems natural to try to extend the above results for arbitrary k ≥ 4. A similar approach to the one taken in Section 3 and inequality (3) yield

n)1/4 ≤ fs,s(k)+1(n) ≤ c2(log n)1/(k−2) (5)

c1(log log ... log

![image 18](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile18.png>)

![image 19](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile19.png>)

k−2

for some positive constants c1 and c2 depending only on k and s. This big discrepancy could be possibly removed by strengthening the upper bound. Analogously to the problem of estimating the Ramsey numbers for hypergraphs one could apply some variation of the stepping-up lemma of Erd˝os and Hajnal (see, e.g., Section 4.7 in [12]). Unfortunately, it is not obvious how to use this idea.

Recently, Conlon, Fox and Sudakov [5] slightly improved the lower bound in (5) and showed that

n)1/3−o(1) ≤ fs,s(k)+1(n).

(log log ... log

![image 20](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile20.png>)

![image 21](<2013-dudek-generalized-ramsey-numbers-uniform_images/imageFile21.png>)

k−2

# References

- [1] N. Alon and M. Krivelevich, Constructive bounds for a Ramsey-type problem, Graphs Combin. 13 (1997), 217–225.
- [2] N. Alon and J. Spencer, The Probabilistic Method, third ed., Wiley, New York, 2008.


- [3] B. Bollob´s and H. R. Hind, Graphs without large triangle free subgraphs, Discrete Math. 87 (1991), no. 2, 119–131.
- [4] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23 (2010), no. 1, 247–266.
- [5] D. Conlon, J. Fox, and B. Sudakov, Essays in extremal combinatorics, submitted.
- [6] A. Dudek, T. Retter, and V. Ro¨dl, On generalized Ramsey numbers of Erdo˝s and Rogers, submitted.
- [7] A. Dudek and V. Ro¨dl, On Ks-free subgraphs in Ks+k-free graphs and vertex Folkman numbers, Combinatorica 31 (2011), 39–53.
- [8] A. Dudek and V. Ro¨dl, On the function of Erdo˝s and Rogers, in Ramsey Theory: Yesterday, Today and Tomorrow, edited by Alexander Soifer, Progress in Mathematics, vol. 285, Springer-Birkh¨auser, 2010, pp. 63–76.
- [9] P. Erd˝os and T. Gallai, On the minimal number of vertices representing the edges of a graph, Publ. Math. Inst. Hungar. Acad. Sci. 6 (1961), 181–202.
- [10] P. Erd˝os and R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. London Math. Soc. 3 (1952), 417–439.
- [11] P. Erd˝os and C.A. Rogers, The construction of certain graphs, Canad. J. Math. 14

(1962), 702–707.

- [12] R. Graham, B. Rothschild, and J. Spencer, Ramsey Theory, Wiley, New York, 1990.
- [13] M. Krivelevich, Bounding Ramsey numbers through large deviation inequalities, Random Structures Algorithms 7 (1995), 145–155.
- [14] M. Krivelevich, Ks-free graphs without large Kr-free subgraphs, Combin. Probab. Comput. 3 (1994), 349–354.
- [15] F. Ramsey, On a problem of formal logic, Proc. Lond. Math. Soc. 30 (1930), 264–286.
- [16] V. Ro¨dl, On a packing and covering problem, European J. Combin. 6 (1985), 69–78.
- [17] J.B. Shearer, On the independence number of sparse graphs, Random Structures Algorithms 7 (1995), 269–271.
- [18] B. Sudakov, A new lower bound for a Ramsey-type problem, Combinatorica 25 (2005), 487–498.
- [19] B. Sudakov, Large Kr-free subgraphs in Ks-free graphs and some other Ramsey-type problems, Random Structures Algorithms 26 (2005), 253-265.
- [20] G. Wolfovitz, K4-free graphs without large induced triangle-free subgraphs, to appear in Combinatorica.


