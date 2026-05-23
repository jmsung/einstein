# arXiv:1210.5451v1[math-ph]19Oct2012

## A geometrical approach to computing free energy landscapes from short-ranged potentials

Miranda Holmes-Cerfon, Steven J. Gortler, and Michael P. Brenner

School of Engineering and Applied Sciences and Kavli Institute for Bionano Science and Technology, Harvard University, Cambridge, MA 02138, USA

Particles interacting with short-ranged potentials have attracted increasing interest, partly for their ability to model mesoscale systems such as colloids interacting via DNA or depletion. We consider the free energy landscape of such systems as the range of the potential goes to zero. In this limit, the landscape is entirely deﬁned by geometrical manifolds, plus a single control parameter. These manifolds are fundamental objects that do not depend on the details of the interaction potential, and provide the starting point from which any quantity characterizing the system – equilibrium or non-equilibrium – can be computed for arbitrary potentials. To consider dynamical quantities we compute the asymptotic limit of the Fokker-Planck equation, and show that it becomes restricted to the low-dimensional manifolds connected by “sticky” boundary conditions. To illustrate our theory, we compute the low-dimensional manifolds for n ≤ 8 identical particles, providing a complete description of the lowest-energy parts of the landscape including ﬂoppy modes with up to 2 internal degrees of freedom. The results can be directly tested on colloidal clusters. This limit is a novel approach for understanding energy landscapes, and our hope is that it can also provide insight into ﬁnite-range potentials.

The dynamics on free energy landscapes is a ubiquitous paradigm for characterizing molecular and mesoscopic systems, from atomic clusters, to protein folding, to colloidal clusters. [1–4]. The predominant strategy for understanding the dynamics on an energy landscape has focused on the stationary points of the energy, the local minima and the transition states, and seeks the dynamical paths which connect these to each other, while more recent models generalize to metastable states connected by paths as a Markov State Model [5]. These techniques have proven to be extremely powerful, giving innumerable insights into the behaviour of complex systems [6–13], On the other hand, a major issue has been the diﬃculty of ﬁnding the transition paths, connecting local minima or metastable states to each other, especially given a complex energy landscape in a highdimensional space. A variety of creative methods have been developed in recent years for eﬃciently ﬁnding transition paths [14–24] but for a given system, there is no guarantee that all such paths have been found.

Here we present a diﬀerent point of view for understanding an energy landscape, that occurs when the range over which particles interact is much smaller than their size. Such is the case in certain mesoscale systems, for example, for C60 molecules [25, 26], or for colloids interacting via depletion [4] or coated with polymers or complementary DNA strands [27–30]. We will show that in this limit, the free energy landscape is described entirely by geometry, plus a single control parameter κ that is a function of the temperature, depth, and curvature of the original potential. This limit is related to the sticky sphere limit of a square-well potential [31], which has been used to investigate thermodynamic properties of hard sticky spheres [32–34]. The landscape can be thought of as a polygon living in a high-

dimensional space, whose corners (0-dimensional manifolds) are joined to each other by lines (1-dimensional manifolds), that in turn form the boundaries of faces (2dimensional manifolds), and so on. These manifolds are ﬁxed functions of the particles’ geometries, independent of the details of the original interaction potential from which the limit was taken.

Once the geometrical manifolds comprising the landscape are computed, non-equilibrium quantities characterizing the dynamics can be calculated by solving the Fokker-Planck equation or its adjoint on these manifolds. We show that in the short-ranged limit these equations acquire an eﬀective boundary condition at the boundary of every p-dimensional manifold in the polygon. This makes the kinetics computationally tractable, since the stiﬀ modes of a narrow potential become a set of boundary conditions.

The geometrical nature of the energy landscape does not mitigate its high dimensionality, but at low temperatures (high κ) both the free energies and the kinetics are dominated by the lowest-dimensional manifolds. This means that the description of the free energy landscape and kinetics for short-ranged potentials reduces to a problem in discrete and computational geometry – to ﬁnd all of the low dimensional manifolds for a given set of interacting particles.

As an illustration of the framework, we characterize the geometrical landscape for n ≤ 8 particles with identical potentials, and demonstrate how these solutions lead to a complete description of the energy landscape and the kinetics of this system. This solution describes both the geometrical limit of small atomic clusters as well as a direct prediction for colloidal clusters interacting with depletion forces [4, 6, 35, 36], where the predictions could be tested experimentally. The solution also provides a

framework for understanding and extending simulations on clusters with ﬁnite range potentials [1]. Our calculation of the energy landscape builds on the enumeration of all ﬁnite sphere packings of n particles with at least 3n−6 contacts [37, 38]. With these as the starting point, we compute every 1- and 2-dimensional manifold of motions that contains a 0- dimensional manifold at its boundary, from which we can extract statistical quantities such as the relative entropies of the diﬀerent types of motions. Then, we solve Fokker Planck equations on these manifolds to obtain transition rates between the lowest energy states, the 0-dimensional manifolds.

#### THE GEOMETRICAL LANDSCAPE

We begin by showing how the geometrical free energy landscape arises as a distinguished limit of particles interacting with arbitrary potentials of ﬁnite range. We consider a point x ∈ RN in conﬁguration space, with the potential energy given as a sum of potentials concentrated near diﬀerent geometrical boundaries as

U (x) =

k

C U(yk(x)/ ). (1)

The functions yk : Rn → R, (k = 1,...,kmax) represent the geometrical boundaries via their level sets {yk(x) = 0}, and U(y) : R → R is the potential energy near each boundary. For concreteness, let us suppose this is a model for n spheres with centers at xi ∈ R3, i = 1...n, so the conﬁguration is x = (x11,x12,x13,x21,...,xn3) ∈ R3n, and we take yk to be the excess bond distance, as yk = |xi(k) − xj(k)|2 − d, where d is the particles’ diameter. Then U(y) is the pairwise interaction potential that we assume has minimum U0 at y = 0 and is negligible beyond some cutoﬀ rc. For ease of exposition, the interaction potential is assumed to be identical between each pair of particles, but this is not a necessary restriction for the geometrical landscape to apply. For the total potential U , the parameter characterizes the range of the potential, while C is proportional to the depth. The geometrical limit requires taking C → ∞ as → 0 in a manner that we specify momentarily.

We consider particles that evolve according to the overdamped Langevin dynamics [39] at temperature T:

1 γ ∇U (x) +

dx dt

= −

√

2Dη(t), (2)

where γ is the friction coeﬃcient, D = (βγ)−1 is the diﬀusion coeﬃcient, β = (kBT)−1, kB is the Boltzmann constant, and η(t) is a 3n-dimensional white noise. The equilibrium probability for this system is the Gibbs distribution [40]:

dρ (x) = (Z )−1e−βU (x)dx. (3)

where Z is the normalizing constant.

The geometrical free energy landscape occurs when the range → 0. The relationship between the depth and the range is critical to obtaining an interesting limit. If only the range goes to zero, then particles are bonded for shorter and shorter times so that in the limit they simply behave like hard spheres. On the other hand, if the depth goes to −∞ too quickly, then the particles simply stick together and only unbind on exponentially long timescales [41]. The interesting limit occurs when particles stick to each other but unbind on accessible timescales; for this we must choose C so that the Boltzmann factor for two particles to be bonded to approaches a ﬁnite, non-zero constant: κ = lim →0 d1 0  rc e−C βU(x/ )dx, where we deﬁne Boltzmann factors non-dimensionally by scaling by the diameter d. Evaluating the integral using Laplace’s method then implies

e−βC U

0

κ = lim

→0

d cβC U (0)

(4)

We call the constant κ the sticky parameter. Note that κ is a function of both the potential and the temperature. The constant c = 2/π for hard-spheres.

In the geometrical limit, the probability measure ρ

becomes concentrated at the exact locations in conﬁguration space where a bond forms, i.e. on the level sets {yk(x) = 0} and all possible multi-way intersections. Thus the limiting probability distribution will be a weighted sum of delta functions, each deﬁned on a manifold corresponding to a diﬀerent set of bond constraints. The weight of the each delta function depends on the number of bonds and a geometrical factor associated with the entropy of the conﬁguration. This gives a geometrical picture of the energy landscape: When κ is large, the occupation probabilities will be dominated by conﬁgurations where the number of bonds m is large. For identical particles, with n ≤ 9, the maximum number of contacts is m = 3n − 6 [37, 38]: these are rigid structures that have no internal degrees of freedom, so they correspond to 0-dimensional manifolds, or “points”. The next lowest conﬁgurations in potential energy are manifolds with m = 3n−7, which are are obtained from rigid structures by breaking one bond. These have one internal degree of freedom so are 1-dimensional manifolds, or “lines”. The lines form the boundaries of 2-dimensional manifolds, or “faces”, when another bond is broken, and continuing up in dimensionality we obtain the entire energy landscape as the union of manifolds of diﬀerent dimensions.

Figure 1 shows a schematic contrasting this limiting case with the traditional picture of an energy landscape. The traditional picture is of an undulating surface, with local minima connected through saddle points, whose heights provide an activation barrier that determines the transition rates between basins. In contrast, in the geometrical limit, the local minima are inﬁnitely narrow

and deep, separated by long, relatively ﬂat spaces in between – the landscape can be thought of as a golf course punctuated with deep trenches very deep holes. Kinetics on this landscape are determined partly by an activation barrier – the time it takes to climb out of the hole – and partly by diﬀusion.

The ﬁgure also shows an explicit 1-dimensional manifold taken from the landscape for n = 6, an example we will return to throughout the text. There are two ground states, the polytetrahedron and the octahedron [38], and the manifold is the set of deformations corresponding to the transition path between these when a single bond is broken.

To explicitly calculate the equilibrium probabilities of the diﬀerent states in the geometrical landscape we consider a conﬁguration with m constraints or equivalently p ≡ 3n − 6 − m bonds broken. The constraints are written as an ordered multiindex α = (α1,α2,...αm) so the manifold of conﬁgurations satisfying such constraints is

Ωα = {x : yα

### (x) = yα

### (x) = ... = yα

(x) = 0,

1

2

m

yβ(x) > 0,β = αi}. (5) We write α = 0 to mean the region where no constraints are active, and let Ω = ∪αΩα be the full space of accessible conﬁgurations. The limiting partition function associated with these constraints is

1 d3n Ω

e−βU (x)dx, (6)

zα = lim →0

α

where Ω α is the neighbourhood surrounding the manifold where the potential U associated with the constraints is active:

Ω α = {x : 0 ≤ yα

(x) ≤  rc,

### (x),...,yα

1

m

yβ(x) >  rc,β = αi}. (7) This splits conﬁguration space near each manifold into two parts – the fast variables yα

changing rapidly along directions associated with the constraints (sometimes called the vibrational modes), and the slow variables yβ that are the unconstrained conﬁguration.

i

To compute the integral in (6) we need a parameterization of the manifolds associated with the constraints. It is convenient to parameterize the fast directions by the constraint variables themselves, x → yα

### . We choose the additional 3n − m variables y ∈ R3n−m so that ∇y·∇yα

### ,...yα

1

m

