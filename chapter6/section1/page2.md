## Basics

The Big Idea: You can ask Scheme questions, called _expressions_. You get back
answers, called _values_. More on this in the coming subsection.

When you want Scheme to _do_ something (e.g. add two numbers together), use
prefix notation--put the operator is at the beginning of the expression,
followed by arguments. For example:

    
    (+ 3 4)

This regular-looking syntax allows us to nest expressions:

    
    (* (max 2 3) (/ 8 4))

Try playing around with some expressions in the [Scheme
interpreter](http://inst.eecs.berkeley.edu/~cs61AS/sp13/js-scheme-
stk/index.html)

