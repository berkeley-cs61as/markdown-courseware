## Overview

In this subsection, we are going to play around with a calculator program that
is written in Racket.

Our calculator program will do arithmetic operations in the same syntax as
Racket. Why are we doing this? We want to increase our understanding on how
Racket evaluates things. In the next lab, we will add more features to it but
for now, all it does is arithmetic operations.

You can download the file from
[here](http://inst.eecs.berkeley.edu/~cs61as/library/calc.rkt). You can also
copy it to your class account by typing the following into a terminal:

`cp ~cs61as/lib/calc.rkt .`

Note the '.' at the end. This will copy the .rkt file to your current
directory.

## The 'READ' function

Before we dive in to the calculator, there is one function we should know: the
`read` function. When you call `(read)`, it will prompt you for some input.

    
    
    > (read)
    123
    123
    

In the example above, we entered `123` into the interpreter. The next `123` shown by the interpreter is the value returned by `read`. So what is it used for? Try this:

    
    
    > (define a (read))
    123
    a
    > a
    123
    

Here, we are assigning `a` to the value of your input. Thus, when we type
`123` again, we store that value in the variable `a`. Try the next one for
something more interesting:

    
    
    > (define a (read))
    (+ 1 2)
    a
    > a
    (+ 1 2)
    > (equal? a '(+ 1 2))
    #t
    

This time, when the interpreter asked us what value we want to put into `a`, we
typed `'(+ 1 2)'`. `a` ended up with the value `'(+ 1 2)'` and NOT 3. The next
line tests whether `a` is equal to the quoted list `'(+ 1 2)'`. What can we
learn from this? **`(read)` accepts user inputs as symbols; they are not
evaluated.**

With that covered, let's go to the Calculator program!

## Calc: How Does it Work?

Let's run the program and walk through what is actually happening. Load
`calc.rkt` in your Racket interpreter (by typing `(enter! 'calc.rkt')`), then call the function `(calc)`:

    
    
    > (calc)
    calc:
    

Notice that our usual prompt ">" is replaced with "calc:". This is an easy way
to know that the expressions you enter which will be evaluated by `calc.rkt`.
Now, try typing some arithmetic operation like `(+ 10 20)`, or some number like `300`, and play around with it!

How does it know how to evaluate math operations? Let's look at what the
`calc` function does. Its definition is reproduced below:

    
    
    (define (calc)
      (display "calc: ")
      (flush)
      (print (calc-eval (read)))
      (calc))
    

The first line says `(display "calc: ")`, which tells the interpreter to show
"calc: " to the 'screen'/output. 

`flush` tells the interpreter to show whatever we type on the 'screen' output (you can ignore this for now). 

The next line, `(print (calc-eval (read)))` tells the interpreter to call `calc-eval` with the user input and print the result. 

The last line is a recursive call to `calc`, which loops us back to the beginning. This is the **read-eval-print-loop (REPL)**: it asks for some user-input, evaluates it, prints the result, and loops. 

This is all that `calc` does. The calculator magic happens in `calc-eval`.

## Calc: Number Inputs

So what does `calc-eval` do? Consider a situation where we type a number in
`calc` as follows:

    
    calc: 42
    42

That wasn't a very exciting result, but under the hood, a lot of things are
interacting. Because the user input is 42, the `calc-eval` will be called as
`(print (calc-eval '42))`. (Remember that `(read)` returns a quoted symbol.)
Let's see how `calc-eval` handles this. Its code is reproduced below.

    
    (define (calc-eval exp)
        (cond ((number? exp) exp)
              ((list? exp) 
               (calc-apply (car exp)
                           (map calc-eval (cdr exp))))
              (else (error "Calc: bad expression:" exp))))
    

`calc-eval`'s body is a `cond`, and because the formal parameter `exp` is
called with 42, the first condition `(number? exp)` will be fulfilled and
`calc-eval` will return `exp`, which is 42. All numbers are treated the same way. A subtle point here is that this is the base-case. For any arithmetic calculation, the simplest argument that can be passed around are numbers.

## Calc: One Operator

The next expression we are going to try is a single operator function call,
like `(+ 1 1)`, `(* 2 3 10)`, or `(- 100 50 20 10)`.

    
    
    calc: (* 2 3 10)
    

This will call `calc-eval` as `(print (calc-eval '(* 2 3 10)))`. (Again,
remember that `read` treats user input as symbols.) How does `calc-eval`
handle this?
    
<div class="mc">
<strong>Test Your Understanding</strong><br><br>
The calc-eval code has be reproduced for you below:
<pre><code>(define (calc-eval exp)
  (cond ((number? exp) exp)
        ((list? exp)
         (calc-apply (car exp)
                     (map calc-eval (cdr exp))))
        (else (error "Calc: bad expression:" exp))))
</code></pre>

What happens when we call the following expression:

<pre><code>(calc-eval '(* 2 3 10))
</code></pre>
<ans text="It returns 60 without calling other compound procedures" explanation=""></ans>
<ans text="It returns '(* 2 3 10)" explanation=""></ans>
<ans text="It calls (calc-apply '(* 2 3 10))" explanation=""></ans>
<ans text="It calls (calc-apply '* '(2 3 10))" explanation="exp is '(* 2 3 10). It's definitely not a number, so it doesn't pass the first condition. It passes the second condition because it is a list. Its car is '* and its cdr is '(2 3 10). It will therefore call (calc-apply '* (map calc-eval '(2 3 10)))" correct></ans>
<ans text="It errors" explanation=""></ans>
<!-- and so on -->
</div>   

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
`'+`, `'-`, `'*`, or `'/`. Everything else results in an error. `Calc-apply` can be described as "find what function it is and do the right thing". In this case,
because `fn` is `'*`, `calc-apply` will call `accumulate` on `args`, which is `'(2 3 10)`, and return `60`.

Convince yourself that for any of the 4 acceptable arguments for `fn`, and any
list of numbers `args`, `calc-apply` will do the right computation.

## Calc: Nested Operators
    
<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Let's test our calculator program by calling a more complex expression. The calc-eval code has be reproduced for you below:
<pre><code>(define (calc-eval exp)
  (cond ((number? exp) exp)
        ((list? exp)
         (calc-apply (car exp)
                     (map calc-eval (cdr exp))))
        (else (error "Calc: bad expression:" exp))))
</code></pre>

What happens when we call the following expression:

<pre><code>(calc-eval '(+ 4 5 (* 10 2) 7))
</code></pre>
<ans text="It returns 36 without calling other compound procedures" explanation=""></ans>
<ans text="It returns '(+ 4 5 20 7)" explanation=""></ans>
<ans text="It calls (calc-apply '(+ 4 5 20 7))" explanation=""></ans>
<ans text="It calls (calc-apply '+ '(4 5 (* 10 2) 7))" explanation=""></ans>
<ans text="It calls (calc-apply '+ '(4 5 20 7))" explanation="Again, exp is a list, with car '+ and cdr '(4 5 (* 10 2) 7). We then evaluate (map calc-eval '(4 5 (* 10 2) 7)). We know that calling calc-eval on a number returns that number. What happens when we call (calc-eval (* 10 2))? We recursively evaluate an expression! This time it is a simpler expression with just a single operator. This is where numbers as a base case comes in." correct></ans>
<ans text="It errors" explanation=""></ans>
<!-- and so on -->
</div>    

## Compound Expressions

So how does our calculator program evaluate compound expressions? It calls
`calc-eval` on simpler expressions, and recursively repeats this until the
expressions are simple enough (just numbers) to simply return the expression. We know that `calc-eval` and `calc-apply` works for numbers and expressions with one operator. Everything else is just a combination. Trust the recursion!

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Which of the following is NOT a possible call in calc?

<ans text="(calc-apply '+ '())" explanation=""></ans>
<ans text="(calc-apply '+ '(1 2 (+ 3 4)))" explanation="The first option is possible. When you call + with no arguments, it would return 0.

This option is not possible, because the second argument is always mapped with calc-eval. You will never have un-evaluated expressions; it should be '(1 2 7) instead." correct></ans>
<!-- and so on -->
</div>

## Takeaways

In this subsection, you learned about `calc.rkt`, which accepts an arithmetic expression (operation) as a symbol and evaluates it like a simplified scientific calculator.

