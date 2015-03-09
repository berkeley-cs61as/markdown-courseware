## Modifying `apply`

Our new version of `apply` is also almost the same as the version in MCE. The
difference is that `eval` has passed in unevaluated operand expressions: For
primitive procedures (which are strict), we evaluate all the arguments before
applying the primitive; for compound procedures (which are non-strict) we
delay all the arguments before applying the procedure.

    
    (define (apply procedure arguments env)
      (cond ((primitive-procedure? procedure)
             (apply-primitive-procedure
              procedure
              (list-of-arg-values arguments env)))  ; changed
            ((compound-procedure? procedure)
             (eval-sequence
              (procedure-body procedure)
              (extend-environment
               (procedure-parameters procedure)
               (list-of-delayed-args arguments env) ; changed
               (procedure-environment procedure))))
            (else
             (error
              "Unknown procedure type -- APPLY" procedure))))
    

The procedures that process the arguments are just like `list-of-values` from
Lesson 12, except that `list-of-delayed-args` delays the arguments instead of
evaluating them, and `list-of-arg-values` uses `actual-value` instead of
`eval`:

    
    (define (list-of-arg-values exps env)
      (if (no-operands? exps)
          '()
          (cons (actual-value (first-operand exps) env)
                (list-of-arg-values (rest-operands exps)
                                    env))))
    (define (list-of-delayed-args exps env)
      (if (no-operands? exps)
          '()
          (cons (delay-it (first-operand exps) env)
                (list-of-delayed-args (rest-operands exps)
                                      env))))
    

