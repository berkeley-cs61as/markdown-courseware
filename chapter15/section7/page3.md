## Adding an Element

How do you add an element to a binary tree? You follow the same algorithm as
when you are finding an element. You need to decide whether to add the new
element x in the leaf of the left subtree or the right subtree.

  * If the tree is empty, make a tree with node x, and empty left and right branches
  * If x is equal to the node of the tree, return the tree (this means x is already in the tree so we don't need to make any changes
  * If x is less than the node of the tree, go to the left subtree
  * If x is larger than the node of the tree, go to the right subtree
    
    
    (define (adjoin-set x set)
      (cond ((null? set) (make-tree x '() '()))
            ((= x (entry set)) set)
            ((< x (entry set))
             (make-tree (entry set) 
                        (adjoin-set x (left-branch set))
                        (right-branch set)))
            ((> x (entry set))
             (make-tree (entry set)
                        (left-branch set)
                        (adjoin-set x (right-branch set))))))
    

