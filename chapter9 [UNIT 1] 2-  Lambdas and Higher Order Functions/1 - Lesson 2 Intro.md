## Introduction

> "I lambda Scheme"

This week we will learn a new special form, lambda, that can make procedures!
Make sure you learn it well. It will be used extensively for the rest of this
course.

## Prerequisites and What to Expect

Lesson 1, is required before working on this lesson.

We will go over lambdas and higher order functions.  We will learn a basic
concept in scheme -- the manipulation of functions using other function.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 1.3 - Abstractions with Higher-Order Procedures](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html)
  * [Lecture Notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=9)

From the previous lab, you should be familiar with the concept of a function.

It is an abstraction that specifies operations on some arguments.

For instance, suppose we specify the function cube:

    
    (define (cube x)  
       (* x x x))

This takes in as argument the number x and returns x^3.

But this abstraction, `cube`, we can treat it like a box and throw it around,
just like any other thing, say a number or a symbol. It has a value and we can
give it a name.

On the whole, defining `cube` as above is not too much different from defining
`var` like so:

`(define var 10)`

![Cubes](https://dl.dropboxusercontent.com/u/16963685/cs61as-
edx/cube_diagram.png)

So, naturally, we can create functions that take functions as **arguments** or
**return** functions.

We will explore this idea in this lab.

