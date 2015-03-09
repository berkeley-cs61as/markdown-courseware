## Introduction

At this point, you know (in principle) how to build a Scheme interpreter in
Scheme. Now we see how to both make the Metacircular Evaluator more efficient
and how changing the Metacircular Evaluator changes how the language is
interpreted, and what advantages this provides. In particular, we form two new
evaluators. The first evaluator separates the syntactic analysis of a program
(analyzing what a program says to do) from its execution (actually doing what
the program says to do) in order to increase efficiency. The second evaluator
changes the interpreter from Applicative Order to Normal Order.

