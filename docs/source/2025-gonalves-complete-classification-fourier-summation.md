---
type: source
kind: paper
title: A Complete Classification of Fourier Summation Formulas on the real line
authors: Felipe Gonçalves, Guilherme Vedana
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2504.02741v1
source_local: ../raw/2025-gonalves-complete-classification-fourier-summation.pdf
topic: general-knowledge
cites:
---

arXiv:2504.02741v1[math.CA]3Apr2025

A COMPLETE CLASSIFICATION OF FOURIER SUMMATION FORMULAS ON THE REAL LINE

FELIPE GONC¸ALVES AND GUILHERME VEDANA

Abstract. We completely classify Fourier summation formulas of the form ż

ÿ8

ϕpptqdµptq “

apλnqϕpλnq,

R

n“0

that hold for any test function ϕ, where ϕp is the Fourier transform of ϕ, µ is a ﬁxed complex measure on R and a : tλnuně0 Ñ C is a ﬁxed function. We only assume the decay condition ż

` ÿ

d|µ|ptq p1 ` t2qc1

|apλnq|e´c

2|λn| ă 8,

![image 1](<2025-gonalves-complete-classification-fourier-summation_images/imageFile1.png>)

R

ně0

for some c1,c2 ą 0. This completes the work initiated by the ﬁrst author previously, where the condition c1 ď 1 was required. We prove that any such pair pµ,aq can be uniquely associated with a holomorphic map Fpzq in the upper-half space that is both almost periodic and belongs to a certain higher index Nevanlinna class. The converse is also true: For any such function F it is possible to generate a Fourier summation pair pµ,aq. We provide important examples of such summation formulas not contemplated by the previous results, such as Selberg’s trace formula.

1. Introduction

Fourier Summation pairs (FS-pairs, for short) play a key role in the study of several questions in Number Theory, from geometry of numbers to analytic number theory. The importance of such formulas relies on the fact that they establish a critical relation between two important quantities: Phase and frequency information. The probably most well-known example of a FS-pair is given by the Poisson Summation formula

ϕpvq “ ÿ

ÿ

ϕppuq,

uPZ

vPZ

that holds for any test1 function ϕ. Throughout this paper we use the following normalization of the Fourier transform

fppξq “ ż

fpxqe´2πix¨ξdx.

Rd

Poisson summation and its higher dimensional versions is a fundamental tool in Number Theory, with countless applications. A FS-pair is a generalization of the Poisson Summation formula: It is a pair pµ, aq, where µ is a complex measure on R and a : R Ñ C is a function with countable support, such that

ż

ÿ8

ϕpptqdµptq “

apλnqϕpλnq (1)

R

n“0

holds for any test function ϕ, where tλnu8n“0 “ supppaq is some enumeration of the support of ap¨q.

![image 2](<2025-gonalves-complete-classification-fourier-summation_images/imageFile2.png>)

Date: April 4, 2025. 1In this paper, a test function ϕ : R Ñ C is always C8 and compactly supported.

There are plenty of examples of FS-pairs in Number Theory. The Guinand-Weil explicit formula (see, for instance, [24, Thm. 12.13]) and, more generally, the Selberg Trace formula (see [4, Thm. 5.6]), all generate FS-pairs. Furthermore, the recent RadchenkoViazovska interpolation formulas in [30] can also be seen as FS-pairs (see also [28, 19]). For a more recent account of diﬀerent kinds of FS-pairs see the last section in [14] (see also Section 6). These summation formulas also appear in Physics. The special class where the support of both µ and ap¨q are locally ﬁnite, which is called a crystalline pair, is used in Crystallography for the reconstruction of the atomic structure of crystals. If the structure of the crystal is represented by a measure µ (this is unknown, a priori), then diﬀraction experiments provide the values of |a|2 from which one can numerically recover µ. Therefore, a complete characterization of the crystalline pairs (and more generaliy FS-pairs) can be a useful tool.

The main objective of this paper is to ﬁnish the classiﬁcation initiated by the ﬁrst named author in [14], where formulas of the type (1) were classiﬁed under the assumption that

şRp1 ` t2q´1d|µ|ptq ă 8. Here, we found a way to circumvent the issues in [14] and allow any polynomial growth for µ, that is, we only require that

şRp1 ` t2q´cd|µ|ptq ă 8 for some c ą 0. The results of this paper are heavily inspired and motivated by recent work in the ﬁeld, such as: The new summation formulas produced by Radchenko and Viazovska [30], Bondarenko, Radchenko and Seip [7], Kurasov and Sarnak [18], Kulikov, Nazarov and Sodin [19] and Ramos and Sousa [28, 29]; The recent results on Lee-Yang polynomials of Alon, Cohen and Vinzant [1, 2]; The classiﬁcation of crystalline pairs of Lev and Olevskii [20, 21] and Olevskii and Ulanovskii [25].

2. Main results

In order to state our main results we will need some preparatory deﬁnitions. We follow the notation in [14] closely. We say that a complex-valued Borel measure µ on R is strongly tempered if

degpµq :“ inf "n P Z; ż

ă 8* ă 8.

d|µ|ptq p1 ` t2qn{2

![image 3](<2025-gonalves-complete-classification-fourier-summation_images/imageFile3.png>)

R

In this case, the map ϕ P SpRq ÞÑ şR ϕptqdµptq deﬁnes a tempered distribution. A function a : R Ñ C is called locally summable if its support supppaq :“ tλ P R; apλq ‰ 0u is

countable, and for some (and hence for all) enumeration supppaq “ tλn; n ě 0u, the sum ÿ

|apλnq| ă 8

ně0; λnPr´T,Ts

for any T ą 0. In addition, we say that ap¨q has ﬁnite exponential growth if ÿ

|apλnq|e´c|λ

n| ă 8,

ně0

ř

for some c ą 0. In particular the sum

λPR apλqϕpλq is well-deﬁned for any function ϕ such that |ϕpλq| À e´c|λ| (for instance if ϕ is a test function). At this point we are able to deﬁne what a Fourier summation pair is.

Deﬁnition 1 (Fourier summation pair). A Fourier summation pair (FS-pair) is a pair pµ, aq, where µ is a strongly tempered measure on R, a : R Ñ C is a locally summable function, such that

ż

ϕpptqdµptq “ ÿ

apλqϕpλq (2)

R

λPR

holds for any test function ϕ. In view of this deﬁnition, the decay condition ż

` ÿ

