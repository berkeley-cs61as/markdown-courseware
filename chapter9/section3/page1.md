Here's an interpreter for you to check out lambda.

Try at least these expressions:

    
    (lambda (x) (+ x 3))  
    ((lambda (x) (+ x 3)) 7)  
    (define add3 (lambda (x) (+ x 3)))  
    (add3 7)
    
    (define (square x) (* x x))   
    (square 5)   
    (define sq (lambda (x) (* x x)))   
    (sq 5)   
    ((lambda (x y) (+ (* 2 x) (* 5 y))) (* 100 100) (* 5 2))  
    

