From the previous lab, you should be familiar with the concept of a function.

It is an abstraction that specifies operations on some arguments.

For instance, suppose we specify the function cube:

    
    (define (cube x)  
       (* x x x))

This takes in as argument the number x and returns x^3.

But this abstraction, `cube`, we can treat it like a box and throw it around,
just like any other thing, say a number or a symbol. It has a value and we can
give it a name.

On the whole, defining `cube` as above is not too much different from defining
`var` like so:

`(define var 10)`

![Cubes](https://dl.dropboxusercontent.com/u/16963685/cs61as-
edx/cube_diagram.png)

So, naturally, we can create functions that take functions as **arguments** or
**return** functions.

We will explore this idea in this lab.

