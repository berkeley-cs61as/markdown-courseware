## Introduction to Python

We are going to learn about Python, the language that CS61A uses. Your friends
in CS61A are writing a Scheme interpreter in Python. Here in CS61AS, you are
going to write a Python Interpreter written in Scheme for your last project.

## Opening Python

To open Python, go to the terminal and type "python". The ">>>" prompt will
show up which is the equivalent of STk's "STk >".

As you will learn, spaces in Python are really important. Spaces for python
are Parentheses for Scheme.

## Playing with Python

Try these commands out in the interpreter. Most of these are taken from the
project spec added with some more examples. Some of the examples are supposed
to error. If there is a behavior that you don't expect, please ask!

### print

How would you ask Python to print "Hello World"? Well,

    
         >>> print "Hello World"
         Hello World
    

and that's it! (Yeah, srsly.) As you may have noticed from that simple
example, Python does not need left parentheses to call functions; you do not
need to precede 'print' with a left parenthesis. Python is case-sensitive, so
"PRINT" would not work. Another key difference is that Python only supports
infix operators, where the operator is present between its operands:

    
         >>> print 2 + 2
         4
    

You don't actually need the 'print' statement; the interpreter automatically
evaluates whatever is typed at the prompt, using a Read-Eval-Print loop that
is very similar to that used in the metacircular evaluator (We'll explore this
two sections from now.) For example:

    
         >>> 2 + 2
         4
    

#### What are the outputs of the following?

    
        >>> 3 + 1 - 5 * 1
        >>> 3 + (1 - 5) * 1
        >>> 10/2
        >>> 10/0
        >>> (5+1)
        >>> (10)
    

### Assignments

Assignments in Python are similar to assignments in other languages. If, for
example, you would like to provide a value to a variable called 'x':

    
         >>> x = 2
         >>> print x
         2
    

In contrast to Scheme, Python makes no distinction between DEFINE and SET!. If
a variable 'x' is not already present, the above assignment creates a new
variable 'x' in the global environment; otherwise, any previous value of 'x'
is overwritten.

#### Try the following:

    
        >>> num
        >>> num = 3
        >>> num
        >>> num = num + 1
        >>> num
        >>> num = "Berkeley"
        >>> num
    

### booleans

"If we used "=" to assign variables, how do we check for equality?". Python
(and most other languages) uses "==" instead.

#### Try the following:

    
         >>> 5 == 1
         >>> 5 == 5
         >>> 5 = 5
         >>> x = 10
         >>> x == 5
         >>> x == 10
         >>> x == x
    

Python has support for the Boolean operators 'and' and 'or', which work
exactly as the corresponding Scheme special forms work:

    
    
         >>> x = 3
         >>> (x == 3) and (x == 4)
         False
    
         >>> True and 3 and 5
         5
    
         >>> True and 3 and False
         False
    
         >>> True or 3 or False
         True
    

The Python equivalents for #t and #f are True and False, respectively
(capitalization is important).

#### Try the following:

    
        >>> True and True and False
        >>> True and True and True
        >>> (1 == 0) and (42 == 42)
        >>> (1 == 1) and (42 == (1 / 0))
        >>> (1 == 0) and (42 == (1 / 0))
        >>> 2 and 3 and 4
    
        >>> (1 == 0) or (42 == (1 / 0))
        >>> (1 == 1) or (42 == (1 / 0))
        >>> True or 5
        >>> False or 5
        >>> 5 or True
        >>> 10 or 5
        >>> False or (1 == 0) or 5
    
        >>> not True
        >>> not False
        >>> not (1==0)
        >>> not 5
        >>> not "world"  
        >>> not ""

### Lists

