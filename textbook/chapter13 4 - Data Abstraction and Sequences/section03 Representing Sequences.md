## Lists

One of the useful structures we can build with pairs is a sequence -- an
ordered collection of data objects. There are many ways to
represent sequences in terms of pairs. One particularly straightforward
representation is the **box-and-pointer diagram**, illustrated in the figure below, where the sequence 1, 2, 3, 4 is represented as a chain of pairs.

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-13.gif)

The `car` of each pair points to the corresponding item in the chain, and the `cdr`
of the pair points to the next pair in the chain. The `cdr` of the last pair, where the slash or diagonal line is, represents the value `nil` instead of a pointer. This signals
the end of the sequence. Note that `nil` is represented by a diagonal line in box-and-pointer diagrams. The entire sequence is constructed by nested `cons` operations:
    
    (cons 1
          (cons 2
                (cons 3
                      (cons 4 nil))))
    

Such a sequence of pairs, formed by nested `cons`es, is called a **list**, and
Scheme provides a primitive called `list` to help the construction of lists. The
above sequence could be reproduced by `(list 1 2 3 4)`.

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Construct various lists!:

## What Will Scheme Output?
<code>(define one-through-four (list 1 2 3 4))</code>
<div class="mc">
<pre><code>one-through-four</code></pre>
<ans text="" explanation="Try again"></ans>
<ans text="" explanation="Try again"></ans>
<ans text="(1 2 3 4)" explanation="Woohoo!" correct></ans>
<ans text="" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(car one-through-four)</code></pre>
<ans text="1" explanation="Correct!" correct></ans>
<ans text="(2 3 4)" explanation="Try again"></ans>
<ans text="3" explanation="Try again"></ans>
<ans text="4" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(cdr one-through-four)</code></pre>
<ans text="1" explanation="Try again"></ans>
<ans text="(2 3 4)" explanation="You got it!" correct></ans>
<ans text="(1 . 2)" explanation="Try again"></ans>
<ans text="4" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(car (cdr one-through-four))</code></pre>
<ans text="1" explanation="Try again"></ans>
<ans text="2" explanation="Fantastic!" correct></ans>
<ans text="3" explanation="Try again"></ans>
<ans text="4" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(cons 10 one-through-four)</code></pre>
<ans text="(10 . 1 2 3 4)" explanation="Try again"></ans>
<ans text="(1 2 3 4 10)" explanation="Try again"></ans>
<ans text="(10 2 3 4)" explanation="Try again"></ans>
<ans text="(10 1 2 3 4)" explanation="Great!" correct></ans>
</div>

## List Operations

Scheme provides useful primitive procedures for lists:

  * `list-ref` takes as arguments a list and a number n and returns the nth item of the list. The first elements of the list is indexed as 0. Here's how list-ref is defined and works: 
    <code>
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

