## Defining Procedures

You already know how to define simple procedures such as `square`. The
standard way to define a procedure is `(define (name formal-parameters)
body)`.

Vocab:

    * Compound Procedure: a compound procedure is a procedure that is defined in terms of Scheme primitive procedures.
    * Name: the name of the procedure is a symbol used to refer to the procedure.
    * Formal Parameters: the formal parameters of a procedure are the names used within the body of the procedure to refer to the arguments.
    * Body: the body of the procedure is the "meat" of the procedure. It is formally defined as "an expression that will yield the value of the procedure application when the formal parameters are replaced by the actual arguments to which the procedure is applied", but you can think of it as instructions for the computer to follow.

In the procedure definition `(define (square x) (* x x))`, the _name_ is
`square`, the _formal parameter_ is `x`, and the _body_ is `(* x x)`.

## Procedures with More than One Formal Parameters

Procedures don't have to have just one formal parameter, such as in `square`.
They can also have multiple formal parameters. The way to create procedures
with multiple arguments is fairly straightforward. It looks something like
this: `(define (foo x y z) (* x y z))`.

We can also create procedures with no arguments at all! The code for that
looks something like this: `(define (foo) 3))`. Now, whenever you call
`(foo)`, it will return 3.

## Procedure-Ception

One of the most useful (and coolest!) parts about programming is that, once
you've defined a procedure, not only can you can use it over and over again,
you can also use it to define other procedures.

Since you're probably sick of `square` right now, let's use another function
as an example. Let's define a predicate `vowel?`, and use it to define another
procedure:

`(define (vowel? letter) (member? letter '(a e i o u))`

Now that we have `vowel?`, we can use it in different procedures. For example,
one of the problems in 0.3 deals with Pig Latin. If a word starts with a
vowel, translating that word into Pig Latin is as simple as adding "ay" to the
end of the word. We're not going to worry about translating words into Pig
Latin right now, we're just going to define yet another predicate to check if
a word starts with a vowel.

`(define (pig-complete? wd) (vowel? (first wd)))`

As you can see, we used one user-defined procedure (`vowel?`), to define
another one.

