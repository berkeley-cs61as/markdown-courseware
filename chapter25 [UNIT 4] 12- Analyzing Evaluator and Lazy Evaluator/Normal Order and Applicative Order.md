## Strict vs. Non-Strict

If the body of a procedure is entered before an argument has been evaluated we
say that the procedure is **non-strict** in that argument. If the argument is
evaluated before the body of the procedure is entered we say that the
procedure is **strict** in that argument. In a purely applicative-order
language, all procedures are strict in each argument. In a purely normal-order
language, all compound procedures are non-strict in each argument, and
primitive procedures may be either strict or non-strict. There are also
languages (see [SICP Exercise 4.31](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-27.html#%_thm_4.31)) that give programmers detailed control
over the strictness of the procedures they define.

A striking example of a procedure that can usefully be made non-strict is
`cons` (or, in general, almost any constructor for data structures). One can
do useful computation, combining elements to form data structures and
operating on the resulting data structures, even if the values of the elements
are not known. It makes perfect sense, for instance, to compute the length of
a list without knowing the values of the individual elements in the list. We
will exploit this idea later in the lesson to implement the streams of Lesson
11 as lists formed of non-strict `cons` pairs.

