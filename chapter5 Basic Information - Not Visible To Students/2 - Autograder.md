## Autograder

Autograders are great. We highly recommend that you use them and get familiar
with them.

In order to run the autograder, type `grader [hw#] [hwfile.scm] ` into the
terminal. Running this will load your code into stk and run tests that check
the accuracy of your responses. You should receive a result almost immediately
that tells you how many tests you passed.

## Templates

In order to run the autograder properly we often must load other code into
stk. In order to make sure everything is loaded properly, we have provided
templates for the homeworks that you can basically fill out and run against
the autograder.

To acquire these templates, you can run `cp
~cs61as/autograder/templates/hw[#].scm .`

## An Example

    
    star [504] ~/hw1 # grader hw1 hw1.scm
    
    Test failed:
    Test code: (dupls-removed (quote (a b c a e d e b)))
    Expected output - some permutation of: (c a d e b)
    Your output: error
    .......................etc..........................
    

