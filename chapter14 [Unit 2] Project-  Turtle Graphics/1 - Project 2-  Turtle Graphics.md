## Project 2: turtle graphics

This project presents a simple language for drawing pictures that illustrates
the power of data abstraction and closure, and also exploits higher-order
procedures in an essential way. The language is designed to make it easy to
experiment with patterns such as below, which are composed of repeated
elements that are shifted and scaled. In this language, the data objects being
combined are represented as procedures rather than as list structure. Just as
cons, which satisfies the closure property, allowed us to easily build
arbitrarily complicated list structure, the operations in this language, which
also satisfy the closure property, allow us to easily build arbitrarily
complicated patterns.

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-24.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-25.gif)

To begin, copy the file `~cs61as/lib/picture.scm` to your directory.

Or, download it from
[here](http://inst.eecs.berkeley.edu/~cs61as/library/picture.scm)

To draw pictures once you've defined the primitive painters:

    
    > (cs)
    > (ht)
    > (===your-painter=== full-frame)
    

For example:

    
    > (wave full-frame)
    > ((square-limit wave 3) full-frame)

## milestones

Units 1-4: 10/4

Units 0-3: 10/15

Units 1-3: 10/11

Units 0-2: 11/15

## The picture language

When we began our study of programming in lesson 1, we emphasized the
importance of describing a language by focusing on the language's primitives,
its means of combination, and its means of abstraction. We'll follow that
framework here.

Part of the elegance of this picture language is that there is only one kind
of element, called a painter. A painter draws an image that is shifted and
scaled to fit within a designated parallelogram-shaped frame. For example,
there's a primitive painter we'll call wave that makes a crude line drawing,
as shown in figure 2.10. The actual shape of the drawing depends on the frame
-- all four images in figure 2.10 are produced by the same wave painter, but
with respect to four different frames. Painters can be more elaborate than
this: The primitive painter called rogers paints a picture of MIT's founder,
William Barton Rogers, as shown in figure 2.11.23 The four images in figure
2.11 are drawn with respect to the same four frames as the wave images in
figure 2.10.

To combine images, we use various operations that construct new painters from
given painters. For example, the beside operation takes two painters and
produces a new, compound painter that draws the first painter's image in the
left half of the frame and the second painter's image in the right half of the
frame. Similarly, below takes two painters and produces a compound painter
that draws the first painter's image below the second painter's image. Some
operations transform a single painter to produce a new painter. For example,
flip-vert takes a painter and produces a painter that draws its image upside-
down, and flip-horiz produces a painter that draws the original painter's
image left-to-right reversed.

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-26.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-27.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-28.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-29.gif)

Figure 2.10: Images produced by the wave painter, with respect to four
different frames. The frames, shown with dotted lines, are not part of the
images.

  
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-30.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-31.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-32.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-33.gif)

Figure 2.11: Images of William Barton Rogers, founder and first president of
MIT, painted with respect to the same four frames as in figure 2.10 (original
image reprinted with the permission of the MIT Museum).

Figure 2.12 shows the drawing of a painter called `wave4` that is built up in
two stages starting from wave:

    
    (define wave2 (beside wave (flip-vert wave)))
    (define wave4 (below wave2 wave2))  
      
    ![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-34.gif)                         ![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-35.gif)  
      
    (define wave2                              (define wave4 
      (beside wave (flip-vert wave)))            (below wave2 wave2)) 
    

Figure 2.12: Creating a complex figure, starting from the wave painter of
figure 2.10.

## combining painters

In building up a complex image in this manner we are exploiting the fact that
painters are closed under the language's means of combination. The beside or
below of two painters is itself a painter; therefore, we can use it as an
element in making more complex painters. As with building up list structure
using cons, the closure of our data under the means of combination is crucial
to the ability to create complex structures while using only a few operations.

