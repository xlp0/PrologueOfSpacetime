# #1 Homotopy Type Theory Explained: A New Foundation for Mathematics

What if fields as vast as algebra, topology, even logic itself,
could be described in a single language?
Not just described in it, but built from it, with its rules,
its structures, and its proofs all living in the same universe.
That's the promise of Homotopy Type Theory:
A new foundation for mathematics,
Where equality is not just a yes-or-no statement,
but a path with shape and structure.
But hang on. What do all these symbols mean?
What even is a type?
Well, we can think of a type as a space.
This space is inhabited by things called terms.
These terms could be numbers, functions, or even types themselves.
At this point it would seem that
types are the same things as sets.
However,
types and sets are fundamentally different from each other.
And the distinction lies in the way types handle equality.
Perhaps an example might explain things.
Suppose we had a type A.
And suppose it is inhabited by the terms x and y.
Note that we use a colon
to denote that terms inhabit a certain type.
In Homotopy Type Theory, two terms are seen as equal
when there's a path from one to the other.
In our case that would be a path from x to y.
However, this is where things get interesting.
In Homotopy Type Theory, we can have multiple paths
demonstrating that x is equal to y.
Let's draw another one.
Let's call these paths, p and q.
We denote this by writing that p and q are inhabitants
of the equality type, x = y.
An equality type is a special kind of type
that contains all the proofs that one term is equal to another.
And we can go one step further:
We can ask if the path p is equal to the path q.
In that case, we're not simply speaking of a path,
but of a path of paths.
Something that looks a bit like this.
Topologists refer to these paths as homotopies.
Hence the name, Homotopy Type Theory.
And yes, if you were wondering, we can go a level higher.
We can speak of paths of paths of paths.
And paths of paths of paths of paths.
We can go up to infinity.
But that's a video for another day.
Thanks for watching.

# #2 Homotopy Type Theory Explained: Universes, Functions, and Π-types

So far we have learned about types,
terms, equality types, paths.
But there is one special type
without which none of this would be possible.
Something type theorists refer to as
a universe.
A universe is a type whose terms are themselves types.
In fact,
by definition, every type we can think of must inhabit a universe,
including universes themselves.
Therefore, every universe inhabits an even bigger universe
such that we have an infinite series of universes
nested within each other.
The power of these universes becomes evident
when we use them in conjunction with functions.
But how do we implement functions in type theory?
Well, to start off
we have something called a function type.
For instance,
let's consider the function type A→B.
We say that the function f inhabits this function type
if f maps every term of A
to a term of B.
You may be thinking: "No big deal.
We do this in mathematics all the time."
But something interesting happens when we map
— not to an ordinary type —
but to a universe.
The functions inhabiting this type
are called type families.
Suppose we had a type family,
capital F.
F would then map every term of A to some type.
But we can go one step further.
Not only can we map to a type in a type family,
we can map to a term in a type in a type family.
But to understand how this is done,
we need to take a look at an indispensable tool
used by type theorists,
the Π-type.
Using the Π-type, we can construct a new kind of function type.
One that redefines our very definition of a function.
For example,
we can construct a function g
that takes every term in its input x
to a term in F(x).
In other words,
the output type depends on the input term.
And thus we have a new breed of functions
that transcend the realms of ordinary functions.
We call them
dependent functions.
Thanks for watching.

# #3 Homotopy Type Theory Explained: Propositions as Types

