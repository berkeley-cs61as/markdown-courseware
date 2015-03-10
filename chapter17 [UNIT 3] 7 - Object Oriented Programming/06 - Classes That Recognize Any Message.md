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

## Message and Args

Notice that in the default-method above, we used **message** to find out what
message we passed in to our object. Similarly, we can also use **args** to
find out what other arguments are passed as a list.

Call message args

(ask jack 'do-math 1 2 5 10)

'do-math

(1 2 5 10)

(ask jack 'dance 'salsa)

'dance

'(salsa)

(ask jack 'swim)

'swim

nil

