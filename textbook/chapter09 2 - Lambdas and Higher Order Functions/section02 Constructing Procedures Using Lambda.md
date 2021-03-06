Take a look at the following definition of `sum-doubles`, which takes two numbers `a` and `b`, and returns the sum of all numbers between `a` and `b` doubled.

    (define (sum-doubles a b)
        (define (double x) (* 2 x))
        (if (> a b)
            0
            (+ (double a) (sum-doubles (+ a 1) b))))

Since the `double` function was not already defined for us, we had to define it ourselves inside of our `sum-doubles` definition.

But doing that is such a waste! Outside of our `sum-doubles` definition, we won't ever be able use that `double` function. Isn't there a quick, easy way to make a user-defined function without first defining, then applying the named function?

## Lambdas: The Anonymous Function

Actually, yes. Let's introduce the **lambda** function, otherwise known as an anonymous function. These mysterious functions will be major players in the concepts we will discuss in future lessons.

The general form for a lambda is as follows:

```
(lambda (<param1> <param2> ... <paramn>) <body>)
```

Let's dissect this. Within the parentheses, we have three major parts:

  * a **tag**, `lambda`, which tells Racket that this is a lambda function,
  * a **list of parameters** (as many as you want),
  * and the **body**&mdash;anything following the list of parameters.


The procedure `double`, for example, can be defined as the following lambda function:

    (lambda (x) (* 2 x))

In other words,

    (define double (lambda (x) (* 2 x)))

would be equivalent to:

    (define (double x) (* 2 x)) 
      
When describing lambdas, you would call it "the function of [params] that returns [body]." For example, "`double` is the function of `x` that returns `(* 2 x)`."

## Calling Lambdas

Just as we can call procedures created using `define`, we can also call lambda functions. The general form of a call to a lambda is as follows:

`((lambda (<param1> <param2> ... <paramn>) <body>) <arg1> <arg2> ... <argn>)`

So if we want to call `(double 5)` as an anonymous function, the substitution model would give us this:

    -> ((lambda (x) (* 2 x)) 5)
    -> ((lambda (x) (* 2 5)) 5)
    -> (* 2 5)
    10

What happens here? When we call a lambda function, the first argument corresponds to the first parameter, the second argument to the second parameter, ..., and the nth argument to the nth parameter. Then, in the body, every occurence of each parameter is replaced with the corresponding argument.

Let's illustrate this with an example expression:

    -> ((lambda (x y z) (+ x y x z)) 1 2 3)


In the body of the lambda, we replace every occurence of `x` with `1`. We replace every `y` we see with `2`. And every time we see a `z`, we replace it with `3`.

    -> ((lambda (x y z) (+ x y x z)) 1 2 3)
    -> ((lambda (x y z) (+ 1 2 1 3)) 1 2 3)
    -> (+ 1 2 1 3)
    7

Now, we can rewrite `sum-doubles` as:

    (define (sum-doubles a b)
        (if (> a b)
            0
            (+ ((lambda (x) (* 2 x)) a) (sum-doubles (+ a 1) b))))

**Note:** The value returned by creating a `lambda` is a procedure, just as much as one made with a call to `define`.


Try these expressions out in the Racket interpreter:

    
    (lambda (x) (+ x 3))  
    ((lambda (x) (+ x 3)) 7)  
    (define add3 (lambda (x) (+ x 3)))  
    (add3 7)
    
    (define (square x) (* x x))   
    (square 5)   
    (define sq (lambda (x) (* x x)))   
    (sq 5)   
    ((lambda (x y) (+ (* 2 x) (* 5 y))) (* 100 100) (* 5 2))  
    