So far we've encountered types inhabited by numbers,
functions, paths, even types themselves.
However, in this video,
we are going to use types in a very special way.
This will allow us to reconstruct logic itself.
We are going to treat types as propositions.
And in some sense,
we've already been doing this with equality types.
For example,
in the same way that the inhabitants of the equality type x = y
are proofs that x is equal to y,
the inhabitants of the proposition P are proofs that P is true.
Note that unlike in classical logic
where we either know that a proposition is true
or we don't know a proposition is true,
in type theory, we could have multiple inhabitants
proving that a proposition is true.
So, to prove that a proposition is true,
we need to construct a term thereof.
But how do we prove that a proposition is false?
Well, type theorists say that a proposition is false
if we can construct a function
from the proposition to the empty type.
And yes, as the name suggests,
an empty type is a type without inhabitants.
But why would we define the falsehood of a proposition like this?
Well, suppose we did have a function
that maps every term in the proposition
to a term in the empty type.
The question that immediately arises is:
"To which terms could it possibly map?"
Thus, such a function could only be defined
if there were no terms in the proposition
to map in the first place.
The proposition must then be uninhabited.
And the analogue of this in classical logic is
not P.
Note that we use this little symbol
to indicate that a proposition is not true.
In logic, this is called negation.
Actually, functions serve a much more general purpose
when we treat types as propositions.
A function from P to Q simply means
that whenever we have a term in P,
we can construct a term in Q.
And logically, this means that P implies Q.
We now know how to construct proofs, negations,
and implications in type theory.
Thanks for watching.

# #4 Homotopy Type Theory Explained: Universal Quantifiers

In the previous video, we learned what happens
when we treat types as propositions.
We also learned how to construct proofs,
negations, and implications in type theory.
In particular, we learned that an implication
is simply a function from  one proposition to another.
But we can go one step further.
Rather than applying ordinary functions to
propositions as types,
we can apply dependent functions.
But how do we do that?
Well, for starters,
consider the type A.
A doesn't have to be a proposition.
In fact, it could be any data type.
Now, suppose we had a type family P
that maps every term in A
to some proposition about that term.
Furthermore,
let's assume that all the  propositions in the type family P
are inhabited.
In that case, we can  construct a dependent function
using the Π-type and the type family P.
This function maps every term in A
to a proof
that the proposition P about that term is true.
If one of these propositions were uninhabited,
such a function could not have been constructed.
The analogue of this in classical logic is
for all x, P(x) is true.
In logic, this is called a universal quantifier.
Thanks for watching.

# #5 Homotopy Type Theory Explained: Products

In set theory, there are two very powerful tools
for creating new sets from old ones.
The Cartesian product
and the disjoint union.
A bit of a mouthful if you ask me.
In type theory, we simply call them
products and co-products.
And these will be the topics of the next two videos.
Let's start with products.
Suppose we had a type A inhabited by the term x,
and we had a type B inhabited by the term y.
In that case, we can construct a pair from x and y.
And this term inhabits the product type A × B.
We can also do what we refer to as projections on a pair.
For example, the projection π₁ picks out the first term
of the pair (x,y), and is thus by definition equal to x.
Note that the colon in front of the equal sign
indicates that the two terms are equal by definition.
This is not an equality type for which we have to construct a path.
We could also perform the projection π₂
to get the second term in the pair.
If we were to draw a picture of this,
we would see that as long as we have a term
in the product type A × B, we could use the projections
to construct a term in A
and to construct a term in B.
But we can go one step further.
We can apply the product type to propositions.
In that case, for a term to inhabit the product type P × Q,
we must have a term in P proving that P is true
AND we must have a term in Q proving that Q is true.
The logical analogue of this is: P AND Q.
The fancy word for this in logic is a "conjunction".
To recap, we can now construct proofs,
negations, implications, universal quantifiers,
and conjunctions in type theory.
Thanks for watching.

# #6 Homotopy Type Theory Explained: Coproducts

