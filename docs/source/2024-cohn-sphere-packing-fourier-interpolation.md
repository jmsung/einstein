---
type: source
kind: paper
title: From sphere packing to Fourier interpolation
authors: Henry Cohn
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2407.14999v1
source_local: ../raw/2024-cohn-sphere-packing-fourier-interpolation.pdf
topic: general-knowledge
cites:
---

# arXiv:2407.14999v1[math.MG]20Jul2024

BULLETIN (New Series) OF THE AMERICAN MATHEMATICAL SOCIETY Volume 61, Number 1, January 2024, Pages 3–22 https://doi.org/10.1090/bull/1813 Article electronically published on October 6, 2023

## FROM SPHERE PACKING TO FOURIER INTERPOLATION

HENRY COHN

Abstract. Viazovska’s solution of the sphere packing problem in eight dimensions is based on a remarkable construction of certain special functions using modular forms. Great mathematics has consequences far beyond the problems that originally inspired it, and Viazovska’s work is no exception. In this article, we’ll examine how it has led to new interpolation theorems in Fourier analysis, specifically a theorem of Radchenko and Viazovska.

1. Sphere packing

The sphere packing problem asks how densely congruent spheres can be packed in Euclidean space. In other words, what fraction of space can be filled with congruent balls, if their interiors are required to be disjoint?1 Everyone can pack spheres intuitively in low dimensions: the optimal two-dimensional packing is a hexagonal arrangement, and optimal three-dimensional packings are stacks of optimal twodimensional layers, nestled together as closely as possible into the gaps in the layers (see Figure 1.1).

In fact, these packings are known to be optimal. The two-dimensional problem was solved by Thue [42,43], with a more modern proof by Fejes T´th [21], and the three-dimensional problem was solved by Hales [23]. The two-dimensional proof is not so complicated, but the three-dimensional proof is difficult to check, because it relies on both enormous machine calculations and lengthy human arguments in a sequence of papers. To give a definitive demonstration of its correctness, Hales and a team of collaborators have produced a formally verified proof [24], i.e., a proof that has been algorithmically verified using formal logic.

On the one hand, the solution of the three-dimensional sphere packing problem is a triumph of modern mathematics, a demonstration of humanity’s ability to overcome even tremendously challenging obstacles. On the other hand, to a general audience it can sound like a parody of pure mathematics, in which mathematicians devote immense efforts to proving an intuitively obvious assertion. It’s natural to feel discouraged about the future of a subfield in which it’s easy to guess the answer and almost impossible to prove it. For comparison, a rigorous solution of the four-dimensional sphere packing problem remains far out of reach. If the difficulty increases as much from three to four dimensions as it did from two to three, then humanity may never see a proof.

Received by the editors July 17, 2023. 2020 Mathematics Subject Classification. Primary 52C17, 42A15. 1To make this question precise, we could take the limit as r → ∞ of the density for packing

unit spheres in a sphere of radius r, or a cube of side length r. We would obtain the same limit for any reasonable container (see, for example, [7]).

3

©2023 by Henry Cohn

Figure 1.1. A two-dimensional cross section of an optimal threedimensional sphere packing, with dotted lines indicating spheres in an adjacent layer.

One noteworthy change as we move to higher dimensions is that we lose much of our intuition, and the answer is no longer easy to guess. For example, it is not always true that we can obtain an optimal packing in Rn by stacking optimal (n − 1)-dimensional layers (see [16] for details). In sufficiently high dimensions, there are no conjectures for optimal packings, the best upper and lower bounds known for the packing density differ by an exponential factor in the dimension, and we cannot even predict whether the densest packings should be crystalline or disordered. In short, we know shockingly little about how spherical particles behave in high dimensions. Of course this means there are plenty of intriguing phenomena to explore.

Certain dimensions stand out in the midst of this ignorance as having exceptionally dense packings. The most amazing of all are eight and twenty-four dimensions, which feature the E8 root lattice and the Leech lattice Λ24. (We will not construct these lattices here; see [17,20,41] for constructions.) Recall that a lattice in Rn is just a discrete subgroup of rank n; in other words, for each basis v1, ..., vn of Rn, the set

{a1v1 + ··· + anvn : a1,...,an ∈ Z} is a lattice. Every lattice leads to a sphere packing by centering congruent spheres at the lattice points, with the radius chosen as large as possible without overlap. Lattice packings are common in low dimensions, but there is no reason to expect an optimal packing to have this sort of algebraic structure in general. For example, in R10 the best packing known, the aptly named Best packing [5], has density more than 8% greater than any known lattice packing in R10. By contrast, the E8 and Leech lattices yield impressively dense packings with extraordinary symmetry groups, and their density and symmetry are so far out of the ordinary that it is difficult to imagine how they could be improved.

In 2016 Maryna Viazovska [44] solved the sphere packing problem in R8 with an innovative use of modular forms, which was soon extended to R24 as well [13]; both E8 and the Leech lattice do indeed turn out to be optimal sphere packings. These are the only cases in which the sphere packing problem has been solved above three dimensions. Although the proofs require more machinery than those in two or three dimensions, most notably the theory of modular forms, they are much shorter and simpler than one might fear. Viazovska’s proof dispelled the gloomy possibility that higher-dimensional sphere packing could be beyond human understanding, and she was awarded a Fields Medal in 2022 for this line of work.

In addition to her breakthrough in sphere packing, Viazovska’s modular form techniques have led to unexpected consequences, such as interpolation theorems showing that a radial function f can be reconstructed from the values of f and its Fourier transform f on certain discrete sets of points. Although Fourier interpolation may sound rather far afield from sphere packing, it turns out to be closely connected. In this article, we’ll explore how Viazovska’s work led to this connection and how to prove a fundamental interpolation theorem of Radchenko and Viazovska [38]. For comparison, [32], [9], [45], [46], and [10] are expositions of her work that focus on other themes.

2. From sphere packing to Fourier analysis

The connection between packing problems and Fourier analysis originated in the work of Delsarte [19] on linear programming bounds for error-correcting codes. For sphere packings in Euclidean space, a continuous analogue of Delsarte’s work was developed by Cohn and Elkies [11]. The quality of this bound depends on the choice of an auxiliary function satisfying certain inequalities, and Viazovska’s breakthrough amounted to figuring out how to optimize that choice.

We will normalize the Fourier transform of an integrable function f : Rn → C by f(y) =

f(x)e−2πi⟨x,y⟩ dx,

Rn

where ⟨·,·⟩ denotes the usual inner product on Rn. We’ll generally restrict our attention to Schwartz functions, i.e., infinitely differentiable functions f such that for all real numbers c > 0 and nonnegative integers i1,...,in,

