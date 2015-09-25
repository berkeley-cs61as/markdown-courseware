Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw6.rkt .

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw6.rkt).

## Autograder

To run the autograder on your computer, download the test file [here](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw6-tests.rkt).
Follow the instructions from previous lessons.

## Exercise 0
**Exercise 0 consists of problems from the lesson. Highly recommended to do. This is NOT for credit.**
  
Load the racket-1 interpreter from the file

`~cs61as/lib/racket1.rkt `

To start the interpreter, type `(racket-1)`. Familiarize yourself with it by
evaluating some expressions. Remember: you have all the Racket primitives for
arithmetic and list manipulation; you have lambda but not higher-order
functions; you don't have define. To stop the racket-1 interpreter and return
to Racket, just evaluate an illegal expression, such as `()`.

0a. Trace in detail how a simple procedure call such as

`((lambda (x) (+ x 3)) 5) `

is handled in racket-1.

0b. Try inventing higher-order procedures; since you don't have define you'll
have to use the Y-combinator trick, like this:

    Racket-1:
    ((lambda (f n)  ; this lambda is defining MAP 
    	((lambda (map) (map map f n)) 
        (lambda (map f n) 
            (if (null? n) 
                '() 
                (cons (f (car n)) (map map f (cdr n))) )) )) ;end of lambda defining MAP 
    first              ; the argument f for MAP
    '(the rain in spain)) ; the argument n for MAP
    
    (t r i s)

0c. Since all the Racket primitives are automatically available in racket-1,
you might think you could use Racket's primitive map function. Try these
examples:

    Racket-1: 
    (map first '(the rain in spain))`

    Racket-1: 
    (map (lambda (x) (first x)) '(the rain in spain))

Explain the results.

0d. Modify the interpreter to add the and special form. Test your work. Be
sure that as soon as a false value is computed, your and returns #f without
evaluating any further arguments.

## Exercise 1
  
Complete the following:

Abelson & Sussman, exercises [2.74, 2.75, 2.76](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-17.html#%25_thm_2.74), [2.77, 2.79,
2.80](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-18.html#%25_thm_2.77), [2.81, 2.83
](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-18.html#%25_thm_2.81)

Note: Some of these are thought-exercises; you needn't actually run any Scheme
programs for them! (Some don't ask you to write procedures at all; others ask
for modifications to a program that isn't online.)

## Exercise 2

  
Write a `map` primitive for `racket-1` (call it `map-1` so you and Racket
don't get confused about which is which) that works correctly for all mapped
procedures.

## Exercise 3

Modify the `racket-1` interpreter to add the `let` special form. Hint: Like a
procedure call, `let` will have to use `substitute` to replace certain
variables with their values. Don't forget to evaluate the expressions that
provide those values!

## Exercise 4
  
[SICP ex. 2.62 ](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-16.html#%25_thm_2.62)

This will help: [SICP 2.3.3](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-16.html#%_sec_2.3.3)

## Exercise 5.

  
The file `~cs61as/lib/bst.scm` contains the binary search tree procedures from
SICP 2.3.3. Using adjoin-set, construct the [trees shown on page
156](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-16.html#%_fig_2.16).

## Extra for Experts: Exercise 6

**Do this if you want to. This is NOT for credit.**
  
Another approach to the problem of type-handling is type inference. If, for
instance, a procedure includes the expression `(+ n k)`, one can infer that
`n` and `k` have numeric values. Similarly, the expression` (f a b)` indicates
that the value of f is a procedure. Write a procedure called inferred-types
that, given a definition of a Scheme procedure as argument, returns a list of
information about the parameters of the procedure. The information list should
contain one element per parameter; each element should be a two-element list
whose first element is the parameter name and whose second element is a word
indicating the type inferred for the parameter. Possible types:

    
    ? (the type can't be inferred)
    
    procedure (the parameter appeared as the first word in an unquoted expression or as the first argument of map or every)
    
    number (the parameter appeared as an argument of +, -, max, or min)
    
    list (the parameter appeared as an argument of append or as the second argument of map or member)
    
    sentence-or-word (the parameter appeared as an argument of first, butfirst, sentence, or member?, or as the second argument of every)
    
    x (conflicting types were inferred)
    
    

You should assume for this problem that the body of the procedure to be
examined does not contain any occurrences of `if` or `cond`, although it may
contain arbitrarily nested and quoted expressions. (A more ambitious inference
procedure both would examine a more comprehensive set of procedures and could
infer conditions like "nonempty list".) Here's an example of what your
inference procedure should return.

    
    (inferred-types
        '(define (foo a b c d e f)
            (f (append (a b) c '(b c))
               (+ 5 d)
               (sentence (first e) f)) ) )
    
    

should return

    
    ((a procedure) (b ?) (c list) (d number)
     (e sentence-or-word) (f x)) 
    

If you're really ambitious, you could maintain a database of inferred argument
types and use it when a procedure you've seen is invoked by another procedure
you're examining!

## Submit Your Homework!

For instructions, see [this guide](../submit.html). It covers basic terminal commands and assignment submission.

If you have any trouble submitting, do not hesitate to ask a TA!
