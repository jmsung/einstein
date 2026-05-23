ORDERED RAMSEY NUMBERS OF LOOSE PATHS AND MATCHINGS

CHRISTOPHER COX1 AND DERRICK STOLEE1

arXiv:1411.4058v2[math.CO]4Dec2014

Abstract. For a k-uniform hypergraph G with vertex set {1, . . . , n}, the ordered Ramsey number ORt(G) is the least integer N such that every t-coloring of the edges of the complete k-uniform graph on vertex set {1, . . . , N} contains a monochromatic copy of G whose vertices follow the prescribed order. Due to this added order restriction, the ordered Ramsey numbers can be much larger than the usual graph Ramsey numbers. We determine that the ordered Ramsey numbers of loose paths under a monotone order grows as a tower of height one less than the maximum degree. We also extend theorems of Conlon, Fox, Lee, and Sudakov [Ordered Ramsey numbers, arXiv:1410.5292] on the ordered Ramsey numbers of 2-uniform matchings to provide upper bounds on the ordered Ramsey number of k-uniform matchings under certain orderings.

1. Introduction

Ramsey theory is a fundamental topic in extremal graph theory. The Ramsey number Rt(n) is the minimum N such that every t-coloring of the edges of the complete graph of order N contains a monochromatic clique of order n. The number Rt(n) can also be deﬁned as the maximum N such that there exists a t-coloring of KN−1 that avoids monochromatic copies of the graph Kn. This concept naturally generalizes to avoiding monochromatic copies of any k-uniform hypergraph G, deﬁning the graph Ramsey number Rt(G), leading to a large number of available questions. The asymptotic growth of Rt(G) varies signiﬁcantly, and depends on several properties of G, such as maximum degree [2] or degeneracy [10].

A recent variation, called ordered Ramsey theory, has received signiﬁcant attention [1, 4, 6, 9, 12, 13]. In this variation, we again look for t-colorings of the complete graph that avoid monochromatic copies of a graph G, except that the order of the vertices of G in this monochromatic copy are very important. This modiﬁcation relaxes some of the constraints on the coloring, so the ordered Ramsey numbers can be much larger than the usual graph Ramsey number, but is still bounded from above by the Ramsey number Rt(n) where n is the number of vertices in G. If G is a 2-uniform path under the standard ordering, then the 2-color ordered Ramsey number of G is equal to the bound of the Erd˝os-Szekeres Theorem [8] (see [3, 12]). If G is a tight 3-uniform path under the standard ordering, then the 2-color ordered Ramsey number of G is equal to the bound of the happy ending problem (see [9]). Due to these connections, much of the previous work has focused on the ordered Ramsey number of tight k-uniform paths under the standard ordering [9, 12, 13], but others considered 2-uniform matchings with an arbitrary ordering [1, 6]. We extend these investigations by determining strong bounds on the ordered Ramsey number of loose k-uniform paths and k-uniform matchings, using an arbitrary number of colors.

An ordered k-uniform hypergraph is a hypergraph G where the edge set E(G) contains k-sets of vertices, and the vertex set V (G) is totally ordered. An ordered hypergraph G is contained in an ordered hypergraph H if there is an injective, order-preserving map from the vertices of G to the vertices of H such that edges of G map to edges of H. Let KNk be the complete k-uniform hypergraph on the vertex set {1,... ,N} and let c : E(KNk ) → {1,... ,t} be a t-coloring of the edges

![image 1](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile1.png>)

Date: October 20, 2021. 1Iowa State University, Ames, IA, USA. {cocox,dstolee}@iastate.edu.

1

in KNk . The i-colored subgraph of KNk is the ordered hypergraph given by the edges in c−1(i). For ordered k-uniform hypergraphs G1,... ,Gt, the ordered Ramsey number OR(G1,... ,Gt) is the minimum N such that for every t-coloring of KNk there is some color i such that the i-colored subgraph contains Gi. This number is necessarily deﬁned and ﬁnite, since there exists an n such that each Gi is a subgraph of Knk and hence OR(G1,... ,Gt) ≤ Rt(n). If G1 = ··· = Gt = G, then we denote OR(G1,... ,Gt) as ORt(G) and refer to this as the diagonal case; otherwise it is the oﬀ-diagonal case.

For positive integers k,ℓ,e such that k > ℓ, the (k,ℓ)-path on e edges, denoted Pek,ℓ, is the k-uniform ordered hypergraph on e(k − ℓ) + ℓ vertices and e totally-ordered edges A1,A2,... ,Ae where two consecutive edges Ai,Ai+1 intersect exactly on the maximum ℓ vertices in Ai and the minimum ℓ vertices in Ai+1. The path Pek,k−1 is called the tight k-uniform path and otherwise Pek,ℓ is a loose path. For ℓ = 0, we can extend the deﬁnition of Pek,ℓ by requiring that two consecutive edges Ai,Ai+1 satisfy maxAi < min Ai+1, and hence the edges are disjoint, forming a matching. Note that when k = 2 the only possibilities are a tight path or a matching. We will primarily use the ordering given by this deﬁnition, and we will specify the special cases when we will consider a possibly diﬀerent ordering on Pek,ℓ.

Deﬁne the intersection number, i(k,ℓ), to be the maximum degree of a vertex in Pek,ℓ for all e ≥ k. Observe that if ℓ > 0, then i(k,ℓ) is the unique integer m ≥ 2 that satisﬁes

m − 1 m

m − 2 m − 1

ℓ k ≤

<

.

![image 2](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile2.png>)

![image 3](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile3.png>)

![image 4](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile4.png>)

The tight paths Pek,k−1 have been investigated thoroughly. For 2-uniform tight paths, the ordered Ramsey number ORt(Pe2,1) is determined by Choudum and Ponnusamy [3], and the oﬀ-diagonal case of the number OR(Pe21,1,... ,Pe2t,1) is demonstrated in full generality by Milans, Stolee, and West [12]. Fox, Pach, Sudakov, and Suk [9] determined the growth of ORt(Pe3,2) to be doubly-exponential, and Moshkovitz and Shapira [13] found that ORt(Pek,k−1) grows as a tower of height k − 1. In fact, Moshkovitz and Shapira determine ORt(Pek,k−1) exactly in terms of high-dimensional integer partitions. In Section 2, we use a version of this theorem using partially-ordered sets (posets), due to Milans, Stolee, and West [12], in order to prove the following relationship between ordered Ramsey numbers of tight and loose paths.

- Theorem 1.1. For k > ℓ ≥ 1, i = i(k,ℓ), and positive integers e1,... ,et, OR(Pek,ℓ1 ,... ,Pek,ℓt ) = (k − ℓ)OR(Pei,i1 −1,... ,Pei,it −1) + ℓ − (k − ℓ)(i − 1).


Therefore, the asymptotic growth of ORt(Pek,ℓ) is a tower of height i(k,ℓ) − 1. In particular, when i(k,ℓ) = 2 we can use the exact theorem for 2-uniform tight paths to exactly determine the ordered Ramsey number.

- Corollary 1.2. For 0 < 2ℓ ≤ k and positive integers e1,... ,et,


t

OR(Pek,ℓ1 ,... ,Pek,ℓt ) = (k − ℓ)

