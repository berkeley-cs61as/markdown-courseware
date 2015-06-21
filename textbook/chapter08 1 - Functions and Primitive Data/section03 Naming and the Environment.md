## Define

One of the most important aspect of a programming language is the ability to
name [variables](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/variable/). The procedure `define` is the way variables are specified
in Racket. For example, `(define x 2)` _binds_ the variable `x` to the
[value](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-
1x/value/) `2`. Now, the expression `(+ x 5)` evaluates to `7`. Where is the
value of `x `stored? In something called the _environment_, which we'll
discuss more in Unit 3.

If this is typed into the Racket interpreter...

`(define pi 3.14159)`

`(define radius 3)`

`(define area (* radius radius pi))`

`(define circumference (* 2 pi radius))`

What would the following evaluate to?

<div class="mc">

<pre><code>area
</code></pre>
<ans text="(* 3 3 3.14159)" explanation="When you define a variable, you should fully evaluate the value"></ans>
<ans text="28.27431" explanation="Nice!!" correct></ans>
<ans text="ERROR" explanation="Try evaluating the expression again!"></ans>
<!-- and so on -->
</div>

<div class="mc">

<pre><code>circumference
</code></pre>
<ans text="18.84954" explanation="Nice!!" correct></ans>
<ans text="28.27431" explanation="Whoops!! Try evaluating the value for *circumference*" correct></ans>
<ans text="circumference" explanation="The interpreter will return the *value* of circumference"></ans>
<!-- and so on -->
</div>

