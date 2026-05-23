# arXiv:1611.01685v1[math.MG]5Nov2016

## A CONCEPTUAL BREAKTHROUGH IN SPHERE PACKING

HENRY COHN

On March 14, 2016, the world of mathematics received an extraordinary Pi Day surprise when Maryna Viazovska posted to the arXiv a solution of the sphere packing problem in eight dimensions [15]. Her proof shows that the E8 root lattice is the densest sphere packing in eight dimensions, via a beautiful and conceptually simple argument. Sphere packing is notorious for complicated proofs of intuitively obvious facts, as well as hopelessly diﬃcult unsolved problems, so it’s wonderful to see a relatively simple proof of a deep theorem in sphere packing. No proof of optimality had been known for any dimension above three, and Viazovska’s paper does not even address four through seven dimensions. Instead, it relies on remarkable properties of the E8 lattice. Her proof is thus a notable contribution to the story of E8, and more generally the story of exceptional structures in mathematics.

One measure of the complexity of a proof is how long it takes the community to digest it. By this standard, Viazovska’s proof is remarkably simple. It was understood by a number of people within a few days of her arXiv posting, and within a week it led to further progress: Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and I worked with Viazovska to adapt her methods to prove that the Leech lattice is an optimal sphere packing in twenty-four dimensions [4]. This is the only other case above three dimensions in which the sphere packing problem has been solved.

The new ingredient in Viazovska’s proof is a certain special function, which enforces the optimality of E8 via the Poisson summation formula. The existence of such a function had been conjectured by Cohn and Elkies in 2003, but what sort of function it might be remained mysterious despite considerable eﬀort. Viazovska constructs this function explicitly in terms of modular forms by using an unexpected integral transform, which establishes a new connection between modular forms and discrete geometry.

A landmark achievement like Viazovska’s deserves to be appreciated by a broad audience of mathematicians, and indeed it can be. In this article we’ll take a look at how her proof works, as well as the background and context. We won’t cover all the details completely, but we’ll see the main ideas and how they ﬁt together. Readers who wish to read a complete proof will then be well prepared to study Viazovska’s paper [15] and the follow-up work on the Leech lattice [4]. See also de Laat and Vallentin’s survey article and interview [13] for a somewhat diﬀerent perspective, as well as [1] and [7] for further background and references.

Henry Cohn is principal researcher at Microsoft Research New England and adjunct professor of mathematics at the Massachusetts Institute of Technology. His email address is cohn@microsoft.com.

1

![image 1](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile1.png>)

- Figure 1. Maryna Viazovska solved the sphere packing problem in eight dimensions.

![image 2](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile2.png>)

![image 3](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile3.png>)

![image 4](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile4.png>)

![image 5](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile5.png>)

- Figure 2. Henry Cohn, Abhinav Kumar, Stephen D. Miller, and Danylo Radchenko collaborated with Maryna Viazovska to extend her methods to twenty-four dimensions.


1. Sphere packing

The sphere packing problem asks for the densest packing of Rn with congruent balls. In other words, what is the largest fraction of Rn that can be covered by congruent balls with disjoint interiors?

Pathological packings may not have well-deﬁned densities, but we can handle the technicalities as follows. A sphere packing P is a nonempty subset of Rn consisting of congruent balls with disjoint interiors. The upper density of P is

vol Brn(0) ∩ P vol Brn(0)

limsup

,

r→∞

where Brn(x) denotes the closed ball of radius r about x, and the sphere packing density ∆Rn in Rn is the supremum of all the upper densities of sphere packings. In other words, we avoid technicalities by using a generous deﬁnition of the packing density. This generosity does not cause any harm, as shown by the theorem of

Groemer that there exists a sphere packing P for which

vol Brn(x) ∩ P vol Brn(x)

lim

= ∆Rn

r→∞

uniformly for all x ∈ Rn. Thus, the supremum of the upper densities is in fact achieved as the density of some packing, in the nicest possible way. Of course the densest packing is not unique, since there are any number of ways to perturb a packing without changing its overall density.

Why should we care about the sphere packing problem? Two obvious reasons are that it’s a natural geometric problem in its own right and a toy model for granular materials. A more surprising application is that sphere packings are error-correcting codes for a continuous communication channel. Real-world communication channels can be modeled using high-dimensional vector spaces, and thus high-dimensional sphere packings have practical importance.

Instead of justifying sphere packing by aspects of the problem or its applications, we’ll justify it by its solutions: a question is good if it has good answers. Sphere packing turns out to be a far richer and more beautiful topic than the bare problem statement suggests. From this perspective, the point of the subject is the remarkable structures that arise as dense sphere packings.

To begin, let’s examine the familiar cases of one, two, and three dimensions. The one-dimensional sphere packing problem is the interval packing problem on the line, which is of course trivial: the optimal density is 1. The two- and threedimensional problems are far from trivial, but the optimal packings, shown in Figure 3, are exactly what one would expect. In particular, the sphere packing density is π/√12 = 0.9068... in R2 and π/√18 = 0.7404... in R3. The twodimensional problem was solved by Thue. Giving a rigorous proof requires a genuine idea, but there exist short, elementary proofs [8]. The three-dimensional problem was solved by Hales [9] via a lengthy and complex computer-assisted proof, which was extraordinarily diﬃcult to check but has since been completely veriﬁed using formal logic [10].

In both two and three dimensions, one can obtain an optimal packing by stacking layers that are packed optimally in the previous dimension, with the layers nestled together as closely as possible. Guessing this answer is not diﬃcult, nor is computing the density of such a packing. Instead, the diﬃculty lies in proving that no other construction could achieve a greater density.

Unfortunately, our low-dimensional experience is poor preparation for understanding high-dimensional sphere packing. Based on the ﬁrst three dimensions, it appears that guessing the optimal packing is easy, but this expectation turns out to be completely false in high dimensions. In particular, stacking optimal layers from the previous dimension does not always yield an optimal packing. (One can recursively determine the best packings in successive dimensions under such a hypothesis [6], and this procedure yields a suboptimal packing by the time it reaches R10.)

The sphere packing problem seems to have no simple, systematic solution that works across all dimensions. Instead, each dimension has its own idiosyncracies and charm. Understanding the densest sphere packing in R8 tells us only a little about R7 or R9, and hardly anything about R10.

Aside from R8 and R24, our ignorance grows as the dimension increases. In high dimensions, we have absolutely no idea how the densest sphere packings behave. We

![image 6](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile6.png>)

![image 7](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile7.png>)

Figure 3. Fragments of optimal sphere packings in two and three dimensions, with density π/√12 = 0.9068... in R2 and π/√18 = 0.7404... in R3.

do not know even the most basic facts, such as whether the densest packings should be crystalline or disordered. Here “do not know” does not merely mean “cannot prove,” but rather the much stronger “cannot predict.”

A simple greedy argument shows that the optimal density in Rn is at least 2−n. To see why, consider any sphere packing in which there is no room to add even one more sphere. If we double the radius of each sphere, then the enlarged spheres must cover space completely, because any uncovered point could serve as the center of a new sphere that would ﬁt in the original packing. Doubling the radius multiplies volume by 2n, and so the original packing must cover at least a 2−n fraction of Rn.

