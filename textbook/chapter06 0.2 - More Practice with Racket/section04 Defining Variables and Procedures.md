## Introduction

Imagine a language in which we cannot use names to refer to computational objects. As we write more and more complex programs, keeping track of the details of each step of computation would get increasingly difficult and inconvenient. Thus, we assign _values_, which are the computational object, to _variables_, identified by a name, by using `define`. This is Racket's simplest means of [abstraction](/textbook/intro-to-computer-science.html#sub1).

Though you have seen various variable and procedure definitions scattered throughout the previous sections, we have not yet formally taught how to use `define`.

To start off, here are a few example expressions that use `define`. Try these out in the Racket interpreter to see what they do.

	-> (define x 5)
	-> (define (square x) (* x x))
	-> (define y (square 3))
	-> (define z (+ x y))

## Defining Variables

The general form of a **variable definition** is as follows:

	(define [name] [value])

The `[name]` represents a **variable** to which **values** are assigned to. For example:

	-> (define x 5)
	-> x
	5

`x` is a variable, and `5` is its value. 

`[value]` can be replaced with any type of value, even expressions. An important property of variable definitions is that **the value of the definition is completely evaluated before being assigned to its variable**.

	-> (define x (+ 5 5))
	-> x
	10

Why is `x` not `(+ 5 5)`? Because when we define `x`, we must first evaluate the expression `(+ 5 5)` to its simplest form, `10`. We then assign `10` to `x`.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
What happens when we call <code>(define x (/ 1 0))</code>?
</div>

## Defining Compound Procedures

**Procedure definition** is an even more powerful abstraction technique than variable definition, in which we can give a name to a compound operation and consequently refer to it as a unit. Let's start with a simple example by defining the `square` procedure:

	(define (square x) (* x x))

We can understand this in the following way:

	(define (square x) (   *     x      x))
       To    square x,  multiply x with x.

The general form of a procedure definition is as follows:

	(define ([name] [formal parameters]) [body])

Notice how a significant difference this has from a variable definition is that the name and parameters are bound by parentheses. Recall that, besides quotes, **a set of parentheses represents a procedure call**. We can translate this by saying: When we call `[name]` with `[formal parameters]`, we will do `[body]`.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
A compound procedure can have any non-negative number of formal parameters, even 0. How do we correctly define a procedure named <code>foo</code> that takes in no arguments, and returns <code>5</code>?

<ans text="(define foo 5)" explanation="This is a variable definition that simply assigns 5 to foo."></ans>
<ans text="(define (foo) 5)" explanation="" correct></ans>
<ans text="(define (foo ()) 5)" explanation=""></ans>
<ans text="(define (foo 0) 5)" explanation=""></ans>
</div>

An important property of procedure definitions is that **the body of the procedure is not evaluated until the procedure is called**. This means that when we define `square`, we do not yet know that we need to multiply `x` by itself. Only when we call `square` on some number, say `3`, do we know that we have to call `(* 3 3)`.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
What happens when we call <code>(define (x) (/ 1 0))</code>?
</div>

### Warning

One thing to pay attention to when creating compound procedures is naming. We need to be very careful when naming our procedures and formal parameters. Racket will not accept multiple definitions, which means that any procedure already defined cannot be used as the name of a compound procedure or a formal parameter. This is an example of a compound procedure definition that is NOT ALLOWED (try it in your interpreter to see why):

	(define (foo sent word)
		(word sent word))

In both instances in the body, which `word` are we referring to, the parameter or the built-in procedure?

### Nesting Procedures

Returning to the concept of nesting expressions, we can also nest procedures within other procedure definitions. As you did in Homework 0-1, we can define the procedure `sum-of-squares` by using the procedure `square` in its definition:

	(define (sum-of-squares x y)
		(+ (square x) (square y)))

This roughly translates to: When we call `sum-of-squares` on `x` and `y`, we will add the `square` of `x` to the `square` of `y`.

## A Summary

To clarify,

```
(define foo 10)
```

  * This is a variable definition.
  * `foo` is the variable name.
  * `10` is the value assigned to `foo`.

```
(define (square x) (* x x))
```

  * This is a compound procedure definition.
  * `square` is the procedure name.
  * `x` is its only formal parameter.
  * `(* x x)` is its body.

```
-> (square 3)
9
```

  * This is an expression, and is also a procedure call.
  * `square` is the procedure, and is the operator of this expression.
  * `3` is the argument to `square`, and is the operand of this expression.
  * `9` is the return value.

## Takeaways

  * We learned that we can use `define` as a means of abstraction
  * We also learned how to define variables and compound procedures

The possibility of associating values and operations to symbols and later retrieving them means that the Racket interpreter must have some form of memory to keep track of these associative pairs. We call this memory the _environment_, which we will expand more on in Lesson 8.