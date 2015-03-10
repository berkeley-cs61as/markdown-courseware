## Define

One of the most important aspect of a programming language is the ability to
name [variables](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/variable/). The procedure `define` is the way variables are named
in Scheme. For example, `(define x 2)` _binds_ the variable `x` to the
[value](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-
1x/value/) `2`. Now, the expression `(+ x 5)` evaluates to `7`. Where is the
value of `x `stored? In something called the _environment_, which we'll
discuss more in Unit 3.

If this is typed into the Scheme prompt...

`(define pi 3.14159)`

`(define radius 3)`

`(define area (* radius radius pi))`

`(define circumference (* 2 pi radius))`

