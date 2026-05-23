---
type: source
kind: paper
title: Buffon Discrepancy and the Steinhaus Longimeter
authors: Stefan Steinerberger
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2603.27807v1
source_local: ../raw/2026-steinerberger-buffon-discrepancy-steinhaus-longimeter.pdf
topic: general-knowledge
cites:
---

# arXiv:2603.27807v1[math.CA]29Mar2026

## BUFFON DISCREPANCY AND THE STEINHAUS LONGIMETER

STEFAN STEINERBERGER

Abstract. Let Ω ⊂ R2 be a convex set. We study the problem of distributing a one-dimensional set S with total length L so that for any line ℓ in R2 the number of intersections #(ℓ ∩ S) is proportional to the length H1(ℓ ∩ Ω) as much as possible; we use the term Buffon discrepancy for the largest error. A construction of Steinhaus can be generalized to prove the existence of sets with Buffon discrepancy ≲ L1/3. We also show that the unit disk D admits a set with uniformly bounded Buffon discrepancy as L → ∞.

1. Introduction

1.1. The problem. The goal of this paper is to present an interesting problem: we are given a bounded, convex domain Ω ⊂ R2. The goal is to find, for any given L > 0, a one-dimensional set S ⊂ Ω with length L so that the following is true: for any line ℓ in R2 the number of intersections #(ℓ ∩ S) is proportional (as much as possible) to the length of the line inside Ω, that is H1(ℓ∩Ω). The obvious questions are: how can this be made precise, how well can it be done and what do extremal sets S look like? Computational experiments (see Fig. 1) suggest that the answer to these questions might be quite interesting; the question is also of obvious interest in higher dimensions; this paper is solely focused on the case of two dimensions.

Figure 1. Sets of lines of length L = 500 inside the unit disk (left) and the Reuleaux triangle (right) with the property that every line through the domain intersects them a number of times roughly proportional to the length (with a fairly small error).

1

- 1.2. Buffon discrepancy. We start by motivating the quantity of interest. Asking for the number of intersections to be proportional introduces two variables: (a) the proportionality factor and (b) the worst case error assuming that proportionality factor. It is clear that these two numbers (denoted c and X in the subsequent Proposition) are highly connected and maybe one does not wish to deal with both at the same time. Our first observation is that there exists a somewhat canonical proportionality factor c suggested by the Cauchy-Crofton formula.


Proposition (Cauchy-Crofton scaling). Let Ω ⊂ R2 be bounded, let S be a set with length H1(S) = L having the property that for some c > 0 and all lines ℓ in R2

#(ℓ ∩ S) − c · H1(ℓ ∩ Ω) ≤ X, then

2 · diam(Ω) area(Ω)

2 π

L area(Ω) ≤

c −

X.

Since we are mainly interested in the asymptotic regime L ≫ X, the Proposition suggests to prescribe the proportionality factor as 2L/(π · area(Ω)). We use this as our starting point to define Buffon discrepancy.

Definition. Let Ω ⊂ R2 be a bounded set in the plane and let S ⊂ Ω be a rectifiable set with length L. We define the Buffon discrepancy of S (with respect to Ω) as

2 π

L area(Ω)H1(ℓ ∩ Ω)

#(ℓ ∩ S) −

,

L∞(µ)

where µ is the kinematic measure and ℓ ranges over all lines.

Note that if the set S were to contain a line segment, then there exists a line ℓ such that #(ℓ ∩ S) = ∞. One could replace line segments by slightly curved segments and take a limit but presumably the more natural way out is to exclude ‘exceptional lines of measure 0’ and this is done by the use of the kinematic measure; recall the formal definition of the L∞−norm as

∥f∥L∞(µ) = inf {C ≥ 0 : |f(x)| ≤ C for µ almost every x} which encapsulates the idea that individual lines as well as sets of lines with measure 0 do not matter.

2000 line segments S with total length L = 500

the red line ℓ intersects #(ℓ ∩ S) = 160 segments and has length H1(ℓ) ∼ 1.769

160 − 2πL2 · 1.769 ∼ 19.24

Figure 2. A set with length L = 500 in the unit disk and a line showing that the Buffon discrepancy of the set is ≥ 19.24.

