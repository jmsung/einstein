## arXiv:1510.06057v1[math.CO]20Oct2015

# Reﬁned Tur´an numbers and Ramsey numbers for the loose 3-uniform path of length three

Andrzej Ruci´nski∗ A. Mickiewicz University Poznan´, Poland rucinski@amu.edu.pl May 27, 2022

Joanna Polcyn A. Mickiewicz University Poznan´, Poland joaska@amu.edu.pl

Abstract

Let P denote a 3-uniform hypergraph consisting of 7 vertices a,b,c,d,e,f,g and 3 edges {a,b,c},{c,d,e}, and {e,f,g}. It is known that the r-color Ramsey number for P is R(P;r) = r + 6 for r 7. The proof of this result relies on a careful analysis of the Tur´an numbers for P. In this paper, we reﬁne this analysis further and compute, for all n, the third and fourth order Tur´n numbers for P. With the help of the former, we conﬁrm the formula R(P;r) = r+6 for r ∈ {8,9}.

### 1 Introduction

For brevity, 3-uniform hypergraphs will be called here 3-graphs. Given a family of 3-graphs F, we say that a 3-graph H is F-free if for all F ∈ F we have H F.

For a family of 3-graphs F and an integer n 1, the Tur´n number of the 1st order, that is, the ordinary Tura´n number, is deﬁned as

ex(1)(n;F) = max{|E(H)| : |V (H)| = n and H is F-free}.

Every n-vertex F-free 3-graph with ex(1)(n;F) edges is called 1-extremal for F. We denote by Ex(1)(n;F) the family of all, pairwise non-isomorphic, n-vertex 3-graphs which are 1-extremal for F. Further, for an integer s 1, the Tur´n number of the (s + 1)-st order is deﬁned as

ex(s+1)(n;F) = max{|E(H)| : |V (H)| = n, H is F-free, and ∀H ∈ Ex(1)(n;F) ∪ ... ∪ Ex(s)(n;F),H H },

∗Research supported by the Polish NSC grant 2014/15/B/ST1/01688.

if such a 3-graph H exists. Note that if ex(s+1)(n;F) exists then, by deﬁnition, ex(s+1)(n;F) < ex(s)(n;F). (1) An n-vertex F-free 3-graph H is called (s+1)-extremal for F if |E(H)| = ex(s+1)(n;F)

and ∀H ∈ Ex(1)(n;F)∪...∪Ex(s)(n;F),H H ; we denote by Ex(s+1)(n;F) the family of n-vertex 3-graphs which are (s + 1)-extremal for F. In the case when F = {F}, we will write F instead of {F}.

A loose 3-uniform path of length 3 is a 3-graph P consisting of 7 vertices, say, a,b,c,d,e,f,g, and 3 edges {a,b,c},{c,d,e}, and {e,f,g}. The Ramsey number R(P;r) is the least integer n such that every r-coloring of the edges of the complete 3-graph Kn results in a monochromatic copy of P. Gyarfas and Raeisi [6] proved, among many other results, that R(P;2) = 8. (This result was later extended to loose paths of arbitrary lengths, but still r = 2, in [13].) Then Jackowska [9] showed that R(P;3) = 9 and

- r + 6 R(P;r) for all r 3. In turn, in [10] and [11], Tur´an numbers of the ﬁrst and second order, ex(1)(n;P) and ex(2)(n;P), have been determined for all feasible values of n, as well as the single third order Tura´n number ex(3)(12;P). Using these numbers, in [11], we were able to compute the Ramsey numbers R(P;r) for r = 4,5,6,7.


- Theorem 1 ([6, 9, 11]). For all r 7, R(P;r) = r + 6.

In this paper we determine, for all n 7, the Tur´an numbers for P of the third and fourth order, ex(3)(n;P) and ex(4)(n;P). The former allows us to compute two more Ramsey numbers.

- Theorem 2. For all r 9, R(P;r) = r + 6.


It seems that in order to make a further progress in computing the Ramsey numbers R(P;r), r 10, one would need to determine higher order Tur´an numbers ex(s)(n;P), at least for some small values of n. Unfortunately, the forth order numbers are not good enough.

Throughout, we denote by Sn the 3-graph on n vertices and with n−21 edges, in which one vertex, referred to as the center, forms edges with all pairs of the remaining vertices. Every sub-3-graph of Sn without isolated vertices is called a star, while Sn itself is called the full star. We denote by C the triangle, that is, a 3-graph with six vertices a,b,c,d,e,f and three edges {a,b,c}, {c,d,e}, and {e,f,a}. Finally, M stands for a pair of disjoint edges.

In the next section we state all, known and new, results on ordinary and higher order Tur´an numbers for P, including Theorem 9 which provides a complete formula for ex(3)(n;P). We also deﬁne conditional Tura´n numbers and quote from [11] three useful lemmas about the conditional Tura´n numbers with respect to P, C, M. Then, in Section 3, we prove Theorem 2, while the remaining sections are devoted to proving Theorem 9.

### 2 Tur´an numbers

A celebrated result of Erdo˝s, Ko, and Rado [2] asserts that for n 6, ex(1)(n;M) =

n−1

