Type the following into the terminal to copy the template file to the current directory (note the period at the end):

```
cp ~cs61as/autograder/templates/hw7.scm .
```

Or you can download it from [here](http://inst.eecs.berkeley.edu/~cs61as/templates/hw7.scm).

## Exercise 1

  
Modify the `person` class given in the template to add a `repeat` method, which repeats the last thing said. For example:

	> (define brian (instantiate person 'brian))
	brian 

	> (ask brian 'repeat)
	() 

	> (ask brian 'say '(hello))
	(hello) 

	> (ask brian 'repeat)
	(hello) 

	> (ask brian 'greet)
	(hello my name is brian) 

	> (ask brian 'repeat)
	(hello my name is brian) 

	> (ask brian 'ask '(close the door))
	(would you please close the door) 

	> (ask brian 'repeat)
	(would you please close the door) 


## Exercise 2

  
This exercise introduces you to `usual`.

Suppose that we want to define a class called `double-talker` to represent people that always say things twice. For example, take a look at the following dialog.

	> (define mike (instantiate double-talker 'mike))
	mike 

	> (ask mike 'say '(hello))
	(hello hello) 

	> (ask mike 'say '(the sky is falling))
	(the sky is falling the sky is falling) 


Consider the following three definitions for the double-talker class:

	(define-class (double-talker name)
		(parent (person name))
		(method (say stuff) (se (usual 'say stuff) (ask self 'repeat))) ) 

	(define-class (double-talker name)
		(parent (person name))
		(method (say stuff) (se stuff stuff)) ) 

	(define-class (double-talker name)
		(parent (person name))
		(method (say stuff) (usual 'say (se stuff stuff))) ) 

Determine which of these definitions work as intended. Determine also for which messages the three versions would respond differently.

## Exercise 3
  
For a statistical project you need to compute lots of random numbers in various ranges. (Recall that `(random 10)` returns a random number between 0 and 9.) Also, you need to keep track of how many random numbers are computed in each range. You decide to use object-oriented programming. Objects of the class random-generator will accept two messages: `number` and `count`. The message `number` means "give me a random number in your range" while `count` means "how many number requests have you had?" The class has an instantiation argument that specifies the range of random numbers for this object, so:

	(define r10 (instantiate random-generator 10))

will create an object such that `(ask r10 'number)` will return a random number between 0 and 9, while `(ask r10 'count)` will return the number of random numbers `r10` has created.

## Exercise 4
  
Define the class `coke-machine`. The instantiation arguments for a `coke-machine` are the number of Cokes that can fit in the machine and the price (in cents) of a Coke. For example,

	(define my-machine (instantiate coke-machine 80 70))

creates a machine that can hold 80 Cokes and sells them for 70 cents each. `coke-machine` objects must accept the
following messages:

* `(ask my-machine 'deposit 25)` means deposit 25 cents. You can deposit several coins and the machine should remember the total.
* `(ask my-machine 'coke)` means push the button for a Coke. The machine then either 1) prints "Not enough money", 2) prints "Machine empty", or 3) returns the amount of change you get. The error messages should be printed using `display` (for example, `(display "Machine empty")`).
* `(ask my-machine 'fill 60)` means add 60 Cokes to the machine.

Here's an example:

	> (ask my-machine 'fill 60)
	> (ask my-machine 'deposit 25)
	> (ask my-machine 'coke)
	"Not enough money"

	> (ask my-machine 'deposit 25) ;; Now there's 50 cents in there.
	> (ask my-machine 'deposit 25) ;; Now there's 75 cents.
	> (ask my-machine 'coke)
	5 ;; return val is 5 cents change.

You may assume that a Coke machine has an infinite supply of change and initially contains zero Cokes.

## Exercise 5

  
We are going to use objects to represent decks of cards. You are given the
list `ordered-deck` containing 52 cards in standard order:

	(define ordered-deck '(AH 2H 3H ... QH KH AS 2S ... QC KC))

You are also given a function to shuffle the elements of a list:

	(define (shuffle deck)
		(if (null? deck)
			'()
			(let ((card (nth (random (length deck)) deck)))
				(cons card (shuffle (remove card deck))) ))) 

A `deck` object responds to two messages: `deal` and `empty?`. It responds to `deal` by returning the top card of the deck, after removing that card from the deck; if the deck is empty, it responds to `deal` by returning `()`. It responds to `empty?` by returning `#t` or `#f`, according to whether all cards have been dealt. Write a class definition for `deck`. When instantiated, a `deck` object should contain a shuffled deck of 52 cards.

## Exercise 6
  
We want to promote politeness among our objects. Write a class `miss-manners`
that takes an object as its instantiation argument. The new `miss-manners`
object should accept only one message, namely `please`. The arguments to the
`please` message should be, first, a message understood by the original
object, and second, an argument to that message. **(Assume that all messages
to the original object require exactly one additional argument.)**

Here is an example using the person class from the upcoming adventure game project:
    
    
    > (define BH (instantiate person 'Brian BH-office))
    BH
    > (ask BH 'go 'down)
    BRIAN MOVED FROM BH-OFFICE TO SODA
    > (define fussy-BH (instantiate miss-manners BH))
    > (ask fussy-BH 'go 'east)
    ERROR: NO METHOD GO
    > (ask fussy-BH 'please 'go 'east)
    BRIAN MOVED FROM SODA TO PSL

## Extra for Experts

Do these if you want an extra challenge. These are *not* for credit.

### Exercise 7
  
The technique of multiple inheritance is described on pages 9 and 10 of ["Object-Oriented Programming - Above-the-line view"](http://www-inst.eecs.berkeley.edu/~cs61as/reader/aboveline.pdf). That section discusses the problem of resolving ambiguous patterns of inheritance, and mentions in particular that it might be better to choose a method inherited directly from a second-choice parent over one inherited from a first-choice grandparent.

Devise an example of such a situation. Describe the inheritance hierarchy of your example, listing the methods that each class provides. Also describe why it would be more appropriate in this example for an object to inherit a given method from its second-choice parent rather than its first-choice grandparent.

## Submit Your Homework!

For instructions, see [this guide](../submit.html). It covers basic terminal commands and assignment submission.

If you have any trouble submitting, do not hesitate to ask a TA!
