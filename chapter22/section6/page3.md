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
    

