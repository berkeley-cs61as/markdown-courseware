## Flatmap

Calling `accumulate` with `append` is so common that Scheme implements this
for us in the procedure called `flatmap`

    
    (define (flatmap proc seq)
      (accumulate append nil (map proc seq)))

Using this definition, we can finally write the function that Jack wants:

    
    (flatmap (lambda (y) 
                 (map (lambda (x) (cons x y))
                      (enumerate 1 4)))
             (enumerate 1 4))
    
    
     

