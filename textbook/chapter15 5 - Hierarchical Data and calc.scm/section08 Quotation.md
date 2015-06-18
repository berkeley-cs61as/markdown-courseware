This section is a short review and overview of the `quote` function (more commonly seen as `'`) and its functionalities to help you prep for the next section, `calc.rkt`.

## Refresher

We have used quotation `'` as a shortcut to create words and sentences since the beginning of this class. The example below should be painstakingly simple to understand:

    
    > (define a 3)
    3
    
    > a
    3
    
    > 'a
    a
    

The use of a single quote is actually a shortcut - `'a` is equivalent to
`(quote a)`. Similarly, `'(a 1 b 2)` is equivalent to `(quote (a 1 b 2))`

**Test Your Understanding**

<div class="mc">
The function quote (') is a special form.

<ans text="True" explanation="If quote were not a special form. Then, when we call (quote a) above, Racket will evaluate the argument first, simplifying the expression to (quote 3) and thus returning '3. That's not right!" correct></ans>
<ans text="False" explanation=""></ans>
<!-- and so on -->
</div>

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
(i.e., it is not `eq?` to any item in the list), then `memq` returns `false`.
Otherwise, it returns the sublist of the list beginning with the first
occurrence of the symbol:

    
    
    >(memq 'apple '(banana raspberry windows android))
    #f
    >(memq 'apple '(banana raspberry windows apple android))
    (apple android)
    >(memq 'apple '(banana raspberry windows (apple android))
    #f

Note that the last example returns `#f` because `(eq? 'apple '(apple
android))` returns #f. Thus, `memq` does not work on deep lists.

You can implement `memq` with the following definition:
    
    
    (define (memq item x)
      (cond ((null? x) false)
            ((eq? item (car x)) x)
            (else (memq item (cdr x)))))
    
**Test Your Understanding**

<div class="mc">
What does the following expression return?

<pre><code>(memq 'everything '(sugar spice (everything nice)))</code></pre>
<ans text="(everything nice)" explanation=""></ans>
<ans text="everything" explanation=""></ans>
<ans text="#f" explanation="memq does not work on deep lists, and cannot find elements on a deeper level." correct></ans>
<!-- and so on -->
</div>    

<div class="mc">
What does the following expression return?

<pre><code>(memq 'chicken '(cow chicken cow and chicken))</code></pre>
<ans text="(chicken cow and chicken)" explanation="If you take a look at the code for memq, we start fromt he beginning of list x and stop once we find item. That means that we will return immediately after the first instance of item in x." correct></ans>
<ans text="(chicken)" explanation=""></ans>
<ans text="#f" explanation=""></ans>
<!-- and so on -->
</div>  

## What Will Racket Print?

For each of the following expressions, predict what Racket will print without using the interpreter. Then, use the interpreter to check your answers.

    * `(list 'a 'b 'c)`
    * `(list (list 'george))`
    * `(cdr '((x1 x2) (y1 y2)))`
    * `(cadr '((x1 x2) (y1 y2))`
    * `(pair? (car '(a short list)))`
    * `(memq 'red '((red shoes) (blue socks)))`
    * `(memq 'red '(red shoes blue socks))`

## Takeaways

In this subsection, you learned:

  * `'hi` is a shorcut for `(quote hi)`.
  * `memq` is a predicate that determines whether a symbol is in a list.

