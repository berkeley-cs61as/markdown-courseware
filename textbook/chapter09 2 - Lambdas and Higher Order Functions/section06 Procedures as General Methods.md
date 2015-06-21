Here, we will explore a more applied example using the tools we learned so
far.

In particular, we will first try to express the calculation of _fixed points_
of functions. A number _x_ is called a _fixed point_ of a function _f_ if _x_
satisfies the equation _f_(_x_) = _x_.

For some functions _f_ we can locate a fixed point by beginning with an
initial guess and applying _f_ repeatedly, until successive values are very
close.

    
    x  
    (f x)  
    (f (f x))  
    ...

Using this idea, we'll make a procedure fixed-point that will keep applying a
function, until we we find two successive values whose difference is less than
some prescribed tolerance.


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

> (fixed-point cos 1.0)

0.7390822985224024

To demonstrate the power of abstracting functions with fixed-point, we will
develop a method to calculate square roots... in only 3 lines of scheme!

Computing the square root of some number _x_ requires finding a _y_ such that
_y_^_2_ = _x_. Putting this equation into the equivalent form _y_ = _x_/_y_, you
can see that we are looking for a fixed point of the function `(lambda (y) (/ x y))`. In code:


    (define (sqrt x)
        (fixed-point (lambda (y) (/ x y))
        1.0))

If you happen to have an interpreter handy, though, you'll find that this
doesn't work. To see why, look at the successive guesses of, say, `(sqrt 4)`:

1

4/1 = 4

4/4 = 1

4/1 = 4

...

It just keeps oscillatting! If you think about it, it'll do that for any
number we put in (expect 0 or 1).

So, instead of changing the guess so much, we'll move it by a little less. To
do that, we'll average the next guess with the currrent guess. That is, the
next guess after _y_ is (1/2)(_y_ + _x_/_y_) instead of _x_/_y. _

The process of making such a sequence of guesses is simply the process of
looking for a fixed point of _y_ = (1/2)(_y_ + _x_/_y_):


    (define (sqrt x)
        (fixed-point (lambda (y) (* 0.5 (+ y (/ x y))))
        1.0))

With this modification, the square-root procedure works.  This approach of
averaging successive approximations to a solution, a technique the SICP
authors call _average damping_, often aids the convergence of fixed-
point searches.

So, let's continue our abstraction frenzy and abstract the average damping
technique as well:

    
    (define (average-damp f)  
         (lambda (y) (* 0.5 (+ y (f y)))))

And now, a new sqrt:

    
    (define (sqrt x)  
      (fixed-point (average-damp (lambda (y) (/ x y)))  
                   1.0))

Amazingly clear, eh?

Notes:

_y_ = (1/2)(_y_ + _x_/_y_) is a simple transformation of the equation _y_ =
_x_/_y_; to derive it, add _y_ to both sides of the equation and divide by 2.

You may have noticed that we have effectively derived Newton's method for
calculating square roots. But... there are so many other ways! If you're
intersted, here's a cool link:

[http://en.wikipedia.org/wiki/Methods_of_computing_square_roots](http://en.wik
ipedia.org/wiki/Methods_of_computing_square_roots)

We will now conclude this lab with another higher-order function.

This one will allow us to write fixed-point AND largest-square (from lab 1).

How, you ask? Because they both fall under the general form of_ iterative
improvement_. That is, you start with a value and keep improving it until it
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

![](https://dl.dropboxusercontent.com/u/16963685/cs61as-edx/abstract_on.png)

