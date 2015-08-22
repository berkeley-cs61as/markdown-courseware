## Mutable Data and Vectors

Back in Unit 2, we used compound data (pairs and lists) to construct computational objects with multiple parts. Then, in Lesson 7, we learned another aspect of data, which Unit 2 did not address&mdash;we are now able to *mutate* data using `set!`. We will now explore how we can mutate *pairs*.

## Prerequisites

Before proceeding, make sure you understand how to manipulate lists and pairs.

## Readings

Use the readings below at your own discretion; they are written in Scheme and will have different syntax than the Racket version we will teach.

  * [SICP 3.3.1-3](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-22.html#%_sec_3.3)
  * [Lecture Notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=56)

## Warning

In Racket, a mutable pair (`mcons`) is not a pair (`cons`); they are completely separate data types. Similarly, a mutable list (`mlist`) is not a list (`list`), except that the empty list is also the empty mutable list.

Using mutable data rather than the usual immutable pairs and lists is a dangerous choice. Make sure you fully understand the consequences of using destructive updates before using mutable data in your projects. The purpose of this lesson is thus to teach the concept of mutable data, rather than to promote a certain programming style.