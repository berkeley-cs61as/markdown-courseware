For all problems that involve writing queries or rules, test your solutions.

To run the query system and load in the sample data:

	> (load "~cs61as/lib/query.scm")
	> (initialize-data-base microshaft-data-base)
	> (query-driver-loop) 

You are now in the query system's interpreter.

To add an assertion:

	(assert! (foo bar))

To add a rule:

	(assert! (rule (foo) (bar)))

Anything else is a query.

## Exercise 1
  
Abelson & Sussman, exercises [4.56](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-29.html#%_thm_4.56), [4.57, 4.58](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-29.html#%_thm_4.57) and [4.65](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-29.html#%_thm_4.65).

## Exercise 2: Extra for Experts

**Do this if you want to. This is NOT for credit.**
  
Earlier in the section, we describe rules that allow inference of the reverse
relation in one direction, i.e.,

	;;; Query input:
	 (forward-reverse (a b c) ?what) 

	;;; Query results:
	 (FORWARD-REVERSE (A B C) (C B A)) 

	;;; Query input:
	 (forward-reverse ?what (a b c)) 

	;;; Query results:
	 ... infinite loop

or

	;;; Query input:
	 (backward-reverse ?what (a b c)) 

	;;; Query results:
	 (BACKWARD-REVERSE (C B A) (A B C)) 

	;;; Query input:
	 (backward-reverse (a b c) ?what) 

	;;; Query results:
	 ... infinite loop 

Define rules that allow inference of the reverse relation in both directions,
to produce the following dialog: 

	;;; Query input:
	 (reverse ?what (a b c)) 

	;;; Query results:
	 (REVERSE (C B A) (A B C)) 

	;;; Query input:
	 (reverse (a b c) ?what) 

	;;; Query results:
	 (REVERSE (A B C) (C B A))

## Submit Your Homework!

For instructions, see [this guide](../submit.html). It covers basic terminal commands and assignment submission.

If you have any trouble submitting, do not hesitate to ask a TA!
