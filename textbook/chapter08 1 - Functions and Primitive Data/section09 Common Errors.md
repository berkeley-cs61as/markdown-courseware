## Try it out yourself!

Type the following into the Racket interpreter. Most of them will generate
errors. Read the error messages and try to figure out what they mean. You don't
have to turn in anything for this section.

```
=> (require berkeley) ;this should not error out. if it does, ask a TA for help
=> (bar 9)
=> (first '())
=> (bf '())
=> (first (bf '(1)))
=> (define (foo x) (+ x 1))) ;notice the extra parenthesis at the end
=> (foo 2 4)
=> (foo)
=> (define baz 3)
=> (baz 8)
=> (se garbly 4)
=> (se 'garbly 4)
=> (se baz 4)
```

You should also take a look at the [list of common errors](https://docs.google.com/document/d/1jGtldEcm_qPoHGknJOkWj1D4-doyBjDivaV_Vn7_Hxk)
