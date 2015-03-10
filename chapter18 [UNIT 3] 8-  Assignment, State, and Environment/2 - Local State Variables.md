## quick glance

Let's take a quick glance at what we will be going over in this section:

![](http://static.ddmcdn.com/gif/need-bank-account-1.jpg)

    
    (define (make-account balance) 
      (define (withdraw amount) 
        (set! balance (- balance amount)) balance) 
      (define (deposit amount) 
        (set! balance (+ balance amount)) balance) 
      (define (dispatch msg) 
        (cond 
          ((eq? msg 'withdraw) withdraw) 
          ((eq? msg 'deposit) deposit) ) ) 
      dispatch) 
    

What do you think? Any idea about what this function does?

## withdraw

Let's withdraw money from the bank account. We will do this using a procedure
`withdraw`, which takes as argument an amount to be withdrawn. If there is
enough money in the account to accommodate the withdrawal, then `withdraw`
should return the balance remaining after the withdrawal. Otherwise,
`withdraw` should return the message `Insufficient funds`. For example, if we
begin with $100 in the account, we should obtain the following sequence of
responses using `withdraw`:

    
    (withdraw 25)
    75
    (withdraw 25)
    50
    (withdraw 60)
    "Insufficient funds"
    (withdraw 15)
    35
    

Observe that the expression `(withdraw 25)`, evaluated twice, yields different
values.

_Wait, but I thought that a particular function call with the same argument
returns the same value!_

Up to now it has, but this is a new kind of behavior for a procedure. All our
procedures could be viewed as functions that pass the vertical line test. A
call to a procedure computes the value of the function applied to the given
arguments, and two calls to the same procedure with the same arguments always
produces the same result. But in this situation, the balance needs to be
changed after each transaction. Otherwise, we all are going to be rich!

To implement `withdraw`, we can use a variable `balance` to indicate the
balance of money in the account and define `withdraw` as a procedure that
accesses balance. The withdraw procedure checks to see if balance is at least
as large as the requested amount. If so, `withdraw` decrements balance by
amount and returns the new value of balance. Otherwise, `withdraw` returns the
Insufficient funds message. Here are the definitions of `balance` and
`withdraw`:

    
    (define balance 100)
    
    (define (withdraw amount)
      (if (>= balance amount)
          (begin (set! balance (- balance amount))
                 balance)
          "Insufficient funds"))
    

Decrementing balance is accomplished by the expression

`(set! balance (- balance amount))`

This uses the `set!` special form, whose syntax is

`(set! [name] [new-value])`

Here `[name]` is a symbol and `[new-value]` is any expression. `Set!` changes
`[name]` so that its value is the result obtained by evaluating `[new-value]`.
In the case at hand, we are changing balance so that its new value will be the
result of subtracting amount from the previous value of balance.

`Withdraw` also uses the `begin` special form to cause two expressions to be
evaluated in the case where the if test is true: first decrementing `balance`
and then returning the value of `balance`. In general, evaluating the
expression

`(begin [exp1] [exp2] ... [expk])`

causes the expressions `[exp1]` through `[expk]` to be evaluated in sequence
and the value of the final expression `[expk]` to be returned as the value of
the entire `begin` form.

Here's a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Play with `withdraw`, `set!` and `begin`:

## wait, there's something!

Before we move on, examine again how `withdraw` and `balance` are defined:

    
    (define balance 100)
    
    (define (withdraw amount)
      (if (>= balance amount)
          (begin (set! balance (- balance amount))
                 balance)
          "Insufficient funds"))  
    

Do you see anything that could cause a trouble?

## trouble detected

So the problem is with the variable `balance`. As specified above, `balance`
is a name defined in the global environment and is freely accessible to be
examined or modified by any procedure. It would be much better if we could
somehow make `balance` **internal** to `withdraw`, so that `withdraw` would be
the only procedure that could access `balance` directly and any other
procedure could access `balance` only indirectly (through calls to
`withdraw`). This would more accurately model the notion that `balance` is a
**local state variable** used by `withdraw` to keep track of the state of the
account.

We can make `balance` internal to `withdraw` by rewriting the definition as
follows:

    
    (define new-withdraw
      (let ((balance 100))
        (lambda (amount)
          (if (>= balance amount)
              (begin (set! balance (- balance amount))
                     balance)
              "Insufficient funds"))))
    

What we have done here is use `let` to establish an environment with a local
variable `balance`, bound to the initial value 100. Within this local
environment, we use `lambda` to create a procedure that takes `amount` as an
argument and behaves like our previous `withdraw` procedure. This procedure --
returned as the result of evaluating the `let` expression -- is `new-
withdraw`, which behaves in precisely the same way as `withdraw` but whose
variable `balance` is not accessible by any other procedure.

    
    > (new-withdraw 10)
    90
    > (new-withdraw 30)
    60
    

Here's a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Play with `new-withdraw` and make sure you understand
how it works:

## what will scheme output?

Predict the result before you try each example. If you don't understand what
Scheme actually does, ask for help! Don't waste your time by just typing this
in without paying attention to the results.

    
    
    (define (make-adder n)                       ((lambda (x) 
      (lambda (x) (+ x n)))                         (let ((a 3)) 
                                                      (+ x a))) 
    (make-adder 3)                                5) 
     
    ((make-adder 3) 5)                           (define k 
                                                   (let ((a 3)) 
    (define (f x) (make-adder 3))                    (lambda (x) (+ x a)))) 
     
    (f 5)                                        (k 5) 
     
    (define g (make-adder 3))                    (define m 
                                                   (lambda (x) 
    (g 5)                                            (let ((a 3)) 
                                                       (+ x a)))) 
    (define (make-funny-adder n)        
      (lambda (x)                                (m 5) 
        (if (equal? x 'new)             
            (set! n (+ n 1))                     (define p 
            (+ x n))))                             (let ((a 3)) 
                                                     (lambda (x) 
    (define h (make-funny-adder 3))                    (if (equal? x 'new) 
                                                           (set! a (+ a 1)) 
    (define j (make-funny-adder 7))                        (+ x a))))) 
     
    (h 5)                                        (p 5) 
     
    (h 5)                                        (p 5) 
     
    (h 'new)                                     (p 'new) 
     
    (h 5)                                        (p 5) 
     
    (j 5)                                        (define r 
                                                   (lambda (x) 
    (let ((a 3))                                     (let ((a 3)) 
      (+ 5 a))                                         (if (equal? x 'new) 
                                                           (set! a (+ a 1)) 
    (let ((a 3))                                           (+ x a))))) 
      (lambda (x) (+ x a)))             
                                                 (r 5) 
    ((let ((a 3))                       
       (lambda (x) (+ x a)))                     (r 5) 
     5)                                 
                                                 (r 'new) 
     
                                                 (r 5)                 
     
    (define s                                    (define (ask obj msg . args) 
      (let ((a 3))                                 (apply (obj msg) args)) 
        (lambda (msg)                             
          (cond ((equal? msg 'new)               (ask s 'add 5) 
                 (lambda ()                       
                   (set! a (+ a 1))))            (ask s 'new) 
                ((equal? msg 'add)                
                 (lambda (x) (+ x a)))           (ask s 'add 5) 
                (else (error "huh?"))))))         
                                                 (define x 5) 
    (s 'add)                                      
                                                 (let ((x 10) 
    (s 'add 5)                                         (f (lambda (y) (+ x y)))) 
                                                   (f 7)) 
    ((s 'add) 5)                                  
                                                 (define x 5) 
    (s 'new)                                      
     
    ((s 'add) 5)                                  
     
    ((s 'new))                                    
     
    ((s 'add) 5) 
    

## substitution model of evaluation

Introducing assignments accompanies a pretty big cost. At this point, you may
realize that we cannot use the substitution model of evaluation anymore
because it yields the wrong value. The trouble here is that substitution is
based ultimately on the notion that the symbols in our language are
essentially names for values. But as soon as we introduce set! and the idea
that the value of a variable can change, a variable can no longer be simply a
name. Now a variable somehow refers to a place where a value can be stored,
and the value stored at this place can change.

_Then how can I evaluate the procedures?_

The new model of evaluation is waiting for you in the next subsection.

## takeaways

In this section, you learned:

  1. How to implement local state variables
  2. Costs of assignments
  3. How to use `set!` and `begin`

## what's next?

Let's go to the next subsection and learn about the new model of evaluation!