Once we can combine painters, we would like to be able to abstract typical
patterns of combining painters. We will implement the painter operations as
Scheme procedures. This means that we don't need a special abstraction
mechanism in the picture language: Since the means of combination are ordinary
Scheme procedures, we automatically have the capability to do anything with
painter operations that we can do with procedures. For example, we can
abstract the pattern in `wave4` as

    
    (define (flipped-pairs painter)
      (let ((painter2 (beside painter (flip-vert painter))))
        (below painter2 painter2)))
    

and define `wave4` as an instance of this pattern:

`(define wave4 (flipped-pairs wave))`

We can also define recursive operations. Here's one that makes painters split
and branch towards the right as shown in figures 2.13 and 2.14:

    
    
    (define (right-split painter n)
      (if (= n 0)
          painter
          (let ((smaller (right-split painter (- n 1))))
            (beside painter (below smaller smaller)))))  
      
    ![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-36.gif)            ![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-37.gif)  
       right-split n                   up-split n  

Figure 2.13: Recursive plans for `right-split` and `corner-split`.

We can produce balanced patterns by branching upwards as well as towards the
right (see exercise 2.44 and figures 2.13 and 2.14):

    
    (define (corner-split painter n)
      (if (= n 0)
          painter
          (let ((up (up-split painter (- n 1)))
                (right (right-split painter (- n 1))))
            (let ((top-left (beside up up))
                  (bottom-right (below right right))
                  (corner (corner-split painter (- n 1))))
              (beside (below painter top-left)
                      (below bottom-right corner))))))  
    
    

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-38.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-39.gif)

`(right-split wave 4)  (right-split rogers 4)`

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-40.gif)
![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-41.gif)

`(corner-split wave 4)  (corner-split rogers 4)`

Figure 2.14: The recursive operations `right-split` and `corner-split` applied
to the painters wave and rogers.

By placing four copies of a corner-split appropriately, we obtain a pattern
called `square-limit`, whose application to wave and rogers is shown in the
figure below:

    
    ![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-25.gif)  
    
    (define (square-limit painter n)
      (let ((quarter (corner-split painter n)))
        (let ((half (beside (flip-horiz quarter) quarter)))
          (below (flip-vert half) half))))  
    

## 1. up-split

Define the procedure `up-split` used by `corner-split`. It is similar to
`right-split`, except that it switches the roles of below and beside.

## higher-order operations

In addition to abstracting patterns of combining painters, we can work at a
higher level, abstracting patterns of combining painter operations. That is,
we can view the painter operations as elements to manipulate and can write
means of combination for these elements -- procedures that take painter
operations as arguments and create new painter operations.

For example, `flipped-pairs` and `square-limit` each arrange four copies of a
painter's image in a square pattern; they differ only in how they orient the
copies. One way to abstract this pattern of painter combination is with the
following procedure, which takes four one-argument painter operations and
produces a painter operation that transforms a given painter with those four
operations and arranges the results in a square. `Tl`, `tr`, `bl`, and `br`
are the transformations to apply to the top left copy, the top right copy, the
bottom left copy, and the bottom right copy, respectively.

    
    (define (square-of-four tl tr bl br)
      (lambda (painter)
        (let ((top (beside (tl painter) (tr painter)))
              (bottom (beside (bl painter) (br painter))))
          (below bottom top))))
    

Then `flipped-pairs` can be defined in terms of `square-of-four` as follows:

    
    (define (flipped-pairs painter)
      (let ((combine4 (square-of-four identity flip-vert
                                      identity flip-vert)))
        (combine4 painter)))
    

and `square-limit` can be expressed as

    
    (define (square-limit painter n)
      (let ((combine4 (square-of-four flip-horiz identity
                                      rotate180 flip-vert)))
        (combine4 (corner-split painter n))))
    

## 2. split

`Right-split` and `up-split` can be expressed as instances of a general
splitting operation. Define a procedure `split` with the property that
evaluating

    
    (define right-split (split beside below))
    (define up-split (split below beside))
    

produces procedures `right-split` and `up-split` with the same behaviors as
the ones already defined.

## frames

