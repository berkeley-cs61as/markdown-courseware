## Procedure-Ception

One of the most useful (and coolest!) parts about programming is that, once
you've defined a procedure, not only can you can use it over and over again,
you can also use it to define other procedures.

Since you're probably sick of `square` right now, let's use another function
as an example. Let's define a predicate `vowel?`, and use it to define another
procedure:

`(define (vowel? letter) (member? letter '(a e i o u))`

Now that we have `vowel?`, we can use it in different procedures. For example,
one of the problems in 0.3 deals with Pig Latin. If a word starts with a
vowel, translating that word into Pig Latin is as simple as adding "ay" to the
end of the word. We're not going to worry about translating words into Pig
Latin right now, we're just going to define yet another predicate to check if
a word starts with a vowel.

`(define (pig-complete? wd) (vowel? (first wd)))`

As you can see, we used one user-defined procedure (`vowel?`), to define
another one.

