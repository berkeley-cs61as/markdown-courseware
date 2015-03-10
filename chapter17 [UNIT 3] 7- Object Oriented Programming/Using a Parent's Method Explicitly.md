## Usual

The correct way to call a parent's method is to use the **usual** keyword.

    
    (define-class (emperor-penguin name)
        (parent (penguin name))
        (method (eat)
            (print '(bon apetit!))
    **        (usual 'eat)))
    **

**usual** takes one or more argument, the first being the message, and the others being any arguments the message needs. This message and necessary arguments are then passed to the parent. In this way, an `emperor-penguin` object will refer to `penguin`'s `eat` method.

Calling usual is just like saying` (ask self ...)` with the same arguments,
except that only methods defi ned within an ancestor class (parent,
grandparent, etc.) are eligible to be used. It is an error to invoke usual
from a class that doesn't have a parent class.

## Naming Intuition

You may be thinking that `usual` is a funny name for this function. Here's the
idea behind the name: We are thinking of subclasses as specializations. That
is, the parent class represents some broad category of things, and the child
is a specialized version. (Think of the relationship of checking-accounts to
`accounts` in general.) The child object does almost everything the same way
its parent does. The child has some special way to handle a few messages, di
fferent from the usual way (as the parent does it). But the child can
explicitly decide to do something in the usual (parent-like) way, rather than
in its own specialized way.

