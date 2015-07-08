## IMPORTANT

**At this point onwards, we will be using the Scheme language.** If you're reading this message, that means that we are still working on transitioning to Racket on this section. The following lesson and all lessons afterwards will be from our old curriculum, and is written in Scheme.

Thank you for your patience!

## Object Oriented Programming (OOP)

  
One of the main advantages of using generic operators is that new modules can
be designed and added to pre-existing modules without modifying the pre-
existing code. Object oriented programming is another technique that has this
advantage. This is the second major programming paradigm that we are studying,
after functional programming.

The Big Idea of object oriented programming is to have data that knows how to
perform computations on itself. For example, a number could be represented as
an object that knows how to be added to, subtracted from, multiplied with, or
divided by another number. This allows programmers to build modules
independently. To create a new data representation, a programmer creates a
class, which is like a blueprint for objects, that specifies the data to be
stored in an object of that class, and what computations can be performed on
such objects. The three main ideas that make object-oriented programming
possible are message passing, local state and inheritance.

In order to use the OOP language in Sublime, you must first enter the following into the Stk interpreter:

	(load "~cs61as/lib/obj.scm")

Afterwards, you will be able to call `define-class` and `ask` as necessary.

## Prerequisites

You need to be done with Unit 2, especially the subsection with "Data
Directed" and "Message Passing".

## Readings

The majority of the content of this lesson is taken from [this
note](http://inst.eecs.berkeley.edu/~cs61as/reader/aboveline.pdf).

This is a [handy cheatsheet](https://docs.google.com/file/d/0B2F__e2jC6gQSHhBdERPZ0pVRG8/edit)
we recommend you use for the homework and quiz.

You should also check out the old lecture notes [here](http://www-inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=46).

## OBJECTS

When we are coding in OOP, we are dealing with objects or "smart data" that
know how to do operations internally and how to interact with other objects.
For example, we can have an object `Fred` of type `human`. He internally knows
how to eat other objects, say, `dumpling`. OOP then allows us to "Ask Fred to
eat dumpling".

## JARGONS

Programmers who use OOP language have special vocabularies to describe
different components of OOP. In the example above, `Fred` is an **instance**
and the general category of `human` is a **class**.

Scheme does not natively support OOP, but we have an extension that provides
OOP to Scheme. This lab will focus on "Above the Line" of abstraction for OOP.
We will see how to design a class and make objects using the given framework.
If you are interested in how OOP is actually implemented in Scheme, don't
worry, one of our future lessons will cover exactly that.

## Takeaways

In this subsection, you learned the general idea of the following terms:

  * Object Oriented Programming (OOP)
  * Object
  * Instance
  * Class

## What's Next?

It's time to learn how to play with OOP and define your own class!

