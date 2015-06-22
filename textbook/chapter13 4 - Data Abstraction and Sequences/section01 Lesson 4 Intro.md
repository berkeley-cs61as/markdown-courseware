## Data Abstraction and Sequences

Now it's time to make things abstract.

## Prerequsites and What to Expect

For this lesson, you're expected to have understood all of Unit 1, especially
lessons 1 and 2.

In lesson 1, we noted that a procedure used as an element in creating a more
complex procedure could be regarded not only as a collection of particular
operations but also as a procedural abstraction. That is, the details of how
the procedure was implemented could be suppressed, and the particular
procedure itself could be replaced by any other procedure with the same
overall behavior. In this lesson, we are going to look at the abstraction on
the data side, and learn how to express sequences in Scheme.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 2 Intro](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-13.html)
  * [SICP 2.1](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%25_sec_2.1)
  * [SICP 2.2.1](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%25_sec_2.2.1)
  * [Lecture Notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=18) (ignore the part on MapReduce--this is different than map!)

## What Is Data Abstraction?

Recall Lesson 1. Do you remember [Procedures as Black-Box
Abstractions](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/coursewa
re/3883a0aeed634eacb512067d5a3801e3/20d0f2cd6cb245dd903891e6013979ff/)? You
don't have to know how the procedures that are used as arguments for [higher-
order procedures](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/higher-order-procedure/) were implemented, as long as they work!
The analogous notion for compound data is called data abstraction. Data
abstraction is a methodology that enables us to isolate how a compound data
object is used from the details of how it is constructed from more primitive
data objects.

The basic idea of data abstraction is to structure the programs that are to
use compound data objects so that they operate on "abstract data." That is,
our programs should use data in such a way as to make no assumptions about the
data that are not strictly necessary for performing the task at hand. At the
same time, a "concrete" data representation is defined independent of the
programs that use the data. The interface between these two parts of our
system will be a set of procedures, called selectors and constructors, that
implement the abstract data in terms of the concrete representation. To
illustrate this technique, we will consider how to design a set of procedures
for manipulating rational numbers.

## Example: Rational Numbers

A rational number is any number that can be expressed as the quotient or the
fraction (_p/q_) of two integers, with the denominator _q_ not equal to zero.
For example, 3/4 is a rational number with the denominator 4 and numerator 3.
How can we express rational numbers in Scheme?

Here's the definition of a rational number, defined as the procedure called make=rational. You don't have to know `cons`,
`car`, or `cdr` operators and how the procedures work yet. Just look at the code below and
play with it using the interpreter Scheme interpreter!

    
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

Here's a [Scheme interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-
scheme-stk/index.html). Define the procedures and play with it:

## What's Next?

Now that we've learned what data abstraction is, let's move on to learning how data abstraction works on rational
numbers.


## What Will Scheme Output? 
Tip: Try writing down on paper, line by line, each steps of what happens when a procedure is called. 

<div class="mc">
<pre><code>(print-rat (make-rational 2 3))</code></pre>
<ans text="(2 . 3)" explanation="Try again"></ans>
<ans text="2/3" explanation="You got it!" correct></ans>
<ans text="0.6666" explanation="Try again"></ans>
<ans text="6" explanation="Try again"></ans>
</div>

<div class="mc">
<pre><code>((print-rat (*rat (make-rational 2 3) (make-rational 1 4)))</code></pre>
<ans text="6/4" explanation="Try again"></ans>
<ans text="(6 . 4)" explanation="Try again"></ans>
<ans text="24" explanation="Try again"></ans>
<ans text="2/12" explanation="You got it!" correct></ans>
</div>






