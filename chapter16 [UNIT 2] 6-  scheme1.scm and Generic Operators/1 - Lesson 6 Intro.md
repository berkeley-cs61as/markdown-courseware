## Introduction

This lesson covers generic operators and introduces the program Scheme-1. Read
on to learn more about these topics!

## Prerequisites

You should have a good understanding of `calc.scm` and data abstraction.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 2.4](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-17.html#%25_sec_2.4)
  * [SICP 2.51-2.52](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-18.html#%25_sec_2.5)
  * [Lecture Notes](http://www-inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=42)

## Generic Operators

In this lesson, we begin our exploration of generic operators, the idea where
we have different types of data and each type of data is intelligent--they
know how to manipulate themselves. Procedures then are "stupid"--they don't
know anything about each of the data types and somehow it still works out.
Because of this ignorance of data types and the ability to operate across
different types, they are dubbed "generic".

We also introduce `scheme1.scm`! Scheme-1 is a simple Scheme interpreter
written in Scheme. While it cannot do all the things STk can do, it does
demonstrate the working parts you need in an interpreter, such as evaluating
expressions `(eval-1)` and applying procedures to arguments `(apply-1)`.
`eval-1` takes a compound expression and reduces it to its simplest value.
`apply-1` takes a procedure and some simple values and applies the procedure
to those values to get a result.

![](http://inst.eecs.berkeley.edu/~cs61AS/sp13/lab/eval-apply.gif)

