# arXiv:1206.2608v1[math.MG]12Jun2012

## UPPER BOUNDS FOR PACKINGS OF SPHERES OF SEVERAL RADII

DAVID DE LAAT, FERNANDO MARIO´ DE OLIVEIRA FILHO, AND FRANK VALLENTIN

Abstract. We give theorems that can be used to upper bound the densities of packings of diﬀerent spherical caps in the unit sphere and of translates of diﬀerent convex bodies in Euclidean space. These theorems extend the linear programming bounds for packings of spherical caps and of convex bodies through the use of semideﬁnite programming. We perform explicit computations, obtaining new bounds for packings of spherical caps of two diﬀerent sizes and for binary sphere packings. We also slightly improve bounds for the classical problem of packing identical spheres.

1. Introduction

How densely can one pack given objects into a given container? Problems of this sort, generally called packing problems, are fundamental problems in geometric optimization.

An important example having a rich history is the sphere packing problem. Here one tries to place equal-sized spheres with pairwise disjoint interiors into n-dimensional Euclidean space while maximizing the fraction of covered space. In two dimensions the best packing is given by placing open disks centered at the points of the hexagonal lattice. In three dimensions, the statement that the best sphere packing has density π/√18 = 0.7404... was known as Kepler’s conjecture; it was proved by Hales [20] in 1998 by means of a computer-assisted proof.

Currently, one of the best methods for obtaining upper bounds for the density of sphere packings is due to Cohn and Elkies [8]. In 2003 they used linear programming to obtain the best known upper bounds for the densities of sphere packings in dimensions 4,...,36. They almost closed the gap between lower and upper bounds in dimensions 8 and 24. Their method is the noncompact version of the linear programming method of Delsarte, Goethals, and Seidel [11] for upper-bounding the densities of packings of spherical caps on the unit sphere.

From a physical point of view, packings of spheres of diﬀerent sizes are relevant as they can be used to model chemical mixtures which consist of multiple atoms or, more generally, to model the structure of composite material. For more about technological applications of these kind of systems of polydisperse, totally impenetrable spheres we refer to Torquato [39, Chapter 6]. In recent work, Hopkins, Jiao, Stillinger, and Torquato [25, 26] presented lower bounds for the densities of packings of spheres of two diﬀerent sizes, also called binary sphere packings.

Date: June 12, 2012. 1991 Mathematics Subject Classiﬁcation. 52C17, 90C22. Key words and phrases. sphere packing, spherical codes, polydisperse spheres, unequal error-

protection, theta number, polynomial optimization, semideﬁnite programming.

The ﬁrst and third author were supported by Vidi grant 639.032.917 from the Netherlands Organization for Scientiﬁc Research (NWO). The second author was supported by Rubicon grant 680-50-1014 from the Netherlands Organization for Scientiﬁc Research (NWO).

1

In coding theory, packings of spheres of diﬀerent sizes are important in the design of error-correcting codes which can be used for unequal error protection. Masnick and Wolf [31] were the ﬁrst who considered codes with this property.

In this paper we extend the linear programming method of Cohn and Elkies to obtain new upper bounds for the densities of multiple-size sphere packings. We also extend the linear programming method of Delsarte, Goethals, and Seidel to obtain new upper bounds for the densities of multiple-size spherical cap packings.

We perform explicit calculations for binary packings in both cases using semidefinite, instead of linear, programming. In particular we complement the constructive lower bounds of Hopkins, Jiao, Stillinger, and Torquato by non-constructive upper bounds. Insights gained from our computational approach are then used to improve known upper bounds for the densities of monodisperse sphere packings in dimensions 4, ... 9, except 8. The bounds we present improve on the best-known bounds due to Cohn and Elkies [8].

- 1.1. Methods and theorems. We model the packing problems using tools from combinatorial optimization. All possible positions of the objects which we can use for the packing are vertices of a graph and we draw edges between two vertices whenever the two corresponding objects cannot be simultaneously present in the packing because they overlap in their interiors. Now every independent set in this conﬂict graph gives a valid packing and vice versa. To determine the density of the packing we use vertex weights since we want to distinguish between “small” and “big” objects. For ﬁnite graphs it is known that the weighted independence number can be upper bounded by the weighted theta number. Our theorems for packings of spherical caps and spheres are inﬁnite-dimensional analogues of this result.


Let G = (V,E) be a ﬁnite graph. A set I ⊆ V is independent if no two vertices in I are adjacent. Given a weight function w: V → R≥0, the weighted independence number of G is the maximum weight of an independent set, i.e.,

w(x) : I ⊆ V is independent .

αw(G) = max

x∈I

Finding αw(G) is an NP-hard problem.

Gr¨tschel, Lov´sz, and Schrijver [19] deﬁned a graph parameter that gives an upper bound for αw and which can be computed eﬃciently by semideﬁnite optimization. It can be presented in many diﬀerent, yet equivalent ways, but the one convenient for us is

ϑ w(G) = min M K − (w1/2)(w1/2)T is positive semideﬁnite,

- K(x,x) ≤ M for all x ∈ V ,
- K(x,y) ≤ 0 for all {x,y}  ∈ E where x = y, M ∈ R, K ∈ RV ×V is symmetric.


Here we give a proof of the fact that ϑ w(G) upper bounds αw(G). In a sense, after discarding the analytical arguments in the proofs of Theorems 1.2 and 1.3, we are left with this simple proof.

- Theorem 1.1. For any ﬁnite graph G = (V,E) with weight function w: V → R≥0 we have αw(G) ≤ ϑ w(G). Proof. Let I ⊆ V be an independent set of nonzero weight and let K ∈ RV ×V , M ∈ R be a feasible solution of ϑ w(G). Consider the sum


w(x)1/2w(y)1/2K(x,y).

x,y∈I

### This sum is at least

w(x)1/2w(y)1/2w(x)1/2w(y)1/2 =

x,y∈I

### because K − (w1/2)(w1/2)T is positive semideﬁnite. The sum is also at most

w(x)

x∈I

2

w(x)K(x,x) ≤ M

w(x)

x∈I

x∈I

because K(x,x) ≤ M and because K(x,y) ≤ 0 whenever x = y as I forms an independent set. Now combining both inequalities proves the theorem.

Multiple-size spherical cap packings. We ﬁrst consider packings of spherical caps of several radii on the unit sphere Sn−1 = {x ∈ Rn : x·x = 1}. The spherical cap with angle α ∈ [0,π] and center x ∈ Sn−1 is given by

C(x,α) = {y ∈ Sn−1 : x · y ≥ cosα }. Its normalized volume equals

1

ωn−1(Sn−2) ωn(Sn−1)

(1 − u2)(n−3)/2 du,

w(α) =

cos α

where ωn(Sn−1) = (2πn/2)/Γ(n/2) is the surface area of the unit sphere. Two spherical caps C(x1,α1) and C(x2,α2) intersect in their topological interiors if and only if the inner product of x1 and x2 lies in the interval (cos(α1+α2),1]. Conversely we have

C(x1,α1)◦ ∩ C(x2,α2)◦ = ∅ ⇐⇒ x1 · x2 ≤ cos(α1 + α2).

A packing of spherical caps with angles α1, ..., αN is a union of any number of spherical caps with these angles and pairwise-disjoint interiors. The density of the packing is the sum of the normalized volumes of the constituting spherical caps.

The optimal packing density is given by the weighted independence number of the spherical cap packing graph. This is the graph with vertex set Sn−1 × {1,...,N}, where a vertex (x,i) has weight w(αi), and where two distinct vertices (x,i) and (y,j) are adjacent if cos(αi + αj) < x · y.

In Section 2 we will extend the weighted theta prime number to the spherical cap packing graph. There we will also derive Theorem 1.2 below, which gives upper bounds for the densities of packings of spherical caps. We will show that the sharpest bound given by this theorem is in fact equal to the theta prime number.

In what follows we denote by Pkn the Jacobi polynomial Pk((n−3)/2,(n−3)/2) of degree k, normalized so that Pkn(1) = 1.

- Theorem 1.2. Let α1, ..., αN ∈ (0,π] be angles and for i, j = 1, ..., N and k ≥ 0


let fij,k be real numbers such that fij,k = fji,k and ∞k=0 |fij,k| < ∞ for all i, j. Write

∞

fij,kPkn(u).

- (1) fij(u) =


k=0

Suppose the functions fij satisfy the following conditions:

- (i) fij,0 − w(αi)1/2w(αj)1/2 Ni,j=1 is positive semideﬁnite;
- (ii) fij,k Ni,j=1 is positive semideﬁnite for k ≥ 1;
- (iii) fij(u) ≤ 0 whenever −1 ≤ u ≤ cos(αi + αj).


Then the density of every packing of spherical caps with angles α1, ..., αN on the unit sphere Sn−1 is at most max{fii(1) : i = 1, ..., N }.

When N = 1, Theorem 1.2 reduces to the linear programming bound for spherical cap packings of Delsarte, Goethals, and Seidel [11]. In Section 4 we use semidefinite programming instead of linear programming to perform explicit computations for N = 2.

Translational packings of bodies and multiple-size sphere packings. We now deal with packings of spheres with several radii in Rn. Theorem 1.3 presented below can be used to ﬁnd upper bounds for the densities of such packings. In fact, it is more general and can be applied to packings of translates of diﬀerent convex bodies.

Let K1, ..., KN be convex bodies in Rn. A translational packing of K1, ..., KN is a union of translations of these bodies in which any two copies have disjoint interiors. The density of a packing is the fraction of space covered by it. There are diﬀerent ways to formalize this deﬁnition, and questions appear as to whether every packing has a density and so on. We postpone further discussion on this matter until Section 3 where we give a proof of Theorem 1.3.

Our theorem can be seen as an analogue of the weighted theta prime number ϑ w for the inﬁnite graph G whose vertex set is Rn × {1,...,N} and in which vertices (x,i) and (y,j) are adjacent if x + Ki and y + Kj have disjoint interiors. The weight function we consider assigns weight volKi to vertex (x,i) ∈ Rn×{1,...,N}. We will say more about this interpretation in Section 3.

For the statement of the theorem we need some basic facts from harmonic analysis. Let f : Rn → C be an L1 function. For u ∈ Rn, the Fourier transform of f at u is

fˆ(u) =

f(x)e−2πiu·x dx.

Rn

We say that function f is a Schwartz function (also called a rapidly-decreasing function) if it is inﬁnitely diﬀerentiable, and if any derivative of f, multiplied by any power of the variables x1, ..., xn, is a bounded function. The Fourier transform of a Schwartz function is a Schwartz function, too. A Schwartz function can be recovered from its Fourier transform by means of the inversion formula:

fˆ(u)e2πiu·x du

f(x) =

Rn

for all x ∈ Rn.

- Theorem 1.3. Let K1, ..., KN be convex bodies in Rn and let f : Rn → RN×N be a matrix-valued function whose every component fij is a Schwartz function. Suppose f satisﬁes the following conditions:


