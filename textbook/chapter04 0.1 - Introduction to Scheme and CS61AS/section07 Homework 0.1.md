## Homework 0.1 Intro

In this homework, you'll use what you've learned in the first day to solve
some problems. You'll also be doing a bit of reading and introducing yourself.

**This homework is due Tuesday, June 23 2015, 11:59PM**

## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
        cp ~cs61as/autograder/templates/hw0-1.rkt .

Or you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw0-1.rkt).

## Introduce Yourself to the Staff

![](http://studentbranding.com/wp-content/uploads/2011/04/Repeat-their-name-
and-introduce-yourself.jpg)

Before you start the exercises, introduce yourself to staff! We want to know
who you are.

Answer the following questions on the homework file:

1) What is your name?

2) What is your major?

3) Are you a returning student? (i.e. Did you take 61AS last semester?)

4) What made you to take 61AS?

5) Tell us interesting things about yourself.

## Exercise 0 - Introduce Yourself to your Classmates

See if you can find a post on Piazza called "Hello World!". Make a followup on that post and introduce yourself. Be sure to include:

  * Name
  * Major and Year
  * One interesting fact about yourself
  * Why you're taking the course

## Exercise 1 - `sum-of-squares`

Here is the syntax for defining a procedure:

    
    (define ([name of procedure] [variables]) [body of procedure])
      

For example, you saw how to define a `square` procedure:

    
    (define (square x) (* x x))
      

After defining, you can use the procedure `square` to find the square of any
number you want. Likewise...

Without using `*` (use `square` instead), define a procedure `sum-of-squares`,
which takes two arguments, and returns the sum of the squares of the two
arguments.

Make sure you test your work!

After you've written your procedure, run the autograder for this exercise and
check if you defined your procedure correctly by typing the following into
your terminal:

    
    grader hw0-1 hw0-1.rkt sum-of-squares

## Words

We've shown you some interesting procedures that allow you to do stuff to
words:

`'` makes a word (e.g., `'pi`) or a group of words (e.g., `'(good morning)`).

`first` takes a word and returns the first letter of that word, or it takes a sentence and returns the first word of that sentence.

`butfirst` (or `bf`) takes a word/sentence and returns everything but the first letter/word.

Keep these procedures and concepts in the back of your mind. They'll come back
in later exercises and labs.

## Special Forms

  
Racket has some control features that allow you to choose what to do next
based on a test. These are called _Special Forms._ Special forms have
particular rules that allow them to skip evaluating some of its arguments.

### `if`

In Racket, `if` is a special form that evaluates only one of its last two
arguments to use as a value. `if` always evaluates its first argument. If the
value of that argument is `true`, then `if` evaluates its second argument and
returns its value. If the value of the first argument is `false`, then if
evaluates its third argument and returns that value.

Here is an example of proper if syntax:

    
    (if (= 5 (+ 2 3))
        'yay!
        (/ 1 0) )

In this case, `yay!` is printed. Because the first expression evaluates to
true, the last argument to `if` is not evaluated, which means we don't get a
divide-by-zero error.

### `cond`

`cond` is a special form that acts just like an `if` statement, except with multiple options. Each clause is tested one at a time until one evaluates to `true`. If none of the clauses are `true`, you can include an `else` clause to capture these cases.

