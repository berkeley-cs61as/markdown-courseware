## Diving into orders of growth

We've just talked about recursive processes and iterative processes and how
iterative processes save memory (and sometimes time too). Now we can come back
to the beginning of this lesson when we introduced orders of growth and be
more precise about how the way procedures are written affect their run time
and memory usage.

## BIG-Θ NOTATIOn

Remember that orders of growth characterize the relative changes in resource
usage (time/memory) as input sizes change. The primary way we describe this
mathematically is with _big-Θ (pronounced "big theta") _notation. Our job as
TAs is to intimidate you, so here is the intimidating formal definition for
big-Θ notation:

> We say that \( f(n) \) has order of growth \( \Theta(g(n)) \) if there are
positive constants \( k_1 \) and \( k_2 \) such that \(k_1 g(n)\le f(n)\le k_2
g(n)\) for any sufficiently large value of \(n\).

## What the heck?

Let's try to make that less scary.

We're going to look at math functions for a second (just a second).

Say \( f(n) = n \) and \( g(n) = n^2 \).

[What does that look like on a
graph?](http://www.wolframalpha.com/input/?i=plot+n+and+n%5E2+from+0+to+3)

Notice that there's a section where \( n \) dominates \( n^2 \) (from 0 to 1),
but after that point \( n^2 \) is larger (all the way to infinity)!

So what if \( f(n) = 1000n + 1000 \) and \( g(n) = n^2 \)?

[We can graph that too.](http://www.wolframalpha.com/input/?i=plot+1000n+%2B+1
000+and+n%5E2+from+0+to+3000)

Notice that \( n^2 \) still dominates in the end. In fact, you can see that no
matter what constants I add to or multiply \( n \) or \( n^2 \) by, \( n^2 \)
will **always** dominate \( n \) in the long run. In big-Θ notation we don't
care about constants!

## What does this mean for scheme procedures?

We care about seeing what the behavior of the running time of the function is
(how long the function takes to run), as we increase the size of the argument.
So if we imagine a graph, the x-axis represents the size of our input, and the
y-axis is how long the function took to run at each x. As the size of the
input increases, the function's runtime does something on the graph. So when
we say something like "the runtime of foo is \( \Theta(n^2) \) where \( n \)
is the length of the list", we are saying that as we use bigger and bigger
lists the runtime increases **quadratically** - if we double \( n \) we
increase the runtime by a factor of 4. Note also that I said what \( n \) is!
**Always** give your units.

## What runs faster than what?

Sorted from fastest to slowest, this is by no means comprehensive:

\( \Theta(1) \)

\( \Theta(log(n)) \)

\( \Theta(n) \)

\( \Theta(nlog(n)) \)

\( \Theta(n^2) \)

\( \Theta(n^3) \)

\( \Theta(2^n) \)

(Anything past this point is kind of useless from a CS point of view)

\( \Theta(n!) \)

\( \Theta(n^n) \)

And of course, these also apply for memory usage as well.

So if we say a procedure runs in \( \Theta(n) \) time we expect it to be
significantly faster than a procedure that runs in \( \Theta(n^2) \) time for
large inputs.

## the real deal

So we know about Theta notation, now how do we actually assign runtimes to
real Scheme procedures? Let's see.

What you must understand is that there is no one method for finding the
runtime of a function. You **MUST** look at a function holistically or you
won't get the right answer. What does this mean? In order to get the correct
runtime, you first must understand what the function is doing! You can't
pattern-match your way to becoming good at this.

This cannot be stressed enough: **UNITS MATTER**. If you say \( \Theta(n^2)
\), you must tell us what \( n \) is.

General Tips:

0. UNDERSTAND WHAT THE FUNCTION IS DOING!!!

1. Try some sample input. That is, pretend you're the interpreter and execute
the code with some small inputs. What is the function doing with this input?
Having concrete examples lets you do tip 0 better. You can also graph how the
runtime increases as the argument size increases.

2. If applicable, draw a picture of the tree of function calls. This shows you
the "growth" of the function or how the function is getting "bigger", which
will help you do tip 0 better.

3. If applicable, draw a picture of how the input is being modified through
the function calls. For example, if your input is a list and your function
recursively does something to that list, draw out a list, then draw out parts
of the list underneath it that are called during the recursion. Helps with tip
0.

4. See tip 0.

## Recursive Processes

The following `reverse` function generates a recursive process:

    
            
              (define (reverse sent)
                (if (empty? sent)
                    '()
                    (se (last sent) (reverse (bl sent)))))
            
          

The running time for this function is \( 5N + 2 \) since it has five constant-
runtime operations: `if, empty?, se, last`, and `bl`. Thus the order of growth
of its running time is \( \Theta(n) \).

Now assume that we call `reverse` with an argument `'(Today was a fairytale)`.

The function call `(reverse '(Today was a fairytale))` will then generate the
following processes:

    
    
          (se fairytale (reverse '(Today was a)))
          (se a (reverse '(Today was)))
          (se was (reverse '(Today)))
          (se Today (reverse '()))
          (se Today '())
          (se was '(Today))
          (se a '(was Today))
          (se fairytale '(a was Today))
          '(fairytale a was Today)

One problem with this recursive process is that it takes too much memory.
Along the process, scheme has to keep track of the pending computations: In
order to accomplish `(se fairytale (reverse '(Today was a)))`, it has to
reserve some memory for the unfinished task `(reverse '(Today was a)).
`Similarly, memory has to be reserved for` (reverse '(Today was)), (reverse
'(Today)),` and `(reverse '())`. Therefore, this function is \( \Theta(n) \)
in memory.

## Iterative Process

Now let's consider another function that does the same thing in a different
way:

    
          (define (reverse-iter sent)
            (define (reverse-helper result se)
              (if (empty? se)
                  result
                  (reverse-helper (se result (last se)) (bl se))))
            (reverse-helper '() sent))

We can see that its runtime has the same order of growth as the recursive
reverse function.

If we call reverse-iter with `'(Today was a fairytale)`:

    
    
          (reverse-helper '() '(Today was a fairytale))
          (reverse-helper '(fairytale) '(Today was a))
          (reverse-helper '(fairytale a) '(Today was))
          (reverse-helper '(fairytale a was) '(Today))
          (reverse-helper '(fairytale a was Today) '())
          Returns '(fairytale a was Today)

Notice that both `reverse` functions use recursion. The difference is that, in
the first version, when the recursive procedure reaches the base case, it
doesn't finish all the work yet; in the second version, that particular
subproblem is solved when the recursive calls reach the base case. The first
function generates a recursive process, while the second one generates an
iterative process.

Another important point about this recursive process is that: since each
`reverse-helper` call does not have unfinished tasks, it takes constant memory
space.

In fact, iterative process always takes constant memory space because each
recursive call always contains **all the information necessary to complete the
computation**.

