## Right after Instantiate

As soon as a Penguin object is instantiated, we want him to: (1) Say his name
and (2) add himself to the `all-penguin` list. Here is how we do it with the
initialize clause:

    
    
    (define-class (penguin name)
        (class-vars (all-penguin nil)
                    (favorite-food tuna))
        (instance-vars (hunger 50)
                       (weight 350))
    	**
        (initialize (print (se '(hi my name is) name))
                    (set! all-penguin (cons name all-penguin)))
    **
        (method (eat)
            (set! hunger (- hunger 1))
            (set! weight (+ weight 5))
            (se 'That favorite-food '(was delicious!))))
    
    > (define jack (instantiate penguin 'jack))
    (hi my name is jack)
    
    > (define jennie (instantiate penguin 'jennie))
    (hi my name is jennie)
    
    > (ask penguin 'all-penguin)
    (jennie jack)
    
    > (ask jack 'all-penguin)
    (jennie jack)
    