In the previous video, we learned about products
and how they are the analogue of conjunctions in logic.
In this video, however, we are going to investigate coproducts.
Suppose we have the types A and B.
In that case we have the coproduct type A + B.
Now, there are two ways in which we can construct
a term of this co-product type.
Firstly, if we had a term x : A,
we could apply what we call a left injection
to get a term in A + B.
Secondly, if we had a term y : B,
we could apply the right injection to construct a term in A + B.
If we were to draw a picture of this,
we would see that as long as we have a term in A
OR we have a term in B,
we can construct a term in A + B.
But we can go one step further.
We can apply the coproduct...
to propositions.
Suppose we have the propositions P and Q.
In that case, we can construct a proof of the proposition P + Q
as long as we have proof of P or a proof of Q.
In other words, the proposition P + Q simply means
P OR Q.
The fancy word for this in logic is a "disjunction".
To recap, we now know how to construct proofs,
negations, implications, universal quantifiers,
conjunctions, and disjunctions in type theory.
Thanks for watching.

# #7 Homotopy Type Theory Explained: Σ-types

At this point, we are familiar with the Π-type
and how it allows us to construct dependent functions
for which the output type depends on the input term.
But to continue on our journey,
we need to take a look at another very special type,
one that's related to the Π-type,
but rather than generalising functions,
this type generalises pairs.
We call it...
...the Σ-type.
Let's see how it works.
Suppose we had a type A
and suppose we had a type family F
that maps every term in A to a type in some universe.
We can then use the type family F to construct a Σ-type.
The inhabitants of this Σ-type are pairs.
Suppose we had such a pair inhabiting this Σ-type.
The first term in the pair would be a term in A.
The second term in the pair
would be a term in the type
that F sends the first term in the pair to.
In this case, z is a term in A,
and w is a term in F(z).
In other words, to construct a term in this Σ-type,
we simply need a term in A
and we need a term in F of that term.
We call these pairs...
dependent pairs.
But why do we say that
the Σ-type generalises the notion of pairs?
Well, suppose the type of the second term in the pair
were not dependent on the first term in the pair.
To do that, we simply consider the case
where F maps every term in A to the same type.
Let's call that type B.
Note that we can write the type family that always maps to B
simply as B.
In that case, a term inhabiting this Σ-type
would simply be a pair whose first term is a term in A
and whose second term is a term in B.
And if this seems familiar, that's because
this is the very definition...
...of a product type.
Thanks for watching.

# #8 Homotopy Type Theory Explained: Existential Quantifiers

In the previous video, we learned about the Σ-type
and how it generalises the notion of a pair
to that...
...of a dependent pair.
In this video, however,
we are going to investigate what happens
when we apply Σ-types...
...to propositions.
Suppose we had a type A
and suppose we had a type family P
that maps every term in A
to some proposition about that term.
Let's use this type family to construct a Σ-type.
The first term in a pair inhabiting the Σ-type
would be a term in A.
Let's pick the term z.
The second term in the pair would be a term in P(z).
Let's call it V.
In other words, to construct a term in this Σ-type,
we need a term in A
and we need a proof
that the proposition P about that term is true.
The classical analogue of this is
there exists an A such that P of A is true.
In logic, this is called...
...an existential quantifier.
To recap,
we can now construct proofs, negations, implications,
universal quantifiers, conjunctions, disjunctions,
and existential quantifiers
in type theory.
Thanks for watching.

# #9 Homotopy Type Theory Explained: Law of Excluded Middle, Lambda Calculus

