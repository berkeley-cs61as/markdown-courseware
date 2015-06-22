## Violating Data Abstraction

In the previous subsection, we talked about data abstraction -- the
methodology that enables us to isolate how a [compound data
object](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-1x
/compound-data/) is used from the details of how it is constructed from more
primitive data objects. What can be the case that violates the abstraction
then? Here's an example:

Here is a function that computes the total point score of a hand of playing
cards.

    
    (define (total hand)
      (if (empty? hand)
          0
          (+ (butlast (last hand))
             (total (butlast hand)) )))
    
    > (total '(3h 10c 4d))
    17

'butlast' is called in two places of the function. It is unclear on what each of these 'butlast' does in the function by simply reading the code. Compare the code with its modiﬁed version below:

    
    (define (total hand)
      (if (empty? hand)
          0
          (+ (rank (one-card hand))
             (total (remaining-cards hand)) )))
    
    (define rank butlast)
    
    (define suit last)
    
    (define one-card last)
    
    (define remaining-cards butlast)
    

While the code is much longer, it is more readable, meaning it is easier to understand what the code does by looking at just the code itself. Here, we know what each of the `butlast` does to function: one gets the rank of the card, and the other gets the remaining cards in the hand. If for
some reason we wanted to modify the program to add up the cards left to right
instead of right to left, editing the original version would be troublesome
because we wouldn't know which `butlast` to change. It would be easier to do so in the new version as we know which butlast does what. The auxiliary functions like `rank`
are called **selectors** because they select one component of a multi-part
datum.

Actually **we're violating the data abstraction** when we type in a hand of
cards as '(3h 10c 4d) because that assumes we know how the cards are
represented-- a card respresented as a word that has a rank number and a one-letter suit.

_So, how can I represent the cards without violating the data abstraction?_

We need a constructor.

## Constructors and Selectors

Constructors allow the user to "glue" data together into a [compound data
object](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki/cs61as-1x
/compound-data). Once an object has been created using a constructor, users can use selectors on the object to extract certain data from this abstract data type. A user is able to
use these constructors and selectors without any information about the
underlying implementation. Let's look at the following example for better understanding.

Here's a newly defined card representation using the constructors `make-card`
and `make-hand:`

    
    (define (make-card rank suit)
      (word rank (first suit)) )
    
    (define rank butlast)

    (define suit last)
    
    (define make-hand se)
    
    (define one-card last)
    
    (define remaining-cards butlast)  
    
    
    (define (total hand)
      (if (empty? hand)
          0
          (+ (rank (one-card hand))
             (total (remaining-cards hand)) )))
    
    > (total (make-hand (make-card 3 'heart) (make-card 10 'club) (make-card 4 'diamond) )) 
    > 17  
     

In the code above, we used data abstraction. As a result, we can change the implementation of the data type without affecting it behavior or the programs that use that data type. This means we can
change how our playing cards are represented, without letting the user know as the behavior is the same.

For example, we can represent a card as a number from 1 and 52, instead of a word comprised of the rank number and the one-letter suit. In the code below, we redefined the body of `make-card`, `rank`, and `suit` and kept `make-hand`, `one-card`, and `total` from the code above. Even with these changes, the code's functionalities remain the same and `total` is called the same way. 

    
    (define (make-card rank suit)
      (cond ((equal? suit 'heart) rank)
            ((equal? suit 'spade) (+ rank 13))
            ((equal? suit 'diamond) (+ rank 26))
            ((equal? suit 'club) (+ rank 39))
            (else (error "say what?")) ))
      
    (define (rank card)
      (remainder card 13))
      
    (define (suit card)
      (nth (quotient card 13) '(heart spade diamond club)))

Here's a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Test `total` with each of the two versions of card
representation:

## Pairs

To enable us to implement the concrete level of our data abstraction, our
language, Scheme, provides a compound structure called a pair, which can be constructed
with the primitive procedure `cons`. This procedure takes in two arguments and
returns a compound data object that contains the two arguments as two elements. These elements can be extracted from the pair using the primitive procedures `car` and
`cdr`. Thus, we can use `cons`, `car`, and `cdr` as follows:

    
    (define x (cons 1 2))
    
    (car x)
    1
    
    (cdr x)
    2
    
    x
    (1 . 2)
    

Notice that a pair is a data object that can be given a name and manipulated,
just like a primitive data object. The last example shows you how Scheme
prints pairs. Moreover, `cons` can be used to form pairs whose elements are also
pairs, and so on:

    
    (define x (cons 1 2))
    
    (define y (cons 3 4))
    
    (define z (cons x y))
    
    (car z)
    (1 . 2)

    (cdr z)
    (3 . 4)

    (car (car z))
    1
    
    (cdr (cdr z))
    4 
      
    ![](/static/pairs.jpg)
    
## What Will Scheme Output?
Tip: Draw the box and pointer diagrams

(define x (cons 4 5))
(define y (cons 'hello 'goodbye))
(define z (cons x y))

<div class="mc">
<pre><code>(car x)</code></pre>
<ans text="y" explanation="Try again"></ans>
<ans text="5" explanation="Try again"></ans>
<ans text="4" explanation="You got it!" correct></ans>
<ans text="(4 . 5)" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(cdr x)</code></pre>
<ans text="y" explanation="Try again"></ans>
<ans text="5" explanation="Wahoo!" correct></ans>
<ans text="4" explanation="Try again"></ans>
<ans text="(4 . 5)" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(car (cdr z))</code></pre>
<ans text="goodbye" explanation="Try again"></ans>
<ans text="4" explanation="Try again"></ans>
<ans text="(hello . goodbye)" explanation="Try again"></ans>
<ans text="hello" explanation="You got it!" correct></ans>
</div>
<div class="mc">
<pre><code>(cdr (cdr z))</code></pre>
<ans text="goodbye" explanation="You're amazing!" correct></ans>
<ans text="4" explanation="Try again"></ans>
<ans text="5" explanation="Try again"></ans>
<ans text="(hello . goodbye)" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(cdr (car z))</code></pre>
<ans text="goodbye" explanation="Try again"></ans>
<ans text="error" explanation="Try again"></ans>
<ans text="5" explanation="You're a genius!" correct></ans>
<ans text="(4 . 5)" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(car (cons 8 3))</code></pre>
<ans text="11" explanation="Try again"></ans>
<ans text="8" explanation="Good job!" correct></ans>
<ans text="3" explanation="Try again"></ans>
<ans text="5" explanation="Try again"></ans>
</div>
<div class="mc">
<pre><code>(car z)</code></pre>
<ans text="4" explanation="Try again"></ans>
<ans text="(5 . 4)" explanation="Try again"></ans>
<ans text="(hello . goodbye)" explanation="Try again"></ans>
<ans text="(4 . 5)" explanation="Correct!" correct></ans>
</div>
<div class="mc">
<pre><code>(car 3)</code></pre>
<ans text="0" explanation="Try again"></ans>
<ans text="(.)" explanation="Try again"></ans>
<ans text="3" explanation="Try again"></ans>
<ans text="error" explanation="You got it!" correct></ans>
</div>



Here's a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Play with pairs and make sure you're comfortable with
it:

## rational numbers revisited

Recall how we represented rational numbers in the introduction:

    
    (define (make-rational num den)
      (cons num den))
    
    (define (numerator rat)
      (car rat))
    
    (define (denominator rat)
      (cdr rat))
    
    (define (*rat a b)
      (make-rational (* (numerator a) (numerator b))
    		 (* (denominator a) (denominator b))))
    
    (define (print-rat rat)
      (word (numerator rat) '/ (denominator rat)))

Do the definitions make much more sense to you now?  This representation uses
a constructor `make-rational` and selectors `numerator` and `denominator`. We
can define additional procedures for arithmetic use only using constructor and
selectors:

    
    (define (add-rat x y)
      (make-rat (+ (* (numer x) (denom y))
                   (* (numer y) (denom x)))
                (* (denom x) (denom y))))
    
    (define (sub-rat x y)
      (make-rat (- (* (numer x) (denom y))
                   (* (numer y) (denom x)))
                (* (denom x) (denom y))))
    
    (define (mul-rat x y)
      (make-rat (* (numer x) (numer y))
                (* (denom x) (denom y))))
    
    (define (div-rat x y)
      (make-rat (* (numer x) (denom y))
                (* (denom x) (numer y))))
    
    (define (equal-rat? x y)
      (= (* (numer x) (denom y))
         (* (numer y) (denom x))))
    

In this case, even if the internal representation of rational numbers change,
we don't have to make any modification to the above procedures. We only need
to change our constructor and selectors. This is the best thing about data
abstraction.

## abtraction barriers

![](http://farm9.staticflickr.com/8505/8388536641_b8428f32fe_b.jpg)

Before continuing with more examples of compound data and data abstraction,
let us consider some of the issues raised by the rational-number example. We
defined the rational-number operations in terms of a constructor `make-rat`
and selectors `numer` and `denom`. In general, the underlying idea of data
abstraction is to identify for each type of data object a basic set of
operations (e.g. the constructors and selectors) in terms of which all
manipulations of data objects of that type will be expressed, and then to use
only those operations in manipulating the data.

We can envision the structure of the rational-number system as shown in the
figure below. The horizontal lines represent abstraction barriers that isolate
different "levels'' of the system. At each level, the barrier separates the
programs (above) that use the data abstraction from the programs (below) that
implement the data abstraction. Programs that use rational numbers manipulate
them solely in terms of the procedures supplied "for public use'' by the
rational-number package: `add-rat`, `sub-rat`, mul-rat, div-rat, and equal-
rat?. These, in turn, are implemented solely in terms of the constructor and
selectors `make-rat`, `numer`, and `denom`, which themselves are implemented
in terms of pairs. The details of how pairs are implemented are irrelevant to
the rest of the rational-number package so long as pairs can be manipulated by
the use of `cons`, `car`, and `cdr`. In effect, procedures at each level are
the interfaces that define the abstraction barriers and connect the different
levels.

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-6.gif)

This simple idea has many advantages. One advantage is that it makes programs
much easier to maintain and to modify. Any complex data structure can be
represented in a variety of ways with the primitive data structures provided
by a programming language.

To understand why this is so important, consider a world where data
abstraction didn't exist. Of course, the choice of representation influences
the programs that operate on it; thus, if the representation were to be
changed at some later time, all such programs might have to be modified
accordingly. This task could be time-consuming and expensive in the case of
large programs unless the dependence on the representation were to be confined
by design to a very few program modules.

Luckily, if the data was implemented without any violation of data
abstraction,  it would be very easy to modify the entire program -- **you only
need to modify constructors and selectors**.

## Further resources

If you'd like some more explanations, here's [SICP 2.1: Introduction to Data
Abstraction](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-14.html#%25_sec_2.1).

Or you can watch [Fall 2010 61A lecture video](http://www.youtube.com/watch?v=
1LZYB8Zs98A&feature=share&list=EC6D76F0C99A731667).

## exercises

Let's see how much you've got from this subsection!

## What's next?

In this subsection, you learned how to implement data using abstraction and
the importance of data abstraction. Now it's time to learn how to represent
sequences in Scheme!

