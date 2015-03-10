## Mutable Data, Vectors

Unit 2 dealt with compound data as a means for constructing computational
objects that have several parts. We abstracted their selectors and
constructors and see how they can be formed by nesting pairs and lists. But we
now know that there is another aspect of data that chapter 2 did not address.
We are now able to mutate data with `set!` and there is a similar operation
for pairs. We will explore `mutators`, operations that modify data objects.

## Prerequisites

For this lab, you will need to have understood unit 2 materials specifically
on manipulating lists and structure hierarchy. We are going to see how we can
mutate the elements and structures of pairs.

## Readings

You should read [SICP 3.3.1-3](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-22.html#%_sec_3.3) to learn about mutation.

You should read [these
notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=56) on
mutation and vectors. Vectors are not covered in SICP, so pay extra attention
to the notes.

## Mutating a Pair

In unit 2 we used pairs as the foundation of our data structures which stores
data. We have seen that we are now walking in a realm where it's possible to
mutate data. There will also be times when we want to mutate what is stored in
our data structures.

`(define x (cons 1 2))`

![](/static/lab9-1.png)

The car of x represents the number of times I fall down the stairs and the cdr
of x represents the number of times I went to the wrong bathroom. I fell down
a stair just now, so I should update the car of x to 2. How can we achieve
this? Scheme allows us to do `(set-car! x 2)`. As the name suggests, `set-
car!`takes in a pair and a value, and changes its car to point to the
specified value.

![](/static/lab9-2.png)

The general form is `(set-car! <pair> <value>)`

## set-cdr!

As you might expect, scheme also provides us with `set-cdr!` which takes in a
pair and a value, and changes the pointer of the pair's cdr to point to the
value. Going with the previous example, `(define x (cons 1 2))`, calling
`(set-cdr! x 3)` will change the pair as shown below.

![](/static/lab9-3.png)

The general syntax is `(set-cdr! <pair> <value>)`. We are going to see more
examples for cars and cdrs in the next subsection.

