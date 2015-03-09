So, how shall we bind some variables? Well, the easiest thing is just to make
a procedure with the arguments we want.

That's exactly what we'll do here. We'll define a procedure `f-helper` to bind
the local variables:

`(define (f x y)`

` (define (f-helper a b)`

` (+ (* x (square a))`

` (* y b)`

` (* a b)))`

` (f-helper (+ 1 (* x y)) `

` (- 1 y)))`

Actually, we can cut out the middleman. Let's make a procedure with lambda and
call it.

`(define (f x y)`

` ((lambda (a b)`

` (+ (* x (square a))`

` (* y b)`

` (* a b)))`

` (+ 1 (* x y))`

` (- 1 y)))`

So, we could actually do this all the time, but the Scheme developers felt
nice and gave us a special form for this. It's called `let`. Using let, the f
procedure could be written as:

`(define (f x y)`

` (let ((a (+ 1 (* x y)))`

` (b (- 1 y)))`

` (+ (* x (square a))`

` (* y b)`

` (* a b))))`