are orthogonal on the manifold. As discussed in the Appendix, it is possible to ﬁnd such a parameterization locally as long as the manifold associated with the constraint variables is regular – i.e., the coordinate transformation for the constraint variables must be smooth and invertible. This happens when the Hessian of the potential energy (say at = 1)

### = 0 on Ωα, i.e. the variables y, yα

i

i

m

)T (8)

Hα(x) = ∇∇U =1(x) = U (0)

∇yα

### (∇yα

i

i

i=1

has m non-zero eigenvalues. We can now evaluate

1 d3n Ω

zα =

α

me−βC

m

i=1 U(Yi) |gij|dY dy (9)

where Y = (Y1,...,Ym) with Yi = yα

### / , gij is the metric tensor associated with the transformation (yα

i

### ,y) → x with components gij = JkiJkj = JTJ, where Jij = ∂x

i

∂yj , and |gij| is its determinant. Let separate the metric tensor into blocks as

i

g =

gab gav gub guv

. (10)

The ﬁrst set of indices run from 1 ≤ a,b ≤ m and describe the fast variables, perpendicular to the manifold, while the second set run from m + 1 ≤ u,v ≤ N and describe the slow variables, along the constraint manifold. Let |gcd| be the determinant of a particular block. It follows from the deﬁnition of the metric that |gab|Y =0 = mi=1 λ−i 1, where the λi’s are the non-zero eigenvalues of Hα(x)/U (0), and the condition of orthogonality gives |gav|Y =0 = |gub|Y =0 = 0. Evaluating the integral in (9) over the fast variables using Laplace’s method, and letting → 0, shows the limit is

1 dp+6 Ω

zα = κm

hα(y) |gα|dy, (11)

α

where

hα(y) =

m

λ−i 1/2 (12)

i=1

is a geometrical factor (representing the “vibrational” degrees of freedom) that depends only on the level sets of the constraints, and gα = guv|Y =0 is the metric on manifold Ωα inherited from the ambient space by restriction. The integral (11) is simply the volume integral of hα(y) over Ωα.

The manifold Ωα contains 6 degrees of freedom representing translation and rotation of the cluster, and the partition function integral can be further simpliﬁed by integrating over the subspace spanned by these motions. This introduces a factor I(x) in the integral, the square root of the moment of inertia tensor [40]. If we let ΩQα be the quotient space formed by identifying points x ∼ z if x can be mapped to z by a combination of translations and rotations, i.e. ΩQα = Ωα/SE(3), where SE(3) is the special Euclidean group, then we can write

1 dp ΩQ

zα = κmζα = κm

hα(x)I(x) |g¯α|dx (13)

α

where g¯α is the metric on ΩQα, and we have dropped constants (such as free volume) that are the same for all

conﬁgurations. For convenience later on, we deﬁne ζα

as the part of the partition function that is independent of κ. The Appendix has a detailed discussion for how to construct g¯α, which is critical for using the formalism developed here for practical calculations. Fig. 1 (bottom) is an example of such a quotient manifold, where each point on the manifold represents the 6-dimensional space of clusters in conﬁguration space that are related by rotations or translations.

The particles in Figure 1 are diﬀerent colours to identify the diﬀerent transitions that occur when moving around conﬁguration space. However, when (as imagined here) the particles are identical, permuting the colors of any particular structure yields a geometrically isomorphic structure on a separate part of the quotient space. The free energy must account for the number nα of distinct manifolds that are geometrically isomorphic to ΩQα. When p = 0 this is nα = C0N!/σ, where σ is the symmetry number, i.e. the number of particle permutations that are equivalent to a rotation, and C0 = 2 if the structure is chiral and C0 = 1 otherwise [42]. For p > 0, we count the multiplicities by counting how many times a mode occurs from the perspective of each 0-dimensional “corner” of the mode, and dividing by the total number of corners. [43] For example, Fig. 1 has corners from two diﬀerent ground states, the polytetrahedron and the octahedron, which occur with multiplicities n1,n2 respectively. For each polytetrahedron, there is ν1 = 1 line coming out of it that is isomorphic to this transition, and for the octahedron there are ν2 = 12 distinct lines. (The numbers ν1, ν2 are indicated on the arrows connecting red circles to blue circles in Figure 2, where the transition under consideration is mode 7.) Therefore the total multiplicity of the line is (n1ν1 + n2ν2)/2. Consider a transition connecting a polytetrahedron to a distinct copy of itself, say mode 5. Here there are ν1 = 4 such lines connected to each polytetrahedron, so the multiplicity of the line is n1ν1/2. In general, each p-dimensional manifold Ωα contains a total of nc corners from N ≤ nc nonisomorphic ground states, each ground state having multiplicity ni, and such that each single ground state is connected to νi distinct manifolds isomorphic to Ωα, so the multiplicity is nα = Ni=1 niνi/nc.

Putting this all together, the total partition function of all structures isomorphic to a given constraint manifold ΩQα is nαzα, and the free energy of these structures are Fα = −kBT log(nαzα). We can separate this free energy into Fα = −mkBT log κ − kBT log(nαζα), using the deﬁnition of ζα in Equation (13). The ﬁrst term (−mkBT log κ) depends on the temperature, bond energy, and width of the potential, whereas the second term with Sα = −kB log(nαζα) is entirely geometrical, and essentially is the entropy of structures corresponding to the constraint set ΩQα. As an example, we have plotted Fα/kBT along the polytetrahedral-octahedral transition in Figure 1 (bottom). This varies smoothly along the manifold as I(x), h(x) vary. The endpoints of the

manifold are the ground states, where the free energy changes discontinuously because the number of bonds has changed – this causes a jump in the energetic part via m, and the entropic part via hα.

With these results in hand, we can now compare the total entropies of ﬂoppy manifolds of diﬀerent dimensions, to understand the temperature range in which the diﬀerent manifolds occur. Let the total geometrical partition function of manifolds of dimension p be

Zp =

nαζα, Z =

dim(ΩQα )=p

p

κ3n−6−pZp. (14)

Here Zp is independent of the temperature and potential, while Z combines everything to obtain the entire landscape. Note that lower dimensional manifolds have more bonds and thus are favored in the partition function when the temperature (or equivalently κ) is small. As temperature increases, κ shrinks and higher dimensional manifolds become more highly populated. Eventually clusters will fall apart into single particles. The temperature dependence of how clusters fall apart is encoded in the relative sizes of the Zp’s. The temperature where the landscape transitions from having more p dimensional structures than p+1 dimensional structures is found by solving κZp = Zp+1 for κ, which gives roughly (kBTp)−1 ≈ lnZp+1/Zp + const.

Free energy landscape for identical particles

To illustrate our asymptotic calculations with a concrete example we have computed the geometrical manifolds up to dimension p = 2 for n = 5,6,7,8 identical particles with diameter d = 1. To do this, we begin the set of clusters with ≥ 3n − 6 bonds derived in Arkus et. al. [38] For every rigid cluster we break each single bond in turn and move along the internal degree of freedom until we form another bond. This is the set of one-dimensional manifolds. For the two dimensional manifolds, we break each pair of bonds from the rigid clusters in turn, and move along the internal degrees of freedom to compute the boundaries, corners, and interior of the two-dimensional manifolds (see Appendix for details.) This algorithm ensures we have every ﬂoppy manifold that can eventually access one of the rigid clusters in our list only by forming bonds, but never breaking them. Our analysis makes three assumptions that we believe to be true, but await rigorous proof: First, we are assuming that the list of clusters in Arkus et. al. [38] is the complete set of rigid (0-dimensional) clusters; this is true as long as there are no rigid clusters with 3n − 7 bonds or less, a condition that was not checked [44]. Secondly, in the calculations of the entropy of the two dimensional ﬂoppy manifolds we assume that the manifolds are topologically equivalent to a disk. The fact that our parameterization algorithm works is evidence for this claim,

TABLE I. Geometric partition functions Zp, and numbers of diﬀerent modes, for the set of p = 0, 1, 2-dimensional manifolds

- as the number of spheres n varies. These are geometrical quantities that do not depend on the temperature or potential. The total partition function of the p-dimensional manifolds, which includes both of these dependencies via κ, is κmZp. n # 0-D # 1-D # 2-D Z0 Z1 Z2 Z1/Z0 Z2/Z1

- 5 1 2 4 10.7 73.8 545 6.9 7.4
- 6 2 5 13 36.1 256 1140 7.1 4.5
- 7 5 16 51 1.1×103 8.5×103 39 × 103 7.6 4.6
- 8 13 75 281 49×103 396×103 1.87×106 8.1 4.7


though we have not proved this rigorously. Thirdly, we assume that all ﬂoppy manifolds can eventually access a rigid mode and are not, for example, circles. We mention these caveats because although we are conﬁdent that they do not apply in the low n examples described here, it is possible that potentially signiﬁcant exceptions arise

- at higher n. The landscape for n = 6 is shown [45] in Figure 2.


as a corner.

Table 1 summarizes the partition function data. The number of diﬀerent modes increases combinatorially with n, as do the geometrical partition functions Zp. Strikingly, the ratios Z1/Z0, Z2/Z1 remain virtually constant as n increases. This implies that the temperature dependence of the landscape is independent of n. Indeed, Figure 4 shows the relative probabilities of 0,1,2-dimensional modes as the temperature varies, for n = 6,7,8, with the yield of a p-dimensional mode given by yp = κ2−pZp/(κ2Z0 + κZ1 + Z2). As an illustration, we have chosen U0/kB = −4, (U (0)/kB)(2/π) = 15, so that κ(T) = e4/T/ 15/T. Because the ratios Zp+1/Zp are nearly the same, these graphs are essentially indistinguishable for diﬀerent numbers of particles. Moreover the critical temperature for transitioning from mostly 0 dimensional structures to 1 dimensional structures (≈ 1/lnZ1/Z0) is quite close to that for transitioning from 1 dimensional structures to 2 dimensional structures (≈ 1/lnZ2/Z1). If this remains true as p increases, it would imply that clusters melt explosively at some critical temperature, rather than incrementally: clusters would occupy either mostly the 0-dimensional modes, or a gaseous, no- or few-bond-state, but not the chain-like ﬂoppy conﬁgurations in between.

There are two ground states, denoted by the red circles, each with 3n − 6 = 12 contacts; the area of the red circles are proportional to the probability of each state, with the polytetrahedral ground state ≈ 25 times more likely than the octahedral. The light blue circles denote the 5 topologically unique structures that are missing a single bond in the ground states – such structures correspond to a one dimensional manifold, with continuous deformation along the direction of the missing bonds. The yellow circles denote the 13 unique structures that are missing two bonds from the ground state. Again, the area of the circles is proportional to the occurrence probability of these modes. These structures correspond to two dimensional manifolds, with continuous deformations allowed along both of the directions between the missing bonds. The connections between the diﬀerent modes are denoted by arrows on this ﬁgure, with structures missing (say) 2 bonds generally arising from breaking a single bond from several diﬀerent pathways.

