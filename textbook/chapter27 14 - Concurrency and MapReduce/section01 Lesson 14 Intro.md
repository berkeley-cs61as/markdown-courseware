## Introduction

In this lesson, we'll discuss the basics of concurrency.

## Prerequisites

You should understand assignment and mutable data.

## Readings

Most of this lesson is based off of [these
notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=64)
and [SICP 3.4](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-23.html#%_sec_3.4).

## Introduction to Concurrency

In Unit 3, we saw the power of computational objects with *local state* as tools for modeling. But this power came at a price.

By introducing assignment we are forced to admit *time* into our
computational models. Before we introduced assignment, all our programs were
timeless, in the sense that any expression that has a value always has the
same value. In contrast, recall the example of modeling withdrawals from a
bank account and returning the resulting balance, introduced at the beginning
of section 3.1.1 in SICP:

```
> (withdraw 25)
75
> (withdraw 25)
50 
```

Here successive evaluations of the same expression yield different values.
This behavior arises from the fact that the execution of assignment statements
(in this case, assignments to the variable `balance`) delineates moments in time
when values change. The result of evaluating an expression depends not only on
the expression itself, but also on whether the evaluation occurs before or
after these moments. Building models in terms of computational objects with
local state forces us to confront time as an essential concept in programming.

We can go further in structuring computational models to match our perception
of the physical world. Objects in the world do not change one at a time in
sequence. Rather we perceive them as acting concurrently&mdash;all at once. So it
is often natural to model systems as collections of computational processes
that execute concurrently. Just as we can make our programs modular by
organizing models in terms of objects with separate local state, it is often
appropriate to divide computational models into parts that evolve separately
and concurrently.

In addition to making programs more modular, concurrent computation can
provide a speed advantage over sequential computation. Sequential computers
execute only one operation at a time, so the amount of time it takes to
perform a task is proportional to the total number of operations performed.
However, if it is possible to decompose a problem into pieces that are
relatively independent and need to communicate only rarely, it may be possible
to allocate pieces to separate computing processors, producing a speed
advantage proportional to the number of processors available.

Unfortunately, the complexities introduced by assignment become even more
problematic in the presence of concurrency. The fact of concurrent execution,
either because the world operates in parallel or because our computers do,
entails additional complexity in our understanding of time.
