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
    