Each element of a mode with two bonds broken can be mapped to a polygon in R2, and these parameterizations are also shown in Figure 2. We have chosen one parameterization (mode 18), to illustrate in detail in Figure 3. The interior of the manifold represents structures with 10 bonds, with each point representing a diﬀerent set of coordinates for the particles. The edges correspond to structures with 11 bonds, while the corners are structures with a full 3n − 6 = 12 bonds. Of the four corners, three correspond to polytetrahedra with diﬀerent permutations of the particles, and the ﬁnal one is an octahedron. The one-dimensional edges connecting the corners are possible transition paths that can be followed by breaking only one bond.

#### KINETICS ON THE GEOMETRICAL LANDSCAPE

We now consider kinetics on the geometrical landscape. The concentration of equilibrium probabilities on manifolds with varying dimensions also applies to non-equilibrium quantities, such as transition rates, ﬁrst-passage times, the evolution of probability density, etc. Such quantities can be computed from the timedependent transition probabilities, which for dynamics given by (2) are obtained from the corresponding forward or backward Fokker-Planck (FP) equations [46]. We show that in the geometrical limit, the FP equation asymptotically approaches a hierarchy of FP equations, one on each manifold of each dimension. These equations are coupled to each other, with equations on manifolds with dimension p serving as boundary conditions for the equations on manifolds with dimension p + 1.

In general the number of corners varies among modes, with no a priori way to determine this without solving the full geometry problem. It ranges from 3–6 for n = 6,7, and from 3–7 for n = 8. Many 2-dimensional modes contain several permutations of a given 0-dimensional mode

The idea behind the derivation is quite natural: if a

potential is deep and narrow, then it equilibrates much more rapidly in the directions along the bonds than along a cluster’s internal degrees of freedom. Therefore the probability density near a cluster with p bonds broken is approximately p(y,t)e−β i U (Yαi), where y parameterizes the internal degrees of freedom of the cluster. The “constant” p(y,t) evolves slowly in the transverse directions according to the Fokker-Planck dynamics (which includes an “eﬀective” potential that arises from the curvature of the manifold), and it also changes due to the ﬂux of probability out of the p+1-dimensional manifolds for which it forms part of their boundary. This gives a hierarchy of coupled FP equations.

To see how this comes about in detail, we examine solutions to the Fokker-Plank equation for the evolution of the probability density p (x,t). Given a parameterization of conﬁguration space R3n with metric tensor g, the non-dimensional Fokker Plank equation corresponding to (2) is

∂tp = div (p grad U + grad p )

1

∂i |g| p gij∂jU + gij∂jp , (15) with boundary conditions at each level set {yi(x) = 0} (p grad U + grad p )·nˆ(i) = p gij∂jU + gij∂jp n ˆ(ji) = 0

=

|g|

where nˆ(i) is the outward normal to the boundary. We have non-dimensionalized lengths by d, times by d2/D, and energy by kBT. Away from all boundaries there is no force, so in Ω0 the limiting probability p evolves only by diﬀusion as

∂tp = − div j0, with j0 = − grad p. (16)

Now consider the evolution near a manifold Ωα, a “wall”. The dynamics in the directions orthogonal to the wall, where bond distances are changing, are much faster than those along it, so near the wall the probability density will rapidly approach a multiple of the equilibrium probability. Parameterizing the region Ω α near the wall as (yα

### ,y) as in the previous section, we obtain p (yα

i

m

m

,y,t) = p(0,y,t)e−

i=1 U (yαi)+ p1e−

i=1 U (yαi),

i

### (17) where  p1(y,yα

,t) is the correction to the leading order formula. This satisﬁes the matching condition that p be asymptotically continuous. This ansatz can also be derived from a consistent asymptotic expansion of (15) after the change of variables Yα

i

### = yα

/ .

i

i

Substituting (17) into the Fokker-Planck equation (15) gives

∂t e−U p = div e−U grad p + O( ). (18)

We would like to to integrate out the fast variables so we need to separate these from the slow ones. This is

most conveniently done using the metric g with block decomposition (10). Making the change of variables Yi = yα

/  shows that (A.36) can be written as

i

- 1

- 2∂a |g|e−U


∂t |g|e−U

gab∂b(p +  p1)

(p + p1) =

α

α

1

∂a |g|e−U

gav∂v(p +  p1)

+

α

1

∂u |g|e−U

gub∂b(p +  p1)

+

α

+ ∂u |g|e−U

guv∂v(p +  p1) . (19) where we abbreviate Uα = mi=1 C U(Yi).

α

We now integrate (19) over the fast variables

mdY1dY2 ...dYm and keep the leading-order parts. The terms ∝ 1 vanish in the limit because gav|Y =0 = gub|Y =0 = 0. The O(1) terms require evaluating an integral similar to (9) which converts |g|e−U

to the factor |guv|κmhα at each point on the manifold.

α

The ﬁrst term is the most interesting. This is the divergence in the fast variables, and although p does not depend on these, the unknown p1 might and contributes at O( −1). However, we can use the divergence theorem to replace this term with an integral of the ﬂux through the p-dimensional fast-variable boundary, at {x : Yi(x) = rc}. We then introduce a second matching condition which requires the ﬂux to be continuous, so we can replace it with the sum of ﬂuxes from each p + 1-dimensional manifold Ωβ which has Ωα as part of its boundary, [47] and evaluate the limit of the boundary integral for these matched ﬂuxes.

Finally, we integrate over the space of rotations and translations of each point, assuming p(x,0) is constant on orbits. The divergence in these directions will disappear by Stokes’ theorem, and the remaining directions provide dynamics on the quotient space. Combining with the previous calculations, yields

1 |g¯uv|

∂u |g¯uv|καg¯uv∂vp +

jβ ·nˆβα

∂t(καp) =

β→α

jβ · nˆβα (20)

= divα (κα gradα p) +

β→α

where the ﬂuxes have leading order part

jα = −κα gradα p on ΩQα. (21) Here κα ≡ κmhαI combines the sticky parameter and the geometric factor at the wall, and the metric tensor g¯ is the quotient metric obtained from the metric gα on ΩQα, which in turn is inherited from the original metric g in the ambient space by restriction: gα = g|Y1=...=Ym=0. The sum is over β such that ΩQα is part of the boundary of the p + 1-dimensional manifold ΩQβ , and where nˆβα is an outward normal vector to ΩQβ at ΩQα. We deﬁne divα , gradα to be the diﬀerential operators on the quotient manifold ΩQα.

Equation (20) has a more intuitive interpretation as the evolution of the probability along the wall. It is clear from the derivation that the total probability density (with respect to the wall coordinates) of being on the wall is Pα ≡ καp. This satisﬁes

bonds, then diﬀuse across the line segment (or face, etc) until it hits the other endpoint. The time it takes to do this depends on the length of the line and on how the entropy of the conﬁguration varies along the line, and we can ﬁnd this by solving an equation on the full line segment (face, etc). In our asymptotic limit there are no meaningful transition “states” – rather, the entire line segment can be thought of as a transition state. Once the energetic barrier of breaking a bond has been overcome, transitions are dominated by diﬀusion.

∂tPα = 1

∂u |g¯uv|(−Pαg¯uv∂v log κα + g¯uv∂vPα) +jβ·nˆβα

|g¯uv|

 −Pα gradα log κα

 + jβ · nˆβα

We now consider how to compute transition rates using the sticky equations (20), supposing we have a stochastic process X(t) whose probability evolution is wellapproximated by these.[49] Consider the transition rate between sets A ⊂ Ω, B ⊂ Ω, and for simplicity let us focus only on the case where these are both (disjoint) subsets of the 0-dimensional manifolds. For example, we may be interested in the transition rate between the octahedron and the polytetrahedron (introduced in Figure 1), in which case A would contain all points in the quotient space representing the octahedron, and B all those representing the polytetrahedron. These rates can be computed using Transition Path Theory, which provides a mathematical framework for computing transition rates directly from the Fokker-Planck equations. We will simply state the facts that are relevant to our example and refer the reader to other resources for more details [50– 52]).

= divα

### + gradα Pα

.

eﬀective force

diﬀusion

ﬂux to/from wall

(22)

The dynamics along the wall is therefore a combination of diﬀusion, plus drift due to an “eﬀective” potential −log κα, plus a ﬂux in and out of the wall.

The eﬀective potential is entropic in nature and comes from the changing wall curvature, which makes the potential look wider in some places than others. A particle will spend more time in the wide places than in the narrow ones, and since it reaches equilibrium much more quickly in the transverse directions than in the along-wall directions, it looks like there is an eﬀective force pushing it to the wider areas. This is the same equation one obtains by letting the depth of the potential become inﬁnite without changing the width [41], but with the addition of the ﬂux in and out of the wall.

The committor function q(x) is the probability, starting from point x, of reaching set B before set A. This solves the stationary backward Fokker-Planck equations with boundary conditions q(A) = 0, q(B) = 1, plus any other boundary conditions remaining from the equations. As shown in the Appendix, the forward sticky equations (20) are self-adjoint (with respect to the invariant measure) so these are also the backward sticky equations.

This ﬂux term is illustrated schematically in Figure 5 for a simple case where the conﬁguration space (x,y) ∈ R2 has a single constraint, y1(x,y) = x – a “wall” at the horizontal axis. The probability integrated over a small box (red) with length ∆x near the wall changes in a time increment ∆t due to two processes: probability ﬂuxing along the wall in the x-coordinate, which contributes a change of ∆t(px(x+∆x,t)−px(x,t)) e−U(y)dy, and the ﬂux of probability from the wall to the interior, which contributes a change of ∆t∆xpy(x,0,t). Equating with ∆tpt(x,t) e−U(y)dy gives the eﬀective boundary condition.

A reactive trajectory is a segment of the path X(t) that hits B before A going forward in time, and A before B going backward in time. The probability current of reactive trajectories is a vector ﬁeld that, when integrated over a surface element, gives the net ﬂux of reactive trajectories through it. Because our process is time-reversible, this current is [51]

To summarize, the limiting FP equation and boundary conditions are (16), plus (20) on every ΩQα. Substituting for the time derivatives shows that the boundary conditions are second-order, and this is why conditions are needed on every boundary and not only those with codimension 1. We call this set of equations the “sticky” equations because it is the Fokker-Planck equation for Sticky Brownian Motion [48], a stochastic process that has a probability atom on the boundary of its domain.

J(x) = ρ(x)∇q(x), (23) where ρ(x) is the equilibrium probability measure. From

(13) we ﬁnd this is ρ(x) = Z−1

κα(x)δα(x), (24)

α

#### TRANSITION RATES FOR STICKY BROWNIAN MOTION

To transition between the rigid conﬁgurations in the geometrical limit, a cluster must break one (or more)

where δα(x) is the singular measure on Ωα, i.e. it satisﬁes Ω f(x)δα(x) = Ω

f(x). Finally, the transition rate kAB is calculated by integrating this ﬂux over a surface S dividing the two states, giving

α

kAB =

J · nˆ dS, (25)

S

where nˆ is the normal pointing from the side containing A into the side containing B.

Computing this exactly requires solving the backward equations on a high-dimensional space, and integrating over a high-dimensional surface – a computationally infeasible proposition. However, when the sticky parameter κ is large, most of the probability is concentrated on the lowest-dimensional manifolds so we expect these to contribute the most to the rates. Therefore, let us expand the equations in powers of κ−1. We suppose all variables have an asymptotic expansion as