1+···+in ∂xi

∂i

f(x1,...,xn) = O(|x|−c)

1 ···∂xi

1

nn

as |x| → ∞. These smoothness and decay conditions can be somewhat weakened in each application below, but Schwartz functions are the best-behaved case. We’ll also frequently study radial functions, i.e., functions f for which f(x) depends only on |x|, in which case we will write f(r) for r ∈ [0,∞) to denote the value f(x) with |x| = r and f′ for the radial derivative of f. Note that the spaces of radial functions and of Schwartz functions are both preserved by the Fourier transform.

The linear programming bound is the following method for producing a density bound from a suitable auxiliary function f. The name “linear programming bound” refers to the fact that optimizing this bound can be recast as an infinite-dimensional linear programming problem (i.e., linear optimization problem).

Rnn-throotofspherepackingdensityin

- 0 4 8 12 16 20 24 28 32 36 40 44 48

0.5

0.6

0.7

0.8

0.9

- 1


linear programming bound sphere packing density

dimension n

Figure 2.1. A plot of the numerically computed linear programming bound [2] and the best sphere packing density currently known [17]. The plot shows the n-th root of the density in dimension n, with n = 8 and n = 24 marked by vertical lines.

- Theorem 2.1 (Cohn and Elkies [11]). Let f : Rn → R be a radial Schwartz function and r a positive real number such that


- (1) f(x) ≤ 0 whenever |x| ≥ r,
- (2) f(y) ≥ 0 for all y, and
- (3) f(0) = f(0) = 1.


Then the optimal sphere packing density in Rn is at most the volume vol(Br/n 2) of a ball of radius r/2 in Rn.

It is far from obvious how to produce good auxiliary functions f for use in this theorem, or how to optimize the choice of f, i.e., minimize r. In fact, the exact optimum is known only for n = 1, 8, and 24. However, one can perform a numerical optimization over a suitable space of functions, such as polynomials of fixed degree times a Gaussian, with the hope that it will converge to the global optimum as the degree tends to infinity. Figure 2.1 compares the resulting numerical bound with the density of the best packing known.

In most dimensions, the linear programming bound seems nowhere near sharp, but the upper and lower bounds appear to touch in eight and twenty-four dimensions. Cohn and Elkies conjectured that they were equal in those cases, and the solutions of the sphere packing problem in these dimensions come from proving

this conjecture.2 For comparison, it is known that the linear programming bound cannot be sharp in dimensions three through five [33], six [18], twelve, or sixteen [15], and it is likely that the only sharp cases are dimensions one, two, eight, and twenty-four.

The optimal auxiliary functions in eight and twenty-four dimensions have come to be known as magic functions, because obtaining an exact solution in these dimensions feels like a miracle. To see how this miracle comes about, we will examine a proof of Theorem 2.1 for the special case of lattice packings. It is based on the Poisson summation formula, which states that

1 vol(Rn/Λ) y∈Λ

f(y)

f(x) =

∗

x∈Λ

for every Schwartz function f : Rn → C and lattice Λ in Rn. In this formula, vol(Rn/Λ) is the volume of the quotient torus (i.e., the volume of a fundamental parallelotope for the lattice or, equivalently, the absolute value of the determinant of a basis), and Λ∗ is the dual lattice, which is spanned by the dual basis v1∗, ..., vn∗ to any basis v1, ..., vn of Λ (i.e., ⟨vi∗,vj⟩ = δi,j). Poisson summation expresses a fundamental duality for Fourier analysis on Rn, and we can apply it as follows.

Proof of Theorem 2.1 for lattice packings. Suppose our sphere packing consists of spheres centered at the points of a lattice Λ in Rn. The sphere packing density is scaling-invariant, and so without loss of generality we can assume that the minimal nonzero vectors in Λ have length r. In other words, the sphere packing uses spheres of radius r/2, so that neighboring spheres are tangent to each other. Then the packing density is vol(Br/n 2)/vol(Rn/Λ), since there is one sphere for each fundamental cell of Λ.

We now apply Poisson summation to the auxiliary function f, to obtain

1 vol(Rn/Λ) y∈Λ

f(x) =

f(y).

∗

x∈Λ

The left side of this equation is bounded above by f(0) = 1, because f(x) ≤ 0 whenever |x| ≥ r, and the right side is bounded below by f(0)/vol(Rn/Λ) = 1/vol(Rn/Λ), since every summand is nonnegative. Thus, we conclude that 1/vol(Rn/Λ) ≤ 1, and the sphere packing density satisfies vol(Br/n 2)/vol(Rn/Λ) ≤ vol(Br/n 2), as desired. □

The proof for more general packings is similar in spirit, but it applies Poisson summation to periodic packings given by unions of translates of a lattice. See [11] or [9] for the details.

Note that the proof of Theorem 2.1 does not actually require f to be radial. However, the conditions on f are linear and rotation-invariant, and thus we can assume f is radial without loss of generality via rotational averaging.

What sort of function f could show that a lattice Λ is an optimal sphere packing? The proof given above drops the terms f(x) with x ∈ Λ \ {0} and f(t) for y ∈ Λ∗ \ {0}. Thus, we obtain a sharp bound if and only if all these omitted terms vanish. Because f and f are radial functions, these conditions amount to saying

2The linear programming bound also seems to be sharp in two dimensions, but no proof is known, despite the fact that the two-dimensional sphere packing problem itself can be solved by elementary means.

f

f

√2 √4 √6 √8

√2 √4 √6 √8

Figure 2.2. This diagram, which is taken from [9], shows the roots of the magic function f and its Fourier transform f in eight dimensions. It is not an accurate plot, since these functions decrease very rapidly.

that f vanishes on all the nonzero vector lengths in Λ, while f vanishes on all the nonzero vector lengths in Λ∗. Furthermore, f and f cannot change sign at these roots, except for a sign change in f at the minimal nonzero vector length in Λ.

It turns out that the E8 and Leech lattices are both self-dual, and their nonzero vector lengths are simply

√

2k for integers k ≥ 1 in E8 and k ≥ 2 in Λ24. Thus, we know exactly what the roots of the magic functions should be. These roots are shown in Figure 2.2 for eight dimensions.

Now the whole problem comes down to constructing magic functions with these roots. That might not seem so difficult, but controlling the behavior of f and f simultaneously is a subtle problem. Of course we can obtain any roots we’d like for f or f in isolation, but not necessarily at the same time. This phenomenon is a form of uncertainty principle [8,12,22], much like the Heisenberg uncertainty principle.

