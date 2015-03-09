## count-leaves code

Using the pseudo-code from the previous page and the `pair?` function above,
we can write the complete code for `count-leaves`:

    
    
    (define (count-leaves x)
        (cond ((null? x) 0)
              ((not (pair? x)) 1)
              (else (+ (count-leaves (car x))
                       (count-leaves (cdr x)))))
    

