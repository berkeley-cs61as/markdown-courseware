## Question B6: Part 1

The way we're having people take food from restaurants is unrealistic in several ways. Our overall goal this week is to fix that. As a first step, you are going to create a `food` class. We will give things that are food two properties, an `edible?` property and a `calories` property. `edible?` will have the value `#t` if the object is a food. If a `person` eats some `food`, the `food`'s `calories` are added to the person's `strength`.

(Remember that the `edible?` property will automatically be `false` for objects other than food, because of the way properties were implemented in Question B4. You don't have to go around telling all the other stuff not to be edible explicitly.)

Write a definition of the `food` class that uses `thing` as the parent class. It should return `#t` when you send it an `edible?` message, and it should correctly respond to a `calories` message.

Replace the procedure named `edible?` in the original `adv.scm` with a new version that takes advantage of the mechanism you've created, instead of relying on a built-in list of types of food.
    
    
    > (define pesto-pasta (instantiate food 'pasta 150))
    ;name is pesto-pasta, calories is 150
    > (ask pesto-pasta 'calories)
    150
    > (ask pesto-pasta 'edible?)
    #t
    > (edible? pesto-pasta)
    #t
    

## Question B6: Part 2

Now that you have the `food` class, invent some child classes for particular kinds of food. For example, make a `pasta` class that inherits from `food`. `pasta` should not have any instantiation variable. Give the `pasta` a **class-variable** called `name` whose value is the word pasta. (We'll need this later when we invent `restaurant` objects.)

Using your pasta class, it should now be possible to instantiate the pesto-pasta above as follows.

    
    > (define pesto-pasta (instantiate pasta))
    > (ask pesto-pasta 'calories)
    150
    

## Question B6: Part 3

Make an `eat` method for people. Your `eat` method should look at your possessions and filter for all the ones that are edible. It should then add the `calories` value of the foods to your `strength`. Then it should make the foods disappear (no longer be your possessions and no longer be at your location).

## Combining Work

Before moving on, get your partner to explain Question A6 and its solution. Also, explain Question B6 and its solution to your partner.

## Question B7

Your job is to define the `police` class. When the police notices a new person entering where he is, the police checks to see if that person is a thief. If the person is a thief the police says "Crime Does Not Pay," then takes away all the thief's possessions and sends the thief directly to jail.

Give thieves and police default strengths. Thieves should start out stronger than persons, but police should be stronger than thieves. Of course, if you eat lots you should be able to build up enough `strength` to take food away from a thief.

Please test your code and turn in a transcript that shows the thief stealing your food, you chasing the thief and the police catching the thief. In case you haven't noticed, we've put a thief in Sproul Plaza to help test your code.
    
    
    > (define somepolice (instantiate police 'grammarpolice soda))
    

## Question B8

Now we want to reorganize `take` so that it looks to see who previously possesses the desired object. If its possessor is` 'no-one`, go ahead and take it as always. Otherwise, invoke:

    
    > (ask thing 'may-take? receiver)
    

The `may-take?` method for a thing that belongs to someone should compare the strength of its owner with the strength of the requesting person to decide whether or not it can be taken. If the receiver has the same strength as the holder, the receiver may take the object. If the thing does not has a holder, the receiver may take the object.

The method should return **`#f`** if the person may not take the thing, or **the thing itself** if the person may take it. This is a little more complicated than necessary right now, but we are planning ahead for a situation in which, for example, an object might want to make a clone of itself for a person to take.

Note the flurry of message-passing going on here. We send a message to the
taker. It sends a message to the thing, which sends messages to two people to
find out their strengths.

