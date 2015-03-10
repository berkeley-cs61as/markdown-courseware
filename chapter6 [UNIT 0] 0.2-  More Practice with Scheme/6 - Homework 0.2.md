## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw0-2.scm .

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw0-2.scm).

## Exercise 0.

  
The expression `(+ 8 2)` has the value 10. It is a compound expression made up
of three atoms. For this problem, write five other Scheme expressions whose
values are also the number ten:

  1. An atom
  2. Another compound expression made up of three atoms
  3. A compound expression made up of four atoms
  4. A compound expression made up of an atom and two compound subexpressions
  5. Any other kind of expression

## Exercise 1.

  
Let's build a repertoire of functions to deal with words and sentences. We'll
give you the second procedure from the previous lab. You might also find the
[word](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-
1x/word/) function useful.

  1. Write a procedure `first-two` that takes a word as its argument, returning a two-letter word containing the first two letters of the argument.
  2. Write a procedure `two-first` that takes two words as arguments, returning a two-letter word containing the first letters of the two arguments.
  3. Now write a procedure `two-first-sent` that takes a two-word sentence as argument, returning a two-letter word containing the first letters of the two words.

`;; The following should output am`

` (first-two 'ambulatory)`

`;; The following should output be`

` (two-first 'brian 'epstein)`

`;; The following should output be`

` (two-first-sent '(brian epstein))`

## Exercise 2.

Write a predicate `teen?` that returns `true` if its argument is between 13
and 19.

`;; This should output #t`

` (teen? 19)`

`;; This should output #f`

` (teen? (/ 39 2))`

## Exercise 3.

  
Write a procedure `indef-article`. See examples below:

`;; This should output (a beatle)`

` (indef-article 'beatle)`

`;; This should output (an album)`

` (indef-article 'album)`

## Exercise 4.

  
Write a procedure `insert-and` that takes a sentence of items and returns a
new sentence with an and in the right place.

`;; This should output (john bill wayne fred and joey)`

` (insert-and '(john bill wayne fred joey))`

## Exercise 5.

  
Write a procedure `query` that turns a statement into a question by swapping
the first two words and adding a question mark to the last word:

`;; This should output (are you experienced?)`

` (query '(you are experienced))`

`;; This should output (should i have known better?)`

` (query '(i should have known better))`

`;; This should output (were you there?)`

`(query '(you were there))`

## Exercise 6.

  
Write a procedure `european-time` to convert a time from American AM/PM
notation into European 24-hour notation. Also write `american-time`, which
does the opposite:

`;; This should output 8`

` (european-time '(8 am))`

`;; This should output 16`

` (european-time '(4 pm))`

`;; This should output (9 pm)`

` (american-time 21)`

`;; This should output (12 pm)`

` (american-time 12)`

`;; This should output 0`

` (european-time '(12 am))`

## Exercise 7.

  
Write a procedure `describe-time` that takes a number of seconds as its
argument and returns a more useful description of that amount of time. Assume
that there are 365.25 days in a year. You only need to account for time
periods up to a day.

`;; This should output (45 seconds)

(describe-time 45)`

`;; This should output (15.5 minutes)

(describe-time 930)`

## Exercise 8.

  
The following program doesn't work. Why not? Fix it and explain why.

If you're stuck, take a look at [Simply Scheme Ch. 7 -
Variables](http://www.cs.berkeley.edu/~bh/ssch7/variables.html)

`(define (superlative adjective word)`

` (se (word adjective 'est) word))`

`;; This should output (dumbest exercise)`

` (superlative 'dumb 'exercise)`

## Submission Guide

**You must finish both lab and homework for a lesson before submitting your homework for that lesson.**

**IF YOU HAVE ANY TROUBLE WITH SUBMITTING, ASK A QUESTION ON PIAZZA OR TALK TO A TA.**

**BEFORE SUBMITTING HOMEWORK: Make sure your file loads in Scheme. You can verify this by typing into STk: (load "hw0-2.scm"),** or whatever the name of your homework file is. You will not receive credit for homework that does not load in Scheme.****

To submit your assignment, you need to be logged in on any of the lab
computers. If you want to submit from home, you must connect remotely to the
lab computers. More on that later.

Now, click on the "Terminal" icon on the left. Terminal is a terminal
emulator, a method of interacting directly to the computer via text commands.
It's sort of an "interpreter" for your entire computer. You can do useful
things with xterm like navigate and manipulate the filesystem (think Windows
Explorer), submit homework (what we're doing now), and start the Scheme
interpreter (via stk)!

Let's submit an assignment. This requires the following steps:

  1. Making a folder for an assignment (optional, but strongly recommended, as we'll see)
  2. Doing the assignment in that folder (or moving the files to that folder if you've already completed the assignment)
  3. Running the `submit` command
  4. Checking if the assignment was correctly submitted

We're going to submit an assignment called "units", which will tell the staff
how many units you're doing.

## 1. Making a folder

In the terminal type

`mkdir units`

This tells the computer to make a directory (a folder) named units. You can
double check that it exists (and also see what else is in this current
directory) by running

`ls`

Now we need to navigate to that folder, so we'll do:

`cd units`

## 2. Finishing the Assignment

In order to complete this assignment, you must create a file named units
(inside the directory named units) and put in it which units you're planning
on doing. For example, if you were to do units 0, 1, 2, and 3, you'd put

`0 1 2 3`

## 3. Submitting

After you've created the file, you can submit the assignment by doing

`submit units`

This tells the computer that you want to submit the assignment units (that the
system knows, it has nothing to do with the name of the file or the directory
that you've created).

## 4. Checking your submission

The following command allows you to look at the times in which you've
submitted:

`glookup -t`

That's all for now. You might be interested in connecting from home in order
to work on all of this. Details about that are under the Resources link on the
top!

