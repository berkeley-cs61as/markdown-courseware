## What Does Evaluate Means?

When we type a Scheme expression such as `(+ 2 3)` into the interpreter, we as
humans know immediately that that is really just `5`. But all the computer
sees is open paren, plus, two, three, close paren. How does it get from the
scheme expression to the value `5`? It _evaluates_ the expression and gets the
value 5 from there. How does it evaluate it? click the arrow to find out...

## How the Interpreter Evaluates Things

The way the interpreter evaluates things can be a little confusing at first,
but will make sense in a little bit. To evaluate a Scheme expression, first
evaluate the subexpressions of the expression. When you reach a procedure
call, apply the operator to the operands and repeat.  Note that evaluation is
recursive--in order to evaluate an expression, we need to first evaluate its
subexpressions. In order to evaluate the subexpressions, we need to evaluate
_their_ subexpressions, and so on until we reach a procedure.

## Example: A Recursion Tree

Let's try evaluating the following expression:

`(* (+ 2 (* 4 6)) `

` (+ 3 5 7))`

This is a fairly complicated procedure, and without recursion it would be very
difficult to evaluate. Evaluating this requires that the evaluation rule be
applied to four different combinations. If we represent the evaluation process
as a tree, it becomes a little easier to understand. This tree, like real
trees, has its roots in the air and its branches sticking into the ground.

Each combination is a node with branches corresponding to a subexpression. The
end branches are operators or numbers. We can imagine that the values of the
operands percolate upwards, starting at the bottom of the tree, getting
evaluated at each branch, and resulting in a new value which is further
evaluated at a higher level.

![Recursion Tree](http://mitpress.mit.edu/sicp/full-text/book/ch1-Z-G-1.gif)

A more detailed explanation is given in the [wiki
entry](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-
1x/eval/) for eval, and it will be further explained in the sections about the
substitution model.

## Define?

What about `define`? It turns out that the ordinary evaluation rules don't
work for `define`, since `(define x 3)` doesn't apply `define` to two
arguments; it instead stores the value of `x` as 3. Define is what is known as
a [special form](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/special-form/), and special forms are the only exceptions to the
rules of evaluation.

