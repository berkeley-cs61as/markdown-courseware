## Implementing Serializers with Mutexes

Now that we know about mutexes and how to use them, it is relatively
straightforward to implement serializers. Our implementation is below. Make
sure you understand how and why it works!

    
    
    (define (make-serializer)
      (let ((mutex (make-mutex)))
        (lambda (p)
          (define (serialized-p . args)
            (mutex 'acquire)
            (let ((val (apply p args)))
              (mutex 'release)
              val))
          serialized-p)))
    

