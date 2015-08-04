## Implementing Streams

On the surface, streams are just lists with different names for the procedures
that manipulate them. They have a constructor, ` cons-stream`, and two
selectors, ` stream-car` and ` stream-cdr`, such that:

 * `(stream-car (cons-stream x y))` is equivalent to `x`.
 * `(stream-cdr (cons-stream x y))` is equivalent to `y`.

As a data abstraction, streams are the same as lists. The difference is the
time at which the elements are evaluated. With ordinary lists, both the `car`
and the `cdr` are evaluated at construction time. With streams, the `cdr` isn't
evaluated until selection time.

Our implementation of streams will be based on a special form called `delay`.
Evaluating `(delay [exp])` does not evaluate the expression `[exp]`, but rather
returns a so-called delayed object, which we can think of as a "promise" to
evaluate `[exp]` at some future time. As a companion to `delay`, there is a
procedure called `force` that takes a delayed object as argument and performs
the evaluation&mdash;in effect, forcing the `delay` to fulfill its promise. We will
see below how `delay` and `force` can be implemented, but first let us use
these to implement streams.

### Constructors and Selectors

`cons-stream` is a special form such that

```
(cons-stream a b)
```

is equivalent to

```
(cons a (delay b))
```

Note that `cons-stream` *must* be a special form.
If it weren't, calling `(cons-stream a b)` would evaluate `b`, meaning `b` wouldn't be delayed.

Since our streams are implemented as pairs, our `stream-car` and `stream-cdr` procedures look like this:

```
(define (stream-car stream) (car stream))

(define (stream-cdr stream) (force (cdr stream)))
```

### Empty Streams

The stream analog of the empty list `'()` is `the-empty-stream`.
It can be identified with the predicate `stream-null?`.

We can implement `the-empty-stream` and `stream-null?` like this:

```
(define the-empty-stream '())
(define stream-null? null?)
```
### Example: Contstructing a Stream

We can now create streams!
Here's a stream containing the first three whole numbers:

```
(define first-three
  (cons-stream 0 (cons-stream 1 (cons-stream 2 the-empty-stream))))
```

This stream is analogous to the list `'(0 1 2)`, which is constructed like this:

```
(cons 0 (cons 1 (cons 2 '())))
```

To print a stream, we can use the predefined procedure `ss` (or `show-stream`):

```
-> (ss first-three)
'(0 1 2)
```

## Stream Analogs of List Procedures

So far, we've learned that streams can represent sequences, just like lists.
We found `list-ref`,
`map`, `for-each`, and `enumerate-interval` helpful for working with lists,
so let's create versions of these procedures for working with streams!

### `stream-ref`
    
     
    (define (stream-ref s n)
      (if (= n 0)
          (stream-car s)
          (stream-ref (stream-cdr s) (- n 1))))
     

If `first-three` is defined as above, then we have the following behavior:

```
-> (stream-ref first-three 0)
0
-> (stream-ref first-three 2)
2
```

Note that `n` starts counting from 0.

### `stream-map`
     
    (define (stream-map proc s)
      (if (stream-null? s)
          the-empty-stream
          (cons-stream (proc (stream-car s))
                       (stream-map proc (stream-cdr s)))))
     

If `first-three` is defined as above, then we have the following behavior:

```
-> (ss (stream-map add1 first-three))
'(1 2 3)
-> (ss (stream-map square first-three))
'(0 1 4)
```

Remember that `ss` stands for `show-stream` and is used for nicely printing streams!

### `stream-for-each`
     
    (define (stream-for-each proc s)
      (if (stream-null? s)
          'done
          (begin (proc (stream-car s))
                 (stream-for-each proc (stream-cdr s)))))

Here's an example of `stream-for-each` in action:

```
-> (stream-for-each displayln first-three)
0
1
2
'done
```
    
### `stream-enumerate-interval`

```     
(define (stream-enumerate-interval low high)
  (if (> low high)
      the-empty-stream
      (cons-stream low
                   (stream-enumerate-interval (+ low 1) high))))
``` 

So `(stream-enumerate-interval 0 2)` is the same as `first-three` above:

```
-> (ss (stream-enumerate-interval 0 2))
'(0 1 2)
```

## Example: Computation Using Streams

In the previous section, we saw a prime <!-- hahahaha --> example of list inefficiency:

```
(car (cdr (filter prime?
                  (enumerate-interval 10000 1000000))))
```