## What Will Scheme Output?
<code>(define lst1 (list 'le 'petit 'prince))

(define lst2 (list 'the 'little 'prince)) </code>

<div class="mc">
<pre><code>(list-ref lst1 1)</code></pre>
<ans text="petit" explanation="Awesome!" correct></ans>
<ans text="error" explanation="Try again"></ans>
<ans text="little" explanation="Try again"></ans>
<ans text="prince" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(length lst2)</code></pre>
<ans text="6" explanation="Try again"></ans>
<ans text="2" explanation="Try again"></ans>
<ans text="3" explanation="Correct!" correct></ans>
<ans text="5" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(append lst1 lst2)</code></pre>
<ans text="(l p p t l p)" explanation="Try again"></ans>
<ans text="(le the petit little prince prince)" explanation="Try again"></ans>
<ans text="(the little prince le petit prince)" explanation="Try again"></ans>
<ans text="(le petit prince the little prince)" explanation="You got it!" correct></ans>
</div>
<div class="mc">
<pre><code>(list (list-ref lst1 0) (list-ref lst2 1) (list-ref lst1 2))</code></pre>
<ans text="(the le prince)" explanation="Try again"></ans>
<ans text="(le little prince)" explanation="Great!" correct></ans>
<ans text="(le petit prince)" explanation="Try again"></ans>
<ans text="(the petit prince)" explanation="Try again"></ans>
</div>

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Play with the list operations and make sure you're
comfortable with them:

## List, Cons, and Append

The three procedures `cons`, `list`, and `append` are confusingly similar.
Here is a picture from [CS Illustrated](http://csillustrated.berkeley.edu/) to
help you keep them straight. It is extremeley important for you to know how to draw the box-and-pointer diagram in relation to these three procedures:

![](https://studio.edge.edx.org/c4x/uc-berkeley/cs61as-1x/asset/list-
constructors-1-poster.jpg)

## Mapping Over Lists

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
here is called `map`. `map` takes as arguments a procedure of one argument and
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
    

`map` is an important construct, not only because it captures a common
pattern, but because it **establishes a higher level of abstraction** in
dealing with lists. In the original definition of `scale-list`, the recursive
structure of the program draws attention to the element-by-element processing
of the list. 

Defining `scale-list` in terms of map suppresses that level of
detail and emphasizes that scaling transforms a list of elements to a list of
results. **The difference between the two definitions is not that the computer
is performing a different process (it isn't) but that we think about the
process differently**. In effect, `map` helps establish an abstraction barrier
that isolates the implementation of procedures that transform lists from the
details of how the elements of the list are extracted and combined. This
abstraction gives us the flexibility to change the low-level details of how
sequences are implemented, while preserving the conceptual framework of
operations that transform sequences to sequences.

## Exercises
The procedure `cube-list` takes a list of numbers as argument and returns a list of the cubes of those numbers.
<code>(cube-list (list 1 2 3 4))
(1 8 27 64)</code>

Here are two different definitions of `cube-list`. Complete both of them by filling in the missing expressions:

<code>(define (cube-list items)
  (if (null? items)
      nil
      (cons ?? ??)))

(define (cube-list items)
  (map ?? ??))</code>

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type the above definitions and see if they work:

## Lists vs. Sentences

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

## What Will Scheme Output?
<code>(define x '(a (b c) d))</code>
<div class="mc">
<pre><code>(car x)</code></pre>
<ans text="a" explanation="You got it!" correct></ans>
<ans text="(b c)" explanation="Try again"></ans>
<ans text="b" explanation="Try again"></ans>
<ans text="d" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(cdr x)</code></pre>
<ans text="a" explanation="Try again"></ans>
<ans text="(b c)" explanation="Try again"></ans>
<ans text="d" explanation="Try again"></ans>
<ans text="((b c) d)" explanation="Awesome!" correct></ans>
</div>
<div class="mc">
<pre><code>(car (cdr x))</code></pre>
<ans text="a" explanation="Try again"></ans>
<ans text="(b c)" explanation="Fantastic!" correct></ans>
<ans text="error" explanation="Try again"></ans>
<ans text="b" explanation="Try again"></ans>
</div>

## Exercises
Define a procedure `reverse` that takes a list as argument and returns a list of the same elements in reverse order:

<code> (reverse (list 1 4 9 16 25))
(25 16 9 4 1)</code>

Your solution should `reverse` lists, not sentences! That is, you should be using `cons`, `car`, and `cdr`, not `first`, `sentence`, etc. For reference, here's how `reverse` is defined for sentences:

<code>(define (reverse sent)
  (if (empty? sent)
      ’()
      (se (reverse (bf sent)) (first sent)) )) </code>


## Box-and-Pointer Diagram

Here are a few details that people sometimes get wrong about box and pointer diagrams:

  1. An arrow can't point to a part of a pair. If an arrowhead is touching a pair, it's pointing to the entire pair, and it doesn't matter exactly where the arrowhead touches the rectangle. If you see something like `(define x (car y))` where `y` is a pair, the arrow for `x` should point to the thing that the `car` of `y` points to, not to the left half of the `y` rectangle.  
![](/static/b-p-d 1.jpg)

  2. The direction of arrows (up, down, left, right) is irrelevant. You can draw them however you want to make the arrangement of pairs neat. That's why it's crucial not to forget the arrowheads!
  
  3. There must be a top-level arrow to show where the structure you're representing begins. How do you draw a diagram for a complicated list? Take this example: 
`((a b) c (d (e f)))`

You begin by asking yourself how many elements the list has. In this case it
has three elements: ﬁrst `(a b)`, then `c`, then the rest. Therefore you
should draw a three-pair backbone: three pairs with the `cdr` of one pointing
to the next one. (The ﬁnal `cdr` is nil.)

![](/static/b-p-d 2.jpg)

Only after you've drawn the backbone should you worry about making the `car`s
of your three pairs point to the three elements of the top-level list.

## Box-and-Pointer Interpreter

Here's a [really helpful tool](http://xuanji.appspot.com/js-scheme-
stk/index.html) to learn box-and-pointer diagrams. It's a Scheme interpreter
that draws the correct diagram for you! Bookmark this link as it will be very helpful for you in understanding this lesson!

## Further Resources

If you'd like some more explanations, here's [SICP 2.2.1: Representing
Sequences](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-15.html#%25_sec_2.2.1).

Or, especially if you have trouble with box-and-pointer diagrams, you can
watch [Fall 2010 61A lecture video](http://www.youtube.com/watch?v=XZjQgDqpD4g
&feature=share&list=PL6D76F0C99A731667).

## Exercises
Let's see how much you've got from this subsection. **Make sure your procedure
doesn't violate data abstraction.**

1. Write a procedure `sum-list` which takes a list of numbers as an argument and returns the sum of the elements of the list. Make sure you're using list operations, not sentences.

<code>
  (sum-list '(1 2 3))
    > 6
    
    (sum-list '(0 -1 5))
    > 4 
    </code>

2. Write a procedure `car-list` which takes a list of lists as an argument and returns a new list that consists of the `car` of each list.

    (define lst (list (list 'hi 'hello) 
                      (list 'my 'cat) 
                      (list 'name 'tag)
                      (list 'is 'that) 
                      (list 'adam 'smith)))
    
    (car-list lst)
    > (hi my name is adam)
    

Here is a [Scheme Interpeter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Type the above definitions and see if they work:

## What's Next?

Go do Homework 3, and start looking at Project 2!

<div class="mc">
<pre><code></code></pre>
<ans text="" explanation="Try again"></ans>
<ans text="(b c)" explanation="You got it!" correct></ans>
<ans text="" explanation="Try again"></ans>
<ans text="" explanation="Try again"></ans>
</div>