## Question A6

`Adv.scm` includes a definition of the class `thief`, a subclass of person. A
`thief` is a character who tries to steal food from other people. Of course,
Berkeley can not tolerate this behavior for long. Your job is to define a
`police` class; `police` objects catch `thieves` and send them directly to
`jail`. To do this you will need to understand how `thiefs` work.

Since a `thief` is a kind of `person`, whenever another `person` enters the
place where the `thief` is, the `thief` gets a `notice` message from the
place. When the `thief` notices a new person, he does one of two things,
depending on the state of his internal `behavior` variable. If this variable
is set to `steal`, the thief looks around to see if there is any food at the
place. If there is food, the thief takes the food from its current possessor
and sets his behavior to `run`. When the thief's behavior is `run`, he moves
to a new random place whenever he `notice`s someone entering his current
location. The `run` behavior makes it hard to catch a thief.

Notice that a `thief` object delegates many messages to its `person` object.

## Question A6 Part 1

To help the police do their work, you will need to create a place called
`jail(`i.e. a` jail` is an instantiation of `place`). Jail has no exits.
Moreover, you will need to create a method for persons and thieves called go-
directly-to. Go-directly-to does not require that the new-place be adjacent to
the current-place. So by calling (ask thief 'go-directly-to jail) the police
can send the thief to jail no matter where the thief currently is located,
assuming the variable thief is bound to the thief being apprehended.

## Question A6 Part 2

Thieves sometimes try to leave their place in a randomly chosen direction.
This, it turns out, won't work if there are no exits from that place -- for
example, the `jail`. Modify the` thief` class so that a `thief` won't try to
leave a place with no exits.

## Combining Work

Before you move on, you need to get your partner to explain problem B6 and its
solution. You will also need to explain problem A6 and its solution to your
partner.

## Question A7 Part 1

We are now going to invent restaurant objects. People will interact with the
restaurants by buying food there. First we have to make it possible for people
to buy stuff. Give` person` objects a` money` property, which is a number,
saying how many dollars they have. Note that `money` is not an object. We
implement it as a number because, unlike the case of objects such as chairs
and potstickers, a person needs to be able to spend _some_ money without
giving up all of it. In principle we could have objects like `quarter` and
`dollar-bill`, but this would make the change-making process complicated for
no good reason.

To make life simple, we'll have every` person` start out with $100. (We should
really start people with no money, and invent banks and jobs and so on, but we
won't.) Create two methods for people`, get-money` and` pay-money`, each of
which takes a number as argument and updates the person's `money` value
appropriately.` Pay-money `must return **true** or **false** depending on
whether the person had enough money.

    
    
    >(ask brian 'money)
    100
    >(ask brian 'get-money 20) ;increases money
    >(ask brian 'money)
    120
    >(ask brian 'pay-money 30) ;decreases money. Returns #t if has enough money  
    #t  
    >(ask brian 'money)
    90
    

## Question A7 Part 2

Another problem with the adventure game is that Noah's only has one bagel.
Once someone has taken that bagel, they're out of business. The same goes with
other restaurants.

To fix this, we're going to invent a new kind of place, called a` restaurant.`
(That is,  `restaurant` is a subclass of `place`.) Each `restaurant` serves
only one kind of food. (This is a simplification, of course, and it's easy to
see how we might extend the project to allow lists of kinds of food.) When a
`restaurant` is instantiated, it should have two extra arguments, besides the
ones that all places have: the class of food objects that this restaurant
sells, and the price of one item of this type:

    
       > (define-class (pasta) (parent (food ...)) ...)
    
       > (define somerestraurant (instantiate restaurant 'somerestaurant pasta 7))
    

Notice that the argument to the restaurant is a **_class_**, not a particular
bagel (instance). Here is an example of the **pasta** food class. Your partner
should have defined some example of food classes as part of B6.

    
    >(define pesto-pasta (instantiate pasta))
    >(ask pesto-pasta 'calories)
    150  
    

`Restaurants` should have two methods. The` menu` method returns a list
containing the name and price of the food that the restaurant sells. The`
sell` method takes two arguments, the `person` who wants to buy something and
the **name** of the food that the person wants. The` sell` method must first
check that the restaurant actually sells the right kind of food. If so, it
should` ask` the buyer to` pay-money` in the appropriate amount. If that
succeeds, the method should **instantiate the food class** and return the
**new food object**. The method should return` #f` if the person can't buy the
food.

Here are some examples:

    
    >(ask somerestaurant 'menu)
    (pasta 7)
    >(ask somerestaurant 'sell someperson 'pasta) ;note that pasta is the name
    

## Question A8

Now we need a` buy` method for people. It should take as argument the **name**
of the food we want to buy:

`>(ask Brian 'buy 'bagel)`

The method must send a` sell` message to the restaurant. If this succeeds
(that is, if the value returned from the` sell` method is an** object** rather
than` #f`) the new food should be added to the person's possessions. If the
person can't buy, return an **error.**