Let's try rewriting it using streams:

```     
(stream-car
  (stream-cdr
    (stream-filter prime?
                   (stream-enumerate-interval 10000 1000000))))
```  

So we begin by calling `stream-enumerate-interval` with the arguments 10,000
and 1,000,000. This creates a stream of the numbers from 10,000 to 1,000,000,
which is equivalent to

```
(cons 10000
      (delay (stream-enumerate-interval 10001 1000000)))
```

So our stream is represented as a pair whose `car` is 10,000 and
whose `cdr` is a promise to enumerate more of the interval if it becomes
necessary. Pretty efficient, right?

Now we filter it using `stream-filter`, which we can implement like this:    
    
    (define (stream-filter pred stream)
      (cond ((stream-null? stream) the-empty-stream)
            ((pred (stream-car stream))
             (cons-stream (stream-car stream)
                          (stream-filter pred
                                         (stream-cdr stream))))
            (else (stream-filter pred (stream-cdr stream)))))
    
`stream-filter` tests if the `stream-car` of the stream (which is 10,000) is prime.
Since 10,000 is not prime, `stream-filter` examines the
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
    
which is equivalent to
    
```
(cons 10007
      (delay
        (stream-filter
          prime?
          (cons 10008
                (delay
                  (stream-enumerate-interval 10009
                                             1000000))))))
```                                             
    
This result is now passed to `stream-cdr` in our original expression. This
forces the delayed `stream-filter`, which in turn keeps forcing the delayed
`stream-enumerate-interval` until it finds the next prime, which is 10,009.
Finally, the result passed to `stream-car` in our original expression is

```
(cons 10009
      (delay
        (stream-filter
          prime?
          (cons 10010
                (delay
                  (stream-enumerate-interval 10011
                                             1000000))))))
```

`stream-car` returns 10,009, and the computation is complete. Only as many
integers were tested for primality as were necessary to find the second prime,
and the interval was enumerated only as far as was necessary to feed the prime
filter.

<div class="mc">
<p>
<strong>Test Your Understanding</strong><p>
What is the fifth number between 150 and 750 that is divisible by 44?
Use streams to calculate your result.
(You may find <code>stream-ref</code> helpful.)

<ans text="308" explanation="Too low. Check your code."></ans>
<ans text="352" explanation="Correct!" correct></ans>
<ans text="396" explanation="Too high. Remember that <code>stream-ref</code> starts numbering at 0."></ans>
<ans text="10,208" explanation="Your answer should be between 150 and 750."></ans> <!-- 5th number after 10,000 that is divisible by 44. -->
</div>

## Implementing `delay` and `force`

### `delay`

Although `delay` and `force` may seem like mysterious operations, their
implementation is really quite straightforward. `delay` must package an
expression so that it can be evaluated later on demand, and we can accomplish
this simply by treating the expression as the body of a procedure. `delay` can
be a special form such that

    
     (delay [exp])

is syntactic sugar for

    
     (lambda () [exp])

Again, note the importance of `delay` being a special form.
If it weren't, calling `(delay b)` would evaluate `b` immediately.

### `force`

`force` simply calls the procedure (of no arguments) produced by `delay`, so
we can implement `force` like this:

     (define (force delayed-object)
      (delayed-object))  

### Memoization

This implementation suffices for `delay` and `force` to work as advertised,
but there is an important optimization that we can include. In many
applications, we end up forcing the same delayed object many times. This can
lead to serious inefficiency in recursive programs involving streams.

The solution is to build delayed objects so that the first time they are forced,
they store the value that is computed. Subsequent forcings will simply return
the stored value without repeating the computation.
This technique is called **memoization**.

One way to accomplish memoization is to use the following procedure, which takes as argument a
procedure (of no arguments) and returns a memoized version of the procedure.
The first time the memoized procedure is run, it saves the computed result. On
subsequent evaluations, it simply returns the result.

```    
(define (memo-proc proc)
  (let ((already-run? #f)
        (result #f))
    (lambda ()
      (if (not already-run?)
          (begin (set! result (proc))
                 (set! already-run? #t)
                 result)
          result))))
``` 

`delay` is then defined so that `(delay [exp])` is equivalent to
    
    (memo-proc (lambda () [exp]))
    
`force` remains unchanged.

## Takeaways

In this section, we discussed

  1. what a stream is,
  2. how to use streams in computations, and
  3. how to implement `delay` and `force`.
