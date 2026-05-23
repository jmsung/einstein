arXiv:1403.0250v1[math.CO]2Mar2014

The Erd˝os-Gy´rfa´s problem on generalized Ramsey numbers

David Conlon ∗ Jacob Fox † Choongbum Lee ‡ Benny Sudakov §

Abstract

Fix positive integers p and q with 2 ≤ q ≤ p2 . An edge-coloring of the complete graph Kn is said to be a (p,q)-coloring if every Kp receives at least q diﬀerent colors. The function f(n,p,q) is the minimum number of colors that are needed for Kn to have a (p,q)-coloring. This function was introduced by Erdo˝s and Shelah about 40 years ago, but Erd˝os and Gy´arf´as were the ﬁrst to study the function in a systematic way. They proved that f(n,p,p) is polynomial in n and asked to determine the maximum q, depending on p, for which f(n,p,q) is subpolynomial in n. We prove that the answer is p − 1.

# 1 Introduction

The Ramsey number rk(p) is the smallest natural number n such that every k-coloring of the edges of the complete graph Kn contains a monochromatic Kp. The existence of rk(3) was ﬁrst shown by Schur [13] in 1916 in his work on Fermat’s Last Theorem and it is known that rk(3) is at least exponential in k and at most a multiple of k!. It is a central problem in graph Ramsey theory to close the gap between the lower and upper bound, with connections to various problems in combinatorics, geometry, number theory, theoretical computer science and information theory (see, e.g., [9, 10]).

The following natural generalization of the Ramsey function was ﬁrst introduced by Erd˝os and Shelah [3, 4] and studied in depth by Erd˝os and Gy´arf´as [5]. Let p and q be positive integers with

### 2 ≤ q ≤ p2 . An edge-coloring of the complete graph Kn is said to be a (p,q)-coloring if every Kp receives at least q diﬀerent colors. The function f(n,p,q) is the minimum number of colors that are needed for Kn to have a (p,q)-coloring.

![image 1](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile1.png>)

∗Mathematical Institute, Oxford OX2 6GG, United Kingdom. Email: david.conlon@maths.ox.ac.uk. Research supported by a Royal Society University Research Fellowship.

†Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: fox@math.mit.edu. Research supported by a Packard Fellowship, by a Simons Fellowship, by NSF grant DMS-1069197, by an Alfred P. Sloan Fellowship and by an MIT NEC Corporation Award.

‡Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: cb lee@math.mit.edu. §Department of Mathematics, ETH, 8092 Zurich, Switzerland and Department of Mathematics, UCLA, Los Ange-

![image 2](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile2.png>)

les, CA 90095. Email: benjamin.sudakov@math.ethz.ch. Research supported in part by SNSF grant 200021-149111 and by a USA-Israel BSF grant.

To see that this is indeed a generalization of the usual Ramsey function, note that f(n,p,2) is the minimum number of colors needed to guarantee that no Kp is monochromatic. That is, f(n,p,2) is the inverse of the Ramsey function rk(p) and so we have

log n log log n ≤ f(n,3,2) ≤ clog n.

c′

![image 3](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile3.png>)

Erd˝os and Gy´arf´as [5] proved a number of interesting results about the function f(n,p,q), demonstrating how the function falls oﬀ from being equal to n2 when q = p2 to being at most logarithmic when q = 2. In so doing, they determined ranges of p and q where the function f(n,p,q) is linear in n, where it is quadratic in n and where it is asymptotically equal to n2 . Many of these results were subsequently sharpened by Sa´rk¨ozy and Selkow [11, 12].

One simple observation made by Erd˝os and Gy´arf´as is that f(n,p,p) is always polynomial in n. To see this, it is suﬃcient to note that if a coloring uses fewer than n1/(p−2) − 1 colors then it necessarily contains a Kp which uses at most p − 1 colors. For p = 3, this is easy to see since one only needs that some vertex has at least two neighbors in the same color. For p = 4, we have that any vertex will have at least n1/2 neighbors in some ﬁxed color. But, since there are fewer than n1/2 − 1 colors on this neighborhood of size at least n1/2, the case p = 3 implies that it contains a triangle with at most two colors. The general case follows similarly.

Erd˝os and Gy´arf´as [5] asked whether this result is best possible, that is, whether q = p is the smallest value of q for which f(n,p,q) is polynomial in n. For p = 3, this is certainly true, since we know that f(n,3,2) ≤ clog n. However, for general p, they were only able to show that f(n,p,⌈log p⌉) is subpolynomial, where here and throughout the paper we use log to denote the logarithm taken base 2. This left the question of determining whether f(n,p,p − 1) is subpolynomial wide open, even for p = 4.

The ﬁrst progress on this question was made by Mubayi [8], who found an elegant construction which implies that f(n,4,3) ≤ ec

√logn. This construction was also used by Eichhorn and Mubayi [2] to demonstrate that f(n,5,4) ≤ ec

![image 4](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile4.png>)

√logn. More generally, they used the construction to show that f(n,p,2⌈log p⌉ − 2) is subpolynomial for all p ≥ 5.

![image 5](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile5.png>)

In this paper, we answer the question of Erd˝os and Gy´arf´as in the positive for all p. That is, we prove that f(n,p,p − 1) is subpolynomial for all p. Quantitatively, our main theorem is the following.

- Theorem 1.1. For all natural numbers p ≥ 4 and n ≥ 1, f(n,p,p − 1) ≤ 216p(logn)1−1/(p−2) log logn.


In Section 2, we deﬁne our (p,p − 1)-coloring by a recursive procedure. We begin by reviewing Mubayi’s (4,3)-coloring, as it is the base case of our recursion. The formal proof of the fact that our coloring is indeed a (p,p − 1)-coloring is quite technical and thus we ﬁrst give an outline of the proof in Section 3. Then, in Section 4, we establish some properties of the coloring. Finally, in

Section 5, we prove that the coloring given in Section 2 is a (p,p − 1)-coloring. We will conclude with some further remarks.

Notation. For vectors v ∈ Xt1+t2,v1 ∈ Xt1,v2 ∈ Xt2, we will often use the notation v = (v1,v2),

in order to indicate that the i-th coordinate of v is equal to the i-th coordinate of v1 for 1 ≤ i ≤ t1 and the (t1 + j)-th coordinate of v is equal to the j-th coordinate of v2 for 1 ≤ j ≤ t2. We will use similar notation for several vectors. Throughout the paper, log denotes the base 2 logarithm. For the sake of clarity of presentation, we systematically omit ﬂoor and ceiling signs whenever they are not essential.

# 2 The coloring construction

The purpose of this section is to deﬁne the coloring used to prove Theorem 1.1. The coloring can be considered as a generalization of (a variant of) Mubayi’s (4,3)-coloring. We therefore ﬁrst introduce this coloring and then redeﬁne it in a way that can be naturally extended. We then present the coloring used to prove Theorem 1.1. As it is a rather involved recursive deﬁnition, we give an example to illustrate it. We conclude the section by establishing a bound on the number of colors used in this coloring. In the following sections, we will show that this coloring is a (p,p−1)-coloring, completing the proof.

## 2.1 Mubayi’s (4, 3)-coloring

Let N = mt for some integers m and t. Suppose that we are given two distinct vectors v,w ∈ [m]t of the form v = (v1,... ,vt) and w = (w1,... ,wt). Deﬁne

c(v,w) = {vi,wi},a1,... ,at , where i is the least coordinate in which vi = wi and aj = 0 if vj = wj and aj = 1 if vj = wj. If

