## Breaking Down Recursion

Let's see how recursion can magically find the factorial of any number. We've replicated the code below:

    
    (define (factorial n)
      (if (= n 0)
          1
          (* n (factorial (- n 1)))))

`factorial` returns `1` when `n` is `0`, otherwise it returns the product of `n`
and the factorial of `n - 1`.

Every recursive procedure uses conditionals, and will need two cases:

  * **Base case:** This case ends the recursion. Any input to a recursive procedure will eventually reach the base case.
  * **Recursive case:** This case reduces the size of the problem. The recursive case will always try to make the problem smaller until it reaches the base case.

There can be more than one base case or recursive case in a recursive procedure, but there must be at least one of each in order for any procedure to be correct and recursive.

There is one base case and one recursive case in our `factorial` procedure. Can you identify them?

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
The case in which `n` is `0` is the <i>base case</i> of <code>factorial</code>. Consider this alternate definition of <code>factorial</code>, which has no base case:

<pre><code>(define (factorial n)
  (* n (factorial (- n 1))))</code></pre>

What is wrong with this alternate definition?

<ans text="It no longer handles the special case of 0! being defined as 1." explanation=""></ans>
<ans text="It always returns 0." explanation=""></ans>
<ans text="It causes an error as soon as n reaches 0." explanation=""></ans>
<ans text="It loops indefinitely" explanation="Since this definition has no base case, factorial will never know when to stop!" correct></ans>
<br><br>
The second case in which we call <code>factorial</code> within itself is the <i>recursive case</i>. Notice that the recursive call solves a smaller problem (i.e., <code>(factorial (- n 1))</code>) than the one we were originally given. Consider this alternate definition of <code>factorial</code>:

<pre><code>(define (factorial n)
  (if (= n 0)
      1
      (factorial n)))</code></pre>

What's wrong with this alternate definition?

<ans text="It causes an error because you cannot define n! in terms of itself." explanation=""></ans>
<ans text="It always returns 1" explanation=""></ans>
<ans text="It keeps multiplying n by itself indefinitely." explanation=""></ans>
<ans text="It loops indefinitely without computing anything." explanation="" correct></ans>
<br><br>
Which of the following statements must hold for every recursive procedure you write? Choose all that apply.
<ans text="It has a base case." correct></ans>
<ans text="It makes exactly one recursive call."></ans>
<ans text="The recursive call solves a smaller problem." correct></ans>
<ans text="One of its arguments must be a number that tracks the stage of computation for the current recursive call."></ans>
</div>

## Leap of Faith

At this point, you may still be wondering how a function can be defined in terms of itself. If you use `factorial` in the middle of defining `factorial`, shouldn't you get an error saying that `factorial` isn't defined yet? In order to make it work, you have to believe that it works. This is, in a sense, a _leap of faith_.

The leap of faith is actually a technique for writing recursive procedures. We must imagine that the procedure you are writing already works for any problem smaller than the one you are currently tackling. Thus, while you are thinking about how to compute `(factorial 5)`, imagine that `(factorial 4)` has already been solved. This will keep your own thoughts from getting stuck in an infinite loop.

Back in Lesson 0-2, we stated an important property of defining procedures, where the procedure body is not evaluated when it is definted. This is the technical reason why recursion can work. Thus, `define` is a special form that does not evaluate its arguments and keeps the procedure body from being evaluated. The body is only evaluated when you call the procedure outside of the definition.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Which of these expressions cause an error in Racket? Select all that apply.

<ans text="(define (boom) (/ 1 0))" explanation=""></ans>
<ans text="(boom)" explanation="" correct></ans>
<ans text="(/ 1 0)" explanation="" correct></ans>
<ans text="(define boom (/ 1 0))" explanation="" correct></ans>
<br><br>
Enter each expression into the Racket interpreter and see what happens.
</div>

## `factorial` Revisited

Let's take a look at the definition of `factorial` again.

    (define (factorial n)
      (if (= n 0)
          1
          (* n (factorial (- n 1)))))

If we would like to evaluate `(factorial 6)`, then we reach the else case of the `if` statement and reduce the problem to `(* 6 (factorial 5))`. To simplify this further, we'll need to evaluate `(factorial 5)`. Thus, we get `(* 5 (factorial 4))`. If we substitute this into the original expression, we get `(* 6 (* 5 (factorial 4)))`. A few more recursive calls later, we'll get something like this:

    
    (factorial 6)
    (* 6 (factorial 5))
    (* 6 (* 5 (factorial 4)))
    (* 6 (* 5 (* 4 (factorial 3))))
    (* 6 (* 5 (* 4 (* 3 (factorial 2)))))
    (* 6 (* 5 (* 4 (* 3 (* 2 (factorial 1))))))
    (* 6 (* 5 (* 4 (* 3 (* 2 (* 1 (factorial 0)))))))

What should we do with `(factorial 0)`? This is the base case, and we should just return `1`. Thus, we get this expression:

    (* 6 (* 5 (* 4 (* 3 (* 2 (* 1 1))))))

This is simply a series of nested multiplication expressions, which we can simplify easily, from inside out: 

    (* 6 (* 5 (* 4 (* 3 (* 2 1)))))
    (* 6 (* 5 (* 4 (* 3 2))))
    (* 6 (* 5 (* 4 6)))
    (* 6 (* 5 24))
    (* 6 120)
    720
    

In Racket, there is a very useful procedure called `trace`, which takes a procedure as an argument and returns the process of the procedure when the procedure is invoked.

In your Racket interpreter, type `(trace factorial)` after defining the `factorial` procedure, then call `(factorial 6)`. What do you see? If you no longer want to trace the procedure, simply type `(untrace factorial)`.

## Example: Fibonacci Numbers

