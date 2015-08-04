## Is Logic Programming Mathematical Logic?

The means of combination used in the query language may at first seem
identical to the operations and, or, and not of mathematical logic, and the
application of query-language rules is in fact accomplished through a
legitimate method of inference. This identification of the query language with
mathematical logic is not really valid, though, because the query language
provides a control structure that interprets the logical statements
procedurally. We can often take advantage of this control structure. For
example, to find all of the supervisors of programmers we could formulate a
query in either of two logically equivalent forms:

    
    (and (job ?x (computer programmer))
         (supervisor ?x ?y))
    

or

    
    (and (supervisor ?x ?y)
         (job ?x (computer programmer)))
    

If a company has many more supervisors than programmers (the usual case), it
is better to use the first form rather than the second because the data base
must be scanned for each intermediate result (frame) produced by the first
clause of the and.

The aim of logic programming is to provide the programmer with techniques for
decomposing a computational problem into two separate problems: "what" is to
be computed, and "how" this should be computed. This is accomplished by
selecting a subset of the statements of mathematical logic that is powerful
enough to be able to describe anything one might want to compute, yet weak
enough to have a controllable procedural interpretation. The intention here is
that, on the one hand, a program specified in a logic programming language
should be an effective program that can be carried out by a computer. Control
("how" to compute) is effected by using the order of evaluation of the
language. We should be able to arrange the order of clauses and the order of
subgoals within each clause so that the computation is done in an order deemed
to be effective and efficient. At the same time, we should be able to view the
result of the computation ("what" to compute) as a simple consequence of the
laws of logic.

Our query language can be regarded as just such a procedurally interpretable
subset of mathematical logic. An assertion represents a simple fact (an atomic
proposition). A rule represents the implication that the rule conclusion holds
for those cases where the rule body holds. A rule has a natural procedural
interpretation: To establish the conclusion of the rule, establish the body of
the rule. Rules, therefore, specify computations. However, because rules can
also be regarded as statements of mathematical logic, we can justify any
"inference" accomplished by a logic program by asserting that the same result
could be obtained by working entirely within mathematical logic.

## Infinite Loops

A consequence of the procedural interpretation of logic programs is that it is
possible to construct hopelessly inefficient programs for solving certain
problems. An extreme case of inefficiency occurs when the system falls into
infinite loops in making deductions. As a simple example, suppose we are
setting up a data base of famous marriages, including

    
    (assert! (married Minnie Mickey))
    

If we now ask

    
    (married Mickey ?who)
    

we will get no response, because the system doesn't know that if A is married
to B, then B is married to A. So we assert the rule

    
    (assert! (rule (married ?x ?y)
                   (married ?y ?x)))
    

and again query

    
    (married Mickey ?who)
    

Unfortunately, this will drive the system into an infinite loop, as follows:

  * The system finds that the married rule is applicable; that is, the rule conclusion `(married ?x ?y)` successfully unifies with the query pattern `(married Mickey ?who)` to produce a frame in which `?x` is bound to Mickey and `?y` is bound to `?who`. So the interpreter proceeds to evaluate the rule body `(married ?y ?x)` in this frame -- in effect, to process the query `(married ?who Mickey)`.
  * One answer appears directly as an assertion in the data base: `(married Minnie Mickey).`
  * The married rule is also applicable, so the interpreter again evaluates the rule body, which this time is equivalent to `(married Mickey ?who)`.

The system is now in an infinite loop. Indeed, whether the system will find
the simple answer `(married Minnie Mickey)` before it goes into the loop
depends on implementation details concerning the order in which the system
checks the items in the data base. This is a very simple example of the kinds
of loops that can occur. Collections of interrelated rules can lead to loops
that are much harder to anticipate, and the appearance of a loop can depend on
the order of clauses in an `and` or on low-level details concerning the order
in which the system processes queries.

## Problems with `not`

Another quirk in the query system concerns `not`. Given the Microshaft data
base introduced earlier, consider the following two queries:

    
    (and (supervisor ?x ?y)
         (not (job ?x (computer programmer))))
    (and (not (job ?x (computer programmer)))
         (supervisor ?x ?y))
    

These two queries do not produce the same result. The first query begins by
finding all entries in the data base that match` (supervisor ?x ?y)`, and then
filters the resulting frames by removing the ones in which the value of `?x`
satisfies` (job ?x (computer programmer))`. The second query begins by
filtering the incoming frames to remove those that can satisfy `(job ?x (computer programmer))`. Since the only incoming frame is empty, it checks the
data base to see if there are any patterns that satisfy `(job ?x (computer programmer))`. Since there generally are entries of this form, the not clause
filters out the empty frame and returns an empty stream of frames.
Consequently, the entire compound query returns an empty stream.

The trouble is that our implementation of not really is meant to serve as a
filter on values for the variables. If a not clause is processed with a frame
in which some of the variables remain unbound (as does `?x` in the example
above), the system will produce unexpected results. Similar problems occur
with the use of `lisp-value` -- the Lisp predicate can't work if some of its
arguments are unbound.

There is also a much more serious way in which the `not` of the query language
differs from the not of mathematical logic. In logic, we interpret the
statement "not P" to mean that P is not true. In the query system, however,
"not P" means that P is not deducible from the knowledge in the data base. For
example, given the Microshaft data base, the system would happily deduce all
sorts of not statements, such as that Ben Bitdiddle is not a baseball fan,
that it is not raining outside, and that 2 + 2 is not 4.78 In other words, the
not of logic programming languages reflects the so-called closed world
assumption that all relevant information has been included in the data base.

## Takeaways

In this subsection, you learned:

  * Logical programming is a procedurally interpretable subset of mathematical logic.
  * There are pitfalls: loops and `not`.