- v = w, deﬁne c(v,v) = 0.


Note that c is a symmetric function. This is a variant of Mubayi’s coloring and can be proved to be a (p,p − 1)-coloring for small values of p.

One might suspect that this is a (p,p − 1)-coloring for large integers p as well, but, unfortunately, it fails to be a (26,25)-coloring (and a (p,p − 1)-coloring for all p ≥ 26) for the following reason. Consider the set {1,2,3}3. This set has 33 = 27 elements and at most 3 · 23 = 24 colors are used in coloring this set. Therefore, we can ﬁnd 26 vertices with at most 24 colors within the set. Moreover, for every ﬁxed p and large enough N, letting s = √log p, the set S = {1,2,... ,2s}s has cardinality 2s2 = p and uses at most 22s 2s < 23s = 23

![image 6](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile6.png>)

√logp colors and, for large enough m and t, is a subset of [m]t. Hence, this edge-coloring of the complete graph on [N] fails to be a (p,23

![image 7](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile7.png>)

√logp)-coloring.

![image 8](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile8.png>)

## 2.2 Redeﬁning Mubayi’s coloring

Before proceeding further, let us redeﬁne the coloring given above from a slightly diﬀerent perspective. We do this to motivate the (p,p − 1)-coloring which we use to establish Theorem 1.1.

- Let m = 2r1 and, abusing notation, identify the set [m] with {0,1}r1. Let r2 = r1t for some positive integer t. Suppose that we are given two vectors v,w ∈ [m]t = {0,1}r1t. We decompose


- v as v = (v1(1),... ,vt(1)), where vi(1) ∈ {0,1}r1 for i = 1,2,... ,t and similarly decompose w. The function c was deﬁned as follows:


c(v,w) = {vi(1),wi(1)},a1,... ,at ,

where i is the least coordinate in which vi(1) = wi(1) and, for j = 1,2,... ,t, aj represents whether vj(1) = wj(1) or not. If v = w, then c(v,v) = 0.

Deﬁne h1 as the ﬁrst coordinate of c. That is, h1(v,w) = {vi(1),wi(1)} (we let h1(v,v) = 0 for convenience). Note that h1 takes a pair of vectors of length r2 = r1t as input and outputs a pair of vectors of length r1.

For two vectors x,y ∈ {0,1}r1 of the form x = (x1,... ,xr1), y = (y1,... ,yr1), deﬁne the function

- h0 as follows. We have h0(x,x) = 0 for each x and, if x = y, then h0(x,y) = {xi,yi}, where i is the minimum index for which xi = yi. Since all xi and yi are either 0 or 1, there are only two possible outcomes for h0, 0 if the two vectors are equal and {0,1} if they are not equal. Note that h0 takes a pair of vectors of length r1 as input and outputs a pair of vectors of length r0 = 1. Thus, both
- h1 and h0 are functions which record the ﬁrst ‘block’ that is diﬀerent. The diﬀerence between the two functions lies in their interpretation of ‘block’: for h1 it is a subvector of length r1 and for h0 it is a subvector of length r0. Summarizing, we see that c is equivalent to the coloring c′ given by


c′(v,w) = h1(v,w),h0(v1(1),w1(1)),... ,h0(vt(1),wt(1)) .

Informally, we ﬁrst decompose the given pair of vectors v and w into subvectors of length r2 and apply h1 (we observe only a single subvector in this case since v and w themselves are vectors of length r2). Then we decompose v and w into subvectors of length r1 and apply h0 to each corresponding pair of subvectors of v and w.

## 2.3 Deﬁnition of the coloring

In this section, we generalize the construction given in the previous section to obtain a (p,p − 1)coloring.

For a positive integer α, we will describe the coloring as an edge-coloring of the complete graph over the vertex set {0,1}α. Let r0,r1,... be a sequence of positive integers such that r0 = 1 and rd−1 divides rd for all d ≥ 1.

For a set of indices I, let πI be the canonical projection map from {0,1}α to {0,1}I. We will write πi instead of π[i] for convenience. Thus πi is the projection map to the ﬁrst i coordinates.

The key idea in the construction is to understand vectors at several diﬀerent resolutions. Suppose that we are given two vectors v,w ∈ {0,1}α. For d ≥ 0, let ad and bd be integers satisfying ad ≥ 0 and 1 ≤ bd ≤ rd such that α = adrd + bd. Let

v = v1(d),v2(d),... ,va(d)

d+1 ,

d+1 ∈ {0,1}bd. We refer to the vectors vi(d) as blocks of resolution d. We similarly decompose w as w = w1(d),w2(d),... ,wa(dd),wa(d)

where vi(d) ∈ {0,1}rd for i = 1,2,... ,ad and va(d)

d+1 for d ≥ 0. We ﬁrst deﬁne two auxiliary families of functions ηd and ξd. For d ≥ 0, if v = w, let

ηd(v,w) = i,{vi(d),wi(d)} ,

where i is the minimum index such that vi(d) = wi(d). If v = w, let ηd(v,v) = 0.

Note that ηd is a symmetric function. Further note that ηd is slightly diﬀerent from hd deﬁned in the previous subsection since we add an additional coordinate which records the index i as well. The main theorem is valid even if we do not add this index, but we choose to add it as it simpliﬁes the proof. We refer the reader to Subsection 6.2 for a further discussion of this point.

For d ≥ 0, let

ξd(v,w) = ηd v1(d+1),w1(d+1) ,... ,ηd va(d+1)

d+1+1,wa(d+1)

d+1+1 .

Note that the function ξd decomposes the vectors into blocks of resolution d + 1 and outputs a vector containing information about blocks of resolution d.

For d ≥ 0, let

cd = ξd × ξd−1 × ... × ξ0. Note that the coloring cd depends on the choice of the parameters r0,r1,... ,rd+1. We prove our main theorem in two steps: we ﬁrst estimate the number of colors and then prove that it is a (p,p − 1)-coloring.

- Theorem 2.1. Let p and β be ﬁxed positive integers with β = 1. For the choice ri = βi for 0 ≤ i ≤ p + 1, the edge-coloring cp of the complete graph on n = 2βp+1 vertices uses at most 24(logn)1−1/(p+1) log logn colors.


Theorem 2.2. Let p and α be ﬁxed positive integers. Then, for every choice of parameters r1,... ,rp+1, the edge-coloring cp is a (p + 3,p + 2)-coloring of the complete graph on the vertex set {0,1}α.

For integers n of the form n = 2βp+1, Theorem 1.1 follows from Theorems 2.1 and 2.2. For general n ≥ p+ 3 ≥ 4, ﬁrst notice that if n2 < 216p(logn)1−1/(p+1) log logn, then the statement is trivially true, as we may color each edge with diﬀerent colors. Hence, we may assume that the inequality does not hold, from which it follows that

2log n ≥ 16p(log n)1−1/(p+1) log log n ≥ 16p(log n)1−1/(p+1)

and n ≥ 2(8p)p+1. Hence, there exists an integer of the form 2βp+1 which is at most n(1+1/8p)p+1 ≤ n2. Therefore, there exists a (p + 3,p + 2)-coloring of the complete graph on the vertex set [n] using at most

24(2 logn)1−1/(p+1) log(2 logn) ≤ 24·2(logn)1−1/(p+1)(1+log logn) ≤ 216(logn)1−1/(p+1) log logn

colors (in the second inequality we used the fact that log log n ≥ log log 4 ≥ 1). Thus we obtain Theorem 1.1. Theorem 2.1 is proved in Subsection 2.5, while Theorem 2.2 is proved in Section 5 and builds on the two sections leading up to it.

