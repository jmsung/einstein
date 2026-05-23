arXiv:1405.6587v2[math.CO]20Sep2014

On the grid Ramsey problem and related questions

David Conlon ∗ Jacob Fox † Choongbum Lee ‡ Benny Sudakov §

Abstract

The Hales–Jewett theorem is one of the pillars of Ramsey theory, from which many other results follow. A celebrated theorem of Shelah says that Hales–Jewett numbers are primitive recursive. A key tool used in his proof, now known as the cube lemma, has become famous in its own right. In its simplest form, this lemma says that if we color the edges of the Cartesian product Kn × Kn in r colors then, for n suﬃciently large, there is a rectangle with both pairs of opposite edges receiving the same color. Shelah’s proof shows that n = r(

) + 1 suﬃces. More than twenty years ago, Graham, Rothschild and Spencer asked whether this bound can be improved to a polynomial in r. We show that this is not possible by providing a superpolynomial lower bound in r. We also discuss a number of related problems.

r+1 2

# 1 Introduction

Ramsey theory refers to a large body of deep results in mathematics whose underlying philosophy is captured succinctly by the statement that “Every large system contains a large well-organized subsystem.” This is an area in which a great variety of techniques from many branches of mathematics are used and whose results are important not only to combinatorics but also to logic, analysis, number theory and geometry.

One of the pillars of Ramsey theory, from which many other results follow, is the Hales–Jewett theorem [13]. This theorem may be thought of as a statement about multidimensional multiplayer tic-tac-toe, saying that in a high enough dimension one of the players must win. However, this fails to capture the importance of the result, which easily implies van der Waerden’s theorem on arithmetic progressions in colorings of the integers and its multidimensional generalizations. To quote [11], “The Hales–Jewett theorem strips van der Waerden’s theorem of its unessential elements and reveals the heart of Ramsey theory. It provides a focal point from which many results can be derived and acts as a cornerstone for much of the more advanced work.”

To state the Hales–Jewett theorem formally requires some notation. Let [m] be the set of integers {1,2,... ,m}. We will refer to elements of [m]n as points or words and the set [m] as the alphabet. For any a ∈ [m]n, any x ∈ [m] and any set γ ⊂ [n], let a ⊕ xγ be the point of [m]n whose j-th

![image 1](<2014-conlon-grid-ramsey-problem-related_images/imageFile1.png>)

∗Mathematical Institute, Oxford OX2 6GG, United Kingdom. Email: david.conlon@maths.ox.ac.uk. Research supported by a Royal Society University Research Fellowship.

†Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: fox@math.mit.edu. Research supported by a Packard Fellowship, by a Simons Fellowship, by NSF grant DMS-1069197, by an Alfred P. Sloan Fellowship and by an MIT NEC Corporation Award.

‡Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: cb lee@math.mit.edu. Research supported in part by NSF Grant DMS-1362326.

![image 2](<2014-conlon-grid-ramsey-problem-related_images/imageFile2.png>)

§Department of Mathematics, ETH, 8092 Zurich. Email: benjamin.sudakov@math.ethz.ch. Research supported in part by SNSF grant 200021-149111 and by a USA-Israel BSF grant.

component is aj if j  ∈ γ and x if j ∈ γ. A combinatorial line is a subset of [m]n of the form {a ⊕ xγ : 1 ≤ x ≤ m}. The Hales–Jewett theorem is now as follows.

- Theorem 1.1. For any m and r there exists an n such that any r-coloring of the elements of [m]n contains a monochromatic combinatorial line.


The original proof of the Hales–Jewett theorem is similar to that of van der Waerden’s theorem, using a double induction, where we prove the theorem for alphabet [m + 1] and r colors by using the statement for alphabet [m] and a much larger number of colors. This results in bounds of Ackermann type for the dependence of the dimension n on the size of the alphabet m. In the late eighties, Shelah [18] made a major breakthrough by ﬁnding a way to avoid the double induction and prove the theorem with primitive recursive bounds. This also resulted in the ﬁrst primitive recursive bounds for van der Waerden’s theorem (since drastically improved by Gowers [10]).

Shelah’s proof relied in a crucial way on a lemma now known as the Shelah cube lemma. The simplest case of this lemma says that if we color the edges of the Cartesian product Kn × Kn in r colors then, for n suﬃciently large, there is a rectangle with both pairs of opposite edges receiving the same color. Shelah’s proof shows that we may take n ≤ r(r+12 ) + 1. In the second edition of their book on Ramsey theory [11], Graham, Rothschild and Spencer asked whether this bound can be improved to a polynomial in r. Such an improvement, if it could be generalized, would allow one to improve Shelah’s wowzer-type upper bound for the Hales–Jewett theorem to a tower-type bound. The main result of this paper, Theorem 1.2 below, answers this question in the negative by providing a superpolynomial lower bound in r. We will now discuss this basic case of Shelah’s cube lemma, which we refer to as the grid Ramsey problem, in more detail.

## 1.1 The grid Ramsey problem

For positive integers m and n, let the grid graph Γm,n be the graph on vertex set [m]×[n] where two distinct vertices (i,j) and (i′,j′) are adjacent if and only if either i = i′ or j = j′. That is, Γm,n is the Cartesian product Km ×Kn. A row of the grid graph Γm,n is a subgraph induced on a vertex subset of the form {i} × [n] and a column is a subgraph induced on a vertex subset of the form [m] × {j}.

A rectangle in Γm,n is a copy of K2 × K2, that is, an induced subgraph over a vertex subset of the form {(i,j),(i′,j),(i,j′),(i′,j′)} for some integers 1 ≤ i < i′ ≤ m and 1 ≤ j < j′ ≤ n. We will usually denote this rectangle by (i,j,i′,j′). For an edge-colored grid graph, an alternating rectangle is a rectangle (i,j,i′,j′) such that the color of the edges {(i,j),(i′,j)} and {(i,j′),(i′,j′)} are equal and the color of the edges {(i,j),(i,j′)} and {(i′,j),(i′,j′)} are equal, that is, opposite sides of the rectangle receive the same color. An edge coloring of a grid graph is alternating-rectangle-free (or alternating-free, for short) if it contains no alternating rectangle. The function we will be interested in estimating is the following.

Deﬁnition. (i) For a positive integer r, deﬁne G(r) as the minimum integer n for which every edge coloring of Γn,n with r colors contains an alternating rectangle. (ii) For positive integers m and n, deﬁne g(m,n) as the minimum integer r for which there exists an alternating-free edge coloring of Γm,n with r colors. Deﬁne g(n) = g(n,n).

Note that the two functions G and g deﬁned above are in inverse relation to each other, in the sense that G(r) = n implies g(n − 1) ≤ r and g(n) ≥ r + 1, while g(n) = r implies G(r) ≥ n + 1 and G(r − 1) ≤ n.

We have already mentioned Shelah’s bound G(r) ≤ r(r+12 ) + 1. To prove this, let n = r(r+12 ) + 1 and suppose that an r-coloring of Γr+1,n is given. There are at most r(r+12 ) ways that one can color the edges of a ﬁxed column with r colors. Since the number of columns is n > r(r+12 ), the pigeonhole principle implies that there are two columns which are identically colored. Let these columns be the j-th column and the j′-th column and consider the edges that connect these two columns. Since there are r + 1 rows, the pigeonhole principle implies that there are two rows that have the same color. Let these be the i-th row and the i′-th row. Then the rectangle (i,j,i′,j′) is alternating. Hence, we see that G(r) ≤ n, as claimed. This argument in fact establishes the stronger bound g(r + 1,r(r+12 ) + 1) ≥ r + 1.

It is surprisingly diﬃcult to improve on this simple bound. The only known improvement, G(r) ≤ r(r+12 ) − r(r−21)+1 + 1, which improves Shelah’s bound by an additive term, was given by Gy´arf´as [12]. Instead, we have focused on the lower bound, proving that G(r) is superpolynomial in

- r. As already mentioned, this addresses a question of Graham, Rothschild and Spencer [11]. This question was also reiterated by Heinrich [14] and by Faudree, Gy´arf´as and Szo˝nyi [8], who proved a lower bound of Ω(r3). Quantitatively, our main result is the following.


- Theorem 1.2. There exists a positive constant c such that

G(r) > 2c(logr)5/2/

√log logr.

![image 3](<2014-conlon-grid-ramsey-problem-related_images/imageFile3.png>)

We will build up to this theorem, ﬁrst giving a substantially simpler proof for the weaker bound G(r) > 2clog2 r. The following theorem, which includes this result, also contains a number of stronger bounds for the oﬀ-diagonal case, improving results of Faudree, Gy´arf´as and Szo˝nyi [8].

- Theorem 1.3. (i) For all C > e2, g(rlogC/2,rr/2C) ≤ r for large enough r.


- (ii) For all positive constants ε, g(2εlog2 r,2r1−ε) ≤ r for large enough r.
- (iii) There exists a positive constant c such that g(cr2,rr2/2/er2) ≤ r for large enough r.


Part (i) of this theorem already shows that G(r) is superpolynomial in r, while part (ii) implies the more precise bound G(r) > 2clog2 r mentioned above, though at the cost of a weaker oﬀ-diagonal result. For (m,n) = (r + 1,r(r+12 )), it is easy to ﬁnd an alternating-free edge coloring of Γm,n with r colors by reverse engineering the proof of Shelah’s bound G(r) ≤ r(r+12 )+1. Part (iii) of Theorem 1.3 shows that n can be close to r(r+12 ) even when m is quadratic in r. This goes some way towards explaining why it is so diﬃcult to improve the bound G(r) ≤ r(r+12 ).

## 1.2 The Erdo˝s–Gy´arf´as problem

The Ramsey-type problem for grid graphs considered in the previous subsection is closely related to a problem of Erd˝os and Gy´arf´as on generalized Ramsey numbers. To discuss this problem, we need some deﬁnitions.

Deﬁnition. Let k,p and q be positive integers satisfying p ≥ k + 1 and 2 ≤ q ≤ k p .

- (i) For each positive integer r, deﬁne Fk(r,p,q) as the minimum integer n for which every edge coloring of Kn(k) with r colors contains a copy of Kp(k) receiving at most q − 1 distinct colors on its edges.


- (ii) For each positive integer n, deﬁne fk(n,p,q) as the minimum integer r for which there exists an edge coloring of Kn(k) with r colors such that every copy of Kp(k) receives at least q distinct colors on its edges.


For simplicity, we usually write F(r,p,q) = F2(r,p,q) and f(n,p,q) = f2(n,p,q). As in the previous subsection, the two functions are in inverse relation to each other: F(r,p,q) = n implies f(n,p,q) ≥ r+1 and f(n−1,p,q) ≤ r, while f(n,p,q) = r implies F(r,p,q) ≥ n+1 and F(r−1,p,q) ≤ n.

