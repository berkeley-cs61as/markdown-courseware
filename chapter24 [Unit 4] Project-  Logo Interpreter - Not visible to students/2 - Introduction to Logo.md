## Getting Logo

Before you begin working on the project, you have to know something about the
Logo programming language. The Logo-in-Scheme interpreter is structured like
the metacircular evaluator, so to run it you say

` $ stk`

` > (load "~cs61as/lib/obj.scm")`

`> (load "~cs61as/lib/logo.scm") `

` > (load "~cs61as/lib/logo-meta.scm") `

` > (initialize-logo) `

` ? `

and the question-mark prompt means that you're talking to Logo. (The versions
in the library are incomplete; you'll have to do the project before you can
really run it!) Errors in your Logo instructions can cause the interpreter to
get a Scheme error message and return you to the Scheme prompt. If this
happens, type `(driver-loop)` to return to Logo. You should only use
`(initialize-logo)` once, or else you will lose any Logo variables or
procedures you've defined.

**NOTE TO MACINTOSH GAMBIT USERS**: Before running this project you must tell Gambit to read a line, not a Scheme expression, in response to the ENTER key. To do this, look in the Edit menu and select Window Styles. Near the bottom right corner of the window that will appear are three check boxes; the middle one is labelled "Enter = Send Line". Check that box (so that you see an X in the box), then click OK. 

**NOTE TO WINDOWS-NATIVE STK USERS**: We don't think there's any way to tell the Windows version of STk to read a line rather than an expression. You must either do the project on the lab machine with ssh, or else install the Unix version of STk on your machine under a Unix simulator such as cygwin. If you want to experiment with a *real* Logo interpreter, to see how it's supposed to work, just say   
`% logo`

