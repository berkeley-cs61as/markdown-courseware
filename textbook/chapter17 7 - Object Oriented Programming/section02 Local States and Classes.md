## Message Passing

The way to get things to happen in OOP is to 'ask' them to do something for
you. The manner in which we do this is similar to the "message passing" that
we did in Lesson 6. How do we do it in OOP vocabulary?

Let's say we have two objects; **`Matt-Account`** and **`Brian-Account`**
which are instances of bank-account classes. They hold the amount of money
that Matt and Brian have, respectively. (You can't type this into Scheme just
yet! we are going to assume we made the objects previously)

    
    >(ask Matt-Account 'balance)
    1000
    
    >(ask Brian-Account 'balance)
    10000
    
    >(ask Matt-Account 'deposit 100)
    1100
    
    >(ask Brian-Account 'withdraw 200)
    9800
    
    >(ask Matt-Account 'balance)
    1100
    
    >(ask Brian-Account 'withdraw 200)
    9600
    

## "Ask"

We use the **ask** procedure to tell objects to carry out a certain action. In
the example above, the bank account objects accepts 3 messages:
**balance,deposit, and withdraw**. For each of the 3 messsages, the bank
account objects know what actions need to be carried out. Notice that some
messages require additional information:

  * For **balance**, it doesn't need any additional arguments. It returns the amount of money that account has. 
    
    (ask Matt-Account 'balance)

  * For **deposit** and **withdraw**, we need one more argument to specify how much we are depositing or withdrawing. 
    
    (ask Matt-Account 'deposit 50000)

The metaphor is that an object "knows how" to do certain tasks. These tasks
are called **methods.**

## States

Consider these calls:

    
    
    > (ask matt-account 'balance)
    500
      
    > (ask brian-account 'balance)  
    9999  
    
    > (ask matt-account 'deposit 500)
    1000
    
    > (ask matt-account 'balance)
    1000
    
    > (ask matt-account 'withdraw 200)
    800
    
    > (ask matt-account 'balance)
    800  
      
    > (ask brian-account 'balance)  
    9999

## States

1) In the first question, we see that Matt's balance changes with each
withdraw and deposit. This feels natural for us because that is how bank
accounts work. But with the functional programming paradigm that we've been
seing so far, we would expect the same call to return the same value.

In the OOP paradigm, the objects have state. That is, they have some knowledge
about what has happened to them in the past. In this example, a bank account
has a balance, which changes when you deposit or withdraw some money.

2) In the second question, we see that although Matt has his 'balance' and
Brian has his 'balance' that never interfere with each other.

In OOP jargon we say that 'balance' is a **local state variable ** or
**Instance variable**. An instance variable will have different values for
different instances.

We can draw a parallel here with the definitions for

    
    
    (define (square x)
        (* x x))

and

    
    
    (define (cube x)
        (* x x x))

Both definitions use x, but they are independent.

## Classes

To create an object in OOP, you need to **instantiate** a class. `matt-
account` and `brian-account` are part of an "account" **class**.

    
    
    > (define Matt-Account (instantiate account 1000))
    Matt-Account
    
    > (define Brian-Account (instantiate account 10000))
    Brian-Account
    

The instantiate function takes a class as its first argument and returns a new
object of that class. Instantiate may require additional arguments depending
on the particular class: in this example you specify an account's initial
balance when you create it.

## Defining a Class

Most of the code in an object-oriented program consists of de nitions of
various classes. A class can be treated as a blueprint for a certain kind of
object: "What should objects of these type be able to do? What variables
should each of them know?". Below is the definition of account class. We will
implement only one method right now and add on to it later. There is a lot to
say about this code and we will explain them one by one.

    
    
    (define-class (account balance)
        (method (deposit amount)
            (set! balance (+ amount balance))
            balance))
    

## define-class

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

