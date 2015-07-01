## Recursive Processes

To begin exploring how procedures use space, consider the following procedure:
```
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

If we were to evaluate (factorial 5) by hand, writing out each step we get the following:
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

Each line describes a new step of the computation--what we need to remember at that time step in order to continue the evaluation. Here is the key observation: if we chose a large enough input for factorial, say 10000, then at some step `(* 10000 (* 9999 (* 9998 (9997 ...))))`, we wouldn't be able fit the entire line in our minds explicitly (even though we can describe what the line should look like, we can't literally visualize all of those parens all at once).

In fact, this is how the computer must keep track of this as well. Each function call is stored in the computer's working memory—a place to store intermediary, incomplete computations. This space is finite and can be easily overflowed. The important thing to remember is that this problem only occurs on large inputs.


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

Test your understanding. Why must we say (> counter max-count)? What happens if we were to do (fact-iter 1 1 n)?
Now if we were to similarly diagram (factorial 5), we would get the following:
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

In this case, the amount of computation information we had to keep in our minds as we carried through the evaluation didn't grow over time. We instead carried it through the arguments, which grow more slowly when stored in the computer.

Note that this iterative process still uses Recursion, but this is different than saying it is a recursive process.

Description of an iterative process. Keeping extra state in order to make the procedure tail recursive. At any point in time, the arguments being carried can be used to compute the overall solution.

If we attempt (factorial 100000000), the code would now run without issue.
Comparing Iterative and Recursive Processes
<table>
<tr>
  <td>Recursive</td>
  <td>Iterative</td>
</tr>
<tr>
  <td>
````
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
</table>
More code. Not as easy to understand.

## Tail Recursion and Writing Tail Recursive Procedures
### Exercises
Factorial was rewritten to keep track of three things. What were those things? Could we rewrite factorial yet again in order to only keep track of two things?

Question: With these changes in mind, will a computer ever run out of space?
Yes. Consider the factorial example. Though the function calls no longer need to be stored in the computer's memory, the numbers themselves that are computed by the process will eventually exceed the computer's ability to store them. However, this takes much larger inputs to do this, and we won't worry about this event for now.

Note that crashy and less-crashy avoid this problem by not increasing the size of the argument past the ability to compute. However, they are silly examples since most real world procedures have arguments that change at each step.

## Further Reading
[SICP 1.2.1 - Linear Recursion and Iteration](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.1)
