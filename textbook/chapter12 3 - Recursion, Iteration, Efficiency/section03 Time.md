## Measuring Time Efficency
In order to measure how fast programs runs, we have to devise a reasonable way to do so. Using a stopwatch to measure how much time it takes wouldn't work because the timings would change each time we had different programs running in the background, random fluctuations, solar flares, etc. Moreover, new computers are generally faster and old timings wouldn't be applicable.

A better way to approach this is to count the number of steps that a procedure takes. Focusing on the procedure allows us to avoid the problem of being tied down to any particular computer.

## Counting Steps
Here are some of the procedures we'll consider as taking "one step":

All of the following procedures take a single step.

- Basic arithmetic operations
- defining variables
- defining procedures
- conditionals?
- user-defined procedure calls

### Example: Counting Steps

```
(define (square x) (* x x)) ; takes a single step
(square 4) ; would take 2 steps (one for the procedure call, and one for the multiplication)
(square (+ 2 3)) ; 3 steps
```

However, the most interesting questions arise when we compare one procedure to another, and ask which one is faster.
In order to make this comparision, we must ask the following for each procedure:

> As we increase the size of the argument, how many steps will this procedure take to run?

In other words, if we were to graph the number of steps a procedure takes (with the input as the x-axis), what is the shape of that graph?

### Example: Function Runtime

- For `square`, we say this is a *constant* time procedure--`(square 2)` takes as many steps as `(square 2000)`. So as we increase the size of our input, the number of steps remains *constant*.
- For `last`, the procedure that finds you the last word of a sentence, we say this is a *linear* time procedure--as we call `last` on larger and larger inputs, the number of steps grows linearly.

In order to formalize this, we have to learn a mathematical construct called **Orders of Growth**.

## Orders of Growth
Orders of Growth describe the relationship between functions. Given two functions *f(n)* and *g(n)*, when we say *f = Θ(g)*, we mean that there exists two numbers, *a*, and *b* such that
*ag(n) ≤ f(n) ≤ bg(n)* for sufficiently large values of *n*.

## Examples

- When *f(n) = n* and *g(n) = 329n*, *f = Θ(g)*.
- When *f(n) = 4n²* and *g(n) = 2n²+n*, *f = Θ(g)*.
- When *f(n) = .0004n³* and *g(n) = 1000n²+30000n*, *f* IS NOT equal to *Θ(g)*.

Based on these examples, we have the following rules

- We can ignore constant factors in procedures
- We can ignore lower terms, e.g. in *2n²+n*, we only care about the *n²*.

Coming back to procedures, we can formally say that `square` is *Θ(1)*, and `last` is *Θ(n)*.

## Example: Exponentiation
Consider the straightforward way to compute `b^n` (`b` to the `n`th power): multiply `b` against itself `n` times. Here's the code for that.

```
(define (expt b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))
```

This runs in linear time with respect to the `n` variable. We know this because of two observations

- If `n` is 2, we make two recursive calls and if `n` is 10, then we make 10 recursive calls.
- In each recursive call, there is *Θ(1)* work being done.

Can we do better? Turns out there's a more clever exponentiation algorithm that takes advantage of the follow idea of *successive squaring*.
> Let's say we were trying to compute b^8. Normally, we would do b \* b \* b \* b \* b \* b \* b \* b. This requires 8 multiplcations. Instead we can do it in 3:
> ![The trick](https://mitpress.mit.edu/sicp/full-text/book/ch1-Z-G-22.gif)
> This method works fine for exponents that are powers of 2. We can also take advantage of successive squaring in computing exponentials in general if we use the rule
> ![The other trick](https://mitpress.mit.edu/sicp/full-text/book/ch1-Z-G-23.gif)

The above tricks give us this procedure:

```
(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(define (even? n)
  (= (remainder n 2) 0))
```

Squaring every even number allows us to cut down on the number of recursive calls. In fact, if you think about it, every other recursive call, we cut down `n` by half. This pattern of reducing the problem by half is means that the number of recursive calls taken is logarithmic with respect to `n`. Therefore, `fast-expt` *= Θ(log(n))*. (If this explanation doesn't make sense, check out 1.2.4. in the Further Reading)

## Exercises
Here are short, ungraded exercises for practice with finding the runtime of a function.

<div class="mc">
What is the runtime of bar?

```
define (bar n)
  (if (zero? (remainder n 7))
      'Bzzst
      (bar (- n 1)) ))
```

<ans text="Θ(1)" explanation="No matter what n is, bar will make at most 6 recursive calls" correct></ans>
<ans text="Θ(n)" explanation="Hint: Think carefully about the number of Recursive Calls made between (bar 48) vs (bar 83)."></ans>
<ans text="Θ(n^2)" explanation="Way off. Consider writing out an example where n = 7, n = 13, etc."></ans>
</div>

<div class="mc">
What is the runtime of sort?

```
(define (sort s)
  (if (empty? s)
      '()
      (insert (sort (bf s)) (first s)) ))

(define (insert sorted-sofar n)
  (if (empty? sorted-sofar)
      (se n)
      (if (< n (first sorted-sofar))
          (se n sorted-sofar)
          (se (first sorted-sofar) (insert (bf sorted-sofar) n)) )))
 
```

<ans text="Θ(1)" explanation="Way off."></ans>
<ans text="Θ(n)" explanation="Hint: start with finding the runtime of insert"></ans>
<ans text="Θ(n^2)" explanation="Yes, insert is in Θ(n), and sort uses insert n times, so Θ(n^2) is the total runtime" correct></ans>
</div>

## Further Reading

- [SICP 1.2.3 Orders of Growth](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_1.2.3)
- [SICP 1.2.4 Exponentiation](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_1.2.4)