## 2.4 Example

Let us illustrate the coloring by working out a small example. Suppose that r1 = 2 and r2 = 4. Let v = (0,0,1,0,1,1,0) and w = (0,0,1,1,1,0,0) be vectors in {0,1}7. Then

- v = (0,0,1,0,1,1,0) = ‘0,0’,‘1,0’,‘1,1’,‘0’ = ‘0,0,1,0’,‘1,1,0’ ,

where the quotation marks indicate the blocks of each resolution. Similarly,

- w = (0,0,1,1,1,0,0) = ‘0,0’,‘1,1’,‘1,0’,‘0’ = ‘0,0,1,1’,‘1,0,0’ .


The function η0 records the ﬁrst pair of blocks of resolution 0 which are diﬀerent. So η0(v,w) = (4,{0,1}),

where the value of the ﬁrst coordinate, 4, indicates that v and w ﬁrst diﬀer in the fourth coordinate. Similarly, the function η1 will record the ﬁrst pair of blocks of resolution 1 which are diﬀerent. So

η1(v,w) = 2,{(1,0),(1,1)} .

Computing ξ0 and ξ1 involves one more step. To compute ξ0, we apply η0 to each pair of blocks of resolution 1. Therefore,

ξ0(v,w) = η0 (0,0),(0,0) ,η0 (1,0),(1,1) ,η0 (1,1),(1,0) ,η0 (0),(0)

= 0,(2,{0,1}),(2, {1,0}), 0 , which is a vector of length four.

Similarly, to compute ξ1, we apply η1 to each pair of blocks of resolution 2. Therefore, ξ1(v,w) = η1 (0,0,1,0),(0,0,1, 1) ,η1 (1,1,0),(1,0,0)

= 2, (1,0),(1,1) , 1, (1,1),(1,0) , which is a vector of length two.

- 2.5 Number of colors In this subsection, we prove Theorem 2.1.


Proof of Theorem 2.1. Recall that β is a positive integer greater than 1 and rd = βd for 0 ≤ d ≤ p + 1. Let α = βp+1. The goal here is to give an upper bound on the number of colors in the edge-coloring cp of the complete graph with vertex set {0,1}α = {0,1}βp+1. First, for 0 ≤ d ≤ p, the function ηd outputs either zero or an index and a pair of distinct blocks of resolution d. Hence, there are at most 1 + α · 2rd(2rd − 1) ≤ α22βd possible outcomes for the function ηd. Second, for 0 ≤ d ≤ p, the function ξd is a product of r α

= βp−d outcomes of ηd. Hence, there are at most

![image 9](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile9.png>)

d+1

p−d

α · 22βd β

= β(p+1)βp−d · 22βp

possible outcomes for the function ξd. Since cp is deﬁned as ξp × ξp−1 × ··· × ξ0, the total number of colors used in cp is at most

p

d=0

β(p+1)βp−d · 22βp ≤ β2(p+1)βp22(p+1)βp ≤ 24(p+1)βp logβ.

- Let n = 2α = 2βp+1 and note that βp = (log n)1−1/(p+1) and log β = p+11 log log n. Thus, we have colored the edges of the complete graph on n vertices using at most


![image 10](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile10.png>)

24(logn)1−1/(p+1) log logn colors, as claimed in Theorem 2.1.

![image 11](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile11.png>)

![image 12](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile12.png>)

![image 13](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile13.png>)

![image 14](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile14.png>)

As we saw in Subsection 2.1, for large enough q, Mubayi’s coloring (which is similar to c1) is not a (q,q − 1)-coloring or even a (q,qε)-coloring for any ﬁxed ε > 0. Similarly, we can see that the same is true for the coloring cp for every ﬁxed p (we will brieﬂy describe the proof of this fact in Subsection 6.3). This explains why we need to consider cp with an increasing value of p.

# 3 Outline of proof

In this section, we outline the proof of Theorem 2.2. Assume that we want to prove that the edge-coloring of the complete graph on the vertex set {0,1}α given by cp is a (p+3,p+2)-coloring. We will use induction on α to prove the stronger statement that the coloring is a (q,q −1) coloring for all q ≤ p + 3. To illustrate a simple case, assume that we are about to prove it for α = rp+1 and have proved it for all smaller values of α. Let S ⊂ {0,1}α be a given set of size at most p + 3. We wish to show that the edges of S receive at least |S| − 1 distinct colors.

Let α′ = rp+1 − rp. For two vectors v,w ∈ S satisfying v = w, let v = (v′,v′′) and w = (w′,w′′) where v′,w′ ∈ {0,1}α′ and v′′,w′′ ∈ {0,1}α−α′ = {0,1}rp. Note that since α′ = rp+1−rp is divisible by rp, the ﬁrst αr′

blocks of resolution p of v are identical to those of v′ and a similar fact holds for

![image 15](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile15.png>)

p

- w and w′.


If v′ = w′ then, by the observation above, the ﬁrst rα′

coordinates of ξp−1 are all zero. On the other hand, if v′ = w′, then the ﬁrst block of resolution p on which v and w diﬀer is one of the ﬁrst αr′

![image 16](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile16.png>)

p

![image 17](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile17.png>)

p

blocks. Hence, in this case, at least one of the ﬁrst rα′

coordinates of ξp−1 is non-zero. Thus, if we deﬁne sets ΛI and ΛE as

![image 18](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile18.png>)

p

ΛI = cp(v,w) : v′ = w′, v,w ∈ S and

ΛE = cp(v,w) : v′ = w′, v = w, v,w ∈ S ,

then we have ΛI ∩ ΛE = ∅. Hence, it suﬃces to prove that |ΛI| + |ΛE| ≥ |S| − 1. The index ‘I’ stands for inherited colors and ‘E’ stands for emerging colors.

The coloring cp contains more information than necessary to prove that the number of colors is large. Hence, we consider only part of the coloring cp. The part of the coloring that we consider for ΛI and ΛE will be diﬀerent, as we would like to highlight diﬀerent aspects of our coloring depending on the situation.

Deﬁne the sets CI and CE as

CI = cp(v′,w′),ηp−1(v′′,w′′) : v′ = w′, v,w ∈ S and

CE = {v′′,w′′} : v′ = w′, v′′ = w′′, v,w ∈ S .

We claim here without proof that |CI| ≤ |ΛI| and |CE| ≤ |ΛE|. Abusing notation, for two vectors v,w ∈ S, we will from now on refer to the color between v and w as the corresponding ‘color’ in CI or CE. It now suﬃces to prove that |CI| + |CE| ≥ |S| − 1.

To analyze the colors in CI and CE, we take a step back and consider the ﬁrst α′ coordinates of the vectors in S. Let S′ = πα′(S). Note that S′ is the collection of vectors v′ in the notation above. There is a certain ‘branching phenomenon’ of vectors and colors. For a vector v′ ∈ S′, let

Tv′ = {v : πα′(v) = v′, v ∈ S}. Hence, Tv′ is the set of vectors in S whose ﬁrst α′ coordinates are equal to v′. Note that

|Tv′| = |S|. (1)

v′∈S′

Consider two vectors v,w ∈ S. If v and w are both in the same set Tv′, then the color between v and w belongs to CE and if they are in diﬀerent sets, then the color between v and w belongs to CI. For a color c ∈ CI, note that the ﬁrst coordinate of c is of the form cp(v′,w′) for two vectors