d|µ|ptq p1 ` t2qc

|apλnq|e´c

2|λn| ă 8,

![image 4](<2025-gonalves-complete-classification-fourier-summation_images/imageFile4.png>)

1

R

ně0

for some c1, c2 ą 0, seems to be the most weak assumption one can impose. In other words, that µ has ﬁnite degree and ap¨q has ﬁnite exponential growth. Moreover, to the best of our knowledge, we are unaware of any summation formula as (2) that holds for every smooth compactly supported function ϕ, but does not satisfy the above decay condition. This is the only decay condition our main result Theorem 1 is going to assume, which makes it quite general.

In order to avoid technicalities, we will state our results for FS-pairs pµ, aq for which µ is a real measure. This implies automatically that ap´λq “ apλq for any λ, a property that we call antipodal and the pair pµ, aq is then called real-antipodal. Given any FS-pair pµ, aq, we can split it into two real-antipodal FS-pairs pµ1, a1q and pµ2, a2q by deﬁning µ1 “ Repµq, µ2 “ ´Impµq, a1pλq :“ papλq ` ap´λqq{2 and a2pλq :“ ´ipap´λq ´ apλqq{2, so that a “ a1 ´ ia2.

![image 5](<2025-gonalves-complete-classification-fourier-summation_images/imageFile5.png>)

![image 6](<2025-gonalves-complete-classification-fourier-summation_images/imageFile6.png>)

![image 7](<2025-gonalves-complete-classification-fourier-summation_images/imageFile7.png>)

Almost Periodic Class. Let C` :“ tz P C; Impzq ą 0u be the complex upper-half plane. A holomorphic map Fpzq deﬁned on C` is said to be almost periodic if, for any 0 ă α ă β ă 8 and ε ą 0, there exists a relatively dense2 set of translations τ Ă R, which may depend on α, β and ε, such that

|Fpz ` tq ´ Fpzq| ď ε, for any t P τ.

sup

αăIm pzqăβ

We denote this class of almost periodic functions by APpC`q. In this case we can deﬁne an analogous of a Fourier coeﬃcient for Fpzq: For any λ P R, the limit

ż T`iy

- 1

![image 8](<2025-gonalves-complete-classification-fourier-summation_images/imageFile8.png>)

- 2T


Fpzqe´2πiλzdz

EFpλq :“ lim

TÑ8

´T`iy

does exist and does not depend on y ą 0. In particular, if Fpz ` icq is almost periodic, then the above limit exists and is independent of y ą c. If Fpz ` icq P APpC`q, its spectrum is deﬁned by

specpFq :“ tλ P R; EFpλq ‰ 0u,

and it is a countable set. For more information about almost periodic functions, see for instance [5, 6, 14].

The Nevanlinna Class. The higher order holomorphic Nevanlinna class Nďk is deﬁned as the set of all holomorphic maps F : C` Ñ C such that for any choice of z1, ..., zN P C`, the Hermitian matrix

ﬀ

«i

![image 9](<2025-gonalves-complete-classification-fourier-summation_images/imageFile9.png>)

Fpznq ` Fpzmq zn ´ zm

![image 10](<2025-gonalves-complete-classification-fourier-summation_images/imageFile10.png>)

![image 11](<2025-gonalves-complete-classification-fourier-summation_images/imageFile11.png>)

1ďn,mďN

has at most k negative eigenvalues (counting multiplicities). We deﬁne

Nďk ´ Nďk :“ tF ´ G; F, G P Nďku. For more information, see Section 3.

![image 12](<2025-gonalves-complete-classification-fourier-summation_images/imageFile12.png>)

2This means that there exists l ą 0 such that τ X px,x ` lq ‰ H for any x P R.

The following is the main result of this paper. It states that if we have a FS-pair pµ, aq, then we can associate a holomorphic function Fpzq in C` that is at the same time almost periodic and belongs to the class Nďk ´ Nďk. This function Fpzq encapsulates the information contained in the pair pµ, aq by having the coeﬃcients of its “Fourier series” given by the function ap¨q and µ is the measure from its Nevanlinna factorization. The converse is also true: starting from any such function Fpzq, it is possible to build a FS-pair. In short, the results in the paper answer the following question:

What is a FS-pair? It is a function in the following class ˆ ď

APpC` ` icq˙.

pNďk ´ Nďkq˙ X ˆ ď

cPR`

kPZ`

- Theorem 1 (Classiﬁcation of FS-pairs). Let pµ, aq be a real-antipodal FS-pair such that ap¨q has ﬁnite exponential growth and that degpµq ď 2pk ` 1q. Then, to the pair pµ, aq corresponds a unique holomorphic map Fpzq in C` which satisﬁes the following properties:


- (I) Fpzq P Nďk ´ Nďk;
- (II) Fp¨ ` ic1q P APpC`q for some c1 ą 0;
- (III) λ ÞÑ EFpλq is a function of ﬁnite exponential growth, this is,


ř

2|λ| ă 8, for some c2 ą 0.

λPR |EFpλq|e´c

This function F is given by the following identities Fpzq “

ż

ap0q ` ÿ

pz2 ` 1qk 2πi

dµptq p1 ` t2qk`1

1 ` tz t ´ z ¨

- 1

![image 13](<2025-gonalves-complete-classification-fourier-summation_images/imageFile13.png>)

- 2


apλqe2πiλz, (3)

` iQpzq “

![image 14](<2025-gonalves-complete-classification-fourier-summation_images/imageFile14.png>)

![image 15](<2025-gonalves-complete-classification-fourier-summation_images/imageFile15.png>)

![image 16](<2025-gonalves-complete-classification-fourier-summation_images/imageFile16.png>)

R

λą0

where Qpzq is a real polynomial of degree ď 2k. The ﬁrst identity above holds for all z P C`, while the second only if Imz ą c1. Both expressions converge absolutely in these domains.

Conversely, if Fpzq is a holomorphic map in C` satisfying properties (I),(II) and (III), then we can construct a real-antipodal FS-pair pµ, aq where ap¨q has ﬁnite exponential growth and degpµq ď 2pk ` 1q. More precisely, there exists c1 ą 0 such that the limit

ż T`iy

- 1

![image 17](<2025-gonalves-complete-classification-fourier-summation_images/imageFile17.png>)

- 2T


Fpzqe´2πiλzdz

EFpλq :“ lim

TÑ8

´T`iy

does exist for all λ P R and y ą c1, and does not depend on y. Moreover, the function λ ÞÑ EFpλq vanishes for λ ă 0 and has ﬁnite exponential growth. The function ap¨q is deﬁned by

$ ’&

EFpλq if λ ą 0, 2ReEFp0q if λ “ 0, EFp´λq if λ ă 0.

apλq :“

’%

![image 18](<2025-gonalves-complete-classification-fourier-summation_images/imageFile18.png>)

The measure µ is the unique real-valued measure coming from the Nevanlinna factorization (5) of Fpzq.

The polynomial Q is uniquely deﬁned by identity (3) and it has degree 2k (and not 2k ` 1 as in (5)) since

ż

Fpiyq ´ iQpiyq yp1 ´ y2qk

dµptq 2πpy2 ` t2qp1 ` t2qk

“ lim

“ 0,

lim

Re

![image 19](<2025-gonalves-complete-classification-fourier-summation_images/imageFile19.png>)

![image 20](<2025-gonalves-complete-classification-fourier-summation_images/imageFile20.png>)

yÑ8

yÑ8

R

and Fpiyq Ñ 21ap0q as y Ñ 8.

![image 21](<2025-gonalves-complete-classification-fourier-summation_images/imageFile21.png>)

Regarding the converse, it turns out that we can weaken the assumption of ﬁnite exponential growth of the Fourier coeﬃcients EFpλq (property (III)) and just require

local summability. In this case we can also construct a FS-pair pµ, aq, though now the function ap¨q is no longer necessarily of ﬁnite exponential growth.

- Theorem 2. Let F P Nďk ´ Nďk be such that Fp¨ ` icq P APpC`q for some c ą 0 and assume that the function λ P R ÞÑ EFpλq is locally summable. Then one can associate a real-antipodal FS-pair pµ, aq exactly as in Theorem 1, except now that ap¨q is only locally summable.


3. The Nevanlinna class

All facts described in this section can be found in [9, 16, 17]. The Nevanlinna class of index k “ 0 is the set of all holomorphic maps F : C` Ñ C such that ReFpzq ě 0 for any z P C`. It can be shown that this is equivalent to F having the following Poisson representation [10, Thm 4]

ż

dµptq 1 ` t2

1 ` tz t ´ z ¨

- 1

![image 22](<2025-gonalves-complete-classification-fourier-summation_images/imageFile22.png>)

- 2πi


Fpzq “ iQpzq `

,

![image 23](<2025-gonalves-complete-classification-fourier-summation_images/imageFile23.png>)

![image 24](<2025-gonalves-complete-classification-fourier-summation_images/imageFile24.png>)

R

where µ is a nonnegative Borel measure on R of degree degpµq ď 2 and Qpzq “ a ` bz with b ď 0. The (generalized) Nevanlinna class of index ď k is deﬁned as the set of all meromorphic maps F : C` Ñ C such that, for any choice z1, ..., zN P C`, the matrix

«i

ﬀ

![image 25](<2025-gonalves-complete-classification-fourier-summation_images/imageFile25.png>)

Fpznq ` Fpzmq zn ´ zm

![image 26](<2025-gonalves-complete-classification-fourier-summation_images/imageFile26.png>)

![image 27](<2025-gonalves-complete-classification-fourier-summation_images/imageFile27.png>)

1ďn,mďN

has at most k negative eigenvalues. The next proposition is a restatement of [9, Prop. 2.1] for the holomorphic scalar case (see also [8, eq. (4)])

Proposition 3. Let F : C` Ñ C be a holomorphic function in the generalized Nevanlinna class of index ď k. Then it is possible to write

ż

pz2 ` 1qm 2πi

tz ` 1 t ´ z ¨

dµptq p1 ` t2qm`1

` iQpzq, (4)

Fpzq “

![image 28](<2025-gonalves-complete-classification-fourier-summation_images/imageFile28.png>)

![image 29](<2025-gonalves-complete-classification-fourier-summation_images/imageFile29.png>)

![image 30](<2025-gonalves-complete-classification-fourier-summation_images/imageFile30.png>)

R

where µ is a nonnegative Borel measure on R such that degpµq ď 2pm ` 1qand Qpzq “ a2m`1z2m`1 ` ... ` a1z ` a0 is a real polynomial of degree ď 2m ` 1 such that a2m`1 ď 0. Conversely, any function deﬁned by (4) with m ď k (and the same constraints on µ and Q) deﬁnes a holomorphic function in the generalized Nevanlinna class of index ď k.

We denote the above class by Nďk. Moreover, in order to account for the cases in which µ is a signed measure, we also consider the class Nďk ´Nďk :“ tF ´G; F, G P Nďku. We can then apply Proposition 3 to obtain that F P Nďk ´ Nďk if and only if

ż

pz2 ` 1qm 2πi

tz ` 1 t ´ z ¨

dµptq p1 ` t2qm`1

Fpzq “

` iQpzq, (5)

![image 31](<2025-gonalves-complete-classification-fourier-summation_images/imageFile31.png>)

![image 32](<2025-gonalves-complete-classification-fourier-summation_images/imageFile32.png>)

![image 33](<2025-gonalves-complete-classification-fourier-summation_images/imageFile33.png>)

R

for m ď k, a signed measure µ with degpµq ď 2pm ` 1q, and Qpzq, a real polynomial of degree at most 2m ` 1.

We now make some few remarks about the class Nďk ´ Nďk. Firstly, we note that F P N0 ´N0 if and only if one can write eF “ P{Q, where P and Q are holomorphic and bounded by 1 in C` (this is the Bounded Type class used in [14], see also [10, Thm. 9]). Secondly, we note that Q is uniquely deﬁned in terms of F. Indeed, we have

Fpiyq ´ iQpiyq p1 ´ y2qmy “ ż

dµptq p1 ` t2qm

1 y2 ` t2

Ñ 0

Re

![image 34](<2025-gonalves-complete-classification-fourier-summation_images/imageFile34.png>)

![image 35](<2025-gonalves-complete-classification-fourier-summation_images/imageFile35.png>)

![image 36](<2025-gonalves-complete-classification-fourier-summation_images/imageFile36.png>)

R

as y Ñ 8, and since Q has degree at most 2m ` 1, we conclude that lim

y´2m´1ReFpiyq “ p´1qm`1a2m`1.

yÑ8

Moreover, since pFpzq ´ iQpzqq{pz2 ` 1qm is holomorphic and Q can only have real coefﬁcients, we must have

Qpzq “ ´ipz2 ` 1qmpRp1{pz ´ iqq ´ R˚p1{pz ` iqq ` a2m`1zpz2 ` 1qm where Rp1{pz ´ iqq is the singular part of the Laurent expansion of Fpzq{pz2 ` 1qm at z “ i. To see this, ﬁrst observe there always exist a polynomial R of degree at most m such that we can write Q in above form. If we momentarily let Singr¨s be the singular part of a given function at z “ i, we obtain

0 “ SingrpFpzq ´ iQpzqq{pz2 ` 1qms “ SingrFpzq{pz2 ` 1qm ´ Rp1{pz ´ iqqs. Thirdly, µ is also uniquely determined by F since a routine argument shows that

Re ż b`is

dz “ ż b

- 1

![image 37](<2025-gonalves-complete-classification-fourier-summation_images/imageFile37.png>)

- 2dµptq


Fpzq ´ iQpzq pz2 ` 1qk

lim

,

![image 38](<2025-gonalves-complete-classification-fourier-summation_images/imageFile38.png>)

![image 39](<2025-gonalves-complete-classification-fourier-summation_images/imageFile39.png>)

p1 ` t2qk`1

sŒ0

a`is

a

whenever a ă b are points of continuity of µ. Finally, we note that (and this is going to be extremely useful later on), whenever (5) holds, then for any y0 ą 0 we also have the representation

ż

tz ` y02 t ´ z ¨

pz2 ` y02qm 2πi

dµptq py02 ` t2qm`1

0pzq, (6) where Qy

` iQy

Fpzq “

![image 40](<2025-gonalves-complete-classification-fourier-summation_images/imageFile40.png>)

![image 41](<2025-gonalves-complete-classification-fourier-summation_images/imageFile41.png>)

![image 42](<2025-gonalves-complete-classification-fourier-summation_images/imageFile42.png>)

R

0p1{pz ´ iy0qq ` R˚

y0p1{pz ` iy0qq ` a2m`1zpz2 ` y02qm and Ry

0pzq “ pz2 ` y02qmpRy

0p1{pz ´ iy0qq is the singular part of Fpzq{pz2 ` y02qm at z “ iy0. The form of Qy

can be derived (as before) by similar considerations from the above integral identity. Hence, to show the above identity holds true, it is enough to prove that if we let Frpzq denote the holomorphic function on the right hand side of (6) then Ppzq :“ ipFpzq ´ Frpzqq is a real polynomial of degree at most 2m ` 1. To this end we make use of the identity

0

ˆ

˙j ´

mÿ´1

pz2 ` r2qmpr2 ` tzq pr2 ` t2qm`1pt ´ zq

z2 ` r2 r2 ` t2

tpr2 ` z2qm pr2 ` t2qm`1

t ` z r2 ` t2

1 t ´ z ´

“

.

![image 43](<2025-gonalves-complete-classification-fourier-summation_images/imageFile43.png>)

![image 44](<2025-gonalves-complete-classification-fourier-summation_images/imageFile44.png>)

![image 45](<2025-gonalves-complete-classification-fourier-summation_images/imageFile45.png>)

![image 46](<2025-gonalves-complete-classification-fourier-summation_images/imageFile46.png>)

![image 47](<2025-gonalves-complete-classification-fourier-summation_images/imageFile47.png>)

j“0

Taking the diﬀerence of two such identities for r “ 1 and r “ y0, we conclude that Ppzq “ ipFpzq ´ Frpzqq extends to an real entire function.

Similarly, limyÑ8 y´2m´1Frpiyq also exists. Since both F and Fr are of Bounded Type3 in C`, a classical result of Krein [10, Prob. 37] shows that F ´ Fr must have ﬁnite exponential type. However, since |Ppiyq| “ Op|y|2m`1q, we conclude that P must be a real polynomial of degree at most 2m ` 1.

4. Preliminaries

In order to prove the main theorem, we follow an analogous of the strategy used in [14]. We begin by deﬁning some auxiliary functions. For z, w P C`, x P R and k P Z` we deﬁne

e´2πiw|x|1xă0 ` e2πiz|x|1xě0 z ´ w

![image 48](<2025-gonalves-complete-classification-fourier-summation_images/imageFile48.png>)

G0pw, z, xq :“

![image 49](<2025-gonalves-complete-classification-fourier-summation_images/imageFile49.png>)

![image 50](<2025-gonalves-complete-classification-fourier-summation_images/imageFile50.png>)

![image 51](<2025-gonalves-complete-classification-fourier-summation_images/imageFile51.png>)

3Functions of bounded type in C` form an algebra that contains polynomials and functions with nonnegative real part, hence F and Fr are of Bounded Type.

Akpxq :“ e´2π|¨| ˚ ¨¨¨ ˚ e´2π|¨|pxq

![image 52](<2025-gonalves-complete-classification-fourier-summation_images/imageFile52.png>)

![image 53](<2025-gonalves-complete-classification-fourier-summation_images/imageFile53.png>)

![image 54](<2025-gonalves-complete-classification-fourier-summation_images/imageFile54.png>)

k-times

Gkpw, z, xq :“ G0pw, z, ¨q ˚ Akpxq pk ě 1q.

- Lemma 4 (Properties of auxiliary functions). The above functions have the following properties


- (i) We have Gxkpw, z, tq “

- 1

![image 55](<2025-gonalves-complete-classification-fourier-summation_images/imageFile55.png>)

- 2πk`1i ¨


1 pt ´ zqpt ´ wq

![image 56](<2025-gonalves-complete-classification-fourier-summation_images/imageFile56.png>)

![image 57](<2025-gonalves-complete-classification-fourier-summation_images/imageFile57.png>)

¨

1 p1 ` t2qk

![image 58](<2025-gonalves-complete-classification-fourier-summation_images/imageFile58.png>)

; where the Fourier transform is taken in the last variable.

- (ii) There exist polynomials rk P QrXs of degree exactly k such that Akpxq “ e´2π|x|π1´krk´1p2π|x|q.

These polynomials have the following generating series ÿ

kě0

qkrkpXq “

ep1´

?1´qqX

![image 59](<2025-gonalves-complete-classification-fourier-summation_images/imageFile59.png>)

![image 60](<2025-gonalves-complete-classification-fourier-summation_images/imageFile60.png>)

?1 ´ q “ 1 ` ˆ

![image 61](<2025-gonalves-complete-classification-fourier-summation_images/imageFile61.png>)

- 1

![image 62](<2025-gonalves-complete-classification-fourier-summation_images/imageFile62.png>)

- 2


X ` 1˙q ` ˆ

1 8

![image 63](<2025-gonalves-complete-classification-fourier-summation_images/imageFile63.png>)

X2 `

5 8

![image 64](<2025-gonalves-complete-classification-fourier-summation_images/imageFile64.png>)

X ` 1˙q2 ` Opq3q,

which converges absolutely for |q| ă 1 and X P R;

- (iii) For λ ě 0 we have Gkpw, z, ´λq “ ´Gkpz, w, λq, and if we write pk´1pxq :“

![image 65](<2025-gonalves-complete-classification-fourier-summation_images/imageFile65.png>)

π1´krk´1p2πxq “ řk´1

j“0 bk´1,jxj, then

pz ´ wqGkpw, z, λq “ e´2πλ

![image 66](<2025-gonalves-complete-classification-fourier-summation_images/imageFile66.png>)

kÿ´1

j“0

j!bk´1,j p2πqj`1p1 ` iwqj`1

![image 67](<2025-gonalves-complete-classification-fourier-summation_images/imageFile67.png>)

![image 68](<2025-gonalves-complete-classification-fourier-summation_images/imageFile68.png>)

ÿj

l“0

p2πλqlp1 ` iwql l!

![image 69](<2025-gonalves-complete-classification-fourier-summation_images/imageFile69.png>)

![image 70](<2025-gonalves-complete-classification-fourier-summation_images/imageFile70.png>)

´ e´2πλ

kÿ´1

j“0

j!bk´1,j p2πqj`1p1 ` izqj`1

![image 71](<2025-gonalves-complete-classification-fourier-summation_images/imageFile71.png>)

ÿj

l“0

p2πλqlp1 ` izql l!

![image 72](<2025-gonalves-complete-classification-fourier-summation_images/imageFile72.png>)

` e2πiλz

kÿ´1

j“0

j!bk´1,j p2πqj`1

![image 73](<2025-gonalves-complete-classification-fourier-summation_images/imageFile73.png>)

„

1 p1 ` izqj`1

![image 74](<2025-gonalves-complete-classification-fourier-summation_images/imageFile74.png>)

`

1 p1 ´ izqj`1

![image 75](<2025-gonalves-complete-classification-fourier-summation_images/imageFile75.png>)

.

If z “ i one should take the limit in the above expression. Moreover, for ﬁxed w P C`, the map z P C` ÞÑ Gkpw, z, λq is holomorphic. The same is true in the variable w if we ﬁx z.

- (iv) For z ‰ ˘i: kÿ´1


„

 “

j!bk´1,j p2πqj`1

1 πk ¨

1 p1 ´ izqj`1

1 p1 ` z2qk

1 p1 ` izqj`1

`

.

![image 76](<2025-gonalves-complete-classification-fourier-summation_images/imageFile76.png>)

![image 77](<2025-gonalves-complete-classification-fourier-summation_images/imageFile77.png>)

![image 78](<2025-gonalves-complete-classification-fourier-summation_images/imageFile78.png>)

![image 79](<2025-gonalves-complete-classification-fourier-summation_images/imageFile79.png>)

![image 80](<2025-gonalves-complete-classification-fourier-summation_images/imageFile80.png>)

j“0

Hence, for z ‰ i, we can write

ÿj

kÿ´1

p2πλqlp1 ` iwql l!

j!bk´1,j p2πqj`1p1 ` iwqj`1

![image 81](<2025-gonalves-complete-classification-fourier-summation_images/imageFile81.png>)

pz ´ wqGkpw, z, λq “ e´2πλ

![image 82](<2025-gonalves-complete-classification-fourier-summation_images/imageFile82.png>)

![image 83](<2025-gonalves-complete-classification-fourier-summation_images/imageFile83.png>)

![image 84](<2025-gonalves-complete-classification-fourier-summation_images/imageFile84.png>)

![image 85](<2025-gonalves-complete-classification-fourier-summation_images/imageFile85.png>)

j“0

l“0

kÿ´1

ÿj

p2πλqlp1 ` izql l! ` e2πiλz ¨

j!bk´1,j p2πqj`1p1 ` izqj`1

´ e´2πλ

![image 86](<2025-gonalves-complete-classification-fourier-summation_images/imageFile86.png>)

![image 87](<2025-gonalves-complete-classification-fourier-summation_images/imageFile87.png>)

j“0

l“0

1 p1 ` z2qk

1 πk ¨

.

![image 88](<2025-gonalves-complete-classification-fourier-summation_images/imageFile88.png>)

![image 89](<2025-gonalves-complete-classification-fourier-summation_images/imageFile89.png>)

Proof. For item (i), a simple computation yields Gx0pw, z, tq “

1 2πipt ´ zqpt ´ wq

.

![image 90](<2025-gonalves-complete-classification-fourier-summation_images/imageFile90.png>)

![image 91](<2025-gonalves-complete-classification-fourier-summation_images/imageFile91.png>)

Since e{´2π|¨|ptq “ πp1`1 t2q, the assertion follows. For item (ii) we have ÿ

![image 92](<2025-gonalves-complete-classification-fourier-summation_images/imageFile92.png>)

qk´1Axkpξq “ ÿ

qk´1 πkp1 ` ξ2qk

1 πp1 ` ξ2q ´ q “

1 πpa1 ´ q{π2 ` ξ2q

“

.

![image 93](<2025-gonalves-complete-classification-fourier-summation_images/imageFile93.png>)

![image 94](<2025-gonalves-complete-classification-fourier-summation_images/imageFile94.png>)

![image 95](<2025-gonalves-complete-classification-fourier-summation_images/imageFile95.png>)

![image 96](<2025-gonalves-complete-classification-fourier-summation_images/imageFile96.png>)

kě1

kě1

By Fourier inversion we obtain ÿ

?

![image 97](<2025-gonalves-complete-classification-fourier-summation_images/imageFile97.png>)

e´2π

1´q{π|x|

qk´1Akp|x|q “

a1 ´ q{π

.

![image 98](<2025-gonalves-complete-classification-fourier-summation_images/imageFile98.png>)

![image 99](<2025-gonalves-complete-classification-fourier-summation_images/imageFile99.png>)

kě1

Setting X “ 2πx and replacing q{π by q we derive the desired assertion. For item (iii), using that Akpxq “ e´2π|x|pk´1p|x|q we have

Gkpw, z, λq “ ˆż ´λ

˙

` ż 0

` ż 8

e´2πiw|λ`t|1p´8,0qpλ ` tq ` e2πiz|λ`t|1r0,8qpλ ` tq z ´ w

![image 100](<2025-gonalves-complete-classification-fourier-summation_images/imageFile100.png>)

Akptqdt “ I1 ` I2 ` I3.

![image 101](<2025-gonalves-complete-classification-fourier-summation_images/imageFile101.png>)

![image 102](<2025-gonalves-complete-classification-fourier-summation_images/imageFile102.png>)

´8

´λ

0

A simple computation yields

p´1qjbjk´1 ż ´λ

kÿ´1

e2πiλw z ´ w

![image 103](<2025-gonalves-complete-classification-fourier-summation_images/imageFile103.png>)

tje2πtp1`iwqdt

![image 104](<2025-gonalves-complete-classification-fourier-summation_images/imageFile104.png>)

I1 “ I1pw, zq “

![image 105](<2025-gonalves-complete-classification-fourier-summation_images/imageFile105.png>)

![image 106](<2025-gonalves-complete-classification-fourier-summation_images/imageFile106.png>)

´8

j“0

kÿ´1

ÿj

e´2πλ z ´ w

p2πλqlp1 ` iwql l!

j!bk´1,j p2πqj`1p1 ` iwqj`1

![image 107](<2025-gonalves-complete-classification-fourier-summation_images/imageFile107.png>)

“

,

![image 108](<2025-gonalves-complete-classification-fourier-summation_images/imageFile108.png>)

![image 109](<2025-gonalves-complete-classification-fourier-summation_images/imageFile109.png>)

![image 110](<2025-gonalves-complete-classification-fourier-summation_images/imageFile110.png>)

![image 111](<2025-gonalves-complete-classification-fourier-summation_images/imageFile111.png>)

![image 112](<2025-gonalves-complete-classification-fourier-summation_images/imageFile112.png>)

j“0

l“0

bk´1,jp´1qj ż 0

kÿ´1

e2πiλz z ´ w

tje2πtp1`izqdt

I2 “ I2pw, zq “

![image 113](<2025-gonalves-complete-classification-fourier-summation_images/imageFile113.png>)

![image 114](<2025-gonalves-complete-classification-fourier-summation_images/imageFile114.png>)

´λ

j“0

#

+

ÿj

kÿ´1

kÿ´1

p2πλqlp1 ` izql l! ` e2πiλz

j!bk´1,j p2πqj`1p1 ` izqj`1

j!bk´1,j p2πqj`1

1 p1 ` izqj`1

1 z ´ w

´e´2πλ

¨

“

![image 115](<2025-gonalves-complete-classification-fourier-summation_images/imageFile115.png>)

![image 116](<2025-gonalves-complete-classification-fourier-summation_images/imageFile116.png>)

![image 117](<2025-gonalves-complete-classification-fourier-summation_images/imageFile117.png>)

![image 118](<2025-gonalves-complete-classification-fourier-summation_images/imageFile118.png>)

![image 119](<2025-gonalves-complete-classification-fourier-summation_images/imageFile119.png>)

![image 120](<2025-gonalves-complete-classification-fourier-summation_images/imageFile120.png>)

j“0

j“0

l“0

and if z “ i, then

kÿ´1

e´2πλ i ´ w

bk´1,jλj`1 j ` 1

I2 “

.

![image 121](<2025-gonalves-complete-classification-fourier-summation_images/imageFile121.png>)

![image 122](<2025-gonalves-complete-classification-fourier-summation_images/imageFile122.png>)

![image 123](<2025-gonalves-complete-classification-fourier-summation_images/imageFile123.png>)

j“0

Note that I2 “ I2pw, zq is a holomorphic function of z P C` by dominated convergence and Morera’s Theorems. In particular it has no pole at z “ i. Routine computations also show that

bk´1,j ż 8

kÿ´1

e2πiλz z ´ w

tje2πtpiz´1qdt

I3 “ I3pw, zq “

![image 124](<2025-gonalves-complete-classification-fourier-summation_images/imageFile124.png>)

![image 125](<2025-gonalves-complete-classification-fourier-summation_images/imageFile125.png>)

0

j“0

kÿ´1

e2πiλz z ´ w

j!bk´1,j p2πqj`1

1 p1 ´ izqj`1

“

¨

.

![image 126](<2025-gonalves-complete-classification-fourier-summation_images/imageFile126.png>)

![image 127](<2025-gonalves-complete-classification-fourier-summation_images/imageFile127.png>)

![image 128](<2025-gonalves-complete-classification-fourier-summation_images/imageFile128.png>)

![image 129](<2025-gonalves-complete-classification-fourier-summation_images/imageFile129.png>)

j“0

The result follows. Finally for item (iv), we deﬁne H0pz, xq :“ e´2πiz|x|1xă0 ` e2πiz|x|1xě0, px P Rq

![image 130](<2025-gonalves-complete-classification-fourier-summation_images/imageFile130.png>)

and set Hkpz, xq :“ H0pz, ¨q ˚ Akpxq (for k ě 1q. Then, for λ “ 0, z “ s P R, we have Hkps, 0q “ ż

1 πk ¨

1 p1 ` s2qk

e2πisxAkpxqdx “ Axkp´sq “

.

![image 131](<2025-gonalves-complete-classification-fourier-summation_images/imageFile131.png>)

![image 132](<2025-gonalves-complete-classification-fourier-summation_images/imageFile132.png>)

R

On the other hand, using that Akpxq “ e´2π|x|pk´1p|x|q and expanding the integral, we obtain

„

.

kÿ´1

1 p1 ´ isqj`1

1 p1 ` isqj`1

j!bk´1,j p2πqj`1

Hkps, 0q “

`

![image 133](<2025-gonalves-complete-classification-fourier-summation_images/imageFile133.png>)

![image 134](<2025-gonalves-complete-classification-fourier-summation_images/imageFile134.png>)

![image 135](<2025-gonalves-complete-classification-fourier-summation_images/imageFile135.png>)

j“0

The claim follows by analytic continuation on s.

We now introduce our main Lemma, which establishes a bridge between the Fourier series and the Nevanlinna factorization of the map Fpzq in Theorem 1. For k an integer, we deﬁne the kernel Sk:

ˆ

˙2pk`1q

sinpπxq πx

1 vk

Skpxq :“

![image 136](<2025-gonalves-complete-classification-fourier-summation_images/imageFile136.png>)

![image 137](<2025-gonalves-complete-classification-fourier-summation_images/imageFile137.png>)

with vk ą 0 chosen so that Sxkp0q “ 1. Note that Sxkptq “

1 vk

1r´1{2,1{2s ˚ ¨¨¨ ˚ 1r´1{2,1{2sptq; the convolution of 2pk ` 1q indicator functions.

![image 138](<2025-gonalves-complete-classification-fourier-summation_images/imageFile138.png>)

- Lemma 5 (The Bridge Lemma). If pµ, aq is a FS-pair such that degpµq ď 2pk ` 1q, then


˙ “

apλqGkpw, z, λqSxk ˆ

ż

ÿ

dµptq p1 ` t2qk

- 1

![image 139](<2025-gonalves-complete-classification-fourier-summation_images/imageFile139.png>)

- 2πk`1i


1 pt ´ zqpt ´ wq

λ T

¨

lim

.

![image 140](<2025-gonalves-complete-classification-fourier-summation_images/imageFile140.png>)

![image 141](<2025-gonalves-complete-classification-fourier-summation_images/imageFile141.png>)

![image 142](<2025-gonalves-complete-classification-fourier-summation_images/imageFile142.png>)

![image 143](<2025-gonalves-complete-classification-fourier-summation_images/imageFile143.png>)

TÑ8

R

|λ|ďTpk`1q

uniformly for z, w P C` in the region

Rc :“ tz P C`; |Repzq| ď 1{c and Impzq ě cu, for all c ą 0.

Proof. Fix a c ą 0 small and write S :“ Sk. Observe that Sp has compact support with supppSpq Ă r´k ´ 1, k ` 1s and Spp0q “ 1. For T ą 0, let STpxq “ TSpTxq which is an approximation of identity as T Ñ 8, and SxTptq “ Sppt{Tq. Take a function ϕ P C8

c pRq, with ϕ ě 0, supppϕq Ă r´1, 1s and ϕpp0q “ 1. For 0 ă ε ă 1, let ϕεpxq “ ϕpx{εq{ε. Then, for ﬁxed T ą 4{c, we deﬁne

Gε,Tpxq “ ´Gkpw, z, ¨qSxT¯ ˚ ϕεpxq which belongs to C8

c p´Tpk ` 1q ´ 1, Tpk ` 1q ` 1q. Also, Gyε,Tptq “ ´

Gxkpw, z, ¨q ˚ ST¯ptqϕppεtq, which converges pointwisely to Gxkpw, z, ¨q ˚ STptq when ε Ó 0. We also claim that

1 pt2 ` c2qk`1

ˇGxkpw, z, ¨q ˚ STptqˇ !c

(7) for z, w P Rc, which we prove in the end. Since pµ, aq is an FS-pair, we have

![image 144](<2025-gonalves-complete-classification-fourier-summation_images/imageFile144.png>)

apλqGε,Tpλq “ ż

´

Gxkpw, z, ¨q ˚ ST¯ptqϕppεtqdµptq.

ÿ

R

|λ|ďTpk`1q`1

Because ap¨q is locally summable, Gε,T Ñ Gkpw, z, ¨qSxT uniformly in R, Gyε,Tptq Ñ Gxkpw, z, ¨q ˚ STptq pointwisely as ε Ó 0, ||ϕp||8 ď 1 and inequality (7), using the Dominated Convergence Theorem we obtain that

apλqGkpw, z, λqSpˆ

˙ “ ż

ÿ

λ T

R Gxkpw, z, ¨q ˚ STptqdµptq (8)

![image 145](<2025-gonalves-complete-classification-fourier-summation_images/imageFile145.png>)

|λ|ďTpk`1q

holds for any w, z P Rc. Note that, for each ﬁxed c ą 0, T ą 4{c and w P C`, the left-hand side above deﬁnes a holomorphic function in z P C`.

We now show that

1 pt2 ` c2qk`1

|Gxkpw, z, tq| !c

. (9) Indeed, we have

![image 146](<2025-gonalves-complete-classification-fourier-summation_images/imageFile146.png>)

1 |t ´ z| ¨ |t ´ w|

1 p1 ` t2qk

1 t2 ` c2 ¨

1 p1 ` t2qk

|Gxkpw, z, tq| !c

¨

!c

.

![image 147](<2025-gonalves-complete-classification-fourier-summation_images/imageFile147.png>)

![image 148](<2025-gonalves-complete-classification-fourier-summation_images/imageFile148.png>)

![image 149](<2025-gonalves-complete-classification-fourier-summation_images/imageFile149.png>)

![image 150](<2025-gonalves-complete-classification-fourier-summation_images/imageFile150.png>)

![image 151](<2025-gonalves-complete-classification-fourier-summation_images/imageFile151.png>)

The family of maps Gxkpw, z, ¨q for z, w P Rc is uniformly continuous, uniformly on z, w, because each function is Lipschitz with constant independent of z, w. Indeed, for t1, t2 P R, we have

´ Gx0pw, z, t2q

Gx0pw, z, t1q p1 ` t21qk

|Gxkpw, z, t1q ´ Gxkpw, z, t2q| !

![image 152](<2025-gonalves-complete-classification-fourier-summation_images/imageFile152.png>)

![image 153](<2025-gonalves-complete-classification-fourier-summation_images/imageFile153.png>)

p1 ` t22qk ˇ ď

ˇ

Gx0pw, z, t1q p1 ` t21qk

´ Gx0pw, z, t1q p1 ` t22qk ˇ

´ Gx0pw, z, t2q p1 ` t22qk ˇ

Gx0pw, z, t1q p1 ` t22qk

`

![image 154](<2025-gonalves-complete-classification-fourier-summation_images/imageFile154.png>)

![image 155](<2025-gonalves-complete-classification-fourier-summation_images/imageFile155.png>)

![image 156](<2025-gonalves-complete-classification-fourier-summation_images/imageFile156.png>)

![image 157](<2025-gonalves-complete-classification-fourier-summation_images/imageFile157.png>)

ˇ

ˇ

1 p1 ` t22qkˇ ` ˇGx0pw, z, t1q ´ Gx0pw, z, t2qˇ

1 p1 ` t21qk

ď ˇGx0pw, z, t1qˇˇ

´

![image 158](<2025-gonalves-complete-classification-fourier-summation_images/imageFile158.png>)

![image 159](<2025-gonalves-complete-classification-fourier-summation_images/imageFile159.png>)

![image 160](<2025-gonalves-complete-classification-fourier-summation_images/imageFile160.png>)

p1 ` t22qk !

|t1 ´ t2|

1 c2

4πc3 !c |t1 ´ t2|, because

k|t1 ´ t2| `

![image 161](<2025-gonalves-complete-classification-fourier-summation_images/imageFile161.png>)

![image 162](<2025-gonalves-complete-classification-fourier-summation_images/imageFile162.png>)

|t1 ´ t2| 4πc3

1 t1 ´ z ´

1 t1 ´ w ´

1 t2 ´ z `

1 t2 ´ wˇ ď

1 2π|z ´ w| ˇ

|Gx0pw, z, t1q ´ Gx0pw, z, t2q| “

.

![image 163](<2025-gonalves-complete-classification-fourier-summation_images/imageFile163.png>)

![image 164](<2025-gonalves-complete-classification-fourier-summation_images/imageFile164.png>)

![image 165](<2025-gonalves-complete-classification-fourier-summation_images/imageFile165.png>)

![image 166](<2025-gonalves-complete-classification-fourier-summation_images/imageFile166.png>)

![image 167](<2025-gonalves-complete-classification-fourier-summation_images/imageFile167.png>)

![image 168](<2025-gonalves-complete-classification-fourier-summation_images/imageFile168.png>)

![image 169](<2025-gonalves-complete-classification-fourier-summation_images/imageFile169.png>)

![image 170](<2025-gonalves-complete-classification-fourier-summation_images/imageFile170.png>)

![image 171](<2025-gonalves-complete-classification-fourier-summation_images/imageFile171.png>)

Since Gxkpw, z, ¨q is uniformly continuous, uniformly for z, w P Rc, we deduce that Gxkpw, z, ¨q˚

ST Ñ Gxkpw, z, ¨q as T Ñ 8, uniformly for z, w P Rc. Combining (8), (7) and (9), and using the Dominated Convergence Theorem, plus the fact that the measure µ is locally ﬁnite, we ﬁnally deduce that

apλqGkpw, z, λqSpˆ

˙ “

ż

ÿ

dµptq p1 ` t2qk

- 1

![image 172](<2025-gonalves-complete-classification-fourier-summation_images/imageFile172.png>)

- 2πk`1i


1 pt ´ zqpt ´ wq

λ T

¨

lim

,

![image 173](<2025-gonalves-complete-classification-fourier-summation_images/imageFile173.png>)

![image 174](<2025-gonalves-complete-classification-fourier-summation_images/imageFile174.png>)

![image 175](<2025-gonalves-complete-classification-fourier-summation_images/imageFile175.png>)

![image 176](<2025-gonalves-complete-classification-fourier-summation_images/imageFile176.png>)

TÑ8

R

|λ|ďTpk`1q

uniformly in z, w P Rc, as desired. All that remains to be proven is (7). Indeed, for T ą 4{c and z, w P Rc, we have

ż

sin2pk`1qpTπsq rpt ´ sq ´ zsrpt ´ sq ´ wsr1 ` pt ´ sq2skpπsq2pk`1q

1 2πk`1iT2k`1

Gxkpw, z, ¨q ˚ STptq “

ds

![image 177](<2025-gonalves-complete-classification-fourier-summation_images/imageFile177.png>)

![image 178](<2025-gonalves-complete-classification-fourier-summation_images/imageFile178.png>)

![image 179](<2025-gonalves-complete-classification-fourier-summation_images/imageFile179.png>)

R

ż

sinkpTπps ` i{Tqq rpt ´ s ´ i{Tq ´ zsrpt ´ s ´ i{Tq ´ wsr1 ` pt ´ s ´ i{Tq2skrπps ` i{Tqs2pk`1q

1 2πk`1iT2k`1

“

ds

![image 180](<2025-gonalves-complete-classification-fourier-summation_images/imageFile180.png>)

![image 181](<2025-gonalves-complete-classification-fourier-summation_images/imageFile181.png>)

![image 182](<2025-gonalves-complete-classification-fourier-summation_images/imageFile182.png>)

R

hence

ż

1 T2k`1

1 rpt ´ sq2 ` c2sk`1ps2 ` 1{T2qk`1

ˇGxkpw, z, ¨q ˚ STptqˇ !c

ds.

![image 183](<2025-gonalves-complete-classification-fourier-summation_images/imageFile183.png>)

![image 184](<2025-gonalves-complete-classification-fourier-summation_images/imageFile184.png>)

R

We now use the Residue Theorem to change the contour of integration to s`ic{2. Indeed, the map

1 rpt ´ sq2 ` c2sk`1ps2 ` 1{T2qk`1

fpsq :“

![image 185](<2025-gonalves-complete-classification-fourier-summation_images/imageFile185.png>)

has a pole of order k ` 1 at s “ i{T, and the residue of fpsq is given by Res

fpsq “ ÿ

γj,m,n pt ´ i{Tqj T2k`1rpt ´ i{Tq2 ` c2sk`lp2i{Tqk`m

,

![image 186](<2025-gonalves-complete-classification-fourier-summation_images/imageFile186.png>)

z“i{T

1ďj,m,nďk`1 k`l´jěk`1

for some coeﬃcients γj,m,n, from which we derive

1 pt2 ` η1c2qk`1

fpsqˇ !c

ˇ Res

, for some η1 ą 0. On the other hand, the integral over the line s ` ic{2 gives ˇ

![image 187](<2025-gonalves-complete-classification-fourier-summation_images/imageFile187.png>)

z“i{T

ż

1 rpt ´ s ´ ic{2q2 ` c2sk`1rps ` ic{2q2 ` 1{T2sk`1

dsˇ ď ż

![image 188](<2025-gonalves-complete-classification-fourier-summation_images/imageFile188.png>)

R

1 T2k`1rpt ´ sq2 ` 3c2{4sk`1ps2 ` 3c2{16qk`1

1 pt2 ` η2c2qk`1

!c

,

![image 189](<2025-gonalves-complete-classification-fourier-summation_images/imageFile189.png>)

![image 190](<2025-gonalves-complete-classification-fourier-summation_images/imageFile190.png>)

R

where we used the elementary fact about convolutions that if |f1pxq|, |f2pxq| ď p1`|Cx|2qk for all |x| ě R1, then |f1 ˚ f2pxq| ď p1`|Cx|2qk for |x| ě R2. The proof is complete.

![image 191](<2025-gonalves-complete-classification-fourier-summation_images/imageFile191.png>)

![image 192](<2025-gonalves-complete-classification-fourier-summation_images/imageFile192.png>)

5. Proof of Theorems 1 and 2

Proof of Theorem 1: Necessity. Since ap¨q has exponential growth, there exists α ą 0 such that

ř

λPR |apλq|e´2πα|λ| ă 8. We claim we can assume that α ă 1. Indeed, suppose the necessity part of Theorem 1 is proven for α ă 1. Now, given an arbitrary FS-pair pµ, aq consider the pair py0´1µpy0¨q, ap¨{y0qq for y0 ą 0 suﬃciently large so that ř

- 1

![image 193](<2025-gonalves-complete-classification-fourier-summation_images/imageFile193.png>)

- 2|λ| “ ř


λPR |apλ{y0q|e´2π

λPR |apλq|e´πy0|λ| ă 8. By hypothesis the function Frpzq “

ż

ap0q ` ÿ

y0´1dµpy0tq p1 ` t2qk`1

pz2 ` 1qk 2πi

tz ` 1 t ´ z ¨

- 1

![image 194](<2025-gonalves-complete-classification-fourier-summation_images/imageFile194.png>)

- 2


apλ{y0qe2πiλz “

` iQpzq,

![image 195](<2025-gonalves-complete-classification-fourier-summation_images/imageFile195.png>)

![image 196](<2025-gonalves-complete-classification-fourier-summation_images/imageFile196.png>)

![image 197](<2025-gonalves-complete-classification-fourier-summation_images/imageFile197.png>)

R

λą0

is a well-deﬁned holomorphic function in C` that belongs to Nďk ´ Nďk, where the second identity above is valid for Imz ą 0 while the ﬁrst is valid for Im z ą 1. Moreover, Fr P APpC` ` iq. By the remarks in the end of Section 3 (see also (6)), it also holds that

ż

ap0q ` ÿ

tz ` y0´2 t ´ z ¨

pz2 ` y0´2qk 2πi

y0´1dµpy0tq py0´2 ` t2qk`1

- 1

![image 198](<2025-gonalves-complete-classification-fourier-summation_images/imageFile198.png>)

- 2


Frpzq “

apλ{y0qe2πiλz “

` iQ1pzq,

![image 199](<2025-gonalves-complete-classification-fourier-summation_images/imageFile199.png>)

![image 200](<2025-gonalves-complete-classification-fourier-summation_images/imageFile200.png>)

![image 201](<2025-gonalves-complete-classification-fourier-summation_images/imageFile201.png>)

R

λą0

for some real polynomial Q1 of degree at most 2k ` 1. We then let Fpzq “ Frpz{y0q and observe that F P APpC` ` iy0q and that

ż

ap0q ` ÿ

pz2 ` 1qk 2πi

dµptq p1 ` t2qk`1

tz ` 1 t ´ z ¨

- 1

![image 202](<2025-gonalves-complete-classification-fourier-summation_images/imageFile202.png>)

- 2


apλqe2πiλz “

` iQ1pz{y0q. The result would then follow.

Fpzq “

![image 203](<2025-gonalves-complete-classification-fourier-summation_images/imageFile203.png>)

![image 204](<2025-gonalves-complete-classification-fourier-summation_images/imageFile204.png>)

![image 205](<2025-gonalves-complete-classification-fourier-summation_images/imageFile205.png>)

R

λą0

ř

λPR |apλq|e´π|λ| ă 8. We begin by applying the Bridge Lemma 5 and multiplying both sides by pz ´ wq to get

Therefore, it suﬃces to consider the case

![image 206](<2025-gonalves-complete-classification-fourier-summation_images/imageFile206.png>)

apλqpz ´ wqGkpw, z, λqSxk ˆ

˙ “

ż

ÿ

z ´ w pt ´ zqpt ´ wq

dµptq p1 ` t2qk

- 1

![image 207](<2025-gonalves-complete-classification-fourier-summation_images/imageFile207.png>)

- 2πk`1i


λ T

![image 208](<2025-gonalves-complete-classification-fourier-summation_images/imageFile208.png>)

¨

lim

, (10)

![image 209](<2025-gonalves-complete-classification-fourier-summation_images/imageFile209.png>)

![image 210](<2025-gonalves-complete-classification-fourier-summation_images/imageFile210.png>)

![image 211](<2025-gonalves-complete-classification-fourier-summation_images/imageFile211.png>)

![image 212](<2025-gonalves-complete-classification-fourier-summation_images/imageFile212.png>)

![image 213](<2025-gonalves-complete-classification-fourier-summation_images/imageFile213.png>)

TÑ8

R

λPR

which converges uniformly for z, w in compact sets of C`. The right-hand side can be written as Hpzq ` Hpwq, where

![image 214](<2025-gonalves-complete-classification-fourier-summation_images/imageFile214.png>)

ż

tz ` 1 t ´ z ¨

dµptq p1 ` t2qk`1

- 1

![image 215](<2025-gonalves-complete-classification-fourier-summation_images/imageFile215.png>)

- 2πk`1i


Hpzq :“

![image 216](<2025-gonalves-complete-classification-fourier-summation_images/imageFile216.png>)

![image 217](<2025-gonalves-complete-classification-fourier-summation_images/imageFile217.png>)

R

is a holomorphic function in C`. Now, we use the explicit form of the map Gk, split the limit into the sum and isolate the z´terms from the w´terms: For z, w P C`, z, w ‰ i, by Lemma (4) (iii) and (iv), the left-hand side of (10) can be written as (by simplicity, we write bj “ bk´1,j)

![image 218](<2025-gonalves-complete-classification-fourier-summation_images/imageFile218.png>)

1 πk ¨

1 πk ¨

1 p1 ` z2qk

1 p1 ` w2qk

![image 219](<2025-gonalves-complete-classification-fourier-summation_images/imageFile219.png>)

Fpzq ¨

` Fpwq ¨

(11)

![image 220](<2025-gonalves-complete-classification-fourier-summation_images/imageFile220.png>)

![image 221](<2025-gonalves-complete-classification-fourier-summation_images/imageFile221.png>)

![image 222](<2025-gonalves-complete-classification-fourier-summation_images/imageFile222.png>)

![image 223](<2025-gonalves-complete-classification-fourier-summation_images/imageFile223.png>)

ÿj

ÿj

kÿ´1

kÿ´1

1 p1 ´ izqj`1´l

1 p1 ` izqj`1´l

j!bj p2πqj`1

j!bj p2πqj`1

![image 224](<2025-gonalves-complete-classification-fourier-summation_images/imageFile224.png>)

γlpTq

γlpTq ´

`

lim

lim

![image 225](<2025-gonalves-complete-classification-fourier-summation_images/imageFile225.png>)

![image 226](<2025-gonalves-complete-classification-fourier-summation_images/imageFile226.png>)

![image 227](<2025-gonalves-complete-classification-fourier-summation_images/imageFile227.png>)

![image 228](<2025-gonalves-complete-classification-fourier-summation_images/imageFile228.png>)

TÑ8

TÑ8

j“0

j“0

l“0

l“0

kÿ´1

ÿj

ÿj

kÿ´1

j!bj p2πqj`1

1 p1 ` iwqj`1´l

1 p1 ´ iwqj`1´l

j!bj p2πqj`1

![image 229](<2025-gonalves-complete-classification-fourier-summation_images/imageFile229.png>)

`

γlpTq ´

γlpTq,

lim

lim

![image 230](<2025-gonalves-complete-classification-fourier-summation_images/imageFile230.png>)

![image 231](<2025-gonalves-complete-classification-fourier-summation_images/imageFile231.png>)

![image 232](<2025-gonalves-complete-classification-fourier-summation_images/imageFile232.png>)

![image 233](<2025-gonalves-complete-classification-fourier-summation_images/imageFile233.png>)

![image 234](<2025-gonalves-complete-classification-fourier-summation_images/imageFile234.png>)

![image 235](<2025-gonalves-complete-classification-fourier-summation_images/imageFile235.png>)

TÑ8

TÑ8

j“0

j“0

l“0

l“0

where

˙e2πiλz,

apλqSxk ˆ

ÿ

- 1

![image 236](<2025-gonalves-complete-classification-fourier-summation_images/imageFile236.png>)

- 2


λ T

ap0q ` lim

Fpzq :“

![image 237](<2025-gonalves-complete-classification-fourier-summation_images/imageFile237.png>)

TÑ8

λą0

which converges uniformly in compact subsets of C`. Note that the deﬁnition of Fpzq does not depend on y0. Moreover,

˙e´2πλ,

apλqSxk ˆ

ap0q ` ÿ

- 1

![image 238](<2025-gonalves-complete-classification-fourier-summation_images/imageFile238.png>)

- 2


λ T

γ0pTq :“

![image 239](<2025-gonalves-complete-classification-fourier-summation_images/imageFile239.png>)

λą0

apλqSxk ˆ

˙p2πλqle´2πλ, for l ě 1.

1 l! ÿ

λ T

γlpTq :“

![image 240](<2025-gonalves-complete-classification-fourier-summation_images/imageFile240.png>)

![image 241](<2025-gonalves-complete-classification-fourier-summation_images/imageFile241.png>)

λą0

and each of the limits limTÑ8 γlpTq for l ě 0, does exist and lim

ap0q ` ÿ

- 1

![image 242](<2025-gonalves-complete-classification-fourier-summation_images/imageFile242.png>)

- 2


apλqe´2πλ, and

γ0pTq “

TÑ8

λą0

1 l! ÿ

apλqp2πλqle´2πλ, for l ě 1.

γlpTq “

lim

![image 243](<2025-gonalves-complete-classification-fourier-summation_images/imageFile243.png>)

TÑ8

λą0

Furthermore, since

ap0q ` ÿ

- 1

![image 244](<2025-gonalves-complete-classification-fourier-summation_images/imageFile244.png>)

- 2


apλqe2πiλz (12)

Fpzq “

λą0

converges uniformly and absolutely for Impzq ą 1{2, we can then interchange summation and diﬀerentiation:

Fpkqpzq “ ÿ

apλqp2πiλqke2πiλz, for k ě 1,

λą0

plqpiq

hence, limTÑ8 γlpTq “ F

![image 245](<2025-gonalves-complete-classification-fourier-summation_images/imageFile245.png>)

l!il for l ě 0. Then we can write (11) as Rpzq ` Rpwq where Rpzq :“

![image 246](<2025-gonalves-complete-classification-fourier-summation_images/imageFile246.png>)

ˆ

˙

ÿj

kÿ´1

![image 247](<2025-gonalves-complete-classification-fourier-summation_images/imageFile247.png>)

Fplqpiq l!il

Fpzq πkp1 ` z2qk

1 p1 ´ izqj`1´l

j!bj p2πqj`1

`

![image 248](<2025-gonalves-complete-classification-fourier-summation_images/imageFile248.png>)

![image 249](<2025-gonalves-complete-classification-fourier-summation_images/imageFile249.png>)

![image 250](<2025-gonalves-complete-classification-fourier-summation_images/imageFile250.png>)

![image 251](<2025-gonalves-complete-classification-fourier-summation_images/imageFile251.png>)

j“0

l“0

kÿ´1

ÿj

Fplqpiq l!il

j!bj p2πqj`1

1 p1 ` izqj`1´l

´

![image 252](<2025-gonalves-complete-classification-fourier-summation_images/imageFile252.png>)

![image 253](<2025-gonalves-complete-classification-fourier-summation_images/imageFile253.png>)

![image 254](<2025-gonalves-complete-classification-fourier-summation_images/imageFile254.png>)

j“0

l“0

which is holomorphic in C`ztiu. Therefore, we obtain Rpzq ` Rpwq “ Hpzq ` Hpwq

![image 255](<2025-gonalves-complete-classification-fourier-summation_images/imageFile255.png>)

![image 256](<2025-gonalves-complete-classification-fourier-summation_images/imageFile256.png>)

for z, w P C`ztiu. By analytic continuation, we conclude there exists some h P R such that Rpzq “ ih ` Hpzq. Multiplying both sides by pz2 ` 1qk and rearranging terms, we get

1 πk “ pz2 ` 1qkHpzq `

i πk

Fpzq

Qpzq where4

![image 257](<2025-gonalves-complete-classification-fourier-summation_images/imageFile257.png>)

![image 258](<2025-gonalves-complete-classification-fourier-summation_images/imageFile258.png>)

- kÿ´1
- l“0


i πk

Qlpzq ´ Q˚l pzq

Qpzq :“ ihpz2 ` 1qk `

![image 259](<2025-gonalves-complete-classification-fourier-summation_images/imageFile259.png>)

kÿ´1

Fplqpiq l!il

j!bj p2πqj`1

1 p1 ` izqj`1´l

Qlpzq “ pz2 ` 1qk

¨

.

![image 260](<2025-gonalves-complete-classification-fourier-summation_images/imageFile260.png>)

![image 261](<2025-gonalves-complete-classification-fourier-summation_images/imageFile261.png>)

![image 262](<2025-gonalves-complete-classification-fourier-summation_images/imageFile262.png>)

j“l

Observe that Qpzq is a real polynomial and Qpzq “ hπkz2k ` rpzq, where rpzq is a real polynomial of degree ď 2k ´ 1. We obtain

ż

pz2 ` 1qk 2πi

dµptq p1 ` t2qk`1

tz ` 1 t ´ z ¨

` iQpzq, which belongs to the class Nďk ´ Nďk.

Fpzq “

![image 263](<2025-gonalves-complete-classification-fourier-summation_images/imageFile263.png>)

![image 264](<2025-gonalves-complete-classification-fourier-summation_images/imageFile264.png>)

![image 265](<2025-gonalves-complete-classification-fourier-summation_images/imageFile265.png>)

R

Now, from (12), we conclude that Fp¨ ` iq is the uniform limit of trigonometric polynomials. Hence, by [14, Lemma 8] Fp¨ ` iq P APpRq. Since Fpzq is holomorphic and bounded in C` ` i, it follows from [14, Lemma 11] that Fp¨ ` iq P APpC`q, and with Fourier coeﬃcients given by apλq. Take c “ 1 and (II) is proved. Finally, (III) follows from the ﬁnite exponential growth assumption on ap¨q.

We now prove suﬃciency by proving Theorem 2.

Proof of Theorem 2. Since Fp¨ ` icq P APpC`q, it follows from [14, Lemma 11] that the limit

ż T`iy

- 1

![image 266](<2025-gonalves-complete-classification-fourier-summation_images/imageFile266.png>)

- 2T


Fpzqe´2πiλzdz exist for all λ P R and does not depend on y ą c. Moreover, it holds ÿ

EFpλq :“ lim

TÑ8

´T`iy

“|Fp¨ ` iyq|2‰ ă 8

|EFpλq|2e´4πλy “ E

λPR

for any y ą c. We now claim that Fp¨ ` 2icq is bounded. Hence, by [14, Lemma 12(i)], it will follow that EFpλq “ 0 for any λ ă 0. In order to prove it is bounded, we will employ the Phragm´en-Lindelo¨f Theorem (as in [10, Thm 1]). Let Gpzq :“ Fpz ` 2icq.

![image 267](<2025-gonalves-complete-classification-fourier-summation_images/imageFile267.png>)

4We recall the notation F˚pzq “ Fpzq.

![image 268](<2025-gonalves-complete-classification-fourier-summation_images/imageFile268.png>)

![image 269](<2025-gonalves-complete-classification-fourier-summation_images/imageFile269.png>)

From Lemma [14, Lemma 11], the map x P R ÞÑ Gpxq P APpRq, hence it is bounded in R. What remais to prove is that

ż π

1 r

log` |Gpreiθq|sinpθqdθ “ 0, (13)

liminf

![image 270](<2025-gonalves-complete-classification-fourier-summation_images/imageFile270.png>)

rÑ8

0

where log`pxq :“ maxtlogpxq, 0u. Indeed, since Fpzq belongs to the class Nďk ´ Nďk, it admits a Nevanlinna factorization: There exists a unique real signed measure µ with degpµq “ 2pm ` 1q, m ď k, and a real polynomial Qpzq of degree at most 2m ` 1, such that

ż

pz2 ` 1qm 2πi

dµptq p1 ` t2qm`1

1 ` tz t ´ z ¨

Fpzq “

` iQpzq

![image 271](<2025-gonalves-complete-classification-fourier-summation_images/imageFile271.png>)

![image 272](<2025-gonalves-complete-classification-fourier-summation_images/imageFile272.png>)

![image 273](<2025-gonalves-complete-classification-fourier-summation_images/imageFile273.png>)

R

for z P C`. We can assume, without lost of generality, that m “ k, otherwise by Proposition 3 we have F P Nďm ´ Nďm, and the proof would follow from induction. Observe that, by splitting in |t| ď 2|z| and |t| ą 2|z|, we obtain ˇ1`tz

2

ˇ ď 1`2|z|

y . Hence Gpreiθq “ Opr2k`2q, and condition (13) follows.

![image 274](<2025-gonalves-complete-classification-fourier-summation_images/imageFile274.png>)

![image 275](<2025-gonalves-complete-classification-fourier-summation_images/imageFile275.png>)

t´z

apλqϕpλq “ ş

ř

ϕpptqdµptq for any test function ϕ. Note that, by linearity, it is enough to show this identity only for antipodal test functions ϕp´xq “ ϕĘpxq, as any test function ϕ can be written as ϕ “ u ` iv, where u and v are antipodal. To this end, let

It remains to prove that

ż

1 ` tz t ´ z ¨

dµptq p1 ` t2qk`1

- 1

![image 276](<2025-gonalves-complete-classification-fourier-summation_images/imageFile276.png>)

- 2πi


pz2 ` 1qk

Hpzq :“ Fpzq ´ iQpzq “

.

![image 277](<2025-gonalves-complete-classification-fourier-summation_images/imageFile277.png>)

![image 278](<2025-gonalves-complete-classification-fourier-summation_images/imageFile278.png>)

R

On one hand, for z P C` and s P R, we have

Hpz ` sq ` Hp´z ` sq “ ż

dµptq p1 ` t2qk`1

![image 279](<2025-gonalves-complete-classification-fourier-summation_images/imageFile279.png>)

Pzpt ´ sqp1 ` s2qkp1 ` t2q

(14)

![image 280](<2025-gonalves-complete-classification-fourier-summation_images/imageFile280.png>)

![image 281](<2025-gonalves-complete-classification-fourier-summation_images/imageFile281.png>)

R

` 2k ż

dµptq p1 ` t2qk`1 `

Pzpt ´ sqsp1 ` s2qk´1pst ´ s2 ` t2s2 ´ ts3q

![image 282](<2025-gonalves-complete-classification-fourier-summation_images/imageFile282.png>)

R

ż

dµptq p1 ` t2qk`1

- 1

![image 283](<2025-gonalves-complete-classification-fourier-summation_images/imageFile283.png>)

- 2


Pzpt ´ sqhpz, s, tq

,

![image 284](<2025-gonalves-complete-classification-fourier-summation_images/imageFile284.png>)

R

where hpz, s, tq is a polynomial in the variables z, s, t with real coeﬃcients such that there is no constant term in z, the degree in t is at most 2, and

z πipt2 ´ z2q

Pzptq :“

![image 285](<2025-gonalves-complete-classification-fourier-summation_images/imageFile285.png>)

is the Poisson kernel. Let ϕ P Cc8p´M, Mq be antipodal, hence ϕp is real-valued. From

- (14) we obtain ż


”Hpz ` sq ` Hp´z ` sqı

![image 286](<2025-gonalves-complete-classification-fourier-summation_images/imageFile286.png>)

ϕppsqds “ (15)

![image 287](<2025-gonalves-complete-classification-fourier-summation_images/imageFile287.png>)

R

“ ż

ż

dµptq p1 ` t2qk`1 ` 2k ż

Pzpt ´ sqp1 ` s2qkϕppsqdsp1 ` t2q

![image 288](<2025-gonalves-complete-classification-fourier-summation_images/imageFile288.png>)

R

R

ż

dµptq p1 ` t2qk`1 `

Pzpt ´ sqsp1 ` s2qk´1pst ´ s2 ` t2s2 ´ ts3qϕppsqds

![image 289](<2025-gonalves-complete-classification-fourier-summation_images/imageFile289.png>)

R

R

ż

ż

dµptq p1 ` t2qk`1

- 1

![image 290](<2025-gonalves-complete-classification-fourier-summation_images/imageFile290.png>)

- 2


Pzpt ´ sqhpz, s, tqϕppsqds

![image 291](<2025-gonalves-complete-classification-fourier-summation_images/imageFile291.png>)

R

R

Taking z “ iy and using the fact that Piy is an approximation of identity when y Ó 0, from the right-hand side of (15) and the Dominated Convergence Theorem we obtain

ż

` 2k ż

dµptq p1 ` t2qk`1

dµptq p1 ` t2qk`1 “ ż

p1 ` t2qk`1ϕpptq

tp1 ` t2qk´1pt2 ´ t2 ` t4 ´ t4qϕpptqds

![image 292](<2025-gonalves-complete-classification-fourier-summation_images/imageFile292.png>)

![image 293](<2025-gonalves-complete-classification-fourier-summation_images/imageFile293.png>)

R

R

ϕpptqdµptq. On the other hand, using that Hpzq “ Fpzq ´ iQpzq, we can write the left-hand side of

R

- (15) in a diﬀerent way. Fix an Impzq ą c and write z “ x ` ipc ` ηq. Since the map s ÞÑ Fps ` ipc ` ηqq P APpRq, by Bochner’s Approximation (see [14, Proposition 7]), it can be approximated by a sequence of trigonometric polynomials


gnpsq “ ÿ

EFpλqe2πiλipc`ηqdnpλqe2πiλs

λě0

such that ||gn ´ Fp¨ ` ipc ` ηqq||8 Ñ 0 as n Ñ 8. Here dn : R Ñ r0, 1s is a sequence of functions, each one with ﬁnite support and such that

#1 if EFpλq ‰ 0 0 if EFpλq “ 0.

dnpλq “

lim

nÑ8

Since Qpzq is a real polynomial of degree at most 2k ` 1 we can write

2ÿk`1

γl,jzlsj

Qpz ` sq “

l,j“0

where the coeﬃcients γl,j are real. Then ż

rgnpx ` sq ´ iQpz ` sqsϕppsqds “ ÿ

EFpλqe2πiλzdnpλqϕpλq

R

0ďλďM

2ÿk`1

ϕpjqp0q p2πiqj

γl,jzl

´ i

.

![image 294](<2025-gonalves-complete-classification-fourier-summation_images/imageFile294.png>)

l,j“0

Since the map λ ÞÑ EFpλq is locally summable, sending n Ñ 8 and using the Dominated Convergence Theorem, it follows that

ż

Hpz ` sqϕppsqds “ ÿ

2ÿk`1

ϕpjqp0q p2πiqj

EFpλqe2πiλzϕpλq ´ i

γl,jzl

,

![image 295](<2025-gonalves-complete-classification-fourier-summation_images/imageFile295.png>)

R

0ďλďM

l,j“0

which holds for Impzq ą c. Now, replacing z by ´z is the above computation and since ϕp is real-valued, we derive

![image 296](<2025-gonalves-complete-classification-fourier-summation_images/imageFile296.png>)

ż

Hp´z ` sqϕppsqds “ ÿ

2ÿk`1

![image 297](<2025-gonalves-complete-classification-fourier-summation_images/imageFile297.png>)

ϕpjqp0q p´1qjp2πiqj

![image 298](<2025-gonalves-complete-classification-fourier-summation_images/imageFile298.png>)

![image 299](<2025-gonalves-complete-classification-fourier-summation_images/imageFile299.png>)

![image 300](<2025-gonalves-complete-classification-fourier-summation_images/imageFile300.png>)

EFpλqe2πiλzϕpλq ` i

γl,jp´zql

.

![image 301](<2025-gonalves-complete-classification-fourier-summation_images/imageFile301.png>)

![image 302](<2025-gonalves-complete-classification-fourier-summation_images/imageFile302.png>)

R

0ďλďM

l,j“0

Hence, for Impzq ą c, we obtain ż

”Hpz ` sq ` Hp´z ` sqı

2ÿk`1

ϕppsqds “ ÿ

ϕpjqp0q p2πiqj

![image 303](<2025-gonalves-complete-classification-fourier-summation_images/imageFile303.png>)

EFpλqe2πiλzϕpλq ´ i

γl,jzl

![image 304](<2025-gonalves-complete-classification-fourier-summation_images/imageFile304.png>)

![image 305](<2025-gonalves-complete-classification-fourier-summation_images/imageFile305.png>)

R

l,j“0

0ďλďM

2ÿk`1

` ÿ

![image 306](<2025-gonalves-complete-classification-fourier-summation_images/imageFile306.png>)

ϕpjqp0q p´1qjp2πiqj

![image 307](<2025-gonalves-complete-classification-fourier-summation_images/imageFile307.png>)

![image 308](<2025-gonalves-complete-classification-fourier-summation_images/imageFile308.png>)

EFpλqe2πiλzϕpλq ` i

γl,jp´zql

.

![image 309](<2025-gonalves-complete-classification-fourier-summation_images/imageFile309.png>)

l,j“0

0ďλďM

![image 310](<2025-gonalves-complete-classification-fourier-summation_images/imageFile310.png>)

Since ϕ is antipodal, then ϕpjqp´λq “ p´1qjϕpjqpλq. From (15) we obtain ÿ

2ÿk`1

ϕpjqp0q p2πiqj

EFpλqe2πiλzϕpλq ´ i

γl,jzl

![image 311](<2025-gonalves-complete-classification-fourier-summation_images/imageFile311.png>)

l,j“0

0ďλďM

2ÿk`1

` ÿ

ϕpjqp0q p2πiqj

EFp´λqe2πi|λ|zϕpλq ` i

![image 312](<2025-gonalves-complete-classification-fourier-summation_images/imageFile312.png>)

γl,jp´zql

“

![image 313](<2025-gonalves-complete-classification-fourier-summation_images/imageFile313.png>)

l,j“0

´Mďλď0

“ ż

ż

dµptq p1 ` t2qk`1 ` 2k ż

Pzpt ´ sqp1 ` s2qkϕppsqdsp1 ` t2q

![image 314](<2025-gonalves-complete-classification-fourier-summation_images/imageFile314.png>)

R

R

ż

dµptq p1 ` t2qk`1 `

Pzpt ´ sqsp1 ` s2qk´1pst ´ s2 ` t2s2 ´ ts3qϕppsqds

![image 315](<2025-gonalves-complete-classification-fourier-summation_images/imageFile315.png>)

R

R

ż

ż

dµptq p1 ` t2qk`1

- 1

![image 316](<2025-gonalves-complete-classification-fourier-summation_images/imageFile316.png>)

- 2


Pzpt ´ sqhpz, s, tqϕppsqds

![image 317](<2025-gonalves-complete-classification-fourier-summation_images/imageFile317.png>)

R

R

holds for Impzq ą c. By analytic continuation, equality holds for any z P C`. Moreover, by antipodal splitting, the above equality holds for any ϕ P Cc8p´M, Mq for arbitrary M ą 0. Taking z “ iy and letting y Ó 0, we obtain

ÿ

2ÿk`1

ϕpjqp0q p2πiqj

EFpλqϕpλq ´ i

γ0,j

![image 318](<2025-gonalves-complete-classification-fourier-summation_images/imageFile318.png>)

j“0

0ďλďM

“ ż

2ÿk`1

` ÿ

ϕpjqp0q p2πiqj

![image 319](<2025-gonalves-complete-classification-fourier-summation_images/imageFile319.png>)

ϕpptqdµptq

EFp´λqϕpλq ` i

γ0,j

![image 320](<2025-gonalves-complete-classification-fourier-summation_images/imageFile320.png>)

R

j“0

´Mďλď0

hence

apλqϕpλq “ ż

apλqϕpλq ` EFp0qϕp0q ` ÿ

EFp0qϕp0q ` ÿ

![image 321](<2025-gonalves-complete-classification-fourier-summation_images/imageFile321.png>)

ϕpptqdµptq

R

´Mďλă0

0ăλďM

or better

apλqϕpλq “ ż

ÿ

ϕpptqdµptq.

R

λPR

The proof is complete.

6. Examples of FS-pairs

We now give some examples of FS-pairs (see also the last section in [14]). We focus on the measures not contemplated by the result in [14], that is, those pairs pµ, aq such that degpµq ě 3.

- 6.1. The Selberg Trace Formula. One example of an FS-pair is the Selberg Trace


formula. If S is a compact hyperbolic surface then, for any even ϕ P C8

c pRq, it holds that

ż

ϕp´ rj 2π¯ “

ÿ

rϕpprq tanhpπrqdr ` 2π ÿ

Λpγq Nγ1{2 ´ Nγ´1{2

ApSq 4π

ϕplogpNγqq, (16)

![image 322](<2025-gonalves-complete-classification-fourier-summation_images/imageFile322.png>)

![image 323](<2025-gonalves-complete-classification-fourier-summation_images/imageFile323.png>)

![image 324](<2025-gonalves-complete-classification-fourier-summation_images/imageFile324.png>)

R

jě0

γPGpSq

where ApSq is the hyperbolic surface area of S, rj P C is a solution for λj “ 1{4 ` rj2, where tλj; j ě 0u is the Laplacian spectrum on S, GpSq is the set of closed oriented geodesics on S. If γ is a closed geodesic on S, then Nγ “ elpγq is the norm of γ and Λpγq “ lpγ0q the length of γ, where γ0 is the unique oriented prime geodesic satisfying γ “ γ0m, for some integer m ě 1. Here, lpγq is the hyperbolic length of the curve γ. For

more details, see [4, Thm. 5.6]. Since tanhp¨q is odd, by symmetrizing (16), we obtain the following identity, which holds for any ϕ P C8

c pRq: 2π ApSq

rj 2π¯ı ´ ż

”

ϕp´ rj 2π¯ ` ϕp´´

ÿ

rϕpprq tanhpπrqdr “ (17)

![image 325](<2025-gonalves-complete-classification-fourier-summation_images/imageFile325.png>)

![image 326](<2025-gonalves-complete-classification-fourier-summation_images/imageFile326.png>)

![image 327](<2025-gonalves-complete-classification-fourier-summation_images/imageFile327.png>)

R

jě0

ÿ

4π2 ApSq

Λpγq Nγ1{2 ´ Nγ´1{2

rϕplogpNγqq ` ϕp´ logpNγqqs.

![image 328](<2025-gonalves-complete-classification-fourier-summation_images/imageFile328.png>)

![image 329](<2025-gonalves-complete-classification-fourier-summation_images/imageFile329.png>)

γPGpSq

This gives a FS-pair pµ, aq with µ “ ř

j{2πq ´ r tanhpπrqdr ap˘ logpNγqq “ Λpγq

jě0pδr

j{2π ` δ´r

, for γ P GpSq.

![image 330](<2025-gonalves-complete-classification-fourier-summation_images/imageFile330.png>)

Nγ1{2´Nγ´1{2

Observe that degpµq “ 3 because of the contribution of the absolutely continuous part and the fact that

ř

jě0 rj´2´ε ă 8 for ε ą 0, which is a consequence of the Spectral Theorem for compact hyperbolic surfaces (see for instance [4, Thm. 3.32]). More generally, by taking (17) for two compact hyperbolic surfaces S1 and S2, and taking the diﬀerence, we obtain a crystalline measure:

- 1

![image 331](<2025-gonalves-complete-classification-fourier-summation_images/imageFile331.png>)

ApS1q

ÿ

jě0

”

ϕp´ rj 2π¯ ` ϕp´´

![image 332](<2025-gonalves-complete-classification-fourier-summation_images/imageFile332.png>)

rj 2π¯ı ´

![image 333](<2025-gonalves-complete-classification-fourier-summation_images/imageFile333.png>)

1 ApS2q

![image 334](<2025-gonalves-complete-classification-fourier-summation_images/imageFile334.png>)

ÿ

mě0

”

ϕp´sm 2π¯ ` ϕp´´

![image 335](<2025-gonalves-complete-classification-fourier-summation_images/imageFile335.png>)

sm 2π¯ı “

![image 336](<2025-gonalves-complete-classification-fourier-summation_images/imageFile336.png>)

- 2π


ÿ

1pγq NS1{2

ΛS

rϕplogpNS

1γqq ` ϕp´ logpNS

1γqqs

![image 337](<2025-gonalves-complete-classification-fourier-summation_images/imageFile337.png>)

![image 338](<2025-gonalves-complete-classification-fourier-summation_images/imageFile338.png>)

1,γ ´ NS´1{2

ApS1q

γPGpS1q

1,γ

ÿ

2pγq NS1{2

ΛS

2π ApS2q

rϕplogpNS

2γqq ` ϕp´ logpNS

2γqqs,

´

![image 339](<2025-gonalves-complete-classification-fourier-summation_images/imageFile339.png>)

![image 340](<2025-gonalves-complete-classification-fourier-summation_images/imageFile340.png>)

2,γ ´ NS´1{2

γPGpS2q

2,γ

where t1{4 ` rj2; j ě 0u and t1{4 ` s2m; m ě 0u are the spectra of the Laplacian in S1 and S2, respectively. Again the measure µ “ ř

j{2πq´ ř

jď0pδr

j{2π ` δ´r

m{2πq has degree at most 3.

mď0pδs

m{2π ` δ´s

- 6.2. A crystalline measure involving the sum of three squares function r3pnq. Recall that, by Legendre’s three square theorem, a non-negative integer n can be written as the sum of three squares of integers if, and only if, n is not of the form 4ap8b ` 7q for non-negative integers a, b. We deﬁne the arithmetic function r3pnq to be the number of ways of representing n as the sum of three squares of integers, this is, r3pnq :“ #tm P


Z3; |m|22 “ nu. We have r3p0q “ 1 and r3pnq “ 0 if n is of the form 4ap8b`7q. By a result of [11], it holds that, for any positive ε

ÿ

4 3

πx3{2 ` Opx3{4`εq. (18)

r3pnq “

![image 341](<2025-gonalves-complete-classification-fourier-summation_images/imageFile341.png>)

nďx

Working out on an old example of Guinand, Meyer in [23, Thm. 4] constructed the crystalline measure

µ “ ÿ

˘

χpnqr3pnq ?n `

δ?n{2 ´ δ´?n{2

,

![image 342](<2025-gonalves-complete-classification-fourier-summation_images/imageFile342.png>)

![image 343](<2025-gonalves-complete-classification-fourier-summation_images/imageFile343.png>)

![image 344](<2025-gonalves-complete-classification-fourier-summation_images/imageFile344.png>)

![image 345](<2025-gonalves-complete-classification-fourier-summation_images/imageFile345.png>)

jě1

and he proved that µp “ ´iµ. Here, the character χ is deﬁned by

$ ’&

´1{2, if n P Nz4N 4, if n P 4Nz16N 0, if n P 16N.

χpnq “

’%

This gives rise to an FS-pair pµ, ´iµq. Because of (18) and the fact that r3p4nq “ r3pnq, a simple integration-by-parts argument shows that degpµq “ 3.

- 6.3. A generalized family of Guinand’s measure. In the last section of [14], a con-


ś

ně1p1 ´ qnq be Dedekind’s etafunction, where q “ e2πiz and z P C`. Consider now the following family

struction of Guinand’s was generalized. Let ηpzq “ q

1 ´ p24c ´ 2qq ` p288c2 ´ 36cqq2 ` Opq3q˘ “ ÿ

`

ηpzq24c´2ηp4zq24c´2 ηp2zq48c´5

αn,cqn`c, of modular forms for a real number c P r0, 1{8s. Consider then the measure

“ qc

![image 346](<2025-gonalves-complete-classification-fourier-summation_images/imageFile346.png>)

ně0

µc “ ÿ

αn,cpδ?n`c ` δ´?n`cq.

![image 347](<2025-gonalves-complete-classification-fourier-summation_images/imageFile347.png>)

![image 348](<2025-gonalves-complete-classification-fourier-summation_images/imageFile348.png>)

ně0

It is shown in [14] that µp “ µ, that is, pµ, µq is a FS-pair. We note that µ0 “ ř

NPZ δn produces Poisson’s summation and µ1{9 is Guinand’s construction in [15], although he did not came up with his construction this way. We also notice that if c ą 1{8, the

coeﬃcients |αn,c| grow exponentially (but some exceptional values of c) and so pµ, µq is not a FS-pair. However, it still possible to generate a summation formula although only for test functions ϕpxq which extend analytically and decay suﬃciently fast in a strip |Imz| ă b, for a suitable b ą 0. For c P r0, 1{8s, numerical experiments indicate that the coeﬃcients oscillate erratically in the interval r´1, 1s, which nevertheless would imply that |αn,c| ď 1. Provably, the Hecke bound shows that |αn,c| !c n1{4, and so degpµcq ď 3 (and conjecturally degpµcq “ 3).

Acknowledgements. The ﬁrst author acknowledges support from the following funding agencies: The Oﬃce of Naval Research GRANT14201749 (award number N629092412126), The Serrapilheira Institute (Serra-2211-41824), FAPERJ (E-26/200.209/2023) and CNPq (309910/2023-4). The second author is supported by CNPq (141446/2023-4).

Competing interest. The authors have no competing interest to declare. References

- [1] L. Alon, A. Cohen and C. Vinzant, Every real-rooted exponential polynomial is the restriction of a Lee-Yang polynomial. Journal of Functional Analysis (2) 286 (2024).
- [2] L. Alon and C. Vinzant, Gap distributions of Fourier quasicrystals via Lee-Yang polynomials. Rev. Mat. Iberoam. 40 (2024), no. 6, pp. 2203–2250.
- [3] M. Baake, N. Strungaru, A note on tempered measures. Colloquium Mathematicum 172

(2023), 15-30.

- [4] N. Bergeron, The Spectrum of Hyperbolic Surfaces. Springer Cham, 2011 - Universitext - XIII, 370 pages.
- [5] A. S. Besicovitch, Almost Periodic Functions. Dover Publications, 1954 - Fourier series - 180 pages.
- [6] H. Bohr, Zur Theorie der fastperiodischen Funktionen I. Acta Math. 45 (1925), p. 29-127.
- [7] A. Bondarenko, D. Radchenko and K. Seip Fourier Interpolation with Zeros of Zeta and L-Functions Constructive Approximation 57 (2023), p. 405-461.
- [8] A. Dijksma, H. Langer, A. Luger and Yu. Shondin, A factorization result for generalized Nevanlinna functions of the class Nκ, Integr. equ. oper. theory 36 (2000) 121-125.
- [9] K. Daho, H. Langer, Matrix Functions of the Class Nk. Math. Nachr. 120 (1985), no. 1, 275-294.
- [10] L. de Branges, Hilbert spaces of entire functions. Prentice Hall, Englewood Cliﬀs. NJ, 1968.
- [11] S.K.K. Choi, A.V. Kumchev, R. Osburn, On sums of three squares. Int J Number Theory 01

(2005), 161-173.

- [12] H. Cohn, N. Elkies, New upper bounds on sphere packings I. Ann. of Math. (2) 157 (2003), no. 2, 689–714.


- [13] H. Cohn, A. Kumar, S. Miller, D. Radchenko, M. Viazovska, The sphere packing problem in dimension 24. Ann. of Math. (2) 185 (2017), no. 3, 1017–1033.
- [14] F. Gon¸calves, A Classiﬁcation of Fourier Summation Formulas and Crystalline Measures. arXiv:2312.11185.
- [15] A. P. Guinand, Concordance and the harmonic analysis of sequences, Acta Math. 101(3-4): 235271 (1959).
- [16] M.G.Krein, H.Langer, Uber¨ einige Fortsetzungsprobleme, die eng mit der Theorie hermitescher

Operatoren im Raume Πκ zusammenh¨ngen. I. Einige Funktionenklassen und ihre Darstellungen. Math. Nachr. 77 (1977), 187-236.

- [17] M. Kaltenback,¨ H. Woracek, Polya class theory for Hermite-Biehler functions of ﬁnite order. J. London Math. Soc. 68 (2003), no. 2, 338–354.
- [18] P. Kurasov and P. Sarnak, Stable polynomials and crystalline measures, Journal of Mathematical Physics, 61(8):083501, 2020.
- [19] A. Kulikov, F. Nazarov and M. Sodin, Fourier uniqueness and non-uniqueness pairs, Zurnal matematiceskoj ﬁziki, analiza, geometrii (2023).
- [20] N. Lev and A. Olevskii, Fourier quasicrystals and discreteness of the diﬀraction spectrum, Adv. Math. 315 (2017), 1-26.
- [21] N. Lev and A. Olevskii, Quasicrystals and Poisson’s summation formula. Invent. math. 200, 585–606 (2015).
- [22] B. Ja. Levin, Distribution of Zeros of Entire Functions. Translations of Mathematical Monographs Vol. 5, American Mathematical Soc., 1964.
- [23] Y. Meyer, Measures with locally ﬁnite support and spectrum. Proc. Natl. Acad. Sci. USA 113

(2016), 3152–3158.

- [24] H. L. Montgomery, R. C. Vaughan, Multiplicative Number Theory I. Classical Theory. Cambridge studies in advanced mathematics Vol. 97, Cambridge University Press, 2007.
- [25] A. Olevskii and A. Ulanovskii, Fourier quasicrystals with unit masses, Comptes Rendus, Math´ematique, 358(11-12):1207–1211, 2020.
- [26] A. Olevskii and A. Ulanovskii, A simple crystalline measure, arXiv:2006.12037v2 .
- [27] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. IHES 129 (2019), 51–81.
- [28] J. Ramos and M. Sousa, Fourier uniqueness pairs of powers of integers, J. Eur. Math. Soc. (JEMS) 24 (2022), no. 12, 4327-4351.
- [29] J. Ramos and M. Sousa, Perturbed interpolation formular and applications, To appear in Analysis & PDE.
- [30] D. Radchenko, M. Viazovska, Fourier interpolation on the real line. Publ.math.IHES 129, 51–81, (2019).
- [31] M. Viazovska, The sphere packing problem in dimension 8. Ann. of Math. (2) 185 (2017), no. 3, 991–1015.


The University of Texas at Austin, 2515 Speedway, Austin, TX 78712, USA

& IMPA - Instituto de Matematica´ Pura e Aplicada, Rio de Janeiro, 22460-320, Brazil. Email address: goncalves@utexas.edu IMPA - Estrada Dona Castorina 110, Rio de Janeiro, RJ - Brasil, 22460-320 Email address: guilherme.israel@impa.br

