## Question A4 -- Part 2

So far the program assumes that anyone can go anywhere they want. In real
life, many places have locked doors.

Invent a `may-enter?` message for places that takes a person as an argument
and always returns `#t`. Then invent a `locked-place` class in which the `may-
enter?` method returns #t if the place is unlocked, or #f if it's locked. (It
should initially be locked.) The `locked-place` class must also have an
`unlock` message. For simplicity, write this method with no arguments and have
it always succeed. In a real game, we would also invent keys, and a mechanism
requiring that the person have the correct key in order to unlock the door.
(That's why `may-enter?` takes the person as an argument.)

Modify the `person` class so that it checks for permission to enter before
moving from one place to another. If a person cannot enter, return an error.
Then create a locked place and test it out.

**Note:** locked-place should take one instantiation variable, its name.
    
    
    (define warehouse (instantiate locked-place 'warehouse))
    

