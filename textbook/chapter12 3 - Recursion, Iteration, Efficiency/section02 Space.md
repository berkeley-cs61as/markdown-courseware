## Recursive Processes

To begin exploring how procedures use space, consider the following procedure:

```
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

If we were to evaluate `(factorial 5)` by hand, writing out each step we get the following:

```
start with  (factorial 5)
replaced by (* 5 (factorial 4))
replaced by (* 5 (* 4 (factorial 3)))
replaced by (* 5 (* 4 (* 3 (factorial 2))))
replaced by (* 5 (* 4 (* 3 (* 2 (factorial 1)))))
replaced by (* 5 (* 4 (* 3 (* 2 (* 1 (factorial 0))))))
replaced by (* 5 (* 4 (* 3 (* 2 (* 1 1)))))
replaced by (* 5 (* 4 (* 3 (* 2 1))))
replaced by (* 5 (* 4 (* 3 2)))
replaced by (* 5 (* 4 6))
replaced by (* 5 24)
replaced by 120
```

Each line describes a new step of the computation--what we need to remember at that time step in order to continue the evaluation. Here is the key observation: if we chose a large enough input for factorial, say 10000, then at some step, we wouldn't be able fit the entire line in our minds.

Computers evaluate procedure calls in the same way. Each function call is stored in the computer's working memory—a place to store intermediary, incomplete computations. This space is finite and can be overflowed. The important thing to remember is that this problem only occurs on very large inputs. The "working memory" is called the "call stack". When that space is used up by a program, it's called a "stack overflow".


## Iterative Processes
Is there a way to fix factorial such that it does not force the computer to run out of space on large inputs? Consider the following:

```
(define (factorial n)
  (fact-iter 1 1 n))

(define (fact-iter product counter max-count)
  (if (> counter max-count)
      product
      (fact-iter (* counter product)
                 (+ counter 1)
                 max-count)))
```

Test your understanding. Why must we say `(> counter max-count)`? What happens if we were to do `(fact-iter 1 1 3)`?
Now if we were to diagram `(factorial 5)` with the code above, we would get the following:

```
start with  (factorial 5)
replaced by (fact-iter 1 1 5)
replaced by (fact-iter 1 2 5)
replaced by (fact-iter 2 3 5)
replaced by (fact-iter 6 4 5)
replaced by (fact-iter 24 5 5)
replaced by (fact-iter 120 6 5)
replaced by 120
```

In this case, the amount of incomplete computations we had to keep in our minds as we carried through the evaluation didn't grow at each step. We instead carried the *incomplete answer to the computation* through the arguments, which saves space. In other words, the complete state of the computation is kept in the arguments to the recursive call--calling `(fact-iter 2 3 5)` would produce the same result as `(fact-iter 1 1 5)`, whereas calling `(factorial 3)` would produce a different result from calling `(factorial 5)`.

Note that this iterative process still uses Recursion, but this is different than saying it is a recursive process.

## Comparing Iterative and Recursive Processes
Looking at these functions side by side, we can identify how these two procedures relate.
<table>
  <thead>
    <tr>
      <th>Recursive</th>
      <th>Iterative</th>
    </tr>
  </thead>
  <tbody>
<tr>
  <td>

```
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

  </td>
  <td>

```
(define (factorial n)
  (fact-iter 1 1 n))

(define (fact-iter product counter 
                   max-count)
  (if (> counter max-count)
      product
      (fact-iter (* counter product)
                 (+ counter 1)
                 max-count)))
```

  </td>
</tr>
</tbody>
</table>

Important observations on the differences:

- The value that is returned as  base case in the Recursive version acts as the starting point for `product` in the iterative version (1). Notice that calling iterative `(factorial 1)`causes the base case to be triggered in `fact-iter`, and 1 is returned.
- In the Recursive version, The `*` procedure is called outside of the recursive call. In the iterative version, all of the arguments are transformed before (or inside of) the recursive call. I.e., `(* counter product)` happens first, and then the recursive call gets made. **This is the key to why the Iterative version is more space efficent.**
- As a corollary, this means the recursive call is the "last" expression that is evaluated in a procedure call (as opposed to a multiplcation.)
- Because the Iterative version needed to keep track of more arguments, it needed a helper procedure where the recursion actually took place. This is often the case for Iterative procedures.

## Tail Recursion and Writing Tail Recursive Procedures
In formal terms, the Iterative `factorial` is more space efficent because the Racket interpreter impliements [Tail Call Elimination](https://en.wikipedia.org/wiki/Tail_call). In other programming languages and other interpreters that aren't Tail Call optimized, the Recursive and Iterative versions use the same amount of space when run. So why do we care?

- Introducing these topics gives us a deeper understanding of recursion, evaluation, and programming languages, which provides a solid background for other topics
- This is a chance to practice thinking critically about resource usage and tradeoffs, which is generally important to Software Engineering and Computer Science.

In order to write a *tail-recursive* procedure, here are a few tips.

- Figure out if you'll need to keep extra arguments in order to keep track of the state of the computation, and whether or not a helper procedure is necessary. Almost always, you'll need some sort of argument to keep track of the "answer so far". In `factorial`, that was `product`.
- In fact as a general rule, the Recursive version of procedures will try to make its arguments progressively smaller, whereas the Iterative version builds up a result. Thus when writing an iterative procedure, think of the starting values needed in order to "build" your answer. In `factorial`, that was 1, 1, and `n`, in `(fact-iter 1 1 n)`.
- Ensure that the recursive call happens "at the last moment". In practice, this means that the arguments are processed (added, subtrated, multiplied, `butfirst`'d, etc.) before the recursive call is made.

## Exercises
The following questions are for your understanding. You will not be graded. You can check your answers with a staff member.

- Iterative `factorial` keeps track of three things in `fact-iter`. What were those things? Could we rewrite `factorial` yet again in order to only keep track of two things?
- If we use an iterative version, will we ever run out of space calling `factorial`?

## Further Reading
[SICP 1.2.1 - Linear Recursion and Iteration](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.1)
