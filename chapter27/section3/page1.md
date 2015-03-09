## Levels of Abstraction

Computers don't really have instructions quite like `reserve` and `release`,
but we'll see that they do provide similar mechanisms. A typical programming
environment includes concurrency control mechanisms at three levels of
abstraction:

    
    SICP name        What's protected              Provided by
    ---------        ----------------              -----------
    serializer       high level abstraction        programming language
                       (procedure, object, ...)
    
    mutex            critical section              operating system
    
    test-and-set!    one atomic                    hardware
                       state transition
    

The serializer and the mutex are, in SICP, abstract data types. There is a
constructor `make-serializer` that's implemented using a mutex, and a
constructor `make-mutex` that's implemented using `test-and-set!`, which is a
(simulated, in our case) hardware instruction.

We'll go over serializers and mutexes in the coming sections.