There exists a trivial lower bound: for fixed Ω as L → ∞, we observe that the intersection #(ℓ ∩ S) is always integer-valued while the length of all chords assume intermediate real values; in general, we always have a trivial bound

2 π

- 1

- 2


L area(Ω)H1(ℓ ∩ Ω)

#(ℓ ∩ S) −

≥

. As it turns out, this trivial lower bound is optimal in the case of the unit disk.

L∞(µ)

- 1.3. Unit Disk. The unit disk D is a natural first example. We prove the existence of a very simple set, a union of suitably placed concentric circles, with uniformly bounded Buffon discrepancy.

- Theorem 1. For any L > 0 there exists a set S ⊂ D with total length L with


max

ℓ

#(ℓ ∩ S) −

2L π2 H1(ℓ ∩ D) ≤ 100.

Figure 3. Two sets of line segments with total length L = 500 inside the unit disk with very small Buffon discrepancy.

It seems, see Fig. 1 and Fig. 3, that there are different types of sets inside the unit disk that have a small Buffon discrepancy. The union of concentric circles is arguably the simplest one; however, it might be interesting to see if it is possible to construct other examples of such sets.

- 1.4. The Steinhaus longimeter. This type of problem appears to be very naturally related to a construction first proposed (and patented!) by Hugo Steinhaus [23, 24, 25, 26]. His 1930 paper On the practice of rectification and notion of length [23] begins by saying that


This note belongs to the area of applied mathematics. It proposes a method which allows the optical measurement of physically given curves. The term ‘optical’ should highlight the distinction between our method and the mechanical [...] There are many conceivable cases where a mechanical device cannot be used. [...] for example if one wants to measure the length of a string-like curved object under the microscope [...] (Steinhaus, [23])

One of the applications he has in mind is measuring the length of objects on a map as is also explained in his 1931 publication in Czasopismo Geograficzne (Geographic Journal) [24]. Steinhaus first explains the usual proof of the Crofton formula and then notes that the proof allows for a discretization: taking 6 lines with an angle of 30 degrees between them and all their translates, Steinhaus notes that the number of intersections between this union of lines and any line segment is nearly proportional to the length of the line segment up to an error between −2.26% and 1.15%. More generally, let Sn,ε denote n lines going through the origin at an equal angle together with all translates by ε,

t + −sin(πk/n) cos(πk/n)

cos(πk/n) sin(πk/n)

sε : t ∈ R, s ∈ Z, 0 ≤ k < n .

Sn,ε =

The set S1,ε is the union of lines parallel to the x−axis while S2,ε is the familiar grid and S3,ε leads to a hexagonal structure. The standard (patented) Steinhaus longimeter construction corresponds to S6,ε.

Figure 4. The sets Sn,1/5 for 1 ≤ n ≤ 5.

We will now argue that this generalized Steinhaus longimeter provides a universal bound for our problem: as L → ∞, the set Sn,ε ∩ Ω, for suitable n,ε, is a set with small Buffon discrepancy.

- Theorem 2. Let Ω ⊂ R2 be a bounded, convex domain. Then there exists cΩ such that, as L → ∞, the set S = Ω ∩ SL1/3,L−2/3 has length H1(S) ∼ L and


2 π

L area(Ω)H1(ℓ ∩ Ω)

≤ cΩ · L1/3.

#(ℓ ∩ S) −

L∞(µ)

It is not difficult to see that this result is sharp: the set Ω could be oriented so that the origin (0,0) ∈ ∂Ω. However, the Steinhaus set Sn,ε has the property that n lines meet at the origin, therefore this bound is the best one can hope for when n ∼ L1/3. One might naturally wonder whether it is possible to avoid this worst case scenario by suitably moving and rotating the set Ω, perhaps an additional averaging procedure can lead to a further improvement.

- 1.5. Open problems. These two results, a uniformly bounded Buffon discrepancy for the unit disk and a bound of L1/3 for general convex sets, naturally suggest a number of different questions. We only list some of the more obvious ones.


