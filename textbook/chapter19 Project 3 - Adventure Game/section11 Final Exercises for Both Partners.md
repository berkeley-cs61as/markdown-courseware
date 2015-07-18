## Question 9

Make the necessary changes so that when a `police` asks to `buy` some food, the restaurant does not charge them any money. (This makes the game more realistic...?)

(Note that `pay-money` and `get-money` should behave the same way. Do not change their implementations.)

    
    
    > (ask somepoliceman 'money)
    100
    > (ask somepoliceman 'buy 'pasta)
    > (ask somepoliceman 'money)
    100
    

## Extra for Experts (Optional)

As you can imagine, this is a truly open-ended project. If you have the time and inclination, you can populate your world with new kinds of people (e.g., college students, children, fire-resistant dragon queens), places (Jacobs Hall, libraries, death match fighting pits), and especially things (telephones, books, dragon glass swords). Oh, the possibilities!

For your enjoyment, we have developed a procedure that creates a labyrinth (a maze) that you can explore. To do so, load the file `~cs61as/lib/labyrinth.scm`. (Note: `labyrinth.scm` may need some modification to work with the procedures you developed in part two of the project.)

Legend has it that there is a vast series of rooms underneath Sproul Plaza. These rooms are littered with food of bygone days and quite a few theives. You can find the secret passage down in Sproul Plaza.

You may want to modify `fancy-move-loop` so that you can look around in nearby rooms before entering so that you can avoid thieves. You might also want your character to maintain a list of rooms visited on its property list so you can find your way back to the earth's surface.