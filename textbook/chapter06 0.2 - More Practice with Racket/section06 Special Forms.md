## The `if` Clause

Although we have done some exercises using `if` in the previous lesson, here is the general structure of the special form:

    (if [test]
        [then]
        [else])

`if` is a special form, since it will not evaluate its arguments unless it is used. Here are a few examples:

    -> (if #t
           'foo
           'baz)
    'foo
    -> (if #f
           'foo
           'baz)
    'baz
    -> (if (= 1 1)
           'foobar
           (/ 1 0))
    'foobar

The last example shows why `if` needs to be a special form. Since `(= 1 1)` evaluates to `#t`, we never reach the else case, `(/ 1 0)`, and successfully return `'foobar`.

## The `cond` Clause

It is possible to nest `if` expressions within itself, like this:

```
(define (roman-value letter)
  (if (equal? letter 'i)
      1
      (if (equal? letter 'v)
          5
          (if (equal? letter 'x)
              10
              (if (equal? letter 'l)
                  50
                  (if (equal? letter 'c)
                      100
                      (if (equal? letter 'd)
                          500
                          (if (equal? letter 'm)
                              1000
                              'huh?))))))))
```

This is useful for conditionals with many clauses. But, the more clauses, the messier and less readable your code becomes. A shorthand for nested `if`s is the `cond` clause, which uses different syntax to complete the same task. Here's the `roman-value` function written using a `cond` statement:

```
(define (roman-value letter)
  (cond ((equal? letter 'i) 1)
        ((equal? letter 'v) 5)
        ((equal? letter 'x) 10)
        ((equal? letter 'l) 50)
        ((equal? letter 'c) 100)
        ((equal? letter 'd) 500)
        ((equal? letter 'm) 1000)
        (else 'huh?)))
```

As you can see, the `cond` clause lets you specify a series of conditions and possible values. The `else` clause at the end specifies the value to return when none of the previous predicates are true.

Translated into English, the above code reads:

  * If the input letter is "i", the value is 1.
  * If the input letter is "v", the value is 5.
  * ...
  * If the input letter is "m", the value is 1000.
  * Otherwise, when none of the above are true, the value is `'huh?`.

The general structure of a `cond` clause is as follows:

    (cond ([test1] [then1])
          ([test2] [then2])
          ...
          ([testn] [thenn])
          (else [else]))

## Special Forms

Special forms are procedures that do not follow normal evaluation steps. We learned earlier that all arguments within an expression are evaluated _before_ the procedure is applied to its arguments. This is not true with special forms. Of the predicates and clauses we've gone over so far, `if`, `cond`, `or`, and `and` are all special forms.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
The following expressions currently error. Rearrange their arguments in a way that will cause the expressions to not error and return the correct value. Do not change any argument values.

<pre><code>(and (/ 1 0) #f #t)
(or #f (/ 1 0) #t)</code></pre>
</div>

Suppose we decided to write our own `if` procedure called `new-if` and defined it like so:

    (define (new-if test then else)
      (if test 
          then 
          else))

This should work exactly like `if`, since it's simply calling `if` in the body. But, **since this is a compound procedure, it is not a special form**. What happens when we call `new-if` like this?

    (new-if (= 1 1) 'foo (/ 1 0))

Since `new-if` is not a special form, it will evaluate all of its arguments first before entering the body.

  1. `(= 1 1)` returns `#t`
  2. `'foo` returns `'foo`
  3. `(/ 1 0)` returns-- wait a second...

And since `(/ 1 0)` errors, our `new-if` is a failed attempt to recreate the `if` special form.

## `if` is Composable

To save time and code space, keep in mind that functions like `if` and `cond` can be used within an expression, instead of being a stand-alone expression. To demonstrate this, consider the following simple function:

    (define (what-am-i age)
      (if (> age 21)
          '(i am a grownup)
          '(i am a child)))

Instead, we can rewrite it this way:

    (define (what-am-i age)
      (se '(i am a) (if (> age 21)
                        'grownup
                        'child)))

Admittedly, there doesn’t seem to be much of a difference. It’s understandable, considering this is a simple function. When this technique is used in more complex functions, we save time by avoiding repetition. We can see above how the rewritten function only writes `'(i am a)` once, while the original definition writes it twice.

## Pitfalls

The structure of a `cond` statement has very strict parenthetical rules. If you're code is erroring, it is very likely you missed a parenthesis or added an extra one. Thus, **_PAY ATTENTION TO PARENTHESES WHEN USING COND STATEMENTS!_**

Another issue is that `and` and `or` cannot be used as if they were in English. To clarify, suppose we have an expression that attempts to check whether an argument was either `'yes` or `'no`:

    (equal? argument (or 'yes 'no))`

This is WRONG. `or` returns the first argument that is not false, and thus will return `'yes` in this example. This expression ultimately is evaluated as:

    (equal? argument 'yes)

If you want to check if the argument is _either_ `'yes` or `'no`, you will need to do the following:

    (or (equal? argument 'yes) (equal? argument 'no))

Last, but definitely not least, it is essential to avoid redundant code. Simple code is smart code, and will make complex programs much more readable and maneuverable. 

Example of redundant code:

    (define (even? number)
      (if (not (odd? number))
          #t
          #f))

This is bad coding style. We can simplify this into just one line:

    (define (even? number)
      (not (odd? number)))

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
<strong>Note:</strong> This is Exercise 3 on your Homework.<br><br>

Write a procedure <code>indef-article</code> that takes in a word as its only argument and returns a sentence. See examples below for how <code>indef-article</code> should work. Remember that the indefinite article for anything that starts with a consonant is "a", and the indefinite article for anything that starts with a vowel is "an". You can ignore any edge cases.

<pre><code>-> (indef-article 'beetle)
'(a beetle)
-> (indef-article 'apple)
'(an apple)</code></pre>
</div>

