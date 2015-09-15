**Recursion** is a method for writing procedures that solve certain types of problems. These problems have solutions that depend on solutions to smaller instances of the same problem. Oftentimes, recursion has us repeat the same procedure over and over again. It looks a little like this:

![](http://caseelse.net/wp-content/uploads/2008/05/recursionagain.jpg)

What's peculiar about recursive procedures is that in order to call the procedure, we'll need to have the procedure call itself, which will have to call itself, which will-- let's go stare at an example.

## Example: Factorial

In math, the factorial of a non-negative integer [mathjaxinline]n[/mathjaxinline], denoted by [mathjaxinline]n![/mathjaxinline], is the product of all positive integers less than or equal to n. For example, [mathjaxinline]3! = 3 * 2 * 1[/mathjaxinline]. Also, by definition, [mathjaxinline]0! = 1[/mathjaxinline].

How can we write the `factorial` procedure in Racket? This presents a challenge, since the numbers that we would like to multiply together depends on the number we want to find the factorial of, the _argument_.

Thus, we'll use recursion. Let's split it into two possible cases: 

  * if [mathjaxinline]n &ge; 1[/mathjaxinline], then [mathjaxinline]n! = n * (n-1)![/mathjaxinline]
  * if [mathjaxinline]n = 0[/mathjaxinline], then [mathjaxinline]n! = 1[/mathjaxinline]

Recursion depends heavily on _conditionals_. If we've finished, return some value. Otherwise, continue recursing. For the factorial example, we recurse until we reach [mathjaxinline]n = 0[/mathjaxinline], where we then return 1. We can use this to write `factorial`. Take a look at the Racket solution for `factorial` below and see if you can make sense of it. Try it out in the interpreter too! It's all right if you don't understand the code at the moment. We will go over recursion more explicitly in the next subsection.

    
    (define (factorial n)
      (if (= n 0)
          1
          (* n (factorial (- n 1)))))

## Takeaways

Here is what we covered in this subsection:

  1. What is recursion?
  2. How is factorial defined using recursion?

Move on to the next subsection to learn how recursion works.
