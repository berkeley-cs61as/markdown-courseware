## Review on Conditionals

We have used [if](https://edge.edx.org/courses/uc-berkeley/cs61as-1x/SICP/wiki
/cs61as-1x/if/) and [conditional](https://edge.edx.org/courses/uc-berkeley
/cs61as-1x/SICP/wiki/cs61as-1x/cond/) in our first lab and in this section
will flesh out more details in this section.

We generally use an 'if' or a 'cond' when we want our function to behave
differently depending on a certain condition. Note that these 2 functions are
one of the few special forms in Scheme; we don't evaluate them with 'evaluate
operator and operand' method.

## Cond Examples

The general form of a cond expression is as follows

`(cond  (<test1> <result1>)`

` (<test2> <result2>)`

` ...`

` (<testn> <resultn>)`

` (else <default>))  ;; The 'else' case is optional`

The pair of expression (<test1> <result1>) is called a clause. The first part
of each pair (the <test>) is a predicate, or an expression that has to
evaluate to true or false.

How you evaluate a 'cond' is as follows:

Evalute <test1>, if it is true, evaluate <result1> and return it. If <test1>
is false, evaluate the next <test>. If it is true, evaluate and return its
corresponding <result>. If it is false, check the next <test> and so on until
you go through all the test. If you hit an else, you return the value
correspoding to it (consider it as the 'default value')

You can write a cond as a series of 'if' statements:

`(if <test1> `

` <result 1>`

`(if <test 2>`

` <result 2>`

` ...`

` (if <testn>`

` <resultn>`

` <default value>)  ;; Close parentheses omitted`

Test your work by copying and pasting your function here and trying it out:

## Predicate and Style

A predicate is any expression that returns true or false. Some examples
include `(< 3 4)`,` (> 10 -2)`, `(= 'apple 'orange)`. You can form compound
predicates by using ` and, or, not. `

Here is an example of a predicate:

`(define (even? x) (= (remainder x 2) 0))`

The convention in scheme when defining your own predicate is to end the name
with '?'.

Notice that the following code is equivalent:

`(define (even? x) (if (= (remainder x 2) 0)`

` #t`

` #f))`

The second code however, is considered to be a 'bad programming style' because
of its redundancy. We urge you to avoid codes like this because verytime you
do, a penguin will cry.

![](http://farm3.static.flickr.com/2600/3829466121_0e5c9b6cca.jpg)

Test your work by copying and pasting your function here and trying it out

