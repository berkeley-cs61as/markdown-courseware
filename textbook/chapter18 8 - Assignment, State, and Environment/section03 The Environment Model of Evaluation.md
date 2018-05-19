## The Environment Model of Evaluation

![](http://www-tc.pbs.org/wgbh/americanexperience/media/uploads/collections/he
roImages/environment_film_landing.jpg)

In the previous subsection, we learned that we can no longer use the
substitution model of evaluation once we use assignments. The new model that
will be used from now on is called the **environment model of evaluation**.

Let's go through the example to see how this new model works. We define a simple `square` procedure and call it on `7`:

    > (define (square x) (* x x))
    square
    > (square 7)
    49

What happens? The substitution model states:

  1. Substitute the actual argument value(s) for the formal parameter(s) in the body of the function.
  2. Evaluate the resulting expression.

In this example, the substitution of `7` for `x` in `(* x x)` gives `(* 7 7)`. In step 2 we evaluate that expression to get the result, `49`.

Now, let's put the substitution model aside and take a look at the more complete and comprehensive **environment model**:

  1. Create a frame with the formal parameter(s) bound to the actual argument values.
  2. Use this frame to extend the lexical environment.
  3. Evaluate the body in the resulting environment.

A **frame** is a collection of name-value associations, or **bindings**. In our example, the frame has one binding that binds `x` to `7`.

Let's skip step 2 for a moment and think about step 3. The idea is that we are going to evaluate the expression `(* x x)`, but we are reﬁning our notion of what it means to "evaluate" an expression. Expressions are no longer evaluated in a vacuum, but instead, every evaluation must be done with respect to some
environment. 

An **environment** can be described as some collection of bindings between names and values. When we are evaluating `(* x x)` and we see the symbol `x`, we want to be able to look up `x` in our collection of bindings and ﬁnd the value `7`. Looking up the value bound to a symbol is something we've done before with global variables. What's new is that instead of one central collection of bindings we now have the possibility of **local environments**. The symbol `x` isn't always `7`. That's only the case during this one invocation of `square`. So, step 3 means to evaluate the expression in the way that we've always understood, but looking up names in a particular place.

What's step 2 about? The point is that we can't evaluate `(* x x)` in an environment with nothing but the `x` to `7` binding, because we also have to look up a value for the symbol `*` (namely, the multiplication function). So, we create a new frame in step 1, but that frame isn't an environment by itself. Instead we use the new frame to extend an environment that already existed.

Which old environment do we extend? In the `square` example, there is only one
candidate, the **global environment**. But in more complicated situations there
may be several environments available.

## Rules for the Environment Model

Now, we will go over the rules for the environment model for different cases. Before we proceed, keep in mind that:

  1. Every expression is either an **atom** or a **list**.
  2. At any time there is a current frame, initially the global frame.

## Expressing Atoms

Let's get some perspective on how we expression atomic values:

  1. Numbers, strings, `#t`, and `#f` are self-evaluating.
  2. If the expression is a symbol, find the **first available** binding. (That is, look in the current frame; if not found there, look in the frame "behind" the current frame; and so on until the global frame is reached.)

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch3-Z-G-2.gif)

## Procedure Invocation

What about procedures? How does the evaluation deal with expressions that invoke procedures?

  1. Evaluate all the subexpressions (using these same rules).
  2. Apply the procedure (the value of the first subexpression) to the arguments (the values of the other subexpressions).

    * If the procedure is compound (user-defined):

      1. Create a frame with the formal parameters of the procedure bound to the actual argument values.
      2. Extend the procedure's defining environment with this new frame.
      3. Evaluate the procedure body, using the new frame as the current frame.

    * If the procedure is primitive:

        1. Apply it by magic. **ONLY COMPOUND PROCEDURE INVOCATIONS CREATES A NEW FRAME.**

## An Example

    
    (define (square x)
      (* x x))
    (define (sum-of-squares x y)
      (+ (square x) (square y)))
    (define (f a)
      (sum-of-squares (+ a 1) (* a 2)))
    

  
  
![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch3-Z-G-5.gif)
  
Procedure objects in the global frame.

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch3-Z-G-6.gif)

Environments created by evaluating `(f 5)`.

## Special Forms

  1. A `lambda` creates a procedure in the form of a double bubble. The left circle points to the text of the `lambda` expression; the right circle points to the defining environment (i.e., to the current environment at the time the `lambda` is seen). **ONLY LAMBDAS CREATE PROCEDURES.**
  2. `define` adds a new binding to the current frame.
  3. `set!` changes the first available binding.
  4. A `let` is a `lambda` with an invocation.
  5. `(define (...) …)` = `lambda` + `define`
  6. Other special forms follow their own rules (`cond`, `if`).

## An Example

    
    (define (make-withdraw balance)
      (lambda (amount)
        (if (>= balance amount)
            (begin (set! balance (- balance amount))
                   balance)
    "Insufficient funds")))
    
  
![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch3-Z-G-7.gif)

Result of defining `make-withdraw` in the global environment.

![](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch3-Z-G-8.gif)

Result of evaluating `(define W1 (make-withdraw 100))`.

## Takeaways

In this subsection, we learned how to evaluate procedures with the environment
model.

## What's Next?

Go to the next subsection and learn how to draw environment diagrams!

