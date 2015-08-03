## Lazy Evaluator

To start, get our version of the lazy evaluator:

    cp ~cs61as/lib/lazy.scm .

Now that we have an evaluator expressed as a Lisp program, we can experiment
with alternative choices in language design simply by modifying the evaluator.
Indeed, new languages are often invented by first writing an evaluator that
embeds the new language within an existing high-level language.

For example, if we wish to discuss some aspect of a proposed modification to
Lisp with another member of the Lisp community, we can supply an evaluator
that embodies the change. The recipient can then experiment with the new
evaluator and send back comments as further modifications. Not only does the
high-level implementation base make it easier to test and debug the evaluator;
in addition, the embedding enables the designer to snarf features from the
underlying language, just as our embedded Lisp evaluator uses primitives and
control structure from the underlying Lisp. Only later (if ever) need the
designer go to the trouble of building a complete implementation in a low-
level language or in hardware.

In this section and the next we explore some variations on Scheme that provide
significant additional expressive power.

## Review of Normal and Applicative Order

In Lesson 1, where we began our discussion of models of evaluation, we noted
that Scheme is an applicative-order language, namely, that all the arguments
to Scheme procedures are evaluated when the procedure is applied. In contrast,
normal-order languages delay evaluation of procedure arguments until the
actual argument values are needed. Delaying evaluation of procedure arguments
until the last possible moment (e.g., until they are required by a primitive
operation) is called lazy evaluation.

Consider the procedure
    
    
    (define (try a b)
      (if (= a 0) 1 b))
    

Evaluating `(try 0 (/ 1 0))` generates an error in Scheme. With lazy
evaluation, there would be no error. Evaluating the expression would return 1,
because the argument `(/ 1 0)` would never be evaluated.

An example that exploits lazy evaluation is the definition of a procedure
`unless`

    (define (unless condition usual-value exceptional-value)
        (if condition
            exceptional-value
            usual-value)) 

that can be used in expressions such as

    (unless (= b 0)
            (/ a b)
            (begin (display "exception: returning 0")
                   0))

This won't work in an applicative-order language because both the usual value
and the exceptional value will be evaluated before `unless` is called. An
advantage of lazy evaluation is that some procedures, such as `unless`, can do
useful computation even if evaluation of some of their arguments would produce
errors or would not terminate.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>

Consider the following:

<pre><code>> (define (double x) (+ x x))
double
> (double (+ 2 1))
6</code></pre>

In applicative order, how many times does <code>+</code> get called?

<ans text="Click to show answer." explanation="2" correct></ans>
<br><br>

In normal order, how many times does <code>+</code> get called?

<ans text="Click to show answer." explanation="3" correct></ans>
</div>

## Strict vs. Non-Strict

If the body of a procedure is entered before an argument has been evaluated we
say that the procedure is **non-strict** in that argument. If the argument is
evaluated before the body of the procedure is entered we say that the
procedure is **strict** in that argument. In a purely applicative-order
language, all procedures are strict in each argument. In a purely normal-order
language, all compound procedures are non-strict in each argument, and
primitive procedures may be either strict or non-strict. There are also
languages (see [SICP Exercise 4.31](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-27.html#%_thm_4.31)) that give programmers detailed control
over the strictness of the procedures they define.

A striking example of a procedure that can usefully be made non-strict is
`cons` (or, in general, almost any constructor for data structures). One can
do useful computation, combining elements to form data structures and
operating on the resulting data structures, even if the values of the elements
are not known. It makes perfect sense, for instance, to compute the length of
a list without knowing the values of the individual elements in the list. We
will exploit this idea later in the lesson to implement the streams of Lesson
11 as lists formed of non-strict `cons` pairs.

