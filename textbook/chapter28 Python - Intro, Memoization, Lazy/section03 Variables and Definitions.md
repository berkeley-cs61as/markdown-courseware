## Variables 
To define a variable use the equal symbol. (To check equality, a double equals is used.) Variables can defined inside and outside of procedure defintion.

```python
>>> x = 1 #set x to be 1
>>> x
1
>>> x == 1 #check if x equals 1
True
```

## Defining Procedures
To define a procedure use “def”. In python, indentations (spacing at the start of a line) and colons are the delimiters that structure the python code into blocks. Therefore, we’ll use indentation to indicate the body of our procedures. When you’re done, you’ll need a empty line with a matching indentation as the def line to close the define block if you are inputing it directly into the interpreter.

```python
>>> def func(x):
...    x = x * 2
...    return x + 1
... 
>>> func(1)
3
```
* Line 1:  (0 space indentation) The function header assigns the function name and parameters
* Line 2:  (3 space indentation) The body of func doubles x and returns (double of x) + 1
* Line 3:  (0 space indentation) Empty Line closes the define block
* Line 4:  Call on func with parameter x as 1
* Line 5:  3 is returned

Note how we use a return statement. A return stops the procedure and delivers the output back to be displayed. Lines lacking the return statement aren’t propagated beyond the procedure innards. An apt analogy would be: a return statement is similar to you speaking aloud and the non-return statements are similar to your thoughts leading up to what you say. 

If your body is a single expression, you can write procedure definitions in one line. You still need the empty line

```python
>>> def func(x): return (x * 2) + 1
...
>>> func(2)
5
```
* Line 1:  (0 space indentation) The function header assigns the function name and parameters and the single expression body
* Line 2:  (0 space indentation) Empty Line closes the define statement
* Line 3:  Call on func with parameter x as 1
* Line 4:  3 is returned
