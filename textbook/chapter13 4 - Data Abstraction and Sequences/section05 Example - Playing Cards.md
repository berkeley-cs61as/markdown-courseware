How cool would it be if we could represent a card game using abstract data types? Let's create a more complex interface than rational numbers that will allow us to represent cards, hands, and decks. With these abstractions, we will be able to play some simple card games!

## Creating the Card

When you look at any card, the two properties that identify it as a playing card are its rank and its suit. Sure, you can observe other properties, such as it's rectangular shape or its plastic-y surface, but those aren't the important qualities that you can use to identify the card. Thus, here we have our `make-card` constructor, which takes in a `rank` and a `suit`:

    (define (make-card rank suit)
      (cons rank (first suit)))

And here are its selectors:

	(define (rank card)
	  (car card))

	(define (suit card)
	  (cdr card))

And so we can create a card and extract its properties with the following calls:

	-> (define c (make-card 13 'heart))
	card
	-> (rank c)
	13
	-> (suit c)
	h

We've just created the king of hearts card.

## Creating a Hand

Just like how a hand of cards is a collection of cards in real life, in our abstraction, a hand will be a **list** of cards. We've defined the constructor and selectors below:

	(define make-hand list) ;; constructor creates a list of cards

	(define first-card car) ;; returns the first card in hand

	(define rest-hand cdr) ;; returns the rest of the hand

	(define empty-hand? null?) ;; checks if you have no cards in your hand

Notice how we defined `make-hand` as a **variable** assigned to the procedure `list`. This is because we don't want to specify how many arguments `make-hand` should take in - we can create a hand of any length. All we want `make-hand` to do is take in an arbitrary number of cards and store them into a list. Here are some example calls to our ADT:

	-> (define my-hand (make-hand (make-card 1 'heart)
							   (make-card 5 'diamond)
							   (make-card 10 'diamond)
							   (make-card 13 'club)))
	my-hand
	-> (first-card my-hand)
	(1 . h)
	-> (rest-hand my-hand)
	((5 . d) (10 . d) (13 . c))

## Using our Implementation

That's all we'll need to represent cards! You have cards, and you have a collection of cards. Everything else can be defined in terms these two objects. For example, a deck is just a hand with a card for every combination of rank and suit (plus two jokers, but we'll omit that for now). 

Now it's time to write some procedures with our implementation. For most card games, the rank of the cards represent its _value_. Let's write a procedure that finds the total value of your hand. `total` takes in a hand and returns the sum of all the values of your cards.

	(define (total hand)
		(if (empty-hand? hand)
			0
			(+ (rank (first-card hand)) (total (rest-hand hand)))))

Here's an example:

	-> (total my-hand)
	29

## Changing the Implementation

What would happen if we changed the way we represented cards? Would our code for `total` still work?

The answer is yes, `total` will work because there is a layer of _abstraction_ that separates it from the way cards or hands are implemented. As long as we keep the same names for our constructors and selectors, all the procedures we built off of it will continue to work. Let's say we changed the way we represent cards to this:

	(define (make-card rank suit)
	  (cond ((equal? suit ’heart) rank)
	        ((equal? suit ’spade) (+ rank 13))
	        ((equal? suit ’diamond) (+ rank 26))
	        ((equal? suit ’club) (+ rank 39))
	        (else (error "say what?")) ))

	(define (rank card)
	  (remainder card 13))

	(define (suit card)
	  (nth (quotient card 13) ’(heart spade diamond club)))

Our `total` procedure will still work with this implementation too. Try it out on the Racket interpreter!

With this style of programming, we can create even bigger programs.