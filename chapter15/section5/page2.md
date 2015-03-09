## Enumerate for Lists

Enumerate will return a list given a lower and a higher range.

  * `(enumerate-interval 0 5)` returns ` (0 1 2 3 4 5)`
  * `(enumerate-interval 10 13) ` returns `(10 11 12 13) `

You can define enumerate (for lists) as:

    
    
    (define (enumerate-interval low high)
      (if (> low high)
          nil
          (cons low (enumerate-interval (+ low 1) high))))
    

