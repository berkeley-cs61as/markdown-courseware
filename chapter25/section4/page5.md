## Testing it Out

With these changes made, we can start the evaluator and test it. The
successful evaluation of the `try` expression discussed in the section on
Normal vs. Applicative Order indicates that the interpreter is performing lazy
evaluation:

    
    
    (define the-global-environment (setup-environment))
    (driver-loop)
    ;;; L-Eval input:
    (define (try a b)
      (if (= a 0) 1 b))
    ;;; L-Eval value:
    ok
    ;;; L-Eval input:
    (try 0 (/ 1 0))
    ;;; L-Eval value:
    1
    