- (1) Is it always possible to find a set with Buffon discrepancy of order ∼ 1 for any convex domain? If so, is there a simple construction? If not, what is the best Buffon discrepancy one can hope for?
- (2) Is it possible to find other explicit examples with Buffon discrepancy of order ∼ 1 for the unit disk? Fig.1 and Fig. 3 show numerically obtained examples suggesting their existence.


- (3) What happens if we were to restrict ourselves to only working with sets S that are a union of intersections of lines with Ω? This would include all Steinhaus sets but would eliminate examples like Fig. 3. Would this fundamentally change the problem?
- (4) What about the analogous problem in higher dimensions? Note that, for example in R3, there are at least two separate problems depending on whether ‘lines’ are understood to be lines or sets of co-dimension 1.


Figure 5. Construction in the style of the Steinhaus longimeter.

It appears as if Steinhaus sets are a fairly natural starting point when it comes to the construction of optimal sets; there are several natural variations one might want to consider, for example, we defined them to all meet in the origin but one could add an offset to each individual line to avoid this cluster. A second interesting aspect is that the Steinhaus sets Sn,ε, especially for n large and ε small, have a fairly intriguing micro-structure (see, Fig. 6 and Fig. 7). There are regions that appear fairly random, there are obvious clusters where many lines meet and there are some relatively empty regions. Theorem 2 suggests that Sn,1/n2 for n ∈ N might be a particularly interesting subfamily.

![image 1](<2026-steinerberger-buffon-discrepancy-steinhaus-longimeter_images/imageFile1.png>)

Figure 6. Microstructures in S50,1/2500.

- 1.6. Related results. We are not aware of any directly related results in integral geometry [22]. Our problem can be understood in the spirit of discrepancy theory, see Beck-Chen [4], Chazelle [6], Drmota-Tichy [10], Kuipers-Niederreiter [15] and Matousek [19]. Indeed, it could be interpreted as the problem finding a suitable discretization of kinematic measure restricted to a domain, however, we know of no work in that direction. The Steinhaus longimeter has had profound impact in stereology, the study of how to extract information from lower-dimensional sets, we refer to [3, 5, 7, 8, 9, 11, 12, 13, 16]. A related result is due to Liu-Zhang-ZhengPaul [17]: they use a low-discrepancy sequence on the sphere to create ‘uniformly distributed’ lines, though, in their setup the goal is surface estimation of an a priori unknown object. This has since been further pursued [14, 21], however, it is really a different problem. We also note the existence of the work of Ambartzumian [1, 2] which, again, seems to be of a very different flavor.


## 2.1. Proof of the Proposition.

2. Proofs

Proof. Since Ω is bounded, we may assume without loss of generality that it is contained in a ball of radius R centered at the origin, i.e. Ω ⊂ B(0,R). We will now consider the set of all lines ℓ that intersect this ball which we can identify with the interval [−R,R] × S1 equipped with the usual product measure: this identifies each line with the angle that it makes with the x−axis (or any other fixed reference direction) as well as the closest (signed) distance it has with the origin. By choosing the product measure, the arising measure is invariant under rotation and translation. This set has total measure 2R × 2π = 4Rπ. Since the set S is rectifiable, we may think of it as a union of finitely many line segments; we first argue that linearity gives that

R

2π

#(ℓ ∩ S)dxdθ = 4L.

−R

0

This can be seen as follows: if S is a line segment of length ε, then the size of its projection depends on the angle α between the projection direction and the orientation of the line segment and evaluates to |cosα|ε. In that case,

R

2π

2π

R

2π

#(ℓ ∩ S)dxdθ =

|cosα|εdα = 4ε.

#(ℓ ∩ S)dxdθ =

−R

−R

0

0

0

Since the integral is additive, we arrive at the desired conclusion. Simultaneously, by Fubini, we have

R

−R

2π

H1(ℓ ∩ Ω)dxdθ =

0

=

2π

R

H1(ℓ ∩ Ω)dxdθ

−R

0

2π

area(Ω)dθ = 2π · area(Ω).

0

If it is now true that for some c,X > 0 and all lines ℓ we have that #(ℓ ∩ S) − c · H1(ℓ ∩ Ω) ≤ X,

then the triangle inequality implies

2π

R

#(ℓ ∩ S) − c · H1(ℓ ∩ Ω)dxdθ