In classical logic, there is a law
that states that every proposition
must either be true
or it must be false.
We call it the Law of Excluded Middle (LEM).
In type theory, this would mean that
every proposition
is either provably true
or provably false.
However, there are some propositions in mathematics
that are neither provably true
nor provably false.
We must therefore conclude
that in type theory,
the law of excluded middle does not hold.
That being said, we can prove
that the law of excluded middle is not not true.
Let's see how this is done.
Bare in mind this is going to be a mind twister.
So feel free to pause or rewind.
Recall that we define a proposition to be
not true when we can construct a function
from the proposition to the empty type.
Therefore, to construct a term of this type,
we need to construct a function
that takes in another function f
that maps A plus ¬ A to the empty type
and returns a term of the empty type.
All right. Then suppose we were given the function f.
How would we construct a term of the empty type?
Well, if only we had a term in the type A,
we could apply the left injection to that term
and then apply f to that term
to get a term in the empty type.
But we don't have a term in A.
But what about a term in not A?
To construct a term in ¬ A,
we need to construct a function from A to the empty type.
But that is exactly what we have just defined.
Here's how we write this.
We make use of something called ꟛ-calculus.
We write ꟛy
where everything after the ꟛ refers to an input.
Then we write a dot
where everything after the dot refers to the output.
And then we write the construction of a term in the empty type:
f applied to the left injection of y.
Now that we have a term in ¬ A,
we can apply the right injection to it
to it to get a term in A + ¬ A.
Finally, we can apply f to this term in
A + ¬ A to get a term in the empty type.
Putting this all together,
we can construct a function
that takes in a function from A + ¬ A to the empty type,
and returns a term in the empty type.
We then define g to be equal to this term
and we fold our definitions on the right
hand side up again to get
g : ¬¬ (A + ¬ A).
In other words, we have just proven that
it is impossible
for any proposition
to be neither true nor false.
Thanks for watching.

# #10 Homotopy Type Theory Explained: Path Induction

In the past few videos, we investigated
how homotopy type theory is applied to logic.
But in this video,
we are going to return to the start of our journey.
We are going to investigate...
path induction.
Recall that we can think of a type as a space
and we can think of the terms in that type
as points in that space.
In this case, an inhabitant of the equality type x = y
corresponds to a path from x to y.
Let's consider the equality type x equality type x=x
In homotopy type theory,
we can always construct a special path from a term to itself.
In this case, we will call this path reflₓ.
But here's where the magic happens.
According to the principle of path induction,
whenever we need to prove that something
is true for a path from x to y,
we only need to prove that it is true for the path
reflₓ from x to x.
Let's take a look at an example.
Suppose we had a path p demonstrating that x is equal to y.
How do we then show that there's a path p⁻¹ from y to x?
Let's express this as a function type.
We want to construct a function that,
given the terms x, y : A,
returns a function that maps a term in x = y to a term in y = x.
Let's call this function sym,
since it proves that equalities are symmetrical.
According to the path induction principle,
we need only consider the case
where y is definitionally equal to x,
and the path from x to x is reflₓ.
In that case, we simply need to define
sym(x, x, reflₓ) as being equal to reflₓ.
Applying the path induction principle,
we now know that since the path reflₓ
from x to x has an inverse,
any path p from x to y also has an inverse.
Therefore, we have just proven
that equalities
are symmetrical.
Thanks for watching.

# #11 Homotopy Type Theory Explained: Inductive Types, Finite Sets, Natural Numbers

So far in this series,
we have learned how to construct types
from preexisting types.  
But in this video,
we are going to learn how to construct types from scratch.
We are going to investigate...
inductive types.
Let's start with  some simple examples.
The unit type, denoted by the numeral 1,
is a type with exactly one term. 
We express this by saying that
the unit type has exactly one constructor.
We can do the same for the type with exactly two terms,
as well as for the type with exactly three terms.
We call these inductive types finite sets.
But what  about infinite sets?
The most famous example of an infinite set
is the natural numbers.
This inductive type only has two constructors:
zero, and a function called successor (succ).  
Applying successor to a natural number
gives us a new natural number.
This allows the natural number type
to have infinitely many terms.
We now know how to construct natural numbers in type theory.
Thanks for watching.

# #12 Homotopy Type Theory Explained: Addition, Currying, Functions from Inductive Types

