## Introducing Words and Sentences

Let's say you defined a procedure called `square` but then wanted the actual
word "square" and not the procedure, simply type `'square` (single quotation
mark followed by the word square) to get the literal word. Notice you do not
need a parenthesis if you working with just a single word.

Sentences are just a collection of words grouped by parentheses. To create a
sentence, you need need one quotation outside the parentheses, like this `'(hi
hey hello)`. Try practicing a bit by writing one or two words and sentences.

## Quote

Before we move onto more words and sentences issues, we need to first discuss
the all-important `quote`. It is a special form that doesn't evaluate its
argument. Instead, it simply returns whatever is inputted as a word or
sentence.

For example,

    
    
    > (define x 4)
    x
    > x
    4
    > (quote x)
    x
    > 'x
    x
    

Since quote is used quite often, there is an abbreviation which is just the
`'` , a single quotation mark. So when you do `'hi`, you're actually doing
`(quote hi)`. and when you do `'(hi hey hello)`, you're actually doing `(quote
(hi hey hello))`. Just keep in this mind for future nuances in the Scheme
language. Use the single quotation mark `'`, but don't forget what is going on
in the background. Remember Scheme always has a procedure on the left side of
a parenthesis in a procedure call.

When working with words and sentences, it would help to have procedures that
manipulate them. The procedures themselves are simple. Combining them
correctly to accomplish your goal is going to the hard part. For now let's
just list them so we know what's available.

  * `first` takes the first letter of a word or the first word in a sentence
  * `last` takes the last letter of a word or the last word in a sentence
  * `butfirst` (or `bf` if you want to use the abbreviated version) removes the first letter of a word _or_ removes the first word of a sentence
  * `butlast` (or `bl` if you want the abbreviated version) removes the last letter of a word _or_ removes the last word of a sentence
  * `item` takes 2 arguments, a number `n` and a word or sentence and returns the nth letter of that word or the nth word of that sentence 
    
        (first 'hi) outputs h
        (first '(hi hello)) outputs hi
        (bl '(hi hey hello)) outputs (hi hey)
        (item 2 'hello) outputs e
        (item 3 '(hi hey hello)) outputs hello

Now that we can take apart a word or sentence, lets learn how to put them
together. The procedure `word` takes a group of words and puts them together
into one big word. You can have as many arguments as you want.

ex: `(word 'fo 'o 'b 'ar)` outputs `foobar`

To put together a sentence use the procedure `sentence` (or `se` for short).
It can take in words or sentences as arguments.

ex: `(se 'foo '(foo bar) 'bar)` outputs `(foo foo bar bar)`.

There is an empty word and empty sentence that you can use to combine words or
sentences which will have no effect when putting together a word or sentence.
The empty word is `""` and the empty sentence is `'()`.

ex: `(word 'foo "")` outputs foo

ex: `(se 'hi 'there '())` outputs `(hi there)`

You might be wondering what is the point of having the empty word and empty
sentence. Their importance will be revealed in the not so distant future. For
now, keep them in mind. You'll need them very soon.

## Exercises

Let's build a repertoire of functions to deal with words and sentences. We'll
define the `second` procedure for you - this procedure returns the second
letter in a word, or the second word in a sentence.

    1. Write a procedure `first-two` that takes a word as its argument, returning a two-letter word containing the first two letters of the argument.
    2. Write a procedure `two-first` that takes two words as arguments, returning a two-letter word containing the first letters of the two arguments.
    3. Now write a procedure `two-first-sent` that takes a two-word sentence as argument, returning a two-letter word containing the first letters of the two words.
    
    (define (second wd)
      (first (bf wd)))   
    

## Pitfalls

Pretty much the only punctuation you can use when working with words and
sentences are ! and ?. You have already seen that the quote has special
meaning in Scheme. The period and comma also have special meaning, so you
cannot use them either.

As mentioned before, there's a difference between a word and a single-word
sentence. For example, people often fall into the trap of thinking that the
`butfirst` of a two-word sentence such as `(frodo baggins)` is the second
word, but it's not. It's a sentence with one word. For example, its
[count](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-
1x/count/) is one, not seven:

    
    
    > (bf '(frodo baggins))
    (baggins)  
      
    > (count (bf '(frodo baggins)))  
    1
    
    > (first (bf '(frodo baggins)))
    baggins  
      
    > (count (first (bf '(frodo baggins))))  
    7

## Takeaways

  * We can build words and sentences using `word` and `sentence`, respectively.
  * `We can also make words and sentences using a quote.  
`

  * We can retrieve parts of a word or parts of a sentence by using procedures like `first`, `butfirst`, `last` and `butlast`.

If you'd like all the details, you can read more about [Words and
Sentences](http://www.cs.berkeley.edu/~bh/ssch5/words.html). Either way, time
to move on now to the next subsection!

