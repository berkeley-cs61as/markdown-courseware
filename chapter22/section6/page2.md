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
    