- (i) the matrix f ˆij(0) − (volKi)1/2(volKj)1/2 Ni,j=1 is positive semideﬁnite;
- (ii) the matrix of Fourier transforms f ˆij(u) Ni,j=1 is positive semideﬁnite for every u ∈ Rn \ {0};
- (iii) fij(x) ≤ 0 whenever Ki◦ ∩ (x + Kj◦) = ∅.


Then the density of any packing of translates of K1, ..., KN in the Euclidean space Rn is at most max{fii(0) : i = 1, ..., N }.

We give a proof of this theorem in Section 3. When N = 1 and when the convex body K1 is centrally symmetric (an assumption which is in fact not needed) then this theorem reduces to the linear programming method of Cohn and Elkies [8].

We apply this theorem to obtain upper bounds for the densities of binary sphere packings, as we discuss in Section 1.3.

| |
|---|


0.96

1.0

1.0

0.94

0.92

Geo.

0.8

0.8

0.9

0.88

0.6

0.6

0.86

0.84

0.82

0.4

0.4

SDP

0.8

0.78

0.2

0.2

0.76

0.2 0.4 0.6 0.8 1.0

0.2 0.4 0.6 0.8 1.0

(a) n = 3

(b) SDP bound/geometric bound for n = 3

| |
|---|


| |
|---|


0.89

0.8

1.0

1.0

0.77

0.86

0.74

0.83

0.8

0.8

0.71

0.8

0.68

0.77

0.65

0.6

0.6

0.74

0.62

0.71

0.59

0.4

0.4

0.68

0.56

0.53

0.65

0.5

0.62

0.2

0.2

0.47

0.59

0.2 0.4 0.6 0.8 1.0

0.2 0.4 0.6 0.8 1.0

(c) n = 4

(d) n = 5

Figure 1. Upper bounds on the packing density for N = 2. The horizontal and vertical axes carry the spherical cap angle; the colors indicate the density, or in the case of plot (b) whether the SDP bound or the geometric bound is sharper.

## 1.2. Computational results for binary spherical cap packings. We applied

- Theorem 1.2 to compute upper bounds for the densities of binary spherical cap packings. The results we obtained are summarized in the plots of Figure 1.


For n = 3, Florian [13, 14] provides a geometric upper bound for the density of a spherical cap packing. He shows that the density of a packing on S2 of spherical caps with angles α1,...,αN ∈ (0,π/3] is at most

max

D(αi,αj,αk),

1≤i≤j≤k≤N

where D(αi,αj,αk) is deﬁned as follows. Let T be a spherical triangle in S2 such that if we center the spherical caps with angles αi, αj, and αk at the vertices of T , then the caps intersect pairwise at their boundaries. The number D(αi,αj,αk) is then deﬁned as the fraction of the area of T covered by the caps.

In Figure 1b we see that for N = 2 it depends on the angles whether the geometric or the semideﬁnite programming bound is sharper. In particular we see that near the diagonal the semideﬁnite programming bound is at least as good as the geometric bound; see also Figure 2a.

We can construct natural multiple-size spherical cap packings by taking the incircles of the faces of spherical Archimedean tilings. A sequence of binary packings is for instance obtained by taking the incircles of the prism tilings. These are the Archimedean tilings with vertex ﬁgure (4,4,k) for k ≥ 3 (although strictly speaking for k = 4 this is a spherical Platonic tiling). The question then is whether the packing associated with the k-prism has maximal density among all packings with the same cap angles π/k and π/2 − π/k, that is, whether the packing is maximal. The packing for k = 3 is not maximal while the one for k = 4 trivially is, since here there is only one cap size, and adding a 9th cap yields a density greater than 1.

Heppes and Kert´esz [22] showed that the conﬁgurations for k ≥ 6 are maximal, and the remaining case k = 5 was later shown to maximal by Florian and Heppes [15]. Florian [13] showed that the geometric bound given above is in fact sharp for the cases where k ≥ 6, and for the k = 5 case it is not sharp but still good enough to prove maximality (notice that given a ﬁnite number of cap angles, the set of obtainable densities is ﬁnite).

Now we illustrate that Theorem 1.2 gives a sharp bound for the density of the packing associated to the 5-prism, thus giving a simple proof of its maximality. The theorem also provides a sharp bound for n = 4 but whether it can provide sharp bounds for the cases n ≥ 6 we do not know at the moment. The numerical results are not decisive.

We shall exhibit functions

4

fij,kPkn(u)

fij(u) =

k=0

which satisfy the conditions of Theorem 1.2 with f11(1) = 5w(α1) + 2w(α2) where α1 =

3π 10

- 1

- 2


π 5

1 2

3π 10

π 5

1 − cos

1 − cos

, α2 =

, w(α1) =

, w(α2) =

.

By complementary slackness of semideﬁnite optimization the coeﬃcients fij,k have to satisfy the following linear conditions:

2π 5

- 4π

- 5


2π 5

= f12(0) = f22(−1); the product

0 = f11 cos

= f11 cos

= f 11 cos

equals

- f11,0 f12,0
- f12,0 f22,0


25w(α1) 10 w(α1)w(α2) 10 w(α1)w(α2) 4w(α2)

25w(α1)2 + 10w(α1)w(α2) w(α1)w(α2)(10w(α1) + 4w(α2)) w(α1)w(α2)(25w(α1) + 10w(α2)) 10w(α1)w(α2) + 4w(α2)2

;

for k = 1,...,4 the product of the two matrices

- f11,k f12,k
- f12,k f22,k


and

w(α1)(5Pk(1) + 10Pk(cos 25π) + 10Pk(cos 24π)) w(α1)w(α2)10Pk(0)

w(α1)w(α2)10Pk(0) w(α2)(2Pk(1) + 2Pk(−1)) equals zero. This linear system together with the additional assumptions

95 100 has a one-dimensional space of solutions from which it is easy to select one which fulﬁlls all requirements of Theorem 1.2.

95 100

= f 12 −

0 = f11(−1) = f12 −

For the remaining 13 Archimedean solids in dimension n = 3 we are only able to show maximality of the packing associated to the truncated octahedron, the

Archimedean solid with vertex ﬁgure (6,6,5). Its density is 0.9056..., the geometric bound shows that the density is at most 0.9088..., and using the semideﬁnite program we get 0.9079... as an upper bound. The ﬁrst packing with caps of angles arcsin(1/3) and arcsin(1/√3) which would be denser is obtained by taking 19 of the smaller caps and 4 of the bigger caps, and has density 0.9103... The upper bounds show however that it is not possible to obtain this dense a packing, thus showing that the truncated octahedron packing is maximal.

600-cell

- 0.90


Icosahedron

Octahedron

0.75

- 0.88


Cross-polytope

0.86

Simplex

0.70

0.84

Simplex

0.82

0.65

0.80

0.78

0.60

0.76

0.2 0.4 0.6 0.8 1.0

0.2 0.4 0.6 0.8 1.0

(a) n = 3

#### (b) n = 4

0.65

0.60

Cross-polytope

Semicube

0.55

Simplex

0.50

0.45

0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

(c) n = 5

Figure 2. Upper bounds on the packing density for N = 1, the horizontal axis carries the spherical cap angle and the vertical axis the packing density.

We also used our programs to plot the upper bounds for N = 1, the classical linear programming bound of Delsarte, Goethals, and Seidel [11], for dimensions n = 3, 4, and 5 in Figure 2. To the best of our knowledge these kinds of plots were not made before and they seem to reveal interesting properties of the bound. For better orientation we show in the plots the packings where the linear programming bound is sharp (cf. Levenshtein [28]; Cohn and Kumar [9] proved the much stronger statement that these packings provide point conﬁgurations which are universally optimal). The dotted line in the plot for n = 3 is the geometric bound, and since we know that both the geometric (cf. Florian [13]) and the semideﬁnite programming

0.95

0.90

n = 2

0.85

0.80

n = 3

0.75

0.70

n = 4

0.65

0.60

n = 5

0.55

0.50

0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

Figure 3. The horizontal axis carries the ratio between the radii of the small and the large spheres. The vertical axis carries our upper bound. Our bounds for dimensions 2, ..., 5 are shown together.

bounds are sharp for the given conﬁgurations, we know that at these peaks the bounds meet.

An interesting feature of the upper bound seems to be that it has some periodic behavior. Indeed, the numerical results suggest that for n = 3, the two bounds in fact meet inﬁnitely often as the angle decreases, and that between any two of these meeting points the semideﬁnite programming bound has a similar shape. Although in higher dimensions we do not have a geometric bound, the semideﬁnite programming bound seems to admit the same kind of periodic behavior.

## 1.3. Computational results for binary sphere packings. We applied Theo-

- rem 1.3 to compute upper bounds for the densities of binary sphere packings. The results we obtained are summarized in the plot of Figure 3, where we show bounds computed for dimensions 2, ..., 5. A detailed account of our approach is given in Section 5. We now quickly discuss the bounds presented in Figure 3.


- Dimension 2. Only in dimension 2 have binary sphere (i.e., circle) packings been studied in depth. We refer to the introduction in the paper of Heppes [21] which surveys the known results about binary circle packings in the plane.


Currently one of the best-known upper bounds for the maximum density of a binary circle packing is due to Florian [12]. Florian’s bound states that a packing of circles in which the ratio between the radii of the smallest and largest circles is r has density at most

πr2 + 2(1 − r2)arcsin(r/(1 + r)) 2r√2r + 1

,

and that this bound is achieved exactly for r = 1 (i.e., for classical circle packings) and for r = 0 in the limit.

The question arises of which bound is better, our bound or Florian’s bound. From our experiments, it seems that our bound is worse than Florian’s bound, at least for r < 1. For instance, for r = 1/2 we obtain the upper bound 0.9174426...,

whereas Florian’s bound is 0.9158118... Whether this really means that the bound of Theorem 1.3 is worse than Florian’s bound, or just that the computational approach of Section 5 is too restrictive to attain his bound, we do not know.

It is interesting to note that for r = 1, that is, for packings of circles of one size, our bound clearly coincides with the one of Cohn and Elkies [8]. This bound seems to be equal to π/√12, but no proof of this is known.

- Dimension 3. Much less is known in dimension 3. In fact we do not know about other attempts to ﬁnd upper bounds for the densities of binary sphere packings in dimensions 3 and higher.

Let us compare our upper bound with the lower bound by Hopkins, Jiao, Stillinger, and Torquato [25]. The record holder for r ≥ 0.2 in terms of highest density occurs for r = 0.224744... and its density is 0.824539... Our computations show that there cannot be a packing with this r having density more than 0.8617125..., so this leaves a margin of 5%.