Viazovska gave a remarkable construction of the eight-dimensional magic function in terms of modular forms, which are a class of special functions defined on the upper half-plane H = {z ∈ C : Im(z) > 0} and satisfying certain transformation laws. The general theory of modular forms can feel somewhat forbidding to beginners, but Poisson summation gives us a simple way to get our hands on one example. The theta function θ: H → C is defined by

2z = 1 + 2eπiz + 2e4πiz + 2e9πiz + ··· ,

eπin

θ(z) =

n∈Z

which converges because z ∈ H means Im(z) > 0 and thus |eπiz| < 1. This function satisfies two key identities,

- (2.1) θ(z + 2) = θ(z) and θ(−1/z) = (−iz)1/2θ(z).


The first identity follows immediately from the defining series, while the second is more subtle and will be proved below. In this equation, we have to choose the branch for (−iz)1/2 carefully. Throughout this paper, fractional powers such as this one will be defined to be positive on the upper imaginary axis (0,∞)i in H and continuous on H.

To prove that θ(−1/z) = (−iz)1/2θ(z), we will use Poisson summation for the one-dimensional lattice Z in R. Consider the complex Gaussian f : R → C defined by

2

f(x) = eπizx

−3 −2 −1 0 1 2 3

Figure 2.3. The regions shown here are ideal hyperbolic triangles (i.e., triangles in the hyperbolic plane with vertices at infinity), and they are fundamental domains for the action of Γθ on the upper half-plane. In particular, each Γθ-orbit intersects each triangle exactly once, unless it intersects the boundary of the triangle. The dots show a typical Γθ-orbit.

with z ∈ H. When z is purely imaginary, this function is an ordinary Gaussian, and the other points in H behave much the same. In particular, one can check that

2

- (2.2) f(y) = (−iz)−1/2eπi(−1/z)y


,

which is the complex generalization of the fact that the Fourier transform of a wide Gaussian is a narrow Gaussian, and vice versa. Now Poisson summation says that

f(x) =

f(y),

x∈Z

y∈Z

because Z is self-dual. This equation amounts to

2

eπizx

x∈Z

### =

2

(−iz)−1/2eπi(−1/z)y

,

y∈Z

and thus θ(−1/z) = (−iz)1/2θ(z).

The functions z  → z + 2 and z  → −1/z map H to itself, and they generate a group of linear fractional transformations of H called Γθ, in honor of the function θ. One can put a metric on H that turns it into the hyperbolic plane, at which point Γθ becomes a discrete group of isometries of H, but we will not need this interpretation. See Figure 2.3 for a picture of a Γθ-orbit in H.

Together with analyticity and some growth conditions, the identities (2.1) say that θ is a modular form of weight 1/2 for the group Γθ. Viazovska’s solution of the eight-dimensional sphere packing problem constructs the magic function using θ and a number of other modular forms, in a way that looks rather mysterious. What do modular forms have to do with radial Schwartz functions?

Instead of examining the details of Viazovska’s construction, let’s think about a bigger picture. We know the eight-dimensional magic function f should satisfy

√

2k = 0 for k ≥ 1, f′

f

√

2k = 0 for k ≥ 2, f

√

2k = 0 for k ≥ 1, and f ′

√

2k = 0 for k ≥ 1,

- as in Figure 2.2. Viazovska conjectured that this data, together with the nonzero value f′ √2 , would be enough to determine f uniquely. In fact, that turns out to be true:


- Theorem 2.2 (Cohn, Kumar, Miller, Radchenko, and Viazovska [14]). Let (n,k0) be (8,1) or (24,2). Then every radial Schwartz function f : Rn → C is uniquely


√

√

√

√

2k , f′

2k , and f ′

2k for integers k ≥

2k , f

determined by the values f

k0. Specifically, there exists an interpolation basis ak,bk, ak, bk of radial Schwartz functions on Rn for k ≥ k0 such that for every f and x ∈ Rn,

∞

∞

√

√

f′

f(x) =

f

2k ak(x) +

2k bk(x)

k=k0

k=k0

∞

∞

√

√

f ′

f

+

2k ak(x) +

2k bk(x),

k=k0

k=k0

where these sums converge absolutely.

In particular, up to scaling the magic function is the interpolation basis function bk

in this theorem. One does not need this interpolation theorem to solve the sphere packing problem, but it is needed for analyzing ground states of more general particle systems in R8 and R24 (see [14]), and it provides a broader context for the magic functions.

0

- Theorem 2.2 is similar in spirit to other interpolation theorems in mathematics.


The simplest and most famous of these theorems is Lagrange interpolation, which says that a polynomial in one variable of degree less than n can be reconstructed from its values at any n distinct points. If the interpolation points are x1, ..., xn, then we can write down an interpolation basis p1, ..., pn as

n

x − xj xk − xj

- (2.3) pk(x) =


,

j=1 j̸=k

so that every polynomial f of degree less than n is given by

n

f(x) =

f(xj)pj(x).

j=1

Lagrange interpolation can be generalized to Hermite interpolation, which takes into account derivatives along similar lines to Theorem 2.2: a polynomial f can be reconstructed from the values f(j)(xk) with 0 ≤ j < dk and 1 ≤ k ≤ m if its degree is less than mk=1 dk.

One important relative of Lagrange interpolation is Shannon sampling, which in the case of Schwartz functions f : R → C says that if f vanishes outside the interval [−r/2,r/2] for some r, then f is determined by its values on r−1Z via

sinπ(rx − n) π(rx − n)

f(x) =

f(n/r)

.

n∈Z

This theorem plays a crucial role in information theory, since it says that a bandlimited signal (i.e., one with a limited range of frequencies) is determined by periodic samples. It’s worth noting that the product formula

∞

sinπx πx

x j2

1 −

=

- (2.4)


j=1

is analogous to the products (2.3) in the Lagrange interpolation basis. Much is known about Shannon sampling and its variations; see, for example, [29] and the references cited therein.

Both Lagrange interpolation and Shannon sampling rely on a notion of size. We measure the size of a polynomial by its degree, and the size of a band-limited function by its bandwidth, the smallest r such that supp( f) ⊆ [−r/2,r/2]. Then the larger a function is, the more interpolation points are required to reconstruct it, with “more” referring to density in the band-limited case. Here the intuition is that size controls how many roots a function can have.3

Puzzlingly, Theorem 2.2 shows no sign of a similar notion of size. It is reminiscent of Shannon sampling, in that it takes into account both f and f, but it treats them symmetrically. In particular, there is little hope of a product formula along the lines of (2.3) or (2.4), because specifying the roots of f will not yield the roots of f. There seems to be a fundamental difference between these interpolation formulas, and neither Lagrange interpolation nor Shannon sampling offers a clue as to how to prove Theorem 2.2.

