## Introduction

In this section we give an overview that explains the general structure of the
system independent of low-level implementation details. After describing the
implementation of the interpreter, we will be in a position to understand some
of its limitations and some of the subtle ways in which the query language's
logical operations differ from the operations of mathematical logic.

It should be apparent that the query evaluator must perform some kind of
search in order to match queries against facts and rules in the data base. One
way to do this would be to implement the query system as a nondeterministic
program (you don't have to worry about this way). Another possibility is to
manage the search with the aid of streams. Our implementation follows this
second approach.

The query system is organized around two central operations called **pattern
matching** and **unification**. We first describe pattern matching and explain
how this operation, together with the organization of information in terms of
streams of frames, enables us to implement both simple and compound queries.

We next discuss unification, a generalization of pattern matching needed to
implement rules. Finally, we show how the entire query interpreter fits
together through a procedure that classifies expressions in a manner analogous
to the way `eval` classifies expressions for the metacircular evaluator.

## Pattern Matching

A pattern matcher is a program that tests whether some datum fits a specified
pattern. For example, the data list `((a b) c (a b))` matches the pattern `(?x
c ?x)` with the pattern variable `?x` bound to` (a b)`. The same data list
matches the pattern` (?x ?y ?z)` with` ?x` and` ?z` both bound to` (a b)` and`
?y` bound to` c`. It also matches the pattern` ((?x ?y) c (?x ?y))` with` ?x`
bound to` a` and` ?y` bound to `b`. However, it does not match the pattern`
(?x a ?y)`, since that pattern specifies a list whose second element is the
symbol` a`.

The pattern matcher used by the query system takes as inputs a pattern (e.g.
`(?x c ?x))`, a datum (e.g. `((a b) c (a b))`), and a frame that specifies
bindings for various pattern variables. It checks whether the datum matches
the pattern in a way that is consistent with the bindings already in the
frame. If so, it returns the given frame augmented by any bindings that may
have been determined by the match. Otherwise, it indicates that the match has
failed.

For example, using the pattern` (?x ?y ?x)` to match the datum` (a b a)` given
an empty frame will return a frame specifying that` ?x` is bound to` a` and`
?y` is bound to `b`. Trying the match with the same pattern, the same datum,
and a frame specifying that `?y` is bound to `a` will fail. Trying the match
with the same pattern, the same datum, and a frame in which` ?y` is bound to
`b` and` ?x` is unbound will return the given frame augmented by a binding of`
?x` to` a`.

The pattern matcher is all the mechanism that is needed to process simple
queries that don't involve rules. For instance, to process the query

    
    (job ?x (computer programmer))
    

we scan through all assertions in the data base and select those that match
the pattern with respect to an initially empty frame. For each match we find,
we use the frame returned by the match to instantiate the pattern with a value
for` ?x`.

## Streams of Frames

The testing of patterns against frames is organized through the use of
streams. Given a single frame, the matching process runs through the data-base
entries one by one. For each data-base entry, the matcher generates either a
special symbol indicating that the match has failed or an extension to the
frame. The results for all the data-base entries are collected into a stream,
which is passed through a filter to weed out the failures. The result is a
stream of all the frames that extend the given frame via a match to some
assertion in the data base.

In our system, a query takes an input stream of frames and performs the above
matching operation for every frame in the stream, as indicated in the figure
below. That is, for each frame in the input stream, the query generates a new
stream consisting of all extensions to that frame by matches to assertions in
the data base. All these streams are then combined to form one huge stream,
which contains all possible extensions of every frame in the input stream.
This stream is the output of the query.

![](http://mitpress.mit.edu/sicp/full-text/book/ch4-Z-G-4.gif)

To answer a simple query, we use the query with an input stream consisting of
a single empty frame. The resulting output stream contains all extensions to
the empty frame (that is, all answers to our query). This stream of frames is
then used to generate a stream of copies of the original query pattern with
the variables instantiated by the values in each frame, and this is the stream
that is finally printed.

## Compound Queries

The real elegance of the stream-of-frames implementation is evident when we
deal with compound queries. The processing of compound queries makes use of
the ability of our matcher to demand that a match be consistent with a
specified frame. For example, to handle the and of two queries, such as

    
    (and (can-do-job ?x (computer programmer trainee))
         (job ?person ?x))
    

(informally, "Find all people who can do the job of a computer programmer
trainee"), we first find all entries that match the pattern

    
    (can-do-job ?x (computer programmer trainee))
    

This produces a stream of frames, each of which contains a binding for ?x.
Then for each frame in the stream we find all entries that match

    
    (job ?person ?x)
    

in a way that is consistent with the given binding for ?x. Each such match
will produce a frame containing bindings for ?x and ?person. The and of two
queries can be viewed as a series combination of the two component queries, as
shown in the figure below. The frames that pass through the first query filter
are filtered and further extended by the second query.

![](http://mitpress.mit.edu/sicp/full-text/book/ch4-Z-G-5.gif)

The and combination of two queries is produced by operating on the stream of
frames in series.

The figure below shows the analogous method for computing the or of two
queries as a parallel combination of the two component queries. The input
stream of frames is extended separately by each query. The two resulting
streams are then merged to produce the final output stream.

![](http://mitpress.mit.edu/sicp/full-text/book/ch4-Z-G-6.gif)

The or combination of two queries is produced by operating on the stream of
frames in parallel and merging the results.

Even from this high-level description, it is apparent that the processing of
compound queries can be slow. For example, since a query may produce more than
one output frame for each input frame, and each query in an` and` gets its
input frames from the previous query, an` and` query could, in the worst case,
have to perform a number of matches that is exponential in the number of
queries. Though systems for handling only simple queries are quite practical,
dealing with complex queries is extremely difficult.

From the stream-of-frames viewpoint, the not of some query acts as a filter
that removes all frames for which the query can be satisfied. For instance,
given the pattern

    
    (not (job ?x (computer programmer)))
    

we attempt, for each frame in the input stream, to produce extension frames
that satisfy` (job ?x (computer programmer))`. We remove from the input stream
all frames for which such extensions exist. The result is a stream consisting
of only those frames in which the binding for` ?x` does not satisfy` (job ?x
(computer programmer))`. For example, in processing the query

    
    (and (supervisor ?x ?y)
         (not (job ?x (computer programmer))))
    

the first clause will generate frames with bindings for `?x` and` ?y`. The not
clause will then filter these by removing all frames in which the binding for
`?x` satisfies the restriction that `?x` is a computer programmer.

The `lisp-value` special form is implemented as a similar filter on frame
streams. We use each frame in the stream to instantiate any variables in the
pattern, then apply the Lisp predicate. We remove from the input stream all
frames for which the predicate fails.

## Unification

In order to handle rules in the query language, we must be able to find the
rules whose conclusions match a given query pattern. Rule conclusions are like
assertions except that they can contain variables, so we will need a
generalization of pattern matching-- called unification--in which both the
"pattern" and the "datum" may contain variables.

A unifier takes two patterns, each containing constants and variables, and
determines whether it is possible to assign values to the variables that will
make the two patterns equal. If so, it returns a frame containing these
bindings. For example, unifying `(?x a ?y)` and `(?y ?z a)` will specify a
frame in which` ?x, ?y,` and` ?z` must all be bound to` a`. On the other hand,
unifying` (?x ?y a)` and` (?x b ?y)` will fail, because there is no value for
`?y` that can make the two patterns equal. (For the second elements of the
patterns to be equal, `?y` would have to be `b`; however, for the third
elements to be equal, `?y` would have to be` a`.) The unifier used in the
query system, like the pattern matcher, takes a frame as input and performs
unifications that are consistent with this frame.

The unification algorithm is the most technically difficult part of the query
system. With complex patterns, performing unification may seem to require
deduction. To unify` (?x ?x)` and `((a ?y c) (a b ?z))`, for example, the
algorithm must infer that `?x` should be `(a b c)`, `?y` should be `b,` and
`?z` should be `c`. We may think of this process as solving a set of equations
among the pattern components. In general, these are simultaneous equations,
which may require substantial manipulation to solve. For example, unifying`
(?x ?x)` and` ((a ?y c) (a b ?z))` may be thought of as specifying the
simultaneous equations

    
    ?x  =  (a ?y c)
    ?x  =  (a b ?z)
    

These equations imply that

    
    (a ?y c)  =  (a b ?z)
    

which in turn implies that

    
    a  =  a, ?y  =  b, c  =  ?z,
    

and hence that

    
    ?x  =  (a b c)
    

In a successful pattern match, all pattern variables become bound, and the
values to which they are bound contain only constants. This is also true of
all the examples of unification we have seen so far. In general, however, a
successful unification may not completely determine the variable values; some
variables may remain unbound and others may be bound to values that contain
variables.

Consider the unification of` (?x a)` and` ((b ?y) ?z)`. We can deduce that` ?x
= (b ?y)` and` a = ?z`, but we cannot further solve for `?x` or` ?y`. The
unification doesn't fail, since it is certainly possible to make the two
patterns equal by assigning values to` ?x` and` ?y.` Since this match in no
way restricts the values` ?y` can take on, no binding for` ?y` is put into the
result frame. The match does, however, restrict the value of `?x`. Whatever
value `?y` has, `?x` must be` (b ?y)`. A binding of `?x` to the pattern` (b
?y)` is thus put into the frame. If a value for` ?y` is later determined and
added to the frame (by a pattern match or unification that is required to be
consistent with this frame), the previously bound `?x` will refer to this
value.

## Applying Rules

Unification is the key to the component of the query system that makes
inferences from rules. To see how this is accomplished, consider processing a
query that involves applying a rule, such as

    
    (lives-near ?x (Hacker Alyssa P))
    

To process this query, we first use the ordinary pattern-match procedure
described above to see if there are any assertions in the data base that match
this pattern. (There will not be any in this case, since our data base
includes no direct assertions about who lives near whom.) The next step is to
attempt to unify the query pattern with the conclusion of each rule. We find
that the pattern unifies with the conclusion of the rule

    
    (rule (lives-near ?person-1 ?person-2)
          (and (address ?person-1 (?town . ?rest-1))
               (address ?person-2 (?town . ?rest-2))
               (not (same ?person-1 ?person-2))))
    

resulting in a frame specifying that `?person-2` is bound to `(Hacker Alyssa
P)` and that` ?x` should be bound to (have the same value as) `?person-1`.
Now, relative to this frame, we evaluate the compound query given by the body
of the rule. Successful matches will extend this frame by providing a binding
for `?person-1`, and consequently a value for` ?x,` which we can use to
instantiate the original query pattern.

In general, the query evaluator uses the following method to apply a rule when
trying to establish a query pattern in a frame that specifies bindings for
some of the pattern variables:

  * Unify the query with the conclusion of the rule to form, if successful, an extension of the original frame.
  * Relative to the extended frame, evaluate the query formed by the body of the rule.

Notice how similar this is to the method for applying a procedure in the
eval/apply evaluator for Lisp:

  * Bind the procedure's parameters to its arguments to form a frame that extends the original procedure environment.
  * Relative to the extended environment, evaluate the expression formed by the body of the procedure.

The similarity between the two evaluators should come as no surprise. Just as
procedure definitions are the means of abstraction in Lisp, rule definitions
are the means of abstraction in the query language. In each case, we unwind
the abstraction by creating appropriate bindings and evaluating the rule or
procedure body relative to these.

## Simple Queries

We saw earlier in this section how to evaluate simple queries in the absence
of rules. Now that we have seen how to apply rules, we can describe how to
evaluate simple queries by using both rules and assertions.

Given the query pattern and a stream of frames, we produce, for each frame in
the input stream, two streams:

  * a stream of extended frames obtained by matching the pattern against all assertions in the data base (using the pattern matcher), and
  * a stream of extended frames obtained by applying all possible rules (using the unifier).

Appending these two streams produces a stream that consists of all the ways
that the given pattern can be satisfied consistent with the original frame.
These streams (one for each frame in the input stream) are now all combined to
form one large stream, which therefore consists of all the ways that any of
the frames in the original input stream can be extended to produce a match
with the given pattern.

## The Query Evaluator and the Driver Loop

Despite the complexity of the underlying matching operations, the system is
organized much like an evaluator for any language. The procedure that
coordinates the matching operations is called` qeval`, and it plays a role
analogous to that of the eval procedure for Lisp. `Qeval` takes as inputs a
query and a stream of frames. Its output is a stream of frames, corresponding
to successful matches to the query pattern, that extend some frame in the
input stream. Like `eval`, `qeval` classifies the different types of
expressions (queries) and dispatches to an appropriate procedure for each.
There is a procedure for each special form (`and, or, not, and lisp-value`)
and one for simple queries.

The driver loop, which is analogous to the `driver-loop` procedure for the
other evaluators in this chapter, reads queries from the terminal. For each
query, it calls `qeval` with the query and a stream that consists of a single
empty frame. This will produce the stream of all possible matches (all
possible extensions to the empty frame). For each frame in the resulting
stream, it instantiates the original query using the values of the variables
found in the frame. This stream of instantiated queries is then printed.

The driver also checks for the special command `assert!`, which signals that
the input is not a query but rather an assertion or rule to be added to the
data base. For instance,

    
    (assert! (job (Bitdiddle Ben) (computer wizard)))
    (assert! (rule (wheel ?person)
                   (and (supervisor ?middle-manager ?person)
                        (supervisor ?x ?middle-manager))))
    

## An Example

Here’s an example, partly traced:

    
    
    ;;; Query input:
    (assert! (rule (append () ?y ?y)))
    
    ;;; Query input:
    (assert! (rule (append (?u . ?v) ?y (?u . ?z))
                   (append ?v ?y ?z)))
    
    ;;; Query input:
    (append ?a ?b (aa bb))
    
    (unify-match (append ?a ?b (aa bb))   ; MATCH ORIGINAL QUERY
                 (append () ?1y ?1y)      ; AGAINST BASE CASE RULE
                 ())                      ; WITH NO CONSTRAINTS
    
    RETURNS: ((?1y . (aa bb)) (?b . ?1y) (?a . ()))
    PRINTS: (append () (aa bb) (aa bb))
    

Since the base-case rule has no body, once we’ve matched it, we can print a
successful result. (Before printing, we have to look up variables in the
environment so what we print is variable-free.)

Now we unify the original query against the conclusion of the other rule:

    
    
    (unify-match (append ?a ?b (aa bb))               ; MATCH ORIGINAL QUERY
                 (append (?2u . ?2v) ?2y (?2u . ?2z)) ; AGAINST RECURSIVE RULE
                 ())                                  ; WITH NO CONSTRAINTS
    
    RETURNS: ((?2z . (bb)) (?2u . aa) (?b . ?2y) (?a . (?2u . ?2v)))
             [call it F1]
    

This was successful, but we’re not ready to print anything yet, because we now
have to take the body of that rule as a new query. Note the indenting to
indicate that this call to unify-match is within the pending rule.

    
    
        (unify-match (append ?2v ?2y ?2z)   ; MATCH BODY OF RECURSIVE RULE
                     (append () ?3y ?3y)    ; AGAINST BASE CASE RULE
                     F1)                    ; WITH CONSTRAINTS FROM F1
    
        RETURNS: ((?3y . (bb)) (?2y . ?3y) (?2v . ()) [plus F1])
        PRINTS: (append (aa) (bb) (aa bb))
    
        (unify-match (append ?2v ?2y ?2z)                 ; MATCH SAME BODY
                     (append (?4u . ?4v) ?4y (?4u . ?4z)) ; AGAINST RECURSIVE RULE
                     F1)                                  ; WITH F1 CONSTRAINTS
    
        RETURNS: ((?4z . ()) (?4u . bb) (?2y . ?4y) (?2v . (?4u . ?4v))
                 [plus F1]) [call it F2]
    
            (unify-match (append ?4v ?4y ?4z) ; MATCH BODY FROM NEWFOUND MATCH
                         (append () ?5y ?5y)  ; AGAINST BASE CASE RULE
                         F2)                  ; WITH NEWFOUND CONSTRAINTS
    
            RETURNS: ((?5y . ()) (?4y . ?5y) (?4v . ()) [plus F2])
            PRINTS: (append (aa bb) () (aa bb))
    
            (unify-match (append ?4v ?4y ?4z)                 ; MATCH SAME BODY
                         (append (?6u . ?6v) ?6y (?6u . ?6z)) ; AGAINST RECURSIVE RULE
                         F2)                                  ; SAME CONSTRAINTS
    
            RETURNS: ()                                       ; BUT THIS FAILS
    

## Takeaways

Here are several takeaways from this subsection:

  * Simple queries are processed with the pattern matcher.
  * To process compound queries, the pattern matcher needs to check if a match is consistent with a specified frame.
  * Rules are handled with unification.

## what's next?

In the next subsection, we are going to talk about the relation between
logical programming and mathematical logic.