In the previous video,
we learned how to construct
inductive types.
But in this video, we are going to learn
how to construct functions
from inductive types to any other type.
But before we continue,
there is something important
which we should know about functions.
Suppose we wanted to construct a function f
with not one but two arguments.
Let's call the input types A and B.
And let's call the output type C.
f would then inhabit the function type
A⟶B⟶C
Syntactically this means that f maps a
term in A to the function type B ⟶ C
This allows us to construct functions
with any number of input arguments.
We call this method of constructing functions
currying.
But back to the main topic of this video.
How do we construct a function from an
inductive type to another type?
For example,
suppose we wanted to construct a function f
from the natural numbers to the type A.
To do this, we define how f acts upon
each constructor of the natural numbers.
This method of constructing functions is
so universal
we can use it to define
addition.
Let's see how it works.
Recall that we can use crying to define
functions with more than one argument.
In the case of addition,
we are going to define a function
from the natural numbers
to a function from the natural numbers to itself.
To start out,
note that adding any number n to the number 0
should return the number n.
Similarly,
m + 1 + n should be equal to m + n + 1.
Let's rewrite these as single argument functions.
And just like that, we have defined
addition.
Let's see it in action.
Suppose we wanted to calculate
2 + 2.
Applying our rules for addition
and unfolding the definitions,
we find that 2 + 2
= 4.
We now know how to do addition in type theory.
Thanks for watching.

# #13 Homotopy Type Theory Explained: Recursors, Multiplication, Factorial

In the previous video, we learned how to do addition.
But in this video,
we are going to learn how to define functions in  a very special way. We are going to investigate...
recursors.
But before we continue, let us define another old friend,
multiplication.
We start by defining 0 × n as being equal to 0.
We then define (m + 1)n as being equal to mn + n.
And just like that, we've defined multiplication.
But let us get back to the main topic of our video, recursors.
A recursor allows us to define functions systematically.
Let's take the natural numbers as an example.
A function from the natural numbers to some other type
effectively picks out a sequence of terms in said type.
It follows that the recursor for natural numbers
is an inhabitant of the following function type.
First we pick an output type. Let's call it X.
Then we pick a term in X to which the number zero is mapped.
This will be the first term in our sequence.
Next, we construct a function that
given some number and its corresponding term in X,
it returns the next term in the sequence.
Finally,
we are left with a function
that maps any number in ℕ to a term in X.
Okay, so the recursor is a very complicated function.
But how exactly does it work?
Well,
suppose we wanted to construct a function f from ℕ to A.
In that case, we can define f to be equal to rec_ℕ(A, a₀ , aₛ).
Note that rec_ℕ is defined in such a way that f(0) :=  a₀,
the first term in our sequence,
and f(succ(n)) is defined as aₛ(n,f(n)).
Let's take a look at an example.
Suppose we wanted to define the function factorial.
How would we go about that?
Well, firstly note that 0! is equal to 1,
and secondly, note that (n + 1)! is equal to (n + 1)n!.
This allows us to define a₀ and aₛ,
which in turn allows us to define factorial using the recursor.
Type theorists so frequently define functions  this way that they have a name for it.
They call it pattern matching.
We now know how to use recursors in type theory.
Thanks for watching.

# #14 Homotopy Type Theory Explained: Inductors

In the previous video,
we learned how to construct functions using recursors.
But in this video,
we are going to generalise that notion to dependent functions.
We are going to investigate inductors.
Let's get started.
Suppose we wanted to construct a dependent function
from the natural numbers to a type in the type family B.
We can then define the inductor for natural numbers   
in a similar way we defined the recursor.
We start by picking a type family
from the natural numbers to some universe.
Let's call it C.
We then pick a term in the type that C sends the term 0 to. 
Next we pick a function that,
given some n : ℕ,
defines a function from C(n) to C(succ(n)).
Finally, we are left with a dependent function
that maps every term n : ℕ to the type C(n). 
Note that the inductor for natural numbers
is a generalisation of the recursor  for natural numbers.
In other words,  
the recursor is simply a special case where we  define the inductor for a constant type family.
So, how do we define f?
Well, we do it the same way we did with a recursor.
We apply the inductor to B, b₀, bₛ.
And similar to the recursor,
we define f(0) to be equal to b₀,
and f(succ(n)) to be equal to bₛ applied to n, f(n).
But we can go one step further.
We can apply inductors to propositions.  
For example,
to construct a proof
that the proposition P is true for every natural number,  
we need only construct two terms.
Firstly, we construct a term in P(0).
We call this the base case.
Secondly, we need to construct a function that
given some proof that P(n) is true,
it returns a proof that P(succ(n)) is  true.
We call this the induction step.
It may now become clear that this is none other
than the type theoretic analogue of mathematical induction.
Thanks for watching.