Another interesting case is r = √2 − 1 = 0.414... Here the best-known lower bound of 0.793... comes from the NaCl-alloy. The large spheres are centered at a face centered cubic lattice and the small spheres are centered at a translated copy of the face centered cubic lattice so that they form a jammed packing. Our upper bound for r = √2 − 1 is 0.813..., less than 3% away from the lower bound. Therefore, we believe that proving optimality of the NaCl-alloy might be doable.

- Dimension 4 and beyond. In higher dimensions even less is known about binary sphere packings. We observed from Figure 3 that it seems that the upper bound is decreasing: as the radius of the small sphere increases from 0.2 to 1, the bound seems to decrease. This suggests that the bound given by Theorem 1.3 is decreasing in this sense, but we do not know a proof of this.


We also do not know the limit behavior of our bound when r approaches 0. Due to numerical instabilities we could not perform numerical calculations in this regime of r.

- 1.4. Improving the Cohn-Elkies bounds. We now present a theorem that can be used to ﬁnd better upper bounds for the densities of monodisperse sphere packings than those provided by Cohn and Elkies [8]; our theorem is a strengthening of theirs.


Fix ε > 0. Given a packing of spheres of radius 1/2, we consider its ε-tangency graph, a graph whose vertices are the spheres in the packing, and in which two vertices are adjacent if the distance between the centers of the respective spheres lies in the interval [1,1 + ε).

Let M(ε) be the least upper bound on the average degree of the ε-tangency graph of any sphere packing. Our theorem is the following:

- Theorem 1.4. Take 0 = ε0 < ε1 < ··· < εm and let f : Rn → R be a Schwartz function such that


- (i) fˆ(0) ≥ volB, where B is the ball of radius 1/2;
- (ii) fˆ(u) ≥ 0 for all u ∈ Rn \ {0};
- (iii) f(x) ≤ 0 whenever x ≥ 1 + εm;
- (iv) f(x) ≤ ηk whenever x ∈ [1+εk−1,1+εk) with ηk ≥ 0, for k = 1, ..., m.


Then the density of a sphere packing is at most the optimal value of the following linear programming problem in variables A1, ..., Am:

max f(0) + η1A1 + ··· + ηmAm A1 + ··· + Ak ≤ U(εk) for k = 1, ..., m, Ai ≥ 0 for i = 1, ..., m,

- (2)


where U(εk) ≥ M(εk) for k = 1, ..., m.

In Section 6 we give a proof of Theorem 1.4 and show how to compute upper bounds for M(ε) using the semideﬁnite programming bounds of Bachoc and Vallentin [4] for the sizes of spherical codes. There we also show how to use semideﬁnite programming and the same ideas we employ in the computations for binary sphere packings (cf. Section 5) to compute better upper bounds for the densities of sphere packings.

In Table 1 we show the upper bounds obtained through our application of Theo-

- rem 1.4. To better compare our bounds with those of Cohn and Elkies, on Table 1 we show bounds for the center density of a packing, the center density of a packing of unit spheres being equal to ∆/volB, where ∆ is the density of the packing, and B is a unit ball.


We omit dimension 8 because for this dimension it is already believed that the Cohn-Elkies bound is itself optimal, and therefore as is to be expected we did not manage to obtain any improvement over their bound. We also note that the bounds by Cohn and Elkies are the best known upper bounds in all other dimensions shown.

Dimension Lower bound Cohn-Elkies bound New upper bound

- 4 0.12500 0.13126 0.130587
- 5 0.08839 0.09975 0.099408
- 6 0.07217 0.08084 0.080618
- 7 0.06250 0.06933 0.069193 9 0.04419 0.05900 0.058951


Table 1. For each dimension we show the best lower bound known, the bound by Cohn and Elkies [8], and the upper bound coming from Theorem 1.4.

In dimension 3 the Cohn-Elkies bound is 0.18616 whereas the optimal sphere packing has center density 0.17678. We can improve the Cohn-Elkies bound to 0.184559 which is also better than the upper bound 0.1847 due to Rogers [33].

2. Multiple-size spherical cap packings

In this section we prove Theorem 1.2 and discuss its relation to an extension of the weighted theta prime number for the spherical cap packing graph.

- 2.1. Proof of Theorem 1.2. Let x1, ..., xm ∈ Sn−1 and r: {1,...,m} →


{1,...,N} be such that

m

C(xi,αr(i)) is a packing of spherical caps on Sn−1.

i=1

Consider the sum

m

w(αr(i))1/2w(αr(j))1/2fr(i)r(j)(xi · xj).

- (3)


i,j=1

By expanding fr(i)r(j)(xi · xj) according to (1) this sum is equal to

∞

m

w(αr(i))1/2w(αr(j))1/2fr(i)r(j),kPkn(xi · xj).

i,j=1

k=0

By the addition formula (cf. e.g. Section 9.6 of Andrews, Askey, and Roy [1]) for the Jacobi polynomials Pkn the matrix Pkn(xi · xj) mi,j=1 is positive semideﬁnite.

From condition (ii) of the theorem, we also know that the matrix fr(i)r(j),k mi,j=1 is positive semideﬁnite for k ≥ 1. So the inner sum above is nonnegative for k ≥ 1. If we then consider only the summand for k = 0 we see that (3) is at least

- (4)

m

i,j=1

w(αr(i))1/2w(αr(j))1/2fr(i)r(j),0P0n(xi · xj) ≥

m

i=1

w(αi)

2

,

where the inequality follows from condition (i) of the theorem.

Now, notice that whenever i = j, the caps C(xi,αr(i)) and C(xj,αr(j)) have disjoint interiors. Condition (iii) then implies that fr(i)r(j)(xi · xj) ≤ 0. So we see that (3) is at most

- (5)

m

i=1

w(αi)fr(i)r(i)(1) ≤ max{fii(1) : i = 1, ..., N }

m

i=1

w(αi). So (3) is at least (4) and at most (5), yielding

m

i=1

w(αi) ≤ max{fii(1) : i = 1, ..., N }.

- 2.2. Theorem 1.2 and the Lova´sz theta number. We now brieﬂy discuss a


generalization of ϑ w to inﬁnite graphs and its relation to the bound of Theorem 1.2. Similar ideas were developed by Bachoc, Nebe, Oliveira, and Vallentin [3].

Let G = (V,E) be a graph, where V is a compact space, and let w: V → R≥0 be a continuous weight function. An element in the space C(V × V ) of real-valued continuous functions over V × V is called a kernel. A kernel K is symmetric if K(x,y) = K(y,x) for all x,y ∈ V . It is positive if it is symmetric and if for

any N ∈ N and for any x1, ..., xN ∈ V , the matrix K(xi,xj) Ni,j=1 is positive semideﬁnite. The weighted theta prime number of G is deﬁned as

- (6)


ϑ w(G) = inf M K − w1/2 ⊗ (w1/2)∗ is a positive kernel,

- K(x,x) ≤ M for all x ∈ V ,
- K(x,y) ≤ 0 for all {x,y}  ∈ E where x = y, M ∈ R, K ∈ C(V × V ) is symmetric.


One may show, mimicking the proof of Theorem 1.1, that ϑ w(G) ≥ αw(G).

Let G = (V,E) be the spherical cap packing graph as deﬁned in Section 1.1. We will use the symmetry of this graph to show that (6) gives the sharpest bound obtainable by Theorem 1.2.

The orthogonal group O(n) acts on Sn−1, and this deﬁnes the action of O(n) on the vertex set V = Sn−1 × {1,...,N} by A(x,i) = (Ax,i) for A ∈ O(n). The group average of a kernel K ∈ C(V × V ) is given by

K((x,i),(y,j)) =

K(A(x,i),A(y,j))dµ(A),

O(n)

where µ is the Haar measure on O(n) normalized so that µ(O(n)) = 1. If (K,M) is feasible for (6), then (K,M) is feasible too. This follows since for each A ∈ O(n), a point (x,i) has the same weight as A(x,i), and two points (x,i) and (y,j) are adjacent if and only if A(x,i) and A(y,j) are adjacent. Since (K,M) and (K,M) have the same objective value M, and since K is invariant under the action of O(n), we may restrict to O(n)-invariant kernels (i.e., kernels K such that K(Au,Av) = K(u,v) for all A ∈ O(n) and u, v ∈ V ) in ﬁnding the inﬁmum of (6).

Schoenberg [34] showed that a symmetric kernel K ∈ C(Sn−1 ×Sn−1) is positive and O(n)-invariant if and only if it lies in the cone spanned by the kernels (x,y)  → Pkn(x · y). We will use the following generalization for kernels over V × V .

- Theorem 2.1. A symmetric kernel K ∈ C(V × V ), with V = Sn−1 × {1,...,N}, is positive and O(n)-invariant if and only if


- (7) K((x,i),(y,j)) = fij(x · y) with

fij(u) =

∞

k=0

fij,kPkn(u),

where fij,k Ni,j=1 is positive semideﬁnite for all k ≥ 0 and ∞k=0 |fij,k| < ∞ for all i, j = 1, ..., N, implying in particular that we have uniform convergence above.

Before we prove the theorem we apply it to simplify problem (6). If K is an O(n)-invariant feasible solution of (6), then K − w1/2 ⊗ (w1/2)∗ is a positive O(n)invariant kernel, and hence can be written in the form (7). Using in addition that P0n = 1, problem (6) reduces to

ϑ w(G) = inf M fii(0) + w(αi) ≤ M for all 1 ≤ i ≤ N, fij(u) + (w(αi)w(αj))1/2 ≤ 0 when −1 ≤ u ≤ cos(αi + αj),

M ∈ R and fij,k Ni,j=1 positive semideﬁnite for all k ≥ 0.

By substituting fij,0 − (w(αi)w(αj))1/2 for fij,0 we see that the solution to this problem indeed equals the sharpest bound given by Theorem 1.2.

- Proof of Theorem 2.1. If we endow the space C(Sn−1) of real-valued continuous function on the unit sphere Sn−1 with the usual L2 inner product, then for f, g ∈ C(V ),


f,g =

N

i=1 Sn−1

f(x,i)g(x,i)dω(x)

gives an inner product on C(V ). The space C(Sn−1) decomposes orthogonally as

C(Sn−1) =

∞

k=0

Hk,

where Hk is the space of homogeneous harmonic polynomials of degree k restricted to Sn−1. With

Hk,i = {f ∈ C(V ) : there is a g ∈ Hk such that f(·,j) = δijg(·)}, it follows that C(V ) decomposes orthogonally as

C(V ) =

∞

k=0

N

i=1

Hk,i.

Given the action of O(n) on V , we have the natural unitary representation on C(V ) given by (Af)(x,i) = f(A−1x,i) for A ∈ O(n) and f ∈ C(V ). It follows that each space Hk,i is O(n)-irreducible and that two spaces Hk,i and Hk ,i are O(n)-equivalent if and only if k = k . Let

{ek,i,l : k ≥ 0, 1 ≤ i ≤ N, and 1 ≤ l ≤ hk } be a complete orthonormal system of C(V ) such that ek,i,1, ..., ek,i,h