That may sound appallingly low, but it is very nearly the best lower bound known. Even the most recent bounds, obtained by Venkatesh [14] in 2013, have been unable to improve on 2−n by more than a linear factor in general and an nlog log n factor in special cases. As for upper bounds, in 1978 Kabatyanskii and Levenshtein [11] proved an upper bound of 2(−0.599...+o(1))n, which remains essentially the best upper bound known in high dimensions. Thus, we know that the sphere packing density decreases exponentially as a function of dimension, but the best upper and lower bounds known are exponentially far apart.

Table 1 lists the best packing densities currently known in up to 36 dimensions, and Figure 4 shows a logarithmic plot. The plot has several noteworthy features:

- (1) The curve is jagged and irregular, with no obvious way to interpolate data points from their neighbors.
- (2) The density is clearly decreasing exponentially, but the irregularity makes it unclear how to extrapolate to estimate the decay rate as the dimension tends to inﬁnity.
- (3) There seem to be parity eﬀects. Even dimensions look slightly better than odd dimensions, multiples of four are better yet, and multiples of eight are the best of all.
- (4) Certain dimensions, most notably 24, have packings so good that they seem to pull the entire curve in their direction. The fact that this occurs is not so surprising, since one expects cross sections and stackings of great packings to be at least good, but the eﬀect is surprisingly large.


dimension

1 0

4 8 12 16 20 24 28 32 36

log(density)

best packing known

−14

- Figure 4. The sphere packing density is jagged and irregular, with no obvious way to interpolate data points from their neighbors.


Table 1. The record sphere packing densities in Rn with 1 ≤ n ≤ 36, from Table I.1 of [7, pp. xix–xx]. All numbers are rounded down.

n density n density n density

- 1 1.000000000 13 0.0320142921 25 0.00067721200977
- 2 0.906899682 14 0.0216240960 26 0.00026922005043
- 3 0.740480489 15 0.0168575706 27 0.00015759439072
- 4 0.616850275 16 0.0147081643 28 0.00010463810492
- 5 0.465257613 17 0.0088113191 29 0.00003414464690
- 6 0.372947545 18 0.0061678981 30 0.00002191535344
- 7 0.295297873 19 0.0041208062 31 0.00001183776518
- 8 0.253669507 20 0.0033945814 32 0.00001104074930
- 9 0.145774875 21 0.0024658847 33 0.00000414068828
- 10 0.099615782 22 0.0024510340 34 0.00000176697388
- 11 0.066238027 23 0.0019053281 35 0.00000094619041
- 12 0.049454176 24 0.0019295743 36 0.00000061614660


- Figure 5. The spheres in a lattice packing form a single orbit under translation (left), while those in a periodic packing can form several orbits (right). The small parallelograms are fundamental cells.


2. Lattices and periodic packings

How can we describe sphere packings? Random or pathological packings can be inﬁnitely complicated, but the most important packings can generally be given a ﬁnite description via periodicity.

Recall that a lattice in Rn is a discrete subgroup of rank n. In other words, it consists of the integral span of a basis of Rn. Equivalently, a lattice is the image of Zn under an invertible linear operator.

A sphere packing P is periodic if there exists a lattice Λ such that P is invariant under translation by every element of Λ. In that case, the translational symmetry group of P must be a lattice, since it is clearly a discrete group, and P consists of ﬁnitely many orbits of this group. A lattice packing is a periodic packing in which the spheres form a single orbit under the translational symmetry group (i.e., their centers form a lattice, up to translation). See Figure 5 for an illustration.

It is not known whether periodic packings attain the optimal sphere packing density in each dimension, aside from the ﬁve cases in which the sphere packing problem has been solved. They certainly come arbitrarily close to the optimal density: given an optimal packing, one can approximate it by taking the spheres contained in a large box and repeating them periodically throughout space, and the density loss is negligible if the box is large enough. However, there seems to be no reason why periodic packings should reach the exact optimum, and perhaps they don’t in high dimensions.

By contrast, lattices probably do not even come arbitrarily close to the optimal packing density in high dimensions. For example, the best periodic packing known in R10 is more than 8% denser than the best lattice packing known. Seen in this light, the optimality of lattices in R8 and R24 is not a foregone conclusion, but rather an indication that sphere packing in these dimensions is particularly simple.

To compute the density of a lattice packing, it’s convenient to view the lattice as a tiling of space with parallelotopes (the n-dimensional analogue of parallelograms). Given a basis v1,...,vn for a lattice Λ, the parallelotope

{x1v1 + ··· + xnvn : 0 ≤ xi < 1 for i = 1,2,...,n}

is called the fundamental cell of Λ with respect to this basis. Translating the fundamental cell by elements of Λ tiles Rn, as in Figure 5. From this perspective, a lattice sphere packing amounts to placing spheres at the vertices of such a tiling. On a global scale, there is one sphere for each copy of the fundamental cell. Thus, if the packing uses spheres of radius r and has fundamental cell C, then its density is the ratio

vol Brn vol(C)

.

Both factors in this ratio are easily computed if we are given r and C. The volume of a fundamental cell is just the absolute value of the determinant of the corresponding lattice basis; we will write it as vol(Rn/Λ), the volume of the quotient torus, to avoid having to specify a basis. Computing the volume of a ball of radius r in Rn is a multivariate calculus exercise, whose answer is

πn/2 (n/2)!

rn,

vol Brn =

where of course (n/2)! means Γ(n/2 + 1) when n is odd. We can therefore compute the density of any lattice packing explicitly. The density of a periodic packing is equally easy to compute: if the packing consists of N translates of a lattice Λ in Rn and uses spheres of radius r, then its density is

N vol Brn vol(Rn/Λ)

.

Of course the density of a packing depends on the radius of the spheres. Given a lattice with no radius speciﬁed, it is standard to use the largest radius that does not lead to overlap. The minimal vector length of a lattice Λ is the length of the shortest nonzero vector in Λ, or equivalently the shortest distance between two distinct points in Λ. If the minimal vector length is r, then r/2 is the largest radius that yields a packing, since that is the radius at which neighboring spheres become tangent.

3. The E8 and Leech lattices

Many dimensions feature noteworthy sphere packings, but the E8 root lattice in R8 and the Leech lattice in R24 are perhaps the most remarkable of all, with connections to exceptional structures across mathematics. In this section, we’ll construct E8 and prove some of its basic properties. It was discovered by Korkine and Zolotareﬀ in 1873, in the guise of a quadratic form they called W8. We’ll give a construction much like Korkine and Zolotareﬀ’s but more modern. The Leech lattice Λ24, discovered by Leech in 1967, is similar in spirit, but more complicated. In lieu of constructing it, we will brieﬂy summarize its properties.

To specify E8, we just need to describe a lattice basis v1,...,v8 in R8. Furthermore, only the relative positions of the basis vectors matter, so all we need to specify is their inner products with each other. All this information will be encoded by the Dynkin diagram

### of E8. In this diagram, the eight nodes correspond to the basis vectors, each of squared length 2. The inner product between distinct vectors is −1 if the nodes are joined by an edge, and 0 otherwise. Thus, if we number the nodes

4

1 2 3

5 6 7 8

then the Gram matrix of inner products for this basis is given by 



2 −1 0 0 0 0 0 0

