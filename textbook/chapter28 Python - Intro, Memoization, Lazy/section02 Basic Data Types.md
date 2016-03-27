## Basics
As experienced programmers, we'll be speeding through the basics so you can dive in. But a few rules before we begin:
* Python is case sensitive
* Indentation via Spaces or tabs are used to structure Python code
* Spaces and tabs are not interchangeable so pick one and stick to it (spaces are recommended)
   * if you are using sublime, under View > Indentation please check "Indentation Using Spaces"
   * if you ever run into errors, under View > Indentation try converting all indentation to spaces and double check your spacing
* Parentheses can be used to clarify order of evaluation (like in math)
   * (1 + 2) * 3
* A # will comment out anything that follows it on the same line

## Math and Numbers
Numbers are self-evaluating (will return themselves). Numerical operations can be performed on numbers, variables holding numerical value, and numerical return values. Here is a table of most of the built in Python numerical operations. Feel free to input these expressions directly into the Python interpreter and examine the results.

|Operation|Expression|Result|
|:---------:|:----------:|:------:|
| Addition| 1 + 2 + 3|6|
| Subtraction| 7 - 1|6|
| Multiplication| 2 * 3|6|
| Division (Floating Point)| 5 / 2 |2.5|
| Division (Floor)| 5 // 2 |2|
| Modulo (remainder)| 5 % 2 |1|
| Less than|5 < 7|True|
| Greater than|5 > 7|False
| Check Equals|5 == 5|True
| Less than or equals|5 <= 2|False
| Greater than or equals|5 >= 2|True

## Boolean Values
Boolean values are encoded by ```True``` and ```False```. Boolean values are again self-evaluating (will return themselves). The following operations return boolean values and when used with other data types will consider them to be true (anything that is not ```False``` is true).

|Operation|Expression|Result|
|:---------:|:----------:|:------:|
|true|```True```|```True```|
|false|```False```|```False```|
|not| not ```True```| ```False```|
|and| 1 and ```True```| ```True```|
|or| ```False``` or not ```True```| ```False```|

## Strings
Strings are another self-evaluating data type. They constructed as a sequence of characters between matching quotes (you can use either single or double quotes but you cannot mix and match them within a string). 

```python
>>> "hello"
'hello'
>>> 'hello'
'hello'
```
Characters inside of the opening and closing quotes are not evaluated. So you can have quote characters inside of a string as long as they are not matching to the open and close quotes

```python
>>> "hello my name is 'Sally'"
"hello my name is 'Sally'"
>>> 'hello my name is "Sally"'
'hello my name is "Sally"'
```
> **Homework Problem 1: Naughty Strings**
>
>What is the error message returned when you improperly use quotes inside of strings?
>
>Provide an example and explain the error message.

Here are some useful operations on string and/or returning strings

|Operation|Expression|Result|Notes|
|:---------:|:----------:|:------:|:--:|
Print | print("hello") | Prints to output | also works on numbers
Selection| "hello"[0] | 'h'| is zero-indexed|
Selection|"hello"[-1]| 'o' | can also be negative|
Slicing| "hello"[1:3]| 'el' | is inclusive of the start; <br> exclusive of the end
Slicing| "hello"[1:] | 'ello' | end defaults to length of string; <br> but first operation
Slicing| "hello"[:-1] | 'hell' | start defaults to zero; <br> but last operation
Concatenation| "hello" + " world"| 'hello world' | cannot mix with numbers <br> creates a new string!
Convert | str(1) | '1'| useful for concatenation of numbers and strings
Repetition| "hello" * 3 | 'hellohellohello'
Contains |'h' in "hello" | ```True```
Get Length | len("hello") |4

## Lists
Lists and strings are similar! Strings are lists of characters, but for the sake of abstraction, we distinguish the two. **Don't** violate our data abstraction barrier when you use strings vs lists, but do use their similarities to wrap your head around how to approach either. (One big difference is that you can't set elements of a string, but you can with a list!)

Surprise, surprise... Lists are self-evaluating! Lists are declared by enumerating comma separated elements between square brackets. Similarly to strings, access list values using indices (indexing starts at 0).

```python
>>> test_list = ["this", "is", "a", "list", 1 , 2 , 3]
>>> test_list
['this', 'is', 'a', 'list', 1 , 2 , 3]
>>> test_list[3]
'list'
```
* Line 1: Set up a list and assign it to a variable named test_list
* Line 2: Check what the variable test_list is
* Line 3: ['this', 'is', 'a', 'list', 1 , 2 , 3] is returned (the list we created!)
* Line 4: Get the fourth element of the list (index = 3)
* Line 5: 'list' is returned (the fourth element)

And again, here is a compilation of list indexing and operations!

->**For the table below, assume x = ["this", "is", "a", "list"]**<-

| Operation | Expression | Results | Notes |
|:---------:|:-----------|:--------|:-----:|
Print | print([1,2,3]) | Prints to output | also works on numbers & strings
Selection| x[0] | 'this'| is zero-indexed|
Selection|x[-1]| 'list' | can also be negative|
Slicing| x[1:3]| 'el' | is inclusive of the start; <br> exclusive of the end
Slicing| x[1:] | 'ello' | end defaults to length of string; <br> but first operation
Slicing| x[:-1] | 'hell' | start defaults to zero; <br> but last operation| Deletion | >>> x = [1, 2, 3]  <br> >>> del(x[0]) <br> >>> x | [2, 3] |  |
| Concatenation | [1, 2, 3] + [4, 5, 6] | [1, 2, 3, 4, 5, 6] |  |
| Concatenation | >>> x = [1, 2, 3] <br> >>> x += [4, 5, 6] <br> >>> x | [1, 2, 3, 4, 5, 6] |  |
| Repetition | ['Hi!'] * 4 | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] |  |
| Contains | 3 in [1, 2, 3] | ```True``` |  |
| Iteration <br> (more on this in the loops section!) | for i in [1, 2, 3]: print(i) | 1<br>2<br>3 |  |
| Get Length | len([1, 2, 3]) | 3 |  |

> **Homework Problem 2: Fruits and Vegetables**
>
> ```x = ["apple", "banana", "carrot"]```
>
> Write one line of code that when executed returns "apples bananas and carrots". 
