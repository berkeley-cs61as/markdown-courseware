## Template

Type the following into the terminal to copy the template file
to the current directory (note the period at the end):

    cp ~cs61as/autograder/templates/hw5.rkt .

Or you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw5.rkt).

## Autograder

If you are working on the lab computers, the `grader` command will run the autograder.  If you are working on your own personal machine, you should download [grader.rkt](http://inst.eecs.berkeley.edu/~cs61as/autograder/grader.rkt) and the [HW 5 tests](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw5-tests.rkt).

## Exercise 1: SICP 2.26

Suppose we define `x` and `y` to be two lists:

`(define x (list 1 2 3))`

`(define y (list 4 5 6))`

What result is printed by the interpreter in response to evaluating each of
the following expressions?

`(append x y)`

`(cons x y)`

  
`(list x y)`

## Exercise 2: SICP 2.29

A binary mobile consists of two branches, a left branch and a right branch.
Each branch is a rod of a certain length, from which hangs either a weight or
another binary mobile. We can represent a binary mobile using compound data by
constructing it from two branches (for example, using list):

    
    (define (make-mobile left right)
        (list left right))
    

A branch is constructed from a length (which must be a number) together with a
structure, which may be either a number (representing a simple weight) or
another mobile:

    
    (define (make-branch len structure)
        (list len structure))
    

**a.** Write the corresponding selectors `left-branch` and `right-branch`, which
return the branches of a mobile, and `branch-length` and `branch-structure`,
which return the components of a branch.

**b.** Using your selectors, define a procedure `total-weight` that returns the
total weight of a mobile.

**c.** A mobile is said to be _balanced_ if the torque applied by its top-left
branch is equal to that applied by its top-right branch (that is, if the
length of the left rod multiplied by the weight hanging from that rod is equal
to the corresponding product for the right side) and if each of the submobiles
hanging off its branches is balanced. Design a predicate that tests whether a
binary mobile is balanced.

**d.** Suppose we change the representation of mobiles so that the constructors
are

`(define (make-mobile left right) (cons left right))`

`(define (make-branch len structure)`

` (cons len structure))`

How much do you need to change your programs to convert to the new
representation?

## Exercise 3: SICP 2.30, 2.31

**a.** Define a procedure `square-tree` analogous to the `square-list` procedure.
That is, `square-tree` should behave as follows:

    
    > (square-tree (list 1 (list 2 (list 3 4) 5) (list 6 7)))
    (1 (4 (9 16) 25) (36 49))
    

**b.** Abstract your answer to produce a procedure `tree-map` with the property
that `square-tree` could be defined as:

`(define (square-tree tree) (tree-map square tree))`

## Exercise 4: SICP 2.36

The procedure `accumulate-n` is similar to `accumulate` except that it takes
as its third argument a sequence of sequences, which are all assumed to have
the same number of elements. It applies the designated accumulation procedure
to combine all the first elements of the sequences, all the second elements of
the sequences, and so on, and returns a sequence of the results. For instance,
if s is a sequence containing four sequences, `((1 2 3) (4 5 6) (7 8 9) (10 11
12))`, then the value of `(accumulate-n + 0 s)` should be the sequence` (22 26
30)`. Fill in the missing expressions in the following definition of
`accumulate-n`:

`(define (accumulate-n op init seqs)`

` (if (null? (car seqs))`

` nil`

` (cons (accumulate op init <??>)`

` (accumulate-n op init <??>))))`

## Exercise 5

Suppose we represent vectors _v_ = (_v_<sub>_i_</sub>) as sequences of numbers, and
matrices _m_ = (_m_<sub>_i_,_j_</sub>) as sequences of vectors (the rows of the matrix).
For example, the matrix

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-20.gif)

is represented as the sequence `((1 2 3 4) (4 5 6 6) (6 7 8 9))`. With this
representation, we can use sequence operations to concisely express the basic
matrix and vector operations. These operations (which are described in any
book on matrix algebra) are the following:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-21.gif)

