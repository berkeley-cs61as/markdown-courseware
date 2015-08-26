## The "Every" Pattern

Here's a procedure to square every number in a sentence of numbers:

    (define (square-sent sent)
      (if (empty? sent) `
          '()
          (se (square (first sent))
              (square-sent (bf sent)))))

Here's a procedure to translate every word of a sentence into Pig Latin:

    (define (pigl-sent sent)
      (if (empty? sent)
          '()
          (se (pigl (first sent))
              (pigl-sent (bf sent)))))

The pattern here is pretty clear. Our recursive case will do something straightforward to the `first` of the sentence, such as `square`ing it or `pigl`ing it, and we'll combine that with the result of a recursive call on the `butfirst` of the sentence.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
<strong>Note:</strong> This is Exercise 5 on your Homework.<br><br>
Write a procedure called <code>initials</code> that takes in a sentence as its argument and returns a sentence of the first letter of each word in the sentence. For example:

<pre><code>-> (initials '(if i needed someone))
'(i i n s)</code></pre>
</div>

## The "Keep" Pattern

In the "every" pattern, we collect the results of transforming each element of a word or sentence into something else. This time we'll consider a different kind of problem: choosing some of the elements and filtering out the others.

First, here is a procedure to select the three-letter words from a sentence:

    -> (define (keep-three-letter-words sent)
         (cond ((empty? sent) '())
               ((= (count (first sent)) 3)
               (se (first sent) (keep-three-letter-words (bf sent))))
               (else (keep-three-letter-words (bf sent)))))

    -> (keep-three-letter-words '(one two three four five six seven))
    '(one two six)

Next, here is a procedure to select the vowels from a word:

    -> (define (keep-vowels wd)
         (cond ((empty? wd) "")
               ((vowel? (first wd))
               (word (first wd) (keep-vowels (bf wd))))
               (else (keep-vowels (bf wd)))))

    -> (keep-vowels 'napoleon)
    'aoeo

Let's look at the differences between the "every" pattern and the "keep" pattern. First of all, the "keep" procedures have three cases, instead of just two as in most of the "every" procedures. In the "every" pattern, we only have to distinguish between the base case and the recursive case. In the "keep" pattern, there is still a base case, but there are two recursive cases: we have to decide whether or not to keep the first available element in the return value. When we do keep an element, we keep the element itself, not some function of the element.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Write a procedure called <code>numbers</code> that takes a sentence as its argument and returns another sentence containing only the numbers in the sentence. You may find the <code>number?</code> predicate useful.

<pre><code>-> (numbers '(76 trombones and 110 cornets))
'(76 110)</code></pre>
</div>

## The "Accumulate" Pattern

Here are two recursive procedures for functions that follow the "accumulate" pattern, which combines all of the elements of the argument into a single result:

    -> (define (addup nums)
         (if (empty? nums)
             0
             (+ (first nums)
                (addup (bf nums)))))
    -> (addup '(8 3 6 1 10))
    28

    -> (define (scrunch-words sent)
         (if (empty? sent)
             "" ; This is an empty word
             (word (first sent)
                   (scrunch-words (bf sent)))))
    -> (scrunch-words '(ack now ledge able))
    'acknowledgeable

What's the pattern? We're using some combiner (`+` or `word`) to connect the word we're up to with the result of the recursive call. The base case tests for an empty argument, but the base case return value must be the identity element of the combiner function.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
In this subsection, we went through various functions as an example of recursion. Which of these functions below follow the accumulate pattern? Select all that apply.

<pre><code>(define (pigl wd)
  (if (pl-done? wd)
      (word wd 'ay)
      (pigl (word (bf wd) (first wd)))))
  
(define (count-ums sent)
  (cond ((empty? sent) 0)
        ((um? (first sent)) (+ 1 (count-ums (bf sent))))
        (else (count-ums (bf sent)))))
  
(define (fib n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1)) (fib (- n 2))))))</code></pre>

<ans text="pigl" explanation="" correct></ans>
<ans text="count-ums" explanation="" correct></ans>
<ans text="fib" explanation="" correct></ans>
</div>