kAB = k0AB + κ−1k1AB + ..., (26)

and similarly for q, µ, ρ, J, etc. Expanding ρ shows that to ﬁrst order it is a measure on points, to second order it is a measure on points and lines, etc. Measures on points will not contribute to the rate because the dividing surface S can be chosen to avoid them, so k0AB = 0 and the leading-order part of the rate is O(κ−1), computed from ρ1∇q0.

Expanding the backward sticky equations in powers of κ−1 gives a set of equations for q0:

divα hαI gradα q0 = 0 on Ωα (p > 0), (27)

with boundary conditions q0(A) = 0, q0(B) = 1, and

β→α(hβI gradβ q0)·nˆβα = 0 on all other 0-dimensional manifolds.

To solve these equations we can ﬁrst ﬁnd the solution on the 0- and 1-dimensional manifolds, then use this as a boundary condition for the solution on the 2-dimensional manifolds, which becomes in turn a boundary condition for the solution on 3-dimensional manifolds, etc. The leading-order rate requires only the solution for p = 0,1. If we enumerate the lines connecting a point ak ∈ A to a point bk ∈ B and use an arc-length parameterization for the kth line whose total length is sk, then this given analytically as q0(s) = Q−k 1 s s=0 (hα(s )I(s ))−1 ds , where

Qk =

sk

(hα(s )I(s ))−1 ds (28)

s=0

is the normalization factor. On all other lines q0(s) = 0.

Any dividing surface S hits each line at a single point, so the leading-order rate (in dimensional units) is

kAB = κ−1k1AB = κ−1

D d2

Z0−1

k

Q−k 1, (29)

where the sum is over all connecting lines. This is asymptotically equivalent to the rate one would obtain simply by restricting the full committor function and invariant measure to the set of 0- and 1-dimensional manifolds.

Transition Rates for hard spheres

We used the formalism to compute the leading-order rates for n = 6,7,8 hard spheres with diameter d = 1. To do this we took the set of 1-dimensional solutions computed as part of the free energy landscape, and computed the factor Qk from (29) on each manifold. Summing over all of the 1-dimensional manifolds that connect

- a 0-dimensional manifold numbered a to a 0-dimensional mode numbered b, gives the transition rate between a,
- b. We also include transitions between diﬀerent ground states belonging to the same mode (e.g. a → a), by multiplying the previous calculation by 2 since transitions can go in either direction along the line.


- Figure 6 shows shows the network of 0-dimensional

states and the reaction rates between each state. The numbers reported are the dimensionless, purely geometrical parts of the rates Z0−1 k Q−k 1, and should be multiplied by κ−1D/d2 to give the dimensional rate. These rates, when multiplied by the total time of a simulation or experiment, give the average number of transitions one would expect to observe, so they are equal for both directions a → b and b → a since our system is time-reversible. To obtain the rate relative to a particular state, i.e. the rate at which one leaves state a to visit state b next, given that the last state visited was state a, one should divide by the so-called reactive probability of a [53]. To leading order, this is equivalent to dividing by the equilibrium probability of a.

Simulations We have veriﬁed our results by performing Brownian dynamics simulations of (2) with a shortrange Morse potential. The results agree very well with our calculations of both free energy and transition rates.

- Figure 7 shows a comparison of the simulated probabilities versus theoretical probabilities of each mode for n = 6 (see SM for n = 7,8), for particles interacting with a Morse potential with range parameter ρ = 30, a range of ≈ 5% of the particle diameter. The agreement is nearly perfect. Fig. 7 also compares the number of each type of transition we saw in the simulations, to that predicted from theory. The theory slightly overpredicts the total number of transitions – this is what one should expect from the geometrical picture, as these leading-order rates neglect the time the system spends in the ﬂoppy manifolds, which would tend to slow it down.


These results are encouraging partly because they are evidence that we have executed these calculations correctly, but also because they suggest the asymptotic limit may apply for experimental systems, such as Meng et. al. [4] where the potential reportedly had roughly this width.

Comparison with other numerical approaches to the free energy landscape

We have compared our results with those obtained by a numerical study that directly searched an energy landscape of a short-ranged potential (a Morse potential, with range roughly 0.05 particle diameters) for local minima and transition states [42]. The numerical method found fewer local minima than there are 0-dimensional modes, and fewer transition states than 1-dimensional modes, suggesting that the asymptotic theory has the roughest landscape. By computing adjacency matrices for the numerical states with a cutoﬀ bond distance of 1 + 1×10−2, we verify that for n = 6,7,8 each local minimum corresponds to a unique 0-dimensional mode, and each transition state lies on a unique 1-dimensional manifold.

We identify the point on the 1-dimensional manifold that is closest to each transition state. The transition states are very close to the local maxima of the vibrational factor −log h(x) (see Appendix for plot), consistent with it being a saddle point of the potential energy. We believe the small discrepancy in location can be attributed to the ﬁnite width of the Morse potential used in the numerical procedure.

- The missing 0-dimensional modes occur for manifolds

that are very close to each other in the quotient space metric (separation ≈ 0.08), which is the case for modes {1,4} (n = 7) and modes {1,2,3,4} (n = 8). For these only one local minimum was found for the entire group. We hypothesize that because the separation is within the range of the potential, the 0-dimensional modes merge to form a single local minimum.

- The missing 1-dimensional modes often, but not al-


ways, correspond to self-self transitions – these transitions do not matter when particles are identical, however they will account for transitions between diﬀerent states when the particles are not all the same (e.g. [54]). For example, for n = 8 the numerical procedure identiﬁes 45 transition states, compared to our 75 one-dimensional manifolds. Of the missing manifolds, 16 are self-self transitions, 9 are nonself-nonself transitions within the group {1,2,3,4}, and 5 are nonself-nonself for endpoints not both in the group.

#### DISCUSSION / CONCLUSIONS

We have developed a new framework for understanding energy landscapes when particles interact with a shortranged potential. We show that in the limit as the range goes to zero and the depth goes to −∞, the energy landscape becomes entirely governed by geometry, with a single parameter κ encapsulating details about the potential and temperature. When κ is large, only the lowest-dimensional geometrical manifolds contribute signiﬁcantly to the landscape and this makes a computa-

tional approach tractable. To illustrate the limit, we have computed the set of low-dimensional manifolds for n ≤ 8 hard, spherical particles. This solution to a nontrivial problem in statistical mechanics can be used to compute equilibrium or non-equilibrium quantities for any potential whose range is short enough.

We were able to calculate this set of low-dimensional manifolds because we began with the set of rigid clusters, and made the conjecture that all ﬂoppy modes can be accessed from these by breaking bond constraints. Solving for the complete set of rigid clusters is a diﬃcult problem in discrete geometry that has only been done for n ≤ 11 [38, 55], but with current computational power and novel approaches [55, 56] one can anticipate reaching larger n. Very large n will eventually require making approximations to the geometry problem. We speculate that as n increases, structures with extra bonds, as well as “singular” structures whose Jacobians have extra zero eigenvalues, will come to dominate the landscape – these have not yet been considered in our asymptotic framework but they are observed with high probability in experiments [4].

We have compared our results to those obtained by numerically searching the free energy landscape of a shortranged Morse potential for local minima and transition states. Our method ﬁnds more minima and transition regions of the potential energy than the numerical search procedure, and this points to a potentially useful extension of our theory – one can imagine starting with the limiting geometrical manifolds, and following these in some way as the range of the potential is increased, to obtain a low-dimensional approximation to the free energy landscape for ﬁnite-width potentials, such as Lennard-Jones or Van der Waals clusters. This method would overcome a major issue with numerical searches which is that there is no way to ensure that all important parts of the landscape has been found – we claim that our manifolds are the complete set of low-energy states so they will remain so under small enough perturbations. In addition, this would provide a way to deal with the increasing ruggedness of energy landscapes with short-ranged potentials, which are a challenge for numerical methods – we start with the most rugged landscape and would only need to smooth it.

We thank David Wales for generously providing data, and Vinothan Manoharan and Eric Vanden-Eijnden for helpful discussions. This research was funded by the National Science Foundation through the Harvard Materials Research Science and Engineering Center (DMR0820484), the Division of Mathematical Sciences (DMS0907985) and the Kavli Institute for Bionano Science and Techology at Harvard University.

———————————————————–

- [1] D. J. Wales, Energy Landscapes (Cambridge University Press, 2003)
- [2] F. Stillinger and T. Weber, Science 225 (1984)
- [3] A. Beberg and V. S. Pande, IEEE International Symposium on Parallel & Distributed Processing(2009)
- [4] G. Meng, N. Arkus, M. Brenner, and V. Manoharan, Science 327, 560 (Jan. 2010)
- [5] G. Bowman and V. Pande, Proc. Natl. Acad. Sci. 107

(2010)

- [6] J. P. K. Doye and D. J. Wales, Science 271 (1996)
- [7] F. Stillinger, Science 267 (1995)
- [8] J. Onuchic, Z. Luthey-Schulten, and P. G. Wolynes, Annu. Rev. Phys. Chem. 48, 545 (1997)
- [9] A. Liwo, J. Lee, D. Ripoll, J. Pillardy, and H. Scheraga, Proc. Natl. Acad. Sci. 96, 5482 (1999)
- [10] P. G. Wolynes, Q. Rev. Biophys. 38, 405 (2005)
- [11] P. Rothemund, Nature 440, 297 (2006)
- [12] C. Clementi, Curr. Opin. Struct. Biol. 18, 10 (2008)
- [13] L. Maragliano, G. Cottone, G. Ciccotti, and E. VandenEijnden, J. Am. Chem. Soc. 132, 1010 (2010)
- [14] R. Swendsen and J. Wang, Phys. Rev. Lett. 57 (1986)
- [15] R. Elber and M. Karplus, Chem. Phys. Lett. 139 (1987)
- [16] W. E, W. Ren, and E. Vanden-Eijnden, Phys. Rev. B 66

(2002)

- [17] P. G. Bolhuis, D. Chandler, C. Dellago, and P. L. Geissler, Annu. Rev. Phys. Chem. 53, 291 (2002)
- [18] G. Hummer, J. Chem. Phys. 516 (2004)
- [19] C. Abrams and E. Vanden-Eijnden, Proc. Natl. Acad. Sci. 107, 4961 (2010)
- [20] D. J. Wales and H. Scheraga, Science 285 (1999)
- [21] J. M. Carr, S. A. Trygubenko, and D. J. Wales, J. Chem. Phys. 122 (2005)
- [22] D. J. Wales, Int. Rev. Phys. Chem. 25, 237 (2006)
- [23] G. Henkelman, B. Uberuaga, and H. Jonsson, J. Chem. Phys. 113 (2000)
- [24] R. Noe, C. Shutte, E. Vanden-Eijnden, L. Reich, and T. Weikl, PNAS 106 (2009)
- [25] M. Hagen, E. Jeijer, G. Mooij, D. Frenekl, and H. Lekkerkerker, Nature 365 (1993)
- [26] J. P. K. Doye and D. J. Wales, Chem. Phys. Lett. 262, 167 (1996)
- [27] R. F. P. S. D. Gazzillo, A. Giacometti, Phys. Rev. E 74

(2006)

