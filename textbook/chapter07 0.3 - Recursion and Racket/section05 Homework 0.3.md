## Template

Type the following command into the terminal to copy the homework template file to the current directory (note the period at the end):

```
cp ~cs61as/autograder/templates/hw0-3.rkt .
```

Or, you can download the template [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw0-3.rkt).

## Exercise 1

  
Write a new version of the `describe-time` procedure from Homework 0-2. You only need to account for time periods up to a day. Instead of returning a decimal number, it should behave like this:

```
-> (describe-time 22222)
'(6 HOURS 10 MINUTES 22 SECONDS)

-> (describe-time 550441)
'(6 DAYS 8 HOURS 54 MINUTES 1 SECONDS)
```

**Hint:** use `quotient`!

See if you can make the program smart enough to know when to use plurals;  this is not required.

## Exercise 2
  
Here's an example of how the procedure `remove-once` should work:

```
-> (remove-once 'morning '(good morning good morning))
'(good good morning)
```

(It's okay if remove-once removes the other "morning" instead, as long as it removes only one of them.)

Write `remove-once`.

## Exercise 3
  
Write the procedure `differences`, which takes a sentence of numbers as its argument and returns a sentence containing the differences between adjacent elements. (The length of the returned sentence is one less than that of the argument.)

```
-> (differences '(4 23 9 87 6 12))
'(19 -14 78 -81 6)
```

## Exercise 4

Write a procedure called `location` that takes two arguments, a word and a sentence. It should return a number indicating where in the sentence that word can be found. If the word isn't in the sentence, return `#f`. If the word appears more than once, return the location of the first appearance.

```
-> (location 'me '(you never give me your money))
4
-> (location 'i '(you never give me your money))
#f
-> (location 'the '(the fork and the spoon))
1
```

## Exercise 5

  
Write a procedure `initials` that takes a sentence as its argument and returns a sentence of the first letters in each of the sentence's words.

```
-> (initials '(if i needed someone))
'(i i n s)
```

## Exercise 6
  
Write a procedure `copies` that takes a number and a word as arguments and returns a sentence containing that many copies of the given word.

```
-> (copies 8 'spam)
'(spam spam spam spam spam spam spam spam)
```

## Exercise 7

  
Write a `GPA` procedure. It should take a sentence of grades as its argument and return the corresponding grade point average. 

**Hint:** write a helper procedure called `base-grade` that takes a grade as argument and returns `0`, `1`, `2`, `3`, or `4`, and another helper procedure called `grade-modifier` that returns `−.33`, `0`, or `.33`, depending on whether the grade has a minus, a plus, or neither.

```
-> (gpa '(A A+ B+ B))
3.67
```

## Exercise 8

  
Write `expand`, which takes a sentence as its argument. It returns a sentence similar to the argument, except that if a number appears in the argument, then the return value contains that many copies of the following word.

```
-> (expand '(4 calling birds 3 french hens))
'(calling calling calling calling birds french french french hens)
-> (expand '(the 7 samurai))
'(the samurai samurai samurai samurai samurai samurai samurai)
```

**Hint:** You don't have to do all the work in just one procedure. Using a helper procedure may help.

## Exercise 9
  
Write a predicate `same-shape?` that takes two sentences as arguments. It should return `#t` if two conditions are met: The two sentences must have the same number of words, and each word of the first sentence must have the same number of letters as the word in the corresponding position in the second sentence.

```
-> (same-shape? '(the fool on the hill) '(you like me too much))
#t
-> (same-shape? '(the fool on the hill) '(and your bird can sing))
#f
```

**Hint:** The primitive procedure `count` may be useful.

## Submit your Homework!

If you forgot how to submit homework, check out the short guide in [Homework 0-2](/textbook/homework-0.2.html).