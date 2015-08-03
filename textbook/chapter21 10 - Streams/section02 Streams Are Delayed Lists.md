## Stream Constructor and Selectors

On the surface, streams are just lists with different names for the procedures
that manipulate them. They have a constructor ` cons-stream` , and two
selectors, ` stream-car` and ` stream-cdr`, which satisfies these constraints:

 * `(stream-car (cons-stream x y))` returns `x`
 * `(stream-cdr (cons-stream x y))` returns `y`

In order to construct the stream as we use it, we will arrange for the cdr of
a stream to be evaluated when it is accessed by the `stream-cdr` procedure
rather than when the stream is constructed.

As a data abstraction, streams are the same as lists. The difference is the
time at which the elements are evaluated. With ordinary lists, both the `car`
and the `cdr` are evaluated at construction time. With streams, the cdr isn't
evaluated until selection time.

Our implementation of streams will be based on a special form called `delay`.
Evaluating `(delay [exp])` does not evaluate the expression [exp], but rather
returns a so-called delayed object, which we can think of as a "promise" to
evaluate [exp] at some future time. As a companion to `delay`, there is a
procedure called `force` that takes a delayed object as argument and performs
the evaluation -- in effect, forcing the delay to fulfill its promise. We will
see below how `delay` and `force` can be implemented, but first let us use
these to construct streams.

`cons-stream` is a special form such that `(cons-stream [a] [b])` is equivalent to `(cons [a] (delay [b]))`.

This means that we will construct using pairs of `cars` and delayed `cdrs`.
These will be our `stream-car` and `stream-cdr` procedures:

```
(define (stream-car stream) (car stream))

(define (stream-cdr stream) (force (cdr stream)))
```
      
Note that `cons-stream` is a special form. If it weren't, calling `(cons-stream a b)` would evaluate `b`, meaning `b` wouldn't be delayed.

## `the-empty-stream`

There is a distinguishable object, `the-empty-stream`, which cannot be the
result of any `cons-stream` operation, and which can be identified with the
predicate `stream-null?`.

## Stream Analogs of List Procedures

We can make and use streams, in just the same
way as we can make and use lists, to represent aggregate data arranged in a
sequence. In particular, we can build stream analogs of `list-ref`, `map`,
`for-each`, and so on.

### `stream-ref`
    
     
    (define (stream-ref s n)
      (if (= n 0)
          (stream-car s)
          (stream-ref (stream-cdr s) (- n 1))))
     

If we define x as

```
(define x (cons-stream 0 (cons-stream 1 (cons-stream 2 the-empty-stream))))
```

then `(stream-ref x 0)` returns 0 and  `(stream-ref x 2)` returns 2.
(Note that n starts counting from 0)

### `stream-map`
     
    (define (stream-map proc s)
      (if (stream-null? s)
          the-empty-stream
          (cons-stream (proc (stream-car s))
                       (stream-map proc (stream-cdr s)))))
     

If x is the same as above, then `(stream-map square x)` returns a stream with
`(0 1 4)`

### `stream-for-each`
     
    (define (stream-for-each proc s)
      (if (stream-null? s)
          'done
          (begin (proc (stream-car s))
                 (stream-for-each proc (stream-cdr s)))))


`stream-for-each` is useful for viewing streams. The
following may be helpful for checking what's going on:

    
     
    (define (display-stream s)
      (stream-for-each display-line s))
    
    (define (display-line x)
      (newline)
      (display x))
     
## Computation Using Streams     

Let's take another look at the second prime computation we saw earlier,
reformulated in terms of streams:

     
    (stream-car
     (stream-cdr
      (stream-filter prime?
                     (stream-enumerate-interval 10000 1000000))))
     

So we begin by calling `stream-enumerate-interval` with the arguments 10,000
and 1,000,000. This creates a stream of the numbers from 10,000 to 1,000,000.

    
     
    (define (stream-enumerate-interval low high)
      (if (> low high)
          the-empty-stream
          (cons-stream
           low
           (stream-enumerate-interval (+ low 1) high))))
     