Before we can show how to implement painters and their means of combination,
we must first consider frames. A frame can be described by three vectors -- an
origin vector and two edge vectors. The origin vector specifies the offset of
the frame's origin from some absolute origin in the plane, and the edge
vectors specify the offsets of the frame's corners from its origin. If the
edges are perpendicular, the frame will be rectangular. Otherwise the frame
will be a more general parallelogram.

Figure 2.15 shows a frame and its associated vectors. In accordance with data
abstraction, we need not be specific yet about how frames are represented,
other than to say that there is a constructor make-frame, which takes three
vectors and produces a frame, and three corresponding selectors `origin-
frame`, `edge1-frame`, and `edge2-frame`

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-42.gif)

Figure 2.15: A frame is described by three vectors -- an origin and two edges.

We will use coordinates in the unit square (0<x,y<1) to specify images. With
each frame, we associate a frame coordinate map, which will be used to shift
and scale images to fit the frame. The map transforms the unit square into the
frame by mapping the vector v = (x,y) to the vector sum

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-43.gif)

For example, (0,0) is mapped to the origin of the frame, (1,1) to the vertex
diagonally opposite the origin, and (0.5,0.5) to the center of the frame. We
can create a frame's coordinate map with the following procedure:

    
    (define (frame-coord-map frame)
      (lambda (v)
        (add-vect
         (origin-frame frame)
         (add-vect (scale-vect (xcor-vect v)
                               (edge1-frame frame))
                   (scale-vect (ycor-vect v)
                               (edge2-frame frame))))))
    

Observe that applying `frame-coord-map` to a frame returns a procedure that,
given a vector, returns a vector. If the argument vector is in the unit
square, the result vector will be in the frame. For example,

    
    ((frame-coord-map a-frame) (make-vect 0 0))
    

returns the same vector as

    
    (origin-frame a-frame)
    

## 3. data abstraction part 1

A two-dimensional vector v running from the origin to a point can be
represented as a pair consisting of an x-coordinate and a y-coordinate.
Implement a data abstraction for vectors by giving a constructor `make-vect`
and corresponding selectors `xcor-vect` and `ycor-vect`. In terms of your
selectors and constructor, implement procedures `add-vect`, `sub-vect`, and
`scale-vect` that perform the operations vector addition, vector subtraction,
and multiplying a vector by a scalar:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-44.gif)

Notice that scale-vect takes two different arguments.  To be compatible with
the given code, you should define scale-vect so that the **first** argument is
the **scalar**, and the **second** argument is the **vector**.

## 4. data abstraction part 2

Here are two possible constructors for frames:

    
    (define (make-frame origin edge1 edge2)
      (list origin edge1 edge2))
    
    (define (make-frame origin edge1 edge2)
      (cons origin (cons edge1 edge2)))
    

For each constructor supply the appropriate selectors to produce an
implementation for frames.

## painter

A painter is represented as a procedure that, given a frame as argument, draws
a particular image shifted and scaled to fit the frame. That is to say, if p
is a painter and f is a frame, then we produce p's image in f by calling p
with f as argument.

The details of how primitive painters are implemented depend on the particular
characteristics of the graphics system and the type of image to be drawn. For
instance, suppose we have a procedure `draw-line` that draws a line on the
screen between two specified points. Then we can create painters for line
drawings, such as the wave painter in figure 2.10, from lists of line segments
as follows:

    
    (define (segments->painter segment-list)
      (lambda (frame)
        (for-each
         (lambda (segment)
           (draw-line
            ((frame-coord-map frame) (start-segment segment))
            ((frame-coord-map frame) (end-segment segment))))
         segment-list)))
    

The segments are given using coordinates with respect to the **unit square.**
For each segment in the list, the painter transforms the segment endpoints
with the frame coordinate map and draws a line between the transformed points.

Representing painters as procedures erects a powerful abstraction barrier in
the picture language. We can create and intermix all sorts of primitive
painters, based on a variety of graphics capabilities. The details of their
implementation do not matter. Any procedure can serve as a painter, provided
that it takes a frame as argument and draws something scaled to fit the frame.

