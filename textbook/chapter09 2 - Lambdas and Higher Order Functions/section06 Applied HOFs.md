**Note:** This section is a bit more dense than the rest of the lesson. If you struggle with this section, don't worry&mdash;it's more advanced than most of what we'll expect you to know.

Here, we will explore two applied examples using the tools we have learned so
far: `fixed-point` and `iterate`.

## `fixed-point`

We will first try to express the calculation of **fixed points**
of functions. A number `x` is called a fixed point of a function `f` if `x`
satisfies the equation `f(x) = x`.

An algorithm that finds a fixed point for some functions `f` is one where we start with an initial guess and apply `f` repeatedly, until successive values are very close.

    
    x  
    (f x)  
    (f (f x))  
    ...

Using this idea, we'll make a procedure `fixed-point` that will keep applying a
function until we find two successive values whose difference is less than
some prescribed `tolerance`. Take a look at our definition of `fixed-point` below:


    (define tolerance 0.00001)
    
    (define (fixed-point f first-guess)
        (define (close-enough? v1 v2)
            (< (abs (- v1 v2)) tolerance))
        (define (try guess)
           (let ((next (f guess)))
              (if (close-enough? guess next)
                  next
                  (try next))))
        (try first-guess))

For example, we can use this method to approximate the fixed point of the
cosine function, starting with 1 as an initial approximation:

    -> (fixed-point cos 1.0)
    0.7390822985224024

To demonstrate the power of abstracting functions with `fixed-point`, we will
develop a method to calculate square roots with only 3 lines of Racket code!

Computing the square root of some number `x` requires finding a `y` such that
<code>y<sup>2</sup> = x</code>. Putting this equation into the equivalent form `y = x / y`, you can see that we are looking for a fixed point of the function `(lambda (y) (/ x y))`. In code:


    (define (sqrt x)
        (fixed-point (lambda (y) (/ x y))
        1.0))

If you happen to have an interpreter handy, though, you'll find that this
doesn't work. To see why, look at the successive guesses of, say, `(sqrt 4)`:

```
1
4/1 = 4
4/4 = 1
4/1 = 4
...
```

It just keeps oscillating! If you think about it, it'll do that for any
number we put in (except 0 or 1).

So, instead of changing the guess by `1`, we'll adjust by a little less. To
do that, we'll average the next guess with the current guess. That is, the
next guess after `y` is `(1/2)(y + x/y)` instead of `x/y`.

The process of making such a sequence of guesses is simply the process of
looking for a fixed point of `y = (1/2)(y + x/y)`:


    (define (sqrt x)
        (fixed-point (lambda (y) (* 0.5 (+ y (/ x y))))
        1.0))

With this modification, the square-root procedure works.  This approach of
averaging successive approximations to a solution, a technique the SICP
authors call `average damping`, often aids the convergence of fixed-
point searches.

So, let's continue our abstraction frenzy and abstract the average damping
technique as well:

    
    (define (average-damp f)  
         (lambda (y) (* 0.5 (+ y (f y)))))

And now, a new `sqrt`:

    
    (define (sqrt x)  
      (fixed-point (average-damp (lambda (y) (/ x y)))  
                   1.0))

Amazingly clear, eh?

Notes:

`y = (1/2)(y + x/y)` is a simple transformation of the equation `y =
x / y`; to derive it, add `y` to both sides of the equation and divide by `2`.

You may have noticed that we have effectively derived Newton's method for
calculating square roots. But... there are so many other ways! If you're
intersted, here's a [cool link](http://en.wikipedia.org/wiki/Methods_of_computing_square_roots).

## `iterate`

We will now conclude this lesson with another higher order function.

This one will allow us to write `fixed-point` AND `largest-square` (from Lesson 1).

How, you ask? Because they both fall under the general form of **iterative
improvement**. That is, you start with a value and keep improving it until it
is good enough.

Notice there are 3 things to abstract here:

  1. the starting value
  2. the function to improve
  3. the function to test if it's good enough

So, with that, we know our parameters and what it should do, so let's write
it!

    
    (define (iterate start improve good-enough?)  
       (if (good-enough? start)  
           start  
           (iterate (improve start) improve good-enough?)))

And now, I'll express `largest-square` with `iterate`:

    
    (define (largest-square total guess)  
        (iterate guess   
                 (lambda (x) (+ x 1))  
                 (lambda (x) (< total (square (+ x 1))))  
          ))

Our abstraction frenzy (mostly) ends here, but be on your toes. Abstraction is
what allows programmers to write complex but readable systems.

Never miss a good opportunity to abstract.
