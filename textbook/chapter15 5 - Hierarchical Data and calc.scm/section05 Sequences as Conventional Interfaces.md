## Sequences as Abstractions

Let's explore more into the concept of abstraction. One major benefit of using abstraction is that it helps us clean up code and increase readability. Some of the functions that we write for sequences can be generalized and abstracted using Higher Order Functions. This idea can be summarized by the following steps:

  * Find a recurring pattern in our code
  * Abstract each element in the pattern using HOFs
  * Redefine our code with using the abstraction

Here are two example functions that will help demonstrate this idea.

`sum-odd-squares` takes in a tree containing numbers and adds together the square of each **odd** element in the tree:

    
    (define (sum-odd-squares tree)
      (cond ((null? tree) 0)  
            ((not (pair? tree))
             (if (odd? tree) (square tree) 0))
            (else (+ (sum-odd-squares (car tree))
                     (sum-odd-squares (cdr tree))))))


`even-fibs` takes in a number `n`, and returns a list of even fibonacci numbers up to and including `n`:

    
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

The first step in our idea was to find a recurring pattern in our code. From how we've described recursion in previous lessons, you might dissect `sum-odd-squares` and `even-fibs` by base cases and recursive calls. Now, let's see what each function does from a different perspective:

`sum-odd-squares`:

  * **enumerates** the leaves of a tree
  * **filters** out the nodes with even data, leaving only odd-valued nodes
  * **maps** the function `square` onto each of the remaining nodes, and finally
  * **accumulates** the results by adding them together, starting with 0.

`even-fibs`:

  * **enumerates** the integers from 0 to `n`
  * **maps** the function `fib` onto each integer
  * **filters** out the odd numbers, leaving only even Fibonacci numbers, and finally
  * **accumulates** the results using `cons`, starting with the empty list.

What pattern do we see here? What at first seemed like two very different functions can now be summarized into four major parts: enumeration, filtering, accumulation, and computation. This is great, because now we can use HOFs to abstract our code. This leads us to step two of our abstraction idea. But before that, let's go over some HOFs.

## Map

We went over the `map` HOF in Lesson 4. You may want to [go back](http://localhost:8000/textbook/representing-sequences.html#sub3) for a quick refresher.

## Filter

`filter` takes in two arguments, `predicate` and `sequence`, and returns the sequence with only the elements of that sequence that satisfy `predicate`.
    
    
    (define (filter predicate sequence)
      (cond ((null? sequence) nil)
            ((predicate (car sequence))
             (cons (car sequence)
                   (filter predicate (cdr sequence))))
            (else (filter predicate (cdr sequence)))))
    
**Test Your Understanding**

<div class="mc">
What does the following expression return?

<pre><code>
(filter (lambda (x) (= (remainder x 2) 0)) (list 0 1 2 3 4 5))
</code></pre>
<ans text="nil" explanation="Hint: what does the lambda function check for?"></ans>
<ans text="(0 1 2)" explanation="Hint: what does ((lambda (x) (= (remainder x 2) 0)) 4) return?"></ans>
<ans text="(0 2 4)" explanation="Correct! This expression filters out all numbers in the sequence that are not divisible by 2." correct></ans>
<ans text="Error" explanation="This expression is syntactically correct."></ans>
<!-- and so on -->
</div>

<div class="mc">
<pre><code>
(filter equal? '(bongo celia momo laval laburrita bongo))
</code></pre>
<ans text="nil" explanation="Hint: what does the predicate check for?"></ans>
<ans text="(bongo celia momo laval laburrita bongo)" explanation="Hint: how many arguments does equal? take in?"></ans>
<ans text="(bongo)" explanation="Hint: how many arguments should the predicate have?"></ans>
<ans text="Error" explanation="Correct! equal? takes in two arguments, but the predicate in filter only checks one element of the sequence at a time. This calls (equal? bongo), which produces an error." correct></ans>
<!-- and so on -->
</div>

## Accumulate

`accumulate` takes in an operation `op`, a starting value `initial`, and a `sequence`. Starting from `initial`, `accumulate` uses `op` to combine all the values in `sequence` into one. Here are some examples:


    > (accumulate + 0 '(1 2 3 4 5))
    15
    > (accumulate append null '((1 2) (3 4) (5 6)))
    (1 2 3 4 5 6)

Here is how we define `accumulate`:    
    
    (define (accumulate op initial sequence)
      (if (null? sequence)
          initial
          (op (car sequence)
              (accumulate op initial (cdr sequence)))))
    

How this HOF works could be a little confusing, so here let's write out the evaluation steps explicitly:

Consider the expression:

`(accumulate + 0 (list 1 2 3 4 5))`

The recursive steps will proceed as follows:

`(+ 1 (accumulate + 0 (list 2 3 4 5)))`

`(+ 1 (+ 2 (accumulate + 0 (list 3 4 5))))`

`(+ 1 (+ 2 (+ 3 (accumulate + 0 (list 4 5)))))`

`(+ 1 (+ 2 (+ 3 (+ 4 (accumulate + 0 (list 5))))))`

`(+ 1 (+ 2 (+ 3 (+ 4 (+ 5 (accumulate + 0 (list)))))))`

`(+ 1 (+ 2 (+ 3 (+ 4 (+ 5 0)))))`

`(+ 1 (+ 2 (+ 3 (+ 4 5))))`

`(+ 1 (+ 2 (+ 3 9)))`

`(+ 1 (+ 2 12))`

`(+ 1 14)`

`15`


## Enumerate

What does `enumerate` do? `enumerate` makes a sequence/list of elements. Our
definition of `filter`, `map`, and `accumulate` are designed for sequences but recall that
one of our functions, `sum-odd-squares` is called on trees. Instead of making
several versions of accumulate, map, and filter, we can differentiate them by just having
different `enumerate` functions.

## Enumerate for Lists

Enumerate will return a list given a lower and upper range.

  * `(enumerate-interval 0 5)` returns ` (0 1 2 3 4 5)`
  * `(enumerate-interval 10 13) ` returns `(10 11 12 13) `

You can define enumerate (for lists) as:

    
    
    (define (enumerate-interval low high)
      (if (> low high)
          nil
          (cons low (enumerate-interval (+ low 1) high))))
    

## Enumerate for Trees

For our tree-version of enumerate, we need a function that accepts a tree, and
returns a list with all of the leaves, so that it is compatible with the rest of our HOFs.

    
    
    (define (enumerate-tree tree)
      (cond ((null? tree) nil)
            ((not (pair? tree)) (list tree))
            (else (append (enumerate-tree (car tree))
                          (enumerate-tree (cdr tree))))))
    

## Putting Everything Together

Here, we reach our final step in our abstraction idea. With all of the helper functions we have defined, we can define a more modular, readable, and compact version of `sum-odd-squares` and `even-fibs`:

    
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
    

What happened this time? We make a list from 0 to `n` (**enumerate**), find
the Fibonacci number for all of them (**map**), keep everything that is even
(**filter**), and put them together into a list (**accumulate**).

## Takeaways

Sequences provide a strong foundation for abstraction with different
combinations of `map`, `filter`, `accumulate` and `enumerate`. Even functions
that may look to have different structures like the ones we used here as an
example, we may be able to break them down using similar process signals.

