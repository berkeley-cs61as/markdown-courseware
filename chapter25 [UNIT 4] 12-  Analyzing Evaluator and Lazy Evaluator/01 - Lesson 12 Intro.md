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

  * [SICP 4.1.7 Separating Syntactic Analysis from Execution ](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html#%_sec_4.1.7)
  * [SICP 4.2 Lazy Evaluation](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-27.html#%_sec_4.2)
  * [Lecture Notes](http://www-inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=93) (Skip the nondeterministic evaluator.)
  * [Therac Paper](http://www-inst.eecs.berkeley.edu/~cs61as/reader/Therac-25.pdf)

##  Analyzing Evaluator

To work with the ideas in this section, get the analyzing metacircular
evaluator:

[http://inst.eecs.berkeley.edu/~cs61as/library/analyze.scm
](http://inst.eecs.berkeley.edu/~cs61as/library/analyze.scm)

The Metacircular Evaluator implemented in section 12 is simple, but it is very
inefficient, because the syntactic analysis of expressions is interleaved with
their execution. Thus if a program is executed many times, its syntax is
analyzed many times. Lets consider an example.

Suppose we’ve defined the `factorial` function as follows:

    
    
    (define (fact num) 
      (if (= num 0)
          1
          (* num (fact (- num 1)))))
    

What happens when we compute `(fact 3)`?

    
      
    eval (fact 3) 
      self-evaluating? ==> #f 
      variable? ==> #f
      quoted? ==> #f 
      assignment? definition?
      if? ==> #f
      lambda? ==> #f
      begin? ==> #f
      cond? ==> #f 
      application? ==> #t 
      eval fact
        self-evaluating? ==> #f
        variable? ==> #t
        lookup-variable-value ==> <procedure fact> 
        list-of-values (3)
          eval3 ==> 3
        apply <procedure fact> (3)
          eval (if (= num 0) ...) 
          self-evaluating? ==> #f 
          variable? ==> #f 
          quoted? ==> #f 
          assignment? ==> #f 
          definition? ==> #f
          if? ==> #t 
            eval-if (if (= num 0) ...) 
              if-predicate ==> (= num 0)
                eval (= num 0)
                self-evaluating? ==> #f
                ...
              if-alternative ==> (* num (fact (- num 1)))              
                eval (* num (fact (- num 1)))
                  self-evaluating? ==> #f
                  ...
                  list-of-values (num (fact (- num 1)))
                    ...
                    eval (fact (- num 1))
                      ...
                      apply <procedure fact> (2)
                        eval (if (= num 0) ...)
    
    

Four separate times, the evaluator has to examine the procedure body, decide
that it’s an if expression, pull out its component parts, and evaluate those
parts (which in turn involves deciding what type of expression each part is).

This is one reason why interpreted languages are so much slower than compiled
languages: The interpreter does the syntactic analysis of the program over and
over again. The compiler does the analysis once, and the compiled program can
just do the part of the computation that depends on the actual values of
variables. In this section, we will study the analyzing evaluator to see how
to prevent the repetitive analysis of a program's syntax.