|4L − c · 2π · area(Ω)| =

−R

0

2π

R

#(ℓ ∩ S) − c · H1(ℓ ∩ Ω) dxdθ ≤ 4πRX. Dividing both sides by 2πarea(Ω) now leads to

≤

−R

0

2 π

2R area(Ω)

L area(Ω) ≤

c −

X. Using R ≤ diam(Ω) implies the result. □

![image 2](<2026-steinerberger-buffon-discrepancy-steinhaus-longimeter_images/imageFile2.png>)

![image 3](<2026-steinerberger-buffon-discrepancy-steinhaus-longimeter_images/imageFile3.png>)

![image 4](<2026-steinerberger-buffon-discrepancy-steinhaus-longimeter_images/imageFile4.png>)

![image 5](<2026-steinerberger-buffon-discrepancy-steinhaus-longimeter_images/imageFile5.png>)

![image 6](<2026-steinerberger-buffon-discrepancy-steinhaus-longimeter_images/imageFile6.png>)

Figure 7. Pictures at an exhibition: S50,1/2500 at small scale.

## 2.2. Proof of Theorem 1.

Proof. We consider a union of circles centered at the origin. More precisely, given radii 0 < r1 < r2 < ··· < rk ≤ 1, we consider the set

k

x ∈ R2 : ∥x∥ = ri . The length of this set is supposed to be L, this requires

S =

i=1

L 2π

r1 + r2 + ··· + rk =

.

For any arbitrary line ℓ, we consider its closest approach to the origin, i.e. d(ℓ) = minx∈ℓ ∥x∥. Then

H1(ℓ ∩ D) = 2 1 − d(ℓ)2. Simultaneously, we have that, except for a set of kinematic measure 0

#(S ∩ ℓ) = 2 · #{1 ≤ i ≤ k : d(ℓ) ≤ ri}. The exceptional set of lines is exactly the set of lines that is tangent to one of the k circles and this tells us that for all lines

|#(S ∩ ℓ) − 2 · #{1 ≤ i ≤ k : d(ℓ) ≤ ri}| ≤ 1.

We arrive at the bound #(ℓ ∩ S) −

2L π2 H1(ℓ ∩ D)

2L π2 H1(ℓ ∩ D) ≤ 1 + 2 · #{1 ≤ i ≤ k : d(ℓ) ≤ ri} −

2L π2

1 − d(ℓ)2 .

≤ 1 + 2 #{1 ≤ i ≤ k : d(ℓ) ≤ ri} −

The line ℓ has been reduced to a number 0 < d(ℓ) < 1 and it remains to find a suitable k ∈ N and a suitable set of k radii r1 < r2 < ··· < rk subject to the boundary conditions indicated above such that

2L π2

#{1 ≤ i ≤ k : ri ≥ r} −

max

0<r<1

1 − r2 is small.

This is merely the problem of discretizing a non-uniform density. More precisely, since √1 − r2 vanishes when r = 1, there is no point in having anything at radius exactly 1. If one imagines starting at r = 1 and slowly decreasing the value of r, we see that (2L/π2)√1 − r2 is monotonically increasing. If one wanted to keep the error uniformly bounded, it might make sense to place a radius every time the value attains a new integer value, i.e. solving for

2L π2

1 − ri2 = i which suggests setting

i2π4 4L2

2L π2

for 1 ≤ i <

ri = 1 −

. Then

i2π4 4L2 ≥ r is equivalent to

2L π2

1 − r2 ≥ i

1 −

which shows that the maximal error term is bounded from above by 1, by construction. Of course, in doing so, there is no a priori guarantee that the length of the set is exactly L and there is no reason why it would be. The total length is

⌊2L/π2⌋

H1(S) = 2π

i=1

i2π4 4L2

1 −

.

We approximate the sum by an integral (which leads to a controlled error because the integrand is in [0,1] and monotonically decreasing) and arrive at the inequality

H1(S) − 2π

2L/π2

0

π4 4L2

x2dx ≤ 8π.

1 −

The area of a quarter disk is merely

2L/π2

π4 4L2

L

x2dx =

1 −

2π and we arrive at

0