The function F(r,p,q) generalizes the Ramsey number since F(2,p,2) is equal to the Ramsey number R(p). Call an edge coloring of Kn a (p,q)-coloring if every copy of Kp receives at least q distinct colors on its edges. The deﬁnitions of F(r,p,q) and f(n,p,q) can also be reformulated in terms of (p,q)-colorings. For example, f(n,p,q) asks for the minimum integer r such that there is a (p,q)-coloring of Kn using r colors.

The function f(n,p,q) was ﬁrst introduced by Erd˝os and Shelah [5, 6] and then was systematically studied by Erd˝os and Gy´arf´as [7]. They studied the asymptotics of f(n,p,q) as n tends to inﬁnity for various choices of parameters p and q. It is clear that f(n,p,q) is increasing in q, but it is interesting to understand the transitions in behavior as q increases. At one end of the spectrum, f(n,p,2) ≤ f(n,3,2) ≤ ⌈log n⌉, while, at the other end, f(n,p, p2 ) = n2 (provided p ≥ 4). In the middle range, Erd˝os and Gy´arf´as proved that f(n,p,p) ≥ n1/(p−2) − 1, which in turn implies that f(n,p,q) is polynomial in n for any q ≥ p. A problem left open by Erd˝os and Gy´arf´as was to determine whether f(n,p,p − 1) is also polynomial in n.

For p = 3, it is easy to see that f(n,3,2) is subpolynomial since it is equivalent to determining the multicolor Ramsey number of the triangle. For p = 4, Mubayi [16] showed that f(n,4,3) ≤ 2c

√log n and Eichhorn and Mubayi [4] showed that f(n,5,4) ≤ 2c

![image 4](<2014-conlon-grid-ramsey-problem-related_images/imageFile4.png>)

√logn. Recently, Conlon, Fox, Lee and Sudakov [3] resolved the question of Erd˝os and Gy´arf´as, proving that f(n,p,p− 1) is subpolynomial for all p ≥ 3. Nevertheless, the function f(n,p,p−1) is still far from being well understood, even for

![image 5](<2014-conlon-grid-ramsey-problem-related_images/imageFile5.png>)

- p = 4, where the best known lower bound is f(n,4,3) = Ω(log n) (see [9, 15]). In this paper, we consider extensions of these problems to hypergraphs. The main motivation for


studying this problem comes from an equivalent formulation of the grid Ramsey problem (actually, this is Shelah’s original formulation). Let K(3)(n,n) be the 3-uniform hypergraph with vertex set

- A ∪ B, where |A| = |B| = n, and edge set consisting of all those triples which intersect both A and
- B. We claim that g(n) is within a factor of two of the minimum integer r for which there exists an


r-coloring of the edges of K(3)(n,n) such that any copy of K4(3) has at least 3 colors on its edges. To see the relation, we abuse notation and regard both A and B as copies of the set [n]. For i ∈ A

and j,j′ ∈ B, map the edge {(i,j),(i,j′)} of Γn,n to the edge (i,j,j′) of K(3)(n,n) and, for i,i′ ∈ A and j ∈ B, map the edge {(i,j),(i′,j)} of Γn,n to the edge (i,i′,j) of K(3)(n,n). Note that this deﬁnes a bijection between the edges of Γn,n and the edges of K(3)(n,n), where the rectangles of Γn,n are in one-to-one correspondence with the copies of K4(3) of K(3)(n,n) intersecting both sides in two vertices. Hence, given a desired coloring of K(3)(n,n), we can ﬁnd a coloring of Γn,n where all rectangles receive at least three colors (and are thus alternating-free), showing that g(n) ≤ r. Similarly, given an alternating-free coloring of Γn,n, we may double the number of colors to ensure that the set of colors used for row edges and those used for column edges are disjoint. This turns an alternating-free coloring of Γn,n into a coloring where each K4(3) receives at least three colors. Hence,

- as above, we see that r ≤ 2g(n).


Therefore, essentially the only diﬀerence between g(n) and f3(2n,4,3) is that the base hypergraph

for g(n) is K(3)(n,n) rather than K2(3)n . This observation allows us to establish a close connection between the quantitative estimates for f3(n,4,3) and g(n), as exhibited by the following pair of inequalities (that we will prove in Proposition 4.1):

g(n) ≤ f3(2n,4,3) ≤ 2⌈log n⌉2g(n). (1)

This implies upper and lower bounds for f3(n,4,3) and F3(r,4,3) analogous to those we have established for g(n) and G(r). More generally, we have the following recursive upper bound for Fk(r,p,q).

- Theorem 1.4. For positive integers r,k, p and q, all greater than 1 and satisfying r ≥ k, p ≥ k + 1 and 2 ≤ q ≤ k p ,

Fk (r,p,q) ≤ r(Fk−1k(r,p−1−1,q)). The above is true even for q > k p−−11 , where we trivially have Fk−1(r,p − 1,q) = p − 1.

By repeatedly applying Theorem 1.4, we see that for each ﬁxed i with 0 ≤ i ≤ k and large enough p,

Fk r,p,

p − i k − i

+ 1 ≤ rr.

..

r

ck,p

,

where the number of r’s in the tower is i. For 0 < i < k, it would be interesting to establish a lower bound on Fk(r,p, k p−−ii ) that is signiﬁcantly larger than this upper bound on Fk(r,p, k p−−ii +1). This would establish an interesting phenomenon of ‘sudden jumps’ in the asymptotics of Fk(r,p,q) at the values q = k p−−ii . We believe that these jumps indeed occur.

Let us examine some small cases of this problem. For graphs, as mentioned above, F(r,p,p) is

polynomial while F(r,p,p − 1) is superpolynomial. For 3-uniform hypergraphs, F3(r,p, p−21 + 1) is polynomial in terms of r. Hence, the ﬁrst interesting case is to decide whether the function

- F3(r,p, p−21 ) is also polynomial. The fact that F3(r,4,3) is superpolynomial follows from Theo-


rem 1.2 and (1), giving some evidence towards the conjecture that F3(r,p, p−21 ) is superpolynomial. We provide further evidence by establishing the next case for 3-uniform hypergraphs.

- Theorem 1.5. There exists a positive constant c such that F3(r,5,6) ≥ 2clog2 r for all positive integers r.


## 1.3 A chromatic number version of the Erdo˝s–Gy´arf´as problem

- A graph with chromatic number equal to p we call p-chromatic. In the process of studying G(r) (and proving Theorem 1.2), we encountered the following variant of the functions discussed in the previous subsection, where Kp is replaced by p-chromatic subgraphs. Deﬁnition. Let p and q be positive integers satisfying p ≥ 3 and 2 ≤ q ≤ p2 .


- (i) For each positive integer r, deﬁne Fχ(r,p,q) as the minimum integer n for which every edge coloring of Kn with r colors contains a p-chromatic subgraph receiving at most q − 1 distinct colors on its edges.
- (ii) For each positive integer n, deﬁne fχ(n,p,q) as the minimum integer r for which there exists an edge coloring of Kn with r colors such that every p-chromatic subgraph receives at least q distinct colors on its edges.


Call an edge coloring of Kn a chromatic-(p,q)-coloring if every p-chromatic subgraph receives

- at least q distinct colors on its edges. As before, the deﬁnitions of Fχ(r,p,q) and fχ(n,p,q) can be restated in terms of chromatic-(p,q)-colorings. Also, an edge coloring of Kn is a chromatic-(p,q)coloring if and only if the union of every q − 1 color classes induces a graph of chromatic number at most p−1. In some sense, this looks like the most natural interpretation for the functions Fχ(r,p,q)


- and fχ(n,p,q). If we choose to use this deﬁnition, then it is more natural to shift the numbers p and


- q by 1. However, we use the deﬁnition above in order to make the connection between Fχ(r,p,q) and F(r,p,q) more transparent.


From the deﬁnition, we can immediately deduce some simple facts such as

Fχ(r,p,q) ≤ F(r,p,q), fχ(n,p,q) ≥ f(n,p,q) (2) for all values of r,p,q,n and

fχ n,p,

p 2

= f n,p,

p 2

=

n 2

for all n ≥ p ≥ 4.

Let n = Fχ(r,p,q) − 1 and consider a chromatic-(p,q)-coloring of Kn that uses r colors in total. Cover the set of r colors by ⌈r/(q − 1)⌉ subsets of size at most q − 1. The chromatic number of the graph induced by each subset is at most p − 1 and thus, by the product formula for chromatic number, we see that

Fχ(r,p,q) − 1 ≤ (p − 1)⌈r/(q−1)⌉. This gives a general exponential upper bound.

On the other hand, when d is a positive integer, p = 2d + 1 and q = d + 1, a coloring of the complete graph which we will describe in Section 2 implies that

Fχ(r,2d + 1,d + 1) ≥ 2r + 1. Whenever r is divisible by d, we see that the two bounds match to give

Fχ(r,2d + 1,d + 1) = 2r + 1. (3) Let us examine the value of Fχ(r,p,q) for some small values of p and q. By using the observations

(2) and (3), we have

- Fχ(r,3,2) = 2r + 1, Fχ(r,3,3) ≤ F(r,3,3) ≤ r + 2

- for p = 3 and

Fχ(r,4,2) ≥ 2r + 1, Fχ(r,4,4) ≤ F(r,4,4) ≤ r2 + 2

- for p = 4 and r ≥ 2. The bound on F(r,4,4) follows since every edge coloring of the complete graph on r2 + 2 vertices with r colors contains a vertex v and a set X of size at least r + 1 such that all the edges connecting v to X have the same color, say red. If an edge e with vertices in X is red, we




get a K4 using at most three colors by taking v, the vertices of e, and any other vertex in X. So we may suppose at most r − 1 colors are used on the edges with both vertices in X. In this case,

- as |X| ≥ F(r − 1,3,3), we can ﬁnd three vertices in X with at most two colors used on the edges connecting them. Adding v to this set gives a set of four vertices with at most three colors used on the edges connecting them.


We show that the asymptotic behavior of Fχ(r,4,3) is diﬀerent from both Fχ(r,4,2) and Fχ(r,4,4).

- Theorem 1.6. There exist positive constants C and r0 such that for all r ≥ r0,

2log2 r/36 ≤ Fχ(r,4,3) ≤ C · 2130

√rlogr.

![image 6](<2014-conlon-grid-ramsey-problem-related_images/imageFile6.png>)

Despite being interesting in its own right, our principal motivation for considering chromatic(p,q)-colorings was to establish the following theorem, which is an important ingredient in the proof of Theorem 1.2.

- Theorem 1.7. For every ﬁxed positive integer n, there exists an edge coloring of the complete graph


√logn colors with the following property: for every subset X of colors with |X| ≥ 2, the subgraph induced by the edges colored with a color from X has chromatic number at most 23

![image 7](<2014-conlon-grid-ramsey-problem-related_images/imageFile7.png>)

Kn with 26

√

![image 8](<2014-conlon-grid-ramsey-problem-related_images/imageFile8.png>)

|X|log|X|. This theorem has the following immediate corollary.

Corollary 1.8. For all positive integers n,r and s ≥ 2,

