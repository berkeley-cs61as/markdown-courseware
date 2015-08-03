Suppose we want to produce an infinite stream containing pairs of integers 
[mathjaxinline] (i, j) [/mathjaxinline] where [mathjaxinline]i \leq j[/mathjaxinline]
and [mathjaxinline]i + j[/mathjaxinline] is prime. If `int-pairs` is the stream of pairs of all
integers, our stream is:

```
(stream-filter (lambda (pair)
                 (prime? (+ (car pair) (cadr pair))))
               int-pairs)
```               

Now all we have to do is define `int-pairs`. How do we do that? Let's start by
supposing that we have two streams, [mathjaxinline]S[/mathjaxinline] and [mathjaxinline]T[/mathjaxinline],
which are both equivalent to `integers`. Now let's
imagine the array (or matrix, if you want to think of it that way) of pairs of
[mathjaxinline]S[/mathjaxinline] and [mathjaxinline]T[/mathjaxinline]:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-45.gif)

The stream of pairs of integers is everything above the diagonal:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-46.gif)

Let's call the general stream of pairs `(pairs s t)`, and consider it to be composed
of three parts: the pair [mathjaxinline] (S\_0, T\_0) [/mathjaxinline], the rest of the pairs in the first row, and
the remaining pairs.

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-47.gif)

The third piece in this decomposition (pairs that are not in the first row) is
(recursively) the pairs formed from `(stream-cdr s)` and `(stream-cdr t)`.
Also note that the second piece (the rest of the first row) is:

```
(stream-map (lambda (x) (list (stream-car s) x))
            (stream-cdr t))1
```

Then our stream of pairs is:

```
(define (pairs s t)
  (cons-stream (list (stream-car s) (stream-car t))
               (combine (stream-map (lambda (x) (list (stream-car s) x))
                                                  (stream-cdr t))
                                      (pairs (stream-cdr s) (stream-cdr t)))))
```

Now we just need to put the streams together using some sort of `combine` function.
We know that appending doesn't work&mdash;let's use `interleave` instead! Our stream of pairs becomes:

```
(define (pairs s t)
  (cons-stream (list (stream-car s) (stream-car t))
               (interleave (stream-map (lambda (x) (list (stream-car s) x))
                                       (stream-cdr t))
               (pairs (stream-cdr s) (stream-cdr t)))))
```
