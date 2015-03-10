## Refresher

We have used quotation `'` to create words and sentences since the beginning
of this class. We will explore its functionality more in depth in this
section.

    
    > (define a 3)
    3
    
    > a
    3
    
    > 'a
    a
    

The use of a single quote is actually a shortcut; typing `'a` is equivalent to
`(quote a)`. Similarly `'(a 1 b 2)` is equivalent to `(quote (a 1 b 2))`

## Predicates and Quotes

To check for equality, we can use the primitive `eq?`

    
    
    > (eq? 'a 'a)
    #t
    > (eq? 'a 'b)
    #f
    > (eq? 'a (first 'afro))
    #t
    
    

Another useful primitive for handling symbols/quotes is `memq`. `memq` takes
two arguments, a symbol and a list. If the symbol is not contained in the list
(i.e., is not `eq?` to any item in the list), then `memq` returns false.
Otherwise, it returns the sublist of the list beginning with the first
occurrence of the symbol

    
    
    >(memq 'apple '(banana raspberry windows android))
    #f
    >(memq 'apple '(banana raspberry windows apple android))
    (apple android)
    >(memq 'apple '(banana raspberry windows (apple android))
    #f

Note that in the last example, it returns false because `(eq? 'apple '(apple
android))` returns #f. `memq` only checks the 'first layer', so to speak.

You can implement `memq` with the following definition:

    
    
    (define (memq item x)
      (cond ((null? x) false)
            ((eq? item (car x)) x)
            (else (memq item (cdr x)))))
    
    

## What will scheme print?

For each of the following, type out what scheme will print. Use `#t` for true
and `#f` for false.

## takeaways

In this subsection, you learned:

  * `'hi` is a shorcut for `(quote hi)`
  * `memq?` is a predicate that determines whether a symbol is in a list