3. First-order Fourier interpolation

How does one prove an interpolation theorem like Theorem 2.2? We’ll examine a technically simpler variant due to Radchenko and Viazovska, which is important in its own right and a beautiful illustration of Fourier interpolation. It deals with functions of one variable (so “radial” becomes “even”), and it studies interpolation to first order, without derivatives. This first-order interpolation theorem does not seem to have any applications to sphere packing, but it’s a fundamental fact about Fourier analysis, and it is remarkable that it was not known until well into the 21st century.

- Theorem 3.1 (Radchenko and Viazovska [38]). There exist even Schwartz func-


tions an: R → R for n = 0, 1, 2, ... such that every even Schwartz function f : R → R satisfies

∞

∞

f √n an(x) +

f √n an(x) for all x ∈ R, and these sums converge absolutely.

f(x) =

n=0

n=0

3Furthermore, size is related to growth at infinity. For degrees of polynomials this is clear, while a band-limited function of bandwidth r can be analytically continued to the entire complex plane and satisfies |f(z)| = O(eπr|z|). In other words, it is an entire function of exponential type πr.

There is also a corresponding theorem about odd functions [38, Theorem 7], which can be proved in almost the same way. We’ll focus on even functions here for simplicity. Note also that the root spacing has changed from √2n to √n in comparison with Theorem 2.2, which reflects the change in the order of interpolation.

As a consequence of this interpolation theorem, if an even Schwartz function f : R → R satisfies f √n = f √n = 0 for n = 0, 1, 2, ..., then f vanishes identically. It’s not so surprising that constructing an explicit interpolation basis a0, a1, ... would require special functions, such as modular forms, but it’s noteworthy that even this corollary about vanishing does not seem easy to prove directly.

In the remainder of this section, we’ll sketch a proof of Theorem 3.1. The sketch will omit a number of analytic details, but it will outline the techniques and explain where additional work is required.

The central question is where the interpolation basis a0, a1, ... comes from. We need to characterize these functions and prove that they have the desired properties. A first observation is that the interpolation basis is not quite unique, because Poisson summation over Z implies that every even Schwartz function f satisfies

f(0) + 2f(1) + 2f(2) + ··· = f(0) + 2 f(1) + 2 f(2) + ··· .

In particular, f(0) is determined by the values f(0), f(1), f(2), ... and f(1), f(2), .... To account for this redundancy, we will impose the constraint a0 = a0, so that the interpolation formula becomes

f(x) = (f(0) + f(0))a0(x) +

∞

f √n an(x) +

n=1

∞

f √n an(x).

n=1

It turns out that this formula is now irredundant, with no additional linear relations between the values f √n and f √n , and the interpolation basis is uniquely determined. Substituting f = an shows that we can characterize an by its values

- at the points √m with m = 0, 1, 2, .... Specifically, for n,m ≥ 1, we must have


an √m =

1 if m = n, and 0 otherwise,

an √m = 0, and an(0) + an(0) = 0, while a0 must satisfy a0 = a0, a0(0) = 1/2, and a0 √m = 0 for all m ≥ 1.

These constraints let us get a handle on an, and we can use them to compute numerical approximations to an. More dramatically, they allow us to use Viazovska’s modular form techniques from [44] to construct an explicitly. For example, we can write down a0 as follows:

- Lemma 3.2. Let a0: R → C be defined by


1

1 4

2

θ(z)3eπizx

dz,

a0(x) =

−1

where we integrate over a semicircle in the upper half-plane H. Then a0 is an even Schwartz function with Fourier transform a0 = a0, and it satisfies a0(0) = 1/2 and a0 √m = 0 for all positive integers m.

−1 + i

1 + i

−1

0

1

Figure 3.1. When we deform the semicircle into this polygonal path, the vertical sides cancel because θ(z + 2) = θ(z).

We’ll use the same semicircular contour of integration in all integrals from −1 to 1 below. Recall that the theta function in this integral is defined for z ∈ H by

2z

eπin

θ(z) =

n∈Z

and satisfies the functional equations θ(z + 2) = θ(z) and θ(−1/z) = (−iz)1/2θ(z). Sketch of proof. The function a0 is manifestly even, and we can prove that it is a Schwartz function by analyzing the behavior of θ(z) as z tends to ±1. Specifically, if we remove small neighborhoods of ±1 from the contour, then we obtain a smooth function of x. One can show that this function and its derivatives are rapidly decreasing as x → ∞, essentially because the complex phases interfere destructively. To show that a0 itself is a Schwartz function, we just have to check that the behavior as z → ±1 is not bad enough to ruin this analysis. We will omit the details here.

To show that a0 = a0, we can take the Fourier transform of the complex Gaussian under the integral sign using (2.2) and change variables to u = −1/z, to obtain

1

1 4

2

θ(z)3(−iz)−1/2eπi(−1/z)x

dz

a0(x) =

−1

−1

1 4

2

θ(−1/u)3(i/u)−1/2eπiux

u−2 du

=

1

1

1 4

2

θ(u)3eπiux

du

=

−1

= a0(x), where the third line follows from θ(−1/u)3 = (−iu)3/2θ(u)3 and −(−iu)3/2(i/u)−1/2u−2 = 1

for u ∈ H. (To check this last identity, note that the left side is always ±1, it is continuous for u ∈ H, and it equals 1 when u = i.)

Finally, we can compute a0 √m for nonnegative integers m using the identity

1

a0 √m =

1 4

θ(z)3emπiz dz

−1

1+i

1 4

θ(z)3emπiz dz,

=

−1+i

where we have deformed the contour to a straight line from −1 + i to 1 + i as in Figure 3.1, which is possible because the integrals between 0 and −1 + i and

between 1 + i and 1 cancel due to θ(z + 2) = θ(z). Now we write

θ(z) = 1 + 2eπiz + 2e4πiz + 2e9πiz + ··· and expand θ(z)3 as a series in powers of eπiz. By Fourier orthogonality, the value

1+i

a0 √m =

1 4

θ(z)3emπiz dz

−1+i

is 1/2 times the coefficient of e−mπiz in this expansion of θ(z)3. In particular, a0(0) = 1/2 and a0 √m = 0 for positive integers m, as desired, since there are no negative powers of eπiz in this series. □

What made this proof work is that the identity θ(−1/z)3 = (−iz)3/2θ(z)3 gave us a0 = a0, while the identity θ(z + 2)3 = θ(z)3 let us compute the values a0 √m as Fourier series coefficients. One can obtain each basis function an using similar constructions, which require increasingly elaborate replacements for θ(z)3 as n grows, and it is not immediately clear how to describe or analyze them systematically. Furthermore, obtaining the basis functions individually does not explain why the interpolation formula actually holds: these functions could in principle exist yet not suffice to reconstruct an arbitrary even Schwartz function in Theorem 3.1.

