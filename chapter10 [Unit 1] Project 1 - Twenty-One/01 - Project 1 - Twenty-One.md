## Project 1: Twenty-One

We expect that this project will take about a week to complete. It is due by
the Unit 1 deadline. You may not work on this project with another student,
but feel free to ask the staff for help.

For our purposes, the rules of twenty-one ("blackjack") are as follows. There
are two players: the "customer" and the "dealer". The object of the game is to
be dealt a set of cards that comes as close to 21 as possible without going
over 21 ("busting"). Each player is dealt two cards, and one of the dealer's
cards is left face up. First, the customer has to decide whether to take
another card ("hit") or finish playing ("stand"). The customer keeps taking
cards until s/he decides to stand. Then the dealer takes over. In our
simulation, the dealer always hits if his total is 16 or less, and stands with
17 or more. Once the dealer stands, the player with the higher total wins. If
either player's total goes over 21, that player automatically loses. (Note
that if the customer's total goes over 21, the dealer doesn't play at all.)

A card is represented as a word, such as `10s` for the ten of spades. (Ace,
jack, queen, and king are `a`, `j`, `q`, and `k`.) The picture cards (jack,
queen, and king) are each worth 10 points; an ace is worth either 1 or 11 at
the player's option. We reshuffle the deck after each game, so strategies
based on remembering which cards were dealt earlier are not possible.

The customer's strategy of when to take another card is represented as a
procedure. The procedure takes two arguments:

  1. The customer's hand so far, represented as a sentence in which each word is a card
  2. The dealer's card that is face up, represented as a single word (not a sentence)

The strategy procedure should return a true or false output indicating whether
or not the customer wants another card.