−1 2 −1 0 0 0 0 0 0 −1 2 −1 −1 0 0 0 0 0 −1 2 0 0 0 0 0 0 −1 0 2 −1 0 0 0 0 0 0 −1 2 −1 0 0 0 0 0 0 −1 2 −1 0 0 0 0 0 0 −1 2

.

- (3.1) vi,vj 1≤i,j≤8 =


 

 

Before we go further, we must address a fundamental question: how do we know there really are vectors v1,...,v8 with these inner products? All we need is for the matrix in (3.1) to be symmetric and positive deﬁnite, and indeed it is, although it’s not obviously positive deﬁnite. That can be checked in several ways. We’ll take the pedestrian approach of observing that the characteristic polynomial of this matrix is

t8 − 16t7 + 105t6 − 364t5 + 714t4 − 784t3 + 440t2 − 96t + 1, which clearly has no roots when t < 0 because every term is then positive.

We can now deﬁne the E8 root lattice to be the integral span of v1,...,v8. We will use this deﬁnition to derive several fundamental properties of E8. These properties will let us determine its packing density, and they will also be essential for Viazovska’s proof.

The E8 lattice is an integral lattice, which means all the inner products between vectors in E8 are integers. This follows immediately from the integrality of the inner products of the basis vectors v1,...,v8. Even more importantly, E8 is an even lattice, which means the squared length of every vector is an even integer. Speciﬁcally, for m1,...,m8 ∈ Z the vector m1v1 + ··· + m8v8 has squared length

|m1v1 + ··· + m8v8|2 = 2m21 + ··· + 2m28 +

2mimj vi,vj ,

1≤i<j≤8

which is visibly even. Thus, the distances between distinct points in E8 are all of the form

√

2k with k = 1,2,..., and in fact each of those distances does occur.

In particular, the distance between neighboring points in E8 is √2, so we can form a packing with spheres of radius √2/2 and density

vol B√8 2/2 vol(R8/E8)

π4 384vol(R8/E8)

=

.

To compute the density of the E8 packing, all we need to compute is vol(R8/E8).

To compute this volume, recall that it’s the absolute value of the determinant of the basis matrix:





←− v1 −→ ←− v2 −→

vol(R8/E8) = det

.

 

 

. ←− v8 −→

However, we can write the Gram matrix vi,vj 1≤i,j≤8 as the product 



  

  

←− v1 −→ ←− v2 −→

v 1 v 2 ··· v 8   

 

 

. ←− v8 −→

of the basis matrix with its transpose, and thus det vi,vj 1≤i,j≤8 = vol(R8/E8)2.

Computing the determinant of the matrix in (3.1) then shows that vol(R8/E8) = 1. In other words, E8 is a unimodular lattice.

Putting together our calculations, we have proved the following proposition: Proposition 3.1. The E8 lattice packing in R8 has density π4/384 = 0.2536....

Our calculations so far have led us to what turns out to be the densest sphere packing in R8, but it’s not obvious from this construction that E8 is an especially interesting lattice. The E8 lattice is in fact magniﬁcently symmetrical, far more so than one might naively guess based on its lopsided Dynkin diagram. Its symmetry group is the E8 Weyl group, which is generated by reﬂections in the hyperplanes orthogonal to each of v1,...,v8. We will not make use of this group, but it’s important to keep in mind that the lattice itself is far more symmetrical than its deﬁnition. This is a common pattern when deﬁning highly symmetrical objects.

Our density calculation for E8 was based on its being an even unimodular lattice. In fact, E8 is the unique even unimodular lattice in R8, up to orthogonal transformations. Even unimodular lattices exist only when the dimension is a multiple of eight, and they play a surprisingly large role in the theory of sphere packing.

The last property of E8 we will need for Viazovska’s proof is that it is its own dual lattice, a concept we will deﬁne shortly. Given a lattice Λ with basis v1,...,vn, let v1∗,...,vn∗ be the dual basis with respect to the usual inner product. In other words,

1 if i = j, and 0 otherwise.

vi,vj∗ =

Then the dual lattice Λ∗ of Λ is the lattice with basis v1∗,...,vn∗. It is not diﬃcult to check that Λ∗ is independent of the choice of basis for Λ; one basis-free way to characterize it is that

- (3.2) Λ∗ = {y ∈ Rn : x,y ∈ Z for all x ∈ Λ}.


The self-duality E8∗ = E8 is a consequence of the following lemma: Lemma 3.2. Every integral unimodular lattice Λ satisﬁes Λ∗ = Λ.

![image 8](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile8.png>)

Figure 6. Stephen D. Miller explains dual lattices and transference theorems to his graduate class on the geometry of numbers.

Proof. Let v1,...,vn be a basis of Λ, and v1∗,...,vn∗ the dual basis of Λ∗. By construction, the basis matrix formed by v1∗,...,vn∗ is the inverse of the transpose of that formed by v1,...,vn, and hence vol(Rn/Λ∗) = 1/vol(Rn/Λ). If Λ is an integral lattice, then Λ ⊆ Λ∗, and the index of Λ in Λ∗ is given by

[Λ∗ : Λ] = vol(Rn/Λ)/vol(Rn/Λ∗) = vol(Rn/Λ)2. If Λ is unimodular as well, then [Λ∗ : Λ] = 1 and hence Λ∗ = Λ.

As mentioned above, the Leech lattice Λ24 is similar to E8 but more elaborate. It’s an even unimodular lattice in R24, but this time with no vectors of length √2, and it’s the unique lattice with these properties, up to orthogonal transformations. The nonzero vectors in Λ24 have lengths

√

2k for k = 2,3,..., and of course Λ∗24 = Λ24 because Λ24 is integral and unimodular. One noteworthy property of Λ24 is that it’s chiral: all of its symmetries are orientation-preserving, and the Leech lattice therefore occurs in left-handed and right-handed variants, which are mirror images of each other. (By contrast, the symmetry group of E8 is generated by reﬂections, so E8 is certainly not chiral.)

The sphere packing density of the Leech lattice is vol B124 vol(R24/Λ24)

π12 12!

=

= 0.001929...,

which looks awfully low, but keep in mind that the optimal density decreases exponentially as a function of dimension. In fact, the density of the Leech lattice is remarkably high, as one can see from Figure 4 and Table 1. For comparison, the best density known in R23 is 0.001905..., which is lower than the density of the Leech lattice, and this is the only case in which the density increases from one dimension to the next in Table 1.

![image 9](<2016-cohn-conceptual-breakthrough-sphere-packing_images/imageFile9.png>)

Figure 7. Noam Elkies developed the linear programming bounds for sphere packing with Henry Cohn.

4. Linear programming bounds

The underlying technique used in Viazovska’s proof is linear programming bounds for the sphere packing density in Rn. These upper bounds were developed by Cohn and Elkies [2], based on several decades of previous work initiated by Delsarte and extended by numerous mathematicians. In this approach to sphere packing, one uses auxiliary functions with certain properties to obtain density bounds. Viazovska’s breakthrough consists of a new technique for constructing these auxiliary functions, but before we turn to her proof let’s examine the general theory and review how the bounds work. We will see that the general bounds do not refer to special dimensions such as eight and twenty-four, which makes it all the more remarkable that they can be used to solve the sphere packing problem in these dimensions.

