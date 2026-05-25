---
type: source
kind: paper
title: Exploring a planet, revisited
authors: Yufei Zhao
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2110.04376v1
source_local: ../raw/2021-zhao-exploring-planet-revisited.pdf
topic: general-knowledge
cites:
---

arXiv:2110.04376v1[math.MG]8Oct2021

# EXPLORING A PLANET, REVISITED

YUFEI ZHAO

A       . Howshouldwe place greatcirclesona sphereto minimizethefurthestdistancebetween a point on the sphere and its nearest great circle? Fejes Tóth conjectured that the optimum is attained by placing circles evenly spaced all passing through the north and south poles. This conjecture was recently proved by Jiang and Polyanskii. We present a short simpliﬁcation of Ortega-Moreno’s alternate proof of this conjecture.

In a classic 1973 M       Research problems column [5], wonderfully titled Exploring a planet, L. Fejes Tóth asked for the most economical way to explore a planet using satellites. Mathematically, the problem asks to place great circles on a sphere to minimize the furtherest distance between a point on the sphere and its nearest great circle. He conjectured that the optimal conﬁguration has evenly spaced great circles all passing through the north and south poles, which he equivalently stated as:

If equal zones cover the sphere then their width is at least / . Here a zone of width is deﬁned as the parallel domain of a great circle of distance /2.

This “zone conjecture” is a spherical analog of Tarski’s plank problem from the 1930’s, which asks to show that any covering of a ball by planks (a plank is the space between two parallel hyperplanes) must use planks of total width at least the diameter of the ball [10]. Tarski gave a beautiful proof of the problem in dimensions 2 and 3 (see the introduction of [8] for an exposition of Tarski’s proof, which relies on an observation by Archimedes). The problem in all dimensions was settled some twenty years later by Bang [2, 3] in a stunning proof. See [4, Section 3.4] for a survey of related problems.

Fejes Tóth’s zone conjecture was recently proved in a beautiful paper of Jiang and Polyanskii [7]. Ortega-Moreno [9], apparently unaware of Jiang and Polyanskii’s work, found another very nice proof of the conjecture. Amazingly, these two proofs are completely diﬀerent! They both prove the result in arbitrary dimensions. The Jiang–Polyanskii proof builds on the ideas of Bang [3] and Goodman and Goodman [6], and it allows zones of diﬀerent widths. Ortega-Moreno’s proof, however, is inspired by Ball’s solution to the complex plank problem [1] and uses inverse eigenvectors and trignometric polynomials, though it only works for equal-width zones.

Here we give a streamlined presentation of Ortega-Moreno’s proof. His proof starts by reformulating the problem in terms of inverse eigenvectors. We eliminate the need to discuss inverse eigenvectors, thereby giving a shorter and more direct proof.

The problem in R is equivalent to showing that given hyperplanes through the origin in R , there is always a point on the unit sphere with distance at least sin 2 to every hyperplane. Let to prove the following.

![image 1](<2021-zhao-exploring-planet-revisited_images/imageFile1.png>)

- 1, . . .,   be the unit normal vectors to the hyperplanes. By compactness of the sphere, it suﬃces


1

- 2 YUFEI ZHAO


= /2

locus( )

< 2

![image 2](<2021-zhao-exploring-planet-revisited_images/imageFile2.png>)

1

/(2 )

= 0

- = 3

- cos 3

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |


0 2

= 4

- cos 4




| | | | | | |
|---|---|---|---|---|---|
| | | | | | |


0 2

(L   ) The vectors used in the proof. (R    ) The dotted points are known values of ( ) overlaid on the plot of cos . Since | ( )| < 1 for all ∉ Z , the intermediate value theorem shows that ( ) and cos have at least 2 − 4 additional crossings in [0, 2 ), not counting the ones drawn.

Theorem. Let 1, . . .,   be unit vectors in R . If maximizes =1 |  ,   | among unit vectors, then |  ,   | ≥ sin 2 for all .

![image 3](<2021-zhao-exploring-planet-revisited_images/imageFile3.png>)

Proof. Suppose for contradiction that |  1,   | < sin 2 (note that |  1,   | > 0 due to the choice of ) . Then (see left ﬁgure) in the 2-dimensional plane spanned by { ,  1}, we can take a vector

