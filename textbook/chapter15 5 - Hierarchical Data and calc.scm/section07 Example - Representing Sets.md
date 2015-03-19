## Intro to Sets

We have seen how we can use lists or trees to introduce hierarchy to our
structure. Sometimes we don't care about a structure's hierarchy; we only need
to know if a certain data is in the structure. One useful structure for this
is a set; a collection of unique data. A set doesn't have duplicates. For
example '(cats dogs bears squirrels cats) is not a set because cats appear
twice. In contrast, '(cats dogs bears squirrels) is a set.

Looking forward, here are some functions that we will define for the Set ADT:

  * `element-of-set?` checks if a certain data is in a set
  * `adjoin-set` adds a new data to a set.
  * `intersection-set` given two sets, returns a new set which contains elements that are in both sets

## element-of-set

One way to implement a set is to use a list where each element only appears
once. We will use the empty list, `nil` to represent the empty set. We can
then implement `element-of-set` as:

    
    
    (define (element-of-set? x set)
      (cond ((null? set) #f)
            ((equal? x (car set)) #t)
            (else (element-of-set? x (cdr set)))))
    

This code is similar to `memq`. We used `equal?` because the member of a set
can be a number, symbol, or anything else.

## adjoin-set

Let us move on to `adjoin-set`! If an item that we are inserting is already in
the set, do nothing. Otherwise, add that element to the set

    
    
    (define (adjoin-set x set)
      (if (element-of-set? x set)
          set
          (cons x set)))
    

## Intersection-Set

How will we do intersection of `set1` and `set2`? We can approach this
recursively. The simplest case would be if either set is empty; we can just
return nil. We can then make the problem smaller by checking if `(car set1)`
is in `set2`. If it is, then include that element in our answer and
recursively check if the rest of `set1` is in` set2`. If it is not in `set2`,
recursively check if the rest of the elements in `set1` are in `set2.`

    
    
    (define (intersection-set set1 set2)
      (cond ((or (null? set1) (null? set2)) '())
            ((element-of-set? (car set1) set2)        
             (cons (car set1)
                   (intersection-set (cdr set1) set2)))
            (else (intersection-set (cdr set1) set2))))
    
    
     

## Set as an Orderded List

You might have noticed that our previous implementation of the set ADT is
relatively slow. This is partly because our sets are not ordered. We can make
it faster by enforcing the rule that the set needs to store data in increasing
order. So `(1 3 4)` is valid whereas `(1 5 3 4)` is not.

## element-of-set?

One advantage of an ordered list is that we don't have to scan the whole set
to find if something is in the list. If we are going through the list and find
that the item we want to put in is smaller than the rest of the list, we know
in advance that our item is not in the list. Our code for `element-of-set?`
will then be as follows:

    
    
    (define (element-of-set? x set)
      (cond ((null? set) false)
            ((= x (car set)) true)
            ((< x (car set)) false)
            (else (element-of-set? x (cdr set)))))
    

Note that we are assuming all the elements in our set are numbers. If this is
not the case, the above code will error.

## Intersection-set

With the new implementation, we can make `intersection-set` faster but we have
to change our logic. When we are calling `(intersection-set set1 set2)` we can
break all possible cases as follows:

  * **`(= (car set1) (car set2))`:** Since they share the same element, we include this element in our answer and check the rest `(intersection-set (cdr set1) (cdr set2))`
  * **`(< (car set1) (car set2))`:** Since `(car set2)` is the smallest element in `set2`, we can directly conclude that `(car set1)` is not in `set2` and therefore not in the intersection. We can continue searching with the next largest in `set1 (intersection-set (cdr set1) set2)`
  * **`(> (car set1) (car set2)`:** This will be the mirror image of above. Since `(car set1)` is the smallest member in `set1`, we know that in advance that `(car set2)` is nowhere in `set1` and therefore not in the intersection. We can continue searching with the next largest member in `set2` `(intersection-set set1 (cdr set2))`

The complete code can be written as follows:

    
    
    (define (intersection-set set1 set2)
      (if (or (null? set1) (null? set2))
          '()    
          (let ((x1 (car set1)) (x2 (car set2)))
            (cond ((= x1 x2)
                   (cons x1
                         (intersection-set (cdr set1)
                                           (cdr set2))))
                  ((< x1 x2)
                   (intersection-set (cdr set1) set2))
                  ((< x2 x1)
                   (intersection-set set1 (cdr set2)))))))
    

## Set as Binary Tree

"I want to go faster"

If you want to make your set work faster, we have to change the way we store
it to allow faster check/access. We can do this by using a **binary tree **(or
trees with two branches); each node of a tree holds one element of a set
(called the entry of that node), and branches to two other (possibly empty)
nodes. The left branch points to another tree which has elements smaller than
the entry node. The right branch points to another tree which has elements
larger than the entry node. Note: in binary trees that allow duplicates, the
programmer of the ADT should choose on which branch elements equal to the
entry node should reside.

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-51.gif)

So how does this make it faster? Imagine that you are working with the
leftmost tree, and wants to check if '11' is in the set. We start from the
top-most node, which has '7'. We know that everything on the left-branch of
'7' is smaller than '7' and everything on the right-branch of '7' is larger
than '7'. The number we are looking at,'11' is larger than '7' so we go down
the right branch. Notice that we don't need to touch the left-branch at all
and can ignore (approximately) half of the elements in the tree. We repeat
this process until we find our number. So since we are at the node with '9',
and we want to find '11' which is larger, we go to the right branch, arriving
at the node we are looking for.

The huge leap here is made when we can ignore half of the tree after every
comparison, which leads us to a running time of Θ(log n). For example, in a
tree with 8 nodes, we just need 3 comparisons max until we reach any leaf. In
a tree with 16 nodes (double the previous one), we just need 4 comparisons
(just 1 more comparison!) until we can reach any leaf.

## Implementing a Binary Tree

One way to implement a binary tree is by using a list where the first item is
the element, the second item is the left subtree and the third item is the
right subtree.

    
    
    (define (entry tree) (car tree))
    (define (left-branch tree) (cadr tree))
    (define (right-branch tree) (caddr tree))
    (define (make-tree entry left right)
      (list entry left right))
    

## Elements-of-set

We can formalize our algorithm for finding if an element is in a set as the
following code:

    
    
    (define (element-of-set? x set)
      (cond ((null? set) false)
            ((= x (entry set)) true)
            ((< x (entry set))
             (element-of-set? x (left-branch set)))
            ((> x (entry set))
             (element-of-set? x (right-branch set)))))
    

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
    

## Unbalanced Tree

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-52.gif)

The image above is the result of adding the elements 1, 2, 3, 4, 5, 6, 7 in
order to an empty tree. (Make sure you try this out with pen and paper to see
that this is the case). We say that this tree is **unbalanced** because one
side of the tree has way more elements than the other.

## DIFFERENT TYPES OF TREES

Previously, we saw how nodes in a tree can have an arbitary number of
children. These types of trees are sometimes called N-way trees. For N-way
trees, we store the children of the tree as a forest, or a list of trees. We
retrieve this forest through the selector `(children <tree>).`

In the previous section, we saw a more specific type of tree, "Binary Trees".
Each node in this tree has at most 2 children. They can be accessed with
`(left-branch <tree>)` and` (right-branch <tree>)`. The constructor for a
binary tree is also different than the constructor for an N-way tree.

When you are working with trees, find out what kind of tree you are working
with and work with the  constructors and selectors that the question provide.
The constructors and selectors for a binary tree would not work at all on an
N-way tree!

## Takeaways

A set is a particular data structure where each element appears only once.
There are multiple ways to represent Sets (as with basically all data
structures). The choice of representation affects the run time of different
functions.