k

is a basis of Hk,i. By Bochner’s characterization [5], a kernel K ∈ C(V × V ) is positive and O(n)-invariant if and only if

- (8) K((x,i),(y,j)) =


∞

hk

N

fij,k

ek,i ,l(x,i)ek,j ,l(y,j),

i ,j =1

k=0

l=1

where each fij,k Ni,j=1 is positive semideﬁnite and ∞k=0 |fij,k| < ∞ for all i, j.

By the addition formula (cf. Chapter 9.6 of Andrews, Askey, and Roy [1]) we have

hk

hk ωn(Sn−1)

Pkn(x · y) for any orthonormal basis ek,1,...,ek,h

ek,l(x)ek,l(y) =

l=1

### of Hk. It follows that hk

k

hk ωn(Sn−1)

Pkn(x · y), and substituting this into (8) completes the proof.

ek,i ,l(x,i)ek,j ,l(y,j) = δii δjj

l=1

Bochner’s characterization for the kernel K, which we used above, usually assumes that the spaces under consideration are homogeneous, so that the decompositions into isotypic irreducible spaces are guaranteed to be ﬁnite. This ﬁniteness is then used to conclude uniform convergence. Since the action of O(n) on V is not transitive, we do not immediately have this guarantee. We can still use the characterization, however, since irreducible subspaces of C(V ) have ﬁnite multiplicity.

- 3. Translational packings of bodies and multiple-size sphere packings


Before giving a proof of Theorem 1.3 we quickly present some technical considerations regarding density. Here we follow closely Appendix A of Cohn and Elkies [8].

Let K1, ..., KN be convex bodies and P be a packing of translated copies of K1, ..., KN, that is, P is a union of translated copies of the bodies, any two copies having disjoint interiors. We say that the density of P is ∆ if for all p ∈ Rn we have

vol(B(p,r) ∩ P) volB(p,r)

,

∆ = lim

r→∞

where B(p,r) is the ball of radius r centered at p. Not every packing has a density, but every packing has an upper density given by

vol(B(p,r) ∩ P) volB(p,r)

.

limsup

sup

p∈Rn

r→∞

We say that a packing P is periodic if there is a lattice L ⊆ Rn that leaves P invariant, that is, which is such that P = x + P for all x ∈ L. In other words, a periodic packing consists of some translated copies of the bodies K1, ..., KN arranged inside the fundamental parallelotope of L, and this arrangement repeats itself at each copy of the fundamental parallelotope translated by vectors of the lattice.

It is easy to see that a periodic packing has a density. This is particularly interesting for us, since in computing upper bounds for the maximum possible density of a packing we may restrict ourselves to periodic packings, as it is known (and easy to see) that the supremum of the upper densities of packings is also achieved by periodic packings (cf. Appendix A in Cohn and Elkies [8]).

To provide a proof of the theorem we need another fact from harmonic analysis, the Poisson summation formula. Let f : Rn → C be a Schwartz function and L ⊆ Rn be a lattice. The Poisson summation formula states that, for every x ∈ Rn,

1 vol(Rn/L) u∈L

fˆ(u)e2πiu·x,

f(x + v) =

∗

v∈L

where L∗ = {u ∈ Rn : u · x ∈ Z for all x ∈ L} is the dual lattice of L and where vol(Rn/L) is the volume of a fundamental domain of the lattice L.

Proof of Theorem 1.3. As observed above, we may restrict ourselves to periodic packings. Let then L ⊆ Rn be a lattice and x1, ..., xm ∈ Rn and r: {1,...,m} → {1,...,N} be such that

m

P =

v + xi + Kr(i)

v∈L

i=1

is a packing. This means that, whenever i = j or v = 0, bodies xi + Kr(i) and v + xj + Kr(j) have disjoint interiors. This packing is periodic and therefore has a well-deﬁned density, which equals

m

1 vol(Rn/L)

volKr(i). Consider the sum

i=1

- (9) v∈L

m

i,j=1

(volKr(i))1/2(volKr(j))1/2fr(i)r(j)(v + xj − xi).

Applying the Poisson summation formula we may express (9) in terms of Fourier transform of f, obtaining

1 vol(Rn/L) u∈L

∗

m

i,j=1

(volKr(i))1/2(volKr(j))1/2fˆr(i)r(j)(u)e2πiu·(x

j−xi),

where L∗ is the dual lattice of L.

Since f satisﬁes condition (ii) of the theorem, matrix f ˆr(i)r(j)(u) mi,j=1 is positive semideﬁnite for every u ∈ Rn. So the inner sum above is always nonnegative. If we then consider only the summand for u = 0, we see that (9) is at least

1 vol(Rn/L)

m

i,j=1

(volKr(i))1/2(volKr(j))1/2fˆr(i)r(j)(0)

≥

1 vol(Rn/L)

m

i,j=1

volKr(i) volKr(j)

=

1 vol(Rn/L)

m

i=1

volKr(i)

2

,

- (10)

where the inequality comes from condition (i) of the theorem.

Now, notice that whenever v = 0 or i = j one has fr(i)r(j)(v+xj−xi) ≤ 0. Indeed, since P is a packing, if v = 0 or i = j then the bodies xi + Kr(i) and v + xj + Kr(j) have disjoint interiors. But then also Kr(i) and v + xj − xi + Kr(j) have disjoint interiors, and then from (iii) we see that fr(i)r(j)(v + xj − xi) ≤ 0. From this observation we see immediately that (9) is at most

- (11)


m

m

volKr(i). So (9) is at least (10) and at most (11). Putting it all together we get that

volKr(i)fr(i)r(i)(0) ≤ max{fii(0) : i = 1, ..., N }

i=1

i=1

m

1 vol(Rn/L)

volKr(i) ≤ max{fii(0) : i = 1, ..., N }, proving the theorem.

i=1

We mentioned in the beginning of the section that Theorem 1.3 is an analogue of the weighted theta prime number for a certain inﬁnite graph. The connection will become more clear after we present a slightly more general version of Theorem 1.3.

An L∞ function f : Rn → CN×N is said to be of positive type if f(x) = f(−x)∗ for all x ∈ Rn and for all L1 functions ρ: Rn → CN we have

ρ(y)∗f(x − y)ρ(x)dxdy ≥ 0.

Rn Rn

When N = 1 we have the classical theory of functions of positive type (see e.g. the book by Folland [16] for background). Many useful properties of such functions can be extended to the matrix-valued case (that is, to the N > 1 case) via a simple observation: a function f : Rn → CN×N is of positive type if and only if for all p ∈ CN the function gp: Rn → C such that

gp(x) = p∗f(x)p is of positive type.

From this observation two useful classical characterizations of functions of positive type can be extended to the matrix-valued case. The ﬁrst one is useful when dealing with continuous functions of positive type. It states that a continuous and bounded function f : Rn → CN×N is of positive type if and only if for every

choice x1, ..., xm of ﬁnitely many points in Rn, the block matrix f(xi −xj) mi,j=1 is positive semideﬁnite.

The second characterization is given in terms of the Fourier transform. It states that an L1 function f : Rn → CN×N is of positive type if and only if the matrix f ˆij(u) Ni,j=1 is positive semideﬁnite for all u ∈ Rn. So in the statement of Theorem 1.3, for instance, one could replace condition (i) by the equivalent condition that f be a function of positive type.

When N = 1, the previous two characterizations of functions of positive type date back to Bochner [6].

With this we may give an alternative and more general version of Theorem 1.3.

Theorem 3.1. Let K1, ..., KN be convex bodies in Rn and let f : Rn → RN×N be a continuous and L1 function. Suppose f satisﬁes the following conditions:

- (i) the matrix f ˆij(0) − (volKi)1/2(volKj)1/2 Ni,j=1 is positive semideﬁnite;
- (ii) f is of positive type;
- (iii) fij(x) ≤ 0 whenever Ki◦ ∩ (x + Kj◦) = ∅.


Then the density of every packing of translates of K1, ..., KN in the Euclidean space Rn is at most max{fii(0) : i = 1, ..., N }.

Let V = Rn × {1,...,N}. Notice that the kernel K : V × V → R such that K((x,i),(y,j)) = fij(x − y),

implicitly deﬁned by the function f, plays the same role as the matrix K from the deﬁnition of the theta prime number (cf. Section 2.2). For instance, this is a positive kernel, since f is of positive type and hence for any L1 function ρ: V → R we have that

K((x,i),(y,j))ρ(x,i)ρ(y,j)d(x,i)d(y,j) ≥ 0.

V V

Theorem 3.1 can then be seen as an analogue of the weighted theta prime number for the packing graph with vertex set V that we consider.

When one reads through the proof of Theorem 1.3, the one step that fails when f is L1 instead of Schwartz is the use of the Poisson summation formula. Indeed, sum (9) is not anymore well-deﬁned in such a situation. The summation formula also holds, however, under somewhat diﬀerent conditions that are just what we need to make the proof go through. The proof of the following lemma makes use of

the well-known interpretation of the Poisson summation formula as a trace formula, which for instance is explained by Terras [38, Chapter 1.3].

Lemma 3.2. Let f : Rn → CN×N be a continuous function of bounded support and positive type. Then for every lattice L ⊆ Rn, every x ∈ Rn, and all i, j = 1, ..., N we have

1 vol(Rn/L) u∈L

fˆij(u)e2πiu·x.

fij(x + v) =

∗

v∈L

Proof. Since each function fij is continuous and of bounded support, the functions gij : Rn/L → C such that

gij(x) =

fij(x + v)

v∈L

are continuous. Indeed, the sum above is well-deﬁned, being in fact a ﬁnite sum (since fij has bounded support), and therefore gij can be seen locally as a sum of ﬁnitely many continuous functions.

Let us now compute the Fourier transform of gij. For u ∈ L∗ we have that gˆij(u) =

gij(x)e−2πiu·x dx

Rn/L

fij(x + v)e−2πiu·x dx

### =

Rn/L v∈L

fij(x)e−2πiu·x dx

=

Rn

= fˆij(u). So we know that

1 vol(Rn/L) u∈L

fˆij(u)e2πiu·x

- (12) gij(x) =


∗

in the sense of L2 convergence. Our goal is to prove that pointwise convergence also holds above.

To this end we consider for i = 1, ..., N the kernel Ki: (Rn/L) × (Rn/L) → C such that

fii(v + x − y).

Ki(x,y) =

v∈L

Since each function fii is of bounded support and continuous, each kernel Ki is continuous. Since for each i we have that fii(x) = fii(−x) for all x ∈ Rn (since f is of positive type), each kernel Ki is self-adjoint. Notice that the functions x  → (vol(Rn/L))−1/2e2πiu·x, for u ∈ L∗, form a complete orthonormal system of L2(Rn/L). Each such function is also an eigenfunction of Ki, with eigenvalue fˆii(u). Indeed, we have

Ki(x,y)(vol(Rn/L))−1/2e2πiu·y dy