to the shell. You exit Logo by saying BYE. (You can download Berkeley Logo for
your home computer [ here](http://www.cs.berkeley.edu/~bh/logo.html) )

## Arithmetic and Sentences

Logo is essentially a dialect of Lisp. That makes it a good choice for this
project, both because it'll be easy to teach you the language and because the
modifications to the evaluator are not as severe as they would be for an
unrelated language. However, Logo was designed for educational use,
particularly with younger children. Many design decisions in Logo are meant to
make the language more comfortable for a beginner. For example, most Logo
procedures are invoked in prefix form (first the procedure name, then the
arguments) as in Lisp, but the common arithmetic operators are also provided
in the customary infix form:

    
    
    ? print sum 2 3 
    5 
    ? print 2+3 
    5
    

(Note: As you work with the Logo-in-Scheme interpreter, you probably won't be
impressed by its comfort. That's because our interpreter has a lot of rough
edges. The most important is in its error handling. A real Logo interpreter
would not dump you into Scheme with a cryptic message whenever you make a
spelling mistake! Bear in mind that this is only a partial implementation.
Another rough edge is that **THERE IS NO PRECEDENCE AMONG INFIX OPERATORS**,
unlike real Logo, in which (as in most languages) multiplication is done
before addition. In this interpreter, infix operators are carried out from
left to right, so `3+4*5` is `7*5` or 35, not `3+20`.)

Even in the trivial example above, adding two numbers, you can see several
differences between Scheme and Logo. The most profound, in terms of the
structure of the interpreter, is that expressions and their subexpressions are
not enclosed in parentheses. (That is, each expression is not a list by
itself.) In the metacircular evaluator, EVAL is given one complete expression
as an argument. In the Logo interpreter, part of EVAL's job will be to figure
out where each expression begins and ends, by knowing how many arguments are
needed by each procedure, for example:

    
    
    	? print sentence word "now "here last [the invisible man]
    

Logo must understand that WORD requires two arguments (the quoted words that
follow it) while LAST requires one, and that the values returned by WORD and
LAST are the two required arguments to SENTENCE. (Also, PRINT requires one
argument.)

Another important difference between Scheme and Logo is that in the latter you
must explicitly say PRINT to print something:

    
    
    ? print 2+1
    3
    ? 2+1
    You don't say what to do with 3
    

An expression that produces an unused value causes an error message. Unlike
Scheme, in which every procedure returns a value, Logo makes a distinction
between OPERATIONS that return a value and COMMANDS that are used for effect.
PRINT is a command; SUM is an operation. This distinction means that Logo has
less of a commitment to functional programming style, and it makes the
interpreter a little more complicated because we have to keep track of whether
we have a value or not. But in some ways it's easier for the user; we don't
keep saying things like "`set!` returns some value or other, but the value is
unspecified and you're not supposed to rely on it in your programs." Also,
Logo users don't see the annoying extra values that Scheme programs sometimes
print because some procedure that was called for effect happens to return `()`
or `#f` or `okay` as a value that gets printed.

##  logo-read

One implication for the interpreter is that instead of Scheme's read-eval-
print loop

`(define (driver-loop)`

` (display "> ") `

` (print (eval (read) the-global-environment)) `

` (driver-loop)) `

Logo just has a read-eval loop without the print.

In Scheme something like 2+3 would be considered a single symbol, not a
request to add two numbers. The plus sign does not have special status as a
delimiter of expressions; only spaces and parentheses separate expressions.
Logo is more like most other programming languages in that several characters
are always considered as one-character symbols even if not surrounded by
spaces. These include arithmetic operators, relational operators, and
parentheses:

` + - * / = < > ( ) `

Remember that in Scheme, parentheses are used to indicate list structure and
are not actually part of the internal representation of the structure. (In
other words, there are no parentheses visible in the box-and-pointer diagram
for a list.) In this Logo interpreter, parentheses are special symbols, just
like a plus sign, and are part of the internal representation of an
instruction line. Square brackets, however, play a role somewhat like that of
parentheses in Scheme, delimiting lists and sublists. One difference is that a
list in square brackets is automatically quoted, so `[...]` in Logo is like
`'(...)` in Scheme:

` ? print [hi there] `

Logo uses the double quotation mark `(") ` to quote a word, so `"foo` in Logo
is like `'foo ` in Scheme. Don't get confused -- these quotation marks are not
used in pairs, as in Scheme string constants `("error message")`; a single one
is used before a word to be quoted.

` ? print "hello `

Just as the Scheme procedure READ reads an expression from the keyboard and
deals with parentheses, spaces, and quotation marks, you are given a LOGO-READ
procedure that handles the special punctuation in Logo lines. One important
difference is that a Scheme expression is delimited by parentheses and can be
several lines long; LOGO-READ reads a single line and turns it into a list. If
you want to play with it from Scheme, first get out of Logo (if you're in it)
by typing ^C twice, then type the invocation `(logo-read)` and the Logo stuff
you want read all on the same line:

`> (logo-read)print 2+(3*4)`

` (print 2 + ( 3 * 4 )) `

`> (logo-read)print se "this [is a [deep] list] `

` (print se "this (is a (deep) list)) `

Remember that the results printed in these examples are Scheme's print
representation for Logo data structures! Don't think, for example, "LOGO-READ
turns square brackets into parentheses." What really happens is that LOGO-READ
turns square brackets into box-and-pointer lists, and Scheme's print procedure
displays that structure using parentheses. Note: In the first of these two
examples, the inner parentheses in the returned value are *not* the boundaries
of a sublist! They are parenthesis symbols.

What logo-read returned was a sentence with eight words:

`print, 2, +, (, 3, *, 4, ` and `) `.

This makes it a little tricky to be sure what you're seeing.

If you want to include one of Logo's special characters in a Logo word, you
can use backslash before it:

`?print "a\+b `

`a+b `

Also, as a special case, a special character other than square bracket is
considered automatically backslashed if it's immediately after a quotation
mark:

`?print "+ `

`+`

All of this is handled by LOGO-READ, a fairly complicated procedure. You are
not required to write this, or even to understand its algorithm, but you'll
need to understand the results in order to work on EVAL.

## Procedures and Variables

Procedures and variables: Here is a Scheme procedure and an example of
defining and using the corresponding Logo procedure:

`(define (factorial n) `

` (if (= n 0) `

` 1 `

` (* n (factorial (- n 1))) )) `

`? to factorial :n `

` -> if :n=0 [output 1] `

` -> output :n * factorial :n-1 `

` -> end `

` ? print factorial 5 `

`120 `

There are several noteworthy points here. First, a procedure definition takes
several lines. The procedure name and formal parameters are part of the first
instruction line, headed by the TO special form. (This is the only special
form in Logo.) The procedure body is entered on lines in response to a special
-> prompt. These instruction lines are not evaluated, as they would be if
entered at a ? prompt, but are stored as part of the procedure text. The
special keyword END on a line by itself indicates the end of the body. (In
real Logo, the special prompt is just > but we use -> to avoid confusion with
the Scheme prompt.)

Unlike Scheme, Logo does not have first-class procedures. Among other things,
this means that a procedure name is not just a variable name that happens to
be bound to a procedure. Rather, procedures and variables are looked up in
separate data structures, so that there can be a procedure and a variable with
the same name. (This is sometimes handy for names like LIST and WORD, which
are primitive procedures but are also convenient formal parameter names. In
Scheme we resort to things like L or LST to avoid losing access to the LIST
procedure.) Variable names are part of a Scheme-like environment structure
(but with dynamic rather than lexical scope); procedure names are always
globally accessible. To distinguish a procedure invocation from a variable
reference, the rule is that a word FOO without punctuation is an invocation of
the procedure named FOO, while the same word with a colon in front (:FOO) is a
request for the value of the variable with that name.

A Logo procedure can be either a command (done for effect) or an operation
(returning a value). In this example we are writing an operation, and we have
to say so by using the OUTPUT command to specify the return value. Once an
OUTPUT instruction has been carried out, the procedure is finished; in this
example, if the IF in the first line of the body outputs 1, the second line of
the body is not evaluated.

The file ~cs61a/lib/test.logo contains definitions of several Logo procedures
that you can examine and test to become more familiar with the language. You
can load these definitions into your Logo interpreter by copying it to your
directory and then using Logo's LOAD command:

` ? load "test.logo `

(Notice that if you want to use a filename including slashes you have to
backslash them to make them part of the quoted word.)

Unlike Scheme's IF, Logo's IF is not a special form. You probably remember a
homework exercise that proved that it had to be, but instead Logo takes
advantage of the fact that square brackets quote the list that they delimit.
The first argument to IF must be the word TRUE or the word FALSE. (Predicate
functions in Logo always return one of these two words. Logo does not accept
any non-FALSE value as true; anything other than these two specific words is
an error.) The second argument is a list containing instructions that should
be run conditionally. Because the list is enclosed in square brackets, the
instructions are not evaluated before IF is invoked. In general, anything that
shouldn't be evaluated in Logo must be indicated by explicit quotation, with
"xxx or [xxx]. The only special form is TO, in which the procedure name and
formal parameter names are not evaluated.

The procedures `first, butfirst`, etc. that we've been using to manipulate
words and sentences were invented in Logo. The Scheme versions don't quite
work as smoothly as the real Logo versions, because Scheme has four distinct
data types for numbers, symbols, strings, and characters; all of these are a
single type (words) in Logo. If you evaluate (bf 104) in Scheme you get "04",
not just 04, because the result has to be a Scheme string in order not to lose
the initial zero. Our Logo interpreter does manage to handle this:

`? print bf 104 `

`04 `

`? print bf bf 104 `

`4 `

The interpreter represents 04 internally as a Scheme symbol, not as a number.
We can nevertheless do arithmetic on it

`? print 7+bf 104 `

`11 `

because all the Logo arithmetic functions have been written to convert
symbols-full-of-digits into regular numbers before invoking the actual Scheme
arithmetic procedure. (This is the job of MAKE-LOGO-ARITH.)

If you used Logo as a kid, what you probably remember is not doing text
processing, but drawing pictures. Our Logo-in-Scheme includes the turtle
graphics primitives FORWARD, BACK, LEFT, RIGHT, CLEARSCREEN, HOME, PENUP,
PENDOWN, PENERASE, SHOWTURTLE, HIDETURTLE, SETXY, XCOR, YCOR, POS, HEADING,
SETHEADING, SETPENCOLOR, PENCOLOR, SETBACKGROUND, and their abbreviations.

## Starting the Project

Okay, time for the actual project. You will need these files:

`~cs61as/lib/obj.scm ` object-oriented tools

`~cs61as/lib/logo.scm ` various stuff Logo needs

`~cs61as/lib/logo-meta.scm ` modified metacircular evaluator

You will only be modifying `logo.scm` and `logo-meta.scm`

These files (or your modified versions of the last two) must be loaded into
Scheme in this order; each one depends on the one before it. Much of the work
has already been done for you. (The names logo-eval and logo-apply are used so
as not to conflict with Scheme's built-in eval and apply functions.)

For reference, `~cs61as/lib/mceval.scm `is the metacircular evaluator without
the modifications for Logo.

Start by examining logo-eval. It has two parts: `eval-prefix`, which is
comparable to the version of `eval` in the text, handles expressions with
prefix operations similar to Scheme's syntax. The result of evaluating such an
expression is then given as an argument to `handle-infix`, which checks for a
possible infix operator following the expression. For now, we'll ignore
`handle-infix`, which you'll write later in the project, and concentrate on
`eval-prefix`. Compare it with the version of eval in the text. The Scheme
version has a COND clause for each of several special forms. (And the real
Scheme has even more special forms than the version in the book.) Logo has
only one special form, used for procedure definition, but to make up for it,
eval-prefix has a lot of complexity concerning parentheses. An ordinary
application (handled by the else clause) is somewhat more complicated than in
Scheme because we must figure out the number of arguments required before we
can collect the arguments. Finally, an important subtle point is that the Logo
version uses LET in several places to enforce a left-to-right order of
evaluation. In Scheme the order of evaluation is unspecified, but in Logo we
don't know where the second argument expression starts, for example, until
we've finished collecting and evaluating the first argument expression.

