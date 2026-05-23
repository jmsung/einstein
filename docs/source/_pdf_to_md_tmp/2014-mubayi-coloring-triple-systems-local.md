arXiv:1410.3010v1[math.CO]11Oct2014

Coloring triple systems with local conditions

Dhruv Mubayi∗

October 24, 2018

Abstract

We produce an edge-coloring of the complete 3-uniform hypergraph on n vertices with eO(

![image 1](<2014-mubayi-coloring-triple-systems-local_images/imageFile1.png>)

√log logn) colors such that the edges spanned by every set of ﬁve vertices receive at least three distinct colors. This answers the ﬁrst open case of a question of Conlon-Fox-Lee-Sudakov [1] who asked whether such a coloring exists with (log n)o(1) colors.

# 1 Introduction

A k-uniform hypergraph H (k-graph for short) with vertex set V (H) is a collection of k-element subsets of V (H). Write Knk for the complete k-graph with vertex set of size n. A (p,q)-coloring of Knk is an edge-coloring of Knk that gives every copy of Kpk at least q colors. Let fk(n,p,q) be the minimum number of colors in a (p,q)-coloring of Knk. This paper deals only with k = 3.

Conlon-Fox-Lee-Sudakov [1] asked whether f3(n,p,p − 2) = (log n)o(1) for p ≥ 3 (the case p = 4 is easy). In this note we answer the ﬁrst open case with a substantially smaller bound.

Theorem 1.

√log logn).

![image 2](<2014-mubayi-coloring-triple-systems-local_images/imageFile2.png>)

f3(n,5,3) = eO(

The problem of determining fk(n,p,q) for ﬁxed k,p,q has a long history, beginning with its introduction by Erd˝os and Shelah [3, 4], and subsequent investigation (for graphs) by Erd˝os and

Gy´arf´as [5]. Studying fk(n,p,q) when q = 2 is equivalent to studying classical Ramsey numbers, and most of the eﬀort on these problems has therefore been for q > 2. The simplest nontrivial case in this regime is f2(n,4,3), which was shown to be no(1) in [10] and later Ω(log n) (see [7, 9]). The same upper bound was shown for f(n,5,4) in [6]. Conlon-Fox-Lee-Sudakov [2] recently extended this construction considerably by proving that f2(n,p,p−1) = no(1) for all ﬁxed p ≥ 4. Their result is sharp in the sense that f2(n,p,p) = Ω(n1/(p−2)).

The ﬁrst nontrivial hypergraph case is f3(n,4,3) and has tight connections to Shelah’s breakthrough proof [12] of primitive recursive bounds for the Hales-Jewett numbers. Answering a question of

![image 3](<2014-mubayi-coloring-triple-systems-local_images/imageFile3.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Research partially supported by NSF grant DMS-1300138. Email: mubayi@uic.edu

Graham-Rothschild-Spencer [8], Conlon et. al. [1] recently proved that f3(n,4,3) = no(1). They also posed a variety of basic questions about f3(n,p,q), including the one we address in this note.

Our construction uses an extension of the coloring in [10] together with the stepping up technique of Erd˝os and Hajnal. It is quite possible that, similar to the situation for graphs, other hypergraph cases will eventually be addressed by the ideas introduced here.

# 2 The Construction

We begin by deﬁning an edge-coloring σ of the complete graph Kn whose vertices are ordered.

Construction of σ: Given integers t < m and n = mt , let V (Kn) be the set of 0/1 vectors of length m with exactly t 1’s. Write v = (v(1),... ,v(m)) for a vertex. The vertices are naturally

ordered by the integer they represent in binary, so v < w iﬀ v(i) = 0 and w(i) = 1 where i is the ﬁrst position (minimum integer) in which v and w diﬀer. By considering vertices as characteristic vectors of sets, we may assume that V (Kn) = [mt ] whenever convenient. For each B ∈ [mt ] , let fB : 2B → [2t] be a bijection. Given vectors v < w that are characteristic vectors of sets S < T, let c1(vw) = min{i : v(i) = 0,w(i) = 1}, c2(vw) = min{j : j > i,v(i) = 1,w(i) = 0}, c3(vw) = fS(S ∩ T) and c4(vw) = fT(S ∩ T). Finally, deﬁne

σ(vw) = (c1(vw),c2(vw),c3(vw),c4(vw)).

If n is not of the form mt , then let n′ ≥ n be the smallest integer of this form, color [n2′] as described above, and restrict the coloring to [n2] . It is known [10, 11] that σ is both a (3,2) and (4,3)-coloring of Kn (we only need the ﬁrst and fourth coordinates of color vectors for this) and, for suitable choice of m and t it uses eO(

![image 4](<2014-mubayi-coloring-triple-systems-local_images/imageFile4.png>)

![image 5](<2014-mubayi-coloring-triple-systems-local_images/imageFile5.png>)

![image 6](<2014-mubayi-coloring-triple-systems-local_images/imageFile6.png>)

![image 7](<2014-mubayi-coloring-triple-systems-local_images/imageFile7.png>)

√log n)

![image 8](<2014-mubayi-coloring-triple-systems-local_images/imageFile8.png>)

colors for all n. We need the following additional properties. Proposition 2. The coloring σ satisﬁes the following properties.

- 1) If v < w < x, then σ(vw) = σ(wx).
- 2) If v < w < min{x,y}, and σ(vw) = σ(vx), then σ(vy) = σ(wx).
- 3) If v < w < x < y with σ(vw) = σ(xy), then σ(vx) = σ(vy).


