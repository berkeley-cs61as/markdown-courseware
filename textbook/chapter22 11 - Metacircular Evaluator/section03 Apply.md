

## Apply

The procedure `apply` takes two arguments: a procedure and a list of arguments to which the
procedure should be applied. `Apply` classifies procedures into two kinds: It
calls `apply-primitive-procedure` to apply primitives; it applies compound
procedures by sequentially evaluating the expressions that make up the body of
the procedure. To create the environment in which we'll evaluate the body of the compound procedure,
we'll extend the base environment of the procedure to include a frame that binds the parameters of
the procedure to the arguments to which the procedure is to be applied.

 Here is the definition of `apply`:

    
    (define (mc-apply procedure arguments)
      (cond ((primitive-procedure? procedure)
                (apply-primitive-procedure procedure arguments))
            ((compound-procedure? procedure)
                (eval-sequence
                  (procedure-body procedure)
                  (extend-environment
                    (procedure-parameters procedure)
                    arguments
                    (procedure-environment procedure))))
            (else
              (error
                "Unknown procedure type -- APPLY" procedure))))
    

We will go through the procedures used in the definition, one-by-one.

## Representing Procedures

In our metacircular evaluator, procedures are represented by tagged lists. Primitive 
procedures have the tag `primitive`, and compound procedures have the tag `procedure`. If
we want to see what type of a procedure something is, we just have to check its tag.

To handle primitives, we assume that we have available the following
procedures:

  * `(apply-primitive-procedure proc args)`  
applies the given primitive procedure to the argument values in the list
'args' and returns the result of the application.

  * `(primitive-procedure? proc)`  
tests whether `proc` is a primitive procedure.


