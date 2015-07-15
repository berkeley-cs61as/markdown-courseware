## Message Passing

The way to get things to happen in OOP is to "ask" them to do something for
you. The manner in which we do this is similar to the "message passing" that
we did in Lesson 6. How do we do it in OOP vocabulary?

Let's say we have two objects: **`Matt-Account`** and **`Brian-Account`**,
which are instances of `bank-account` classes. They hold the amount of money
that **Matt** and **Brian** have, respectively. (You can't type this into Scheme just yet! We are going to assume we made the objects previously.)

    
    > (ask Matt-Account 'balance)
    1000
    
    > (ask Brian-Account 'balance)
    10000
    
    > (ask Matt-Account 'deposit 100)
    1100
    
    > (ask Brian-Account 'withdraw 200)
    9800
    
    > (ask Matt-Account 'balance)
    1100
    
    > (ask Brian-Account 'withdraw 200)
    9600
    

## `ask`

We use the **`ask`** procedure to tell objects to carry out a certain action. In
the example above, the bank account objects accepts 3 messages:

  * `balance`
  * `deposit`
  * `withdraw`

For each of the 3 messsages, the bank account objects know what actions need to be carried out. Notice that some messages require additional information:

  * For **balance**, it doesn't need any additional arguments. It returns the amount of money that account has. 

<pre><code>> (ask Matt-Account 'balance)
1000</code></pre>

  * For **deposit** and **withdraw**, we need one more argument to specify the amount we are depositing or withdrawing. 
    
<pre><code>> (ask Matt-Account 'deposit 50000)
51000</code></pre>

The metaphor is that an object "knows how" to do certain tasks. These tasks
are called **methods**.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Suppose we have a bank account for Max, and we enter the following expressions:

<pre><code>(ask max-account 'balance)
1000

(define withdraw 'deposit)</code></pre>

What is returned from the following expression?

<pre><code>(ask max-account 'withdraw 100)</code></pre>

<ans text="1000" explanation=""></ans>
<ans text="900" explanation="we are calling the method 'withdraw that is defined within our bank account class" correct></ans>
<ans text="1100" explanation=""></ans>
<ans text="Error" explanation=""></ans>
<ans text="None of the above" explanation=""></ans>
<!-- and so on -->
<br><br>

What if, INSTEAD of the previous expression, we call this expression:

<pre><code>(ask max-account withdraw 100)</code></pre>

<ans text="1000" explanation=""></ans>
<ans text="900" explanation=""></ans>
<ans text="1100" explanation="Since there is no quote before it, we are not calling the 'withdraw method. Instead, we are calling the method that is stored inside the variable withdraw, which is the method 'deposit." correct></ans>
<ans text="Error" explanation=""></ans>
<ans text="None of the above" explanation=""></ans>
</div>

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

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
We called <code>(ask matt-account 'balance)</code> several times, each with different values. What does this tell us about OOP?
<ans text="It is representative of Functional Programming" explanation=""></ans>
<ans text="It is representative of Non-Functional Programming" explanation="Since we see that making the same calls return different values, this tells us that OOP is non-functional in style." correct></ans>
<ans text="Not enough information" explanation=""></ans>
<!-- and so on -->
<br><br>

Both <code>matt-account</code> and <code>brian-account</code> returns how much money each person has. How does Matt's actions with his account (method calls to <code>matt-account</code>) affect Brian's account?

<ans text="Brian's account changes by the same amount." explanation=""></ans>
<ans text="Brian's account sees no change" explanation="The current methods we have only affect variables unique to each object in a class. Later, we'll observe differences between instance variables and class variables." correct></ans>
</div>

## OOP Paradigm vs. Functional Programming Paradigm

In the first question, we see that Matt's balance changes with each
withdraw and deposit. This feels natural for us because that is how bank
accounts work. But, with the functional programming paradigm that we've been
using so far, we would expect the same call to return the same value.

In the OOP paradigm, the objects have **state**. That is, they have some knowledge about what has happened to them in the past. In this example, a bank account has a balance, which changes when you deposit or withdraw some money.

### Local State Variables

In the second question, we see that although Matt has his 'balance' and
Brian has his 'balance' that never interfere with each other.

In OOP jargon we say that 'balance' is a **local state variable **, or
**instance variable**. An instance variable will have different values for
different instances.

We can draw a parallel here with the definitions for

    
    
    (define (square x)
        (* x x))

and

    
    
    (define (cube x)
        (* x x x))

Both definitions use x, but they are independent.