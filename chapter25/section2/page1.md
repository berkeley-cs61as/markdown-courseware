(Be sure to read section [4.1.7](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-26.html#%_sec_4.1.7) of SICP before proceeding).

Here is a nice example of evaluating `factorial` using the analyzing
evaluator. Lets consider the following Scheme code:

    
      (define factorial
        (lambda (n)
          (if (= n 1)
              1
              (* (factorial (- n 1)) n))))
      (factorial 2) ;; low argument, so that the example is not too long)))
    

There are two statements here: one definition and one application.

We start with the definition, which we will call `d` here (where `d` stands
for '(define (factorial n) ...)'):

    
      (eval d env)
      ((analyze d) env)
      ((analyze-definition d) env)
    

`analyze-definition` will first analyze the `definition-value` and then create
an execution procedure that, when executed, will `define` the variable name to
the analyzed `definition-value`.

This point is crucial. We are not just assigning a `lambda` to `factorial`, we
are assigning an _analyzed_ `lambda` to `factorial`. This will provide a
performance boon later on.

So, to figure out the value of `factorial`, we analyze the `lambda`, with...
`analyze-lambda`, of course (through the dispatch in analyze).

The boon that `analyze-lambda` provides is really from analyzing the body
_once_, and then making a procedure Abstract Data Type with an `analyzed` body
(a scheme procedure), instead of a simple list of instructions, like in the
old `eval`.

The point is that, on invocations of our `lambda`, we won't have to deal with
parsing. Parsing will _only_ be done upon creating the `lambda`.

Let's see this in action.

(NOTE: I'll be using `:=` as a way to denote storing:

    
    var := value 

This isn't really scheme, but I think it's easier than having a bunch of `let`
statements.)

    
    (analyze-lambda '(lambda (n) ...)')
    

Now we need to `analyze` the body, then store it for later, so that we don't
redundantly `analyze` the body again.

    
    analyzed-body := (analyze (lambda-body '(lambda (n) (if ...))'))
    
    (analyze-if '(if (= n 1)
                     1
                     (* (factorial (- n 1)) n))')
    

`analyze-if` analyzes everything it's given, stores it, and then creates a new
execution procedure with those stored values.

    
      if-pred := (analyze '(= n 1)')
      ; this is the execution procedure: (lambda (env)
      ;                                    (execute-application (analyzed/= env)
    
      if-true := (analyze '1')
      ; this is the execution procedure: (lambda (env) 1)
    
      if-false := (analyze '(* (factorial (- n 1)) n)')
      ; this is too long to write out, but it's
      ; kind of like if-pred
    
      ;;this is the execution procedure we return:
      ;;lets call this execution procedure 'analyzed-fact-if'
      (lambda (env)
        (if (true? (if-pred env))
            (if-true env)
            (if-false env)))
    

And now that we know that result, let's go back to `analyze-lambda`.

    
      analyzed-body := analyzed-fact-if
      (analyze-lambda '(lambda (n) ...)')
         => (lambda (env) (make-procedure '(n) analyzed-body env'))
    

We store the last expression into the `factorial` variable, and we're done
defining `factorial`. Note that we only analyze the body _ONCE_: during the
analysis stage. We never `analyze` during the evaluation stage! This means
that during evaluation, every time we call this `factorial` function, we know
its body contains an `if` statement, and that the `if` statement checks if `n`
equals `0` (and what to do if the predicate is true or false).

Now, on to evaluating factorial. This is where you'll see all the cryptic
analyzing work pay off.

    
      (eval '(factorial 2) env') ; env has factorial definition
    
      ((analyze '(factorial 2)') env)
    
      ((analyze-application '(factorial 2)') env)
    
      ((lambda (env) (execute-application ...)) env)
    
      ((procedure-body {internal factorial value})
       (extend-environment ...)) ; extend-environment is same as old eval
    
      ;; Lets call the extended environment, env2
      (analyzed-body env2) ; analyzed-body from definition above
    
     ((lambda (env)
       (if (true? (if-pred env))
           (if-true env)
           (if-false env)))
      env2)
    
     (if (true? (if-pred env2)) ; (= n 0)
         (if-true env2)   ; 1
         (if-false env2)) ; (* (factorial (- n 1)) n)
    

Here, `n = 2 != 0`, so we'll end up calling executing `(if-false env2)`. `if-
false` will do an application of `*` to `(factorial (- n 1))` and `n`, but
these arguments have already been `analyzed` (when we did `analyze-lambda`).
So we evaluate the analyzed `(factorial (- n 1))`, which is:

    
      (analyzed-factorial {result of calling analyzed (- n 1)})
    
      (analyzed-body env3)
      ;env3 := env2 extended with n := (- {previous n} 1) = (- 2 1) = 1
    
      (if (true? (if-pred env3)) ; (= n 0)
          (if-true env3)   ; 1
          (if-false env3)) ; (* (factorial (- n 1)) n)
    

We recurse again, in the same fashion:

    
      (if (true? (if-pred env4)) ; (= n 0)
          (if-true env4) ; 1
          (if-false env4)) ; (* (factorial (- n 1)) n)
    

Here, `n` actually equals `0`, so we call `(if-true env4).` `if-true`
disregards `env4` and returns the number `1`. Then, we go back to all the
execute-application primitive applications and multiply everything together.

And we get... `2`.

So, we're done.

Notice that during the evaluation phase, we never check the syntax of a
statement. The syntax has already been looked at, and `analyzed`. We simply
carry out what these `analyzed` statements tell us to do. Think about the gain
in efficiency here when computing something like `(factorial 100)`.

