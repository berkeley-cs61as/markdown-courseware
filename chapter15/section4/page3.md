## example: count-leaves

To count the leaves of a tree, we write `count-leaves` procedure using mutual
recursion. If the node is a leaf node, then just return 1. Otherwise, it calls
another function `count-leaves-in-forest` that counts the number of leaves in
the forest of the tree. Then `count-leaves-in-forest` looks at the `car` of
`forest`. What is it? It is a tree! So we call `count-leaves` on `(car
forest)`, count the number of leaves of the rest of the forest (which still is
a forest) by calling `(count-leaves-in-forest (cdr forest))`, and then add the
two together to get the total number of leaves in the forest.`

`

    
    (define (count-leaves tree)
      (if (leaf? tree)
          1
          (count-leaves-in-forest (children tree))))
     
    (define (count-leaves-in-forest forest)
      (if (null? forest)
          0
          (+ (count-leaves (car forest))
             (count-leaves-in-forest (cdr forest)))))
    

