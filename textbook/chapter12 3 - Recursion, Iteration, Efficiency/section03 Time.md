## Measuring Time Efficency



## Orders of Growth
Orders of Growth describe the relationship between functions. 

So for example,


## Examples of Time Efficient Programs

## Examples of Time Inefficent Programs

## Exercises

Here are some exercises that allow you to get practice with finding the runtime of a function. Most of these are designed to trick you..
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
## Further Reading
