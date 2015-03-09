Now that we've seen how functions can be passed around, let's actually explore
how this can be useful.

Consider the following three functions:

`(define (sum-squares a b)`

` (if (> a b) `

` 0`

` (+ **(square a)** (sum-squares (+ a 1) b))))`

`(define (sum-cubes a b)`

` (if (> a b) `

` 0`

` (+ **(cube a)** (sum-cubes (+ a 1) b))))`

`(define (sum-doubles a b)`

` (if (> a b) `

` 0`

` (+ **(* 2 a)** (sum-doubles (+ a 1) b))))`

These compute the sum of squares, cubes, and doubles of integers between a and
b, respectively.

For example, `(sum-squares 5 8)` computes 5^2 + 6^2 + 7^2 + 8^2 .

However, notice how very similar these are. I have bolded the differences
among them.

Can we abstract these differences somehow? Well, how would we do it?

What we need is some way to represent the operations done on `a` in each
procedure, so we can abstract them. But... that's exactly what functions do!

So, our generalized procedure can take a function as an argument and apply it
to a in the proper place.

It would look like this:

`(define (sum fn a b)`

` (if (> a b) `

` 0`

` (+ (fn a) (sum fn (+ a 1) b))))`

Now, to do the same thing as `(sum-squares 5 8)`, we do:

`(sum square 5 8)`

This is wonderful! We get the functionality of all 3 procedures above, having
only written one procedure.

If needed, the 3 special case procedures above can now be defined using sum as
follows:

`(define (sum-squares a b)`

` (sum square a b))`

    
    (define (sum-cubes a b)
      (sum cube a b))
    
    (define (sum-doubles a b)
      (define (double x) (* 2 x))
      (sum double a b))