√logn and Fχ(r,23

√slogs + 1,s + 1) ≥ 2log2 r/36.

√slogs + 1,s + 1) ≤ 26

![image 9](<2014-conlon-grid-ramsey-problem-related_images/imageFile9.png>)

![image 10](<2014-conlon-grid-ramsey-problem-related_images/imageFile10.png>)

![image 11](<2014-conlon-grid-ramsey-problem-related_images/imageFile11.png>)

fχ(n,23

Our paper is organized as follows. In Section 2, we review two coloring functions that will be used throughout the paper. In Section 3, we prove Theorems 1.2 and 1.3. In Section 4, we prove Theorems 1.4 and 1.5. In Section 5, we prove Theorems 1.6 and 1.7. We conclude with some further remarks and open problems in Section 6.

Notation. We use log for the base 2 logarithm and ln for the natural logarithm. For the sake of clarity of presentation, we systematically omit ﬂoor and ceiling signs whenever they are not essential. We also do not make any serious attempt to optimize absolute constants in our statements and proofs.

The following standard asymptotic notation will be used throughout. For two functions f(n)

- and g(n), we write f(n) = o(g(n)) if limn→∞ f(n)/g(n) = 0 and f(n) = O(g(n)) or g(n) = Ω(f(n)) if there exists a constant M such that |f(n)| ≤ M|g(n)| for all suﬃciently large n. We also write


- f(n) = Θ(g(n)) if both f(n) = O(g(n)) and f(n) = Ω(g(n)) are satisﬁed.


# 2 Preliminaries

We begin by deﬁning two edge colorings of the complete graph Kn, one a (3,2)-coloring and the other a (4,3)-coloring. These will be used throughout the paper.

We denote the (3,2)-coloring by cB, where ‘B’ stands for ‘binary’. To deﬁne this coloring, we let t be the smallest integer such that n ≤ 2t. We consider the vertex set [n] as a subset of {0,1}t by identifying x with (x1,... ,xt), where ti=1 xi2i−1 is the binary expansion of x − 1. Then, for two vertices x = (x1,... ,xt) and y = (y1,... ,yt), cB(x,y) is the minimum i for which xi = yi. This coloring uses at most ⌈log n⌉ colors and is a (3,2)-coloring since three vertices cannot all diﬀer in the i-th coordinate. In fact, it is a chromatic-(2d + 1,d + 1)-coloring for all integers d ≥ 1, since it gives an edge partition E = E1 ∪ ··· ∪ Et of Kn for t = ⌈log n⌉ such that, for all J ⊂ [t], the graph consisting of the edges j∈J Ej has chromatic number at most 2|J|.

The (4,3)-coloring, which is a variant of Mubayi’s coloring [16], will be denoted by cM. To deﬁne this coloring, we let t be the smallest integer such that n ≤ 2t2 and m = 2t. We consider the vertex

set [n] as a subset of [m]t by identifying x with (x1,... ,xt), this time by examining the base m expansion of x − 1. For two vertices x = (x1,... ,xt) and y = (y1,... ,yt), let

cM(x,y) = {xi,yi},a1,... ,at ,

where i is the minimum index in which x and y diﬀer and aj = 0 or 1 depending on whether xj = yj or not (note that the coloring function cM is symmetric in its two variables).

The coloring cM is a (3,2)-coloring since it partitions the edge set of Kn into bipartite graphs and a simple case analysis similar to that given in [16] shows that it is a (4,3)-coloring (the proof of Theorem 1.6 given in Section 5 shows that cM is even a chromatic-(4,3)-coloring). Since 2(t−1)2 < n, the total number of colors used is at most

√logn. Hence, cM uses at most r = 26

√logn) ≤ 26

![image 12](<2014-conlon-grid-ramsey-problem-related_images/imageFile12.png>)

![image 13](<2014-conlon-grid-ramsey-problem-related_images/imageFile13.png>)

