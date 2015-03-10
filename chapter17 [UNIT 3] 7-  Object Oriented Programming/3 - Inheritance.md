## Intro

You can imagine that as our program grows larger and larger in OOP, you will
define more objects and classes. Some of the classes will share similar
characteristics. For example you might have a `box` class, a `safe-deposit-
box` class, and a `locked-box` class. They all need to know similar methods
like adding items to it and removing items from it. It will be redundant to
recode it for every single box-like class. What we want is to define a generic
class (like `box` class) that knows the general methods like `open`ing and
then let the more specific classes (like `safe-deposit-box` class) **inherit**
from the general class.

## Parents and Children

Let's say we want to create a `checking-account` class. Checking accounts are
just like regular bank accounts, except that you can write checks as well as
withdrawing money in person. But you're charged ten cents every time you write
a check.

    
    
    > (define Hal-Account (instantiate checking-account 1000))
    Hal-Account
    > (ask Hal-Account 'balance)
    1000
    > (ask Hal-Account 'deposit 100)
    1100
    > (ask Hal-Account 'withdraw 50)
    1050
    > (ask Hal-Account 'write-check 30)
    1019.9
    

One way to implement a `checking-account` is to copy all of the code we have
for the `account` class but then if we need to make a change in our `account`
then we need to remember to change our `checking-account.`

It is very common in object-oriented programming that one class will be a
specialization of another: the new class will have all the methods of the old,
plus some extras, just as in this bank account example. To describe this
situation we use the metaphor of a family of object classes. The original
class is the parent and the specialized version is the child class. We say
that the child inherits the methods of the parent. (The names subclass for
child and superclass for parent are also sometimes used.)

## Parents

Here's how we create a subclass of the account class:

    
    
    (define-class (checking-account init-balance)
    **    (parent (account init-balance))**
        (method (write-check amount)
            (ask self 'withdraw (+ amount 0.10)) ))
    

This example introduces the parent clause in `define-class`. In this case, the
parent is the `account` class. Note that because the `accoun`t class needs 1
instantiation variable, we need to provide that argument as well (hence the
`(account init-balance)`).

Whenever we send a message to a `checking-account` object, where does the
corresponding method come from? If a method of that name is defi ned in the
`checking-account` class, it is used; otherwise, the OOP system looks for a
method in the parent account class. If the parent doesn't have that method, we
will look at the parent's parent, and so on.

## The 'self' Keyword

What should `write-check` do? It should reduce the account's balance by the
specified amount and additional fee. We already know how to reduce our
balance, it's just the `withdraw` method! To call a method that we already
defined from the body of another method, we use the **self**, hence the `(ask
self 'withdraw (+ amount 0.10))`. Each ob ject has a local state variable
`self` whose value is the object itself.

## Scope

Methods defi ned in a certain class only have access to the local state
variables de fined in the same class. For example, a method de fined in the
`checking-account` class can't refer to the `balance` variable de fined in the
`account` class; likewise, a method in the `account` class can't refer to the
`init-balance` variable.

This rule corresponds to the usual Scheme rule about scope of variables: each
variable is only available within the block in which it's defi ned. (Not every
OOP implementation works like this, by the way.)

## Takeaways

Several takeaways from this subsection:

  * Some classes will be a more 'specialized' or 'specific' version of another class. In these cases, we want to make the specific class a 'child' of the 'parent' class.
  * A child class inherits all methods of the parent class.
  * Keep track of what variable is actually in scope in your class.

## what's next?

We are going to learn what kinds of variables a class can have.

