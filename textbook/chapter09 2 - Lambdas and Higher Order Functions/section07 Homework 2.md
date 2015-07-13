## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw2.rkt .


Or you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw2.rkt).

## Autograder

If you are working on the lab computers, the `grader` command will run the autograder.  If you are working on your own personal machine, you should download [grader.rkt](http://inst.eecs.berkeley.edu/~cs61as/autograder/grader.rkt) and the [HW 2 tests](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw2-tests.rkt).

## Exercise 1

  
Write a procedure `substitute` that takes three arguments: a sentence, an old
word, and a new word. It should return a copy of the sentence, but with every
occurrence of the old word replaced by the new word.

```
-> (substitute '(she loves you yeah yeah yeah) 'yeah 'maybe)
(she loves you maybe maybe maybe)
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
(define (square x) (* x x))
(square 5)
```

```
(define sq (lambda (x) (* x x)))
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
    #t

## Exercise 8

### SICP 1.31a

The `sum` procedure is only the simplest of a vast number of similar abstractions that can be captured as higher-order procedures. Write an analogous procedure called `product` that returns the product of the values of a function at points over a given range. Show how to define `factorial` in terms of `product`. Also use `product` to compute approximations to pi using the formula

![](https://mitpress.mit.edu/sicp/full-text/book/ch1-Z-G-30.gif)

**Notes:**

  * You should base your `product` function off of the `sum` function earlier in the text. It should take 4 arguments: `term`, `a`, `next`, and `b`. Find the `sum` function and figure out what each of these arguments do.
  * The function to estimate pi should be called `estimate-pi`. It should take in no arguments, and should estimate pi using at least 100 terms of the formula given in SICP.

### SICP 1.32a

Show that `sum` and `product` (Exercise 1.31) are both special cases of a still more general notion called `accumulate` that combines a collection of terms, using some general accumulation function:

    (accumulate combiner null-value term a next b)

`accumulate` takes as arguments the same term and range specifications as `sum` and `product`, together with a `combiner` procedure (of two arguments) that specifies how the current term is to be combined with the accumulation of the preceding terms and a `null-value` that specifies what base value to use when the terms run out. Write `accumulate` and show how `sum` and `product` can both be defined as simple calls to `accumulate`.

### SICP 1.33

You can obtain an even more general version of `accumulate` (Exercise 1.32) by introducing the notion of a _filter_ on the terms to be combined. That is, combine only those terms derived from values in the range that satisfy a specified condition. The resulting `filtered-accumulate` abstraction takes the same arguments as `accumulate`, together with an additional predicate of one argument that specifies the filter. Write `filtered-accumulate` as a procedure. Show how to express the following using `filtered-accumulate`:

**a.** the sum of the squares of the prime numbers in the interval `a` to `b` (assuming that you have a `prime?` predicate already written)

**b.** the product of all the positive integers less than `n` that are relatively prime to `n` (i.e., all positive integers _i < n_ such that _GCD(i,n) = 1_).

**Notes:**

  * The predicate should be the last argument to `filtered-accumulate`.
  * You should define functions `sum-sq-prime` and `prod-of-some-numbers`.

### SICP 1.40

Define a procedure `cubic` that can be used together with the `newtons-method` procedure in expressions of the form

    (newtons-method (cubic a b c) 1)

to approximate zeros of the cubic _x<sup>3</sup> + ax<sup>2</sup> + bx + c_.

### SICP 1.41

Define a procedure `double` that takes a procedure of one argument as argument and returns a procedure that applies the original procedure twice. For example, if `inc` is a procedure that adds `1` to its argument, then `(double inc)` should be a procedure that adds `2`. What value is returned by the following expression?

    (((double (double double)) inc) 5)

### SICP 1.43

If _f_ is a numerical function and _n_ is a positive integer, then we can form the _n_th repeated application of _f_, which is defined to be the function whose value at _x_ is _f(f(...(f(x))...))_. For example, if _f_ is the function _x -> x + 1_, then the _n_th repeated application of _f_ is the function _x -> x + n_. If _f_ is the operation of squaring a number, then the _n_th repeated application of _f_ is the function that raises its argument to the _2<sup>n</sup>_th power. Write a procedure that takes as inputs a procedure that computes _f_ and a positive integer _n_ and returns the procedure that computes the _n_th repeated application of _f_. Your procedure should be able to be used as follows:

    -> ((repeated square 2) 5)
    625

### SICP 1.46

Several of the numerical methods described in this chapter are instances of an extremely general computational strategy known as _iterative improvement_. Iterative improvement says that, to compute something, we start with an initial guess for the answer, test if the guess is good enough, and otherwise improve the guess and continue the process using the improved guess as the new guess. Write a procedure `iterative-improve` that takes two procedures as arguments: a method for telling whether a guess is good enough and a method for improving a guess. `iterative-improve` should return as its value a procedure that takes a guess as argument and keeps improving the guess until it is good enough. Rewrite the `sqrt` procedure of section [1.1.7](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%_sec_1.1.7) and the `fixed-point` procedure of section [1.3.3](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_sec_1.3.3) in terms of `iterative-improve`.

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
