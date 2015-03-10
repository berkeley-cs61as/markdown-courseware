## Submission Guide

**You must finish both lab and homework for a lesson before submitting your homework for that lesson.**

**IF YOU HAVE ANY TROUBLE WITH SUBMITTING, ASK A QUESTION ON PIAZZA OR TALK TO A TA.**

**BEFORE SUBMITTING HOMEWORK: Make sure your file loads in Scheme. You can verify this by typing into STk: (load "hw0-2.scm"),** or whatever the name of your homework file is. You will not receive credit for homework that does not load in Scheme.****

To submit your assignment, you need to be logged in on any of the lab
computers. If you want to submit from home, you must connect remotely to the
lab computers. More on that later.

Now, click on the "Terminal" icon on the left. Terminal is a terminal
emulator, a method of interacting directly to the computer via text commands.
It's sort of an "interpreter" for your entire computer. You can do useful
things with xterm like navigate and manipulate the filesystem (think Windows
Explorer), submit homework (what we're doing now), and start the Scheme
interpreter (via stk)!

Let's submit an assignment. This requires the following steps:

  1. Making a folder for an assignment (optional, but strongly recommended, as we'll see)
  2. Doing the assignment in that folder (or moving the files to that folder if you've already completed the assignment)
  3. Running the `submit` command
  4. Checking if the assignment was correctly submitted

We're going to submit an assignment called "units", which will tell the staff
how many units you're doing.

## 1. Making a folder

In the terminal type

`mkdir units`

This tells the computer to make a directory (a folder) named units. You can
double check that it exists (and also see what else is in this current
directory) by running

`ls`

Now we need to navigate to that folder, so we'll do:

`cd units`

## 2. Finishing the Assignment

In order to complete this assignment, you must create a file named units
(inside the directory named units) and put in it which units you're planning
on doing. For example, if you were to do units 0, 1, 2, and 3, you'd put

`0 1 2 3`

## 3. Submitting

After you've created the file, you can submit the assignment by doing

`submit units`

This tells the computer that you want to submit the assignment units (that the
system knows, it has nothing to do with the name of the file or the directory
that you've created).

## 4. Checking your submission

The following command allows you to look at the times in which you've
submitted:

`glookup -t`

That's all for now. You might be interested in connecting from home in order
to work on all of this. Details about that are under the Resources link on the
top!

