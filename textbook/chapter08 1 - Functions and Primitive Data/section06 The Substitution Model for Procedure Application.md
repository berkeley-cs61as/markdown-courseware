##  Applying Compound Procedures

So far we have seen how Racket breaks down and evaluates expressions such as:

`(+ 1 2)`

`(+ 3 4 (* 2 5))`

by following these steps:

  1. Evaluate the procedure
  2. Evaluate the arguments
  3. Apply the procedure to the arguments.

We have been slightly handwavy with step 3. How exactly do you 'apply'
procedures? For primitive functions like  `+`, `-` , `quote`, `or`, `and`, `not`, we can
assume that it is built into the interpreter . We are more interested in
something more complex: how do we apply compound (i.e. user defined) procedures? Since we 
can define arbitarily many compound procedures, they can't all be built into the
interpreter. There needs to be a a common step-by-step way to apply compound
procedures. One way to think about this is the Substitution Model, which we
will explore in this subsection.

##  Substitution Model

To apply a compound procedure with the Substitution Model, you substitute each
formal parameter in the body with the corresponding argument's value and evaluate it
normally. What does this actually mean? It's easier to see through an example:

Consider the `sum-of-squares` procedure from the very first lab, which can be
defined as follows:


<pre><code>(define (sum-of-squares x y)  
     (+ (square x) (square y))) ;; This line is the 'body' of the procedure
     (define (square x) (* x x))
</code></pre>



How does the Substitution Model handle `(sum-of-squares 3 4)` ?

  1. We have a formal parameter, x which is called with the [ argument](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-1x/argument/) 3 and another formal parameter y which is called with the argument 4.
  2. We substitute every occurence of x and y in the body with 3 and 4 respectively
  3. The body then becomes `(+ (square 3) (square 4))`
  4. Using the definition of square, this reduces to `(+ (* 3 3) (* 4 4)). `
  5. Applying both multiplications gives `(+ 9 16)`
  6. Applying addition gives the result of `25`

Step 1 and 2 are the most crucial part of the Substitution Model: finding what
values are passed into the function, and substituting every occurence of a variable in the body
with its corresponding value.

## Formal Parameters' Names

You might have noticed by now that the names of formal parameters are
arbitary. For example all of the followings are equivalent:

`(define (square x) (* x x))`

`(define (square apple) (* apple apple))`

`(define (square magikarp) (* magikarp magikarp))`

The Substitution Model handles all three equivalently, though it is best to
pick a name that is easy to understand (In this case, the first definition is
ideal). The main point is to stay consistent within the body.  The following
for example, might cause an error:

`(define (square x) (* apple apple))`

![](http://foundersgrp.files.wordpress.com/2011/01/apple-cube.jpg)

When we use Substitution Model with  `(square 4)` with the definition above, you
can notice that things are not properly defined. The procedure `square` accepts an argument,
x which in this case is 4. What do we do in the body? We need to find the
value of `apple` and do `(* apple apple)`. What is the value of `apple`? We
don't know! We only know what `x` is!

## Substitution Model & Racket

Does Racket actually use the Substitution Model to apply compound procedures? Not
quite. We use the Substitution Model to help us think about procedure application. Racket does something slightly more complicated, which we will explore in Unit 3 and 4. Later on, we will find that the Substitution Model is not sufficient to explain some functions in Racket. This model will serve as a framework which we will build on.

## Applicative Order vs Normal Order

Our method of evaluation by evaluating operator, evaluating the operands and then
applying the operator is just one possible rule of evaluation. The ordering we have been 
using is called "Applicative Order".  An alternative method of evaluation would be to
not evaluate the operand until the value is needed. This method is called
"Normal Order".  We can see the difference between these 2 from the following
example:

`(square (+ 3 2))`

Note that the input to square is (`+ 3 2). `

  * Applicative Order:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(square (+ 3 2))`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(square 5)  `

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(* 5 5)  `

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`25`

In Applicative Order, you would evaluate the parameter `x`, before you go the
body of square, which is `(* x x)`. When you evaluate `(+ 3 2)`, you get `5` and
this is what you pass into square. So `x` is bound to `5`.

  * Normal Order:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(square (+ 3 2))`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(* (+ 3 2) (+ 3 2))`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(* 5 5)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`25`

In Normal Order, you don't evaluate `(+ 3 2)` until you absolutely need to. So in this case, the `x` in `(square x)` is bound to `(+ 3 2)`.

Notice that, in Normal Order, since you don't evaluate the `x`, which is `(+ 3 2)`, until it's needed, you need to evaluate it twice. On the other hand, in Applicative Order, since you evaluate the operand `x` before applying the procedure, you only evaluate `(+ 3 2)` once.

Consider the following piece of code:

<pre><code>(define (double_first a b) (+ a a))

(double_first (+ 1 1) (+ 2 2)) </code></pre>

 <div class="mc">
In Applicative Order, how many times is (+ 1 1) evaluated?

<ans text="0" explanation="Try again!"></ans>
<ans text="1" explanation="Nice!" correct></ans>
<ans text="2" explanation="Try again!" ></ans>
<ans text="3" explanation="Try again!"></ans>
</div>

<div class="mc">
In Normal Order, how many times is (+ 1 1) evaluated?

<ans text="0" explanation="Try again!"></ans>
<ans text="1" explanation="Try again!" ></ans>
<ans text="2" explanation="Nice!" correct></ans>
<ans text="3" explanation="Try again!"></ans>
</div>

<div class="mc">
In Applicative Order, how many times is (+ 2 2) evaluated?

<ans text="0" explanation="Try again!"></ans>
<ans text="1" explanation="Nice!" correct></ans>
<ans text="2" explanation="Try again!" ></ans>
<ans text="3" explanation="Try again!"></ans>
</div>

<div class="mc">
In Normal Order, how many times is (+ 2 2) evaluated?

<ans text="0" explanation="Nice!" correct></ans>
<ans text="1" explanation="Try again!" ></ans>
<ans text="2" explanation="Try again!" ></ans>
<ans text="3" explanation="Try again!"></ans>
</div>



## Takeaways

Some takeaways from this subsection:

  * The Substitution Model helps us in understanding how application works, but it is NOT how the interpreter does application.
  * Evaluating the arguments before applying (i.e. Applicative Order) is one method of evaluating. There are other methods of evaluation (i.e. Normal Order) where you only evaluate the arguments when you need the value

