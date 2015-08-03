## Mutating a Pair

In Unit 2, we used pairs as the foundation of our data structures that stores data. We are now walking in a realm where it's possible to mutate, or _destructively update_ data. This terminology is not meant to have any negative connotation - it simply means that an update to mutable data will "destroy" the old value of the data structure, clearing any previous values.

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

## Changing Pointers: `set-mcar!`

Suppose we have our first example:

	(define x (mcons 1 2))

![](/static/lab9-1.png)

Let the `mcar` of `x` represent the number of cloudy days this week and the `mcdr` of `x` represent the number of sunny days. We observe that today is cloudy, so we update the `mcar` of `x` to `2`. How do we achieve this? Racket allows us to call `(set-mcar! x 2)`. As the name suggests, `set-mcar!` takes in a mpair and a value, and changes the `mcar` of that mpair to point to the specified value.

![](/static/lab9-2.png)

The general form is `(set-mcar! <pair> <value>)`

## Changing Pointers: `set-mcdr!`

As you might expect, Racket also provides us with `set-mcdr!`, which takes in a mpair and a value, and changes the mpair's `mcdr` pointer to point to the specified value. Using the previous example:

![](/static/lab9-1.png)


Calling `(set-mcdr! x 3)` will change the mpair as shown below.

![](/static/lab9-3.png)

The general form is `(set-mcdr! <pair> <value>)`. 

## Mutating Complex Pairs

In this subsection, we will go over mutation using `set-mcar!` and `set-mcdr!` on more complex pairs.

Let us work with the following mpairs and their box-and-pointer diagrams:
    
    (define x (mcons (mlist 'a 'b) (mlist 'c 'd)))
    (define y (mlist 'e 'f))    

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-13.gif)

We'll now work through two different examples in which mutation occurs. Each scenario will start off with the original mpairs defined above. We highly recommend drawing box-and-pointer diagrams for each exercise.

### Example 1

What happens when we call `(set-mcar! x y)` on the original configuration? The `mcar` pointer of `x`, which initially pointed to `(mlist 'a 'b)`, is changed to point to what `y` points to, `(mlist 'e 'f)`. This call thus results in the following box-and-pointer diagram:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-14.gif)

What happens to the mlist of 'a and 'b? Since there are no longer any pointers that point _to_ that mlist, it is no longer accessible and will eventually be erased from memory.

<div class="mc">
	<strong>Test Your Understanding</strong>
	<br><br>
	What does <code>x</code> from Example 1 print?
	<ans text="(mcons 'e (mcons 'f (mcons 'c (mcons 'd '()))))" explanation=""></ans>
	<ans text="(mcons (mcons 'e (mcons 'f '())) (mcons 'c (mcons 'd '())))" explanation="" correct></ans>
	<ans text="(mcons 'e (mcons 'f (mcons (mcons 'c (mcons 'd '())) '())))" explanation=""></ans>
	<ans text="(mcons (mcons 'e (mcons 'f '())) (mcons (mcons 'c (mcons 'd '())) '()))" explanation=""></ans>
	<br><br>
	From Example 1, we now call 

	<pre><code>(set-mcar! (mcar x) 'z)</code></pre> 

	What does <code>y</code> from Example 1 print?
	<ans text="(mcons 'e (mcons f '()))" explanation=""></ans>
	<ans text="(mcons 'z (mcons f '()))" explanation="(mcar x) will return the pair that contains 'e. The call to set-mcar! will change its mcar pointer from 'e to 'z. Because y shares that pair with x, y is now (mcons 'z (mcons f '()))" correct></ans>
	<ans text="Error" explanation=""></ans>
</div>

### Example 2

This time, let's define a new mpair, `z`, like so: 

	(define z (mcons y (mcdr x)))

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-15.gif)

  * `x` will print ((a b) c d)
  * `y` will print (e f)
  * `z` will print ((e f) c d)

