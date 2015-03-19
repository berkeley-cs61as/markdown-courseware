## Template

You can copy the template for this homework by typing in your terminal:

    
      cp ~cs61as/autograder/templates/hw10.scm .
    

Or, you can download it
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw10.scm).

## Extra Resource

Stuck on the homework? Check out this week's [discussion
notes](/static/dis11.pdf) for some great tips on understanding and writing
code for streams.

##  Exercise 1.

Do the following reading for this exercise:

  * [SICP 3.5.1 Streams Are Delayed Lists](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-24.html#%_sec_3.5.1)

What is the type of the value of `(delay (+ 1 27))`? What is the type of the
value of `(force (delay (+ 1 27)))`?

## Exercise 2.

Do the following reading for this exercise:

  * [SICP 3.5.1 Streams Are Delayed Lists](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-24.html#%_sec_3.5.1)

Evaluation of the expression

`(stream-cdr (stream-cdr (cons-stream 1 '(2 3))))`

produces an error. Why?

## Exercise 3.

    
    
    (define (enumerate-interval low high) 
      (if (> low high) 
          '() 
          (cons low (enumerate-interval (+ low 1) high)) ) )
    
    (define (stream-enumerate-interval low high) 
      (if (> low high) 
          the-empty-stream 
          (cons-stream low (stream-enumerate-interval (+ low 1) high)) ) )
    

What's the difference between the following two expressions?

    
    
    (delay (enumerate-interval 1 3))
    (stream-enumerate-interval 1 3) 

## Exercise 4.

An unsolved problem in number theory concerns the following algorithm for
creating a sequence of positive integers _s_1, _s_2, ...

Choose _s_1 to be some positive integer.

For n > 1,

if _s_n is odd, then _s_n+1 is 3_s_n+1;

if _s_n is even, then _s_n+1 is _s_n/2.

No matter what starting value is chosen, the sequence always seems to end with
the values 1, 4, 2, 1, 4, 2, 1, ... However, it is not known if this is always
the case.

a. Write a procedure `num-seq` that, given a positive integer `n` as argument,
returns the stream of values produced for `n` by the algorithm just given. For
example, `(num-seq 7)` should return the stream representing the sequence 7,
22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, ...

b. Write a procedure `seq-length` that, given a stream produced by `num-seq`,
returns the number of values that occur in the sequence up to and including
the first 1. For example, `(seq-length (num-seq 7))` should return 17. You
should assume that there is a 1 somewhere in the sequence.

## Exercise 5.

It's that time of the HW. SICP!

Complete the following: Abelson & Sussman, exercises [3.50, 3.51,
3.52](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-24.html#%_thm_3.50), [3.53, 3.54, 3.55,
3.56](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-24.html#%_thm_3.53), [3.64](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-24.html#%25_thm_3.64), [3.66,
3,68](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-24.html#%25_thm_3.66)

## Exercise 6.

  
Write and test two functions to manipulate nonnegative proper fractions. The
first function, `fract-stream`, will take as its argument a list of two
nonnegative integers, the numerator and the denominator, in which the
numerator is less than the denominator. It will return an infinite stream of
decimal digits representing the decimal expansion of the fraction. The second
function, `approximation`, will take two arguments: a fraction stream and a
nonnegative integer numdigits. It will return a list (not a stream) containing
the first numdigits digits of the decimal expansion.

`(fract-stream '(1 7))` should return the stream representing the decimal
expansion of 1/7, which is 0.142857142857142857...

`(stream-car (fract-stream '(1 7)))` should return `1`.

`(stream-car (stream-cdr (stream-cdr (fract-stream '(1 7)))))` should return
`2`.

`(approximation (fract-stream '(1 7)) 4)` should return `(1 4 2 8)`.

`(approximation (fract-stream '(1 2)) 4)` should return `(5 0 0 0)`.

## CHALLENGE PROBLEMS

### Do this if you want to. This is NOT for credit.

## Exercise 7.

  
Do exercises [3.59 - 3.62](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-24.html#%_thm_3.59).

## Exercise 8.

  
Consider this procedure:

`(define (hanoi-stream n)`

` (if (= n 0)`

` the-empty-stream`

` (stream-append (hanoi-stream (- n 1))`

` (cons-stream n (hanoi-stream (- n 1)))))) `

It generates finite streams; here are the first few values:

`(hanoi-stream 1) (1)`

` (hanoi-stream 2) (1 2 1)`

` (hanoi-stream 3) (1 2 1 3 1 2 1)`

` (hanoi-stream 4) (1 2 1 3 1 2 1 4 1 2 1 3 1 2 1) `

Notice that each of these starts with the same values as the one above it,
followed by some more values. There is no reason why this pattern can't be
continued to generate an infinite stream whose first 2n - 1 elements are
`(hanoi-stream n)`. Generate this stream.

## EXERCISE 9.

  
I type the following code into STk and get the given outputs. Assume `ints` is
the infinite stream of integers, starting from one.

`STk>(define foo (stream-map (lambda (x) (display x)) ints))`

1foo

STk>(show-stream foo 5)

23456(okay okay okay okay okay ...)

Why does this happen? Hint: it has to do with delaying and memoization.

# **DO NOT FORGET TO TURN IN YOUR HOMEWORK!**


