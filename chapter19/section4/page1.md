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

