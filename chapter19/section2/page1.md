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

