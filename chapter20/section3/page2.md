## Deleting from a Queue

To delete from a queue, we can simply change the `front-ptr` to point to the
next pair.

    
    
    (define (delete-queue! queue)
      (cond ((empty-queue? queue)
             (error "DELETE! called with an empty queue" queue))
            (else
             (set-front-ptr! queue (cdr (front-ptr queue)))
             queue))) 
    

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-20.gif)

If starting from the queue above we decide to delete the first time, the
change will only be where the `front-ptr` points to:

![](http://mitpress.mit.edu/sicp/full-text/book/ch3-Z-G-21.gif)

