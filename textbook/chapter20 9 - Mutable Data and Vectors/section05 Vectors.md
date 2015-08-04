## Vectors

So far, we've programmed mostly in pairs, which we've used to make linked
lists. We used lists to represent **sequences**, an abstract data type. While
lists are great, they have one big disadvantage--referring to the nth element
of a list takes Θ(n) time because we have to `cdr` n times.

We want a way to be able to refer to the nth element of a sequence while
taking constant time. In Racket, [vectors](http://docs.racket-lang.org/reference/vectors.html) provide a mechanism of doing
this. If you've programmed in Java or other C-like languages, it's essentially
the same idea as an array.

Unfortunately, vectors have a drawback. In a linked list (which is essentially
the list structure you've been working with so far this semester),  adding to
the end of a list can be done Θ(1) time, since all we have to do is `cons` to
the start of a list. However, adding to a vector takes Θ(n) time, where n is the
length of the vector.

## How Vectors Work

How do vectors work? How can we access the elements of a vector in constant time?

When you create a vector, you must specify the size of the vector you would
like. Creating a vector of size n sets aside a chunk of memory n size long, so that
the elements of a vector are stored side by side in memory. Since we know the address 
in memory of the first item in the vector, we can add k to that address to get the kth 
element of the vector. This is how we can access any element in constant time!

The downside is that in order to get all the elements side by side in a single chunk of
memory, we have to allocate the chunk all at once. This is why adding an
element to a vector takes Θ(n) time -- we would have to allocate a new chunk
of memory (i.e. create a new array of size n+1) and copy all of the old elements over!

## vector primitives

**NOTE: Vectors index from 0.**

What this means is that the first element is referred to as the 0th element. That
means that in the vector  `#(1 2 3 4)`, 1 is at the 0th index, 2 is at the 1st
index, and so on.

Some of the vector primitives are analogous to the primitives for lists:

`(vector a b c d...)  (list a b c d...)`

`(vector-ref vec n)  (list-ref lst n)`

`(vector-length vec)  (length lst)`

But what about `cons` and `append`? Since adding an element to a vector takes
Θ(n) time, there are no primitives to add to the end of a vector. There are,
however, different constructors.

As discussed before, one of the main weaknesses of vectors is that we have to
declare how long the vector is going to be when we create it. Therefore, the
way to create an empty vector of length `len` is `(make-vector len)`. If you
want all the elements to be initially set to a certain value, you can instead
say `(make-vector len val)`.

So far, we can either create a vector with empty elements or a vector with all
the same elements. That's not very useful. So, how do we change the elements
of a vector? With mutation! Specifically, we use `(vector-set! vec n value)`
in order to set the nth element of a vector to a certain value. This is
similar to `set-car!` and `set-cdr!`

Note: There exist procedures `list->vector` and `vector->list` that convert
between the two types. However, in the lab and homework, you won't be
using these procedures since the whole point of this lesson is to learn vectors
:)

## Vector programming

When you're programming with vectors, you're usually going to use
[iteration](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/iteration/) to loop through a vector. Here are a few examples of
coding with vectors so that you can get your feet wet.

Here's the `map` function for lists:

    
    (define (map fn lst) 
        (if (null? lst) 
            '() 
            (cons (fn (car lst)) 
                  (map (cdr lst)))))
    

Now let's make the same function for vectors:

    
    (define (vector-map fn v) 
        (define (loop newvec i) 
            (if (< i 0) 
                newvec 
               (begin (vector-set! newvec i (fn (vector-ref v i))) 
                      (loop newvec (- i 1))))) 
        (loop (make-vector (vector-length v))
              (- (vector-length v) 1)))
    

It's a lot more complicated than `map` for lists! For one, our `vector-map` we
have an extra index variable `i` that keeps track of where we are in the
vector at all times. We also have to know the length of our vector, because
that is how our function knows when to stop.

`map` for lists was done with recursion, while `vector-map` is done with
iteration. At the beginning of the semester, we mentioned that recursion is
usually considered more elegant than iteration. Hopefully you now see why.

## For-loops
As we've just seen, using recursive iteration on vectors is cumbersome. In order
to make our lives easier, we can use [for-loops](http://docs.racket-lang.org/guide/for.html) 
with vectors. A for-loop automates an iterative process for us.

For-loops have the following general form:
 
    (for ([id sequence-expr] ...)
      body ...+)
  

Here, `id` is the name of a new variable, `sequence-expr` is some sequence (such as a list or a vector), and body is what we'd like
to be executed for every iteration. The `body` of the for-loop gets executed as many times as the length of the `sequence-expr` specifies.
For each iteration of the body, the `id` variable gets bound to the next element in the sequence. 

Let's clear all this up with an example. Consider the following for-loop:

 
    (for ([i '(1 2 3)])
      (display i))
       

The first time around, the variable `i` gets bound to the number 1. We then display the variable `i`, so 1 gets displayed. Since we've finished
executing the body,the for-loop goes on to the next iteration and binds `i` to 2, and then evaluates the body, so 2 gets displayed. The final iteration binds
`i` to 3, and displays 3. 

You can also have multiple variable ids in your forloops. Consider the following for-loop:


    (for ([i '(1 2 3)] [k '(4 5 6)])
      (display i)
      (display k))
       

The first iteration of the for-loop binds the variable `i` to 1 and `k` to 4, and then executes the body, displaying 1 and 4. The second iteration binds `i` to 2
and `k` to 5, and so on. Be careful if you use more than one id in your for-loops though; the for-loop will stop iterating after one of the sequences has been emptied.
For example, the following for-loop will never bind `k` to 7:

    (for ([i '(1 2 3)] [k '(4 5 6 7)])
      (display i)
      (display k)) 

In most cases, it's tedious to have to write out all of the values in our `sequence-expr`. This is why Racket has a procedure [in-range](http://docs.racket-lang.org/reference/sequences.html#%28def._%28%28lib._racket%2Fprivate%2Fbase..rkt%29._in-range%29%29), which returns a sequence of numbers in a specified range. Here are some examples of uses of `in-range`:

     -> (in-range 3)
      ;; returns a sequence of integers from 0 to 2 (does not include the 3)
      (0 1 2)
     -> (in-range 1 5)
      ;; returns a sequence of integers from 1 to 4 (does not include the 5)
      (1 2 3 4)
     -> (in-range 0 3 0.5)
      ;; returns a sequence of numbers from 0 to 3 separated by 0.5 (does not include the 3)
      (0 0.5 1 1.5 2 2.5)


To see how for-loops make dealing with vectors much easier, let's rewrite `map` using a for-loop:

    (define (vector-map fn v)
      (let ((newvec (make-vector (vector-length v))))
        (for ([i (in-range (vector-length v))])
          (vector-set! newvec i (fn (vector-ref v i))))
      newvec))
          

You can compare this code to our recursive code for vector-map and see how for-loops make our code much cleaner.

## vectors vs lists

Here are some comparisons between the running times for list and vector
procedures.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-e3zv{font-weight:bold}
</style>
<table class="tg">
  <tr>
    <th class="tg-e3zv">operation</th>
    <th class="tg-e3zv">list</th>
    <th class="tg-e3zv">vector</th>
  </tr>
  <tr>
    <td class="tg-031e">nth element</td>
    <td class="tg-031e">(list-ref lst n), Θ(n)</td>
    <td class="tg-031e">(vector-ref vec n), Θ(1)</td>
  </tr>
  <tr>
    <td class="tg-031e">adding an element</td>
    <td class="tg-031e">cons, Θ(1)</td>
    <td class="tg-031e">No primitive procedure, Θ(n)</td>
  </tr>
  <tr>
    <td class="tg-031e">length</td>
    <td class="tg-031e">(length lst), Θ(n)</td>
    <td class="tg-031e">(vector-length vec), Θ(1)</td>
  </tr>
</table>

There's no one best way to represent sequences--vectors and lists are good for
different things. If you're going to be adding and subtracting a lot of
elements from your sequence, it's best to use a list because `cons` runs in
constant time. On the other hand, if you're going to have a fixed number of
elements but are going to be changing a lot of them, vectors are better
because `vector-ref` runs in constant time.

## example: shuffling

Suppose we have a deck of cards, and we want to shuffle it. What would be the
best sequence to represent this?

First, let's use a list and use mutation to shuffle the deck destructively.

    
    (define (list-shuffle! lst) 
        (if (null? lst) 
            '() 
            (let ((index (random (length lst)))) 
              (let ((pair ((repeated cdr index) lst)) 
                    (temp (car lst))) 
                (set-car! lst (car pair)) 
                (set-car! pair temp) 
                (list-shuffle! (cdr lst)) 
                lst))))
    

This does what we want, but it's very slow--Θ(n2) time. In fact, any list-
based solution would take Θ( n2 ) time because it takes Θ(n) time to find a
random element, and we have to do that n times.

Let's try the same thing, but use a vector instead of a list.

    (define (vector-shuffle! vec)
      (for ([i (in-range (vector-length vec))])
        (let ((index (random (+ i 1)))
              (temp (vector-ref vec i)))
          (vector-set! vec i (vector-ref vec index))
          (vector-set! vec index temp))))
    

This is essentially the same algorithm, but performed on a vector instead of a
list. However, this takes Θ(n) time because it performs n constant time
operations since `vector-ref` is in constant time.

## Quiz Tips

Working with vectors might feel different at first, especially with all of the
new functions. We highly suggest to write notes in your cheat sheet on various
function primitives we used (e.g. make-vect, vector-ref, etc) as well as
helper procedures you are going to define in the HW exercises (e.g. vector-
append) and [these notes](http://www-
inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#61)(e.g. vector-map).

