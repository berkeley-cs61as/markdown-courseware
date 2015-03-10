## Introduction

This lesson will teach you the basics of concurrency and client/server.

## Prerequisites

You should understand assignment and mutable data.

## Readings

Most of this lesson is based off of [these
notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=64).

To learn more about concurrency, you can also read [SICP Section
3.4](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-23.html#%_sec_3.4).

## Concurrency Intro

We've seen the power of computational objects with local state as tools for
modeling. Yet, as you saw earlier in Unit 3, this power extracts a price: the
loss of referential transparency, giving rise to a thicket of questions about
sameness and change, and the need to abandon the substitution model of
evaluation in favor of the more intricate environment model.

The central issue lurking beneath the complexity of state, sameness, and
change is that by introducing assignment we are forced to admit time into our
computational models. Before we introduced assignment, all our programs were
timeless, in the sense that any expression that has a value always has the
same value. In contrast, recall the example of modeling withdrawals from a
bank account and returning the resulting balance, introduced at the beginning
of section 3.1.1 in SICP:

`(withdraw 25)`

` 75`

` (withdraw 25)`

` 50 `

Here successive evaluations of the same expression yield different values.
This behavior arises from the fact that the execution of assignment statements
(in this case, assignments to the variable balance) delineates moments in time
when values change. The result of evaluating an expression depends not only on
the expression itself, but also on whether the evaluation occurs before or
after these moments. Building models in terms of computational objects with
local state forces us to confront time as an essential concept in programming.

We can go further in structuring computational models to match our perception
of the physical world. Objects in the world do not change one at a time in
sequence. Rather we perceive them as acting concurrently - all at once. So it
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

## Client/Server Intro

Before networks, most programs ran on a single computer. Today it's common for
programs to involve cooperation between computers. The usual reason is that
you want to run a program on your computer that uses data located elsewhere. A
common example is using a browser on your computer to read a web page stored
somewhere else.

To make this cooperation possible, two programs are actually required: the
client program on your personal computer and the server program on the remote
computer. Sometimes the client and the server are written by a single group,
but often someone publishes a standard document that allows any client to work
with any server that follows the same standard. For example, you can use
Mozilla, Netscape, or Internet Explorer to read most web pages, because they
all follow standards set by the World Wide Web Consortium.

For this course we provide a sample client/server system, implementing a
simple Instant Message protocol. The ﬁles are available in

    
        ~cs61as/lib/im-client.scm
        ~cs61as/lib/im-server.scm
    