Linear programming bounds are based on harmonic analysis. That may sound surprising, since sphere packing is a problem in discrete geometry, which at ﬁrst glance seems to have little to do with the continuous problems studied in harmonic analysis. However, there is a deep connection between these ﬁelds, because the Fourier transform is essential for understanding the action of the additive group Rn on itself by translation, so much so that one can’t truly understand lattices without harmonic analysis.

Deﬁne the Fourier transform f of an integrable function f : Rn → R by

f(y) =

f(x)e−2πi x,y dx.

Rn

Fourier inversion tells us that if f is integrable as well, then one can similarly recover f from f:

f(y)e2πi x,y dy

- (4.1) f(x) = Rn


almost everywhere. In other words, the Fourier transform gives the unique coeﬃcients needed to express f in terms of complex exponentials.

To avoid analytic technicalities, we will focus on Schwartz functions. Recall that f : Rn → R is a Schwartz function if f is inﬁnitely diﬀerentiable, f(x) = O (1 + |x|)−k for all k = 1,2,..., and the same holds for all the partial derivatives of f (of every order). Schwartz functions behave particularly well, well enough to justify everything we’d like to do with them, and they are closed under the Fourier transform. We could get by with weaker hypotheses, but in fact Viazovska’s construction produces Schwartz functions, so we might as well focus on that case.

The signiﬁcance of the Fourier transform in sphere packing is that it diagonalizes the operation of translation by any vector. Speciﬁcally, (4.1) implies that

f(y)e2πi t,y e2πi x,y dy,

f(x + t) =

Rn

which means that translating the input to the function f by t amounts to multiplying its Fourier transform f(y) by e2πi t,y . Simultaneously diagonalizing all these translation operators makes the Fourier transform an ideal tool for studying periodic structures.

The key technical tool behind linear programming bounds is the Poisson summation formula, which expresses a duality between summing a function over a lattice and summing the Fourier transform over the dual lattice, as deﬁned in (3.2). Poisson summation says that if f is a Schwartz function, then

- (4.2) x∈Λ

f(x) =

1 vol(Rn/Λ) y∈Λ

∗

f(y).

In other words, summing f over Λ∗ is almost the same as summing f over Λ, with the only diﬀerence being a factor of vol(Rn/Λ). When expressed in this form, Poisson summation looks mysterious, but it becomes far more transparent when written in the translated form

- (4.3) x∈Λ


1 vol(Rn/Λ) y∈Λ

f(y)e2πi y,t .

f(x + t) =

∗

This equation reduces to (4.2) when t = 0, and it has a simple proof. As a function of t, the left side of (4.3) is periodic modulo Λ, while the right side is its Fourier series. In particular, the right side uses exactly the complex exponentials t  → e2πi y,t that are periodic modulo Λ, namely those with y ∈ Λ∗ (as follows easily from

- (3.2)). Orthogonality let us compute the coeﬃcient of such an exponential, and some manipulation yields f(y)/vol(Rn/Λ).


Now we can state and prove the linear programming bounds, which show how to convert a certain sort of auxiliary function into a sphere packing bound. Speciﬁcally, we will use functions f : Rn → R such that f is eventually nonpositive (i.e., there exists a radius r such that f(x) ≤ r for |x| ≥ r) while f is nonnegative everywhere.

Theorem 4.1 (Cohn and Elkies [2]). Let f : Rn → R be a Schwartz function and r a positive real number such that f(0) = f(0) > 0, f(y) ≥ 0 for all y ∈ Rn, and

- f(x) ≤ 0 for |x| ≥ r. Then the sphere packing density in Rn is at most vol Br/n 2 .


The name “linear programming” refers to optimizing a linear function subject to linear constraints. The optimization problem of choosing f so as to minimize r can

be rephrased as an inﬁnite-dimensional linear program after a change of variables, but we will not adopt that perspective here.

Proof. The proof consists of applying the contrasting inequalities f(x) ≤ 0 and

- f(y) ≥ 0 to the two sides of Poisson summation. We will begin by proving the theorem for lattice packings, which is the simplest case.


Suppose Λ is a lattice in Rn, and suppose without loss of generality that the minimal vector length of Λ is r (since the sphere packing density is invariant under rescaling). In other words, the packing uses balls of radius r/2, and its density is

vol Br/n 2 vol(Rn/Λ)

.

Proving the desired density bound vol Br/n 2 for Λ amounts to showing that vol(Rn/Λ) ≥ 1. By Poisson summation,

1 vol(Rn/Λ) y∈Λ

- (4.4) x∈Λ


f(y).

f(x) =

∗

Now the inequality f(x) ≤ 0 for |x| ≥ r tells us that the left side of (4.4) is bounded above by f(0), and the inequality f(y) ≥ 0 tells us that the right side is bounded below by f(0)/vol(Rn/Λ). It follows that

f(0) vol(Rn/Λ)

f(0) ≥

,

which yields vol(Rn/Λ) ≥ 1 because f(0) = f(0) > 0.

The general case is almost as simple, but the algebraic manipulations are a little trickier. Because periodic packings come arbitrarily close to the optimal sphere packing density, without loss of generality we can consider a periodic packing using balls of radius r/2, centered at the translates of a lattice Λ ⊆ Rn by vectors t1,...,tN. The packing density is

N vol Br/n 2 vol(Rn/Λ)

, and so we wish to prove that vol(Rn/Λ) ≥ N.

We will use the translated Poisson summation formula (4.3), which after a little manipulation implies that

2

N

N

1 vol(Rn/Λ) y∈Λ

e2πi y,t

f(tj − tk + x) =

f(y)

.

j

∗

j,k=1 x∈Λ

j=1

Again we apply the contrasting inequalities on f and f to the left and right sides, respectively. On the left, we obtain an upper bound by throwing away every term except when j = k and x = 0; on the right, we obtain a lower bound by throwing away every term except when y = 0. Thus,

N2 vol(Rn/Λ)

Nf(0) ≥

f(0),

which implies that vol(Rn/Λ) ≥ N and hence that the density is at most vol Br/n 2 , as desired.

This proof technique may look absurdly ineﬃcient. We start with Poisson summation, which expresses a deep duality, and then we recklessly throw away all the nontrivial terms, leaving only the contributions from the origin. One practical justiﬁcation is that we have little choice in the matter, since we don’t know what the other terms are (they all depend on the lattice). A deeper justiﬁcation is that the omitted terms are generally small, and sometimes zero, so omitting them is not

- as bad as it sounds. To apply Theorem 4.1, we must choose an auxiliary function f. The theorem


then shows how to obtain a density bound from f, but it says nothing about how to choose f so as to minimize r and hence minimize the density bound. Sadly, optimizing the auxiliary function remains an unsolved problem, and the best possible choice of f is known only when n = 1, 8, or 24.

As a ﬁrst step towards solving this problem, note that we can radially symmetrize f, so that f(x) depends only on |x|, because all the constraints on f are linear and rotationally invariant. Then f is really a function of one radial variable, as is f. Functions of one variable feel like they should be tractable, but this optimization problem turns out to be impressively subtle.