To give a uniform account of these functions, we will construct generating functions for the interpolation basis. For τ ∈ H, let

∞

an(x)enπiτ, and denote its Fourier transform in x by

F(τ,x) =

n=0

∞

an(x)enπiτ.

F(τ,x) =

n=0

Being Fourier series, these functions satisfy the functional equations (3.1) F(τ + 2,x) = F(τ,x) and F(τ + 2,x) = F(τ,x). Furthermore, formula (2.2) for the Fourier transform of a complex Gaussian implies that the interpolation formula from Theorem 3.1 for the function f(x) = eπiτx

2

is equivalent to

2

F(τ,x) + (−iτ)−1/2 F(−1/τ,x) = eπiτx

, and thus F and F must satisfy this functional equation, in addition to those in

- (3.1). In fact, these three functional equations turn out to be almost all we need to


obtain a working interpolation basis. Lemma 3.3 is stated somewhat informally, but it can be made precise.

- Lemma 3.3. If there exists a function F such that F and F satisfy these three functional equations and certain analyticity and growth bounds, then Theorem 3.1 follows.


Sketch of proof. The idea behind the proof is surprisingly simple. If F and F are sufficiently well-behaved, then the functional equations F(τ + 2,x) = F(τ,x) and F(τ + 2,x) = F(τ,x) imply that they can be expanded as Fourier series. We can define the functions an to be the Fourier coefficients of F(τ,x), and an must be the corresponding coefficient of F(τ,x), as in the original definitions of F and F

above. The fact that there are no terms with n < 0 amounts to boundedness as Im(τ) → ∞, and the constraint that a0 = a0 can be phrased similarly (namely that F(τ,x) − F(τ,x) decays as Im(τ) → ∞).

Now the third functional equation says that

∞

∞

2

an(x)(−iτ)−1/2enπi(−1/τ) = eπiτx

an(x)enπiτ +

,

n=0

n=0

which becomes ∞

∞

an(x) f √n = f(x) if we set f(x) = eπiτx

an(x)f √n +

n=0

n=0

2

. In other words, it states that the interpolation theorem holds when f is a complex Gaussian.

One can show that complex Gaussians span a dense subspace of the even Schwartz functions. To complete the proof, all we need to show is that for each x ∈ R, the functional Λx that takes an even Schwartz function f to

∞

∞

f √n an(x) −

f √n an(x)

Λx(f) = f(x) −

n=0

n=0

is continuous, so that vanishing on a dense subspace implies vanishing everywhere. The topology on the space of Schwartz functions is defined by a family of seminorms, and proving that Λx is continuous requires proving that the seminorms of an and an grow at most polynomially as n → ∞. To prove the required bounds, we can use Fourier orthogonality to write an(x) and an(x) as integrals in τ of F(τ,x) and F(τ,x), respectively, and then use suitable growth bounds for F and F to bound the seminorms of these integrals. □

We can now imitate the construction of a0 from θ(z)3 in Lemma 3.2 to obtain the generating functions F and F explicitly. To do so, we will replace θ(z)3 with the functions K and K from Proposition 3.4, which is again stated informally. Note that K is not a Fourier transform of K; instead, this notation is simply mnemonic, since K will be used to construct F.

Proposition 3.4. There exist meromorphic functions K and K on H × H that satisfy the following conditions for all τ,z ∈ H:

- (1) K(τ + 2,z) = K(τ,z) and K(τ + 2,z) = K(τ,z),
- (2) K(τ,z + 2) = K(τ,z) and K(τ,z + 2) = K(τ,z),
- (3) K(−1/τ,z) = −(−iτ)1/2 K(τ,z),
- (4) K(τ,−1/z) = (−iz)3/2 K(τ,z),
- (5) z  → K(τ,z) and z  → K(τ,z) have poles only when z is in the Γθ-orbit of τ,
- (6) all their poles are simple poles,
- (7) the residue of z  → K(τ,z) at z = τ is 1/(2πi) and at z = −1/τ is 0 (in other words, there is no pole there),
- (8) the residue of z  → K(τ,z) at z = τ is 0, and
- (9) K and K satisfy certain growth bounds, which we will not discuss here.


The motivation behind the transformation laws in Proposition 3.4 is that they generalize how θ(z)3 transforms, and we’ll see that they perfectly describe what

we need to obtain F and F as integrals of K and K. At first glance the most mysterious aspect may be the poles, which did not occur for θ(z)3. We’ll see below that the poles lead to the inhomogeneous term eπiτx

2

### in the functional equation F(τ,x) + (−iτ)−1/2 F(−1/τ,x) = eπiτx

2

.

Before we examine how to use K and K to construct F and F, we will take a look at how Proposition 3.4 is proved.

Sketch of proof. The functions K and K can be described explicitly in terms of modular forms, using three ingredients: the theta function θ, the modular function λ, and a Hauptmodul (principal modular function) J for the group Γθ.

We have already been using θ, and λ is a similar analytic function on H that dates back to the 19th century. For our purposes, its key properties will be how Γθ acts on it, namely

λ(z + 2) = λ(z) and λ(−1/z) = 1 − λ(z).

Note that it is not quite invariant under Γθ. We define J(z) to be λ(z)(1−λ(z))/16, so that J(z) is invariant under both generators of Γθ; i.e.,

J(z + 2) = J(z) and J(−1/z) = J(z). Then it turns out that J generates the function field of the quotient of H by the action of Γθ (this quotient has genus 0), and J(z) = J(τ) if and only if z and τ are in the same orbit of Γθ.

Using these tools, we can guess much of what K(τ,z) and K(τ,z) should look like. Conditions (3) and (4) suggest that these functions should have factors of θ(τ)θ(z)3 to get the correct weights for the transformation laws. Conditions (4) and (5) imply that they should be given by 1/(J(z) − J(τ)) times something holomorphic, and the signs in (3) and (4) can be obtained using 1 − 2λ(−1/z) = −(1 − 2λ(z)).

In fact, we can take K(τ,z) = θ(τ)θ(z)3

J(z)(1 − 2λ(τ)) + J(τ)(1 − 2λ(z)) 4(J(z) − J(τ)) and

J(z)(1 − 2λ(τ)) − J(τ)(1 − 2λ(z)) 4(J(z) − J(τ))

K(τ,z) = θ(τ)θ(z)3

,

