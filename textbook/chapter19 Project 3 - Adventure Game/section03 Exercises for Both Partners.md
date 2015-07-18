## Instructions

The first two exercises in this part should be done by both partners! You may work in pairs, as long as both partners fully understand the exercise and the concepts it covers. (There should still only be one solution that both partners agree on.) The remaining exercises will have numbers such as "A3", which translates to "Exercise 3 for Partner A".

The project is split into two major parts. After both partners have completed their exercises for part 1, combine your work and make sure that either partner understands the others' work. Since part 2 of the project depends on working code from part 1, combine your code for `adv.scm` and `adv-world.scm` carefully.

## Question 1

Instantiate a new Person object to represent yourself. Put yourself in a new place called `dormitory` (or wherever you live) and connect it to campus so that it is a reachable place. Create a place called `kirin`, north of `soda`. (It's actually on Solano Avenue.) Put a thing called `potstickers` there. Then give the necessary commands to move your character to `kirin`, take the `potstickers`, then move yourself to where `Brian` is, put down the `potstickers`, and have `Brian` take them. Then go back to the lab and get back to work. (There is no truth to the rumor that you'll get an A in the course for doing this in real life!) All this is just to ensure that you know how to speak the language of the
adventure program.

**List all messages that are sent during this episode.** It's a good idea to see if you can work this out in your head, at least for some of the actions that take place, but you can also trace the `ask` procedure to get a complete list. You don't have to hand in this listing of messages. (**You must turn in a transcript of the episode without the tracing.**) The purpose of this exercise is to familiarize you with the ways in which the different objects send messages
back and forth as they do their work.

[Tip: we have provided a `move-loop` procedure that you may find useful as an
aid in debugging your work. You can use it to move a person repeatedly.]

## Question 2

It is very important that you think about and understand the kinds of objects
involved in the adventure game. Please answer the following questions:

**a)** What kind of thing is the value of variable `Brian`? **Hint:** What is returned by STk in the following situation:
  
```    
> Brian
```

**b)** List all the messages that a Place understands. (You might want to maintain such a list for your own use, for every type of object, to help in the debugging effort.)

**c)** We have been defining a variable to hold each object in our world. For example, we defined `bagel` by saying:

```   
> (define bagel (instantiate thing 'bagel))
```

This is just for convenience. Every object does not have to have a top-level definition. Every object DOES have to be constructed and connected to the world. For instance, suppose we did this:
  
```
> (can-go Telegraph-Ave 'east (instantiate place 'Peoples-Park))

;;; assume Brian is at Telegraph
> (ask Brian 'go 'east)
```
  
What is returned by the following expressions and why?
  
```    
> (ask Brian 'place)

> (let ((where (ask Brian 'place)))
       (ask where 'name))

> (ask Peoples-park 'appear bagel)
``` 

**d)** The implication of all this is that there can be multiple names for objects. One name is the value of the object's internal `name` variable. In addition, we can define a variable at the top-level to refer to an object. Moreover, one object can have a private name for another object. For example, `Brian` has a variable `place` which is currently bound to the object that represents People's Park. Some examples to think about:
  
```    
> (eq? (ask Telegraph-Ave 'look-in 'east) (ask Brian 'place))

> (eq? (ask Brian 'place) 'Peoples-Park)

> (eq? (ask (ask Brian 'place) 'name) 'Peoples-Park)
```    

Okay. Suppose we type the following into STk:

```    
> (define computer (instantiate thing 'Durer))
```    

Which of the following is correct? Why?
  
```    
(ask 61a-lab 'appear computer)
```

or

```  
(ask 61a-lab 'appear Durer)
```

or

```  
(ask 61a-lab 'appear 'Durer)
```    

What is returned by `(computer 'name)`? Why?

**e)** We have provided a definition of the Thing class that does not use the object-oriented programming syntax described in the handout. Translate it into the new notation.

**f)** Sometimes it's inconvenient to debug an object interactively because its methods return objects and we want to see the names of the objects. You can create auxiliary procedures for interactive use (as opposed to use inside object methods) that provide the desired information in printable form. For example:
  
```    
(define (name obj) (ask obj 'name))
(define (inventory obj)
    (if (person? obj)
        (map name (ask obj 'possessions))
        (map name (ask obj 'things))))
```    

Write a procedure `whereis` that takes a person as its argument and returns
the name of the place where that person is. Write a procedure `owner` that
takes a thing as its argument and returns the name of the person who owns it.
(Make sure it works for things that aren't owned by anyone.)

Procedures like this can be very helpful in debugging the later parts of the
project, so feel free to write more of them for your own use. Now it's time
for you to make your first modifications to the adventure game. This is where
you split the work individually.