If we can’t fully optimize the choice of f, then what can we do? Several explicit constructions are known, but in general we must resort to numerical computation. For this purpose, it’s convenient to use auxiliary functions of the form f(x) = p(|x|2)e−π|x|

2

, where p is a polynomial. These functions are ﬂexible enough to approximate arbitrary radial Schwartz functions, but simple enough to be tractable. Numerical optimization then yields a high-precision approximation to the linear programming bound, which is shown in Figure 8 and Table 2.

5. The hunt for the magic functions

The most striking property of Figure 8 is that the upper and lower bounds in Rn seem to touch when n = 8 or 24. In other words, there should be magic auxiliary functions that solve the sphere packing problem in these dimensions, by achieving r = √2 in Theorem 4.1 when n = 8 and r = 2 when n = 24. (These values of r are the minimal vector lengths in E8 and Λ24, respectively.) This is exactly what has now been proved, and the proof simply amounts to constructing an appropriate auxiliary function. Linear programming bounds do not seem to be sharp for any other n > 2, which makes these two cases truly remarkable.

The existence of these magic functions was conjectured by Cohn and Elkies [2] on the basis of numerical evidence and analogies with other problems in coding theory. Further evidence was obtained by Cohn and Kumar [3] in the course of proving that the Leech lattice is the densest lattice in R24, while Cohn and Miller [5] carried out an even more detailed study of the magic functions. These calculations left no doubt that the magic functions existed: one could compute them to ﬁfty decimal places, plot them, approximate their roots and power series coeﬃcients, etc. They were perfectly concrete and accessible functions, amenable to exploration and experimentation, which indeed uncovered various intriguing patterns. All that was missing was an existence proof.

However, proving existence was no easy matter. There was no sign of an explicit formula, or any other characterization that could lead to a proof. Instead, the magic functions seemed to come out of nowhere.

dimension

1 0

4 8 12 16 20 24 28 32 36

linear programming bound

log(density)

best packing known

−14

Figure 8. The logarithm of sphere packing density as a function of dimension. The upper curve is the numerically optimized linear programming bound, while the lower curve is the best packing currently known. The truth lies somewhere in between.

Table 2. The linear programming bound for the sphere packing density in Rn with 1 ≤ n ≤ 36. All numbers are rounded up.

n upper bound n upper bound n upper bound

- 1 1.000000000 13 0.0624817002 25 0.001384190723
- 2 0.906899683 14 0.0463644893 26 0.000991023890
- 3 0.779746762 15 0.0342482621 27 0.000708229796
- 4 0.647704966 16 0.0251941308 28 0.000505254217
- 5 0.524980022 17 0.0184640904 29 0.000359858186
- 6 0.417673416 18 0.0134853405 30 0.000255902875
- 7 0.327455611 19 0.0098179552 31 0.000181708382
- 8 0.253669508 20 0.0071270537 32 0.000128843289
- 9 0.194555339 21 0.0051596604 33 0.000091235604
- 10 0.147953479 22 0.0037259420 34 0.000064522197
- 11 0.111690766 23 0.0026842799 35 0.000045574385
- 12 0.083775831 24 0.0019295744 36 0.000032153056


The fundamental diﬃculty is explaining where the magic comes from. One can optimize the auxiliary function in any dimension, but that will generally not produce a sharp bound for the packing density. Why should eight and twenty-four dimensions be any diﬀerent? The numerical results show that the bound is nearly sharp in those dimensions, but why couldn’t it be exact for a hundred decimal places, followed by random noise? That’s not a plausible scenario for anyone with faith in the beauty of mathematics, but faith does not amount to a proof, and any proof must take advantage of special properties of these dimensions.

For comparison, the answer is far less nice in sixteen dimensions. By analogy with r = √2 when n = 8 and r = 2 when n = 24, one might guess that r = √3 when n = 16, but that bound cannot be achieved. Instead, numerical optimization seems to converge to r2 = 3.0252593116828820..., which is close to 3 but not equal to it. This number has not yet been identiﬁed exactly.

Despite the lack of an existence proof, the proof of Theorem 4.1 implicitly describes what the magic functions must look like:

Lemma 5.1. Suppose f satisﬁes the hypotheses of the linear programming bounds for sphere packing in Rn, with f(x) ≤ 0 for |x| ≥ r, and suppose Λ is a lattice in Rn with minimal vector length r. Then the density of Λ equals the bound vol Br/n 2

from Theorem 4.1 if and only if f vanishes on Λ \ {0} and f vanishes on Λ∗ \ {0}. Proof. Recall that the proof of Theorem 4.1 for a lattice Λ amounted to dropping all the nontrivial terms in the Poisson summation formula, to obtain the inequality

f(0) vol(Rn/Λ)

1 vol(Rn/Λ) y∈Λ

f(0) ≥

f(y) ≥

.

f(x) =

∗

x∈Λ

The only way this argument could yield a sharp bound is if all the omitted terms were already zero. In other words, f proves that Λ is an optimal sphere packing if and only if f vanishes on Λ \ {0} and f vanishes on Λ∗ \ {0}.

As discussed in the previous section, without loss of generality we can assume that f is a radial function, as is f. We know exactly where the roots of f and f should be, since E8 = E8∗ with vector lengths

√

2k for k = 1,2,..., while Λ24 = Λ∗24 with vector lengths

√

2k for k = 2,3,.... These roots should have order two, to avoid sign changes, except that the ﬁrst root of f should be a single root. See Figure 9 for a diagram.

Thus, our problem is simple to state: how can we construct a radial Schwartz function f such that f and f have the desired roots and no others? Note that Poisson summation over E8 or Λ24 then implies that f(0) = f(0), and ﬂipping the sign of f if necessary ensures that all the necessary inequalities hold.

Unfortunately it’s diﬃcult to take advantage of this characterization. The problem is that it’s hard to control a function and its Fourier transform simultaneously: it’s easy to produce the desired roots in either one separately, but not at the same time. Our inability to control f without losing control of f is at the root of the Heisenberg uncertainty principle, and it’s a truly fundamental obstacle.

One natural way to approach this problem is to carry out numerical experiments. Cohn and Miller used functions of the form f(x) = p(|x|2)e−π|x|

2

to approximate the magic functions, where p is a polynomial chosen to force f and f to have many of the desired roots. Such an approximation can never be exact, since it has only

f

√2 √4 √6 √8

f

√2 √4 √6 √8

Figure 9. A schematic diagram showing the roots of the magic function f and its Fourier transform f in eight dimensions. The ﬁgure is not to scale, because the actual functions decrease too rapidly for an accurate plot to be illuminating.

ﬁnitely many roots, but it can come arbitrarily close to the truth. This investigation uncovered several noteworthy properties of the magic functions, which showed that they had unexpected structure. For example, if we normalize the magic functions f8 and f24 in 8 and 24 dimensions so that f8(0) = f24(0) = 1, then Cohn and Miller conjectured that their second Taylor coeﬃcients are rational:

27 10|x|2 + O |x|4 , f8(x) = 1 −

3 2|x|2 + O |x|4 ,

f8(x) = 1 −

14347 5460 |x|2 + O |x|4 , f24(x) = 1 −

205 156|x|2 + O |x|4 .

f24(x) = 1 −

