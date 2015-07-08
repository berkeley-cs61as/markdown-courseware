To create an object in OOP, you need to **instantiate** a class. `matt-account` and `brian-account` are part of an "account" **class**.

    
    
    > (define Matt-Account (instantiate account 1000))
    Matt-Account
    
    > (define Brian-Account (instantiate account 10000))
    Brian-Account
    

The `instantiate` function takes a class as its first argument and returns a new
object of that class. `instantiate` may require additional arguments depending
on the particular class: in this example, you must specify an account's initial
balance when you create it.

## Defining a Class

Most of the code in an object-oriented program consists of definitions of
various classes. A class can be treated as a blueprint for a certain kind of
object: "What should objects of these type be able to do? What variables
should each of them know?". Below is the definition of account class. We will
implement only one method right now and add on to it later. There is a lot to
say about this code and we will explain them one by one.

    
    
    (define-class (account balance) ;; define a class called account
        (method (deposit amount) 
            ;; objects of this class will have one method called deposit
            (set! balance (+ amount balance))
            balance)
            ;; deposit sets the balance the the current value plus the deposit amount and then returns the new balance
            )
    

## `define-class`

There's a new special form, define-class. The syntax of define-class is
analogous to that of define. Where you would expect to see the name of the
procedure you're defi ning comes the name of the class you're defi ning. In
place of the parameters to a procedure come the initialization variables of
the class: these are local state variables whose initial values must be given
as the extra arguments to instantiate. In the example below, the
initialization variable "balance" is set to 1000.

    
    (define Matt-Account (instantiate account 1000))

The body of a class consists of any number of clauses; in this example there
is only one kind of clause, the method clause, but we'll learn about others
later.

## Method

The syntax for defi ning methods was also chosen to resemble that of de fining
procedures. The "name" of the method is actually the message used to access
the method. When we say `(ask matt-account 'deposit 50)`, we are essentially
saying "In `matt-account`, find the method with the name 'deposit and call
that method with argument 50". In other words, `matt-account` will call
`(deposit 50)` .

With the class definition we have now, we can actually do `(ask matt-account
'balance)`. Some might say: "But we did not have any method definition for
balance yet!" That is true, but the above code still works. For each local
state variable in a class, a corresponding method of the same name is de fined
automatically. These methods have no arguments, and they just return the
current value of the variable with that name. Because we have state variable
`balance` when we instantiate `matt-account`, we have a method of the same
name 'balance for free. This is one way we can create  a `state;` we will see
an alternative for this later.

## SET!

In the body of `deposit`, we've introduced a new procedure, `set!` This
procedure changes the value of a state variable. Its first argument is
unevaluated; it is the name of the variable whose value you wish to change.
The second argument is evaluated; the value of this expression becomes the new
value of the variable. set! changes the value of a variable, but does not
return anything.

    
    > (define a 3)
    a
    
    > a
    3
    
    > (set! a (+ 2 4))
    okay ; What Scheme prints when nothing is returned
    
    > a
    6
    
    > (set! a (+ a a))
    okay  
      
    > a  
    12 

The "!" in "set!" is a convention in Scheme for functions that mutate
something (just like the convention that procedures ending in "?" return #t or
#f).

## Defining 'Withdraw' Methods

We defined the `deposit` method, now lets see how we define more, specifically
the `withdraw` method. Note that the order in which these methods appear don't
matter.

    
    
    (define-class (account balance)
        (method (deposit amount)
            (set! balance (+ amount balance))
            balance)  
    
        (method (withdraw amount)
            (if (< balance amount)
                "Insufficient Fund"
                (begin 
                  (set! balance (- balance amount))
                  balance)))
    

Again, `withdraw` is a method that takes in 1 argument called 'amount'. If
there is not enough money in `balance` return "Insufficient Fund", otherwise
reduce `balance` by `amount` and return the remaining `balance`. We are using
a new special form, `begin`. What does it actually do?

## Where Should I Begin?

Imagine if we **don't** use the `begin` special-form. What do you think will
happen?

    
    
    (if (< balance amount)
        "Insufficient Fund"
        (set! balance (- balance amount))
        balance)
    

`If` only accepts 3 arguments; a condition, then-case, and else-case. If we
don't use `begin`, we will have 4 arguments and the interpreter will throw an
error. Until now, in every procedure we've evaluated only one expression, to
provide the return value of that procedure. It's still the case that a
procedure can only return one value. Now, though, we sometimes want to
evaluate an expression for what it does instead of what it returns, e.g.
changing the value of a variable. The call to `begin` indicates that the
`(set! amount (- amount balance))` and the `balance` together form a single
argument to if.

## Takeaways

Several takeaways from this subsection:

  * In OOP, we work with objects: smart data that know what values they have and what functions they can do.
  * Objects have states: knowledge on what has happened to them in the past.
  * Every object is a part of a certain class.
  * A class can have many methods. The order in which they are defined doesn't matter.

## what's next?

Can a class inherit from another class? We will see in the next subsection.

