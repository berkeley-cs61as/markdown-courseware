## Handling `if`

The other place we must change the evaluator is in the handling of` if`, where
we must use `actual-value` instead of `eval` to get the value of the predicate
expression before testing whether it is `true` or `false`:

    
    (define (eval-if exp env)
      (if (true? (actual-value (if-predicate exp) env))
          (eval (if-consequent exp) env)
          (eval (if-alternative exp) env)))
    