m2 · 2t = 23t < 23(1+

√logn colors to color the edge set of the complete graph on n = 2log2 r/36 vertices.

![image 14](<2014-conlon-grid-ramsey-problem-related_images/imageFile14.png>)

# 3 The grid Ramsey problem

In order to improve the lower bound on G(r), we need to ﬁnd an edge coloring of the grid graph which is alternating-free. The following lemma is the key idea behind our argument. For two edge-coloring functions c1 and c2 of the complete graph Kn, let G(c1,c2) be the subgraph of Kn where e is an edge if and only if c1(e) = c2(e).

- Lemma 3.1. Let m,n and r be positive integers. There exists an alternating-rectangle-free edge coloring of Γm,n with r colors if and only if there are edge colorings c1,... ,cm of the complete graph Kn with r colors satisfying


χ(G(ci,cj)) ≤ r for all pairs of indices i,j.

Proof. We ﬁrst prove the ‘if’ statement. Consider the grid graph Γm,n. For each i, color the edges of the i-th row using the edge coloring ci. Then, for each distinct pair of indices i and i′, construct auxiliary graphs Hi,i′ whose vertex set is the set of edges that connect the i-th row with the i′-th row (that is, edges of the form {(i,j),(i′,j)}) and where two vertices {(i,j),(i′,j)} and {(i,j′),(i′,j′)} are adjacent if and only if the two row edges that connect these two column edges have the same color.

The fact that χ(G(ci,ci′)) ≤ r implies that there exists a vertex coloring of Hi,i′ with r colors. Color the corresponding edges {(i,j),(i′,j)} according to this vertex coloring. Under this coloring, we see that whenever a pair of edges of the form {(i,j),(i,j′)} and {(i′,j),(i′,j′)} have the same color, the colors of the edges {(i,j),(i′,j)} and {(i,j′),(i′,j′)} are distinct. This gives a coloring of the column edges. Hence, we found the required alternating-rectangle-free edge coloring of Γm,n with r colors.

For the ‘only if’ statement, given an alternating-rectangle-free edge coloring of Γm,n with r colors, deﬁne ci as the edge-coloring function of the i-th row of Γm,n, for each i ∈ [m]. One can easily reverse the process above to show that the colorings c1,... ,cm satisfy the condition. We omit the details.

To ﬁnd an alternating-rectangle-free edge coloring of Γm,n, we will ﬁnd edge colorings of the rows which satisfy the condition of Lemma 3.1. Suppose that E(Kn) = E1 ∪ ··· ∪ Et is a partition of the edge set of Kn. For an index subset I ⊂ [t], we let GI be the subgraph of Kn whose edge set is given by i∈I Ei.

- Lemma 3.2. Let m,n,r and t be positive integers. Suppose that an edge partition E(Kn) = E1∪···∪ Et of Kn is given. Let I be a random subset of [t] where each element in I is chosen independently with probability 1/r and suppose that


- 1

![image 15](<2014-conlon-grid-ramsey-problem-related_images/imageFile15.png>)

- 2m


. Then g(m,n) ≤ r and G(r) ≥ min{m,n} + 1.

P[χ(GI) ≥ r + 1] ≤

Proof. For each i ∈ [2m], choose a vector vi ∈ [r]t independently and uniformly at random. Let ci be an edge coloring of Kn with r colors where for each t′ ∈ [t], we color all the edges in Et′ using the value of the t′-th coordinate of vi. Color the i-th row of Γ2m,n (which is a copy of Kn) using ci.

For a pair of distinct indices i,j ∈ [2m], let I(i,j) be the subset of indices t′ ∈ [t] for which vi and vj have the same value on their t′-th coordinates (thus implying that ci and cj use the same color on Et′). Then I(i,j) has the same distribution as a random subset of [t] obtained by taking each element independently with probability 1/r. Moreover,

G(ci,cj) = GI(i,j). Hence,

- 1

![image 16](<2014-conlon-grid-ramsey-problem-related_images/imageFile16.png>)

- 2m


.

P[χ(G(ci,cj)) ≥ r + 1] = P[χ(GI(i,j)) ≥ r + 1] ≤

Therefore, the expected number of pairs i,j with i < j having χ(GI(i,j)) ≥ r + 1 is at most 2m

- 2

- 1

![image 17](<2014-conlon-grid-ramsey-problem-related_images/imageFile17.png>)

- 2m ≤ m. Hence, there exists a choice of coloring functions ci for which this number is at most


- m. If this event happens, then we can remove one row from each pair i,j having χ(GI(i,j)) ≥ r + 1 to obtain a set R ⊂ [2m] of size at least m which has the property that χ(GI(i,j)) ≤ r for all i,j ∈ R. By considering the subgraph of Γ2m,n induced on R × [n] and using Lemma 3.1, we obtain an alternating-rectangle-free edge coloring of Γm,n with r colors. The result follows.


We prove Theorems 1.2 and 1.3 in the next two subsections. We begin with Theorem 1.3, which establishes upper bounds for g(m,n) in various oﬀ-diagonal regimes. As noted in the introduction, parts (i) and (ii) already yield weak versions of Theorem 1.2. In particular, part (i) implies that G(r) is superpolynomial in r, while part (ii) yields the bound G(r) > 2clog2 r. We recall the stronger oﬀ-diagonal statements below.

- 3.1 Proof of Theorem 1.3


Parts (i) and (ii) : For all C > e2, ε > 0 and large enough r, g(rlogC/2,rr/2C) ≤ r and

- g(2εlog2 r,2r1−ε) ≤ r.


Let n = 2t for some t to be chosen later. The edge coloring cB from Section 2 gives an edge partition E = E1 ∪ ··· ∪ Et of Kn for t = log n such that, for all J ⊂ [t],

χ(GJ) = 2|J|.

Hence, if we let I be a random subset of [t] obtained by choosing each element independently with probability 1/r, then

P[χ(GI) ≥ r + 1] = P |I| ≥ log(r + 1) ≤

t log(r + 1)

1 rlog(r+1) ≤

![image 18](<2014-conlon-grid-ramsey-problem-related_images/imageFile18.png>)

et r log(r + 1)

![image 19](<2014-conlon-grid-ramsey-problem-related_images/imageFile19.png>)

log(r+1)

. (4)

- For part (i), let C be a given constant and take t = r log r/2C. Then the right-hand side of (4) is at most (r + 1)−log(C/e). In Lemma 3.2, we can take m = 12(r + 1)log(C/e) ≥ rlogC/2 and

![image 20](<2014-conlon-grid-ramsey-problem-related_images/imageFile20.png>)

- n = 2t = rr/2C to get g(rlogC/2,rr/2C) ≤ r.


- For part (ii), let ε be a given constant and take t = r1−ε. For large enough r, the right-hand


side of (4) is at most 12r−εlogr. Hence, by applying Lemma 3.2 with m = rεlogr = 2εlog2 r and n = 2t = 2r1−ε, we see that

![image 21](<2014-conlon-grid-ramsey-problem-related_images/imageFile21.png>)

g(2εlog2 r,2r1−ε) ≤ r. Part (iii) : There exists a positive constant c such that g(cr2,rr2/2/er2) ≤ r for large enough r.

Let c = e−3. Let n = cr2 and partition the edge set of Kn into t = n2 sets E1,... ,Et, each of size exactly one. As before, let I be a random subset of [t] obtained by choosing each element independently with probability 1/r. In this case, we get GI = G(n, 1r) (where G(n,p) is the binomial random graph). Therefore,

![image 22](<2014-conlon-grid-ramsey-problem-related_images/imageFile22.png>)

P[χ(GI) ≥ r + 1] = P[χ(G(cr2,1/r)) ≥ r + 1].

The event χ G(cr2, 1r) ≥ r +1 is contained in the event that G(cr2, 1r) contains a subgraph of order

![image 23](<2014-conlon-grid-ramsey-problem-related_images/imageFile23.png>)

![image 24](<2014-conlon-grid-ramsey-problem-related_images/imageFile24.png>)

- s ≥ r + 1 of minimum degree at least r. The latter event has probability at most


r s/2

cr2

cr2

2 es r

rs/2

ecr2 s

s2/2 rs/2

cr2 s

r 1 r

1 r

≤

. (5)

![image 25](<2014-conlon-grid-ramsey-problem-related_images/imageFile25.png>)

![image 26](<2014-conlon-grid-ramsey-problem-related_images/imageFile26.png>)

![image 27](<2014-conlon-grid-ramsey-problem-related_images/imageFile27.png>)

![image 28](<2014-conlon-grid-ramsey-problem-related_images/imageFile28.png>)

s=r+1

s=r+1

For s = r, if r is large enough, then the summand is

(ecr)2er

1 r

![image 29](<2014-conlon-grid-ramsey-problem-related_images/imageFile29.png>)

r r/2

er2 rr2/2

.

≤

![image 30](<2014-conlon-grid-ramsey-problem-related_images/imageFile30.png>)

We next show that the summands are each at most a quarter of the previous summand. As the series starts at s = r + 1 and ends at s = cr2, the series is then at most half the summand for s = r. The ratio of the summand for s + 1 to the summand for s, where r + 1 ≤ s + 1 ≤ cr2, is

r 1/2

2 e(s + 1) r

s(r−2)/2 ecr2 s + 1

r 1 r

s + 1 s

![image 31](<2014-conlon-grid-ramsey-problem-related_images/imageFile31.png>)

![image 32](<2014-conlon-grid-ramsey-problem-related_images/imageFile32.png>)

![image 33](<2014-conlon-grid-ramsey-problem-related_images/imageFile33.png>)

![image 34](<2014-conlon-grid-ramsey-problem-related_images/imageFile34.png>)

which is at most

e(r−2)/2

er+2c2(s + 1)r−2 r2r−4

![image 35](<2014-conlon-grid-ramsey-problem-related_images/imageFile35.png>)

1/2

1 4

≤ e(r−2)/2(er+2cr)1/2 = e−r/2 <

,

![image 36](<2014-conlon-grid-ramsey-problem-related_images/imageFile36.png>)

for r suﬃciently large. Hence, the right-hand side of (5) is at most er2r−r2/2/2 and

er2 2rr2/2

.

P[χ(GI) ≥ r + 1] ≤

![image 37](<2014-conlon-grid-ramsey-problem-related_images/imageFile37.png>)

By Lemma 3.2, we conclude that g(cr2,rr2/2/er2) ≤ r.

## 3.2 Proof of Theorem 1.2

In the previous subsection we used quite simple edge partitions of the complete graph as an input to Lemma 3.2 to prove Theorem 1.3. These partitions were already good enough to give the superpolynomial bound G(r) > 2clog2 r. To further improve this bound and prove Theorem 1.2, we make use of a slightly more sophisticated edge partition guaranteed by the following theorem.

Theorem 3.3. There exists a positive real r0 such that the following holds for positive integers r and positive reals α ≤ 1 satisfying (log r)α ≥ r0. For n = 2(logr)2+α/200, there exists a partition E = E1 ∪ ··· ∪ E√r of the edge set of the complete graph Kn such that

![image 38](<2014-conlon-grid-ramsey-problem-related_images/imageFile38.png>)

√

![image 39](<2014-conlon-grid-ramsey-problem-related_images/imageFile39.png>)

χ(GI) ≤ 23(logr)α/2

|I|log 2|I|

for all I ⊂ [√r].

![image 40](<2014-conlon-grid-ramsey-problem-related_images/imageFile40.png>)

The proof of this theorem is based on Theorem 1.7, which is in turn based on considering the coloring cM, and will be given in Section 5.

Now suppose that a positive integer r is given and let α ≤ 1 be a real to be chosen later. Let E1 ∪ ··· ∪ E√r be the edge partition of Kn for n = 2(logr)2+α/200 given by Theorem 3.3. Let I be a random subset of [√r] chosen by taking each element independently with probability 1r. Then, by Theorem 3.3, we have

![image 41](<2014-conlon-grid-ramsey-problem-related_images/imageFile41.png>)

![image 42](<2014-conlon-grid-ramsey-problem-related_images/imageFile42.png>)

![image 43](<2014-conlon-grid-ramsey-problem-related_images/imageFile43.png>)

(log r)2−α log log r

χ(GI) ≥ r + 1 ⇒ |I| ≥ c

, for some positive constant c. Therefore,

![image 44](<2014-conlon-grid-ramsey-problem-related_images/imageFile44.png>)

(log r)2−α log log r ≤

P[χ(GI) ≥ r + 1] ≤ P |I| ≥ c

![image 45](<2014-conlon-grid-ramsey-problem-related_images/imageFile45.png>)

√r c(log r)2−α/log log r

![image 46](<2014-conlon-grid-ramsey-problem-related_images/imageFile46.png>)

1 r

![image 47](<2014-conlon-grid-ramsey-problem-related_images/imageFile47.png>)

c(log r)2−α/ log log r

≤ r−c′(logr)2−α/log logr

holds for some positive constant c′. By Lemma 3.2, for m = 2c′(logr)3−α/log logr−1, we have g(m,n) ≤

- r. We may choose α so that


√log logr). This gives G(r) ≥ 2Ω((logr)5/2/

m = n = eΩ((logr)5/2/

![image 48](<2014-conlon-grid-ramsey-problem-related_images/imageFile48.png>)

√log logr), as required.

![image 49](<2014-conlon-grid-ramsey-problem-related_images/imageFile49.png>)

# 4 The Erd˝os–Gy´arf´as problem

In the introduction, we discussed how the grid Ramsey problem is connected to a hypergraph version of the Erd˝os–Gy´rf´as problem. We now establish this correspondence more formally.

Proposition 4.1. For all positive integers n, we have

g(n) ≤ f3(2n,4,3) ≤ 2⌈log n⌉2g(n).

Proof. Since K(3)(n,n) is a subhypergraph of K2(3)n , a (4,3)-coloring of K2(3)n immediately gives a coloring of K(3)(n,n) such that every copy of K4(3) receives at least three colors. Hence, by the correspondence between coloring functions for K(3)(n,n) and coloring functions for Γn,n explained in the introduction, it follows that g(n) ≤ f3(2n,4,3).

We prove the other inequality by showing that for all m ≤ n,

f3(2m,4,3) ≤ f3(m,4,3) + 2⌈log m⌉g(m). (6) By repeatedly applying this recursive formula, we obtain the claimed inequality

f3(2n,4,3) ≤ 2⌈log n⌉2g(n). Thus it suﬃces to establish the recursive formula (6). We will do this by presenting a (4,3)-coloring of K2(3)m. Let A and B be two disjoint vertex subsets of K2(3)m, each of order m. Given a (4,3)coloring of Km(3) with f3(m,4,3) colors, color the hyperedges within A using this coloring and also the hyperedges within B using this coloring. Since we started with a (4,3)-coloring, every copy of K4(3) lying inside A or B contains at least 3 colors on its edges. This leaves us with the copies which intersect both A and B.

Let H be the bipartite hypergraph that consists of the edges which intersect both parts A and

- B. By deﬁnition, we have an alternating-free edge coloring of the grid graph Γm,m using g(m) colors. We may assume, by introducing at most g(m) new colors, that the set of colors used for the row edges and the column edges are disjoint. This gives an edge coloring of Γm,m, where each rectangle receives at least three colors. Let c1 be a coloring of H using at most 2g(m) colors, where for an edge {i,j,j′} ∈ H with i ∈ A,j,j′ ∈ B, we color it with the color of the edge {(i,j),(i,j′)} in Γm,m and for an edge {i,i′,j} ∈ H with i,i′ ∈ A,j ∈ B, we color it with the color of the edge {(i,j),(i′,j)} in Γm,m. Let c2 be a coloring of H constructed based on the coloring cB given in Section 2 as follows: for an edge {i,j,j′} ∈ H with i ∈ A,j,j′ ∈ B, let c2({i,j,j′}) = cB({j,j′}) and for an edge {i,i′,j} ∈ H with i,i′ ∈ A,j ∈ B, let c2({i,i′,j}) = cB({i,i′}). Now color the hypergraph H using the coloring function c1 × c2.


Consider a copy K of K4(3) which intersects both parts A and B. If |K ∩ A| = |K ∩ B| = 2, then assume that K = {i,i′,j,j′} for i,i′ ∈ A and j,j′ ∈ B. One can see that the set of colors used by c1 on K is identical to the set of colors used on the rectangle (i,j,i′,j′) in Γm,m considered above. Thus K receives at least three distinct colors. If |K ∩ A| = 1 and |K ∩ B| = 3, then the three hyperedges in K which intersect A use at least two colors from the coloring c2, while the unique hyperedge of K ∩B is colored with a diﬀerent color. Hence K contains at least three colors. Similarly, K contains

- at least three colors if |K ∩ A| = 3 and |K ∩ B| = 1.


Since c1 uses at most 2g(m) colors and c2 uses at most ⌈log m⌉ colors, we see that c1 ×c2 uses at most 2⌈log m⌉g(m) colors. Recall that we used at most f3(m,4,3) colors to color the edges inside A and B. Therefore, we have found a (4,3)-coloring of K2(3)m using at most

f3(m,4,3) + 2⌈log m⌉g(m) colors, thereby establishing (6).

## 4.1 A basic bound on Fk(r, p, q)

Here we prove Theorem 1.4 that provides a basic upper bound on the function Fk(r,p,q). Recall that we are given positive integers r,k,p, and q all greater than 1 and satisfying r ≥ k.

Let N = r(Fk−1k(r,p−1−1,q)) and suppose that we are given an edge coloring of KN(k) with r colors (denoted by c). Let [N] be the vertex set of KN(k). For each integer t in the range 1 ≤ t ≤ Fk−1(r,p−1,q), we will inductively ﬁnd a pair of disjoint subsets Xt and Yt of [N] with the following properties:

- 1. |Xt| = t and |Yt| ≥ min{N/r(k−t1),N − t},
- 2. for all x ∈ Xt and y ∈ Yt, x < y,
- 3. for all edges e ∈ Xtk∪Yt satisfying |e ∩ Xt| ≥ k − 1, the color of e is determined by the ﬁrst k − 1 elements of e (note that the ﬁrst k − 1 elements necessarily belong to Xt).


For the base cases t = 1,... ,k − 2, the pair of sets Xt = {1,2,... ,t} and Yt = [N] \ Xt trivially satisfy the given properties. Now suppose that for some t ≥ k − 2, we are given pairs Xt and Yt and wish to construct sets Xt+1 and Yt+1. Since t < Fk−1(r,p − 1,q), Property 1 implies that |Yt| ≥ 1 and in particular that Yt is nonempty. Let x be the minimum element of Yt and let Xt+1 = Xt ∪{x}.

For each element y ∈ Yt \ {x}, consider the vector of colors of length k |X−t2| whose coordinates are c(e′ ∪ {x,y}) for each e′ ∈ k X−t2 . By the pigeonhole principle, there are at least |Yt|−1

vertices which have the same vector. Let Yt+1 be these vertices. This choice immediately implies Properties

![image 50](<2014-conlon-grid-ramsey-problem-related_images/imageFile50.png>)

r(|kX−t2|)

- 2 and 3 above. To check Property 1, note that


N/r(k−t1) − t − 1 r(|kX−t2|)

|Yt| − 1 r(|kX−t2|) ≥

=

|Yt+1| ≥

![image 51](<2014-conlon-grid-ramsey-problem-related_images/imageFile51.png>)

![image 52](<2014-conlon-grid-ramsey-problem-related_images/imageFile52.png>)

t + 1 r(k−t2)

N r(kt+1−1) −

![image 53](<2014-conlon-grid-ramsey-problem-related_images/imageFile53.png>)

![image 54](<2014-conlon-grid-ramsey-problem-related_images/imageFile54.png>)

N r(kt+1−1) − 1,

>

![image 55](<2014-conlon-grid-ramsey-problem-related_images/imageFile55.png>)

where the ﬁnal inequality follows from t ≥ k − 2 and r ≥ k. Since N = r(Fk−1k(r,p−1−1,q)), Fk−1(r,p − 1,q) ≥ t + 1 and |Yt+1| is an integer, this implies that |Yt+1| ≥ N

.

![image 56](<2014-conlon-grid-ramsey-problem-related_images/imageFile56.png>)

r(kt+1−1)

Let T = Fk−1(r,p − 1,q) and note that |XT| = Fk−1(r,p − 1,q) and |YT| ≥ 1. Construct an auxiliary complete (k − 1)-uniform hypergraph over the vertex set XT and color each edge with the color guaranteed by Property 3 above. This gives an edge coloring of KT(k−1) with r colors and thus, by deﬁnition, we can ﬁnd a set A of p−1 vertices using fewer than q colors on its edges in the auxiliary (k − 1)-uniform hypergraph. It follows from Property 3 that for an arbitrary y ∈ YT, A ∪ {y} is a set of p vertices using fewer than q colors on its edges in the original k-uniform hypergraph.

## 4.2 A superpolynomial lower bound for F3(r, 5, 6)

√logn) colors. This shows that f3(n,5,6) = 2O(

In this subsection, we present a (5,6)-coloring of Kn(3) using 2O(

![image 57](<2014-conlon-grid-ramsey-problem-related_images/imageFile57.png>)

√logn) and F3(r,5,6) = 2Ω(log2 r).

![image 58](<2014-conlon-grid-ramsey-problem-related_images/imageFile58.png>)

The edge coloring is given as a product c = c1 ×c2 ×c3 ×c4 of four coloring functions c1,c2,c3,c4. The ﬁrst coloring c1 is a (4,3)-coloring of Kn(3) using f3(n,4,3) colors. Combining Proposition 4.1 and Theorem 1.2, we see that f3(n,4,3) = 2O((logn)2/5(log logn)1/5).

Let n = 2d and write the vertices of Kn as binary strings of length d. To deﬁne c2,c3 and c4, for three distinct vertices u,v,w, assume that the least coordinate in which not all vertices have the same bit is the i-th coordinate and let ui,vi,wi be the i-th coordinate of u,v,w, respectively. Without loss of generality, we may assume that ui = vi = wi, i.e. (ui,vi,wi) = (0,0,1) or (1,1,0). Deﬁne the second color c2 of the triple of vertices {u,v,w} as i. Thus c2 uses at most log n colors. Deﬁne the third color c3 as the value of wi, which is either 0 or 1. Deﬁne the fourth color c4 as

- cM(u,v), where cM is the graph coloring given in Section 2, which is both a (3,2) and (4,3)-coloring.


√logn) colors. The number of colors in the coloring c is

