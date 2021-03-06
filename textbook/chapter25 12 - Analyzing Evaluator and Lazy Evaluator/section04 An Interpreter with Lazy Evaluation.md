## The Big Idea

In this section we will implement a normal-order language that is the same as
Scheme, except that **compound procedures are non-strict in each argument. Primitive procedures will still be strict.** It is not difficult to modify
the evaluator of Lesson 12 so that the language it interprets behaves this
way. Almost all the required changes center around procedure application.

(Remember, the choices above are just that: choices! The metacircular
evaluator from Lesson 12 works perfectly fine, but sometimes we want Scheme to
act differently. This section will be about modifying the MCE code so that our
interpreted Scheme is normal-order.)

The basic idea is that, when applying a procedure, the interpreter must
determine which arguments are to be evaluated and which are to be delayed. The
delayed arguments are not evaluated; instead, they are transformed into
objects called **thunks**. The thunk must contain the information required to
produce the value of the argument when it is needed, as if it had been
evaluated at the time of the application. Thus, the thunk must contain the
argument expression and the environment in which the procedure application is
being evaluated.

The process of evaluating the expression in a thunk is called **forcing**. In
general, a thunk will be forced only when its value is needed: when it is
passed to a primitive procedure that will use the value of the thunk; when it
is the value of a predicate of a conditional; and when it is the value of an
operator that is about to be applied as a procedure. One design choice we have
available is whether or not to memoize thunks, as we did with delayed objects
in Lesson 11. With memoization, the first time a thunk is forced, it stores
the value that is computed. Subsequent forcings simply return the stored value
without repeating the computation. We'll make our interpreter memoize, because
this is more efficient for many applications. There are tricky considerations
here, however.

## Modifying the Evaluator

The main difference between the lazy evaluator and the one in Lesson 12 is in
the handling of procedure applications in `eval` and `apply`.

The `application?` clause of `eval` becomes

    
    ((application? exp)
     (apply (actual-value (operator exp) env)
            (operands exp)
            env))
    

This is almost the same as the `application?` clause of `eval` in Lesson 12.
For lazy evaluation, however, we call `apply` with the operand expressions,
rather than the arguments produced by evaluating them. Since we will need the
environment to construct thunks if the arguments are to be delayed, we must
pass this as well. We still evaluate the operator, because `apply` needs the
actual procedure to be applied in order to dispatch on its type (primitive
versus compound) and `apply` it.

Whenever we need the actual value of an expression, we use

    
    (define (actual-value exp env)
      (force-it (eval exp env)))
    

instead of just `eval`, so that if the expression's value is a thunk, it will
be forced.

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
    

## Handling `if`

The other place we must change the evaluator is in the handling of` if`, where
we must use `actual-value` instead of `eval` to get the value of the predicate
expression before testing whether it is `true` or `false`:

    
    (define (eval-if exp env)
      (if (true? (actual-value (if-predicate exp) env))
          (eval (if-consequent exp) env)
          (eval (if-alternative exp) env)))
    

## Modifying the `driver-loop`

Finally, we must change the `driver-loop` procedure (the `read-eval-print`
loop) to use `actual-value` instead of `eval`, so that if a delayed value is
propagated back to the `read-eval-print` loop, it will be forced before being
printed. We also change the prompts to indicate that this is the lazy
evaluator:

    
    (define input-prompt ";;; L-Eval input:")
    (define output-prompt ";;; L-Eval value:")
    (define (driver-loop)
      (prompt-for-input input-prompt)
      (let ((input (read)))
        (let ((output
               (actual-value input the-global-environment)))
          (announce-output output-prompt)
          (user-print output)))
      (driver-loop))
    

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
    

## Representing Thunks

Our evaluator must arrange to create thunks when procedures are applied to
arguments and to force these thunks later. A thunk must package an expression
together with the environment, so that the argument can be produced later. To
force the thunk, we simply extract the expression and environment from the
thunk and evaluate the expression in the environment. We use `actual-value`
rather than `eval` so that in case the value of the expression is itself a
thunk, we will force that, and so on, until we reach something that is not a
thunk:

    
    (define (force-it obj)
      (if (thunk? obj)
          (actual-value (thunk-exp obj) (thunk-env obj))
          obj))
    

One easy way to package an expression with an environment is to make a list
containing the expression and the environment. Thus, we create a thunk as
follows:

    
    (define (delay-it exp env)
      (list 'thunk exp env))
    
    (define (thunk? obj)
      (tagged-list? obj 'thunk))
    
    (define (thunk-exp thunk) (cadr thunk))
    
    (define (thunk-env thunk) (caddr thunk))
    

Actually, what we want for our interpreter is not quite this, but rather
thunks that have been memoized. When a thunk is forced, we will turn it into
an evaluated thunk by replacing the stored expression with its value and
changing the thunk tag so that it can be recognized as already evaluated.

    
    (define (evaluated-thunk? obj)
      (tagged-list? obj 'evaluated-thunk))
    
    (define (thunk-value evaluated-thunk)
      (cadr evaluated-thunk))
    (define (force-it obj)
      (cond ((thunk? obj)
             (let ((result (actual-value
                            (thunk-exp obj)
                            (thunk-env obj))))
               (set-car! obj 'evaluated-thunk)
               (set-car! (cdr obj) result)  ; replace exp with its value
               (set-cdr! (cdr obj) '())     ; forget unneeded env
               result))
            ((evaluated-thunk? obj)
             (thunk-value obj))
            (else obj)))
    

Notice that the same `delay-it` procedure works both with and without
memoization.

