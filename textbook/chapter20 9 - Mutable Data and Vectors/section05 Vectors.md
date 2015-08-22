## Vectors

So far, we've programmed mostly in pairs, which we've used to make linked lists. We used lists to represent **sequences**, an abstract data type. While lists are great, they have one big disadvantage - referring to the nth element of a list takes `Θ(n)` time because we have to call `cdr` `n` times.

We want a way to be able to refer to the nth element of a sequence while taking constant (`Θ(1)`) time. In Scheme, **vectors** provide a mechanism of doing this. If you've programmed in Java or other C-like languages, it's essentially the same idea as an array.

Unfortunately, vectors have a drawback. In a linked list (which is essentially the list structure you've been working with so far this semester),  adding to the end of a list can be done `Θ(1)` time, since all we have to do is `cons` to the end of a list. However, adding to a vector takes `Θ(n)` time, where `n` is the length of the vector.

## How Vectors Work

How do vectors work? What is the black magic that allows you to reference elements in constant time? Well, it turns out that it's not, in fact, black magic.

When you create a vector, you must specify the size of the vector you would like. Creating a vector of size n sets aside a chunk of memory n size long. Since we know the address of the first "block" of memory, we can add k to that address to get the kth element of the vector. This is how we can access any element in constant time!

The downside is that in order to get all the elements in a single chunk of memory, we have to allocate the chunk all at once. This is why adding an element to a vector takes `Θ(n)` time -- we would have to allocate a new chuck of memory (i.e. create a new array) and copy all of the old elements over!

## Vector Primitives

**NOTE: Vectors index from 0.**

By this we mean the first element is referred to as the 0th element. That means that in the vector  `#(1 2 3 4)`, 1 is at the 0th index, 2 is at the 1st index, and so on.

Some of the vector primitives are analogous to the primitives for lists:

<table class="table table-bordered table-striped">
<thead><tr>
    <th>Vectors</th>
    <th>Lists</th>
</tr></thead><tbody>
<tr>
    <td><code>(vector a b c d...)</code></td>
    <td><code>(list a b c d...)</code></td>
</tr>
<tr>
    <td><code>(vector-ref vec n)</code></td>
    <td><code>(list-ref lst n)</code></td>
</tr>
<tr>
    <td><code>(vector-length vec)</code></td>
    <td><code>(length lst)</code></td>
</tr>
</tbody>
</table>

But what about `cons` and `append`? Since adding an element to a vector takes `Θ(n)` time, there are no primitives to add to the end of a vector. There are, however, different constructers.

As discussed before, one of the main weaknesses of vectors is that we have to declare how long the vector is going to be when we create it. Therefore, the way to create an empty vector of length `len` is `(make-vector len)`. If you want all the elements to be initially set to a certain value, you can instead say `(make-vector len val)`.

So far, we can either create a vector with empty elements or a vector with all the same elements. That's not very useful. So, how do we change the elements of a vector? We do it with mutation! Specifically, we use `(vector-set! vec n value)` in order to set the nth element of a vector to a certain value. This is similar to `set-car!` and `set-cdr!`

**Note:** There exist procedures `list->vector` and `vector->list` that convert between the two types. However, in the lesson and homework, you will not be using these procedures since the purpose of this lesson is to learn vectors.

## Vector Programming

When you're programming with vectors, you're usually going to use [iterative processes](/textbook/space.html#sub1) to loop through a vector. Here are a few examples of coding with vectors so that you can get your feet wet.

Here's the `map` function for lists:

    
    (define (map fn lst) 
        (if (null? lst) 
            '() 
            (cons (fn (car lst)) 
                  (map (cdr lst)))))
    

Now let's make the same function for vectors, called `vector-map`:

    
    (define (vector-map fn v) 
        (define (loop newvec i) 
            (if (< i 0) 
                newvec 
               (begin (vector-set! newvec i (fn (vector-ref v i))) 
                      (loop newvec (- i 1))))) 
        (loop (make-vector (vector-length v))
              (- (vector-length v) 1)))
    

It's a lot more complicated than `map` for lists! For one, our `vector-map` has an extra index variable `i` that keeps track of where we are in the vector at all times. We also have to know the length of our vector, because that is how our function knows when to stop.

`map` for lists was done with recursion, while `vector-map` is done with iteration. At the beginning of the semester, we mentioned that recursion is usually considered more elegant than iteration. Hopefully you now see why.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>

Write a function <code>vector-addup</code> that takes in a vector of numbers and returns the sum of all the numbers. Test it out in the Racket interpreter to check your answer.
</div>

## Vectors vs. Lists

Here are some comparisons between the running times for list and vector procedures.

<table class="table table-bordered table-striped">
<thead><tr>
    <th>Operation</th>
    <th>Lists</th>
    <th>Vectors</th>
</tr></thead><tbody>
<tr>
    <td>Finding the nth element</td>
    <td><code>(list-ref lst n)</code><br>Runs in Θ(n)</td>
    <td><code>(vector-ref vec n)</code><br>Runs in Θ(1)</td>
</tr>
<tr>
    <td>Adding an element</td>
    <td><code>cons</code><br>Runs in Θ(1)</td>
    <td><code>N/A</code><br>Runs in Θ(n)</td>
</tr>
<tr>
    <td>Finding the length</td>
    <td><code>(length lst)</code><br>Runs in Θ(n)</td>
    <td><code>(vector-length vec)</code><br>Runs in Θ(1)</td>
</tr>
</tbody>
</table>

There's no one best way to represent sequences - vectors and lists are good for different things. If you're going to be adding and removing elements frequently from your sequence, it's best to use a list, since `cons` runs in constant time. On the other hand, if you're going to have a fixed number of elements but plan on changing a lot of them, vectors are better, since `vector-ref` runs in constant time.

## Example: Shuffling

Suppose we have a deck of cards and we want to shuffle it. What would be the best sequence to represent this?

First, let's use a list and use mutation to shuffle the deck.

    
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
    

This does what we want, but it's very slow - Θ(n<sup>2</sup>) time. In fact, any list-based solution would take Θ(n<sup>2</sup>) time, because it takes Θ(n) time to find a random element, and we have to do that n times.

Let's try the same thing, but use a vector instead of a list.

    
    (define (vector-shuffle! vec) 
        (define (loop n) 
            (if (= n 0) 
                vec 
                (let ((index (random n)) 
                      (temp (vector-ref vec (- n 1))))  
                  (vector-set! vec (- n 1) (vector-ref vec index)) 
                  (vector-set! vec index temp) 
                  (loop (- n 1)) 
        (loop (vector-length vec)))
    

This is essentially the same algorithm, but performed on a vector instead of a list. However, this takes Θ(n) time because it performs n constant time operations, since `vector-ref` is in constant time.

## Quiz Tips

Working with vectors might feel different at first, especially with all of the new functions. We highly suggest to write notes in your cheat sheet on various function primitives we used (e.g. `make-vect`, `vector-ref`, etc.) as well as helper procedures you are going to define in the homework exercises (e.g. `vector-append`) and [these notes](http://www-inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#61) (e.g., `vector-map`).