ei + ℓ.

i=1

Conlon, Fox, Lee, and Sudakov [6] and Balko, Cibulka, Kra´l, and Kync˘l [1] independently investigated how the ordered Ramsey number ORt(G) diﬀers among orderings of a 2-uniform graph G. In particular, they investigated upper bounds of ORt(M) for a 2-uniform matching M, and found that these upper bounds are nearly sharp. In Section 3, we extend the methods in these papers to attain upper bounds on the ordered Ramsey numbers of k-uniform matchings under certain “controlled” orderings. We present an upper bound on the t-color ordered Ramsey number ORt(Pe2,1) for an arbitrarily-ordered copy of Pe2,1 that nearly matches the upper bound on ORt(M) for a 2-uniform

matching M, extending work of Cibulka, Gao, Krcˇ´l, Valla, and Valtr [4] on two colors. Several conjectures and open problems are presented in Section 4.

1.1. Notation. We follow standard notation from [15]. For an (ordered) hypergraph G, we use V (G) as the vertex set of G, E(G) as the edge set of G, |G| as the number of edges in G, and k will always denote the size of an edge in G. For integers m ≤ n, let [n] = {1,... ,n}, [m,n] =

{m,m + 1,... ,n − 1,n}, and let [mn] denote the set of m-element subsets of [n]. For k ≥ 2, the complete k-uniform (ordered) hypergraph with vertex set [N] is denoted KNk . The 2-uniform case is special, so KN denotes KN2 .

We use lg n = log2 n. We always use e the number of edges in a graph and never as the base of the natural logarithm. The tower function of height t, denoted by towt(n), is

tow0(n) = n, and towt(n) = 2towt−1(n) for t ≥ 1. We use ⊆ to denote any partial order, including the containment order. We use ≤ to denote a total order, including a linear extension of a partial order. A list (x1,... ,xn) is descent-free if xi  ⊇ xi+1 for all i ∈ [n − 1]. Note that any sublist of a linear extension is descent-free.

2. Ordered Ramsey Numbers of Loose Paths

To study the ordered Ramsey number of loose paths, we ﬁrst review the previous results on the ordered Ramsey number of tight paths. For a poset P = (P,⊆), a down-set is a set S ⊆ P such that if y ∈ S and x ⊆ y, then x ∈ S. For a set A ⊆ P, let D(A) be the minimal down-set containing A; observe that D forms a bijection between antichains and down-sets of P. The poset J(P) consists of all down-sets in P, ordered by containment.

Let m,e1,... ,et be positive integers and m ≥ 1. Deﬁne the poset Qm(e1,... ,et) iteratively as follows: let Q1(e1,... ,et) be a disjoint union of t chains of size e1−1,... ,et−1, and Qm+1(e1,... ,et) = J(Qm(e1,... ,et)). The size of Qk(e1,... ,et) is equal to the largest N such that we can t-color KNk while avoiding ordered copies of Pek,k1 −1,... ,Pek,kt −1.

- Theorem 2.1 (Moshkovitz and Shapira [13]; Milans, Stolee, and West [12]). Let k,e1,... ,et be positive integers and k ≥ 2. Then,


OR(Pek,k1 −1,... ,Pek,kt −1) = |Qk(e1,... ,et)| + 1. We extend this result to loose paths by referring to the same poset deﬁnitions. In particular, the most important parameter aﬀecting the asymptotic growth of ORt(Pek,ℓ) is i(k,ℓ), and the value k contributes only to the leading constant.

Theorem 2.2. If k > ℓ ≥ 1 and e1,... ,et are positive integers, then OR(Pek,ℓ1 ,... ,Pek,ℓt ) = (k − ℓ)|Qi(k,ℓ)(e1,... ,et)| + ℓ − (k − ℓ)(i(k,ℓ) − 2).

Proof. Note that if ei = 1 for any i, then any t-coloring avoiding an i-colored copy of P1k,ℓ will not use the color i; hence ei can be removed from the list and we can consider t−1 coloring. Also note that Q1(e1,... ,et) equals Q1(e′1,... ,e′t′) where e′1,... ,e′t′ is the list of integers ej ≥ 2 for j ∈ [t]. Let i = i(k,ℓ) and ℓ′ = ℓ − (k − ℓ)(i − 2). For m ∈ [i], let Qm = Qm(e1,... ,et). Let C1 ∪ ··· ∪ Ct be a partition of Q1 into a disjoint union of t chains such that each Cj contains ej − 1 elements.

Let A1,... ,Ak−ℓ be copies of Qi and let π : j k=1−ℓ Aj → Qi be the natural projection map. Also, let L be a chain of size ℓ′ − 1. Deﬁne Q∗i = A1 ∪ ··· ∪ Ak−ℓ ∪ L to be a poset with the relation between two distinct elements x,y ∈ Q∗i deﬁned as:

- • If x,y ∈ L, keep the same relation as in L.


- • If x ∈ Aj and y ∈ L, let x < y.
- • If x ∈ Aj and y ∈ Aj′, where π(x) = π(y), provide x and y with the same relationship as π(x) and π(y).
- • If x ∈ Aj and y ∈ Aj′, where π(x) = π(y), let x ≤ y if j ≤ j′.


We show that OR(Pek,ℓ1 ,... ,Pek,ℓt ) = |Q∗i| + 1.

Lower Bound. Fix a linear extension of Q∗i . We consider π to be a a projection from Q∗i \ L → Qi. For a list (x1,... ,xn) in Q∗i \ L, we extend π so that π(x1,... ,xn) = (π(x1),... ,π(xn)). Further, given a list (x1,... ,xn) in Q∗i, we deﬁne the reduction of the list to be r(x1,... ,xn) = (x1,x(k−ℓ)+1,... ,xs(k−ℓ)+1) where s is the largest integer such that s(k − ℓ) + 1 ≤ n.

Notice ﬁrst that r(x1,... ,xs(k−ℓ)+ℓ) = (x1,x(k−ℓ)+1,... ,x(k−ℓ)(s+i−2)+1) and that ℓ′ = (s(k − ℓ) + ℓ) − (k − ℓ)(s + i − 2). Hence, if (x1,... ,xs(k−ℓ)+ℓ) is a sublist of the linear extension of Q∗i, then r(x1,... ,xs(k−ℓ)+ℓ) is a descent-free list in Q∗i \ L.

Note that in this linear extension of Q∗i, if x ∈ Aj and y ∈ Aj+1 with π(x) = π(y), then there is no z ∈ Q∗i such that x < z < y. Therefore, if (x1,... ,xs(k−ℓ)+ℓ) is a descent-free list in Q∗i, then not only is r(x1,... ,xs(k−ℓ)+ℓ) a descent-free list in Q∗i \ L, but π(r(x1,... ,xs(k−ℓ)+ℓ)) is a descent-free list with no repetition in Qi.

