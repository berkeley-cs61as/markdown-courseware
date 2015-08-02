To work with the ideas in the next homework problems, you should first

`(load "~cs61as/lib/concurrency.scm")`

## Exercise 1

  
Exercise [3.38](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-23.html#%_thm_3.38), [3.39, 3.40, 3.41,
3.42](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-23.html#%_thm_3.39), [3.44](http://mitpress.mit.edu/sicp
/full-text/book/book-Z-H-23.html#%_thm_3.44), [3.46,
3.48](http://mitpress.mit.edu/sicp/full-
text/book/book-Z-H-23.html#%_thm_3.46), of Abelson & Sussman

## Exercise 2: Chaining Mapreduce

Write the function `real-most-frequent` that accepts a list of key-value pairs
where the key is the name of the file, and the values are lines from that file
(just like our all-songs example) . Our output is again, a list of **single**
key-value pair. You may want to reuse any functions we have defined so far in
the lesson.
    
    >(real-most-frequent all-songs)
    ((i . 4))

## Exercise 3: Mapreduce with Streams

Our current mapreduce works with lists. Mapreduce in real life works with
really large datasets: so large that a list won't be able to contain them. One
way to solve this is to have a mapreduce that works on streams instead of
list. You can find our mapreduce version that work on streams
[here](/static/streammapreduce.scm). or at
"~cs61as/lib/mapreduce/streammapreduce.scm"

What changed? Our map, sort-into-buckets, and filter works with streams now.
What do you as a user need to provide? The mapper and reducer, just like what
you did previously. How do the mappers and reducers changed? **they don't**.
The behavior of mapper and reducer doesn't change. You can load the file and
try `(mapreduce mapper reducer 0 all-songs)` where the mapper and reducer are
ones you've defined in the lessons. They would work the same way. The only
difference is that if all-songs is large, our previous version will crash and
brun whereas our stream version would still be able to process it

## Exercise 4: Do You Want to be the Very Best?

You have access to a stream of all 744 pokemon data
[here](/static/pokemon_data) and "~cs61as/lib/mapreduce/pokemon_data".
`streammapreduce.scm` should load it automatically and define the variable
"data" as your input. The key is the pokemon national number, the value is a
list of regional number, name, name (yes it appears twice), and the rest are
types that they have. For example the first element is `(1 1 bulbasaur
bulbasaur grass poison)` so it has the national number 1, regional number of
1, names bulbasaur, and has the types 'grass' and 'poison'. A Pokemon can
either have 1 or 2 types. Here is an example of one that only has one type:
`(4 4 charmander charmander fire)`. You can take a look at the input by typing
`(ss data)` in the interpreter after loading the files.

Define the mapper, reducer and base-case such that calling mapreduce with
`(mapreduce mapper reducer base-case data)` would return a list of key-value
pairs where the keys are different types, and the values represent how many
times a pokemon of that type appears in the dataset. The final result should
yield the following (in any order):

    
    
    ((grass . 86) (dragon . 39) (normal . 99) (flying . 93) (poison . 59) (ice . 35) (fire . 58) (ghost . 37) (psychic . 77) (electric . 47) (water . 124) (fairy . 35) (bug . 70) (steel . 42) (ground . 62) (rock . 54) (fighting . 45) (dark . 44))
    
## Submit Your Homework

