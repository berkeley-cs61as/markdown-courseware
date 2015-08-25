## Homework 0.1 Intro

In this homework, you'll use what you've learned so far to solve
some problems. You'll also be doing a bit of reading and introducing yourself.

Remember: you can view the due date for this homework on either the [front page](../index.html)
or the [deadlines spreadsheet](https://docs.google.com/spreadsheets/u/1/d/1JftJo7ko0wx-jxAEF9_QxYXfzHCYqCNqKeRwOU9K65A/edit?usp=sharing).

## Template

A template file provides the basic skeleton for a homework assignment.

If you're on a lab computer, type the following command into your terminal to copy the template to the
current directory (note the period at the end):
    
        cp ~cs61as/autograder/templates/hw0-1.rkt .

Or you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw0-1.rkt).

## Autograder

If you are working on the lab computers, the `grader` command will run the autograder.  If you are working on your own personal machine, you should download [grader.rkt](http://inst.eecs.berkeley.edu/~cs61as/autograder/grader.rkt) and the [HW 0-1 tests](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw0-1-tests.rkt).

## Exercise 0

First, introduce yourself to the staff!

In your homework file, answer the following questions:

1. What is your name?
2. What is your major?
3. Are you a returning student? (That is, did you take 61AS last semester?)
4. What made you to take 61AS?
5. Tell us some interesting things about yourself.

Now, see if you can find a post on Piazza called "Hello World!". Make a follow-up on that post and introduce yourself. Be sure to include:

  * Name
  * Major and year
  * One interesting fact about yourself
  * Why you're taking the course

## Exercise 1

Here is the syntax for defining a procedure:

    
    (define ([name of procedure] [variables]) [body of procedure])
      

For example, you saw how to define a `square` procedure:

    
    (define (square x) (* x x))
      

After defining it, you can use the procedure `square` to find the square of any
number you want:

```
-> (square 3)
9
```

Using `square`, define a procedure `sum-of-squares` that takes two arguments and returns the sum of the squares of the two
arguments:

```
-> (sum-of-squares 3 4)
25
```

Make sure you test your work!

After you've written your procedure, run the autograder for this exercise and
check if you defined your procedure correctly.  If you are on the lab computers, type the following into your terminal:

    
    grader hw0-1 hw0-1.rkt sum-of-squares

If you are working on your own machine, type the following into your terminal:


    racket -tm grader.rkt -- hw0-1-tests.rkt hw0-1.rkt sum-of-squares

## Interlude

Before we present the next exercise, we need to cover some more Racket features.
Students taking Unit 0 should consider this a preview&mdash;we'll explore these features more in Lesson 0.2.

### Words and Sentences

We've shown you some interesting procedures that allow you to do stuff to words and sentences:

* `'` makes a word (e.g., `'pi`) or a sentence (e.g., `'(good morning)`).
* `first` takes a word and returns the first letter of that word, or it takes a sentence and returns the first word of that sentence.
* `butfirst` (or `bf`) takes a word/sentence and returns everything but the first letter/word.

Keep these procedures and concepts in the back of your mind. They'll come back
in later exercises and lessons.

### Special Forms
  
Racket has some control features that allow you to choose what to do next
based on a test. These features are examples of _special forms_&mdash;procedures with special evaluation rules.
We'll talk about special forms more later in the course.

### `if`

In Racket, `if` is a special form that takes three arguments.
`if` always evaluates its first argument. If the
value of that argument is `true`, then `if` evaluates its second argument and
returns its value. If the value of the first argument is `false`, then if
evaluates its third argument and returns that value.

Here is an example of proper if syntax:

    
    (if (= 5 (+ 2 3))
        'yay!
        (/ 1 0))

The result of this example expression is the word `'yay!`. Because the first expression is true,
the last argument to `if` is not evaluated, which means we don't get a
divide-by-zero error.

### `cond`

`cond` is a special form that acts just like `if`,
except with multiple options. Each condition is tested one at a time until one evaluates to `true`.
An `else` clause is typically used at the end to capture cases where all prior conditions evaluated to `false`.

Here is an example:

    
    (cond ((= 3 1) 'wrong!)
          ((= 3 2) 'still-wrong!)
          (else 'yay))

In this example, the first two conditions return `false`, so the overall expression evaluates to the word `'yay!`.

Some good procedures to use for the test cases are `>`, `<`, and `=`.

### `and`

`and` checks whether *all* of its arguments are `true`:

``` 
-> (and (> 5 3) (< 2 4))
#t
-> (and (> 5 3) (< 2 1))
#f
```

(Note that `#t` and `true` can be used interchangeably, as can `#f` and `false`.)

Why is `and` a special form? Because it evaluates its arguments and stops as soon as
it can, returning `false` as soon as any argument evaluates to `false`. This turns
out to be useful. Suppose we have the following:

```
(define (divisible? big small)
  (= (remainder big small) 0))
(define (num-divisible-by-4? x)
  (and (number? x) (divisible? x 4)))
```

Then we can do this:

```
-> (num-divisible-by-4? 16)
#t
-> (num-divisible-by-4? 6) 
#f
-> (num-divisible-by-4? 'aardvark)
#f
```

Notice how the last call didn't fail. Since `(number? 'aardvark)` evaluates to `false`,
`and` returns `#f` before evaluating its second argument.
Calling `(divisible? 'aardvark 4)` would cause an error:

```
-> (divisible? 'aardvark 4)
; remainder: contract violation
;   expected: integer?
;   given: 'aardvark
;   argument position: 1st
; [,bt for context]
```

This message simply says that the procedure `remainder` reported an error because it expected an integer 
but instead got `'aardvark`. 

A subtle point about `and`: if all its arguments evaluate to
`true`, instead of simply returning `#t` it will return the value of its last
argument.

```    
-> (and #t (+ 3 5))
8
-> (and (- 2 1) 100)
100
```    

Anything that is not `#f` is `#t`. So, `100` is `true`, `'foo` is `true`, and so on.

#### `or`

`or` checks whether **any** of its arguments are `true`.

    
    -> (or (> 5 3) (< 2 1))
    #t
    -> (or (> 5 6) (< 2 1))
    #f
    

Why is `or` a special form? It evaluates its arguments and stops as soon as
one of its arguments evaluates to `true`.

    
    > (or #f #t (/ 1 0))
    #t
    

A subtle point about `or`: like `and`, if any one of its arguments evaluate to `true`, `or` returns the value of the evaluated expression rather than just simply `#t`.

    
    -> (or #f (+ 1 2 3))
    6
    -> (or (* 3 4) (- 2 1))
    12

## Exercise 2

### Part a

Take a moment to read through the above, and try them out in the interpreter.
Then, write a procedure `can-drive` that takes the age of a person as an argument. If the age is below 16, return the sentence
`'(Not yet)`. Otherwise, return the sentence `'(Good to go)`. Make sure to test your code in the
interpreter.

After you've finished this exercise, run the autograder on your code to check
if it's correct by typing the following into your terminal:

    
    grader hw0-1 hw0-1.rkt can-drive

Or, on your own machine:


    racket -tm grader.rkt -- hw0-1-tests.rkt hw0-1.rkt can-drive


### Part b

Write a procedure `fizzbuzz` that takes a number and outputs the word `'fizz` if the number is divisible by 3,
`'buzz` if it's divisible by 5, `'fizzbuzz` if it's divisible by both 3 and 5, and otherwise, the number itself.
You may find the function `remainder` useful. Make sure to test your code in the interpreter.

After you've finished this exercise, check your solution by typing the
following into your terminal:

    
    grader hw0-1 hw0-1.rkt fizzbuzz

Or, on your own machine:

    racket -tm grader.rkt -- hw0-1-tests.rkt hw0-1.rkt fizzbuzz

## Exercise 3

Why did the Walrus cross the Serengeti?

To figure out the answer, look on Piazza for the post labeled "Answer to Homework 0-1 Exercise 3".

## Exercise 4

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
    
Let's try it out:

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

## Recommended Readings

The following readings are recommended:

  * [Lecture Notes 1](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf)
  * [SICP 1.1](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%25_sec_1.1)

## Running the Autograder

Before submitting any homework, there are two checks you need to make:

  1. Your homework *must* load into the Racket interpreter. Any submissions that do not load will not receive any credit.
  2. Run your homework through the autograder to check your answers. If you cannot get your homework to pass all the autograder tests, don't fret.
  Submit your homework anyway. Remember, homeworks are graded based on effort. 

To run the autograder, type the following into the terminal:
    
    grader <assignment name> <file name>

For example, to run the autograder on this homework, type the following into
the terminal:
    
     grader hw0-1 hw0-1.rkt

## Submitting Your Homework

Here is a [guide](../submit.html) on basic terminal commands and homework submission.

If you have any trouble submitting, do not hesitate to ask a TA!