## 5. segments

A directed line segment in the plane can be represented as a pair of vectors
-- the vector running from the origin to the start-point of the segment, and
the vector running from the origin to the end-point of the segment. Use your
vector representation from the previous page (Data Abstraction Part 1) to
define a representation for segments with a constructor `make-segment` and
selectors `start-segment` and `end-segment`.

## 6. primitive painters

Use `segments->painter` to define the following primitive painters:

a. The painter that draws the outline of the designated frame.

b. The painter that draws an ``X'' by connecting opposite corners of the
frame.

c. The painter that draws a diamond shape by connecting the midpoints of the
sides of the frame.

d. The `wave` painter.

## transforming and combining painters

An operation on painters (such as `flip-vert` or `beside`) works by creating a
painter that invokes the original painters with respect to frames derived from
the argument frame. Thus, for example, `flip-vert` doesn't have to know how a
painter works in order to flip it -- it just has to know how to turn a frame
upside down: The flipped painter just uses the original painter, but in the
inverted frame.

Painter operations are based on the procedure `transform-painter`, which takes
as arguments a painter and information on how to transform a frame and
produces a new painter. The transformed painter, when called on a frame,
transforms the frame and calls the original painter on the transformed frame.
The arguments to `transform-painter` are points (represented as vectors) that
specify the corners of the new frame: When mapped into the frame, the first
point specifies the new frame's origin and the other two specify the ends of
its edge vectors. Thus, arguments within the unit square specify a frame
contained within the original frame.

    
    (define (transform-painter painter origin corner1 corner2)
      (lambda (frame)
        (let ((m (frame-coord-map frame)))
          (let ((new-origin (m origin)))
            (painter
             (make-frame new-origin
                         (sub-vect (m corner1) new-origin)
                         (sub-vect (m corner2) new-origin)))))))
    

Here's how to flip painter images vertically:

    
    (define (flip-vert painter)
      (transform-painter painter
                         (make-vect 0.0 1.0)   ; new origin
                         (make-vect 1.0 1.0)   ; new end of edge1
                         (make-vect 0.0 0.0))) ; new end of edge2
    

Using `transform-painter`, we can easily define new transformations. For
example, we can define a painter that shrinks its image to the upper-right
quarter of the frame it is given:

    
    (define (shrink-to-upper-right painter)
      (transform-painter painter
                         (make-vect 0.5 0.5)
                         (make-vect 1.0 0.5)
                         (make-vect 0.5 1.0)))
    

Other transformations rotate images counterclockwise by 90 degrees

    
    (define (rotate90 painter)
      (transform-painter painter
                         (make-vect 1.0 0.0)
                         (make-vect 1.0 1.0)
                         (make-vect 0.0 0.0)))
    

or squash images towards the center of the frame:

    
    (define (squash-inwards painter)
      (transform-painter painter
                         (make-vect 0.0 0.0)
                         (make-vect 0.65 0.35)
                         (make-vect 0.35 0.65)))
    

Frame transformation is also the key to defining means of combining two or
more painters. The `beside` procedure, for example, takes two painters,
transforms them to paint in the left and right halves of an argument frame
respectively, and produces a new, compound painter. When the compound painter
is given a frame, it calls the first transformed painter to paint in the left
half of the frame and calls the second transformed painter to paint in the
right half of the frame:

    
    (define (beside painter1 painter2)
      (let ((split-point (make-vect 0.5 0.0)))
        (let ((paint-left
               (transform-painter painter1
                                  (make-vect 0.0 0.0)
                                  split-point
                                  (make-vect 0.0 1.0)))
              (paint-right
               (transform-painter painter2
                                  split-point
                                  (make-vect 1.0 0.0)
                                  (make-vect 0.5 1.0))))
          (lambda (frame)
            (paint-left frame)
            (paint-right frame)))))
    