- v′,w′ ∈ S′. Further note that cp(v′,w′) is the color of an edge that lies within S′. Hence, c is a ‘branch’ of some color of an edge that lies within S′. In particular, by induction on α, we see that


|CI| ≥ |S′| − 1. (2)

For a color c ∈ CE, let µc be the number of (unordered) pairs of vectors v,w such that c is the color between v and w. We have the following equation

µc =

v′∈S′

c∈CE

|Tv′| 2 ≥

(|Tv′| − 1). (3)

v′∈S′

Let us ﬁrst consider the simple case when µc = 1 for all c ∈ CE (that is, there are no overlaps between the emerging colors). In this case, we have |CE| = c∈C

µc. By (2), we have

E

|CI| + |CE| ≥ (|S′| − 1) + |CE| = (|S′| − 1) +

µc,

c∈CE

which by (3) and (1) is at least (|S′| − 1) +

(|Tv′| − 1) =

v′∈S′

|Tv′| − 1 = |S| − 1

v′∈S′

and thus the conclusion follows for the case when µc = 1 for all c ∈ CE. However, there might be some overlap between the emerging colors. Note that there are |CE| emerging colors instead of the c∈C

µc which we obtain by counting with multiplicity. Thus, there are c∈C

E

(µc − 1) ‘lost’ emerging colors. Our key lemma asserts that every lost emerging color will be accounted for by contributions towards |CI|. Formally, we will improve (2) and obtain the following inequality

E

|CI| ≥ (|S′| − 1) +

(µc − 1). (4)

c∈CE

Given this inequality, we will have

|CI| + |CE| ≥ (|S′| − 1) +

(µc − 1) + |CE| = (|S′| − 1) +

µc,

c∈CE

c∈CE

which, as above, implies that |CI| + |CE| ≥ |S| − 1.

We conclude this section with a sketch of the proof of (4). To see this, we further study the branching of the colors. Deﬁne CB as the set of colors that appear within the set S′, that is,

CB = cp(v′,w′) : v′,w′ ∈ S′ ,

where the index ‘B’ stands for base colors. Every color c ∈ CI is of the form c = (c′,?), where c′ ∈ CB and the question mark ‘?’ stands for an unspeciﬁed coordinate. Thus, we immediately have at least |CB| colors in CI (this is the content of Equation (2)). Now take a color c′′ = {v′′,w′′} ∈ CE and suppose that c′′ has multiplicity µc′′. Then there exist vectors xi ∈ S′ for i = 1,2,... ,µc′′ such that c′′ is the color between (xi,v′′) and (xi,w′′). Consider the colors of the two pairs (x1,v′′),(x2,v′′)

and (x1,v′′),(x2,w′′) in CI. These are

- cp(x1,x2),ηp−1(v′′,v′′) = (c1,2,0) ∈ CI and
- cp(x1,x2),ηp−1(v′′,w′′) = c1,2,ηp−1(c′′) ∈ CI,


respectively, where c1,2 ∈ CB (here we abuse notation and deﬁne ηp−1(c′′) = ηp−1(v′′,w′′), which is allowed since the right-hand-side is symmetric in the two input coordinates). Note that by the inductive hypothesis, there are at least µc′′ − 1 distinct colors of the form ci,j for distinct pairs of indices i and j. Hence, by considering these colors, we add colors of the types (ci,j,0) and (ci,j,ηp−1(c′′)) for at least µc′′ − 1 distinct colors ci,j ∈ CB. Even if one of these two colors equals the color (ci,j,?) counted above, we have added at least µc′′ − 1 colors to CI by considering the color c′′ ∈ CE.

Now consider another color c′′1 ∈ CE. This color adds a further µc′′

− 1 colors to CI as long as

1

ηp−1(c′′) = ηp−1(c′′1). Therefore, if we can somehow guarantee that ηp−1(c′′) is distinct for all c′′, then we have

|CI| ≥ |CB| +

(µc − 1),

c∈CE

which proves (4), since |CB| ≥ |S′| − 1 by the inductive hypothesis.

Hence, it would be helpful to have distinct ηp−1(c′′) for each c′′ ∈ CE. Even though we cannot always guarantee this, we can show that there exists a resolution in which the corresponding fact does hold. This will be explained in more detail in Section 5.

# 4 Properties of the coloring

In this section, we collect some useful facts about the coloring functions cd. Before listing these properties, we introduce the formal framework that we will use to describe them.

## 4.1 Reﬁnement of functions

For a function f : A → B, let Πf = {f−1(b) : b ∈ f(A)}. Thus, Πf is a partition of A into sets whose elements map by f to the same element in B. For two functions f and g deﬁned over the

same domain, we say that f reﬁnes g if Πf is a reﬁnement of Πg. This deﬁnition is equivalent to saying that f(a) = f(a′) implies that g(a) = g(a′) and is also equivalent to saying that there exists a function h for which g = h ◦ f. The term f reﬁnes g is also referred to as g factors through f in category theory. This formalizes the concept that f contains more information than g.

For two functions f and g deﬁned over the same domain A, let f × g be the function deﬁned over A where (f × g)(a) = (f(a),g(a)). The following proposition collects several basic properties of reﬁnements of functions which will be useful in the proof of the main theorem.

Proposition 4.1. Let f1,f2,f3 and f4 be functions deﬁned over the domain A.

- (i) (Identity) f1 reﬁnes f1.
- (ii) (Transitivity) If f1 reﬁnes f2 and f2 reﬁnes f3, then f1 reﬁnes f3.
- (iii) If f1 reﬁnes f3, then f1 × f2 reﬁnes f3.
- (iv) If f1 reﬁnes both f2 and f3, then f1 reﬁnes f2 × f3.
- (v) If f1 reﬁnes f3 and f2 reﬁnes f4, then f1 × f2 reﬁnes f3 × f4.
- (vi) If f1 reﬁnes f2, then, for all A′ ⊂ A, we have |f1(A′)| ≥ |f2(A′)|.


Proof. Let Πi = Πfi for i = 1,2,3.

- (i) This is trivial since Π1 reﬁnes Π1.
- (ii) If f1 reﬁnes f2 and f2 reﬁnes f3, then Π1 reﬁnes Π2 and Π2 reﬁnes Π3. Therefore, Π1 reﬁnes Π3 and f1 reﬁnes f3.
- (iii) Since f1 × f2 clearly reﬁnes f1, this follows from (ii).
- (iv) If f1(a) = f1(a′), then f2(a) = f2(a′) and f3(a) = f3(a′). Hence, (f2 × f3)(a) = (f2 × f3)(a′) and we conclude that f1 reﬁnes f2 × f3.
- (v) By (iii), f1 × f2 reﬁnes both f3 and f4. Therefore, by (iv), f1 × f2 reﬁnes f3 × f4.
- (vi) For i = 1,2, let Πi|A′ = {X ∩ A′ : X ∈ Πi,X ∩ A′ = ∅} and note that |fi(A′)| = Πi|A′ . Since Π1 is a reﬁnement of Π2, we see that Π1|A′ is a reﬁnement of Π2|A′. Therefore, it follows that


|f1(A′)| = Π1|A′ ≥ Π2|A′ = |f2(A′)|, as required.

![image 19](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile19.png>)

![image 20](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile20.png>)

![image 21](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile21.png>)

![image 22](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile22.png>)

Reﬁnements arise in our proof because we often consider colorings with less information than the full coloring. In the outline above, we considered several diﬀerent sets of colors, namely, ΛI, ΛE, CI and CE and we claimed without proof that |CI| ≤ |ΛI| and |CE| ≤ |ΛE|. If we can show that ΛI is a reﬁnement of CI and ΛE is a reﬁnement of CE, then these inequalities follow from Proposition

