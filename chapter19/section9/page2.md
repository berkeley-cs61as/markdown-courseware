## Subclass

Now that you have the` food` class, invent some child classes for particular
kinds of food. For example, make a `pasta` class that inherits from` food`.
`pasta` should not have any instantiation variable. Give the `pasta` a
**class-variable** called `name` whose value is the word pasta. (We'll need
this later when we invent` restaurant` objects.)

Using your pasta class, it should now be possible to instantiate the pesto-
pasta above as follows.

    
    >(define pesto-pasta (instantiate pasta))
    >(ask pesto-pasta 'calories)
    150
    

