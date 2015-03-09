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
    

