## Defining Variables

We use `define` to assign values to variables.

For example, `(define x 2)` assigns the value `2` to `x`:

```
-> (define x 2)
-> x
2
-> (+ x 5)
7
```

After calling `(define x 2)`, we say that `x` is *bound* to `2`.
Variable bindings are stored in *environments*, which we'll talk more about in Unit 3.

## Check for Understanding

<div class="mc">
Suppose the following is typed into the Racket interpreter:

<pre><code>(define pi 3.14159)
(define radius 3)

(define area (* radius radius pi))
(define circumference (* 2 pi radius))
</code></pre>

What would <code>area</code> evaluate to?
<ans text="<code>(* 3 3 3.14159)</code>" explanation="When you define a variable, you should fully evaluate the value."></ans>
<ans text="28.27431" explanation="Nice!!" correct></ans>
<ans text="ERROR" explanation="Try evaluating the expression again!"></ans>

What would <code>circumference</code> evaluate to?
<ans text="18.84954" explanation="Nice!!" correct></ans>
<ans text="28.27431" explanation="Whoops!! Try evaluating the value for <code>circumference</code>." correct></ans>
<ans text="circumference" explanation="The interpreter will return the <i>value</i> of <code>circumference</code>."></ans>
<!-- and so on -->
</div>
