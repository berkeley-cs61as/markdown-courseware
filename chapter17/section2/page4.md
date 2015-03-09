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

