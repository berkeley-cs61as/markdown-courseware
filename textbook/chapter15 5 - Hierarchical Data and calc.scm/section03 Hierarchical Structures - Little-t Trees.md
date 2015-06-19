## An Overview of Little-t Trees

Previously, we have seen that structures like `(cons (list 1 2) (list 3 4))`
can be represented in a tree-like structure:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-16.gif)

We will explore general properties of trees here and look at the details
towards the end of the lesson.

The structure is made up of branches and leaves. The tree above has 5
**branches**; they correspond to the lines on the diagram above. Notice that a
branch can contain a **sub-tree**. In this case the branch `((1 2) 3 4)` contains sub-tree `(1 2)`. Leaves of the tree structure can be found at the bottom-most level, also called the **fringe**. A **leaf** has no branches connecting from it. The tree above has 4 leaves; `1`, `2`, `3`, and `4`.

Unlike trees in the real world, trees in Computer Science tend to be upside-down.

![](http://www.berndtgroup.net/~/media/images/thinking/blog/2014/deeptreestructure2.ashx)

## Number of Leaves

Let's write a general function, `count-leaves`, that counts the number of leaves in a tree.
Recall how we defined `length`, which finds the number of elements in a list:

  * `length` of a list `x` is 1 plus the `length` of the `cdr` of `x`.
  * `length` of an empty list is 0.

The structure of the function is the same for `count-leaves`:

  * `count-leaves` of the empty list is 0

Our reduction step is slightly different, though. In `length`, we are guaranteed that the `car` of the list is a single element, and can correctly return 1. But for `count-leaves`, its `car` may contain more trees, and so its length will not always be 1. Therefore, we need to recursively find the `count-leaves` of the `car` of the tree as well! Here we have our recursive call:

  * `count-leaves` of a tree is the `count-leaves` of the `car` of the tree plus `count-leaves` of the `cdr` of the tree.

Eventually we will `car` ourselves to the leaf of the tree, and so our base case will be:

  * `count-leaves` of a leaf is `1`

## `pair?`

When we call `car` on a tree, we have to determine if it returns another tree (a pair), or a leaf (an atom, or single element). How do we check for it? Racket has a built-in procedure `pair?` that tests if its argument is the result of a `cons`.

  * `(pair? (cons 1 2))` returns `#t`
  * `(pair? (cons 1 (cons 2 3)))` returns `#t`
  * `(pair? 2)` returns `#f`
  * `(pair? 'pear)` returns `#f`
  * `(pair? '())` returns `#f`

## `count-leaves`

Using the pseudo-code from the previous page and the `pair?` function above,
we can write the complete code for `count-leaves`:

    
    
    (define (count-leaves x)
        (cond ((null? x) 0) ;; is the tree is empty?
              ((not (pair? x)) 1) ;;is the tree a single element?
              (else (+ (count-leaves (car x)) ;; else, call count-leaves on the car
                       (count-leaves (cdr x))))) ;; and cdr of x and add them up.
    

## `scale-tree`

In Lesson 4, we saw the function `scale-list`, which multiplies each
item in the list by a given numeric factor. We are going to write an analogous
function, `scale-tree` that accepts a deep-list and a factor, and multiplies all elements in the deep-list by that factor.

Here is an example call:

    
    > (scale-tree (list 1 (list 2 (list 3 4) 5) (list 6 7)) 10)
    (10 (20 (30 40) 50) (60 70))


<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Below is an unfinished definition of scale-tree. Which <strong>base case(s)</strong> do we need in order to correctly define scale-tree?

<pre><code>(define (scale-tree tree factor)
  (cond ;;Your answer here.
        (else 
          (cons (scale-tree (car tree) factor) 
                (scale-tree (cdr tree) factor)))))
</code></pre>
<ans text="A. ((null? tree) 0)" explanation="Returning 0 for a null tree will cons extraneous 0s to the ends of sequences in some cases. Can you give an example for when this will happen?"></ans>
<ans text="B. ((null? tree) null)" explanation="This is a correct base case, but we also need another one for scale-tree to work correctly."></ans>
<ans text="C. ((not (pair? tree)) (* factor tree))" explanation="This is a correct base case, but we also need another one for scale-tree to work correctly."></ans>
<ans text="D. A and C" explanation="We handle the single element case correctly, but not the null tree case. Returning 0 for a null tree will cons extraneous 0s to the ends of sequences in some cases. Can you give an example for when this will happen?"></ans>
<ans text="E. B and C" explanation="Correct! B takes care of when the argument is an empty tree, while C checks if the input tree is an atom and correctly scales it by factor" correct></ans>
<!-- and so on -->
</div>

Now, try `scale-tree` out in your interpreter with some examples of your own!

## `deep-reverse`

Let's work on a problem with a similar structure. This time, we want to write a function, `deep-reverse`, that reverses the order of all elements in a deep-list. If written correctly, `deep-reverse` will also work for lists that do not contain other lists inside of it. Here is an example:

    
    > (define x (list (list 1 2) (list 3 4)))
    ((1 2) (3 4))
    
    > (deep-reverse x)
    ((4 3) (2 1))
    

Notice that not only do `(1 2)` and `(3 4)` switch places, but its elements do as well.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Below is an unfinished definition of deep-reverse. Which <strong>recursive call(s)</strong> do we need in order to correctly define deep-reverse?

<pre><code>(define (deep-reverse d-l)
  (cond ((null? d-l) null)
        ;;Your answer here.
  ))
</code></pre>
<ans text="A. ((pair? (car d-l)) (append (deep-reverse (cdr d-l)) (list (deep-reverse (car d-l)))))" explanation="This is a correct recursive call, but we also need another one for deep-reverse to work correctly."></ans>
<ans text="B. ((pair? (car d-l)) (append (cdr d-l) (list (deep-reverse (car d-l)))))" explanation="The cdr of the d-l must also be reversed!"></ans>
<ans text="C. (else (append (deep-reverse (cdr d-l)) (list (car d-l))))" explanation="This is a correct recursive call, but we also need another one for deep-reverse to work correctly."></ans>
<ans text="D. (else (append (car d-l) (list (deep-reverse (cdr d-l)))))" explanation="This recursive call does not reverse the car and cdr of d-l."></ans>
<ans text="E. A and C" explanation="Correct! The case where (car d-l) is a pair is taken care of by A, and the case where (car d-l) is not a pair is taken care of by C." correct></ans>
<ans text="F. B and D" explanation="Check the explanations for B and D, respectively"></ans>
<!-- and so on -->
</div>

Try this out in your Racket interpreter!

## Takeaways

As trees can contain subtrees, to do anything useful to data that are
contained in the leaves we generally have to use a recursive function.

