##  Question 8

**Make sure you are completely done with part 7 before attempting this part!**

Add the STEP and UNSTEP primitive commands. They take a word as argument,
which must be the name of a user-defined procedure. STEP sets to true, and
UNSTEP sets to false, a flag inside the procedure structure (you'll have to
add this to the procedure ADT). When a defined procedure is called, if the
stepping flag is set, Logo should print each line of the procedure definition,
followed by a ">>> " prompt, before evaluating that line, and then wait for
the user to enter a line (it'll usually be an empty line, but in any case you
can ignore what the user types; you're just waiting for him/her to type it).
Then run the line from the procedure. For example:

`? to garply`

`-> print "hello`

`-> print "goodbye`

`-> end`

`? garply`

`hello`

`goodbye`

`? step "garply`

`? garply`

`print "hello>>> [user hits return/enter key]`

`hello`

`print "goodbye>>>`

`goodbye`

`? unstep "garply` `? garply` `hello` `goodbye` `?`

This is a Logo debugging assistance feature. Try it on a recursive procedure!

**When your partner is done with their part 8, merge your code and move on to part 9! Part 9 cannot be attempted until both partners are done with part 8.**

