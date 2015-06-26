## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw1.rkt .

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw1.rkt).

**If you get stuck on this homework, review [Lesson 0.3](https://berkeley-cs61as.github.io/textbook/how-recursion-works.html) 
for a detailed explanation of recursion.**

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

**If you are having trouble submitting, ask a question on Piazza or contact a TA.**

**Before submitting:** Make sure your file loads in Racket.
You can verify this by typing into Racket: `(enter! "hw1.rkt")`, where "hw1.rkt" is the name of your homework file.
You will not receive credit for homework that does not load in Racket.

To submit your assignment, you need to be logged in on any of the lab
computers. If you want to submit from home, you must connect remotely to the
lab computers. More on that later.

Now, click on the "Terminal" icon on the left. Terminal is a terminal
emulator, a method of interacting directly to the computer via text commands.
It's sort of an "interpreter" for your entire computer. You can do useful
things with xterm like navigate and manipulate the filesystem (think Windows
Explorer), submit homework (what we're doing now), and start the Racket
interpreter (via `racket`)!

Let's submit an assignment. This requires the following steps:

  1. Making a folder for an assignment (optional, but strongly recommended, as we'll see)
  2. Doing the assignment in that folder (or moving the files to that folder if you've already completed the assignment)
  3. Running the `submit` command
  4. Checking if the assignment was correctly submitted

We're going to submit an assignment called "units", which will tell the staff
how many units you're doing.

### Making a Folder

In the terminal, type:

```
mkdir units
```

This tells the computer to make a directory (folder) named `units`. You can
double check that it exists (and also see what else is in this current
directory) by running `ls`.

Now we need to navigate to that folder, so we'll do:

```
cd units
```

### Finishing the Assignment

In order to complete this assignment, you must create a file named `units`
(inside the directory named `units`). In that file, write which units you're planning
on doing. For example, if you were to do units 0, 1, 2, and 3, you'd put

```
0 1 2 3
```

Please **do not** include any additional spaces or blank lines!

### Submitting

After you've created the file, you can submit the assignment by doing

```
submit units
```

This tells the computer that you want to submit the assignment "units".
Follow any instructions that appear.

### Checking Your Submission

The following command allows you to look at the times in which you've
submitted:

```
glookup -t
```

That's all for now. You might be interested in connecting from home in order
to work on all of this. Details about that are under the Resources link on the
top!

