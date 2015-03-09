## Question A8

Now we need a` buy` method for people. It should take as argument the **name**
of the food we want to buy:

`>(ask Brian 'buy 'bagel)`

The method must send a` sell` message to the restaurant. If this succeeds
(that is, if the value returned from the` sell` method is an** object** rather
than` #f`) the new food should be added to the person's possessions. If the
person can't buy, return an **error.**

