## A Preview

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
    

What do you think? Do you have any idea about what this function does?

## Withdraw

Let's withdraw money from the bank account. We will do this using a procedure
`withdraw`, which takes as argument an amount to be withdrawn. If there is
enough money in the account to accommodate the withdrawal, then `withdraw`
should return the balance remaining after the withdrawal. Otherwise,
`withdraw` should return the message `"Insufficient funds"`. For example, if we
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

    (set! balance (- balance amount))

This uses the `set!` special form, whose syntax is

    (set! [name] [new-value])

Here `[name]` is a symbol and `[new-value]` is any expression. `Set!` changes
`[name]` so that its value is the result obtained by evaluating `[new-value]`.
In the case at hand, we are changing balance so that its new value will be the
result of subtracting amount from the previous value of balance.

`Withdraw` also uses the `begin` special form to cause two expressions to be
evaluated in the case where the if test is true: first decrementing `balance`
and then returning the value of `balance`. In general, evaluating the
expression

    (begin [exp1] [exp2] ... [expk])

causes the expressions `[exp1]` through `[expk]` to be evaluated in sequence
and the value of the final expression `[expk]` to be returned as the value of
the entire `begin` form.

Play with `withdraw`, `set!` and `begin` on your STk interpreter!

## Something's Fishy...

Before we move on, examine again how `withdraw` and `balance` are defined:

    
    (define balance 100)
    
    (define (withdraw amount)
      (if (>= balance amount)
          (begin (set! balance (- balance amount))
                 balance)
          "Insufficient funds"))  
    

Do you see anything that could cause a trouble?

## Trouble Detected

The problem is with the variable `balance`. As specified above, `balance`
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
    

Play with `new-withdraw` on the STk interpreter and make sure you understand how it works.

## `make-account`

Here is a simplified version of the `make-account` procedure in SICP:

    (define (make-account balance) 
      (define (withdraw amount) 
        (set! balance (- balance amount)) balance) 
      (define (deposit amount) 
        (set! balance (+ balance amount)) balance) 
      (define (dispatch msg) 
        (cond ((eq? msg 'withdraw) withdraw) 
              ((eq? msg 'deposit) deposit) ) ) 
      dispatch)

Now, let's try to rewrite this using local state variables. Fill in the blank in the following code so that the result works exactly the same as the `make-account` procedure above. That is, it responds to the same messages and produces the same return values. The differences between the two procedures are that the inside of `make-account` above is enclosed in the `let` statement below, and the names of the parameters to `make-account` are different.

    (define (make-account init-amount) 
      (let (______________________) 
        (define (withdraw amount) 
          (set! balance (- balance amount)) balance) 
        (define (deposit amount) 
          (set! balance (+ balance amount)) balance) 
        (define (dispatch msg) 
          (cond ((eq? msg 'withdraw) withdraw) 
                ((eq? msg 'deposit) deposit) ) ) 
        dispatch) )

<div class="mc">
<ans text="Click to view answer." explanation="(balance init-amount)" correct></ans>
</div>

Now, modify either version of make-account so that, given the message balance, it returns the current account balance, and given the message init-balance, it returns the amount with which the account was initially created. For example,

    > (define acc (make-account 100)) 
    acc 
    > (acc 'balance) 
    100

<div class="mc">
<ans text="Click to view answer." explanation="add ((eq? msg 'balance) balance) to the cond statement in the dispatch procedure." correct></ans>
</div>

Make another modification such that, given the message transactions (any deposit or withdrawal), it returns a list of all transactions made since the account was opened. For example:

    > (define acc (make-account 100)) 
    acc 
    > ((acc 'withdraw) 50) 
    50 
    > ((acc 'deposit) 10) 
    60
    > (acc 'balance)
    60
    > (acc 'transactions) 
    ((deposit 10) (withdraw 50))

Before viewing the entire solution below, try out your definition in the STk interpreter and make sure you understand the entire code for `make-account`.

Here is our solution:

    (define (make-account init-amount) 
      (let ((balance init-amount)
            (transactions '())) 
        (define (withdraw amount) 
          (set! balance (- balance amount))
          (set! transactions (cons (list 'withdraw amount) transactions)) 
          balance) 
        (define (deposit amount) 
          (set! balance (+ balance amount))
          (set! transactions (cons (list 'deposit amount) transactions)) 
          balance) 
        (define (dispatch msg) 
          (cond ((eq? msg 'withdraw) withdraw) 
                ((eq? msg 'deposit) deposit)
                ((eq? msg 'balance) balance)
                ((eq? msg 'transactions) transactions) ) ) 
        dispatch) )

## The Substitution Model of Evaluation

Given this definition:

    (define (plus1 var) 
      (set! var (+ var 1)) 
      var)

Follow the [substitution model](http://berkeley-cs61as.github.io/textbook/the-substitution-model-for-procedure-application.html) to find the result of computing

    (plus1 5)

That is, show the expression that results from substituting `5` for `var` in the body of `plus1`, and then compute the value of the resulting expression.

Now, try it in the STk interpreter. Did you get the same answer? Why or why not?

Introducing assignments accompanies a pretty big cost. At this point, you may realize that we cannot use the substitution model of evaluation anymore because it yields the wrong value. The trouble here is that substitution is based ultimately on the notion that the symbols in our language are essentially names for values. But as soon as we introduce `set!` and the idea that the value of a variable can change, a variable can no longer be simply a name. Now a variable somehow refers to a place where a value can be stored, and the value stored at this place can change. 

_Then how can I evaluate the procedures?_

The new model of evaluation is waiting for you in the next subsection.

## Takeaways

In this section, you learned:

  1. How to implement local state variables
  2. Costs of assignments
  3. How to use `set!` and `begin`

## What's Next?

Let's go to the next subsection and learn about the new model of evaluation!