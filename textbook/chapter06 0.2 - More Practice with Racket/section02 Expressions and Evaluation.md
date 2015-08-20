## Introduction

In this subsection, you will learn more about Functional Programming. You will also learn about expressions and evaluation.

## Functional Programming

Before we jump into the Racket language itself, we will go over the deceptively simple big idea for this lesson. In short, it states that, when evaluating an expression, we can take the value returned by one function and use it as an argument to another function. By "hooking up" two functions in this way, we invent a new, third function. For example, let's say we have a function that adds the letter s to the end of a word (in pseudo-code):

    
    add-s("run") = "runs"

and another function that puts two words together into a sentence:

    
    sentence("day", "tripper") = "day tripper"

We can combine these to create a new function that represents the third person
singular form of a verb:

    
    third-person(verb) = sentence("she", add-s(verb))

That general formula looks like this when applied to a particular verb:

    
    third-person("sing") = "she sings"

The way we say it in Racket is

    
    (define (third-person verb)
      (sentence 'she (add-s verb)))

Don't worry if this is confusing or unintuitive to you; you'll get plenty of practice on this concept. Nevertheless, it will turn out that we can express a wide variety of computational algorithms by linking functions together in this way. This linking is what we mean by **functional programming**.

## Expressions

**The Big Idea:** You can ask Racket "questions", called **expressions**. The Racket interpreter will then "think" about your question, or **evaluate** your expression. You then get back answers, called **values**. Everything we type into Racket (that does not error) is an expression.

When you want Racket to _do_ something (e.g. add two numbers together), you write an expression in **prefix notation**. Although all non-error inputs are expressions, the most interesting kind is a **call to a procedure**. Take a look at the following example:

    
    (+ 3 4)

In this example:

  * **`+`** is the procedure, or the _operator_ of the expression
  * **`3`** is an argument to `+`, or an _operand_ of the expression
  * **`4`** is also an argument/operand

This syntax allows us to **nest** expressions:

    
    (* (max 2 3) (/ 8 4))

  * `*`, `max`, and `/` are all procedures
  * `*` is the operator of the large expression, while `(max 2 3)` and `(/ 8 4)` are the operands of the large expression
  * `max` is the operator of the first subexpression, while `2` and `3` are the operands of the first subexpression
  * `/` is the operator of the second subexpression, while `8` and `4` are the operands of the second subexpression

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Which of the following are valid Racket expressions? Select all that apply.

<ans text="4" explanation="Numbers are expressions in Racket!" correct></ans>
<ans text="(2 * 2)" explanation="This is not valid because it does not use Racket's prefix notation."></ans>
<ans text="(sqrt (sqrt 16))" explanation="sqrt is a primitive procedure in Racket, and thus this is a valid expression." correct></ans>
<ans text="(+ 2 2)" explanation="" correct></ans>
</div>

Now, open up the Racket interpreter on your computer and try out some expressions of your own.

## Evaluation

Racket evaluates expressions using Applicative Order (taught in Lesson 1), which follows these rules:

  1. Evaluate the operator and operands
  2. Apply the operator to the operands

How Racket actually understands and evaluates an expression is rather complex, and is gone over in Lesson 11. For now, let's move on to the next subsection!
