# Due by April 28th, 2016 at 11:59PM PST (but you should probably do this before/during Project 4)

## Template

Download [here](https://drive.google.com/open?id=0Bx-YJoc_dDDGQjhHSnNlRDNkaTg).

## Autograder

Sorry! There's no autograder as of now. Just test your work as best you can, you'll be graded pretty leniently. A for effort. It'll be in the works if time permits.

## Exercises

**Homework Problem 1: Naughty Strings**

What is the error message returned when you improperly use quotes inside of strings?

Provide an example and explain the error message.

*****

**Homework Problem 2: Fruits and Vegetables*

```x = ["apple", "banana", "carrot"]```

Write one line of code that when executed returns "apples bananas and carrots". 

*****

**Homework Problem 3: Fizz Buzz**

Write a program that prints the integers from 1 to n (n is an argument to the procedure).
But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".

*****

**Homework Problem 4: Snow White and the Seven Dwarves**

Write a program called snow_white that takes in two numbers as arguments, the first is the num_chants, the second is the max_sing.

The program:
1. prints "heigh" "ho" alternatingly
2. prints "its off to work we go" after num_chants of "heigh" or "ho"
3. stops printing after having "it's off to work we go" max_sing times

EXAMPLE: should print it's off to work we go between every ```5``` alternating his and hos, for a maximum of ```2``` times.

    snow_white(5, 2)
    heigh
    ho
    heigh
    ho
    heigh
    it's off to work we go
    ho
    heigh
    ho
    heigh
    ho
    it's off to work we go

Use a while loop (and possibly control statements) to accomplish this behavior.

*****

**Homework Problem 5: Push First Odd Back (taken from CS10)**

Write a function called push_first_odd_back that takes in a list as an argument
This function should place the first odd number at the back of the input list. 
Do not return a new list - in fact this function shouldn't return anything, 
it should only modify the input list. (Hint: use the while loop)

*****

**Homework Problem 6: Cats and Dogs**

Write a program that return True if the string "cat" and "dog" appear the same number of times in the given string. 

    cat_dog('catdog') → True
    cat_dog('catcat') → False
    cat_dog('1cat1cadodog') → True

*****

**Homework Problem 7: Character Frequencies**

Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. 
Represent the frequency listing as a Python dictionary with each letter as a key that stores the number of times that letter appears. 
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

*****

**Homework Problem 8.1: Caesar's Ciphers**

Write a function rotate_letters() that takes in a number and creates a new mapping of lower case letters offset by that number.
Return the new mapping as a dictionary such that the original letter is mapped to the shifted letter.
For example, ```rotate_letters(2)``` would map ```'a'```-```'c'```, ```'b'```-```'d'```, ```'c'```-```'e'``` and so on.


**Homework Problem 8.2: Caesar's Ciphers**

Write a function decode_cipher() that takes in a dictionary of letter mappings and a cipher string (of only lower case letters).
Return the decoded string that is created when every character is replaced by its mapping from the dictionary
For example, ```decode_cipher(rotate_letters(2), "abc")``` should return ```"cde"```
Use this function to decode "jbj fpurzr vf terng" given that the letters had been shifted by 13.

*****

**Homework Problem 9: Memoized Factorial**

Write a memoized factorial procedure in a similar fashion to memo_fib. You MUST use recursion.

(Factorial of 5 = 5 * 4 * 3 * 2 * 1)

*****

**Homework Problem 10: Growing Pains (Exponentially)**

Write a generator ```gen_exp()``` that takes a number n and generates (for eternity) the exponential of n to the n to the n starting at n.
For example the first few elements of ```gen_exp(2)``` should be 2, (2^2), ((2^2)^ 2), (((2^2)^ 2) ^ 2)

*****

## Submit Your Homework!

Submit as python_hw instead of hw12. Please submit on/after April 1, 2016 (not earlier)!

For instructions, see [this guide](../submit.html). It covers basic terminal commands and assignment submission.

If you have any trouble submitting, do not hesitate to ask a TA!
