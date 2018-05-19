## Introduction

This week’s big idea is logic programming or declarative programming.

It’s the biggest step we’ve taken away from expressing a computation in
hardware terms. When we discovered streams, we saw how to express an algorithm
in a way that’s independent of the order of evaluation. Now we are going to
describe a computation in a way that has no (visible) algorithm at all!

We are using a logic programming language that A&S implemented in Scheme.
Because of that, the notation is Scheme-like, i.e., full of lists. Standard
logic languages like Prolog have different notations, but the idea is the
same.

## Prerequisites

This lesson follows a very different paradigm than anything you've seen so
far. As such, there are no prerequisites!

## Readings

Most of this lesson is taken from [these notes](http://www-inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=102) and [SICP Sections 4.4.1-4.4.3](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-29.html#%_sec_4.4).

## Logic Programming

  
Logic programming excels in providing interfaces to data bases for information
retrieval. The query language we shall use in this chapter is designed to be
used in this way.

All we do is assert facts:

    
    > (load "~cs61as/lib/query.scm")
    > (query)
    
    ;;; Query input:
    (assert! (Brian likes potstickers))
    

and ask questions about the facts:

    
    ;;; Query input:
    (?who likes potstickers)
    
    ;;; Query results:
    (BRIAN LIKES POTSTICKERS)
    

Although the assertions and the queries take the form of lists, and so they
look a little like Scheme programs, they're not! There is no application of
function to argument here; an assertion is just data.

This is true even though, for various reasons, it's traditional to put the
verb (the relation) ﬁrst:

    
    (assert! (likes Brian potstickers))
    

We'll use that convention hereafter, but that makes it even easier to fall
into the trap of thinking there is a function called `likes`. Read on to learn
how we program in this peculiar language!