- 4.1 (vi) above.


## 4.2 Properties of the coloring

We developed our formal framework for a rigorous treatment of the following two lemmas. It may be helpful at this stage to recall the deﬁnitions of ηd, ξd and cd from Subsection 2.3. Lemma 4.2. Suppose that α, α′ and d are integers with d ≥ 0 and 1 ≤ α′ ≤ α. Then the following hold (where all functions are considered as deﬁned over {0,1}α × {0,1}α):

- (i) ηd reﬁnes ηd ◦ (πα′ × πα′).
- (ii) ξd reﬁnes ξd ◦ (πα′ × πα′).
- (iii) cd reﬁnes cd ◦ (πα′ × πα′). Proof. The case α′ = α is trivial so we assume that α′ < α.


- (i) Let v and w be vectors in {0,1}α and let v′ = πα′(v) and w′ = πα′(w). We will show that one can compute the value of ηd(v′,w′) based only on the value of ηd(v,w). This clearly implies the desired conclusion. If ηd(v,w) = 0, then v = w and it follows that ηd(v′,w′) = 0. Assume then that ηd(v,w) = (i,{vi(d),wi(d)}) for some index i and blocks vi(d),wi(d) of resolution d. Let j be the ﬁrst coordinate in which the two vectors vi(d) and wi(d) diﬀer. Then the ﬁrst coordinate x (note that 1 ≤ x ≤ α) in which v and w diﬀer is x = (i − 1) · rd + j and satisﬁes

(i − 1) · rd < x ≤ min{i · rd,α}.

Note that the values of i and j can be deduced from ηd(v,w) and hence x can as well. It thus suﬃces to verify that ηd(v′,w′) can be computed using only α,α′,rd, x, i, vi(d) and wi(d).

If α′ > i · rd, then we have ηd(v′,w′) = ηd(v,w) = (i,{vi(d),wi(d)}) and the claim is true. On the other hand, if α′ ≤ i · rd, then there are two cases. If α′ < x, then we have v′ = w′. Therefore, ηd(v′,w′) = 0 and the claim holds for this case as well. The ﬁnal case is when x ≤ α′ ≤ i · rd. In this case, we see that

ηd(v′,w′) = i, π[α′−(i−1)rd](vi(d)),π[α′−(i−1)rd](wi(d)) and the claim holds.

- (ii) Let v and w be two vectors in {0,1}α. Then


ξd(v,w) = ηd(v1(d+1),w1(d+1)),ηd(v2(d+1),w2(d+1)),... ,ηd(va(d+1+1),wa(d+1+1)) ,

for some integer a ≥ 0. Let v′ = πα′(v) and w′ = πα′(w). Suppose that (j − 1)rd+1 < α′ ≤ jrd+1. Then note that the j-th block of resolution d + 1 of v′ is π[α′−(j−1)rd+1](vj(d+1)) and that of w′ is π[α′−(j−1)rd+1](wj(d+1)). Then ξd(v′,w′) consists of j coordinates, where for 1 ≤ i < j the i-th coordinate is identical to the i-th coordinate of ξd(v,w) and, for i = j, the j-th coordinate is

ηd ◦ (π[α′−(j−1)rd+1] × π[α′−(j−1)rd+1])(vj(d+1),wj(d+1)).

Thus the function ξd reﬁnes ξd ◦ (πα′ × πα′) coordinate by coordinate (by part (i) of this lemma). Hence, by Proposition 4.1(v), we see that ξd reﬁnes ξd ◦ (πα′ × πα′).

- (iii) This follows from cd = ξd × ··· × ξ0, part (ii) of this lemma and Proposition 4.1(v).


![image 23](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile23.png>)

![image 24](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile24.png>)

![image 25](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile25.png>)

![image 26](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile26.png>)

- Lemma 4.2 seems intuitively obvious and might even seem trivial at ﬁrst sight, but a moment’s thought reveals the fact that it is nontrivial. To see this, consider the function

hd(v,w) = {vi(d),wi(d)},

which is the projection to the second coordinate of ηd(v,w). Then the function hd fails to satisfy Lemma 4.2(i). Moreover, if the functions ξd and cd were built using hd instead of ηd, these would also fail to satisfy the claim of Lemma 4.2.

The next lemma completes the proof of one of the promised claims, namely, that ΛI (or, rather, a generalization thereof) reﬁnes CI.

- Lemma 4.3. Suppose that positive integers d,p,α and α′ are given such that 1 ≤ d ≤ p + 1 and


α′ is the maximum integer less than α divisible by rd. Let γd be the function which takes a pair of vectors v,w ∈ {0,1}α as input and outputs

γd(v,w) = (cp(v′,w′),ηd−1(v′′,w′′)),

where v = (v′,v′′) and w = (w′,w′′) for v′,w′ ∈ {0,1}α′ and v′′,w′′ ∈ {0,1}α−α′. Then cp|{0,1}α×{0,1}α reﬁnes γd.

Proof. For brevity, we restrict the functions to the set {0,1}α × {0,1}α throughout the proof. By Lemma 4.2(iii), we know that cp reﬁnes cp ◦ (πα′ × πα′) and hence cp reﬁnes the ﬁrst coordinate of γd. On the other hand, since α′ is the maximum integer less than α divisible by rd, the term ηd−1(v′′,w′′) forms the last coordinate of the vector ξd−1(v,w). Hence, by Proposition 4.1(iii), ξd−1 reﬁnes ηd−1(v′′,w′′). By the deﬁnition of cp and Proposition 4.1(iii), we know that cp reﬁnes ξd−1. Therefore, by transitivity (Proposition 4.1(ii)), we see that cp reﬁnes ηd−1(v′′,w′′). Thus, cp reﬁnes both coordinates of γd and hence, by Proposition 4.1(iv), we see that cp reﬁnes γd.

![image 27](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile27.png>)

![image 28](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile28.png>)

![image 29](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile29.png>)

![image 30](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile30.png>)

# 5 Proof of the main theorem

In this section we prove Theorem 2.2, which asserts that for all α ≥ 1 and p ≥ 1, the edge-coloring of the complete graph on the vertex set {0,1}α given by cp is a (p + 3,p + 2)-coloring. We will prove by induction on α that every set S with |S| ≤ p + 3 receives at least |S| − 1 distinct colors. The base case is when α ≤ rp. In this case, for two distinct vectors v,w ∈ {0,1}α, we have ξp(v,w) = ηp(v,w) = (1,{v,w}) . Hence, for a given set S ⊂ {0,1}α, the edges within this set are all colored with distinct colors, thereby implying that at least |S2| ≥ |S| − 1 colors are used.

Now suppose that α > rp is given and the claim has been proved for all smaller values of α. Let S ⊂ {0,1}α be a given set with |S| ≤ p + 3. For each 1 ≤ d ≤ p, let αd be the largest integer less than α which is divisible by rd. Note that since rd−1 divides rd for all 1 ≤ d ≤ p, we have

αp ≤ αp−1 ≤ ··· ≤ α1.

For 1 ≤ d ≤ p, deﬁne sets ΛI(d) and ΛE(d) as

ΛI(d) = cp(v,w) : παd(v) = παd(w), v,w ∈ S and

ΛE(d) = cp(v,w) : παd(v) = παd(w), v = w, v,w ∈ S . Since αd is divisible by rd, if παd(v) = παd(w), then the ﬁrst αrd

