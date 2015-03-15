##  Question 1

A Logo line can contain more than one instruction:

`? print "a print "b `

`a`

`b`

`?`

This capability is important when an instruction line is given as an argument
to something else:

`? to repeat :num :instr`

`-> if :num=0 [stop]`

`-> run :instr`

`-> repeat :num-1 :instr`

`-> end`

`? repeat 3 [print "hi print "bye]`

`hi`

`bye`

`hi`

`bye`

`hi`

`bye`

`?`

On the other hand, an instruction line used as argument to something might not
contain any complete instructions at all, but rather an expression that
provides a value to a larger computation:

`? print ifelse 2=3 [5*6] [8*9]`

`72`

`?`

In this example, when the IFELSE procedure is invoked, it will turn the list
[8*9] into an instruction line for evaluation. (Note: This example is here to
explain to you why you need to handle an "instruction line" without a complete
instruction. You can't actually type this into your Logo interpreter yet; you
haven't invented infix notation or predicates.)

Logo-eval's job is to evaluate one instruction or expression and return its
value. (An instruction, in which a command is applied to arguments, has no
return value. In our interpreter this is indicated by logo-eval returning the
symbol `=NO-VALUE=` instead of a value.) We need another procedure that
evaluates an entire line, possibly containing several instructions, by
repeatedly invoking logo-eval until either the line is empty (in which case
`=NO-VALUE=` should be returned) or logo-eval returns a value (i.e., a value
other than `=NO-VALUE=`), in which case that value should be returned. You
will write this procedure, called eval-line,like this:

`(define (eval-line line-obj env)`

`...)`

You'll find several invocations of eval-line in the interpreter, most
importantly in driver-loop where each line you type after a ? prompt is
evaluated.

## Question 2

Conditionals. The Logo primitives IF and IFELSE require as argument the word
TRUE or the word FALSE. Of course our implementation of the Logo predicates
will use Scheme predicates, which return #T and #F instead.

Your job is to write the higher-order function LOGO-PRED whose argument is a
Scheme predicate and whose return value is a Logo predicate, i.e., a function
that returns TRUE instead of #T and FALSE instead of #F. This higher-order
function is used in the table of primitives like this:

`(add-prim 'emptyp 1 (logo-pred empty?))`

That is, the Scheme predicate EMPTY? becomes the Logo predicate EMPTYP. (The
"P" at the end of the name stands for "Predicate," by the way. Some versions
of Logo use this convention, while others use ? at the end the way Scheme
does. The educational merits of the two conventions are hotly debated in the
Logo community.)

The spiffiest way to do this is to create a LOGO-PRED that works for predicate
functions of any number of arguments. To do that you have to know how to
create a Scheme function that accepts any number of arguments. You do it with
(lambda args (blah blah)). That is, the formal parameter name ARGS is not
enclosed in parentheses. When the procedure is called, it will accept any
number of actual arguments and they will all be put in a list to which ARGS is
bound. (This is discussed in exercise 2.20.)

Alternatively, I'll accept two procedures LOGO-PRED-1 for predicate functions
of one argument and LOGO-PRED-2 for functions of two arguments, but then
you'll have to fix the add-prim invocations accordingly.

By the way, IF and IFELSE won't work until your group does problem 3 below.
Meanwhile, you should just be able to PRINT the values returned by the
predicates, once you've combined the work of your two people so far.

When you've finished these two steps, you must combine your work with that of
person A. When you've done that, you should be able to run the interpreter and
carry out instructions involving only primitive procedures and constant
(quoted or self-evaluating) data. **You aren't yet ready for variables,
conditionals, or defining procedures, and you can only use prefix arithmetic
operators.**

Try these examples and others:

    
    
    ? print 3 
    3
    ? print sum product 3 4 8
    20
    ? print [this is [a nested] list]
    this is [a nested] list
    ? print 3 print 4
    3
    4
    ? print equalp 4 6
    false
    ?
    

** When you and your partner are done with number 2, combine your code and move on to number 3!**

##  Question 5

Time to define procedures! You are going to write eval-definition, a procedure
that accepts a line-obj as argument. (The corresponding feature in the
metacircular evaluator also needs the environment as an argument, but recall
that in Logo procedures are not part of the environment; they go in a
separate, global list.) The line-obj has just given out the token TO, and is
ready to provide the procedure name and formal parameters. Your job is to read
those, then enter into an interactive loop in which you read Logo lines and
store them in a list, the procedure body. You keep doing this until you see a
line that contains only the word END. You put together a procedure
representation in the form

`(list name 'compound arg-count (cons formals body))`

and you prepend this to the procedure list in the (Scheme) variable the-
procedures. The arg-count is the number of formal parameters you found.
Formals is a list of the formal parameters, without the colons. Body is the
list of instruction lines, not including the END line. Don't turn the lines
into line-objects; that'll happen when the procedure is invoked.

To print the prompt, say (prompt "-> ").

It's going to be a little hard to test the results of your work until you can
invoke user-defined procedures, which requires one more step. Meanwhile you
could leave Logo, and ask Scheme to look at the first element of the-
procedures to see if you've done it right.

** When you are done, combine your work with your partner's question 5 and move on to question 6**

##  Question 8

Add the commands TEST, IFTRUE (abbreviation IFT), and IFFALSE (abbreviation
IFF). These are alternatives to the IF/IFELSE style of conditional evaluation,
provided in Logo because an IFELSE that carries out several conditional
instructions can lead to one very long instruction line, hard to read and hard
to edit. Here's how it works:

The command TEST takes one argument, which must be TRUE or FALSE. It remembers
the value for later, and does nothing else. Note: If TEST is called inside a
procedure, the argument value is remembered locally, but does not modify the
caller's test result (or the global one).

The command IFTRUE takes one argument, an instruction list. If the remembered
TEST value is TRUE, then the instruction list is run. If the remembered value
is FALSE, nothing happens. The command IFFALSE is the same only backwards. It
is an error if IFTRUE or IFFALSE is used before any TEST has been done. Note:
It is *not* an error to use IFTRUE or IFFALSE inside a procedure, before the
procedure does a TEST, provided that a TEST has been done by the caller. That
is, each procedure call inherits its caller's test flag.

Suggestion: Put a variable with an untypeable-in name, such as the string "
TEST", in every frame.

**When your partner is done with question 8 as well, move on to part 9!**

