## Sequences as Abstractions

We have stressed several times that if we see a program that has the same
general structure, we can generally abstract it and make a more general form
of it. This idea can be extended even to chunks of code that have somewhat
different structures. Let's compare two example functions to see this.

Consider the following function that sums up all leaves in a tree (deep list)
that are odd:

    
    (define (sum-odd-squares tree)
      (cond ((null? tree) 0)  
            ((not (pair? tree))
             (if (odd? tree) (square tree) 0))
            (else (+ (sum-odd-squares (car tree))
                     (sum-odd-squares (cdr tree))))))
    

Here is another function that returns a list with only the even Fibbonaci
numbers:

    
    (define (even-fibs n)
      (define (next k)
        (if (> k n)
            nil
            (let ((f (fib k)))
              (if (even? f)
                  (cons f (next (+ k 1)))
                  (next (+ k 1))))))
      (next 0))
    

From a first glance at the two functions, we might say "These two functions
have nothing in common!". Sure, the functions look completely different but
they do share the same logic:

  
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-17.gif)

This is what the first program does:

  * enumerates the leaves of a tree;
  * filters them, selecting the odd ones;
  * squares each of the selected ones; and
  * accumulates the results using +, starting with 0.

This is what the second program does:

  * enumerates the integers from 0 to _n_;
  * computes the Fibonacci number for each integer;
  * filters them, selecting the even ones; and
  * accumulates the results using cons, starting with the empty list.

## Filter

So we decomposed our functions abstractly to 'enumerate', 'map', 'filter' and
'accumulate'. So how do we design them so that they work on sequences? We
defined `map` in the previous lesson, so let's look at `filter`. `filter`
should only select elements in a sequence that satisfies a certain predicate.

    
    
    (define (filter predicate sequence)
      (cond ((null? sequence) nil)
            ((predicate (car sequence))
             (cons (car sequence)
                   (filter predicate (cdr sequence))))
            (else (filter predicate (cdr sequence)))))
    

## Accumulate

The job of `accumulate` is to reduce series of values into one. For example,
you can use accumulate with the operation `+` and base case 0 to add a list of
numbers into a single value. You can also accumulate with the operation
`append` and base case `nil` to append multiple lists together. Here is the
definition for `accumulate ('initial' `is the base case`).`

    
    
    (define (accumulate op initial sequence)
      (if (null? sequence)
          initial
          (op (car sequence)
              (accumulate op initial (cdr sequence)))))
    

## Step by Step

Consider the call `(accumulate + 0 (list 1 2 3 4 5))`

The recursive call will be called like this:

`(+ 1 (accumulate + 0 (list 2 3 4 5)))`

`(+ 1 (+ 2 (accumulate + 0 (list 3 4 5))))`

`(+ 1 (+ 2 (+ 3 (accumulate + 0 (list 4 5)))))`

`(+ 1 (+ 2 (+ 3 (+ 4 (accumulate + 0 (list 5))))))`

`(+ 1 (+ 2 (+ 3 (+ 4 (+ 5 (accumulate + 0 (list)))))))`

`(+ 1 (+ 2 (+ 3 (+ 4 (+ 5 0)))))`

and it evaluates the rest normally.

## Enumerate

What does `enumerate` do? `enumerate` makes a sequence/list of elements. Our
definition of `filter` and `map` are designed for sequences but recall that
one of our functions, `sum-odd-squares` is called on trees. Instead of making
several versions of maps and filters, we can differentiate them by just having
different `enumerate` functions.

## Enumerate for Lists

Enumerate will return a list given a lower and a higher range.

  * `(enumerate-interval 0 5)` returns ` (0 1 2 3 4 5)`
  * `(enumerate-interval 10 13) ` returns `(10 11 12 13) `

You can define enumerate (for lists) as:

    
    
    (define (enumerate-interval low high)
      (if (> low high)
          nil
          (cons low (enumerate-interval (+ low 1) high))))
    

## Enumerate for Trees

For our tree-version of enumerate, we need a function that accepts a tree, and
returns a list with all of the leaves, so that it is compatible with our `map`
and `filter.`

    
    
    (define (enumerate-tree tree)
      (cond ((null? tree) nil)
            ((not (pair? tree)) (list tree))
            (else (append (enumerate-tree (car tree))
                          (enumerate-tree (cdr tree))))))
    

## Putting Everything Together

With all of the helper functions we have defined, we can define a more modular
`sum-odd-squares` and `even-fibs`.

    
    (define (sum-odd-squares tree)
      (accumulate +
                  0
                  (map square
                       (filter odd?
                               (enumerate-tree tree)))))
    

What did we do here? We find all the leaves in the tree (**enumerate**), keep
everything that is odd (**filter**), square everything left (**map**), and add
up the results (**accumulate**).

Similarly we can define `even-fibs` as follows:

    
    (define (even-fibs n)
      (accumulate cons
                  nil
                  (filter even?
                          (map fib
                               (enumerate-interval 0 n)))))
    

What happened this time? We make a list from 0 until n (**enumerate**), find
the fibonacci number for all of them (**map**), keep everything that is even
(**filter**), and put them together into a list (**accumulate**).

## Takeaways

Sequences provide a strong foundation for abstraction with different
combinations of `map`, `filter`, `accumulate` and `enumerate`. Even functions
that may look to have different structures like the ones we used here as an
example, we may be able to break them down using similar process signals.

