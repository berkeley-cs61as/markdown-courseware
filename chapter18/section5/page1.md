## Counter Example

Now let's implement a simple counter. Every time the `counter` is called, it
increments its own local variable and the global variable for all counters.
Here is the code for our counter class:

    
    (define make-counter
        (let ((glob 0))
            (lambda ()
                (let ((loc 0))
                    (lambda ()
                        (set! loc (+ loc 1))
                        (set! glob (+ glob 1))
                        (list loc glob))))))
    

It works something like this:

    
    > (define counter1 (make-counter))
    counter1
    
    > (define counter2 (make-counter))
    counter2
    
    > (counter1)
    (1 1)
    
    > (counter1)
    (2 2)
    
    > (counter2)
    (1 3)
    
    > (counter1)
    (3 4)
    

The class variable `glob` is created in an environment that surrounds the
creation of the outer lambda, which represents the entire class. The instance
variable `loc` is created in an environment that's inside the class lambda,
but outside the second lambda that represents an instance of the class.