- 2 . Moreover, for n 7, Ex(1)(n;M) = {Sn}. We will need the second order version


of this Tur´an number, together with the 2-extremal family. Such a result has been proved already by Hilton and Milner [8] (see [4] for a simple proof). For a given set of vertices V , with |V | = n 7, let us deﬁne two special 3-graphs. Let x,y,z,v ∈ V be four diﬀerent vertices of V . We set

- G1(n) = {{x,y,z}} ∪ h ∈

V 3

: v ∈ h,h ∩ {x,y,z} = ∅ ,

- G2(n) = {{x,y,z}} ∪ h ∈


V 3

: |h ∩ {x,y,z}| = 2 . Note that for i ∈ {1,2}, Gi(n)  ⊃ M and |Gi(n)| = 3n − 8.

- Theorem 3 ([8]). For n 7, ex(2)(n;M) = 3n − 8 and Ex(2)(n;M) = {G1(n),G2(n)}.

Later, we will use the fact that C ⊂ Gi(n)  ⊃ P, i = 1,2.

Recently, the third order Tura´n number for M has been established by Han and Kohayakawa. Let G3(n) be the 3-graph on n vertices, with distinguished vertices x,y1,y2,z1,z2 whose edge set consists of all edges spanned by x,y1,y2,z1,z2 except for {y1,y2,zi}, i = 1,2, and all edges of the form {x,zi,v}, i = 1,2, where v  ∈ {x,y1,y2,z1,z2}.

- Theorem 4 ([7]). For n 7, ex(3)(n;M) = 2n − 2 and Ex(3)(n;M) = {G3(n)}.

Interestingly, the number n−21 serves as the Tur´an number for two other 3-graphs, C and P. The Tur´an number ex(1)(n;C) has been determined in [3] for n 75 and later for all n in [1].

- Theorem 5 ([1]). For n 6, ex(1)(n;C) = n−21 . Moreover, for n 8, Ex(1)(n;C) = {Sn}.

For large n, the Tura´n numbers for longer (than three) loose 3-uniform paths were found in [12]. The case of length three has been omitted in [12], probably because the authors thought it had been taken care of in [5], where k-uniform loose paths were considered, k 4. However, the method used in [5] did not quite work for 3-graphs. In [10] we ﬁxed this omission. Given two 3-graphs F1 and F2, by F1 ∪ F2 denote a vertex-disjoint union of F1 and F2. If F1 = F2 = F we will sometimes write 2F instead of F ∪ F.

- Theorem 6 ([10]).


 

n

3 and Ex(1)(n;P) = {Kn} for n 6, 20 and Ex(1)(n;P) = {K6 ∪ K1} for n = 7,

ex(1)(n;P) =



n−1

2 and Ex(1)(n;P) = {Sn} for n 8.

Interestingly, although the ordinary Tura´n numbers for the 2-matching M and the 3-path P are equal for n 8, their higher order counterparts diﬀer signiﬁcantly, being, respectively, of linear and quadratic order in n. In [11] we have completely determined the second order Tura´n number ex(2)(n;P), together with the corresponding 2-extremal 3-graphs. A comet Co(n) is an n-vertex 3-graph consisting of the complete 3-graph K4 and the full star Sn−3, sharing exactly one vertex which is the center of the star (see Fig. 1). This vertex is called the center of the comet, while the set of the remaining three vertices of the K4 is called its head.

![image 1](<2015-polcyn-refined-tur-numbers-ramsey_images/imageFile1.png>)

Figure 1: The comet Co(n)

##### Theorem 7 ([11]).

- ex(2)(n;P) =

 



15 and Ex(2)(n;P) = {S7} for n = 7, 20 + n−36 and Ex(2)(n;P) = {K6 ∪ Kn−6} for 8 n 12, 40 and Ex(2)(n;P) = {2K6 ∪ K1,Co(13)} for n = 13, 4 + n−24 and Ex(2)(n;P) = {Co(n)} for n 14.

Note that for n 6 the second order number is not deﬁned, since each 3-graph is a sub-3-graph of Kn. The main message behind the above result is that for n 8 it provides an upper bound on the number of edges in an n-vertex P-free 3-graph which is not a star.

Also in [11], we managed to calculate the third order Tura´n number for P and n = 12. Theorem 8 ([11]).

ex(3)(12;P) = 32 and Ex(3)(12;P) = {Co(12)}.

The main Tur´an-type result of this paper provides a complete formula for the third order Tura´n number for P.

- Theorem 9.


- ex(3)(n;P) =


 



- 3n − 8 and Ex(3)(n;P) = {G1(n),G2(n)} for 7 n 10, 25 and Ex(3)(n;P) = {G1(n),G2(n),Co(n)} for n = 11, 32 and Ex(3)(n;P) = {Co(n)} for n = 12, 20 + n−27 and Ex(3)(n;P) = {K6 ∪ Sn−6} for 13 n 14,
- 4 + n−25 and Ex(3)(n;P) = {K4 ∪ Sn−4} for n 15.


In particular, for n 14, Theorem 9 gives an upper bound on the number of edges in an n-vertex P-free 3-graph which is neither a star nor is contained in the comet Co(n).