Rn/L

= (vol(Rn/L))−1/2

fii(v + x − y)e2πiu·y dy

Rn/L v∈L

= (vol(Rn/L))−1/2

fii(x − y)e2πiu·y dy

Rn

= (vol(Rn/L))−1/2

fii(y)e2πiu·(x−y) dy

Rn

### = fˆii(u)(vol(Rn/L))−1/2e2πiu·x.

Since f is of positive type, the matrices of Fourier transforms f ˆij(u) Ni,j=1, for u ∈ Rn, are all positive semideﬁnite. In particular this implies that the Fourier transforms of fii, for i = 1, ..., N, are nonnegative. So we see that each Ki is a continuous and positive kernel. Mercer’s theorem (see for instance Courant and Hilbert [10]) then implies that Ki is trace-class, its trace being the sum of all its eigenvalues. So for each i = 1, ..., N, the series

fˆii(u)

- (13) u∈L∗


converges, and since each summand is nonnegative, it converges absolutely.

Suppose now that i, j = 1, ..., N are so that i = j. Since the matrices of Fourier transforms are nonnegative, for all u ∈ Rn we have that the matrix

f ˆii(u) fˆij(u) fˆij(u) fˆjj(u)

is positive semideﬁnite, and this in turn implies that |fˆij(u)|2 ≤ fˆii(u)fˆjj(u) for all u ∈ Rn. Using then the convergence of the series (13) and the Cauchy-Schwarz inequality, one gets

|fˆij(u)| ≤

(fˆii(u)fˆjj(u))1/2 ≤

fˆii(u)

u∈L∗

u∈L∗

u∈L∗

and we see that in fact for all i, j = 1, ..., N the series

1/2

fˆjj(u)

u∈L∗

1/2

,

fˆij(u)

u∈L∗

converges absolutely.

This convergence result shows that the sum in (12) converges absolutely and uniformly for all x ∈ Rn/L. This means that the function deﬁned by this sum is a continuous function, and since gij is also a continuous function, and in (12) we have convergence in the L2 sense, we must also then have pointwise convergence, as we aimed to establish.

With this we may give a proof of Theorem 3.1:

- Proof of Theorem 3.1. Using Lemma 3.2, we may repeat the proof of Theorem 1.3 given before, proving the theorem for continuous functions of bounded support. To extend the proof also to continuous L1 functions we use the following trick.


Let f : Rn → RN×N be a continuous and L1 function satisfying the hypothesis of the theorem. For each T > 0 consider the function gT : Rn → RN×N deﬁned such that

vol(B(0,T) ∩ B(x,T)) volB(0,T)

gT(x) =

f(x),

where B(p,T) is the ball of radius T centered at p.

It is easy to see that gT is a continuous function of bounded support. It is also clear that it satisﬁes condition (iii) from the statement of the theorem. We now show that gT is a function of positive type, that is, it satisﬁes condition (ii).

For this pick any points x1, ..., xm ∈ Rn. Let χi: Rn → {0,1} be the characteristic function of B(xi,T) and denote by φ,ψ the standard inner product between

functions φ and ψ in the Hilbert space L2(Rn). Then

vol(B(0,T) ∩ B(xi − xj,T)) volB(0,T)

gT(xi − xj) =

f(xi − xj)

vol(B(xi,T) ∩ B(xj,T)) volB(0,T)

f(xi − xj)

=

χi,χj volB(0,T)

f(xi − xj).

=

This shows that the matrix gT(xi − xj) mi,j=1 is positive semideﬁnite, being the Hadamard product, i.e. entrywise product, of two positive semideﬁnite matrices. We therefore have that gT is of positive type.

Now, gT is a continuous function of positive type and bounded support, satisfying condition (iii). It is very possible, however, that gT does not satisfy condition (i), and so the conclusion of the theorem may not apply to gT. Let us now ﬁx this problem.

Notice that gijT converges pointwise to fij as T → ∞. Moreover, for all T > 0 we have |gijT (x)| ≤ |fij(x)|. It then follows from Lebesgue’s dominated convergence theorem that gˆijT (0) → fˆij(0) as T → ∞. This means that there exists a number T0 > 0 such that for each T ≥ T0 we may pick a number α(T) ≥ 1 so that the function hT : Rn → CN×N such that

hTii(x) = α(T)giiT(x) for i = 1, ..., N, hTij(x) = gijT (x) for i, j = 1, ..., N with i = j

for all x ∈ Rn satisﬁes condition (ii). We may moreover pick the numbers α(T) in such a way that limT→∞ α(T) = 1.

It is also easy to see that each function hT is of positive type and bounded support and satisﬁes condition (iii). Hence the conclusion of the theorem applies for each hT, and so for every T ≥ T0 we see that

MT = max{hTii(0) : i = 1, ..., N }

is an upper bound for the density of any packing of translated copies of K1, ..., KN. But then, since giiT(0) = fii(0) for all T ≥ 0, and since limT→∞ α(T) = 1, we see that

max{fii(0) : i = 1, ..., N } = lim

MT, ﬁnishing the proof.

T→∞

4. Computations for binary spherical cap packings

In this and the next section we describe how we obtained the numerical results of Sections 1.2 and 1.3. Our approach is computational: to apply Theorems 1.2 and 1.3 we use techniques from semideﬁnite programming and polynomial optimization.

We start by brieﬂy discussing the case of binary spherical cap packings. Next we will discuss the more computationally challenging case of binary sphere packings.

It is a classical result of Luk´cs (see e.g. Theorem 1.21.1 in Szeg¨ [37]) that a real univariate polynomial p of degree 2d is nonnegative on the interval [a,b] if and only if there are real polynomials q and r such that p(x) = (q(x))2+(x−a)(b−x)(r(x))2. This characterization is useful when we combine it with the elementary but powerful observation (discovered independently by several authors, cf. Laurent [27]) that a real univariate polynomial p of degree 2d is a sum of squares of polynomials if and only if p(x) = v(x)TQv(x) for some positive semideﬁnite matrix Q, where v(x) = (1,x,...,xd) is a vector whose components are the monomial basis.

Let α1, ..., αN ∈ (0,π] be angles and d be an integer. Write v0(x) = (1,x,...,xd) and v1(x) = (1,x,...,xd−1). Using this characterization together with Theorem 1.2, we see that the optimal value of the following optimization problem gives an upper bound for the density of a packing of spherical caps with angles α1, ..., αN.

- Problem A. For k = 0, ..., 2d, ﬁnd positive semideﬁnite matrices fij,k Ni,j=1, and for i, j = 1, ..., N, ﬁnd (d + 1) × (d + 1) positive semideﬁnite matrices Qij and d × d positive semideﬁnite matrices Rij that minimize


2d

max

fii,k : i = 1, ..., N

k=0

and are such that

fij,0 − w(αi)1/2w(αj)1/2 Ni,j=1 is positive semideﬁnite and the polynomial identities

2d

fij,kPkn(u) + Qij,v0(u)v0(u)T

- (14)


k=0

+ Rij,(u + 1)(cos(αi + αj) − u)v1(u)v1(u)T = 0 are satisﬁed for i, j = 1, ..., N.

Above, A,B denotes the trace inner product between matrices A and B. Problem A is a semideﬁnite programming problem, as the polynomial identities (14) can each be expressed as 2d+1 linear constraints on the entries of the matrices involved. Indeed, to check that a polynomial is identically zero, it suﬃces to check that the coeﬃcient of each monomial 1, x, ..., x2d is zero, and for each such monomial we get a linear constraint.

In the above, we work with the standard monomial basis 1, x, ..., x2d, but we could use any other basis of the space of polynomials of degree at most 2d, both to deﬁne the vectors v0 and v1 and to check the polynomial identity (14). Such a change of basis does not change the problem from a formal point of view, but can drastically improve the performance of the solvers used. In our computations for binary spherical cap packings it was enough to use the standard monomial basis. We will see in the next section, when we present our computations for the Euclidean space, that a diﬀerent choice of basis is essential.

We reported in Section 1.2 on our calculations for N = 1, and 2 and n = 3, 4, and 5. The bounds, for the angles under consideration, do not seem to improve beyond d = 25, so we use this value for d in all computations. To obtain these bounds we used the solver SDPA-QD, which works with quadruple precision ﬂoating point numbers, from the SDPA family [18].

5. Computations for binary sphere packings

In this section we discuss our computational approach to ﬁnd upper bounds for the density of binary sphere packings using Theorem 1.3. This is a more diﬃcult application of semideﬁnite programming and polynomial optimization techniques than the one described in Section 4.

It is often the case in applications of sum of squares techniques that, if one formulates the problems carelessly, high numerical instability invalidates the ﬁnal results, or even numerical results cannot easily be obtained. This raises questions of how to improve the formulations used and the precision of the computations, so that we may provide rigorous bounds. We also address these questions and, since

the techniques we use and develop might be of interest to the reader who wants to perform computations in polynomial optimization, we include some details.

- 5.1. Theorem 1.3 for multiple-size sphere packings. In the case of multiplesize sphere packings, Theorem 1.3 can be simpliﬁed. The key observation here is that, when all the bodies Ki are spheres, then condition (iii) depends only on the norm of the vector x. More speciﬁcally, if each Ki is a sphere of radius ri,

then Ki◦ ∩ (x + Kj◦) = ∅ if and only if x ≥ ri + rj.

So in Theorem 1.3 one can choose to restrict oneself to radial functions. A function f : Rn → C is radial if the value of f(x) depends only on the norm of x. If f : Rn → C is radial, for t ≥ 0 we denote by f(t) the common value of f for vectors of norm t.

The Fourier transform fˆ(u) of a radial function f also depends only on the norm of u; in other words, the Fourier transform of a radial function is also radial. By restricting ourselves to radial functions, we obtain the following version of Theorem 1.3.

Theorem 5.1. Let r1, ..., rN > 0 and let f : Rn → RN×N be a matrix-valued function whose every component fij is a radial Schwartz function. Suppose f satisﬁes the following conditions:

- (i) the matrix f ˆij(0) − (volB(ri))1/2(volB(rj))1/2 Ni,j=1 is positive semideﬁnite, where B(r) is the ball of radius r centered at the origin;
- (ii) the matrix of Fourier transforms f ˆij(t) Ni,j=1 is positive semideﬁnite for every t > 0;
- (iii) fij(w) ≤ 0 if w ≥ ri + rj, for i, j = 1, ..., N.


Then the density of any packing of spheres of radii r1, ..., rN in the Euclidean space Rn is at most max{fii(0) : i = 1, ..., N }.

One might ask whether the restriction to radial functions worsens the bound of Theorem 1.3. For spheres, this is not the case. Indeed, suppose each body Ki is a sphere. If f : Rn → RN×N is a function satisfying the conditions of the theorem, then its radialized version, the function

f(x) =

Sn−1

f( x ξ)dωn(ξ),

