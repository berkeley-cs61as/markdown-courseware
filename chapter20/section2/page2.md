## Scenario 1

The effect of calling `(set-car! x y)` to the original configuration:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-14.gif)

The call changes the car-pointer on x, which was initially pointing to the
`(list a b)` is now pointing to what y is pointing, `(list e f)`. Now what
happened to the list with a and b? Since nothing points to it right now, we
can't access it anymore.

