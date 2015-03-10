## Introduction to Scheme and CS61AS

"Welcome to CS 61AS, the world's best computer science course, because we use
the world's best CS book as the textbook. The only thing wrong with this
course is that all the rest of the CS courses for the rest of your life will
seem a little disappointing (and repetitive)."

## Prerequisites and What to Expect

Before you continue, make sure that you have done all but the last step listed
[here. ](https://docs.google.com/a/berkeley.edu/document/d/1CN3FeXF0l_Yy9o9nHm
7uJHCXehK8S9Tq4wJZUaKMdKw/edit)

A Lesson is comprised of the subsections you see on the lefthand panel. **This
is Lesson 0.1: Introduction to Scheme and 61AS. You are currently in the
"Lesson 0.1 Intro" subsection.**

This Lesson runs through the basics of the Scheme programming language, and
also some of the need to know information regarding CS 61AS. Lessons are
structured so that you learn by exploring, making mistakes, asking questions,
and otherwise trying things out. Have fun!

## Deadlines

Typically you would turn in the subsection labeled "Homework" and take a Quiz.
For this Lesson, you must turn in Homework 0 (last subsesection for the Lesson
on the left). **Homework 0 is due by ****Friday Jan 23 2015, 11:59PM*.** We'll
show you how to submit in lab on Friday. There will be no Quiz with this
Lesson.

# What is Computer Science?

Note that all links in the following paragraphs are completely optional
reading and are included solely for the interest and amusement of the reader.

There isn't any one right answer. Computer Science means a lot of different
things to a lot of different people. For some it means building [a web
application that allows you to connect and keep up with your
friends](https://joindiaspora.com/). For others, it means engineering [self-
driving cars](http://en.wikipedia.org/wiki/Google_driverless_car). For yet
others, it means [lots and lots of
math](http://www.cs.princeton.edu/theory/index.php/Compbook/Draft). And [so
on](http://techcrunch.com/2013/07/11/raspberry-pi-microwave-hack/).

But here is a working definition: Computer Science answers the following
questions:

  1. What can we compute?
  2. How do we compute it?
  3. What can we do with that?

In this sense, Computer Science isn't about computers (that's a part of
Electrical Engineering), and it isn't really a science at the core (scientists
discover, we invent.)

