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

<table>
<thead>
<tr>
<th style="text-align:center">Operation</th>
<th style="text-align:center">Expression</th>
<th style="text-align:center">Result</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Addition</td>
<td style="text-align:center">1 + 2 + 3</td>
<td style="text-align:center">6</td>
</tr>
<tr>
<td style="text-align:center">Subtraction</td>
<td style="text-align:center">7 - 1</td>
<td style="text-align:center">6</td>
</tr>
<tr>
<td style="text-align:center">Multiplication</td>
<td style="text-align:center">2 * 3</td>
<td style="text-align:center">6</td>
</tr>
<tr>
<td style="text-align:center">Division (Floating Point)</td>
<td style="text-align:center">5 / 2</td>
<td style="text-align:center">2.5</td>
</tr>
<tr>
<td style="text-align:center">Division (Floor)</td>
<td style="text-align:center">5 // 2</td>
<td style="text-align:center">2</td>
</tr>
<tr>
<td style="text-align:center">Modulo (remainder)</td>
<td style="text-align:center">5 % 2</td>
<td style="text-align:center">1</td>
</tr>
<tr>
<td style="text-align:center">Less than</td>
<td style="text-align:center">5 &lt; 7</td>
<td style="text-align:center">True</td>
</tr>
<tr>
<td style="text-align:center">Greater than</td>
<td style="text-align:center">5 &gt; 7</td>
<td style="text-align:center">False</td>
</tr>
<tr>
<td style="text-align:center">Check Equals</td>
<td style="text-align:center">5 == 5</td>
<td style="text-align:center">True</td>
</tr>
<tr>
<td style="text-align:center">Less than or equals</td>
<td style="text-align:center">5 &lt;= 2</td>
<td style="text-align:center">False</td>
</tr>
<tr>
<td style="text-align:center">Greater than or equals</td>
<td style="text-align:center">5 &gt;= 2</td>
<td style="text-align:center">True</td>
</tr>
</tbody>
</table>

## Boolean Values
Boolean values are encoded by ```True``` and ```False```. Boolean values are again self-evaluating (will return themselves). The following operations return boolean values and when used with other data types will consider them to be true (anything that is not ```False``` is true).

<table>
<thead>
<tr>
<th style="text-align:center">Operation</th>
<th style="text-align:center">Expression</th>
<th style="text-align:center">Result</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">true</td>
<td style="text-align:center"><code>True</code></td>
<td style="text-align:center"><code>True</code></td>
</tr>
<tr>
<td style="text-align:center">false</td>
<td style="text-align:center"><code>False</code></td>
<td style="text-align:center"><code>False</code></td>
</tr>
<tr>
<td style="text-align:center">not</td>
<td style="text-align:center">not <code>True</code></td>
<td style="text-align:center"><code>False</code></td>
</tr>
<tr>
<td style="text-align:center">and</td>
<td style="text-align:center">1 and <code>True</code></td>
<td style="text-align:center"><code>True</code></td>
</tr>
<tr>
<td style="text-align:center">or</td>
<td style="text-align:center"><code>False</code> or not <code>True</code></td>
<td style="text-align:center"><code>False</code></td>
</tr>
</tbody>
</table>

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

