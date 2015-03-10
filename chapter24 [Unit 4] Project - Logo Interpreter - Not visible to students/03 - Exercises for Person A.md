##  Question 1

As explained above, EVAL can't be given a single complete expression as its
argument, because expressions need not be delimited by parentheses and so it's
hard to tell where an expression ends. Instead, EVAL must read through the
line, one element at a time, to figure out how to group things. LOGO-READ,
you'll recall, gives us a Logo instruction line in the form of a list. Each
element of the list is a "token" (a symbol, a number, a punctuation character,
etc.) and EVAL reads them one by one. You might imagine that EVAL would accept
this list as its argument and would get to the next token by CDRing down, like
this:

`(define (eval-prefix line-list env)`

` ... `

`(let ((token (car line-list)))`

`...`

`(set! line-list (cdr line-list))`

`...) `

` ...) `

but in fact this won't quite work because of the recursive invocation of eval-
prefix to evaluate subexpressions. Consider a line like

`print sum (product 2 3) 4`

One invocation of eval-prefix would be given the list

` (sum ( product 2 3 ) 4) `

as argument. It would cheerfully cdr down its local line-list variable, until
it got to the word "product"; at that point, another invocation of eval-prefix
would be given the ENTIRE REMAINING LIST as its argument (since we don't know
in advance how much of that list is part of the subexpression). When the inner
eval-prefix finishes, the outer one still needs to read another argument
expression, but it has no way of knowing how much of the list was read by the
inner one.

Our solution is to invent a LINE-OBJECT data type. This object will be used as
the argument to logo-eval, which in turn uses it as argument to eval-prefix;
the line-object will remember, in its local state, how much of the line has
been read. The very same line-object will be the argument to the inner eval-
prefix. When that finishes, the line object (still available to the outer
invocation of eval-prefix) has already dispensed some tokens and knows which
tokens remain to be processed.

Your job is to define the LINE-OBJECT class. It has one instantiation
variable, a list containing the text of a line. Objects in the class should
accept these messages:

`(ask line-obj 'empty?)`

should return #T if there is nothing left to read in the line-list, #F if
there are still tokens unread.

`(ask line-obj 'next)`

should return the next token waiting to be read in the line, and remove that
token from the list.

`(ask line-obj 'put-back token)`

should stick the given token at the front of the line-list, so that the next
NEXT message will return it. This is used when EVAL has to read past the end
of an expression to be sure that it really is the end, but then wants to un-
read the extra token.

There are several places in `logo-meta.scm` that send these messages to the
objects you'll create, so you can see examples of their use. You'll get ASK
from `obj.scm` and should use its syntax conventions.

Also write a short procedure `(make-line-obj text)` that creates and returns a
line object instance with the given text. This procedure is invoked in several
places within the Logo interpreter.

##  Question 2

We need to be able to print the results of Logo computations. Logo provides
three primitive procedures for this purpose:

`? print [a [b c] d] ; don't show outermost brackets `

` a [b c] d `

`? show [a [b c] d] ; do show outermost brackets `

`[a [b c] d] `

`? type [a [b c] d] ; don't start new line after printing `

`a [b c] d? `

PRINT and SHOW can be defined in terms of TYPE, and we have done so in the
procedures logo-print and logo-show (defined in logo.scm). Your job is to
write logo-type. It will take a word or list as argument, and print its
contents, putting square brackets around any sublists but not around the
entire argument. You should use the Scheme primitive DISPLAY to print the
individual words. DISPLAY is described in the Scheme reference manual in your
course reader. Hint: `(display " ")` will print a space.

When you've finished these two steps, you must combine your work with that of
person B. When you've done that, you should be able to run the interpreter and
carry out instructions involving only primitive procedures and constant
(quoted or self-evaluating) data. (You aren't yet ready for variables,
conditionals, or defining procedures, and you can only use prefix arithmetic
operators.)

(There are some suggestions for things to test at the end of person B's
problems for this week.)

**When you and your partner are done with number 2, combine your code and move on to number 3!**

##  Question 5

**Make sure you are completely done with question 4 before attempting this problem!**

Infix arithmetic. Logo-eval calls eval-prefix to find a Scheme-style
expression and evaluate it. Then it calls

`(handle-infix value line-obj env)`

We have provided a "stub" version of handle-infix that doesn't actually handle
infix, but merely returns the value you give it. Your task is to write a
version that really works. The situation is this. We are dealing with the
instruction line

`? print 3 + 2`

We are inside the logo-eval that's preparing to invoke PRINT. It knows that
PRINT requires one argument, so it recursively called logo-eval. (Actually
logo-eval calls eval-prefix, which calls collect-n-args, which calls logo-
eval.) The inner logo-eval called eval-prefix, which found the expression 3,
whose value is 3. But the argument to PRINT isn't really just 3; it's 3 + 2.

The job of handle-infix is to notice that the next token on the line is an
infix operator (one of `+ - * / = < >`), find the corresponding procedure, and
apply it to the already-found value (in this case, 3) and the value of the
expression after the infix operator (in this case, 2). Remember that this
following expression need not be a single token; you have to evaluate it using
eval-prefix. If the next token isn't an infix operator, you must put it back
into the line and just return the already-found value. Remember that there may
be another infix operator after you deal with the first one, as in the
instruction

`? print 3 * 4 + 5`

`17`

We've provided a procedure called de-infix that takes an infix operator as
argument and returns the name of the corresponding Logo primitive procedure.

To further your understanding of this problem, answer the following question:
What difference would it make if your handle-infix invoked logo-eval instead
of eval-prefix as suggested above? Show a sample instruction for which this
change would give a different result.

By the way, don't forget that we are not asking you to handle the precedence
of multiplication over addition correctly. Your handle-infix will do all infix
operations from left to right, unless parentheses are used. (You don't have to
deal with parentheses in handle-infix. Logo-eval already knows about them.)

**Once partner B is done with their part 5, merge your code and work on part 6 togther. Part 6 cannot be attempted until your partner is done with their code.**

##  Question 8

**Make sure you are completely done with part 7 before attempting this part!**

Add the STEP and UNSTEP primitive commands. They take a word as argument,
which must be the name of a user-defined procedure. STEP sets to true, and
UNSTEP sets to false, a flag inside the procedure structure (you'll have to
add this to the procedure ADT). When a defined procedure is called, if the
stepping flag is set, Logo should print each line of the procedure definition,
followed by a ">>> " prompt, before evaluating that line, and then wait for
the user to enter a line (it'll usually be an empty line, but in any case you
can ignore what the user types; you're just waiting for him/her to type it).
Then run the line from the procedure. For example:

`? to garply`

`-> print "hello`

`-> print "goodbye`

`-> end`

`? garply`

`hello`

`goodbye`

`? step "garply`

`? garply`

`print "hello>>> [user hits return/enter key]`

`hello`

`print "goodbye>>>`

`goodbye`

`? unstep "garply` `? garply` `hello` `goodbye` `?`

This is a Logo debugging assistance feature. Try it on a recursive procedure!

**When your partner is done with their part 8, merge your code and move on to part 9! Part 9 cannot be attempted until both partners are done with part 8.**