Computer Scientist are like engineers: we [build cool
stuff](http://www.youtube.com/watch?v=gy5g33S0Gzo), we [solve
problems](http://en.wikipedia.org/wiki/Pancake_sorting).

## Complexity and Abstraction

All interesting problems in Computer Science are inherently complex. For
example, your web browser, the one you're using to view this page, has a lot
of moving parts: when you type in an url, the browser has to figure out which
server to go to, ask the server to give it the webpage you're looking for,
download the webpage, understand the webpage, and display it on your screen.
Each of these steps has their own parts and so on. How do we make sure all of
this works? In one word? Abstraction!

Abstraction is the ability to treat a complicated process as one whole unit,
and using that unit in an even more complex process. We already use
abstraction in our daily lives. For example, when you think of a celebrity,
let's say Neil Patrick Harris:

![Neil Patrick
Harris](http://upload.wikimedia.org/wikipedia/en/7/7d/Barney_Stinson.jpg)

One typically thinks "Hey, it's Neil!", not "Hey, it's a complicated chemical
process involving water, protein, connective tissue, fats, apatite,
carbohydrates, and DNA!"

This idea of Abstraction is wonderful, because now instead of keeping track of
the chemical reactions going on in this organism's metabolism, we can enjoy
him playing Barney on an episode of _How I Met your Mother_.

Another example of Abstraction is the description above of how a web browser
works. I left out all the messy details about exactly how you would type on a
keyboard which sends electronic signals to the motherboard when you type in a
url; how the computer recongizes that you've hit "Enter" and that now it's
time to run the code that finds out the server to contact; the algorithms
involved in finding that server in a network of thousands of servers; and so
on.

CS 61AS is about the different ways we abstract complexity using programming,
and how that allows us to solve different, complicated problems.

## Introduction

Notice that in the previous page, there was little mention of [programming
languages](http://en.wikipedia.org/wiki/Programming_language). That's because
in the grand scheme of things, programming languages don't matter. They only
matter because for any given problem, one language might let us solve the
problem in fewer lines of code over another, or one language might let us
solve the problem more efficiently, and so on.

What of the problem of teaching Computer Science? Which language should we use
for that? We have chosen Scheme, a dialect of [the Lisp programming
language](http://en.wikipedia.org/wiki/Lisp_programming_language). Among other
things, Scheme is a programming language suited for learning Computer Science.
We believe this partly because we can teach it to you in a day. We'll show
basics of the language today, after which you can start thinking about
Computer Science. As you learn more Computer Science, we'll incrementally show
you more of the language. Let's begin.

## Some things to notice

  1. In Scheme, [parentheses matter](http://xkcd.com/297/).
  2. When you ask a procedure to perform its action, you _call_ it. This is also called _invoking_ a procedure. Whenever you invoke a procedure, you must wrap the procedure call (the call to the procedure) in a set of paretheses.
  3. Everytime we invoke a procedure, we must follow prefix notation: the procedure that we're invoking is always the leftmost thing in the parentheses. Everything else are _arguments_ to that procedure--things we feed in to the procedure in order to get our answer. For example, we feed in 2 and 2 into + in order to get the answer 4.

## A Scheme Interpreter

Of course, a language is no good if no one speaks it. For programming
languages, the dialog is usually  between the programmer and a computer. An
**Interpreter** is a program that translates a particular language into
actions and computations that the computer performs. Interpreters is one way
to make computers do things, like compute large prime numbers or count all the
distinct words used in all of Shakespeare's plays.

Let's start our Scheme interpreter. We do this by opening a Terminal (Ctrl-
Alt-t) and then typing in "stk" (no quotes) and hitting Enter. We'll explain
later about what we just did. For now, let's play around!

## What will Scheme output?

What does the Scheme interpreter output when you try the following examples?
Type each example into the interpreter to try it out. Try out every example
individually and think about the result. Some of these examples will cause
errors - you should figure out why they cause errors. (If something errors,
the interpreter will output `"*** Error:"` along with some error message.)

    
    5
    (+ 2 3)
    (+ 5 6 7 8)
    (+ (* 3 4) 5)
    (+)
    +
    (sqrt 16)
    
    'hello
    (first 'hello)
    (first hello)
    (butfirst 'hello)
    (bf 'hello)
    (first (bf 'hello))
    (first 274)
    (+ (first 23) (last 45))
    
    (define pi 3.14159)
    pi
    'pi
    (+ pi 7)
    '(good morning)
    '(+ 2 3)
    

## The Big Ideas Behind 61AS

This class is full of Big Ideas. Here are the first two:

# The purpose of this course is _to help you learn_.

# The staff is here to _help you succeed_.

If at any point, you feel like this isn't the case, speak up! We're here to
help. :D

## How do you take 61AS?

61AS is a lab centric class. There is no lecture. You learn by working through
short readings and guided labs and participating in discussions. The TAs guide
you and help you get unstuck in lab and review the main ideas in discussions.
This style of learning promotes mastery and retention--learn by doing.

## Big Ideas

In 61AS, we will explore many Big Ideas that underlie all of Computer Science.
Here are some of the big ones:

**Functions** - To start off with, we'll think of programs as functions. All programs are essentially built up of a bunch of functions. We'll start here and see what exactly is a function and what we can use them for.

**Data** - Data is another thing essential to programs. Making data the central focus of our programs leads to powerful results.

**State** - These ideas deal with the question of "How do we program assuming we can change things over time?"

**Interpreters** - We go into how an interpreter works, and end up writing our own. We'll also consider a few other interpreters and see what they all have in common.

**Programming Paradigms** - Where we blow your mind and make you program in a completely different way than you've been doing for the past 13 weeks.

## Pacing

In terms of credit, 61AS is like no other course. Here are some of the
details.  See the syllabus for the full details.

  1. You can take 61AS over two semesters. We've divded the course into four required parts, or Units (corresponding with the units on Telebears). For example you can decide to take Units 1-3 this semester, and then Unit 4 next semester. There are also two optional units, unit 0 and unit 5, for which you can get CS 98 credit.
  2. Once you decide how many Units you're taking this semester, you follow a set of deadlines that keep you on track. There is a slipday system in place to give you a bit of extra time when you need it (see the syllabus for details.) This is useful if you have, say, 2 midterms and a paper due for other classes this week. However, if you miss too many of these deadlines, we will ask you to switch to a track with less Units. Conversely, if you're ahead of your deadlines, you may want to consider moving to a track with more Units. **You must finialize the Units you're taking by the unit change deadline.** We have incorperated deadlines into 61AS because from experience, we've determined that it's extremely miserable to finish the rest of the course in time if you don't meet them.

## Telebears

The staff  wil go over exactly what you should have on Telebears in the coming
weeks (the first three weeks of class). Don't worry about it now (the first
day). If you're worried or if something is urgent, talk with a TA.

## Units and Tracks

As mentioned above, the course is divided into Units:

  0. Introduction  
[optional, recommended for students with no programming experience]

  1. Functions
  2. Data
  3. State
  4. Interpreters and other Paradigms
  5. Programming Languages - Register Machines, Garbage Collection, Compilers  
[optional, recommended for students who want to be challenged even further]

Also mentioned above, you can take the course over two semesters by taking
some Units now and some Units next semester:

    
             Semester 1 | Semester 2
    ____________________|_____________
    Track 1-4  1 2 3 4  |
    Track 1-3  1 2 3    | 4
    Track 0-3  0 1 2 3  | 4
    ____________________|_____________
    Track 0-2  0 1 2    | 3 4
    Track 1-2    1 2    | 3 4
    

Tracks 0, 1, and 2 will allow you take CS 61B next semester.  However, you
must finish unit 4 in order to complete the CS 61A requirement.

**We expect everyone to start with either Track 0-3 or 1-4.**

Unit 5 is omitted from this chart. Talk with a TA if you're interested in
pursuing Unit 5.

## Alternatives to 61AS

**CS 61A** is the sister course to 61AS. It is offered in the traditional lecture-lab-discussion format, and covers the same Big Ideas as 61AS, except in the Python language and with a slightly different syllabus. 61A is the equivalent of Units 1-4 of 61AS. Taking either Units 1-4 of 61AS OR taking 61A will fullfil the requirements for CogSci, BioE, etc. More information:  
[http://www-inst.eecs.berkeley.edu/~cs61a/](http://www-
inst.eecs.berkeley.edu/~cs61a/)

[http://www-inst.eecs.berkeley.edu/~cs61a/fa13/61as.html](http://www-
inst.eecs.berkeley.edu/~cs61a/fa13/61as.html)

**CS 10** is called "The Beauty and Joy of Computing". It covers the equivilent of Units 0 and 1 of 61AS and is also aims to provide a gentle intro to Computer Science. CS 10 does not fullfil any of the requirements that 61A or 61AS fullfil. It uses a graphical language called Snap! that allows you to program by dragging and dropping components together. More info: [http://inst.eecs.berkeley.edu/~cs10/](http://inst.eecs.berkeley.edu/~cs10/)

## Takeaways

Here are some things covered in this subsection:

  1. What is Computer Science? How do we solve complex problems?
  2. What 61AS is about?
  3. What is Scheme? How do we interact with it? What are some of its features?

## Now what?

Now work on the "Homework 0.1" subsection.

