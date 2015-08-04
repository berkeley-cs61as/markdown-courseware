Back in Unit 1, we wrote a procedure for approximating the square root
of a given number&mdash;let's call it `x`. The idea was to generate a sequence of better
and better guesses for the square root of `x` by applying over and over again
the procedure that improves guesses:

```
(define (sqrt-improve guess x)
  (average guess (/ x guess)))
(define (average x y)
  (/ (+ x y) 2))
```

We can do the same thing using streams by creating an infinite stream of guesses, starting with an initial guess of
1:

```
(define (sqrt-stream x)
  (define guesses 
    (cons-stream 1.0 (stream-map (lambda (guess) 
                                   (sqrt-improve guess x)) 
                                 guesses)))
  guesses)
```

For example:

```
-> (ss (sqrt-stream 2015))
'(1.0
  1008.0
  504.999503968254
  254.494803448699
  131.20622519086908
  73.28186410691475
  50.38921769381862
  45.18896569765265
  44.88974861660058
  44.88875138600392
  ...)
```

Successive elements of the stream get closer and closer to the square
root of 2015, which is [about 44.88875137492688156359](http://www.wolframalpha.com/input/?i=sqrt(2015)).

<!-- They get the point

Similarly, we used the following formula to approximate pi:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-41.gif)

Now, let's calculate pi with an infinite stream:

```
(define (pi-summands n)
  (cons-stream (/ 1.0 n)
               (stream-map - (pi-summands (+ n 2)))))

(define pi-stream
  (scale-stream (partial-sums (pi-summands 1)) 4))
```

The first few elements look like this:

```
4.
2.666666666666667
3.466666666666667
2.8952380952380956
3.3396825396825403
2.9760461760461765
3.2837384837384844
3.017071817071818
```

As you can tell, the numbers are converging on pi&mdash;after looking at the first
eight elements, we know pi is somewhere between 3.28 and 3.02.

-->