![image 59](<2014-conlon-grid-ramsey-problem-related_images/imageFile59.png>)

Recall that cM uses at most 2O(

√logn) = 2O(

√logn),

2O((logn)2/5(log logn)1/5) · log n · 2 · 2O(

![image 60](<2014-conlon-grid-ramsey-problem-related_images/imageFile60.png>)

![image 61](<2014-conlon-grid-ramsey-problem-related_images/imageFile61.png>)

as desired. Now we show that each set of 5 vertices receives at least 6 colors in the coloring c. Let i be the least coordinate such that the ﬁve vertices do not all agree.

- Case 1: One of the vertices (call it v1) has one bit at coordinate i, while the other four vertices (call

- them v2,v3,v4,v5) have the other bit. The 6 triples containing v1 are diﬀerent colors from the other


4 triples. Indeed, the triples containing v1 have c2 = i, while the other triples have c2 greater than i. Since cM is a (4,3)-coloring of graphs, c4 tells us that the triples containing v1 have to use at least 3 colors. On the other hand, by the coloring c1, the triples in the 4-set {v2,v3,v4,v5} have to use at least 3 colors. Hence, at least 6 colors have to be used on the set of ﬁve vertices.

- Case 2: Two of the vertices (call them v1,v2) have one bit at coordinate i, while the other three vertices (call them v3,v4,v5) have the other bit. Let V0 = {v1,v2} and V1 = {v3,v4,v5}. Let A be the set of colors of triples in {v1,...,v5}. We partition A into A0,A1,A2 as follows. For each j ∈ {0,1,2}, let Aj be the set consisting of the colors of triples containing exactly j vertices from V0. It follows from the colorings c2 and c3 that the three color sets A0,A1,A2 form a partition of A. Indeed, the color in A0 has second coordinate c2 greater than i, while the colors in A1 and A2 have second coordinate c2 = i. Furthermore, the colors in A1 have third coordinate c3 distinct from the third coordinate c3 of the colors in A2. Note also that |A0| = 1.


- Case 2a: |A2| = 3. Since the coloring cM is a (3,2)-coloring of graphs, c4 implies that the triples containing v1 whose

other two vertices are in V1 receive at least 2 colors. This implies that |A1| ≥ 2 and, therefore, the number of colors used is at least |A0| + |A1| + |A2| ≥ 6.

- Case 2b: |A2| = 2. Suppose without loss of generality that (v1,v2,v3) and (v1,v2,v4) have the same color, which is


diﬀerent from the color of (v1,v2,v5). As each K4(3) uses at least 3 colors in coloring c1, (v1,v3,v4) and (v2,v3,v4) have diﬀerent colors. Note that c4(v1,v3,v4) = c4(v2,v3,v4) = cM(v3,v4). Since cM is a (3,2)-coloring of graphs, at least one of cM(v3,v5) or cM(v4,v5) is diﬀerent from cM(v3,v4).

Suppose, without loss of generality, that cM(v3,v5) = cM(v3,v4). Since c is deﬁned as the product of c1,... ,c4, we see that the color of (v1,v3,v5) is diﬀerent from both that of (v1,v3,v4) and (v2,v3,v4). Thus |A1| ≥ 3. Then the number of colors used is at least |A0| + |A1| + |A2| ≥ 6.

- Case 2c: |A2| = 1. This implies that the three edges (v1,v2,vj) for j = 3,4,5 are of the same color. First note


that as in the previous case, there are at least two diﬀerent colors among cM(v3,v4), cM(v3,v5) and

- cM(v4,v5). Without loss of generality, suppose that cM(v3,v4) = cM(v3,v5). Since c is deﬁned as the product of c1,... ,c4, this implies that the set A′1 = {c(v1,v3,v4),c(v2,v3,v4)} is disjoint from the set A′′1 = {c(v1,v3,v5),c(v2,v3,v5)}. Now, by considering the coloring c1, since all three edges (v1,v2,vj) for j = 3,4,5 are of the same color, we see that |A′1| = 2 and |A′′1| = 2. Hence |A1| ≥ |A′1|+|A′′1| = 4. Then the number of colors used is at least |A0| + |A1| + |A2| ≥ 6.


# 5 A chromatic number version of the Erd˝os–Gy´arf´as problem

- 5.1 Bounds on Fχ(r, 4, 3) In this subsection, we prove Theorem 1.6. This asserts that


√rlogr.

2log2 r/36 ≤ Fχ(r,4,3) ≤ C · 2130

![image 62](<2014-conlon-grid-ramsey-problem-related_images/imageFile62.png>)

In order to obtain the upper bound, we use the concept of dense pairs. Suppose that a graph G is given. For positive reals ε and d, a pair of disjoint vertex subsets (V1,V2) is (ε,d)-dense if for every pair of subsets U1 ⊆ V1 and U2 ⊆ V2 satisfying |U1| ≥ ε|V1| and |U2| ≥ ε|V2|, we have

e(U1,U2) ≥ d|U1||U2|,

where e(U1,U2) is the number of edges of G with one endpoint in U1 and the other in U2. The following result is due to Peng, Ro¨dl and Rucin´ski [17]. Recall that the edge density of a graph G

with m edges and n vertices is m/ n2 . Theorem 5.1. For all positive reals d and ε, every graph on n vertices of edge density at least d contains an (ε,d/2)-dense pair (V1,V2) for which

1 8

nd12/ε. The original theorem of Peng, Ro¨dl and Rucin´ski takes a bipartite graph with n vertices in each

|V1| = |V2| ≥

![image 63](<2014-conlon-grid-ramsey-problem-related_images/imageFile63.png>)

part and dn2 edges as input and outputs an (ε,d/2)-dense pair with parts of size at least 12nd12/ε. The theorem as stated above is an immediate corollary since every n-vertex graph of density d contains

![image 64](<2014-conlon-grid-ramsey-problem-related_images/imageFile64.png>)

a bipartite subgraph with m = ⌊n2⌋ ≥ n4 vertices in each part and at least dm2 edges.

![image 65](<2014-conlon-grid-ramsey-problem-related_images/imageFile65.png>)

![image 66](<2014-conlon-grid-ramsey-problem-related_images/imageFile66.png>)

Proof of upper bound in Theorem 1.6. Let n = Fχ(r,4,3) − 1 and suppose that a chromatic(4,3)-coloring of Kn using r colors is given. Take a densest color, say red, and consider the graph G induced by the red edges. This graph has density at least 1r. By applying Theorem 5.1 with ε = lnrr 1/2, we obtain an (ε, 21r)-dense pair (V1,V2) in G such that

![image 67](<2014-conlon-grid-ramsey-problem-related_images/imageFile67.png>)

![image 68](<2014-conlon-grid-ramsey-problem-related_images/imageFile68.png>)

![image 69](<2014-conlon-grid-ramsey-problem-related_images/imageFile69.png>)

12/ε

√rlnr.

1 8

1 r

![image 70](<2014-conlon-grid-ramsey-problem-related_images/imageFile70.png>)

≥ ne−13

|V1| = |V2| ≥

n

![image 71](<2014-conlon-grid-ramsey-problem-related_images/imageFile71.png>)

![image 72](<2014-conlon-grid-ramsey-problem-related_images/imageFile72.png>)

For a color c which is not red, let G+c be the graph obtained by adding all edges of color c to the graph G. Since the given coloring is a chromatic-(4,3)-coloring, we see that G+c is 3-colorable for all c. Consider an arbitrary proper 3-coloring of G+c. If there exists a color class in this proper coloring which intersects both V1 and V2 in at least ε|V1| vertices, then, since (V1,V2) is an (ε, 21r)-dense pair, there exists an edge between the two intersections, thereby contradicting the fact that the 3-coloring is proper.

![image 73](<2014-conlon-grid-ramsey-problem-related_images/imageFile73.png>)

Hence, G+c has an independent set Ic of size at least (1 − 2ε)|V1| in either V1 or V2. For i = 1,2, deﬁne Ci to be the set of colors c ∈ [r] for which this independent set Ic is in Vi. Since |C1| + |C2| ≥ r − 1, we may assume, without loss of generality, that |C1| ≥ r−21.

![image 74](<2014-conlon-grid-ramsey-problem-related_images/imageFile74.png>)

For each v ∈ V1, let d(v) be the number of colors c ∈ C1 for which v ∈ Ic. Note that

|Ic| ≥ |C1| · (1 − 2ε)|V1|. (7)

d(v) =

c∈C1

v∈V1

For each X ⊂ C1 of size 4r, let IX = c∈X Ic. We have

![image 75](<2014-conlon-grid-ramsey-problem-related_images/imageFile75.png>)

d(v) r/4 ≥ |V1| ·

|C1| · (1 − 2ε) r/4

|IX| =

,

v∈V1

X⊂C1 |X|=r/4

where the inequality follows from (7) and convexity. Since |C1| ≥ r−21, we have

![image 76](<2014-conlon-grid-ramsey-problem-related_images/imageFile76.png>)

|C1| r/4

|IX| ≥ (1 − 8ε)r/4|V1| ·

.

X⊂C1 |X|=r/4

Thus we can ﬁnd a set X ⊂ C1 for which |IX| ≥ (1 − 8ε)r/4|V1|. By deﬁnition, the set IX does not contain any color from X and hence the original coloring induces a chromatic-(4,3)-coloring of a complete graph on |IX| vertices using at most 3r/4 colors. This gives

- 3r

![image 77](<2014-conlon-grid-ramsey-problem-related_images/imageFile77.png>)

- 4


,4,3 − 1 ≥ |IX| ≥ (1 − 8ε)r/4|V1|.

Fχ

For ε ≤ 1/16, the inequality 1 − 8ε ≥ e−16ε holds. Hence, for large enough r, the right-hand side above is at least

√

√

√

√

![image 78](<2014-conlon-grid-ramsey-problem-related_images/imageFile78.png>)

![image 79](<2014-conlon-grid-ramsey-problem-related_images/imageFile79.png>)

![image 80](<2014-conlon-grid-ramsey-problem-related_images/imageFile80.png>)

![image 81](<2014-conlon-grid-ramsey-problem-related_images/imageFile81.png>)

e−4εr · ne−13

rlnr. We conclude that there exists r0 such that if r ≥ r0, then

rlnr = e−4

rlnr · ne−13

rlnr = (Fχ(r,4,3) − 1)e−17

√

- 3r

![image 82](<2014-conlon-grid-ramsey-problem-related_images/imageFile82.png>)

- 4


![image 83](<2014-conlon-grid-ramsey-problem-related_images/imageFile83.png>)

Fχ(r,4,3) ≤ e17

rlnrFχ

,4,3 .

√rlnr holds for all r. This clearly holds for the base cases r < r0, so suppose r ≥ r0. Using the above inequality and the induction hypothesis, we obtain

![image 84](<2014-conlon-grid-ramsey-problem-related_images/imageFile84.png>)

We now prove by induction that there is a constant C such that Fχ(r,4,3) ≤ Ce130

√rlnrFχ

![image 85](<2014-conlon-grid-ramsey-problem-related_images/imageFile85.png>)

Fχ(r,4,3) ≤ e17

√

√rlnrCe130

- 3r

![image 86](<2014-conlon-grid-ramsey-problem-related_images/imageFile86.png>)

- 4


![image 87](<2014-conlon-grid-ramsey-problem-related_images/imageFile87.png>)

,4,3 ≤ e17

√rlnr,

![image 88](<2014-conlon-grid-ramsey-problem-related_images/imageFile88.png>)

![image 89](<2014-conlon-grid-ramsey-problem-related_images/imageFile89.png>)

(3r/4) ln(3r/4) ≤ Ce130

which completes the proof.

We now turn to the proof of the lower bound. In order to establish the lower bound, we show that Mubayi’s coloring cM is in fact a chromatic-(4,3)-coloring. This then implies that Fχ(r,4,3) ≥ 2log2 r/36, as claimed. Recall that in the coloring cM, we view the vertex set of Kn as a subset of [m]t for some integers m and t and, for two vertices x,y ∈ [m]t of the form x = (x1,... ,xt) and y = (y1,... ,yt), we let

cM(x,y) = {xi,yi},a1,... ,at , where i is the minimum index for which xi = yi and aj = δ(xj,yj) is the Dirac delta function. Proof of lower bound in Theorem 1.6. Consider the coloring cM on the vertex set [m]t. Suppose that two colors c1 and c2 are given and let

c1 = {x1,y1},a1,1,... ,a1,t and c2 = {x2,y2},a2,1,... ,a2,t .

Suppose that a1,i1 is the ﬁrst non-zero a1,j term and a2,i2 is the ﬁrst non-zero a2,j term. In other words, for a pair of vertices which are colored by c1, the ﬁrst coordinate in which the pair diﬀer is the i1-th coordinate (and a similar claim holds for c2).

Let G be the graph induced by the edges which are colored by either c1 or c2. We will prove that χ(G) ≤ 3 by presenting a proper vertex coloring of G using three colors, red, blue and green.

- Case 1: i1 = i2 = i for some index i. First, color all the vertices whose i-th coordinate is equal to x1 in red. Second, color all the

vertices whose i-th coordinate is equal to x2 in blue (if x1 = x2, there are no vertices of color blue). Third, color all other vertices in green.

To show that this is a proper coloring, note that if the color between two vertices z,w ∈ [m]t is either c1 or c2, then the i-th coordinate of z and w must be diﬀerent. This shows that the set of red vertices and the set of blue vertices are both independent sets. It remains to show that the set of green vertices is an independent set. To see this, note that if the color between z and w is either c1 or c2, then the i-th coordinates zi and wi must satisfy

{zi,wi} = {x1,y1} or {x2,y2},

as this is the only way the ﬁrst coordinate of cM(z,w) can match that of c1 or c2. However, all vertices which have i-th coordinate x1 or x2 are excluded from the set of green vertices. This shows that our coloring is proper.

- Case 2: i1 = i2. Without loss of generality, we may assume that i1 < i2. We will ﬁnd a proper coloring by


considering only the i1-th and i2-th coordinates. For v ∈ [m]t of the form v = (v1,v2,... ,vt), let

 

 

- 0 if vi1 = x1
- 1 if vi1 = y1 ∗ otherwise


- 0 if vi2 = x2
- 1 if vi2 = y2 ∗ otherwise


πi1(v) =

and πi2(v) =

.





Consider the projection map

π : [m]t → {0,1,∗} × {0,1,∗}

deﬁned by π(v) = (πi1(v),πi2(v)) and let H = π(G) be the graph on {0,1,∗} × {0,1,∗} induced by the graph G and the map π. More precisely, a pair of vertices v,w ∈ {0,1,∗} × {0,1,∗} forms an edge if and only if there exists an edge of G between the two sets π−1(v) and π−1(w) (see Figure 1). Note that a proper coloring of H can be pulled back via π−1 to give a proper coloring of G. It therefore suﬃces to ﬁnd a proper 3-coloring of H.

(*,0) (*,1) (*,*)

- (0,0) (0,1) (0,*)
- (1,0) (1,1) (1,*)


Figure 1: Graph H = π(G) when a1,i2 = 1.

Consider two vertices z,w ∈ [m]t. If cM(z,w) = c2, then the ﬁrst coordinate in which z and w diﬀer is the i2-th coordinate. This implies that z and w have identical i1-th coordinate. Hence, the set of possible edges of the form {π(z),π(w)} is E2 = {{00,01},{10,11},{∗0, ∗1}}.

Now suppose that cM(z,w) = c1. Then the possible edges of the form {π(z),π(w)} diﬀer according to the value of a1,i2.

- Case 2a: a1,i2 = 0. In this case, the i2-th coordinate of z and w must be the same and thus the possible edges of the

form (π(z),π(w)) are E1 = {{00,10},{01,11},{0∗,1∗}}. One can easily check that the graph with edge set E1 ∪ E2 is bipartite.

- Case 2b: a1,i2 = 1. In this case, the i2-th coordinate of z and w must be diﬀerent and thus the possible edges of


the form (π(z),π(w)) are E1 = {{00,11},{00,1∗},{01, 10},{01,1∗},{0∗, 10}, {0∗,11},{0∗, 1∗}}. A 3-coloring of the graph with edge set E1 ∪ E2 is given by coloring the set of vertices {00,10,∗0} in red, {01,0∗} in blue and {11,1∗,∗1,∗∗} in green (see Figure 1).

- 5.2 An edge partition with slowly growing chromatic number In this section, we will prove Theorem 1.7 by showing that cM has the required property.


Theorem 1.7. The coloring cM has the following property: for every subset X of colors with |X| ≥ 2, the subgraph induced by the edges colored with a color from X has chromatic number at most 23

√

![image 90](<2014-conlon-grid-ramsey-problem-related_images/imageFile90.png>)

|X|log|X|.

Proof. Consider the coloring cM on the vertex set [m]t. For a set of colors X, let GX be the graph induced by the edges colored by a color from the set X. Recall that each color c under this coloring

is of the form

c = {vi,wi},a1,a2,... ,at .

Deﬁne ι(c) = i to be the minimum index i for which ai = 1. For this index i, deﬁne η1(c) = vi and η2(c) = wi, where we break symmetry by imposing vi < wi. Let aj(c) = aj for j = 1,... ,t.

Given a set of colors X, construct an auxiliary graph H over the vertex set X whose edges are deﬁned as follows. For two colors c1,c2 ∈ X, let i1 = ι(c1), i2 = ι(c2) and assume that i1 ≤ i2. Then c1 and c2 are adjacent if and only if ai2(c1) = 1 (it is well-deﬁned since if i1 = i2, then ai2(c1) = ai1(c2) = 1). Let I be the family of all independent sets in H. We make the following claim, whose proof will be given later.

Claim 5.2. The following holds:

- (i) For all I ∈ I, the graph GI is bipartite.
- (ii) χ(GX) ≤ |I|. Suppose that the claim is true. Based on this claim, we will prove by induction on |X| that


√

![image 91](<2014-conlon-grid-ramsey-problem-related_images/imageFile91.png>)

|X|log|X|. For |X| = 2, we proved in the previous subsection that cM is a chromatic(4,3)-coloring, that is, the union of any two color classes is 3-colorable. This clearly implies the required result in this case. Now suppose that the statement has been established for all sets of size less than |X|.

χ(GX) ≤ 23

![image 92](<2014-conlon-grid-ramsey-problem-related_images/imageFile92.png>)

Let α = log|X|X| | . If there exists an independent set I ∈ I of size at least α, then, by the fact that GX = GI ∪ GX\I and Claim 5.2 (i), we have

![image 93](<2014-conlon-grid-ramsey-problem-related_images/imageFile93.png>)

χ(GX) ≤ χ(GI) · χ(GX\I) ≤ 2χ(GX\I). If |X \ I| ≥ 2, then the right hand side is at most 2 · 23

√

√

![image 94](<2014-conlon-grid-ramsey-problem-related_images/imageFile94.png>)

![image 95](<2014-conlon-grid-ramsey-problem-related_images/imageFile95.png>)

|X\I|log|X\I| < 23

|X|log|X| (the inequality

comes from |I| ≥ α) by the inductive hypothesis, and if |X \ I| ≤ 1, then since χ(GX\I) ≤ 2, the right hand side is at most 4. Hence the claimed bound holds in both cases.

On the other hand, if the independence number is less than α, then, by Claim 5.2 (ii) and the fact that |X| ≥ 2, we have

√

√

α−1

|X| i ≤ |X|2

![image 96](<2014-conlon-grid-ramsey-problem-related_images/imageFile96.png>)

![image 97](<2014-conlon-grid-ramsey-problem-related_images/imageFile97.png>)

|X|/log|X| = 22

|X|log|X|.

χ(GX) ≤

i=0

This proves the theorem up to Claim 5.2, which we now consider.

Proof of Claim 5.2. (i) Suppose that I ∈ I is given. By deﬁnition, for each color c ∈ I, we have distinct values of ι(c). For each c ∈ I, consider the map πc : [m]t → {0,1}, where for x ∈ [m]t of the form x = (x1,x2,... ,xt), we deﬁne

πc(x) =

- 0 if xι(c) ≤ η1(c)
- 1 if xι(c) > η1(c).


Deﬁne the map π : [m]t → {0,1}I as

π(x) = (πc(x))c∈I.

Consider the graph π(GI) over the vertex set {0,1}I. Let c and c′ be two distinct colors in I. If ι(c′) < ι(c), then aι(c′)(c) = 0 since ι(c) is the minimum index i for which ai(c) = 1 and if ι(c′) > ι(c),

- then aι(c′)(c) = 0 since I is an independent set in the auxiliary graph H deﬁned above. Hence, if e = {y,z} is an edge of color c, then the two vectors y and z have identical ι(c′)-coordinate for all c′ = c, thus implying that π(y) and π(z) have identical c′-coordinate for all c′ = c. Further note that for x ∈ {0,1}I, we have πc(x) = 0 if the ι(c)-th coordinate of x is η1(c) and πc(x) = 1 if the ι(c)-th coordinate of x is η2(c). Since {yι(c),zι(c)} = {η1(c),η2(c)}, we see that πc(y) = πc(z).


Therefore, two vertices v,w ∈ {0,1}I can be adjacent in π(GI) if and only if v and w diﬀer in exactly one coordinate, implying that π(GI) is a subgraph of the hypercube, which is clearly bipartite. A bipartite coloring of this graph can be pulled back to give a bipartite coloring of GI. (ii) We prove this by induction on the size of the set X. The claim is trivially true for |X| = 0 and 1, since |I| = 1 and 2, respectively, and the graph GX has chromatic number 1 and 2, respectively.

Now suppose that we are given a set X and the family I of independent sets in H (as deﬁned above). Let c ∈ X be a color with maximum ι(c) and let i = ι(c). Let Ic be the family of independent sets containing c and Ic′ be the family of all other independent sets.

Let A be the subset of vertices of [m]t whose i-th coordinate is η1(c). For two vectors x,y ∈ A, we have ai(cM(x,y)) = 0, since both x and y have i-th coordinate η1(c). Hence, in the subgraph of GX induced on the set A, we only see colors c′ ∈ X which have ai(c′) = 0. Let Xc ⊆ X be the set of colors c′ such that ai(c′) = 0. The observation above implies that GX[A] is a subgraph of GXc. By the inductive hypothesis, χ(GXc) is at most the number of independent sets of H[Xc]. Moreover, by the deﬁnitions of Xc and Ic and the choice of c, the independent sets of H[Xc] are in one-to-one correspondence with the independent sets in Ic. Thus, we have

χ(GX[A]) ≤ χ(GXc) ≤ |Ic|.

Now consider the set B = [m]t \A. The subgraph of GX induced on B does not contain any edge of color c and therefore GX[B] is a subgraph of GX\{c}. By the inductive hypothesis, χ(GX\{c}) is at most the number of independent sets of H[X \{c}]. By deﬁnition, the independent sets of H[X \{c}] are in one-to-one correspondence with independent sets in Ic′. Therefore, we have

χ(GX[B]) ≤ χ(GX\{c}) ≤ |Ic′|. Hence,

χ(GX) ≤ χ(GX[A]) + χ(GX[B]) ≤ |Ic| + |Ic′| = |I|, and the claim follows.

Using Theorem 1.7, we can now prove Theorem 3.3, which we restate here for the reader’s convenience. Recall that for an edge partition E1 ∪ ... ∪ Et of the complete graph Kn and a set I ⊆ [t], we deﬁne GI as the subgraph of Kn with edge set i∈I Ei.

Theorem 3.3. There exists a positive real r0 such that the following holds for every positive integer r and positive real α ≤ 1 satisfying (log r)α ≥ r0. For n = 2(logr)2+α/200, there exists a partition E = E1 ∪ ··· ∪ E√r of the edge set of the complete graph Kn such that

![image 98](<2014-conlon-grid-ramsey-problem-related_images/imageFile98.png>)

√

![image 99](<2014-conlon-grid-ramsey-problem-related_images/imageFile99.png>)

χ(GI) ≤ 23(logr)α/2

|I|log 2|I|

for all I ⊂ [√r].

![image 100](<2014-conlon-grid-ramsey-problem-related_images/imageFile100.png>)

Proof. Let N = 2log2 r/200 and t = (log r)α (since (log r)α ≥ r0 and α ≤ 1, we can guarantee that N and t are large enough by asking that r0 be large enough). Color the edge set of the complete graph on the vertex set [N]t as follows. For two vectors v,w ∈ [N]t of the form v = (v1,... ,vt) and w = (w1,... ,wt), we let

c(v,w) = i,cM(vi,wi) , where i is the minimum index for which vi = wi. Since cM on KN uses at most 26

√r

√logN ≤

![image 101](<2014-conlon-grid-ramsey-problem-related_images/imageFile101.png>)

![image 102](<2014-conlon-grid-ramsey-problem-related_images/imageFile102.png>)

logr colors (see the discussion in Section 2), our coloring uses at most

![image 103](<2014-conlon-grid-ramsey-problem-related_images/imageFile103.png>)

√r log r ≤

√r

![image 104](<2014-conlon-grid-ramsey-problem-related_images/imageFile104.png>)

![image 105](<2014-conlon-grid-ramsey-problem-related_images/imageFile105.png>)

t ·

![image 106](<2014-conlon-grid-ramsey-problem-related_images/imageFile106.png>)

colors in total. Since n = Nt, this coloring gives an edge partition E = E1 ∪··· ∪Es of the complete graph on n vertices, for some integer s ≤

√r.

![image 107](<2014-conlon-grid-ramsey-problem-related_images/imageFile107.png>)

Now suppose that a set I ⊂ [s] is given. The set I can be partitioned into t sets I1 ∪ ··· ∪ It according to the value of the ﬁrst coordinate as follows: for each i ∈ [t], deﬁne Ii as the set of indices

- j ∈ I for which the color of the edges Ej has i as its ﬁrst coordinate. For each i, let πi : [N]t → [N] be the projection map to the i-th coordinate. Then the graph πi(GIi) becomes a subgraph of KN induced by the union of |Ii| colors of cM. Hence, by Theorem 1.7, we know that


√

![image 108](<2014-conlon-grid-ramsey-problem-related_images/imageFile108.png>)

|Ii| log 2|Ii|

χ(GIi) ≤ χ(πi(GIi)) ≤ 23

for each i ∈ [t], where we introduce the extra 2 in the logarithm to account for the possibility that |Ii| = 1. Therefore, we see that

√

![image 109](<2014-conlon-grid-ramsey-problem-related_images/imageFile109.png>)

|Ii|log 2|Ii|.

χ(GIi) ≤ 23 i∈[t]

χ(GI) ≤

i∈[t]

Since √xlog 2x is concave, Jensen’s inequality implies that the sum in the exponent satisﬁes

![image 110](<2014-conlon-grid-ramsey-problem-related_images/imageFile110.png>)

i∈[t]

|Ii|log 2|Ii| ≤ t (|I|/t)log(2|I|/t) ≤ t|I|log 2|I| = (log r)α/2 |I|log 2|I|.

![image 111](<2014-conlon-grid-ramsey-problem-related_images/imageFile111.png>)

![image 112](<2014-conlon-grid-ramsey-problem-related_images/imageFile112.png>)

![image 113](<2014-conlon-grid-ramsey-problem-related_images/imageFile113.png>)

![image 114](<2014-conlon-grid-ramsey-problem-related_images/imageFile114.png>)

This implies the required result.

# 6 Concluding Remarks

## 6.1 The grid Ramsey problem with asymmetric colorings

One may also consider an asymmetric version of the grid Ramsey problem, where we color the row edges using r colors but are allowed to use only two colors on the column edges. Let G(r,2) be the minimum n for which such a coloring is guaranteed to contain an alternating rectangle. One can easily see that

r ≤ G(r,2) ≤ r3 + 1.

The following construction improves the lower bound to G(r,2) ≥ 41r2. Let n = 14r2 and p be a prime satisfying r2 ≤ p ≤ r and n ≤ 2p (the existence of such a prime follows from Bertrand’s postulate). Consider the n × n grid. For each i ∈ [n], assign to the i-th row a sequence (ai,1,... ,ai,p) ∈ [r]p so that for all distinct i and i′ there exists at most one coordinate j ∈ [p] for which ai,j = ai′,j (the construction will be given below). Given these sequences, for each i ∈ [n] and distinct j,j′ ∈ [n], color the edge {(i,j),(i,j′)} as follows: examine the binary expansions of j and j′ to identify the ﬁrst bit t in which the two diﬀer and color the edge with color ai,t (this is possible since 2p ≥ n). For two distinct rows, suppose that the sequences corresponding to these rows coincide in the k-th coordinate. Then the intersection of the two rows is a subgraph of the graph connecting vertices whose k-th bit in the binary expansion is 0 to those whose k-th bit in the binary expansion is 1. Thus, the intersection of any two rows is a bipartite graph and therefore, by the same argument as in the proof of Lemma 3.1, we obtain G(r,2) ≥ n (note that we in fact obtain a coloring of the cr2 × 2c′r grid).

![image 115](<2014-conlon-grid-ramsey-problem-related_images/imageFile115.png>)

![image 116](<2014-conlon-grid-ramsey-problem-related_images/imageFile116.png>)

![image 117](<2014-conlon-grid-ramsey-problem-related_images/imageFile117.png>)

It suﬃces to construct a collection of sequences with the property claimed above. For a,b ∈ Zp, consider the following sequence with entries in Zp:

Ba,b = a,a + b,a + 2b,... ,a + (p − 1)b .

For two distinct pairs (a,b) and (a′,b′), the sequences Ba,b and Ba′,b′ can overlap in the i-th coordinate if and only if a + ib = a′ + ib′, which is equivalent to (b − b′)i = a′ − a. Since (a,b) = (a′,b′), we see that there exists at most one index i in the range 0 ≤ i ≤ p − 1 for which a + ib = a′ + ib′. Thus the sequences Ba,b have the claimed property. Note that the total number of sequences is at least

- p2 ≥ n. Moreover, since p ≤ r, by abusing notation, we may assume that the sequences are in fact in [r]p and, therefore, we can use them in the construction of our coloring.


The following question may be more approachable than the corresponding problem for G(r). Question 6.1. Can we improve the upper bound on G(r,2)?

- 6.2 The Erdo˝s–Gy´arf´as problem in hypergraphs As mentioned in the introduction, for each ﬁxed i with 0 ≤ i ≤ k and large enough p,


ck,p

r

..

p − i k − i

+ 1 ≤ rr.

,

Fk r,p,

where the number of r’s in the tower is i. It would be interesting to establish a lower bound on F(r,p, k p−−ii ) exhibiting a diﬀerent behavior.

Problem 6.2. Let p,k and i be positive integers with k ≥ 3 and 0 < i < k. Establish a lower bound on Fk(r,p, k p−−ii ) that is signiﬁcantly larger than the upper bound on Fk(r,p, k p−−ii + 1) given above.

We have principally considered the i = 1 case of this question. For example, the Erd˝os–Gy´rf´as problem on whether F(n,p,p − 1) is superpolynomial for all p ≥ 3 corresponds to the case where

- k = 2 and i = 1. Theorems 1.2 and 1.5 represent progress on the analogous problem with k = 3.


The next open case, showing that F3(r,6,10) is superpolynomial, appears diﬃcult.

For i ≥ 2, it seems likely that one would have to invoke a variant of the stepping-up technique of Erd˝os and Hajnal (see, for example, [11]). In particular, we would like to know the answer to the following question.

Question 6.3. Is F3(r,p,p − 2) larger than 2rc for any ﬁxed c?

For p = 4, a positive solution to this problem follows since we know that the Ramsey number of K4(3) is double exponential in the number of colors (see, for example, [2]). The general case appears

- to be much more diﬃcult.


Another case of particular importance is F2d−1(r,2d,d + 1), since it is this function (or rather a d-partite variant) which is used by Shelah in his proof of the Hales–Jewett theorem. If the growth rate of this function is a tower of bounded height for all d, then it would be possible to give a tower-type bound for Hales–Jewett numbers. However, we expect that this is not the case.

Problem 6.4. Show that for all s there exists d such that

2r

..

F2d−1 (r,2d,d + 1) ≥ 22.

, where the number of 2’s in the tower is at least s.

## 6.3 Studying the chromatic number version of the Erdo˝s–Gy´arf´as problem

Since we know that both F(r,p,p − 1) and Fχ(r,4,3) are superpolynomial in r, it is natural to ask the following question (see also [3]).

Question 6.5. Is Fχ(r,p,p − 1) superpolynomial in r?

By following a similar line of argument to the lower bound for Fχ(r,4,3), we can show that cM is also a chromatic-(5,4)-coloring. Therefore, Fχ(r,5,4) = 2Ω(log2 r), answering Question 6.5 for p = 5. Since the proof is based on rather tedious case analysis, we will post a supplementary note rather than including the details here. It would be interesting to determine whether the (p,p− 1)-colorings deﬁned in [3] are also chromatic-(p,p − 1)-colorings. If so, they would provide a positive answer to

- Question 6.5.

In Theorem 1.6, we showed that 2Ω(log2 r) ≤ Fχ(r,4,3) ≤ 2O(

√rlogr). It would be interesting to reduce the gap between the lower and upper bounds. Since Fχ(r,4,2) ≥ 2r + 1, we see that Fχ(r,4,2) is exponential in r, while Fχ(r,4,3) is subexponential in r. For p ≥ 5, the value of q for which the transition from exponential to subexponential happens is not known. However, recall that Fχ(r,2d + 1,d + 1) is exponential in r for all d ≥ 1. This followed from showing that in the edge coloring cB the union of every d color classes induces a graph of chromatic number 2d (see Section 2). The following question asks whether a similar edge coloring exists if we want the union of every d color classes to induce a graph of chromatic number at most 2d − 1.

![image 118](<2014-conlon-grid-ramsey-problem-related_images/imageFile118.png>)

- Question 6.6. Is Fχ(r,2d,d + 1) = 2o(r) for all d ≥ 2?


A positive answer to Question 6.6 would allow us to determine, for all p, the maximum value of

- q for which Fχ(r,p,q) is exponential in r. Indeed, for 2d−1 < p ≤ 2d, we have Fχ(r,p,d) ≥ Fχ(r,2d−1 + 1,d) = 2Ω(r),


while a positive answer to Question 6.6 would imply Fχ(r,p,d + 1) ≤ Fχ(r,2d,d + 1) = 2o(r).

Hence, given a positive answer to Question 6.6, the maximum value of q for which Fχ(r,p,q) is exponential in r would be q = ⌈log p⌉.

A key component in our proof of Theorem 1.2 was Theorem 1.7, which says that in the coloring cM, the chromatic number of the union of any s color classes is not too large. We suspect that our estimate on the chromatic number is rather weak. It would be interesting to improve it further. More generally, we have the following rather informal question, progress on which might allow us to improve the bounds in Theorem 1.2.

- Question 6.7. Given an edge partition of the complete graph Kn, how slowly can the chromatic number of the graph determined by the union of s color classes grow?


Finally, let F be a family of graphs and deﬁne F(r,q;F) to be the minimum integer n for which every edge coloring of Kn with r colors contains a subgraph F ∈ F that contains fewer than q colors. F(r,q;F) generalizes both F(r,p,q) and Fχ(r,p,q) since we may take F to be {Kp} for F(r,p,q) and the family of all p-chromatic graphs for Fχ(r,p,q). Our results suggest that F(r,q;F) is closely related to the chromatic number of the graphs in F. The case where F consists of a single complete bipartite graph was studied in [1].

Acknowledgement. We would like to thank the anonymous referee for several helpful comments.

# References

- [1] M. Axenovich, Z. Fu¨redi and D. Mubayi, On generalized Ramsey theory: the bipartite case, J. Combin. Theory Ser. B 79 (2000), 66–86.
- [2] M. Axenovich, A. Gy´arf´as, H. Liu and D. Mubayi, Multicolor Ramsey numbers for triple systems, Discrete Math. 322 (2014), 69–77.
- [3] D. Conlon, J. Fox, C. Lee and B. Sudakov, The Erd˝os–Gy´rf´as problem on generalized Ramsey numbers, to appear in Proc. London Math. Soc.
- [4] D. Eichhorn and D. Mubayi, Edge-coloring cliques with many colors on subcliques, Combinatorica 20 (2000), 441–444.
- [5] P. Erd˝os, Problems and results on ﬁnite and inﬁnite graphs, in Recent advances in graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974), 183–192, Academia, Prague, 1975.
- [6] P. Erd˝os, Solved and unsolved problems in combinatorics and combinatorial number theory, in Proceedings of the twelfth southeastern conference on combinatorics, graph theory and computing, Vol. I (Baton Rouge, La., 1981), Congr. Numer. 32 (1981), 49–62.
- [7] P. Erd˝os and A. Gy´arf´as, A variant of the classical Ramsey problem, Combinatorica 17 (1997), 459–467.
- [8] R. Faudree, A. Gy´arf´as and T. Szo˝nyi, Projective spaces and colorings of Km × Kn, in Sets, graphs and numbers (Budapest, 1991), 273–278, Colloq. Math. Soc. Ja´nos Bolyai, 60, NorthHolland, Amsterdam, 1992.


