## Introduction

Notice that in the previous page, there was little mention of [programming
languages](http://en.wikipedia.org/wiki/Programming_language). That's because
in the grand scheme of things, programming languages don't matter. They only
matter because, for any given problem, one language might let us solve the
problem in fewer lines of code over another, or one language might let us
solve the problem more efficiently, and so on.

What of the problem of teaching computer science? Which language should we use
for that? We have chosen Racket, a dialect of [Lisp](http://en.wikipedia.org/wiki/Lisp_programming_language).
We'll show basics of the language today, after which you can start thinking about computer science. As you learn more computer science, we'll incrementally show you more of the language.

Let's begin.

<!--
Among other things, Racket is a programming language suited for learning Computer Science. We believe this partly because we can teach it to you in a day.
-->


## Basic Rules

  1. In Racket, parentheses (also known as *parens*) matter.
  2. When you ask a procedure to perform its action, you _call_ it. This is also called _invoking_ a procedure. Whenever you invoke a procedure, you must wrap the procedure call (the call to the procedure) in a set of parentheses.
  3. Everytime we invoke a procedure, we must follow **prefix notation**: the name of the procedure we're invoking is always the leftmost item in the parentheses.
  All of the other things are _arguments_ to that procedure&mdash;things we feed in to the procedure in order to get our answer.

Here's an example of an expression that demonstrates the three rules above:

```
(+ 1 2)
```

In this example, we're feeding the arguments `1` and `2` into the procedure `+`, which adds numbers.
We should expect the answer to be 3.

## The Racket Interpreter

Of course, a language is no good if no one speaks it. For programming
languages, the dialog is usually  between the programmer and a computer. An
**interpreter** is a program that translates a particular language into
actions and computations that the computer performs. Interpreters are one way
to make computers do things, such as computing large prime numbers or counting all the distinct words used in all of Shakespeare's plays.

Let's start our Racket interpreter. We do this by opening a terminal and then typing in `racket` and hitting Enter.
You've just started the Racket interpreter!

You can now type Racket expressions for the interpreter to evaluate:

```
-> (+ 1 2)
3
```

## What Will Racket Output?

Type each example below into the interpreter to try it out.
Before entering each example, take a moment and think about what the output should be.
Some of these examples cause errors&mdash;why do they do that? (If something errors, the interpreter will output an error message.)

    
    5
    (+ 2 3)
    (+ 5 6 7 8)
    (+ (* 3 4) 5)
    (+)
    +
    (sqrt 16)
    (/ 3 2)
    (/ 3 0)
    
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
    
<!-- The questions that used to be here were downright bad

<div class="mc">
What do parentheses do?
<ans text="A. Parens are used to call, or invoke, a procedure." explanation="Yes!" correct></ans>
<ans text="B. Parens are only used for stylistic purposes, and can be omitted." explanation="Parens are never optional. You must always have a reason for inserting or removing parens."></ans>
</div>

-->

## Takeaways

In this section, we learned the basics of Racket. We also tried our hands at the Racket interpreter.
