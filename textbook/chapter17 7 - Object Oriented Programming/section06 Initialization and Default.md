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
    

A penguin has 2 instance variables: its `hunger` and `weight`. The penguin class has 2 class variables: its favorite food which is `tuna`, and `all-penguin` which is a list of all names of penguins ever created. Currently, `all-penguin` is never updated. On some occassions like this, we want our objects to do a certain thing when it is created. We can do this with the **`initialize`** clause.

![](http://wikimotive.com/wp-content/uploads/sites/2/2013/05/Cute-Penguin-
Wallpaper-2013.jpg)

## Right After Instantiate

As soon as a Penguin object is instantiated, we want him to:

  1. Say his name and
  2. add himself to the `all-penguin` list. Here is how we do it with the initialize clause:

    
    
<pre><code>(define-class (penguin name)
    (class-vars (all-penguin nil)
                (favorite-food tuna))
    (instance-vars (hunger 50)
                   (weight 350))
    <strong>(initialize (print (se '(hi my name is) name))
                (set! all-penguin (cons name all-penguin)))</strong>
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
(jennie jack)</code></pre>

## The Default Method

So this is our definition of the Penguin class that we have so far:

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

Let's say we call the following methods:

    > (define jack (instantiate penguin 'jack))
    (hi my name is jack)

    > (ask jack 'favorite-food)
    tuna

    > (ask jack 'eat)
    (That tuna was delicious!)

    > (ask jack 'back-flip)
    *** Error: No method back-flip in class penguin

It looks like `jack` doesn't know how to `back-flip`. Our penguins only know a handful of messages right now, but as the designer of the penguin class, we don't want them to throw an error for every other message. Instead, if a penguin sees a message it doesn't understand we want them to eat instead. We can do this with the **default-method** clause. Take a look at the addition to our Penguin class:

<pre><code>(define-class (penguin name)
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
    <strong>(default-method
        (print (se '(I dont know how to) message '(I will eat instead)))
        (ask self 'eat)))</strong></code></pre>

And now we call these methods:

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

Notice that in the default-method above, we used message to find out what message we passed in to our object. Similarly, we can also use args to find out what other arguments are passed as a list.

For example, if we call

    (ask jack 'do-math 1 2 5 10)

Then, the variable `message` will point to `'do-math`, while the variable `args` will point to `(1 2 5 10)`.