## Question B3

Define a method `take-all` for people. If given that message, a person should
`take` all the things at the current location that are not already owned by
someone.

    
    
    > (ask someperson 'take-all)
    

## Question B4: Part 1

It's unrealistic that anyone can take anything from anyone. We want to give
our characters a `strength`, and then one person can take something from
another only if the first has greater `strength` than the second.

However, we aren't going to clutter up the person class by adding a local
`strength` variable. That's because we can anticipate wanting to add lots more
attributes as we develop the program further. People can have _charisma_ or
_wisdom_; things can be _food_ or not; places can be _indoors_ or not.
Therefore, you will create a class called `basic-object` that keeps a local
variable called `properties` containing an attribute-value table like the one
that we used with `get` and `put` in Lesson 6. However, `get` and `put`
refer to a single, fixed table for all operations; in this situation we need a
separate table for every object. The file `tables.scm` contains an
implementation of the table Abstract Data Type:
    
  * Constructor: `(make-table)` returns a new, empty table.
  * Mutator: `(insert! key value table)` adds a new key-value pair to a table.
  * Selector: `(lookup key table)` returns the corresponding value, or `#f` if the key is not in the table.
    

You'll learn how tables are implemented in [SICP 3.3.3 (pp. 266-268)](https://mitpress.mit.edu/sicp/full-text/sicp/book/node63.html). For now, just take them as primitive.

You'll modify the `person`, `place` and `thing` classes so that they will inherit from `basic-object`. This object will accept a message `put` so that the following call does the right thing:
    
      
    	> (ask Brian 'put 'strength 100)
    

Also, the `basic-object` should treat any message not otherwise recognized as a request for the attribute of that name, so
    
    
    	> (ask Brian 'strength)
    	100
    

should work WITHOUT having to write an explicit `strength` method in the class
definition.

Don't forget that the property list mechanism returns `#f` if you ask for a property that isn't in the list. This means that the following call should never give an error message, even if we haven't `put` that property in that object:

    
    
    	> (ask Brian 'charisma)
    

This is important for true-or-false properties, which will automatically be `#f` (but not an error) unless we explicitly `put` a `#t` value for them.

Give people some reasonable initial strength. (They should be the same for every newly instantiated person object.) Later, they'll be able to get stronger by eating.

## Question B4: Part 2

You'll notice that the type predicate `person?` checks to see if the type of
the argument is a member of the list `'(person police thief)`. This means that
the `person?` procedure has to keep a list of all the classes that inherit
from `person`, which is a pain if we make a new subclass.

We'll take advantage of the property list to implement a better system for
type checking. If we add a method named `person?` to the person class, and
have it always return `#t`, then any object that's a type of person will
automatically inherit this method. Objects that don't inherit from person
won't find a `person?` method and won't find an entry for `person?` in their
property table, so they'll return `#f`.

Similarly, places should have a `place?` method, and things a `thing?` method.

    
    > (ask brian 'person?)
     #t

Add these type methods and change the implementation of the type predicate
procedures (at the very bottom of `adv.scm`) to this new implementation. Don't
forget to add the definition for `place?`.

The new type predicate should do the following:    
    
     > (person? brian)
     #t
     > (place? soda)
     #t
     > (thing? coffee)
     #t
     

  
Remember that `person?` should work for classes that inherit from `person`,
like `thief` and `police` (defined later). Similarly with `place?` and `thing`?

## Question B5: Part 1

In the modern era, many places allow you to get connected to the net. Define a
`hotspot` as a kind of place that allows network connectivity. Each hotspot
should have a `name` and a `password` as instantiation variables that you must
know to connect.

    
    > (define library (instantiate hotspot 'library 1234))   
    ;name of hotspot is library, password is 1234  
    

(Note: We're envisioning a per-network password, not a per-person password as
you use with AirBears.) The hotspot has a `connect` method with two arguments,
a `laptop` (a kind of thing, to be invented in a moment) and a password. If
the password is correct, and the laptop is in the hotspot, add it to a list of
connected laptops otherwise, return an error. When the laptop leaves the
hotspot, remove it from the list.

    
    > (ask library 'connect somelaptop 1234)

Hotspots also have a `surf` method with two arguments, a laptop and a text
string, such as

    
        "http://www.cs.berkeley.edu"
    

If the laptop is connected to the network, then the surf method should

    
        (system (string-append "lynx " url))
    

where URL is the text string argument (note the space after x in "lynx ").
Otherwise, return an error.

    
    > (ask library surf somelaptop "http://www.cs.berkeley.edu")

## Question B5: Part 2

Now invent the `laptop` class. A laptop has one instantiation variable, its
name.

    
    > (define somelaptop (instantiate laptop 'somelaptop)

A laptop is a thing that has two extra methods: `connect`, with a password as
argument, sends a `connect` message to the place where the laptop is. If the
password is wrong, return an error.

    
    > (ask somelaptop 'connect 1234)

A laptop also has another method, `surf`, with a URL text string as argument,
sends a `surf` message to the place where it is. Thus, whenever a laptop
enters a new hotspot, the user must ask to `connect` to that hotspot's
network; when the laptop leaves the hotspot, it must automatically be
disconnected from the network. (If it's in a place other than a hotspot, the
`surf` message won't be understood; if it's in a hotspot but not connected,
return an error).

    
    > (ask somelaptop 'surf "www.berkeley.edu")