Surprisingly, as an immediate consequence we obtain an exact formula for the 4th Tur´an number for P, at least for n 15. Indeed, consider the 3-graph Ro(n), called rocket, obtained from the star Sn−4 with center x by adding to it 4 more vertices, say, a,b,c,d, and three edges: {x,a,b},{a,b,c}, {a,b,d}. Clearly, |Ro(n)| = |K4 ∪ Sn−4| − 1, Ro(n)  ⊂ Sn, Ro(n)  ⊂ Co(n), and Ro(n)  ⊂ K4∪Sn−4. Hence, ex(4)(n;P) ex(3)(n;P) − 1, but, in view of inequality (1), the two numbers cannot be equal.

In a similar fashion, by choosing an appriopriate 4-extremal 3-graph, one can show that ex(4)(7;P) = ex(3)(7;P) − 1 and ex(4)(14;P) = ex(3)(14;P) − 1. With some additional eﬀort we were also able to calculate the remaining values of ex(4)(n;P) and determine the families Ex(4)(n;P) of 4-extremal 3-graphs. As these numbers are, however, of no use for calculating the respective Ramsey numbers, we state Theorem 10 without proof. Let K5+2 be the 3-graph obtained from K5 by ﬁxing two of its vertices, say a,b, and adding two more vertices c,d and two edges {a,b,c} and {a,b,d}.

##### Theorem 10.



12 and Ex(4)(n;P) = {G3(n),K5+2} for n = 7,

- 2n − 2 and Ex(4)(n;P) = {G3(n)} for 8 n 9, 20 and Ex(4)(n;P) = {K5 ∪ K5} for n = 10, 20 and Ex(4)(n;P) = {G3(n)} for n = 11, 28 and Ex(4)(n;P) = {G1(n),G2(n)} for n = 12, 33 and Ex(4)(n;P) = {K6 ∪ G1(n),K6 ∪ G2(n)} for n = 13, 40 and Ex(4)(n;P) = {2K6 ∪ 2K1,K4 ∪ S10)} for n = 14, 48 and Ex(4)(n;P) = {Ro(n),K6 ∪ S9} for n = 15,
- 3 + n−25 and Ex(4)(n;P) = {Ro(n)} for n 16.




- ex(4)(n;P) =




To determine Tura´n numbers, it is sometimes useful to rely on Theorem 3 and divide all 3-graphs into those which contain M and those which do not. To this end, it is convenient to deﬁne conditional Tur´an numbers (see [10, 11]). For a family of 3-graphs F, an F-free 3-graph G, and an integer n |V (G)|, the conditional Tur´n number is deﬁned as

ex(n;F|G) = max{|E(H)| : |V (H)| = n, H is F-free, and H ⊇ G}

Every n-vertex F-free 3-graph with ex(n;F|G) edges and such that H ⊇ G is called G-extremal for F. We denote by Ex(n;F|G) the family of all n-vertex 3-graphs which are G-extremal for F. (If F = {F}, we simply write F instead of {F}.)

To illustrate the above mentioned technique, observe that for n 7 ex(2)(n;P) = max{ex(n;P|M),ex(2)(n;M)} Thm= 3 max{ex(n;P|M),3n−8} = ex(n;P|M), the last equality holding for suﬃciently large n (see [11] for details).

In the proof of Theorem 9 we will use the following three lemmas, all proved in [11]. For the ﬁrst one we need one more piece of notation. If, in the above deﬁnition, we

restrict ourselves to connected 3-graphs only (connected in the weakest, obvious sense) then the corresponding conditional Tura´n number and the extremal family are denoted by exconn(n;F|G) and Exconn(n;F|G), respectively.

- Lemma 1 ([11]). For n 7, exconn(n;P|C) = 3n − 8 and Exconn(n;P|C) = {G1(n),G2(n)}.

Lemma 1 as stated in [11] does not provide family Exconn(n;P|C). However, it is clear form its proof that the C-extremal 3-graphs are the same as in Theorem 3.

- Lemma 2 ([11]).

ex(n;{P,C}|M) =

 



2n − 4 for 6 n 9, 20 for n = 10,

4 + n−24 and Ex(n;{P,C}|M) = {Co(n)} for n 11.

- Lemma 3 ([11]). For n 6 ex(n;{P,C,P2 ∪ K3}|M) = 2n − 4,

where P2 is a pair of edges sharing one vertex.

3 Proof of Theorem 2

As mentioned in the Introduction, the inequality R(P;r) r + 6, r 1, has been already observed in [9]. We are going to show that R(P;r) r + 6 for 8 r 9. Along the way, we need to strengthen the results for 3 r 7 as follows. Let Kn − e denote the 3-graph with n vertices and n3 − 1 edges, while Kn − 2e denote each of the three possible (up to isomorphism) 3-graphs with n vertices and n3 − 2 edges. Write H → (P;r) if every r-coloring of the edges of H yields a monochromatic copy of P.

- Lemma 4. For every n = 9,...,13, Kn − 2e → (P;n − 6).


Proof. A coloring which does not yield a monochromatic copy of P is referred to as proper. Below, for each n we assume that there is a proper coloring of Kn − 2e and arrive at a contradiction.