<table>
<thead>
<tr>
<th style="text-align:center">Operation</th>
<th style="text-align:center">Expression</th>
<th style="text-align:center">Result</th>
<th style="text-align:center">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Print</td>
<td style="text-align:center">print(“hello”)</td>
<td style="text-align:center">Prints to output</td>
<td style="text-align:center">also works on numbers</td>
</tr>
<tr>
<td style="text-align:center">Selection</td>
<td style="text-align:center">“hello”[0]</td>
<td style="text-align:center">‘h’</td>
<td style="text-align:center">is zero-indexed</td>
</tr>
<tr>
<td style="text-align:center">Selection</td>
<td style="text-align:center">“hello”[-1]</td>
<td style="text-align:center">‘o’</td>
<td style="text-align:center">can also be negative</td>
</tr>
<tr>
<td style="text-align:center">Slicing</td>
<td style="text-align:center">“hello”[1:3]</td>
<td style="text-align:center">‘el’</td>
<td style="text-align:center">is inclusive of the start; <br> exclusive of the end</td>
</tr>
<tr>
<td style="text-align:center">Slicing</td>
<td style="text-align:center">“hello”[1:]</td>
<td style="text-align:center">‘ello’</td>
<td style="text-align:center">end defaults to length of string; <br> but first operation</td>
</tr>
<tr>
<td style="text-align:center">Slicing</td>
<td style="text-align:center">“hello”[:-1]</td>
<td style="text-align:center">‘hell’</td>
<td style="text-align:center">start defaults to zero; <br> but last operation</td>
</tr>
<tr>
<td style="text-align:center">Concatenation</td>
<td style="text-align:center">“hello” + &quot; world&quot;</td>
<td style="text-align:center">‘hello world’</td>
<td style="text-align:center">cannot mix with numbers <br> creates a new string!</td>
</tr>
<tr>
<td style="text-align:center">Convert</td>
<td style="text-align:center">str(1)</td>
<td style="text-align:center">‘1’</td>
<td style="text-align:center">useful for concatenation of numbers and strings</td>
</tr>
<tr>
<td style="text-align:center">Repetition</td>
<td style="text-align:center">“hello” * 3</td>
<td style="text-align:center">‘hellohellohello’</td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">Contains</td>
<td style="text-align:center">‘h’ in “hello”</td>
<td style="text-align:center"><code>True</code></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">Get Length</td>
<td style="text-align:center">len(“hello”)</td>
<td style="text-align:center">4</td>
<td style="text-align:center"></td>
</tr>
</tbody>
</table>

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

**For the table below, assume x = ["this", "is", "a", "list"]**

<table>
<thead>
<tr>
<th style="text-align:center">Operation</th>
<th style="text-align:left">Expression</th>
<th style="text-align:left">Results</th>
<th style="text-align:center">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Print</td>
<td style="text-align:left">print([1,2,3])</td>
<td style="text-align:left">Prints to output</td>
<td style="text-align:center">also works on numbers &amp; strings</td>
</tr>
<tr>
<td style="text-align:center">Selection</td>
<td style="text-align:left">x[0]</td>
<td style="text-align:left">‘this’</td>
<td style="text-align:center">is zero-indexed</td>
</tr>
<tr>
<td style="text-align:center">Selection</td>
<td style="text-align:left">x[-1]</td>
<td style="text-align:left">‘list’</td>
<td style="text-align:center">can also be negative</td>
</tr>
<tr>
<td style="text-align:center">Slicing</td>
<td style="text-align:left">x[1:3]</td>
<td style="text-align:left">‘el’</td>
<td style="text-align:center">is inclusive of the start; <br> exclusive of the end</td>
</tr>
<tr>
<td style="text-align:center">Slicing</td>
<td style="text-align:left">x[1:]</td>
<td style="text-align:left">‘ello’</td>
<td style="text-align:center">end defaults to length of string; <br> but first operation</td>
</tr>
<tr>
<td style="text-align:center">Slicing</td>
<td style="text-align:left">x[:-1]</td>
<td style="text-align:left">‘hell’</td>
<td style="text-align:center">start defaults to zero; <br> but last operation</td>
</tr>
<tr>
<td style="text-align:center">Concatenation</td>
<td style="text-align:left">[1, 2, 3] + [4, 5, 6]</td>
<td style="text-align:left">[1, 2, 3, 4, 5, 6]</td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">Concatenation</td>
<td style="text-align:left">&gt;&gt;&gt; x = [1, 2, 3] <br> &gt;&gt;&gt; x += [4, 5, 6] <br> &gt;&gt;&gt; x</td>
<td style="text-align:left">[1, 2, 3, 4, 5, 6]</td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">Repetition</td>
<td style="text-align:left">[‘Hi!’] * 4</td>
<td style="text-align:left">[‘Hi!’, ‘Hi!’, ‘Hi!’, ‘Hi!’]</td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">Contains</td>
<td style="text-align:left">3 in [1, 2, 3]</td>
<td style="text-align:left"><code>True</code></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">Iteration <br> (more on this in the control section!)</td>
<td style="text-align:left">for i in [1, 2, 3]: print(i)</td>
<td style="text-align:left">1<br>2<br>3</td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:center">Get Length</td>
<td style="text-align:left">len([1, 2, 3])</td>
<td style="text-align:left">3</td>
<td style="text-align:center"></td>
</tr>
</tbody>
</table>

> **Homework Problem 2: Fruits and Vegetables**
>
> ```x = ["apple", "banana", "carrot"]```
>
> Write one line of code that when executed returns "apples bananas and carrots". 