![image 4](<2021-zhao-exploring-planet-revisited_images/imageFile4.png>)

⊥ with | | < 1 such that, setting

:= (cos ) + (sin ) , one has /(2 ) ⊥ 1 (picture what happens when | | = 1, and then shorten ). Let ( ) =

,   ,  

.

![image 5](<2021-zhao-exploring-planet-revisited_images/imageFile5.png>)

=1

We have + = − and so ( + ) = (−1) ( ). Let us focus on the domain ∈ [0,  ). Since

0 = , wehave (0) = 1. Since 1 ⊥ /(2 ), we have (2 ) = 0. So ( ) = cos for ∈ {0, 2 }. Since | | < 1, for any ∈ (0,  ) we have | | < 1 and thus | ( )| < 1 by the maximality hypothesis on . So ( ) −cos has sign changes at = / , 2 / , . . ., ( −1) / (where cos alternates between ±1), and thus it has at least − 2 distinct zeros in ( / , ( − 1) / ). Combining with the two additional zeros at = 0,  /(2 ), we see that ( ) − cos has at least distinct zeros in [0,  ), and hence at least 2 distinct zeros in [0, 2 ) (see right ﬁgure).

![image 6](<2021-zhao-exploring-planet-revisited_images/imageFile6.png>)

![image 7](<2021-zhao-exploring-planet-revisited_images/imageFile7.png>)

Expanding, for some trignometric polynomial 1( ) of degree at most − 2, ( ) =

, (cos ) + (sin ) ,  

,   ,  

cos −1 sin + sin2 1( ).

= cos +

![image 8](<2021-zhao-exploring-planet-revisited_images/imageFile8.png>)

![image 9](<2021-zhao-exploring-planet-revisited_images/imageFile9.png>)

=1

=1

We saw in the previous paragraph that ( ) is maximized at = 0, and thus

0 = ′(0) =

,   ,  

.

![image 10](<2021-zhao-exploring-planet-revisited_images/imageFile10.png>)

=1

So the second term in the expansion of ( ) above is zero. Thus ( ) − cos = cos + sin2 1( ) − cos = sin2 2( ),

for some trignometric polynomial 2( ) of degree at most − 2. So ( ) − cos = sin2 2( ) has at most 2 − 2 distinct zeros in [0, 2 ), contradicting the earlier claim.

EXPLORING A PLANET, REVISITED 3

Acknowledgments. The author thanks the referees and the editor for helpful comments.

The author was supported by NSF award DMS-1764176, NSF CAREER award DMS-2044606, a Sloan Research Fellowship, and the MIT Solomon Buchsbaum Fund.

R         

- [1] Keith M. Ball, The complex plank problem, Bull. London Math. Soc. 33 (2001), 433–442.
- [2] Thøger Bang, On covering by parallel-strips, Mat. Tidsskr. B 1950 (1950), 49–53.
- [3] Thøger Bang, A solution of the “plank problem.”, Proc. Amer. Math. Soc. 2 (1951), 990–993.
- [4] Peter Brass, William Moser, and János Pach, Research problems in discrete geometry, Springer, 2005.
- [5] L. Fejes Toth, Research problems: Exploring a planet, Amer. Math. Monthly 80 (1973), 1043–1044.
- [6] A. W. Goodman and R. E. Goodman, A circle covering theorem, Amer. Math. Monthly 52 (1945), 494–498.
- [7] Zilin Jiang and Alexandr Polyanskii, Proof of László Fejes Tóth’s zone conjecture, Geom. Funct. Anal. 27 (2017), 1367–1377.
- [8] Andrey Kupavskii and János Pach, From Tarski’s plank problem to simultaneous approximation, Amer. Math. Monthly 124 (2017), 494–505.
- [9] Oscar Ortega-Moreno, An optimal plank theorem, Proc. Amer. Math. Soc. 149 (2021), 1225–1237.
- [10] Alfred Tarski, Uwagi o stopniu równoważności wielokątów [Remarks on the degree of equivalence of polygons], Parametr 2 (1932), 310–314.


D          M          , M             I         T         , C        , MA 02139, USA Email address: yufeiz@mit.edu