- n = 9: For every 3-coloring of K9 − 2e there is a color with at least 28 edges and thus, if it is proper, then, by Theorem 6, that color must form a full star. After removing the

center of that star, we obtain a proper 2-coloring of K8 − 2e, which, again by Theorem 6, contains a monochromatic copy of P, a contradiction.

- n = 10: For every 4-coloring of K10−2e there is a color with at least 30 edges and thus, if it is proper, then, by Theorems 6 and 7, that color must form a star. After removing the center of that star we are back to the n = 9 case.


- n = 11: For every 5-coloring of K11−2e there is a color with at least 33 edges and thus, if it is proper, then, again by Theorems 6 and 7, that color must form a star. After removing the center of that star we are back to the n = 10 case.

We leave the most diﬃcult case of n = 12 to the end of the proof.

n = 13: For every 7-coloring of K13−2e there is a color with at least 41 edges and thus, if it is proper, then, one more time by Theorems 6 and 7, that color must form a star. After removing the center of that star we jump to the n = 12 case.

- n = 12: Consider a 6-coloring of K12 − 2e. If a color forms a star, then, after removing its center, we obtain a 5-coloring of K11 − 2e (or K11 − e or K11) which, as we have already proved, contains o monochromatic copy of P. Thus, from now on we assume no color class forms a star. However, there is a color with at least 37 edges and thus, if it is proper, then, this time by Theorems 6-8, that color must be a sub-3-graph of


K6 ∪ K6. After removing that copy of K6 ∪ K6, we are looking at a proper 5-coloring of a complete, 6 by 6 bipartite 3-graph H, with possibly up to two edges missing. As |H| 220 − 40 − 2 = 178, the average number of edges per color is at least 35.6. On the other hand no color may have been applied to more than 36 edges. The reason is that, as explained above, such a color class would need to be a sub-3-graph of a copy of K6 ∪ K6, but it is easy to check that every copy of K6 ∪ K6 shares at most 36 edges with H. This implies that among the ﬁve color classes at least three have size 36. But it was shown already in [11] (proof of Theorem 1, case r = 6) that the coexistence of three disjoint sub-3-graphs in H, each having 36 edges and contained in a copy of K6 ∪ K6, is impossible.

| |
|---|


Proof of Theorem 2: In the case r = 8 we are going to prove a little stronger result to be used in the case r = 9.

- r = 8: For every 8-coloring of K14 − e there is a color with at least 46 edges, and thus, if it is proper, then, by Theorems 6, 7, and 9, that color must either form a star or be a sub-3-graph of the comet Co(14). In either case, we remove the center of the structure in question, a star or a comet, and in addition, if it is the comet, the edge spanned by its head. We get at a 7-coloring of K13 − e or K13 − 2e which, by Lemma 4, yields a monochromatic copy of P, a contradiction. It follows that K14 − e → (P;8), and so, K14 → (P;8) too. Hence, we have proved Theorem 2 for r = 8.
- r = 9: For every 9-coloring of K15 there is a color with at least 51 edges, and thus, if it is proper, then, again by Theorems 6, 7, and 9, that color must form a sub-3-graph of S15 or Co(15). Similarly to the case r = 8, we remove a vertex and possibly an edge, to obtain an 8-coloring of K14 or K14 −e, which, by the case r = 8 yields a monochromatic copy of P, a contradiction.


| |
|---|


### 4 Proof of Theorems 9

For n = 12, Theorem 9 has been already proved in [11] (cf. Theorem 8 in Introduction). Therefore, it seems natural to divide the proof into two ranges of n: smaller than 12

and larger than 12. The general set-up is, however, the same for both. We ﬁrst check that all candidates for being 3-extremal 3-graphs do qualify, that is, are P-free, are not contained in any of the 1-extremal or 2-extremal 3-graphs with the same number of vertices, and have the number of edges given by the formula to be proved. Then, we consider an arbitrary n-vertex, qualifying 3-graph H and show that unless it is one of the candidate 3-extremal 3-graphs itself, its number of edges is strictly smaller than theirs.

For the latter task, we distinguish two cases: when H is connected and disconnected. The entire proof is inductive, in the sense that here and there we apply the very

- Theorem 9 for smaller instances of n, once they have been conﬁrmed.


- 4.1 7 n 11 First note that by Theorems 6 and 7, for 7 n 11


Ex(1)(n;P) ∪ Ex(2)(n;P) = {Sn,K6 ∪ Kn−6}.

Moreover, for i ∈ {1,2}, Gi(n) Sn and Gi(n) K6 ∪Kn−6. Consequently, since Gi(n) is P-free,

ex(3)(n;P) |Gi(n)| = 3n − 8.

We are going to show that, in fact, the 3-graphs Gi(n), i ∈ {1,2} are the only 3-extremal 3-graphs for n 10, whereas, for n = 11, in addition, the comet Co(11) ∈ Ex(3)(11;P).

For 7 n 11, let H be an n-vertex P-free 3-graph, satisfying H Sn and H K6 ∪ Kn−6. (2)

We ﬁrst assume that H is connected. If H ⊃ C or H  ⊃ M then, by, respectively, Theorem 3 or Lemma 1,

