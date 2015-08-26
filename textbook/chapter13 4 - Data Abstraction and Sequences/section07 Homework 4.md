## Template

Type the following into the terminal to copy the template file
to the current directory (note the period at the end):

    cp ~cs61as/autograder/templates/hw4.rkt .

Or you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw4.rkt).

## Autograder

If you are working on the lab computers, the `grader` command will run the autograder.  If you are working on your own personal machine, you should download [grader.rkt](http://inst.eecs.berkeley.edu/~cs61as/autograder/grader.rkt) and the [HW 4 tests](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw4-tests.rkt).

## Warm-up
  
Try and predict what the following expressions will return, then check your answers with the Racket interpreter:

* `(define x (cons 4 5))`
* `(car x)`
* `(cdr x)`
* `(define y (cons 'hello 'goodbye))`
* `(define z (cons x y))`
* `(car (cdr z))`
* `(cdr (cdr z))`
* `(cdr (car z))`
* `(car (cons 8 3))`
* `(car z)`
* `(car 3)`

## Exercise 1

### SICP 2.7 

Alyssa's program is incomplete because she has not specified the implementation of the interval abstraction. Here is a definition of the interval constructor:

    (define (make-interval a b) (cons a b))

Define selectors `upper-bound` and `lower-bound` to complete the implementation.

### SICP 2.8

Using reasoning analogous to Alyssa's, describe how the difference of two intervals may be computed. Define a corresponding subtraction procedure, called sub-interval.

### SICP 2.10

Ben Bitdiddle, an expert systems programmer, looks over Alyssa's shoulder and comments that it is not clear what it means to divide by an interval that spans zero. Modify Alyssa's code to check for this condition and to signal an error if it occurs.

**Note:** Spans zero means that one bound is <= zero and the other is >= zero!

### SICP 2.12

Define a constructor `make-center-percent` that takes a center and a percentage tolerance and produces the desired interval. You must also define a selector `percent` that produces the percentage tolerance for a given interval. The `center` selector is the same as the one shown above.

### SICP 2.17

Define a procedure `last-pair` that returns the list that contains only the last element of a given (nonempty) list:

    -> (last-pair (list 23 72 149 34))
    (34)

### SICP 2.20

The procedures `+`, `*`, and `list` take arbitrary numbers of arguments. One way to define such procedures is to use `define` with **dotted-tail notation**. In a procedure definition, a parameter list that has a dot before the last parameter name indicates that, when the procedure is called, the initial parameters (if any) will have as values the initial arguments, as usual, but the final parameter's value will be a list of any remaining arguments. For instance, given the definition

    (define (f x y . z) <body>)

the procedure `f` can be called with two or more arguments. If we evaluate

    (f 1 2 3 4 5 6)

then in the body of `f`, `x` will be `1`, `y` will be `2`, and `z` will be the list `'(3 4 5 6)`. Given the definition

    (define (g . w) <body>)

the procedure `g` can be called with zero or more arguments. If we evaluate

    (g 1 2 3 4 5 6)

then in the body of `g`, `w` will be the list `'(1 2 3 4 5 6)`.

Use this notation to write a procedure `same-parity` that takes one or more integers and returns a list of all the arguments that have the same even-odd parity as the first argument. For example,

    -> (same-parity 1 2 3 4 5 6 7)
    (1 3 5 7)

    -> (same-parity 2 3 4 5 6 7)
    (2 4 6)

### SICP 2.22

Louis Reasoner tries to rewrite the first `square-list` procedure of Exercise 2.21 so that it evolves an iterative process:

    (define (square-list items)
      (define (iter things answer)
        (if (null? things)
            answer
            (iter (cdr things) 
                  (cons (square (car things))
                        answer))))
      (iter items nil))

Unfortunately, defining `square-list` this way produces the answer list in the reverse order of the one desired. Why?

Louis then tries to fix his bug by interchanging the arguments to `cons`:

    (define (square-list items)
      (define (iter things answer)
        (if (null? things)
            answer
            (iter (cdr things)
                  (cons answer
                        (square (car things))))))
      (iter items nil))

This doesn't work either. Explain.


## Exercise 2

  
Write a procedure `my-substitute` that takes three arguments: a list, an old
word, and a new word. It should return a copy of the list, but with every
occurrence of the old word replaced by the new word, even in sublists. For
example:

    -> (my-substitute '((lead guitar) (bass guitar) (rhythm guitar) drums)
                      'guitar
                      'axe)
    ((lead axe) (bass axe) (rhythm axe) drums)

You might find the procedure `list?` useful:
    
    -> (list? (list 1 2 3))
    #t
    -> (list? 'apple)
    #f
    -> (list? 4)
    #f
    

## Exercise 3

  
Now write `my-substitute2` that takes a list, a list of old words, and a list of
new words; the last two lists should be the same length. It should return a
copy of the first argument, but with each word that occurs in the second
argument replaced by the corresponding word of the third argument:

    -> (my-substitute2 '((4 calling birds) (3 french hens) (2 turtle doves))
                       '(1 2 3 4)
                       '(one two three four))
    ((four calling birds) (three french hens) (two turtle doves))

## Extra for Experts

Do these if you want an extra challenge. These are *not* for credit.

### Exercise 4

Write the procedure `cxr-function` that takes as its argument a word starting
with c, ending with r, and having a string of letters a and/or d in between,
such as `cdddadaadar`. It should return the corresponding function.

### Exercise 5
  
[SICP Ex. 2.6](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.4). Besides addition, invent multiplication and exponentiation of nonnegative integers. If you're really enthusiastic, see if you can invent subtraction. (Remember, the rule of this game is that you have only lambda as a starting point.) Read `~cs61as/lib/church-hint` for some suggestions.

### Exercise 6
  
[SICP Ex. 2.18](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.18); this should take some thought, and you should make sure you get it right, but don't get stuck on it for a whole hour. Note: Your solution should reverse lists, not sentences! That is, you should be using `cons`, `car`, and `cdr`, not `first`, `sentence`, etc.

## Submit Your Homework!

For instructions, see [this guide](../submit.html). It covers basic terminal commands and assignment submission.

If you have any trouble submitting, do not hesitate to ask a TA!
