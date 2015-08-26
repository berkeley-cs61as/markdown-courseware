## Template

Type the following command at the terminal to copy the template file to the
current directory (note the period at the end):

    
    cp ~cs61as/autograder/templates/hw3.rkt .

Or you can download the template
[here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw3.rkt).

## Autograder

If you are working on the lab computers, the `grader` command will run the autograder.  If you are working on your own personal machine, you should download [grader.rkt](http://inst.eecs.berkeley.edu/~cs61as/autograder/grader.rkt) and the [HW 3 tests](http://inst.eecs.berkeley.edu/~cs61as/autograder/tests/hw3-tests.rkt).

## Exercise 1: Invariant for Fast Exponentiation

<p>Here is the <code>fast-expt</code> procedure from earlier in this lesson:
<pre><code>(define (even? n)
  (= (remainder n 2) 0))

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))</code></pre></p>
  <p>Design a procedure that evolves an iterative exponentiation process that uses successive squaring and uses a logarithmic number of steps, as does <code>fast-expt</code>.</p>
  <p>(Hint: Using the observation that (<i>b</i><sup><i>n</i>/2</sup>)<sup>2</sup> = (<i>b</i><sup>2</sup>)<sup><i>n</i>/2</sup>, keep, along with the exponent <i>n</i> and the base <i>b</i>, an additional state variable <i>a</i>, and define the state transformation in such a way that the product <i>a b<sup>n</sup></i> is unchanged from state to state. At the beginning of the process <i>a</i> is taken to be 1, and the answer is given by the value of <i>a</i> at the end of the process. In general, the technique of defining an invariant quantity that remains unchanged from state to state is a powerful way to think about the design of iterative algorithms.)</p>

## Exercise 2: Golden Ratio (Optional)

<p>Read the subsection on <a href="http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_sec_Temp_106">finding fixed points of functions</a> in SICP, and do <a href="http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%25_thm_1.35">Exercise 1.35</a>.</p>

## Exercise 3: `cont-frac`

### Part 1

An infinite _continued_ fraction is an expression of the form:

<div> <!-- Prevent underscores from screwing up Markdown conversion -->
[mathjax]f=\frac{N_1}{D_1+\frac{N_2}{D_2+\frac{N_3}{D_3+\cdots}}}[/mathjax]
</div>

As an example, one can show that

<div> <!-- Prevent underscores from screwing up Markdown conversion -->
[mathjax]\frac{1}{\phi}=\frac{1}{1+\frac{1}{1+\frac{1}{1+\cdots}}}[/mathjax]
</div>

where [mathjaxinline]\phi=\frac{1+\sqrt{5}}{2}[/mathjaxinline] is the golden ratio.
One way to approximate an infinite continued fraction is to truncate the expansion after a
given number of terms. Such a truncation&mdash;a so-called <i>[mathjaxinline]k[/mathjaxinline]-term finite continued
fraction</i>&mdash;has the form:

<div> <!-- Prevent underscores from screwing up Markdown conversion -->
[mathjax]\frac{N_1}{D_1+\frac{N_2}{\ddots+\frac{N_k}{D_k}}}[/mathjax]
</div>

Suppose that <code>n</code> and <code>d</code> are procedures of one argument
(the term index [mathjaxinline]i[/mathjaxinline]) that return the
[mathjaxinline]N[/mathjaxinline] and [mathjaxinline]D[/mathjaxinline] of
the [mathjaxinline]i[/mathjaxinline]-th term of the continued fraction.
Define a procedure <code>cont-frac</code> such
that evaluating <code>(cont-frac n d k)</code> computes the value of the [mathjaxinline]k[/mathjaxinline]-term
finite continued fraction. Check your procedure by approximating [mathjaxinline]\frac{1}{\phi}[/mathjaxinline]
using

```
(cont-frac (lambda (i) 1.0)
           (lambda (i) 1.0)
           k)
```

for successive values of <code>k</code>. How large must you make <code>k</code> in order to get an approximation that is accurate to 4 decimal places?

### Part 2

If your `cont-frac` procedure generates a recursive process, write one that generates an iterative process.
If it generates an iterative process, write one that generates a recursive process.

### Part 3

In 1737, Swiss mathematician Leonhard Euler showed that

<div> <!-- Prevent underscores from screwing up Markdown conversion -->
[mathjax]
e - 2=\frac{N_1}{D_1+\frac{N_2}{D_2+\frac{N_3}{D_3+\cdots}}}
[/mathjax]
</div>

for the parameters

<div> <!-- Prevent underscores from screwing up Markdown conversion -->
[mathjax]
\begin{cases}
N_i = 1\\
D_i = 1,2,1,1,4,1,1,6,1,1,8,\cdots
\end{cases}
[/mathjax]
</div>

where [mathjaxinline]e[/mathjaxinline] is the base of natural logarithms.
Write a program that uses your `cont-frac` procedure to approximate [mathjaxinline]e[/mathjaxinline]
using Euler's expansion.

## Exercise 4: `next-perf`

<p>A <i>perfect number</i> is defined as a number equal to the sum of all its factors less than itself. For example, the first perfect number is 6, because its factors are 1, 2, 3, and 6, and 1+2+3=6. The second perfect number is 28, because 1+2+4+7+14=28. What is the third perfect number?</p>
<p>Write a procedure <code>(next-perf n)</code> that tests consecutive integers starting with <code>n</code> until a perfect number is found. Then you can evaluate <code>(next-perf 29)</code> to solve the problem.</p>
<p>Hint: you’ll need a <code>sum-of-factors</code> subprocedure.</p>
<p>Note: If you run this program when the system is heavily loaded, it may take half an hour to compute the answer! Try tracing helper procedures to make sure your program is on track, or start by computing <code>(next-perf 1)</code> and see if you get 6.</p>

## Exercise 5: Interchanging Base Cases

 <p>Here is the definition of <code>count-change</code> program from earlier in this lesson:
<pre><code>
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
</code></pre></p>
  <p>Explain the effect of interchanging the order in which the base cases in the <code>cc</code> procedure are checked.</p>
  <p>That is, describe completely the set of arguments for which the original <code>cc</code> procedure would return a different value or behave differently from a <code>cc</code> procedure coded as given below, and explain how the returned values would differ.
<pre><code>(define (cc amount kinds-of-coins)
  (cond
    [(or (&lt; amount 0) (empty? kinds-of-coins)) 0]
    [(= amount 0) 1]
    [else ... ] ) ) ; as in the original version</code></pre></p>

## Exercise 6: Invariant for Exponentiation

<p>Here is the iterative exponentiation procedure from earlier in this lesson:
<pre><code>(define (expt b n)
  (expt-iter b n 1))

(define (expt-iter b counter product)
  (if (= counter 0)
      product
      (expt-iter b
                (- counter 1)
                (* b product))))</code></pre></p>
  <p>Give an algebraic formula relating the values of the parameters <code>b</code>, <code>n</code>, <code>counter</code>, and <code>product</code> of the iterative exponentiation procedure defined above.</p>
  <p>(The kind of answer we're looking for is "the sum of <code>b</code>, <code>n</code>, and <code>counter</code> times <code>product</code> is always equal to 37.")</p>
   
## Submit Your Homework!

For instructions, see [this guide](../submit.html). It covers basic terminal commands and assignment submission.

If you have any trouble submitting, do not hesitate to ask a TA!
