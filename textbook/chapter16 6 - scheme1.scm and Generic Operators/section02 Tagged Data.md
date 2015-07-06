## The Big Idea

The first problem we're going to tackle is keeping track of data types.

Think back to Lesson 4 where we implemented rational numbers. We made the decision 
to store rational numbers as a pair, where the `car` held the numerator and 
the `cdr` held the denominator. Meanwhile, our frenemy, Ben Bitdiddle, implemented 
complex numbers. He represented these numbers as a pair as well: the `car` held the real part
and the `cdr` held the imaginary part.

![](/static/pair_3.4.PNG)

Now, given a pair whose `car` is 3 and whose `cdr` is 4, how can we tell if the given data
represents the rational number 3/4 or the complex number 3+4i? 
Because the raw data we are given can be interpreted either way, we can't know for sure! 
In fact, the pair may be neither of the two and actually represent some other data type.
That's why need a system to associate data with its particular type.

(Sidenote: Okay, at this point you might be mad at Ben--why did he have to use
the same representation as us! However, he really isn't to blame. Even if he
uses a different internal representation, we **cannot** use this distinction
to check the type of the data: this would break data abstraction barriers!)

The solution is to have_tagged data_: Each datum carries around
information about its type. We can do this by attaching tags to all our data. To
accomplish this, we need a constructor to tag our data: `attach-tag` and
selectors to grab the tag and the data from a piece of tagged data: `type-tag` and `contents`.

Here's a possible implementation for handling tagged data.

    (define (attach-tag tag data)
        (cons tag data))
    
    (define (type-tag tagged-data)
        (if (pair? tagged-data)
            (car tagged-data)
            (error "Not tagged data")))
    
    (define (contents tagged-data)
        (if (pair? tagged-data)
            (cdr tagged-data)
            (error "Not tagged data")))
    
    

Can you think of a way to define another set of constructors and selectors
that accomplishes the same task, but has a different internal representation?

## Writing Procedures that Use Tagged Data

Now that we've decided to tag our data, we've got to fix our implementations of the rational and complex number data types.
    
    ~~(define (make-rational num denom)~~
       ~~(cons num denom))~~

    (define (make-rational num denom)
        (attach-tag 'rational (cons num denom)))
    
    (define (make-complex real imag)
        (attach-tag 'complex (cons real imag)))
    

Notice, we easily could have replaced the function `attach-tag` with `cons`
and the code would have still worked. **However, this violates the data
abstraction barrier and should never be done!**

Now that we're able to tell the type of the data, let's try to actually do
something with that data!

## Why Tagged Data is So Cool

So hopefully you were able to write the procedure in the previous section. It
should look something like this:

    
    (define (add-numbers num1 num2)
        (cond ((and (equal? (type-tag num1) 'rational)
                    (equal? (type-tag num2) 'rational))
               (add-rational num1 num2))
              ((and (equal? (type-tag num1) 'complex)
                    (equal? (type-tag num2) 'complex))
               (add-complex num1 num2))
              ((and (equal? (type-tag num1) 'rational)
                    (equal? (type-tag num2) 'complex))
               (add-rational-complex num1 num2))
              (else
               (add-rational-complex num2 num1))))
    

After writing all of that code, hopefully you noticed and learned a few
things:

  1. We don't even need to know how tags are implemented to write this procedure! This is because we properly _abstracted away_ those details.
  2. If we want to add another type of number to our system, we'll have to rewrite our function, adding a fair number of extra conditions. The modifications would be straightforward, but in large systems this might not be scalable.

## Tagged Data in the Real World

The example we've shown you so far is a little contrived. In fact, we'll show
you arguably better ways of writing the same procedure later in this lesson.
However, there are many systems which do use tagged data in the real world. In
fact, **Scheme uses tagged data to evaluate your code!**

Every interpreter of Lisp-like languages uses type tagging when passing data
around. First, you'll need a little background. At some point in your life,
you've probably heard that computers read in only 1's and 0's. The sequence of
1's and 0's are computer instructions; they tell the computer what to do. As
you probably also know, a sequence of 1's and 0's can be evaluated as a number
(written in binary). However, sometimes a sequence of 1's and 0's need to
represent a word...so how does Scheme know how to interpret the sequence of
numbers? The answer is type-tagging! Scheme adds a few extra 1's and 0's to
the data (the tag) so that it knows how to interpret the data and can do the
right thing!

## Weaknesses of Tagged Data

As we alluded to in the last section, there are a few weaknesses in the tagged
data design.

One, the generic interface procedures (such as `add-numbers`) must know about
all of the different representations. For instance, suppose we wanted to
incorporate a new type of number into our system. We would need to identify
this new representation with a type, and then add clauses to `add-numbers,
multiply-numbers, divide-numbers`,  etc. to check for the new type and apply
the appropriate procedure for that type of number.

Another weakness of the technique is that even though the individual
representations and corresponding procedures can be designed separately, we
must guarantee that no two procedures in the entire system have the same name.
This is why we created the new procedure `add-numbers,` which calls `add-
rational,` `add-complex`, and `add-rational-complex`.

The issue underlying both of these weaknesses is that the technique for
implementing generic interfaces is not _additive_. The person implementing the
generic procedures must modify those procedures each time a  new
representation or type is added. Additionally, the people who originally wrote
the rational number system and the complex number system must now modify their
code to avoid name conflicts. In each of these cases, the changes that must be
made to the code are straightforward, but they must be made nonetheless, and
this is a source of inconvenience and error.