|H| 3n − 8,

with the equality for H = Gi(n), i ∈ {1,2} only. Otherwise, |H| ex(n;{P,C}|M) 3n − 8,

where the second inequality holds by Lemma 2, and it becomes equality only if n = 11 and H = Co(11).

Next, we show that if a P-free 3-graph H satisfying (2) is disconnected, then |H| <

- 3n − 8. Let m = m(H) be the number of vertices in the smallest componet of H. Since n 11, we have m 5. Moreover, m = 2, since no component of a 3-graph may have two vertices. Thus, m ∈ {1,3,4,5}. Note also that, as a consequence of the second part of (2), no union of components of H may have 6 vertices together. Consequently,


- m = n − 6. We now break the proof into several cases. If n = 7, we must have m = 3 and thus,


|H| 1 + 4 < 3n − 8 = 13.

For n 8, if m = 1, that is, if there is an isolated vertex v in H, then H −v still satisﬁes

(2) with n − 1 instead of n, and, by induction,

|H| ex(3)(n − 1;P) 3(n − 1) − 8 < 3n − 8. If m = 3, then, for n = 8,10,11,we apply the bound

|H| 1 + ex(1)(n − 3;P) < 3n − 8, where the last inequality follows by Theorem 6. If m = 4, we have, similarly, |H| 4 + ex(1)(n − 4;P) < 3n − 8, for n = 8,9,11. Finally, if m = 5 (and n = 10), |H| 2 × 53 < 22.

- 4.2 n 13 By Theorems 6 and 7,


Ex(1)(13;P) ∪ Ex(2)(13;P) = {S13,Co(13),K6 ∪ K6 ∪ K1}, while for n 14,

Ex(1)(n;P) ∪ Ex(2)(n;P) = {Sn,Co(n)}, Therefore, to determine ex(3)(n;P) for n 13 we have to ﬁnd the largest number of edges in an n-vertex P-free 3-graph H such that H Sn, H Co(n) and for n = 13, in addition, H K6 ∪ K6 ∪ K1. The 3-graphs

Hn := K6 ∪ Sn−6 for n ∈ {13,14} and Hn := K4 ∪ Sn−4 for n 15 satisfy all the above conditions. Hence, for n 13,

ex(3)(n;P) |Hn|. We are going to show that also the opposite inequality holds, as well as, that the equality holds for Hn only.

To this end, let H = Hn be an n-vertex P-free 3-graph such that

H Sn, and H Co(n), (3) and for n = 13, in addition, H K6 ∪ K6 ∪ K1. We will show that |H| < |Hn|.

Assume ﬁrst that H is connected. If, in addition, H ⊃ C or H  ⊃ M, then, by, respectively, Lemma 1 or Theorem 3,

|H| 3n − 8 < |Hn|. Otherwise, H is a {P,C}-free, connected 3-graph containing M. Since, by Lemma 3, ex({n;P,C,P2 ∪ K3}|M) = 2n − 4 < |Hn|,

we may assume that P2 ∪ K3 ⊂ H. Thus, the connected case will be completed once we have proved the following lemma.

- Lemma 5. If H is a connected, n-vertex, n 13, {P,C}-free 3-graph such that H ⊃ P2 ∪ K3, and H Co(n), then |H| < |Hn|.


(Note that for n = 13, the additional requirement that H K6 ∪ K6 ∪ K1 is, due to connectedness, fulﬁlled automatically.) We devote an entire section to prove Lemma 5. Meanwhile, taking Lemma 5 for granted, let us quickly complete the proof of Theorem 9.

Assume that H is disconnected and, as before, let m = m(H) be the order of the smallest component of H, 1 m n − m, m = 2. Below, to bound |H|, we use the Tur´an numbers for P of the 1st, 2nd, and 3rd order and utilize, respectively, Theorems 6, 7, and 9 (per induction).

If v is an isolated vertex (m = 1), then, similarly as for small n, H − v satisﬁes (3), because otherwise H would not. Hence, for n 15,

|H| ex(3)(n − 1;P) < |Hn|.

For n = 14, we cannot guarantee that H − v  ⊂ K6 ∪ K6 ∪ K1, so we use the second order Tura´n number instead which still does the job:

- |H| ex(2)(13;P) = 40 < 41 = |H14|.

To complete the case m = 1 notice that for n = 13, since H K6 ∪ K6 ∪ K1, we have H − v  ⊂ K6 ∪ K6, and we are in position to use induction again. Hence,

- |H| ex(3)(12;P) = 32 < 35 = |H13|.


For m 3, let us express H as a vertex disjoint union of two 3-graphs:

H = H ∪ H , |V (H )| = m, |V (H )| = n − m Then, clearly, both H and H are P-free, and thus

|H| ex(1)(m;P) + ex(1)(n − m;P). (4) For m = 3, since H Co(n), we have H Sn−3 and consequently

|H| 1 + ex(2)(n − 3;P) < |Hn|, where the last inequality is easily veriﬁed by hand.

For m = 4 and n ∈ {13,14} by (4),

n − 5 2

|H| 4 + ex(1)(n − 4;P) = 4 +

< 20 +

n − 7 2

