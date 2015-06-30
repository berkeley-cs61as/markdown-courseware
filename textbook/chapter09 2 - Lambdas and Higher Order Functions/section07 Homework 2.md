## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw2.rkt .


Or you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw2.rkt).

## Exercise 1

  
Write a procedure `substitute` that takes three arguments: a sentence, an old
word, and a new word. It should return a copy of the sentence, but with every
occurrence of the old word replaced by the new word.

```
(substitute '(she loves you yeah yeah yeah) 'yeah 'maybe)
;; Outputs: (she loves you maybe maybe maybe)
```

## Exercise 2

  
Type each of the following into Racket, and note the results. See if you can
predict the results before letting Racket do the computation.

```
(lambda (x) (+ x 3))
```

```
((lambda (x) (+ x 3)) 7)
```

`make-adder` is a function that returns another function.

```
(define (make-adder num)
  (lambda (x) (+ x num)))
((make-adder 3) 7)
```

```
(define plus3 (make-adder 3))
(plus3 7)
```

```
(define (square x) ( x x))
(square 5)
```

```
(define sq (lambda (x) ( x x)))
(sq 5)
```

```
(define (try f) (f 3 5))
(try +)
(try word)
```

## Exercise 3

  
Consider a function `g` for which the expression

`((g) 1) `

returns the value `3` when evaluated.

Determine how many arguments `g` has. In one word, also describe as best you
can the type of value returned by `g`.

## Exercise 4

  
For each of the following expressions, what must `f` be in order for the
evaluation of the expression to succeed, without causing an error? For each
expression, give a definition of `f` such that evaluating the expression will
not cause an error, and say what the expression's value will be, given your
definition.

  1. `f1`
  2. `(f2)`
  3. `(f3 3)`
  4. `((f4))`
  5. `(((f5)) 3)`

## Exercise 5

Find the values of the following expressions, where `add1` is a primitive procedure that adds one to its argument, and `t` is defined as follows:

    (define (t f)
      (lambda (x) (f (f (f x)))) )

Work these out before trying them on the computer.

  1. `((t add1) 0)`
  2. `((t (t add1)) 0)`
  3. `(((t t) add1) 0)`

## Exercise 6

  
Find the values of the following expressions where `t` is defined as in
Exercise 5, and `s` is defined as follows:

    (define (s x)
      (+ 1 x))

Work these out before trying them on the computer

  1. `((t s) 0) `
  2. `((t (t s)) 0) `
  3. `(((t t) s) 0)`

## Exercise 7

  
Write and test the `make-tester` procedure. Given a word `w` as its argument,
`make-tester` returns a procedure of one argument `x` that returns `true` if
`x` is equal to `w` and `false` otherwise.

    -> ((make-tester 'hal) 'hal)
    #t
    -> ((make-tester 'hal) 'cs61a)
    #f
    -> (define sicp-author-and-astronomer? (make-tester 'gerry))
    -> (sicp-author-and-astronomer? 'hal)
    #f
    -> (sicp-author-and-astronomer? 'gerry)
    #f

## Exercise 8

  
Abelson & Sussman, exercises [1.31(a)](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-12.html#%25_thm_1.31),
[1.32(a)](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-12.html#%25_thm_1.32), [1.33](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-12.html#%25_thm_1.33),
[1.40](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-12.html#%25_thm_1.40), [1.41](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-12.html#%25_thm_1.41),
[1.43](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-12.html#%25_thm_1.43), [1.46](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%25_thm_1.46)

(Pay attention to footnote 51; you'll need to know the ideas in these
exercises later in the semester.)

Notes:

* For 1.31a, you should base your `product` function off of the `sum` function
earlier in the text. It should take 4 arguments: `term`, `a`, `next`, and
`b`. Find the `sum` function and figure out what each of these arguments do.
* For 1.31a, the function to estimate pi should be called `estimate-pi`. It
should take in no arguments, and should estimate pi using at least 100 terms
of the formula given in SICP.
* For 1.33, the predicate should be the last argument to `filtered-accumulate`
(see text box).
* For 1.33, you should define functions `sum-sq-prime` and `prod-of-some-
numbers` (see text box).

## Exercise 9

  
Last week you wrote procedure `squares`, that squared each number in its
argument sentence, and saw `pigl-sent`, that `pigl`ed each word in its argument
sentence. Generalize this pattern to create a higher order procedure called
`my-every` that applies an arbitrary procedure, given as an argument, to each word of an argument sentence.

    -> (my-every square '(1 2 3 4))
    (1 4 9 16)
    -> (my-every first '(nowhere man))
    (n m)


## Exercise 10

  
Using the higher order functions, our simply-scheme library provides its own versions of the `every` function from the last exercise and the `keep` function shown in our lessons. Get familiar with these by working these examples out before trying them on the computer:

  1. `(every (lambda (letter) (word letter letter)) 'purple) `
  2. `(every (lambda (number) (if (even? number) (word number number) number)) '(781 5 76 909 24)) `

  3. `(keep even? '(781 5 76 909 24)) `
  4. `(keep (lambda (letter) (member? letter 'aeiou)) 'bookkeeper) `
  5. `(keep (lambda (letter) (member? letter 'aeiou)) 'syzygy) `
  6. `(keep (lambda (letter) (member? letter 'aeiou)) '(purple syzygy)) `
  7. `(keep (lambda (wd) (member? 'e wd)) '(purple syzygy))`

## Submit Your Homework

Don't remember how? No worries. Take a look at the instructions for [Homework 1](homework-1.html#sub9).
