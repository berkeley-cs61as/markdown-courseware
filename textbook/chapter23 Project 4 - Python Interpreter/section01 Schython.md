You've seen how to implement a Scheme interpreter in Lesson 11 (`mceval.scm`). For this project, you will be helping us construct a Python interpreter called Schython (Scheme + Python = Schython).

To get the necessary project files and the spec, type the following into your interpreter:

	cp -r ~cs61as/lib/schython/ .

You may replace the `.` with whichever directory you want to save your project in.

## Project Files

Here's a breakdown of the files contained inside of `schython/`:

<table class="table table-bordered table-striped">
<thead><tr>
    <th>File Name</th>
    <th>Purpose</th>
</tr></thead><tbody>
<tr>
    <td>1.<code>schython.text</code></td>
    <td>This is the spec for your Schython project.</td>
</tr>
<tr>
    <td>2.<code>start.scm</code></td>
    <td>The file that will load the files needed to test your code. Make sure it is in the same directory as the rest of your Schython files.</td>
</tr>
<tr>
    <td>3.<code>obj.scm</code></td>
    <td>The code for our object-oriented system. OOP is used to create and manipulate the line-object class in <code>parser.scm</code>. Do NOT make changes to this file.</td>
</tr>
<tr>
    <td>4.<code>parser.scm</code></td>
    <td>The parser for our Schython interpreter. This file breaks down lines of input into Python characters recognizable by the Scheme interpreter. You should edit this file.</td>
</tr>
<tr>
    <td>5.<code>py-meta.scm</code></td>
    <td>This file is responsible for evaluating parsed Python code from our <code>parser.scm</code>. You should edit this file.</td>
</tr>
<tr>
    <td>6.<code>py-primitives.scm</code></td>
    <td>This file contains all the Scheme representations of Python data types. You should edit this file.</td>
</tr>
<tr>
    <td>7.<code>primitives.py</code></td>
    <td>A file containing a list of Python functions. Do NOT make changes to this file.</td>
</tr>
<tr>
    <td>8.<code>memoize.py</code></td>
    <td>The file for your answer to Question 9. You should edit this file.</td>
</tr>
<tr>
    <td>9.<code>tests</code></td>
    <td>A directory containing some tests that you can run to test your code. They are taken from the examples in <code>schython.text</code>. Instructions on how to run these tests can be found in the <code>README</code> file in this directory. Your grades will be determined by how many of these test cases you pass. </td>
</tr>
</tbody>
</table>

To load the project, type the following into your interpreter:

	(load "start.scm")

## Scoring

Each partner will work on nine problems. Five of these (Questions 1, 2, 6, 8, and 9) are common to both partners; the others (Questions 3, 4, 5, and 7) should be completed separately.

Groups will hand in a single completed copy of the project, with one answer for each question. Partners will receive the same score for the common exercises and different scores for the separate questions.

There will be points (indicated in `schython.text`) where partners should combine their work. This is necessary in order to move on to the next sections of the project.

If you cannot find a partner and/or wish to work alone, please talk to a TA.

## More About Python 

Python is a modern and very popular language used for teaching introductory CS courses, and is the language used in CS 61A. We will go over the basics of the Python language necessary to write the Schython interpreter in the spec. But, if you are interested (this is not at all required for this project), you can take a look at [Python's documentation](https://docs.python.org/3/tutorial/index.html) for a more comprehensive breakdown of the language.