= |Hn|;

and for n 15, either H ⊆ Sn−4 and so H ⊆ K4 ∪ Sn−4 = Hn (in which case we are done) or H Sn−4 but then,

|H| 4 + ex(2)(n − 4;P) < 4 +

n − 5 2

= |Hn|.

- For m = 5 by (4),

|H| ex(1)(5;P) + ex(1)(n − 5;P) = 10 +

n − 6 2

< |Hn|.

- For m = 6 and n = 13, since H K6 ∪ K6 ∪ K1 we have H  ⊂ K6 ∪ K1 and so,


|H | ex(2)(7;P) = |S7| whereas for n 14, we bound |H | ex(1)(n − 6;P) = |Sn−6|. Hence, in both cases we have

|H| ex(1)(6;P) + |Sn−6| = 20 +

n − 7 2 |Hn|.

However, for n ∈ {13,14}, the ﬁrst inequality must be strict (since H = Hn), while for

- n 15 the second inequality is strict. For m = 7 we have n 14 and, by (4), for n = 14


|H| ex(1)(7;P) + ex(1)(7;P) = 20 + 20 < 41 = |H14|, whereas, for n 15

|H| ex(1)(7;P) + ex(1)(n − 7;P) = 20 +

n − 8 2

< 4 +

n − 5 2

= |Hn|.

Finally, for m 8 we have n 16 and, by (4),

|H| ex(1)(m;P) + ex(1)(n − m;P) =

m − 1 2

n − 9 2 <

n − m − 1 2

7 2

+

+

n − 5 2

n − 5 2

3 2

= |Hn|.

+

< 4 +

#### 4.3 Preparations for the proof of Lemma 5

Under the assumptions on H in Lemma 5, let Q be a copy of P2 in H such that there is at least one edge disjoint from U = V (Q). We know that Q exists, because P2∪K3 ⊂ H. Let V = V (H) and W = V \ U. Further, let W0 be the set of vertices of degree zero in H[W] and W1 = W \ W0. (see Fig. 2). Note that, by deﬁnition, H[W] = H[W1] and |W1| 3.

We also split the set of edges of H. First, notice that, since H is P-free, there is no edge with one vertex in each U, W0, and W1. Let for i = 0,1, Hi be the sub-3-graph of H composed of the edges intersecting both U and Wi. Then, clearly,

H = H[U] ∪ H[W] ∪ H0 ∪ H1, (5) with all four parts edge-disjoint.

![image 2](<2015-polcyn-refined-tur-numbers-ramsey_images/imageFile2.png>)

Figure 2: Set-up for the proof of Lemm 5

Let x be the vertex of degree two in Q. If for some h ∈ H0 ∪H1 we have |h∩U| = 1, then h ∩ U = {x}, since otherwise h together with Q would form a copy of P in H. We let

F0 = {h ∈ H0 ∪ H1 : h ∩ U = {x}}.

Also, the edges h ∈ H0 ∪ H1 with |h ∩ U| = 2 must be such that the pair h ∩ U is contained in an edge of Q, since otherwise h together with Q would form a copy of C in H. For k = 1,2, deﬁne

Fk = {h ∈ H0 ∪ H1 : |h ∩ U \ {x}| = k}.

We have H0 ∪ H1 = F0 ∪ F1 ∪ F2 (see Fig. 3.) Further, for i = 0,1 and k = 0,1,2, we set

Fik = Fk ∩ Hi.

![image 3](<2015-polcyn-refined-tur-numbers-ramsey_images/imageFile3.png>)

Figure 3: Three types of edges in H0 ∪ H1 Note that, since H is P-free, F11 = ∅ and thus,

H1 = F10 ∪ F12. (6)

Observe also that, because H is connected, H1 = ∅. Consequently, since the presence of any edge of H1 forbids at least 4 edges of H[U],

|H[U]| 6. (7)

In [11] the authors have proven the following bound on the number of edges in H1:

|H1| 2|W1| − 3. (8) We use (8) to estimate |H[W]| + |H1|.

- Fact 1. Set |W1| = z. We have


 

z

3 + 2z − 3 for 3 z 5,

z−1

2 + 2z − 3 for 6 z 7,

|H[W]| + |H1|

(9)



(z−1)2

2 + 2 for z 8.

Proof. For 3 z 5, the above inequality is an immediate consequence of (8), whereas for 6 z 7, we use (8) and the bound |H[W]| z−21 , stemming from Theorem 5. For z 8 we have to consider two cases. Suppose ﬁrst that H[W] ⊆ Sz with the center v ∈ W1. Since H is P-free, every edge h ∈ F12 must have h ∩ W1 = {v}. Hence, |F12| 2. Moreover, if e ∈ F10, then the pair e ∩ W1 must be nonseparable in H[W1], that is, every edge of H[W1] must contain both these vertices or none. Since, as it can be easily proved, there are at most z−21 nonseparable pairs in W1,

|F10|

z − 1 2

.

Consequently,

z − 1 2

|H1| 2 +

(10) and, again using Theorem 5,

(z − 1)2 2

z − 1 2

z − 1 2

|H[W]| + |H1|

+ 2 +