- [28] R. Dreyfus, M. Leunissen, R. Sha, A. Tkachenko, N. Seeman, D. Pine, and P. Chaikin, Phys. Rev. Lett. 102

(2009)

- [29] R. Macfarlane, B. Lee, M. Jones, N. Harris, G. Schatz, and C. Mirkin, Science 334 (2011)
- [30] W. B. Rogers and J. C. Crocker, PNAS 108 (2011)
- [31] R. Baxter, J. Chem. Phys. 49 (1968)
- [32] G. Stell, J. Stat. Phys. 63 (1991)
- [33] M. Miller and D. Frenkel, Phys. Rev. Lett. 90 (2003)
- [34] D. Gazzillo and A. Giacometti, J. Chem. Phys. 120

(2004)

- [35] A. Malins, S. Williams, J. Eggers, and H. T. dn C. P. Royall, J. Phs. Condens. Matter 21, 1 (2009)
- [36] D. J. Wales, Chem. Phys. Chem. 11, 2491 (2010)
- [37] N. Arkus, V. Manoharan, and M. Brenner, Phys. Rev. Lett. 103 (2009)
- [38] N. Arkus, V. Manoharan, and M. Brenner, SIAM J. Disc. Math. 25, 1860 (2011)


- [39] M. P. Allen and D. J. Tildesley, Computer simulation of liquids (Oxford University Press, 1989)
- [40] L. D. Landau and E. M. Lifshitz, Statistical Physics, Course of Theoretical Physics, Vol. 5 (Pergamon Press, 1978)
- [41] I. Fatkullin, G. Kovacic, and E. Vanden-Eijnden, Communications In Mathematical Sciences 8, 439 (Jun. 2010)
- [42] F. Calvo, J. P. K. Doye, and D. J. Wales, Nanoscale 4, 1085 (2012)
- [43] This is a combinatorial argument; it is equivalent to considering the molecular symmetry group for nonrigid molecules as in [1], Section 3.4.
- [44] The existence of such pathological examples is not ruled out purely by rank constraints on the Jacobian as there could be singular structures, see e.g. the examples in Asimow & Roth (1978) “The rigidity of graphs”, Trans. Amer. Math. Soc. 245:279–289.
- [45] Quantitative summaries are given in Table III and Figure 11 in the Appendix.
- [46] C. Gardiner, Stochastic Methods: A handbook for the natural and social sciences, 4th ed. (Springer (Berlin), 2009)
- [47] Speciﬁcally, we require that ˜jα · nˆrc|Yi=rc = ˜jβ ·

nˆ(i)|yαi=0, where nˆrc is the normal to level set Yi = rc and nˆ(i) is the normal to level set yi = 0, and ˜jα = −e−Uαgab∂b(p +  p1) with a similar expression for ˜jβ.

- [48] N. Ikeda and S. Watanabe, Stochastic Diﬀerential Equations and Diﬀusion Processes (Elsevier, 1981)
- [49] Note that we have not actually constructed a process that satisﬁes this in the strong sense. However, we began with a process satisfying (2) and showed the sticky equations describe its probability evolution asymptotically so we use these to compute rates.
- [50] P. Metzner, C. Schuette, and E. Vanden-Eijnden, Journal of Chemical Physics 125 (Aug. 2006), doi:“bibinfo doi DOI 10.1063/1.2335447
- [51] E. Vanden-Eijnden, Lect. Note Phys 703, 453 (2006)
- [52] W. E and E. Vanden-Eijnden, Annual Review of Physical Chemistry 61 (2010)
- [53] C. Schutte, F. Noe, J. Lu, M. Sarich, and E. VandenEijnden, J. Chem. Phys. 134 (2011)
- [54] S. Hormoz and M. Brenner, Proc. Natl. Acad. Sci. 108, 19885 (2011)
- [55] R. Hoy, J. Harwayne-Gidansky, and C. O’Hern, Phys. Rev. E 85 (2012)
- [56] A. Sommese and C. Wampler, Numerical solution of polynomial systems arising in engineering and science (World Scientiﬁc, 2005)
- [57] J. W. Bruce and P. J. Giblin, Curves and singularities, 2nd ed. (Cambridge University Press, 1984)
- [58] J. M. Lee, Manifolds and Diﬀerential Geometry, Graduate Studies in Mathematics, Vol. 107 (AMS, 2009)
- [59] K. J. Falconer, J. London Math. Soc. 27, 356 (1983)
- [60] G. S. Katzenberger, The Annals of Probability 19, 1587

(1991)

- [61] S. Gallot, D. Hulin, and J. Lafontaine, Riemannian Geometry, 3rd ed. (Springer, 2004)
- [62] R. Abraham and J. Marsden, Foundations of Mechanics, 2nd ed. (Addison-Wesley, 1987)
- [63] J. P. Sethna, Statistical mechanics: entropy, order parameters, and complexity, Vol. 14 (Oxford University Press, 2006)
- [64] If we were to construct a stochastic process Xt with Fokker-Planck equation (20) and with initial condition


- X0 = x, then we would be able to write u(x, t) = Eg(Xt). Unfortunately we are only aware of such constructions for processes that have singular measures on manifolds of co-dimension 1 [48], and not processes that are sticky on manifolds of several diﬀerent dimensions simultaneously, so we focus instead on the PDE interpretation.
- [65] G. Ciccotti, T. Lilievre, and E. Vanden-Eijnden, Commun. Pure Appl. Math. 61, 0001 (2008)
- [66] M. Floater and M. Riemers, Computer aided geometric design 18, 77 (2001)
- [67] M. Floater and K. Hormann, Computer aided geometric design 14, 231 (1997)
- [68] P. Persson and G. Strang, SIAM Review 46, 329 (2004)
- [69] V. de Silva and G. Carlsson, in Proc. Sympos. PointBased Graph. (2004) pp. 157–166
- [70] D. Field, International Journal for numerical methods in engineering 47, 887 (2000)
- [71]


![image 1](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile1.png>)

FIG. 1. Top: schematic of a traditional depiction of an energy landscape. Local minima are separated by energy barriers (red line) that govern the transition rate from one basin to another. Middle: schematic of a geometrical energy landscape, showing the 0- and 1–dimensional sets. Local minima are inﬁnitesimally narrow, deep points, separated by long, nearly ﬂat lines. Along these the dynamics is governed mainly by diﬀusion, so the length of the line (in red) determines the transition rate. Bottom: Example of a 1-dimensional manifold from the landscape for n = 6, showing the transition path from polytetrahedron (left) to octahedron (right). Black line is the free energy Fα/kBT = − log nαhαI −11 log κ along the 1-dimensional manifold in units of kBT, where we chose κ = 20. Black dots are the free energy Fα/kBT = − log nαhαI − 12 log κ for the 0-dimensional endpoints. Red crosses mark locations of clusters that are plotted explicitly (they are plotted with 1/2 their actual diameter for clarity), and the horizontal axis is a parameterization of the manifold in the quotient-space distance s.

![image 2](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile2.png>)

- FIG. 2. Free energy landscape for n=6 with 0, 1, and 2 bonds broken. Red circles are 0-dimensional modes, blue are 1-


dimensional, yellow are 2-dimensional. The area of each circle is proportional to the geometrical partition function nαζα of each mode, hence to its probability in equilibrium relative to modes of the same dimension. Modes are identiﬁed by numbers and arrows show the connectivity: an arrow from mode i to mode j indicates that mode i is part of the boundary of mode j. The number on each arrow indicates the number of diﬀerent manifolds of type j that are connected to a single manifold of type i. The computed parameterizations are shown for each of the 2-dimensional modes.

![image 3](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile3.png>)

- FIG. 3. A two-dimensional manifold (mode 18, n = 6), parameterized in the plane, with selected points on the manifold plotted as clusters. The vertex of each triangle represents a cluster and black or red dots indicate the ones that are plotted. The corners (black dots) are rigid structures, or 0-dimensional manifolds. The edges are 1-dimensional manifolds and points on these are obtained from rigid structures by breaking one bond, while points in the interior form a


- 2-dimensional manifold and are obtained by breaking two bonds. The 1-dimensional manifolds, beginning at the octahedron (left) and moving clockwise, are 7,5,5,7. The text indicates the type of bond that breaks or forms as one moves along each edge.


![image 4](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile4.png>)

- FIG. 4. Relative yields of 0-dimensional, 1-dimensional, 2-dimenisional modes (neglecting all higher-dimensional modes) for n = 6, 7, 8. The yield for p-dimensional modes is calculated as yp = κ2−pZp/(κ2Z0 + κZ1 + Z2) with κ(T) =


e−(U0/kB)/T/ (U (0)/kB)(2/π)/T. We used U0/kB = −4, (U (0)/kB)(2/π) = 15, but the numbers don’t change the qualitative shape. Note that modes with dimensions > 2 will become important at the higher temperatures.

![image 5](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile5.png>)

- FIG. 5. Schematic showing the asymptotic boundary condition near a one-dimensional boundary. On the left, grey shading indicates the depth of the potential, and dashed line indicates the boundary at which the outer and inner solutions. By considering the total probability ﬂux in/out of each small volume element near the boundary (red box), one can replace the detailed dynamics near the boundary in the limit as  rc → 0 with an eﬀective boundary condition (right).


![image 6](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile6.png>)

##### FIG. 6. Rates (geometrical components) at leading-order, for n = 6, 7, 8. Dimensional rates are κ−1D/d2 times the above. These rates indicate the total number of each type of transition one expects to see, per unit time.

Theoretical counts Mode 1 2

- 1 1570 ± 78 153 ± 24
- 2 153 ± 24 0


Simulation counts Mode 1 2

- 1 1256 124
- 2 124 0


![image 7](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile7.png>)

![image 8](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile8.png>)

- FIG. 7. Figures: Theoretical probabilities of each mode (relative to modes of the same dimension), versus probabilities computed from simulations using a potential with width ≈ 5% of particle diameter, for n = 6. The red line is Theory=Simulation indicating a perfect match. Tables: number of transitions of each type, for simulation and theoretical prediction. The theoretical prediction indicates expected 95% conﬁdence intervals, computed using a normal approximation to a binomial. The sticky parameter was κ = 16 and the total running time was 2.3 × 103 units.


Parameterization of a neighbourhood of Ωα

We provide a brief argument for the following statement made in the main text: given a regular point x ∈ Ωα, there exists a diﬀerentiable parameterization of a neighbourhood N(x) ⊂ R3n of the form y × {yα

i}mi=1, with y ∈ R3n−m, such that ∇y · ∇yα

= 0 on Ωα.

i

Recall that a regular point x ∈ Ωα is a point such that the Jacobian of the transformation x → (yα

(x)) has rank m. If x is regular then it has a neighbourhood Nα(x) ⊂ Ωα that is a diﬀerentiable manifold with co-dimension m [57, 58], so there exists a parameterization near x by y ∈ R3n−m; let the associated mapping be z : R3n−m → Ωα.

(x),...,yα

1

m

