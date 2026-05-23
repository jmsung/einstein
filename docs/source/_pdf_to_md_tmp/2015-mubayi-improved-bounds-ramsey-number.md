arXiv:1511.09104v2[math.CO]3Feb2016

Improved bounds for the Ramsey number of tight cycles versus cliques

Dhruv Mubayi∗

Abstract

The 3-uniform tight cycle Cs3 has vertex set Zs and edge set {{i,i + 1,i + 2} : i ∈ Zs}. We prove that for every s  ≡ 0 (mod 3) and s ≥ 16 or s ∈ {8,11,14} there is a cs > 0 such that the 3-uniform hypergraph Ramsey number r(Cs3,Kn3) satisﬁes

r(Cs3,Kn3) < 2c

snlogn.

This answers in strong form a question of the author and Ro¨dl who asked for an upper bound of the form 2n

1+ǫs for each ﬁxed s ≥ 4, where ǫs → 0 as s → ∞ and n is suﬃciently large. The result is nearly tight as the lower bound is known to be exponential in n.

# 1 Introduction

A triple system or 3-graph H with vertex set V (H) is a collection of 3-element subsets of V (H). Write Kn3 for the complete 3-graph with vertex set of size n . Given 3-graphs F,G, the Ramsey number r(F,G) is the minimum n such that every red/blue coloring of Kn3 results in a monochromatic red copy of F or a monochromatic blue copy of G. In this paper we consider the 3-graph Ramsey number of cycles versus complete 3-graphs.

For ﬁxed s ≥ 3 the graph Ramsey number r(Cs,Kt) has been extensively studied. The case s = 3 is one of the oldest questions in Ramsey theory and it is known that r(C3,Kt) = Θ(t2/log t) (see [1, 7] and [3, 6] for recent improvements). The next case r(C4,Kt) seems substantially more diﬃcult and the best known upper and lower bounds are O(t2/log2 t) and Ω(t3/2/log t), respectively. An old open problem of Erd˝os asks whether there is a positive ǫ for which r(C4,Kt) = O(t2−ǫ). For larger cycles, the best known bounds can be found in [2, 11], and the order of magnitude of r(Cs,Kt) is not known for any ﬁxed s ≥ 4.

There are several natural ways to deﬁne a cycle in hypergraphs. Two possibilities are to consider loose cycles and tight cycles. Here we consider tight cycles. For s > 3, the tight cycle Cs3 is the 3-graph with vertex set Zs (integers modulo s) and edge set

{{i,i + 1,... ,i + k − 1} : i ∈ Zs}.

