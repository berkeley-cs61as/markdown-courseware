## An Overview of Little-t Trees

Let's discuss some general properties of little-t trees.
We've seen that structures like `(cons (list 1 2) (list 3 4))`
can be represented in a tree-like structure:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-16.gif)

Little-t trees are composed of *branches* and *leaves*.
The tree above has five
**branches**; they correspond to the lines on the diagram above. Notice that a
branch can lead to a **subtree**&mdash;a tree that is contained within a larger tree.
In this case, the branch `((1 2) 3 4)` contains the subtree `(1 2)`.
A **leaf** has no branches connecting from it. The tree above has 4 leaves: `1`, `2`, `3`, and `4`.
Leaves are found at the "bottom" of the tree, also called the **fringe**. 

Compared to trees in the real world, trees in computer science tend to be upside-down!

## Recursion with Little-t Trees

When working with trees, it is usually helpful to think recursively.
As an example, let's write a function `count-leaves` that counts the number of leaves in a tree.

We'll start by informally outlining what our function will do in plain English.
This is called writing **pseudocode**. After we understand how our `count-leaves` function
should behave, we'll write the actual Racket code for it. This is good general technique for
solving problems.

### Pseudocode

Recall how we defined `length`, which finds the number of elements in a list:

  * `length` of an empty list is 0.
  * `length` of a non-empty list `x` is 1 plus the `length` of the `cdr` of `x`.

The base case is the same for `count-leaves`:

  * `count-leaves` of an empty list is 0.

Our recusive case is slightly different though.
In `length`, we are guaranteed that the `car` of the list is a single element, so we count its length as 1.
But for `count-leaves`, its `car` may contain one or more trees, and so its length will not always be 1.
Therefore, we need to recursively find the `count-leaves` of the `car` of the tree as well! Our recursive call is therefore:

  * `count-leaves` of a tree is the `count-leaves` of the `car` of the tree plus `count-leaves` of the `cdr` of the tree.

Eventually we will `car` ourselves to the leaf of the tree, and so our second base case will be:

  * `count-leaves` of a leaf is `1`.

### The `pair?` Predicate

When we call `car` on a tree, we have to determine if it returns another tree (a pair), or a leaf (a single element, technically known as an *atom*).
How do we check for it? Racket has a built-in predicate `pair?` that tests if its argument is the result of a `cons`. For example:

  * `(pair? (cons 1 2))` returns `#t`.
  * `(pair? (cons 1 (cons 2 3)))` returns `#t`.
  * `(pair? 2)` returns `#f`.
  * `(pair? 'pear)` returns `#f`.
  * `(pair? '())` returns `#f`.

### Real Code

Using `pair?` and the pseudocode above,
we can write the complete code for `count-leaves`:
    
    (define (count-leaves x)
        (cond ((null? x) 0) ;; is the tree is empty?
              ((not (pair? x)) 1) ;;is the tree a single element?
              (else (+ (count-leaves (car x)) ;; else, call count-leaves on the car
                       (count-leaves (cdr x))))) ;; and cdr of x and add them up.
    

## Example: `scale-tree`

In Lesson 4, we saw the function `scale-list`, which multiplies each
item in a list by a given numeric factor. We are going to write an analogous
function, `scale-tree`, which accepts a deep list and a numeric factor and multiplies all elements in the deep list by that factor.

Here is an example call:

    
    > (scale-tree (list 1 (list 2 (list 3 4) 5) (list 6 7)) 10)
    (10 (20 (30 40) 50) (60 70))


<div class="mc">
<p>
<strong>Test Your Understanding</strong>
<p>
Below is an unfinished definition of scale-tree. Which base case(s) do we need to correctly define <code>scale-tree</code>?

<pre><code>(define (scale-tree tree factor)
  (cond ;;Your answer here.
        (else 
          (cons (scale-tree (car tree) factor) 
                (scale-tree (cdr tree) factor)))))
</code></pre>
<ans text="A. <code>((null? tree) 0)</code>" explanation="Returning 0 for a null tree will cons extraneous 0s to the ends of sequences in some cases. Can you give an example for when this will happen?"></ans>
<ans text="B. <code>((null? tree) null)</code>" explanation="This is a correct base case, but we also need another one for scale-tree to work correctly."></ans>
<ans text="C. <code>((not (pair? tree)) (* factor tree))</code>" explanation="This is a correct base case, but we also need another one for scale-tree to work correctly."></ans>
<ans text="D. Both A and C" explanation="We handle the single element case correctly, but not the null tree case. Returning 0 for a null tree will cons extraneous 0s to the ends of sequences in some cases. Can you give an example for when this will happen?"></ans>
<ans text="E. Both B and C" explanation="Correct! B takes care of when the argument is an empty tree, while C checks if the input tree is an atom and correctly scales it by factor." correct></ans>
<!-- and so on -->
</div>

Now, try `scale-tree` out in your interpreter with some examples of your own!

## Example: `deep-reverse`

Let's work on a problem with a similar structure.
This time, we want to write a function called `deep-reverse` that reverses the order of all elements in a deep list.
For example:

    
    > (define x (list (list 1 2) (list 3 4)))
    ((1 2) (3 4))
    
    > (deep-reverse x)
    ((4 3) (2 1))
    

Notice that not only do `(1 2)` and `(3 4)` switch places, but their elements do as well.
`deep-reverse` should also work for lists that do not contain other lists inside of it.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Below is an unfinished definition of <code>deep-reverse</code>.
Which recursive call(s) do we need in order to correctly define <code>deep-reverse</code>?

<pre><code>(define (deep-reverse d-l)
  (cond ((null? d-l) null)
        ;;Your answer here.
  ))
</code></pre>
<ans text="A. ((pair? (car d-l)) (append (deep-reverse (cdr d-l)) (list (deep-reverse (car d-l)))))" explanation="This is a correct recursive call, but we also need another one for deep-reverse to work correctly."></ans>
<ans text="B. ((pair? (car d-l)) (append (cdr d-l) (list (deep-reverse (car d-l)))))" explanation="The cdr of the d-l must also be reversed!"></ans>
<ans text="C. (else (append (deep-reverse (cdr d-l)) (list (car d-l))))" explanation="This is a correct recursive call, but we also need another one for deep-reverse to work correctly."></ans>
<ans text="D. (else (append (car d-l) (list (deep-reverse (cdr d-l)))))" explanation="This recursive call does not reverse the car and cdr of d-l."></ans>
<ans text="E. Both A and C" explanation="Correct! The case where (car d-l) is a pair is taken care of by A, and the case where (car d-l) is not a pair is taken care of by C." correct></ans>
<ans text="F. Both B and D" explanation="Check the explanations for B and D, respectively"></ans>
<!-- and so on -->
</div>

Try this out in your Racket interpreter!

## Takeaways

Trees can contain subtrees, so recursion can be very helpful when solving problems involving trees.