Proof. It suﬃces to consider the ﬁrst coordinate c1 of σ to prove the ﬁrst two properties. For 1), observe that i = c1(vw) implies that w(i) = 1, while i = c1(wx) implies that w(i) = 0. For 2), let i = c1(vw) = c1(vx) and suppose for contradiction that i′ = c1(vy) = c1(wx) so that v(j) = y(j) for j < i′. Assume ﬁrst that i < i′ . Then y(i) = v(i) = 0, while w(i) = 1. This implies that w > y, a contradiction. Now assume that i > i′ (i = i′ is impossible since w(i) = 1 while w(i′) = 0). Then 0 = v(i′) = x(i′) = 1 due to c1(vy) = i′,c1(vx) = i > i′ and c1(wx) = i′.

We now prove 3) so assume we are given v < w < x < y with c1(vw) = c1(xy) = i < j = c2(vw) = c2(xy). Then v(j) = x(j) = 1 and y(j) = 0. Suppose that v,w,x,y are characteristic vectors of V,W,X,Y respectively. Then c3(vx) = c3(V X) = fV (V ∩X) while c3(vy) = c3(V Y ) = fV (V ∩Y ).

If c3(vx) = c3(vy), then fV (V ∩ X) = fV (V ∩ Y ) and since fV is a bijection, V ∩ X = V ∩ Y . But this is impossible as j ∈ (V ∩ X) \ Y .

![image 9](<2014-mubayi-coloring-triple-systems-local_images/imageFile9.png>)

![image 10](<2014-mubayi-coloring-triple-systems-local_images/imageFile10.png>)

![image 11](<2014-mubayi-coloring-triple-systems-local_images/imageFile11.png>)

![image 12](<2014-mubayi-coloring-triple-systems-local_images/imageFile12.png>)

We are now ready to describe the edge-coloring χ of Kn3 that we will use.

Construction of χ: Given a copy of Kn on [n] and the edge-coloring σ, we produce an edgecoloring χ of the 3-graph H on {0,1}n as follows. Order the vertices of H according to the integer that they represent in binary. Given vertices x < y in V (H), let γxy be the ﬁrst coordinate where x and y diﬀer. Given vertices x < y < z, let δxyz equal 1 if γxy < γyz and −1 otherwise. For an edge uvw with u < v < w, let

χ(uvw) = (σ(γuvγvw),δuvw).

![image 13](<2014-mubayi-coloring-triple-systems-local_images/imageFile13.png>)

![image 14](<2014-mubayi-coloring-triple-systems-local_images/imageFile14.png>)

![image 15](<2014-mubayi-coloring-triple-systems-local_images/imageFile15.png>)

![image 16](<2014-mubayi-coloring-triple-systems-local_images/imageFile16.png>)

