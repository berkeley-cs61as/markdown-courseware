## Breaking Down Recursion

Now we are going to look at how recursion does the magic. Let's start by
figuring out `factorial.`

    
    (define (factorial n)
      (if (= n 0)
          1
          (* n (factorial (- n 1)))))

`factorial` returns 1 when `n` is 0, otherwise it returns the product of `n`
and the factorial of `n` - 1.

## How Does It work?

At this point, you may still be wondering how a function can be defined in
terms of itself. If you use `factorial` in the middle of defining `factorial`,
shouldn't you get an error saying that `factorial` isn't defined yet? We'll go
over that on the next page...

## Leap of Faith

So how can `factorial` call itself in the middle of the definition when it's
not completely defined? Well in order to make it work, you have to believe
that it works. We call this the _leap of faith_.

The leap of faith is actually a technique for writing recursive procedures.
You have to imagine that the procedure you're writing already works for any
problem smaller than the one you're currently tackling. So while you're
thinking about how to compute `(factorial 5)`, imagine that `(factorial 4)`
will be magically computed for you. This will keep your own thoughts from
getting stuck in an infinite loop.

The technical reason why recursion works is because procedures are _not_
evaluated when you define them. Remember,
`[define](https://preview.edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/define/)` is a special form that keeps the procedure body from
being evaluated. The body is only evaluated when you call the procedure
outside of the definition, and then the recursive calls are evaluated one by
one as Scheme gets to them.

Type each function above in the
[interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-scheme-
stk/index.html) and see what Scheme outputs:

## `factorial` Revisited

Let's look at the definition of factorial again. Hopefully it makes more sense
at this point.

    (define (factorial n)
      (if (= n 0)
          1
          (* n (factorial (- n 1)))))

So as part of computing `(factorial 6)`, Scheme computes `(factorial 0)` and
gets the answer 1. After Scheme gets that answer, it uses the answer to
calculate `(factorial 1)` by multiplying it with 1 (the argument), and uses
the resulting value to calculate `(factorial 2)`, and so on. When Scheme
finally gets the answer for `(factorial 5)`, it multiplies 6 by the answer for
`(factorial 5)`, and returns the resulting value.

Here's the process:

    
    (factorial 6)
    (* 6 (factorial 5))
    (* 6 (* 5 (factorial 4)))
    (* 6 (* 5 (* 4 (factorial 3))))
    (* 6 (* 5 (* 4 (* 3 (factorial 2)))))
    (* 6 (* 5 (* 4 (* 3 (* 2 (factorial 1))))))
    (* 6 (* 5 (* 4 (* 3 (* 2 (* 1 (factorial 0)))))))
    (* 6 (* 5 (* 4 (* 3 (* 2 (* 1 1))))))
    (* 6 (* 5 (* 4 (* 3 (* 2 1)))))
    (* 6 (* 5 (* 4 (* 3 2))))
    (* 6 (* 5 (* 4 6)))
    (* 6 (* 5 24))
    (* 6 120)
    720
    

In Scheme, there is a very useful procedure called `trace`, which takes a
procedure as an argument and returns the process of the procedure when the
procedure is invoked.

Here is a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type `(trace factorial)` after defining a `factorial`
procedure, then call `(factorial 6)`. What do you see? If you no longer want
to trace the procedure, simply type `(untrace factorial)`.

## Example: Fibonacci Numbers

Consider computing the sequence of Fibonacci numbers, in which each number is
the sum of the preceding two: \[0, 1, 1, 2, 3, 5, 8, 13, 21\]

In general, the Fibonacci numbers can be defined by the rule
\[\text{Fib}(n)=\begin{cases}0&\text{if }n=0\\ 1&\text{if }n=1\\
\text{Fib}(n-1)+\text{Fib}(n-2)&\text{otherwise}\end{cases}\]

We can immediately translate this definition into a recursive procedure for
computing Fibonacci numbers:

    
    (define (fib n)
      (cond ((= n 0) 0)
            ((= n 1) 1)
            (else (+ (fib (- n 1))
                     (fib (- n 2))))))

Consider what happens when we call `(fib 2)`. The procedure makes two
recursive calls `(fib 1)` and `(fib 0)`, which return 1 and 0 respectively.
These numbers are added together, and the procedure returns 1.

You may be wondering if it's really necessary to have two separate base cases.
Consider what would happen if we left out the base case for `n` = 1. `(fib 1)`
would call `(fib 0)` and `(fib -1)`. `(fib 0)` would return 0, but `(fib -1)`
would never reach a base case, and the procedure would loop indefinitely.

## Example: Pig Latin

Pig Latin is a language game where words in English are altered according to a
simple set of rules. Pig Latin takes the first consonant (or consonant
cluster) of an English word, moves it to the end of the word and suffixes an
"ay". For example, pig yields igpay, banana yields ananabay, and trash yields
ashtray.

We can write Pig Latin in Scheme using recursion and helper procedure:

    (define (pigl wd)
      (if (pl-done? wd)
          (word wd 'ay)
          (pigl (word (bf wd) (first wd)))))

    (define (pl-done? wd)
      (vowel? (first wd)))

    (define (vowel? letter)
      (member? letter '(a e i o u)))

member? is a Scheme primitive procedure. it takes two arguments, a letter and
a sequence of letters and returns true if the letter is in the sequence.

Pig Latin is done when a vowel is found, so the base case is when `pl-done?`
returns true, and it just concatenates* "ay" at the end of the word.
Otherwise, in the recursive case, it calls itself with the concatenation of
the butfirst of the word and the first of word.  Think about what happens if
the word contains no vowels.

* When we concatenate two words, we just join them end-to-end (e.g. concatenation of CS and 61AS is CS61AS)

Here's a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Play with `pigl`! Also `trace` it and see what Scheme
outputs:

## Sentences

In Scheme, you quote a group of words in order to represent a sentence. For
example, to express "I love Scheme," you have to type `'(I love Scheme)`.
Another way of constructing a sentence is to use a `se` procedure. se
procedure takes as many arguments as you want, and make a sentence with the
arguments.

Just like words, you can use `first`, `bf`, `last`, `bl` procedures on
sentences. The only difference is that they return a word, not a letter.

For example:

`(se 'hey 'it 'is 'neil!)` returns `(hey it is neil!)`.

`(first '(hey it is neil!))` returns `hey`.

`(bf '(hey it is neil!))` returns `(it is neil!)`.

`(last '(hey it is neil!))` returns `neil!`.

`(bl '(hey it is neil!)` returns `(hey it is)`.

Here's a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html), so play around with sentences! You'll have to know
well enough them for the next example.

## Base Case

To solve this problem, we will handle the empty sentence as a separate base
case. The predicate `empty?` is used to check for the empty sentence. Here is
the completed version of `sum-sent`:

    
    (define (sum-sent sent)
      (if (empty? sent)
          0
          (+ (first sent) (sum-sent (bf sent)))))

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Define `sum-sent` and play with it! Make sure you
understand it:

## Further Reading

If you think you need some more detailed explanation of recursion, read
[Simply Scheme: How Recursion Works](http://www.cs.berkeley.edu/~bh/ssch13
/convince-recur.html).

## Exercises

Let's see how much you got from this subsection!

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type the above definitions and see if they work:

## What's Next?

Now the next subsection will work on common recursive patterns. Go check it
out!