+ 2. (11) Otherwise, either H[W]  ⊇ M, and then, by Theorem 3,

|H[W]| 3z − 8, (12) or H[W] ⊇ M and then, by Lemma 2,

 

2z − 4 for 8 z 9, 20 for z = 10, 4 + z−24 for z 11.

|H[W]| ex(n;{P,C}|M) =

(13)



Consequently, by (8),

 

4z − 7 for 8 z 9, 37 for z = 10,

|H[W]| + |H1|

(14)



z−4

2 + 2z + 1 for z 11,

2

and it is easy to check that for z 8, the R-H-S of (14) is smaller than (z−1)

###### 2 + 2.

#### 4.4 Proof of Lemma 5

We adopt the notation from the previous subsection. In particular, recall that z = |W1|. Additionally, we set s = |W0|. Our plan is to ﬁrst give the proof in three ‘smallest’ cases: s = 0, z = 3, and n ∈ {13,14,15}.

- s = 0 (W0 = ∅). Then H0 = ∅, z = n − 5 8, and, by (5), (7), and (9),


(z − 1)2 2

|H| = |H[U]| + |H[W]| + |H1| 6 +

+ 2.

This implies that for n = 13, |H| 32 < 35, for n = 14, |H| 40 < 41, while for n 15, it can be easily checked that

(z − 1)2 2

|H| 6 +

+ 2 < 4 +

z 2

= |Hn|.

Therefore, from now on we will be assuming that W0 = ∅, or s 1. The proofs of the other two special cases, z = 3 and n ∈ {13,14,15}, are both split into two subcases with respect to F12. We begin with bounding the number of edges in H[U ∪ W0] when F12 = ∅.

- Fact 2. If F12 = ∅, then


 

8 for s = 1, 3s + 7 for 2 s 4,

|H[U ∪ W0]|

(15)



s+2

2 + 1 for s 5.

Proof. Let u and v be some two vertices of U belonging to the same edge of F12. If H[U ∪ W0] ⊆ Ss+5 (with the center in x), then, since H is P-free, the only edge of H[U ∪ W0] containing u or v is {x,u,v}. Hence

s + 2 2

|H[U ∪ W0]|

+ 1. (16)

Otherwise, either H[U ∪ W0]  ⊇ M and, assuming that s 2, and thus |U ∪ W0| 7, by Theorem 3,

|H[U ∪ W0]| ex(2)(s + 5;M) = 3(s + 5) − 8 = 3s + 7, (17) or H[U ∪ W0] ⊇ M and, by Lemma 2, this time including s = 1,

 

2s + 6 for 1 s 4, 20 for s = 5, 4 + s+12 for s 6.

|H[U ∪ W0]| ex(s + 5;{P,C}|M) =

(18)



For s = 1 we argue as follows. Since H is P-free, every edge of H[U ∪ W0] must contain either both of u and v or none. There are only 8 such edges and so, |H[U ∪ W0]| 8. In summary, (15) follows by (16), (17), (18), and the above bound for s = 1.

z = 3, F21 = ∅. We combine bounds (9) of Fact 1 and (15) to estimate |H|. Since s = n − 5 − z 13 − 8 = 5,

s + 2 2

3 3

|H| = |H[U ∪ W0]| + |H1| + |H[W]|

+ 2 · 3 − 3 = n − 6 2

+ 1 +

+ 5 < |Hn|.

z = 3, F21 = ∅. Then, by (6), |H1| |F10| 3. Since H Co(n) we have H[U ∪ W0] Ss+5 and consequently, by Theorem 7,

H[U ∪ W0] ex(2)(s + 5;P) =

20 + s−31 for 10 s + 5 12, 4 + s+12 for s + 5 13

Hence, for 13 n 15 (10 s + 5 12)

|H| = |H[U ∪ W0]| + |H1| + |H[W]| 20 +

s − 1 3

+ 3 + 1 = 24 +

n − 9 3

< |Hn|,

while for n 16 (s + 5 13)

|H| = |H[U ∪ W0]| + |H1| + |H[W]| 4 +

n − 7 2

8 +

< 4 +

s + 1 2

n − 5 2

+ 3 + 1 =

= |Hn|.

Consequently for the rest of the proof we will be assuming that z 4 (and s 1).

n ∈ {13,14,15}, F21 = ∅. We again combine bounds (9) of Fact 1 and (15) to estimate |H|. For n = 13 = 5 + s + z, where 4 z 7, the worst case is when z = 7 and s = 1, in which we get

|H| 34 < 35.

- For n = 14 = 5 + s + z, where 4 z 8, the worst case is when z = 7 and s = 2, and so

|H| 39 < 41.

- For n = 15 = 5 + s + z, where 4 z 9, |H| 42 < 49.


n ∈ {13,14,15}, F21 = ∅. For z = 4 by an easy inspection one can show that |H1| + |H[W]| 1 + 2 = 3. Also, since H is C-free, by Theorem 5, |H[U ∪ W0]| s+42 . Therefore, for n = 13, |H| 28+3 < 35, for n = 14, |H| 36+3 < 41, and for n = 15, |H| 45 + 3 < 49.

Finally, for z 5, we may apply Theorem 5 to H[W1 ∪ {x}], obtaining the bound

