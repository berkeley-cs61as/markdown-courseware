## Question 9

Combine the two partners' work. For example, both partners have created new
methods for the` person` class. Both partners have done work involving
strengths of kinds of people; make sure they work together.

Now make it so that when a` police` person asks to` buy` some food the
restaurant doesn't charge him or her any money. (This makes the game more
realistic...)

(Note that pay-money and get-money should behave the same)

    
    
    >(ask somepoliceman 'buy 'pasta)
    

## Optional Extras

As you can imagine, this is a truly open-ended project. If you have the time
and inclination, you can populate your world with new kinds of people (e.g.,
punk-rockers), places (Gilman-St), and especially things (magic wands, beer,
gold pieces, cars looking for parking places...).

For your enjoyment we have developed a procedure that creates a labyrinth (a
maze) that you can explore. To do so, load the file
`~cs61as/lib/labyrinth.scm`. [Note: `labyrinth.scm` may need some modification
to work with the procedures you developed in part two of the project.]

Legend has it that there is a vast series of rooms underneath Sproul Plaza.
These rooms are littered with food of bygone days and quite a few theives. You
can find the secret passage down in Sproul Plaza.

You may want to modify` fancy-move-loop` so that you can look around in nearby
rooms before entering so that you can avoid thieves. You might also want your
character to maintain a list of rooms visited on its property list so you can
find your way back to the earth's surface.

## Submitting

You need to submit your modified `adv.scm, adv-world.scm `files and your
transcript. This should include solutions to Questions 1-9 **for both
partners**. Make sure you have added comments to your code highlighting all of
the changes you've made.

Also, make sure you clearly indicate at the top of adv.scm which partner is
Person A and which is Person B.

Only one person should submit. When you submit, it will prompt you for your
partner's login. (If it prompts you to put another log-in, type "." and enter)

To ensure submission went well, both partners should type

    
    glookup -t
    

into their terminal. This command gives you a list of all submitted
assignments, as well as when they were submitted.

Remember: ONLY ONE PERSON SHOULD SUBMIT!

If you need to re-submit your project for any reason, have the same person as
before submit the file. If this is not possible, send your reader an email as
a heads-up explaining the situation.