Observe how the painter data abstraction, and in particular the representation
of painters as procedures, makes beside easy to implement. The beside
procedure need not know anything about the details of the component painters
other than that each painter will draw something in its designated frame.

## 7. flip-horiz

Define the transformation `flip-horiz`, which flips painters horizontally, and
transformations that rotate painters counterclockwise by 180 degrees and 270
degrees.

## 8. below

Define the `below` operation for painters. `Below` takes two painters as
arguments. The resulting painter, given a frame, draws with the first painter
in the bottom of the frame and with the second painter in the top. Define
below in two different ways -- first by writing a procedure that is analogous
to the `beside` procedure given above, and again in terms of beside and
suitable rotation operations (from the exercise above).

## Levels of Language for robust design

The picture language exercises some of the critical ideas we've introduced
about abstraction with procedures and data. The fundamental data abstractions,
painters, are implemented using procedural representations, which enables the
language to handle different basic drawing capabilities in a uniform way. The
means of combination satisfy the closure property, which permits us to easily
build up complex designs. Finally, all the tools for abstracting procedures
are available to us for abstracting means of combination for painters.

We have also obtained a glimpse of another crucial idea about languages and
program design. This is the approach of stratified design, the notion that a
complex system should be structured as a sequence of levels that are described
using a sequence of languages. Each level is constructed by combining parts
that are regarded as primitive at that level, and the parts constructed at
each level are used as primitives at the next level. The language used at each
level of a stratified design has primitives, means of combination, and means
of abstraction appropriate to that level of detail.

Stratified design pervades the engineering of complex systems. For example, in
computer engineering, resistors and transistors are combined (and described
using a language of analog circuits) to produce parts such as and-gates and
or-gates, which form the primitives of a language for digital-circuit design.
These parts are combined to build processors, bus structures, and memory
systems, which are in turn combined to form computers, using languages
appropriate to computer architecture. Computers are combined to form
distributed systems, using languages appropriate for describing network
interconnections, and so on.

As a tiny example of stratification, our picture language uses primitive
elements (primitive painters) that are created using a language that specifies
points and lines to provide the lists of line segments for
`segments->painter`, or the shading details for a painter like `rogers`. The
bulk of our description of the picture language focused on combining these
primitives, using geometric combiners such as `beside` and `below`. We also
worked at a higher level, regarding `beside` and `below` as primitives to be
manipulated in a language whose operations, such as `square-of-four`, capture
common patterns of combining geometric combiners.

Stratified design helps make programs robust, that is, it makes it likely that
small changes in a specification will require correspondingly small changes in
the program. For instance, suppose we wanted to change the image based on wave
shown in figure 2.9. We could work at the lowest level to change the detailed
appearance of the wave element; we could work at the middle level to change
the way `corner-split` replicates the wave; we could work at the highest level
to change how `square-limit` arranges the four copies of the corner. In
general, each level of a stratified design provides a different vocabulary for
expressing the characteristics of the system, and a different kind of ability
to change it.

## 9. square limit

Make changes to the square limit of wave shown in the figure below by working
at each of the levels described above. In particular:

![](http://mitpress.mit.edu/sicp/full-text/book/ch2-Z-G-24.gif)

a. Add some segments to the primitive `wave` painter of exercise 6, Primitive
Painters (to add a smile, for example).

b. Change the pattern constructed by `corner-split` (for example, by using
only one copy of the `up-split` and `right-split` images instead of two).

c. Modify the version of `square-limit` that uses `square-of-four` so as to
assemble the corners in a different pattern. (For example, you might make the
big Mr. Rogers look outward from each corner of the square.)

## testing

You now finished implementing the painters! Let's test your code. To test it,
type on Scheme:

    
    > (cs)
    > (ht)
    > (===your-painter=== full-frame)
    
    For example:
    > (wave full-frame)
    > ((square-limit wave 3) full-frame)
      
    (note that you cannot actually draw on js-scheme. If you are using ssh, make sure to have the -X option turned on)

