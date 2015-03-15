## Template

From now on, for most labs we will have template files for the labs in which
you can write your answers. Type the following command at the terminal to copy
the template file to the current directory (note the period at the end):

`cp ~cs61as/autograder/templates/hw4.scm .`

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw4.scm).

## Exercise 1.

  
Try these in Scheme, starting from the left column:

`(define x (cons 4 5))`

` (car x)`

` (cdr x)`

` (define y (cons 'hello 'goodbye))`

` (define z (cons x y))`

` (car (cdr z))`

` (cdr (cdr z))`

## Exercise 2.

  
Predict the result of each of these before you try it.

`(cdr (car z))`

` (car (cons 8 3))`

` (car z)`

` (car 3)`

## Exercise 1.

  
Complete the following:

  * [SICP Ex. 2.7, 2.8, 2.10, 2.12](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.7)
  * [SICP Ex. 2.17, SICP Ex. 2.20](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.17)
  * [SICP Ex. 2.22](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.22)

Note: Spans zero means that one bound is <= zero and the other is >= zero!

## Exercise 3.

  
Read over the following code and enter them into Scheme.

`;; Enter these definitions into Scheme:`

` (define (make-rational num den)`

` (cons num den))`

`(define (numerator rat)`

` (car rat))`

`(define (denominator rat)`

` (cdr rat))`

`(define (*rat a b)`

` (make-rational (* (numerator a) (numerator b))`

` (* (denominator a) (denominator b))))`

`(define (print-rat rat)`

` (word (numerator rat) '/ (denominator rat)))`

`;; Now try these:`

` (print-rat (make-rational 2 3))`

` (print-rat (*rat (make-rational 2 3) (make-rational 1 4)))`

Now define a procedure `+rat` to add two rational numbers, in the same style
as `*rat` above.

## Exercise 5.

  
This week you'll learn that sentences are a special case of lists, which are
built out of pairs. Explore how that's done with experiments such as these:

`(define x '(a (b c) d))`

` (car x)`

` (cdr x)`

` (car (cdr x))`

## Exercise 4.

  
Do the following exercises:

    * [SICP Ex. 2.2](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.2)
    * [SICP Ex. 2.3](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.3)
    * [SICP Ex. 2.4](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%_thm_2.4)

Notes: For 2.4, name the procedures` proc-cons`,` proc-car`, and `proc-cdr`.

## Exercise 2.

  
Write a procedure `substitute` that takes three arguments: a list, an old
word, and a new word. It should return a copy of the list, but with every
occurrence of the old word replaced by the new word, even in sublists. For
example,

`(substitute '((lead guitar) (bass guitar)`

` (rhythm guitar) drums)`

` 'guitar`

` 'axe)`

` ;; Should output ((lead axe) (bass axe) (rhythm axe) drums)`

You might find the procedure `list?` useful.

    
    
    >(list? (list 1 2 3))
    #t
    
    >(list? 'apple)
    #f
    
    >(list? 4)
    #f
    

## Exercise 3.

  
Now write `substitute2` that takes a list, a list of old words, and a list of
new words; the last two lists should be the same length. It should return a
copy of the first argument, but with each word that occurs in the second
argument replaced by the corresponding word of the third argument:

`(substitute2 '((4 calling birds)`

` (3 french hens)`

` (2 turtle doves))`

` '(1 2 3 4)`

` '(one two three four))`

` ;; Expected output:`

` ;; ((four calling birds)`

` ;; (three french hens)`

` ;; (two turtle doves))`

# Extra for Experts

### Do this if you want to. This is NOT for credit.

## Exercise 4.

  
Write the procedure `cxr-function` that takes as its argument a word starting
with c, ending with r, and having a string of letters a and/or d in between,
such as `cdddadaadar`. It should return the corresponding function.

## Exercise 5.

  
[SICP Ex. 2.6](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-14.html#%_thm_2.4). Besides addition, invent multiplication
and exponentiation of nonnegative integers. If you're really enthusiastic, see
if you can invent subtraction. (Remember, the rule of this game is that you
have only lambda as a starting point.) Read `~cs61as/lib/church-hint` for some
suggestions.

## Exercise 6.

  
[SICP Ex. 2.18](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-15.html#%_thm_2.18); this should take some thought, and you
should make sure you get it right, but don't get stuck on it for a whole hour.
Note: Your solution should reverse lists, not sentences! That is, you should
be using `cons`, `car`, and `cdr`, not `first`, `sentence`, etc.

