## The `**Every**` Pattern

Here's a procedure to square every number in a sentence of numbers:

`(define (square-sent sent)`

` (if (empty? sent) `

` '() `

` (se (square (first sent)) (square-sent (bf sent)))))`

Here's a procedure to translate every word of a sentence into Pig Latin:

`(define (pigl-sent sent)`

` (if (empty? sent) `

` '() `

` (se (pigl (first sent)) (pigl-sent (bf sent)))))`

The pattern here is pretty clear. Our recursive case will do something
straightforward to the `first` of the sentence, such as `square`ing it or
`pigl`ing it, and we'll combine that with the result of a recursive call on
the `butfirst` of the sentence.

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type in your definition above and see if it works:

## The `**Keep**` Pattern

In the every pattern, we collect the results of transforming each element of a
word or sentence into something else. This time we'll consider a different
kind of problem: choosing some of the elements and forgetting about the
others.

First, here is a procedure to select the three-letter words from a sentence:

`(define (keep-three-letter-words sent)`

` (cond ((empty? sent) '())`

` ((= (count (first sent)) 3)

(se (first sent) (keep-three-letter-words (bf sent))))`

` (else (keep-three-letter-words (bf sent)))))`

` > (keep-three-letter-words '(one two three four five six seven))`

` (ONE TWO SIX)`

Next, here is a procedure to select the vowels from a word:

`(define (keep-vowels wd)`

` (cond ((empty? wd) "")`

` ((vowel? (first wd))

(word (first wd) (keep-vowels (bf wd))))`

` (else (keep-vowels (bf wd)))))`

` > (keep-vowels 'napoleon)`

` AOEO`

Let's look at the differences between the every pattern and the keep pattern. First
of all, the keep procedures have three cases, instead of just two as in most
of the every procedures. In the every pattern, we only have to distinguish
between the base case and the recursive case. In the keep pattern, there is
still a base case, but there are two recursive cases; we have to decide
whether or not to keep the first available element in the return value. When
we do keep an element, we keep the element itself, not some function of the
element.

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type in your definition above and see if it works:

## The `**Accumulate**` Pattern

Here are two recursive procedures for functions that combine all of the
elements of the argument into a single result:

`(define (addup nums)`

` (if (empty? nums)`

` 0`

` (+ (first nums) (addup (bf nums)))))`

`(define (scrunch-words sent)`

` (if (empty? sent)`

` ""`

` (word (first sent) (scrunch-words (bf sent)))))`

`> (addup '(8 3 6 1 10))`

` 28`

`> (scrunch-words '(ack now ledge able))`

` ACKNOWLEDGEABLE`

What's the pattern? We're using some combiner (`+` or `word`) to connect the
word we're up to with the result of the recursive call. The base case tests
for an empty argument, but the base case return value must be the identity
element of the combiner function.

## further reading

If you'd like to read some more about the common recursive patterns, read
[Simply Scheme: Common Recursive
Patterns](http://www.cs.berkeley.edu/~bh/ssch14/recur-patterns.html). It goes
through the exact same materials but with additional cases and explanations.

If you're ready, go do Homework 0.3!