H1(S) − L ≤ 8π.

We can now simply add or remove the remaining length by adding/removing at most ≤ 20 circles of radius 1 leading to a uniformly bounded error. □

## 2.3. Proof of Theorem 2.

Proof. Let x,y ∈ R2 be two distinct points in the plane. It is our goal to count the number of intersections between the line segment from x to y and the family of lines that belong to the Steinhaus set Sn,ε which is given by

t + −sin(πk/n) cos(πk/n)

cos(πk/n) sin(πk/n)

sε t ∈ R, s ∈ Z, 0 ≤ k < n.

Our goal is to obtain uniform estimates which implies that the precise structure of the set Ω does not play a role: convexity enters implicitly in the sense that any line going through Ω will enter at a point x ∈ ∂Ω and leave the set Ω in another point y ∈ ∂Ω except for tangent lines in which case x = y which is also covered by the subsequent argument.

Figure 8. Counting the number of intersections for a full Steinhaus set (left) and for the translates of a fixed line (right).

We proceed by fixing 0 ≤ k < n and counting the number of lines with fixed k intersecting the line segment from x to y. A quick inspection, see Fig. 8, shows that this depends on the projection of the line segment onto the orthogonal direction (up to an error of O(1) coming from the two endpoints); that number is

1 ε

−sin(πk/n) cos(πk/n)

,y − x + O(1).

Summing over 0 ≤ k < n and writing y −x = (−a,b) for some a,b ∈ R, we see that the number of intersections is given by

n−1

1 ε

|asin(πk/n) + bcos(πk/n)| + O(n).

#intersections =

k=0

The sum Σ can be rewritten as Σ = a2 + b2

n−1

b √a2 + b2

a √a2 + b2

sin(πk/n) +

cos(πk/n)

k=0

n−1

πk n

= a2 + b2

sin

+ θ

k=0

for a suitable θ depending only on a,b. This sum has been extensively studied, see Moran [20] or Steinhaus [23]. Using the Fourier series

∞

2 π −

cos(2mx) 4m2 − 1 and plugging in, we arrive at

4 π

|sin(x)| =

m=1

n−1

∞

n−1

cos(2m πkn + θ ) 4m2 − 1

πk n

2 π −

4 π

+ θ =

sin

m=1

k=0

k=0

∞

n−1

2n π −

4 π

1 4m2 − 1

=

cos 2m

m=1

k=0

The inner sum is 0 unless m is a multiple of n. Thus

πk n

+ θ .

∞

n−1

2n π −

4 π

n 4ℓ2n2 − 1

πk n

+ θ =

cos(2ℓnθ).

sin

ℓ=1

k=0

One could now argue that this expression is minimized when θ = 0 and maximized when θ = π/(2n) and obtain a precise closed-form expression in terms of the cotangent and the cosecant (which is done by Moran and Steinhaus). We do not require results at that level of precision and simply argue that

Altogether

∞

∞

1 4ℓ2n2 − 1

ncos(2ℓnθ) ≤

ℓ=1

ℓ=1

n 4ℓ2n2 − 1 ≤

1 n

.

1 ε

#intersections =

- 1 ε

- 2n


=

n−1

|asin(πk/n) + bcos(πk/n)| + O(n)

k=0

√a2 + b2 εn

a2 + b2 + O

+ O(n)

π

- 1 ε

- 2n


diam(Ω) εn

a2 + b2 + O

=

+ n

π

We see that the leading order term is directly proportional to the length √a2 + b2 which is exactly what we want. It remains to obtain a uniform estimate for the error. We observe that the Steinhaus set Sn,ε has length ∼ n/ε inside a unit square and thus also for any bounded domain with an implicit constant depending on Ω. Then, fixing n/ε ∼ L to be the length of the set, we want to minimize

L n2

1 nε

+ n leading to n ∼ L1/3 and therefore ε ∼ L2/3.

+ n =

This choice of parameters then yields the desired result. □ Acknowledgment. The author is grateful to Google DeepMind (special thanks to Bogdan Georgiev and Adam Zsolt Wagner) for facilitating the use of AlphaEvolve. It was used as an exploratory tool in the early stages of the manuscript where it was used to search for sets with good properties.