If all the higher-order coeﬃcients had been rational as well, then it would have opened the door to determining these functions exactly, but frustratingly it seems that the other coeﬃcients are far more subtle and presumably irrational. The magic functions retained their mystery, and this Taylor series behavior went unexplained until the exact formulas for the magic functions were discovered.

Given the diﬃculty of controlling f and f simultaneously, one natural approach is to split them into eigenfunctions of the Fourier transform. By Fourier inversion, every radial function f satisﬁes f = f. Thus, if we set f+ = f + f /2 and f− = f − f /2, then f = f+ + f− with f+ = f+ and f− = −f−. Because f and f vanish at the same points, they share these roots with f+ and f−. Our goal is therefore to construct radial eigenfunctions of the Fourier transform with prescribed roots. The advantage of this approach is that it conveniently separates into two distinct problems, namely constructing the +1 and −1 eigenfunctions, but these problems remain diﬃcult.

6. Modular forms

Ever since the Cohn-Elkies paper in 2003, number theorists had hoped to construct the magic functions using modular forms. The reasoning is simple: modular forms are deep and mysterious functions connected with lattices, as are the magic functions, so wouldn’t it make sense for them to be related? Unfortunately, they are entirely diﬀerent sorts of functions, with no clear connection between them. That’s where matters stood until Viazovska discovered a remarkable integral transform, which enabled her to construct the magic functions using modular forms. We’ll get there shortly, but ﬁrst let’s brieﬂy review how modular forms work.

We’ll start with some examples. Every lattice Λ has a theta series ΘΛ, deﬁned by eπi|x|

2z.

- (6.1) ΘΛ(z) = x∈Λ


This series converges when Imz > 0, and it deﬁnes an analytic function on the upper half-plane h = {z ∈ C : Imz > 0}. To motivate the deﬁnition, think of the theta series as a generating function, where the coeﬃcient of eπitz counts the number of x ∈ Λ with |x|2 = t. However, there’s one aspect not explained by the generating function interpretation: why write this function in terms of eπiz? Doing so may at ﬁrst look like a gratuitous nod to Fourier series, but it leads to an elegant transformation law based on applying Poisson summation to a Gaussian:

Proposition 6.1. If Λ is a lattice in Rn, then

n/2

1 vol(Rn/Λ)

i z

ΘΛ∗(−1/z) for all z ∈ h.

ΘΛ(z) =

Proof. One of the most important properties of Gaussians is that the set of Gaussians is closed under the Fourier transform: the Fourier transform of a wide Gaussian is a narrow Gaussian, and vice versa. More precisely, for t > 0 the Fourier transform of the Gaussian x  → e−tπ|x|

2/t. In fact, the same holds whenever t is a complex number with Ret > 0, by analytic continuation. Then Poisson summation tells us that

2

on Rn is x  → t−n/2e−π|x|

1 vol(Rn/Λ) y∈Λ

2/t.

2

t−n/2e−π|y|

e−tπ|x|

=

∗

x∈Λ

Setting z = it, we ﬁnd that

n/2

1 vol(Rn/Λ)

i z

ΘΛ∗(−1/z) whenever Imz > 0, as desired.

ΘΛ(z) =

If we set Λ = E8, then Λ∗ = E8 as well, and we ﬁnd that ΘE

### (−1/z) = z4ΘE

(z). Furthermore, E8 is an even lattice, and hence the Fourier series (6.1) implies that ΘE

8

8

### (z). These two symmetries are the most important properties of ΘE

### (z + 1) = ΘE

8

8

. For exactly the same reasons, the theta series of the Leech lattice Λ24 satisﬁes

8

### (−1/z) = z12ΘΛ

ΘΛ

### (z) and ΘΛ

### (z + 1) = ΘΛ

(z).

24

24

24

24

The mappings z  → z + 1 and z  → −1/z generate a discrete group of transformations of the upper half-plane, called the modular group. It turns out to be the same as the action of the group SL2(Z) on the upper half-plane by linear fractional transformations, but we will not need this fact except for naming purposes.

A modular form of weight k for SL2(Z) is a holomorphic function ϕ: h → C such that ϕ(z + 1) = ϕ(z) and ϕ(−1/z) = zkϕ(z) for all z ∈ h, while ϕ(z) remains bounded as Imz → ∞. (The latter condition is called being holomorphic at inﬁnity, because it means the singularity there is removable.) It’s not hard to show that

the weight of a nonzero modular form must be nonnegative and even, and the only modular forms of weight zero are the constant functions.

satisfy the transformation laws for modular forms of weight 4 and 12, respectively, and it is easy to check that they are holomorphic

We have seen that ΘE

### and ΘΛ

8

24

- at inﬁnity. Thus, these theta series are modular forms. There are a number of other well-known modular forms. For example, the


Eisenstein series Ek deﬁned by Ek(z) =

- 1

- 2ζ(k) (m,n)∈Z2


1 (mz + n)k

(m,n) =(0,0)

is a modular form of weight k for SL2(Z) whenever k is an even integer greater than 2 (while it vanishes when k is odd). The proofs of the required identities Ek(z +1) = Ek(z) and Ek(−1/z) = zkEk(z) simply amount to rearranging the sum. Here ζ denotes the Riemann zeta function, and 2ζ(k) is a normalizing factor. The advantage of this normalization is that it leads to the Fourier expansion

∞

2 ζ(1 − k)

σk−1(m)e2πimz,

- (6.2) Ek(z) = 1 +


m=1

where σk−1(m) is the sum of the (k − 1)-st powers of the divisors of m and ζ(1 − k) turns out to be a rational number.

The notational conﬂict between the Eisenstein series Ek and the E8 lattice is unfortunate, but both notations are well established. Fortunately, we will never need to set k = 8, and the context should easily distinguish between Eisenstein series and lattices.

Modular forms are highly constrained objects, which makes coincidences commonplace. For example, ΘE

is the same as E4, because there is a unique modular form of weight 4 for SL2(Z) with constant term 1. Equivalently, for m = 1,2,... there are exactly 240σ3(m) vectors x ∈ E8 with |x|2 = 2m. The theta series ΘΛ

8

is not an Eisenstein series, but it can be written in terms of them as

24

7 12

5 12

E43 +

E62.

ΘΛ

=

24

More generally, let Mk denote the space of modular forms of weight k for SL2(Z). Then k≥0 Mk is a graded ring, because the product of modular forms of weights k and is a modular form of weight k + . This ring is isomorphic to a polynomial ring on two generators, namely E4 and E6. In other words, the set

E4iE6j : i,j ≥ 0 and 4i + 6j = k is a basis for the modular forms of weight k. In particular, there is no modular form of weight 2 for SL2(Z), because the weights of E4 and E6 are too high to generate such a form.

One cannot obtain a modular form of weight 2 by setting k = 2 in the double sum deﬁnition of Ek. The problem is that rearranging the terms is crucial for proving modularity, but when k = 2 the series converges only conditionally, not absolutely. Instead, we can deﬁne E2 using (6.2). That deﬁnes a merely quasimodular form, rather than an actual modular form, because one can show that E2(−1/z) = z2E2(z) − 6iz/π rather than z2E2(z). This imperfect Eisenstein series will play a role in constructing the magic functions.

