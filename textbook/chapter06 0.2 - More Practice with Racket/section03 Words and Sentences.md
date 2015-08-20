## Introduction

When we think of functions, we automatically assume math and numbers. In fact, in Racket and any other functional programming language, we can have functions that manipulate non-numerical values. 

### Words

Let's say you defined a procedure called `square`: 

    (define (square x) (* x x))

But later wanted to access the actual word `'square` instead of the procedure, we would simply type `'square` (single quotation mark followed by the word square) to get the **literal word**. Notice how you do not need parentheses around the expression if you working with just a single word.

### Sentences

**Sentences** are just a collection of words grouped together with parentheses. To create a sentence, you need need one quotation outside the parentheses, like this `'(hi hey hello)`. Try practicing a bit by writing one or two words and sentences.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Try each of the following in the Racket interpreter.

<pre><code>'61AS</code></pre>
<ans text="Click to reveal answer." explanation="'Neil" correct></ans>
<pre><code>'(I love 61AS!)</code></pre>
<ans text="Click to reveal answer." explanation="'(I love 61AS!)" correct></ans>
<pre><code>('I 'love '61AS!)</code></pre>
<ans text="Click to reveal answer." explanation="This will error, since Racket will try to take the word 'I and apply it as a procedure to arguments 'love and '61AS!." correct></ans>
</div>

## `quote`

The `'` you saw in the above sections is actually an abbreviation for a function called `quote`. This means that:

  * `'x` is equivalent to `(quote x)`
  * `'(hi hey hello)` is equivalent to `(quote (hi hey hello))`

`quote` is different from most other procedures in that it does not evaluate its argument. Functions that exhibit this type of behavior are **special forms**. You do not need to understand special forms for now; we will go more in depth on this topic in a later subsection. For now, it will suffice to know that `quote` is a function that takes in one argument and returns it as a word or sentence. Take the following example:
    
    -> (define x 4)
    x
    -> x
    4
    -> (quote x)
    x
    -> 'x
    x
    

Since `quote` is used quite often, it is given the abbreviation `'`, a single quotation mark. Remember that, although it may seem this way in its abbreviated form, `quote` is simply a function that can be called like any other function in Racket.

## Word and Sentence Selectors

When working with words and sentences, it would help to have procedures that manipulate them. The procedures themselves are simple. Combining them correctly to accomplish your goal is going to the hard part. For now, here is a list of procedures you can use to select data from words or sentences.

### `first`

`first` takes in a word and returns the first letter of the word, or takes in a sentence and returns the first word of the sentence.

    -> (first 'hello)
    'h
    -> (first '(hi hey hello))
    'hi

### `last`

`last` takes in a word and returns the last letter of the word, or takes in a sentence and returns the last word of the sentence.

    -> (last 'hello)
    'o
    -> (last '(hi hey hello))
    'hello

### `butfirst` or `bf`

`butfirst`, or its abbreviated version `bf`, takes in a word and returns all but the first letter of the word, or takes in a sentence and returns all but the first word of the sentence.

    -> (butfirst 'hello)
    'ello
    -> (bf 'hello)
    'ello
    -> (butfirst '(hi hey hello))
    '(hey hello)
    -> (bf '(hi hey hello))
    '(hey hello)

### `butlast` or `bl`

`butlast`, or its abbreviated version `bl`, takes in a word and returns all but the last letter of the word, or takes in a sentence and returns all but the last word of the sentence.    

    -> (butlast 'hello)
    'hell
    -> (bl 'hello)
    'hell
    -> (butlast '(hi hey hello))
    '(hi hey)
    -> (bl '(hi hey hello))
    '(hi hey)

### `item`

`item` takes in a number `n` and a word and returns the `n`th letter in the word. Or, it takes in a number `n` and a sentence and returns the `n`th word in the sentence.

    -> (item 2 'hello)
    'e
    -> (item 2 '(hi hey hello))
    'hey

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Try and guess what Racket will output for the following expressions, then check your answers with the Racket interpreter.

<pre><code>(first '(foo foo))</code></pre>
<ans text="Click to reveal answer." explanation="'foo" correct></ans>

<pre><code>(bf '(foo foo))</code></pre>
<ans text="Click to reveal answer." explanation="'(foo)" correct></ans>

<pre><code>(equal? (first '(foo foo)) (bf '(foo foo)))</code></pre>
<code>equal?</code> is a function that checks if two elements are the same.
<ans text="Click to reveal answer." explanation="#f. 'foo is a word, while '(foo) is a sentence. They are not equal." correct></ans>
</div>

## Word and Sentence Constructors

Now that we can take apart a word or sentence, lets learn how to put them
together. 

### `word`

`word` takes in any number of words as arguments [concatenates](http://dictionary.reference.com/browse/concatenate) them into one big word.

    -> (word 'play 'ground)
    'playground
    -> (word 'fo 'o 'b 'ar)
    'foobar
    -> (word 'cs '61 'as)
    'cs61as

### `sentence` or `se`

`sentence`, or its abbreviated version `se`, takes in any number of words or sentences as arguments and creates one sentence of all of its arguments. 

    -> (sentence 'I 'love 'cs '61as!)
    '(I love cs 61as!)
    -> (se 'foo 'bar)
    '(foo bar)
    -> (se 'foo '(foo bar) 'bar)
    '(foo foo bar bar)

### The Empty Word

There is an empty word that you can combine with other words which will have no effect when used. This is represented by `""`.

    -> (word 'foo "")
    'foo
    -> (word "" 'foo)
    'foo
    -> (word "" "")
    ""

### The Empty Sentence

There is also an empty sentence that you can combine with other sentences which will have no effect when used. This is represented by `'()`.

    -> (se 'hi 'there '())
    (hi there)
    -> (se '() 'hi 'there)
    (hi there)
    -> (se 'hi '() 'there)
    (hi there)
    -> (se '() '() '())
    '()

At the moment it may not be clear as to why need these empty words and sentences. Keep these in mind for now, as they will be very useful when we learn recursion in Lesson 0-3.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
<strong>Note:</strong> This is Exercise 1 on your Homework.<br><br>

Let's build some functions to deal with words and sentences. We'll define the <code>second</code> procedure for you - this procedure returns the second letter in a word, or the second word in a sentence.

<pre><code>(define (second item)
    (first (bf item)))</code></pre>
<ol>
  <li>Write a procedure `first-two` that takes a word as its argument, returning a two-letter word containing the first two letters of the argument.</li>
  <li>Write a procedure `two-first` that takes two words as arguments, returning a two-letter word containing the first letters of the two arguments.</li>
  <li>Now write a procedure `two-first-sent` that takes a two-word sentence as argument, returning a two-letter word containing the first letters of the two words.</li>
</ol>
</div>
    

## Pitfalls

Basically the only punctuation you can use when working with words and sentences are `!` and `?`. You have already seen that the quote `'` has a special meaning in Racket. The period and comma also have special meaning, so you cannot use those, either.

As you saw in an earlier exercise, there's a difference between a word and a sentence containing one word. For example, people often mistakenly assume that the `butfirst` of a two-word sentence such as `(computer science)` is `'science`. In actuality, it is a sentence with one word: `(science)`. Another way of proving the difference between a word and a one-word sentence is by `count`-ing both of them:
    
    -> (bf '(computer science))
    '(science)  
      
    -> (count (bf '(computer science)))  
    1 ;; because there is ONE word in the sentence.
    
    -> (first (bf '(computer science)))
    'science
      
    > (count (first (bf '(computer science))))  
    7 ;; because there are SEVEN letters in the word 'science

## Takeaways

  * We can build words and sentences using `word` and `sentence`, respectively.
  * We can also make words and sentences using a quote.  
  * We can retrieve parts of a word or parts of a sentence by using procedures like `first`, `butfirst`, `last` and `butlast`.
