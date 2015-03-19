## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

`cp ~cs61as/autograder/templates/hw9.scm .`

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw9.scm).

## Exercise 1.

  
Suppose that the following definitions have been provided.

`(define x (cons 1 3))`

`(define y 2) `

A CS 61AS student, intending to change the value of `x` to a pair with `car`
equal to `1` and `cdr` equal to `2`, types the expression `(set! (cdr x) y)`
instead of `(set-cdr! x y)` and gets an error. Explain why.

## Exercise 2.

  
a. Provide the arguments for the two `set-cdr!` operations in the blanks below
to produce the indicated effect on `list1` and `list2`. Do not create any new
pairs; just rearrange the pointers to the existing ones.

`> (define list1 (list (list 'a) 'b))`

` list1 `

`> (define list2 (list (list 'x) 'y))`

` list2 `

`> (set-cdr! ________ ________)`

` okay `

`> (set-cdr! ________ ________)`

` okay `

`> list1`

` ((a x b) b) `

`> list2`

` ((x b) y) `

b. After filling in the blanks in the code above and producing the specified
effect on `list1` and `list2`, draw a box-and-pointer diagram that explains
the effect of evaluating the expression `(set-car! (cdr list1) (cadr list2))`.

## Exercise 3.

  
Exercises [3.13 and 3.14](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-22.html#%_thm_3.13) in Abelson & Sussman

## Exercise 4.

  
Exercises [3.16, 3.17](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-22.html#%_thm_3.16), [3.21](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-22.html#%_thm_3.21), [3.25, and
3.27](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-22.html#%_thm_3.25)
in Abelson & Sussman

You don't need to draw the environment diagram for exercise 3.27; use a trace
to provide the requested explanations. Treat the table procedures `lookup` and
`insert!` as primitive; i.e. don't trace the procedures they call. Also,
assume that those procedures work in constant time. We're interested to know
about the number of times `memo-fib` is invoked.

## Exercise 5.

Write `vector-append`, which takes two vectors as arguments and returns a new
vector containing the elements of both arguments, analogous to `append` for
lists.

**Don't use a list as an intermediate value. (That is, don't convert the vectors to lists!)**

## Exercise 6.

  
Write `vector-filter`, which takes a predicate function and a vector as
arguments, and returns a new vector containing only those elements of the
argument vector for which the predicate returns `true`. The new vector should
be exactly big enough for the chosen elements. Compare the running time of
your program to this version:

`(define (vector-filter pred vec)`

` (list->vector (filter pred (vector->list vec))))`

**Don't use a list as an intermediate value. (That is, don't convert the vectors to lists!)**

## Exercise 7.

  
Sorting a vector:

  1. Write `bubble-sort!`, which takes a vector of numbers and rearranges them to be in increasing order. (You'll modify the argument vector; don't create a new one.) It uses the following algorithm:
    1. Go through the array, looking at two adjacent elements at a time, starting with elements 0 and If the earlier element is larger than the later element, swap them. Then look at the next overlapping pair (0 and 1, then 1 and 2, etc.).
    2. Recursively `bubble-sort` all but the last element (which is now the largest element).
    3. Stop when you have only one element to sort.
  2. Prove that this algorithm really does sort the vector. Hint: Prove the parenthetical claim in step 2.
  3. What is the order of growth of the running time of this algorithm?

**Don't use a list as an intermediate value. (That is, don't convert the vectors to lists!)**

## Extra for Experts

### Do this if you want to. This is NOT for credit.

## Exercise 8.

  
Abelson & Sussman, exercises [3.19](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-22.html#%_thm_3.19) and [3.23](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-22.html#%_thm_3.23). Exercise 3.19 is incredibly hard
but if you get it, you'll feel great about yourself. You'll need to look at
some of the other exercises you skipped in this section. Exercise 3.23 isn't
quite so hard, but be careful about the Θ(1) - i.e. constant-time requirement.

## Exercise 9.

  
Write the procedure `cxr-name`. Its argument will be a function made by
composing `cars` and `cdrs`. It should return the appropriate name for that
function:

`> (cxr-name (lambda (x) (cadr (cddar (cadar x)))))`

` CADDDAADAR`

# **DO NOT FORGET TO TURN IN YOUR HOMEWORK!**

