## Intro

You can imagine that as our program grows larger and larger in OOP, you will define more objects and classes. Some of the classes will share similar characteristics. For example, you might have a `box` class, a `safety-deposit-box` class, and a `locked-box` class. They all need to know similar methods like adding items to it and removing items from it. It will be redundant to recode it for every single box-like class. What we want is to define a generic class (like a `box` class) that knows the general methods like `open`ing and then let the more specific classes (like the `safe-deposit-box` class) **inherit** from the general `box` class.

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

<pre><code>(define-class (checking-account init-balance)
    <strong>(parent (account init-balance))</strong>
    (method (write-check amount)
        (ask self 'withdraw (+ amount 0.10)) ))</code></pre>
    

This example introduces the parent clause in `define-class`. In this case, the
parent is the `account` class. Note that because the `account` class needs one
instantiation variable, we need to provide that argument as well (hence the
`(account init-balance)`).

Whenever we send a message to a `checking-account` object, where does the
corresponding method come from? If a method of that name is defined in the
`checking-account` class, it is used; otherwise, the OOP system looks for a
method in the parent account class. If the parent doesn't have that method, we
will look at the parent's parent, and so on.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
These questions follow our class definitions for <code>account</code> and <code>checking-account</code> above.

<pre><code>(define sam (instantiate checking-account 500))</code></pre>

Which one of these will return an error?
<ans text="(ask sam 'init-balance)" explanation=""></ans>
<ans text="(ask sam 'balance)" explanation=""></ans>
<ans text="(ask sam 'withdraw 200)" explanation=""></ans>
<ans text="(ask sam 'deposit 200)" explanation=""></ans>
<ans text="(ask sam 'write-check 50)" explanation=""></ans>
<ans text="None of the above" explanation="init-balance will be fine because we have an instantiation variable called init-balance. We get a method for that for free.

balance, withdraw, and deposit are fine because although the class checking-account doesn't have a method for balance, its parent does.

write-check is a method specifically defined for checking-account." correct></ans>
<!-- and so on -->
</div>

## The 'self' Keyword

What should `write-check` do? It should reduce the account's balance by the specified amount and additional fee. We already know how to reduce our balance, it's just the `withdraw` method! To call a method that we already defined from the body of another method, we use the **self**, hence the `(ask self 'withdraw (+ amount 0.10))`. Each object has a local state variable `self` whose value is the object itself.

## Scope

Methods defined in a certain class only have access to the local state variables de fined in the same class. For example, a method de fined in the `checking-account` class can't refer to the `balance` variable de fined in the `account` class; likewise, a method in the `account` class can't refer to the `init-balance` variable. 

This rule corresponds to the usual Scheme rule about scope of variables: each variable is only available within the block in which it's defi ned. (Not every OOP implementation works like this, by the way.) 

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Classes are wonderful! They keep objects organized. Inheritance is wonderful! They keep classes organized. Be aware about the states that a child has and which ones are updated.

<pre><code>>(define nick (instantiate checking-account 500))
>(ask nick 'init-balance)
500
>(ask nick 'balance)
500
>(ask nick 'deposit 50)
550</code></pre>

What does the following expression return?

<pre><code>(ask nick 'balance)</code></pre>
<ans text="Click to view answer." explanation="550. nick is an instance of a checking-account. Its parent knows how to 'deposit' and will update the balance by 50" correct></ans>
<!-- and so on -->
<br><br>

What does the following expression return?

<pre><code>(ask nick 'init-balance)</code></pre>

<ans text="Click to view answer." explanation="500. The 'deposit' changes 'balance' and not 'init-balance' therefore, since all of the methods in account class changes balance and not init-balance, init-balance will always stay the same." correct></ans>
<br><br>

Suppose we now have the following snippet of code:

<pre><code>(define-class (checking-account init-balance)
    (parent (account init-balance)) 
    (method (write-check amount)
        (ask self 'withdraw (+ amount 0.10)) )
    (method (show-balance) balance)  )
    
(define jeffrey (instantiate checking-account 500))</code></pre>

We added a new method, show-balance to the class. What will (ask jeffrey 'show-balance) return?

<ans text="2000" explanation=""></ans>
<ans text="1000" explanation=""></ans>
<ans text="500" explanation=""></ans>
<ans text="Error" explanation="You have to use (ask self 'balance) and not just balance" correct></ans>
</div>

## Takeaways

Several takeaways from this subsection:

  * Some classes will be a more 'specialized' or 'specific' version of another class. In these cases, we want to make the specific class a 'child' of the 'parent' class.
  * A child class inherits all methods of the parent class.
  * Keep track of what variable is actually in scope in your class.

## What's Next?

We are going to learn what kinds of variables a class can have.

