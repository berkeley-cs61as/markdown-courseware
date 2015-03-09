## pitfalls

You should keep in mind the structure of cond. If you're code is not working,
it is possible you're missing a parenthesis or added an extra one. I will
repeat this since this is a small paragraph and you will therefore probably
not pay much attention to it even though its important. PAY ATTENTION TO
PARENTHESIS WHEN USING COND.PAY ATTENTION TO PARENTHESIS WHEN USING COND.PAY
ATTENTION TO PARENTHESIS WHEN USING COND.PAY ATTENTION TO PARENTHESIS WHEN
USING COND.

Another issue is that and and `or` cannot be used as if they were in English.
To clarify, suppose we have an expression that checks whether an argument was
"yes" or "no":

`(equal? argument (or 'yes 'no))`

This is WRONG. Remember `or` returns the first thing that is not false. Thus
this expression ultimately is evaluated as:

(equal? argument 'yes)

If you want to check is the argument was "no" as well, you need to have two
equality checks:

`(or (equal? argument 'yes) (equal? argument 'no))`

One last thing, DO NOT make your code redundant. Be smart with it, like
everything else in life.

`(define (even? number)

(if (not (odd? number))

#t

#f))

`

This is bad coding practice as you could have written this in just one line:

`(define (even? number)

(not (odd? number)))`

You do not need an `if` statement to return true or false if those are the
only 2 choices.