Given some point x ∈ Ω α (not necessarily on Ωα), we deﬁne a mapping x → (yα

(x ),y(x )), where y(x ) is found from the limit of the gradient ﬂow map, i.e. y(x ) = z−1(limt→∞ φ(t)) where φ solves dφ dt = −∇ i U(yα

,y) as (yα

i

i

(φ)), φ(0) = x . (We abbreviate yα

i

i

to mean the full list of constraint variables.) Results from [59] (see also [60]) show that this map exists and is smooth enough in a neighbourhood ⊂ Ω of x ∈ Ωα, provided Ωα is regular and U(y) is suﬃciently smooth. Since the mapping x → (yα

,y) has full rank at x ∈ Ω, it does also in a neighbourhood N(x) ⊂ Ω and so by the Inverse Function Theorem it is invertible. The orthogonality at Ωα follows because this is a level set of the constraints.

i

Note that while this provides the required parameterization in a neighbourhood of x ∈ Ωα, we have not shown that it extends to the set Ω α (see (7)). This is not a problem for the asymptotic calculations, as these remain valid if Ω α is replaced with an atlas of local parameterizations N(x), patched together with a partition of unity – the asymptotics only require the local behaviour near yα

= 0 and are not sensitive to the cutoﬀs at rc.

i

Quotient space metric and equations

In this section we give more details about the quotient space and metric structure on it, and show how these arise naturally from our equations. Although these facts are well-known in Riemannian geometry [58, 61] and wellused in chemistry and mechanics [40, 62, 63], we have not found a reference dealing succinctly with our particular context so we collect the relevant facts and demonstrations here.

The manifold structure on the quotient space Recall that we deﬁned the quotient space associated with a manifold Ωα to be ΩQα = Ωα/G, where the G = SE(3) is the Special Euclidean group, i.e. the group of rotations and translations of a cluster. Then ΩQα is a smooth manifold if the Lie group G acts properly and freely on Ωα ([62], Prop. 4.1.23 p.266, [61]). To act properly is a compactness condition and it can be checked that it is satisﬁed for SE(3). To act freely means that the only element

g ∈ G such that g · x = x is the identity. This is the case provided there is no cluster in Ωα such that the spheres all lie on a line; for ﬂoppy manifolds with up to two bonds broken this is true when n ≥ 5.

The orbit of a cluster x is the set of points of the form g · x for g ∈ G, and is written as [x]. Each orbit is identiﬁed as an element in ΩQα by the canonical projection

π : Ωα → Ωα/G := {[x] : x ∈ Ωα}. (A.30)

This projection shows how to map the tangent spaces to each other, via the pushforward map. Let Tα(x), TαQ([x]) be the tangent spaces at x ∈ Ωα, [x] ∈ ΩQα respectively. The tangent vectors map as follows: if c(t) ∈ Ωα is a curve such that c(0) = x, then the tangent vector c (0) ∈ Tα(x) maps to the tangent vector

d dtπ(c(t))|t=0 ∈ TαQ([x]). Note that tangent vectors can also be identiﬁed as derivations, which we will write as

∂u.

Metric on the quotient space The group G acts isometrically on Ωα, which means it respects the inner product  ·,· gα

on the manifold: given t1,t2 ∈ Tα(x), the inner product satisﬁes t1,t2 g

= g · t1,g · t2 g

for all g ∈ G. Therefore one can construct a metric on the quotient manifold that is compatible with the projection (making the projection a Riemannian submersion), and this metric is unique [61].

α

α

To specify the metric we decompose Tα(x) into the vertical subspace Tαv(x), containing the directions tangent to the action of G, and the horizontal subspace Tαh(x), its orthogonal complement. Therefore Tα(x) = Tαv(x)⊕Tαh(x).

Let Pα(x) : Tα → Tαh the the orthogonal projection operator (we omit the argument x for succinctness.) Let [t] denote an element of TαQ that has representative t ∈ Tα. The metric g¯α on the quotient space ΩQα is computed from the metric gα on Ωα as

=  Pαt1,Pαt2 g

[t1],[t2] gQ

α

α

. (A.31)

Fokker-Planck equations on the quotient space Next we show how this diﬀerential structure arises naturally as a result of our manipulations to the Fokker-Planck equation.

Consider a point x0 ∈ Ωα, and let us parameterize a neighbourhood on Ωα in such a way that at x0, the directions tangent to inﬁnitesimal rotations and translations are orthogonal to the remaining variables. This can be

done with the standard Euler angles. Let

- Rx(θ) =

 

1 0 0 0 cosθ −sinθ 0 sinθ cosθ

 

- Ry(θ) =

 

cosθ 0 sinθ 0 1 0

−sinθ 0 cosθ

 

- Rz(θ) =


 

 

cosθ −sinθ 0 sinθ cosθ 0

0 0 1

be the matrices for rotation of a point about the x,y,z axes respectively, with block-diagonal versions appropriate to a cluster of n particles Rx(θ), Ry(θ), Rz(θ). These are obtained as, for example,

  

  

Rx(θ)

...

Rx(θ) =

Rx(θ)

with n copies along the diagonal and zeros everywhere else, and similarly for the other matrices. Let

T(µ1,µ2,µ3) = (µ1,µ2,µ3,µ1,...,µ1,µ2,µ3)T

be a vector representing translations. Let φ(y) : Rp → R3n parameterize the remaining directions with φ(0) =

x0, so that a neighbourhood of x0 on Ωα can be parameterized with variables (θx,θy,θz,µ1,µ2,µ3,y) as

x = Rz(θz)Ry(θy)Rx(θx)φ(y) + T(µ1,µ2,µ3). (A.32)

We can choose φ(y) so that it is orthogonal to inﬁnitesimal rotations and translations at x0: this means that we require ∂y∂φ

k y=0· ∂R

∂θx θx=0x0 = 0 , for each yk and each rotation matrix; the condition for translations is satisﬁed if the center of mass of x0 is at the origin.

x

The metric tensor on Ωα is gα = JTJ where J is the Jacobian of the transformation (θx,θy,θz,µ1,µ2,µ3,y) → x. This has a simple block diagonal structure at x0:

 

  (A.33)

g¯α 0 0 0 I 0 0 0 I3

gα(x0) =

where

  i

 . (A.34)

yi2 + zi2 − i xiyi − i xizi

− i xiyi i x2i + zi2 − i −yizi − i xizi − i −yizi i x2i + yi2

I =

Here g¯α is the p×p contribution from the y-variables, I3 is the 3×3 identity matrix, and I is the moment of inertia tensor, which assumes the conﬁguration is written as x = (x1,y1,z1,...,xn,yn,zn). We will write its determinant

- as I2(x0) ≡ det(I). Therefore the Fokker-Planck equation on Ωα after in-

tegrating over the fast variables has the following form

- at x0:


1 |gα|

∂t(κmhαp) =

∂i |gα|κmhαgij∂jp +

β→α

1 |g¯α|I2

∂u |g¯α|I2κmhαg¯uv∂vp +

=

Here gij, guv are the elements of gα, g¯α respectively, a,b index the rotational and translational variables, and we have substituted (A.33) in the second equation. We will not deal with the ﬂux explicitly as this comes from the same manipulations on the higher-dimensional manifolds.

Integrating (A.35) over orbits gets rid of the second term on the RHS, by Stokes’ theorem, so we are left with

1 |g¯α|

jβ·nˆβα. (A.36)

∂u |g¯α|κmhαIg¯uv∂vp¯ +

- ∂t(κmhαIp¯) =


β→α

where p¯ is the integrated value of p on an orbit (this is Cp

jβ · nˆβα

1 |g¯α|I2

∂a |g¯α|I2κmhαgab∂bp +

jβ · nˆβα. (A.35)

β→α

if p is constant on the orbit, where the constant C does not depend on x0.) Because this does not depend on the location along the orbit of a point, we can identify it with a function on the quotient space as p¯(x,t) = p¯Q([x],t). For the same reason we can identify tangent vectors via the canonical projection as ∂up¯ = ∂[u]p¯Q. The metric g¯uv has the same elements as the quotient metric g¯[u][v] because it only involves tangent vectors in the horizontal subspace, and it is independent of the representative x0 that we chose for [x0] because G acts isometrically.

After identifying functions, tangent vectors, and the metric in (A.36) with their projections in the quotient space, we obtain (20) in the text.

Representing the quotient space To parameterize the quotient manifold it is convenient to map it to a space that has an explicit representation. For our numerical implementation we store the edge-lengths of all the particles (we call this “bond-distance” space.) This representation actually forms the quotient space with reﬂections as well, so it is only diﬀeomorphic to ΩQα if Ωα does not contain a cluster where all of the particles lie in a plane.

An alternate parameterization would be to constrain one vertex to be at the origin, one vertex to lie on the x-axis, and one vertex to lie on the xy-plane. This would embed ΩQα in Ωα.

Given a parameterization of the quotient manifold in some space B with canonical projection π, the tangent vectors and metric can be computed from the pushforward map (A.30) via numerical diﬀerentiation. That is, given a point [x] ∈ B with representative x ∈ Ωα where this is two-dimensional, we compute the two unit tangent vectors t1,t2 ∈ Tα(x) that are perpendicular to the inﬁnitesimal rotations and translations. This is easy to do from the null space of the matrix M deﬁned in section . We take small steps in each of these directions to obtain points x1 = x + ∆s t1, x2 = x + ∆s t2, project to B, and obtain ﬁrst-order estimates of the quotient tangent directions as [t1] = (π(x1) − x)/∆s, [t2] = (π(x2) − x)/∆s. These have lengths 1 and inner product t1,t2 g

, which deﬁnes the metric on B.

α

We use a ﬁrst-order scheme to ﬁnd the distance between two nearby points [x1],[x2] in B. We ﬁnd the separation vector v = [x1] − [x2], project this onto the tangent space at [x1] and ﬁnd the length of this projection. We repeat at the tangent space to [x2] and average the lengths.

Note that parameterizing the quotient manifold as a subset of Ωα would imply slightly diﬀerent numerical algorithms. For example, to ﬁnd the distance between two nearby points, one would simply project the separation vector v onto the horizontal tangent space at x1, x2 (these representatives can be chosen equal to [x1], [x2]) – this might be more eﬃcient than the bond-distance space method.

Adjoint equations

In this section we compute the backward FokkerPlanck equation associated with (20). We could derive

this using the same asymptotic procedure on the backward equation associated with (2), however we prefer to demonstrate how to convert between the forward and backward sticky equations directly. We only outline the arguments here, leaving several steps to the reader.

Recall that the backward equation describes the evolution of u(x,t), the expected value of some function g(x) that starts with a unit mass at x and is subsequently stirred by the probability dynamics. [64] This is obtained from the transition probability measure Px(dy,t) as

u(x,t) =

Px(dy,t)g(y) =

p(x,y,t)g(y)dρ(y)

Ω

Ω

(A.37) where the transition probability has initial condition Px(y,0) = α δα(y − x) and we have used the fact that it has a density p(x,y,t) with respect to the equilibrium measure dρ(y) (see (24)). Note this implies p(x,y,0) = α δα(y − x)/κα.

We suppose that Px satisﬁes the ChapmanKolmogorov equation as this property holds for the original probability measure p dx from which it derives:

Px(dz,t − s)Pz(dy,s) = Px(dy,t). (A.38)

z∈Ω

This allows us to write

