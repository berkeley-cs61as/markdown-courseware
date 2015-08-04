## Appending Streams

<!--
![](http://upload.wikimedia.org/wikipedia/en/e/e8/Escher_Waterfall.jpg)
-->

Suppose you have two streams and you want to merge one with the other, akin to
`append` with lists. With `append`, we join the beginning of one list
to the end of another. An equivalent stream definition would look like this:

```
(define (stream-append s1 s2)
  (if (stream-null? s1)
      s2
      (cons-stream (stream-car s1) 
                   (stream-append (stream-cdr s1) s2))))
```

But wait! Streams can be of *infinite* length! If we call `(stream-append s1 s2)`
and `s1` is an infinite stream, we'll never be able to access any of the elements of
`s2`.

## Interleaving Streams

An alternative is to **interleave** the two streams:

```
-> (ss ones)
'(1 1 1 1 1 1 1 1 1 1 ...)
-> (ss integers)
'(1 2 3 4 5 6 7 8 9 10 ...)
-> (ss (interleave ones integers))
'(1 1 1 2 1 3 1 4 1 5 ...)
```


By interleaving the two streams, we can be certain that we will use elements
from both streams. We can define `interleave` like this:

```    
(define (interleave s1 s2) 
  (if (stream-null? s1)
      s2
      (cons-stream (stream-car s1)
                   (interleave s2 (stream-cdr s1)))))
```

