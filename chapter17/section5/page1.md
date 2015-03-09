## Initialization

Glance through the `penguin` class:

    
    (define-class (penguin name)
        (class-vars (all-penguin nil)
                    (favorite-food 'tuna))
        (instance-vars (hunger 50)
                       (weight 350))
        (method (eat)
            (set! hunger (- hunger 1))
            (set! weight (+ weight 5))
            (se 'That favorite-food '(was delicious!))))
    
    
    > (define jack (instantiate penguin 'jack))
    
    > (ask jack 'eat)
    (that tuna was delicious!)
    
    > (ask jack 'hunger)
    49
    
    > (ask jack 'weight)
    355
    

A penguin has 2 instance variables: its `hunger` and `weight`. The penguin
class has 2 class variables: its favorite food which is `tuna`, and `all-
penguin` which is a list of all names of penguins ever created. Currently,
`all-penguin` is never updated. On some occassions like this, we want our
objects to do a certain thing when it is created. We can do this with the
**initialize** clause.

![](http://wikimotive.com/wp-content/uploads/sites/2/2013/05/Cute-Penguin-
Wallpaper-2013.jpg)

