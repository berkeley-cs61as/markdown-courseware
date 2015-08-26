## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw1.rkt .

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw1.rkt).

**If you get stuck on this homework, review [Lesson 0.3](https://berkeley-cs61as.github.io/textbook/how-recursion-works.html) 
for a detailed explanation of recursion.**

## Autograder

If you are working on the lab computers, the `grader` command will run the autograder.  If you are working on your own personal machine, you should download [grader.rkt](http://inst.eecs.berkeley.edu/~cs61as/autograder/grader.rkt) and the [HW 1 tests](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw1-tests.rkt).

## Exercise 1

Write a procedure `dupls-removed` that, given a sentence as input, returns the
result of removing duplicate words from the sentence. This problem uses
[recursion](https://berkeley-cs61as.github.io/textbook/how-recursion-works.html).

```
;; This should output (c a d e b)
(dupls-removed '(a b c a e d e b)) 
```

```
;; This should output (a b c)
(dupls-removed '(a b c)) ;;
```

```
;; This should output (b a) 
(dupls-removed '(a a a a b a a))
```

As a reminder, you can run the autograder on the lab computers by:

    
    grader hw1 hw1.rkt dupls-removed

And on your own machine:


    racket -tm grader.rkt -- hw1-tests.rkt hw1.rkt dupls-removed


## Exercise 2

  
Write a procedure `count-word` that takes a sentence and a word as arguments
and outputs the number of occurences of the input word in the sentence.

```
;; This should output 2
(count-word '(i really really like 61as) 'really)
```

```
;; This should output 0
(count-word '(i lambda racket) 'love)
```

## Exercise 3

  
Explain what would happen if you used `new-if` (from Lab 0) instead of `if` in
the `pigl` procedure.

Here is the definition of pigl from previous lab

```
(define (pigl wd)
  (if (pl-done? wd)
      (word wd 'ay)
      (pigl (word (bf wd) (first wd)))))

(define (pl-done? wd)
  (vowel? (first wd)))

(define (vowel? letter)
  (member? letter '(a e i o u)))
```

## Exercise 4

  
Write a procedure `squares` that takes a sentence of numbers as its argument
and returns a sentence of the squares of the numbers.

```
;; This should output (1 4 9)
(squares '(1 2 3))
```

## Exercise 5

  
Write a procedure `switch` that takes a sentence as its argument and returns a
sentence in which every instance of the words `I` or `me` is replaced by `you`,
while every instance of `you` is replaced by `me` except at the beginning of
the sentence, where it's replaced by `I`. (The word `I` is the only word that
should be capitalized.)

```
;; This should output (I told you that you should wake me up)
(switch '(you told me that I should wake you up))
```

## Exercise 6

Write a predicate `ordered?` that takes a sentence of numbers as its argument
and returns `#t` if the numbers are in ascending order, or `#f` otherwise.

```
(ordered? '(1 2 3)) ; #t
```

```
(ordered? '(2 1 3)) ; #f
```

```
(ordered? '(2)) ; #t
```

## Exercise 7

  
Write a procedure `ends-e` that takes a sentence as its argument and returns a
sentence containing only those words that end in the letter E.

```
;; This should output (please the above the blue)
(ends-e '(please put the salami above the blue elephant))
```

## Exercise 8

Most versions of Lisp provide `and` and `or` procedures like the ones we've
seen. In principle, there is no reason why these can't be ordinary procedures,
but some versions of Lisp make them special forms.

Suppose, for example, we
evaluate `(or (= x 0) (= y 0) (= z 0))`. If `or` is an ordinary procedure, all
three argument expressions will be evaluated before or is invoked. But if the
variable `x` has the value 0, we know that the entire expression has to be
true regardless of the values of `y` and `z`. A Lisp interpreter in which `or`
is a special form can evaluate the arguments one by one until either a true
one is found or it runs out of arguments.

Devise a test that will tell you whether Racket's `and` and
`or` are special forms or ordinary functions. This is a somewhat tricky problem,
but it'll get you thinking about the evaluation process more deeply.
Why might it be advantageous for an interpreter to treat `or`
as a special form and evaluate its arguments one at a time? Can you think of
reasons why it might be advantageous to treat `or` as an ordinary function?

## Submitting Your Homework

Please refer to the guide in [Homework 0-2](/textbook/homework-0.2.html) for how to submit your homework.

