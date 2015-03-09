## Exercise 5.

This lab activity consists of example programs for you to run in Scheme.
Predict the result before you try each example. If you don't understand what
Scheme actually does, ask for help! Don't waste your time by just typing this
in without paying attention to the results.

    
    (define (make-adder n)                       ((lambda (x) 
      (lambda (x) (+ x n)))                         (let ((a 3)) 
                                                      (+ x a))) 
    (make-adder 3)                                5) 
     
    ((make-adder 3) 5)                           (define k 
                                                   (let ((a 3)) 
    (define (f x) (make-adder 3))                    (lambda (x) (+ x a)))) 
     
    (f 5)                                        (k 5) 
     
    (define g (make-adder 3))                    (define m 
                                                   (lambda (x) 
    (g 5)                                            (let ((a 3)) 
                                                       (+ x a)))) 
    (define (make-funny-adder n)        
      (lambda (x)                                (m 5) 
        (if (equal? x 'new)             
            (set! n (+ n 1))                     (define p 
            (+ x n))))                             (let ((a 3)) 
                                                     (lambda (x) 
    (define h (make-funny-adder 3))                    (if (equal? x 'new) 
                                                           (set! a (+ a 1)) 
    (define j (make-funny-adder 7))                        (+ x a))))) 
     
    (h 5)                                        (p 5) 
     
    (h 5)                                        (p 5) 
     
    (h 'new)                                     (p 'new) 
     
    (h 5)                                        (p 5) 
     
    (j 5)                                        (define r 
                                                   (lambda (x) 
    (let ((a 3))                                     (let ((a 3)) 
      (+ 5 a))                                         (if (equal? x 'new) 
                                                           (set! a (+ a 1)) 
    (let ((a 3))                                           (+ x a))))) 
      (lambda (x) (+ x a)))             
                                                 (r 5) 
    ((let ((a 3))                       
       (lambda (x) (+ x a)))                     (r 5) 
     5)                                 
                                                 (r 'new) 
     
                                                 (r 5)                 
     
    (define s                                    (define (ask obj msg . args) 
      (let ((a 3))                                 (apply (obj msg) args)) 
        (lambda (msg)                             
          (cond ((equal? msg 'new)               (ask s 'add 5) 
                 (lambda ()                       
                   (set! a (+ a 1))))            (ask s 'new) 
                ((equal? msg 'add)                
                 (lambda (x) (+ x a)))           (ask s 'add 5) 
                (else (error "huh?"))))))         
                                                 (define x 5) 
    (s 'add)                                      
                                                 (let ((x 10) 
    (s 'add 5)                                         (f (lambda (y) (+ x y)))) 
                                                   (f 7)) 
    ((s 'add) 5)                                  
                                                 (define x 5) 
    (s 'new)                                      
     
    ((s 'add) 5)                                  
     
    ((s 'new))                                    
     
    ((s 'add) 5) 

