## Review on Conditionals

We used `if` and conditionals in our first lab.
In this section, we will flesh out more details.

We generally use an `if` or a `cond` when we want our function to behave
differently depending on a certain condition. Note that these two functions are
_special forms_ in Racket; we don't evaluate them using the usual
"evaluate the operands fully, and then apply the operator" method.

## `cond` Examples

The general form of a `cond` expression is:

```
(cond  (<test1> <result1>)
       (<test2> <result2>)
       ...
       (<testn> <resultn>)
       (else <default>))  ;; The 'else' case is optional
```

Each `(<test> <result>)` pair is called a _clause_. The first part
of each pair (the `<test>`) is a _predicate_&mdash;an expression that must evaluate
to either true or false.

To evaluate a `cond` expression, start by evaluating `<test1>`. If it is true, evaluate
and return `<result1>`. If `<test1>` is false, repeat for `<test2>`, and so on until there
are no more tests. If you hit an `else`, return the value corresponding to it (the "default value").

You can write a `cond` expression as a series of 'if' statements:

```
(if <test1>
    <result1>
    (if <test2>
        <result2>
        ...
        (if <testn>
            <resultn>
            <default>) ;; Closing parentheses omitted
```       

### Exercise

The function `plural` below takes in a word and returns its plural form. For example, `(plural 'carrot)` returns `'carrots` and `(plural 'body)` returns `'bodies`. It does _not_ perform correctly for `(plural 'boy)`, which _should_ return `'boys`; the buggy version below returns `'boies` instead.

```
(define (plural wd) 
  (if (equal? (last wd) 'y) 
      (word (bl wd) 'ies)
      (word wd 's)))
```

<div class="mc">
Choose which line of code to add in the blank below so that (plural 'boy) behaves correctly (that is, it should return boys). Suppose `vowel?` is defined as before.

<pre><code>(define (plural wd) 
  (if __________________
      (word (bl wd) 'ies)
      (word wd 's)))
</code></pre>

<ans text="(and (equal? (last wd) 'y') (not (vowel? (last (bl wd)))))" explanation="What if the word is only a letter long?" ></ans>
<ans text="(or (equal? (last wd) 'y)) (> (length word) 1) (not (vowel? (last (bl wd)))))" explanation="This will return true for any word that ends with y." ></ans>
<ans text="(and (equal? (last wd) 'y)) (> (length word) 1) (not (vowel? (last (bl wd)))))" explanation="Yup!" correct></ans>
<ans text="(equal? (last wd) 'y)" explanation="That's just the original code!"></ans>
<!-- and so on -->
</div>

## Predicate and Style

A predicate is any expression that returns true or false. Some examples
include `(< 3 4)`,` (> 10 -2)`, and `(= 'apple 'orange)`. You can form compound
predicates by using `and`, `or`, and `not`.

Here is an example of a predicate:

```
(define (even? x)
  (= (remainder x 2) 0))
```

When defining a predicate, it is conventional to end the name of the procedure
with a question mark (`?`).

Here's another way to define `even?`:

```
(define (even? x)
  (if (= (remainder x 2) 0)
      #t
      #f))
```

Although this definition is equivalent to the original definition above, it contains redundancies.
We urge you to avoid writing code like this.
Redundant code can make your programs more difficult to understand, and is typically considered
an example of bad programming style.

### Exercises

We define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers

For example, `(max-sum-squares 1 2 3)` returns `13`, which is `4 + 9`

<div class="mc">
Why isn't the code below correct?

<pre><code>(define (square x) (* x x))

	(define (max-sum-squares a b c) (max (+ (square a) (square b)) (+ (square b) (square c)) (+ (square a) (square c))))
</code></pre>
<ans text="This definition won't work for arguments that are less than 1" explanation="Nice!" correct></ans>
<ans text="This definition won't work because max only take in two arguments" explanation="Nope! Max can take in as many arguments as you want"></ans>
<ans text="This definition won't work because square needs to be defined inside of the body of max-sum-squares" explanation="Since square is defined in what's called the global environment, we can use it inside of the body of any procedure."></ans>
<!-- and so on -->
</div>

PRACTICE QUESTION:
Write a procedure `pigl` that takes a word as an argument and returns that word in pig latin. Here are the rules for pig latin:

If the input word starts with a vowel then we append "ay" to the input.

If the input word starts with a consonant then we move all the starting consonants to the end of the word and then append "ay" to the end.

Here are some examples:

<pre><code>(pigl 'hello) ; ellohay 
(pigl 'open) ; openay 
(pigl 'scheme) ; emeschay
</code></pre>

What happens if our input doesn't have a vowel, like `(pigl 'my)`? Make sure your `pigl` checks if a word has no vowels and just returns that word directly. 

<pre><code>(pigl my) ; my
</code></pre>

Check your answer in your Racket interpreter with the examples above!