z 2

|H1| + |H[W]| = |H[W1 ∪ {x}]|

.

In summary,

|H| = |H[U ∪ W0]| + |H1| + |H[W]|

s + 4 2

+

z 2

,

and consequently, by choosing optimal pairs (z,s), for n = 13 = 5 + s + z, where

- 5 z 7, we get |H| 31 < 35,


for n = 14 = 5 + s + z, where 5 z 8, we get

|H| 38 < 41, whereas for n = 15 = 5 + s + z, where 5 z 9,

|H| 46 < 49.

Thus, we are done with the proof of Lemma 5 in all three cases: s = 0, z = 3, and n ∈ {13,14,15}. In fact, recalling our argument from Section 4.2, we have actually proved Theorem 9 for all n 15. To complete the proof of Lemma 5 for the remaining values of n, we need only to prove Fact 3 below. The proof is by induction on n, and we include the case n = 15 there to serve as the inductive base.

Note that compared to Lemma 5, we now relax the assumption of connectivity, replacing it with that of H1 = ∅. Also, although we have already proved Lemma 5 for s = 0, or W0 = ∅, we do not impose the opposite assumption here. Both these relaxations are made to accommodate the inductive proof below. Finally, note that we may drop the assumption that H Co(n), as it follows from the fact that |W1| 4 (a comet cannot contain two edges not containing the center). For a 3-graph G and a vertex v ∈ V (G), let G(v) denote the link graph of v in G, that is, the set of pairs of vertices which together with v form an edge of G.

- Fact 3. If H is an n-vertex, n 15, {P,C}-free 3-graph such that H ⊃ P2 ∪ K3, and, under the notation of Subsection 4.3, z = |W1| 4 and H1 = ∅, then


n − 5 2

|H| < 4 +

= |Hn|.

Proof. The proof is by induction on n with the initial step n = 15 done earlier. Let n 16. It can be easily checked that, since H is P-free, for every v ∈ W either

F0(v) = ∅ or F2(v) = ∅. (19) Moreover, by the deﬁnitions of F1 and F2,

|F1(v)| 4 and |F2(v)| 2. (20)

If W0 = ∅, then we are done by an earlier proof (at the beginning of this section). Otherwise, ﬁx v ∈ W0 and observe that, by the remark preceding (5), |F0(v)| |W0|−1. Thus, by (19) and (20), since |W0| = n − 5 − |W1| n − 9,

|H(v)| = |F0(v)|+|F1(v)|+|F2(v)| 4+max{2,|W0|−1} 4+n−10 = n−6. (21)

Notice that H − v satisﬁes the assumptions of Fact 3. Indeed, as the removal of v aﬀects H0 only, in the obtained sub-3-graph we still have both, H1 = ∅ and |W1| 4. Consequently, by the induction’s assumption and (21)

|H| = |H − v| + |H(v)| < 4 +

n − 6 2

+ n − 6 = 4 +

n − 5 2

= |Hn|.

| |
|---|


### References

- [1] R. Csa´k´any, J. Kahn, A homological Approach to Two Problems on Finite Sets, Journal of Algebraic Combinatorics 9 (1999), 141-149.
- [2] P. Erdo¨s, C. Ko, R. Rado, Intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. 12(2) (1961), 313-320.
- [3] P. Frankl, Z. F¨uredi, Exact solution of some Tura´n-type problems, J. Combin. Th. Ser. A 45 (1987), 226-262.
- [4] P. Frankl, Z. Fu¨redi, Non-trivial Intersecting Families, J. Combin. Th. Ser. A 41

(1986), 150-153.

- [5] Z. Fu¨redi, T. Jiang, R. Seiver, Exact solution of the hypergraph Tur´an problem for k-uniform linear paths, Combinatorica 34(3) (2014), 299-322.
- [6] A. Gy´arfa´s, G. Raeisi, The Ramsey number of loose triangles and quadrangles in hypergraphs, Electron. J. Combin. 19(2) (2012), # R30.
- [7] J. Han, Y. Kohayakawa, Maximum size of a non-trivial intersecting uniform family which is not a subfamily of the Hilton-Milner family, submitted.
- [8] A.J.W. Hilton, E.C. Milner, Some intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. 18(2) (1967), 369-384.
- [9] E. Jackowska The 3-colored Ramsey number of 3-uniform loos paths of length 3, Australasian J. Combin, 63(2) (2015), 314-320.
- [10] E. Jackowska, J. Polcyn, A Rucin´ski, Tura´n numbers for linear 3-uniform paths of length 3, submitted.


- [11] E. Jackowska, J. Polcyn, A Ruci´nski, Multicolor Ramsey numbers and restricted Tur´an numbers for the loose 3-uniform path of length three, submitted.
- [12] A. Kostochka, D. Mubayi, J. Verstra¨ete, Tur´an Problems and Shadows I: Paths and Cycles, J. Combin. Theory Ser. A 129 (2015), 57-79.
- [13] G.R. Omidi, M. Shahsiah, Ramsey Numbers of 3-Uniform Loose Paths and Loose Cycles, J. Comb. Theory, Ser. A 121 (2014), 64-73.