Consider computing the sequence of Fibonacci numbers, in which each number is
the sum of the preceding two: 

\begin{align} 0, 1, 1, 2, 3, 5, 8, 13, 21 \end{align}

In general, the Fibonacci numbers can be defined by the following rule:

\begin{align}
Fib(n) =
\begin{cases}
0, & \text{if n = 0}
\\\\
1, & \text{if n = 1}
\\\\
Fib(n - 1) + Fib(n - 2), & \text{otherwise}
\end{cases}
\end{align}

We can immediately translate this definition into a recursive procedure for computing Fibonacci numbers:

    
    (define (fib n)
      (cond ((= n 0) 0)
            ((= n 1) 1)
            (else (+ (fib (- n 1))
                     (fib (- n 2))))))

Consider what happens when we call `(fib 2)`. The procedure makes two recursive calls `(fib 1)` and `(fib 0)`, which return `1` and `0` respectively. These numbers are added together, and the procedure returns `1`.

You may be wondering if it's really necessary to have two separate base cases. Consider what would happen if we left out the base case for when `n` is `1`. `(fib 1)` would call `(+ (fib 0) (fib -1))`. `(fib 0)` would return `0`, but `(fib -1)` would never reach a base case, and the procedure would loop indefinitely.

## Example: Pig Latin

You may be familiar with Pig Latin, which is a language game where words in English are altered according to a simple set of rules: take the first consonant (or consonant cluster) of an English word and move it to the end of the word and append "ay" to the word. For example, "pig" yields "igpay", "trash" yields "ashtray", and "object" yields "objectay".

We can write Pig Latin in Racket using recursion and helper procedure:

    (define (pigl wd)
      (if (pl-done? wd)
          (word wd 'ay)
          (pigl (word (bf wd) (first wd)))))

    (define (pl-done? wd)
      (vowel? (first wd)))

    (define (vowel? letter)
      (member? letter '(a e i o u)))

As a reminder, `member?` is a Racket primitive procedure that takes two arguments, a letter and a word and returns true if the letter is in the word.

Pig Latin is done when a vowel is found, so the base case is when `pl-done?` returns true, and it just concatenates "ay" at the end of the word. Otherwise, in the recursive case, it calls itself with the concatenation of the `butfirst` of the word and the first of word.  Think about what happens if the word contains no vowels.

Use your Racket interpreter to try out this implementation of `pigl`. Don't forget to take advantage of the `trace` procedure!

## Example: `sum-sent`

Suppose we have a sentence of numbers, such as the one below: 

```
(define sent '(1 2 3 4 5))
```

We want to define a procedure called `sum-sent` that can find the sum of all the numbers in `sent`, but we also want `sum-sent` to be able to find the sum of _any_ sentence of numbers. Since the output depends on the size of the input sentence, we will have to use recursion!

Let's take the leap of faith. Imagine that `sum-sent` already knows how to calculate the sentence containing all but the first number, e.g, `'(2 3 4 5)`. To find this, we would simply call `(sum-sent (bf sent))`, and we should have faith that it will give us the correct sum. Given that, we know that: 

    (sum-sent '(1 2 3 4 5)) ==> (+ 1 (sum-sent '(2 3 4 5)))

If we generalize this for any sentence of numbers, this gives us our recursive case:

    (+ (first sent) (sum-sent (bf sent)))

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
What happens when we stop here and define <code>sum-sent</code> as follows?

<pre><code>(define (sum-sent sent)
  (+ (first sent) (sum-sent (bf sent))))</code></pre>

<ans text="It will work correctly, unless we call (sum-sent '()), where '() is the empty sentence." explanation=""></ans>
<ans text="It will always return the empty sentence." explanation=""></ans>
<ans text="It will cause an error as soon as it reaches the end of the sentence." explanation="" correct></ans>
<ans text="It will loop indefinitely" explanation=""></ans>
</div>

We're missing the base case! To solve this problem, we must add a case that will handle the empty sentence. The predicate `empty?` can be used to check for the empty sentence. Here is the completed version of `sum-sent`:

    
    (define (sum-sent sent)
      (if (empty? sent)
          0
          (+ (first sent) (sum-sent (bf sent)))))
<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Suppose we have a sentence of negative numbers, <code>'(-1 -3 -4 -6)</code>. What will Racket output? Run through this example using the code for <code>sum-sent</code> above without typing it into the interpeter. Then, use the interpreter to check your work.

<ans text="Click to reveal answer." explanation="-14" correct></ans>
</div>

Feel free to try out more examples with `sum-sent` in the Racket interpreter. If the recursion is confusing, try looking at what `trace` outputs.

## Exercises

<div class="mc">
<strong>Test Your Understanding: <code>count-ums</code></strong><br><br>

When you teach a class, people will get distracted if you say "um" too many times. Write a procedure called <code>count-ums</code> that takes in a sentence of words as its arguments and counts the number of times "um" appears in that sentence:

<pre><code>-> (count-ums '(today um we are going to um talk about the um combining method))
3</code></pre>

Write <code>count-ums</code> recursively.<br><br>
<strong>Hint #1:</strong> What should happen when the sentence is empty?<br>
<strong>Hint #2:</strong> What should happen when the first word of the sentence is "um"?<br>
<strong>Hint #3:</strong> What should happen when the first word of the sentence is NOT "um"?<br>
<br><br>

<strong>Test Your Understanding: <code>countdown</code></strong><br><br>

Write a procedure called <code>countdown</code> that takes in a number and works as follows:

<pre><code>-> (countdown 10)
'(10 9 8 7 6 5 4 3 2 1 blastoff!)
-> (countdown 3)
'(3 2 1 blastoff!)
-> (countdown 1)
'(1 blastoff!)
-> (countdown 0)
'blastoff!</code></pre>
</div>