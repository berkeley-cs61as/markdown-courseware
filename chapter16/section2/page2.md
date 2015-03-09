## Tagged Data in the Real World

The example we've shown you so far is a little contrived. In fact, we'll show
you arguably better ways of writing the same procedure later in this lesson.
However, there are many systems which do use tagged data in the real world. In
fact, **Scheme uses tagged data to evaluate your code!**

Every interpreter of Lisp-like languages uses type tagging when passing data
around. First, you'll need a little background. At some point in your life,
you've probably heard that computers read in only 1's and 0's. The sequence of
1's and 0's are computer instructions; they tell the computer what to do. As
you probably also know, a sequence of 1's and 0's can be evaluated as a number
(written in binary). However, sometimes a sequence of 1's and 0's need to
represent a word...so how does Scheme know how to interpret the sequence of
numbers? The answer is type-tagging! Scheme adds a few extra 1's and 0's to
the data (the tag) so that it knows how to interpret the data and can do the
right thing!

