
## Prerequisites and What to Expect

You're should understand all the materials covered so far, especially
sequences and list manipulation.

In this section, we are going to go over the streams and their a few of their
applications. Be prepared to be exposed to a fair amount of information and
synthesize it!

## Readings

This lesson is based off this [reading](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-24.html#%_sec_3.5).

## Streams

  
We've gained a good understanding of assignment as a tool in modeling, as well
as an appreciation of the complex problems that assignment raises. It is time
to ask whether we could have gone about things in a different way, so as to
avoid some of these problems. In this section, we explore an alternative
approach to modeling state, based on data structures called streams. As we
shall see, streams can mitigate some of the complexity of modeling state.

Let's step back and review where this complexity comes from. In an attempt to
model real-world phenomena, we made some apparently reasonable decisions: We
modeled real-world objects with local state by computational objects with
local variables. We identified time variation in the real world with time
variation in the computer. We implemented the time variation of the states of
the model objects in the computer with assignments to the local variables of
the model objects.

Is there another approach? Can we avoid identifying time in the computer with
time in the modeled world? Must we make the model change with time in order to
model phenomena in a changing world? Think about the issue in terms of
mathematical functions. We can describe the time-varying behavior of a
quantity x as a function of time x(t). If we concentrate on x instant by
instant, we think of it as a changing quantity. Yet if we concentrate on the
entire time history of values, we do not emphasize change-the function itself
does not change.

If time is measured in discrete steps, then we can model a time function as a
(possibly infinite) sequence. In this section, we will see how to model change
in terms of sequences that represent the time histories of the systems being
modeled. To accomplish this, we introduce new data structures called streams.
From an abstract point of view, a stream is simply a sequence. However, we
will find that the straightforward implementation of streams as lists (as in
section 2.2.1) doesn't fully reveal the power of stream processing. As an
alternative, we introduce the technique of delayed evaluation, which enables
us to represent very large (even infinite) sequences as streams.

Stream processing lets us model systems that have state without ever using
assignment or mutable data. This has important implications, both theoretical
and practical, because we can build models that avoid the drawbacks inherent
in introducing assignment. On the other hand, the stream framework raises
difficulties of its own, and the question of which modeling technique leads to
more modular and more easily maintained systems remains open.

In lesson 4, we have seen some of the applications and benefits of sequences.
We had experience with powerful abstractions for manipulating sequences as we
worked with sequences as lists: `map` `accumulate`, and `filter`.

But there are downsides to list representations. Manipulating these list
sequences require that our programs construct and copy data structures (which
could be HUGE) at every step of the process. Not very efficient :\.

Let's try to see this in action. The first program is the iterative style we
know and love

    
     
    (define (sum-primes a b)
      (define (iter count accum)
        (cond ((> count b) accum)
              ((prime? count) (iter (+ count 1) (+ count accum)))
              (else (iter (+ count 1) accum))))
      (iter a 0))
     

This second program makes use of `accumulate`,
`filter`, and `enumerate-interval`.

    
     
    (define (sum-primes a b)
      (accumulate +
                  0
                  (filter prime? (enumerate-interval a b))))
     

In carrying out the computation, the first program needs only to store the sum
being accumulated.

In contrast, the filter in the second program cannot do any testing until
enumerate-interval has constructed a complete list of the numbers in the
interval. The filter generates another list, which in turn is passed to
accumulate before being collapsed to form a sum.

Such large intermediate storage is not needed by the first program, which we
can think of as enumerating the interval incrementally, adding each prime to
the sum as it is generated.

Here's another example of list inefficiency:

```
(car (cdr (filter prime?
                  (enumerate-interval 10000 1000000))))
```

This code would take a long time to run because we generate a huge list of integers
and a huge list of primes, even though we only want the second prime number.

##  ... Let's use streams!

Streams are a clever idea that allows one to use sequence manipulations
without incurring the costs of manipulating sequences as lists. With streams
we can achieve the best of both worlds: We can formulate programs elegantly as
sequence manipulations, while attaining the efficiency of incremental
computation. The basic idea is to construct a stream only partially, and to
pass the partial construction to the program that consumes the stream. If the
consumer attempts to access a part of the stream that has not yet been
constructed, the stream will automatically construct just enough more of
itself to produce the required part, thus preserving the illusion that the
entire stream exists. In other words, although we will write programs as if we
were processing complete sequences, we design our stream implementation to
automatically and transparently interleave the construction of the stream with
its use.

