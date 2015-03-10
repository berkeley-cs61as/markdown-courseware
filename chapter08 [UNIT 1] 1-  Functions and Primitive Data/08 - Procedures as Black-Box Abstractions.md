## Procedures as Abstractions

So far we have defined functions that does a single computation by itself
(like `square`, `fib,` and `factorial`). You can create a much more complex
function by combining different functions, each handling a subproblem of the
original problem. We will build on an example of such function in this section
and explore the idea of 'functions as
[abstractions](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/abstraction/)'.

## Extended Example: Largest Square

Charlie has a large amount of block (not bar) chocolates,  and he wants to
show it off to his friends by organizing those blocks in the largest possible
square arrangement! So let's say that Charlie has 13 blocks of chocolate. Then
the largest square arrangement is a 3x3 = 9 (shown left), with 4 leftovers
(shown right)

![](http://i.imgur.com/wo9ZcRW.png?1)![](http://www.haighschocolates.com.au
/wp-content/uploads/2013/06/block-chocolate_honeycomb-block-510x340.jpg)

Charlie wonders 'how big can the side of my square be given a certain amount
of chocolate blocks?' We can represent this question as a function, `(largest-
square total guess)`. The function `largest-square` takes two arguments,
`total` which represents how many chocolate blocks Charlie has (in the example
above 13) and `guess` which represents your initial guess on what's the
largest side you can have. This function will output the largest side your
chocolate square can have (in this case, 3). We will break this function into
subproblems, and put all the pieces together in the rest of this section.

## Largest Square: Overview

One thing that may seem odd is the redundant argument `guess`. You can write a
function that does the same thing with just the `total `argument. We included
`guess` to add an extra layer of complexity to the question. . Consider
`guess` to be Charlie's estimate on how large he thinks his side can be. In
our original example of 13 blocks of chocolate, suppose Charlie takes a `
guess ` that the maximum side is 2:

guessleftovernext guess

2

13-4= 9

2+1= 3

3

13-9= 4

3+1= 4

4

13-16= -3

4+1= 5

For each function call on ` largest-square ` like ` (largest-square 13 2) `,
we are going to check if the current guess (in this case 2) is good enough.
How do we check if our guess is good enough? It is good enough if our next
guess uses more chocolate blocks than we have available. If we can guess
better, then we use the next guess and call ` largest-square ` recursively.

## Largest Square: Skeleton Code

Given our intuition in the last page, we can formalize our function
definition. If your `guess` is good enough, return your `guess`. If you can
have a better `guess`, call `largest-square` with a better `guess`

    
     (define (largest-square total guess)
    	(if (good-enough? total guess)
    		guess
    		(largest-square total (next-guess guess))))
    

_"Wait wait, you just defined a function but it calls other functions that
aren't defined yet! We haven't defined 'good-enough?' or 'improve-guess'! "_

Yup, the definitions of the functions inside  are incomplete but notice that
we (the programmers) can **understand** what the function is doing! We have
broken down the problem of finding 'largest-square' into some small problems
like 'is it close enough?' and 'improve our guess'. We could've broken the
code in a different way, like in every 3 lines, every 5 lines but then each
subproblem will not have an _identifiable_ task. Breaking them to a coherent,
identifiable task is crucial.

This will be a key idea that we will visit again in the end, but first let's
finish the definition.

## Largest Squares: Subproblems

Time to do the neccessary work to make the function work!

    
     (define (largest-square total guess)
    	(if (good-enough? total guess)
    		guess
    		(largest-square total (next-guess guess))))
    

## Functions as Abstractions

What can we learn from the square chocolate example? Remember that when we
first _only _define ` largest-square `, we can understand what the procedure
is doing, without actually needing to know how `good-enough?` or `next-guess`
is implemented. We can consider these functions to be abstracted for us; we
know what it will output but we don't care ** how ** it is implemented. As
long as they do the right thing, we are happy!

You can also apply this in real life. When we turn on the TV, we never
consider "Oh the TV works because we shoot electron across the screen which
are guided by electromagnets which allows us to view stuff!". We usually think
more along the lines of "If I press this button, I can watch movies". We don't
need to know how the TV works to use it; Its implementation is abstracted away
for us

## Internal Definitions

We have defined a relatively complex procedure which depends on other
procedures. Now we will see if we can improve the organization of the code!

Notice that our definition of ` good-enough? ` and ` next-guess ` are very
specific to the `largest-square` problem; we can hardly find any other
functions that may use these functions. Also, when Charlie wants to find what
the largest square is, he will call the ` largest-square` function and not
touch the two helper functions directly. In such cases, it would be preffered
to organize it such that only ` largest-square` has access to those two helper
functions

How can we do that? We can define the functions inside the body of ` largest-
square ` as follows:

    
    
    (define (largest-square total guess)
    	(define (next-guess guess) (+ guess 1))
    	(define (good-enough? total guess)
    		(< total (square (next-guess guess))))
    	(if (good-enough? guess)
    		guess
    		(largest-square total (next-guess guess))))
    

## Scope of Variables

(define (largest-square total guess)

    
    	(define (next-guess guess) (+ guess 1))
    	(define (good-enough? total guess)
    		(< total (square (next-guess guess))))
    	(if (good-enough? guess)
    		guess
    		(largest-square total (next-guess guess))))
    

Previously we mentioned that the functions `good-enough?` and `next-guess` are
defined only inside the function `largest-square. ` Now that those functions
are inside `largest-square`, we can take other redundant parts out of the
function. Notice that `next-guess` and `good-enough?` accepts the same `total`
and `guess` that is passed in to larger-square. Removing the redunant
arguments in the two helper functions results in:

(define (largest-square total guess)

    
    	(define (next-guess) (+ guess 1))
    	(define (good-enough?)
    		(< total (square (next-guess))))
    	(if (good-enough?)
    		guess
    (largest-square total (next-guess))))  
      
    How do you keep track of what is available to a function and what is not? We will spend a lot of time on this in Unit 3. When a function defined inside another function, the one inside has access to variables and parameters of the outer function. Because next-guess is defined inside largest-square, next-guess has access to largest-square's parameters, total and guess.  
      
    

If you find a mnemonic helpful, consider the outer function as a parent and
the inner function as a baby. A parent may lend the baby their stuff (like a
handphone) but the baby won't let the parents to take away his toys

![](http://4.bp.blogspot.com/-yfy4u4_1Wb4/TxbQrWKytMI/AAAAAAAAIxs/Hi9b9LWDPGY/
s400/cute-baby-playing-handphone-448x336.jpg) ![](http://kidsbesttoys.net/wp-
content/images/lamaze-tug-and-play-knot-block-baby-toy-3.jpg)