√logn) colors, χ is an edge-coloring of KN3 (N = 2n) with eO(

![image 17](<2014-mubayi-coloring-triple-systems-local_images/imageFile17.png>)

Since σ is an edge-coloring of Kn with eO(

√log logN) colors as promised. Moreover, extending this construction to all N is trivial by

![image 18](<2014-mubayi-coloring-triple-systems-local_images/imageFile18.png>)

considering the smallest N′ ≥ N which is a power of 2, coloring [N2′] and restricting to [N2] . We are left with showing that χ is a (5,3)-coloring of KN3 .

Proof that χ is a (5,3)-coloring: Suppose, for contradiction, that X = {x1,... ,x5} where x1 < x2 < x3 < x4 < x5 are ﬁve vertices of H forming a 2-colored K53. Let γi = γxixi+1. Let γ = minγj and assume this minimum is achieved by γp. Note that this minimum is uniquely achieved, and γi = γi+1 for all i.

- Case 1: p ∈ {1,4}. The arguments for both cases are almost identical so we only consider the case p = 1. By assumption we have γ1 < γ2. First assume that γ3 > γ2. If γ4 > γ3, then the K4 on {γi : i ∈ [4]} has three colors since σ is a (4,3)-coloring and this gives at least three colors to the edges in X. If γ4 < γ3 then the K3 on {γi : i ∈ [3]} has two colors since σ is a (3,2)-coloring and this gives two colors to the edges of H within {xi : i ∈ [4]} with positive δ-coordinate. On the other hand δx3x4x5 = −1, so we again have three colors on X. We now suppose that γ3 < γ2. If γ4 < γ3, then the K3 on {γ2,γ3,γ4} has two colors since σ is a (3,2)-coloring and this gives two colors to the edges of H within {x2,x3,x4,x5} with negative δ-coordinate. On the other hand δx1x2x3 = 1, so we again have three colors on X. Finally, we may assume that γ1 < γ3 < min{γ2,γ4}. Now σ(γ1γ3) = σ(γ3,γ4) due to property 1) of σ, hence χ(x1x3x4) = χ(x3x4x5) and both have positive δ-coordinates. But δx2x3x4 = −1, so χ(x2x3x4) is the third color on X.
- Case 2: p ∈ {2,3}. The arguments for both cases are almost identical so we only consider the case p = 2. We have γ3 > γ2. If in addition γ4 > γ3, then we get two colors among {x2,x3,x4,x5} with positive δ-coordinate while δx1x2x3 = −1. So we may assume that γ2 < γ4 < γ3. Now χ(x2x3x4) and χ(x2x4x5) both have positive δ coordinates while δx3x4x5 = −1. Hence we have three colors unless σ(γ2γ3) = σ(γ2γ4) which we may assume. Certainly δx1x2x3 = −1, so we are done unless σ(γ2γ1) = σ(γ4γ3) which we also assume. If γ1 = γ4, then σ(γ2γ4) = σ(γ4γ3) and hence {γ2,γ4,γ3} is a monochromatic triangle, contradiction. If γ1 > γ4, then γ2 < γ4 < min{γ1,γ3} with σ(γ2γ4) = σ(γ2γ3) and σ(γ2γ1) = σ(γ4γ3). This contradicts property 2). If γ1 < γ4, then γ2 < γ1 < γ4 < γ3 with σ(γ2γ1) = σ(γ4γ3) and σ(γ2γ4) = σ(γ2γ3). This contradicts property 3) and completes the proof.


![image 19](<2014-mubayi-coloring-triple-systems-local_images/imageFile19.png>)

![image 20](<2014-mubayi-coloring-triple-systems-local_images/imageFile20.png>)

![image 21](<2014-mubayi-coloring-triple-systems-local_images/imageFile21.png>)

![image 22](<2014-mubayi-coloring-triple-systems-local_images/imageFile22.png>)

Acknowledgment. I am grateful to David Conlon and Choongbum Lee for carefully reading an earlier draft of this note and giving comments that helped improve the presentation.

# References

- [1] D. Conlon, J. Fox, C. Lee, B. Sudakov, On the grid Ramsey problem and related questions, Int. Math. Res. Not., to appear.
- [2] D. Conlon, J. Fox, C. Lee and B. Sudakov, The Erd˝os-Gy´rf´as problem on generalized Ramsey numbers, Proc. London Math. Soc., to appear.
- [3] P. Erd˝os, Problems and results on ﬁnite and inﬁnite graphs, in Recent advances in graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974), 183–192, Academia, Prague, 1975.
- [4] P. Erd˝os, Solved and unsolved problems in combinatorics and combinatorial number theory, in Proceedings of the twelfth southeastern conference on combinatorics, graph theory and comput-ing, Vol. I (Baton Rouge, La., 1981), Congr. Numer. 32 (1981), 49–62.
- [5] P. Erd˝os and A. Gy´arf´as, A variant of the classical Ramsey problem, Combinatorica 17 (1997), 459–467.
- [6] D. Eichhorn and D. Mubayi, Edge-coloring cliques with many colors on subcliques, Combinatorica 20 (2000), 441–444.
- [7] J. Fox and B. Sudakov, Ramsey-type problem for an almost monochromatic K4, SIAM J. Discrete Math. 23 (2008), 155–162.
- [8] R. L. Graham, B. L. Rothschild and J. H. Spencer, Ramsey theory, second ed., Wiley Interscience Series in Discrete Mathematics and Optimization, John Wiley & Sons Inc., New York, 1990.
- [9] A. Kostochka and D. Mubayi, When is an almost monochromatic K4 guaranteed?, Combin. Probab. Comput. 17 (2008), 823–830.
- [10] D. Mubayi, Edge-coloring cliques with three colors on all 4-cliques, Combinatorica 18 (1998), 293–296.
- [11] D. Mubayi, An explicit construction for a Ramsey problem, Combinatorica, 24 (2004), no. 2, 313–324
- [12] S. Shelah, Primitive recursive bounds for van der Waerden numbers, J. Amer. Math. Soc. 1


(1989), 683–697.

