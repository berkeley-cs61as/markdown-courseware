## Composing cons and lists

Previously we have seen how to use `cons` to 'group' a pair of data together,
like `(cons 1 2)` which returns a pair `(1 . 2)`. We can also use `list` to
group an arbitary amount of data together. For example if you type `(list 1 2
'bagel 4)` in the interpreter, Racket will print the list `(1 2 bagel 4)`.
Notice that we can put **any** sort of data inside them, even pairs and lists!

The following call makes a pair of lists:

`(cons (list 1 2) (list 3 4))`. The first item of the pair is the list `(1 2)` and the second is the list `(3 4)`. We can show this structure with the following box-and-pointers diagram:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-15.gif)

**Note:** if, at this point, you are not familiar with drawing and interpreting box-and-pointer diagrams, please go back and review the [section](http://berkeley-cs61as.github.io/textbook/representing-sequences.html) in Lesson 4.

You can also represent the structure using "little-t trees"

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-16.gif).

Every element in a sequence is a node in a tree. Elements
that are sequences (i.e., `(1 2)`) are called subtrees, where its branches have nodes containing the elements of that sequence. Elements that are not sequences (i.e., `3`) are also subtrees, but do not have any branches connecting off of it.

Why did we call them "little-t trees"? Later on in this section, we are going
to be learning about the "capital-T Tree" data type, which is **completely
different** from the tree data type. This notation is kept for the sake of consistency and clarity.

We may also refer to "little-t trees" as "deep lists" (since they are lists within lists within lists within ...), which is less ambiguous, but also less descriptive of the tree-like
structure of lists of lists.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Suppose we evaluate the expression (list 1 (list 2 (list 3 4))). What is returned when we enter this into the interpreter? Draw for yourself the corresponding box-and-pointer structure, and the interpretation of this as a tree.

<ans text="(1 2 3 4)" explanation=""></ans>
<ans text="(1 (2 (3 4)))" explanation="" correct></ans>
<ans text="(1 2 (3 4))" explanation=""></ans>
<ans text="(1 . 2 . 3 4)" explanation=""></ans>
<ans text="None of the above" explanation=""></ans>
<!-- and so on -->
</div>

## Shorthand Review

To make your life easier, make sure you refresh yourself on [shorthand notation](LINK HERE!!!!!) for `car`s and `cdr`s.

![](http://socialkennesaw.com/wp-content/uploads/2013/05/half-cop-car-
ksaw.jpg)

## Takeaways

In this subsection, you learned:

  * We can use nested `cons` to make a nested list
  * The nested list can be represented as a tree structure
  * `caar`, `caddr`, `cdaddr`