Px(dz,t−s)u(z,s) =

px(z,t−s)u(z,s)dρ(z).

u(x,t) =

Ω

Ω

(A.39) We can now obtain an evolution equation for u. Applying ∂t to (A.39) and using (24) gives

∂u ∂t

=

ptu dρ(y) =

Ω

( div grad p)u dρ(y)

Ω

u( grad p · nˆ)

=

p( div grad u) +

Ω

i Ωi

− p( grad u · nˆ) + κiu div grad p.

Here {Ωi} is the set of manifolds of co-dimension 1 that form the boundary of the full space Ω, κi are the sticky factors along these manifolds, div , grad denote differential operators on Ω and divi , gradi will denote those on Ωi, nˆ denotes a generic outward normal to the appropriate manifold, and integration is with respect to the volume element appropriate for each manifold. We now substitute for grad p · nˆ using the forward sticky equations to obtain

- ∂u


=

∂t

=

p( div grad u) +

Ω

p( div grad u) +

Ω

u( divi κi gradi p − κi div grad p) − p grad u · nˆ + κiu div grad p

i Ωi

p( divi κi gradi u − grad u · nˆ) +

i Ωi

κi(u gradi p · nˆ(ij) − p gradi u · nˆ(ij)) (A.40)

j Ωj i→j

Here {Ωj} is the set of manifolds of co-dimension 2, forming the boundaries of the manifolds Ωi; the sum in the ﬁnal term is over all manifolds Ωi that have Ωj as a boundary, and nˆ(ij) is the outward normal vector from Ωi at Ωj.

Evaluating (A.40) at s = t gives the backward sticky equations

∂tu = div grad u in Ω κi∂tu = divi κi gradi u − ∇u · nˆ in Ωi (A.41) ∂tu = (boundary terms) in Ωj

We stop at the ﬁrst two terms; the interested reader can show that evaluating the boundary terms leads to the expected equations on the lower-dimensional manifolds. This set of equations is identical to the forward equations, so the system is self-adjoint.

Parameterizing the manifolds

In this section we outline the method we used to parameterize the quotient manifolds ΩQα describing clusters of hard spheres with up to 2 bonds broken. The method can be broken down into two separate sets of algorithms. The ﬁrst algorithm generates points on the manifold, by taking linear steps along the tangent directions and projecting back down to the manifold. This is suﬃcient to calculate the 1-dimensional manifolds. The second algorithm links up the points with bars to form a simplex on which calculations can be performed, and is required for 2- and higher-dimensional manifolds.

1-dimensional manifolds

Consider ﬁrst the 1-dimensional manifolds. We take steps along the manifold as follows: given a point x0 ∈ Ωα, a set of bond-distance constraints {yk}mk=1, and a basis {ti}6i=1 for the part of the tangent space at x0 parallel to rotational and translational motions, we form a matrix M = (∇y1,...,∇ym,t1,...,t6)T and compute the null space of M. When x0 is a regular point on the manifold, this null space contains a single vector v lying in the tangent space of Ωα(x0), so we take a step in that direction as x1 = x0 +(∆s)v. Because v is orthogonal to

translations and rotations, the length of our step in the quotient metric is ||x1 − x0||Qα = ∆s + O(∆s2).

This step pushes us slightly oﬀ the manifold, so we project back down to it by ﬁnding a set of Lagrange multipliers λk so that the projected point x 1 = x1 +

k λk∇yk(x1) lies on the manifold, i.e. we solve the non-

linear system of equations yk(x1 + k λk∇yk(x1)) = 0 [65]. This is easily done using Newton’s method as we

are typically very close to the manifold.

Beginning with a rigid cluster x0 with an associated set of bond constraints, we break a bond by deleting one of the constraints, and perform the steps above until another bond is formed. This provides an ordered set of points in the quotient manifold, along with distances between them – this is a “line”.

2-dimensional manifolds

Computing the 2-dimensional manifolds is more involved; here are the steps we followed.

Compute the boundaries First, we compute the boundaries of the manifold. To compute a 2-dimensional manifold ΩQα with constraint list y1(x),...,yn(x), we start with a corner point x0 ∈ ΩQα with two extra constraints yi

, we walk along the 1-dimensional manifold (as in the previous section) until another bond is formed, corresponding say to constraint yi

(x),yi

(x). Deleting one of these, say yi

1

2

1

. We add this to our constraint list, delete the next extraneous constraint yi

3

, and repeat. We continue in this way, deleting one extraneous constraint at each corner, until we reach the original corner x0. This gives us the boundary of ΩQα, including corners.

2

Generate points in the interior Second, we generate a collection of points in the interior. Beginning with every point on the boundary, we generate lines in the interior by holding all constraints ﬁxed except the one that takes us oﬀ the boundary, and walk in this direction until we exit the manifold. We throw away points that are too close in some metric to existing points to avoid generating too many points.

Triangulate the points Third, we triangulate the points. Many typical algorithms will not work here because our surface is not embedded in R3, so we adopt an algorithm proposed by by [66] (see also [67]) that works as follows.

- 1. Map the boundary to a ﬁxed convex polygon in R2.
- 2. Map the interior points to the interior of that region in R2, by letting each interior point be a convex combination of its neighbouring points. More speciﬁcally: let x1,...xn be the set of interior points, and let Ni be a neighbourhood of an interior point xi. Given a set of strictly positive weights λij

such that x

j∈Ni λij = 1, ﬁnd parameter points u1,...un ∈ R2 that solve the linear system of equations

ui =

xj∈Ni

λijuj, i = 1,...,n.

Each ui is contained in the convex hull of its neighbours, so it will be in the interior of the region deﬁned in step (1) [66].

- 3. Triangulate the parameter points in R2 (we use a Delauney triangulation.) This lifts back to a triangulation of the manifold.


To implement this, we choose the boundary region so that the corners lie on a circle with a ﬁxed radius, and the line segments joining them lie on arcs of circles whose lengths are approximately the same as the lines they are parameterizing. Points along these arcs are placed so the inter-point distance in the plane is proportional to the distance in the quotient metric between the points. The quality of the triangulation will depend on the choice of boundary region, and we ﬁnd better qualities as the angles at the corners more closely represent the angles on the manifold.

Choosing the neighbourhood Ni is a balance between sampling many points to get a smoother parameterization, and choosing fewer points so the manifold is roughly linear in the neighbourhood and does not contain any folds or other external branches of the manifold. We choose the neighbourhood to be the k nearest points along the manifold, where a range of roughly 8 ≤ k ≤ 15 works well for the step sizes we use, but k will increase

- as step size decreases. There are many ways to choose the weights; the most


straightforward is for them to be the same, but almost as straightforward is for them to be inversely proportional to distance in some metric. For rapid but still good quality results we use the metric in bond-distance space – this takes the list of pairwise bond distances and computes the Euclidean distance between the vectors.

Improve the triangulation Finally, we improve the quality of the triangulation by letting the triangle sides be springs and evolving the points on the manifold with the spring forces, re-triangulating when necessary. Springs are chosen to be slightly longer than the average distance between points so the points want to spread out and ﬁll the whole space. When a point hits a boundary

it is absorbed, and is subsequently constrained to move along the boundary. This algorithm was introduced by

- [68] for a triangulation of the Euclidean plane, and we adapt it by replacing the length in the plane with the distance metric in the quotient manifold. In practice, we typically use bond-space distance instead as this is faster to compute and still gives a good quality triangulation.

Integration on the manifolds To compute quantities integrated over the manifolds, such as for the partition functions zαgeom, we used ﬁnite elements on the simplex with standard piecewise linear elements. The sides of the triangles must be calculated in the quotient space metric.

Remarks

Topology The calculations above require that the 2dimensional manifolds be topologically equivalent to a disc. Because we have obtained smooth parameterizations, we are conﬁdent that this is true for all the ﬂoppy manifolds under consideration. Alternatively, one could show this from a collection of points using Betti numbers

- [69], for example. This points to an interesting question in discrete ge-


ometry – under what conditions is the topology of ﬂoppy manifolds a polygon? One has to rule out surfaces of higher genus and non-orientable surfaces, among other things. We expect this can be shown for low-dimensional manifolds and small n, but larger p or n may be more complicated.

Numerical parameters and convergence For the calculations reported in the text we used a step size of ∆s = 0.01 to calculate the one-dimensional manifolds, and ∆s = 0.05 to generate points on the boundary and interior of the 2-dimensional manifolds. When generating points we threw away points that were closer than 0.5∆s in bond-distance space to already-generated points. We typically ran the triangulation step 3 times before retriangulating, using a step size of ∆t = 0.1 and an internal pressure parameter of 1.2 (see [68]), although a small selection of manifolds had to be re-triangulated after each spring step. We ran the triangulation until the area of the manifold, computed in bond-distance space, changed less than ∆s/20 after 3 consecutive retriangulations. We checked for convergence in two ways: by calculating the manifolds using a coarser resolution (∆s = 0.1 for the 2-dimensional manifolds, ∆s = 0.05 for the 1-dimensional manifolds), and by running the triangulation algorithm for longer, until the minimum triangle quality (q = 2rin/rout, the ratio between (twice) the radius of the largest inscribed circle and the smallest circumscribed circle, see e.g. [70]) was greater than 0.2. Both tests allowed us to conclude that our calculated ratios Z2/Z1, Z1,Z0 are correct to ±0.05, ±0.01 respectively (although we have not reported this many decimal points for the latter).

Simulations

We have performed Brownian dynamics simulations of interacting particles to test our asymptotic calculations. We solve equation (2) with D = β = 1 using a forward Euler timestep. For the potential we started with a Morse potential with maximum depth E

- at r = 1 and range parameter ρ; this takes the form U(r) = Ee−ρ(r−1) e−ρ(r−1) − 2 . The hard-core part for r < 1 was modelled with a parabolic potential of the


form U(r) = 21m2U (1)(r − 1)2 − E for some number m; we choose m = 2. This constrains the time step to be

∆t (m2U (1))−1 and we typically choose a factor of 6–8 less. The sticky factor, accounting for the parabolic

√ E

part, is κ = mm+1 e

π 2.

2Eρ2

The whole potential was truncated at rc = 1+4/ρ, by adding a linear term to keep the force continuous at rc, as Utrunc(r) = U(r)−(U(rc)+U (rc)(r −rc)) for r < rc, and Utrunc(r) = 0 otherwise. This modiﬁes the sticky parameter to

exp(E − U(rc) − U (rc)(1 − rc)) 2Eρ2

m + 1 m

π 2

κ =

. (A.42)

We began with an initial condition drawn from the equilibrium distribution of rigid modes, and ran several copies of the simulation for a very long time. At time increments of 1 × 10−2 we checked to see which ﬂoppy mode the cluster occupied by forming its adjacency matrix, computing the number of bonds, and if this number was ≥ 3n−6−2, ﬁnding the adjacency matrix in our list of ﬂoppy modes to which it was topologically equivalent. This allows us to compute the occupation probabilities of each ﬂoppy mode.

To form the adjacency matrix, we said particles were bonded when they were at a distance of less than 1+2/ρ; this is the range beyond which the force is negligible. (Choosing a bond distance of 1 + 1/ρ gave results that were inconsistent with the asymptotics.) We used the Matlab function graphisomorphism.m to determine topological equivalencies.