Now, consider 2 ≤ m ≤ i and let x,y ∈ Qm with x y. Let fm(x,y) be some element of the set y \ x inside of Qm−1. Further, we extend fm so that if (x1,... ,xn) is a descent-free list in Qm, then fm(x1,... ,xn) = (fm(x1,x2),... ,fm(xn−1,xn)). If x y and y z, then fm(x,y) ∈ y \ x and fm(y,z) ∈ z \y, so fm(x,y) fm(y,z). Hence, if (x1,... ,xn) is a descent-free list in Qm, then fm(x1,... ,xn) is a descent-free list of length n−1 in Qm−1. For a decent-free list (x1,... ,xn) in Qi, deﬁne f(0)(x1,... ,xn) = fi(x1,... ,xn) and f(h)(x1,... ,xn) = fi−h(f(h−1)(x1,... ,xn)). Observe that if (x1,... ,xn) is a descent-free list of length n in Qi, then f(h)(x1,... ,xn) is a descent-free list of length n − h in Qi−h.

For a descent-free list (x1,... ,xk) in Q∗i, let (y1,... ,yi) be deﬁned as (y1,... ,yi) = (π(x1),π(x(k−ℓ)+1),... ,π(x(k−ℓ)(i−1)+1)) = π(r(x1,... ,xk)). Observe that (y1,... ,yi) is a descent-free list in Qi, so f(i−1)(y1,... ,yi) is an element in Q1.

For N = |Q∗i |, deﬁne a t-coloring c on E(KNk ) as c(x1,... ,xk) = j whenever f(i−1)(y1,... ,yi) ∈ Cj, for (y1,... ,yi) = π(r(x1,... ,xk)). We now demonstrate that the coloring c avoids a j-colored Pek,ℓj for all colors j ∈ [t].

Suppose that (x1,... ,xs(k−ℓ)+ℓ) is the vertex set of a j-colored copy of Psk,ℓ for some s ≥ 1. Let

(y1,... ,ys+i−1) = (π(x1),... ,π(x(k−ℓ)(s+i−2)+1)) = π(r(x1,... ,xs(k−ℓ)+ℓ)). Notice that (x(k−ℓ)(r−1)+1,... ,x(k−ℓ)(r−1)+k) is an edge of Psk,ℓ for r ∈ {1,... ,s}, and

(yr,yr+1,... ,yr+i−1) = π(r(x(k−ℓ)(r−1)+1,... ,x(k−ℓ)(r−1)+k)).

Thus, f(i−1)(yr,yr+1,... ,yr+i−1) is an element of the chain Cj, so f(i−1)(y1,... ,ys+i−1) is a descentfree list of length s in Cj. Because a descent-free list in a chain must be strictly increasing,

- s ≤ |Cj| = ej − 1. Thus, c avoids Pek,ℓj in color j for each j ∈ [t].


Upper Bound. Let c be a t-coloring of E(KNk ) that avoids Pek,ℓj in color j for all j ∈ [t]. We will show that N ≤ |Q∗i |. For Y ⊆ [N] with |Y | = h > k − ℓ, let Y + denote the h − (k − ℓ) largest elements of Y and Y − denote the h − (k − ℓ) smallest elements of Y . We will begin by iteratively deﬁning a function

gm : k−(m− [N1)(] k−ℓ) → Qm for m ∈ [i] with the property that for all Y ∈ k−(m− [N2)(] k−ℓ) , gm(Y −) gm(Y +).

We start with the case m = 1. Suppose that X ∈ [Nk] with c(X) = j. Let h be the largest integer such that there is an j-colored Phk,ℓ that has X as its maximum edge. Because c avoids Pek,ℓj in color j, h ≤ ej − 1. Supposing that x1 ⊂ ··· ⊂ xej−1 are the elements of Cj in Q1, let g1(X) = xh. For Y ∈ 2 [kN−]ℓ , if c(Y −) = c(Y +), then g1(Y −) and g1(Y +) are in diﬀerent chains of Q1, so they are not comparable. If c(Y −) = c(Y +), then g1(Y +) ⊇ g1(Y −) because Y − and Y + form a P2k,ℓ in color c(Y −) = c(Y +). Therefore g1(Y −) g1(Y +).

Let 1 < m ≤ i, and for X ∈ k−(m− [N1)(] k−ℓ) , deﬁne gm(X) = D({gm−1(Y ) : Y + = X}). Because Qm = J(Qm−1), gj(X) ∈ Qj. Suppose that Y ∈ k−(m− [N2)(] k−ℓ) and note that gm−1(Y ) ∈ gm(Y +). If also gm−1(Y ) ∈ gm(Y −), then there is some Z ∈ k−(m− [N2)(] k−ℓ) such that Z+ = Y − and gm−1(Y ) ⊆ gm−1(Z). For W = Y ∪ Z, it holds that W− = Z and W+ = Y , so gm−1(W−) ⊇ gm−1(W+); a contradiction. Therefore, gm−1(Y ) ∈ gm(Y +) \ gm(Y −), so gm(Y −) gm(Y +).

Now that gi is deﬁned, and gi maps [Nℓ′] to Qi, we construct a function φ : {ℓ′,... ,N} → Qi. For ℓ′ ≤ x ≤ n, let φ(x) = gi({x − ℓ′ + 1,... ,x}). We claim that for any R ∈ Qi, |φ−1(R)| ≤ k − ℓ. If ℓ′ ≤ x1 < ··· < xk−ℓ+1 ≤ n, then φ(x1) = ··· = φ(xk−ℓ+1). Let W = {xk−ℓ+1 − ℓ′ + 1,... ,xk−ℓ+1} and Y = {x1 − ℓ′ + 1,... ,x1}. Since φ(x1) = φ(xk−ℓ+1) by assumption, we have gi(Y ) = gi(W). In particular, gi(Y ) ⊇ gi(W) as elements in Qi. Realizing that xk−ℓ−ℓ′+1 < min W, let X = Y ∪ {x1,... ,xk−ℓ−ℓ′+1} ∪ W. Note that |X| = ℓ′ + k − ℓ and that X− = Y while X+ = W. However, X ∈ ℓ′+ [Nk−] ℓ and gi(X−) gi(X+), a contradiction. Since |φ−1(R)| ≤ k − ℓ for all R ∈ Qi, N − ℓ′ + 1 ≤ (k − ℓ)|Qi| = |Q∗i | − (ℓ′ − 1), so N ≤ |Q∗i|.

- Theorem 1.1 follows from Theorems 2.1 and 2.2. Corollary 1.2 follows from Theorem 2.2 after


observing that |Q2(e1,... ,et)| = tj=1 ej because we can select a down-set of Q1(e1,... ,et) by selecting at most one element from each chain to be a maximal element of the down-set.

For m ≥ 3, the value of |Qm(e1,... ,et)| is not known exactly, but note that |Q3(e1,... ,et)| is the number of antichains in Q2(e1,... ,et). When e1 = ··· = et = 2, the poset Q2(e1,... ,et) is the t-dimensional boolean lattice, denoted 2[t], and counting the number of antichains in 2[t] is already a famous and diﬃcult problem known as Dedekind’s problem. Thus, we will use the bounds of Moshkovitz and Shapira on ORt(Pek,k−1) [13, Corollary 3] to ﬁnd the following corollary.

- Corollary 2.3. For e ≥ 2, k < 2ℓ < 2k, and ℓ′ = ℓ − (k − ℓ)(i(k,ℓ) − 1),


√

