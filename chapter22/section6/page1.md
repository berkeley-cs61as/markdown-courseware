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
    

