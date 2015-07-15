## EnvDraw

EnvDraw is a cool program that you can run on your class account to help you
draw environment diagrams. To use it:

  1. Type `envdraw` into a terminal. (If this doesn't work, first SSH into torus, and then type the command.) This command should then open an STk interpreter.
  2. At the interpreter, type `(envdraw)`.
  3. You should see a new EnvDraw window open. At the `EnvDraw>` prompt, try defining the `square` function. Then, look at the EnvDraw window and see what happens!

## Overview

Now you're going to start drawing your own environment diagrams! We'll start
from the basics and gradually build on them. Literally all of the rules you
need to draw these diagrams are in the previous section. Make sure you know
all of them by the time you're done with this lesson.

All of the example environment diagrams we show you in this section are taken
from the EnvDraw program.

## Define

Let's start by defining a variable in Scheme and looking at the corresponding
environment diagram. Specifically, we'll try drawing the diagram for:

    
    (define x 3)
    

The first step is to always draw the global environment. Make sure to label
it! Next, we need to figure out how to handle the `define`. By looking at the
rules in the previous section, you should learn that `define` adds a new
binding to the current frame. Let's draw it out:

![](/static/define_x_3.PNG)

That's all there is to it! Simply write "x" with an arrow pointing to 3, all
within the global environment. (Note: you don't have to write "[other bindings]" in your own environment diagrams for this class. EnvDraw does this for completeness.)

Now we're going to move onto defining procedures. What happens when you type
the following code into a STk interpreter? We'll continue off of our diagram from earlier.

    
    (define (square x) (* x x))
    

The first thing we're going to do is change the above code so it uses a
lambda:

    
    (define square (lambda (x) (* x x)))
    

Notice that this expression now has all of the same basic parts as `(define x
3)`. So we follow the exact same procedure: write "square" in the global frame
and draw an arrow pointing to the lambda. We draw a lambda as a double-bubble.
The first bubble points to the arguments and the body. The second bubble
points to the defining environment, or the current environment at the time the
lambda is seen. This is how your diagram should now look.

![](/static/define_square.PNG)

Now you're done! To recap, you first need to draw the lambda. Make the first
bubble point to the args and body, and the second point to the defining
environment. Next, simply write "square" in the global environment and make it
point to the lambda.

In the next section, we'll cover how to actually call the `square` function we
just defined.

There is one very important point we're ignoring in these examples: `define`
doesn't _always_ add things to the global environment. Instead, it adds it to
the _current frame_ (which happens to be the global environment in the cases
above). We'll walk you through how to figure out what the current frame is in
a later section.

## Applying Primitive Procedures

Now, let's draw the environment diagram for:

    
    
    (define y (+ 3 4))
    

The difference from the previous example is that we must first apply the `+`
procedure to `3` and `4` before we can assign the value of `y`. You can assume that all primitive procedures are applied by magic. Nothing needs to be drawn out for them. Thus, the full environment diagram would simply look like:

![](/static/define_y_3_4.PNG)

## Applying User-Defined Procedures

Let's say we now want to actually call the `square` function we defined earlier.
We'll call it with the code:

    
    (square 5)
    

To call a user-defined procedure, we follow the following steps:

  1. Create a frame with the formal parameters of the procedure bound to the actual argument values.

![](/static/square_5_a.png)

  2. Extend the procedure's defining environment with this new frame.

![](/static/square_5_b.png)

  3. Evaluate the procedure body, using the new frame as the current frame.

The last step doesn't actually involve changing the environment diagram.
Instead, this is when we finally find the value of the call. To evaluate the
body of square, we must first figure out the value of `x`. We always use the
_first available_ binding for a variable. This means we look at the binding of
`x -> 5` in our current frame, rather than the binding of `x -> 3` in the global
frame. Once we've figured out the value of `x`, we multiply it to itself
(remember, you can just assume this is done by magic). And now we're done!
We've multiplied `5` by itself, yielding the answer of `25`.

Remember, only compound procedure invocation creates a new frame!

## Atomic Expressions

The trick to evaluating atomic expressions (such as finding the value of a
symbol) relies on figuring out which frame is the current frame. Before we get
into that, remember that the rules of evaluating atomic expressions are:

  1. Numbers, strings, #t, and #f are self-evaluating.
  2. If the expression is a symbol, ﬁnd the ﬁrst available binding. (That is, look in the current frame; if not found there, look in the frame "behind" the current frame; and so on until the global frame is reached.)

All of the hard work is in case 2 above. Recall our environment diagram from
the last section:

![](/static/square_5_b.png)

Remember that a new frame is only drawn when invoking a **user-defined procedure**. Thus, the current frame can only differ from the global environment when you are within the scope of another function. While this is a super important point, don't sweat it too much for now. Make sure you understand all of the examples thus far. We'll introduce more complicated examples further in the lesson.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Recall that our environment diagram so far looks like this:

<img src="/static/square_5_b.png">

If I now type <code>x</code> into the interpreter, what will its value be?
<ans text="3" explanation="" correct></ans>
<ans text="5" explanation="When you type x directly into the interpreter, you are in the global environment. This means the current frame is the global frame. Scheme finds the value of x by checking the global frame for some binding to x. In this case, we found a value for x and thus return its value of 3."></ans>
<br><br>

I now improperly define the function <code>cube</code> as follows: 

<pre><code>(define (cube x) (* y y y))</code></pre>

First, draw the environment diagram corresponding to this definition. Add this definition on to the environment diagram we've drawn so far.

<ans text="I promise I've tried drawing the diagram" explanation="Okay, I trust you. Now try it in EnvDraw." correct></ans>
<br><br>

Draw the resulting environment diagram from evaluating the code: 

<pre><code>(cube 2)</code></pre>

What does it output?

<ans text="I promise I've tried drawing the diagram" explanation="Try it in EnvDraw." correct></ans>
</div>

## Freeloading Frames

At this point, our environment diagram now has three frames, the global frame, E1, and E2. E1 and E2 were created by calls to `square` and `cube`, respectively. However, once these functions return (or finish), the frames E1 and E2 we've created are useless! They are no longer reachable and their bindings no longer matter.

This isn't always the case. In the next sections we'll go over some code that makes these frames useful much after the initial procedure call.

## Using `set!`

Now let's look at how to handle `set!`. You may recall that `set!` changes the
_first available_ binding. Remember that we find the first available binding
by looking in the current frame, and then looking in the frames "behind" that
frame.

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Let's try it out! Starting fresh, draw the environment diagram that corresponds to the following lines of code:

<pre><code>(define x 3)
(define (change x n)
  (set! x n))
(change x 5)</code></pre>

<ans text="I promise I've tried drawing the diagram" explanation="" correct></ans>
<br><br>
What is the value of <code>x</code>?

<ans text="ERROR" explanation=""></ans>
<ans text="3" explanation="Remember that set! changes the value of the first available binding. This means the value of x is changed in E1, not the global environment! Thus, when you type x into the interpreter, you'll get the old value of x in the global frame, 3. Look at the environment diagram above and this should make sense." correct></ans>
<ans text="5" explanation=""></ans>
<br><br>

How can you fix the <code>change</code> procedure so the value of <code>x</code> in the global environment changes? Indicate ALL possible fixes.

<ans text="Change (define (change x n) ...) to (define (change y n) ...)" explanation="" correct></ans>
<ans text="Change (set! x n) to (set! 'x n)" explanation=""></ans>
<ans text="Change (define (change x n) ...) to (define (change n) ...)" explanation="Try drawing out the environment diagrams! In the first and third options, when we try (set! x n), we will only find a binding for x in the global frame. Thus, the set! will change the binding of x in the global frame, the first available binding. 

The second option will simply error." correct></ans>
<ans text="Not possible" explanation=""></ans>
</div>

## Using `let`

Using `let` tends to cause a lot of students trouble. But don't despair! Whenever you're having troubles with `let`, remember these simple rules:

  1. Convert the `let` into a lambda statement plus invocation.

For example, you can rewrite

    
    (let ((x 7)
          (y 10))
        (+ x y))

as

    
    ((lambda (x y) (+ x y)) 7 10)

  2. Draw the corresponding `lambda`. Remember, a `lambda` is just a double-bubble with the correct arrows.
  3. Call the `lambda` with the proper arguments. Remember, this includes drawing a new frame and binding the formal parameters to the actual argument values.

If you can remember these simple rules, you'll have no trouble at all!

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Draw the environment diagram for the following code:

<pre><code>(let ((x 7)
      ( y 10))
    (+ x y))</code></pre>

<ans text="I promise I've tried drawing the diagram" explanation="Remember to try it out on EnvDraw." correct></ans>
<br><br>
Now let's try something more complex. Draw the resulting environment diagram for the following code:

<pre><code>(define (make-withdraw initial-amount)
    (let ((balance initial-amount))
        (lambda (amount)
            (if (>= balance amount)
                (begin (set! balance (- balance amount))
                       balance)
                "Insufficient funds"))))
(define W1 (make-withdraw 100))
(W1 50)</code></pre>

<ans text="I promise I've tried drawing the diagram" explanation="" correct></ans>
</div>

## Takeaways

At this point, you know everything you need to draw any environment diagram,
no matter how complicated! As we go through problems in the future, don't
forget the basics! Even the most complicated pieces of code can be boiled down
into simple rules.

If there is even a single thing covered so far that you don't understand, ask
for help! Environment diagrams is one of those topics that a lot of students
find difficult.

## What's Next?

Using our new-found knowledge of the environment model of evaluation, in the
next section we're going to walk through how to implement OOP by clever-ly
using lambdas and lets.

## For the Quiz

When you are taking Quiz 8, you are allowed to have a copy of the [Environment Diagram Rules](https://docs.google.com/document/d/1GbRF9rB9TtFbf--89MBDEHzygF2E5_E2wpLBh4rb4Z4/edit) **in addition to** your double-sided cheat-sheet.