## Overview

So far the only local state variables we've seen have been instantiation
variables. In this subsection we will look at two other types: instance
variables and class variables.

## Instance Variable

Recall the `checking-account` class:

    
    (define-class (checking-account init-balance)
        (parent (account init-balance))
        (method (write-check amount)
            (ask self 'withdraw (+ amount 0.10)) ))
    

Whenever we write a check, we charged the account with an additional 10 cents.
All `checking-accounts` start with a 10 cent fee, but now we want to be able
to change the fee as we go. One way to do this is to add `check-fee` as an
instantiation variable.

    
    
    (define-class (checking-account init-balance check-fee)
        (parent (account init-balance))
        (method (write-check amount)
            (ask self 'withdraw (+ amount check-fee)) )
        (method (set-fee! fee)
            (set! check-fee fee)) ))
    
    (define lily (instantiate checking-account 1000 0.10))
    (define ted (instantiate checking-account 1000 0.10))
    (define barney (instantiate checking-account 9999 0.10))
    
    

But this format is slightly redundant because we have to specify the `check-
fee` every time, even though we always want it to start at 10 cents. We will
introduce a new clause, **instance-vars** that solves our problems.``

    
    (define-class (checking-account init-balance)
        (parent (account init-balance))
    **    (instance-vars (check-fee 0.10))**
        (method (write-check amount)
            (ask self 'withdraw (+ amount check-fee)))
        (method (set-fee! fee)
            (set! check-fee fee)) )
    

## Instance vs Instantiation variables

Instantiation variables are also instance variables; that is, every instance
has its own private value for them. The only diff erence is in the notation
and when you set the initial value. For instantiation variables you give a
value when you call instantiate, but for other instance variables you give the
value in the class de finition.

## Class Variables

The third kind of local state variable is a class variable. Unlike the case of
instance variables, there is only one value for a class variable for the
entire class. Every instance of the class shares this value. For example,
let's say we want to have a class of `worker`s that are all working on the
same project. That is to say, whenever any of them works, the total amount of
work done is increased. On the other hand, each worker gets hungry separately
as he or she works. Therefore, there is a common `work-done` variable for the
class, and a separate `hunger` variable for each instance.

    
    
    (define-class (worker)
        (instance-vars (hunger 0))
        (class-vars (work-done 0))
        (method (work)
            (set! hunger (+ hunger 1))
            (set! work-done (+ work-done 1))
            'whistle-while-you-work ))  
    
    > (define brian (instantiate worker))
    BRIAN
    > (define matt (instantiate worker))
    MATT
    > (ask matt 'work)
    WHISTLE-WHILE-YOU-WORK
    > (ask matt 'work)
    WHISTLE-WHILE-YOU-WORK
    > (ask matt 'hunger)
    2
    > (ask matt 'work-done)
    2
    > (ask brian 'work)
    WHISTLE-WHILE-YOU-WORK
    > (ask brian 'hunger)
    1
    > (ask brian 'work-done)
    3
    > (ask worker 'work-done)
    3
    

As you can see, asking any `worker` object to work increments the `work-done`
variable. In contrast, each worker has its own `hunger` instance variable, so
that when Brian works, Matt doesn't get hungry. You can ask any instance the
value of a class variable, or you can ask the class itself. This is an
exception to the usual rule that messages must be sent to instances, not to
classes.

## Takeaways

There are three kinds of local state variables: instantiation, instance, and
class.

  * An instantiation variable is specified when you create an object using `instantiate`.
  * An instance variable is a variable that each object has and is independent from each other; changing the value of one doesn't affect the others.
  * A class variable is a variable that is shared with all objects of that class; change the value of a class variable and every object of that class will notice the change.

