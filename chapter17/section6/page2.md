## Eat all the thing

    
    (define-class (penguin name)
        (class-vars (all-penguin nil)
                    (favorite-food 'tuna))
        (instance-vars (hunger 50)
                       (weight 350))
        (initialize (print (se '(hi my name is) name))
                    (set! all-penguin (cons name all-penguin)))
        (method (eat)
            (set! hunger (- hunger 1))
            (set! weight (+ weight 5))
            (se 'That favorite-food '(was delicious!)))
      
    **    (default-method
            (print (se '(I dont know how to) message '(I will eat instead)))
            (ask self 'eat)))
    **
    > (define jack (instantiate penguin 'jack))
    (hi my name is jack)
    
    > (ask jack 'back-flip)
    (I dont know how to back-flip I will eat instead)
    (that tuna was delicious!)
    
    > (ask jack 'weight)
    355
    
    > (ask jack 'fly)
    (I don't know how to fly I will eat instead)
    (that tuna was delicious!)
    
    > (ask jack 'weight)
    360  
      
    
    

![](http://farm7.staticflickr.com/6205/6051390563_411371570f_z.jpg)

