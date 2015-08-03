##  Analyzing Evaluator

To work with the ideas in this section, get the analyzing metacircular
evaluator:

    cp ~cs61as/lib/analyze.scm .

The Metacircular Evaluator implementation in Lesson 12 is simple, but it is very inefficient because of how the syntactic analysis of expressions is interleaved with their execution. Thus, if a program is executed many times, its syntax is analyzed many times. Let's consider an example.

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

This is one reason why interpreted languages are so much slower than [compiled languages](https://en.wikipedia.org/wiki/Compiled_language): The interpreter does the syntactic analysis of the program over and over again. The compiler does the analysis once, and the compiled program can just do the part of the computation that depends on the actual values of variables. In this section, we will study the analyzing evaluator to see how to prevent the repetitive analysis of a program's syntax.

##  The Separation

`eval` takes two arguments, an expression and an environment. Of those, the expression argument is the same every time we revisit the same expression, whereas the environment will be different each time. For example, when we compute `(fact 3)`, we evaluate the body of `fact` in an environment in which `num` has the value `3`. That body includes a recursive call to compute `(fact 2)`, in which we evaluate the same body, but now in an environment with `num` bound to `2`.

Our plan is to look at the evaluation process, find those parts which depend
only on `exp` and not on `env`, and do those only once. The procedure that
does this work is called `analyze`.

What is the result of `analyze`? It has to be something that can be combined
somehow with an environment in order to return a value. The solution is that
`analyze` returns a procedure that takes only `env` as an argument, and does
the rest of the evaluation.

Instead of

    (eval exp env) ==> value


we now have

    1. (analyze exp) ==> exp-procedure 
    2. (exp-procedure env) ==> value

<div class="mc">
<strong>Test Your Understanding</strong><br><br>

What type of argument(s) does the procedure returned by analyze accept?

<ans text="expression" explanation=""></ans>
<ans text="environment" explanation="Analyze returns a function that carries out the task of a given syntactic expression. The syntactic expressions in a program often depend on values that are stored in the environment (such as set! statements)." correct></ans>
<ans text="Both an expression and an environment" explanation=""></ans>
</div>

When we evaluate the same expression again, we only have to repeat step 2. What we’re doing is akin to memoization, in that we remember the result of a computation to avoid having to repeat it. The difference is that now we’re remembering something that’s only part of the solution to the overall problem, instead of a complete solution.

We can duplicate the effect of the original `eval` this way:

    (define (eval exp env)
      ((analyze exp) env))


## `analyze`

`analyze` has a structure similar to that of the original `eval`:

    (define (analyze exp)
      (cond
        ((self-evaluating? exp)
          (analyze-self-eval exp)) 
        ((variable? exp)
          (analyze-var exp)) 
        ...
        ((foo? exp) (analyze-foo exp)) 
        ...))

The difference is that the procedures such as `eval-if` that take an expression and an environment as arguments have been replaced by procedures such as `analyze-if` that take only the expression as argument. How do these analysis procedures work? As an intermediate step in our understanding, here is a version of `analyze-if` that exactly follows the structure of `eval-if` and doesn’t save any time:

**`eval-if`:**

    (define (eval-if exp env)
      (if (true? (eval (if-predicate exp) env))
          (eval (if-consequent exp) env) 
          (eval (if-alternative exp) env)))
    
**`analyze-if`:**

    (define (analyze-if exp) 
      (lambda (env)
        (if (true? (eval (if-predicate exp) env)) 
            (eval (if-consequent exp) env)
            (eval (if-alternative exp) env))))


This version of `analyze-if` returns a procedure with `env` as its argument,
whose body is exactly the same as the body of the original `eval-if`.
Therefore, if we do

    ((analyze-if some-if-expression) some-environment)

the result will be the same as if we’d said

    (eval-if some-if-expression some-environment)

in the original metacircular evaluator.

But we’d like to improve on this first version of `analyze-if` because it
doesn’t really avoid any work. Each time we call the procedure that `analyze-
if` returns, it will do all of the work that the original `eval-if` did.

The first version of `analyze-if` contains three calls to `eval`. Each of
those calls does an analysis of an expression and then a computation of the
value in the given environment. What we’d like to do is split each of those
`eval` calls into its two separate parts, and do the first part only once, not
every time:

    (define (analyze-if exp)
      (let ((pproc (analyze (if-predicate exp)))
            (cproc (analyze (if-consequent exp)))
            (aproc (analyze (if-alternative exp)))) 
        (lambda (env)
          (if (true? (pproc env)) 
              (cproc env)
              (aproc env)))))

In this final version, the procedure returned by `analyze-if` doesn’t contain
any analysis steps. All of the components were already analyzed before we call
that procedure, so no further analysis is needed.

The biggest gain in efficiency comes from the way in which `lambda`
expressions are handled. In the original metacircular evaluator, leaving out
some of the data abstraction for clarity here, we have

    (define (eval-lambda exp env) (list ’procedure exp env))

The evaluator does essentially nothing for a `lambda` expression except to
remember the procedure’s text and the environment in which it was created. But
in the analyzing evaluator we analyze the body of the procedure (using the
`analyze-sequence` procedure); what is stored as the representation of the
procedure does not include its text! Instead, the evaluator represents a
procedure in the metacircular Scheme as a procedure in the underlying Scheme,
along with the formal parameters and the defining environment.

(Be sure to read [Section 4.1.7](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html#%_sec_4.1.7) from SICP to see how all of the syntactic analysis procedures are implemented).

## Level Confusion

The analyzing evaluator turns an expression such as

    (if A B C)

into a procedure

    (lambda (env)
      (if (A-execution-procedure env)
          (B-execution-procedure env) 
          (C-execution-procedure env)))

This may seem like a step backward; we’re trying to implement `if` and we end
up with a procedure that does an `if`. Isn’t this an infinite regress?

No, it isn’t. The `if` in the execution procedure is handled by the underlying
Scheme, not by the metacircular Scheme. Therefore, there’s no regress; we
don’t call `analyze-if` for that one. Also, the `if` in the underlying Scheme
is much faster than having to do the syntactic analysis for the `if` in the
meta-Scheme.

## So What?

The syntactic analysis of expressions is a large part of what a compiler does.
In a sense, this analyzing evaluator is a compiler! It compiles Scheme into
Scheme, so it’s not a very useful compiler, but it’s really not that much
harder to compile into something else, such as the machine language of a
particular computer.

A compiler whose structure is similar to this one is called a _recursive descent_ compiler. Today, in practice, most compilers use a different
technique (called a stack machine) because it’s possible to automate the
writing of a parser that way. (I mentioned this earlier as an example of data-
directed programming.) But if you’re writing a parser by hand, it’s easiest to
use recursive descent.

(Be sure to read section [4.1.7](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html#%_sec_4.1.7) of SICP before proceeding).

## An Example

Here is a nice example of evaluating `factorial` using the analyzing
evaluator. Let's consider the following Scheme code:

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
      ;;let's call this execution procedure 'analyzed-fact-if'
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
    
      ;; let's call the extended environment, env2
      (analyzed-body env2) ; analyzed-body from definition above
    
     ((lambda (env)
       (if (true? (if-pred env))
           (if-true env)
           (if-false env)))
      env2)
    
     (if (true? (if-pred env2)) ; (= n 0)
         (if-true env2)   ; 1
         (if-false env2)) ; (* (factorial (- n 1)) n)
    

Here, `n = 2 != 0`, so we'll end up calling executing `(if-false env2)`. `if-false` will do an application of `*` to `(factorial (- n 1))` and `n`, but
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