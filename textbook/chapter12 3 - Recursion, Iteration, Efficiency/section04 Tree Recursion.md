## A New Class of Problems
There are some problems for which we haven't explicitly described a recursive pattern for yet.
Consider the following problem:

> I want to go up a flight of stairs that has `n` steps. I can either take 1 or 2 steps each time. How many different ways can I go up this flight of stairs?

For example, consider the case where `n` is 5. Then there are 8 possible ways:

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

What


`count-stairs` is *tree recursive* because whenever it is called, its branch out and form an upside-down tree. For example, `(count-stairs 5)`:
![An upside down tree](../static/count-stairs/\(count-stairs 5\).png)

## Counting Change
Let consider a harder problem to solve:

> How many different ways can we make change of $1.00, given half-dollars, quarters, dimes, nickels, and pennies? More generally, can we write a function to compute the number of ways to change any given amount of money using any set of currency denominations?

Let's consider 


<!-- TODO: Use a sentence to represent denominations instead? -->

```
(define (count-change amount)
  (cc amount 5))
(define (cc amount kinds-of-coins)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (= kinds-of-coins 0)) 0)
        (else (+ (cc amount
                     (- kinds-of-coins 1))
                 (cc (- amount
                        (first-denomination kinds-of-coins))
                     kinds-of-coins)))))
(define (first-denomination kinds-of-coins)
  (cond ((= kinds-of-coins 1) 1)
        ((= kinds-of-coins 2) 5)
        ((= kinds-of-coins 3) 10)
        ((= kinds-of-coins 4) 25)
        ((= kinds-of-coins 5) 50)))
```