<div class="mc">
	<strong>Test Your Understanding</strong>
	<br><br>
	From Example 2, we now call:

	<pre><code>(set-mcdr! (mcdr z) null)</code></pre>

	What does <code>x</code> print in this case?
	<ans text="(mcons 'a (mcons 'b '()))" explanation=""></ans>
	<ans text="(mcons (mcons 'e (mcons f '())) '())" explanation=""></ans>
	<ans text="(mcons (mcons 'e (mcons f '())) (mcons 'c '()))" explanation="(mcdr z) will return the mpair with 'c. The set-mcdr! will change its mcdr pointer to null. The mpair with 'd now has nothing that points to it." correct></ans>
	<br><br>
	From Example 2, what needs to be called such that <code>z</code> will return <code>(mcons (mcons e (mcons f '())) (mcons b '()))</code>?
	<ans text="(set-mcdr! z (mcar x))" explanation""></ans>
	<ans text="(set-mcdr! z (mcar (mcdr (mcar x))))" explanation=""></ans>
	<ans text="(set-mcdr! z (mcdr (mcar x)))" explanation="the mcar of z currently points (e f) already. Its mcdr points to the mpair with c, which is not where we want it to be. We want to call something like (set-mcdr! z ???). ??? needs to be the mpair with b, which is (mcdr (mcar x))." correct></ans>
	<ans text="(set-mcar! (mcdr (mcar x)) (mcdr z))" explanation=""></ans>
	<ans text="Cannot be done in a single call." explanation=""></ans>
</div>

## `append` vs. `mappend` vs. `mappend!`

Before we start this subsection, try this exercise our to make sure you are somewhat familiar with mutating mpairs.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Given the following piece of code:

<pre><code>(define a (mlist 1 2 3 4 5))
(set-mcdr! (mcdr a) (mcdr (mcdr (mcdr a))))</code></pre>

What will <code>a</code> print? Try it yourself by drawing a box-and-pointer diagram first, and then check your work with the Racket interpeter.

<ans text="Click to show answer." explanation="(mcons 1 (mcons 2 (mcons 4 (mcons 5 '()))))" correct></ans>
</div>

### `append`

Recall the definition of `append` we have been using for non-mutable pairs:

	(define (append x y)
		(if (null? x)
    	y
    	(cons (car x) (append (cdr x) y))))

`append` forms a new list by `cons`-ing together the elements of `x` and `y`. This means that `append` returns a new list.

![](/static/lab9-4.png)

### `mappend`

We want to do the same for mutable pairs, but since they are different data types from immutable pairs, `append` will not work for them. Instead, the analogous non-destructive function for mutable pairs is called **`mappend`**. `mappend` returns a new list, and works almost exactly like `append`:

	(define (mappend mx my)
		(if (null? mx)
			my
			(mcons (mcar mx) (mappend (mcdr mx) my))))

Racket's actual implementation of `mappend` will take in any number of mlists as arguments and will return a new mlist with all argument mlists appended together.

### `mappend!`

If, instead, we wish to destructively append mlists together, without creating any new mpairs, the Racket procedure `mappend!` (pronounced m-append-bang) will mutate the tail of each argument mlist to refer to the next, using `set-mcdr!`. Here is a simplified definition that only takes in two mlists:

	(define (mappend! mx my)
		(if (null? (mcdr mx))
			(set-mcdr! mx my)
			(mappend! (mcdr mx) my)))

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Given the following piece of code:

<pre><code>-> (define x (mlist 'a 'b))
x
-> (define y (mlist 'c 'd))
y
-> (define z (mappend x y))
z
-> z
(mcons 'a (mcons 'b (mcons 'c (mcons 'd '()))))</code></pre>

What does <code>(mcdr x)</code> return?

<ans text="Click to show answer." explanation="(mcons 'b '()) mappend does not change any existing mpairs, so it does not change x." correct></ans>
<br><br>
Assume <code>x</code> and <code>y</code> are as defined above. We now execute this piece of code:

<pre><code>> (define w (mappend! x y))
w
-> w
(mcons 'a (mcons 'b (mcons 'c (mcons 'd '()))))</code></pre>

What does <code>(mcdr x)</code> return now?

<ans text="Click to show answer." explanation="(mcons 'b (mcons 'c (mcons 'd '()))) mappend! will make the mcdr of the last pair in x point to y. We then assign w to x." correct></ans>
</div>

## Sharing and Identity

We can see from the previous exercises that it is imperative to know when an mpair is shared and when it is being created. Take the following example:

	-> (define x (mcons 1 2))
	x
	-> (define y x)
	y
	-> (define z (mcons 1 2))
	z

In the code above, `x` and `y` refer to the same mpair, while `z` points to a different mpair that contains the same elements. This is what their box-and-pointer diagrams look like:

![](/static/lab9-5.png)

Recall from Lesson 0.2 the `equal?` predicate. Earlier, we vaguely described `equal?` as a procedure that checks two arguments for equality. To be more specifice, when `equal?` is called with two mpairs, it will return `#t` if they contain the same elements, and `#f` otherwise. If we use `equal?` on our `x`, `y`, and `z` above, we will get the following:

	-> (equal? x y)
	#t
	-> (equal? x z)
	#t
	-> (equal? y z)
	#t

Even though `z` points to a different pair than `x` and `y`, since all three mpairs contain the same elements, `equal?` will return `#t` for all three expressions above.

But then, how can we differentiate between different pairs? We introduce a third equality checker, a Racket primitive called `eq?`, that checks whether its two arguments **point** to the same object.

	-> (equal? x y)
	#t
	-> (equal? x z)
	#f
	-> (equal? y z)
	#f

## MPair Operators

Since mpairs are a completely data type from pairs, as we have mentioned time and time again, they have a separate set of operators. We saw above that the operators for pairs and lists, such as `cons`, `list`, `car`, and `cdr` will not work on mpairs and mlists.

The comprehensive set of mpair operators can be found in the Racket documentation [here](http://docs.racket-lang.org/reference/mpairs.html) and [here](http://docs.racket-lang.org/compatibility/mlists.html).

## Takeaways
  * `set-mcar!` and `set-mcdr!` change the respective `mcar` and `mcdr` pointers of an mpair. 
  * Procedures such as `mcons,` `mlist` and `mappend` create new mpairs. 
  * Knowing which mpairs are shared between different mlists is crucial to determining whether mutating one will influence the other. 
  * Drawing box-and-pointer diagrams extremely helpful in sorting out mpairs and visually analyzing the effects of mutative procedures.