# #15 Homotopy Type Theory Explained: Higher Inductive Types, Circle, Sphere

So far we have used inductive types
to represent finite sets and infinite sets.
But in this video we are going up a level.
We are going to investigate higher inductive types. 
Let's take a look at an example.
Suppose we had a space
and in the middle of the space there's a big hole.
How would we represent this as an inductive type?
We can start by adding the constructor base. 
But now comes the part where higher inductive types are different from ordinary sets.
We can add path constructors.
Let us add the path constructor loop from base to itself.
Note that we still have the path refl from base to itself.
We can think of refl as a path that we can contract to a single point.
Note that we do not have a path constructor from loop to refl.
This reflects the fact that we can't draw a homotopy from loop to refl.
There is a hole in the way.
We call this type S¹.
It is also sometimes called the circle type
because any space that can be expressed this way
can be deformed into a circle.
But we can go one step further.
We can represent a sphere.  
We start with a base point
and then we add a path of paths from refl_base to refl_base.
We call it surf since this represents the surface of our sphere.
Let's see what this homotopy looks like.
Note that surf isn't equal to refl_refl_base
since, again, there's a hole in the middle.
And yes, if you were wondering,
we can use this method to represent any n-dimensional sphere.
But who knows how to draw  that?
We now know how to construct higher inductive types
in homotopy type theory.
Thanks for watching.

# #16 Homotopy Type Theory Explained: Torus, Transitivity

In the previous video,
we learned about higher inductive types
and how they can be used
to describe different kinds of spaces.
In this video, however, we are going to describe a shape
that is a staple among topologists.
We are going to investigate
the torus.
But first, there is something important
which we should know about equality types.
Recall that we used the path induction principle
to prove that for every path from x to y,
there is a path from y to x.
In other words, equalities are symmetrical.
But what if we wanted to prove
that equalities
are transitive?
This would mean that we could construct a function,
let's call it trans,
that given a path p from x to y,
and a path q from y to z,
we have a path
p ⚬ q from x to z.
Let's see how we can prove this.
Note that applying trans to x, y, z, p, q
should give us a path from x to z.
But how do we define such a path?
We can start by applying the path induction principle to p.
In that case, y is definitionally equal to x
and p is defined as a refl.
We apply the same procedure to the path q
so that we only have to define a path
from x to x.
We let this path be reflₓ.
And thus we have proven
that equality types are transitive.
We can also use path induction to prove
things like reflₓ⚬ p = p
and p⚬p⁻¹ = reflₓ
We can even prove that composition is associative
and that the inverse of the inverse of
some path p is equal to p.
It follows that whenever we define a path like, say,
loop in S¹,
we are not just defining one path.
We are defining infinitely many paths.
And now for the moment we've all been waiting for:
We are going to use path composition
to define
a torus.
We start with a base point.
We then add a path p from base to base.
We then add another path q from base to base.
And then finally,
to define the surface of our torus,
we add a path of paths from p⚬q to q⚬p.
We now know how to define a torus
in homotopy type theory.
If you like this series, you can support me on Ko-fi.
The link is in the description.
Thanks for watching.

# #17 Homotopy Type Theory Explained: Fibrations, Transport