By default all modular forms are required to be holomorphic, but we can of course consider quotients that are no longer holomorphic. A meromorphic modular form is the quotient of two modular forms, and it is weakly holomorphic if it is holomorphic on h (but not necessarily at inﬁnity). Unlike the holomorphic case, there is an inﬁnite-dimensional space of weakly holomorphic modular forms of each even weight, positive or negative. Allowing a pole at inﬁnity oﬀers tremendous ﬂexibility.

On the face of it, modular forms seem to have little to do with the magic functions. In particular, it’s not clear what modular forms have to do with the radial Fourier transform in n dimensions. One hint that they may be relevant comes from the Laplace transform. As we saw when we looked at theta series, Gaussians are a particularly useful family of functions for which we can easily compute the Fourier transform. It’s natural to deﬁne a function f as a continuous linear combination of Gaussians via

∞

2

e−tπ|x|

f(x) =

g(t)dt,

0

2

where the weighting function g(t) gives the coeﬃcient of the Gaussian e−tπ|x|

. This formula is simply the Laplace transform of g, evaluated at π|x|2.

Assuming g is suﬃciently well behaved, we can compute f by interchanging the Fourier transform with the integral over t, which yields

f(y) =

=

∞

2/tg(t)dt

t−n/2e−π|y|

0

∞

2

e−tπ|y|

tn/2−2g(1/t)dt.

0

In other words, taking the Fourier transform of f amounts to replacing g with t  → tn/2−2g(1/t).

As a consequence, if g(1/t) = εt2−n/2g(t) with ε = ±1, then f = εf. Thus, we can construct eigenfunctions of the Fourier transform by taking the Laplace transform of functions satisfying a certain functional equation. What’s noteworthy about this functional equation is how much it looks like the transformation law for a modular form on the imaginary axis. If we set g(t) = ϕ(it), then the modular form equation ϕ(−1/z) = zkϕ(z) with z = it corresponds to g(1/t) = iktkg(t). If ϕ is a meromorphic modular form of weight k = 2 − n/2 that vanishes at i∞ and has no poles on the imaginary axis, then f is a radial eigenfunction of the Fourier transform in Rn with eigenvalue ik.

Of course this is far from the only way to construct Fourier eigenfunctions, but it’s a natural way to construct them from modular forms. As stated here, it’s clearly not ﬂexible enough to construct the magic functions, because it produces only one eigenvalue. If we take n = 8 and weight k = 2 − n/2 = −2, then ik = −1, so we can construct a −1 eigenfunction but not a +1 eigenfunction for the same dimension. This turns out not to be a serious obstacle: there are many variants of modular forms (for other groups or with characters), and it’s not hard to produce eigenfunctions with both eigenvalues. However, there’s a much worse problem. If we build an eigenfunction this way, then there’s no obvious way to control the roots of the eigenfunction using the Laplace transform. Given that our goal is to prescribe the roots, this approach seems to be useless. What’s holding us back is that we

have not taken full advantage of the modular form: we are using only the identity ϕ(−1/z) = zkϕ(z), and not ϕ(z + 1) = ϕ(z).

7. Viazovska’s proof

The fundamental problem with the Laplace transform approach in the previous section is that it seems to be impossible to achieve the desired roots. Viazovska gets around this diﬃculty by a bold construction: she simply inserts the desired roots by brute force, by including an explicit factor of sin2 π|x|2/2 , which vanishes to second order at |x| =

√

2k for k = 1,2,... and fourth order at x = 0. In her construction for eight dimensions, both eigenfunctions have the form

∞

2t dt for some function g.

g(t)e−π|x|

- (7.1) sin2 π|x|2/2


0

One obvious issue with this approach is that sin2 π|x|2/2 vanishes more often than we would like. Speciﬁcally, it vanishes to fourth order when x = 0 and second order when |x| = √2, whereas we wish to have no root when x = 0 and only a ﬁrst-order root when |x| = √2. To avoid this diﬃculty, the integral in (7.1) must have poles at 0 and √2 as a function of |x|, which cancel the unwanted roots. The integral will converge only for |x| > √2, but the function deﬁned by (7.1) extends to |x| ≤

√2 by analytic continuation.

Which choices of g will produce eigenfunctions of the Fourier transform in R8? This is not clear, because the factor of sin2 π|x|2/2 disrupts the straightforward Laplace transform calculations from the end of Section 6. Instead, Viazovska writes the sine function in terms of complex exponentials and carries out elegant contour integral arguments to show that (7.1) gives an eigenfunction whenever g satisﬁes certain transformation laws. Identifying the right conditions on g is not at all obvious, and it’s the heart of her paper.

To get a +1 eigenfunction, Viazovska shows that it suﬃces to take g(t) = t2ϕ(i/t), where ϕ is a weakly holomorphic quasimodular form of weight 0 and depth 2 for SL2(Z). Here, a quasimodular form of depth 2 is a quadratic polynomial in E2 with modular forms as coeﬃcients, where E2 is the Eisenstein series of weight 2. Recall that E2 fails to be a modular form because of the strange transformation law E2(−1/z) = z2E2(z) − 6iz/π, but that functional equation works perfectly here.

To get a −1 eigenfunction, Viazovska shows that it suﬃces to take g(t) = ψ(it), where ψ is a weakly holomorphic modular form of weight −2 for a subgroup of SL2(Z) called Γ(2) and ψ satisﬁes the additional functional equation

ψ(z) = ψ(z + 1) + z2ψ(−1/z).

We have not discussed modular forms for other groups such as Γ(2), but they are similar in spirit to those for SL2(Z). In particular, the ring of modular forms for Γ(2) is generated by two forms of weight 2, namely Θ4Z (the fourth power of the theta series of the one-dimensional integer lattice) and its translate z  → Θ4Z(z + 1).

These conditions for ϕ and ψ are every bit as arcane as they look. It’s far from obvious that they lead to eigenfunctions, but Viazovska’s contour integral proof shows that they do. Even once we know that this method gives eigenfunctions, it’s unclear how to choose ϕ and ψ to yield the magic eigenfunctions, or whether this is possible at all.

Fortunately, one can write down some necessary conditions, and then the simplest functions satisfying those conditions work perfectly. In particular, we can take

- 4π(E2E4 − E6)2

- 5(E62 − E43)


ϕ = and

32Θ4Z|T 5Θ8Z − 5Θ4Z|TΘ4Z + 2Θ8Z|T 15πΘ8Z Θ4Z − Θ4Z|T 2

ψ = −

,

where f|T denotes the translate z  → f(z + 1) of a function f. Thus, to obtain the magic function for E8 we set

- (7.2) f(x) = sin2 π|x|2/2

∞

0

t2ϕ(i/t) + ψ(it) e−π|x|

2t dt

for the speciﬁc ϕ and ψ identiﬁed by Viazovska. Because the ϕ and ψ terms yield eigenfunctions of the Fourier transform, we ﬁnd that

f(y) = sin2 π|y|2/2

∞

0

t2ϕ(i/t) − ψ(it) e−π|y|

2t dt.

The integral in the formula for f(x) converges only when |x| > √2, but the one in the formula for f(y) turns out to converge whenever |y| > 0, because the problematic growth of the integrand cancels in the diﬀerence t2ϕ(i/t) − ψ(it).