- [9] J. Fox and B. Sudakov, Ramsey-type problem for an almost monochromatic K4, SIAM J. Discrete Math. 23 (2008), 155–162.
- [10] W. T. Gowers, A new proof of Szemere´di’s theorem, Geom. Funct. Anal. 11 (2001), 465–588.
- [11] R. L. Graham, B. L. Rothschild and J. H. Spencer, Ramsey theory, second ed., WileyInterscience Series in Discrete Mathematics and Optimization, John Wiley & Sons Inc., New York, 1990.
- [12] A. Gy´arf´as, On a Ramsey type problem of Shelah, in Extremal problems for ﬁnite sets (Visegr´d, 1991), 283–287, Bolyai Soc. Math. Stud., 3, Ja´nos Bolyai Math. Soc., Budapest, 1994.
- [13] A. W. Hales and R. I. Jewett, Regularity and positional games, Trans. Amer. Math. Soc. 106

(1963), 222–229.

- [14] K. Heinrich, Coloring the edges of Km × Km, J. Graph Theory 14 (1990), 575–583.
- [15] A. Kostochka and D. Mubayi, When is an almost monochromatic K4 guaranteed?, Combin. Probab. Comput. 17 (2008), 823–830.
- [16] D. Mubayi, Edge-coloring cliques with three colors on all 4-cliques, Combinatorica 18 (1998), 293–296.
- [17] Y. Peng, V. Ro¨dl and A. Rucin´ski, Holes in graphs, Electron. J. Combin. 9 (2002), Research Paper 1, 18 pp.
- [18] S. Shelah, Primitive recursive bounds for van der Waerden numbers, J. Amer. Math. Soc. 1


(1989), 683–697.

