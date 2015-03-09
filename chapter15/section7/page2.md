## Elements-of-set

We can formalize our algorithm for finding if an element is in a set as the
following code:

    
    
    (define (element-of-set? x set)
      (cond ((null? set) false)
            ((= x (entry set)) true)
            ((< x (entry set))
             (element-of-set? x (left-branch set)))
            ((> x (entry set))
             (element-of-set? x (right-branch set)))))
    