These formulas deﬁne Schwartz functions that have the desired roots, and one can check that f(0) = f(0) = 1, but it’s not obvious that they satisfy the inequalities f(x) ≤ 0 for |x| ≥

√2 and f(y) ≥ 0 for all y, because there might be additional sign changes. In fact, these inequalities hold for a fundamental reason:

- (7.3) t2ϕ(i/t) + ψ(it) < 0 and t2ϕ(i/t) − ψ(it) > 0


for all t ∈ (0,∞). In other words, the inequalities already hold at the level of the quasimodular forms, with no need to worry about the Laplace transform except to observe that it preserves positivity. Note that the restriction of the inequality f(x) ≤ 0 to |x| ≥

√2 ﬁts perfectly into this framework, because the integral in (7.2) diverges for |x| < √2 and thus we do not obtain f(x) ≤ 0 there. All that remains is to prove the inequalities (7.3). Unfortunately, no simple proof of these inequalities is known at present, but one can verify them by reducing the problem to a ﬁnite calculation.

Thus, Viazovska’s formula (7.2) deﬁnes the long-sought magic function for E8 and solves the sphere packing problem in eight dimensions. What about twenty-four dimensions? The same basic approach works, but choosing the quasimodular forms requires more eﬀort. Fortunately, the conjectures by Cohn and Miller can be used to help pin down the right choices. Once the magic function has been identiﬁed, there are additional technicalities involved in verifying the inequality for f, but these challenges can be overcome, which leads to a solution of the sphere packing problem in twenty-four dimensions.

8. Future prospects

Nobody expects Viazovska’s proof to generalize to any other dimensions above two. Why just eight and twenty-four? At one level, we really don’t know why. Nobody has been able to ﬁnd a proof, or even a compelling heuristic argument, that rules out similar phenomena in higher dimensions. We can’t even rule out the

possibility that linear programming bounds might solve the sphere packing problem in every suﬃciently high dimension, although that’s clearly ridiculous.

Despite our lack of understanding, the special role of eight and twenty-four dimensions aligns with our experience elsewhere in mathematics. Mathematics is full of exceptional or sporadic phenomena that occur in only ﬁnitely many cases, and the E8 and Leech lattices are prototypical examples. These objects do not occur in isolation, but rather in constellations of remarkable structures. For example, both E8 and the Leech lattice are connected with binary error-correcting codes, combinatorial designs, spherical designs, ﬁnite simple groups, etc. Each of these connections constrains the possibilities, especially given the classiﬁcation of ﬁnite simple groups, and there just doesn’t seem to be room for a similar constellation in higher dimensions.

Instead, solving the sphere packing problem in further dimensions will presumably require new techniques. One particularly attractive case is the D4 root lattice, which is surely the best sphere packing in R4. This lattice shares some of the wonderful properties of E8 and the Leech lattice, but not enough for the four-dimensional linear programming bound to be sharp. It would be a plausible target for any generalization of this bound, and in fact such a generalization may be emerging.

Building on work of Schrijver, Bachoc and Vallentin, and other researchers, de Laat and Vallentin have generalized linear programming bounds to a hierarchy of semideﬁnite programming bounds [12]. Linear programming bounds are the ﬁrst level of this hierarchy, which means that E8 and the Leech lattice have the simplest possible proofs from this perspective. What about D4? Perhaps this case can be solved at one of the next few levels of the hierarchy. Much work remains to be done here, and it’s unclear what the prospects are for any particular dimension, but it is not beyond hope that four dimensions could someday join eight and twenty-four among the solved cases of the sphere packing problem.

Acknowledgments

I am grateful to James Bernhard, Donald Cohn, Matthew de Courcy-Ireland, Stephen D. Miller, Frank Morgan, David Rohrlich, Achill Sch¨urmann, Frank Vallentin, and Maryna Viazovska for their feedback and suggestions.

Photo Credits

Figure 1 is courtesy of Daniil Yevtushynsky. The photos in Figure 2 are courtesy of Mary Caisley, Mark Ostow, C. J. Mozzochi, and Julia Semikina, from left to right. Figures 3 and 7 are courtesy of Henry Cohn. Figure 6 is courtesy of Matthew Kownacki.

References

- [1] H. Cohn, Packing, coding, and ground states, PCMI 2014 lecture notes, 2016. arXiv:1603.05202
- [2] H. Cohn and N. Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157 (2003), no. 2, 689–714. arXiv:math/0110009 MR1973059 doi:10.4007/annals.2003.157.689
- [3] H. Cohn and A. Kumar, Optimality and uniqueness of the Leech lattice among lattices, Ann. of Math. (2) 170 (2009), no. 3, 1003–1050. arXiv:math/0403263 MR2600869 doi:10.4007/annals.2009.170.1003
- [4] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24, preprint, 2016. arXiv:1603.06518


- [5] H. Cohn and S. D. Miller, Some properties of optimal functions for sphere packing in dimensions 8 and 24, preprint, 2016. arXiv:1603.04759
- [6] J. H. Conway and N. J. A. Sloane, What are all the best sphere packings in low dimensions?, Discrete Comput. Geom. 13 (1995), no. 3–4, 383–403. MR1318784 doi:10.1007/BF02574051
- [7] J. H. Conway and N. J. A. Sloane, Sphere packings, lattices and groups, third edition, Grundlehren der Mathematischen Wissenschaften 290, Springer, New York, 1999. MR1662447 doi:10.1007/978-1-4757-6568-7
- [8] T. C. Hales, Cannonballs and honeycombs, Notices Amer. Math. Soc. 47 (2000), no. 4, 440–449. MR1745624
- [9] T. C. Hales, A proof of the Kepler conjecture, Ann. of Math. (2) 162 (2005), no. 3, 1065–1185. MR2179728 doi:10.4007/annals.2005.162.1065
- [10] T. Hales, M. Adams, G. Bauer, D. T. Dang, J. Harrison, T. L. Hoang, C. Kaliszyk, V. Magron, S. McLaughlin, T. T. Nguyen, T. Q. Nguyen, T. Nipkow, S. Obua, J. Pleso, J. Rute, A. Solovyev, A. H. T. Ta, T. N. Tran, D. T. Trieu, J. Urban, K. K. Vu, and R. Zumkeller, A formal proof of the Kepler conjecture, preprint, 2015. arXiv:1501.02155
- [11] G. A. Kabatyanskii and V. I. Levenshtein, Bounds for packings on a sphere and in space, Problems Inform. Transmission 14 (1978), no. 1, 1–17. MR0514023
- [12] D. de Laat and F. Vallentin, A semideﬁnite programming hierarchy for packing problems in discrete geometry, Math. Program. 151 (2015), no. 2, Ser. B, 529–553. arXiv:1311.3789 MR3348162 doi:10.1007/s10107-014-0843-4
- [13] D. de Laat and F. Vallentin, A breakthrough in sphere packing: the search for magic functions, Nieuw Arch. Wiskd. (5) 17 (2016), no. 3, 184–192. arXiv:1607.02111
- [14] A. Venkatesh, A note on sphere packings in high dimension, Int. Math. Res. Not. 2013 (2013), no. 7, 1628–1642. MR3044452 doi:10.1093/imrn/rns096
- [15] M. S. Viazovska, The sphere packing problem in dimension 8, preprint, 2016. arXiv:1603.04246


