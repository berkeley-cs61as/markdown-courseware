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