The result returned is ` (cons 10000 (delay (stream-enumerate-interval 10001
1000000)))` This is a stream represented as a pair whose `car` is 10,000 and
whose `cdr` is a promise to enumerate more of the interval if it becomes
necessary. Now we filter it using ` stream-filter`

    
    
    (define (stream-filter pred stream)
      (cond ((stream-null? stream) the-empty-stream)
            ((pred (stream-car stream))
             (cons-stream (stream-car stream)
                          (stream-filter pred
                                         (stream-cdr stream))))
            (else (stream-filter pred (stream-cdr stream)))))
    

`stream-filter` tests the `stream-car` of the stream (the car of the pair,
which is 10,000). Since this is not prime, `stream-filter` examines the
`stream-cdr` of its input stream. The call to `stream-cdr` forces evaluation
of the delayed `stream-enumerate-interval`, which now returns

    
    
    (cons 10001
          (delay (stream-enumerate-interval 10002 1000000)))
    

`stream-filter` now looks at the `stream-car` of this stream, 10,001, sees
that this is not prime either, forces another `stream-cdr`, and so on, until
`stream-enumerate-interval` yields the prime 10,007, whereupon `stream-
filter`, according to its definition, returns

    
    
    (cons-stream (stream-car stream)
                 (stream-filter pred (stream-cdr stream)))
    

which is

    
    
    (cons 10007
          (delay
            (stream-filter
             prime?
             (cons 10008
                   (delay
                     (stream-enumerate-interval 10009
                                                1000000))))))
    

This result is now passed to `stream-cdr` in our original expression. This
forces the delayed `stream-filter`, which in turn keeps forcing the delayed
`stream-enumerate-interval` until it finds the next prime, which is 10,009.
Finally, the result passed to `stream-car` in our original expression is

    
    
    (cons 10009
          (delay
            (stream-filter
             prime?
             (cons 10010
                   (delay
                     (stream-enumerate-interval 10011
                                                1000000))))))
    

`Stream-car` returns 10,009, and the computation is complete. Only as many
integers were tested for primality as were necessary to find the second prime,
and the interval was enumerated only as far as was necessary to feed the prime
filter.

## Implementing `delay` and `force`

Although `delay` and `force` may seem like mysterious operations, their
implementation is really quite straightforward. `delay` must package an
expression so that it can be evaluated later on demand, and we can accomplish
this simply by treating the expression as the body of a procedure. `delay` can
be a special form such that

    
     (delay [exp])

is syntactic sugar for

    
     (lambda () [exp])

`force` simply calls the procedure (of no arguments) produced by `delay`, so
we can implement `force` as a procedure:

    
     (define (force delayed-object)
      (delayed-object))  
      
Again, note the importance of `delay` being a special form. If it is not, then when we call `(delay b)`, `b` will be evaluated before we evaluate the body.

This implementation suffices for `delay` and `force` to work as advertised,
but there is an important optimization that we can include. In many
applications, we end up forcing the same delayed object many times. This can
lead to serious inefficiency in recursive programs involving streams. The
solution is to build delayed objects so that the first time they are forced,
they store the value that is computed. Subsequent forcings will simply return
the stored value without repeating the computation. In other words, we
implement `delay` as a special-purpose memoized procedure. One way to
accomplish this is to use the following procedure, which takes as argument a
procedure (of no arguments) and returns a memoized version of the procedure.
The first time the memoized procedure is run, it saves the computed result. On
subsequent evaluations, it simply returns the result.

    
    
    (define (memo-proc proc)
      (let ((already-run? false) (result false))
        (lambda ()
          (if (not already-run?)
              (begin (set! result (proc))
                     (set! already-run? true)
                     result)
              result))))
    

`Delay` is then defined so that (delay [exp]) is equivalent to

    
    
    (memo-proc (lambda () [exp]))
    

and `force` is unchanged

## Takeaways

In this section, you learned:

  1. What a stream is
  2. Some useful applications of streams
  3. How to implement `delay` and `force`

## What's Next?

Let's go to the next subsection and learn about infinite lists!

