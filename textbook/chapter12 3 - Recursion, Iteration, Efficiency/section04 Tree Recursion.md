## A New Class of Problems
There are some problems for which we haven't explicitly described a recursive pattern for yet.
Consider the following problem:

> I want to go up a flight of stairs that has `n` steps. I can either take 1 or 2 steps each time. How many different ways can I go up this flight of stairs?

For example, in the case where `n` is 5, there are 8 possible ways:

<code>
[1 1 1 1 1](../static/count-stairs/11111.png)<br>
[2   1 1 1](../static/count-stairs/2111.png)<br>
[1 2   1 1](../static/count-stairs/1211.png)<br>
[1 1 2   1](../static/count-stairs/1121.png)<br>
[1 1 1 2  ](../static/count-stairs/1112.png)<br>
[1 2   2  ](../static/count-stairs/122.png)<br>
[2   1 2  ](../static/count-stairs/212.png)<br>
[2   2   1](../static/count-stairs/221.png)
</code>

In order to solve this problem, we have to introduce a pattern called *Tree Recursion*. Tree Recursion is just a phrase to describe when you make a recursive call more than once in your recursive case. Why would we need to do this here? Consider one solution to the above problem:

```
(define (count-stairs n)
  (cond [(= n 1) 1]
        [(= n 2) 2]
        [else (+ (count-stairs (- n 1))
                 (count-stairs (- n 2)) ]) ))
```

Breaking the procedure down, there are three parts to consider

- There are two base cases, with two different outcomes.
  - If there is only one step to climb, there is only one way (by taking that step)
  - If there are two steps to climb, there is exactly two ways (1-step 1-step, or 2-step)
- Otherwise, the problem is made smaller by breaking it into two worlds
  - In the first world, we take one step, and thus the number of steps is reduced by one
  - In the second world, we take two steps, and thus the number of steps is reduced by two
- Making two recursive calls to those smaller problems gives us the answer to those smaller problems, and adding up those up gives us the answer to the original problem.

`count-stairs` is *tree recursive* because whenever it is called, its branch out and form an upside-down tree. For example, `(count-stairs 5)`:
![An upside down tree](../static/count-stairs/\(count-stairs 5\).png)

## Counting Change
Let consider a harder problem to solve:

> How many different ways can we make change of $1.00, given half-dollars, quarters, dimes, nickels, and pennies? More generally, can we write a function to compute the number of ways to change any given amount of money using any set of currency denominations?

We approach the problem in a similar fashion as above. By thinking carefully about the problem statement, we can notice that we have to keep track of a two things: what our amount currently is, and which coins we have to use (we can keep track of this in a sentence, e.g. `'(50 25 10 5 1)`). From there, we can observe a few things about our base cases:

- If the amount is exactly 0, we should count that as 1 way to make change
  - This may seem counter-intuitive, but there's exactly one way to make change for $0--use no coins.
- If the amount is less than 0, we should count that as 0 ways to make change.
  - You can't make change for negative amounts!
- If we run out of cois to use, we should count that as 0 ways to make change.
  - This will become more intuitive once we consider the recursive case.

For the recursive case, we again have to make two recursive calls. These two recursive calls break our problem into two worlds:

- In one world, we use the the largest coin (the `first` of `(50 25 10 5 1)`)
  - Why are the coins in that order? Because it's easy to reason about. The sentence could be in a different order, and while that will affect the computation, it will not affect the result.
- In the other world, we never use the largest coin again.
  - For example, if we never use the half dollar again, our new sentence should be `(25 10 5 1)`.

When we translate this into code, we get the following:

```
(define (count-change amount)
  (cc amount `(50 25 10 5 1)))

(define (cc amount kinds-of-coins)
  (cond [(= amount 0) 1]
        [(or (< amount 0) (empty? kinds-of-coins)) 0]
        [else (+ (cc amount
                     (bf kinds-of-coins))
                 (cc (- amount
                        (first kinds-of-coins))
                     kinds-of-coins))] ))
```


## Further Reading
[SICP 1.2.2 Tree Recursion](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_1.2.2)
[SICP 1.2.2 Example: Counting Change](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html#%_toc_%_sec_Temp_52)

