## overview

In this subsection, we are going to play around with a calculator program that
is written in Scheme.

Our calculator program will do arithmetic operations in the same syntax as
Scheme. Why are we doing this? We want to increase our understanding on how
Scheme evaluates things. In the next lab, we will add more features to it but
for now, all it does is arithmetic operations.

You can download the file from
[here](http://inst.eecs.berkeley.edu/~cs61as/library/calc.scm). You can also
copy it to your class account by typing the following into a terminal:

`cp ~cs61as/lib/calc.scm .`

Note the '.' at the end. This will copy the .scm file to your current
directory.

## The 'READ' function

Before we dive in to the calculator, there is one function we should know, the
`read` function. When you call `(read)` it will ask you to type some value.

    
    
    > (read)
    123
    123
    

Try calling `read` like above. Scheme will ask you to type some input (in this
case I typed `'123'` hence the second line). The next `'123'` shown by the
interpreter is the value returned by `read`. So what is it used for? Try this:

    
    
    > (define a (read))
    123
    a
    > a
    123
    

Here, we are assigning '`a'` to some value that a user input. Here I typed
`'123'` again, so that is what is stored in `a`. Try the next one for
something more interesting:

    
    
    > (define a (read))
    (+ 1 2)
    a
    > a
    (+ 1 2)
    > (equal? a '(+ 1 2))
    #t
    

Here, when the interpreter asked us what value we want to put into `a`, we
typed `'(+ 1 2)'`. `a` ended up with the value `'(+ 1 2)'` and NOT 3. The next
line tests whether `a` is equal to the quoted list `'(+ 1 2)'`. What can we
learn from this? `(read)` accepts user inputs as **symbols**; they are **not
evaluated.**

With that covered, let's go to the Calculator program!

## Calc: How Does it Work?

Let's run the program and walk through what is actually happening. Load
`calc.scm` in a scheme interpreter, and call the function `(calc)`

    
    
    > (calc)
    calc:
    

Notice that our usual prompt ">" is replaced with "calc:". This is an easy way
to know that your typing expressions which will be evaluated by `calc.scm`.
Now, try typing some arithmetic operation like `(+ 10 20), `some number like`
300,` and play around with it!

How does it know how to evaluate math operations? Let's look at what the
`calc` function does. Its definition is reproduced below:

    
    
    (define (calc)
      (display "calc: ")
      (flush)
      (print (calc-eval (read)))
      (calc))
    

The first line says `(display "calc: ")` which tells the interpreter to show
"calc: " to the 'screen'/output. `flush` tells the interpreter to show
whatever we type on the 'screen' output (you can ignore this for now). The
next line, `(print (calc-eval (read)))` tells the interpreter to call `calc-
eval` with a user-input and print the result. The last line is a recursive
call to `calc`, which loops us back to the beginning. This is the read-eval-
print-loop (REPL); it asks for some user-input, evaluates it, prints the
result, and loops. This is all that `calc` does. The calculator magic happens
in `calc-eval.`

## Calc: Number Inputs

So what does `calc-eval` do? Consider a situation where we type a number in
`calc` as follows:

    
    calc: 42
    42

That wasn't a very exciting result, but under the hood a lot of things are
interacting. Because the user input is 42, the `calc-eval` will be called as
`(print (calc-eval '42))` (remember that `(read)` returns a quoted symbol).
Let's see how `calc-eval` handles this. Its code is reproduced below.

    
    (define (calc-eval exp)
        (cond ((number? exp) exp)
              ((list? exp) 
               (calc-apply (car exp)
                           (map calc-eval (cdr exp))))
              (else (error "Calc: bad expression:" exp))))
    

`calc-eval`'s body is a `cond` and because the formal parameter `exp` is
called with 42, the first condition `(number? exp)` will be fulfilled and
return `exp`, which is 42. All numbers are treated the same way. A subtle
point here is that this is the base-case. For any arithmetic calculation, the
simplest argument that can be passed around are numbers.

## Calc: One Operator

The next expression we are going to try is a single operator function call,
like `(+ 1 1)`, `(* 2 3 10)`, `(- 100 50 20 10)`

    
    
    calc:(* 2 3 10)
    

This will call `calc-eval` as `(print (calc-eval '(* 2 3 10))) `(Again,
remember that `read` treats user-input as symbols.) How does `calc-eval`
handle this?

    
    
    (define (calc-eval exp)
      (cond ((number? exp) exp)
            ((list? exp)
             (calc-apply (car exp)
                         (map calc-eval (cdr exp))))
            (else (error "Calc: bad expression:" exp))))
    

## Calc-Apply

Our simple expression (* 2 3 10) to `calc` gets passed in to `calc-apply` as
`(calc-apply '* '(2 3 10))`. What does it do next? Here is the code for calc-
apply:

    
    
    (define (calc-apply fn args)
      (cond ((eq? fn '+) (accumulate + 0 args))
            ((eq? fn '-) (cond ((null? args) (error "Calc: no args to -"))
                               ((= (length args) 1) (- (car args)))
                               (else (- (car args) (accumulate + 0 (cdr args))))))
            ((eq? fn '*) (accumulate * 1 args))
            ((eq? fn '/) (cond ((null? args) (error "Calc: no args to /"))
                               ((= (length args) 1) (/ (car args)))
                               (else (/ (car args) (accumulate * 1 (cdr args))))))
            (else (error "Calc: bad operator:" fn))))
    

Notice that the formal argument `fn` in `calc-apply` only accepts 4 values:
'+, '-, '*, '/. Everything else results in an error. `Calc-apply` can be
described as "find what function it is and do the right thing". In this case
because fn is '*, `calc-apply` will call accumulate on args, which is `'(2 3
10) `and returns` 60.`

Convince yourself that for any of the 4 acceptable arguments for `fn`, and any
list of numbers `args`, `calc-apply` will do the right computation.

## Calc: Nested Operators

Let's test our calculator program to the limit by calling something very
complex, like the nested operations `(+ 4 5 (* 10 2) 7)`.

    
    
    calc:(+ 4 5 (* 10 2) 7)
    

## Compound Expressions

So how does our calculator program evaluates compound expressions? It calls
`calc-eval` on simpler expressions, and recursively repeats this until the
expressions are simple enough (just numbers). We know that `calc-eval` and
`calc-apply` works for numbers, and expressions with one operators. Everything
else is just a combination. Trust the recursion!

## takeaways

In this subsection, you learned about `calc.scm`, which accepts an expression
(operation) as a symbol.

