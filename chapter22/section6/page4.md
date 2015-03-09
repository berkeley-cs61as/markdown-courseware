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
    

