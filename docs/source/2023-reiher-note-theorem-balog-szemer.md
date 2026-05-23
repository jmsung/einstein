---
type: source
kind: paper
title: Note on the Theorem of Balog, Szemerédi, and Gowers
authors: Christian Reiher, Tomasz Schoen
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2308.10245v2
source_local: ../raw/2023-reiher-note-theorem-balog-szemer.pdf
topic: general-knowledge
cites:
---

## NOTE ON THE THEOREM OF BALOG, SZEMERÉDI, AND GOWERS

CHRISTIAN REIHER AND TOMASZ SCHOEN

Abstract. We prove that every additive set A with energy EpAq ě |A|3{K has a subset A1 Ď A of size |A1| ě p1´εqK´1{2|A| such that |A1´A1| ď OεpK4|A1|q. This is, essentially, the largest structured set one can get in the Balog-Szemerédi-Gowers theorem.

# arXiv:2308.10245v2[math.CO]18Feb2024

§1. Introduction

An additive set is a nonempty finite subset of an abelian group. The energy of an additive set A is defined to be the number EpAq of quadruples pa1,a2,a3,a4q P A4 solving the equation a1 ` a2 “ a3 ` a4. An easy counting argument shows

EpAq “ ÿ

rA´Apdq2 , (1.1)

dPA´A

where rA´Apdq indicates the number of representations of d as a difference of two members of A. So the Cauchy-Schwarz inequality yields EpAq ě |A|4{|A ´ A| and, in particular, every additive set A with small difference set A ´ A contains a lot of energy. In the converse direction Balog and Szemerédi [2] proved that large energy implies the existence of a substantial subset whose difference set is small. After several quantitative improvements (see e.g., Gowers [3] and Balog [1]) the hitherto best version of this result was obtained by the second author [4].

Theorem 1.1. Given a real K ě 1 every additive set A with energy EpAq ě |A|3{K has a subset A1 Ď A of size |A1| ě Ωp|A|{Kq such that |A1 ´ A1| ď OpK4|A1|q. □

When investigating the question how a quantitatively optimal version of this result might read, there are two different directions one may wish to pursue. First, there is the obvious problem whether the exponent 4 can be replaced by some smaller number. Second, one may try to find “the largest” set A1 Ď A such that |A1 ´ A1| ď OKp|A1|q holds. As the following example demonstrates, there is no absolute constant ε‹ ą 0 such that |A1| ě p1 ` ε‹qK´1{2|A| can be achieved in general.

Fix an arbitrary natural number n. For a very large finite abelian group G we consider the additive set

A “ ␣pg1,...,gnq P Gn: there is at most one index i such that gi ‰ 0

(

1

whose ambient group is Gn. Obviously we have

|A| “ |G|n ` Onp1q and EpAq “ |A|3{n2 ` Onp|A|2q, so the real number K satisfying EpAq “ |A|3{K is roughly n2. However, every A1 Ď A of size |A1| ě p1 ` εq|G| satisfies |A1 ´ A1| ě ε2|G|2. Our main result implies that this is, in some sense, already the worst example. More precisely, for every fixed ε ą 0 the Balog-Szemerédi-Gowers theorem holds with |A1| ě p1 ´ εqK´1{2|A|. Perhaps surprisingly, we can also reproduce the best known factor K4.

Theorem 1.2. Given real numbers K ě 1, ε P p0,1{2q, and an additive set A with energy EpAq ě |A|3{K there is a subset A1 Ď A such that

|A1| ě p1 ´ εqK´1{2|A| and |A1 ´ A1| ď 233ε´9K4|A1| “ OεpK4|A1|q.

Our proof has two main cases and in one of them (see Lemma 3.1 below) we even get the stronger bound |A1 ´ A1| ď OεpK3|A1|q. It would be interesting to prove this in the second case as well. Using examples of the form A “ tx P Zd: }x} ď Ru one can show that the exponent 4 cannot be replaced by any number smaller than logp4q{logp27{16q « 2.649 (see [5]).

§2. Preliminaries

This section discusses two auxiliary results we shall require for the proof of Theorem 1.2. The first of them is similar to [6, Lemma 6.19].

- Lemma 2.1. If δ,ξ P p0,1s and R Ď A2 denotes a binary relation on a set A such that |R| ě δ|A|2, then there is a set A1 Ď A of size |A1| ě δp1 ´ ξq|A| which possesses the following property: For every pair pa1,a2q P A12 there are at least 2´7δ4ξ4|A|2|A1| triples px,b,yq P A3 such that pa1,xq,pb,xq,pb,yq,pa2,yq P R.


ř

Proof. Set Npxq “ ta P A: pa,xq P Ru for every x P A. Since

xPA |Npxq| “ |R| ě δ|A|2, the Cauchy-Schwarz inequality yields

ÿ

|Npxq|2 ě δ2|A|3 . (2.1)

xPA

Setting Kpa,a1q “ tx P A: a,a1 P Npxqu for every pair pa,a1q P A2 and Ω “ ␣pa,a1q P A2: |Kpa,a1q| ď δ2ξ2|A|{8

(

a double counting argument yields ÿ

|Npxq2 X Ω| “ ÿ

|Kpa,a1q| ď δ2ξ2|A||Ω|{8 ď δ2ξ2|A|3{8.

pa,a1qPΩ

xPA

- Together with (2.1) we obtain ÿ


`|Npxq|2 ´ 8ξ´1|Npxq2 X Ω|˘ ě δ2p1 ´ ξq|A|3

xPA

and, hence, there exists some x‹ P A such that the set A‹ “ Npx‹q satisfies

|A‹|2 ´ 8ξ´1|A2‹ X Ω| ě δ2p1 ´ ξq|A|2 . (2.2) We shall prove that the set

A1 “ ta P A‹: the number of all a1 P A‹ with pa,a1q P Ω is at most |A‹|{4u has all required properties. By (2.2) we have

|A‹ ∖ A1||A‹|{4 ď |A2‹ X Ω| ď ξ|A‹|2{8, for which reason

(2.2)

|A1| ě p1 ´ ξ{2q|A‹| ě p1 ´ ξq1{2|A‹|

ě δp1 ´ ξq|A|, meaning that A1 is indeed sufficiently large. To conclude the proof we need to show ÿ

|Kpa1,bq ˆ Kpb,a2q| ě 2´7δ4ξ4|A|2|A1|

bPA

for every pair pa1,a2q P A12. This follows from the fact that due to the definition of A1 there are at least |A‹|{2 elements b P A‹ such that the sets Kpa1,bq and Kpb,a2q both have at least the size δ2ξ2|A|{8. □

- Lemma 2.2. Suppose that the real numbers x1,...,xn P r0,1s do not vanish simultaneously. Denote their sum by S and the sum of their squares by T. For every α P p0,1q there exists a set I Ď rns such that


xi ě max #αT,ˆp1 ´ αq5|I|4T4 210S2

˙1{6+ .

ÿ

iPI

Proof. For reasons of symmetry we may assume x1 ě ¨¨¨ ě xn. Set Si “ ři

j“1 xj for every nonnegative i ď n. Due to T ď x1S and x1 ď 1 we have T ď S “ Sn and thus there exists a smallest index k P rns satisfying Sk ě αT. Notice that

kÿ´1

kÿ´1

x2i ď

xi “ Sk´1 ď αT .

i“1

i“1

Moreover x1 ě T{S implies the existence of a largest index ℓ such that xℓ ě p1´αqT{p2Sq. Due to

p1 ´ αqT 2

p1 ´ αqT 2S

ÿn

ÿn

x2i ď

xi ď

,

i“ℓ`1

i“ℓ`1

we have

p1 ´ αqT 2

ÿℓ

x2i ě

, (2.3) whence, in particular, ℓ ě k. Next,

i“k

ℓˆp1 ´ αqT 2S

˙2 ď

ÿℓ

x2i ď T entails

i“1

p1 ´ αq2ℓT ď 4S2 . (2.4) Now assume for the sake of contradiction that our claim fails. Every i P rk,ℓs satisfies

Si ě Sk ě αT and thus the failure of I “ ris discloses

˙1{6 . Combined with ixi ď Si this entails

Si ă ˆp1 ´ αq5i4T4 210S2

x2i ď ˆp1 ´ αq5T4

˙1{3 ÿℓ

ÿℓ

i´2{3 .

210S2

i“k

i“k

In view of (2.3) we are thus led to ˆ

˙1{3 ď

i´2{3 ď ż ℓ

27S2 p1 ´ αq2T

ÿℓ

x´2{3dx “ 3ℓ1{3 ,

0

i“k

i.e., 27S2 ď 27p1 ´ αq2ℓT, which contradicts (2.4). □ §3. The proof of Theorem 1.2

Let us fix two real numbers K ě 1 and ε P p0,1{2q as well as an additive set A satisfying EpAq ě |A|3{K. We consider the partition

A ´ A “ P ¨Y Q defined by

d P A ´ A: rA´Apdq ě K´1{2|A|( and Q “ ␣

P “ ␣

d P A ´ A: rA´Apdq ă K´1{2|A|(

. According to (1.1) at least one of the cases

p4 ´ εq|A|3 4K

ε|A|3 4K

ÿ

ÿ

rA´Apdq2 ě

rA´Apdq2 ě

or

(3.1)

dPP

dPQ

needs to occur and we begin by analysing the left alternative. ř

## Lemma 3.1. If

dPP rA´Apdq2 ě ε|A|3{p4Kq, then there exists a set A1 Ď A of size |A1| ě p1 ´ εqK´1{2|A| such that |A1 ´ A1| ď 210ε´4K3|A1|.

Proof. For every difference d P P we set Ad “ A X pA ` dq. Due to |Ad| “ rA´Apdq the hypothesis implies

ÿ

|Ad|2 ě ε|A|3{p4Kq. (3.2)

dPP

For every pair px,yq P A2 the set Lpx,yq “ td P P : x,y P Adu has at most the cardinality |Lpx,yq| ď rA´Apx ´ yq, because every difference d P Lpx,yq corresponds to its own representation x ´ y “ px ´ dq ´ py ´ dq of x ´ y as a difference of two members of A. Applying this observation to all pairs in

Ξ “ ␣px,yq P A2: rA´Apx ´ yq ď ε2|A|{p16Kq( we obtain

ε2|A||Ξ| 16K ď

ε2|A|3 16K

ÿ

|A2d X Ξ| “ ÿ

|Lpx,yq| ď ÿ

rA´Apx ´ yq ď

.

px,yqPΞ

px,yqPΞ

dPP

- Together with (3.2) this yields ÿ


`

ε|A2d| ´ 4|A2d X Ξ|˘ ě 0

dPP

and, consequently, for some element dp‹q P P the set A‹ “ Adp‹q satisfies |A2‹XΞ| ď ε|A‹|2{4. We contend that the set

A1 “ ␣

(

a P A‹: There are at most |A‹|{4 pairs of the form pa,xq in Ξ

has the required properties. As in the proof of Lemma 2.1 we obtain

|A1| ě p1 ´ εq|A‹| “ p1 ´ εqrA´Apdp‹qq ě p1 ´ εqK´1{2|A|; so it remains to derive the required upper bound on |A1 ´ A1|.

To this end we consider an arbitrary pair pa,a1q of elements of A1. Owing to the definition of A1 there are at least |A‹|{2 elements x P A‹ such that pa,xq R Ξ and pa1,xq R Ξ. For each of them we have a ´ a1 “ pa ´ xq ´ pa1 ´ xq, there are at least ε2|A|{p16Kq pairs pa1,a2q P A2 solving the equation a ´ x “ a1 ´ a2 and at least the same number of pairs pa3,a4q P A2 such that a1 ´ x “ a3 ´ a4. Altogether there are at least

ε4|A|2|A‹|{p29K2q ě 2´9ε4K´5{2|A|3 possibilities of writing a ´ a1 “ pa1 ´ a2q ´ pa3 ´ a4q and for this reason we have |A1 ´ A1| ď

|A|4 2´9ε4K´5{2|A|3

“ 29ε´4K5{2|A| ď 210ε´4K3|A1|. □ We conclude the proof of Theorem 1.2 by taking care of the right case in (3.1).

ř

Lemma 3.2. If

dPQ rA´Apdq2 ě p1 ´ ε{4q|A|3{K, then there is a set A1 Ď A of size |A1| ě p1 ´ εqK´1{2|A| such that |A1 ´ A1| ď 233ε´9K4|A1|.

Proof. Let Q “ td1,...,d|Q|u enumerate Q. By the definition of Q there are real numbers x1,...,x|Q| P r0,1s such that

rA´Apdiq “ xiK´1{2|A| holds for every i P r|Q|s. Owing to

ř

dPA´A rA´Apdq “ |A|2 and the hypothesis we have ÿ|Q|

ÿ|Q|

x2i ě p1 ´ ε{4q|A|.

xi ď K1{2|A| as well as

i“1

i“1

By Lemma 2.2 applied with α “ 1 ´ ε{4 there exist an index set I Ď r|Q|s such that ÿ

xi ě max !p1 ´ ε{2q|A|,

2´21ε5K´1|I|4|A|2˘1{6) . (3.3)

`

iPI

Now we set Q1 “ tdi: i P Iu, consider the relation

R “ tpa1,a2q P A2: a1 ´ a2 P Q1u and define δ P p0,1s by |R| “ δ|A|2. Due to

1 K1{2|A|

ÿ

δ “ |A|´2 ÿ

rA´Apdiq “

xi

iPI

iPI

the bounds in (3.3) imply both

δ ě p1 ´ ε{2qK´1{2 and |I|4 δ6|A|4

ď 221ε´5K4 . (3.4)

By Lemma 2.1 applied to ξ “ ε{2 and R there exists a set A1 Ď A of size |A1| ě p1 ´ ε{2qδ|A| ě p1 ´ εqK´1{2|A|

such that for every pair pa1,a2q P A12 there are at least 2´11ε4δ4|A|2|A1| triples px,b,yq P A3 with pa1,xq,pb,xq,pb,yq,pa2,yq P R. Due to the equation

pa1 ´ a2q “ pa1 ´ xq ´ pb ´ xq ` pb ´ yq ´ pa2 ´ yq

this means that every difference a1´a2 P A1´A1 has at least 2´11ε4δ4|A|2|A1| representations of the form q1 ´ q2 ` q3 ´ q4 with q1,q2,q3,q4 P Q1, whence

|Q1|4 2´11ε4δ4|A|2|A1|

(3.4)

ď 232ε´9K4pδ|A|{|A1|q2|A1|.

|A1 ´ A1| ď

?2 the result follows. □

Due to |A1| ě p1 ´ ε{2qδ|A| ě δ|A|{

Acknowledgement. We would like to thank the referees for reading our article very carefully.

References

- [1] A. Balog, Many additive quadruples, Additive combinatorics, CRM Proc. Lecture Notes, vol. 43, Amer. Math. Soc., Providence, RI, 2007, pp. 39–49, DOI10.1090/crmp/043/03. MR2359466 Ò1

- [2] A. Balog and E. Szemerédi, A statistical theorem of set addition, Combinatorica 14 (1994), no. 3, 263–268, DOI10.1007/BF01212974. MR1305895 Ò1

- [3] W. T. Gowers, A new proof of Szemerédi’s theorem for arithmetic progressions of length four, Geom. Funct. Anal. 8 (1998), no. 3, 529–551, DOI10.1007/s000390050065. MR1631259 Ò1

- [4] T. Schoen, New bounds in Balog-Szemerédi-Gowers theorem, Combinatorica 35 (2015), no. 6, 695–701, DOI10.1007/s00493-014-3077-4. MR3439793 Ò1

- [5] X. Shao, Large values of the additive energy in Rd and Zd, Math. Proc. Cambridge Philos. Soc. 156

(2014), no. 2, 327–341, DOI10.1017/S0305004113000741. MR3177873 Ò1

- [6] T. Tao and V. Vu, Additive combinatorics, Cambridge Studies in Advanced Mathematics, vol. 105, Cambridge University Press, Cambridge, 2006. MR2289012 Ò2


Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany Email address: Christian.Reiher@uni-hamburg.de

A. Mickiewicz University, Department of Discrete Mathematics, Poznań, Poland Email address: schoen@amu.edu.pl

