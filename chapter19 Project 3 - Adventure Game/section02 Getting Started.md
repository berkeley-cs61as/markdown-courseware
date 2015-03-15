## Getting Started

In this laboratory assignment, we will be exploring two key ideas: the
simulation of a world in which objects are characterized by a set of state
variables, and the use of message passing as a programming technique for
modularizing worlds in which objects interact.

Object-oriented programming is becoming an extremely popular methodology for
any application that involves interactions among computational entities.

Examples:

  * operating systems (processes as objects)
  * window systems (windows as objects)
  * games (asteroids, spaceships, gorillas as objects)
  * drawing programs (shapes as objects)

To start, copy the following five files into your directory:

    
       ~cs61as/lib/obj.scm           The object-oriented system
       ~cs61as/lib/adv.scm           The adventure game program
       ~cs61as/lib/tables.scm	An ADT you'll need for parts A5 and B4
       ~cs61as/lib/adv-world.scm     The specific people, places, and things
       ~cs61as/lib/small-world.scm   A smaller world you can use for debugging  
      
    (i.e. in the terminal, type "cp ~cs61as/lib/obj.scm ." to copy the first file. Don't forget the "." at the end)

To work on this project, you must load these files into Scheme in the correct
order: `obj.scm` first, then `adv.scm` and `tables.scm` when you're using
that, and finally the particular world you're using, either `adv-world.scm` or
`small-world.scm`. The work you are asked to do refers to `adv-world.scm`;
`small-world.scm` is provided in case you'd prefer to debug some of your
procedures in a smaller world that may be less complicated to remember and
also faster to load.

(To load a scheme file e.g. obj.scm, type (load "obj.scm") in the interpreter)

The reason the adventure game is divided into `adv.scm` (containing the
definitions of the object classes) and `adv-world.scm` (containing the
specific instances of those objects in Berkeley) is that when you change
something in `adv.scm` you may need to reload the entire world in order for
your changed version to take effect. Having two files means that you don't
also have to reload the first batch of procedures.

## An Intro to the Program

In this program there are three classes: THING, PLACE, and PERSON.

Here are some examples selected from `adv-world.scm`:

    
    
    ;;; construct the places in the world
    (define Soda (instantiate place 'Soda))
    (define BH-Office (instantiate place 'BH-Office))
    (define art-gallery (instantiate place 'art-gallery))
    (define Pimentel (instantiate place 'Pimentel))
    (define 61A-Lab (instantiate place '61A-Lab))
    (define Sproul-Plaza (instantiate place 'Sproul-Plaza))
    (define Telegraph-Ave (instantiate place 'Telegraph-Ave))
    (define Noahs (instantiate place 'Noahs))
    (define Intermezzo (instantiate place 'Intermezzo))
    (define s-h (instantiate place 'sproul-hall))
    
    ;;; make some things and put them at places
    (define bagel (instantiate thing 'bagel))
    (ask Noahs 'appear bagel)
    
    (define coffee (instantiate thing 'coffee))
    (ask Intermezzo 'appear coffee)
    
    ;;; make some people
    (define Brian (instantiate person 'Brian BH-Office))
    (define hacker (instantiate person 'hacker Pimentel))
    
    ;;; connect places in the world
    
    (can-go Soda 'up art-gallery)
    (can-go art-gallery 'west BH-Office)
    (can-go Soda 'south Pimentel)
    

Having constructed this world, we can now interact with it by sending messages
to objects. Here is a short example.

    
    
    ; We start with the hacker in Pimentel.
    
    > (ask Pimentel 'exits)
    (NORTH SOUTH)
    > (ask hacker 'go 'north)
    HACKER moved from PIMENTEL to SODA
    

We can put objects in the different places, and the people can then take the
objects:

    
    
    > (define Jolt (instantiate thing 'Jolt))
    JOLT
    > (ask Soda 'appear Jolt)
    APPEARED
    > (ask hacker 'take Jolt)
    HACKER took JOLT
    TAKEN
    

You can take objects away from other people, but the management is not
responsible for the consequences... (Too bad this is a fantasy game, and there
aren't really vending machines in Soda that stock Jolt.)