and fairly routine computations show that conditions (1) through (9) hold. The functions K and K turn out to be uniquely determined by these conditions, but we will not verify that here, to avoid having to state the conditions more carefully and deal with residues and growth bounds.

It’s worth noting that one can simplify some of the verification by writing K and K in terms of the function h := 1 − 2λ via

1 − h(τ)h(z) 4(h(τ) − h(z)) and

K(τ,z) = θ(τ)θ(z)3

1 + h(τ)h(z) 4(h(τ) + h(z))

K(τ,z) = θ(τ)θ(z)3

.

For example, h is a Hauptmodul for a subgroup of Γθ called Γ(2), and these formulas show that the poles of z  → K(τ,z) and z  → K(τ,z) occur only on the Γ(2)-orbits of τ and −1/τ, respectively. □

All that remains is to use K and K to construct functions F and F for use in Lemma 3.3. To do so, we can imitate Lemma 3.2. As a first attempt to produce F from K, we could try setting

1

2

K(τ,z)eπizx

- (3.2) F(τ,x) =


dz.

−1

However, this formula can’t possibly hold for all τ, because the integrand has poles on the Γθ-orbit of τ, and as one varies τ, sometimes these poles cross the contour of integration. Instead, we can use this definition only on subsets of H for which the poles avoid the contour of integration. As shown in Figure 2.3, one such subset consists of all the points τ ∈ H such that τ has distance strictly greater than 1 from 2Z. For such τ, we define F(τ,x) by (3.2); we will deal with other values of τ via analytic continuation in Lemma 3.5.

To obtain F(τ,x) we can take the Fourier transform of F(τ,x) in x. For τ strictly further than distance 1 from 2Z, we can use the semicircular contour, and almost exactly the same computation as in the proof of Lemma 3.2 shows that

1

2

K(τ,z)(−iz)−1/2eπi(−1/z)x

F(τ,x) =

dz

−1

1

2

K(τ,−1/z)(i/z)−1/2eπizx

z−2 dz

= −

−1

1

2

K(τ,z)(−iz)3/2(i/z)−1/2z−2eπizx

= −

dz

−1

1

2

K(τ,z)eπizx

=

dz.

−1

Lemma 3.5. The functions τ  → F(τ,x) and τ  → F(τ,x) can be analytically continued to all of H, and they satisfy the functional equations F(τ+2,x) = F(τ,x), F(τ + 2,x) = F(τ,x), and F(τ,x) + (−iτ)−1/2 F(−1/τ,x) = eπiτx

2

. Sketch of proof. Let S = {τ ∈ H : |τ − 2n| > 1 for all n ∈ Z}. We have defined F(τ,x) and F(τ,x) for τ ∈ S, and the functional equations

F(τ + 2,x) = F(τ,x) and F(τ + 2,x) = F(τ,x) for τ ∈ S are immediate consequences of

K(τ + 2,z) = K(τ,z) and K(τ + 2,z) = K(τ,z). To prove the lemma, it will suffice to analytically continue τ  → F(τ,x) and τ  → F(τ,x) to some open neighborhood of the closure of S in H, such that the continuations satisfy

2

F(τ,x) + (−iτ)−1/2 F(−1/τ,x) = eπiτx

whenever τ and −1/τ are both in this neighborhood. Then we can use the functional equations to extend these functions to all the hyperbolic triangles in Figure 2.3.4

We can now use the information about poles and residues in Proposition 3.4. When we analytically continue F(τ,x) to τ just below the semicircle from −1 to 1,

4Note that as we pass from a triangle to the adjacent triangles, we can never reach the same triangle via two different paths of adjacencies, and thus we don’t need to worry about inadvertently defining a multivalued function of τ.

the only relevant pole of z  → K(τ,z) is at z = τ, since −1/τ is the only other nearby point in the Γθ-orbit of τ, and there is no pole at that point. We can set

- (3.3) F(τ,x) = Cτ

K(τ,z)eπizx

2

dz,

where Cτ is a deformation of the semicircle to form a contour from −1 to 1 that passes below τ, so that τ never lies on the contour.

Similarly, we can analytically continue F(τ,x) to just below the semicircle via F(τ,x) =

Cτ′

K(τ,z)eπizx

2

dz,

where this time there is no pole at x = τ, and the condition is that the contour Cτ′ stays above the pole of z  → K(τ,z) at z = −1/τ.

Now we can prove the functional equation F(τ,x) + (−iτ)−1/2 F(−1/τ,x) = eπiτx

2

as follows when τ is just below the semicircle. The identity

K(−1/τ,z) = −(−iτ)1/2 K(τ,z), or equivalently

K(−1/τ,z) = −(−iτ)1/2K(τ,z), shows that

(−iτ)−1/2 F(−1/τ,x) =

C−′ 1/τ

(−iτ)−1/2 K(−1/τ,z)eπizx

2

dz

=

C−′ 1/τ

−(−iτ)−1/2(−iτ)1/2K(τ,z)eπizx

2

dz

= −

C−′ 1/τ

K(τ,z)eπizx

2

dz.

- (3.4)


Combining (3.3) and (3.4) with the residue theorem implies that F(τ,x) + (−iτ)−1/2 F(−1/τ,x) is 2πi times the sum of the residues of all the poles of z  → K(τ,z)eπizx

2

between

Cτ and C−′ 1/τ. The only pole that could lie between these contours is at z = τ, since z  → K(τ,z) has no pole at z = −1/τ, and by construction it does lie between

2

2

at z = τ is eπiτx

them. The residue of z  → K(τ,z)eπizx

### /(2πi), and so F(τ,x) + (−iτ)−1/2 F(−1/τ,x) = eπiτx

2

, as desired. □

Lemma 3.5 shows that F(τ,x) and F(τ,x) can be analytically continued to all τ ∈ H in such a way that they satisfy the three functional equations. That is almost everything we need to prove Theorem 3.1 using Lemma 3.3. However, to apply this lemma we need to verify certain growth conditions for F(τ,x) and F(τ,x) as τ approaches the real line. Verifying these conditions is the most technical part of the proof of the interpolation theorem, and we will not examine it here. In short, the verification combines bounds on K and K with careful accounting of how quickly the inhomogeneous terms from the third functional equation can accumulate during the analytic continuation. Once this is done, the proof of Theorem 3.1 is complete.

This proof is satisfyingly thorough in that it not only proves the interpolation formula but also provides plenty of additional information. For example, we can obtain explicit formulas for the interpolation basis a0, a1, ... by using the identity K(τ + 2,z) = K(τ,z) to write K as a Fourier series

∞

φn(z)enπiτ

K(τ,z) =

n=0

when Im(τ) is large. Then

1

2

φn(z)eπizx

an(x) =

