## Streams in Lazy Evaluator

With lazy evaluation, streams and lists can be identical, so there is no need
for special forms or for separate list and stream operations. All we need to
do is to arrange matters so that `cons` is non-strict. One way to accomplish
this is to extend the lazy evaluator to allow for non-strict primitives, and
to implement `cons` as one of these. An easier way is to recall Lesson 4 that
there is no fundamental need to implement `cons` as a primitive at all.
Instead, we can represent pairs as procedures

    
    (define (cons x y)
      (lambda (m) (m x y)))
    (define (car z)
      (z (lambda (p q) p)))
    (define (cdr z)
      (z (lambda (p q) q)))

In terms of these basic operations, the standard definitions of the list
operations will work with infinite lists (streams) as well as finite ones, and
the stream operations can be implemented as list operations. Here are some
examples:

    
    (define (list-ref items n)
      (if (= n 0)
          (car items)
          (list-ref (cdr items) (- n 1))))
    
    (define (map proc items)
      (if (null? items)
          '()
          (cons (proc (car items))
                (map proc (cdr items)))))
    (define (scale-list items factor)
      (map (lambda (x) (* x factor))
           items))
    (define (add-lists list1 list2)
      (cond ((null? list1) list2)
            ((null? list2) list1)
            (else (cons (+ (car list1) (car list2))
                        (add-lists (cdr list1) (cdr list2))))))
    (define ones (cons 1 ones))
    (define integers (cons 1 (add-lists ones integers)))
    ;;; L-Eval input:
    (list-ref integers 17)
    ;;; L-Eval value:
    18
    

Note that these lazy lists are _even lazier_ than the streams of Lesson 11:
The `car` of the list, as well as the `cdr`, is delayed. In fact, even
accessing the `car` or `cdr` of a lazy pair need not force the value of a list
element. The value will be forced only when it is really needed -- e.g., for
use as the argument of a primitive, or to be printed as an answer.