t) + ℓ′ ≤ ORt(Pek,ℓ) ≤ (k − ℓ)towi(k,ℓ)−2(2et−1) + ℓ′. In [11], Gerencse´r and Gy´arf´as showed that for n ≥ m ≥ 1,

(k − ℓ)towi(k,ℓ)−2(et−1/2

![image 5](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile5.png>)

m 2

R(Pn2,1,Pm2,1) = n +

+ 2.

![image 6](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile6.png>)

Comparatively, OR(Pn2,1,Pm2,1) = nm+1, which shows a large discrepancy between the ordered and unordered variants of the Ramsey number in just the 2-uniform case. It should, however, be noted

that over all orderings of a (k,ℓ)-path, the standard ordering on Pek,ℓ does not necessarily minimize the ordered Ramsey number. For example, it is easy to observe that there exists an ordering of

P2k,k−1 such that ORt(P2k,k−1) ≤ k + t − 1.

The proof of Theorem 1.1 using Theorem 2.2 is valuable because it shows a direct connection between the poset Qi(e1,... ,et) and the ordered Ramsey number OR(Pek,ℓ1 ,... ,Pek,ℓt ) and the best asymptotic bounds on the ordered Ramsey numbers come from this poset perspective. However,

- Theorem 1.1 can be proven directly by translating t-colorings that avoid (k,ℓ)-paths with t-colorings that avoid tight i-uniform paths.


Direct Proof of Theorem 1.1. Recall from the proof of Theorem 2.2 the deﬁnitions of i and ℓ′. Let N = OR(Pei,i1 −1,... ,Pei,it −1) and N′ = (k − ℓ)N + ℓ′.

For a k-uniform edge {x1,... ,xk}, we deﬁne the rational reduction, denoted r(x1,... ,xk), to be the the i-uniform edge {⌈x1/(k − ℓ)⌉,⌈x(k−ℓ)+1/(k − ℓ)⌉,... ,⌈x(i−1)(k−ℓ)+1/(k − ℓ)⌉}. For an i-uniform edge {x1,... ,xi}, the canonical preimage, denoted r−1(x1,... ,xi), is deﬁned as

![image 7](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile7.png>)

![image 8](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile8.png>)

  ∪

r−1(x1,... ,xi) = 

ℓ′

k−ℓ

- i−1
- j=1


{(k − ℓ)(xi − 1) + a} .

{(k − ℓ)(xj − 1) + a}



![image 9](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile9.png>)

a=1

a=1

Observe that (i−1)(k −ℓ)+ℓ′ = k and hence r−1(x1,... ,xi) has k ordered elements. Finally, note that r sends k-uniform edges from KNk ′ to i-uniform edges in KNi and r−1 sends i-uniform edges from KNi to k-uniform edges in KNk ′.

![image 10](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile10.png>)

![image 11](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile11.png>)

![image 12](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile12.png>)

Let N = OR(Pei,i1 −1,... ,Pei,it −1) and N′ = (k − ℓ)N + ℓ′.

Lower Bound. There exists a t-coloring c : E(KNi −1) → [t] of KNi −1 that avoids a j-colored copy of Pei,ij −1 for each j ∈ [t]. Deﬁne a coloring c′ : E(KNk ′−1) → [t] by c′(x1,... ,xk) = c(r(x1,... ,xk)). Suppose that there is a color j and a list x1 < ··· < xm of vertices such that there is a j-colored copy of Pek,ℓj in c′ on the vertices x1,... ,xm. Then, for each k-uniform edge {xp,... ,xp+k−1} in this copy of Pek,ℓj , the edge r(xp,... ,xp+k−1) has color j in c. Also, for two consecutive edges {xp,... ,xp+k−1} and {xp+ℓ,... ,xp+k+ℓ−1} the rational reductions r(xp,... ,xp+k−1) and r(xp+ℓ,... ,xp+k+ℓ−1) intersect in i−1 vertices. Thus, the ej edges given by the rational reductions form a j-colored copy of Pei,ij −1, a contradiction. Therefore, c′ avoids a j-colored copy of Pek,ℓj and hence OR(Pek,ℓ1 ,... ,Pek,ℓt ) ≥ N′.

![image 13](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile13.png>)

![image 14](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile14.png>)

![image 15](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile15.png>)

![image 16](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile16.png>)

Upper Bound1. Let c′ : E(KNk ′) → [t] be a t-coloring of KNk ′. Deﬁne a t-coloring c : E(KNi ) → [t] of KNi as c({x1,x2,... ,xi}) = c′(r−1(x1,... ,xi)). By the deﬁnition of N, there exists a j-colored copy of Pei,ij −1 on vertices x1,... ,xm for some j ∈ [t]. For each i-uniform edge {xq,... ,xq+i−1} in this copy of Pei,ij −1, the k-uniform edge r−1(xq,... ,xq+i−1) also has the color j with respect to c′. Further, for two consecutive i-uniform edges {xq,... ,xq+i−1} and {xq+1,... ,xq+i} in this copy of Pei,ij −1, the k-uniform edges r−1(xq,... ,xq+i−1) and r−1(xq+1,... ,xq+i) intersect in exactly ℓ vertices. Therefore, there is a j-colored copy of Pek,ℓj with respect to the coloring c′ and therefore OR(Pek,ℓ1 ,... ,Pek,ℓt ) ≤ N′.

![image 17](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile17.png>)

![image 18](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile18.png>)

![image 19](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile19.png>)

![image 20](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile20.png>)

Now that we have determined the ordered Ramsey number for a particularly “nice” ordering of a (k,ℓ)-path, it is natural to ask for general bounds on ORt(Pek,ℓ) where the vertices of Pek,ℓ are ordered arbitrarily. In order to simplify that statement of the next lemma and theorem, we deviate slightly from our standard notation and use Pp instead of Pp2−,11 to denote the 2-uniform path on p vertices. The case for t = 2 was originally proven by Cibulka, Gao, Krcˇ´l, Valla, and Valtr [4, Theorem 6]; we include the full proof for the sake of completeness.

Lemma 2.4. Let n and p be positive integers, and let P2p be any ordering of the 2-uniform ordered path on 2p vertices. Then

t−1

1

p((p+1)t−1(np−1)+1).

![image 21](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile21.png>)

![image 22](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile22.png>)

P2p,... ,P2p) ≤ 2

