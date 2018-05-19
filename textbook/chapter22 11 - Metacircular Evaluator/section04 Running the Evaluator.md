## Running the Evaluator

Let's look at how Scheme runs the evaluator. So far, we learned how the Scheme
expressions are evaluated using `mc-eval` and `mc-apply`. Then how is the evaluator
program running?

What our evaluator program does is to reduce all the expressions to the
application of primitive procedures.  So all we need to run the evaluator is
to create a mechanism that uses the underlying Scheme system for the application
of primitive procedures.

There must be a binding for each primitive procedure name, so that when `mc-eval`
evaluates the operator of an application of a primitive, it will find an
object to pass to `mc-apply`. We thus set up a global environment that associates
unique objects with the names of the primitive procedures that can appear in
the expressions we will be evaluating (for example, we'll bind `+` to the
underlying Scheme procedure with the same name). The global environment also includes
bindings for the symbols `true` and `false`, so that they can be used as
variables in expressions to be evaluated.

    
    (define (setup-environment)
      (let ((initial-env
             (extend-environment (primitive-procedure-names)
                                 (primitive-procedure-objects)
                                 the-empty-environment)))
        (define-variable! 'true true initial-env)
        (define-variable! 'false false initial-env)
        initial-env))
    (define the-global-environment (setup-environment))
    

For convenience in running the metacircular evaluator, we provide a **driver
loop** that models the read-eval-print loop (or REPL) of the underlying Scheme system. It
prints a **prompt**, reads an input expression, evaluates this expression in
the global environment, and prints the result. We precede each printed result
by an **output prompt** so as to distinguish the value of the expression from
other output that may be printed.

    
    (define input-prompt ";;; M-Eval input:")
    (define output-prompt ";;; M-Eval value:")
    (define (driver-loop)
      (prompt-for-input input-prompt)
      (let ((input (read)))
        (let ((output (mc-eval input the-global-environment)))
          (announce-output output-prompt)
          (user-print output)))
      (driver-loop))
    (define (prompt-for-input string)
      (newline) (newline) (display string) (newline))
    
    (define (announce-output string)
      (newline) (display string) (newline))
    

We use a special printing procedure, `user-print`, to avoid printing the
environment part of a compound procedure, which may be a very long list (or
may even contain cycles).

    
    (define (user-print object)
      (if (compound-procedure? object)
          (display (list 'compound-procedure
                         (procedure-parameters object)
                         (procedure-body object)
                         '(procedure-env>))
          (display object)))
    

Now all we need to do to run the evaluator is to initialize the global
environment and start the driver loop. Here is a sample interaction:

    
    (define the-global-environment (setup-environment))
    (driver-loop)
    ;;; M-Eval input:
    (define (append x y)
      (if (null? x)
          y
          (cons (car x)
                (append (cdr x) y))))
    ;;; M-Eval value:
    ok
    ;;; M-Eval input:
    (append '(a b c) '(d e f))
    ;;; M-Eval value:
    (a b c d e f)

_Wait, I still don't get it. How can we evaluate Scheme code with an evaluator
that is written in Scheme?_

It's because Scheme is powerful enough to handle a program as data, and to let
us construct data structures that are both hierarchical and circular. I have
an analogy for you in the next section.

## Data as Programs

To understand interpreting Scheme expression with the interpreter written in
Scheme, think of a program as a description of an abstract machine. For
example, you can think of the program to compute factorials:

    
    (define (factorial n)
      (if (= n 1)
          1
          (* (factorial (- n 1)) n)))

as the description of a machine containing parts that decrement, multiply, and
test for equality, together with a two-position switch and another factorial
machine. (The factorial machine is infinite because it contains another
factorial machine within it -- recursion!) So the machine will look like this:

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch4-Z-G-2.gif)

Like `factorial`, the evaluator is a very special machine that takes a
description of other machine as input, and then configures itself to emulate
the given machine. For example, if we give the evaluator the definition of
`factorial`, the evaluator will emulate it and be able to compute factorials.

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch4-Z-G-3.gif)

So our evaluator is just a universal machine that mimics all other machines!

If you'd like to know more about the machines, ask for Unit 5.

## Takeaways

In this subsection, you learned how the evaluator works.

## What's Next?

Go do your homework! You should also start on Project 4, where you'll learn
the Python programming language.

