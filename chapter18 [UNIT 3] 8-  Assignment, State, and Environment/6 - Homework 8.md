Type the following command at the terminal to copy the template file to the
current directory:

`cp ~cs61as/autograder/templates/hw8.scm .`

Or you can download
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw8.scm).

## Exercise 1.

  
Given below is a simplified version of the make-account procedure on page 223
of Abelson and Sussman.

`(define (make-account balance) `

` (define (withdraw amount) `

` (set! balance (- balance amount)) balance) `

` (define (deposit amount) `

` (set! balance (+ balance amount)) balance) `

` (define (dispatch msg) `

` (cond `

` ((eq? msg 'withdraw) withdraw) `

` ((eq? msg 'deposit) deposit) ) ) `

`dispatch) `

Fill in the blank in the following code so that the result works exactly the
same as the `make-account` procedure above, that is, responds to the same
messages and produces the same return values. The differences between the two
procedures are that the inside of make-account above is enclosed in the let
below, and the names of the parameter to make-account are different.

`(define (make-account init-amount) `

` (let ( YOUR CODE HERE ) `

` (define (withdraw amount) `

` (set! balance (- balance amount)) balance) `

` (define (deposit amount) `

` (set! balance (+ balance amount)) balance) `

` (define (dispatch msg) `

` (cond `

` ((eq? msg 'withdraw) withdraw) `

` ((eq? msg 'deposit) deposit) ) ) `

` dispatch) ) `

## Exercise 2.

Modify either version of `make-account` so that, given the message balance, it
returns the current account balance, and given the message `init-balance`, it
returns the amount with which the account was initially created. For example:

`> (define acc (make-account 100)) `

`acc `

`> (acc 'balance)

100`

## Exercises.

  
Complete the following: Abelson & Sussman, exercises [3.3,
3.4](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-20.html#%_thm_3.3),
[3.7, 3.8](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-20.html#%_thm_3.7), [3.10](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-21.html#%25_thm_3.10),
[3.11](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-21.html#%25_thm_3.11) Note: For 3.3 and 3.4, you should
create a function called make-password-account instead of make-account.

## Exercise 4.

  
Given this definition:

`(define (plus1 var) `

` (set! var (+ var 1)) `

` var) `

Show the result of computing

`(plus1 5)`

using the substitution model. That is, show the expression that results from
substituting 5 for `var` in the body of `plus1`, and then compute the value of
the resulting expression. What is the actual result from Scheme?

## Exercise 3.

  
Modify `make-account` so that, given the message transactions, it returns a
list of all transactions made since the account was opened. For example:

`> (define acc (make-account 100)) `

` acc `

` > ((acc 'withdraw) 50) `

` 50 `

`> ((acc 'deposit) 10) `

` 60 `

`> (acc 'transactions) `

` ((withdraw 50) (deposit 10))`

## Extra for Experts

### Do this if you want to. This is NOT for credit.

  
The purpose of the environment model is to represent the scope of variables;
when you see an `x` in a program, which variable `x` does it mean? Another way
to solve this problem would be to rename all the local variables so that there
are never two variables with the same name. Write a procedure `unique-rename`
that takes a `(quoted)` lambda expression as its argument, and returns an
equivalent lambda expression with the variables renamed to be unique:

`> (unique-rename '(lambda (x) (lambda (y) (x (lambda (x) (y x)))))) `

`(lambda (g1) (lambda (g2) (g1 (lambda (g3) (g2 g3))))) `

Note that the original expression had two variables named `x`, and in the
returned expression it's clear from the names which is which. You'll need a
modified counter object to generate the unique names.

You may assume that there are no `quote`, `let`, or `define` expressions, so
that every symbol is a variable reference, and variables are created only by
`lambda`.

Describe how you'd use `unique-rename` to allow the evaluation of Scheme
programs with only a single `(global)` frame.

## Exercise 5.

This lab activity consists of example programs for you to run in Scheme.
Predict the result before you try each example. If you don't understand what
Scheme actually does, ask for help! Don't waste your time by just typing this
in without paying attention to the results.

    
    (define (make-adder n)                       ((lambda (x) 
      (lambda (x) (+ x n)))                         (let ((a 3)) 
                                                      (+ x a))) 
    (make-adder 3)                                5) 
     
    ((make-adder 3) 5)                           (define k 
                                                   (let ((a 3)) 
    (define (f x) (make-adder 3))                    (lambda (x) (+ x a)))) 
     
    (f 5)                                        (k 5) 
     
    (define g (make-adder 3))                    (define m 
                                                   (lambda (x) 
    (g 5)                                            (let ((a 3)) 
                                                       (+ x a)))) 
    (define (make-funny-adder n)        
      (lambda (x)                                (m 5) 
        (if (equal? x 'new)             
            (set! n (+ n 1))                     (define p 
            (+ x n))))                             (let ((a 3)) 
                                                     (lambda (x) 
    (define h (make-funny-adder 3))                    (if (equal? x 'new) 
                                                           (set! a (+ a 1)) 
    (define j (make-funny-adder 7))                        (+ x a))))) 
     
    (h 5)                                        (p 5) 
     
    (h 5)                                        (p 5) 
     
    (h 'new)                                     (p 'new) 
     
    (h 5)                                        (p 5) 
     
    (j 5)                                        (define r 
                                                   (lambda (x) 
    (let ((a 3))                                     (let ((a 3)) 
      (+ 5 a))                                         (if (equal? x 'new) 
                                                           (set! a (+ a 1)) 
    (let ((a 3))                                           (+ x a))))) 
      (lambda (x) (+ x a)))             
                                                 (r 5) 
    ((let ((a 3))                       
       (lambda (x) (+ x a)))                     (r 5) 
     5)                                 
                                                 (r 'new) 
     
                                                 (r 5)                 
     
    (define s                                    (define (ask obj msg . args) 
      (let ((a 3))                                 (apply (obj msg) args)) 
        (lambda (msg)                             
          (cond ((equal? msg 'new)               (ask s 'add 5) 
                 (lambda ()                       
                   (set! a (+ a 1))))            (ask s 'new) 
                ((equal? msg 'add)                
                 (lambda (x) (+ x a)))           (ask s 'add 5) 
                (else (error "huh?"))))))         
                                                 (define x 5) 
    (s 'add)                                      
                                                 (let ((x 10) 
    (s 'add 5)                                         (f (lambda (y) (+ x y)))) 
                                                   (f 7)) 
    ((s 'add) 5)                                  
                                                 (define x 5) 
    (s 'new)                                      
     
    ((s 'add) 5)                                  
     
    ((s 'new))                                    
     
    ((s 'add) 5) 