also satisﬁes the conditions of the theorem, and it provides the same upper bound. This shows in particular that, for the case of multiple-size sphere packings, Theorem 5.1 is equivalent to Theorem 1.3.

- 5.2. A semideﬁnite programming formulation. To simplify notation and because it is the case of our main interest we now take N = 2. Everything in the following also goes through for arbitrary N with obvious modiﬁcations.


To ﬁnd a function f satisfying the conditions of Theorem 5.1 we specify f via its Fourier transform. Let d ≥ 0 be an odd integer and consider the even function ϕ: R≥0 → R2×2 such that

d

aij,kt2k,

ϕij(t) =

k=0

where each aij,k is a real number and aij,k = aji,k for all k. We set the Fourier transform of f to be

2

fˆij(u) = ϕij( u )e−π u

### . Notice that each fˆij is a Schwartz function, so its Fourier inverse is also Schwartz.

The reason why we choose this form for the Fourier transform of f is that it makes it simple to compute f from its Fourier transform by using the following result.

## Lemma 5.2. We have that

2

2

Lkn/2−1(π x 2),

u 2ke−π u

e2πiu·x du = k!π−ke−π x

### (15) Rn

where Ln/k 2−1 is the Laguerre polynomial of degree k with parameter n/2 − 1.

For background on Laguerre polynomials, we refer the reader to the book by Andrews, Askey, and Roy [1]. Proof. With f(u) = u 2ke−π u

2

, the left hand side of (15) is equal to fˆ(−x). By [1, Theorem 9.10.3] we have

∞

2

fˆ(−x) = 2π x 1−n/2

s2ke−πs

Jn/2−1(2πs x )sn/2 ds,

0

where Jn/2−1 is the Bessel function of the ﬁrst kind with parameter n/2−1. Using [1, Corollary 4.11.8] we see that this is equal to

1F1 −k n/2

Γ(k + n/2) Γ(n/2)

2

e−π x

### (16) π−k

;π x 2 , where 1F1 is a hypergeometric series.

By [1, (6.2.2)] we have

1F1 −k n/2

k! (n/2)k

Ln/k 2−1(π x 2), where (n/2)k = (n/2)(1 + n/2)···(k − 1 + n/2).

;π x 2 =

By substituting this in (16), and using the property that Γ(x + 1) = xΓ(x) for all x = 0,−1,−2,..., we obtain the right hand side of (15) as desired.

So we have

d

2

2

Ln/k 2−1(π x 2).

ϕij( u )e−π u

e2πiu·x du =

aij,k k!π−ke−π x

fij(x) =

Rn

k=0

Notice that it becomes clear that fij is indeed real-valued, as required by the theorem.

Consider the polynomial

d

akt2k.

p(t) =

k=0

2

According to Lemma 5.2, if g(x) is the Fourier inverse of gˆ(u) = p( u )e−π u

, then g( x ) = q( x )e−π x

2

, where

d

ak k!π−kLn/k 2−1(πw2)

q(w) =

k=0

is a univariate polynomial. We denote the polynomial q above by F−1[p]. Notice that F−1[p] is obtained from p via a linear transformation, i.e., its coeﬃcients are linear combinations of the coeﬃcients of p. With this notation we have

2

fij(x) = F−1[ϕij]( x )e−π x

. Let

2

d

aij,kt2kyiyj.

### (17) σ(t,y1,y2) =

i,j=1

k=0

If this polynomial is a sum of squares, then it is nonnegative everywhere, and hence the matrices ϕij(t) 2i,j=1 are positive semideﬁnite for all t ≥ 0. This implies that f satisﬁes condition (ii) of Theorem 5.1. (The converse is also true, that if the matrices ϕij(t) 2i,j=1 are positive semideﬁnite for all t ≥ 0, then σ is a sum of squares; For a proof see Choi, Lam, Reznick [7]. This fact is related to the KalmanYakubovich-Popov lemma in systems and control; see the discussion in Aylward, Itani, and Parrilo [2].)

Moreover, we may recover ϕ, and hence fˆ, from σ. Indeed we have

- ϕ11(t) = σ(t,1,0), ϕ22(t) = σ(t,0,1), and
- ϕ12(t) = (1/2)(σ(t,1,1) − σ(t,1,0) − σ(t,0,1)).


- (18)

So we can express condition (i) of Theorem 5.1 in terms of σ. We may also express condition (iii) in terms of σ, since it can be translated as

- (19) F−1[ϕij](w) ≤ 0 for all w ≥ ri + rj and i, j = 1, 2 with i ≤ j. If we ﬁnd a polynomial σ of the form (17) that is a sum of squares, is such that
- (20) ϕij(0) − (volB(ri))1/2(volB(rj))1/2 2i,j=1 is positive semideﬁnite, and satisﬁes (19), then the density of a packing of spheres of radii r1 and r2 is upper bounded by


max{F−1[ϕ11](0),F−1[ϕ22](0)}.

We may encode conditions (19) in terms of sums of squares polynomials (cf. Section 4), and therefore we may encode the problem of ﬁnding a σ as above as a semideﬁnite programming problem, as we show now.

Let P0, P1, ... be a sequence of univariate polynomials where polynomial Pk has degree k. Consider the vector of polynomials v, which has entries indexed by {0,..., d/2 } given by

v(t)k = Pk(t2) for k = 0, ..., d/2 . We also write V (t) = v(t)v(t)T.

Consider also the vector of polynomials m with entries indexed by {1,2} × {0,..., d/2 } given by

m(t,y1,y2)i,k = Pk(t2)yi for i, j = 1, 2 and k = 0, ..., d/2 .

Since σ is an even polynomial, it is a sum of squares if and only if there are positive semideﬁnite matrices S0, S1 ∈ R(d+1)×(d+1) such that

σ(t,y1,y2) = S0,m(t,y1,y2)m(t,y1,y2)T + S1,t2m(t,y1,y2)m(t,y1,y2)T .

From the matrices S0 and S1 we may then recover ϕij and also F−1[ϕij]. A more convenient way for expressing ϕij in terms of S0 and S1 is as follows. Consider the matrices

1 0 0 0

- 0 0
- 0 1


0 1/2 1/2 0

. Then

Y11 =

, Y22 =

, and Y12 =

ϕij(t) = S0,V (t) ⊗ Yij + S1,t2V (t) ⊗ Yij and

F−1[ϕij](w) = S0,F−1[V (t)](w) ⊗ Yij + S1,F−1[t2V (t)](w) ⊗ Yij , where F−1, when applied to a matrix, is applied to each entry individually.

With this, we may consider the following semideﬁnite programming problem for ﬁnding a polynomial σ satisfying the conditions we need.

- Problem B. Find (d + 1) × (d + 1) real positive semideﬁnite matrices S0 and S1, and ( d/2 +1)×( d/2 +1) real positive semideﬁnite matrices Q11, Q22, and Q12 that minimize


max{ S0,F−1[V (t)](0) ⊗ Y11 + S1,F−1[t2V (t)](0) ⊗ Y11 ,

S0,F−1[V (t)](0) ⊗ Y22 + S1,F−1[t2V (t)](0) ⊗ Y22 } and are such that

