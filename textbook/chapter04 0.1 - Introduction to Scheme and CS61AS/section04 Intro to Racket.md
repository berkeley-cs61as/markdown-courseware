## Introduction

Notice that in the previous page, there was little mention of [programming
languages](http://en.wikipedia.org/wiki/Programming_language). That's because
in the grand scheme of things, programming languages don't matter. They only
matter because for any given problem, one language might let us solve the
problem in fewer lines of code over another, or one language might let us
solve the problem more efficiently, and so on.

What of the problem of teaching Computer Science? Which language should we use
for that? We have chosen Racket, a dialect of [the Lisp programming language](http://en.wikipedia.org/wiki/Lisp_programming_language). Among other things, Racket is a programming language suited for learning Computer Science. We believe this partly because we can teach it to you in a day. We'll show basics of the language today, after which you can start thinking about Computer Science. As you learn more Computer Science, we'll incrementally show you more of the language. Let's begin.

## Basic Rules

  1. In Racket, [parentheses matter](http://xkcd.com/297/).
  2. When you ask a procedure to perform its action, you _call_ it. This is also called _invoking_ a procedure. Whenever you invoke a procedure, you must wrap the procedure call (the call to the procedure) in a set of parentheses.
  3. Everytime we invoke a procedure, we must follow **prefix notation*: a notation that dictates that the procedure that we're invoking is always the leftmost item in the parentheses. Everything else are _arguments_ to that procedure -- things we feed in to the procedure in order to get our answer. For example, for this expression: `(+ 2 2)`, we feed in `2` and `2` into `+` in order to get the answer, `4`.

## The Racket Interpreter

Of course, a language is no good if no one speaks it. For programming
languages, the dialog is usually  between the programmer and a computer. An
**interpreter** is a program that translates a particular language into
actions and computations that the computer performs. Interpreters are one way
to make computers do things, such as computing large prime numbers or counting all the distinct words used in all of Shakespeare's plays.

Let's start our Racket interpreter. We do this by opening a Terminal (`Ctrl-
Alt-t`) and then typing in `racket` and hitting Enter. You've just started the Racket interpreter!

## What Will Racket Output?

What does the Racket interpreter output when you try the following examples?
Type each example into the interpreter to try it out. Before entering each example, take a moment and think about what the output should be. Some of these examples will cause errors -- why is that? (If something errors, the interpreter will output `"*** Error:"` along with some error message.)

    
    5
    (+ 2 3)
    (+ 5 6 7 8)
    (+ (* 3 4) 5)
    (+)
    +
    (sqrt 16)
    
    'hello
    (first 'hello)
    (first hello)
    (butfirst 'hello)
    (bf 'hello)
    (first (bf 'hello))
    (first 274)
    (+ (first 23) (last 45))
    
    (define pi 3.14159)
    pi
    'pi
    (+ pi 7)
    '(good morning)
    '(+ 2 3)
    

## Today I Learned...

Take a shot at these questions to test your understanding!

<div class="mc">
What do parens (parentheses) do?
<ans text="A. Parens are used to call, or invoke, a procedure" explanation="" correct></ans>
<ans text="B. Parens are used in special procedures (e.g. define)" explanation=""></ans>
<ans text="C. Parens are only used for stylistic purposes, and can be omitted." explanation="PARENS ARE NEVER OPTIONAL. You must ALWAYS have a reason for inserting or removing parens."></ans>
<ans text="D. A and B" explanation=""></ans>
<ans text="E. A, B, and C" explanation="PARENS ARE NEVER OPTIONAL. You must ALWAYS have a reason for inserting or removing parens."></ans>
<!-- and so on -->
<br>
What does define do?
<ans text="A. It assigns a name to a value" explanation=""></ans>
<ans text="B. It defines a new procedure" explanation=""></ans>
<ans text="C. It changes the value of a previously defined variable" explanation=""></ans>
<ans text="D. A and C" explanation=""></ans>
<ans text="E. A, B, and C" explanation="" correct></ans>
<!-- and so on -->
<br>
What does the quote symbol (') do?
<ans text="A. It returns everything after it as a literal value" explanation="" correct></ans>
<ans text="B. It takes everything after it and prints it out" explanation=""></ans>
<ans text="C. A and B" explanation=""></ans>
<ans text="D. It does nothing" explanation=""></ans>
<!-- and so on -->
</div>

## Takeaways

In this section, we learned the basics of Racket, and also tried our hands at the Racket interpreter.