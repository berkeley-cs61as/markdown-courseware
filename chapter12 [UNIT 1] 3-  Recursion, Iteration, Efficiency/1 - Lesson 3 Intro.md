## Lesson 3: Procedures and the Processes They Generate

This lesson is about the details. How fast is your program? How much memory
does it need? While we won't emphasize this measurement of how good a program
is in this course, it will be used in nearly all of your other CS classes.

## Readings

Here are the relevant readings for this lesson:

  * [SICP 1.2 - Procedures and the Processes They Generate](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html)
  * [Lecture Notes](http://inst.eecs.berkeley.edu/~cs61as/reader/notes.pdf#page=14)

## before we begin

This week is about efficiency. Usually in 61AS we're happy if you can get a
program working at all except for this week, when we introduce ideas that will
be more important to you later.

We want to know about the efficiency of algorithms, not of computer hardware.
So instead of measuring runtime in microseconds we ask about the number of
times some primitive (ﬁxed-time) operation is performed. Still, it's almost
impossible to calculate this number exactly since the number of steps to do
different operations will vary between different computers.

So then, what can we do?

Instead, we can measure the _order of growth_ of the number of steps we take.
Consider `max`, which takes in numbers as arguments and outputs the largest
one. When we double the number of arguments, will `max` take twice as long?
Will it take 1.5 times as long? Even though it's hard to count the exact
number of steps a procedure takes, characterizing the order of growth still
allows us to make judgements on how long a procedure will take to complete!

Orders of growth are relevant to memory as well. The more a procedure has to
"remember" while its executing, the more memory it has to use. Since memory is
a limited resource as well it's a good idea to find ways to keep memory usage
low. Let's talk about iteration, one way to reduce memory loss in recursive
procedures.