![image 1](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile1.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Research partially supported by NSF grant DMS-1300138. Email: mubayi@uic.edu

We can view the vertex set of Cs3 as s points on a circle and the edge set as the s circular subintervals each containing 3 consecutive vertices.

The author and Ro¨dl [9] investigated the hypergraph Ramsey number r(Cs3,Kn3) for ﬁxed s ≥ 5 and large n. When s ≡ 0 (mod 3) the tight cycle Cs3 is 3-partite, and in this case it is trivial to observe that r(Cs3,Kn3) grows like a polynomial in n. Determining the growth rate of this polynomial appears to be a very diﬃcult problem and the order of magnitude is not known for any s > 3. When s  ≡ 0 (mod 3) the Ramsey number is exponential in n as shown in [9] below.

- Theorem 1.1. ([9]) Fix s ≥ 5 and s  ≡ 0 (mod 3). There are positive constants c1 and c2 such that


2c1n < r(Cs3,Kn3) < 2c2n2 logn.

Note that when s = 4, the cycle C43 is K43 and in this case the lower bound was proved much earlier by Erd˝os and Hajnal [5], and in fact has been improved to 2c1nlogn more recently by Conlon-FoxSudakov [4].

As s gets large, the tight cycle Cs3 becomes sparser, so one might expect that r(Cs3,Kn3) decreases as a function of n (for ﬁxed s). This was asked by Ro¨dl and the author in [9].

Problem 1.2. ([9]) Is the following true? For each ﬁxed s ≥ 4 there exists ǫs such that ǫs → 0 as s → ∞ and

r(Cs3,Kn3) < 2n1+ǫs for all suﬃciently large n.

In this short note we give an aﬃrmative answer to this problem by proving the following stronger upper bound.

- Theorem 1.3. Fix a positive integer s  ≡ 0 (mod 3) such that s ≥ 16 or s ∈ {8,11,14}. There is a positive constant c such that


r(Cs3,Kn3) < 2cnlogn.

Proving a similar result for small values of s remains an open problem, in particular, the cases s ∈ {4,5,7,10,13}.

# 2 Proof

The proof of Theorem 1.3 has three components. The ﬁrst is an observation from [9] that the supersaturation phenomenon from extremal hypergraph theory can be applied to hypergraph Ramsey problems. The crucial new observation here is that we can apply this to families of hypergraphs rather than just individual ones. The second is a strengthening of the original proof due to Erd˝os and Hajnal [5] that r(K43 \ e,Kn3) < 2cnlogn for some absolute c > 0, where K43 \ e is the triple system with four vertices and three edges (another proof of this upper bound has been given by Conlon-Fox-Sudakov [4], though that proof is not suitable for our purposes). Finally, the third component is an explicit homomorphism of C83 into a particular 3-graph H6 on six vertices.

In order to apply the program above to solve Problem 1.2 (and prove Theorem 1.3), we need to ﬁnd an F for which r(F,Kn3) = 2n1+o(1) on the one hand, and Cs3 can be embedded in a blowup of F on the other hand. We remark that there are no (non 3-partite) 3-graphs F for which the order of magnitude of log r(F,Kn3) is known, and the only (non 3-partite) F for which r(F,Kn3) = 2n1+o(1) is known is F = K43 \ e. But tight cycles to not embed into a blowup of K43 \ e. We overcome this problem by ﬁnding a (new) family F of 3-graphs for which we can prove r(F,Kn3) = 2n1+o(1) and yet embed tight cycles in blowups of each member of F.

## 2.1 Supersaturation

Given a hypergraph H and vertex v ∈ V (H), we say that w ∈ V (H) is a clone of v if no edge contains both v and w and for every e ∈ H, v ∈ e if and only if (e ∪ {w}) \ v ∈ H. Given a triple system F and a vertex v in F, let F(v) be the triple system obtained from F by replacing v with two clones v1,v2. We will use the following result of the author and Ro¨dl.

Theorem 2.1. ([9]) Let F be a triple system with f vertices and v ∈ V (F). Then r(F(v),Kn3) < (r(F,Kn3))f + f.

A blowup of F is a a hypergraph obtained by successively applying the cloning operation. In particular, if each vertex is cloned p times, then denote the obtained blowup as F(p). By applying Theorem 2.1 repeatedly, we obtain the following easy corollary.

- Corollary 2.2. ([9]) Fix a k-graph F and an integer p ≥ 2. There exists c = c(F,p) such that r(F(p),Kn3) < (r(F,Kn3))c.

Given a ﬁnite family F of 3-graphs, deﬁne r(F,Kn3) to be the minimum N such that every red/blue coloring of KN3 results in a red copy of some member of F or a blue copy of Kn3. Also, for a positive integer p, deﬁne F(p) = {F(p) : F ∈ F}. By using the pigeonhole principle, a trivial modiﬁcation of the proof of Corollary 2.2 yields the following extension to ﬁnite families.

- Corollary 2.3. Fix a ﬁnite family F of k-graphs and an integer p ≥ 2. There exists c = c(F,p) such that


r(F(p),Kn3) < (r(F,Kn3))c.

## 2.2 The triple systems H5 and H6

Deﬁne H5 to be the 3-graph with vertex set {a,b,u,v,w} and edge set {abu,abv,abw,auv,buw} and H6 to be the 3-graph with vertex set {a,b,u,v,w,x} and edge set {abu,abv,abw,abx,auv,bwx}. We will need the following result result of Spencer [10]. Suppose H is an N vertex triple system with average degree at most D. Then H has an independent set of size at least (2/3)N/D1/2.

Theorem 2.4. There is an absolute positive constant c such that r({K43,H5,H6},Kn3) < 2cnlogn.

Proof. Suppose that H is an N vertex triple system with no independent set of size n. We will show that H contains a copy of some member in {K43,H5,H6} as long as N ≥ 4n(n!)2. By interpreting the edges of H as the red edges in a red/blue coloring of KN3 , this proves the theorem.

We proceed by induction on n. The result is clearly true for n = 1. Suppose it holds for n − 1 and let us show it for n. If every pair of vertices in H lie in at most d = 4n−1(n − 1)!2 edges, then the number of edges of H is at most N2 d/3 and the average degree of H is at most

N 2 d

=

D =

![image 2](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile2.png>)

N

d(N − 1) 2

.

![image 3](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile3.png>)

Therefore by [10], H has an independent set of size at least

N D1/2

- 2

![image 4](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile4.png>)

- 3


=

![image 5](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile5.png>)

- 2

![image 6](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile6.png>)

- 3


N (d(N − 1)/2)1/2

>

![image 7](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile7.png>)

N1/2 d1/2

- 2

![image 8](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile8.png>)

- 3


![image 9](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile9.png>)

2nn! 2n−1(n − 1)!

- 2

![image 10](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile10.png>)

- 3


≥

> n,

![image 11](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile11.png>)

a contradiction.

We may therefore assume that there is pair of vertices a,b in H that lie in at least d + 1 edges. Consider the set N(a,b) = {x : abx ∈ H}. Since |N(a,b)| > d, by induction, N(a,b) contains a copy of some member of {K43,H5,H6} or an independent set S of size at least n − 1. We may assume the latter, otherwise we are done. Now we may use a or b to enlarge the independent set S by one. If we succeed, then we obtain an independent set of size n, which is a contradiction, so we may assume that there is an edge of the form auv and an edge of the form bwx where u,v,w,x ∈ S. Let t = |{u,v} ∩ {w,x}|. If t = 2, then a,b,u,v forms a copy of K43, if t = 3, then we get a copy of H5 and if t = 4, then a,b,u,v,w,x forms a copy of H6.

![image 12](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile12.png>)

![image 13](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile13.png>)

![image 14](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile14.png>)

![image 15](<2015-mubayi-improved-bounds-ramsey-number_images/imageFile15.png>)

Using Theorem 2.4, Corollary 2.3, and the fact that H6 is a subhypergraph of K43(2) and a subhypergraph of H5(2), we obtain the following.

Corollary 2.5. There is an absolute positive constant c such that r(H6,Kn3) < 2cnlogn.

## 2.3 Embedding cycles

In order to ﬁnish the proof, we will show that for all s ≥ 5,

- (1) C83 ⊂ H6(2),
- (2) Cs3+3 ⊂ Cs3(2), and
- (3) C23s ⊂ Cs3(2). We will apply (1)–(3) together with Corollaries 2.2 and 2.5. Using (1) we obtain


r(C83,Kn3) ≤ r(H6(2),Kn3)) < (r(H6,Kn3))O(1) < 2O(nlogn).