dz,

−1

which generalizes Lemma 3.2. Similarly, the Fourier coefficients of K yield formulas for an.

On the other hand, some aspects of the proof are quite delicate. For example, it is very sensitive to the form √n of the interpolation points. Specifically, the proof of the functional equation

2

F(τ,x) + (−iτ)−1/2 F(−1/τ,x) = eπiτx

2

depends on the fact that the complex Gaussian x  → eπiτx

equals enπiτ when evaluated at the interpolation point x = √n. If we replaced √n with other interpolation points rn, then the Fourier series for F(τ,x) would have to be replaced with

∞

2

an(x)er

nπiτ,

n=0

and it would no longer satisfy F(τ +2,x) = F(τ,x) if the values rn2 are not integers. That would disrupt the algebraic mechanism behind the proof.

Much remains to be understood regarding generalizations of the Radchenko– Viazovska theorem and how Fourier interpolation fits into a broader picture. One significant line of work [3,4] connects Fourier interpolation to uniqueness theory for the Klein–Gordon equation [26–28]. Other noteworthy papers examine the density of possible interpolation points [1, 30, 31, 39] and whether they can be perturbed [35], interpolation formulas using zeros of zeta and L-functions [6], and extensions to nonradial functions [1,36,37,40]. Perhaps the most surprising development so far has been a paper on sphere packing and quantum gravity [25], which shows the equivalence of linear programming bounds with the spinless modular bootstrap bound for free bosons in conformal field theory, and which furthermore shows that certain bases of special functions constructed by Maz´ˇc and Paulos [34] for the conformal bootstrap can be transformed into Fourier interpolation bases.

Acknowledgments

I am grateful to Rupert Li and Danylo Radchenko for helpful feedback on a draft of this article.

About the author

Henry Cohn is a senior principal researcher at Microsoft Research New England and an adjunct professor of mathematics at MIT. His primary research interests are in discrete mathematics, with connections to computer science and physics.

### References

- [1] Anshul Adve, Density criteria for Fourier uniqueness phenomena in Rd, Preprint, arXiv:2306.07475, 2023.
- [2] Nima Afkhami-Jeddi, Henry Cohn, Thomas Hartman, David de Laat, and Amirhossein Tajdini, High-dimensional sphere packing and the modular bootstrap, J. High Energy Phys. 12

- (2020), Paper No. 066, 44, DOI 10.1007/jhep12(2020)066. MR4239386

[3] Andrew Bakan, Haakan Hedenmalm, Alfonso Montes-Rodrı´guez, Danylo Radchenko, and Maryna Viazovska, Fourier uniqueness in even dimensions, Proc. Natl. Acad. Sci. USA 118

- (2021), no. 15, Paper No. 2023227118, 4, DOI 10.1073/pnas.2023227118. MR4294062


- [4] Andrew Bakan, Haakan Hedenmalm, Alfonso Montes-Rodrı´guez, Danylo Radchenko, and Maryna Viazovska, Hyperbolic Fourier series, Preprint, arXiv:2110.00148, 2021.
- [5] M. R. Best, Binary codes with a minimum distance of four, IEEE Trans. Inform. Theory 26

(1980), no. 6, 738–742, DOI 10.1109/TIT.1980.1056269. MR596287

- [6] Andriy Bondarenko, Danylo Radchenko, and Kristian Seip, Fourier interpolation with zeros of zeta and L-functions, Constr. Approx. 57 (2023), no. 2, 405–461, DOI 10.1007/s00365022-09599-w. MR4577389
- [7] S. V. Borodachov, D. P. Hardin, and E. B. Saff, Asymptotics of best-packing on rectifiable sets, Proc. Amer. Math. Soc. 135 (2007), no. 8, 2369–2380, DOI 10.1090/S0002-9939-07-08975-7. MR2302558
- [8] Jean Bourgain, Laurent Clozel, and Jean-Pierre Kahane, Principe d’Heisenberg et fonctions positives (French, with English and French summaries), Ann. Inst. Fourier (Grenoble) 60

(2010), no. 4, 1215–1232, DOI 10.5802/aif.2552. MR2722239

- [9] Henry Cohn, A conceptual breakthrough in sphere packing, Notices Amer. Math. Soc. 64

(2017), no. 2, 102–115, DOI 10.1090/noti1474. MR3587715

- [10] Henry Cohn, The work of Maryna Viazovska, Fields medal laudatio, 2022. arXiv:2207.06913, DOI 10.4171/ICM2022/213.
- [11] Henry Cohn and Noam Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157 (2003), no. 2, 689–714, DOI 10.4007/annals.2003.157.689. MR1973059
- [12] Henry Cohn and Felipe Gonc¸alves, An optimal uncertainty principle in twelve dimensions via modular forms, Invent. Math. 217 (2019), no. 3, 799–831, DOI 10.1007/s00222-019-00875-4. MR3989254
- [13] Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska, The sphere packing problem in dimension 24, Ann. of Math. (2) 185 (2017), no. 3, 1017–1033, DOI 10.4007/annals.2017.185.3.8. MR3664817
- [14] Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska,

Universal optimality of the E8 and Leech lattices and interpolation formulas, Ann. of Math.

(2) 196 (2022), no. 3, 983–1082, DOI 10.4007/annals.2022.196.3.3. MR4502595

- [15] Henry Cohn, David de Laat, and Andrew Salmon, Three-point bounds for sphere packing, Preprint, arXiv:2206.15373, 2022.
- [16] J. H. Conway and N. J. A. Sloane, What are all the best sphere packings in low dimensions?, Discrete Comput. Geom. 13 (1995), no. 3-4, 383–403, DOI 10.1007/BF02574051. MR1318784
- [17] J. H. Conway and N. J. A. Sloane, Sphere packings, lattices and groups, 3rd ed., Grundlehren der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 290, Springer-Verlag, New York, 1999. With additional contributions by E. Bannai, R. E. Borcherds, J. Leech, S. P. Norton, A. M. Odlyzko, R. A. Parker, L. Queen and B. B. Venkov, DOI 10.1007/978-1-4757-6568-7. MR1662447
- [18] Matthew de Courcy-Ireland, Maria Dostert, and Maryna Viazovska, Six-dimensional sphere packing and linear programming, Preprint, arXiv:2211.09044, 2022.
- [19] P. Delsarte, Bounds for unrestricted codes, by linear programming, Philips Res. Rep. 27

(1972), 272–289. MR314545

