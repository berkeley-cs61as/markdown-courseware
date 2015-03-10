## Composing cons and lists

Previously we have seen how to use cons to 'group' a pair of data together,
like `(cons 1 2)` which returns a pair `(1 . 2)`. We can also use `list` to
group an arbitary amount of data together. For example if you type `(list 1 2
'bagel 4)` in the interpreter, Scheme will print the list `(1 2 bagel 4)`.
Notice that we can put **any** sort of data inside them, even pairs and lists!

The following call makes a pair of lists:

`(cons (list 1 2) (list 3 4))`. The first item of the pair is the list `(1 2)`
and the second is the list `(3 4)`. We can show this structure with the
following box-and-pointers diagram:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-15.gif)

You can also represent the structure using "little-t trees"

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-16.gif).

The elements in each sequence is treated as a branch of the tree. Elements
that are sequences (for example the `(1 2)`) are called subtrees.

Why did we call them "little-t trees"? Later on in this section, we are going
to be learning about the "big-T Tree" data type, which is** completely
different** from the tree data type. Sorry about this confusion, but it's the
notation that the book uses and we use it for the sake of consistancy.

We may also refer to "little-t trees" as "deep lists" (lists of lists of lists
of ...), which is less ambiguous, but also less descriptive of the tree-like
structure of lists of lists.

## Shortcut

Series of cars and cdrs can be downright ugly, like in the previous exercise.
In the online interpreter we use as well as in Emacs, there is a built-in
short-hand notation to do a series of cars and cdrs.

` (car (cdr a))` is equivalent to ` (cadr a) `.

`(car (cdr (car (car a))))` is equivalent to `(cadaar a)`.

In general you can do up to ` cxxxxr ` where x is either a or d.

![](http://socialkennesaw.com/wp-content/uploads/2013/05/half-cop-car-
ksaw.jpg)

## takeaways

In this subsection, you learned:

  * We can use nested `cons` to make a nested list
  * The nested list can be represented as a tree structure
  * `caar`, `caddr`, `caaaadddddddr`

