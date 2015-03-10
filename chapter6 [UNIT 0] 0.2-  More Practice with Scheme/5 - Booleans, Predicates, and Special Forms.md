## True and false

Sometimes, we want to express _conditionals_--that is the ability to act based
on the results of a test. For example, "If we're out of milk, then go to the
store. Else, add milk to our cereal and enjoy."

In order to do the above, we have to have some idea of true and false. Scheme
has 2 boolean values, #t and #f:

    
    > (= 1 1)
    #t
    
    > (> 3 4)
    #f
    
    > (if #t
        '(the condition was true)
        '(the condition was false))
    (the condition was true)
    
    > (if #f
        '(the condition was true)
        '(the condition was false))
    (the condition was false)
    
    > (if (= 1 1)
        '(the condition was true)
        '(the condition was false))
    (the condition was true)
    

## Predicates

A function that returns a true or false value is called a predicate. For
example, even? is a predicate used to test whether a number is even. (even? 3)
will return #f.

Lets look at some predicates that are given to us.

  * `<, >, =, <=, >=` are the standard mathematical operators for comparing 2 numbers.  Beware:  the = function can only take numbers as arguments - for words and sentences, you should use equal?.
  * `member?` takes two arguments, checking to see if the first one is a member of the second. You can use this to check if a letter is in a word OR if a word is in a sentence.
  * `empty?` checks if its argument is the empty word "" or the empty sentence '()
  * equal? checks if two values are equal to each other.

ex:

`(< 1 2)` returns #t

`(member? 'a 'aeiou)` returns #t

`(member? 'dream '(I have a dream))` returns #t

``(empty? '(hi))` returns #f`

`(equal? 'apples 'oranges)` returns #f

(`equal? 'apples 'apples)` returns #t

`(equal? '(it is a bird) '(it is a plane)`) returns #f

`(equal? '(it is a bird) '(it is a bird))` returns #t

Then there are predicates like `number?` or `word?` that check whether or not
the input is a number or word respectively. There is a predicate checking for
numbers, booleans, words, and sentences. You can also create your own
predicates like:

`(define (vowel? letter)

(member? letter 'aeiou))`

## Exercises

Write a predicate `teen?` that returns true if its argument is between 13 and
19.

## Everything That Isn't False Is True

When evaluating whether or not a statement is true or false, remember that
anything is considered true unless it is false. If you do `(if 1 2 3)`, this
code actually doesn't error and returns 2 since 1 isn't false. This is useful
for things like semipredicates. An example of a semipredicate is

`(define (integer-quotient big little)

(if (divisible? big little)

(/ big little)

#f))

`

Note how it will return a number if `big` is divisible by `little` and false
otherwise. This allows us to make statements like

    
    (if (integer-quotient 5 6)
       '(do something)
       '(do something else))

, without actually needing the predicate to evaluate exactly to true.

## And & or

`and` is a predicate that takes however many expressions and returns the last
element if everything was not false and returns false otherwise.

ex: `(and 1 2 3)` outputs 3

` (and (number? 'hi) 2 3)` outputs false

`or` is a predicate that takes however many expressions and returns the first
true element and returns false otherwise.

ex: `(or 1 #f 2)` outputs 1

`(or (even? 1) #f (number? 'foo))` outputs false

## The cond clause

If you have a huge mess of `if`'s lying around like this

`(define (roman-value letter)

(if (equal? letter 'i)

1

(if (equal? letter 'v)

5

(if (equal? letter 'x)

10

(if (equal? letter 'l)

50

(if (equal? letter 'c)

100

(if (equal? letter 'd)

500

(if (equal? letter 'm)

1000

'huh?))))))))`

Then it may be easier to use `cond`, which would do essentially the same thing
but much neater. First lets look at how at the code equivalent using `cond` to
see how it's structured.

`(define (roman-value letter)

(cond **(**(equal? letter 'i) 1**)**

** (**(equal? letter 'v) 5**)**  
** (**(equal? letter 'x) 10**)**  
** (**(equal? letter 'l) 50**)**  
** (**(equal? letter 'c) 100**)**  
** (**(equal? letter 'd) 500**)**  
** (**(equal? letter 'm) 1000**)**  
**(**else 'huh?**)** )) `

Note that within each bolded set of parenthesis (it might be hard to see,
sorry) is a predicate and what to do if the predicate were true. This code
first checks if the letter is i and if it is, it outputs 1. If the letter was
not i, then it moves on to the next set of bolded parenthesis. The final set
of bolded parenthesis is an else clause. This is the code that executes if
none of the previous predicates were true. It is possible to write cond
without using the else clause. If you don't have an else clause, the
procedures stops if none of the predicates were true.

## Special forms

Special forms are procedures that don't exactly follow normal conventions. You
were told earlier that everything within an expression is evaluated. This is
not true with special forms. `if`, `or`, and `and` are all special forms. if
does not need to evaluate both statements if its only going to use one, right?
So if you do`(if true 2 (/ 1 0))`, Scheme will ignore the division by zero
since all it needs is the 2.

`and` immediately stops evaluating all its arguments as soon as it hits false.
It evaluates from left to right. As an example look at this expression: `(and
(/ 1 0) 1 #f)` will cause an error since (/ 1 0) was evaluated first. Now if
we change the order of the statements `(and 1 #f (/ 1 0))`, there will be no
error. 1 is evaluated and then #f is evaluated. Since there is a false, `and`
immediately stops.

`or` is exactly like `and` except it stops whenever it hits anything thats not
false. `(or true (/ 1 0))` would not error out, while `(or false (/ 1 0))`
would.

The important thing to get out of this is that not all arguments are
evaluated. Suppose we wrote our own `if` procedure called `new-if` and defined
it like so:

`(define (new-if predicate if-true if-false)

(if predicate if-true if-false)) `

It works exactly like `if` (mostly because it is using `if`) but since it is
not a special form, it will evaluate all arguments so doing `(new-if 1 2 (/ 1
0))` will cause an error. Anything you define will not be a special form.

## If is composable

To save you time and coding, you should keep in mind that functions like `if`
can be used within an expression, instead of being a stand alone expression.
To demonstrate what I mean, consider the following simple function:

`(define (what-am-i age)

(if (> age 21)

'(i am a grownup)

'(i am a child)))

`

Instead you can do this:

`(define (what-am-i age)

(se '(i am a) (if (> age 21)

'grownup

'child)))

`

Admittedly, there doesn’t seem to be much of a difference. It’s understandable
considering this is a simple function. What you should keep in mind is that we
avoided typing out the whole sentence twice as with the first definition. Try
to combine as many common elements as possible before using `if`.

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

## Exercise

Write a procedure `indef-article`. See examples below for how it works.
Remember that the indefinite article for anything that starts with a consonant
is "a", and the indefinite article for anything that starts with a vowel is
"an".

`>(indef-article 'beatle)

(a beatle)

>(indef-article 'album)

(an album)

`

