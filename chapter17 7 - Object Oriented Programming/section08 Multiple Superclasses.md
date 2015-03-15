## Multiple Superclasses

It is possible for a class to have more than one parent. We can have a `TA`
class, a `singer` class, and a `TA-singer` class.

    
    (define-class (singer)
        (method (introduce) '(I am aiming for MTV awards!))
        (method (sing) '(tralala lalala)))
    
    (define-class (TA)
        (method (introduce) '(GO BEARS!))
        (method (teach) '(Let me help you with that box-and-pointer diagram)) )
    
    (define-class (singer-TA)
        (parent (singer) (TA)) )
    
    (define-class (TA-singer)
        (parent (TA) (singer)) )
    
    > (define rohin (instantiate singer-TA))
    > (define mona (instantiate TA-singer))
    
    > (ask rohin 'introduce)
    (I am aiming for MTV awards!)
    
    > (ask rohin 'sing)
    (tralala lalala)
    
    > (ask rohin 'teach)
    (Let me help you with that box-and-pointer diagram)
    
    
    > (ask mona 'introduce)
    (GO BEARS!)
    
    > (ask mona 'sing)
    (tralala lalala)
    
    > (ask mona 'teach)
    (Let me help you with that box-and-pointer diagram)
    

## Order of Parent

Note that `TA-singer` and `singer-TA` both inherit the `TA` class and `singer`
class, but in different order. When we ask instances of both class the same
message, the first parent takes precedence.

## Cheatsheet for Quizzes

FYI, you are allowed to have a copy of [this sheet ](https://docs.google.com/f
ile/d/0B2F__e2jC6gQSHhBdERPZ0pVRG8/edit?usp=drive_web) **in addition to** your
one-page-double-sided cheatsheet you normally have.

