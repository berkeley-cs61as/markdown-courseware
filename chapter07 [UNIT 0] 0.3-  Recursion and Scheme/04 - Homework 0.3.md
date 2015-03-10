## Exercise 0.

  
When you teach a class, people will get distracted if you say "um" too many
times.

Write a `count-ums` that counts the number of times "um" appears in a
sentence:

`(count-ums '(today um we are going to um talk about the combining um
method))`

` 3`

Here are some special-case count-ums procedures for sentences of particular
lengths:

`(define (count-ums0 sent)`

` 0)`

`(define (count-ums1 sent)`

` (if (equal? 'um (first sent))`

` 1`

` 0))`

`(define (count-ums2 sent)`

` (if (equal? 'um (first sent))`

` (+ 1 (count-ums1 (bf sent)))`

` (count-ums1 (bf sent))))`

`(define (count-ums3 sent)`

` (if (equal? 'um (first sent))`

` (+ 1 (count-ums2 (bf sent)))`

` (count-ums2 (bf sent))))`

Write `count-ums` recursively.

`;; This should output 3`

` (count-ums`

` '(today um we are going to um talk about the ``combining um method))`

## Exercise 1.

  
Write a procedure `countdown` that works like this:

`(countdown 10)`

` (10 9 8 7 6 5 4 3 2 1 blastoff!)`

`;; This should output (3 2 1 blastoff!)`

` (countdown 3)`

## Exercise 2.

  
Write a procedure `numbers` that takes a sentence as its argument and returns
another sentence containing only the numbers in the argument. You might find
the `number?` predicate useful.

`;; This should output (76 110)`

` (numbers '(76 trombones and 110 cornets))`

## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw0-3.scm .

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw0-3.scm).

## Exercise 1.

  
Write a new version of the `describe-time` procedure from Homework 0.2. You
only need to account for time periods up to a day. Instead of returning a
decimal number, it should behave like this:

`(describe-time 22222)`

` (6 HOURS 10 MINUTES 22 SECONDS)`

`(describe-time 550441)`

` (6 DAYS 8 HOURS 54 MINUTES 1 SECONDS)`

HINT: use quotient!

It would be even better if you could make the program smart enough to know
when to use the plural.

## Exercise 2.

  
Here's an example of how the procedure `remove-once` should work:

`(remove-once 'morning '(good morning good morning))`

` (GOOD GOOD MORNING) `

(It's okay if remove-once removes the other "morning" instead, as long as it
removes only one of them.)

Write `remove-once`.

## Exercise 3.

  
Write `differences`, which takes a sentence of numbers as its argument and
returns a sentence containing the differences between adjacent elements. (The
length of the returned sentence is one less than that of the argument.)

`;; This should output (19 -14 78 -81 6)`

` (differences '(4 23 9 87 6 12))`

## Exercise 4.

As part of computing `(factorial 6)`, Scheme computes `(factorial 2)` and gets
the answer 2. After Scheme gets that answer, how does it know what to do next?
Explain how Scheme knows what to do after it gets 2 from `(factorial 2)`. For
your reference, here is the factorial program:

`(define (factorial n)

(if (= n 0)

1

(* n (factorial (- n 1)))))`

## Exercise 4.

  
Write a procedure called `location` that takes two arguments, a word and a
sentence. It should return a number indicating where in the sentence that word
can be found. If the word isn't in the sentence, return `#f`. If the word
appears more than once, return the location of the first appearance.

`;; This should output 4`

` (location 'me '(you never give me your money))`

` ;; This should output #f`

` (location 'i '(you never give me your money))`

` ;; This should output 1`

` (location 'the '(the fork and the spoon)) `

## Exercise 5.

  
Write a procedure `initials` that takes a sentence as its argument and returns
a sentence of the first letters in each of the sentence's words.

`;; This should output (i i n s)`

` (initials '(if i needed someone))`

## Exercise 6.

  
Write a procedure `copies` that takes a number and a word as arguments and
returns a sentence containing that many copies of the given word.

`;; This should output (spam spam spam spam spam spam spam spam)`

` (copies 8 'spam)`

## Exercise 7.

  
Write a `GPA` procedure. It should take a sentence of grades as its argument
and return the corresponding grade point average. Hint: write a helper
procedure base-grade that takes a grade as argument and returns 0, 1, 2, 3, or
4, and another helper procedure grade-modifier that returns −.33, 0, or .33,
depending on whether the grade has a minus, a plus, or neither.

`;; This should output 3.67 or 3.66.`

` (gpa '(A A+ B+ B))`

## Exercise 8.

  
Write `expand`, which takes a sentence as its argument. It returns a sentence
similar to the argument, except that if a number appears in the argument, then
the return value contains that many copies of the following word.

`(expand '(4 calling birds 3 french hens))`

` (CALLING CALLING CALLING CALLING BIRDS FRENCH FRENCH FRENCH HENS) `

`;; This should output (the samurai samurai samurai samurai samurai samurai
samurai).`

` (expand '(the 7 samurai))`

HINT: You don't have to do all the work in just one procedure. Using a helper
procedure may help.

## Exercise 9.

  
Write a predicate `same-shape?` that takes two sentences as arguments. It
should return #t if two conditions are met: The two sentences must have the
same number of words, and each word of the first sentence must have the same
number of letters as the word in the corresponding position in the second
sentence.

`;; This should output #t`

` (same-shape? '(the fool on the hill) '(you like me too much))`

` ;; This should output #f`

` (same-shape? '(the fool on the hill) '(and your bird can sing))`

HINT: A ```count` procedure may be useful.

**You must finish both lab and homework for a lesson before submitting your homework for that lesson.**

**IF YOU HAVE ANY TROUBLE WITH SUBMITTING, ASK A QUESTION ON PIAZZA OR TALK TO A TA.**

To submit your assignment, you need to be logged in on any of the lab
computers. If you want to submit from home, you must connect remotely to the
lab computers. More on that later.

Now, right click on the background and select xterm. Xterm is a terminal
emulator, a method of interacting directly to the computer via text commands.
It's sort of an "interpreter" for your entire computer. You can do useful
things with xterm like navigate and manipulate the filesystem (think Windows
Explorer), submit homework (what we're doing now), and start the Scheme
interpreter (via stk)!

If you've been saving your assignments in your Desktop folder, you need to go
there. If you were using Windows or MacOS, you'd probably open up a graphical
interface and click the Desktop folder icon. In xterm, we do

`cd ~/Desktop`

This tells the computer to change directories (a directory is what we'd call a
folder in Windows) from wherever you are now, to ~/Desktop, a folder named
Desktop that happens to be in your home directory (that's what the (~/) is
for).

From there, you can type

`ls`

which shows all of the files and folders in ~/Desktop. Make sure that your HW
1 file is in there. If not, using cd and ls, go to the folder which contains
your HW 1 file. Then, you can type:

`submit hw0-3`

to submit Homework 1. If you have more than one file in your Desktop folder,
submit will ask you "Do you want to submit …" for each file. Say (type) 'no'
to every file except for the HW 1 file.

Here is a quick video showing this for hw4: http://youtu.be/N_fmp6p9Ot0