Compound procedures are constructed from parameters, procedure bodies, and
environments using the constructor `make-procedure`:

    
    (define (make-procedure parameters body env)
      (list 'procedure parameters body env))
    (define (compound-procedure? p)
      (tagged-list? p 'procedure))
    (define (procedure-parameters p) (cadr p))
    (define (procedure-body p) (caddr p))
    (define (procedure-environment p) (cadddr p))
    

## Primitive Procedures

At this point, you may wonder how primitive
procedures are represented in Racket. There is actually no right way to
represent the primitive procedures, as long as `apply` can identify and apply
them by using the procedures `primitive-procedure?` and `apply-primitive-
procedure`.

People who created Racket decided to represent a primitive procedure as a tagged list
that begins with the symbol `primitive` and contains a procedure in the
underlying Racket that implements that primitive.

    
    (define (primitive-procedure? proc)
      (tagged-list? proc 'primitive))
    
    (define (primitive-implementation proc) (cadr proc))
    
    (define primitive-procedures
      (list (list 'car car)
            (list 'cdr cdr)
            (list 'cons cons)
            (list 'null? null?)
            <more primitives>
            ))
    
    (define (primitive-procedure-names)
      (map car
           primitive-procedures))
    
    (define (primitive-procedure-objects)
      (map (lambda (proc) (list 'primitive (cadr proc)))
           primitive-procedures))
    

To apply a primitive procedure, we simply apply the implementation procedure
to the arguments, using the underlying Racket system:

    
    (define (apply-primitive-procedure proc args)
      (apply-in-underlying-scheme
       (primitive-implementation proc) args))
    

## Operations on Environments

In order to evaluate compound procedures, the evaluator needs operations for manipulating environments. What
is an environment again? It is a sequence of frames, where each frame is a
table of bindings that associate variables with their corresponding values. We
use the following operations for manipulating environments:

  * `(lookup-variable-value <var> <env>)`  
returns the value that is bound to the symbol <var> in the environment <env>,
or signals an error if the variable is unbound.

  * `(extend-environment <variables> <values> <base-env>)`  
returns a new environment, consisting of a new frame in which the symbols in
the list <variables> are bound to the corresponding elements in the list
<values>, where the enclosing environment is the environment <base-env>.

  * `(define-variable! <var> <value> <env>)`  
adds to the first frame in the environment <env> a new binding that associates
the variable <var> with the value <value>.

  * `(set-variable-value! <var> <value> <env>)`  
changes the binding of the variable <var> in the environment <env> so that the
variable is now bound to the value <value>, or signals an error if the
variable is unbound.

To implement these operations we represent an environment as a list of frames.
The enclosing environment of an environment is the `cdr` of the list. The
empty environment is simply the empty list.

    
    (define (enclosing-environment env) (cdr env))
    (define (first-frame env) (car env))
    (define the-empty-environment '())
    

Each frame of an environment is represented as a mutable pair of mutable lists: a list of the
variables bound in that frame and a list of the associated values.

    
    (define (make-frame variables values)
      (mcons variables values))
    (define (frame-variables frame) (mcar frame))
    (define (frame-values frame) (mcdr frame))
    (define (add-binding-to-frame! var val frame)
      (set-mcar! frame (mcons var (mcar frame)))
      (set-mcdr! frame (mcons val (mcdr frame))))
    

To extend an environment by a new frame that associates variables with values,
we make a frame consisting of the list of variables and the list of values,
and we adjoin this to the environment. We signal an error if the number of
variables does not match the number of values.

Notice that since our variables and values must both be mutable lists, we
first have to convert non-mutable lists to their mutable equivalent.
    
    (define (extend-environment vars vals base-env)
      (if (not (mlist? vars)) (set! vars (list->mlist vars)) 'ok)
      (if (not (mlist? vals)) (set! vals (list->mlist vals)) 'ok)
      (if (= (mlength vars) (mlength vals))
          (cons (make-frame vars vals) base-env)
          (if (< (mlength vars) (mlength vals))
              (error "Too many arguments supplied" vars vals)
              (error "Too few arguments supplied" vars vals))))
    

To look up a variable in an environment, we scan the list of variables in the
first frame. If we find the desired variable, we return the corresponding
element in the list of values. If we do not find the variable in the current
frame, we search the enclosing environment, and so on. If we reach the empty
environment, we signal an "unbound variable" error.

    
    (define (lookup-variable-value var env)
      (define (env-loop env)
      (define (scan vars vals)
        (cond ((null? vars)
              (env-loop (enclosing-environment env)))
              ((eq? var (mcar vars))
                (mcar vals))
              (else (scan (mcdr vars) (mcdr vals)))))
      (if (eq? env the-empty-environment)
          (error "Unbound variable" var)
          (let ((frame (first-frame env)))
            (scan (frame-variables frame)
                  (frame-values frame)))))
      (env-loop env))
    

To set a variable to a new value in a specified environment, we scan for the
variable, just as in `lookup-variable-value`, and change the corresponding
value when we find it.

    
    (define (set-variable-value! var val env)
      (define (env-loop env)
      (define (scan vars vals)
        (cond ((null? vars)
                (env-loop (enclosing-environment env)))
              ((eq? var (mcar vars))
                (set-mcar! vals val))
              (else (scan (mcdr vars) (mcdr vals)))))
      (if (eq? env the-empty-environment)
          (error "Unbound variable -- SET!" var)
          (let ((frame (first-frame env)))
            (scan (frame-variables frame)
                  (frame-values frame)))))
      (env-loop env))
    

To define a variable, we search the first frame for a binding for the
variable, and change the binding if it exists (just as in `set-variable-
value!`). If no such binding exists, we adjoin one to the first frame.

    
    (define (define-variable! var val env)
      (let ((frame (first-frame env)))
        (define (scan vars vals)
          (cond ((null? vars)
                  (add-binding-to-frame! var val frame))
                ((eq? var (mcar vars))
                  (set-mcar! vals val))
                (else (scan (mcdr vars) (mcdr vals)))))
        (scan (frame-variables frame)
          (frame-values frame))))

**Important:** Notice that when we are defining variables, the value associated
with each variable has already been determined by applying `mc-eval`, so we don't
have to call `mc-eval` again!

It's also important to notice the distinction between defining variables in the metacircular
evaluator's environment and defining variables in underlying Racket. 

## Apply Revisited

Let's look at the definition of `apply` again. Does it make sense this time?

    
    (define (apply procedure arguments)
      (cond ((primitive-procedure? procedure)
             (apply-primitive-procedure procedure arguments))
            ((compound-procedure? procedure)
             (eval-sequence
               (procedure-body procedure)
               (extend-environment
                 (procedure-parameters procedure)
                 arguments
                 (procedure-environment procedure))))
            (else
             (error
              "Unknown procedure type -- APPLY" procedure))))

<div class="mc">
Which of the following use mc-apply? Multiple answers may be correct, so check each answer individually.

<ans text="apply" explanation="Correct!" correct></ans>
<ans text="apply-primitive-procedure" explanation="Incorrect!"></ans>
<ans text="eval-sequence" explanation="Incorrect!"></ans>
<ans text="extend-environment" explanation="Incorrect!"></ans>
<!-- and so on -->
</div>

## Takeaways

In this subsection, you learned the following:

  1. How `apply` is defined
  2. How primitive procedures are defined and applied
  3. How the operations on environments are defined

## What's Next?

We are going to learn how the evaluator runs as a program.

