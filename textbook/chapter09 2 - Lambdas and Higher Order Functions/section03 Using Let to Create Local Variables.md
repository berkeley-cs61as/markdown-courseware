**Local variables** are variables that only exist within a local environment. Here's an example:

    (define (foo x)
      (define a 5)
      (+ x a))

The local environment is the environment created by the function `foo`, and the local variable is `a`. Note that `x` is *not* a local variable, even though it also cannot be accessed outside of `foo`&mdash;it is formally called the parameter.

## Introduction to `let`

The special form `let` is essentially a call to a lambda function, arranged differently. For example, take the following lambda function call:

    -> ((lambda (x y z) (+ x y x z)) 1 2 3)
    7

This is equivalent to the following let statement:

    -> (let ((x 1) (y 2) (z 3)) (+ x y x z))
    7

When will this ever be useful? Two words: local variables. Rarely will we use a `let` statement to simply call a lambda function. Instead, we use it create local variables inside of a function.

## An Example: Polynomials

Let's say we want to use Racket to compute the following polynomial with any given *x* and *y*:

[mathjax]f(x,y) = x(1+xy)^2 + y (1-y) + (1+xy)(1-y)[/mathjax]

Rewriting this ugly polynomial as an ugly procedure:

    (define (f x y)
      (+ (* x (+ 1 (square (* x y)))) (* y (- 1 y)) (* (+ 1 (* x y)) (- 1 y))))

Yuck. Instead, we could use some substitution:

[mathjax]\displaystyle a = 1 + xy[/mathjax]

[mathjax]\displaystyle b = 1 -y[/mathjax]

So that we get:

[mathjax]\displaystyle f(x,y) = xa^2 + yb + ab[/mathjax]

Okay, I guess that's better. Writing this in Racket, we will define a helper function called `f-helper` so that we can use substitution:

    (define (f x y)
        (define (f-helper a b)
            (+ (* x (square a))
               (* y b)
               (* a b)))
        (f-helper (+ 1 (* x y))
                  (- 1 y)))

Take a minute to confirm that this does the same thing as the earlier definition of `f`. As we learned in the previous section, we don't really need an extra function definition inside `f`. Instead, we can use a lambda:

    (define (f x y)
        ((lambda (a b)
            (+ (* x (square a))
               (* y b)
               (* a b)))
        (+ 1 (* x y))
        (- 1 y)))

Sadly, even after all this substitution and reorganizing, it's still a bit messy. This is where `let` comes in!


    (define (f x y)
       (let ((a (+ 1 (* x y)))
             (b (- 1 y)))
         (+ (* x (square a)) (* y b) (* a b))))

Finally, we get a more readable version of our initial polynomial function `f`. We can clearly see that we're assigning a value to `a` and `b`, then plugging it into the body of the `let` statement.

## `let`: General Form

The general structure of a let statement is

    (let ((<var1> <exp1>)
          (<var2> <exp2>)
          ...
          (<varn> <expn>))
      <body>)

Remember, underneath, this is nothing more than a lambda call. The above structure is equivalent to

    ((lambda (<var1> <var2> ... <varn>) <body>)
      <exp1> <exp2> ... <expn> )


Try out these expressions (and more!) in the Racket interpreter.

(Note: A semicolon denotes a comment. Racket will ignore the rest of the line
after a semicolon.)

    
    (define y 10)  
    
    (let ((y 0)) y) ;; notice that let overrides global vars  
    
    (let ((x 10)  
          (z x))   
        z) ;; this will break, translate to lambda to see why  
    
    (let ((a 1))  
      (let ((a 2))  
        (let ((a 3))  
           a))) ;; nested lets are valid.   
    
    (let ((test 'wait-what?))  
      5)  
    test  ;; let only binds variables inside its body  
    
    (let ((a 1))  
      (+ a (let ((a 2))  
        (+ a (let ((a 3))  
                a))))) ;; challenge: figure out what that last one returns, before checking interpreter  
     