We also kept track of transitions between rigid clusters, by recording the times and mode numbers at which the system ﬁrst hits a rigid state that occupies a separate part of conﬁguration space than the previous rigid state. This is easily done by checking whether or not the current adjacency matrix of a rigid mode is identical to the adjacency matrix of the previous rigid mode.

- Figure 8 shows the simulated probabilities versus the-

oretically computed probabilities of each ﬂoppy mode for n = 7,8, for simulations using a Morse potential with the same parameters as in the text (Figure 7): E = 8.5, ρ = 30, dt = 2×10−6. This implies the sticky parameter is κ = 16. Again, there is excellent agreement.

- Figure 9 plots the elements of the transition count ma-


![image 9](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile9.png>)

![image 10](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile10.png>)

![image 11](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile11.png>)

![image 12](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile12.png>)

![image 13](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile13.png>)

![image 14](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile14.png>)

FIG. 8. Simulated versus theoretical probabilities of ﬂoppy modes, for n = 7 (top), n = 8 (bottom), for a Morse potential with range parameter ρ = 30. The running time of each simulation varied and is given in the title.

trix for n = 6,7,8 from simulations, versus two theoretical calculations. The blue markers come from the leading-order asymptotic approximation, computed from (29). The magenta markers come simply restricting the dynamics to the network of points and lines, which gives geometric rates of (Z0 + κ−1Z1)−1 k Q−k 1 – these are the blue rates multiplied by 1/(1 + κ−1Z1/Z0), so are asymptotically equivalent, but uniformly smaller.These rates do a better job of predicting the simulated rates for this value of the range parameter.

To calculate rates for n = 7,8 we have grouped the 0dimensional modes that are very close together into one mode (these are modes {1,4} for n = 7, modes {1,2,3,4} for n = 8). The rate from a mode in this group to a mode not in the group is the sum of the rates out of each mode in a group, and the rates within a group are ignored. We were able to make a distinction between modes in a group only by using a range parameter of ρ = 150 (not shown).

Table II shows the ratios Zp+1/Zp extracted from the simulations. These are uniformly smaller than the theoretically computed values, but approach the theory as the range of the potential decreases. This is because the simulations use an excess bond length that is ﬁnite rather than inﬁnitesimal, so some clusters are counted as being on p-dimensional manifolds, when in the limit they would be on p+1-dimensional manifolds. One could potentially correct for this if one had no knowledge of the potential, but wanted to use these measurements to estimate the sticky parameter.

Data

We provide details for the ﬂoppy modes for n = 6. Details for n = 7,8 are available upon request.

Table III reports the following quantities for each mode: the volume S ≡ ΩQ

1 , mean geometrical sticky

α

![image 15](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile15.png>)

![image 16](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile16.png>)

![image 17](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile17.png>)

- FIG. 9. Elements of the count matrix for n = 6, 7, 8 (left, middle, right).


Z1/Z0 A B C

- 6 5.5 5.9
- 7 5.8 6.0 7.2
- 8 5.2 6.4 6.7


Z2/Z0 A B C

- 6 3.4 4.1
- 7 3.5 3.8 4.2
- 8 3.6 3.6 4.7


TABLE II. Ratios extracted from simulations with diﬀerent range and sticky parameters. These were computed as (time in p + 1-dimensional modes) / (time in p-dimensional modes) / κ, where κ is computed using (A.42). Parameters were (A) dt = 2e − 6, E = 8.5, ρ = 30 (κ = 16), (B) dt = 8e − 7, E = 10, ρ = 50 (κ = 31), (C) dt = 2.5e − 7, E = 10.6, ρ = 150 (κ = 22)

### parameter h¯ ≡ ( ΩQ

### h)/S, mean rotational contribution I¯ ≡ ( ΩQ

α

I)/S, multiplicity nα (divided by a constant). Each of the integrals is over a single manifold in the set of isomorphic manifolds, and the average for rigid modes is simply the point value. For ﬂoppy modes we also report the corners, in the order they occur as one travels around the boundary.

α

Mode h¯ I¯ S nα zα corners

- 0-dimensional modes

- 1 0.061 3.16 180 34.64
- 2 0.034 2.83 15 1.44

1-dimensional modes

- 3 0.066 3.30 0.85 180 33.30 1, 1
- 4 0.063 3.29 0.89 90 16.65 1, 1
- 5 0.057 3.29 0.95 360 64.03 1, 1
- 6 0.069 3.49 1.47 360 126.89 1, 1
- 7 0.045 3.04 0.63 180 15.40 1, 2


- 2-dimensional modes


- 16 0.075 3.37 0.35 180 15.99 1, 1, 1
- 17 0.075 3.76 2.00 360 202.45 1, 1, 1, 1, 1
- 18 0.083 4.01 2.17 180 130.10 1, 1, 1, 1
- 19 0.064 3.53 1.07 360 87.44 1, 1, 1, 1
- 20 0.057 3.17 0.23 180 7.52 1, 1, 2
- 21 0.073 3.79 2.84 360 284.23 1, 1, 1, 1, 1, 1
- 22 0.055 3.17 0.24 90 3.76 1, 1, 2
- 23 0.064 3.56 1.55 72 25.33 1, 1, 1, 1, 1
- 24 0.067 3.48 0.64 360 53.23 1, 1, 1
- 25 0.063 3.59 1.58 360 129.53 1, 1, 1, 2, 1
- 26 0.054 3.27 0.59 360 37.56 1, 1, 2, 1
- 27 0.081 4.07 2.67 120 105.52 1, 1, 1
- 28 0.072 3.77 2.39 90 57.97 1, 1, 1, 1


TABLE III. Free energy data for each mode, n = 6.

Figure 11 provides a way to identify the individual modes. It shows the rigid clusters with particles numbered. The table indicates how to reach each ﬂoppy mode by starting with a given rigid structure and breaking selected bonds. In most cases there are multiple ways to reach each ﬂoppy structure and every possible bond combination that does so is listed.

Figure 10 plots the transition states computed in [42] along each of the identiﬁed 1-dimensional ﬂoppy manifolds.

![image 18](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile18.png>)

![image 19](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile19.png>)

![image 20](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile20.png>)

![image 21](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile21.png>)

![image 22](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile22.png>)

![image 23](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile23.png>)

![image 24](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile24.png>)

![image 25](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile25.png>)

##### FIG. 10. Vibrational contribution to the free energy − log h(x) along selected 1-dimensional manifolds (red line). Markers indicate the transition state computed in [42] for a potential with ﬁnite width.

- FIG. 11. Rigid clusters for n = 6. Right, Mode 1 (polytetrahedron), Left, Mode 2 (octahedron). The table below shows which bonds to break to reach each ﬂoppy mode.


![image 26](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile26.png>)

![image 27](<2012-holmescerfon-geometrical-approach-computing-free-energy_images/imageFile27.png>)

Mode Starting Cluster break bonds

- 3 1 1-3, 2-4
- 4 1 1-4
- 5 1 1-5, 4-5, 1-6, 4-6
- 6 1 2-5, 3-5, 2-6, 3-6
- 7 1 5-6 2 1-3, 2-3, 1-4, 2-4, 1-5, 2-5, 3-5, 4-5, 1-6, 2-6, 3-6, 4-6
- 8 1 {1-3, 1-4}, {1-3, 2-4}, {1-3, 2-4}
- 9 1 {1-3, 1-5}, {1-3, 2-5}, {1-3, 1-6}, {1-3, 2-6}, {2-4, 3-5}, {2-4, 4-5}, {2-4, 3-6}, {2-4, 4-6}, {2-5, 3-5}, {2-5, 3-5}
- 10 1 {1-3, 3-5}, {1-3, 3-6}, {2-4, 2-5}, {2-4, 2-5}
- 11 1 {1-3, 4-5}, {1-3, 4-6}, {2-4, 1-5}, {2-4, 1-6}, {1-5, 2-5}, {3-5, 4-5}, {1-6, 2-6}, {1-6, 2-6}
- 12 1 {1-3, 5-6}, {1-3, 5-6} 2 {1-3, 2-3}, {1-3, 1-4}, {2-3, 2-4}, {1-4, 2-4}, {1-5, 2-5}, {1-5, 1-6}, {2-5,

- 2-6}, {3-5, 4-5}, {3-5, 3-6}, {4-5, 4-6}, {1-6, 2-6}, {1-6, 2-6}

13 1 {1-4, 1-5}, {1-4, 2-5}, {1-4, 3-5}, {1-4, 4-5}, {1-4, 1-6}, {1-4, 2-6}, {1-4,

- 3-6}, {1-4, 4-6}, {1-5, 3-5}, {2-5, 4-5}, {1-6, 3-6}, {1-6, 3-6}


- 14 1 {1-4, 5-6}, {1-4, 5-6} 2 {1-3, 2-4}, {2-3, 1-4}, {1-5, 2-6}, {2-5, 1-6}, {3-5, 4-6}, {3-5, 4-6}
- 15 1 {1-5, 4-5}, {1-5, 4-5}
- 16 1 {1-5, 1-6}, {1-5, 3-6}, {2-5, 4-6}, {3-5, 1-6}, {4-5, 2-6}, {4-5, 2-6}
- 17 1 {1-5, 2-6}, {2-5, 1-6}, {2-5, 5-6}, {3-5, 4-6}, {3-5, 5-6}, {4-5, 3-6}, {2-6, 5-6}, {2-6, 5-6}

2 {1-3, 1-5}, {1-3, 3-5}, {1-3, 1-6}, {1-3, 3-6}, {2-3, 2-5}, {2-3, 3-5}, {2-3, 2-6}, {2-3, 3-6}, {1-4, 1-5}, {1-4, 4-5}, {1-4, 1-6}, {1-4, 4-6}, {2-4, 2-5}, {2-4, 4-5}, {2-4, 2-6}, {2-4, 4-6}, {1-5, 3-5}, {1-5, 4-5}, {2-5, 3-5}, {2-5, 4-5}, {1-6, 3-6}, {1-6, 4-6}, {2-6, 3-6}, {2-6, 3-6}

- 18 1 {1-5, 4-6}, {1-5, 5-6}, {4-5, 1-6}, {4-5, 5-6}, {1-6, 5-6}, {1-6, 5-6} 2 {1-3, 2-5}, {1-3, 4-5}, {1-3, 2-6}, {1-3, 4-6}, {2-3, 1-5}, {2-3, 4-5}, {2-3,

1-6}, {2-3, 4-6}, {1-4, 2-5}, {1-4, 3-5}, {1-4, 2-6}, {1-4, 3-6}, {2-4, 1-5}, {2-4, 3-5}, {2-4, 1-6}, {2-4, 3-6}, {1-5, 3-6}, {1-5, 4-6}, {2-5, 3-6}, {2-5, 4-6}, {3-5, 1-6}, {3-5, 2-6}, {4-5, 1-6}, {4-5, 1-6}

- 19 1 {2-5, 2-6}, {2-5, 2-6}
- 20 1 {2-5, 3-6}, {2-5, 3-6}


