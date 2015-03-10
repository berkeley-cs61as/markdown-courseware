Another use of lambda is in creating local variables. Those are very nice to
have, especially for making code readable.

For example, suppose we wish to compute the function

[mathjax]f(x,y) = x(1+xy)^2 + y (1-y) + (1+xy)(1-y)[/mathjax]

which we could also express as

[mathjaxinline]\displaystyle a[/mathjaxinline]

[mathjaxinline]\displaystyle = 1 + xy[/mathjaxinline]

[mathjaxinline]\displaystyle b[/mathjaxinline]

[mathjaxinline]\displaystyle = 1 -y[/mathjaxinline]

[mathjaxinline]\displaystyle f(x,y)[/mathjaxinline]

[mathjaxinline]\displaystyle = x a^2 + y b + a b[/mathjaxinline]

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

The general form of a let expression is

`(let ((<_var1_> <_exp1_>)`

` (<_var2_> <_exp2_>)`

` ![](http://mitpress.mit.edu/sicp/full-text/book/book-Z-G-D-18.gif)`

` (<_var_n__> <_exp_n__>))`

` <_body_>)`

Remember, underneath, this is nothing more than a lambda call:

`((lambda (`<_var1_> <_var2_> ... <_varn_>) <_body_>)

<_exp1_> <_exp2_> ... <_expn_> )

Here's an interpreter for you to check out lambda.

Try at least these expressions.

(Note: a semicolon denotes a comment, scheme will ignore the rest of the line
after a semicolon.)

    
    (define y 10)  
    (let ((y 0)) y) ;; notice that let overrides global vars  
    (let ((x 10)  
          (z x))   
        z) ;; this will break, translate to lambda to see why  
    (let ((a 1))  
      (let ((a 2))  
        (let ((a 3))  
           a) )) ;; nested lets are valid.   
    (let ((test 'wait-what?))  
      5)  
    test  ;; let only binds variables inside its body  
    (let ((a 1))  
      (+ a (let ((a 2))  
        (+ a (let ((a 3))  
              a) ) ) ) )   
    ;; challenge: figure out what that last one returns, before checking interpreter  
     

