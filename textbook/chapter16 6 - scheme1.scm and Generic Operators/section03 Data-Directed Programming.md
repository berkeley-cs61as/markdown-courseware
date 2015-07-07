## What is Data-Directed-Programming?

Data-directed programming is a means to increase the flexibility of your code by modularizing data typing even further.
Instead of controlling information regarding data types and operators(procedures) inside functions using `cond` clauses, we record this information in a data structure that we can add to and retrieve from. You are given tools to do so: `put` to set up the data structure and `get` to examine it. Intuitively, we're simply adding entries into a table-like data structure.
    
        > (get 'foo 'baz)
        #f
        > (put 'foo 'baz 'hello)
        > (get 'foo 'baz)
        hello
    

In the code above, we try to retrieve the entry with keys `'foo` and `'baz`.
Because that entry does not exist (we haven't `put` it yet!), we get `#f`. The
next line places an entry into the table with keys `'foo` and `'baz`. In the
last line, we retrieve the information we just placed.

Once you put something in the table, it stays there. (This is our ﬁrst
departure from functional programming, we are allowing you to make an assignment. But our intent is to set up the table
at the beginning of the computation and then to treat it as constant
information, not as something that is mutable.) For now we take `put` and `get` as
primitives; we'll see how to build them in Unit 3.

To understand how all of this relates to data-directed programming, begin with
the observation that we have a few operations that we want to be able to apply
to a variety of types. Depending on the type(s) of the input data, we call a
different procedure to carry out the same basic operation. For example, adding
two rational numbers uses a different procedure than adding two complex
numbers. We are basically dealing with a two-dimensional table that contains
the possible operations on one axis and the possible types on the other axis.
Note that the possible types might actually be a list of types, if the
procedure requires more than one argument.

Using this paradigm, adding a new type to the system does not require changing
any existing procedures; we need only add new entries to the table.

## A New Example System

As the last section mentioned, the "keys" for our table must be a list of
types if we want to continue to use our arithmetic example. Instead of dealing
with this unnecessary complexity right now, we're going to switch to a
friendlier example that should be a little easier to follow. However, all of
the big ideas are exactly the same.

Our data types will be squares and circles; our operations will be area and
perimeter. For some comparison (and review) the tagged-data version of these
operations would be written:

    
    (define pi 3.141592654)
    
    ;;this is the tagged-data version where types are processed by the generic procedure being called
    (define (make-square side)
        (attach-tag 'square side))
    
    ;;this is the tagged-data version where types are processed by the generic procedure being called
    (define (make-circle radius)
        (attach-tag 'circle radius))
    
    ;;this is the tagged-data version where types are processed by the generic procedure being called
    (define (area shape)
        (cond ((eq? (type-tag shape) 'square)
               (* (contents shape) (contents shape)))
              ((eq? (type-tag shape) 'circle)
               (* pi (contents shape) (contents shape)))
              (else (error "Unknown shape -- AREA"))))
    
    ;;this is the tagged-data version where types are processed by the generic procedure being called
    (define (perimeter shape)
        (cond ((eq? (type-tag shape) 'square)
               (* 4 (contents shape)))
              ((eq? (type-tag shape) 'circle)
               (* 2 pi (contents shape)))
              (else (error "Unknown shape -- PERIMETER"))))
    

You should be able to completely understand the above code! We'll be using
this example with squares and circles throughout the rest of the lesson.

## "put"-ing it All Together

Using the data structure introduced at the top of the page, it is now possible for a system to handle any number of types
without having to change existing code! Here's what the new code would look
like (the constructors remain the same):

    ;;this is the data-directed version where types and operations 
    ;;are handled by a data structure that stores the information
    (put 'square 'area (lambda (s) (* s s)))
    (put 'circle 'area (lambda (r) (* pi r r)))
    (put 'square 'perimeter (lambda (s) (* 4 s)))
    (put 'circle 'perimeter (lambda (r) (* 2 pi r)))
    

Notice that the entry in each cell of the table is a function, not a symbol.
We can now redeﬁne the generic operators ("generic" because they work for any
of the types):

    ;;this is the data-directed version where types and operations 
    ;;are handled by a data structure that stores the information    
    (define (area shape-obj)
        (operate 'area shape-obj))
    
    (define (perimeter shape-obj)
        (operate 'perimeter shape-obj))
    
    (define (operate op obj)
        (let ((proc (get (type-tag obj) op)))
          (if proc
              (proc (contents obj))
              (error "Unknown operator for type"))))
    

The magic occurs in the `operate` procedure. Given an operation and some data,
it looks up the correct procedure to apply to that data. If there is an entry
(which means we know how to handle that operation), then we simply apply the
procedure. Otherwise, we throw an error.

## A Clarification on Data-Directed-Programming

Don't get the idea that Data-Directed-Programming just means a two-dimensional table of operator and
type names! DDP is a very general, great idea. It means putting the details of
a system into data, rather than into programs, so you can write general
programs instead of very speciﬁc ones.

In the old days, every time a company got a computer they had to hire a bunch
of programmers to write things like payroll programs for them. They couldn't
just use someone else's program because the details would be different, e.g.,
how many digits in the employee number. These days you have general business
packages and each company can "tune" the program to their speciﬁc purpose with
a data ﬁle.

Another example showing the generality of Data-Directed-Programming is the compiler. It used to be
that if you wanted to invent a new programming language you had to start from
scratch in writing a compiler for it. But now we have formal notations for
expressing the syntax of the language. (See section 7.1, page 38, of the
Scheme Report at the back of the course reader.) A single program can read
these formal descriptions and compile any language.

