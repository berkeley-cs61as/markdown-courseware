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

