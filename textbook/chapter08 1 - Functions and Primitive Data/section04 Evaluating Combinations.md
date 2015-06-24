## What Does Evaluate Mean?

When we type a Racket expression such as `(+ 2 3)` into the interpreter, we as
humans know immediately that that is really just `5`. But all the computer
sees is open parentheses, plus, two, three, close parentheses. How does it get from the
Racket expression to the value `5`? It _evaluates_ the expression and gets the
value 5 from there. How does it evaluate it? 

## How the Interpreter Evaluates Things

The way the interpreter evaluates things can be a little confusing at first,
but will make sense soon. To evaluate a Racket expression, first
evaluate the subexpressions of the expression. In other words, you first evaluate
the operands fully, and then apply the operator. When you reach a procedure
call, apply the operator to the operands and repeat.  Note that evaluation is
recursive--in order to evaluate an expression, we need to first evaluate its
subexpressions. In order to evaluate the subexpressions, we need to evaluate
_their_ subexpressions, and so on until we reach a procedure.

## Example: A Recursion Tree

Let's try evaluating the following expression:

`(* (+ 2 (* 4 6)) `

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` (+ 3 5 7))`

This is a fairly complicated expression, and without recursion it would be very
difficult to evaluate. Evaluating this requires that the evaluation rule be
applied four different times. If we represent the evaluation process
as a tree, it becomes a little easier to understand. This tree, unlike real
trees, has its roots in the air and its branches sticking into the ground.

Each combination is represented by a node with branches corresponding to a subexpression. 
The end branches are operators or numbers. We can imagine that the values of the
operands swim upwards, starting at the bottom of the tree, getting
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

<div class="mc">
Which of the following is not a primitive function in Racket?

<ans text="+" explanation="Nope! + follows the regular rules of evaluation"></ans>
<ans text="if" explanation="Nice!! *if* is a special form!" correct></ans>
<ans text="not" explanation="Nope! *not* follows the regular rules of evaluation"></ans>
<ans text="square" explanation= "Nope! *square* follows the regular rules of evaluation"></ans>
</div>