coordinates of ξd−1(v,w) will all be zero. On the other hand, if παd(v) = παd(w), then this is not the case. Since ξd−1 is part of cp, this implies that ΛI(d) ∩ ΛE(d) = ∅. Hence, for all d, the number of colors within S is exactly |ΛI(d)| + |ΛE(d)|. It therefore suﬃces to prove that |ΛI(d)| + |ΛE(d)| ≥ |S| − 1 for some index d.

![image 31](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile31.png>)

d

We would like to extract only the important information from the colors in ΛI(d) and ΛE(d). For each 1 ≤ d ≤ p and a given pair of vectors v,w ∈ S, let v = (vd′ ,vd′′) and w = (wd′ ,wd′′) for vd′ ,wd′ ∈ {0,1}αd and vd′′,wd′′ ∈ {0,1}α−αd. Deﬁne the sets CI(d) and CE(d) as

CI(d) = cp(vd′ ,wd′ ),ηd−1(vd′′,wd′′) : vd′ = wd′ , v,w ∈ S and

CE(d) = {vd′′,wd′′} : vd′ = wd′ , vd′′ = wd′′, v,w ∈ S .

By Lemma 4.3 and Proposition 4.1(vi), we see that |CI(d)| ≤ |ΛI(d)|. We also have |CE(d)| ≤ |ΛE(d)|. To see this, suppose that a color {vd′′,wd′′} ∈ CE(d) comes from a pair of vectors v = (vd′ ,vd′′) and

- w = (wd′ ,wd′′) in S. Since vd′ = wd′ and αd is divisible by rd, the function ηd applied to the last pair of blocks of resolution d + 1 of v and w is equal to (i,{vd′′,wd′′}) for some integer i. Therefore, the last coordinate of ξd(v,w) has value (i,{vd′′,wd′′}). This implies that |CE(d)| ≤ |ΛE(d)|. Hence, it now suﬃces to prove that |CI(d)| + |CE(d)| ≥ |S| − 1 for some index 1 ≤ d ≤ p.


Assume for the sake of contradiction that we have |CI(d)| + |CE(d)| ≤ |S| − 2 for all 1 ≤ d ≤ p. The following is the key ingredient in our proof.

Claim 5.1. If |CI(p)| + |CE(p)| ≤ |S| − 2, then there exists an index d such that ηd−1(c) is distinct for each c ∈ CE(d).

The proof of this claim will be given later. Let d be the index guaranteed by this claim and let CI = CI(d), CE = CE(d). Abusing notation, for two vectors v,w ∈ S, we will from now on refer to the color between v and w as the corresponding ‘color’ in CI or CE.

Let S′ = παd(S) and, for a vector v′ ∈ S′, let Tv′ = {v : παd(v) = v′, v ∈ S}. Note that the sets Tv′ form a partition of S. Therefore,

|Tv′| = |S|. (5)

v′∈S′

Let CB be the set of colors which appear within the set S′ under the coloring cp. Since S′ ⊂ {0,1}αd and αd < α, the inductive hypothesis implies that

|CB| ≥ |S′| − 1. (6)

For a color c ∈ CE, let µc be the number of (unordered) pairs of vectors v,w such that c is the color between v and w. Note that

µc =

v′∈S′

c∈CE

|Tv′| 2 ≥

(|Tv′| − 1). (7)

v′∈S′

Together with the three equations above, the following bound on |CI|, whose proof we defer for a moment, yields a contradiction.

|CI| ≥ |CB| +

(µc − 1). (8)

c∈CE

Indeed, if this inequality holds, then, by (8), (6) and (7), respectively, we have

 (|S′| − 1) +

|CI| + |CE| ≥

≥ (|S′| − 1) +

v′∈S′

(µc − 1)

 + |CE| = (|S′| − 1) +

µc

c∈CE

c∈CE

(|Tv′| − 1) =

|Tv′| − 1.

v′∈S′

By (5), we see that the right hand side is equal to |S|−1. Therefore, we obtain |CI|+|CE| ≥ |S|−1, which contradicts the assumption that |CI| + |CE| ≤ |S| − 2.

To prove (8), we examine the interaction between the three sets of colors CI, CB and CE. Note that each color c ∈ CI is of the form c = (c′,?) for some c′ ∈ CB, where the question mark ‘?’ stands for an unspeciﬁed coordinate. This fact already gives the trivial bound |CI| ≥ |CB|. To obtain (8), we improve this inequality by considering the ‘?’ part of the color and its relation to colors in CE. Take a color c′′ = {v′′,w′′} ∈ CE and suppose that c′′ has multiplicity µc′′ ≥ 2. Then there exist vectors x,y ∈ S′ such that (x,v′′),(x,w′′) ∈ Tx and (y,v′′),(y,w′′) ∈ Ty. Consider the color of the pairs (x,v′′),(y,v′′) and (x,v′′),(y,w′′) in CI. These colors are of the form

- cp(x,y),ηd−1(v′′,v′′) = (cp(x,y),0) ∈ CI and
- cp(x,y),ηd−1(v′′,w′′) = cp(x,y),ηd−1(c′′) ∈ CI.


Here we abuse notation and deﬁne ηd−1(c′′) = ηd−1(v′′,w′′), which is allowed since the right-handside is symmetric in the two input coordinates. Therefore, having a color c′′ with µc′′ ≥ 2 already implies that |CI| ≥ |CB| + 1. We carefully analyze the gain coming from these pairs for each color in CE. To this end, for each x ∈ S′, we deﬁne

CE,x = {v′′,w′′} : (x,v′′),(x,w′′) ∈ Tx, v′′ = w′′ .

For each c′ ∈ CB, we will count the number of colors of the form (c′,?) ∈ CI. There are two cases.

- Case 1 : For all x,y ∈ S′ with cp(x,y) = c′, CE,x ∩ CE,y = ∅. Apply the trivial bound asserting that there is at least one color of the form (c′,?) in CI.
- Case 2 : There exists a pair x,y ∈ S′ with cp(x,y) = c′ such that CE,x ∩ CE,y = ∅. If we have c′′ ∈ CE,x ∩ CE,y for some x,y ∈ S′ with cp(x,y) = c′, then, by the observation above, we have both (c′,0) and (c′,ηd−1(c′′)) in CI. This shows that the number of colors in CI of the form (c′,?) is at least


{(c′,0)} ∪ (c′,ηd−1(c′′)) : ∃x,y ∈ S′, cp(x,y) = c′, c′′ ∈ CE,x ∩ CE,y . By Claim 5.1, the function ηd−1 is injective on CE and thus the above number is equal to 1 + c′′ : ∃x,y ∈ S′, cp(x,y) = c′, c′′ ∈ CE,x ∩ CE,y .

By combining cases 1 and 2, we see that the number of colors in CI satisﬁes |CI| ≥ |CB| +

c′′ : ∃x,y ∈ S′, cp(x,y) = c′, c′′ ∈ CE,x ∩ CE,y

c′∈CB

c′ : ∃x,y ∈ S′, cp(x,y) = c′, c′′ ∈ CE,x ∩ CE,y .

= |CB| +

c′′∈CE

For a ﬁxed color c′′ ∈ CE, there are precisely µc′′ vectors x ∈ S′ for which the color c′′ is in CE,x. Hence, by the induction hypothesis, for each ﬁxed c′′, we have

c′ : ∃x,y ∈ S′, cp(x,y) = c′, c′′ ∈ CE,x ∩ CE,y ≥ µc′′ − 1. Thus we obtain

