## List Operators

Racket provides useful primitive procedures for lists:

### `list-ref` 

`list-ref` takes as arguments a list and a number `n` and returns the `n`th item of the list. The first element of the list is indexed as `0`, meaning it is the `0`th element of the list. Here's how `list-ref` is defined: 
    
    (define (list-ref lst n)
      (if (= n 0)
          (car lst)
          (list-ref (cdr lst) (- n 1))))
  
and here is an example of how it works:

    -> (define squares (list 1 4 9 16 25))
    squares
    -> (list-ref squares 3)
    16

### `null?` 

`null?` takes a list as an argument and returns `#t` if the list is empty. Otherwise, it returns `#f`:

    
    (null? (list 1 3))
    #f
    
    (null? '())
    #t

### `length` 

`length` takes a list as an argument and returns the number of items in a list. Here's how `length` is defined: 
    
    (define (length items)
      (if (null? items)
          0
          (+ 1 (length (cdr items)))))

and here is an example:
    
    -> (define odds (list 1 3 5 7))
    odds
    -> (length odds)
    4

## Higher Order Functions with Lists

From here on out, we’ll be mostly using lists and pairs rather than sentences. This is great, since it means we'll be able to take a closer look at how data is represented by Racket. But, this also means that a lot of the important higher order functions we previously defined with sentences must now be rewritten to work with pairs.

### `every` vs. `map`

Recall the HOF `every`, which takes in a function and a sentence, and returns a sentence with the function applied to every element of the sentence. The equivalent of this HOF using pairs is called `map`, which it takes in a function and a _list_, and returns a list with the function _mapped_ to every element in the list. `map` is a recursively defined function, as you can see here:

    (define (map proc items)
      (if (null? items)
          null
          (cons (proc (car items))
                (map proc (cdr items)))))

The procedure `null?` for lists is analogous to the procedure `empty?` for sentences, and checks whether or not the given argument is the empty list. Here are a few example calls to `map`:

    -> (map square (list 1 2 3 4 5))
    (1 4 9 16 25)
    -> (map car (list (cons 1 2) (cons 3 4) (cons 5 6)))
    (1 3 5)


### `keep` vs. `filter`

We already had a quick glimpse of `filter` in the `filtered-accumulate` problem in Homework 2, so you should already have some idea of what the HOF `filter` should do. `filter` takes in two arguments, a predicate and a list, and returns a list with only elements that satisfy the predicate. Take a look at the formal definition:

    (define (filter pred lst)
      (cond ((null? lst) null)
            ((pred (car lst))
              (cons (car lst) (filter pred (cdr lst))))
            (else (filter pred (cdr lst)))))

And here are some examples:

    -> (filter odd? '(1 2 3 4 5))
    (1 3 5)
    -> (filter (lambda (x) (> x 2)) '(1 2 3 4 5))
    (3 4 5)

### `accumulate`

Finally, there is the procedure `accumulate` for sentences. This procedure takes in a function of two arguments, a base case value, and a sentence of values, and continuously combines the values in the list using this operation and ending/starting with the base case value. There are two equivalents to accumulate for lists: `foldl` and `foldr`. Both take in a function of two values, a base case value, and a list. 

`fold-left` starts from the last (right-most) element in the list and continuously applies the function recursively until it reaches the first element of the list. Thus, it _folds_ to the left. For example, here are the steps to evaluate a call to `foldl`:

    -> (foldl cons '() '(1 2 3 4))
    ... (cons 4 (cons 3 (cons 2 (cons 1 '()))))
    (4 3 2 1)

Here's another example:

    -> (define combiner (lambda (x y) (cons (add1 x) y)))
    combiner
    (foldl combiner '() '(1 2 3 4))
    ... (combiner 4 (combiner 3 (combiner 2 (combiner 1 '()))))
    ... (5 . (4 . (3 . (2 . ()))))
    (5 4 3 2)

On the other hand, `fold-right` starts from the first (left-most) element in the list and continuously applies the function recursively until it reaches the last element of the list. Thus, it _folds_ to the right. Take these calls for example:

    -> (foldr cons '() '(1 2 3 4))
    ... (cons 1 (cons 2 (cons 3 (cons 4 '()))))
    (1 2 3 4)

    -> (foldr + 0 '(1 2 3 4))
    ... (+ 1 (+ 2 (+ 3 (+ 4 0))))
    10

We now have two versions of `accumulate`, where the values of `foldl` and `foldr` would only differ when they are called with combiner functions in which order matters. 

## Summary of HOFs

To make the transition easier, here’s a table illustrating some operations on sentences and their equivalent for lists.

<table class="table table-bordered table-striped">
<thead><tr>
    <th>SENTENCE</th>
    <th>LIST</th>
</tr></thead><tbody>
<tr>
    <td><code>se/sentence</code></td>
    <td><code>cons/list/append</code></td>
</tr>
<tr>
    <td><code>first</code></td>
    <td><code>car</code></td>
</tr>
<tr>
    <td><code>bf/butfirst</code></td>
    <td><code>cdr</code></td>
</tr>
<tr>
    <td><code>last</code></td>
    <td>NO EQUIVALENT</td>
</tr>
<tr>
    <td><code>bl/butlast</code></td>
    <td>NO EQUIVALENT</td>
</tr>
<tr>
    <td><code>count</code></td>
    <td><code>length</code></td>
</tr>
<tr>
    <td><code>item</code> (one-indexed)</td>
    <td><code>list-ref</code> (zero-indexed)</td>
</tr>
<tr>
    <td><code>every</code></td>
    <td><code>map</code></td>
</tr>
<tr>
    <td><code>keep</code></td>
    <td><code>filter</code></td>
</tr>
<tr>
    <td><code>accumulate</code></td>
    <td><code>foldl/foldr</code></td>
</tr></tbody>
</table>