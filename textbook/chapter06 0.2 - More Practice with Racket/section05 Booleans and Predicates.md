## Booleans: True and False

**Booleans** are formally defined as a binary variable that has only two possible values: "true" and "false". These are extremely useful when expressing _conditionals_, or instructions for choosing an action based on the results of a test. A logical example of this would be: If we're out of milk, then go to the store. Else, add milk to our cereal and enjoy.

In order to test whether or not we are out of milk, we'll need to use booleans. Racket's "true" is represented by `#t` or `true`, while "false" is represented by `#f` or `false`.
    
    -> (= 1 1)
    #t
    
    -> (= 1 2)
    #f
    
    > (if #t
        '(the condition was true)
        '(the condition was false))
    (the condition was true)
    
    > (if #f
        '(the condition was true)
        '(the condition was false))
    (the condition was false)
    
    > (if (= 1 1)
        '(the condition was true)
        '(the condition was false))
    (the condition was true)
    

## Predicates

A function that, when called, returns either `true` or `false` is called a **predicate**. For example, `even?` is a predicate used to test whether a number is even. 

    -> (even? 2)
    #t
    -> (even? 3)
    #f

Predicates will NEVER return a value other than `#t` or `#f`. Below is a list of some useful predefined predicates in Racket. This list is in no way comprehensive, and you will definitely discover many more predicates in future lesson.

### Mathematical Operators

Racket has the standard mathematical operators that you will need to compare numerical values:

  * `<` will return `#t` if the first argument is less than the second.
  * `>` will return `#t` if the first argument is greater than the second.
  * `=` will return `#t` if the two arguments are equal.
  * `<=` will return `#t` if the first argument is less than or equal to the second.
  * `>=` will return `#t` if the first argument is greater than or equal to the second.

**WARNING:** These predicates will only work on **numbers**. Using these to compare words, sentences, or any other type of value will produce errors.

```
-> (= (+ 3 3) 6)
#t
-> (= 'foo 'foo)
; =: contract violation
;   expected: number?
;   given: 'foo
;   argument position: 1st
; [,bt for context]
```

### `member?`

`member?`, when given a letter and a word, returns `#t` if the word contains the letter, and `#f` otherwise. When `member?` is given a word and a sentence, it returns `#t` if the sentence contains the word, and `#f` otherwise.

    -> (member? 'a 'aeiou)
    #t
    -> (member? 'b 'aeiou)
    #f

    -> (member? 'foo '(foo bar baz))
    #t
    -> (member? 'foobar '(foo bar baz))
    #f

### `empty?`

The predicate `empty?` takes in one argument of any type and returns `#t` if the argument is the empty word `""` or the empty sentence `'()`, and `#f` otherwise.

    -> (empty? "")
    #t
    -> (empty? 'foo)
    #f

    -> (empty? '())
    #t
    -> (empty? '(foo bar baz))
    #f

    -> (empty? 3)
    #f

### `equal?`

`equal?` takes in two arguments of any type and returns `#t` if they are the same, and `#f` otherwise.

    -> (equal? (+ 1 1) 2)
    #t
    -> (equal? 3 1)
    #f

    -> (equal? 'foo 'foo)
    #t
    -> (equal? '(foo bar baz) '(foo bar baz))
    #t

    -> (equal? + +)
    #t

### Type Checkers

Racket also provides predicates that check whether a value is of a particular type:

  * `number?` checks if a value is a number.
  * `word?` checks if a value is a word.
  * `sentence?` checks if a value is a sentence.
  * `boolean?` checks if a value is a boolean.

### Compound Procedures as Predicates

You can most definitely create your own predicates, since they are in fact procedures. For example:

```
(define (vowel? letter)
  (member? letter 'aeiou))
```

`vowel?` checks whether its argument letter is a vowel.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
<strong>Note:</strong> This is Exercise 2 on your Homework.<br><br>

Write a predicate called <code>teen?</code> that takes in a number as its argument and returns <code>#t</code> if the number is between 13 and 19, inclusive.
</div>

## Everything That Isn't False is True

When evaluating whether or not an expression is true or false, it is important to remember that anything is considered true unless it is false. This means that all numbers, words, sentences, and procedures are true, even `""`, `'()`, and `0`. Here are some counter-intuitive examples to consider:

    -> (false? "") ;; is "" false?
    #f ;; no, it is not
    -> (false? '())
    #f
    -> (false? 0)
    #f
    -> (false? false?) ;; is the procedure false? false?
    #f ;; no, the procedure itself is not false

## Logical Operators

We can also use logical operations in Racket.

### `and`

`and` is a predicate that any number of arguments of any type. It returns the last element if everything was not false, and returns `#f` otherwise. For example:

    -> (and 1 2 3)
    3
    -> (and (= 1 1) (member? 'a 'aeiou))
    #t
    -> (and (number? 'hi) 2 3)
    #f

### `or`

`or` is a predicate that takes any number of arguments of any type. It and returns the first true element, and returns `#f` otherwise. For example:

    -> (or (even? 4) (= 1 1))
    #t
    -> (or 1 #f 2)
    1
    -> (or (even? 1) #f (number? 'foo))
    #f

### `not`

`not` takes a single argument of any type simply negates the argument that it takes in. For example:

    -> (not #f)
    #t
    -> (not #t)
    #f
    -> (not 3)
    #f
    -> (not (and (and 3 3) (or #f #f)))
    #t

### `nand`

`nand` is equivalent to `(not (and ...`. For example:

    -> (nand #f #t)
    ...(not (and #f #t))
    ...(not #f)
    #t

### `nor`

`nor` is, you guessed it, equivalent to `(not (or ...`. For example:

    -> (nor #f #t)
    ...(not (or #f #t))
    ...(not #t)
    #f

### `xor`

`xor` takes two arguments of any type and, if exactly one (no more or less) of its arguments is not `#f`, return that argument. Otherwise, return `#f`.

    -> (xor 11 #f)
    11
    -> (xor #f 11)
    11
    -> (xor 11 22)
    #f
    -> (xor #f #f)
    #f