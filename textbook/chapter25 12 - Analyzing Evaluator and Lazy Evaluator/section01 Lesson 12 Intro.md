## Introduction

At this point, you know (in principle) how to build a Scheme interpreter in
Scheme. Now we see how to both make the Metacircular Evaluator more efficient
and how changing the Metacircular Evaluator changes how the language is
interpreted, and what advantages this provides. In particular, we form two new
evaluators. The first evaluator separates the syntactic analysis of a program
(analyzing what a program says to do) from its execution (actually doing what
the program says to do) in order to increase efficiency. The second evaluator
changes the interpreter from Applicative Order to Normal Order.

## Prerequisites and What to Expect

You should be very familiar with the Metacircular Evaluator from Lesson 11.
This lesson builds heavily upon the ideas and code of the MCE.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 4.1.7 Separating Syntactic Analysis from Execution](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-26.html#%_sec_4.1.7)
  * [SICP 4.2 Lazy Evaluation](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-27.html#%_sec_4.2)
  * [Lecture Notes](http://www-inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=93) (Skip the nondeterministic evaluator.)
  * [Therac Paper](http://www-inst.eecs.berkeley.edu/~cs61as/reader/Therac-25.pdf)

When you're ready, move on to the next section!
