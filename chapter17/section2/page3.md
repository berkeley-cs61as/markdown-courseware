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

