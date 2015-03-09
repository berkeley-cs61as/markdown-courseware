## Enumerate for Trees

For our tree-version of enumerate, we need a function that accepts a tree, and
returns a list with all of the leaves, so that it is compatible with our `map`
and `filter.`

    
    
    (define (enumerate-tree tree)
      (cond ((null? tree) nil)
            ((not (pair? tree)) (list tree))
            (else (append (enumerate-tree (car tree))
                          (enumerate-tree (cdr tree))))))
    

