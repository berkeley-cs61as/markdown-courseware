## Question A3

You will notice that whenever a person goes to a new place, the place gets an
`'enter` message. In addition, the place the person previously inhabited gets
an `'exit` message. When the place gets the message, it calls each procedure
on its list of `entry-procedures` or `exit-procedures` as appropriate. Places
have the following methods defined for manipulating these lists of procedures:
`add-entry-procedure, add-exit-procedure, remove-entry-procedure, remove-exit-
procedure, clear-all-procs`. You can read their definitions in the code.

Sproul Hall has a particularly obnoxious exit procedure attached to it. Fix
`sproul-hall-exit` so that it counts how many times it gets called, and stops
being obnoxious after the third time.

Remember that the `exit-procs` list contains procedures, not names of
procedures! It's not good enough to redefine `sproul-hall-exit`, since Sproul
Hall's list of exit procedures still contains the old procedure. The best
thing to do is just to load `adv-world.scm` again, which will define a new
Sproul Hall and add the new exit procedure.

## Question A4 -- Part 1

We've provided people with the ability to say something using the messages
`'talk` and `'set-talk`. As you may have noticed, some people around this
campus start talking whenever anyone walks by. We want to simulate this
behavior. In any such interaction there are two people involved: the one who
was already at the place (hereafter called the `talker`) and the one who is
just entering the place (the `listener`). We have already provided a mechanism
so that the `listener` sends an `enter` message to the place when entering.
Also, each person is ready to accept a `notice` message, meaning that the
person should notice that someone new has come. The `talker` should get a
`notice` message, and will then talk, because we've made a person's `notice`
method send itself a `talk` message. (Later we'll see that some special kinds
of people have different `notice` methods.)

Your job is to modify the `enter` method for places, so that in addition to
what that method already does, it sends a `notice` message to each person in
that place **other than the person who is entering.** The `notice` message
should have the newly-entered person as an argument. (You won't do anything
with that argument now, but you'll need it later.)

Add the following to adv-world:

    
    (define singer (instantiate person 'rick sproul-plaza))
    
    (ask singer 'set-talk "My funny valentine, sweet comic valentine")
    
    (define preacher (instantiate person 'preacher sproul-plaza))
    
    (ask preacher 'set-talk "Praise the Lord")
    
    (define street-person (instantiate person 'harry telegraph-ave))
    
    (ask street-person 'set-talk "Brother, can you spare a buck")
      
    Try walking around to sproul-plaza and telegraph-ave to see if the messages are triggered
    

YOU MUST INCLUDE A TRANSCRIPT IN WHICH YOUR CHARACTER WALKS AROUND AND
TRIGGERS THESE MESSAGES.

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
    

## Question A5

Walking around is great, but some people commute from far away, so they need
to park their vehicles in garages. A vehicle is just a `thing`, but you'll
have to invent a special kind of place called a `garage`. Garages have two
methods (besides the ones all places have): `park` and `unpark`. You'll also
need a special kind of `thing` called a `ticket`; what's special about it is
that it has a `number` as an instantiation variable.

The `park` method takes a vehicle (a `thing`) as its argument. First check to
be sure that the vehicle is actually in the garage. (The person who possesses
the vehicle will enter the garage, then ask to park it, so the vehicle should
have entered the garage along with the person before the `park` message is
sent.) Then generate a `ticket` with a unique serial number. (The counter for
serial numbers should be shared among all garages, so that we don't get in
trouble later trying to `unpark` a vehicle from one garage that was parked in
a different garage.) Every ticket should have the name `ticket`.

You'll associate the ticket number with the vehicle in a key-value table like
the one that we used with `get` and `put` in 2.3.3. However, `get` and `put`
refer to a single, fixed table for all operations; in this situation we need a
separate table for every garage. The file `tables.scm` contains an
implementation of the table Abstract Data Type:

    
    constructor: (make-table) returns a new, empty table.
    
    mutator: (insert! key value table) adds a new key-value pair to a table.
    
    selector: (lookup key table) returns the corresponding value, or #f if
                         the key is not in the table.
    

You'll learn how tables are implemented in SICP 3.3.3 (pp. 266-268). For now,
just take them as primitive.

Make a table entry with the ticket number as the key, and the vehicle as the
value. Then ask the vehicle's owner to lose the vehicle and take the ticket.

The `unpark` method takes a ticket as argument. First make sure the object you
got is actually a ticket (by checking the name). Then look up the ticket
number in the garage's table. If you find a vehicle, ask the ticket's owner to
lose the ticket and take the vehicle. Also, insert `#f` in the table for that
ticket number, so that people can't unpark the vehicle twice.

A real-life garage would have a limited capacity, and would charge money for
parking, but to simplify the project you don't have to simulate those aspects
of garages.

**Be sure not to name anything a "car"! This will mess up everything!**

  * A ticket only has one instantiation variable, a serial number.   
`(instantiate ticket 120)`

  * A ticket is a thing with the name 'ticket
  * A garage takes one instantiation variable, its name.   
`(instantiate garage 'soda-garage)`

  * Do not define a new class for vehicles. You can assume that park is called with the correct argument
  * Parking a vehicle that is not owned by anyone, should return an error
  * Unparking a vehicle that is not parked should return an error