The time has come.
We have reached the point in our journey
where we are ready to tackle...
fibrations.
But first we should discuss the  transport function.
Let's see how it works.
Suppose we had the terms x, y : A, a path p from x to y,
and a type family capital P indexed by A.
We could then construct a transport function from P(x) to P(y).
If P were a proposition,
this would mean that if we had proof that P(x) is true
and that x is equal to y,
we would have proof that P(y) is true.
We can construct the transport function using path induction
with a base case: transportᴾ (reflₓ) is equal to the identity function
— that being the function that, given an input x, returns x.
Note that we can abbreviate transportᴾ(p) as p⁎.
All right then. But what is a fibration?
Well, suppose we had a space A
and that above A there lay another space.
We can then speak of a type family P that sends every point in A
to a type of points lying above it.
We call these types fibres.
In other words, the space lying above A
can be expressed as the Σ-type of all the fibres in the type family P.
We call it the total space.
And A is called the base space.
Now this is where the transport function comes in.
Suppose we had the term u : P(x)
and let us assume that there is a path p from x to y
such that we can construct the transport function p⁎ from P(x) to P(y).
By applying p⁎ to u, it follows that
if we have a point in a fibre, we can construct a point in another fibre
as long as those fibres are connected in the base space.
We now know how to do fibrations in homotopy type theory.
Thanks for watching.

# #18 Homotopy Type Theory Explained: Path-lifting

In the previous video, we learned about fibrations
and how to construct terms in a total space using the transport function.
But in this video, instead of constructing points in the total space,
we will construct paths.
But first we must learn how  to construct paths between pairs.
Suppose we had the pairs (a,b) and (c,d) inhabiting the type A × B.
We can then speak of a pair of paths (p,q)  inhabiting the type a=c × b=d.
We can then apply the function pair⁼ to our pair of paths to get a path between pairs.
But what about dependent pairs?
Well, suppose we did have the pairs (x,u) and (y,v) inhabiting the Σ-type "Σ P(a)"
where P is some type family.
Note that we can't speak of a path between dependent pairs
in the same way we did with non-dependent pairs
since u and v are not of the same type
and thus we can't speak of the  equality type u=v.
So here's what we do.
We construct a pair of paths (w,r)
where w is a path from x to y and r is a path from p⁎(u) to v.
We can do this since p⁎(u) is a term in P(y).
We can then apply the function pair equals to our pair of paths
to get a path between dependent pairs.
We can now construct paths in a total space.
Let's see how it is done.
Suppose we wanted to find a path between the terms (x,u) and (y,p⁎(u))
in the total space.
If we were to construct a path between these pairs
in the same way we constructed a path between (x,u) and (y,v) earlier,
we need only construct a pair of paths in the following Σ-type.
For the first term, we already have the  path p from x to y.
And for the second term, we pick the path reflₚ⁎₍ᵤ₎.
We can then apply pair⁼ to construct a path from (x,u) to (y,p⁎(u)).
Let's call this path lift(u,p).
We thus have a function that.
given a path p from x to y in the base space,
we have a path lift(u,p) from (x,u) to (y,p⁎(u)) in the total space.
Similarly, given a term v in the fibre P(x)
and a path q from x to y,
we can construct the path lift(v,q) such that it lies above q.
We now know how to lift paths in homotopy type theory.
Thanks for watching.

# #19 Homotopy Type Theory Explained: Mapping out of S¹, functoriality

So far we've learned how to construct functions
from inductive types to any other type.
But in this video we are going to learn
how to construct functions out of higher inductive types.
In particular, we are going to learn how to construct functions
out of the circle type.
But first there is something we should know about functions.
Suppose we had the type A
inhabited by the terms x and y
and that there's a function f from A to  the type B
such that we have the terms f(x) and f(y) in B.
We can then use the path induction  principle
to show that given any path p from x to y,
we can construct a path ap_f(p) from f(x) to f(y).
In other words, functions respect equality.
Mathematicians refer to this as the functoriality of functions.
Let's see it in action.
Suppose we wanted to construct a function
from the circle type to some type A.
According to the recursion principle for the circle type,
if we had a term b in A and we had a path ℓ from b to b,
there exists a function f from the circle type to A
such that f of base is definitionally equal to b
and ap_f(loop) is homotopic to ℓ.
We now know how to construct functions
out of the circle type in homotopy type theory.
Thanks for watching.

