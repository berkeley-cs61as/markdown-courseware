## Functional Programming

> "Did you mean: [recursion](https://www.google.com/search?q=recursion)"

In this lab we will dive into functional programming and recursion. In short,
recursion is idea of having a procedure solve some big problem by making it a
little bit smaller somehow and then calling itself. When it calls itself, it
makes the problem smaller yet again. This continues until the problem is small
enough to be trivially solved. Recursion can be hard to get used to if you
have never used it before. Some things to remember when programming
recursively are:

  1. Remember to have a base case. Your recursion should reach a point where it no longer needs to call itself to get an answer. At some point the problem should be trivial enough to just output an answer.
  2. Always make your problem smaller. Whenever you make a recursive call make sure your arguments are smaller than what they were to begin with. If they aren't, then you can get yourself into some nasty infinite loops.
  3. Lastly, trust the recursion! Don't overthink the problem. If your recursion makes sense and you've followed hints 1 and 2 you probably have working code. You don't always need to trace through the recursion to make sure your procedure works as you expect it to.

## Prerequisites and What to Expect

For this lesson, you should understand the very basics of Racket and know
proper syntax.

In this lesson, you will learn recursion.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 1.1 - The Elements of Programming](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%25_sec_1.1)
  * [Lecture Notes](https://docs.google.com/document/d/1_E7HFl1F0L-CCkL3UJfBtdhMwIRuMHuMzy05ByYn7Fk/edit)

If you'd like more resources, check out all of the readings for Unit 0.


## Functions

Before we talk about functions in computer science, let's talk about functions
in math. In math, a function [mathjaxinline]f(x)[mathjaxinline] takes a single input [mathjaxinline]x[mathjaxinline], does
"something" to that [mathjaxinline]x[mathjaxinline], and returns a new value. For each [mathjaxinline]x[mathjaxinline] that the
function takes in, it returns only one value, and it returns _the same value
every time_. For example, if [mathjaxinline]f(x) = x + 2[mathjaxinline], every single time we plug in 4 to
[mathjaxinline]f(x)[mathjaxinline], we will get 6. In no circumstance will we input 4 and get 5,
[mathjaxinline]\sqrt{2}[mathjaxinline], 7, or anything other than 6.

It's the same thing in computer science! A function is defined as a
[procedure](https://preview.edge.edx.org/courses/uc-berkeley/cs61as-
1x/SICP/wiki/cs61as-1x/procedure/) that has the property that the output is
dependent on the inputs--that is, when given a certain input(s) to a function,
it returns the same output every time.

`(define (square x)`

`(* x x))`

is a function because whenever we put in an input, we always get that input
times itself.

In addition to functions, Racket also has a more general type of data type
called a _procedure_. A procedure is like a function, but it does not have to
necessarily return the same output for every input. For example, `square` is a
function, but `random` is not, because for the same input, we can get a
different output for each call of random.

To clarify: in Racket, **all functions are procedures, but not all procedures
are functions**.

Here are some things covered in this subsection:

1. Functions--what they are, how to define them.

2. Primitive procedures

3. Special Forms

What next?

Start the next subsection 1!

