## Data Abstraction and Sequences

Remember all that fancy talk about abstraction in Lesson 0.1, and the sneak peek into abstraction using HOFs in Lesson 2? In this lesson, you will finally try your hand at creating some really interesting abstract data types. You'll learn that when programming, controlled complexity and layering abstractions will leave you with clean, professional code. 

## Prerequisites and What to Expect

**Prerequisites:** Learning computer science is cumulative. Make sure you know all the preceding lessons, with emphasis on Lessons 1 and 2. 

**What to Expect:** One way programming can be summarized is with the following three (very very general) categories:

  * Storing Data
  * Extracting Data
  * Manipulating Data

In Lesson 2, we learned **procedural abstraction**. In other words, we learned how to create generalized, "customizable" procedures using abstraction. This falls under the third category above, manipulation of data. For example, we have a list of numbers - our _data_ - and we want to _manipulate_ it to find the sum of all of its squares. We generalized this with our abstracted procedure, _sum_. If you don't remember this, we recommend you take a second to [review](http://berkeley-cs61as.github.io/textbook/hofs-procedures-as-arguments.html).

This lesson is about **data abstraction**, which falls into the first two categories. We will first introduce data structures used to store data (pairs and lists), show how to extract and manipulate them (`map`), and then finally teach you how to create your own abstract data types.

Get pumped.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 2 Intro](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-13.html)
  * [SICP 2.1](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-14.html#%25_sec_2.1)
  * [SICP 2.2.1](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%25_sec_2.2.1)
  * [Lecture Notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=18) (ignore the part on MapReduce -- this is different than map!)

