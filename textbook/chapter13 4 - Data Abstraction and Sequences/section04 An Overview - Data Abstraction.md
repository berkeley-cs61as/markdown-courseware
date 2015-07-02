## What Is Data Abstraction?

Recall Lesson 1 - do you remember [Procedures as Black-Box Abstractions](http://berkeley-cs61as.github.io/textbook/procedures-as-black-box-abstractions.html)? You don't have to know how the procedures that are used as arguments for [higher order functions](http://berkeley-cs61as.github.io/textbook/hofs-procedures-as-arguments.html) were implemented, as long as they work! This allowed us to create generalized, "customizable" functions that made our code concise, readable, and _flexible_. 

The analogous notion for compound data is called **data abstraction**, and it is a methodology that enables us to isolate how a compound data object is used from the details of how it is constructed from more primitive data objects. In other words, you don't need to know how a car's engine works to drive the car.

The basic idea of data abstraction is to structure the programs that use compound data objects so that they operate on "abstract data." That is, our programs should use data in such a way that it does not make any assumptions on _how_ the data is stored or extracted. And so, the way data is represented is "concrete" and independent from the program that uses it. 

Programs and projects that professional programmers write are often accessible to the public, who _aren't_ all code savvy. If a tech company writes a cool program in Python, they won't expect their clients to know how they wrote their program, or even how to understand Python, in order to use their product. So how do these programmers let non-programmer people to use their creations? Abstraction. This is what programming is all about.

The interface between these two parts of our system will be a set of procedures, called **constructors** and **selectors**:

  * The **constructor** creates the object that stores our data.
  * The **selector(s)** extracts the data that you will use from the object created by the constructor.

The object that a constructor creates is called an **abstract data type (ADT)**.

## Example: Rational Numbers

To illustrate this technique, let's consider how to design an interface for manipulating rational numbers.

A rational number is any number that can be expressed as the quotient or the fraction (_p/q_) of two integers, where _q_ is non-zero. For example, 3/4 is a rational number with the denominator 4 and numerator 3, while π is an irrational number.

Although the Racket language already accommodates fractions in its dictionary, let's try to represent it by creating our own abstract data type. Before we jump into making our constructors and selectors, let's first look at the information we need. 

The minimal data needed for a complete representation of a rational number is the numerator and a denominator. So, we can arbitrarily pick any way to store these two numbers. Here we chose to store it in a _pair_:

    (define (make-rational numer denom)
      (if (= 0 denom)
          (error "Divisor cannot be 0!")
          (cons numer denom)))

That's it for our constructor! It's simply a procedure that, when called with the proper arguments, "creates" a rational number by storing it in a pair. Sure, `(3 . 4)` doesn't really _look_ like a fraction, but that's exactly what are selectors are here for. How can we _extract_ the numerator and denominator from our abstract data type? Take a look:

    (define (numerator rat)
      (car rat))

    (define (denominator rat)
      (cdr rat))

The first selector, `numerator`, takes in a rational number as its argument and returns its numerator by calling `car` on it. The second selector returns the denominator by calling `cdr` on it. And now, our abstract data type implementation is complete! We can make a rational number and extract its data like so:

    -> (define x (make-rational 3 4))
    x
    -> (numerator x)
    3
    -> (denominator x)
    4

Do you see how, in the calls above, there is nothing that reveals _how_ the rational number was represented? You've _abstracted_ away the method of representing your data and left a clean interface that almost anybody can use. 

The constructors and selectors of an abstract data type go hand in hand. The selectors for this rational numbers implementation will not work for a different implementation of rational numbers. We could have used lists, sentences, decimals, etc. The beauty of abstraction is that we _don't know_.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Consider the problem of representing line segments in a plane. Each segment is represented as a pair of points: a starting point and an ending point.<br><br>

Points are represented as a pair of coordinates:

<pre><code>(define (make-point x y) (cons x y))
(define (x-coord point) (car point))
(define (y-coord point) (cdr point))</code></pre>

Define a constructor called make-segment and selectors called start-segment and end-segment that define the representation of segments in terms of points. You may choose any method of storing the data you wish.
</div>

## Procedures using ADT

To build off of our rational numbers ADT, let's write some procedures that respect the abstraction of our implementation. One useful procedure is `print-rat`, which actually let's us see what a rational number "looks like" given its abstract representation.

    -> (define (print-rat rat)
        (word (numerator rat) '/ (denominator rat)))
    -> (define x (make-rational 3 4))
    x
    -> (print-rat x)
    3/4

This way we can pretend our rational number isn't actually a pair. :)

What's the use of rational numbers if we can't do mathematical operations on them? Here, we've defined some simple arithmetic procedures for our ADT:

    (define (add-rat rat1 rat2)
      (make-rational (+ (* (numerator rat1) (denominator rat2))
                        (* (numerator rat2) (denominator rat1)))
                     (* (denominator rat1) (denominator rat2))))

    (define (sub-rat rat1 rat2)
      (make-rational (- (* (numerator rat1) (denominator rat2))
                        (* (numerator rat2) (denominator rat1)))
                     (* (denominator rat1) (denominator rat2)))))
    
    (define (mul-rat rat1 rat2)
      (make-rational (* (numerator rat1) (numerator rat2))
                     (* (denominator rat1) (denominator rat2))))

    (define (div-rat rat1 rat2)
      (make-rational (* (numerator rat1) (denominator rat2))
                     (* (denominator rat1) (numerator rat2)))))

    (define (equal-rat? rat1 rat2)
      (= (* (numerator rat1) (denominator rat2))
         (* (numerator rat2) (denominator rat1))))

Notice how these procedures _respect_ the abstraction. Nowhere in our code do we call `cons` to create a rational, or `car`/`cdr` to select the numerator or denominator. Failing to do so is called a **data abstraction violation**, but we can talk about that in a later section. For now, let's move on to a bigger and better example!

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Using your implementation of line segments above, define a procedure called segment-length that takes in a line segment and returns its length.
</div>