- [20] Wolfgang Ebeling, Lattices and codes, 3rd ed., Advanced Lectures in Mathematics, Springer Spektrum, Wiesbaden, 2013. A course partially based on lectures by Friedrich Hirzebruch, DOI 10.1007/978-3-658-00360-9. MR2977354
- [21] L. Fejes, Uber¨ einen geometrischen Satz (German), Math. Z. 46 (1940), 83–85, DOI 10.1007/BF01181430. MR1587


- [22] Felipe Gon¸calves, Diogo Oliveira e Silva, and Stefan Steinerberger, Hermite polynomials, linear flows on the torus, and an uncertainty principle for roots, J. Math. Anal. Appl. 451

(2017), no. 2, 678–711, DOI 10.1016/j.jmaa.2017.02.030. MR3624763

- [23] Thomas C. Hales, A proof of the Kepler conjecture, Ann. of Math. (2) 162 (2005), no. 3, 1065–1185, DOI 10.4007/annals.2005.162.1065. MR2179728
- [24] Thomas Hales, Mark Adams, Gertrud Bauer, Tat Dat Dang, John Harrison, Le Truong Hoang, Cezary Kaliszyk, Victor Magron, Sean McLaughlin, Tat Thang Nguyen, Quang Truong Nguyen, Tobias Nipkow, Steven Obua, Joseph Pleso, Jason Rute, Alexey Solovyev, Thi Hoai An Ta, Nam Trung Tran, Thi Diep Trieu, Josef Urban, Ky Vu, and Roland Zumkeller, A formal proof of the Kepler conjecture, Forum Math. Pi 5 (2017), e2, 29, DOI 10.1017/fmp.2017.1. MR3659768
- [25] Thomas Hartman, Dalimil Maz´acˇ, and Leonardo Rastelli, Sphere packing and quantum gravity, J. High Energy Phys. 12 (2019), 048, 66, DOI 10.1007/jhep12(2019)048. MR4075697
- [26] Haakan Hedenmalm and Alfonso Montes-Rodr´ıguez, Heisenberg uniqueness pairs and the Klein-Gordon equation, Ann. of Math. (2) 173 (2011), no. 3, 1507–1527, DOI 10.4007/annals.2011.173.3.6. MR2800719
- [27] Haakan Hedenmalm and Alfonso Montes-Rodr´ıguez, The Klein-Gordon equation, the Hilbert transform, and dynamics of Gauss-type maps, J. Eur. Math. Soc. (JEMS) 22 (2020), no. 6, 1703–1757, DOI 10.4171/jems/954. MR4092897
- [28] Haakan Hedenmalm and Alfonso Montes-Rodr´ıguez, The Klein-Gordon equation, the Hilbert transform and Gauss-type maps: H∞ approximation, J. Anal. Math. 144 (2021), no. 1, 119– 190, DOI 10.1007/s11854-021-0173-4. MR4361892
- [29] J. R. Higgins, Five short stories about the cardinal series, Bull. Amer. Math. Soc. (N.S.) 12

(1985), no. 1, 45–89, DOI 10.1090/S0273-0979-1985-15293-0. MR766960

- [30] Aleksei Kulikov, Fourier interpolation and time-frequency localization, J. Fourier Anal. Appl. 27 (2021), no. 3, Paper No. 58, 8, DOI 10.1007/s00041-021-09861-y. MR4273648
- [31] Aleksei Kulikov, Fedor Nazarov, and Mikhail Sodin, Fourier uniqueness and non-uniqueness pairs, Preprint, arXiv:2306.14013, 2023.
- [32] David de Laat and Frank Vallentin, A breakthrough in sphere packing: the search for magic functions, Nieuw Arch. Wiskd. (5) 17 (2016), no. 3, 184–192. Includes an interview with Henry Cohn, Abhinav Kumar, Stephen D. Miller and Maryna Viazovska. MR3643686
- [33] Rupert Li, Dual linear programming bounds for sphere packing via discrete reductions, Preprint, arXiv:2206.09876, 2022.
- [34] Dalimil Maz´acˇ and Miguel F. Paulos, The analytic functional bootstrap. Part II. Natural bases for the crossing equation, J. High Energy Phys. 2 (2019), 163, DOI 10.1007/jhep02(2019)163. MR3925259
- [35] Jo˜ao P. G. Ramos and Mateus Sousa, Perturbed interpolation formulae and applications, Preprint, arXiv:2005.10337, 2020.
- [36] Jo˜ao P. G. Ramos and Martin Stoller, Perturbed Fourier uniqueness and interpolation results in higher dimensions, J. Funct. Anal. 282 (2022), no. 12, Paper No. 109448, 34, DOI 10.1016/j.jfa.2022.109448. MR4403065
- [37] Danylo Radchenko and Martin Stoller, Fourier non-uniqueness sets from totally real number fields, Comment. Math. Helv. 97 (2022), no. 3, 513–553, DOI 10.4171/cmh/538. MR4468993
- [38] Danylo Radchenko and Maryna Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129 (2019), 51–81, DOI 10.1007/s10240-018-0101-z. MR3949027
- [39] Naser Talebizadeh Sardari, Higher Fourier interpolation on the plane, Preprint, arXiv:2102.08753, 2021.
- [40] Martin Stoller, Fourier interpolation from spheres, Trans. Amer. Math. Soc. 374 (2021), no. 11, 8045–8079, DOI 10.1090/tran/8440. MR4328691
- [41] Thomas M. Thompson, From error-correcting codes through sphere packings to simple groups, Carus Mathematical Monographs, vol. 21, Mathematical Association of America, Washington, DC, 1983. MR0749038
- [42] A. Thue, Om nogle geometrisk-taltheoretiske Theoremer, Forhandlingerne ved de Skandinaviske Naturforskeres 14 (1892), 352–353.
- [43] Axel Thue, Uber¨ die dichteste Zusammenstellung von kongruenten Kreisen in der Ebene, Skrifter udgivne af Videnskabs-Selskabet i Christiania. I. Mathematisk-Naturvidenskabelig Klasse 1 (1910), 1–9.


- [44] Maryna S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. (2) 185

(2017), no. 3, 991–1015, DOI 10.4007/annals.2017.185.3.7. MR3664816

- [45] Maryna Viazovska, Sharp sphere packings, Proceedings of the International Congress of Mathematicians—Rio de Janeiro 2018. Vol. II. Invited lectures, World Sci. Publ., Hackensack, NJ, 2018, pp. 455–466, DOI 10.1142/9789813272880 0063. MR3966775

- [46] Maryna Viazovska, Almost impossible E8 and Leech lattices, Eur. Math. Soc. Mag. 121


(2021), 4–8, DOI 10.4171/mag-47. MR4400365

Microsoft Research New England, One Memorial Drive, Cambridge, Massachusetts 02142

Email address: cohn@microsoft.com