# #20 Homotopy Type Theory Explained: Sections

In the previous video, we learned
about the functoriality
of functions
and how it allows us to construct functions
out of higher inductive types.
But first,
there is something we should note about functoriality.
Recall that the functorality of functions
implies that functions map not only the points out of a type.
They also map the paths out of a type.
In other words, functions are continuous.
But what about dependent functions?
Suppose we had a type A
inhabited by the terms x and y
and we had a path p from x to y.
And suppose there were a type family P
such that we can speak of a dependent function
mapping any term x in A to the fibre P(x) lying above it.
Let's assume we have such a function f.
One would assume that for f to be continuous,
it should be possible to construct a path from f(x) to f(y).
But since f(x) and f(y) aren't of the same type, we cannot do so.
However,
we can construct a path in the total space
from (x, f(x)) to (y, p⁎(f(x))).
Then, to complete the path,
we can use the path induction principle
to construct the path apd_f(p) in the fibre lying over y
from p⁎(f(x)) to f(y).
Let's take a look at an example.
Suppose we wanted to construct a dependent function
out of the circle type,
and let us again call the type family P.
To construct our dependent function,
we only need a term b : P(base)
and we need a path ℓ from loop⁎(b) to b.
In that case, there exists a dependent function f
such that f(base) := b and apd_f(loop) is homotopic to ℓ.
It now becomes clear
that whenever we construct a dependent function
out of a higher inductive type,
we are describing a section of the total space
that looks like the base space.
That's why topologists call this a section.
We now know how to construct sections
in homotopy type theory.
Thanks for watching.

# #21 Homotopy Type Theory Explained: Contractibility, Interval Type

In the previous video, we learned how to  construct sections.
In this video, however, we are going to use sections in a very special way.
We are going to learn how to prove that a type is contractible.
But what does it mean for a type to be contractible?
Well, suppose we are given a type A.
We then say that the proposition  that A is contractible
is defined as follows.  
There exists a term c : A
such that we can construct a function
that takes any term x : A and returns a path from c to x.
In other words, a contractible type can do this.
We refer to c as the centre of the contraction.
But before we can see it in action,
we must first go back to the transport function.
Suppose we had a type B inhabited by the terms x₁, x₂ and a.
And let there be a path p from x₁ to x₂
and a path q from a to x₁.
We can then apply the transport function
to move the path q, from a to x₁, to the path p⁎(q), from a to x₂.
And yes, we can prove this using path induction.
Similarly, we can show that a path from x₁ to a
can be moved along p to a path from x₂ to a.
And a path from x₁ to itself
can be moved along p to a path from x₂ to itself.
Armed with this knowledge, we can now prove that a type is contractible.
Suppose we had a type I inhabited by the terms 0, 1, and a path called segment from 0 to 1.
We call this the interval type.
We'll pick 1 as the centre.
We then need to construct a function f
that maps every term x in the interval type to a path from x to 1.
To construct this section, we let f(0) be seg,
we let f(1) be refl,
and finally, to complete the section,
we need a path from seg⁎(f(0)) to f(1).
In other words, we need to find a path from seg⁎(seg) to refl₁.
And we can do so using one of the transport theorems from earlier.
But what about the circle type?
Well, it turns out if you want to prove that S¹ is contractible,
you have to prove that refl_base is equal to loop.
But we cannot do so since there's a hole in the middle.
In other words, for a type to be contractible,
not only need all the terms be connected,
all the holes need to be filled.
We now know how to show that a type is contractible
in homotopy type theory.
Thanks for watching.