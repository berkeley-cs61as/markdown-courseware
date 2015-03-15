## What are Mutexes?

A mutex is an object that supports two operations -- the mutex can be
acquired, and the mutex can be released. Once a mutex has been acquired, no
other acquire operations on that mutex may proceed until the mutex is
released.

The mutex is a mutable object (here we'll use a one-element list, which we'll
refer to as a cell) that can hold the value true or false. When the value is
false, the mutex is available to be acquired. When the value is true, the
mutex is unavailable, and any process that attempts to acquire the mutex must
wait.

Our mutex constructor `make-mutex` begins by initializing the cell contents to
false. To acquire the mutex, we test the cell. If the mutex is available, we
set the cell contents to true and proceed. Otherwise, we wait in a loop,
attempting to acquire over and over again, until we find that the mutex is
available. To release the mutex, we set the cell contents to false.

    
    
    (define (make-mutex)
      (let ((cell (list false)))            
        (define (the-mutex m)
          (cond ((eq? m 'acquire)
                 (if (test-and-set! cell)
                     (the-mutex 'acquire))) ; retry
                ((eq? m 'release) (clear! cell))))
        the-mutex))
    (define (clear! cell)
      (set-car! cell false))
    

`Test-and-set!` tests the cell and returns the result of the test. In
addition, if the test was false, `test-and-set!` sets the cell contents to
true before returning false. This procedure is a Scheme primitive. Its
implementation requires hardware support.

## Using Mutexes

The book uses an intermediate level of abstraction between the serializer and
the atomic hardware capability, called a mutex. What’s the diﬀerence between a
mutex and a serializer? The serializer provides, as an abstraction, a
protected operation, without requiring the programmer to think about the
mechanism by which it’s protected. The mutex exposes the sequence of events.
Just as the earlier incorrect implementation said

    
    
    (set! in-use #t)
    (apply proc args)
    (set! in-use #f)
    

the correct version uses a similar sequence

    
    
    (mutex ’acquire)
    (apply proc args)
    (mutex ’release)
    

By the way, all of the versions in these sections have another bug; we’ve
simpliﬁed the discussion by ignoring the problem of return values. We want the
value returned by protected-proc to be the same as the value returned by the
original proc, even though the call to proc isn’t the last step. Therefore the
correct implementation is

    
    
    (mutex ’acquire)
    (let ((result (apply proc args)))
        (mutex ’release)
        result)
    

as in the book’s implementation on page 311.

## Implementing Serializers with Mutexes

Now that we know about mutexes and how to use them, it is relatively
straightforward to implement serializers. Our implementation is below. Make
sure you understand how and why it works!

    
    
    (define (make-serializer)
      (let ((mutex (make-mutex)))
        (lambda (p)
          (define (serialized-p . args)
            (mutex 'acquire)
            (let ((val (apply p args)))
              (mutex 'release)
              val))
          serialized-p)))
    

