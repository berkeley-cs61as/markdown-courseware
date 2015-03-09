## A New Example System

As the last section mentioned, the "keys" for our table must be a list of
types if we want to continue to use our arithmetic example. Instead of dealing
with this unnecessary complexity right now, we're going to switch to a
friendlier example that should be a little easier to follow. However, all of
the big ideas are exactly the same.

Our data types will be squares and circles; our operations will be area and
perimeter. For some comparison (and review) the type-tag version of these
operations would be written:

    
    (define pi 3.141592654)
    
    (define (make-square side)
        (attach-tag 'square side))
    
    (define (make-circle radius)
        (attach-tag 'circle radius))
    
    (define (area shape)
        (cond ((eq? (type-tag shape) 'square)
               (* (contents shape) (contents shape)))
              ((eq? (type-tag shape) 'circle)
               (* pi (contents shape) (contents shape)))
              (else (error "Unknown shape -- AREA"))))
    
    (define (perimeter shape)
        (cond ((eq? (type-tag shape) 'square)
               (* 4 (contents shape)))
              ((eq? (type-tag shape) 'circle)
               (* 2 pi (contents shape)))
              (else (error "Unknown shape -- PERIMETER"))))
    

You should be able to completely understand the above code! We'll be using
this example with squares and circles throughout the rest of the lesson.

