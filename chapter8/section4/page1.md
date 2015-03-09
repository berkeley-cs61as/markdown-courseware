## Define?

What about `define`? It turns out that the ordinary evaluation rules don't
work for `define`, since `(define x 3)` doesn't apply `define` to two
arguments; it instead stores the value of `x` as 3. Define is what is known as
a [special form](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/special-form/), and special forms are the only exceptions to the
rules of evaluation.