We can define the dot product as

    
    (define (dot-product v w)
        (accumulate + 0 (map * v w)))
    
    

Fill in the missing expressions in the following procedures for computing the
other matrix operations. (The procedure accumulate-n is defined in the
previous exercise)

`(define (matrix-*-vector m v)`

` (map <??> m))`

`(define (transpose mat)`

` (accumulate-n <??> <??> mat))`

`(define (matrix-*-matrix m n)`

` (let ((cols (transpose n)))`

` (map <??> m)))`

## Exercise 6: SICP 2.38

The `accumulate` procedure is also known as `fold-right`, because it combines
the first element of the sequence with the result of combining all the
elements to the right. There is also a `fold-left`, which is similar to `fold-right`, except that it combines elements working in the opposite direction:

    
    (define (fold-left op initial sequence)
        (define (iter result rest)
            (if (null? rest)
                result
                (iter (op result (car rest))
                      (cdr rest))))
        (iter initial sequence))
    

What are the values of the following:

    
    (fold-right / 1 (list 1 2 3))
    (fold-left / 1 (list 1 2 3))
    (fold-right list nil (list 1 2 3))
    (fold-left list nil (list 1 2 3))
    

Describe a property that `op` should satisfy to guarantee that `fold-right`
and `fold-left` will produce the same values for any sequence.

## Exercise 7: SICP 2.54

Two lists are said to be equal if they contain equal elements arranged in the
same order. For example,

    
    (equal? '(this is a list) '(this is a list))
    

is true, but

    
    (equal? '(this is a list) '(this (is a) list))
    

is false. To be more precise, we can define `equal?` recursively in terms of
the basic `eq?` equality of symbols by saying that a and b are `equal?` if
they are both symbols and the symbols are `eq?`, or if they are both lists
such that `(car a)` is `equal?` to `(car b)` and `(cdr a)` is `equal?` to
`(cdr b)`. Using this idea, implement `equal?` as a procedure.

Note: you should know by now that `equal?` is a built-in procedure as well.
This means your definition will overwrite the built-in definition.

## Exercise 8

We can represent a set as a list of distinct elements, and we can represent
the set of all subsets of the set as a list of lists. For example, if the set
is `(1 2 3)`, then the set of all subsets is `(() (3) (2) (2 3) (1) (1 3) (1
2) (1 2 3))`. Complete the following definition of a procedure that generates
the set of subsets of a set and give a clear explanation of why it works:

    
    (define (subsets s)
      (if (null? s)
          (list nil)
          (let ((rest (subsets (cdr s))))
            (append rest (map <??> rest)))))
    

## Exercise 9

  
Extend `calc.rkt` to include words as data, providing the operations `first,
butfirst, last, butlast, and word`. Unlike Racket, your calculator should
treat words as self-evaluating expressions except when seen as the operator of
a compound expression. That is, it should work like these examples:

`calc: foo`

` foo`

` calc: (first foo)`

` f`

` calc: (first (butfirst hello))`

` e`

  

Remember, you can get the program by typing

`cp ~cs61as/lib/calc.rkt .`

Or download it from
[here](http://inst.eecs.berkeley.edu/~cs61as/library/calc.rkt).

## Exercise 10: Extra for Experts

**Do this if you want to. This is NOT for credit.**

Read [section 2.3.4](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-16.html#%25_sec_2.3.4) and do exercises 2.67 - 2.72.

## Exercise 11: Extra for Experts

**Do this if you want to. This is NOT for credit.**

Programming by example: In some programming systems, instead of writing an
algorithm, you give examples of how you'd like the program to behave, and the
language figures out the algorithm itself:

`> (define pairup (regroup '((1 2) (3 4) ...)))`

` > (pairup '(the rain in spain stays mainly on the plain))`

` ((the rain) (in spain) (stays mainly) (on the))`

Write `regroup`. Read `~cs61as/lib/regroup.problem` for details.

