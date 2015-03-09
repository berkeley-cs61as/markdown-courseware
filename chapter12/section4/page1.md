## Recursive Processes

The following `reverse` function generates a recursive process:

    
            
              (define (reverse sent)
                (if (empty? sent)
                    '()
                    (se (last sent) (reverse (bl sent)))))
            
          

The running time for this function is \( 5N + 2 \) since it has five constant-
runtime operations: `if, empty?, se, last`, and `bl`. Thus the order of growth
of its running time is \( \Theta(n) \).

Now assume that we call `reverse` with an argument `'(Today was a fairytale)`.

The function call `(reverse '(Today was a fairytale))` will then generate the
following processes:

    
    
          (se fairytale (reverse '(Today was a)))
          (se a (reverse '(Today was)))
          (se was (reverse '(Today)))
          (se Today (reverse '()))
          (se Today '())
          (se was '(Today))
          (se a '(was Today))
          (se fairytale '(a was Today))
          '(fairytale a was Today)

One problem with this recursive process is that it takes too much memory.
Along the process, scheme has to keep track of the pending computations: In
order to accomplish `(se fairytale (reverse '(Today was a)))`, it has to
reserve some memory for the unfinished task `(reverse '(Today was a)).
`Similarly, memory has to be reserved for` (reverse '(Today was)), (reverse
'(Today)),` and `(reverse '())`. Therefore, this function is \( \Theta(n) \)
in memory.

