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

