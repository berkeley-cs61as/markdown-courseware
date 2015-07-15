## Template

Type the following command at the terminal to copy the template file to the
current directory:

    cp ~cs61as/autograder/templates/hw8.scm .

Or you can download it [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw8.scm).

## Exercises
  
Complete the following: 

  * [SICP 3.3, 3.4](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-20.html#%_thm_3.3)
  * [SICP 3.7, 3.8](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-20.html#%_thm_3.7)
  * [SICP 3.10](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-21.html#%25_thm_3.10)
  * [SICP 3.11](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-21.html#%25_thm_3.11) 

**Note:** For exercises 3.3 and 3.4, you should create a function called `make-password-account` instead of `make-account`.

## Extra for Experts

**Do this if you want to. This is NOT for credit.**

  
The purpose of the environment model is to represent the scope of variables;
when you see an `x` in a program, which variable `x` does it mean? Another way
to solve this problem would be to rename all the local variables so that there
are never two variables with the same name. Write a procedure `unique-rename`
that takes a `(quoted)` lambda expression as its argument, and returns an
equivalent lambda expression with the variables renamed to be unique:

    > (unique-rename '(lambda (x) (lambda (y) (x (lambda (x) (y x))))))
    (lambda (g1) (lambda (g2) (g1 (lambda (g3) (g2 g3)))))

Note that the original expression had two variables named `x`, and in the
returned expression it's clear from the names which is which. You'll need a
modified counter object to generate the unique names.

You may assume that there are no `quote`, `let`, or `define` expressions, so
that every symbol is a variable reference, and variables are created only by
`lambda`.

Describe how you'd use `unique-rename` to allow the evaluation of Scheme
programs with only a single `(global)` frame.