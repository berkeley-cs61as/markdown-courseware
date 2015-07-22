## Mutable Data and Vectors

Unit 2 dealt with compound data as a means for constructing computational objects that have several parts. We abstracted their constructors and selectors and saw how they can be formed by nesting pairs and lists. But, we learned from Lesson 7 that there is another aspect of data that Unit 2 did not address. We are now able to mutate data with `set!`, and there is a similar operation for pairs. We will explore `mutators`, operations that modify data objects.

## Prerequisites

For this lab, make sure you understand all material from Unit 2, specifically manipulating lists and structure hierarchy. We are going to see how we can mutate the elements and structure of pairs.

## Readings

Take a look at the following readings:

  * [SICP 3.3.1-3](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-22.html#%_sec_3.3)
  * [These notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=56) are from old CS 61A lectures and cover mutation and vectors.