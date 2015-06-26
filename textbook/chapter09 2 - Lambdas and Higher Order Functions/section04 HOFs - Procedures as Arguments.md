Formally defined, a **Higher Order Function (HOF)** is any function that does at least one of the following:

  * Takes a function(s) as an argument(s)
  * Returns a function as its output

Before we jump in, let's have a quick refresher.

## The Substitution Model Revisited

You should already be very familiar with defining functions like this:

    (define (f x)
      (plus1 x))

In this function definition, the parameter of `f` is `x`, which is fed into the body as an argument to the built-in procedure `plus1`. If we bring back our substitution model from Lesson 1, we can say that a call to `f`, say, `(f 5)`, would be evaluated with the following steps:

    -> (f 5)
    -> (plus1 5)
    6

The argument `5` is substituted into the body of `f` and we call `plus1` on `5` to get `6`. Alright, that was too easy. But what if, instead of using `x` as an argument to the function in the body, we use it as the _function_?

## A Simple Higher Order Function

Let's look at an example.

    (define (f g)
      (g 2))

Do you see how `g` is in front? Hmm. What happens if we call `(f 5)` this time?

    -> (f 5)
    -> (5 2)
    ; application: not a procedure;
    ;  expected a procedure that can be applied to arguments
    ;   given: 5
    ; [,bt for context]

Whoops. Looks like we need to feed `f` a procedure instead.

    -> (f square)
    -> (square 2)
    4

We could also feed `f` a lambda function!

    -> (f (lambda (x) (* x x)))
    -> ((lambda (x) (* x x)) 2)
    -> (* 2 2)
    -> 4

Would you look at that! We just defined a function, `f`, that takes a procedure, `g`, as its argument and applies `g` to `2`. There it is, your first higher order function. Play around and see if you can define your own procedures that take other procedures as arguments.

## Uses of Passing Functions as Arguments

Now that we've seen how functions can be passed around, let's actually explore
how this can be useful.

Consider the following three functions:

<pre><code>(define (sum-doubles a b)
  (if (> a b)
      0
      (+ <u>(* 2 a)</u> (sum-doubles (+ a 1) b))))    

(define (sum-squares a b)  
  (if (> a b)
      0
      (+ <u>(square a)</u> (sum-squares (+ a 1) b))))

(define (sum-cubes a b)
  (if (> a b)
      0
      (+ <u>(cube a)</u> (sum-cubes (+ a 1) b))))</code></pre>


These three functions compute the sum of the doubles, squares, and cubes of all integers between a and b, respectively.

For example, `(sum-squares 5 8)` computes 5<sup>2</sup> + 6<sup>2</sup> + 7<sup>2</sup> + 8<sup>2</sup>.

Defining all three of these functions seems a bit redundant. Do you see how these three functions are nearly identical in definition, except for the underlined portions of the code? It's time to build some abstraction.

We know that for each of the three functions, we apply some operation to every element between `a` and `b`. So instead of having a specific function for each operation, let's abstract it away and put it in the function parameters!

So instead of having a specialized `sum-[op]` function for every possible operator, we'll just have a general function called `sum`:

<pre><code>(define (sum <u>fn</u> a b)
  (if (> a b)
      0
      (+ <u>(fn a)</u> (sum <u>fn</u> (+ a 1) b))))</code></pre>

We've underlined the major differences in the code above. In this definition of `sum`, we apply some input function `fn` to each number between `a` and `b`, as you can see in the recursive call.

Now, we can do this:

    (sum (lambda (x) (* 2 x)) 5 8)

and this:

    (sum square 5 8)

and this too:

    (sum cube 5 8)

Having only written one procedure, `sum`, we get the functionality of all three procedures above. What a deal!

If you like, the initial three procedures can be redefined using `sum` as follows:
    
    
    (define (sum-squares a b)
      (sum square a b))
    
    (define (sum-cubes a b)
      (sum cube a b))
    
    (define (sum-doubles a b)
      (sum (lambda (x) (* 2 x)) a b))

In your homework, we will take the abstraction of `sum` even further with an extremely useful and well-known HOF called `accumulate`. **Make sure you understand how `accumulate` works, as you will need it in future exercises!**