- Using (2) repeatedly we obtain for all s ≡ 2 (mod 3) and s ≥ 11, that r(Cs,Kn3) ≤ r(C8(s),Kn3) < (r(C8,Kn3))O(1) < 2O(nlogn).


- Using (3) for s = 16 ≡ 1 (mod 3) we obtain


r(C16,Kn3) ≤ r(C8(2),Kn3) < (r(C8,Kn3))O(1) < 2O(nlogn). Finally, applying (2) again will ﬁnish the proof for all s ≡ 1 (mod 3) and s ≥ 16.

We now turn to the proofs of (1)–(3). Recall that H6 = {abu,abv,abw,abx,auv,bwx}. Showing that C83 ⊂ H6(2) is equivalent to producing a homomorphism φ from C83 to H6 where every vertex of H6 has at most two preimages. Deﬁne φ as follows:

- φ(1) = u
- φ(2) = v


φ(8) = φ(3) = a φ(7) = φ(4) = b

- φ(5) = x
- φ(6) = w.


It is easy to check that for every i ∈ Z8 we have φ(i)φ(i + 1)φ(i + 2) ∈ H6. Next we show that (2) holds by producing φ : Zs+3 → Zs as follows: let φ(i) = i for i ∈ {1,... ,s}, φ(s + 1) = s − 2, φ(s + 2) = s − 1 and φ(s + 3) = s. It is easy to check that φ is a homomorphism from V (Cs3+3) to V (Cs3). Finally, (3) holds due to φ : Z2s → Zs as follows: let φ(i) = φ(s + i) = i for i ∈ {1,... ,s}.

# References

- [1] M. Ajtai, J. Komlo´s and E. Szemere´di: A Note on Ramsey Numbers. J. Combin. Theory Ser. A, 29 (1980) 354–360.
- [2] T. Bohman and P. Keevash, The early evolution of the H-free process, Inventiones Mathematicae, 181 (2010) 291–336.
- [3] T. Bohman and P. Keevash, Dynamic concentration of the triangle-free process, submitted, http://arxiv.org/abs/1302.5963arXiv.1302.5963.
- [4] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23

(2010), no. 1, 247–266.

- [5] P. Erd˝os and A. Hajnal, On Ramsey like theorems, Problems and results, Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 123–140, Inst. Math. Appl., Southhend-on-Sea, 1972.
- [6] G. Fiz Pontiveros, S. Griﬃths, R. Morris, The triangle-free process and R(3,k), submitted, http://arxiv.org/abs/1302.6279 arXiv.1302.6279.
- [7] J.H. Kim, The Ramsey number R(3,t) has order of magnitude t2/log t, Random Structures & Algorithms, 7 (1995) 173–207.
- [8] A. Kostochka, D. Mubayi, J. Verstrae¨te, On independent sets in hypergraphs, Random Structures & Algorithms, 44 224–239.


- [9] D. Mubayi, V. Ro¨dl, Hypergraph Ramsey numbers: tight cycles versus cliques, to appear, Bulletin of the London Mathematical Society.
- [10] J. Spencer, Tura´n theorem for k-graphs, Disc. Math. 2 (1972), 183–186.
- [11] B. Sudakov, A new lower bound for a Ramsey-type problem, Combinatorica 25 (2005), 487– 498.


