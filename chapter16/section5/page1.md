## Practice with Scheme-1

Okay, so even though you just finished staring at the code, you probably don't
completely understand all of it yet. Let's go through a few exercises to
better acquaint you with the program.

  1. Manually trace through (in detail) how scheme-1 handles the following procedure call:  

    
         ((lambda (x) (+ x 3)) 5)

In particular, walk through all of the functions that scheme-1 must call to
evaluate this expression.

  2. Try inventing higher-order procedures; since you don't have define you'll have to use the Y-combinator trick, like this: 
    
         Scheme-1: ((lambda (f n)        ; this lambda is defining MAP 
                      ((lambda (map) (map map f n)) 
                       (lambda (map f n) 
                      (if (null? n) 
                          '() 
                          (cons (f (car n)) (map map f (cdr n))) )) )) 
                    first              ; here are the arguments to MAP 
                    '(the rain in spain)) 
                   (t r i s)
    

  3. Since all the Scheme primitives are automatically available in scheme-1, you might think you could use STk's primitive map function. Try these examples: 
    
        Scheme-1: (map first '(the rain in spain)) 
        Scheme-1: (map (lambda (x) (first x)) '(the rain in spain))
    

Explain the results.

  4. Modify the interpreter to add the `and` special form. Test your work. Be sure that as soon as a false value is computed, your `and` returns `#f` without evaluating any further arguments.