**This is so important we'll repeat it again:  All strategies have the same domain and range.  The domain of a strategy is a sentence of cards (the customer's hand) and a single card (the dealer's face up card).  The range of a strategy is a boolean (true or false).**

Start by getting the starter files. You can do this by typing (from a lab
computer)

`cp -r ~cs61as/lib/proj1 .`

(The -r option tells the cp command that it is copying an entire folder
instead of a single file.)

To get it on your laptop, if you use Mac OS or Unix:

scp -r cs61as-xx@cory.eecs.berkeley.edu:~cs61as/lib/proj1 .

On Windows,  you can use WinSCP to copy over the files.

Alternatively (for any operating system) you can download it from
[here](http://inst.eecs.berkeley.edu/~cs61as/library/proj1).

There are two starter files - twenty-one.scm and grader.scm.  The twenty-
one.scm file contains a definition of the procedure `twenty-one`. After you
define a procedure representing the customer's strategy, you will call
`(twenty-one strategy) ` to play a game of twenty-one using a randomly
shuffled deck of cards. `twenty-one` returns 1, 0, or −1 according to whether
the customer won, tied, or lost.

The grader.scm file contains tests to check that your code is correct.  You
can run the tests by typing (load "grader.scm") in STk.  **These tests are not
comprehensive - it is _very_ easy to write incorrect code that will pass the
few tests we have given you.  You _must_ write more tests to make sure your
code is correct.** Since testing is an integral part of writing code, a small
portion of your grade will be determined by the quality of your tests.

## best-total

The program in twenty-one.scm is incomplete. It lacks a procedure `best-total`
that takes a hand (a sentence of card words) as argument, and returns the
total number of points in the hand. It's called _best_-total because if a hand
contains aces, it may have several different totals. The procedure should
return the largest possible total that's less than or equal to 21.  If no such
total is possible, then it must return some number larger than 21. For
example:

    
    > (best-total '(2c 6d 3s 8h)) ; 2 + 6 + 3 + 8 = 19  
    19  
    > (best-total '(ad 8s)) ; in this hand the ace counts as 11
    19
    > (best-total '(ad 8s 5h)) ; here it must count as 1 to avoid busting
    14
    > (best-total '(ad as 9h)) ; here one counts as 11 and the other as 1
    21
    > (best-total '(ad 8s 8c 5h)) ; no matter how we count it, this total is over 21
    22
    

Write `best-total` as part of twenty-one.scm. You can run some simple tests by
executing (load "grader.scm") in STk. Test it thoroughly by adding more tests
to grader.scm. Don't rely on the examples given above. Instead, try to think
of cases where your procedure might do the wrong thing, and test it on those
cases. You can avoid losing points for an incorrect procedure by demonstrating
that you know exactly what it's doing wrong.

You can add a test by making a call to the run-test procedure.  This procedure
takes in 4 arguments.  The first two arguments are the test number and the
procedure being tested.  The next two arguments are code you want to test and
the value it should produce.

For example:

    
    (run-test 1 "best-total"               ;; Test 1 for best-total
              (best-total '(2c 6d 3s 8h))  ;; Code to run for test 1
              19)                          ;; Expected output

The above code creates the first test for best-total, which says that calling
best-total on the sentence '(2c 6d 3s 8h) should give 19.

## stop-at-17

Time to define your first strategy procedure, `stop-at-17`. This will be just
like the dealer's strategy: take another card if and only if your current
total is strictly less than 17.  (So, if the current total is exactly 17, you
do **not** take another card.)

Remember: The domain of a strategy is a sentence of cards (the customer's
hand) and a single card (the dealer's face up card).  The range of a strategy
is a boolean (true or false).

Put your definition of `stop-at-17` in twenty-one.scm, and add tests for it in
grader.scm.  Note that you will have to uncomment the line

;; (test-stop-at-17)

in grader.scm to run the tests for stop-at-17.

At this point, you have everything you need to play a game of twenty-one.

## play-n

Write a procedure `play-n` such that `(play-n strategy n)` plays `n` games
with the given strategy and returns the number of games that the customer won
minus the number that s/he lost. Try this on your strategy from the previous
problem, as well as strategies from the problems that follow.

Put your definition of `play-n` in twenty-one.scm. Don't forget: a "strategy"
is a procedure! We're asking you to write a procedure that takes another
procedure as an argument.

## dealer-sensitive

Define a strategy named `dealer-sensitive` that hits (takes a card) if and
only if

  * the dealer has an ace, 7, 8, 9, 10, or picture card showing, and the customer's total is less than 17

_or_

  * the dealer has a 2, 3, 4, 5, or 6 showing, and the customer's total is less than 12.

The idea is that in the second case, the dealer is much more likely to "bust"
(go over 21), since there are more 10-point cards than anything else.

As before, you should put your definition in twenty-one.scm, and add more
tests to grader.scm.

## stop-at

Generalize the idea behind `stop-at-17` by writing a higher-order procedure
called `stop-at`. `(stop-at n)` should return a strategy that keeps hitting
until the customer's total is at least `n`. For example, `(stop-at 17)` should
return a strategy just like `stop-at-17`. As always, we want you to show a
reasonable amount of testing in grader.scm.

Before you start writing code, take a moment to think about the domain and
range of stop-at.

## valentine

On Valentine's Day, your local casino has a special deal: If you win a round
of twenty-one with a heart in your hand, they pay double. You decide that if
you have a heart in your hand, you should play more aggressively than usual.
Write a `valentine` strategy that stops at 17 unless you have a heart in your
hand, in which case it stops at 19.

## suit-strategy

Generalize the previous problem by defining a procedure `suit-strategy` that
takes three arguments:

  1. A suit (`h`, `s`, `d`, or `c`)
  2. A strategy to be used if your hand doesn't include that suit
  3. A strategy to be used if your hand _does_ include that suit

It should return a strategy that behaves accordingly.

Note the order of the arguments - the first of the two strategies is the one
to be used if the hand does _not_ include the suit.

Define a strategy valentine2 that does the same thing as the valentine
strategy from the previous problem; this time you should use the suit-strategy
procedure and the `stop-at` procedure instead of defining it from scratch.

## majority

Define a procedure `majority` that takes three strategies as arguments and
returns a new strategy as a result. The returned strategy should decide
whether or not to hit by consulting the three argument strategies and going
with the majority. That is, the result strategy should return `#t` if and only
if at least two of the three argument strategies do. Test your procedure in
grader.scm by constructing "majority strategies" out of the strategies you
defined in previous problems.

## reckless

Some people just can't resist taking one more card. Write a procedure
`reckless` that takes a strategy as its argument and returns another strategy.
This new strategy should take one more card than the original would. (In other
words, the new strategy should stand if the old strategy would stand given the
`butlast` of the customer's hand.)

## Jokers

Once you have completed all the previous problems, make a copy of your
modified twenty-one.scm file called joker.scm.

We are going to change the rules of twenty-one by adding two jokers to the
deck. A joker can be worth any number of points from 1 to 11. Modify whatever
has to be modified to make this work. (The main point of this exercise is
precisely for you to figure out which procedures must be modified.) **You may
have to modify the code we provided as well, since it does not correctly deal
with jokers.** You will submit both joker.scm and twenty-one.scm for grading.
Don't worry about making strategies optimal; just be sure nothing blows up and
the hands are totalled correctly. You should add a reasonable number of tests
to grader.scm for any procedures that you modify.  Make sure you add these
tests _after_ the (load "grader.scm").

## Project 1 Submission

You should submit three files for this project:

  1. Your modified version of twenty-one.scm
  2. joker.scm
  3. Your modified version of grader.scm with additional tests for your procedures

Put all three files in the same folder, so that you can submit all of them
together. When you are ready to submit, navigate to that folder and type
`submit proj1`. If you need to resubmit one of the files, you should resubmit
all of them together.