OR(K2n,

![image 23](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile23.png>)

Proof. We prove by ﬁrst showing that the theorem holds for all n when t = 2, and then continue by induction on t. For n = 1 and t = 2, we see that OR(K2,P2p) = 2p = 2

1

p((p+1)(p−1)+1).

![image 24](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile24.png>)

![image 25](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile25.png>)

1The authors thank Josef Cibulka for providing the translation of colorings in this direction.

Let V (P2p) = {v1,... ,v2p} with indices i1,... ,i2p deﬁned such that the ordering on V (P2p) is vi1 < ··· < vi2p.

Consider a 2-coloring c of E(KN) where N = 2(p+1)n−1 = 2pM with M = 2(p+1)(p−1). Let V1,... ,V2p be intervals partitioning [N] with |Vi| = M and max Vi < min Vi+1. As per the ordering of V (P2p), let Uj = Vij. Thus, any path (u1,... ,u2p) with uj ∈ Uj is a copy of P2p.

For j ∈ [2p] deﬁne Aj to be the set of vertices v in Uj such that there exist uk ∈ Uk for k ∈ [j − 1] such that c(u1,u2) = c(u2,u3) = ··· = c(uj−1,v) = 2. Notice that A1 = U1 and A2p = ∅ by the assumption that c avoids P2p in color 2. Let I be the largest integer such that |AI| ≥ M/2; thus, let A = AI and B = UI+1 \ AI+1. Note that |B| ≥ M/2 and the bipartite graph induced by (A,B) has no edges of color 2.

Observe that M/2 = 2(e+1)(n−1)−1 ≥ OR(K2n−1,P2p) by the induction hypothesis on n. Therefore,

- A or B has a P2p in color 2 or both have a copy of K2n−1 in color 1. If the former is true, we are done, so suppose the latter holds. Therefore, A ∪ B has a K2n in color 1, so OR(K2n,P2p) ≤ 2(p+1)n−1.


1

p((p+1)t−1(np−1)+1). Realizing that (p+1)

Now, suppose that t > 2 and consider a t-coloring, c, of E(KN) for N = 2

![image 26](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile26.png>)

t−1(np−1)+1

t−2(np−1)+1

p = (p + 1)(p+1)

p − 1, we ﬁnd through the t = 2 case that N ≥ OR(K

![image 27](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile27.png>)

![image 28](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile28.png>)

p((p+1)t−2(np−1)+1),P2p). Thus, c either has a P2p in color t or a K

1

![image 29](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile29.png>)

2

p((p+1)t−2(np−1)+1) which is void of color t. If the former holds, then we are done, so suppose the latter holds. By the induction hypothesis on t,

1

![image 30](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile30.png>)

2

t−2

1

p((p+1)t−2(np−1)+1) ≥ OR(K2n,

![image 31](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile31.png>)

![image 32](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile32.png>)

P2p,... ,P2p); therefore, we either have a K2n in color 1 or a P2p in some color j ∈ {2,... ,t − 1}.

2

![image 33](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile33.png>)

- Lemma 2.4 immediately implies the following theorem.


- Theorem 2.5. Let Pp be any ordered 2-uniform path on p vertices, then


1

⌈lgp⌉((⌈lgp⌉+1)t−1(⌈lgp⌉2−1)+1) = 2O(lgt p).

ORt(Pp) ≤ 2

![image 34](<2014-cox-ordered-ramsey-numbers-loose_images/imageFile34.png>)

As a means to a lower bound on this value, Conlon, Fox, Lee and Sudakov [6] provided the following lower bound on the ordered Ramsey number of a randomly-ordered 2-uniform matching, which was also proved in a weaker form by Balko, Cibulka, Kra´l and Kyn˘cl [1].

- Theorem 2.6 (Conlon, Fox, Lee and Sudakov [6, Theorems 2.3]). There exists a positive constant c, such that if M is a randomly-ordered matching on e edges, then asymptotically almost surely,


OR2(M) ≥ (2e)clog(2e)/log log(2e).

Since Pp contains a matching of size ⌊p/2⌋, we see that almost every ordering of Pp yields OR2(Pp) ≥ 2Ω(lg2 p/lg lgp). Hence, Theorem 2.5 is fairly tight when t = 2. Therefore, for almost every ordering of Pp, ORt(Pp) grows as a quasi-polynomial in p for a ﬁxed t and possibly double-exponentially in

- t for a ﬁxed p. Comparatively, for the standard ordering of Pp, ORt(Pp) grows polynomially in p and exponentially in t.


3. Ordered Ramsey Numbers of k-Uniform Matchings Recall that the ordered path Pek,0 has disjoint edges, and therefore is a matching. The proof of

- Theorem 2.2 holds for ℓ = 0, but instead we will consider a more general class of ordered matchings. For a ﬁxed 0 ≤ r ≤ k and positive integer e, the (k,r)-nested matching on e edges is the ordered graph Mek,r deﬁned iteratively as: E(M1k,r) consists of one edge A1 = [k], and E(Mek,r+1) consists of


the edges in E(Mek,r) and an edge Ae+1 consisting of the r least integers greater than maxV (Mek,r) and the k −r greatest integers less than min V (Mek,r). We say (k,r) is the nesting pattern of Mek,r. Note that Mek,r is isomorphic to Mek,k−r when the ordering is reversed, and Mek,0 ∼= Mek,k ∼= Pek,0.

In [5], Cockayne and Lorimer show that for integers e1 ≥ ··· ≥ et, if Mi is a 2-uniform matching on ei edges, then

t

(ei − 1).

R(M1,... ,Mt) = e1 + 1 +

i=1

This value is not far from the value of the ordered Ramsey number for 2-uniform nested matchings. The following lemma presents a lower bound on the ordered Ramsey number of t k-uniform nested matchings, even if the nesting patterns diﬀer among the matchings.

- Lemma 3.1. For positive integers e1,... ,et and r1,... ,rt ∈ {0,... ,k},


t

OR(Mek,r1 1,... ,Mek,rt t) ≥ k 1 +

(ei − 1) .

i=1

Proof. Let N = k 1 + ti=1(ei − 1) − 1. Let L1,... ,Lt,R1,... ,Rt be intervals partitioning [N], with L1 = R1, such that for i ∈ {1,... ,t−1}, max Li+1 < min Li and maxRi < min Ri+1. Further, let |L1| = ke1 −1, and for i ∈ {2,... ,t} let |Li| = (k −ri)(ei −1) and |Ri| = ri(ei −1). For an edge

X ∈ [nk] , let c(X) = max{i : X ∩ (Li ∪ Ri) = ∅}. The interval L1 is too small for c to contain a copy of Mek,r1 1 in color 1.

Suppose that c contained a copy of Mek,ri i in color i for some i ∈ {2,... ,t}. If ri = k, then Li = ∅ and |Ri| = k(ei − 1); therefore some edge of Mek,ri i does not intersect Ri and hence does not have color i. The case ri = 0 is similar, except |Li| = k(ei − 1) and Ri = ∅.

Now suppose 1 ≤ ri < k. Let p1,... ,pei be the minimum vertices of the edges of Mek,ri i and q1,... ,qei be the set of maximum vertices, hence p1 < p2 < ··· < pei < qei < ··· < q1. In fact, pm + k − ri < pm+1 and qm − ri > qm+1 for m = 1,... ,ei − 1. Since each edge receives color i, either pm ∈ Li or qm ∈ Ri for all m. However, because |Li| = (k − ri)(ei − 1) and |Ri| = ri(ei − 1), it must be the case that pei ∈/ Li and qei ∈/ Ri. Therefore, c avoids Mek,ri i for all i.

When all nesting patterns are the same, the bound from Lemma 3.1 is sharp.

- Theorem 3.2. For positive integers e1,... ,et, and 0 ≤ r ≤ k,


t

OR(Mek,r1 ,... ,Mek,rt ) = k 1 +

(ei − 1) .

i=1

Proof. The lower bound follows from Lemma 3.1. We prove the upper bound by induction on t i=1 ei. If ti=1 ei = t, then ei = 1 for all i, so OR(Mek,r1 ,... ,Mek,rt ) = k, and the claim holds.

Suppose that ti=1 ei > t and let c be a t-coloring of E(KNk ) where N = k 1 + ti=1(ei − 1) . Suppose that c({1,... ,r} ∪ {N − k + r + 1,... ,N}) = j for some j ∈ [t]. Let G be the graph

given by deleting the vertices in {1,... ,r} ∪ {N − k + r + 1,... ,N} from KNk . Let e′j = ej − 1 and e′i = ei for i = j. Notice that G ∼= KNk −k and N − k = k 1 + ti=1(e′i − 1) . Therefore, since

i=1 e′i = ti=1 ei −1, the induction hypothesis implies that G contains an i-colored copy of Mek,r′ i

- t


i

- for some i. Since e′i = ei when i = j, we have i = j. Then the j-colored copy of Mek,rj


j−1 along with the edge {1,... ,r} ∪ {N − k + r + 1,... ,N} is a j-colored copy of Mek,rj j.

Notice that i(k,0) = 1 and |Q1(e1,... ,et)| = ti=1(ei − 1); thus, the r = 0 case of Theorem 3.2 agrees with the bound in Theorem 2.2 using ℓ = 0. Interestingly, as opposed to the large discrepancy

between the ordered and ordinary Ramsey numbers of paths, we see that ORt(Me2,r) ≤ 2Rt(Me2,r). However, this trend does not continue when the ordering of the matching is not nested as in Mek,r. Likely Mek,r minimizes the ordered Ramsey number ORt(M) among all orderings of k-uniform matchings M on e edges.

Conlon, Fox, Lee and Sudakov [6] explore the ordered Ramsey numbers of 2-uniform matchings.

- Theorem 3.3 (Conlon, Fox, Lee and Sudakov [6]). Let M2,... ,Mt be ordered 2-uniform matchings, and let p ≥ 2. Then OR(Kp,M2,... ,Mt) ≤ OR(M2,... ,Mt)⌈lgp⌉. Therefore, for an ordered 2uniform matching M with e edges, ORt(M) ≤ (2e)⌈lg(2e)⌉t−1 ≤ 2⌈lg(2e)⌉t.


Compare the upper bound here with the lower bound from Theorem 2.6, showing that this upper bound is nearly tight. In terms of e, the bound above is quasi-polynomial, but in terms of t the bound is doubly-exponential.

Deﬁne the k-uniform graph Gks iteratively on s as follows: let Gk0 consist of a single vertex, and for s ≥ 1, let Gks consist of k disjoint, consecutive copies of Gks−1, and introduce every k-uniform edge consisting of exactly one vertex from each copy. Notice that G2s = K2s.

The above deﬁnition of Gks uses a “concatenation” step to glue k copies of Gks−1 to form Gks. We now state an equivalent deﬁnition, which we refer to as the “blow-up” construction of Gks, that uses an “expansion” step that is key to the proof of Lemma 3.6. Let V (Gks−1) = {x1,... ,xks−1} with xi < xi′ if and only if i < i′. Duplicate each vertex xi k times to form a list of vertices x(1)i ,... ,xi(k). Two vertices x(ij) and x(j

′)

′)

