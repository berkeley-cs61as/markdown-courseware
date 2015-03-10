## lists

One of the useful structures we can build with pairs is a sequence -- an
ordered collection of data objects. There are, of course, many ways to
represent sequences in terms of pairs. One particularly straightforward
representation is illustrated in figure below, where the sequence 1, 2, 3, 4
is represented as a chain of pairs.

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-13.gif)

The `car` of each pair is the corresponding item in the chain, and the `cdr`
of the pair is the next pair in the chain. The `cdr` of the final pair signals
the end of the sequence by pointing to a distinguished value that is not a
pair, represented in box-and-pointer diagrams as a diagonal line and in
programs as the value of the variable `nil`. The entire sequence is
constructed by nested `cons` operations:

    
    (cons 1
          (cons 2
                (cons 3
                      (cons 4 nil))))
    

Such a sequence of pairs, formed by nested `cons`es, is called a **list**, and
Scheme provides a primitive called `list` to help in constructing lists. The
above sequence could be produced by `(list 1 2 3 4)`.

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Construct various lists!:

## list operations

Scheme provides useful primitive procedures for lists:

  * `list-ref` takes as arguments a list and a number n and returns the nth item of the list. The first elements of the list is indexed as 0. Here's how list-ref is defined and works: 
    
    (define (list-ref items n)
      (if (= n 0)
          (car items)
          (list-ref (cdr items) (- n 1))))
    
    (define squares (list 1 4 9 16 25))
    
    (list-ref squares 3)
    16

  * `null?` takes a list as an argument and returns `#t` if the list is empty. Otherwise it returns `#f:`  

    
    (null? (list 1 3))
    #f
    
    (null? '())
    #t

  * `length` takes a list as an argument and returns the number of items in a list. Here's how `length` is defined and works: 
    
    (define (length items)
      (if (null? items)
          0
          (+ 1 (length (cdr items)))))
    
    (define odds (list 1 3 5 7))
    
    (length odds)
    4

  * `append` takes two(or more) lists as arguments and combines their elements to make a new list: 
    
    (define (append list1 list2)
      (if (null? list1)
          list2
          (cons (car list1) (append (cdr list1) list2))))
    
    (append squares odds)
    (1 4 9 16 25 1 3 5 7)
    
    (append odds squares)
    (1 3 5 7 1 4 9 16 25)
    
    (append odds squares evens)
    (1 3 5 7 1 4 9 16 25 2 4)

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Play with the list operations and make sure you're
comfortable with them:

## list, cons, and append

The three procedures `cons`, `list`, and `append` are confusingly similar.
Here is a picture from [CS Illustrated](http://csillustrated.berkeley.edu/) to
help you keep them straight:

![](https://studio.edge.edx.org/c4x/uc-berkeley/cs61as-1x/asset/list-
constructors-1-poster.jpg)

## mapping over lists

One extremely useful operation is to apply some transformation to each element
in a list and generate the list of results. For instance, the following
procedure scales each number in a list by a given factor:

    
    (define (scale-list items factor)
      (if (null? items)
          nil
          (cons (* (car items) factor)
                (scale-list (cdr items) factor))))
    
    (scale-list (list 1 2 3 4 5) 10)
    (10 20 30 40 50)
    

We can abstract this general idea and capture it as a common pattern expressed
as a higher-order procedure, just as in Unit 1. The higher-order procedure
here is called `map`. `Map` takes as arguments a procedure of one argument and
a list, and returns a list of the results produced by applying the procedure
to each element in the list:

    
    (define (map proc items)
      (if (null? items)
          nil
          (cons (proc (car items))
                (map proc (cdr items)))))
    
    (map abs (list -10 2.5 -11.6 17))
    (10 2.5 11.6 17)
    
    (map (lambda (x) (* x x))
         (list 1 2 3 4))
    (1 4 9 16)
    

Now we can give a new definition of scale-list in terms of map:

    
    (define (scale-list items factor)
      (map (lambda (x) (* x factor))
           items))
    

`Map` is an important construct, not only because it captures a common
pattern, but because it **establishes a higher level of abstraction** in
dealing with lists. In the original definition of `scale-list`, the recursive
structure of the program draws attention to the element-by-element processing
of the list. Defining `scale-list` in terms of map suppresses that level of
detail and emphasizes that scaling transforms a list of elements to a list of
results. **The difference between the two definitions is not that the computer
is performing a different process (it isn't) but that we think about the
process differently**. In effect, `map` helps establish an abstraction barrier
that isolates the implementation of procedures that transform lists from the
details of how the elements of the list are extracted and combined. This
abstraction gives us the flexibility to change the low-level details of how
sequences are implemented, while preserving the conceptual framework of
operations that transform sequences to sequences.

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type the above definitions and see if they work:

## lists vs. sentences

We started out the semester using an abstract data type called _sentence_ that
looks a lot like a list. What's the diﬀerence, and why did we do it that way?
Our goal was to allow you to create aggregates of words without having to
think about the structure of their internal representation (i.e., about
pairs). We do this by deciding that the elements of a sentence must be words
(not sublists), and enforcing that by giving you the constructor `sentence`
that creates only sentences.

To give you a better idea about what a sentence is, here's a version of the
constructor function:

    
    
    (define (se a b)
        (cond ((word? a) (se (list a) b))
              ((word? b) (se a (list b)))
              (else (append a b)) ))
    (define (word? x)
        (or (symbol? x) (number? x)) )
    

`se` is a lot like `append`, except that the latter behaves oddly if given
words as arguments. `se` can accept words or sentences as arguments.

## box and pointer diagram

Here are a few details that people sometimes get wrong about them:

  1. An arrow can't point to half of a pair. If an arrowhead touches a pair, it's pointing to the entire pair, and it doesn't matter exactly where the arrowhead touches the rectangle. If you see something like `(define x (car y))` where `y` is a pair, the arrow for `x` should point to the thing that the `car` of `y` points to, not to the left half of the `y` rectangle.  
![](/static/b-p-d 1.jpg)

  2. The direction of arrows (up, down, left, right) is irrelevant. You can draw them however you want to make the arrangement of pairs neat. That's why it's crucial not to forget the arrowheads!
  3. There must be a top-level arrow to show where the structure you're representing begins. How do you draw a diagram for a complicated list? Take this example:   
`((a b) c (d (e f)))`

You begin by asking yourself how many elements the list has. In this case it
has three elements: ﬁrst `(a b)`, then `c`, then the rest. Therefore you
should draw a three-pair backbone: three pairs with the `cdr` of one pointing
to the next one. (The ﬁnal `cdr` is null.)

![](/static/b-p-d 2.jpg)

Only after you've drawn the backbone should you worry about making the `car`s
of your three pairs point to the three elements of the top-level list.

## Box-and-Pointer Interpreter

Here's a [really helpful tool](http://xuanji.appspot.com/js-scheme-
stk/index.html) to learn box-and-pointer diagrams. It's a Scheme interpreter
that draws the correct diagram for you!

## further resources

If you'd like some more explanations, here's [SICP 2.2.1: Representing
Sequences](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-15.html#%25_sec_2.2.1).

Or, especially if you have trouble with box-and-pointer diagrams, you can
watch [Fall 2010 61A lecture video](http://www.youtube.com/watch?v=XZjQgDqpD4g
&feature=share&list=PL6D76F0C99A731667).

## exercises

Let's see how much you've got from this subsection. **Make sure your procedure
doesn't violate data abstraction.**

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type the above definitions and see if they work:

## what's next?

Go do Homework 3, and start looking at Project 2!

