## Mutating a Pair

In Unit 2, we used pairs as the foundation of our data structures that stores data. We are now walking in a realm where it's possible to mutate, or _destructively update_ data. This terminology is not meant to have any negative connotation - it simply means that an update to mutable data will "destroy" the old value of the data structure.

## Creating Mutable Pairs and Lists

To create a **mutable pair**, we use the procedure `mcons`. Its corresponding selectors for extracting the first and second elements of the **mpair** are `mcar` and `mcdr`, respectively:

	-> (define x (mcons 1 2))
	-> (mcar x)
	1
	-> (mcdr x)
	2

Similarly, **mutable lists** are simply nested mpairs, created using the procedure `mlist`:

	-> (define y (mlist 1 2 3))
	-> (mcar y)
	1
	-> (mcdr y)
	(mcons 2 (mcons 3 '()))

Notice how taking the `mcdr` of a mutable list does not return `'(2 3)`. The above notation is used to emphasize the difference between a **pair** and an **mpair**. Again, they are completely different data structures. 

## Changing Pointers

Suppose we have our first example:

	(define x (mcons 1 2))

![](/static/lab9-1.png)

The `car` of `x` represents the number of times I fall down the stairs and the cdr of x represents the number of times I went to the wrong bathroom. I fell down
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

## Changing Pointers

Let us see how `set-car!` and `set-cdr!` work with more complicated lists.

    
    
    (define x (cons (list a b) (list c d)))
    (define y (list e f))
    

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-13.gif)

The next few calls on `set-car!` and `set-cdr!` are independent and will be
based on this original configuration. For the next few questions, drawing the
box-pointer is highly recommended.

## Scenario 1

The effect of calling `(set-car! x y)` to the original configuration:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-14.gif)

The call changes the car-pointer on x, which was initially pointing to the
`(list a b)` is now pointing to what y is pointing, `(list e f)`. Now what
happened to the list with a and b? Since nothing points to it right now, we
can't access it anymore.

## Scenario 2

From the original configuration, we called `(define z (cons y (cdr x)))`.

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-15.gif)

`x` will print ((a b) c d)

`y` will print (e f)

`z` will print ((e f) c d)

## CHANGING POINTERS, Creating new pairs

Using `set-car!` and `set-cdr!` modifies existing pairs. Procedures like
`cons` and `list` on the other hand, creates a new pair. What about `append`?
Does it 'merge' two lists by changing the `cdr` pointer of one of them?
Remember the definition of `append` we have been using:

    
    
    (define (append x y)
      (if (null? x)
          y
          (cons (car x) (append (cdr x) y))))
    

`append` forms a new list by `cons`-ing elements of `x` and `y`. This tells us
that `append` returns a new list.

![](/static/lab9-4.png)

## Sharing and Identity

The previous exercises raises a big sign that knowing when a pair is shared
and created is important. In the code above, x and y refer to the same pairs
while z makes a different pair with the same elements.

![](/static/lab9-5.png)

`(define x (cons 1 2))`

`(define y x)`

`(define z (cons 1 2))`

Remember the `equal?` predicate? It can check if two pairs contain the same
elements.

`(equal? x y), (equal? x z), (equal? y z)` all returns true because all
structure holds the same elements at the same place, 1 and 2. Is it possible
to differentiate that x and z point to different structures? Yes! Scheme has
the `eq?` predicate which takes 2 arguments and checks if the 2 arguments
"refer to the same thing".

`(eq? x y)` returns #t

`(eq? x z)` returns #f

`(eq? y z)` returns #f

## Takeaways

set-car! and set-cdr! change the respective car and cdr pointers. Procedures
like `cons,` `list` and `append` create new pairs. Knowing which pairs are
shared between different lists is crucial to determining whether mutating one
will influence the other. Drawing box-pointer diagrams will be very helpful.

