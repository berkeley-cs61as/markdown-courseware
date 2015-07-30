## Exercise 0.
Some warmup questions to check your understanding:

- List all the procedures in the metacircular evaluator that call `eval`.
- List all the procedures in the metacircular evaluator that call `apply`.
- Explain why `make-procedure` does not call `eval`.

## A Note on Homework 11

Some students have complained that this week's homework is very time-
consuming.

Accordingly, with some reluctance, we've marked a few exercises as optional;
these are the ones to leave out if you're really pressed for time. But it's
much better if you do all of them!

The optional ones have * next to them.

## Template

You can copy the template for this homework by typing the following in your
terminal:

    
      cp ~cs61as/autograder/templates/hw11.scm .
    

Or, you can download it
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw11.scm).

## Exercise 1.

  
Abelson & Sussman, exercises [4.3, 4.6, 4.7*,
4.10*](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.3), [4.11*,
4.13](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.11), [4.14](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-26.html#%_thm_4.14), and
[4.15](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.15).

## Exercise 4.
  
Abelson & Sussman, exercises [4.1](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.1), [4.2, 4.4, and
4.5](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html#%_thm_4.2).

## Exercise 2*.

  
Modify the metacircular evaluator to allow type-checking of arguments to
procedures. Here is how the feature should work. When a new procedure is
defined, a formal parameter can be either a symbol as usual or else a list of
two elements. In this case, the second element is a symbol, the name of the
formal parameter. The first element is an expression whose value is a
predicate function that the argument must satisfy. That function should return
`#t` if the argument is valid. For example, here is a procedure foo that has
typechecked parameters num and list:

```
> (define (foo (integer? num) ((lambda (x) (not (null? x))) lst))
    (list-ref lst num))
> (foo 3 '(a b c d e))
d
> (foo 3.5 `(a b c d e))
Error: wrong argument type -- 3.5
> (foo 2 '())
Error: wrong argument type -- ()
```

In this example we define a procedure `foo` with two formal parameters, named
`num` and `list`. When `foo` is invoked, the evaluator will check to see that
the first actual argument is an integer and that the second actual argument is
not empty. The expression whose value is the desired predicate function should
be evaluated with respect to `foo`'s defining environment. (Hint: Think about
extend-environment.)

## More Challenge Problems
 Here are some more optional exercises if you're interested in this section. These exercises are not for credit. 

- Abelson & Sussman, exercises [4.16 - 4.21](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_thm_4.16).