i′ are ordered as x(ij) < x(j

i′ if i < i′, or i = i′ and j < j′. The graph Gks has vertex set {x(ij) : i ∈ [ks−1],j ∈ [k]} and the edges of Gks are of the form {x(1)i ,... ,x(ik)} for i ∈ [ks−1] or {x(ij1)

,... ,xi(jk)

} for every edge {xi1,... ,xik} in Gks−1 and any tuple (j1,... ,jk) ∈ [k]k.

1

k

Using the graph Gks, we attain a bound on the t-color ordered Ramsey numbers of certain “nice” orderings of k-uniform matchings. This bound is a generalization of Theorem 3.3, where Gks replaces the complete graph.

- Lemma 3.4. Let M2,... ,Mt be any k-uniform ordered matchings and s ≥ 0. Then OR(Gks,M2,... ,Mt) ≤ OR(M2,... ,Mt)s.


Proof. We prove by induction on s. When s = 0, the graph Gk0 consists of a single vertex, and hence every coloring of K1k contains a copy of Gks in every color. Suppose that s > 0 and let r = OR(M2,... ,Mt). Let c be a t-coloring of Krks that avoids a

- j-colored copy of Mj for each j ∈ {2,... ,t} and avoids a 1-colored copy of Gks. Let V1,... ,Vr be equal-sized intervals partitioning [rs] such that maxVi < min Vi+1 for i ∈ [r − 1]. By the induction hypothesis, restricting c to Vi yields either a copy of Gk(s−1) in color 1 or a j-colored copy of Mj


- for some j ∈ {2,... ,t}. Since c contains no j-colored copy of Mj, each Vi contains a copy of Gk(s−1). Since c avoids Gks, then for any indices 1 ≤ i1 < ··· < ik ≤ r there must be xij ∈ Vij


such that c(xi1,... ,xik) = 1. Deﬁne a coloring of E(Krk) by letting c′(vi1,... ,vik) be any color in {c(xi1,... ,xik) : xij ∈ Vij} \ {1}. By the deﬁnition of r, c′ contains an j-colored copy of Mj for some j ∈ {2,... ,t} and therefore c also contains a j-colored copy of Mj; a contradiction.

Let M be an ordered k-uniform matching on vertex set [ke]. We say that M is k-nestable if there exist disjoint intervals I1,... ,Ik, some of which may be empty or degenerate, spanning [ke] such that 1 ∈ I1,ke ∈ Ik, where each edge in M either is contained in some interval Ij or spans all intervals I1,... ,Ik, and for each j ∈ [k] the edges contained within Ij form a matching, denoted

Mj, that is either k-nestable or empty. A set of intervals I1,... ,Ik satisfying these properties is a k-nesting of M. Notice that every matching contained as a subgraph of Gks for some s must be k-nestable; in particular, every 2-uniform matching is 2-nestable as G2s ∼= K2s. The following lemma provides the converse to this observation.

- Lemma 3.5. If M is a k-nestable ordered matching with e edges for k ≥ 3, then M is contained within Gk2e−1.


Proof. We prove by induction on e. The statement is trivial when e = 1 as both M and Gk1 are a single k-uniform edges. Suppose the ordered k-uniform matching M has vertex set [ke] for e ≥ 2.

Let I1,... ,Ik be a k-nesting of M, and let M1,... ,Mk be the matchings induced by the edges within each interval. For j ∈ [k], let ej be the number of edges in the matching Mj. Deﬁne M′ to be the matching M − kj=1 Mj. Since ej < e, by the inductive hypothesis, there exist order-preserving graph embeddings πj : V (Mj) → V (Gk2e

j−1) from Mj to a subgraph within Gk2e

j−1. If M′ happens to be empty, for v ∈ V (Mj) deﬁne π′(v) to be the copy of πj(v) in the ﬁrst copy of Gk2e

j ej−1. Further, deﬁne π′′(v) to be the copy of π′(v) in the jth copy of Gk2 max

j−1 contained within Gk2 max

j ej. It is readily seen that π′′ is an embedding of M into Gk2 max

j ej−1 contained within Gk2 max

j ej. Because e > maxj ej, the claim follows.

Now suppose that M′ is nonempty, and let e′ = (e − kj=1 ej) +maxj ej. Because M′ is nonempty, e′ > maxj ej. We will show that M is contained within Gk2e′−1. We begin by embedding kj=1 Mj

- into Gk2e′−1 using the embeddings π1,... ,πk. This comes in two steps: ﬁrst the embedding of Mj is “expanded” into Gk2e′−2 by using the blow-up construction of Gks, then the k embeddings
- into Gk2e′−2 are “concatenated” to allow for an embedding of M into Gk2e′−1. Let v be a vertex


j−1), we must convert πj(v) to a vertex in Gk2e′−2. Let ℓ(v) be the number of vertices in V (M′) ∩ Ij less than v. There can be at most |E(M′)| such vertices, so 0 ≤ ℓ(v) ≤ |E(M′)| ≤ (e′ − ej) ≤ k2(e′−ej)−2. Thus, there exists a k-ary representation of ℓ(v) as