### References

- [1] R. Ambartzumian, Combinatorial integral geometry, John Wiley & Sons, 1982
- [2] R. Ambartzumian, Factorization calculus and geometric probability, Cambridge University Press, 1990
- [3] A. Baddeley, H. Gundersen and L. Cruz-Orive, Estimation of surface area from vertical sections. Journal of microscopy, 142 (1986), 259-276.
- [4] J. Beck and W. Chen, Irregularities of Distribution, Cambridge University Press, 2010
- [5] J. Bodziony and K. Hu¨bner, Hugo Steinhaus – an unknown stereologist. Acta Stereol. 6

(1987), p. 69-78.

- [6] B. Chazelle, The Discrepancy Method, Cambridge University Press, 2000
- [7] D. Coeurjolly and R. Klette, A comparative evaluation of length estimators of digital curves. IEEE transactions on pattern analysis and machine intelligence, 26(2), 252-258.
- [8] L. M. Cruz-Orive, Stereology: a historical survey. Image Analysis and Stereology, 36 (2017), p. 153-177.
- [9] L. M. Cruz-Orive and X. Gual-Arnau, Precision of circular systematic sampling. Journal of microscopy, 207 (2002), 225-242.
- [10] M. Drmota and R. Tichy, Sequences, Discrepancies and Applications, Springer, 2006.
- [11] A. Gadek-Moszczak and P. Matusiewicz, Polish stereology – A historical review. Image Analysis and Stereology, 36 (2017), 207-221.
- [12] A. Gomez, M. Cruz, and L. M. Cruz-Orive, On the precision of curve length estimation in the plane, Image Analysis and Stereology 35.1 (2016), 1-14.
- [13] M. Kiderlen and D. Meschenmoser, Error bounds for surface area estimators based on Crofton’s formula. Image Analysis and Stereology, 28 (2009), 165-177.
- [14] P. Kothari, A. Nayyeri, R. O’Donnell and C. Wu, Testing surface area. In Proceedings of the twenty-fifth annual ACM-SIAM symposium on Discrete algorithms (pp. 1204-1214). Society for Industrial and Applied Mathematics, 2014.
- [15] L. Kuipers and H. Niederreiter, Uniform Distribution of Sequences, Dover, 2006
- [16] A. S. Kulkarni, S. Mitter, T. Richardson and J. N. Tsitsiklis, Local versus nonlocal computation of length of digitized curves. IEEE Transactions on Pattern Analysis and Machine Intelligence, 16 (2022), p. 711-718.
- [17] Y. Liu, J. Yi, H. Zhang, G. Q. Zheng and J. Paul, Surface area estimation of digitized 3D objects using quasi-Monte Carlo methods. Pattern Recognition, 43 (2010), 3900-3909.
- [18] D. H. Maling, Measurements from maps: principles and methods of cartometry, ButterworthHeinemann, 2016.
- [19] J. Matousek, Geometric discrepancy: An illustrated guide (Vol. 18). Springer Science & Business Media, 1999.
- [20] P. A. P. Moran, Measuring the length of a curve. Biometrika, 53 (1966), p. 359-364.
- [21] J. Neeman, Testing surface area with arbitrary accuracy, In Proceedings of the forty-sixth annual ACM symposium on Theory of computing, pp. 393-397. 2014.
- [22] L. Santalo, Integral geometry and geometric probability. Cambridge University Press, 2004.
- [23] H. Steinhaus, Zur Praxis der Rektifikation und zum Langenbegriff, Akad. Wiss. Leipzig, Ber. 82, 1930, 120-130.
- [24] H. Steinhaus, Longimetr. Kalka do mierzenia dlugosci linji krzywych, Czasopismo Geograficzne 3 (1931), s.211-215
- [25] H. Steinhaus, W sprawie mierzenia dlugosci linij krzywych plaskich, Polski Przeglad Kartograficzny 37 (1932), p. 145–153
- [26] H. Steinhaus, Length, shape and area. In Colloquium mathematicum 3 (1954), p. 1-13.


Department of Mathematics and Department of Applied Mathematics, University of Washington, Seattle, WA 98195, USA Email address: steinerb@uw.edu