|CI| ≥ |CB| +

(µc′′ − 1),

c′′∈CE

which is (8).

## 5.1 Proof of Claim 5.1

- Claim 5.1 asserts that there exists an index d such that ηd−1(c) is distinct for each c ∈ CE(d).


It will be useful to consider the function hd, which is deﬁned as follows: for distinct vectors v and

- w, deﬁne hd(v,w) = {vi(d),wi(d)},


where vi(d),wi(d) are the ﬁrst pair of blocks of resolution d for which vi(d) = wi(d). Also, deﬁne hd(v,v) = 0 for all vectors v. Note that we can also deﬁne hd over unordered pairs {v,w} of vectors as hd({v,w}) = hd(v,w), since hd(v,w) = hd(w,v) for all pairs v and w. Throughout the subsection, by abusing notation, we will be applying hd to both ordered and unordered pairs without further explanation.

Recall that ηd(v,w) = (i,{vi(d),wi(d)}) and ηd(v,v) = 0 and, therefore, ηd reﬁnes hd (both considered as functions over the domain CE(d)). Hence, to prove the claim, it suﬃces to prove that hd−1(c) is distinct for each c ∈ CE(d). Another important observation is that for all 1 ≤ d ≤ p, we can redeﬁne the sets CE(d) as

CE(d) = hd(v,w) : παd(v) = παd(w), v = w, v,w ∈ S . We ﬁrst prove that there is a certain monotonicity between the sets CE(d) for 1 ≤ d ≤ p.

- Claim 5.2. For all d satisfying 2 ≤ d ≤ p, there exists an injective map d : CE(d−1) → CE(d) which maps {x,y} ∈ CE(d−1) to


d(x,y) = (v,x),(v,y) ∈ CE(d), for some vector v ∈ {0,1}αd−1−αd depending on the color {x,y}. Furthermore, hd−1 ◦ d is the identity map on CE(d−1).

Proof. Take a color {x,y} ∈ CE(d−1) and assume that {x,y} = hd−1(vx,vy) for vx,vy ∈ S. By the deﬁnition of CE(d−1), we may take vx and vy of the form

vx = (v0,x) and vy = (v0,y),

for some vector v0 ∈ {0,1}αd−1. Fix an arbitrary such pair (vx,vy) for each {x,y} ∈ CE(d−1). Let v0 = (v1,v2) for v1 ∈ {0,1}αd and v2 ∈ {0,1}αd−1−αd. Then vx = (v1,v2,x) and vy = (v1,v2,y). Since

παd(vx) = v1 = παd(vy), we see that

hd(vx,vy) = (v2,x),(v2,y) ∈ CE(d).

Deﬁne d(x,y) = hd(vx,vy) and note that the range of d is indeed CE(d). Moreover, since v2 is a vector of length αd−1 − αd which is divisible by rd−1, we see that

hd−1(d(x,y)) = hd−1 (v2,x),(v2,y) = {x,y}. The claim follows.

![image 32](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile32.png>)

![image 33](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile33.png>)

![image 34](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile34.png>)

![image 35](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile35.png>)

In particular, Claim 5.2 implies that

|CE(1)| ≤ |CE(2)| ≤ ··· ≤ |CE(p)|.

If |CE(1)| ≤ 1, then d = 1 trivially satisﬁes the required condition. Hence, we may assume that |CE(1)| ≥ 2. On the other hand, recall that we are assuming that |CI(p)| +|CE(p)| ≤ |S| − 2 ≤ p +1. If |CI(p)| = 0, then there exists at most one element vp ∈ παp(S) and all elements of S are of the form (vp,x) for some x ∈ {0,1}α−αp. But then

|S| 2 ≥ |S| − 1, (9)

|CE(p)| ≥

contradicting our assumption. Therefore, we may assume that |CI(p)| ≥ 1, from which it follows that |CE(p)| ≤ p. Hence,

2 ≤ |CE(1)| ≤ |CE(2)| ≤ ··· ≤ |CE(p)| ≤ p. If p = 1, this is impossible. If p ≥ 2, then, by the pigeonhole principle, there exists an index d such that |CE(d−1)| = |CE(d)|. For this index, the map d deﬁned in Claim 5.2 becomes a bijection. Then, since hd−1 ◦ d is the identity map on CE(d−1), we see that hd−1(c) are distinct for all c ∈ CE(d). This proves the claim.

# 6 Concluding Remarks

## 6.1 Better than (p + 3, p + 2)-coloring

![image 36](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile36.png>)

Let r = p+42 . We can in fact prove that cp is a (p + ⌊r⌋ + 1,p + ⌊r⌋)-coloring. This improvement comes from exploiting the slackness of the inequality (9) used in Subsection 5.1. To see this, we

![image 37](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile37.png>)

replace the bound on S by |S| ≤ p + r + 1 in the proof given above. Since we have already proved the result for |S| ≤ p + 3, we may assume that |S| ≥ p + 4.

If |CI(p)| ≥ r − 1, then we have

|CE(p)| ≤ |S| − 2 − |CI(p)| ≤ p

and we can proceed as in the proof above. We may therefore assume that |CI(p)| < r − 1. Let Sp = παp(S). Then, since

|Sp| − 1 ≤ |CI(p)| < r − 1, we know that |Sp| < r. Since

|πα−p1(v)| = |S|,

v∈Sp

there exists a v ∈ Sp such that |πα−p1(v)| ≥ ||SS|

p|. Note that every pair of vectors w1,w2 ∈ πα−p1(v) gives a distinct emerging color. Moreover, by the inductive hypothesis, we have at least |Sp| − 1

![image 38](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile38.png>)

inherited colors. Hence, the total number of colors in the coloring cp within the set S is at least

|Sp| − 1 + |πα−p1(v)| 2 ≥ |Sp| − 1 +

|S| |Sp|

|S| |Sp|

- 1

![image 39](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile39.png>)

- 2


− 1 ,

![image 40](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile40.png>)

![image 41](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile41.png>)

which, since

![image 42](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile42.png>)

![image 43](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile43.png>)

|S| 2

p + 4 2 ≤

|Sp| < r =

, is minimized when |Sp| is maximized. Thus the number of colors within the set S is at least |S| 2 − 1 + |S| −

![image 44](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile44.png>)

![image 45](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile45.png>)

![image 46](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile46.png>)

![image 47](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile47.png>)

|S| 2

= |S| − 1.

![image 48](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile48.png>)

![image 49](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile49.png>)

This concludes the proof.

- 6.2 Using fewer colors Recall that the coloring cp was built from the functions

ηd(v,w) = i,{vi(d),wi(d)} ,

where i is the minimum index for which vi(d) = wi(d). The function ηd can in fact be replaced by the function

hd(v,w) = vi(d),wi(d)

(note that this is the function used in Section 5.1). In other words, even if we replace all occurrences of ηd with hd in the deﬁnition of cp, we can still show that cp is a (p + 3,p + 2)-coloring. Moreover, there exists a constant ap such that the coloring of the complete graph on n vertices deﬁned in this way uses only

2ap(logn)1−1/(p+1) colors. That is, we gain a log log n factor in the exponent compared to Theorem 2.1. The tradeoﬀ is that the proof is now more complicated, the chief diﬃculty being to ﬁnd an appropriate analogue of Lemma 4.2 which works when ηd is replaced by hd.

- 6.3 Top-down approach


