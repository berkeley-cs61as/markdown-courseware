## Introduction to recursion

> "In order to understand recursion, one must first understand recursion."

>

> "Did you mean: _[recursion](https://www.google.com/search?q=recursion)"_

## PREREQUISITES AND WHAT TO EXPECT

For this lesson, you have to have understood lessons 0.1 and 0.2 well.

In this lesson, you will learn recursion, one of the central ideas of computer
science. Open your mind and be prepared to see the magic recursion does!

## Readings

Here are the relevant readings for this lesson:

  * [SS Ch. 11 - Introduction to Recursion](http://www.cs.berkeley.edu/~bh/ssch11/recursion.html)
  * [SS Ch. 12 - The Leap of Faith](http://www.cs.berkeley.edu/~bh/ssch12/leap.html)
  * [SS Ch. 13 - How Recursion Works](http://www.cs.berkeley.edu/~bh/ssch13/convince-recur.html)
  * [SS Ch. 14 - Common Recursive Patterns](http://www.cs.berkeley.edu/~bh/ssch14/recur-patterns.html)

## What is recursion?

Recursion is a method for writing procedures that solve certain types of
problems. These problems have solutions that depend on solutions to smaller
instances of the same problem. Oftentimes, recursion has us repeat the same
procedure over and over again. It looks a little like this:

![](http://caseelse.net/wp-content/uploads/2008/05/recursionagain.jpg)

What's peculiar about recursive procedures, however, is that in order to
perform the same procedure, we call the recursive procedure itself within
itself. Let's go stare at an example.

## Example: factorial

In math, the factorial of a non-negative integer \(n\), denoted by \(n\)!, is
the product of all positive integers less than or equal to n. For example,
\(3! = 3\times 2\times 1\). Also, by definition, \(0! = 1\).

How can we write the factorial procedure in Scheme? Certainly, we can't write
just the product of several numbers since we want to calculate the factorial
of any number.

Here's an idea: For any number \(n \geq 1\), we can see that \(n! =
n\times(n-1)!\), and for \(n = 0\), \(n! = 1\). We can use this to write
`factorial`. Look at it closely and play with it! It's ok if you don't
understand the code at the moment. We will go through how it works in the next
subsection.

    
    (define (factorial n)
      (if (= n 0)
          1
          (* n (factorial (- n 1)))))

Here is a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Try out `factorial` with various numbers:

## takeaways

Here are some things covered in this subsection:

  1. What is recursion?
  2. How factorial is defined using recursion?

## now what?

Go to the next subsection and learn how recursion works.

