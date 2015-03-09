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

