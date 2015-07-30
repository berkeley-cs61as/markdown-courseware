## metacircular evaluator

Do you remember Racket-1 in Lesson 6? Now it's time to explore how Scheme
evaluates expressions!

## prerequisites and what to expect

A good understanding of how Racket-1 works will be helpful in this chapter.
There's a lot of code to understand in this chapter, perhaps more so than previous sections. Don't be afraid to ask questions!

## Readings

These are the relevant readings for this lesson:

  * [SICP Intro to Chapter 4](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-25.html)
  * [SICP 4.1.1-6](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html)
  * [Lectures Notes](http://www-inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=78)

## what is an evaluator?

So far, we learned how to write procedures that output what we want. Once we
define those procedures and type them in the Scheme prompt, we get the value.
But have you wondered how those procedures actually get evaluated and work in
Scheme (you probably did in Lesson 6)? How does Scheme know what the
expression means? Well, there's an evaluator.

An **evaluator** (or **interpreter**) for a programming language is a
procedure that, when applied to an expression of the language, performs the
actions required to evaluate that expression.

_Wait, what? The evaluator is just a procedure?_

Yes, it is. The evaluator is just another program!

## what is the metacircular evaluator?

![](http://mitpress.mit.edu/sicp/full-text/sicp/book/chapter-4/figs/eval-
apply.gif)

  
Our evaluator for Scheme will be implemented as a Scheme program. It may seem
circular to think about evaluating Scheme programs using an evaluator that is
itself implemented in Scheme. However, evaluation is a process, so it is
appropriate to describe the evaluation process using Scheme, which, after all,
is our tool for describing processes. An evaluator that is written in the same
language that it evaluates is said to be metacircular.

The metacircular evaluator is essentially a Scheme formulation of the
environment model of evaluation described in Lesson 8. Recall that the model
has two basic parts:

* To evaluate a combination (a compound expression other than a special form), evaluate the subexpressions and then apply the value of the operator subexpression to the values of the operand subexpressions.
* To apply a compound procedure to a set of arguments, evaluate the body of the procedure in a new environment. To construct this environment, extend the environment part of the procedure object by a frame in which the formal parameters of the procedure are bound to the arguments to which the procedure is applied.

These two rules describe the essence of the evaluation process, a basic cycle
in which expressions to be evaluated in environments are reduced to procedures
to be applied to arguments, which in turn are reduced to new expressions to be
evaluated in new environments, and so on, until we get down to symbols, whose
values are looked up in the environment, and to primitive procedures, which
are applied directly. This evaluation cycle will be embodied by the interplay
between the two critical procedures in the evaluator, `eval` and `apply`,
which we will go through the details soon.

The implementation of the evaluator will depend upon procedures that define
the syntax of the expressions to be evaluated. We will use data abstraction to
make the evaluator independent of the representation of the language. For
example, rather than committing to a choice that an assignment is to be
represented by a list beginning with the symbol `set!` we use an abstract
predicate `assignment?` to test for an assignment, and we use abstract
selectors `assignment-variable` and `assignment-value` to access the parts of
an assignment. We will learn the implementation of expressions and operations
that specify the representation of procedures and environments. For example,
`make-procedure` constructs compound procedures, `lookup-variable-value`
accesses the values of variables, and `apply-primitive-procedure` applies a
primitive procedure to a given list of arguments.

## takeaways

In this subsection, you learned:

  1. The definition of evaluator
  2. The definition of metacircular evaluator

## what's next?

Now it's time to understand how Scheme actually works! Exciting!

