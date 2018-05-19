So, creating abstract data types is handy, and it's nice to be able write programs without worrying about implementation details. But, what's actually stopping us from crossing the abstraction barrier and use the underlying implementation?

Nothing, actually. Racket will not complain if you use `cons` instead of `make-rational`, or if you use `car` instead of `numerator`. We've reproduced the code for the rational numbers ADT below:

    (define (make-rational numer denom)
      (if (= 0 denom)
          (error "Divisor cannot be 0!")
          (cons numer denom)))

    (define (numerator rat)
      (car rat))

    (define (denominator rat)
      (cdr rat))

Technically, if we make the following calls, the selectors will still return what we expect:

    -> (define x (make-rational 3 4))
    x
    -> (define num (car x))
    num
    -> (= num (numerator x))
    #t

So, why would we want to use the selector if we can just use `car` instead? This works for now, but problems arise when we later change our implementation of our constructors and selectors. Going under the abstraction and making assumptions on how the data structure was implemented is called a **data abstraction violation (DAV)**.

## Example: Violating the Data Abstraction

Let's say we write a new function, `expt-rat`, that takes a rational number and the power to which we exponentiate the rational number and returns another rational number to that power. This is the procedure we wrote:

    (define (expt-rat rat n)
      (make-rational (expt (car rat) n) 
                     (expt (cdr rat) n)))

Can you spot the DAV? Given our current implementation of rational numbers, `expt-rat` should work with no problems:

    -> (define x (make-rational 3 4))
    x
    -> (expt-rat x 2)
    (9 . 16)

But this is dangerous! You can't guarantee your code will work if, later on, you decide to change your implementation. Let's say we rewrite the implementation this way:

    (define (make-rational numer denom)
      (lambda (m) (cond ((equal? m 'numerator) numer)
                        ((equal? m 'denominator) denom)
                        (else (error "bad message to rational")))))

    (define (numerator rat)
      (rat 'numerator))

    (define (denominator rat)
      (rat 'denominator))

What happens now when we call `expt-rat`?

    -> (define y (make-rational 5 6))
    y
    -> (expt-rat y 4)
    ; car: contract violation
    ;   expected: pair?
    ;   given: #<procedure>
    ; [,bt for context]

We get an error! Our code for `expt-rat` above assumes that we store the rational number as a pair, and foolishly calls `car` to retrieve the numerator and `cdr` for the denominator. And thus, Racket throws a fit when we try calling these procedures on a lambda function.

## Abstraction Barriers

![A window into a lab with a warning tape that says "ABSTRACTION BARRIER DO NOT CROSS"](http://farm9.staticflickr.com/8505/8388536641_b8428f32fe_b.jpg)

We defined the rational-number operations in terms of a constructor `make-rat` and selectors `numerator` and `denominator`. In general, the underlying idea of data abstraction is to identify for each type of data object a basic set of operations (e.g. the constructors and selectors) in terms of which all manipulations of data objects of that type will be expressed, and then to use only those operations in manipulating the data.

We can envision the structure of the rational-number system as shown in the figure below. The horizontal lines represent abstraction barriers that isolate different "levels" of the system. At each level, the barrier separates the programs (above) that use the data abstraction from the programs (below) that implement the data abstraction. Programs that use rational numbers manipulate them solely in terms of the procedures supplied "for public use" by the rational-number package: `add-rat`, `sub-rat`, `mul-rat`, `div-rat`, and `equal-rat?`. These, in turn, are implemented solely in terms of the constructor and selectors `make-rat`, `numerator`, and `denominator`, which themselves are implemented in terms of pairs. The details of how pairs are implemented are irrelevant to the rest of the rational-number package so long as pairs can be manipulated by the use of `cons`, `car`, and `cdr`. In effect, procedures at each level are the interfaces that define the abstraction barriers and connect the different levels.

![Abstraction diagram for numbers](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/ch2-Z-G-6.gif)

This simple idea has many advantages. One advantage is that it makes programs much easier to maintain and to modify. Any complex data structure can be represented in a variety of ways with the primitive data structures provided by a programming language.

To understand why this is so important, consider a world where data abstraction didn't exist. Of course, the choice of representation influences the programs that operate on it; thus, if the representation were to be changed at some later time, all such programs might have to be modified accordingly. This task could be time-consuming and expensive in the case of large programs unless the dependence on the representation were to be confined by design to a very few program modules.

Luckily, if the data was implemented without any violation of data abstraction,  it would be very easy to modify the entire program -- you only need to modify constructors and selectors.
