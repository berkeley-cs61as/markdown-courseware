## Trees- Overview

Previously we have seen that structures like `(cons (list 1 2) (list 3 4)) `
can be represented as trees:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-16.gif)

We will explore general properties of trees here and look at the details
towards the end of the lesson.

The structure is made up of branches and leaves. The tree above has 5
branches; they correspond to the lines on the diagram above` `. Notice that a
branch can contain trees (in this case the ` (1 2)`). Leaves of the tree
structure can be found at the bottom-most level. The tree above has 4 leaves;
1, 2, 3 and 4.

Unlike trees in the real world, trees in Computer Science tend to be upside-
down.

![](http://tamingthewolf.com/wp-
content/uploads/2010/08/draw_upside_down_tree.png)

## Number of Leaves

How do we find a general function that counts the number of leaves in a tree?
Recall how we defined `length` that finds the length of a list:

  * `length` of a list x is 1 plus the `length` of the cdr of x
  * `length` of an empty list is 0

The structure of the function is the same for `count-leaves`

  * `count-leaves` of the empty list is 0

Our reduction step is slightly different though. In `length` we don't care
what is in the `car` of the list. But for `count-leaves`, its `car` may
contain more trees, therefore we need to find the `count-leaves` of the `car`
of the tree.

  * `count-leaves` of a tree is the `count-leaves` of the `car` of the tree plus `count-leaves` of the `cdr` of the tree.

Eventually we will `car` ourselves to the leaf of the tree so we need the base
case:

  * `count-leaves` of a leaf is 1

## Pair?

When we go to the `car` of the tree, we have to determine if it is another
tree, or a leaf. How do we check for it? Scheme has a built-in `pair?`
procedure that tests if something can be made from a `cons` or not.

  * `(pair? (cons 1 2))` returns `#t`
  * `(pair? (cons 1 (cons 2 3)))` returns `#t`
  * `(pair? 2)` returns `#f`
  * `(pair? 'pear)` returns `#f`
  * `(pair? '())` returns `#f`

## count-leaves code

Using the pseudo-code from the previous page and the `pair?` function above,
we can write the complete code for `count-leaves`:

    
    
    (define (count-leaves x)
        (cond ((null? x) 0)
              ((not (pair? x)) 1)
              (else (+ (count-leaves (car x))
                       (count-leaves (cdr x)))))
    

## scale-tree

In the previous leson we saw the function `scale-list` which multiplies each
item in the list by a given factor. We are going to write an analogous
function, `scale-tree` that accepts a tree and a factor to multiply all the
leaves by.

Here is an example call:

`(scale-tree (list 1 (list 2 (list 3 4) 5) (list 6 7)) 10)`

It will output: `(10 (20 (30 40) 50) (60 70))`

## Deep Reverse

Let us work on a problem with similar structure. This time we want to reverse
the order of all elements in a list, including lists within a list. Here is an
example:

    
    >(define x (list (list 1 2) (list 3 4)))
    ((1 2) (3 4))
    
    >(deep-reverse x)
    ((4 3) (2 1))
    

Notice that not only does (1 2) and (3 4) switch places, but its elements also
got reversed. You can find the interpreter [
here](http://inst.eecs.berkeley.edu/~cs61as/sp13/js-scheme-stk/index.html).

## Takeaways

As trees can contain subtrees, to do anything useful to data that are
contained in the leaves we generally have to use a recursive function.

