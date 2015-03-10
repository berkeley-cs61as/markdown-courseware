## Question B8

Now we want to reorganize` take` so that it looks to see who previously
possesses the desired object. If its possessor is` 'no-one`, go ahead and take
it as always. Otherwise, invoke

    
    >(ask thing 'MAY-TAKE? receiver)
    

The` may-take?` method for a thing that belongs to someone should compare the
strength of its owner with the strength of the requesting person to decide
whether or not it can be taken. If the receiver has the same strength as the
holder, the receiver may take the object. If the thing does not has a holder,
the receiver may take the object.

The method should return**` #f`** if the person may not take the thing, or**
the thing itself** if the person may take it. This is a little more
complicated than necessary right now, but we are planning ahead for a
situation in which, for example, an object might want to make a clone of
itself for a person to take.

Note the flurry of message-passing going on here. We send a message to the
taker. It sends a message to the thing, which sends messages to two people to
find out their strengths.

