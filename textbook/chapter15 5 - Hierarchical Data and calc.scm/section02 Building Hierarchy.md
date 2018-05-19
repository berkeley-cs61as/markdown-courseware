## Composing pairs and lists

Previously we saw how to use `cons` to "group" a pair of values together,
e.g. `(cons 1 2)`, which returns a pair `(1 . 2)`. We can also use `list` to
group an arbitary amount of data together. For example if you type `(list 1 2
'bagel 4)` in the interpreter, Racket will print the list `(1 2 bagel 4)`.
Notice that we can put *any* sort of data inside them, even other pairs and lists!

Now let's make a pair of lists:

```
(cons (list 1 2) (list 3 4))
```

The first item of the pair is the list `(1 2)` and the second is the list `(3 4)`. We can show this structure with the following box-and-pointer diagram:

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch2-Z-G-15.gif)

(If you aren't familiar with drawing and interpreting box-and-pointer diagrams, please go back and review the [section](http://berkeley-cs61as.github.io/textbook/representing-sequences.html) in Lesson 4.)

You can also represent the structure `((1 2) 3 4)` using a **little-t tree**:

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch2-Z-G-16.gif)

With litle-t trees, every element in a sequence is a node. In the example above, `(1 2)` is an element of `((1 2) 3 4)`,
so it's a node. But it's also a tree with two children nodes&mdash;one for each element.

Why do we call this a "little-t tree"? Later on in this lesson, we'll discuss the "capital-T Tree" data type, which is *completely
different* from the little-t tree data type. We use this notation for the sake of consistency and clarity.

We may also refer to little-t trees as **deep lists** (since they are lists within lists within lists within...), which is less ambiguous, but also less descriptive of the tree-like structure of lists of lists.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Suppose we evaluate the expression <code>(list 1 (list 2 (list 3 4)))</code>. What is returned when we enter this into the interpreter? Draw for yourself the corresponding box-and-pointer structure and the corresponding little-t tree.

<ans text="<code>(1 2 3 4)</code>" explanation="This answer lacks nested structure!"></ans>
<ans text="<code>(1 (2 (3 4)))</code>" explanation="Yes!" correct></ans>
<ans text="<code>(1 2 (3 4))</code>" explanation="Isn't the list containing 2 nested inside the outermost list?"></ans>
<ans text="<code>(1 . 2 . 3 4)</code>" explanation="Too many dots!"></ans>
<ans text="None of the above" explanation="Sorry, try again!"></ans>
<!-- and so on -->
</div>

## Takeaways

In this section, we discussed nested `cons` structures. We also introduced little-t trees.

### Before We Continue...

Review the [shorthand notation](http://berkeley-cs61as.github.io/textbook/representing-sequences.html#sub2) for `car`s and `cdr`s.
It will come in handy!
