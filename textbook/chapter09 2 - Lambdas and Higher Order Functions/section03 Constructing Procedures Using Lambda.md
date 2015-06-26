In the previous section, you may have noticed that sum-doubles had a slightly
different definition than sum-cubes or sum-squares:

    
    (define (sum-doubles a b)
      (define (double x) (* 2 x))
      (sum double a b))

There is no double function available, so we have to define our own, for a
one-time use.

But that's really annoying! Can't we just create a function on the spot?

Actually, yes. We can do it using the special form `lambda`, which creates
procedures.

The general form for lambda is:

`(lambda (<arg1> <arg2> ... <argn>) <body>)`

The procedure double, for example can be described as:

`> (lambda (x) (* 2 x))`

This is the same thing as defining double and then checking its value:

    
    > (define (double x) (* 2 x))
    > double  
      
    You can think of lambda as "the function of ... that returns ...". For example, the above lambda would be "the function of x that returns (* 2 x)"
    

In fact, using lambda, we can equivalently define double as follows:

`(define double (lambda (x) (* 2 x)))`

And now, we can rewrite sum-doubles as:

    
    (define (sum-doubles a b)
      (sum (lambda (x) (* 2 x)) a b)) 

**Note:** The value returned by `lambda` is a procedure, just as much as one made with `define`.


Try at least these expressions using Racket in terminal:

    
    (lambda (x) (+ x 3))  
    ((lambda (x) (+ x 3)) 7)  
    (define add3 (lambda (x) (+ x 3)))  
    (add3 7)
    
    (define (square x) (* x x))   
    (square 5)   
    (define sq (lambda (x) (* x x)))   
    (sq 5)   
    ((lambda (x y) (+ (* 2 x) (* 5 y))) (* 100 100) (* 5 2))  
    

