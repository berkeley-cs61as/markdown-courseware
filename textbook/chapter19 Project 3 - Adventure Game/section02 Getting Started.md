## Getting Started

In this laboratory assignment, we will be exploring two key ideas: 

  * The simulation of a world in which objects are characterized by a set of state variables
  * The use of **message passing** as a programming technique for modularizing worlds in which objects interact.

Object-oriented programming is becoming an extremely popular methodology for any application that involves interactions among computational entities.

Some examples include:

  * Operating systems (processes as objects)
  * Windows systems (windows as objects)
  * Games (asteroids, spaceships, gorillas as objects)
  * Drawing programs (shapes as objects)

## Project Files

To start, copy the necessary files for the project into your directory:

    cp -r ~cs61as/lib/adventure/ .

<table class="table table-bordered table-striped">
<thead><tr>
    <th>File Name</th>
    <th>Purpose</th>
</tr></thead><tbody>
<tr>
    <td>1.<code>obj.scm</code></td>
    <td>The code for our object-oriented system.</td>
</tr>
<tr>
    <td>2.<code>adv.scm</code></td>
    <td>The adventure game program. It contains the definitions of the object classes.</td>
</tr>
<tr>
    <td>3.<code>tables.scm</code></td>
    <td>An ADT you'll need for Questions A5 and B4.</td>
</tr>
<tr>
    <td>4.<code>adv-world.scm</code></td>
    <td>The specific instances of the objects (i.e., people, places, and things) in the adventure game.</td>
</tr>
<tr>
    <td>5.<code>small-world.scm</code></td>
    <td>A smaller, simplified world that you can use for debugging.</td>
</tr>
</tbody>
</table>

To work on this project, you must load these files into STk in the exact order you see in the table above. Load either `adv-world.scm` OR `small-world.scm`, but NOT BOTH. The work you are asked to do refers to `adv-world.scm`;
`small-world.scm` is provided in case you'd prefer to debug some of your
procedures in a smaller world that may be less complicated to remember and
also faster to load.

To load a Scheme file, e.g., `obj.scm`, type 

    (load "obj.scm")

into the interpreter.

The reason the adventure game is divided into `adv.scm` and `adv-world.scm` is that when you make any changes to the class definitions in `adv.scm`, you may need to reload the entire world in order for your changed version to take effect. Having two files means that you don't also have to reload the first batch of procedures.

## An Intro to the Program

In this program there are three main classes: Person, Place, and Thing.

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
to objects. Here is a short example:

    
    
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