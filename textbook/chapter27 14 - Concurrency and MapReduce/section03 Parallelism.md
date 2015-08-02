## Getting Started

To work with the ideas in this section, you'll need our concurrency library. From a lab machine (or over SSH), type the following into your Scheme interpreter:

```    
(load "~cs61as/lib/concurrency.scm")
```

## An Overview

Many things we take for granted in ordinary programming become problematic
when there is any kind of parallelism involved. These situations include:

* multiple processors (hardware) sharing data
* software multithreading (simulated parallelism)
* operating system input/output device handlers

This is covered in greater detail in CS 162 (operating systems).

## Why Parallelism Is Hard

To see in simple terms what the problem is, think about the Scheme expression

    
    (set! x (+ x 1))

As you'll learn in more detail in 61C, Scheme translates this into a sequence
of instructions to your computer. The details depend on the particular
computer model, but it'll be something like this:

    
    lw $8, x        ; Put the value of x into processor register number 8.
    addi $8, $8, 1  ; Take the value of register 8, add 1 to it, and put  
                    ; the new value back into register 8.
    sw $8, x        ; Set the value in register 8 as the value of x.
    

You don't have to understand the details of the code here (you'll learn about
it in 61C), but you should have an idea of what's going on.

(A _register_ is a place where computers put values so that it can operate on
them.  So a computer usually can't immediately add 1 to x - it has to first
put the value of x in a register, and only then can it add 1 to it.)

Ordinarily we would expect this sequence of instructions to have the desired
effect. If the value of x was 100 before these instructions, it should be 101
after them.

But imagine that this sequence of three instructions can be interrupted by
other events that come in the middle. To be specific, let's suppose that
someone else is also trying to add 1 to x's value. Now we might have this
sequence:

    
    my process      value of x   other process
    ----------      ----------   -------------  
      $8 = ??        x = 100       $9 = ??
      
    lw $8, x  
      $8 = 100       x = 100       $9 = ??
      
    addi $8, $8, 1  
      $8 = 101       x = 100       $9 = ??
      
                                 lw $9, x  
      $8 = 101       x = 100       $9 = 100
      
                                 addi $9, $9, 1  
      $8 = 101       x = 100       $9 = 101
      
                                 sw $9, x  
      $8 = 101       x = 101       $9 = 101
      
    sw $8, x  
      $8 = 101       x = 101       $9 = 101

The ultimate value of x will be 101, instead of the correct 102.

The general idea we need to solve this problem is the critical section, which
means a sequence of instructions that mustn't be interrupted. The three
instructions starting with the load and ending with the store are a critical
section.

Actually, we don't have to say that these instructions can't be interrupted;
the only condition we must enforce is that they can't be interrupted by
another process that uses the variable x. It's okay if another process wants
to add 1 to y meanwhile. So we'd like to be able to say something like

    
    reserve x
    lw $8, x
    addi $8, 1
    sw $8, x
    release x
    

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

