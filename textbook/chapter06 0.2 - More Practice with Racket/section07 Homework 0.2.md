## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw0-2.rkt .

Or you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw0-2.rkt).

## Autograder

If you are working on the lab computers, the `grader` command will run the autograder.  If you are working on your own personal machine, you should download [grader.rkt](http://inst.eecs.berkeley.edu/~cs61as/autograder/grader.rkt) and the [hw0-2-tests](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw0-2-tests.rkt).

## Exercise 0
  
The expression `(+ 8 2)` has the value `10`. It is a compound expression made up of three atoms. For this problem, write five other Racket expressions whose values are also `10`:

  1. An atom
  2. Another compound expression made up of three atoms
  3. A compound expression made up of four atoms
  4. A compound expression made up of an atom and two compound subexpressions
  5. Any other kind of expression

## Exercise 1
  
Let's build some functions to deal with words and sentences. We'll give you the second procedure from the previous lab. You might also find the [word](/textbook/words-and-sentences.html#sub3) function useful.

  1. Write a procedure `first-two` that takes a word as its argument, returning a two-letter word containing the first two letters of the argument.
  2. Write a procedure `two-first` that takes two words as arguments, returning a two-letter word containing the first letters of the two arguments.
  3. Now write a procedure `two-first-sent` that takes a two-word sentence as argument, returning a two-letter word containing the first letters of the two words.

```
-> (first-two 'ambulatory)
'am
-> (two-first 'brian 'epstein)
'be
-> (two-first-sent '(brian epstein))
'be
```

## Exercise 2

Write a predicate `teen?` that returns `#t` if its argument is between 13 and 19, inclusive.

```
-> (teen? 19)
#t
-> (teen? (/ 39 2))
#f
```

## Exercise 3
  
Write a procedure `indef-article` that takes in a word as its only argument and returns a sentence. See examples below for how `indef-article` should work. Remember that the indefinite article for anything that starts with a consonant is "a", and the indefinite article for anything that starts with a vowel is "an". You can ignore any edge cases.

```
-> (indef-article 'beetle)
'(a beetle)
-> (indef-article 'apple)
'(an apple)
```

## Exercise 4
  
Write a procedure `insert-and` that takes a sentence of items and returns a new sentence with an `and` in the grammatically correct place.

```
-> (insert-and '(john bill wayne fred joey))
'(john bill wayne fred and joey)
```

## Exercise 5
  
Write a procedure `query` that turns a statement into a question by swapping
the first two words and adding a question mark to the end of the last word. You can ignore any edge cases.

```
-> (query '(you are experienced))
'(are you experienced?)
-> (query '(i should have known better))
'(should i have known better?)
-> (query '(you were there))
'(were you there?)
```

## Exercise 6

Write a procedure `european-time` to convert a time from American AM/PM
notation into European 24-hour notation. Also, write `american-time`, which
does the opposite.

```
-> (european-time '(8 am))
8
-> (european-time '(4 pm))
16
-> (european-time '(12 am))
0

-> (american-time 21)
'(9 pm)
-> (american-time 12)
'(12 pm)
```

## Exercise 7
  
Write a procedure `describe-time` that takes a number of seconds as its argument and returns a more useful description of that amount of time. Assume that there are 365.25 days in a year. You only need to account for time periods up to a day.

```
-> (describe-time 45)
'(45 seconds)

-> (describe-time 930)
'(15.5 minutes)
```

## Exercise 8
  
The following program doesn't work. Why not? Fix it and explain why.

```
(define (superlative adjective word)
  (se (word adjective 'est) word))
```

This is how `superlative` should work:

```
-> (superlative 'dumb 'exercise)
'(dumbest exercise)
```

## Submit your Homework!

**If you are having trouble submitting, ask a question on Piazza or contact a TA.**

**Before submitting:** Make sure your file loads in Racket.
You can verify this by typing into Racket: 

```
(require "hw0-2.rkt")
```

Where `"hw0-2.rkt"` is the name of your homework file. **You will not receive credit for homework that does not load in Racket.**

To submit your assignment, you need to be logged in on any of the lab
computers. If you want to submit from home, you must connect remotely to the
lab computers. There is a guide on how to do that [here](https://docs.google.com/document/d/1a-eE4zeEpnL7vT54gbOAn8jLElMxwqPH3GkPnE3bXdU/edit).

Open the Terminal.

Let's submit `hw0-2.rkt`. This requires the following steps:

  1. Making a directory for an assignment (optional, but strongly recommended, as we'll see)
  2. Placing the assignment in that folder (or moving the files to that folder if you've already completed the assignment)
  3. Running the `submit` command
  4. Checking if the assignment was correctly submitted

### Making a Directory

In the terminal, type:

```
mkdir hw0-2
```

This tells the computer to make a directory (folder) named `hw0-2`. You can
double check that it exists (and also see what else is in this current
directory) by running `ls`.

Now we need to navigate to that folder, so we'll do:

```
cd hw0-2
```

Now, make sure your `hw0-2.rkt` file is inside the `hw0-2` directory. The [mv](http://linux.about.com/library/cmd/blcmdl1_mv.htm) command is useful. Or, you can just do this outside of your terminal. If you need help on this step, ask a TA.

### Submitting

After your homework file is in the right directory, you can submit the assignment by doing

```
submit hw0-2
```

This tells the computer that you want to submit the assignment called "hw0-2". Follow the prompts that appear afterwards. If insanity is detected, that means your file does not load into Racket! Make tweaks to your code until it loads without errors and try submitting again.

### Checking Your Submission

The following command allows you to look at the times in which you've
submitted:

```
glookup -t
```

And you're done!