Python has lists! (Why wouldn't it?)

    
         >>> x = [1, 2, 3]
    

"x" is now a variable that stores a list of three numbers. As you can guess,
the Scheme analog is "(list 1 2 3)". Python lists can also be deep:

    
         >>> x = [[1, 2, 3], 2, 3]
    

Unfortunately, we can't CAR or CDR down a Python list. To access particular
elements of a list:

    
         >>> x[1]
         2
    

The notation "x[1]" returns the second element of the list (Python uses zero-
based counting). Again, in this case, the "[" character can be considered an
infix operator.

#### Try the following:

    
        >>> [0,1,3,-1,5]
        >>> lst = [0,1,3,-1,5]
        >>> lst
        >>> 0 in lst
        >>> 4 in lst
        >>> 0 not in lst
        >>> 4 not in lst
    
        >>> newlst = ["hey","I am", "a list", "too", ["boo", 100]]
        >>> newlst
        >>> "hey" in newlst
        >>> "am" in newlst
        >>> newlst[0]
        >>> newlst[0] == "hey"
        >>> newlst[1]
        >>> newlst[4]
        >>> newlst[5]
    

## Blocks

### Ifs

An important aspect of Python, born of its dedication to readable code, is its
usage of INDENTATION. In most other languages, including Scheme, indentation
is not an issue, since these languages ignore the number of spaces, and
instead use spaces to delimit symbols, numbers and words. However, in Python,
the number of spaces at the beginning of a line is important.

    
         >>> x = 2
         >>> if x == 1:
         ...   x = x + 1
         ...   print x
    

(You will have to press the ENTER key once more at the "..." prompt that will
show immediately after, to signify that you are done with the 'if'-statement.)
The 'if'-statement in Python works the same as its equivalent in Scheme: if
the condition of the 'if'-statement is satisfied, then the body is evaluated.
Notice that we have used '==' instead of '=': since the '=' character is
already used for assignment, we use '==' to check for equality. Notice also
that the body is indented: all statements in the body need to begin with the
same indentation. As a result, the following would not work:

    
         >>> x = 2
         >>> if x > 1:
         ...   x = x + 1
         ...    print x
    

because the second statement in the body is indented more than the first
statement. Similarly, the following would not work:

    
         >>> x = 2
         >>> if x > 1:
         ...    x = x + 1
         ...   print x
    

because the second statement in the body is indented less than the first
statement. In general, you would only DEDENT when you are done with a set of
related statements, or a BLOCK. All statements in a block need to be indented
with the same number of spaces. As a further example, an 'if'-statement can
also have an 'else'-clause, which is evaluated if the condition is not
satisfied.

    
         >>> x = 2
         >>> if x > 1:
         ...   x = x + 1
         ...   print x
         ... else:
         ...    x = x - 1
         ...    print x
    

Notice that the lines inside the blocks corresponding to the 'if'-statement
and its 'else'-clause are indented the same amount, but the blocks themselves
are indented by different amounts (though they don't have to be!). The
'if'-statement and the 'else'-clause, however, need to be indented by the same
amount because they belong to the same statement. However, *all statements
that are not part of a block or sub-block of statements should have no
indentation*. Try the following statement (which has an indentation of two
spaces after ">>> ") at the Python interpreter prompt:

    
         >>>   2 + 3
    

Indentation enforces clean code, but can take a while to get used to; the key
thing to remember is that you only need to indent when you are starting a new
block of statements.

#### Try the following:

    
    
         >>> if x == 3:
         ...   print x + 1
         ... elif x < 4:
         ...   print x + 2
         ... elif x > 5:
         ...   print x + 3
         ... else:
         ...   print x + 4
    

### Defining Functions

Python also has FUNCTIONS, its analog to Scheme's procedures. The following
defines the 'square' function:

    
         >>> def square(x):
         ...   return x * x
    

(Again, you will have to press the ENTER key once more at the "..." prompt
that will show immediately after, to signify that you are done with the
procedure body.) This syntax is similar to C-like languages, where the
arguments to the function are enclosed between parentheses and present
immediately after the name of the function. To call the function:

    
         >>> square(3)
         9
    

In this sense, the left parenthesis can be considered an infix operator, where
the operator is between its operands. To see why this is the case, recall that
in Scheme, the left parenthesis can be considered as a prefix operator, which
"calls" its first argument on the subsequent arguments. Similarly, in Python,
the left parenthesis "calls" its first argument ('square') on the next
argument ('3'). Also, if Python procedures need to return values, we have to
explicitly add a 'return'-statement to the body to return the answer; by
contrast, in Scheme, the very last line of a procedure definition is always
returned. This allows us to distinguish between Python functions that return
values, and Python functions that do not return values but are used primarily
for their side-effects:

    
         >>> def foo():
         ...   print "Hello World"
    

#### Try the following:

    
    >>> def sum_of_squares(x,y):
    ...   return square(x) + square(y)
    
    >>> sum_of_squares(3,4)
    >>> square(square(2))
    

### Loops

Python has constructs for loops. The project spec has a more in depth
explanation but give the following codes a shot:

#### while

A "while" loop takes in a predicate, and will keep evaluating the body until
the predicate evaluates to False.

    
    >>> x = 3
    >>> while x < 5:
    ...   print x
    ...   x = x + 1
    
    >>> y = 1
    >>> while y < 50:
    ...   print y
    ...   y = y*2
    
    

#### for

A "for" loop takes in a list (or any kind of sequence) and runs through the
body with each element of the sequence.

    
    
    >>> for i in [1, 3, 5, 2, 4]:
         ...   print i
    
    >>> for wd in ["Twinkle","twinkle","little","stars"]:
    ...   print wd
    