- (21) S0,V (0) ⊗ Yij − (volB(ri))1/2(vol(B(rj))1/2 2i,j=1 is positive deﬁnite and the polynomial identities
- (22)


S0,F−1[V (t)](w) ⊗ Yij + S1,F−1[t2V (t)](w) ⊗ Yij

+ Qij,(w2 − (ri + rj)2)V (w) = 0 are satisﬁed for i, j = 1, 2 and i ≤ j.

Any solution to this problem gives us a polynomial σ of the shape (17) which is a sum of squares and satisﬁes conditions (19) and (20), and so the optimal value is an upper bound for the density of any packing of spheres of radius r1 and r2. There might be, however, polynomials σ satisfying these conditions that cannot be obtained as feasible solutions to Problem B, since condition (22) is potentially more restrictive than condition (19) (compare Problem B above with Luk´cs’ result mentioned in Section 4). In our practical computations this restriction was not problematic and we found very good functions.

Observe also that Problem B is really a semideﬁnite programming problem. Indeed, the polynomial identities in (22) can each be represented as d + 1 linear constraints in the entries of the matrices Si and Qij. This is the case because testing whether a polynomial is identically zero is the same as testing whether each monomial has a zero coeﬃcient and so, since all our polynomials are even and of degree 2d, we need only check if the coeﬃcients of the monomials x2k are zero

- for k = 0, ..., d.


- 5.3. Numerical results. When solving Problem B, we need to choose a sequence P0, P1, ... of polynomials. A choice which works well in practice is


Pk(t) = µ−k 1Ln/k 2−1(2πt),

where µk is the absolute value of the coeﬃcient of Ln/k 2−1(2πt) with largest absolute value. We observed in practice that the standard monomial basis performs poorly.

To represent the polynomial identities in (22) as linear constraints we may check that each monomial x2k of the resulting polynomial has coeﬃcient zero. We may use, however, any basis of the space of even polynomials of degree at most 2d to represent such identities. Given such a basis, we expand each polynomial in it and check that the expansion has only zero coeﬃcients. The basis we use to represent the identities is P0(t2), P1(t2), ..., Pd(t2), which we observed to work much better than t0, t2, ..., t2d. Notice that no extra variables are necessary if we use a diﬀerent basis to represent the identities. We need only keep, for each polynomial in the matrices F−1[V (t)](w), F−1[t2V (t)](w), w2V (w), and V (w), its expansion in the basis we want to use.

The plot in Figure 3 was generated by solving Problem B with d = 31 using the solver SDPA-GMP from the SDPA family [18]. The input for the solver was generated by a SAGE [36] program working with ﬂoating-point arithmetic and precision of 256 bits. For each dimension 2, ..., 5 we solved Problem B with r1 = r/1000 and r2 = 1 for r = 200, ..., 1000; the reason we start with r = 200 is that for smaller values of r the solver runs into numerical stability problems. We also note that the solver has failed to solve some of the problems, and these points have

been disconsidered when generating the plot. The number of problems that could not be solved was small though: for n = 2 all problems could be solved, for n = 3 there were 6 failures, for n = 4 we had 18 failures, and ﬁnally for n = 5 the solver failed for 137 problems.

With our methods we can achieve higher values for d, but we noticed that the bound does not improve much after d = 31. For instance, in dimension 2 for r1 = 1/2 and r2 = 1, we obtain the bound 0.9174466... for d = 31 and the bound 0.9174426... for d = 51.

∗ ∗ ∗

In the previous account of how the plot in Figure 3 was generated, we swept under the rug all precision issues. We generate the data for the solver using ﬂoating-point arithmetic, and the solver also uses ﬂoating-point arithmetic. We cannot therefore be sure that the optimal value found by the solver gives a valid bound at all.

If we knew a priori that Problem B is strictly feasible (that is, that it admits a solution in which the matrices Si and Qij are positive deﬁnite), and if we had some control over the dual solutions, then we could use semideﬁnite programming duality to argue that the bounds we compute are rigorous; see for instance Gijswijt [17, Chapter 7.2] for an application of this approach in coding theory. The matter is however that we do not know that Problem B is strictly feasible, neither do we have knowledge about the dual solutions. In fact, most of our approach to provide rigorous bounds consists in ﬁnding a strictly feasible solution.

A naive idea to turn the bound returned by the solver into a rigorous bound would be to simply project a solution returned by the solver onto the subspace given by the constraints in (22). If the original solution is of good quality, then this would yield a feasible solution.

There are two problems with this approach, though. The ﬁrst problem is that the matrices returned by the solver will have eigenvalues too close to zero, and therefore after the projection they might not be positive semideﬁnite anymore. We discuss how to handle this issue below.

The second problem is that to obtain a rigorous bound one would need to perform the projection using symbolic computations and rational arithmetic, and the computational cost is just too big. For instance, we failed to do so even for d = 7.

Our approach avoids projecting the solution using symbolic computations. Here is an outline of our method.

- (1) Obtain a solution to the problem with objective value close the optimal

value returned by the solver, but in which every matrix Si and Qij is positive deﬁnite by a good margin and the maximum violation of the constraints is very small.

- (2) Approximate matrices Si and Qij by rational positive semideﬁnite matrices S¯i and Q¯ij having minimum eigenvalues at least λi and µij, respectively.
- (3) Compute a bound on how much constraints (22) are violated by S¯i and Q¯ij using rational arithmetic. If the maximum violation of the constraints is


small compared to the bounds λi and µij on the minimum eigenvalues, then we may be sure that the solution can be changed into a feasible solution without changing its objective value too much.

We now explain how each step above can be accomplished.

First, most likely the matrices Si, Qij returned by the solver will have eigenvalues very close to zero, or even slightly negative due to the numerical method which might allow infeasible steps.

To obtain a solution with positive deﬁnite matrices we may use the following trick (cf. L¨fberg [30]). We solve Problem B to ﬁnd its optimal value, say z∗. Then

we solve a feasibility version of Problem B in which the objective function is absent, but we add a constraint to ensure that

max{ S0,F−1[V (t)](0) ⊗ Y11 + S1,F−1[t2V (t)](0) ⊗ Y11 , S0,F−1[V (t)](0) ⊗ Y22 + S1,F−1[t2V (t)](0) ⊗ Y22 } ≤ z∗ + η,

where η > 0 should be small enough so that we do not jeopardize the objective value of the solution, but not too small so that a good strictly feasible solution exists. (We take η = 10−5, which works well for the purpose of making a plot.) The trick here is that most semideﬁnite programming solvers, when solving a feasibility problem, will return a strictly feasible solution — the analytical center —, if one can be found.

This partially addresses step (1), because though the solution we ﬁnd will be strictly feasible, it might violate the constraints too much. To quickly obtain a solution that violates the constraints only slightly, we may project our original solution onto the subspace given by constraints (22) using ﬂoating-point arithmetic of high enough precision. If the solution returned by the solver had good precision to begin with, then the projected solution will still be strictly feasible.

As an example, for our problems with d = 31, SDPA-GMP returns solutions that violate the constraints by at most 10−30. By doing a projection using ﬂoating-point arithmetic with 256 bits of precision in SAGE, we can bring the violation down to about 10−70 without aﬀecting much the eigenvalues of the matrices.

So we have addressed step (1). For step (2) we observe that simply converting the ﬂoating-point matrices Si, Qij to rational matrices would work, but then we would be in trouble to estimate the minimum eigenvalues of the resulting rational matrices in a rigorous way. Another idea of how to make the conversion is as follows.

Say we want to approximate ﬂoating-point matrix A by a rational matrix A¯. We start by computing numerically an approximation to the least eigenvalue of A. Say λ˜ is this approximation. We then use binary search in the interval [λ/˜ 2,λ˜] to ﬁnd the largest λ so that the matrix A − λI has a Cholesky decomposition; this we do using ﬂoating-point arithmetic of high enough precision. If we have this largest λ, then

A = LLT + λI

where L is the Cholesky factor of A − λI. Then we approximate L by a rational matrix L¯ and we set

A¯ = L¯L¯T + λI,

obtaining thus a rational approximation of A and a bound on its minimum eigenvalue.

Our idea for step (3) is to compare the maximum violation of constraints (22) with the minimum eigenvalues of the matrices. To formalize this idea, suppose that constraints (22) are slightly violated by S¯i, Q¯ij. So for instance we have

S ¯0,F−1[V (t)](w) ⊗ Y11 + S ¯1,F−1[t2V (t)](w) ⊗ Y11

- (23)


+ Q ¯11,(w2 − (2r1)2)V (w) = p,

where p is an even polynomial of degree at most 2d. Notice that we may compute an upper bound on the absolute values of the coeﬃcients of p using rational arithmetic.

To ﬁx this constraint we may distribute the coeﬃcients of p in the matrices S¯0 and Q¯11 (a very similar idea was presented by L¨fberg [29]). To make things precise,

- for k = 1, ..., d write


- i(k) = min{ d/2 ,k − 1},
- j(k) = k − 1 − i(k).


Pairs (i(k),j(k)) correspond to entries of the matrix V (w). Notice that the polynomial (w2 − (2r1)2)V (w)i(k)j(k) has degree 2k.

So the polynomials

- R0 = F−1[V (t)00](w),
- R1 = (w2 − (2r1)2)V (w)i(1)j(1),


.

Rd = (w2 − (2r1)2)V (w)i(d)j(d) form a basis of the space of even polynomials of degree at most 2d. We may then express our polynomial p in this basis as

p = α0R0 + ··· + αdRd. Now, we subtract α0 from (S¯0)(1,0),(1,0) and αk from (Q¯11)i(k)j(k), for k = 1, ..., d. The resulting matrices satisfy constraint (23), and as long as the αk are small enough, they should remain positive semideﬁnite. More precisely, it suﬃces to require that d (α1,...,αd) ∞ ≤ µ11 and |α0| ≤ λ0.

There are two issues to note in our approach. The ﬁrst one is that it has to be applied again twice to ﬁx the other two constraints in (22). The applications do not conﬂict with each other: in each one we change a diﬀerent matrix Q¯ij and diﬀerent entries of S¯0. We have to be careful though that we consider the changes to S¯0 at once in order to check that it remains positive semideﬁnite.

The second issue is how to compute the coeﬃcients αk. Computing them explicitly using symbolic computation is infeasible. One way to do it then is to consider the basis change matrix between the bases x2k, for k = 0, ..., d, and R0, ..., Rd, which we denote by U. Then we know that

(α0,...,αd) ∞ ≤ U−1 ∞ p ∞, where p ∞ is the ∞-norm of the vector of coeﬃcients of p in the basis x2k.

So if we have an upper bound for U−1 ∞ we are done. To quickly ﬁnd such an upper bound, we use an algorithm of Higham [24] (cf. also Higham [23]) which works for triangular matrices, like U. This bound proved to be good enough for our purposes.

6. Improving sphere packing bounds

We now prove Theorem 1.4 and show how to use it in order to compute the bounds presented in Table 1. Proof of Theorem 1.4. Let x1, ..., xN ∈ Rn and L ⊆ Rn be a lattice such that

N

v + xi + B

v∈L

i=1

is a sphere packing, where B is the ball of radius 1/2 centered at the origin. We may assume that, if i = j and v = 0, then the distance between the centers of v +xi +B and xj + B is greater than 1 + εm. Indeed, we could discard all xi that lie at distance less than 1+εm from the boundary of the fundamental parallelotope of L. If the fundamental parallelotope is big enough (and if it is not, we may consider a dilated version of L instead), this will only slightly alter the density of the packing, and the resulting packing will have the desired property.

Consider the sum

N

f(v + xi − xj).

- (24)


i,j=1 v∈L

Using the Poisson summation formula, we may rewrite it as

N

1 vol(Rn/L)

fˆ(u)e2πiu·(x

i−xj).

i,j=1 u∈L∗

By discarding all summands in the inner sum above except the one for u = 0, we see that (24) is at least

N2 volB vol(Rn/L)

.

For k = 1, ..., m, write Fk = {(i,j) : xi − xj ∈ [1 + εk−1,1 + εk)}. Then we see that (24) is at most

Nf(0) + η1|F1| + ··· + ηm|Fm|. So we see that

N volB vol(Rn/L) ≤ f(0) + η1|F1| N

+ ··· + ηm |Fm| N

.

Notice that the left-hand side above is exactly the density of our packing. Now, from the deﬁnition of M(ε), it is clear that for k = 1, ..., m we have

|F1| N

+ ··· + |Fk|

N ≤ M(εk), and the theorem follows.

To ﬁnd good functions f satisfying the conditions required by Theorem 1.4 we used the same approach from Section 5. We ﬁx an odd positive integer d and specify f via its Fourier transform, writing

d

akt2k

ϕ(t) =

k=0

and setting

2

fˆ(u) = ϕ( u )e−π u

. Using Lemma 5.2 we then have that

2

f(x) = F−1[ϕ]( x )e−π x

, where

d

akk!π−kLkn/2−1(πw2) is a polynomial obtained as a linear transformation of ϕ.

F−1[ϕ](w) =

k=0

Constraint (ii), requiring that fˆ(u) ≥ 0 for all u ∈ Rn, can be equivalently expressed as requiring that the polynomial ϕ should be a sum of squares.

Recalling the result of Luk´cs mentioned in Section 4, one may also express constraint (iii) in terms of sums of squares: one simply has to require that there exist polynomials p0(w) and q0(w) such that

F−1[ϕ](w) = −(p0(w))2 − (w2 − (1 + εm)2)(q0(w))2.

In a similar way, one may express constraints (iv). For instance, for a given k, we require that there should exist polynomials pk(w) and qk(w) such that F−1[ϕ](w)e−π(1+ε

k−1)2 − η1 = −(pk(w))2 − (w − (1 + εk−1))((1 + εk) − w)(qk(w))2, and this implies (iv).

So we may represent the constraints on f in terms of sums of squares, and therefore also in terms of semideﬁnite programming, as we did in Sections 4 and 5. There

is only the issue that now we want to ﬁnd a function f that satisﬁes constraints (i)– (iv) of the theorem and that minimizes the maximum in (2). This does not look like a linear objective function, but since by linear programming duality this maximum is equal to

min f(0) + y1U(ε1) + ··· + ymU(εm) yi + ··· + ym ≥ ηi for i = 1, ..., m, yk ≥ 0 for k = 1, ..., m,

we may transform our original problem into a single minimization semideﬁnite programming problem, the optimal value of which provides an upper bound for the densities of sphere packings.

It is still a question how to compute upper bounds for M(ε). For this we use upper bounds on the sizes of spherical codes. A spherical code with minimum angular distance 0 < θ ≤ π is a set C ⊆ Sn−1 such that the angle between any two distinct points in C is at least θ. In other words, a spherical code with minimum angular distance θ gives as packing of spherical caps with angle θ/2. We denote by A(n,θ) the maximum cardinality of any spherical code in Sn−1 with minimum angular distance θ.

There is a simple relation between A(n,θ) and M(ε). Namely, if ε < √2 − 1, then

M(ε) ≤ A(n,arccost(ε)), where

1 2(1 + ε)2

t(ε) = 1 −

.

To see this, suppose x, y ∈ Rn are such that x , y ∈ [1,1+ε) and x−y ≥ 1. Then by the law of cosines, if θ is the angle between x and y, we have

x 2 + y 2 − x − y 2 2 x y

. The maximum of the right-hand side above for vectors x and y such that x , y ∈ [1,1 + ε) and x − y ≥ 1 gives t(ε).

cosθ =

Indeed, to maximize the right-hand side above, we may assume that x−y = 1. Then

α2 + β2 − 1 2αβ

cosθ =

= Θ(α,β), where α = x and β = y .

If we compute the derivative of Θ(α,β) with respect to α we obtain

α2 − β2 + 1 2α2β

.

From this we see that, since ε < √2 − 1, for a ﬁxed β ∈ [1,1 + ε), function Θ(α,β) is increasing in α, for α ≥ 1. Similarly, by taking the derivative with respect to β, one may conclude that for a ﬁxed α ∈ [1,1+ε), function Θ(α,β) is increasing in β, for β ≥ 1. So Θ(α,β) is maximized in our domain when one takes α = β = 1 + ε. This implies that

1 2(1 + ε)2

cosθ ≤ Θ(1 + ε,1 + ε) = 1 −

, and so we have t(ε).

For the bounds of Table 1 we took d = 31. To compute upper bounds for A(n,θ) we used the semideﬁnite programming bound of Bachoc and Vallentin [4]. The bounds we used for computing Table 1 are given in Table 2.

Finally, we mention that all numerical issues discussed in Section 5 also happen with the approach we sketched in this section. In particular, the choices of bases are

important for the stability of the semideﬁnite programming problems involved. We use the same bases as described in Section 5 though, so we skip a detailed discussion here. Notice moreover that our bounds are rigorous, having been checked with the same approach described in Section 5.

Dimension (ε,U(ε)) pairs

- 3 (0.022753, 12), (0.054092, 13), (0.082109, 14), (0.113864, 15)
- 4 (0.008097, 24), (0.017446, 25), (0.025978, 26), (0.036951, 27)
- 5 (0.003013, 45), (0.008097, 46), (0.013259, 47), (0.017446, 48)
- 6 (0.002006, 79), (0.004024, 80), (0.006054, 81), (0.008097, 82)
- 7 (0.001001,136), (0.002006,137), (0.003013,138), (0.004024,139), (0.005037,140)


9 (0.003013,373), (0.029233,457), (0.030325,459), (0.031421,464), (0.032520,468), (0.033622,473)

Table 2. For each dimension considered in Table 1 we show here the sequence ε1 < ··· < εm and the upper bounds U(εk) used in our application of Theorem 1.4.

We refrained from performing similar calculations for higher dimensions because of two reasons. Firstly, we expect that the improvements are only minor. Secondly, the computations of the upper bounds for M(ε) in higher dimensions require substantially more time as one needs to solve the semideﬁnite programs with a high accuracy solver, see Mittelmann and Vallentin [32].

Acknowledgements

We thank Rudi Pendavingh and Hans D. Mittelmann for very helpful discussions from which we learned how to perform the numerically stable computations.

References

- [1] G.E. Andrews, R. Askey, and R. Roy, Special Functions, Cambridge University Press, Cambridge, 1999.
- [2] E. Aylward, S. Itani, and P.A. Parrilo, Explicit SOS decompositions of univariate polynomial matrices and the Kalman-Yakubovich-Popov Lemma, Proceedings of the 46th IEEE Conference on Decision and Control, 2007.
- [3] C. Bachoc, G. Nebe, F.M. de Oliveira Filho, and F. Vallentin, Lower bounds for measurable chromatic numbers, Geom. Funct. Anal. 19 (2009), 645–661. (http://arxiv.org/abs/0801. 1059)
- [4] C. Bachoc and F. Vallentin, New upper bounds for kissing numbers from semideﬁnite programming, J. Amer. Math. Soc. 21 (2008), 909–924. (http://arxiv.org/abs/math/0608426)
- [5] S. Bochner, Hilbert distances and positive deﬁnite functions, Ann. of Math. (3) 42 (1941), 647–656.
- [6] S. Bochner, Vorlesungen u¨ber Fouriersche Integrale, Akademische Verlagsgesellschaft, Leipzig, 1932.
- [7] M.D. Choi, T.Y. Lam, and B. Reznick, Real zeros of positive semideﬁnite forms I, Math. Z. 171 (1980) 1–26.
- [8] H. Cohn and N.D. Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157

(2003), 689–714. (http://arxiv.org/abs/math/0110009)

- [9] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc 20 (2007), 99–148. (http://arxiv.org/abs/math/0607446)
- [10] R. Courant, D. Hilbert, Methods of mathematical physics, Interscience Publishers, 1953.
- [11] P. Delsarte, J.M. Goethals, and J.J. Seidel, Spherical codes and designs, Geom. Dedicata 6

(1977), 363–388.

- [12] A. Florian, Ausf¨ullung der Ebene durch Kreise, Rend. Circ. Mat. Palermo 9 (1960) 300–312.


- [13] A. Florian, Packing of incongruent circles on the sphere, Monatsh. Math. 133 (2001), 111–129.
- [14] A. Florian, Remarks on my paper: packing of incongruent circles on the sphere, Monatsh. Math. 152 (2007), 39–43.
- [15] A. Florian and A. Heppes, Packing Circles of Two Diﬀerent Sizes on the Sphere II, Period. Math. Hungar. 39 (1999), 125–127.
- [16] G.B. Folland, A Course in Abstract Harmonic Analysis, Studies in Advanced Mathematics, CRC Press, Boca Raton, 1995.
- [17] D.C. Gijswijt, Matrix Algebras and Semideﬁnite Programming Techniques for Codes, PhD thesis, University of Amsterdam, 2005. (http://arxiv.org/abs/1007.0906)
- [18] K. Fujisawa, M. Fukuda, K. Kobayashi, M. Kojima, K. Nakata, M. Nakata, and M. Yamashita, SDPA (SemiDeﬁnite Programming Algorithm) Users Manual — Version 7.0.5, Research Report B-448, Dept. of Mathematical and Computing Sciences, Tokyo Institute of Technology, Tokyo, 2008, http://sdpa.sourceforge.net.
- [19] M. Gr¨otschel, L. Lova´sz, and A. Schrijver, The ellipsoid method and its consequences in combinatorial optimization, Combinatorica 1 (1981), 169–197.
- [20] T.C. Hales, A proof of the Kepler conjecture, Ann. of Math. (2) 162 (2005), 1065–1185.
- [21] A. Heppes, Some Densest Two-Size Disc Packings in the Plane, Discrete Comput. Geom. 30

(2003), 241–262.

- [22] A. Heppes and G. Kerte´sz, Packing circles of two diﬀerent sizes on the sphere, in: Intuitive Geometry, Bolyai Soc. Math. Stud. 6 (1997), 357–365.
- [23] N.J. Higham, A survey of condition number estimation for triangular matrices, SIAM Review 29 (1987) 575–595.
- [24] N.J. Higham, Upper bounds for the condition number of a triangular matrix, Numerical Analysis Report No. 86, University of Manchester, Manchester, 1983.
- [25] A.B. Hopkins, Y. Jiao, F.H. Stillinger, and S. Torquato, Phase diagram and structural diversity of the densest binary sphere packings, Phys. Rev. Lett. 107 (2011), 125501, 5pp. (http://arxiv.org/abs/1108.2210)
- [26] A.B. Hopkins, F.H. Stillinger, and S. Torquato, Densest binary sphere packings, Phys. Rev. E 85, 021130 (2012), 19pp. (http://arxiv.org/abs/1111.4917)
- [27] M. Laurent, Sums of squares, moment matrices and optimization over polynomials, in: Emerging Applications of Algebraic Geometry, Vol. 149 of IMA Volumes in Mathematics and its Applications (M. Putinar and S. Sullivant, eds.), Springer, New York, 2009, pp. 157–270.
- [28] V.I. Levenshtein, Universal bounds for codes and designs, in: Handbook of Coding Theory, Vol. I, North-Holland, Amsterdam, 1998, pp. 499–648.
- [29] J. L¨ofberg, Pre- and post-processing sums-of-squares programs in practice, IEEE Transactions on Automatic Control 54 (2009), 1007–1011.
- [30] J. L¨ofberg, Strictly feasible sums-of-squares solutions, post in YALMIP Wiki, 2011.
- [31] B. Masnick and J. Wolf, On linear unequal error protection codes, IEEE Transactions on Information Theory 13 (1967), 600–607.
- [32] H.D. Mittelmann and F. Vallentin, High accuracy semideﬁnite programming bounds for kissing numbers, Experiment. Math. 19 (2010), 174–178. (http://arxiv.org/abs/0902. 1105)
- [33] C.A. Rogers, The packing of equal spheres, Proc. London Math. Soc. 8 (1958), 609-620.
- [34] I.J. Schoenberg, Positive deﬁnite functions on spheres, Duke Math. J. 9 (1942), 96–108.
- [35] A. Schrijver, Combinatorial Optimization: Polyhedra and Eﬃciency, Springer-Verlag, Berlin, 2003.
- [36] W.A. Stein et al., Sage Mathematics Software (Version 4.8), The Sage Development Team, 2012, http://www.sagemath.org.
- [37] G. Szego¨, Orthogonal Polynomials, American Mathematical Society Colloquium Publications Volume XXIII, American Mathematical Society, Providence, 1975.
- [38] A. Terras, Harmonic analysis on symmetric spaces and applications I, Springer-Verlag, Berlin, Heidelberg and New York, 1985.
- [39] S. Torquato, Random Heterogeneous Materials, Microstructure and macroscopic properties, Springer-Verlag, New York, 2002.


D. de Laat, Delft Institute of Applied Mathematics, Delft University of Technol-

ogy, P.O. Box 5031, 2600 GA Delft, The Netherlands E-mail address: mail@daviddelaat.nl F.M. de Oliveira Filho, Institut fur¨ Mathematik, Freie Universitat¨ Berlin, Arnim-

allee 2, 14195 Berlin, Germany E-mail address: fmario@mi.fu-berlin.de F. Vallentin, Delft Institute of Applied Mathematics, Delft University of Tech-

nology, P.O. Box 5031, 2600 GA Delft, The Netherlands E-mail address: f.vallentin@tudelft.nl

