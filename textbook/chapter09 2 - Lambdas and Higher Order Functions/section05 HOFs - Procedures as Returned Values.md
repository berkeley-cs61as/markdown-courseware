We've seen how to write a procedure that takes another procedure as an argument. It turns out we can do the opposite as well - we can create a procedure that _returns_ a procedure! Returning procedures is a great way to abstract even further. Instead of creating the procedure directly, we can have a program that creates the procedure for us! Depending on what arguments we give the program, it can create many different procedures.

## Example: `make-power`

(We're not actually making power. That'd be powerplaying ;).)

Let's say we want to define a procedure `sum-powers` that takes the `n`th power of everything number between `a` and `b` and sums them together. We already have our `procedure`, reproduced below:

	(define (sum f a b)
		(if (> a b)
			0
			(+ (f a) (sum (+ a 1) b))))

From what we learned so far, it'd look something like this:

	(define (sum-powers n a b)
		(sum (lambda (x) (expt x n)) a b))

But what if we create a new function called `make-power`, that, given a power `n`, returns a _function_ that takes a number `x` and returns its `n`th power? It looks like this:

	(define (make-power n)
		(lambda (x) (expt x n)))

As we noted earlier, lambdas return functions. This means that if we define the call to `make-power` as a lambda, it will return a function! We can now do this:

	(define square (make-power 2))
	(define cube (make-power 3))

And we can rewrite our sum-powers function like this:

	(define (sum-powers n a b)
		(sum (make-power n) a b))


Note also how much we've progressed in abstraction. At the beginning of this
lab, we defined a different procedure for each different type of sum: `sum-doubles`, `sum-squares`, and `sum-cubes`.

But now, we have abstracted the summation itself, so that we can express any
summation in a single clear line.