Here is an example:

    
    (cond ((= 3 1) 'wrong!)
          ((= 3 2) 'still-wrong!)
          (else 'yay))

In this case, the first two conditions return `false`, and `yay` is printed.

Some good procedures to use for the test cases are `>`, `<`, and `=`.

### `and`

`and` checks whether **all** its arguments are `true`.

    
    > (and (> 5 3) (< 2 4))
    #t
    > (and (> 5 3) (< 2 1))
    #f
    

Why is `and` a special form? It evaluates its arguments and stops as soon as
it can, returning `#f` as soon as any argument evaluates to false. This turns
out to be useful:

    
    > (define (divisible? big small)
        (= (remainder big small) 0))
    > (define (num-divisible-by-4? x)
        (and (number? x) (divisible? x 4)))
    > (num-divisible-by-4? 16)
    #t
    > (num-divisible-by-4? 6) 
    #f
    > (num-divisible-by-4? 'aardvark)
    #f  ;; and exits before trying to find the remainder of 'aardvark
    > (divisible? 'aardvark 4)
    ERROR: AARDVARK IS NOT A NUMBER
    

A subtle point about `and`: similar to `or`, if all its arguments evaluate to
`true`, instead of simply returning `#t` it will return the value of its last
argument.

    
    > (and #t (+ 3 5))
    8
    > (and (- 2 1) 100)
    100
    

Anything that is not `#f` is `#t`. So, `100` is `true`, `'foo` is `true`, and so on.

### `or`

`or` checks whether **any** of its arguments are `true`.

    
    > (or (> 5 3) (< 2 1))
    #t
    > (or (> 5 6) (< 2 1))
    #f
    

Why is `or` a special form? It evaluates its arguments and stops as soon as
one of its arguments evaluates to `true`.

    
    > (or #f #t (/ 1 0))
    #t
    

A subtle point about `or`: just like `and`, if any one of its arguments evaluate to `true`, `or` returns the value of the evaluated expression rather than just simply `#t`.

    
    > (or #f (+ 1 2 3))
    6
    > (or (* 3 4) (- 2 1))
    12

## Exercise 2a - `can-drive`

Take a moment to read through the above, and try them out in the interpreter.
Then, write a procedure `can-drive` that takes the age of a person as an
argument. If the age is below `16`, return the sentence '`(not yet)`. Otherwise,
return the sentence '`(Good to go)`. Make sure to test your code in the
interpreter.

After you've finished this exercise, run the autograder on your code to check
if it's correct by typing the following into your terminal:

    
    grader hw0-1 hw0-1.rkt can-drive

## Exercise 2b - `fizzbuz`

Write a procedure `fizzbuzz` that takes a number and outputs the word '`fizz`
if the number is divisible by `3`, '`buzz` if it's divisible by `5`, '`fizzbuzz`
if it's divisible by both `3` and `5`, and otherwise, the number itself. You may
find the function `remainder` useful. Make sure to test your code in the
interpreter.

After you've finished this exercise, check your solution by typing the
following into your terminal:

    
    grader hw0-1 hw0-1.rkt fizzbuzz

## Exercise 3 - The Most Baffling Question

Why did the Walrus cross the Serengeti?

To figure out this answer, look on Piazza for the post labeled "Answer to Homework 0-1 Exercise 3".

## Exercise 4 - `new-if`

See what happens when you type the following snippets of code into the
interpreter:

    
    (define (infinite-loop) (infinite-loop))
    
    (if (= 3 6)
      (infinite-loop)
      (/ 4 2))
    

Now we want to see if we can write a procedure that behaves just like `if`.
Here's our attempt:

    
    (define (new-if test then-case else-case)
      (if test
        then-case
        else-case))
    
    ;; Let's try it out:
    (new-if (= 3 6)
      (infinite-loop)
      (/ 4 2))
    

It didn't work!

Here is another example that breaks:

    
    (new-if (= 3 6)
      (/ 1 0)
      (/ 4 2))

Why didn't `new-if` behave like `if`? What can you learn about `if` from this
example? Think about this and try to figure it out. Expect to see it again.

## Takeaways

This homework provides practice involving the following ideas:

  1. Procedures
  2. Short Circuiting
  3. Using Piazza

## Recommended Readings

The following reading is recommended:

  * [Lecture Notes 1](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf)
  * [SICP 1.1 - The Elements of Programming](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%25_sec_1.1)

## Running the Autograder

Before submitting any homework, there are two checks you need to make:

  1. Your homework MUST load into the Racket interpreter. Any submissions that do not load will not receive any credit.
  2. Run your homework through the autograder to check your answers. If you cannot get your homework to pass all the autograder tests, don't fret, and submit your homework anyway. We grade based on effort. 

To run the autograder, type the following into the terminal:

    
    grader <assignment name> <file name>

For example, to run the autograder on this homework, type the following into
the terminal:

    
     grader hw0-1 hw0-1.rkt

Remember that if you pass the autograder when you submit your homework, you're
guaranteed full credit and your slip days are reset!

## Submitting your Homework

Here is a [quick guide](http://berkeley-cs61as.github.io/textbook/submitting-homework.html) to turning in homework and basic Unix commands. If you have any trouble submitting, do not hesitate to ask a TA!

## Moving Forward

Start on Lesson 1. If Lesson 1 looks completely foreign to you, talk to a TA and s/he will get you on track.

