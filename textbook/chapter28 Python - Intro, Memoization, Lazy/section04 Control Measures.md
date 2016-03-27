## If, Elif, Else
Conditional statements are formed using if, elif, and else statements. An if statement is composed of a predicate and a body that is executed if the predicate is satisfied. Elif is shorthand for “else if” and is used for any additional conditions beyond the first if statement. An elif statement has a similar construction as an if statement. The else statement follows all if and elif statement as is triggered when none of the conditional statements prior are fulfilled. 

If, elif, and else use indentation and colons to block the code appropriately. When you’re done, you’ll need a empty line with a matching indentation as the first line to close the conditional when you are inputting directly into the interpreter.

```python
>>> if False:
...    3
... elif True:
...    4
... else:
...    5
...
4
```

* Line 1:  (0 space indentation) The if condition
* Line 2:  (3 space indentation) The if body
* Line 3:  (0 space indentation) The else if condition
* Line 4:  (3 space indentation) The else if body
* Line 5:  (0 space indentation) The else
* Line 6:  (3 space indentation) The else body
* Line 7:  (0 space indentation) Empty Line closes the if block and invokes evaluation
* Line 8: 4 is returned (the if case is skipped, the elif case is triggered, never reaches the else case)

Note that no return statement is used. That is because the conditional statement is outside of a procedure definition. Inside of a function body, you would expect “return 3” instead of “3” and so on, if that were the desired return value.

> **Homework Problem 3: Fizz Buzz**
>
>Write a program that prints the integers from 1 to n (n is an argument to the procedure).
>But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
>For numbers which are multiples of both three and five print "FizzBuzz".


## Loops and Range
In python, loops are supported. Loop execute a block or line of code multiple times. Loops are useful for when you would like to progress through a sequence  or repeat an operation---use a loop to iterate, instead of recursion. ```for``` loops control the number of iterations to correspond with the entries of a sequence to iterate over. ```while``` loops control the number of iterations with a predicate.

Certain control statements can be invoked within loops to stop and break out of the loop or to skip to the next iteration. ```break``` does the former and ```continue``` does the latter action. Consult online resources if you need an example of their use.

### While loops
While loops contain a predicate which is checked before the start of every iteration. If the predicate is not satisfied, the while loop stops. A while block uses a colon and indentation to indicate which line is the header and which are in the body

```python
>>> x = 0
>>> while x < 3:
...    print("repeat")
...    x += 1
...
hello
hello
hello
>>> x #check what x is
3
```

* Line 1: set up a variable x equals to zero
* Line 2: (0 spaces) While header with condition of x being less than 3
* Line 3: (3 spaces) While body line calls print
* Line 4: (3 spaces) While body line increments x by 1 (x += 1 is the same as x = x + 1)
* Line 5: (0 spaces) Empty line closes While block and the block is evaluated
* Line 6: hello is printed (for x = 0)
* Line 7: hello is printed (for x = 1)
* Line 8: hello is printed (for x = 2) 
* Line 9: check the value of x
* Line 10: 3 is returned for the value of x (which is NOT less than 3)

> **Homework Problem 4: Snow White and the Seven Dwarves**
>
> Write a program called snow_white that takes in two numbers as arguments, the first is the num_chants, the second is the max_sing.
>
> The program:
> 1. prints "heigh" "ho" alternatingly
> 2. prints "its off to work we go" after num_chants of "heigh" or "ho"
> 3. stops printing after having "it's off to work we go" max_sing times
>
> EXAMPLE: should print it's off to work we go between every ```5``` alternating his and hos, for a maximum of ```2``` times.
>
>     >>> snow_white(5, 2)
>     heigh
>     ho
>     heigh
>     ho
>     heigh
>     it's off to work we go
>     ho
>     heigh
>     ho
>     heigh
>     ho
>     it's off to work we go
>
> Use a while loop (and possibly control statements) to accomplish this behavior.




> **Homework Problem 5: Push First Odd Back (taken from CS10)**
>
> Write a function called push_first_odd_back that takes in a list as an argument
> This function should place the first odd number at the back of the input list. 
> Do not return a new list - in fact this function shouldn't return anything, 
> it should only modify the input list. (Hint: use the while loop)

### For Loops
For loops contain a variable and a sequence (more on this later). With each iteration, the value of the variable changes to the next value in the sequence. As with other multiple line blocks, for loops are delimited by colons and indentation and are completed with an empty line. Within the body of the for loop, you can access the value of the variable being iterated over. 

The ```range``` function creates a progression of numbers which can then be used in a ```for``` loop for control. Range takes in a start, end, and increment to create a sequence that includes the start and incremental entries up to, but excluding the end. Range will default start to zero and increment to one if not provided. For now, only use ```range``` in the context of a ```for``` loop, later in the lesson we'll go in depth on how ```range``` works.

TIP: if you want x iterations and don't actually plan on using the iteration variable, use ```range(x)```

```python
>>> for i in range(2): #same as do two times
...    print "hello"
...
hello
hello
```
```python
>>> for i in range(3): #i is 0 then 1 then 2
...    print i
...
0
1
2
```
```python
>>> for i in range(2, 6, 2): #start at 2, stop before 6, skip 2
...    print(i)
...
2
4
```
You can also use a string or a list in the place of range as a sequence to iterate over
```python
>>> sum = 0
>>> for number in [1,5,8]: #iterating over a list
...    sum += number
...
>>> sum
14
```
```python
>>> longer_string = ""
>>> for letter in "apple": #iterating over string
...    longer_string += letter * 3
...
>>> longer_string
'aaappppppllleee'
```


> **Homework Problem 6: Cats and Dogs**
>
> Write a program that return True if the string "cat" and "dog" appear the same number of times in the given string. 
>
>     cat_dog('catdog') → True
>     cat_dog('catcat') → False
>     cat_dog('1cat1cadodog') → True
