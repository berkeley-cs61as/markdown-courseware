## Exercises

Let's build a repertoire of functions to deal with words and sentences. We'll
define the `second` procedure for you - this procedure returns the second
letter in a word, or the second word in a sentence.

    1. Write a procedure `first-two` that takes a word as its argument, returning a two-letter word containing the first two letters of the argument.
    2. Write a procedure `two-first` that takes two words as arguments, returning a two-letter word containing the first letters of the two arguments.
    3. Now write a procedure `two-first-sent` that takes a two-word sentence as argument, returning a two-letter word containing the first letters of the two words.
    
    (define (second wd)
      (first (bf wd)))   
    

