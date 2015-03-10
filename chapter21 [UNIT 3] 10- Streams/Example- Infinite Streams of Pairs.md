Suppose we want to produce an infinite stream of pairs of ints `(i, j); i <= j
` such that `i + j` is prime. If `int-pairs` is the stream of pairs of all
integers, our stream is:

`(stream-filter (lambda (pair)`

`(prime? (+ (car pair) (cadr pair))))`

`int-pairs)`

Now all we have to do is define `int-pairs`. How do we do that? Let's start by
supposing that we have two streams, S and T, where S = T = `ints`. Now let's
imagine the array (or matrix, if you want to think of it that way) of pairs of
S and T:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-45.gif)

The stream of pairs of integers is everything above the diagonal; that is,

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-46.gif)

Call the general stream of pairs (pairs S T), and consider it to be composed
of three parts: the pair (S0,T0), the rest of the pairs in the first row, and
the remaining pairs.

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-47.gif)

The third piece in this decomposition (pairs that are not in the first row) is
(recursively) the pairs formed from `(stream-cdr S)` and `(stream-cdr T)`.
Also note that the second piece (the rest of the first row) is:

`(stream-map (lambda (x) (list (stream-car s) x))`

`(stream-cdr t))`

Then our stream of pairs is:

`(define (pairs s t)`

` (cons-stream `

`(list (stream-car s) (stream-car t))`

`(_combine-in-some-way_`

`(stream-map (lambda (x) (list (stream-car s) x))`

`(stream-cdr t))`

`(pairs (stream-cdr s) (stream-cdr t)))))`

Now we just need to put the streams together. We know that appending doesn't
work, so we will use interleave instead! Our stream of pairs becomes:

`(define (pairs s t)`

` (cons-stream `

`(list (stream-car s) (stream-car t))`

`(interleave`

`(stream-map (lambda (x) (list (stream-car s) x))`

`(stream-cdr t))`

`(pairs (stream-cdr s) (stream-cdr t)))))`

