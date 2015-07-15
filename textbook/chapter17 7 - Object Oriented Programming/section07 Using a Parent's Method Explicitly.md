## Calling the Parent

Our penguin class is getting cramped! To clean things up, lets make a child for it called `emperor-penguin`. It can do everything that a `penguin` does, except that when it eats, an `emperor-penguin` says `'(bon apetit)` before eating food. Does the following definition work?

    
    
    (define-class (emperor-penguin name)
        (parent (penguin name))
        (method (eat)
            (print '(bon apetit!))
            (ask self 'eat)))
    

![](http://www.windows2universe.org/earth/polar/images/emperor_nsf_lg.jpg)

<div class="mc">
<strong>Test Your Understanding</strong><br><br>
Let's say we define <code>napoleon</code> as follow:

<pre><code>(define napoleon (instantiate emperor-penguin 'napoleon))</code></pre>

What happens when we call <code>(ask napoleon 'eat)</code>?

<ans text="prints '(bon apetit) only" explanation=""></ans>
<ans text="prints '(bon apetit) and '(That tuna was delicious!)" explanation=""></ans>
<ans text="Loops infinitely" explanation="Remember that when we ask an object a certain message, we see if that class knows how to handle that message. If not, then we check if their parent does. Here, we ask the emperor-penguin to eat. The class accepts the message, prints '(bon apetit) and tries to find if napoleon knows how to handle the eat message. But self refers to napoleon, which is of emperor-penguin class, so we go to that class's eat message again! We print '(bon apetit) again, and loops infinitely." correct></ans>
<ans text="Throws an error" explanation=""></ans>
</div>

## Usual

The correct way to call a parent's method is to use the **usual** keyword.

    
<pre><code>(define-class (emperor-penguin name)
    (parent (penguin name))
    (method (eat)
        (print '(bon apetit!))
        <strong>(usual 'eat)))</strong></code></pre>

**usual** takes one or more argument, the first being the message, and the others being any arguments the message needs. This message and necessary arguments are then passed to the parent. In this way, an `emperor-penguin` object will refer to `penguin`'s `eat` method.

Calling usual is just like saying `(ask self ...)` with the same arguments,
except that only methods defi ned within an ancestor class (parent,
grandparent, etc.) are eligible to be used. It is an error to invoke usual
from a class that doesn't have a parent class.

## Naming Intuition

You may be thinking that `usual` is a funny name for this function. Here's the idea behind the name: We are thinking of subclasses as specializations. That is, the parent class represents some broad category of things, and the child is a specialized version. (Think of the relationship of checking-accounts to `accounts` in general.) The child object does almost everything the same way its parent does. The child has some special way to handle a few messages, different from the usual way (as the parent does it). But the child can explicitly decide to do something in the usual (parent-like) way, rather than in its own specialized way.