Returning procedures is a great way to abstract further. Instead of creating
the procedure directly, we can have a program that creates the procedure for
us!

We'll start again with a few simple examples and move up.

Try these expressions in the interpreter:

    
    (define (make-adder num) 
      (lambda (x) (+ x num))) 
     
    ((make-adder 3) 7) 
     
    (define plus3 (make-adder 3)) 
     
    (plus3 7)   
      
    (define (make-power n)  
      (lambda (x) (expt x n)))  
      
    (define cube (make-power 3))  
      
    (cube 2)

But, what's so great about procedures as returned values anyway? In the last
example, couldn't we just call + directly, instead of make-adder?

Yes, we could, but only if we just wanted to compute a sum.

If we needed to pass the function plus3 around, as an argument, saying `(make-
adder 3)` would be much nicer than saying `(lambda (x) (+ x 3))` .

Let's look at sum again. Recall that` (sum fn a b)` the same as:

`(+ (fn a) (fn (+ a 1)) ... (fn b))`

Suppose we wanted to compute the sum of powers of 4 between 1 and 4. That is,
1^4 + 2^4 + 3^4 + 4^4.

We could use lambda directly and do:

`(sum (lambda (x) (expt x 4)) 1 4) `

But, in fact, we have a procedure make-power from last section, which allows
us to bypass this lambda. Instead, we can do:

`(sum (make-power 4) 1 4) `

Isn't that much clearer?

Note also how much we've progressed in abstraction. At the beggining of this
lab, we defined a different procedure for each different type of sum: `sum-
squares, sum-cubes, sum-doubles`.

But now, we have abstracted the summation itself, so that we can express any
summation in a single clear line.

