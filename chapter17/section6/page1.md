## Default Method

This is what we have so far:

    
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
            (se 'That favorite-food '(was delicious!))))
    
    
    > (define jack (instantiate penguin 'jack))
    (hi my name is jack)
    
    > (ask jack 'favorite-food)
    tuna
    
    > (ask jack 'eat)
    (That tuna was delicious!)
    
    > (ask jack 'back-flip)
    *** Error:
        No method back-flip in class penguin
    

Woops, we just asked our `penguin` to do something it doesn't know. Our
`penguin`s only know a handful of messages right now, but as the designer of
the `penguin` class, we don't want them to throw an error for every other
message. Instead, if a `penguin` sees a message it doesn't understand we want
them to `eat` instead. We can do this with the **default-method** clause.