in Mj. Since πj(v) ∈ V (Gk2e

2(e′−ej)−3 i=0 aiki for nonnegative integers a0,... ,a2(e′−ej)−3 satisfying 0 ≤ ai < k. Deﬁne a list x0,

x1, ... , x2(e′−ej)−2 iteratively as x0 = πj(v) and xi+1 = x(iai), where xi is a vertex in Gk2e

j+i−1 and xi(a) is the ath copy of xi in Gk2e

j+i as in the blow-up construction of Gks. Let π′(v) = x2(e′−ej)−2, which is a vertex in Gk2e′−2.

Observe that for two consecutive vertices u < v in Mj, there are at least (k − 1)2(e′−ej)−2 vertices between π′(u) and π′(v) in Gk2e′−2 because ℓ(v) ≥ ℓ(u), and that |V (M′) ∩ [u,v]| = ℓ(u) − ℓ(v) ≤ e′ − ej ≤ (k − 1)2(e′−ej)−2 because k ≥ 3. Also note that if u = min V (Mj), then there are exactly ℓ(u) vertices in Gk2e′−2 less than π′(u), and if v = max V (Mj), then there are at least |E(M′)|−ℓ(v) vertices in Gk2e′−2 greater than π′(v). Now for v ∈ V (Mj), deﬁne π′′(v) to be the copy of π′(v) in the jth copy of Gk2e′−2 within Gk2e′−1.

We now select vertices in Gk2e′−1 to embed the vertices of M′. Consider an interval Ij, let vmin be the least vertex in Mj, and let vmax be the greatest vertex in Mj. There are ℓ = ℓ(vmin) vertices u1,... ,uℓ of M′ in Ij that precede vmin, and the same number of vertices x1,... ,xℓ in the jth copy of Gk2e′−2 less than π′′(vmin); hence we deﬁne π′′(ui) = xi for i ∈ [ℓ]. For two consecutive vertices u ≤ v of Mj, there are m = ℓ(v) − ℓ(u) vertices u1,... ,um of M′ between

- u and v, and at least (k − 1)2(e′−ej)−2 ≥ ℓ(v) − ℓ(u) vertices in the jth copy of Gk2e′−2 between π′′(u) and π′′(v). Therefore, we can select the vertices π′′(u1),... ,π′′(um) in order. Finally, there are n = |E(M′)| − ℓ(vmax) vertices u1,... ,un of M′ in Ij that are greater than vmax, and there are at least |E(M′)| − ℓ(vmax) vertices in the jth copy of Gk2e′−2 greater than π′′(vmax), so we can


select the vertices π′′(u1),... ,π′′(un) in order. The resulting injection π′′ : V (M) → Gk2e′−1 is an embedding of M into Gk2e′−1.

Note that in the proof of Lemma 3.5, the “expansion” step takes 2(e′ − ej) − 1 iterations. In the case of one of the standard nesting matchings Mek,r, this is exactly one iteration. Thus, even for a matching Mek,r where the ordered Ramsey number is small, it is not possibly to embed Mek,r into Gks for any s < 2e−1 whenever 1 ≤ r ≤ k−1. When a k-nesting contains two nonempty matchings Mj and Mj′, or when there are multiple edges in M′, the iterative process given above may require fewer than 2e − 1 steps. However, it does appear that Ω(e) steps are required for most k-nested matchings on e edges, as most of the edges will likely live in M′.

The following theorem follows from Lemmas 3.4 and 3.5 and the fact that OR1(M) = ek if M is a

- k-uniform ordered matching with e edges.


- Theorem 3.6. Let k ≥ 3 and e ≥ 2. If M is a k-nestable ordered matching with e edges, then ORt(M) ≤ (ek)(2e−1)t−1 = 2(2e−1)t−1 lg(ek).


This extends the previous bound on 2-uniform matchings [6]. While the bound remains doublyexponential in terms of t, the bound has increased from quasi-polynomial to exponential in terms of e. Most notably, this bound is only polynomial in k.

Notice that for these “nice” orderings of a k-uniform matching on e edges, the bound on the ordered Ramsey number ORt(M) is only slightly larger than the ordered Ramsey number ORt(Pek,ℓ) of the naturally-ordered (k,ℓ)-path on e edges when i(k,ℓ) = 3.

We say that a k-uniform ordered matching M is simply interlacing if for any pair of distinct edges A,B in M, where A = {a1 < a2 < ··· < ak} and B = {b1 < b2 < ··· < bk} either ai and bi are consecutive in A ∪ B for each i or there is some i where ai < b1 < bk < ai+1 (where a0 = −∞ and ak+1 = +∞). If the former holds, we say that A and B interlace, and if the latter holds, we say that A and B nest. Notice that every 2-uniform matching is simply interlacing.

- Corollary 3.7. If k ≥ 3, e ≥ 2, and M is a simply-interlacing k-uniform ordered matching with e edges, then M is k-nestable; hence ORt(M) ≤ (ek)(2e−1)t−1 = 2(2e−1)t−1 lg(ek).


Proof. By Theorem 3.6, it suﬃces to show that M is k-nestable. Deﬁne a relation on the edges of M by A ≺ B if bi < a1 < ak < bi+1 for some 0 ≤ i ≤ k − 1, where A = {a1 < ··· < ak} and

- B = {b1 < ··· < bk} (again under the convention that b0 = −∞). While ≺ is not a partial order (as transitivity fails), it does admit maximal elements. Let A1,... ,Ap be the edges of M that are either maximal with respect to ≺ or interlace with some maximal edge. Therefore, Ai and Ai′ interlace. We refer to these edges as spanning edges.


For each i ∈ [p], label the vertices in Ai as Ai = {ai,1 < ··· < ai,k}; also let ai,0 = −∞ and ai,k+1 = +∞. Observe that for each j ∈ [k − 1], we have maxi∈[p] ai,j < mini∈[p] ai,j+1, as otherwise there is a pair of edge Ai and Ai′ where ai,j > ai′,j+1 and hence ai,j and ai′,j are not consecutive in Ai ∪ Ai′. Therefore, we can deﬁne disjoint intervals I1,... ,Ik such that Ij = [mini∈[p] ai,j,maxi∈[p] ai,j]. These intervals do not necessarily span V (M), but we will expand them to include vertices not in A1,... ,Ap.

For a non-spanning edge B in M, there is at least one edge Ai where B ≺ Ai. Therefore, there exists a j ∈ {0,... ,k − 1} such that ai,j < min B < max B < ai,j+1. Observe that since k ≥ 3, for any i′ ∈ [p] the edge B is comparable to Ai′ since there is some ai′,j′ not in the interval [ai,j,ai,j+1]. While it may not be the case that B ≺ Ai′, it is true that for every i′ ∈ [p] and ai′,j+ci′ < min B < maxB < ai′,j+ci′+1 for some ci′ ∈ {−1,0,+1}, as Ai′ ≺ B only when ai′,k < min B. Therefore, let jB be the minimum integer satisfying jB ≥ 1 and jB ≥ j + ci′ for each i′ ∈ [p].

If B,B′ are two non-spanning edges in M and jB < jB′, then max B < ai,jB+1 for all i ∈ [p] and ai′,jB′ < min B′ for some i′ ∈ [p]. Then maxB < ai′,jB+1 < min B′. Therefore, if for every nonspanning edge B in M we minimally extend the interval IjB to contain the edge B, the intervals I1,... ,Ik will always be disjoint.

Note that the matching Mj given by the edges entirely within the interval Ij is a simply-interlacing k-uniform ordered matching and hence is k-nestable by an inductive argument. Therefore, the

intervals I1,... ,Ik form a k-nesting of M.

We conclude by noting that Lemma 3.4 will not apply to most ordered k-uniform matchings for

- k ≥ 3. For k ≥ 4, let A and B be deﬁned as A = {1,... ,⌊k/2⌋} ∪ {k + 1,... ,k + ⌈k/2⌉}, B = {⌊k/2⌋ + 1,... ,k} ∪ {k + ⌈k/2⌉,... ,2k}.


Observe that the ordered matching with edges A and B is not k-nestable. While every ordered 3-uniform matching on two edges is 3-nestable, there exists an ordered 3-uniform matching that is not 3-nestable. A randomly-ordered matching contains these conﬁgurations with high probability, so the bound of Theorem 3.6 does not apply to most ordered matchings.

4. Future Directions

Our investigation into arbitrarily-ordered k-uniform matchings provides upper bounds that are similar to the previous bounds in the 2-uniform case. Extending the techniques from 2-uniform matchings comes at the cost that it does not apply to all k-uniform ordered matchings, but they do provide bounds that are exponential and not a tower. However, our methods do not allude to lower bounds, and hence it is unclear whether our upper bounds are tight.

The largest question left open from our study of ordered Ramsey numbers is related to arbitrary orderings of (k,ℓ)-paths. While we found upper bounds on ORt(Pe2,1), our techniques did not easily extend to higher uniformities. Upper bounds on ORt(Pek,ℓ) for arbitrary orderings of Pek,ℓ would be very interesting and would signiﬁcantly extend our current techniques. Noticing that towk−2(Ω(n2)) ≤ R2(Knk) ≤ towk−1(O(n)) (see [7]), the bound for ORt(Pek,k−1) for the natural ordering cannot be far oﬀ a general bound for ORt(Pek,k−1) for an arbitrary ordering. However, ORt(Pek,ℓ) for the natural ordering grows as a tower of height i(k,ℓ) − 1, so the upper bound for ORt(Pek,ℓ) for an arbitrary ordering may be much larger, especially if i(k,ℓ) = 2. Thus, bounds on tight paths may not lead to bounds on loose paths in the same way that Theorem 1.1 draws this connection for monotone paths.

The generalized diamond Dr consists of r copies of P22,1 who share ﬁrst and last vertices. The ordering of the intermediate vertices is unimportant as all orderings yield isomorphic graphs. Balko,

Cibulka, Kra´l, and Kync˘l [1] determined that OR2(D2) = 11. We would like to determine, asymptotically or otherwise, the growth of ORt(Dr) in terms of r. While the study of monotone paths explains what happens when a graph gets “longer,” the study of the generalized diamond will yield a better understanding of what happens when a graph gets “wider.”

The natural extension of Dr to higher uniformities, Drk,ℓ, consists of r copies of P2k,ℓ who share their ﬁrst k−ℓ and last k−ℓ vertices. However, unless ℓ = 1, Drk,ℓ admits many nonisomorphic orderings of the intermediate vertices, none of which are essentially natural. Presumably, a somewhat symmetric ordering of the intermediate vertices will minimize ORt(Drk,ℓ), but other than the fact that it is bounded below by ORt(P2k,ℓ), it is unclear how large this number can become.

Acknowledgments

The authors would like to thank David Conlon and Josef Cibulka for remarks that helped improve this paper. In particular, Josef Cibulka presented the translation of colorings in the direct proof of Theorem 1.1.

References

- [1] M. Balko, J. Cibulka, K. Kr´l, and J. Kync˘l. Ramsey numbers of ordered graphs, preprint available as arXiv:1310.7208.
- [2] V. Chva´tal, V. Ro¨dl, E. Szemere´di, and W. T. Trotter. The Ramsey number of a graph with bounded maximum degree, J. Combin. Theory Ser. B 34 (1983), 239-243.
- [3] S.A. Choudum and B. Ponnusamy. Ordered Ramsey numbers, Discrete Mathematics 247 (2002), 79-92.
- [4] J. Cibulka, P. Gao, M. Krcˇ´al, T. Valla, and P. Valtr, On the Geometric Ramsey Number of Outerplanar Graphs, to appear in Discrete & Computational Geometry, preprint available as arXiv:1310.7004.
- [5] E.J. Cockayne and P.J. Lorimer. The Ramsey number for stripes, Journal of the Australian Mathematical Society 19 (1975), 252-256.
- [6] D. Conlon, J. Fox, C. Lee, and B. Sudakov. Ordered Ramsey numbers, preprint available as arXiv:1410.5292.
- [7] P. Erd˝s, A. Hajnal, and R. Rado. Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16

(1965), 93-196.

- [8] P. Erd˝s and G. Szekeres. A combinatorial problem in geometry, Compositio Math. 2 (1935), 463-470.
- [9] J. Fox, J. Pach, B. Sudakov, and A. Suk. Erd˝s-Szekeres-type theorems for monotone paths and convex bodies, Proc. London Math. Soc. (2012).
- [10] J. Fox and B. Sudakov, Two remarks on the Burr–Erd˝s conjecture, European J. Combin. 30 (2009), 1630–1645.
- [11] L. Gerencse´r and A. Gya´rfa´s. On Ramsey-Type Problems, Annales Universitatis Scientiarum Budapestinensis 10 (1967), 167-170.
- [12] K. Milans, D. Stolee, and D. West. Ordered Ramsey theory and track representations of graphs, preprint.
- [13] G. Moshkovitz and A. Shapira. Ramsey theory, integer partitions and a new proof of the Erd˝s–Szekeres theorem, Adv. Math. 262 (2014), 1107–1129.
- [14] X. Peng. The Ramsey number of generalized loose paths in uniform hypergraphs, preprint available as arXiv:1305.0294.
- [15] D. B. West. Introduction to graph theory. Prentice Hall, Inc., Upper Saddle River, NJ, 1996.


