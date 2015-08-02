## What Are Serializers

We introduce an abstraction called a serializer. This is a procedure that
takes as its argument another procedure (call it `proc`). The serializer
returns a new procedure (call it `protected-proc`). When invoked, `protected-proc`
invokes `proc`, but only if the same serializer is not already in use by
another protected procedure. `proc` can have any number of arguments, and
`protected-proc` will take the same arguments and return the same value.

There can be many diﬀerent serializers, all in operation at once, but each one
can't be doing two things at once. So if we say

    
    (define x-protector (make-serializer))
    (define y-protector (make-serializer))
    (parallel-execute (x-protector (lambda () (set! x (+ x 1))))
                      (y-protector (lambda () (set! y (+ y 1)))))
    

then both tasks can run at the same time; it doesn't matter how their machine
instructions are interleaved.

But if we say

    
    (parallel-execute (x-protector (lambda () (set! x (+ x 1))))
                      (x-protector (lambda () (set! x (+ x 1)))))
    

then, since we're using the same serializer in both tasks, the serializer will
ensure that they don't overlap in time.

We've introduced a new primitive procedure, `parallel-execute`. It takes any
number of arguments, each of which is a procedure of no arguments, and invokes
them, in parallel rather than in sequence. (This isn't a standard part of
Scheme, but an extension for this section of the textbook.)

You may be wondering about the need for all those (lambda ()...) notations.
Since a serializer isn't a special form, it can't take an expression as
argument. Instead we must give it a procedure that it can invoke.

Let's look at a sample of how this code works:

    
    (define x-protector (make-serializer))
    (define protected-increment-x (x-protector (lambda () (set! x (+ x 1)))))
    > x
    100
    > (protected-increment-x)
    > x
    101
    

## Implementing Serializers

A serializer is a high-level abstraction. How do we make it work? Here is an
**incorrect attempt** to implement serializers:

    
    (define (make-serializer)
      (let ((in-use? #f))
        (lambda (proc)
          (define (protected-proc . args)
            (if in-use?
                (begin
                 (wait-a-while) ; Never mind how to do that.
                 (apply protected-proc args)) ; Try again.
                (begin
                 (set! in-use? #t) ; Don't let anyone else in.
                 (apply proc args) ; Call the original procedure.
                 (set! in-use? #f)))) ; Finished, let others in again.
          protected-proc)))
    

This is a little complicated, so concentrate on the important parts. In
particular, never mind about the _scheduling_ aspect of parallelism--how we
can ask this process to wait a while before trying again if the serializer is
already in use. And never mind the stuﬀ about `apply`, which is needed only so
that we can serialize procedures with any number of arguments.

The part to focus on is this:

    
    (if in-use?
        ....... ; wait and try again
        (begin (set! in-use #t)   ; Don't let anyone else in. 
               (apply proc args)  ; Call the original procedure.
               (set! in-use #f))) ; Finished, let others in again. 
    

The intent of this code is that it ﬁrst checks to see if the serializer is
already in use. If not, we claim the serializer by setting `in-use` true, do
our job, and then release the serializer.

The problem is that this sequence of events is subject to the same parallelism
problems as the procedure we're trying to protect! What if we check the value
of `in-use`, discover that it's false, and right at that moment another
process sneaks in and grabs the serializer? In order to make this work we'd
have to have another serializer protecting this one, and a third serializer
protecting the second one, and so on.

_There is no easy way to avoid this problem by clever programming tricks
within the competing processes._ We need help at the level of the underlying
machinery that provides the parallelism: the hardware and/or the operating
system. That underlying level must provide a _guaranteed atomic_ operation
with which we can test the old value of `in-use` and change it to a new value
with no possibility of another process intervening. (It turns out that there
is a very tricky software algorithm to generate guaranteed atomic test-and-
set, but in practice, there is almost always hardware support for parallelism.
Look up "Peterson's algorithm" in Wikipedia if you want to see the software
solution.)

The textbook assumes the existence of a procedure called `test-and-set!` with
this guarantee of atomicity. Although there is a pseudo-implementation on page
312, that procedure won't really work, for the same reason that my pseudo-
implementation of `make-serializer` won't work. What you have to imagine is
that `test-and-set!` is a single instruction in the computer's hardware,
comparable to the Load Word instructions and so on that we started with. (This
is a realistic assumption; modern computers do provide some such hardware
mechanism, precisely for the reasons we're discussing now.)

To understand how to properly implement serializers, you first need to learn
about and understand Mutexes (in two sections).

