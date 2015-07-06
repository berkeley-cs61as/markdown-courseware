## What is Message Passing?

In conventional style, the operators are represented as functions that know
about the different types; the types themselves are just data. In Data-Directed-Programming, the
operators and types are all data, and there is one universal operate function
that does the work. We can also stand conventional style on its head,
representing the types as functions and the operations as mere data.

In fact, not only are the types functions, but so are the individual data
themselves. That is, there is a function (`make-circle` below) that represents
the circle type, and when you invoke that function, it returns a function that
represents the particular circle you give it as its argument. Each circle is
an object and the function that represents it is a dispatch procedure that
takes as its argument a message saying which operation to perform.

The new definitions of `make-square` and `make-circle` are below.

    
    (define (make-square side)
        (lambda (message)
            (cond ((eq? message 'area)
                   (* side side))
                  ((eq? message 'perimeter)
                   (* 4 side))
                  (else (error "Unknown message")))))
    
    (define (make-circle radius)
        (lambda (message)
            (cond ((eq? message 'area)
                   (* pi radius radius))
                  ((eq? message 'perimeter)
                   (* 2 pi radius))
                  (else (error "Unknown message")))))
    
    (define square5 (make-square 5))
    
    (define circle3 (make-circle 3))
    

## Why is Message Passing Important?

Message passing may seem like an overly complicated way to handle this problem
of shapes, but we'll see in the next lesson that it's one of the key ideas in
creating object-oriented programming. Message passing becomes much more
powerful when combined with the idea of local state that we'll learn next
week.

We seem to have abandoned tagged data; every shape type is just some function,
and it's hard to tell which type of shape a given function represents. We
could combine message passing with tagged data, if desired, by adding a `type`
message that each object understands.

    
    (define (make-square side)
        (lambda (message)
            (cond ((eq? message 'area)
                   (* side side))
                  ((eq? message 'perimeter)
                   (* 4 side))
                  ((EQ? MESSAGE 'TYPE) 'SQUARE)
                   (else (error "Unknown message")))))
    

