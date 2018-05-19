## Introduction

> "I lambda Racket"

This week we will learn a new special form, `lambda`, that can make procedures!
Make sure you learn it well, for it will be used extensively for the rest of this
course.

## Prerequisites and What to Expect

**Prerequisites:** Lesson 1 is required before working on this lesson. You should be familiar with concepts such as functions, procedures, and calling a procedure.

**What to Expect:** In this lesson, we will:

  * explain lambdas and higher order functions
  * learn a basic concept in Racket, or any other function-oriented programming language -- the manipulation of functions using other functions.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 1.3 - Abstractions with Higher-Order Procedures](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-12.html)
  * [Lecture Notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=9)

## Sneak Peek

We learned how to create, modify, and call procedures in Lesson 1. Every procedure has a name, its arguments, and a body where we tell the function what to do with its arguments.

For instance, here is the procedure `cube`, which takes in one argument `x` and returns `x` cubed:

    
    (define (cube x)  
       (* x x x))

We `define` a procedure whose name is `cube`, argument is `x`, and body is `(* x x x)`. You should be able to tell by now that the body multiplies three `x`'s together and returns `x` cubed.

`cube` is a procedure, or abstraction, that we can treat like a box and throw around, just like any other number or symbol. It has a _value_ and we can
give it a _name_.

Now that we think about it, defining `cube` the way we did above is not too far off from defining `var` like this:

	(define var 10)

![Cubes](https://dl.dropboxusercontent.com/u/16963685/cs61as-
edx/cube_diagram.png)

In the box `var`, we put `10`. In the box `(cube x)`, we put `(* x x x)`. In one box, we put a number, and in the other, we put an expression. Pretty similar, right? What if, instead putting a primitive value or expression into the box, we put a **function** inside? Inconceivable! 

It'll probably look something like this:


	(define f [some function])

`[some function]` is where we would put a lambda. Keep reading to find out more!