There is another way to understand our coloring as a generalization of Mubayi’s coloring. Recall that Mubayi’s coloring is given as follows: for two vectors v,w ∈ [m]t satisfying v = (v1,... ,vt) and w = (w1,... ,wt), let

c(v,w) = {vi,wi},a1,a2,... ,at , where i is the minimum index for which vi = wi and aj = 0 if vj = wj and aj = 1 if vj = wj.

Suppose that we are given positive integers t1 and t2. For two vectors v,w ∈ [m]t1t2, let v = (v1(1),... ,vt(1)2 ) and w = (w1(1),... ,wt(1)2 ) for vectors vi(1) ∈ [m]t1 and wi(1) ∈ [m]t1. Deﬁne the coloring c(2) as

c(2)(v,w) = {vi(1),wi(1)},c(v1(1),w1(1)),... ,c(vt(1)2 ,wt(1)2 ) ,

where i is the minimum index for which vi(1) = wi(1). Note that this can also be understood as a variant of c, where we record more information in the (a1,... ,at) part of the vector (this is a ‘top-down’ approach and the previous deﬁnition is a ‘bottom-up’ approach). The coloring c(2) is essentially equivalent to c2 deﬁned in Section 6.2 above and can be further generalized to give a coloring corresponding to cp for p ≥ 3. However, the proof again becomes more technical for this choice of deﬁnition.

One advantage of deﬁning the coloring using this top-down approach is that it becomes easier to see why the coloring cp on Kn2 contains the coloring cp on Kn1, where n1 < n2, as an induced coloring. To see this in the example above, suppose that n1 = mt1t2 and n2 = ns1s2 for m ≤ n, t1 ≤ s1 and t2 ≤ s2. Then the natural injection from [m] to [n] extends to an injection from [m]t1 to [n]s1 and then to an injection from [m]t1t2 to [n]s1s2. This injection shows that the coloring c(2) on Kn2 contains the coloring c(2) on Kn1 as an induced coloring. As in Section 2.1, it then follows that c(2) (and thus c2) fails to be a (q,qε)-coloring for large enough q. Similarly, for all ﬁxed p ≥ 3, we can show that cp fails to be a (q,qε)-coloring for large enough q.

## 6.4 Stronger properties

We can show (see [1]) that Mubayi’s coloring, discussed in Section 2.1, actually has the following stronger property: for every pair of colors, the graph whose edge set is the union of these two color classes has chromatic number at most three (previously, we only established the fact that the clique number is at most three). We suspect that this property can be generalized.

- Question 6.1. Let p ≥ 4 be an integer. Does there exist an edge-coloring of the complete graph


Kn with no(1) colors such that the union of every p− 1 color classes has chromatic number at most p?

We do not know whether our coloring has this property or not.

## 6.5 Lower bound

Some work has also been done on the lower bound for f(n,p,p − 1). As mentioned in the introduction, for p = 3 it is known that c′log loglognn ≤ f(n,3,2) ≤ clog n. For p = 4, the gap between the lower and upper bounds is much wider. The well-known bound rk(4) ≤ kck on the multicolor Ramsey number of K4 translates to f(n,4,3) ≥ clog loglognn, while Mubayi’s coloring gives an upper bound of f(n,4,3) ≤ ec

![image 50](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile50.png>)

![image 51](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile51.png>)

√logn. The lower bound has been improved, ﬁrst by Kostochka and Mubayi

![image 52](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile52.png>)

[7], to f(n,4,3) ≥ clog log loglogn n and then, by Fox and Sudakov [6], to f(n,4,3) ≥ clog n, which is the current best known bound.

![image 53](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile53.png>)

For p ≥ 5, we can obtain a similar lower bound from the following formula, valid for all p and q. f nf(n,p − 1,q − 1),p,q ≥ f(n,p − 1,q − 1). (10)

To prove this formula, put N = nf(n,p − 1,q − 1) and consider an edge-coloring of KN with fewer than f(n,p − 1,q − 1) colors. It suﬃces to show that there exists a set of p vertices which uses at most q −1 colors on its edges. If f(n,p−1,q −1) = 1, then the inequality above is trivially true. If

not, then for a ﬁxed vertex v, there exists a set V of at least f(n,p− N1−,q1−1)−1 ≥ n vertices adjacent to v by the same color. Since the edges within the set V are colored by fewer than f(n,p−1,q −1) colors, the deﬁnition of f(n,p − 1,q − 1) implies that we can ﬁnd a set X of p − 1 vertices with at most q − 2 colors used on its edges. It follows that the set X ∪ {v} is a set of p vertices with at most q − 1 colors used on its edges. The claim follows.

![image 54](<2014-conlon-erd-problem-generalized-ramsey_images/imageFile54.png>)

From (10) and the lower bound f(n,4,3) ≥ clog n, one can deduce that f(n,p,p − 1) ≥ (1 + o(1))f(n,4,3) ≥ (c + o(1))log n for all p ≥ 5. On the other hand, since the best known upper bound on f(n,p,p − 1) is f(n,p,p − 1) ≤ 216p(logn)1−1/(p−2) log logn,

the gap between the upper and lower bounds gets wider as p gets larger. It would be interesting to know whether either bound can be substantially improved. In particular, the following question seems important.

- Question 6.2. For p ≥ 5, can we give better lower bounds on f(n,p,p − 1) than the one which follows from f(n,4,3)?


# References

- [1] D. Conlon, J. Fox, C. Lee and B. Sudakov, On the grid Ramsey problem and related questions, in preparation.
- [2] D. Eichhorn and D. Mubayi, Edge-coloring cliques with many colors on subcliques, Combinatorica 20 (2000), 441–444.
- [3] P. Erd˝os, Problems and results on ﬁnite and inﬁnite graphs, in Recent advances in graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974), 183–192, Academia, Prague, 1975.
- [4] P. Erd˝os, Solved and unsolved problems in combinatorics and combinatorial number theory, in Proceedings of the Twelfth Southeastern Conference on Combinatorics, Graph Theory and Computing, Vol. I (Baton Rouge, La., 1981), Congr. Numer. 32 (1981), 49–62.


- [5] P. Erd˝os and A. Gy´arf´as, A variant of the classical Ramsey problem, Combinatorica 17 (1997), 459–467.
- [6] J. Fox and B. Sudakov, Ramsey-type problem for an almost monochromatic K4, SIAM J. Discrete Math. 23 (2008/09), 155–162.
- [7] A. Kostochka and D. Mubayi, When is an almost monochromatic K4 guaranteed? Combin. Probab. Comput. 17 (2008), 823–830.
- [8] D. Mubayi, Edge-coloring cliques with three colors on all 4-cliques, Combinatorica 18 (1998), 293–296.
- [9] J. Nesˇetrˇil and M. Rosenfeld, I. Schur, C. E. Shannon and Ramsey numbers, a short story, Discrete Math. 229 (2001), 185–195.
- [10] V. Rosta, Ramsey theory applications, Electron. J. Combin. 11 (2004), Research Paper 89, 48 pp.
- [11] G. N. Sa´rk¨ozy and S. M. Selkow, On edge colorings with at least q colors in every subset of p vertices, Electron. J. Combin. 8 (2001), Research Paper 9, 6pp.
- [12] G. N. Sa´rk¨ozy and S. M. Selkow, An application of the regularity lemma in generalized Ramsey theory, J. Graph Theory 44 (2003), 39–49.
- [13] I. Schur, Uber¨ die Kongruenz xm +ym = zm (mod p), Jber. Deutsch. Math.-Verein. 25 (1916), 114–116.


