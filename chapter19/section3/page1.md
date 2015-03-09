## Question 2

It is very important that you think about and understand the kinds of objects
involved in the adventure game. Please answer the following questions:

  1. What kind of thing is the value of variable `BRIAN`? Hint: What is returned by scheme in the following situation: You type:
    
    > BRIAN

  2. List all the messages that a `PLACE` understands. (You might want to maintain such a list for your own use, for every type of object, to help in the debugging effort.)
  3. We have been defining a variable to hold each object in our world. For example, we defined bagel by saying:
    
    (define bagel (instantiate thing 'bagel))

This is just for convenience. Every object does not have to have a top-level
definition. Every object DOES have to be constructed and connected to the
world. For instance, suppose we did this:

    
    
    > (can-go Telegraph-Ave 'east (instantiate place 'Peoples-Park))
    
    ;;; assume BRIAN is at Telegraph
    > (ask Brian 'go 'east)
    
    

What is returned by the following expressions and WHY?

    
    
    > (ask Brian 'place)
    
    > (let ((where (ask Brian 'place)))
           (ask where 'name))
    
    > (ask Peoples-park 'appear bagel)
    
    

  4. The implication of all this is that there can be multiple names for objects. One name is the value of the object's internal NAME variable. In addition, we can define a variable at the top-level to refer to an object. Moreover, one object can have a private name for another object. For example, BRIAN has a variable PLACE which is currently bound to the object that represents People's Park. Some examples to think about:
    
    
    > (eq? (ask Telegraph-Ave 'look-in 'east) (ask Brian 'place))
    
    > (eq? (ask Brian 'place) 'Peoples-Park)
    
    > (eq? (ask (ask Brian 'place) 'name) 'Peoples-Park)
    

OK. Suppose we type the following into scheme:

    
    
    > (define computer (instantiate thing 'Durer))
    

Which of the following is correct? Why?

    
    
    (ask 61a-lab 'appear computer)
    
    or 
    
    (ask 61a-lab 'appear Durer)
    
    or
    
    (ask 61a-lab 'appear 'Durer)
    

What is returned by `(computer 'name)`? Why?

  5. We have provided a definition of the THING class that does not use the object-oriented programming syntax described in the handout. Translate it into the new notation.
  6. Sometimes it's inconvenient to debug an object interactively because its methods return objects and we want to see the names of the objects. You can create auxiliary procedures for interactive use (as opposed to use inside object methods) that provide the desired information in printable form. For example:
    
    
    (define (name obj) (ask obj 'name))
    (define (inventory obj)
        (if (person? obj)
            (map name (ask obj 'possessions))
            (map name (ask obj 'things))))
    

Write a procedure `WHEREIS` that takes a person as its argument and returns
the name of the place where that person is. Write a procedure `OWNER` that
takes a thing as its argument and returns the name of the person who owns it.
(Make sure it works for things that aren't owned by anyone.)

Procedures like this can be very helpful in debugging the later parts of the
project, so feel free to write more of them for your own use. Now it's time
for you to make your first modifications to the adventure game. This is where
you split the work individually.

