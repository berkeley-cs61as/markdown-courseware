## Mutating a Pair

In Unit 2, we used pairs as the foundation of the data structures that store
data. We have seen that we are now walking in a realm where it's possible to
mutate data. There will also be times when we want to mutate what is stored in
our data structures.

`(define x (cons 1 2))`

![](/static/lab9-1.png)

### `set-car!`

Let the `car` of `x` represent the number of times I fall down the stairs and the `cdr` of `x` represent the number of times I went to the wrong bathroom. I fell down a flight of stairs just now, so I should update the `car` of `x` to `2`. How can we achieve this without creating a new pair? Scheme allows us to `set!` the value of some item using the following function:

	(set-car! x 2)

As the name suggests, `set-car!` takes in a pair and a value, and changes its `car` to point to the specified value of the second argument.

![](/static/lab9-2.png)

The general form is

	(set-car! <pair> <value>)

### `set-cdr!`

As you might expect, Scheme also provides us with the function `set-cdr!`, which takes in a pair and a value, and changes the pointer of the pair's `cdr` to point to the value. Going with the previous example, calling 

	(set-cdr! x 3)

will change the pair as shown below.

![](/static/lab9-3.png)

The general syntax is

	(set-cdr! <pair> <value>)

## Changing Pointers

Let us see how `set-car!` and `set-cdr!` work with more complicated lists. We are given the following pairs:    
    
    (define x (cons (list a b) (list c d)))
    (define y (list e f))
    

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-13.gif)

The next few calls on `set-car!` and `set-cdr!` are independent and will be
based on this original configuration. For the next few questions, drawing the
box-pointer is highly recommended.

### Example 1

The effect of calling

	(set-car! x y)

to the original configuration will give the resulting box-and-pointer diagram:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-14.gif)

The call changes the car-pointer on `x`, which initially points to `(list a b)`, to wherever `y` is pointing: `(list e f)`. What happens to the list with `a` and `b`? Nothing actually happens to it, but since it has no pointers that reference it, the list is no longer reachable.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
In Example 1 above, what does <code>x</code> print?.

<ans text="(e f c d)" explanation=""></ans>
<ans text="((e f) c d)" explanation="" correct></ans>
<ans text="(e f (c d))" explanation=""></ans>
<ans text="((e f) (c d))" explanation=""></ans>
<ans text="(ask sam 'write-check 50)" explanation=""></ans>
<!-- and so on -->
<br>
Let's say we have the original configuration from Example 1, and now we decided to call the following expression:

<pre><code>(set-car! (car x) 'z)</code></pre>

What does <code>y</code> print?

<ans text="(e f)" explanation=""></ans>
<ans text="(z f)" explanation="(car x) will return the pair that contains 'e. The set-car! will change its car-pointer from 'e to 'z. Because y shares that pair with x, y is now (z f)" correct></ans>
<ans text="Error" explanation=""></ans>
</div>


### Example 2

From the original configuration, we now call

	(define z (cons y (cdr x)))

This gives us the following box-and-pointer diagram:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-15.gif)


  * `x` will print `((a b) c d)`

  * `y` will print `(e f)`

  * `z` will print `((e f) c d)`

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
From the configuration shown in Example 2, we now decide to call

<pre><code>(set-cdr! (cdr z) nil)</code></pre>

What does <code>x</code> print now?

<ans text="(a b)" explanation=""></ans>
<ans text="((a b))" explanation=""></ans>
<ans text="((a b) c)" explanation="(cdr z) will return the pair with 'c. The set-cdr will change its cdr pointer to nil. The pair with 'd now has nothing that points to it." correct></ans>
<!-- and so on -->
<br>
From the configuration shown in Example 2, what should we call so that <code>z</code> will return <code>((e f) b)</code>?

<ans text="(set-cdr! z (car x))" explanation=""></ans>
<ans text="(set-cdr! z (cadar x))" explanation=""></ans>
<ans text="(set-cdr! z (cdar x))" explanation="the car of z currently points (e f) already. Its cdr, points to the pair with c which is not where we want it to be. We want to call something like (set-cdr! z ???). ??? needs to be the pair with b, which is (cdar x)." correct></ans>
<ans text="(set-car! (cdar x) (cdr z))" explanation=""></ans>
<ans text="Cannot be done with a single call" explanation=""></ans>
</div>

## Creating New Pairs

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

<div class="mc">
<strong>Test Your Understanding</strong><br><br>

What will the following piece of code print when entered into STk? Take an educated guess, then try it out in the interpreter.

	> (define a (list 1 2 3 4 5))
	a
	> (set-cdr! (cdr a) (cdddr a))
	okay
	> a

<ans text="Click here to reveal answer." explanation="(1 2 4 5)" correct></ans>
<br>
The procedure `append!` is similar to `append`, but it is a mutator rather than a constructor. It appends the lists by splicing them together, modifying the final pair of `x` so that its `cdr` is now `y`. (It is an error to call `append!` with an empty `x`.) For example,

<pre><code>(define (append! x y)
	(set-cdr! (last-pair x) y)
	x)</code></pre>

The `last-pair` procedure accepts a list and returns the last pair of the list:

<pre><code> (define (last-pair x)
	(if (null? (cdr x))
		x
		(last-pair (cdr x))))</code></pre>

Now, let's take a look at this piece of code:

<pre><code>> (define x (list 'a 'b))
x      
> (define y (list 'c 'd))
y
> (define z (append x y))
z     
> z
(a b c d)</code></pre>

What does <code>(cdr x)</code> return? Try it out by yourself before putting it into STk.

<ans text="Click here to reveal answer." explanation="(b)" correct></ans>

Now, take the following call to <code>append!</code>

<pre><code>> (define w (append! x y))
w
> w
(a b c d)</code></pre>

What does <code>(cdr x)</code> return now?

<ans text="Click here to reveal answer." explanation="(b c d)" correct></ans>
</div>

## Sharing and Identity

The previous exercises raises a big sign that knowing when a pair is shared and created is important. In the code above, `x` and `y` refer to the same pairs, while `z` makes a different pair with the same elements.

![](/static/lab9-5.png)

```
(define x (cons 1 2))
(define y x)
(define z (cons 1 2))
```

Remember the `equal?` predicate? It can check if two pairs contain the same
elements.

`(equal? x y)`, `(equal? x z)`, `(equal? y z)` all return `#t`, because they all hold the same elements at the same place. Is it possible to differentiate that `x` and `z` point to different structures? Yes! Scheme has the `eq?` predicate which takes 2 arguments and checks if the 2 arguments refer to the same pair.

```
> (eq? x y)
#t
> (eq? x z)
#f
> (eq? y z)
#f
```

## Takeaways

`set-car!` and `set-cdr!` change the respective `car` and `cdr` pointers. Procedures like `cons`, `list`, and `append` create new pairs. Knowing which pairs are shared between different lists is crucial to determining whether mutating one will influence the other. Drawing box-and-pointer diagrams will be very helpful.