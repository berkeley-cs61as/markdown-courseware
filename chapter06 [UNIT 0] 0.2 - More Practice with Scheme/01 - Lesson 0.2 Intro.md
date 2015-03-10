## Introduction

This lesson covers the Scheme programming language in more depth and also
introduces the Big Idea of Functional Programming, a programming paradigm that
focuses on making functions work together in order to solve problems.

## Prerequisites and What to Expect

The first day material, Lesson 0.1, is required before working on this lesson.

We will go over basic syntax of Scheme, and how to use it to solve simple
problems. The idea of Functional Programming will be highlighted as you write
various functions and expressions that solve these problems.

## Readings

Here are the relevant readings for this lesson:

  * [SS Ch. 3 - Expressions](http://www.cs.berkeley.edu/~bh/ssch3/people.html)
  * [SS Ch. 4 - Defining Procedures](http://www.cs.berkeley.edu/~bh/ssch4/defining.html)
  * [SS Ch. 5 - Words and Sentences](http://www.cs.berkeley.edu/~bh/ssch5/words.html)
  * [SS Ch. 6 - Booleans, Predicates, and Special Forms](http://www.cs.berkeley.edu/~bh/ssch6/true.html)

## Introduction to Scheme

Scheme is a dialect of Lisp, i.e.

> "the greatest single programming language ever designed" -- Alan Kay

Why do we learn it?

> "Lisp is worth learning for the profound enlightenment experience you will
have when you finally get it; that experience will make you a better
programmer for the rest of your days, even if you never actually use Lisp
itself a lot." -- Eric Raymond

## Basics

The Big Idea: You can ask Scheme questions, called _expressions_. You get back
answers, called _values_. More on this in the coming subsection.

When you want Scheme to _do_ something (e.g. add two numbers together), use
prefix notation--put the operator is at the beginning of the expression,
followed by arguments. For example:

    
    (+ 3 4)

This regular-looking syntax allows us to nest expressions:

    
    (* (max 2 3) (/ 8 4))

Try playing around with some expressions in the [Scheme
interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-scheme-
stk/index.html)

## Functional Programming

The big idea for this lesson is deceptively simple. It's that we can take the
value returned by one function and use it as an argument to another function.
By "hooking up" two functions in this way, we invent a new, third function.
For example, let's say we have a function that adds the letter s to the end of
a word (in pseudo-code):

    
    add-s("run") = "runs"

and another function that puts two words together into a sentence:

    
    sentence("day", "tripper") = "day tripper"

We can combine these to create a new function that represents the third person
singular form of a verb:

    
    third-person(verb) = sentence("she", add-s(verb))

That general formula looks like this when applied to a particular verb:

    
    third-person("sing") = "she sings"

The way we say it in Scheme is

    
    (define (third-person verb)
      (sentence 'she (add-s verb)))

This idea might not seem like a big deal to you. Nevertheless, it will turn
out that we can express a wide variety of computational algorithms by linking
functions together in this way. This linking is what we mean by "functional
programming."

