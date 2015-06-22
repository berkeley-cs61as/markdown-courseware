## Review on Conditionals

We have used [if](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/if/) and [conditional](https://edge.edx.org/courses/uc-berkeley
/cs61as-1x/SICP/wiki/cs61as-1x/cond/) in our first lab and in this section
will flesh out more details.

We generally use an `if` or a `cond` when we want our function to behave
differently depending on a certain condition. Note that these 2 functions are
one of the few special forms in Racket; we don't evaluate them with 'evaluate
operator and operand' method discussed in the previous section.

## Cond Examples

The general form of a cond expression is as follows

`(cond  (<test1> <result1>)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` (<test2> <result2>)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` ...`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` (<testn> <resultn>)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` (else <default>))  ;; The 'else' case is optional`

The pair of expression `(<test1> <result1>)` is called a clause. The first part
of each pair (the `<test>`) is a predicate, or an expression that has to
evaluate to true or false.

How you evaluate a `cond` is as follows:

Evalute `<test1>`, if it is true, evaluate `<result1>` and return it. If `<test1>`
is false, evaluate the next `<test>`. If the result is true, evaluate and return its
corresponding `<result>`. If it is false, check the next `<test>` and so on until
you go through all the tests. If you hit an `else`, you return the value
corresponding to it (consider it the 'default value')

You can write a cond as a series of 'if' statements:

`(if <test1> `

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` <result 1>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`(if <test 2>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` <result 2>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` ...`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` (if <testn>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` <resultn>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` <default value>)  ;; Close parentheses omitted`


The function 'plural' below accepts one input, and returns its plural form. i.e. `(plural 'carrot)` returns `'carrots`, `(plural 'body)` returns `'bodies`. It does not perform correctly for `(plural 'boy)` which SHOULD return `'boys` but the buggy version below returns `'boies` instead.

<pre><code>(define (plural wd) 
  (if (equal? (last wd) 'y) 
    (word (bl wd) 'ies)
    (word wd 's)))
</code></pre>

<div class="mc">
Choose which line of code to add in the blank below so that (plural 'boy) behaves correctly (that is, it should return boys). Suppose vowel? is defined as before.

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
include `(< 3 4)`,` (> 10 -2)`, `(= 'apple 'orange)`. You can form compound
predicates by using ` and, or, not. `

Here is an example of a predicate:

`(define (even? x) (= (remainder x 2) 0))`

The convention in Racket when defining your own predicate is to end the name of the procedure
with '?'.

Notice that the following code is equivalent to the definition above:

`(define (even? x) (if (= (remainder x 2) 0)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` #t`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` #f))`

The second code example, however, is considered to be bad programming style because
of its redundancy. We urge you to avoid code like this, because it reduces readibility.


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

